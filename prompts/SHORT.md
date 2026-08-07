# SHORT PROMPT — condensation WITHOUT the TERSE marker system (arm S)
# Purpose: produce the "short" version of each document — same telegraphic
# condensation as TERSE, but NO notation: no line markers, no symbolic operators,
# no anchors, no detail levels. This isolates what the marker system itself
# contributes. Paste everything below the line into any AI, then paste one
# prose document at a time.
# ------------------------------------------------------------------------------

You condense prose documents into SHORT form: telegraphic, line-based notes that keep every fact while removing grammatical filler. SHORT uses NO special notation — no symbols, no markers, no tags. It reads like extremely compact human notes.

=== WHAT SHORT LOOKS LIKE ===
- One fact per line. Plain section headings are allowed (e.g. "Planning").
- Modality is expressed with ordinary words, briefly: "decision:", "must", "must not", "estimate:", "rejected:", "open question:".
- No TERSE symbols: do not use line-initial "!", "!!", ">", "?", "~", "x", "+", "-"; do not use "->", "=>", "<-", "|" as operators; no "&id"/"*id"; no L0/L1/L2. Normal punctuation only. ("=", ">", "<" may appear only in their ordinary mathematical sense, e.g. "budget 60k EUR", "latency under 15 ms".)

EXAMPLE
SOURCE: Following our meeting on July 10th, the team decided to migrate the customer database to PostgreSQL rather than staying on MySQL, mainly because of better JSON support and the fact that our lead developer Sarah already has deep experience with it. MongoDB was also considered but was ruled out due to the lack of relational joins. The migration is estimated to take about three weeks, although this remains uncertain. Sarah will prepare a detailed migration plan by August 1st. One question is still open: should we host in the EU region or in the US, given GDPR constraints?

SHORT:
Customer DB migration, 2026-07-10.
Decision: migrate customer DB to PostgreSQL, was MySQL. Reasons: better JSON support; Sarah deep experience.
Rejected: MongoDB, no relational joins.
Estimate: migration about 3 weeks, uncertain.
Action: Sarah, migration plan, due 2026-08-01.
Open question: hosting EU or US, GDPR.

=== CONDENSATION RULES (apply to EVERY line) ===
Write like a telegram: every character costs.
C1. Delete articles, possessives, demonstratives (the/a/an/this; le/la/les/un/une/ce/cette...).
C2. Delete copulas and light verbs. "The project sponsor is Claire Renaud" -> "Sponsor: Claire Renaud".
C3. Compress modality phrases to their short word: "the team has decided to" -> "Decision:"; "it is mandatory that" -> "must"; "it is estimated that / this remains uncertain" -> "Estimate: ... uncertain"; "was considered but ruled out" -> "Rejected:".
C4. Nominalize verbs: "The vendor will end support on March 31, 2027" -> "Vendor support ends 2027-03-31".
C5. Dates in ISO (2027-03-31; "Feb 12 at 6 pm" -> 2027-02-12 18:00). Numbers and units compact (50 000 euros -> 50k EUR; nine years -> 9 years).
C6. State the document's subject once at the top; never re-open lines with it.
C7. Replace section sentences with a short plain heading on its own line.
C8. Merge trivially related micro-facts on one line with ";" or ","; split any line carrying two unrelated claims.
C9. Size target: the SHORT body should land around 50-65% of the source's characters. Above 75% means the lines are still sentences - redo the pass.

PROTECTED (never compressed away): numbers, units, names, dates, quoted text (verbatim) - and negations ("not", "no", "never", "except", "aucun", "sauf"): always explicit. Comparatives keep an explicit direction word ("C cheaper than B by 6%"). Qualifiers gating a threshold or a legal condition ("strictly", "written and motivated") are kept. The document's self-description (type, sector, audience) is preserved as explicit lines near the top. Content words stay in the source language. Add nothing absent from the source; lose nothing present in it; keep open questions open and uncertainties uncertain.

=== SELF-CHECK (mandatory before answering) ===
(1) every fact, number, name and date of the source is present; (2) every negation and uncertainty preserved; (3) NO TERSE symbol anywhere - plain words only; (4) body at or under ~65% of the source's characters (above 75%: redo).

OUTPUT: only the final SHORT document. No commentary, no code fences.
