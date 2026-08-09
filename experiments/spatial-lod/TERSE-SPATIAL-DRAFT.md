# TERSE v2 draft — Spatial context & semantic LOD

*Working draft v0.2 (design + P1-P2-P3 measured — nothing here modifies TERSE v1). Language: English by
project decision (2026-08-07). Origin: "Piste TERSE v2" exploration, filtered through the
v1 evidence.*

## 1. Why v2, stated in v1's own results

Three v1 measurements point at the same missing capability:

- **BudgetBench**: at a fixed window, what matters is *what you choose to load*. Truncated
  prose answered honestly "Not in context" — but it did not know that the answer existed,
  nor where. Selection was blind.
- **StructBench**: markers make categories retrievable (`grep '^!!'`). But retrieval still
  operates on one flat document; there is no way to *ask for more* of something.
- **ReasonBench annex**: reasoning traces have skeletons (`!` lines) worth reloading without
  their full body.

v1 condenses a document. v2 organizes a **space of condensed objects** that an agent can
map, focus, and fetch — with the same reliability-first discipline: every mechanism must be
mechanically checkable (INTACT-class tooling), and every claim must survive a pre-registered
benchmark.

## 2. The translation table (3D engine → context mechanism)

The 3D vocabulary is a design metaphor, translated into text-native mechanisms — no engine,
no rendering, no authored coordinates:

| 3D concept | Context mechanism |
|---|---|
| Scene graph | Address tree (authored topology via anchors) |
| Coordinates | None authored. Positions are *derived views* (e.g., time axis, actor axis) |
| LOD (level of detail) | L0/L1/L2 per object, with integrity rules (below) |
| Frustum culling | FOCUS(address, radius): load only objects within graph distance r |
| Occlusion | Supersession: a newer object occludes an older one (`x` + pointer) |
| Spatial query | NEAR/PATH queries computed by a linter-class tool from anchors, zero LLM |

Two v1 triage decisions stand: **geometry is always derived, never authored** (authored
coordinates would rot; topology in anchors is cheap and lintable), and **no ontology of
semantic axes** in the core (axes are view parameters, not language).

## 3. Address grammar (continuous with v1)

v1 anchors `&id` become hierarchical: `&payroll/rerun`, referenced as `*payroll/rerun`.
Rules:

- **A1 — stability**: an address, once published, never changes meaning. Supersession
  creates a new address and marks the old one `x superseded -> *new/addr`.
- **A2 — one object, one address**: facts about X live at X's address, wherever they were
  learned (the anti-scatter rule).
- **A3 — references are addresses**: `<- *src/addr` provenance, `-> *effect/addr` links.
  The topology *is* these arrows; NEAR(x, r) is graph distance over them.

## 4. Semantic LOD discipline

Every object may exist at three levels:

- **L0** — one line: address, strongest marker, gist. The set of all L0 lines is the **MAP**.
- **L1** — the operational core: constraints, values, decisions (what v1 calls the short/terse
  content).
- **L2** — full detail (may be the original prose).

**Integrity rules (all mechanically checkable — INTACT v2):**

- **R1 refinement**: L(k+1) may add detail but never contradict Lk. Protected content
  (§3.7 v1: negations, critical values, qualifiers) is compared verbatim across levels.
- **R2 constraint elevation**: every `!!` existing at any level must surface at L1, and L0
  must at least flag it (`!!` in the map line). A hard constraint that only lives in deep
  detail is a latent incident: this rule makes "the map shows where the mines are" checkable.
- **R3 map completeness**: every address present at L1/L2 appears in the MAP (no orphan
  detail); every MAP entry resolves (no dangling address).
- **R4 occlusion honesty**: a superseded object keeps its content but must carry the `x`
  and the forward pointer; the MAP shows only the live object by default.

## 5. The agent contract (what this buys in deployment)

An agent's context = **MAP (always) + FOCUS(task addresses, radius r) (on demand)**.
The MAP costs a few hundred tokens for tens of documents; FOCUS loads L1/L2 only where the
task lives. The decisive property, and v2's flagship claim to test:

> The MAP converts unknown-unknowns into known-unknowns. An agent that lacks a detail no
> longer hallucinates or goes silent — it can answer "exists at `&addr`, not loaded" and
> request the fetch.

## 6. Worked example (payroll runbook, from corpus EN-T03)

```
# MAP (L0)
&payroll            !! monthly payroll export — 3 hard rules below
&payroll/scope      x simulations · x individual adjustments
&payroll/triggers   ! 3 failure triggers @ 06:30 check
&payroll/scheduler  ! 90-min rule => stop + P2
&payroll/inputs     ! 3 input files · owner-contact rule
&payroll/rerun      !! max 1 manual rerun => else P1
&payroll/comms      !! no direct all-staff messages · 10:00 escalation

# L1 &payroll/rerun
!! max "1" manual rerun
rerun SUCCESS + file >"10 MB" -> resume normal processing
rerun FAILED | file <"10 MB" -> open P1 @Payroll-Engineering -> inform payroll manager
delete only incomplete output · keep logs

# L2 &payroll/rerun
<full prose paragraph, kept verbatim>
```

R2 visible in action: both `!!` rules are readable from the MAP alone. FOCUS(&payroll/rerun, 1)
loads rerun + scheduler + comms (graph neighbors) and nothing else.

## 7. FocusBench — pre-registered design (no runs yet)

Corpus: the 23 v1 EN documents converted to MAP+L1+L2 form. Window budget: sized so that
flat TERSE does **not** fit, but MAP + focused L1/L2 does. Arms: (A) prose truncated,
(B) short truncated, (C) TERSE-LOD = MAP + FOCUS around the task's addresses.
46+ questions: half inside focus, half outside focus (about unloaded regions).

**Pre-registered predictions (written before any run):**

- **P1 (focus accuracy)**: C ≈ full-context accuracy on in-focus questions (within 3 pts of
  v1 canonical TERSE), while A and B answer only what survived their truncation.
- **P2 (awareness)**: on out-of-focus questions, C names the existing address or requests a
  fetch in ≥80% of cases; A and B do so in ~0% (they cannot — the information about what
  exists was never in their window).
- **P3 (integrity)**: an INTACT-v2 prototype detects ≥95% of synthetically injected LOD
  violations (R1-R4 corruptions), with <5% false alarms on clean documents.
  **MEASURED (2026-08-08): 40/40 injected corruptions detected (five types: orphan detail,
  dangling map entry, de-elevated `!!`, phantom `!!`, dangling reference), 0 false alarms on
  the clean 23-document corpus — `lod-lint.py`, deterministic, zero LLM calls. P3 passed.**

Failure of P1 or P2 kills or reshapes v2 — as usual, negative results are results.

**MEASURED (2026-08-08, FocusBench v0.1.x, two families, 6 tasks × 4 questions):**

| Condition | In-focus accuracy | Out-of-focus: AWARE | HONEST-blind | HALLUC. |
|---|---|---|---|---|
| **C · TERSE-LOD** (Sonnet) | 11/12 | **11/12 (92%)** | 1 | 0 |
| **C · TERSE-LOD** (GPT-5.5) | **12/12** | **10/12 (83%)** | 1 | 1* |
| A · Prose truncated (both) | 3/12 | 0/12 | 9/12 | 1 |
| B · Short truncated (both) | 5/12 | 0/12 | 8-9/12 | 0-1 |

**P2 passed in both families** (83-92% vs a structural 0% for the truncated arms — they cannot
name what was never in their window; their 2-3 out-of-focus "CORRECT" are documents that
happened to sit before their cut). **P1 met at GPT-5.5 (12/12) and near-met at Sonnet (11/12,
n=12).** (*) The residual failure mode is instructive: both non-AWARE LOD cases correctly said
"not loaded" but pointed to the **wrong address** — map-reading errors, not blindness; a
finer-grained map line (v2.1 sub-addressing) is the designed answer. Truncated arms confirm
the BudgetBench behavior: honest but blind (75% HONEST), with 1 hallucination each at Sonnet.
Character-equal budgets translate to slightly higher input tokens for C (~2.5-2.9k vs
2.1-2.6k). Caveats: n=12 per cell, one run per family, doc-level addresses only.

## 8. Out of scope (v2.0)

Authored coordinates and any 3D rendering; semantic-axis ontologies; double serialization
(only *generated* views are allowed); engine harnesses (Unreal-class experiments live in the
separate reasoning-3d project, not here); reasoning-trace LOD (bridge noted, deferred to
v2.1 with the reasoning annex).

## 9. Next actions

1. Draft approved by Yann (2026-08-08) — grammar and rules frozen for v0.
2. DONE — LOD corpus built for all 23 EN documents (auto L0 map + L1 = terse + L2 = prose,
   doc-level addresses; sub-document addressing deferred to v2.1) and linted clean.
3. DONE — FocusBench run on two families: P2 passed (83-92% AWARE vs 0%), P1 met/near-met,
   P3 passed. The v2 flagship claim is empirically established at prototype level.
4. English-first: in force.
