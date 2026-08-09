# CONVERT-LOD — self-contained conversion prompt (v0.1)

*Paste this whole prompt into any capable model, followed by ONE source document. It produces
the sub-addressed MAP+L1 form defined in TERSE-SPATIAL-DRAFT (grammar A1-A3, rules R1-R4).
Output language: English.*

---

You will convert the source document below into a **spatially addressed TERSE structure**:
a document-level map entry, a set of REGION map lines, and one L1 block per region.

## 1. Segment into regions
Identify 4–8 functional regions (scope, triggers, procedure steps, decisions, constraints,
communications, open questions...). Each region gets an address: `&<doc>/<slug>` where
`<doc>` is the document id given to you (e.g. `t03`) and `<slug>` is a short lowercase
hyphenated name (`triggers`, `rerun`, `comms`). Addresses are permanent: choose names that
survive edits.

## 2. Write the MAP block (L0)
First line: the document itself — `&<doc> [!!] <title> — <one-line gist> [<n> hard rules]`.
Then one line per region — `&<doc>/<slug> [marker] <gist, max ~12 words>`.
The line's marker is the strongest marker present in that region's content: `!!` if it
contains any hard constraint, else `!` if it contains decisions/rules, else nothing.
**Rule R2 (mandatory): every `!!` that exists anywhere in the document must be visible at
L0 — on its region's line AND flagged on the document line.** A hard constraint that hides
in detail is a defect.

## 3. Write one L1 block per region
Header: `[L1 &<doc>/<slug>]`. Content: TERSE lines (telegraphic, one fact/rule per line):
- `!!` hard constraint (never weaken, never drop; keep numbers, thresholds, IDs **verbatim
  in quotes**: `"10 MB"`, `"06:30"`, `"P1"`)
- `!` decision or rule · `x` rejected/excluded (keep the reason) · `?` open question ·
  `>` action/step · bare line = fact
- Operators: `->` leads to/then · `=>` if-then · `<-` source/because · `|` or · `vs` versus
- **Never delete negations** ("do not", "never", "except"), quantifiers ("only", "at most"),
  or qualifiers that change meaning.
- Cross-references: when a region's content depends on or points to another region (or
  another document), write `-> *<doc>/<slug>` (or `<- *...` for provenance). These arrows ARE
  the topology later used by FOCUS(address, radius).

## 4. Integrity self-check before answering (rules R1-R4)
- R1: nothing in an L1 block contradicts its map line.
- R2: every `!!` surfaces at L0 (region line + document line).
- R3: every region in the MAP has exactly one L1 block, and every `*` reference points to an
  address that exists in your output (or is explicitly external).
- R4: superseded content is kept but marked `x superseded -> *<new address>`.

## 5. Output format (exactly this, no commentary)
```
# MAP
&<doc> ...
&<doc>/<slug-1> ...
...

[L1 &<doc>/<slug-1>]
...

[L1 &<doc>/<slug-2>]
...
```

## Worked micro-example (payroll runbook, excerpt)
```
# MAP
&t03 !! Monthly payroll export runbook — failure triage & rerun rules [6 hard rules]
&t03/scope x simulations · x individual adjustments
&t03/triggers ! 3 failure triggers @ "06:30" check
&t03/rerun !! max "1" manual rerun => else P1

[L1 &t03/rerun]
!! max "1" manual rerun
rerun SUCCESS + file >"10 MB" -> resume normal processing
rerun FAILED | file <"10 MB" -> open "P1" @Payroll-Engineering -> inform payroll manager
delete only incomplete output · keep logs
<- *t03/triggers
```

SOURCE DOCUMENT (id: `<doc-id>`):
<<<
[paste the document here]
>>>
