# Spatial context & semantic LOD — exploratory annex

*Second companion experiment to TERSE. Status: exploratory prototype in two waves — wave 1:
doc-level addresses, a three-map ablation over 6 tasks; wave 2: sub-document addressing
(148 regions), the fetch loop measured end to end at three granularities over 24 questions,
and a cross-document linking pass. One run per (family × configuration). It does not modify
TERSE v1 claims.*

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

## Wave 2 — executing the contract (sub-addressing, the fetch loop, the graph)

The first wave *gave* models a focus; this wave has them **earn** it. All artifacts below are
in this folder; raw results in `results/`.

**Sub-addressed corpus.** `CONVERT-LOD-PROMPT.md` applied to all 23 documents by Sonnet
(`terse-convert-runner.html`, one isolated call per document) yields 148 regions (mean 6.4/doc,
102 carrying hard constraints), a 171-line region map (16.4k chars — 3.6× the doc-level map,
5.0× under the full L1 corpus, 82,397 chars), 284 intra-document references with **zero dangling** and a
perfect map↔block bijection. Converter compliance is itself a finding: 43/102 hard regions
arrived un-elevated despite a mandatory prompt rule — `lod-lint.py` repaired them mechanically
(elevation is derivable), repairs counted in the corpus file. The R1 value check flagged 40
quoted values: 25 benign reformattings and 15 format conversions (mostly 24h↔AM/PM) —
semantically right, contractually non-verbatim; the prompt gains "copy formats exactly as
printed" in its next revision. Corpus: `LOD-CORPUS-SUB-EN.json` (normalization and R1
classification embedded).

**FetchBench — the loop, end to end** (`terse-fetchbench.html`; 24 questions; call 1 sees only
a map and replies with fetch addresses, the harness loads them, call 2 answers; routing hit is
deterministic, answers are judged; per-question input tokens recorded):

| Condition | Routing | Correct | Hard cohort routed | Avg input tk/Q |
|---|---|---|---|---|
| B · doc-fetch — Sonnet / GPT-5.5 | 20/24 · 22/24 | 19 · 22 | 10/12 · 12/12 | 3,997 · 3,168 |
| C · region-fetch — Sonnet / GPT-5.5 | 22/24 · 22/24 | 21 · 21 | **12/12 · 12/12** | 10,228 · 8,431 |
| D · two-stage — Sonnet / GPT-5.5 | 19/24 · 22/24 | 17 · 21 | 10/12 · 12/12 | 2,811 · **2,228** |

Three findings. (1) **Fine gists route what coarse gists cannot**: the two questions that
resisted every doc-level map (F3/F4) resolve at region granularity in both families — the hard
cohort routes 12/12. (2) **Granularity buys reliability, not economy, at this corpus scale**:
the region map rides every call (16.4k chars ×2), while whole documents (~2.5k) are already
cheap to fetch — region-fetch costs 2.6× more. (3) **Two-stage fetch (doc map → elected
document's region map) is only as strong as its weakest stage**: with a reliable stage-1
router it is the best configuration measured (GPT-5.5: region-grade routing at the lowest cost,
2,228 tk/Q, and the region-only miss F2-t03 repaired exactly as predicted — region lines
scored outside their document's context can mislead, stage 1 restores that context); with a
weaker stage-1 router the errors compound (Sonnet degrades to 19/24; its best configuration
remains flat region-fetch). Routing is the bottleneck throughout: a routing hit almost always
becomes a correct answer. Named residuals: one question that presupposes its document (a v1 QA
item reused in a routing setting — question design, not map design), the twin-runbook
generic-title attractor (t16/t20), and right-doc-wrong-region misses that a single-shot loop
cannot recover — an iterative fetch (the model may ask again) is the designed next step.

**The graph's missing dimension, honestly.** A linking pass (`terse-linkpass.html`, one call
over the global region map, strict lintable edge format) proposed 33 edges: 31 intra-document
(off-contract; that structure already existed) and **2 cross-document** — both between the two
security incidents (t15↔t08), both resolving, merged into the corpus with provenance and
visibly analogical rather than operational ("mirrors", "aligns with"). The honest reading: this
corpus is an **archipelago** — 23 independent fictional organizations with almost no real
cross-document dependencies to find, so the model rightly found almost none. Graph-radius FOCUS
across documents therefore remains structurally untestable here; it awaits a corpus from a
single organization, where escalation paths and shared systems actually cross documents.

## Caveats

n=12 per cell per map version and n=24 per FetchBench cell, one run per (family ×
configuration); mechanically generated doc-level gists, model-generated region structure
(one converter, one run); judge-based answer grading; the map ablation and the two-stage
design were reactive (built after seeing failures — stated plainly). A prototype's evidence,
claimed as such.

## Replicate

Every measurement in this annex reruns from this folder, locally (file://), with your own
key: `terse-focusbench.html` (embeds map v3; the mapv1/v2/v3 results in `results/` carry the
map version in the filename; ~144 calls), `terse-fetchbench.html` (conditions B/C/D — doc,
region, two-stage; 3-4 calls per question), `terse-convert-runner.html` (rebuilds the
sub-addressed corpus from the prompt in `CONVERT-LOD-PROMPT.md`, 23 calls),
`terse-linkpass.html` (1 call), and `python3 lod-lint.py --self-test` (deterministic, free).
The corpora (`LOD-CORPUS-EN.json` doc-level, `LOD-CORPUS-SUB-EN.json` sub-addressed with
normalization and provenance), tasks, budgets and judge prompts are all embedded or in this
folder.

## Roadmap

Iterative fetch (let the model ask again on a right-doc-wrong-region miss); a single-organization
corpus where cross-document dependencies actually exist, unlocking graph-radius FOCUS;
gist/title quality as a measured variable; questions authored for routing (not reused QA);
repeated runs; LOD over reasoning traces (bridge to the reasoning annex: reload only the `!`
skeleton). One outward-facing note: the stateless MCP spec (2026-07-28) makes `tools/list`
results cacheable and deterministically ordered — a tool catalog is a MAP problem (one L0 line
per tool, `!!` on destructive/approval-gated, selection = routing), and the finding "routing
is the bottleneck" should transfer; a ToolBench measuring tool-selection accuracy under
condensed vs raw catalogs at matched budgets is a natural follow-up.
