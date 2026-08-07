# TERSE — a token-efficient notation for discursive context

> **What TOON does for JSON, TERSE does for prose.**

**TERSE** — *Token-Efficient Representation of Semantic Elements.*

**Status:** consolidated draft v0.12 · CC-BY 4.0 (tools and benchmarks in the repository: MIT) · changelog in §11
**Repository:** https://github.com/yannsouetre/terse-notation — corpus, benchmarks, raw results, and a README summarising §6.

**Positioning (v0.10).** TERSE is **reliability-first**: a condensation discipline whose guarantees (protected negations, values, qualifiers; provenance anchors; markers that operationalize fuzzy categories) exist to keep condensed context *faithful and retrievable*. The token economy is real — and it is the corollary, not the point. Measured profile against verbose prose (canonical paired run, all questions): ~59–67% of the input tokens for −2.2/−2.4 pts QA, with the marker layer costing ≈0.3 pt QA and 0.8–2.8% more tokens than marker-free condensation while buying +3.5 pts of structural recall (measured on the GPT run; what replicated on a second model family is the category-collapse signature of §6 Run 5, not the recall figure) and machine-parseability. Markers are for operational context — runbooks, agent memories, decision logs, system prompts — where category retrieval must be reliable; plain short covers narrative content. And none of the silent corruptions of statistical compressors.

> *Naming note — not related to IBM's TERSE mainframe compression format (1984), nor to Terse, an x86 assembly-style language (1987). Both are legacy projects outside the LLM space; the name is kept with this disambiguation.*

---

## 1. Why

Most of what enters an LLM's context window is not structured data — it is **discursive prose**: instructions, briefs, agent memories, meeting notes, project state. Prose is optimized for linear human reading, not for information density: a large share of its tokens serve grammatical glue and textual coherence rather than content.

Existing solutions cover only the edges of this problem:

- **TOON / CSV / compact JSON** — excellent for uniform, tabular data; not applicable to discursive content.
- **Automatic prompt compressors** (LLMLingua, gisting/gist tokens) — effective, but their output is not readable, writable, or maintainable by a human.
- **Informal habits** (telegraphic prompting, ad-hoc shorthand) — no shared conventions, no spec, no benchmark.

TERSE fills the gap: a **compact, human-writable, language-neutral notation for discursive context**, learnable by any LLM from a short legend.

**Goals**

1. 40–60% fewer tokens than equivalent prose.
2. No measurable loss on factual comprehension (benchmarked, §6).
3. Writable and readable by a human in any text editor, with zero tooling.
4. Language-neutral skeleton: markers carry the semantics, content words may be in any language.

**Non-goals**

- Replacing TOON/JSON/CSV for structured data (TERSE is complementary — §3.6).
- Compressing text whose exact wording matters (legal, literary, quotations): keep those verbatim.
- Machine-only codes unreadable by humans (that niche is served by automatic compressors).
- Ad-hoc user prompts: nobody should be asked to type TERSE, and translating a one-off prompt costs more than it saves.

**Primary targets** (in order): system prompts and standing agent instructions; agent memory files; inter-agent messages. These are fixed infrastructure texts — written once by a motivated author, read many times by machines, and cacheable, so the legend's fixed cost is paid once and then amortized to near zero by prompt caching. Model-generated output (terse reasoning drafts, Chain-of-Draft adjacent) is a prospective extension — see arm F in §6.

---

## 2. Design principles

1. **The default is silent.** The most frequent statement type — a plain fact — carries no marker. You only pay tokens for what departs from the default.
2. **Recycle, don't invent.** Every marker reuses a convention massively present in LLM training data (YAML anchors, arrows, indentation, `?`, `!`, `|`). Models parse them natively; each marker tokenizes as a single cheap token. A symbol only has value if models have already learned what it means.
3. **One line = one claim.** Lines are atomic. This enables diffing, partial reading, precise citation, and line-level editing of context files.
4. **Epistemic status is never compressed away.** Negation, uncertainty, questions, and rejected options must remain explicit. This is a safety rule, not a style rule: a compression scheme that can silently turn "do not deploy" into "deploy" is broken.
5. **Legend-teachable.** The entire notation must fit in a short preamble (§4) that any model can learn one-shot, with no fine-tuning.
6. **Position disambiguates.** A small glyph set is reused safely because meaning is bound to position: a marker is only a marker as the *first* character of a line; the same glyph inline is ordinary content (`>` at line start = action; `churn > 5%` inline = greater-than).
7. **One meaning, one form.** No alternative syntaxes for the same semantics. Variants split the corpus, complicate validation, and double the legend.

---

## 3. The notation

### 3.1 Document header (optional fields)

```
CTX:   <title>
AS-OF: <date>
MODE:  strict | open          (default: open)
LEX:   <abbr>=<expansion>; <abbr>=<expansion>
```

**`MODE`** declares the reading contract for marker *absence* (closed-world vs open-world):

- **`open`** (default) — markers are used where helpful; unmarked lines are simply *unclassified* and the model uses judgment. Absence of a marker carries no information. Sloppy writing degrades gracefully.
- **`strict`** — the writer guarantees exhaustive marking. Absence becomes informative: a line without `~` is confirmed, not an estimate; a document without `?` has no open questions. Suitable for agent memories and instruction files, where a model must be able to *rely* on absences.

**Scope and immutability:** one `MODE` per document, applying to the whole document; it cannot change mid-document (a mid-document switch would make absence-semantics retroactively ambiguous). To change modes, start a new document (new `CTX` block). Several TERSE documents may coexist in one context window, each governed by its own header.

**`LEX`** declares document-local abbreviations. Abbreviating without declaring is invalid.

### 3.2 Line markers (first character(s) of a line)

| Marker | Meaning | Example |
|--------|---------|---------|
| (none) | fact / statement | `team = 12 people, 3 remote` |
| `!`    | decision (settled) | `! PostgreSQL over MySQL` |
| `!!`   | hard constraint (non-negotiable: obligation or prohibition) | `!! customer data stays in EU (GDPR)` |
| `>`    | action / next step | `> @sarah migration plan, due 2026-08-01` |
| `?`    | open question | `? hosting EU \| US` |
| `~`    | estimate / uncertain | `~ migration ≈ 3 weeks` |
| `x`    | rejected / ruled out | `x MongoDB (no relational joins)` |
| `+` / `-` | pro / con — **scoped**: markers only when indented under a `?` or `!` line; ordinary characters anywhere else | see §5.2 |

`!!` covers prohibitions as well as obligations because negation is always explicit (§3.7): `!! never bulk-email customers without opt-in check`.

### 3.3 Inline operators

| Operator | Meaning |
|----------|---------|
| `->`     | leads to / causes / then (sequence: *it happens*) |
| `=>`     | conditional rule (contingency: *only if*) — `churn > 5% => rollback` |
| `<-`     | because / derived from |
| `=`      | is / equals / defined as |
| `\|`     | alternative (inclusive or) — `hosting EU \| US` |
| `vs`     | opposition / trade-off under arbitration — `Prisma vs raw SQL` |
| `@`      | anchor: person, date, or place (`@sarah`, `@2026-07`, `@Paris`) |
| `"…"`    | verbatim — content inside quotes is never condensed or altered |

`->` vs `=>`: `launch -> press release` (after launch, PR follows) versus `budget > 50k => escalate @dg` (escalate *only if* the condition holds). `=>` lines are greppable: extracting every `=>` yields the complete rule set of a document; extracting every `!!` yields its constraint set.

**Logical composition (mapping from SQL/logic keywords).** The classic connectives are already present — in symbol form, preferred over English keywords for language-neutrality (a writer should not need English to reason) and under principle 7 (one meaning, one form):

| Keyword | TERSE form |
|---------|-----------|
| IF … THEN | `condition => consequence` |
| OR | `\|` |
| AND | `;` between clauses, `,` inside lists — `<- cost; CS familiarity` reads "because cost AND familiarity" |
| NOT | explicit negation words, protected by §3.7 rule 3 (never dropped) |
| CASE / WHEN | several `=>` lines forming a rule set |

Compound conditions group with parentheses: `(churn > 5%, NPS < 30) => rollback`. Note: `&` is **reserved for anchor definitions** and never means "and".

Inline `>` and `<` are ordinary comparison operators (principle 6); only line-initial `>` marks an action.

### 3.4 Hierarchy and references

- **Indentation (2 spaces)** = the line elaborates its parent line.
- **Group label:** a short unmarked line ending with `:` (e.g. `planning:`) labels a group; its members are indented under it. Use it instead of section sentences.
- **`&id`** defines an anchor on a line; **`*id`** references it from anywhere in the document (YAML anchor/alias convention). This gives non-linear structure — forward and backward jumps, including across detail levels — without repetition.

### 3.5 Detail levels (progressive disclosure)

Optional section labels split a document into layers of increasing granularity:

```
L0: <one-line gist of the whole document>
L1:
<standard operating detail — the default reading level>
L2:
<fine detail, edge cases, history>
```

A reader — human or model — can be instructed to load only `L0`–`L1`, trading depth for context budget. `L0` alone must remain a faithful summary.

### 3.6 Interoperability

For tabular data inside a TERSE document, embed a fenced TOON or CSV block rather than forcing tables into lines. TERSE handles the discourse; TOON handles the tables.

### 3.7 Condensation rules

1. Drop articles, copulas, and connective filler ("the", "is", "in order to").
2. **The marker replaces its own words:** "decided to" → `!`, "must (not)" → `!!`, "estimated / uncertain" → `~`, "ruled out" → `x`, "open whether" → `?`. Never keep both the marker and the phrase — a marked full sentence is markup, not TERSE.
3. Keep all content words, numbers, units, and names verbatim; dates in ISO form (2027-03-31); numbers and units compact (50 000 euros → 50k EUR).
4. **Never drop negation** ("not", "no", "except", "never"). If condensation creates any ambiguity, restore the full wording.
5. Abbreviate only through `LEX`-declared abbreviations.
6. One idea per line; prefer a new indented line over a long compound line. State the document's subject once (in `CTX`), not at the start of every line.
7. Text inside quotation marks is copied verbatim.
8. **Size discipline:** a faithful conversion of factual prose lands around 50–65% of the source's characters (numbers, names and dates are incompressible; only grammar is). Above ~75% is markup without condensation (see the §6 field finding), not TERSE. Character reduction over-estimates token reduction: deleted grammar words are cheap tokens, kept content words are expensive ones — as a rule of thumb, token reduction ≈ 0.8 × character reduction.
9. **Protected precision** (from Run 1 error analysis, §6): (a) comparatives keep an explicit direction word — "C cheaper than B by 6%", never a bare signed figure; (b) qualifiers that gate a threshold or a legal condition ("strictly", "written **and motivated**", "formal") are content words — never dropped; (c) the document's self-description (type, sector, intended audience) is preserved as explicit facts near the header, e.g. `type = scoping note (industrial)` — titles compress, metadata must not vanish with them.

---

## 4. The legend (canonical preamble)

Prepend this once to teach the notation to any model:

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

(Measured: ≈ 224 tokens on the Claude tokenizer — twice the initial ~120 estimate. A fixed cost, amortized once savings exceed it; in production the legend belongs in a cached system prompt, where its marginal cost after the first call is near zero.)

---

## 5. Examples

### 5.1 Minimal example

**Prose** (99 words, ≈ 130 tokens):

> Following our meeting on July 10th, the team decided to migrate the customer database to PostgreSQL rather than staying on MySQL, mainly because of better JSON support and the fact that our lead developer Sarah already has deep experience with it. MongoDB was also considered but was ruled out due to the lack of relational joins. The migration is estimated to take about three weeks, although this remains uncertain. Sarah will prepare a detailed migration plan by August 1st. One question is still open: should we host in the EU region or in the US, given GDPR constraints?

**TERSE** (≈ 55 tokens, header included):

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

≈ 58% token reduction on this sample (estimates; exact counts per tokenizer are part of the benchmark, §6). Note what is *not* lost: the decision is marked as settled, the rejected option is preserved with its reason, the estimate is flagged as uncertain, and the open question stays open.

### 5.2 Full example — all features

```
CTX: CRM revamp — project state
AS-OF: 2026-07-18
MODE: strict
LEX: CS=customer success; MW=marketing website

L0: CRM revamp on track for Sept go-live; EU-data constraint drives all infra choices; budget risk on data cleanup.

L1:
!! &eu customer data stays in EU (GDPR)
! CRM = HubSpot (was Salesforce) <- cost; CS familiarity
! hosting -> Frankfurt <- *eu
~ go-live @2026-09-15
> @marco data-cleanup plan, due 2026-08-01
? MW integration: native form | API bridge
  + native: zero code
  - native: weak analytics
  + API bridge: full tracking
  - API bridge: ~2 wks dev
budget = 60k EUR
  ~ cleanup may add 8-10k
churn > 5% post-launch => rollback plan *rb

L2:
x Salesforce (licensing 3x; admin overhead)
x self-hosted CRM (*eu satisfied, but maintenance cost)
legacy DB @2019: 40% duplicate contacts -> cleanup scope
&rb rollback = freeze sync, revert DNS, restore @2026-09-14 snapshot
@marco = data lead since 2026-03
```

**What the anchors buy.** `&eu` is defined once; two decisions reference it with `*eu` (3–4 tokens each) instead of restating the constraint (~12 tokens each). `&rb` lives in L2, yet the L1 rule `=> rollback plan *rb` points to it — a jump across detail levels, which linear prose cannot do without repetition.

**What the levels buy.** Three read budgets from one file: `L0` alone (~25 tokens) for routing decisions; `L0+L1` (~140 tokens) for normal operation; full document for deep work.

**Honest caveats — hypotheses to test, not features to assert:**

- Anchors have a fixed cost and pay off only when a referent is reused; below some document size they are probably neutral or negative.
- Levels pay off only in selective-loading scenarios; if a consumer always reads the whole file, `L0` is overhead.

---

## 6. Benchmark protocol (pre-registered)

*In plain terms: the notation is tested in pieces, so every feature must earn its place with data — anything that fails its test gets demoted from core to extension.*

- **Corpus:** 15–20 realistic context documents (project briefs, meeting notes, agent memories), each authored in four versions: prose-EN, TERSE-EN, prose-FR, TERSE-FR.
- **Treatment arms (ablations):**
  - **A.** Prose (baseline)
  - **B.** Core notation only (markers + condensation; no levels, no anchors)
  - **C.** B + detail levels, evaluated under selective loading
  - **D.** B + anchors, on documents long enough for referent reuse
  - **E.** Full notation

Two additions from field methodology (v0.8):
- **Arm S ("short")** — condensation without the marker system: telegraphic, line-based, plain-language modality words ("must", "decided", "rejected"), no TERSE symbols. Completes the 2×2 factorial — A = neither, B0 = markers only, S = condensation only, B = both — and isolates the semantic markers' own contribution: if S matches B on accuracy at similar tokens, markers earn structure and greppability only; if B beats S, markers demonstrably aid comprehension.
- **External baseline: LLMLingua-2** at matched compression ratio (per-document rate set to the TERSE/prose ratio), answering "at equal token budget, who keeps more accuracy?" — plus an exploratory combo (LLMLingua over TERSE), with an integrity check required: statistical compressors can drop negations and markers, which TERSE's guarantees forbid.
- **Metrics per arm:**
  1. Token count, measured with the official tokenizers of the major model families.
  2. Factual QA accuracy: 20–30 questions per document whose answers are contained in the context; prose vs TERSE vs TERSE+legend, across models.
  3. Rule-extraction accuracy: find all `=>` rules and all `!!` constraints of a document.
  4. For arm C, the **equal-budget test**: at an identical token budget, `L0+L1` selective loading vs prose truncated to the same length. If structure beats truncation at equal cost, that is the headline result.
- **Success criterion (fixed in advance):** ≥ 50% token reduction with ≤ 2 points QA accuracy loss.
- **Cross-lingual claim:** the FR/EN token-count gap under TERSE is smaller than under prose (language-neutrality demonstrated, not asserted).
- A negative or partial result (e.g. "beyond N% compression, accuracy degrades by M") is published as-is.

**Prospective arm F** (out of scope for corpus v1): reasoning tasks — standard chain-of-thought vs TERSE-constrained draft reasoning. Motivation: reasoning tokens are billed as output, and Chain-of-Draft-style results suggest telegraphic reasoning steps can keep most accuracy for a fraction of the tokens, while a TERSE draft — unlike latent approaches — stays human-readable.

**Display policy.** The headline result is the trade-off itself (tokens saved vs accuracy points lost); each user sets their own tolerance for degradation. The pre-registered threshold above is reported unchanged, as a reference footnote — never as a pass/fail verdict on a use case.

**Field finding — markup without condensation** (23-doc bilingual corpus, third-party converters, v0.4.1 prompt): converters applied the markers largely correctly but kept full grammatical sentences. Result: TERSE at 100–113% of source characters (mean 103%, identical in FR and EN) — *larger* than the prose. Lesson: **markers alone are net-negative on size; all compression comes from condensation.** The CONVERT prompt now treats condensation as its central section, with a quantified size target enforced in the self-check. The under-condensed corpus is retained as **arm B0 (markup-only)**: it isolates the token cost and the comprehension effect of structure, separately from condensation.

**Run 7 — canonical paired run (bench v0.11, questions = all, single draw shared by the three arms of each document).** 23 docs × 542 questions per arm and language, Sonnet 4.6. **EN: prose 97.05% · short −35% tk / 95.20% · TERSE −33% / 94.62%. FR: prose 97.97% · short −41% / 95.76% · TERSE −41% / 95.75%** (paired short-vs-TERSE in FR: 6 flips each way — statistically indistinguishable). Global (1,084 per arm; 1,080 graded for TERSE): prose 97.5%, short 95.5% (−2.0), TERSE 95.2% (−2.3). This homogeneous dataset supersedes the earlier patchwork EN baselines; QA equivalence of short and TERSE is now established at full protocol, which isolates the marker layer's value where Runs 5–6 measured it: structural retrieval and budget fit.

**Run 6 — equal-budget deployment test (BudgetBench, Sonnet 4.6).** One context window sized to the full TERSE corpus (57,491 chars): prose truncated at that budget keeps only 13 of 23 documents whole; short and TERSE fit entirely. 46 questions (2 per document, 20 of them on documents beyond prose's cut). **Overall: prose-truncated 56.5% · short 89.1% · TERSE 87.0%.** Beyond the cut: prose 5.0% (19/20 honest "Not in context", zero confabulation — the reader did not invent), short 100%, TERSE 95%. Inside the window, full prose leads (96.2% vs 80.8% for both condensed formats on this 26-question subset — a larger gap than the single-document QA delta; small sample, and multi-document haystacks appear to tax condensed formats more: reported as is). Net reading: at equal window size, condensation trades a few within-window points for the ~40% of the corpus that verbose prose cannot even see. Design note: the budget is set in characters; prose's cheaper chars-per-token mean a token-equal budget would move the cut slightly in prose's favor.

**Run 5 — structural retrieval, cross-family replication (GPT reader, manual protocol).** The 23 EN documents concatenated per format; 10 extraction queries (11 prompts — Q4 split by scope; the payload's own header says 12, uncorrected and identical across arms); 112 prose-grounded gold items independently audited; three isolated ChatGPT conversations (one per format, golds never shown); central mechanical grading with hand-verified contested items. Inputs: prose 25,965 tk / short 18,415 / terse 18,809 (Claude-tokenizer measurements of the same payloads — a manual ChatGPT session returns no token count). **Completeness: prose 110/112 (98.2%) · TERSE 108/112 (96.4%) · short 104/112 (92.9%).** Output tokens (approx.): prose ~3,212 / short ~2,846 / terse ~2,950. The decisive replication: on "list every settled decision" (Q1), **short collapses to 3/9 on a second model family — the same failure signature as the Sonnet run — while TERSE answers 9/9**, above even prose's 8/9 on the Sonnet run. Note the asymmetry: the short-collapse replicated across families, but TERSE's own Q1 cell was left ungraded in the Sonnet run, so only the GPT run supports the 9/9. Reading: marked lines make categories retrievable where unmarked telegraphic prose becomes a haystack; TERSE recovers nearly all of prose's recall at 72% of its input cost. Caveats: single run per format; grading is mechanical-plus-manual (method and per-item data in results/); GPT model version reported by the operator.

**Run 3 — final consolidated results (five arms, 46 documents, ~920 questions/arm, Sonnet 4.6 reader).** Pooled, each arm paired against prose on its own documents:

| Arm | Tokens | Accuracy |
|---|---|---|
| Prose | — | 97.7% |
| **Short** (condensation, no markers) | **−39%** | **96.2%** (−1.5 pts) |
| **TERSE** (condensation + markers) | **−38%** | **95.3%** (−2.4 pts) |
| LLMLingua-2 (matched budget) | −35% | 91.4% (−6.3 pts) |
| LLMLingua-2 over TERSE | −52% | 85.4% (−12.3 pts) |

Per language: EN short −35%/95.7% vs terse −33%/95.0%; FR short −41%/96.7% vs terse −41%/95.7%. On the hard EN cluster (T18–T23), terse edges short (90.8% vs 90.0%) — within noise.

Findings. (1) **Human-writable condensation carries the value**: at equal or better compression, short and TERSE lose 1.5–2.4 pts where LLMLingua-2 loses 6.3 — and the compressor's failures are *silent corruptions*: thresholds rewritten (99.5% becoming "95%", 5,000 becoming "15,000 USD"), polarities inverted ("Yes" on a gold "No"), identifiers and shell commands mangled; in FR, 19 of its 35 failures are negation/value-class. A statistical compressor has no semantic guarantees; §3.7's protected classes are exactly the difference, and the INTACT companion linter mechanizes their verification. (2) **The marker layer buys no QA accuracy** (short ≥ terse overall) — it is repositioned as what the data supports: *optional machine-readable structure at no meaningful token cost* (greppable `!!`/`=>` sets, strict mode, selective loading — structural properties the QA metric does not exercise and which remain untested). TERSE is best described as **a condensation discipline (§3.7) with an optional marker layer (§3.2)**. (3) Caveats: terse baselines come from earlier runs (different question draws); 17 EN terse answers ungraded; single reader family — replication invited.

**Run 2 results** (bench v0.7 — permissive judge). **FR corpus, 19 docs × 20 questions (380 graded/arm): −39% tokens (61% ratio; per-doc 48–73%) for −1.6 pts (98.4% → 96.8%) — within the accuracy criterion.** EN corpus re-run, 23 docs × 10 sampled questions: tokens identical to Run 1 to the digit (21548/14392 — instrument determinism confirmed), accuracy 94.3% → 90.9% (−3.5 pts) on this draw versus −3.0 on Run 1's draw, with prose itself dropping 3.5 pts between draws: 10-question sampling injects variance in both arms. Lessons: (1) publication runs use *all* questions; (2) the cross-lingual pattern holds a third time — French compresses more (−39% vs −33%) and here also preserved accuracy better.

**Run 1 results** (bench v0.6, full EN corpus: 23 docs × 10 sampled questions, Sonnet 4.6 reader, arms A/B): **−33% tokens** (TERSE at 67% of prose; per-doc range 57–82%, longer documents compressing better) for **−3.0 pts accuracy** (97.8% → 94.8%, 230 graded questions per arm). Character reduction was ~40%; the char→token discount matches §3.7.8. Paired analysis: 9 questions prose-correct/TERSE-wrong vs 2 TERSE-correct/prose-wrong (in both reverse cases the fact was buried mid-paragraph in prose and found as a greppable line in TERSE — the structural retrieval benefit, observed). Failure taxonomy of the 9: document self-description lost (3), precision/qualifier erosion — comparatives, "strictly", "motivated" (3), judge strictness on answers *more* specific than the gold (2), attribute-attachment confusion under heavy condensation (1). Mitigations shipped in v0.7: §3.7.9 protected-precision rules and a judge instruction accepting answers that contain the gold plus correct detail. Below the pre-registered reference (≥50%, ≤2 pts) — reported as such; the trade-off stands on its own.

**Pilot results** (bench v0.2, quick mode — 4 questions/doc, Haiku 4.5 reader, 3 short designer-authored docs; indicative only): core arm −26% tokens (EN) and −43% (FR) with 0 accuracy loss (12/12, matching prose); a full-notation doc (MODE, LEX, L0, anchors, ~300 prose tokens) came out +5% — structural overhead exceeds condensation at that size when the whole document is loaded, which is exactly what the ablation design exists to price. Legend fixed cost measured at 224 tokens (identical across two documents — instrument sanity check). Cross-lingual claim supported: the FR/EN token gap fell from +58% (prose) to +21% (TERSE). Known biases: tiny sample, documents authored by the notation's designer, judge from the same model family as the reader.

---

## 7. Corpus authoring pipeline

Corpus documents are built **prose-first**, in this exact order — questions are always written from the prose, never from the TERSE version, so the notation cannot be taught to the test. The TERSE Bench "Corpus builder" automates steps 2–5; the prompts below are the exact ones it uses, for standalone use in any chat or API. The CONVERT prompt is **self-contained** — it embeds the full writer-grade syntax reference and a worked example, and depends on no attachment. Replace `{PROSE}`/`{TERSE}` with your texts and `{N}` with the question count.

*Design note — reading vs writing competence.* The §4 legend is reader-grade: it suffices for a model to *understand* TERSE (pilot: zero accuracy loss with no legend at all). Writing valid TERSE is a harder task and needs the full reference below. Prompt length is irrelevant here: conversion is a one-off authoring cost, not a recurring inference cost.

**Step 1 — Collect.** Pick a real document (anonymize it) or generate a realistic synthetic one — ideally with models from several families, to vary style. Target mix: system prompts and agent instructions, project briefs, meeting minutes, memory files, runbooks. Size bands: short 100–300 tokens (covered by the sample corpus), medium 500–1500, long 2000–5000 (required for arms C/D).

**Step 2 — Convert** with the CONVERT prompt (7.1). It embeds the legend, the condensation rules, and a mandatory self-check pass (facts, negations, marker validity).

**Step 3 — Audit** with the AUDIT prompt (7.2), ideally run on a model from another family than the converter. Fix the TERSE version and re-audit until `"ok": true`.

**Step 4 — Question set** with the QUESTIONS prompt (7.3), run on the **prose only**: factual lookups, at least one negation/constraint, one rule/trigger if present, and exactly one trap whose gold answer is "not in context" (hallucination probe).

**Step 5 — Assemble.** One JSON object per document: `{"id","lang","title","prose","terse","questions":[{"q","a"}]}`, plus one optional field per additional arm — `short` (companion SHORT prompt, arm S), `llml` and `llmlx` (LLMLingua baselines). Bench v0.11 reads this flat schema and exposes each field as its own run-matrix column. Merge objects into `{"docs":[…]}` — by hand, or with the bench's "Import JSON file(s) — merge" button, which accepts single-doc and full-corpus files alike.

**Step 6 — Bilingual versions.** Translate the **prose** first, then re-run steps 2–5 on the translation. Never translate the TERSE version directly.

### 7.1 CONVERT prompt (self-contained)

```
You are a converter into TERSE (Token-Efficient Representation of Semantic Elements), a compact, human-readable notation for discursive context. TERSE keeps every fact of a prose document while removing grammatical filler, so that LLMs can read the same information in far fewer tokens. Your job: rewrite the source document below in valid TERSE, losing nothing, adding nothing.

=== TERSE SYNTAX REFERENCE ===

A TERSE document = an optional header + one claim per line.

HEADER (only include fields that apply):
CTX: <short title>              - always include
AS-OF: <date>                   - if the document states its date
MODE: strict                    - include it only if you mark every line exhaustively (recommended for conversions)
LEX: <abbr>=<expansion>; ...    - declare every abbreviation you use; no undeclared abbreviations

LINE MARKERS - the FIRST character(s) of a line define its type:
(no marker)  plain fact             team = 12 people, 3 remote
!            settled decision       ! CRM = HubSpot (was Salesforce)
!!           hard constraint (non-negotiable obligation or prohibition)   !! customer data stays in EU (GDPR)
>            action / next step     > @sarah migration plan, due 2026-08-01
?            open question          ? hosting EU | US
~            estimate / uncertain   ~ go-live @2026-09-15
x            rejected / ruled out   x MongoDB (no relational joins)
+  and  -    pro and con, ONLY when indented under a "?" or "!" line:
             ? ORM: Prisma | raw SQL
               + Prisma: faster onboarding
               - Prisma: weak on complex queries

INLINE OPERATORS (inside a line):
->   leads to / causes / then       launch -> press release
=>   if-then rule (only if)         churn > 5% => rollback
<-   because / derived from         ! hosting -> Frankfurt <- GDPR
=    is / equals / defined as       budget = 60k EUR
|    alternative (inclusive or)     ? hosting EU | US
vs   trade-off under arbitration    Prisma vs raw SQL
@    person, date or place anchor   @sarah, @2026-07, @Paris
"..."  verbatim - text in quotes must be copied exactly, never condensed
Note: ">" inline is the ordinary comparison operator (churn > 5%); only line-initial ">" means action. "&" is reserved for anchors and never means "and": write "and" with ";" between clauses or "," inside lists.

STRUCTURE:
- Indentation (2 spaces) = the line elaborates its parent line.
- A short unmarked line ending with ":" (e.g. "planning:") labels a group; its lines are indented under it.
- &id defines an anchor on a line; *id references it from anywhere (avoids repeating a fact):
  !! &eu customer data stays in EU (GDPR)
  ! hosting -> Frankfurt <- *eu
- Detail levels, for LONG documents only: "L0:" = one-line gist of the whole document, then "L1:" = main content, then "L2:" = fine detail and history. A reader may load only L0+L1, so L0 must stay a faithful summary.

=== WORKED EXAMPLE ===

SOURCE (prose): Following our meeting on July 10th, the team decided to migrate the customer database to PostgreSQL rather than staying on MySQL, mainly because of better JSON support and the fact that our lead developer Sarah already has deep experience with it. MongoDB was also considered but was ruled out due to the lack of relational joins. The migration is estimated to take about three weeks, although this remains uncertain. Sarah will prepare a detailed migration plan by August 1st. One question is still open: should we host in the EU region or in the US, given GDPR constraints?

CONVERSION (TERSE):
CTX: customer DB migration
AS-OF: 2026-07-10
MODE: strict

! migrate customer DB -> PostgreSQL (was MySQL)
  <- better JSON support; @sarah deep experience
x MongoDB (no relational joins)
~ migration = about 3 weeks
> @sarah migration plan, due 2026-08-01
? hosting EU | US <- GDPR

=== CONDENSATION TECHNIQUE (the heart of the job) ===
Write like a telegram: every character costs. A marker NEVER excuses keeping the sentence - the marker REPLACES the words that carried its meaning.

ANTI-PATTERN (the most common failure: markup without condensation):
BAD:  ! The team decided to migrate the customer database to PostgreSQL before the deadline.
GOOD: ! migrate customer DB -> PostgreSQL before 2027-03-31
BAD:  ! La direction a decide de migrer vers NovaCRM avant cette echeance.
GOOD: ! migration -> NovaCRM avant 2027-03-31
If a line still reads as a grammatical sentence, it is not TERSE yet.

Condensation rules, applied to EVERY line:
C1. Delete articles, possessives, demonstratives (the/a/an/this; le/la/les/un/une/ce/cette...).
C2. Delete copulas and light verbs; use "=", ":", "->" instead. "The project sponsor is Claire Renaud" -> "sponsor = Claire Renaud".
C3. The marker replaces its own words: "decided to" -> "!" ; "must / must not / mandatory" -> "!!" ; "is estimated at / roughly / remains uncertain" -> "~" ; "was ruled out / will not be done" -> "x" ; "the question remains whether" -> "?". Never keep both the marker and the phrase.
C4. Nominalize verbs: "The vendor will end support on March 31, 2027" -> "vendor support ends = 2027-03-31".
C5. Dates in ISO (2027-03-31; "Feb 12 at 6 pm" -> 2027-02-12 18:00). Numbers and units compact (50 000 euros -> 50k EUR; nine years -> 9 years).
C6. State the document's subject once (CTX); never re-open lines with it. Indentation attaches details to their parent line.
C7. A short unmarked line ending with ":" (e.g. "planning:") labels a group; indent its lines under it. Use it instead of section sentences.
C8. Merge trivially related micro-facts on one line with ";" or ","; split any line carrying two unrelated claims.
C9. One claim per line; prefer a new indented line over a long compound line.
C10. Size target: the TERSE body should land around 50-65% of the source's characters. Above 75% means you only added markers to sentences - restart the condensation pass.

NEVER compressed away: numbers, units, names, dates, text inside quotation marks (copied verbatim) - and negations ("not", "no", "never", "except", "aucun", "sauf"): keep them explicit, always. If condensing creates any ambiguity, keep the full wording. Use L0/L1/L2 and anchors only if the conversion exceeds ~40 lines. Add no information absent from the source; lose none present in it; do not resolve open questions or uncertainties - mark them "?" or "~".

=== SELF-CHECK (mandatory before answering) ===
Re-read your draft against the source and verify:
(1) every fact, number, name and date of the source is present;
(2) every negation and uncertainty is preserved;
(3) every line starts with a valid marker or none;
(4) "+"/"-" appear only indented under a "?" or "!" line;
(5) every abbreviation you used is declared in LEX;
(6) the TERSE body is at or under ~65% of the source's characters - above 75%, your lines are still sentences: redo the condensation pass.
Fix violations, then output.

OUTPUT: only the final TERSE document. No commentary, no code fences.

=== SOURCE DOCUMENT ===
{PROSE}
```

### 7.2 AUDIT prompt

```
You audit a conversion for information equivalence. Compare SOURCE (prose) and CONVERSION (TERSE notation). Ignore style; check facts, numbers, names, dates, negations, uncertainty, decisions, open questions.
Output ONLY JSON, no code fences: {"ok": true|false, "missing": ["fact in source but absent from conversion"], "added": ["fact in conversion but absent from source"]}

<source>
{PROSE}
</source>
<conversion>
{TERSE}
</conversion>
```

### 7.3 QUESTIONS prompt

```
You write a QA set for a reading-comprehension benchmark, from the document below, in the document's language.
Write {N} question/answer pairs:
- mostly factual lookups (names, numbers, dates, decisions, reasons);
- at least one about a negation, constraint, or rejected option;
- at least one about a conditional rule or trigger, if the document has any;
- exactly one trap question that sounds plausible but is NOT answered in the document; its gold answer must be exactly: "not in context".
All other questions must be answerable from the document alone. Answers must be short and factual.
Output ONLY a JSON array, no code fences: [{"q":"...","a":"..."}]

<document>
{PROSE}
</document>
```

---

## 8. Native generation (system prompts)

Conversion (§7) exists for corpus building and for migrating existing documents. The production value of TERSE, however, is **native generation**: an AI writing its memory entries, status reports, inter-agent messages — and, experimentally, its reasoning drafts — directly in TERSE. The zero-detour rule is absolute: *think, then write TERSE; never draft prose and convert* — a prose-then-convert pipeline at inference time spends more tokens than it saves and defeats the purpose.

The templates below are for AI engineers to paste into system prompts. They share one common core; place the template (with the core inlined at `{CORE}`) in the **cached** system prompt, so its fixed cost is paid once.

### 8.1 Common core — inline where `{CORE}` appears

```
TERSE writing rules (Token-Efficient Representation of Semantic Elements):
- One claim per line. The line marker is the FIRST character(s): no marker = fact, "!" = decision, "!!" = hard constraint or prohibition, ">" = action, "?" = open question, "~" = estimate/uncertain, "x" = rejected. "+"/"-" = pro/con, only indented under a "?" or "!" line.
- Inline: "->" leads to/then; "=>" if-then rule; "<-" because; "=" is/equals; "|" or; "vs" trade-off; "@" person/date/place; text in quotes = verbatim. "&id" defines an anchor, "*id" reuses it. Indentation (2 spaces) = detail of the parent line. A short unmarked line ending with ":" labels a group.
- Telegraphic style: no articles, no copulas; the marker replaces its own words ("must" -> "!!", "decided to" -> "!", "uncertain" -> "~", "ruled out" -> "x"); dates in ISO (2027-03-31); numbers and units compact (50k EUR); the subject is stated once, not re-opened in every line.
- Negations always explicit ("not", "no", "never", "except"). Numbers, names, dates and quoted text: verbatim, never compressed. If condensing creates ambiguity, keep the full wording.
- Compose directly in TERSE. Never write prose first and then convert.
```

### 8.2 Template — agent memory & status reports

```
When you write memory entries, status reports, handoff notes, or logs, write them natively in TERSE.
{CORE}
Open each document with "CTX: <subject>" and "AS-OF: <date>". Declare any abbreviation in "LEX:". Use "MODE: strict" and mark exhaustively: an unmarked line asserts a confirmed fact — a reader may rely on the absence of "~" or "?".
```

### 8.3 Template — inter-agent messages

```
Messages you send to other agents are written natively in TERSE.
{CORE}
Address agents and people with "@name". State requests as ">" lines (one action each), standing rules as "=>" lines, open points as "?" lines. Put verbatim payloads (ids, code, exact strings) in quotes. Keep a message under ~20 lines; reference shared context with "*id" instead of restating it.
```

### 8.4 Template — terse reasoning drafts (experimental)

```
When asked to show your working, write the visible reasoning as a TERSE draft: one step per line, at most ~8 words per line, markers and operators as defined.
{CORE}
End with a final line: "answer = <final answer>".
```

*Status of 8.4: experimental, pending arm F (§6). Two honest warnings for engineers: visible reasoning tokens feed back into the model's computation — constraining them can change reasoning quality in either direction (Chain-of-Draft-adjacent results are encouraging but task-dependent), so measure on your own tasks before adopting. And a TERSE draft stays human-readable: it preserves the monitorability of the reasoning, which is an advantage over opaque compression and a property worth keeping.*

---

## 9. Tooling roadmap

- **Linter / validator** — shipped as **INTACT** (tools/intact.html): a no-API, in-browser semantic-integrity checker comparing a source and its condensed version (altered values, vanished negations, corrupted identifiers vs legitimate deletions). Checks: unknown line markers; `+`/`-` used outside `?`/`!` scope; dangling `*id` (no matching `&id`) and duplicate `&id`; abbreviations not declared in `LEX`; invalid `MODE` value or mid-document mode change; `L0` present and single-line when levels are used. The linter is also the practical answer to marker-confusion risks: ambiguity gets caught mechanically, the way it is for code, JSON, or Markdown.
- **Converters** (later): prose → TERSE assistant prompt; TERSE → prose renderer for round-trip checks.

---

## 10. Open questions

- A canonical **dense-list / enumeration form** — dogfooding (PROJECT.terse) showed that one-claim-per-line strains against compact enumerations (spec summaries, feature lists).

- **Action marker `>` under observation.** Line-initial `>` (action) coexists with inline `>` (comparison) and with markdown's blockquote habit. Position rules keep it unambiguous for machines (principle 6), but early human readers have stumbled on it. Revisit if the benchmark or linter usage shows real confusion; candidate replacements to be evaluated against the admission tests.
- Long-form aliases `pro:`/`con:` for `+`/`-`: **rejected for now** under principle 7 (one meaning, one form); revisit only with evidence of persistent confusion, and as a replacement rather than a variant.
- An *else / default branch* form for `=>` rules — currently expressed as a second rule with the complementary condition; a dedicated form is deferred until real usage shows the need.
- Logic extension (quantifiers ∀/∃) as an optional module — condensed "all"/"any" currently do the job for fewer tokens.
- Round-tripping: guidelines for prose → TERSE → prose reconstruction fidelity.

---

## 11. Changelog

- **v0.1** — Initial spec (working name GIST): principles 1–5, core markers (`!`, `>`, `?`, `~`, `x`), operators (`->`, `<-`, `=`, `vs`, `@`, quotes), hierarchy, anchors, detail levels, legend, benchmark protocol.
- **v0.2 (proposals)** — Naming collision analysis (GitHub Gist; gisting/gist-tokens literature); `MODE` strict/open; marker admission test; candidates `!!`, scoped `+`/`-`, `|`, `=>`; rejected `¤`, `}`, `#`, line-initial `<`, ∀/∃; ablation-based benchmark.
- **v0.3 (this document, consolidated)** — Name fixed: **TERSE**. `MODE` adopted, immutable per document. Four new markers adopted (`!!`, scoped `+`/`-`, `|`, `=>`). Principles 6 (position disambiguates) and 7 (one meaning, one form) added. Tooling roadmap added (linter). Action marker `>` placed under observation for v0.4.
- **v0.3.1** — Name check completed: TERSE kept, with a disambiguation note (IBM TERSE compression format, 1984; Terse assembler, 1987); candidates TELEX and BREVE rejected — both actively used in the AI space. §3.3: logical-composition mapping (IF/THEN, OR, AND, NOT, CASE/WHEN), grouping parentheses for compound conditions, `&`-is-never-"and" note. New open question: else/default branch.
- **v0.4** — Scope made explicit: primary targets (system prompts, agent instructions/memories, inter-agent messages) and user prompts as a non-goal. Legend cost corrected to the measured 224 tokens. §6: pilot results recorded (core −26%/−43% at 0 accuracy loss; full-notation overhead at small sizes; FR/EN gap 58%→21%), display policy (trade-off as headline, threshold as footnote), prospective arm F (terse reasoning drafts). New §7: corpus authoring pipeline with the CONVERT / AUDIT / QUESTIONS prompts (identical to those embedded in TERSE Bench v0.4). Open question added: dense-list form.
- **v0.4.1** — CONVERT prompt rewritten as fully self-contained (writer-grade syntax reference, worked example, no dependency on the legend or any attachment), after field feedback that the legend-based version under-specified writing. Design note added to §7: the legend is reader-grade (understanding), the full reference is writer-grade (producing); prompt length is a one-off authoring cost. Bench updated to v0.4.1 with the same prompt.
- **v0.5** — Field finding recorded in §6: third-party conversions of a 23-doc bilingual corpus applied markers but kept full sentences → TERSE at 103% of prose size; markers alone are net-negative, all compression comes from condensation; under-condensed corpus retained as arm B0 (markup-only). CONVERT prompt rebuilt around a "condensation technique" core: anti-pattern examples, rules C1–C10 (marker replaces its words, nominalization, ISO dates, compact units, no subject repetition, group labels), quantified size target (50–65%, alarm at 75%) enforced in the self-check. §3.7 expanded to match; §3.4 gains the group-label form (short unmarked line ending with `:`). Companion REPAIR prompt published for fixing existing under-condensed conversions. Bench updated to v0.5.
- **v0.6** — New §8, "Native generation (system prompts)": zero-detour rule (never prose-then-convert at inference), common core block, and three engineer-ready templates — agent memory/status (strict mode), inter-agent messages, and experimental terse reasoning drafts with explicit warnings (reasoning tokens feed back into computation; drafts stay human-readable, preserving monitorability). Sections renumbered (Tooling §9, Open questions §10, Changelog §11). Bench v0.6: question count selector (5/10/15/20/all) with per-document random sampling without replacement, one draw shared by all arms of a run.
- **v0.7** — Run 1 recorded in §6 (full EN corpus, Sonnet 4.6: −33% tokens, −3.0 pts; paired failure taxonomy). §3.7 gains the char→token calibration (≈0.8×) and rule 9 "protected precision" (explicit comparatives, threshold qualifiers, document self-description). Bench v0.7: judge accepts answers that contain the gold plus correct additional detail.
- **v0.8** — Run 2 recorded in §6: FR 19 docs × 20 Q at −39% tokens / −1.6 pts (within the accuracy criterion); EN re-run confirms instrument determinism and reveals question-sampling variance (publication runs use all questions). §6 arms extended: arm S ("short" — condensation without markers, completing the 2×2 factorial A/B0/S/B) and external baseline LLMLingua-2 at matched ratio, plus exploratory LLMLingua-over-TERSE with a mandatory negation/marker integrity check. Companion SHORT prompt and LLMLingua Colab script published.
- **v0.9** — Run 3 final consolidated results recorded (five arms, 46 docs): condensation carries the value; marker layer repositioned as optional machine-readable structure; LLMLingua-2 baseline loses 6.3 pts at matched budget with documented silent corruptions; combo collapses. INTACT integrity linter shipped as companion tool.
- **v0.10** — Reliability-first positioning formalized (§1). Run 5 recorded: structural-retrieval cross-family replication (GPT reader, manual isolated-conversation protocol) — TERSE 96.4% vs short 92.9% vs prose 98.2% on 112 audited gold items; Q1 marker signal replicated across model families. Roadmap: reliability markers (list exhaustiveness, mandatory provenance in strict mode, INTACT-verified critical values).
- **v0.11** — Run 6 recorded: equal-budget deployment test — at a window sized to full TERSE, truncated prose answers 56.5% overall vs 87–89% for the condensed formats; beyond its cut, prose answers honestly "Not in context" (zero confabulation) while short/TERSE answer 95–100%. Within-window nuance reported (96.2% vs 80.8%, small sample).
- **v0.12** — Run 7 recorded: canonical paired run (all questions, three arms, one draw per document) supersedes the patchwork EN baselines; short and TERSE statistically indistinguishable on QA (FR: 6 paired flips each way); positioning updated with operational-context guidance. Bench export labels fixed (bench v0.11). Roadmap label: "v2 — spatial context & semantic LOD".
