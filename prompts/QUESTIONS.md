# QUESTIONS prompt

Writes the QA set for a corpus document.

**Usage.** Replace `{PROSE}` and `{N}`. **Run it on the prose only, never on the TERSE version** — otherwise the notation gets taught to the test. Step 4 of the corpus pipeline (SPEC §7).

Canonical source: [`SPEC.md`](../SPEC.md) §7. This file is a verbatim extract kept in sync with it; the TERSE Bench "Corpus builder" embeds the same text.

---

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
