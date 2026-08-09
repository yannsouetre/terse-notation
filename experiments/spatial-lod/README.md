# Spatial context & semantic LOD — exploratory annex

*Second companion experiment to TERSE. Status: exploratory prototype — doc-level addresses,
6 tasks, one run per model family. It does not modify TERSE v1 claims.*

## Question

TERSE v1 condenses a document. This annex organizes a **space of condensed objects**: every
document gets an address (`&t01`…`&t23`) and exists at three levels of detail — **L0** (one
map line: address, `!!` flag, gist), **L1** (the TERSE operational core), **L2** (full prose).
An agent's context becomes **MAP (always) + FOCUS (L1 of the task's documents)**. The design
borrows 3D-engine vocabulary as translated mechanisms only (LOD, frustum→FOCUS,
occlusion→supersession); geometry is always derived, never authored. Full design:
`TERSE-SPATIAL-DRAFT.md` (address grammar A1-A3, integrity rules R1-R4).

The flagship claim, pre-registered before any run:

> **The MAP converts unknown-unknowns into known-unknowns.** An agent that lacks a detail no
> longer hallucinates or goes silent — it answers "exists at `&addr`, not loaded" and requests
> the fetch.

## Protocol (FocusBench v0.1)

23-document corpus in MAP+L1+L2 form (MAP v1: 2,648 chars for the whole base; the shipped v3 map: 4,522). 6 tasks; each
loads the MAP plus the full L1 of its 3 focus documents (condition **C · TERSE-LOD**).
Conditions **A · prose** and **B · short** receive the **same character budget**, matched per
task and per map version (v1 8.7–11.4k chars, v2 9.8–12.5k, v3 10.6–13.3k), filled from the
start of the corpus and truncated — the baselines' budget grows with the map, so they are
never penalised by its enrichment. Per task: 2
in-focus questions, 2 out-of-focus questions (about unloaded regions). Out-of-focus answers
are judge-classified: CORRECT / **AWARE** (states the information is not loaded AND names the
source address, or requests its fetch) / HONEST-blind (states absence without locating) /
HALLUCINATION. Stateless API calls; ~144 requests per run.

**Pre-registered predictions:** P1 — C ≈ full-context accuracy in focus; P2 — C reaches ≥80%
AWARE out of focus while A/B sit at ~0% (structurally: what exists beyond their cut was never
in their window); P3 — a deterministic linter detects ≥95% of injected LOD-integrity
violations with <5% false alarms.

## Results — a three-map ablation (unplanned, and the best part)

The first run passed P2 but exposed a failure mode; fixing it produced a trade-off; the
hybrid fix resolved it. Three map-line designs, identical tasks/questions/judges, both
families (out-of-focus classes over 12 questions per cell; "helpful" = CORRECT + AWARE):

| Map version (line content) | In-focus | Helpful out-of-focus | HALLUC. |
|---|---|---|---|
| **v1** — title + first L1 line (topical) | 11-12/12 | S 11/12 · G 10/12 (**AWARE 92%/83%**) | 0 / 1* |
| **v2** — title + top hard rule + counts | **12/12 both** | 9/12 both (75%) | 1 / 1 |
| **v3** — hybrid: topical gist + top rule + counts | **12/12 both** | 10/12 both (83%) | **0** / 1* |

Truncated baselines (all versions): in-focus 3-6/12, AWARE 0/12 — structurally blind to what
lies beyond their cut (~75% honest "not in context", no location).

**Verdicts on the pre-registered predictions.** P1 met (12/12 both families from map v2 on;
11-12/12 at v1). P2 passed at v1 (92%/83% AWARE) and recovered at v3 (83% helpful) after the
v2 dip. P3 passed deterministically — with its own postmortem (below): `lod-lint.py
--self-test` reproducibly detects **56/56** injected corruptions across all four rules (seven
types: orphan detail, dangling map entry, de-elevated `!!`, phantom `!!`, dangling reference,
corrupted quoted value, missing supersession pointer), **0 false alarms** on the clean corpus,
zero model calls. The R1 pass also forced a semantic decision worth recording: two quoted
identifiers cited at L1 live in their documents' *titles* but not in the L2 body. Ruling
(now in the linter's contract): the document header travels with every level, so R1's
verification haystack is title + body — a value inherited from the title is faithful, not
drifted. (R4's evidence is an injection self-check with a discrimination counter-test; the
corpus contains no real supersessions yet — stated as such.)

**Instrument postmortem #2 (P3).** The originally reported "40/40" was measured on map v1 —
whose lines did not contain the literal `top!!:`. The v3 hybrid line introduced that literal
in every gist, and the linter's elevation check was a *substring* test (`"!!" in line`):
de-elevated flags became structurally undetectable (0/8), silently voiding one rule of five.
The pre-publication audit (second Claude instance, injection rerun) caught it; the check is
now anchored on the leading elevation flag, the self-test ships *inside* the linter
(`--self-test`, so the claim is reproducible rather than quoted), and the numbers above are
the re-measured ones. Same lesson as the reasoning annex: **the instrument changed under the
claim — re-measure after every instrument change.**

**The map-design lesson (what the ablation actually measured):** the L0 line is a design
variable with two independent jobs. *Topical* content routes out-of-focus questions to the
right address (v1's strength — removing it in v2 cost 3 routing hits); *rule-signature*
content pins twin documents apart and sharpens in-focus use (v2's strength — the
ransomware-vs-cloud-DR pointer error of v1 never recurred). The hybrid line does both, at
4.5k chars for a 23-document base. Bonus observed at v3: one question became answerable from
the map line itself (the agent's name sat in the gist) — maps are not only routers.

**Residual failures, named and disclosed:** (a) two questions phrased far from any gist
vocabulary ("orders pending Wednesday morning" vs a delivery-delays gist) still route
nowhere — gist wording bounds routing recall; (b) GPT-5.5 once pointed to a document whose
*generic title* ("PROCEDURE / RUNBOOK") attracts runbook-shaped questions — title quality is
part of map quality; (c) one out-of-focus question was genuinely ambiguous between two
similar documents (two AI-agent scoping notes, one loaded), producing the single v2
hallucination in both families — disclosed rather than repaired post-hoc; the v3 map answers
it correctly. Sub-document addressing (`CONVERT-LOD-PROMPT.md`, linter-ready) is the designed
next step for (a) and (b).

## Caveats

n=12 per cell per map version, one run per (family × map), doc-level addresses only,
mechanically generated L0 gists, judge-based grading on out-of-focus classes; the map
ablation was reactive (v2 and v3 designed after seeing failures — stated plainly). A prototype's evidence,
claimed as such.

## Replicate

The shipped `terse-focusbench.html` embeds map v3; results for all three map versions are in
`results/` with the map version in the filename. Open it locally (file://), pick a provider and key, "Test the endpoint",
Run (~144 calls). The LOD corpus (`LOD-CORPUS-EN.json`), tasks, budgets, judge prompts and
the linter (`lod-lint.py`, self-test included) are all in this folder.

## Roadmap

Sub-document addressing via `CONVERT-LOD-PROMPT.md` (regions `&t03/rerun`, cross-references
that build the topology); FOCUS by graph radius over those references; gist/title quality as
a measured variable; more tasks and repeated runs; LOD over reasoning traces (bridge to the
reasoning annex: reload only the `!` skeleton).
