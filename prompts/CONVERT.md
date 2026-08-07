# CONVERT prompt

Turns a prose document into valid TERSE. Self-contained: it embeds the full writer-grade syntax reference and a worked example, and depends on no attachment.

**Usage.** Replace `{PROSE}` with your source document. Run it in any chat or via API. Step 2 of the corpus pipeline (SPEC §7).

Canonical source: [`SPEC.md`](../SPEC.md) §7. This file is a verbatim extract kept in sync with it; the TERSE Bench "Corpus builder" embeds the same text.

---

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
