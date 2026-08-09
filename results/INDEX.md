# Results index

Every run of the project, including the ones that were superseded and the ones that failed to meet their criterion. Files in this folder are the raw exports: **nothing has been filtered, re-scored or removed after the fact.** One edit was made, and it is not a scoring edit — a live private URL in corpus document `T12` was replaced by an `example.com` address of identical length and structure, everywhere it appeared, including in these result files. It is the gold answer to 2 questions out of 1,084 — one per language. Nothing else in any export was touched.

Narrative and caveats for each run: [`SPEC.md`](../SPEC.md) §6. Headline figures: [`README.md`](../README.md).

This folder holds the results of the TERSE v1 benchmarks only. The exploratory reasoning annex keeps its own raw exports next to its report, under [`experiments/reasoning/results/`](../experiments/reasoning/results/). The spatial-LOD annex does the same, under [`experiments/spatial-lod/results/`](../experiments/spatial-lod/results/).

---

## Current results

| File | Run | What it establishes |
|---|---|---|
| `canonical-EN.json` | **Run 7 — canonical paired run, EN** | 23 docs × 542 questions × 3 arms, Sonnet 4.6, all questions, one draw shared by the three arms. Prose 97.05% · short −35.0%/95.20% · TERSE −33.2%/94.62%. |
| `canonical-FR.json` | **Run 7 — canonical paired run, FR** | Same protocol. Prose 97.97% · short −41.5%/95.76% · TERSE −41.0%/95.75%. Paired short-vs-TERSE: 6 flips each way. |
| `structbench-GPT.json` | **Run 5 — structural retrieval, cross-family** | 112 audited gold items, 10 extraction queries (11 prompts), GPT-5.6 Sol reader in three isolated conversations. Prose 98.2% · TERSE 96.4% · short 92.9%. Q1: short 3/9, TERSE 9/9. Totals only — see the caveat below. |
| `structbench-sonnet-v0.1.json` | Structural retrieval, first family (`SPEC.md` §6 refers to it inside the Run 5 paragraph as "the Sonnet run"; it carries no run number of its own) | The same benchmark on Sonnet 4.6, automated (structbench v0.1). Produced the Q1 short-collapse (3/9) that Run 5 replicated on a second family. **Partially graded**: 2 prose cells, 3 short cells and 5 terse cells are `"found": null`, including terse's own Q1 — so no per-format total is computable here, and this run supports the Q1 signature only. |
| `budgetbench.json` | **Run 6 — equal-window deployment** | One window of 57,491 characters. Prose truncated 56.5% overall / 5.0% past its cut · short 89.1%/100% · TERSE 87.0%/95%. 46 questions. |

### StructBench supporting material

The cross-family run was executed by hand — three isolated ChatGPT conversations, one per format, with the gold lists never shown to the reader. Everything needed to audit or repeat it:

| File | What it is |
|---|---|
| `structbench-golds-audit.md` | The **pre-audit** draft gold lists (10 queries, 47 items as published here) and the independent-auditor prompt sent to attack them. The audit expanded them to the 112 items used for scoring — that expansion is visible in the per-query `gold` counts of `structbench-sonnet-v0.1.json` (9+12+17+24+17+10+1+10+9+3 = 112), but **the auditor's own output was not kept as a file**, so the expansion itself is not independently auditable. The golds were audited before any arm ran, on purpose. |
| `structbench-protocol-prose.md` `-short.md` `-terse.md` | The exact payload sent to the reader for each format: instructions, the queries, and the full concatenated corpus in that format. One file, one conversation. The payload header says "12 extraction queries" where the file lists 10 (11 prompts, Q4 split by scope); left uncorrected because it is what was actually sent, identically to all three arms. |
| `structbench-GPT-answers-prose.txt` `-short.txt` `-terse.txt` | The reader's verbatim answers, unedited. Grading was done centrally against the audited golds, with contested items arbitrated by hand. |

*Known adjustment, applied uniformly:* the Q9 gold for `EN-T05` was found inconsistent after the run. All three formats had answered it; it is scored 9/9 for all three rather than dropped, which is neutral between arms. Recorded in `structbench-GPT.json`.

---

## Archive — superseded runs

Kept because the trajectory is part of the evidence. These use earlier bench versions, earlier spec versions, and — importantly — **question sub-sampling**, which is exactly what made them unreliable.

| File | Run | Why it is superseded |
|---|---|---|
| `archive/run1-EN-sonnet46.json` | Run 1 (bench v0.6) | First full EN corpus: −33% tokens, −3.0 pts, on 10 sampled questions per document. Its paired failure taxonomy drove the v0.7 fixes (protected precision, judge leniency on over-specific answers). Superseded by Run 7. |
| `archive/run2.1-EN-sonnet46.json` | Run 2, EN (10-question draw) | 23 documents × 10 sampled questions (230 per arm). Token counts came out **identical to Run 1 to the digit** (21,548 / 14,392) — the instrument is deterministic. Accuracy moved 3.5 pts on a different draw, prose included: sampling variance, not signal. This is why publication runs now use all questions. **Not used in the §4 table.** |
| `archive/run2.2-EN…` `run2.3-EN…` | Run 2, EN (20-question draw) | The same corpus at 20 questions per document (460 per arm, 15 + 8 documents). These two are what feed the prose and TERSE rows of the §4 table, together with the FR files. |
| `archive/run2.1-FR-sonnet46.json` | Run 2, FR (main) | 19 documents × 20 sampled questions: −39.2% tokens for −1.6 pts (98.42% → 96.84%) — the only run that met the accuracy half of the pre-registered criterion. On a partial corpus and a sampled draw, so it does not headline. |
| `archive/run2.2-FR-sonnet46.json` | Run 2, FR (tail) | The remaining 4 documents (`FR-T20`–`FR-T23`). Together with the file above it covers all 23; the −39%/−1.6 pts figure belongs to `run2.1-FR` alone. |
| `archive/run3.1-EN-short-llml.txt` | Run 3, EN part 1 | Exported as formatted text rather than JSON (bench v0.10 display export). Kept verbatim. |
| `archive/run3.2-EN-short-llml.json` | Run 3, EN part 2 | The short / LLMLingua / LLMLingua-over-TERSE arms, EN documents 18–23. |
| `archive/run3.3-FR-short-llml.json` `run3.4-FR…` | Run 3, FR | Same arms, FR documents 1–15 and 16–23. |

**The `README.md` §4 table is assembled from two campaigns, not one.** The `run3.*` files contain only the `short`, `llml` and `llmlTerse` arms — there is no prose or TERSE arm in them. Provenance, row by row:

| §4 row | Source files | Recomputes to |
|---|---|---|
| Prose 97.7% | `run2.2-EN` + `run2.3-EN` + `run2.1-FR` + `run2.2-FR` | 899/920 = 97.72% |
| TERSE −38% / 95.3% | same four files | 861/903 = 95.35%, 33,102 tk (17 EN answers ungraded) |
| Short −39% / 96.2% | `run3.1` + `run3.2` + `run3.3` + `run3.4` | 885/920 = 96.20%, 32,565 tk |
| LLMLingua-2 −35% / 91.4% | same four Run 3 files | 841/920 = 91.41%, 34,531 tk |
| LLML over TERSE −52% / 85.4% | same four Run 3 files | 786/920 = 85.43%, 25,508 tk |

The two campaigns share the question draw on 30 of the 46 documents; on the 16 documents carrying 30–32 questions (8 per language) each sampled its own 20, overlapping on 11 to 15 of them. That is the table's weakness, and the reason Run 7 exists. Run 2's prose and TERSE figures are superseded by Run 7; the LLMLingua figures stand, since no later run repeats that arm. Each campaign is split across several files because runs were executed in chunks — the bench resumes across sessions.

Also recorded in `SPEC.md` §6 but with no file here: the **pilot** (bench v0.2, 3 designer-authored documents, Haiku reader, indicative only) and the **v0.5 field finding** (third-party converters applied markers without condensing, producing TERSE at 103% of source size — the finding that reoriented the whole specification around condensation).

---

## Recomputing the headline figures

Nothing here needs to be taken on trust. From the repository root:

```python
import json
d = json.load(open("results/canonical-EN.json", encoding="utf-8"))
for arm in ("prose", "short", "terse"):
    tk = sum(doc["arms"][arm]["tokensNet"] for doc in d["docs"])
    qa = [q for doc in d["docs"] for q in doc["arms"][arm]["qa"] if q["correct"] is not None]
    ok = sum(1 for q in qa if q["correct"])
    print(f"{arm:6s} {tk:6d} tokens   {ok}/{len(qa)} = {100*ok/len(qa):.2f}%")
```

Every `qa` entry carries the question, the gold answer, the model's verbatim candidate answer and the judge's verdict, so any grading decision can be re-examined item by item. Four entries across the two canonical files have `"correct": null` — ungraded by the judge; the README states both denominators.
