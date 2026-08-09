# TERSE — a token-efficient notation for discursive LLM context

*What TOON does for JSON, TERSE does for prose. A draft specification, a bilingual corpus, three benchmarks you can re-run yourself — including the results that missed their pre-registered target.*

**Yann Souetre — August 2026.** Code and tools: MIT. Specification, corpus and results: CC-BY 4.0.

> Draft v0.12. This is an open specification, not a product: no release cadence is promised, but issues are read and answered, and **replications on other model families are the single most useful thing anyone can contribute.** Every table below can be re-run from this repository in about five minutes.

---

## TL;DR

- **The problem.** Most of what enters an LLM's context window is not structured data — it is prose: system prompts, agent memories, briefs, runbooks, meeting notes. Prose is optimized for linear human reading, not information density. TOON and its relatives cover tabular data; nothing covers the discursive half.
- **The proposal.** TERSE = a **condensation discipline** (telegraphic rewriting with protected classes: numbers, negations, qualifiers, verbatim quotes) plus an **optional marker layer** (`!` decision, `!!` hard constraint, `>` action, `?` open question, `~` estimate, `x` ruled out). An eight-line legend, learned one-shot by any model.
- **Headline result** (23 documents and 542 questions per arm in *each* language, Sonnet 4.6 reader, one question draw shared by all three arms): **−38% input tokens for −2.3 points of strict QA accuracy.**
- **The negative result we publish anyway.** Our pre-registered success criterion was ≥50% token reduction at ≤2 points loss. **We missed it on both counts.** It is reported unchanged, as a footnote rather than a verdict.
- **The marker layer buys no QA accuracy.** Marker-free condensation ("short") matches full TERSE question-for-question (FR: 6 paired flips each way — a coin toss). We say so, and repositioned the spec accordingly.
- **What the markers *do* buy, measured**: **+3.5 points of structural recall** (TERSE 96.4% vs marker-free 92.9%, GPT reader). The part that *replicated across model families* is narrower and sharper: on *"list every settled decision"*, marker-free condensation collapses to **3/9** on both families tested. Markers operationalize categories.
- **Human-writable condensation beats statistical compression.** At matched budget, LLMLingua-2 loses 6.3 points — and its failures are *silent corruptions*: thresholds rewritten, negations inverted, identifiers mangled. All catalogued. A no-API integrity linter ([`tools/intact.html`](tools/intact.html)) mechanizes the check.
- **Bilingual by construction.** French prose costs 47% more tokens than the English equivalent in this corpus; under TERSE the gap falls to 30%.

---

## Try it in 5 minutes

1. Download [`bench/terse-bench.html`](bench/terse-bench.html) and open it in your browser.
2. Point it at any endpoint: Anthropic, an OpenAI-compatible API, or a local Ollama (free, no key).
3. Load [`corpus/corpus-EN.json`](corpus/corpus-EN.json) (drag-and-drop, or paste), pick your arms in the run matrix, click **Run benchmark**.

Questions and gold answers ship with the corpus. Runs resume after an interruption and export mid-run. The same applies to [`bench/terse-structbench.html`](bench/terse-structbench.html) (structural retrieval) and [`bench/terse-budgetbench.html`](bench/terse-budgetbench.html) (equal-window deployment).

## The notation in eight lines

```
Notation legend — each line is one claim; a marker counts only as the FIRST character of a line.
No prefix = fact.  "!"=decision  "!!"=hard constraint  ">"=action  "?"=open question
"~"=estimate  "x"=ruled out.  Indented under a "?" or "!" line: "+"=pro, "-"=con.
Inline: "->"=leads to  "=>"=if-then rule  "<-"=because  "|"=alternative  "vs"=trade-off
"@"=person/date/place  text in quotes = verbatim.  "&id" defines an anchor, "*id" references it.
Indentation = detail of parent line.  L0/L1/L2 = increasing detail levels.
MODE strict = every line exhaustively marked, absence is informative; MODE open = unmarked lines are unclassified.
Grammar words omitted; negation always explicit.
```

Measured cost of the legend: **224 tokens** on the Claude tokenizer, fixed, amortized once savings exceed it — and near-zero in production, where it belongs in a cached system prompt. A pilot found zero accuracy loss with *no* legend at all: the notation is readable on sight. Writing valid TERSE is the harder task, which is what [`prompts/CONVERT.md`](prompts/CONVERT.md) is for.

Before and after — the benchmark's built-in sample document, so you can check it against `bench/terse-bench.html` directly:

```
Following our meeting on July 10th, the team decided to migrate the customer database to
PostgreSQL rather than staying on MySQL, mainly because of better JSON support and the fact
that our lead developer Sarah already has deep experience with it. MongoDB was also considered
but was ruled out due to the lack of relational joins. The migration is estimated to take about
three weeks, although this remains uncertain. Sarah will prepare a detailed migration plan by
August 1st. One question is still open: should we host in the EU region or in the US, given
GDPR constraints?
```

```
CTX: customer DB migration
AS-OF: 2026-07-10

! migrate customer DB -> PostgreSQL (was MySQL)
  <- better JSON support; @sarah deep experience
x MongoDB (no relational joins)
~ migration ≈ 3 weeks
> @sarah migration plan, due 2026-08-01
? hosting EU | US <- GDPR
```

---

## 1. Results — reading comprehension

**Canonical paired run.** 23 documents per language, *all* questions (542 per arm per language), one question draw shared by the three versions of each document, Sonnet 4.6 as reader and judge. Raw data: [`results/canonical-EN.json`](results/canonical-EN.json), [`results/canonical-FR.json`](results/canonical-FR.json).

| Version | Tokens EN | Accuracy EN | Tokens FR | Accuracy FR |
|---|---|---|---|---|
| Prose (baseline) | 21,548 | 97.05% | 31,726 | 97.97% |
| **Short** — condensation, no markers | **−35.0%** | 95.20% | **−41.5%** | 95.76% |
| **TERSE** — condensation + markers | **−33.2%** | 94.62% | **−41.0%** | 95.75% |

Pooled over both languages (1,084 questions per arm; 1,080 graded for TERSE): prose 97.51% · short 95.48% (−2.0 pts) · **TERSE 95.19% (−2.3 pts) at −37.9% tokens**.

> **Denominator note.** Four answers were returned ungraded by the judge (3 EN-TERSE, 1 FR-TERSE) and are excluded, as in `SPEC.md` §6. Counting them as wrong instead — the worst case — gives EN 94.10%, FR 95.57%, pooled 94.83%. Both figures are recomputable from the raw JSON; nothing else in this README changes.

**Short and TERSE are statistically indistinguishable on QA.** In French the paired comparison flips 6 questions each way — a coin toss. In English short leads by a hair (10 flips vs 7). The marker layer does not aid comprehension, and this repository does not claim it does.

**Cross-lingual.** French prose costs **+47.2%** more tokens than English prose for the same content. Under short the gap is +32.6%, under TERSE **+30.0%**. Condensation removes roughly a third of the penalty French speakers pay per API call — measured, not asserted.

**Pre-registered criterion: not met.** The target fixed in advance was ≥50% token reduction with ≤2 points of accuracy loss. We reached −38% for −2.3 pts. Reported as a reference footnote, never as a pass/fail verdict on a use case: the headline result is the trade-off itself, and each user sets their own tolerance.

## 2. Results — structural retrieval (where the markers earn their place)

**StructBench, cross-family replication.** The 23 English documents concatenated per format; 10 extraction queries (11 prompts — Q4 is split by scope); 112 prose-grounded gold items independently audited before any run; three isolated ChatGPT conversations (one per format, golds never shown to the reader); central mechanical grading with contested items verified by hand. Reader: GPT-5.6 Sol. Raw data and full protocol: [`results/structbench-GPT.json`](results/structbench-GPT.json) and the `structbench-*` files in [`results/`](results/).

| Context | Input tokens † | Completeness (112 audited gold items) |
|---|---|---|
| Prose | 25,965 | 110/112 — 98.2% |
| **TERSE** | 18,809 | **108/112 — 96.4%** |
| Short (no markers) | 18,415 | 104/112 — 92.9% |

† Token counts are Claude-tokenizer measurements of the same three payloads, carried over from the automated Sonnet run. A manual ChatGPT session returns no token count, so these are not GPT-tokenizer figures; treat them as a size comparison between formats, not as the GPT bill.

The decisive item is Q1, *"list every settled decision"*: **marker-free short collapses to 3/9 on GPT — the same failure it produced on Sonnet — while TERSE answers 9/9 on GPT**, above even prose's 8/9 on the Sonnet run. Unmarked telegraphic prose becomes a haystack; `!` lines stay retrievable.

*Caveats, stated plainly.* One run per format, no repetition; grading is mechanical plus manual arbitration; the reader's exact model version is reported by the operator, not verified independently. **What replicated across families is the short-collapse on Q1, not the +3.5-point recall figure**: in the earlier Sonnet run ([`results/structbench-sonnet-v0.1.json`](results/structbench-sonnet-v0.1.json)) many cells were left ungraded — including TERSE's own Q1 — so no comparable per-format total exists there. The 112-item completeness table above rests on the GPT run alone. The final audited gold lists are not published as a separate file; the totals and the per-query `missing` items are in the JSON, and `structbench-golds-audit.md` holds the pre-audit lists and the auditor's prompt.

## 3. Results — equal-window deployment

**BudgetBench.** One context window sized to the full TERSE corpus (57,491 characters — 57,102 of corpus plus the per-document headers). Prose truncated at that budget keeps only 13 of 23 documents whole; short and TERSE fit entirely. 46 questions, 20 of them on documents past prose's cut. Raw data: [`results/budgetbench.json`](results/budgetbench.json).

| Same window (57k chars) | Overall (46 Q) | Beyond prose's cut (20 Q) |
|---|---|---|
| Prose truncated (13/23 docs fit) | 56.5% | 5.0% |
| Short (whole corpus fits) | 89.1% | 100% |
| **TERSE (whole corpus fits)** | **87.0%** | **95%** |

At equal window size, condensation answers what verbose prose cannot even see.

Two honest qualifications. **Prose did not confabulate**: on 19 of the 20 questions past its cut it answered "Not in context" — the right answer for a reader who cannot see the document. And **inside** the shared window, full prose leads clearly (96.2% vs 80.8% for both condensed formats on that 26-question subset) — a wider gap than the single-document QA delta, suggesting multi-document haystacks tax condensed formats more. Small sample, reported as is. Design note: the budget is set in characters, and prose's cheaper characters-per-token mean a token-equal budget would move the cut slightly in prose's favour.

## 4. External baseline — statistical compression

A consolidated comparison over the same 46 documents, ~920 questions per arm, assembled from two earlier campaigns — superseded for the headline by the canonical run above, but the only place the compressor arm was ever measured. **Provenance, since it matters:** the prose and TERSE rows come from Run 2 (`archive/run2.2-EN`, `run2.3-EN`, `run2.1-FR`, `run2.2-FR` — 899/920 and 861/903, 17 EN TERSE answers ungraded); the short and LLMLingua rows come from Run 3 (`archive/run3.1`–`3.4`, 920 per arm). The two campaigns share the question draw on 30 of the 46 documents and differ on the 16 (8 per language) that carry 30–32 questions, where each sampled its own 20 — overlap 11 to 15 questions out of 20. That is a real weakness of this table, and precisely why the canonical run exists.

| Arm | Tokens | Accuracy |
|---|---|---|
| Prose | — | 97.7% |
| Short | −39% | 96.2% (−1.5 pts) |
| TERSE | −38% | 95.3% (−2.4 pts) |
| LLMLingua-2 at matched budget | −35% | 91.4% (−6.3 pts) |
| LLMLingua-2 applied over TERSE | −52% | 85.4% (−12.3 pts) |

The gap is not only in the score. LLMLingua-2's failures are **silent corruptions**: 5,000 becoming "15,000 USD", a gold "No" answered "Yes", identifiers and shell commands mangled — and in the combo arm, a 99.5% threshold rewritten as "95%". In French, 19 of its 35 failures are negation- or value-class. A small self-contained specimen ships in the corpus itself: in `EN-T12`, the compressor turned a URL into `https://example. com/…`, splitting the domain with a space. A statistical compressor has no semantic guarantees; TERSE's protected classes (`SPEC.md` §3.7) are exactly the difference, and [`tools/intact.html`](tools/intact.html) — the INTACT linter, no API, runs in your browser — mechanizes the verification of any source-to-condensed pair.

Reproduce the compressor arm with [`tools/llmlingua_colab.py`](tools/llmlingua_colab.py); the compressed texts ship in the corpus as the `llml` and `llmlx` fields.

## 5. When to use what — the honest user guide

The marker layer costs ≈0.3 points of QA and 0.8–2.8% more tokens than plain condensation (EN +2.8%, FR +0.8%). What it buys, measured: +3.5 points of structural recall on the GPT run; category queries that do not collapse — the one effect that replicated on a second model family; and machine-parseability — `grep '^!!'` extracts every hard constraint of a document for zero tokens, and INTACT can then verify them.

- **Use markers for operational context**: runbooks, agent memories, decision logs, system prompts, inter-agent messages — anywhere category retrieval must be reliable and anywhere a machine will read the output.
- **Use plain condensation for narrative content**: briefs, notes, articles. You get the same tokens and the same accuracy without learning a notation.
- **Do not convert at inference time.** TERSE's production value is *native generation* — an agent writing its memory in TERSE directly. Drafting prose and converting it spends more tokens than it saves (`SPEC.md` §8).
- **Prompt caching does not make this redundant.** The cache helps *fixed* content; condensation also shrinks the *variable* content — evolving memories, inter-agent messages — and the attention window consumed.

## 6. Limits and non-results

Everything here is checkable against the raw JSON in [`results/`](results/).

- The pre-registered criterion (≥50% / ≤2 pts) was **not met**: −38% for −2.3 pts.
- The marker layer contributes **no QA accuracy**. It was hypothesized to aid comprehension; it does not. The spec was rewritten around what the data supports.
- A **single reader family** for the QA benchmark (Sonnet 4.6), and the judge comes from the same family as the reader — a known bias.
- **StructBench and BudgetBench are single runs**, no repetition, small question sets. Their point estimates are indicative; the Q1 collapse is the robust part, because it replicated across families. The +3.5-point recall figure did not: it rests on the GPT run alone (§2).
- **The §4 comparison table mixes two campaigns** with partly different question draws (§4). It is the weakest table in this README and the only one measuring the compressor.
- **The corpus is mostly synthetic-realistic**, authored for this study and partly by the notation's designer — a real bias, since such prose may be more regular and more condensable than documents found in the wild. Two of the 23 documents (`T12`, `T13`) are genuine user prompts, lightly sanitized. Third-party corpora welcome.
- **One URL in the corpus was replaced before publication.** `T12` contained a live private link; it now reads `https://example.com/stafffor2345643`, the same length and structure as the original, substituted identically in the corpus, the raw results and the benchmark files. It is the gold answer to 2 questions out of 1,084 (one per language) and nothing else changed. Disclosed here because the results files are otherwise untouched exports.
- Arm **B0** (markers without condensation) is documented in `SPEC.md` §6 as a field finding — markers alone are net-negative on size, at 103% of source characters — but **no B0 corpus or B0 run is published here**. The 2×2 factorial is complete on three cells out of four.
- Earlier runs used **question sub-sampling**, which injected enough variance to move prose itself by 3.5 points between draws. That is why the canonical run uses all questions, and why the earlier runs are archived rather than headlined.
- An earlier field finding — third-party converters applying markers correctly but keeping full sentences, producing TERSE *larger* than its source — is what forced the spec's central lesson: **all compression comes from condensation, none from markers.**

- An exploratory annex on notation as a reasoning medium lives in [`experiments/reasoning/`](experiments/reasoning/) — including the post-audit instrument postmortem.
- A second annex measures addressed, level-of-detail context (MAP + FOCUS): [`experiments/spatial-lod/`](experiments/spatial-lod/) — where the map converts unknown-unknowns into known-unknowns, and where a second instrument postmortem is recorded.

## 7. What would help most

In rough order of value: a **replication on another model family** (the bench file is all you need); a **third-party corpus**, ideally real documents rather than synthetic ones; a **run with a judge from a different family than the reader**; the missing **B0 arm**; and the untested structural properties — selective L0/L1 loading, strict-mode exhaustiveness, anchor reuse on long documents. Open an issue.

## 8. Repository map

| Path | Contents |
|---|---|
| [`SPEC.md`](SPEC.md) | The specification: notation, condensation rules, benchmark protocol, every run's results and caveats (§6), authoring pipeline (§7), native-generation templates (§8), changelog (§11). |
| [`bench/`](bench/) | Three single-file HTML benchmarks, no build step: `terse-bench` (QA, v0.11), `terse-structbench` (structural retrieval, v0.3), `terse-budgetbench` (equal window, v0.1). |
| [`corpus/`](corpus/) | 23 documents × 2 languages × 5 versions (`prose`, `short`, `terse`, `llml`, `llmlx`) + 542 questions per language with gold answers. Schema in [`corpus/README.md`](corpus/README.md). |
| [`prompts/`](prompts/) | The authoring pipeline as standalone prompts: `CONVERT`, `AUDIT`, `QUESTIONS`, `SHORT`. |
| [`tools/`](tools/) | `intact.html` — the INTACT semantic-integrity linter (no API, in-browser; detects on English and French text alike). `llmlingua_colab.py` — the compressor baseline, for Google Colab. |
| [`results/`](results/) | Every run, with an [`INDEX.md`](results/INDEX.md) saying what each one is and what supersedes it — including the superseded ones, in `archive/`. |
| [`experiments/`](experiments/) | Exploratory annexes. Currently: [reasoning in a condensed medium](experiments/reasoning/) — pre-registered hypothesis, two model families, two languages, instrument postmortem; and [spatial context & semantic LOD](experiments/spatial-lod/) — addressed MAP + FOCUS context, a three-map ablation, pre-registered P1–P3, second instrument postmortem. |

## Licence

`LICENSE` is the MIT licence, and it governs the code: the three benchmarks in `bench/`, the tools in `tools/`, and any script. The written and measured material — `SPEC.md`, this README, the corpus in `corpus/`, the prompts in `prompts/` and the results in `results/` — is released under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). In both cases: use it, fork it, build on it; just say where it came from.

## Citation

```
Souetre, Y. (2026). TERSE — a token-efficient notation for discursive LLM context (v0.12).
https://github.com/yannsouetre/terse-notation
```

*Naming note: unrelated to IBM's TERSE mainframe compression format (1984) or the Terse assembly-style language (1987). Both are legacy projects outside the LLM space; the name is kept with this disambiguation.*
