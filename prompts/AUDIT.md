# AUDIT prompt

Checks a prose→TERSE conversion for information equivalence and returns machine-readable JSON.

**Usage.** Replace `{PROSE}` and `{TERSE}`. Ideally run on a model from a different family than the converter. Fix and re-audit until `"ok": true`. Step 3 of the corpus pipeline (SPEC §7).

Canonical source: [`SPEC.md`](../SPEC.md) §7. This file is a verbatim extract kept in sync with it; the TERSE Bench "Corpus builder" embeds the same text.

---

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
