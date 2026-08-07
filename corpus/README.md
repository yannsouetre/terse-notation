# Corpus

23 documents per language (EN, FR), each in five versions, with 542 questions per language and their gold answers.

| File | Documents | Questions | Size |
|---|---|---|---|
| `corpus-EN.json` | 23 (`EN-T01` … `EN-T23`) | 542 | 405 KB |
| `corpus-FR.json` | 23 (`FR-T01` … `FR-T23`) | 542 | 443 KB |

The FR documents are translations of the EN prose, re-converted independently — never translated from the TERSE version (`SPEC.md` §7, step 6). Document ids are aligned across languages: `EN-T07` and `FR-T07` are the same document.

## Schema

Flat, one entry per document. This is the schema `bench/terse-bench.html` v0.11 expects; it also accepts the legacy one-document-per-variant form with `-short` / `-llml` / `-llmlx` id suffixes.

```json
{
  "docs": [
    {
      "id": "EN-T01",
      "lang": "EN",
      "title": "PROJECT SCOPING NOTE",
      "prose": "…",
      "short": "…",
      "terse": "…",
      "llml":  "…",
      "llmlx": "…",
      "questions": [ { "q": "…", "a": "…" } ]
    }
  ]
}
```

## The five versions

| Field | Benchmark arm | What it is | Produced by |
|---|---|---|---|
| `prose` | A — baseline | The source document. Realistic business prose: scoping notes, incident reports, runbooks, meeting minutes, agent memories. | Authored first; everything else derives from it. |
| `short` | S | Telegraphic condensation with **no notation** — plain modality words ("decision:", "must", "rejected:"), no symbols. | [`prompts/SHORT.md`](../prompts/SHORT.md) |
| `terse` | B — full notation | The same condensation **plus** the marker layer. | [`prompts/CONVERT.md`](../prompts/CONVERT.md), audited with [`prompts/AUDIT.md`](../prompts/AUDIT.md) |
| `llml` | external baseline | LLMLingua-2 applied to the prose at a compression rate matched to the TERSE/prose ratio. | [`tools/llmlingua_colab.py`](../tools/llmlingua_colab.py) |
| `llmlx` | exploratory | LLMLingua-2 applied **over** the TERSE version. Collapses (−12.3 pts); kept because negative results are results. | idem |

Measured size, as a share of the source's characters (mean over 23 documents):

| | `short` | `terse` | `llml` | `llmlx` |
|---|---|---|---|---|
| EN | 59% | 60% | 68% | 48% |
| FR | 57% | 58% | 64% | 45% |

Characters are not tokens: the char→token discount is ≈0.8× (`SPEC.md` §3.7.8), which is why a 60% character ratio shows up as −33% tokens rather than −40%. Every figure published in the README is a **real token count returned by the API**, never a character estimate.

## Questions

Written from the **prose only**, never from the TERSE version — otherwise the notation would be taught to the test (`SPEC.md` §7, step 4). Generated with [`prompts/QUESTIONS.md`](../prompts/QUESTIONS.md) and reviewed by hand.

Most documents carry 20 questions; a few carry 30 or 32. Each set mixes factual lookups with at least one negation or rejected option, at least one conditional rule where the document has one, and **exactly one trap question** whose gold answer is "not in context" — a hallucination probe. A reader that answers the trap confidently is penalised, in every arm equally.

## Reusing this corpus

It is CC-BY 4.0: use it freely with attribution. Two honest caveats before you do.

Most documents are **synthetic-realistic** — written for this study, in part by the notation's designer. That is a real bias: the prose may be more regular, and more condensable, than documents found in the wild. A replication on third-party or genuinely real (anonymized) documents is the single most useful contribution this project could receive.

Two documents, `T12` and `T13`, are the exception: they are **genuine user prompts**, kept because real requests have a messiness synthetic prose does not imitate — first-person phrasing, references to an earlier exchange, half-specified requirements. They were lightly sanitized before publication: a live private link in `T12` now reads `https://example.com/stafffor2345643`. The substitution preserves the original's exact length and structure, and was applied identically in the corpus, the raw results and the benchmark files, so the token measurements and the two gold answers that quote the URL (one per language) stay coherent. It is the only content edit in this repository.

The `terse` versions were produced by a model and audited by a model. They are *valid* TERSE, not necessarily *optimal* TERSE — a human expert would likely compress further.
