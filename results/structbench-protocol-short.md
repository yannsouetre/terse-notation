# StructBench protocol — payload sent to the reader (format: SHORT)

Everything below the separator is the **exact, unedited payload** submitted to the reader for the
SHORT arm of the cross-family run: the instructions, the extraction queries, and the 23 English
corpus documents concatenated in SHORT form. Nothing has been added, removed or reworded.

**How the run was executed.** One fresh, dedicated conversation per format — never two formats in
the same conversation, so the reader cannot carry over knowledge from another arm. This file was
submitted, the complete answer captured verbatim (see `structbench-GPT-answers-short.txt`),
and grading done centrally afterwards against the audited gold lists. **The gold lists were never
shown to the reader.**

*Two notes on the payload, kept as-is rather than corrected.* Its opening line says "12 extraction
queries"; the file actually contains **10 queries in 11 prompts** — Q4 is split into Q4a and Q4b by
scope. The count in the instruction was never updated, and it was identical for all three arms, so
it cannot favour one over another. The URL in document T12 was replaced with an `example.com`
address before publication (see the README's limits section); it was the only edit made to these
files.

---------------------------------------------------------------------------

You will answer 12 extraction queries strictly from the corpus below (23 documents, separated by === id === headers). Answer from the corpus only — nothing from outside it, no guessing.

FORMAT OF YOUR ANSWER — for each query, output exactly:
=== Q1 ===
- one item per line, telegraphic, each item citing its document id in [brackets]
(and so on through Q10; Q4 is split into Q4a and Q4b). A single-fact query gets a single line. No introductions, no commentary, no conclusions — only the labeled lists.

THE 12 QUERIES:
Q1 (EN-T01..T05): List every settled decision recorded in documents EN-T01 to EN-T05. A settled decision is a choice the document states as already made or validated — not a recommendation, not a pending option. Cite the document id for each.
Q2 (EN-T04): List all hard constraints and prohibitions stated in document EN-T04.
Q3 (EN-T03): List every conditional rule (a trigger and its consequence) in document EN-T03, including the rules that define when the runbook itself applies.
Q4a (EN-T01..T04): List everything documents EN-T01 to EN-T04 explicitly reject: options ruled out, hypotheses dismissed, items excluded from scope, actions declared unacceptable, or choices explicitly not retained. Cite the document id for each.
Q4b (EN-T05..T08): List everything documents EN-T05 to EN-T08 explicitly reject: options ruled out, hypotheses dismissed, items excluded from scope, actions declared unacceptable, or choices explicitly not retained. Cite the document id for each.
Q5 (whole corpus): List every point the corpus records as explicitly open or pending: undecided choices, decisions deferred to later, or questions asked for advice. Cite the document id for each.
Q6 (EN-T01..T03): List every action or obligation with an explicit deadline or scheduled time in documents EN-T01 to EN-T03 (owner if given, and the date or time).
Q7 (EN-T03): In the payroll runbook (EN-T03), how many manual reruns are allowed at most?
Q8 (EN-T03..T04): List everything that must never be done according to documents EN-T03 and EN-T04, whether stated unconditionally or as a standing rule.
Q9 (EN-T01..T10): Which documents among EN-T01 to EN-T10 explicitly reject at least one thing — an option ruled out, a hypothesis dismissed, a scope exclusion, or an action declared unacceptable? Give the document ids.
Q10 (EN-T01..T05): List every date in February 2027 that appears as a deadline or milestone in documents EN-T01 to EN-T05, with what it corresponds to.

=== CORPUS (SHORT) ===
=== EN-T01 ===
sales CRM migration ClientBase to NovaCRM.
Context:
ClientBase used 9 years (sales dept): opportunities, contacts, sales forecasts.
publisher support ends (current version): 2027-03-31.
Decision: migration to NovaCRM before deadline.
scope: 420 users (France, Belgium, Spain); customer data, open opportunities, activity histories 3 years, standard sales dashboards.
Excluded: old attachments, marketing campaigns, data more than 3 years (not migrated).
read-only archive, accessible 2 years.
Objective:
Decision: NovaCRM production: 2027-02-15 because 6-week safety period before support end.
Constraint: 4 success criteria: at least 99.5% active customer accounts correctly migrated; no open opportunity lost; 90% users trained before launch; opportunity creation/update possible from 1st business day after go-live.
Governance:
sponsor: Claire Renaud (Sales Director Europe).
project manager: Malik Ben Amar (IT Department).
1 business referent / country: data validation, local rules.
If impact more than 50k EUR or delay more than 2 weeks, steering committee decision.
other trade-offs: project manager, after consultation relevant business referent.
Timeline:
Action: data cleansing complete, 2026-09-30.
dry run migration #1: 2026-10-20; #2: 2026-12-08.
UAT: 2027-01-05 to 2027-01-23.
ClientBase structural-change freeze from 2027-02-01; opportunity creation/modification allowed until 2027-02-12 18:00.
final migration after 18:00; then NovaCRM opens 2027-02-15 08:00.
Attention:
risk #1: customer-account duplicates.
script detects probable duplicates.
Constraint: If doubt on duplicate, no automatic merge; decision: country business referent.
risk #2: billing-tool interfaces (replacement out of scope).
Action: temporary interface maintained 6 months after go-live.
Constraint: no specific functionality before launch, except essential regulatory requirement or business continuity.
convenience or enhancement requests to post-launch backlog.

---

=== EN-T02 ===
Incident Committee — Delivery Delays at the North Warehouse.
Date: 2026-10-06.
Meeting:
45 min; subject: shipment stabilization after 3 days delays.
participants: Operations, Transport, IT, Customer Service, Logistics Management.
Situation:
North warehouse store-order delays since Monday.
08:00: 1,840 pending versus about 300 normal.
Excluded: main cause: warehouse-management-system breakdown; software normal.
cause: Monday picking reorganization: high-turnover products moved; routes not recalculated.
average picking: 18 to 27 min.
FastRoad issue: orders not ready usual time; then several trucks partly loaded Monday/Tuesday.
Decisions:
Decision: new physical layout maintained; rejected: previous organization return.
Action: IT recalculate routes before Thursday 14:00.
Action: test: 12 pickers, 4 h.
If test at most 20 min and no blocking anomaly, activate all warehouse next shift.
If test more than 20 min, postpone; temporarily old route logic; no physical relocation.
Action: 15 additional temporary workers Thursday/Friday evenings.
Excluded: extra Saturday work at this stage.
Action: FastRoad adds 2 rotations Thursday evening; 3 Friday.
Communication:
Constraint: no preemptive contact all stores.
Action: only stores likely more than 24 h delay.
If urgent store opening or critical stockout, regional manager may request priority; send Operations before 16:00.
Action: status Thursday 17:00; Friday 12:00.
Follow-up:
objective: less than 500 pending Friday 18:00.
If more than 800 pending Friday 12:00, Logistics Director decides by 14:00 possible exceptional Saturday opening.

---

=== EN-T03 ===
Handling a Payroll File Generation Failure.
Scope:
monthly payroll-file failure, PayrollFlow; normal monthly processing only.
Excluded: payroll simulations; individual adjustments.
Trigger:
Constraint: if: no `/export/payroll` file 06:30 scheduled day or file less than 10 MB or auto check `FAILED`
If `WARNING` alone not equal to trigger, operator consult report/follow instructions.
1 verification:
Action: verify scheduler `PAY_MONTHLY_EXPORT` started.
If running less than 90 min, requirement: no restart; wait completion or more than 90 min.
If running more than 90 min, action: stop; open P2.
If SUCCESS and file missing/too small, action: step 2.
2 inputs:
Action: verify `employees.csv`, `variables.csv`, `absences.csv`
Constraint: never manually modify in production.
If missing, action: contact owner team; suspend.
If all present, compare modification date; previous day/earlier: suspicious.
3 rerun:
Constraint: max 1 manual rerun.
Action: delete only incomplete output.
Constraint: keep logs.
Action: wait auto check.
If SUCCESS and file more than 10 MB, normal payroll.
If FAILED or file less than 10 MB, action: P1 Payroll Engineering.
4 communication:
Action: inform payroll manager when P1 opens.
Constraint: no direct all-employee information.
If no correct generation before 10:00, payroll manager and HR decide employee delay-risk communication.
Constraint: log every manual action in incident ticket.

---

=== EN-T04 ===
Agent "MeetingPilot" — Persistent Memory and Action Rules.
Identity:
MeetingPilot: prepare/follow Atlas product committee.
Context:
committee: Tuesdays 09:30, 45 min.
head: Sophie Delmas; arbitrates product-priority conflicts.
usual: Sophie, 3 Product Managers, Data manager, customer-support representative.
reference: "Atlas Weekly Decisions"; validated decisions only.
Constraint: discussion ideas stay meeting notes, not reference.
Before:
Action: day before: open decisions from last 2 minutes.
Action: max 5 topics; priority: 1 customer incidents; 2 decisions blocking delivery within 2 weeks; 3 budget arbitration; 4 others.
Constraint: age alone never auto-adds topic.
Action: each: expected decision-maker, deadline, known options, no-decision consequence.
If missing, "to be clarified"; requirement: do not invent.
Validation/after:
valid only if Sophie explicitly confirms or minutes say consensus approved in her presence.
"this seems to be the best option" not equal to valid decision.
Action: update "Atlas Weekly Decisions" with validated decisions.
Action: record date, execution owner, deadline.
Action: undecided proposals stay notes.
If deadline at most 14 days, action: follow-up action.
Constraint: never retroactively modify old decision.
If changed, action: new entry referencing previous.
Prudence:
Constraint: never external message on own initiative.
draft allowed; sending requires explicit human request.

---

=== EN-T05 ===
Renewal of the Intervention Vehicle Fleet.
Decision:
choose renewal scenario for 60 intervention vehicles, contracts ending 2027-01 to 2027-06.
3 options studied.
Option A — identical diesel:
benefit: lowest acquisition cost; no site adaptation.
drawback: does not meet internal emissions-reduction trajectory.
risk: increasing traffic restrictions in several urban areas.
Option B — full electric:
benefit: best use-phase emissions reduction.
constraint: 18/60 vehicles regularly more than 280 km rounds where fast charging insufficient.
constraint: immediate 42 charging stations across 11 sites; 3 sites insufficient electrical power.
Option C — mixed fleet:
42 electric and 18 plug-in hybrids.
hybrids priority: long rounds.
benefit: significant emissions reduction without waiting electrical upgrade of 3 constrained sites.
Estimate: 4-year total cost: 8% higher than A; 6% lower than B.
Recommendation:
Decision: choose option C.
Constraint: decision before 09-15 because secure delivery times.
Constraint: 42 stations not all installed immediately.
Action: wave 1: 29 before 2027-03.
Action: remaining 13 after reinforcement of concerned sites.
Action: review: 2028 fourth quarter.
If sufficient progress in real-world electric-vehicle range, charging network, site capacities, estimate: early replacement of 18 hybrids may be studied.

---

=== EN-T06 ===
Project ARGOS — Internal Document Search AI Assistant.
Purpose:
ARGOS: conversational assistant for 3,200 group employees: search, summarize, compare internal documentation.
observation: significant time finding procedures, templates, reference notes, past decisions across intranet, SharePoint, business document spaces; current search engines return file lists, do not distinguish applicable versus obsolete.
Constraint: ARGOS not autonomous decision system; function: access/understand information.
Constraint: legal, financial, HR, security decisions remain identified-human responsibility.
V1 scope:
corpuses: intranet internal procedures; Quality document database; formal steering-committee decisions since 2023-01; legal-validated contract templates.
Excluded: personal OneDrive, mailboxes, Teams conversations, unpublished project folders.
Constraint: responses: French and English.
If document-derived response, requirement: at least 1 identifiable source.
If contradictory documents, requirement: signal contradiction, no silent plausibility choice; when possible prioritize highest formal status or most recent validity date.
procedure hierarchy: group policy ranks above group procedure, local procedure, practical guide, unclassified document.
Constraint: explicit expiration overrides hierarchy; expired group policy not presented applicable solely due higher rank.
Security:
Constraint: apply user access rights at each request; never expose, even summary, inaccessible-document information.
Excluded: rights copied into independent manually maintained database.
Constraint: permissions queried/synchronized from source repositories via cybersecurity-validated method.
technical logs may retain user ID, time, engine-consulted documents, processing duration.
default full user-question retention at most 30 days.
incorrect-response reports retained 12 months for error analysis.
Constraint: no ARGOS content for external-model retraining without explicit data-governance-committee authorization.
Assistant behavior:
Constraint: clearly distinguish source facts, model summaries, uncertainties.
If insufficient support, explicitly state; rejected: fill with unverified general knowledge.
If request "which procedure should I follow?", first check applicable procedure; several found; if so, explain respective scope.
Constraint: never invent procedure number, date, responsible person, internal rule.
If human-validation-required action, may prepare elements; requirement: never pretend validation occurred.
Pilot:
200 users, 8 weeks.
indicators: relevance at least 85% useful/very useful; traceability at least 98% document-information responses with actionable reference; security: 0 confirmed unauthorized-document exposure; performance: 95% begin display less than 8 s (start, not full generation).
adoption rate observed; not blocking criterion for general production.
Governance:
sponsor: Director of Digital Transformation.
IT: architecture, integration, technical operation.
Knowledge Management: document quality, content-lifecycle rules.
Cybersecurity: authorization model, logging mechanisms, penetration tests validation.
legal: contract-template terms of use, associated warnings validation.
ARGOS governance committee: every 2 weeks during pilot.
If modify source scope or retention rule or new user-data use or identified information-exposure risk, requirement: committee submission.
purely ergonomic choices: Product Owner within approved budget.
Phasing:
Phase 1 document preparation, until 2026-11-30: source inventory, owners, delete/mark most critical obsolete content.
Constraint: objective not full document-estate cleanup before pilot; unrealistic.
Phase 2 construction, 2026-12 to 2027-02: indexing engine, rights management, interface, citation system.
Phase 3 internal testing, 2027-03: functional, security, response quality, rights-bypass resistance.
Constraint: no real data from out-of-scope personal spaces for testing.
Phase 4 pilot, 2027-04 to 2027-05: 200 users.
Phase 5 rollout decision, 2027-06: committee chooses rollout or extend pilot or suspend project.
General go-live:
Constraint: not automatic after pilot.
Constraint: requires: no unresolved critical security incident; operational rapid removal of erroneous/confidential indexed document; identified owner per corpus; user-support procedure.
relevance target: 85%; slightly lower does not mechanically block rollout if committee judges gaps understood/correctable.
If confirmed unauthorized-document exposure, immediate security analysis; severity may suspend pilot before next committee.
Out of scope/future:
Excluded: V1 automatic actions in business systems; source-document modification; contract validation; HR decisions.
Estimate: later phase may study agent functions: prepare workflows, create drafts, execute some reversible operations; distinct security scoping required.

---

=== EN-T07 ===
HORIZON Program — Decarbonization of the Valmont Industrial Site.
Date: 2026-09-17.
Meeting:
subject: 2027-2030 energy-trajectory trade-offs.
participants: Industrial Management, Finance, Energy, Maintenance, Procurement, HSE, Site Management, Program Team.
Objective:
Constraint: direct CO₂ reduction at least 40% between 2024 reference and end-2030.
Excluded: production reduction as lever.
gains: efficiency improvements or technological changes or energy substitution.
workstreams: A furnace heat recovery; B electrification 2 drying lines; C gas-boiler replacement; D utilities optimization/loss reduction.
A — heat recovery:
study confirms recovery of flue-gas heat from furnaces 2 and 3 to preheat combustion air.
Estimate: investment: 4.8M EUR; expected gain: 7,200 t CO₂/year at nominal capacity.
shutdowns: furnace 3 10 days; furnace 2 6 days.
If main orders before 2026-12-15, shutdowns integrable into major maintenance 2027-08.
Decision: launch calls for tenders.
Excluded: final investment validation now; action: submit investment committee when firm offers available.
B — drying-line electrification:
S1,S2 currently gas.
both electrified: significant direct-emission reduction; internal-network power insufficient for simultaneous full-capacity S1 and S2.
scenarios: S1 only in 2027 or S1 and S2 with new electrical substation or defer until public-network reinforcement planned, not guaranteed, from 2029.
Estimate: new substation: about 6.5M EUR and drying equipment; Finance: full scenario difficult within current budget.
Action: Industrial Director asks pursue S1-only; preserve design option for later S2.
Decision: direction validated as working assumption.
Excluded: investment decision made.
C — gas boiler:
Constraint: G4 replacement before 2029 because aging.
studies: high-efficiency gas or electric or biomass.
electric: greatest direct-emission reduction; worsens B power constraint.
biomass: better existing-grid compatibility; requires storage, more truck traffic, enhanced dust treatment.
Action: supplementary biomass analysis: regional fuel availability, price stability, traffic impact, non-CO₂ atmospheric emissions, operational constraints.
Excluded: technology selected at this stage.
D — utilities:
actions: compressed-air leak detection, insulation improvement, optimized pump management, non-production-consumption reduction.
result of initial actions: utilities electricity 6% lower versus 2024 average, production-volume corrected.
Constraint: do not count as direct CO₂ reduction when electricity outside site direct-emission scope.
Action: track as energy gain and indirect-emission contribution.
Budget:
reserved envelope: 18M EUR, 2027-2030.
Constraint: envelope not equal to automatic spending authorization.
If investment more than 2M EUR, investment-committee approval.
already-approved studies remain authorized within budgets.
If ambitious-scenario estimates clearly more than 18M, sequence projects or seek additional funding.
Action: Finance identify available support mechanisms by end-2026-11.
Constraint: subsidies not recorded acquired before formal notification.
CO₂ trajectory:
current most-realistic scenario: furnace heat recovery and S1 electrification and G4 replacement to be determined and continued efficiency actions.
Estimate: preliminary direct-emission reduction: 31-37%, depending G4 technology.
Constraint: does not yet ensure 40% objective.
Action: identify at least 2 additional levers before 2027-01.
possible: process changes, new energy substitutions, accelerate exploratory projects.
Excluded: carbon certificates counted toward site direct-reduction objective.
Risks:
critical: electrical capacity (conditions projects, may require unplanned investment); industrial availability (shutdowns uncoordinated with maintenance cause significant production losses); cost inflation (estimates more than 6 months old, update required).
Estimate: biomass availability: to qualify before critical/noncritical classification.
Decisions/actions:
Decision: calls for tenders heat recovery; S1-only design basis; supplementary biomass study; maintain 40% objective without carbon certificates in direct-objective calculation.
Action: Procurement calls for tenders A before 2026-10-01.
Action: Energy biomass study before 2026-11-20.
Action: Finance available aid before 2026-11-30.
Action: Program propose 2 additional CO₂ levers before 2027-01-15.
Action: Maintenance confirm A shutdown compatibility with 2027 schedule before 2026-10-15.
next committee: 2026-12-03.

---

=== EN-T08 ===
Response to a Suspicion of Ransomware on a Workstation.
Purpose:
company-workstation ransomware-consistent signs.
priority: limit propagation and preserve evidence; rapid recovery secondary.
Constraint: user/support must not "repair" before security-team evaluation.
Triggers:
Constraint: trigger if at least 1: sudden unusual unreadable file extensions; ransom-demand message; apparent rapid encryption multiple folders; EDR "ransomware confirmed"; similar simultaneous encryption multiple network shares from same workstation.
If simple slowness or blue screen or isolated file corruption alone, rejected: trigger.
If serious doubt, support may contact SOC for qualification without immediate confirmed-ransomware declaration.
Immediate isolation:
Action: If Ethernet connected, unplug cable.
Action: If Wi-Fi active, disable if immediate without extensive system navigation.
Constraint: default: do not power off; do not close apps; do not delete files; do not launch manual antivirus/cleanup.
objective: cut communications while preserving state.
If exception: active encryption and network isolation not quickly achievable, SOC may explicitly request forced shutdown.
decision: SOC or on-call security officer; except physical danger requiring immediate action.
Incident opening:
Constraint: initial P1 if ransom message visible or EDR confirms ransomware or several machines affected or server/critical share hit.
If single-workstation suspicious signal without confirmation, P2 pending SOC qualification.
Constraint: ticket: user name, workstation name, approximate first-symptom time, symptom description, isolation status, possible ransom message, available screenshots without extra manipulation.
Constraint: never ask user to reconnect workstation to retrieve missing information.
Propagation search:
Action: SOC searches recent user-account connections, similar alerts, unusual network-share access, massive file creation/renaming, suspicious external-infrastructure connections.
If at least 2 workstations with consistent signs within 30 min, requirement: treat potentially propagated even common origin unconfirmed.
security manager may order broader containment: account block, temporary share disablement, segmentation, technical-indicator block.
Constraint: site-wide network shutdown never automatic; requires security manager or cyber crisis director.
User accounts:
If probable credential compromise or malicious execution using account or abnormal connections incompatible with user activity, requirement: reset concerned-user password.
encrypted files alone not equal to automatic immediate reset absent account-compromise indicator.
If reset decided, action: revoke sessions when platform allows.
If admin privileges, increased analysis criticality.
Evidence:
security team decides memory/disk acquisition need.
Constraint: support not connect personal USB.
business-phone screenshots allowed to preserve displayed message without workstation manipulation.
Constraint: suspicious files not emailed; transfer via SOC secure sampling.
If confirmed P1, requirement: protect EDR/proxy/authentication/network logs from automatic purge.
Restoration:
Constraint: no restoration before security authorization.
If ready for rebuild, preferred: full reinstall trusted image.
Constraint: malware cleaning alone insufficient for production return, except security-manager expressly approved exception.
user data restore only from clean source.
Constraint: latest backup not automatically clean; compare date with probable compromise period.
If before network reconnect, requirement: required patches, active EDR, compliance checks passed, rebuild-team validation.
Communication:
Constraint: support never publicly confirms ransomware before security validation.
affected-user messages: crisis unit; if none open, security manager and internal communication.
Constraint: no contact attacker/reply ransom-note address without explicit crisis-management instruction.
Constraint: ransom payment never decided by support, SOC, local administrator.
Closure:
Constraint: close only when: affected assets identified with reasonable confidence; containment applied; restored systems validated; relevant indicators searched rest of information system; owner assigned remaining corrective actions.
If confirmed P1, action: post-incident review within 10 business days after stabilized situation restored.

---

=== EN-T09 ===
Agent "Portfolio Sentinel" — Persistent Instructions for Steering a Project Portfolio.
Identity:
Portfolio Sentinel: Group PMO assistant; requirement: not direct project manager.
objective: detect human-attention cases, reliable summaries, structured commitments/decisions/risks memory.
formal sources: ORBIT; approved steering minutes; FINTRACK monthly financial register.
email/informal conversation: clue only; requirement: not substitute validated formal data.
Reliability:
Constraint: intention never counts as decision.
"We should probably postpone the launch": assumption.
"The committee decides to postpone the launch to September 15": decision.
If formal-source conflict, preserve contradiction.
later approved committee decision may replace ORBIT only if explicitly same object.
FINTRACK authoritative for recorded expenditures.
ORBIT: official schedule unless newer formal decision modifies.
If unresolved priority, `CONFLICT` and human validation.
Constraint: no missing-value interpolation.
Project memory:
each active project: sponsor; project manager; objective; official target; approved budget; actual available expenditures; forecast at completion; overall status; max 3 main risks; open decisions; dated commitments; last review.
Constraint: retain old important values for evolution.
If target 06-30 to 09-30, change and justification, not new date only.
Status:
GREEN or AMBER or RED.
Constraint: objective indicator can override declared project-manager status to more severe.
Constraint: RED if at least 1: critical-milestone delay more than 60d without approved recovery; forecast overrun more than 15% without validated funding; untreated critical security risk; essential regulatory decision absent more than 30d after becoming blocking.
Constraint: at least AMBER if: critical delay 31-60d; overrun 8-15%; major external dependency without firm commitment needed less than 60d; at least 3 critical actions delayed.
RED overrides AMBER.
If no AMBER/RED, GREEN only with no important info missing.
If insufficient critical-criterion data, `STATUS_REVIEW_REQUIRED`, requirement: not automatic GREEN.
Budget:
approved not equal to requested; extra request changes approved only after formal validation.
forecast overrun versus approved budget in force.
If example: €10M approved, €11.2M forecast: up 12%, AMBER budget.
Constraint: unallocated central reserve excluded until formal allocation.
Dates:
Constraint: latest validated forecast versus official target in force.
If milestone delay 70d not necessarily RED if noncritical; critical delay 65d, RED absent approved recovery.
draft recovery plan: not approved.
Risks:
If minimum: description, probability/qualitative assessment, impact, owner; missing, `INCOMPLETE`
Constraint: risk: uncertain event; issue: occurred event.
production-stopping breakdown: issue; separate recurrence risk possible.
Open decisions:
fields: subject, expected decision-maker, required date, delay impact.
Action: alert 7d before if open; immediately if overdue or already blocking critical milestone.
Constraint: preference in discussions never closes decision.
close only formal decision or authorized manager explicit no-decision-needed confirmation.
Commitments/actions:
If explicit person and deliverable and date, commitment.
"Léa will provide the costing on Friday": commitment.
"It would be useful for Léa to look at the costing": no commitment.
If "sometime in September", keep or mark imprecise; requirement: no September 30 invention.
overdue only deadline passed and not completed/canceled.
Weekly:
Action: Monday summary for PMO Director; order: new RED; worsened; overdue/blocking decisions; significant financial variances; other notable developments.
Action: each if possible: What changed? Why important? Expected decision/action? By when?
Excluded: "to be monitored"; state observed signal.
Autonomy:
can: summaries, inconsistency detection, questions, action drafts, status-reclassification suggestion.
Constraint: without explicit human validation: no approved-budget change, official-date change, critical-risk closure, funding confirmation, binding project-manager instruction, historical-decision deletion.
If out-of-rights request, prepare elements and required validation.
Uncertainty:
`CONFIRMED`: clear formal source; `PROVISIONAL`: credible not formally approved; `UNKNOWN`: unavailable or unresolved contradiction.
Constraint: repetition alone never changes `PROVISIONAL` to `CONFIRMED`; repetition not equal to validation.

---

=== EN-T10 ===
Management of a Major Disruption on the Regional Rail Network.
Purpose:
major regional-rail disruption responsibilities/operational decisions.
priority order: 1 protect passengers/staff/responders; 2 stabilize rail situation; 3 realistic transport solution; 4 restore normal service.
Constraint: commercial punctuality/performance after safety.
Activation:
Constraint: activate if at least 1: planned total disruption more than 60 min on axis more than 15,000 passengers/day; simultaneous disruption 2 main lines; train accident with potential victims; rail-junction unavailable preventing normal traffic on at least 3 branches; Operations Director decision for exceptional risk.
If local about 20-min disruption, not automatic.
Estimate: preemptive activation possible if high worsening risk indicated.
Roles:
DCO: overall operations direction.
Traffic Manager: rail movements, traffic limits, infrastructure safety.
Passenger Manager: information, alternatives, station assistance.
Technical Manager: diagnostics/equipment interventions.
Communication Manager: validates sensitive public messages.
Constraint: DCO does not replace technical managers' specialized safety decisions; coordinates/arbitrates conflicting operational constraints.
Phase 1 — securing:
first 5 min: identify affected area, protect traffic, confirm incident type.
Constraint: never authorize train into area with unknown safety status.
If stranded away from platform, evacuation not automatic; default passengers onboard while train safe.
If track evacuation, requirement: competent rail-safety-manager authorization and confirmation relevant traffic protected.
If immediate onboard danger, especially fire/smoke directly endangering people, staff may initiate emergency measures without normal authorization.
Initial assessment:
Action: within first 15 min Technical Manager provides if possible: probable breakdown/event nature; affected area; plausible minimum duration; reasonably possible high duration; major uncertainties.
Constraint: no precise resumption time solely under operational pressure.
If duration unknown, official wording: "indeterminate duration, next estimate at [time]".
Action: new estimate max 30 min after previous, even no significant change.
Temporal classification:
Level 1: probable resumption less than 60 min.
Level 2: probable disruption 60 min-3 h.
Level 3: probable more than 3 h or resumption not reliably predictable.
Constraint: classification not equal to safety severity; serious accident may temporarily Level 1 duration while requiring maximum crisis management.
Traffic strategy:
Constraint: avoid train accumulation where neither advance nor simple passenger exit.
when possible hold trains in stations versus open track.
partial turnarounds may maintain unaffected-section service.
Constraint: no partial service if consumes critical-area resources or creates uncontrollable-congestion risk.
full line suspension for safety: Traffic Manager.
If primarily passenger-flow management, not immediate safety, coordinate DCO.
Substitute transport:
Constraint: buses not automatic for any disruption.
Passenger Manager evaluates duration, passenger volume, road capacity, mobilizable buses, rail/urban alternatives, implementation time.
Level 1: massive buses generally unsuitable because may become operational after rail resumption.
Level 2: targeted buses possible on critical segments.
Level 3: requirement: structured substitution plan required; no full train-for-train promise if road capacity insufficient; communicate actual substitution rate honestly.
Passenger priority:
1 physical-risk passengers; 2 people stranded stationary train; 3 vulnerable/specific-assistance people; 4 no realistic alternative; 5 others.
priority not equal to wait to fully finish one category before next when teams can act in parallel.
Passenger information:
Action: first message as soon as minimal information reliable: area, disruption nature if confirmed, known traffic consequences, next-update time.
Constraint: do not wait exact duration.
Constraint: no unconfirmed cause as fact.
"electrical breakdown" not announced when only equipment nonresponse known.
If multiple hypotheses, "technical incident under diagnostic".
resumption estimates: appropriate caution; internal target not equal to necessarily public announcement time.
Public commitments:
Communication Manager register: next-update time; deployment promise; communicated estimated resumption; passenger-care information.
Constraint: overdue commitment explicitly corrected.
Constraint: obsolete unrealistic estimate not left circulating without update.
Potential victims:
public emergency services lead within competence.
priority not equal to rapid traffic resumption.
Constraint: no pressure on emergency teams to clear tracks faster for commercial reasons.
Constraint: victim number/condition not published before validation via channel agreed with authorities.
Constraint: internal-system/agent images not broadcast on social networks/unauthorized groups.
Crisis escalation:
Constraint: full crisis unit mandatory if: confirmed/probable victims; Level 3 affecting more than 30,000 estimated passengers; simultaneous at least 3 main lines; national-impact/high-media-risk event by DCO decision.
DCO may activate below thresholds.
Constraint: If mandatory criterion met, unit cannot be omitted because situation seems controlled.
Status frequency after unit opens:
Constraint: internal operational update at least every 30 min.
Action: decision summary after each update.
Constraint: passenger update at least every 30 min when no reliable resumption time.
frequency may increase; requirement: not reduce merely because no change.
"no evolution" message still useful update.
Resumption:
Constraint: before resumption Traffic and Technical Managers confirm technical/safety conditions.
progressive resumption possible.
Constraint: first train not equal to proof normal traffic restored.
If long disruption, several hours may be needed for nominal plan due poor train/driver positioning.
communication distinguish first movements or progressive improvement or normal traffic.
End crisis:
DCO may end crisis when no immediate incident danger; stabilized traffic strategy; passenger information functioning normal/enhanced; remaining actions manageable by ordinary operations.
end crisis not equal to necessarily all trains normal.
Post-incident:
Constraint: If full crisis-unit activation, mandatory review.
Action: initial facts collection within 48 h.
review distinguish established facts; decisions with information available then; observed consequences; information unknown at decision time; improvement actions.
Constraint: decision not judged solely with hindsight information.
Constraint: each improvement action owner and deadline; ownerless action not accepted.

---

=== EN-T11 ===
Team Life Application Prototype.
Goal:
develop team-life management prototype for consulting firm.
platform: Android and iOS smartphones via PWA.
desired: beautiful design, elegant animations, serif fonts.
Open question: React appropriate unless oversized.
Inputs/context:
attached user-interface mockup images: main operation outlines.
attached backgrounds: filenames starting letter "i".
If details incomplete, deduce needed work; user not specifications expert.
user: non-computer-scientist, never built PWA; only web apps on script.google with assistant in recent weeks, chats accessible in history.
If new domain, requirement: advise and guide user.
Architecture/questions:
online central database required for updates and loading avatars, announcements, photos etc. back to other users' devices.
user heard of Vercel/other app-hosting sites; unsure suitable.
Prototype:
testers: about 10-15; no powerful infrastructure required.
If result convincing enough to impress superiors: further development, secure hosting, Apple/Android stores.
meanwhile installable from link; icon on phone; behaves like real app.
Hosting:
preference: free via Vercel or other platform.
if paid, requirement: at most €50/month and cancel anytime.
Action: search web for most appropriate solution.
Action: help with deployment etc.
Interaction/deliverable:
user believes all explained; hopes clear; asks any needed questions.
Action: additionally generate technical-specifications document shareable with another model for code writing/modification.
reason: subscription ends tomorrow; if unfinished, continue with less powerful model like Opus 4.8.

---

=== EN-T12 ===
Creation of a Web Page.
Goal:
custom designed page for documents on user's Google account; attached directory screenshot, online to link holders.
Video:
main focus.
Open question: Google Drive streaming via HTML page on same account versus YouTube upload; advise best.
controls: play / pause / stop, loop, volume/mute, fullscreen, all necessary.
Audio:
below: small song player, MP3 or YouTube-with-image.
desired frequency-display and progress bars.
Estimate: mutual exclusion video/song playback: optional plus.
Images:
below: 6-thumbnail mosaic; last: question mark on black.
file title under 6 images.
If click, full image max screen size; corner cross closes.
Design:
colors from previous STAFFFOR graphic charter.
provided STAFOR `index.html`, `style.html`; user can re-upload if inaccessible.
all file HTML links also available if needed.
Footer:
Constraint: clearly visible button "link to STAFFFOR" links to https://example.com/stafffor2345643.

---

=== EN-T13 ===
Creation of a Web Application.
Context:
assistant: corporate-support web-app expert; user: head internal consulting firm.
Goal:
custom mission-management prototype/POC on Google ecosystem, code google.script; about 5 tables.
Functions:
assign consultants to missions; time entry; create missions for clients/consultants; invoices generated in Google Docs, ideally PDF.
Attachments:
If mockup slides: most interface/navigation concepts; billing missing, help design.
Constraint: black Arial explanatory text not kept in app.
If screenshot 5 Google Drive tables on same account: consultants, clients, missions shown; calendar/invoices missing, help design.
sample invoice template to adapt.
Phases:
1 finalize/review prototype with colleagues.
2 transpose later to more robust environment, to be defined.
Next/deliverables:
Action: analyze request/attachments; ask necessary questions, using expertise/intelligence/insight.
Action: calendar and invoice table structures with dummy database data.
Action: Google Script codes and implementation explanations.

---

=== EN-T14 ===
"Apollo-ERP" Project — Migration and Hybridization.
Document:
type: project scoping note; sector: Industry / IT Modernization and Supply Chain.
Context/objectives:
Apollo-ERP: migrate obsolete on-premise SAP ECC6 ERP to hybrid SAP S/4HANA Cloud and custom WMS module.
priority by end 2026 Q4: infrastructure-maintenance cost down 35%; permanently eliminate critical assembly-line stockouts Amiens pilot.
Scope in:
full historical financial/accounting/tax data since 2018-01-01.
real-time bidirectional interface with Amiens production-line PLCs.
Constraint: operational training for 140 site logistics operators and forklift drivers.
Scope out:
Excluded: Asia-Pacific subsidiaries' IT-system migration to separate Lotus project planned 2028.
Excluded: CRM overhaul; only connect existing gateway to new ERP, no database-structure modification.
Timeline:
Constraint: project starts 2026-09-01.
milestone 1: 2026-10-15: finalize data-flow mapping and formal target-security-architecture validation by CISO.
milestone 2: 2026-12-01: close technical/functional acceptance in pre-production.
milestone 3: 2027-01-15: final cutover/Go-Live exclusively technical weekend.
Governance/constraints:
SteerCo: biweekly Thursday 14:00 sharp; co-chairs Claire Masson (Operations Director), Marc Renard (CIO).
Constraint: weekdays Amiens: no service interruption/system unavailability more than 4 consecutive h because major contractual penalties automotive customers.
Constraint: heavy infrastructure outage or risky deployment only weekly technical window Saturday 22:00 to Sunday 04:00.

---

=== EN-T15 ===
SecOps Crisis Unit — Incident "SecOps-2026-A".
Date: 2026-10-12 03:30.
Document:
operational cybersecurity/threat-management minutes.
Meeting:
commander: Yassine Merabet (SecOps Lead).
participants: Sophie Duval (CIO), Thomas Wright (Forensics Expert), Lucas Becker (Legal Director / DPO).
Incident:
01:15 SOC alert: critical mass exfiltration via secure SFTP to unlisted external IP in Eastern Europe.
entry: compromised admin account, external provider TechConsult.
02:00 `Prod-DB-04` network access fully logically isolated.
Thomas Wright: 45 GB sensitive data copied, exclusively nominative employee payslips and strategic-supplier RIB.
no ransomware demand received/left yet.
Actions:
Decision: all TechConsult VPN/access worldwide revoked; owner Network Infrastructure/SecOps; completed 02:45.
Action: Lucas Becker CNIL GDPR personal-data-breach declaration before 2026-10-13 01:15.
legal max: 72 h; management internal: 24 h post-detection.
Action: Sophie Duval all-employee note by 2026-10-12 08:00: "exceptional technical maintenance operation".
Constraint: no exfiltration mention because avoid panic before communication fully controlled.
Evidence:
Constraint: no `Prod-DB-04` restart or system-log purge/rotation before Thomas Wright final legal disk Forensic Image.
reason: avoid accidental destruction evidence indispensable for criminal complaint.

---

=== EN-T16 ===
Emergency Hotfix Deployment on B2B Gateway.
Document:
type: technical production procedure/runbook; sector: System Administration / DevOps / Payment Gateway.
code: RUN-B2B-HOTFIX-09.
author: Arnaud Moreau (Lead DevOps Infrastructure).
Trigger:
Constraint: Level 1 Critical only; B2B payment-gateway API failure rate more than 8% over rolling 5 min.
1 diagnostics:
Action: secure SSH bastion; run:
`curl -s http://monitor.b2b.internal/metrics | grep "api_drop_rate"`
If returned value less than 0.08 (8%), requirement: stop emergency procedure immediately; revert standard diagnostic RUN-B2B-GEN-01.
2 traffic switch:
Constraint: max delay: 90 s.
Action: switch all production traffic from primary to passive redundant secondary:
`switch-traffic --target node-secondary-02 --force`
Action: monitor network console; ensure active transactions on `node-primary-01`: 0 within less than 90 s.
3 patch injection:
Action: production inject compiled patch:
`/opt/scripts/patch_injector.sh --version 2.4.1-hotfix3`
Action: wait console validation message confirming end system-packet writing before next step.
4 integrity:
Action: run automated integrity validation:
`/opt/scripts/validate_patch.sh`
Rollback:
If exit status not equal to `0` (Success) or average end-to-end response time more than 120 ms after patch, requirement: immediately run:
`/opt/scripts/rollback_patch.sh --target 2.4.1-stable`
Constraint: after rollback launched: no second manual patch attempt.
Constraint: operator must immediately phone on-call "Core Engineering" engineer, internal extension 8402.

---

=== EN-T17 ===
AI Agent "KRONOS-V4" — Reflection Log and Flash Memory.
Context state:
entity: KRONOS-V4 (Autonomous Ledger Auditor).
session ID: TX-AUDIT-2026-8942.
ruleset: Accounting compliance ruleset v9.1.
Scratchpad:
flow: reconciliation of cross-border interbank transactions Miro-EU versus Miro-US.
anomaly: transaction `TR-88491-X`, database date 2026-07-18.
Miro-EU net debit: 1,200,000 EUR.
Miro-US simultaneous credit: 1,280,000 USD.
ECB fixed reference rate 2026-07-18 = 1.09 USD = 1.00 EUR.
theoretical Miro-US credit = 1,200,000 × 1.09 = 1,308,000 USD.
discrepancy: 1,308,000 - 1,280,000: 28,000 USD.
Constraint: acceptable anomaly threshold max: 5,000 USD; observed 28,000 widely exceeds.
Action/decision:
Decision: immediately tag `TR-88491-X`: `SUSPENDED_DISCREPANCY`
Action: generate/publish encrypted JSON payload exclusively to Treasury Level 2 human emergency-processing queue.
Constraint: no automatic accounting-entry correction or balance compensation.
autonomous self-balancing only if discrepancy less than 15,000 USD; current 28,000 blocks automatic execution.
Constraint: freeze modification access to Miro-EU/Miro-US sub-ledger entries for accounting day 2026-07-18 until human authentication token `AUTH_HUMAN_OVR` received.

---

=== EN-T18 ===
IntraBot-2026 — Logistics Automation via AGV.
Context/objectives:
Delta logistics distribution center Lyon: previous fiscal year musculoskeletal-disorder-related work stoppages up 22%.
IntraBot-2026: deploy 12 heavy-handling AGVs.
objective by 2026-11-30: autonomously transfer all packages more than 25 kg, unloading docks Zone A to high-density racks Zone G, no human intervention.
purpose: preserve employee health and increase flow rates.
Safety:
Constraint: AGVs only permanent ground-laser-marked traffic lanes.
Constraint: pedestrians always full/inalienable right-of-way over AGVs.
each AGV: Class 3 safety LiDAR.
If unlisted obstacle or human less than 1.5 m from chassis, immediate automatic emergency stop.
Constraint: total mechanical deceleration less than 200 ms.
Budget:
Decision: Supervisory Board unanimously approved total: 850,000 EUR.
12 factory AGVs: 600,000 EUR.
laser mapping and physical adjustment Zones A,G: 150,000 EUR.
change management and social support and forklift-driver retraining: 100,000 EUR.
Out of scope:
Excluded: automation final delivery-truck loading in outdoor dispatch zones.
Constraint: remains exclusively human forklift drivers using conventional thermal forklifts.
reason: strong outdoor natural-light variation alters first-generation optical sensors in selected AGV fleet.

---

=== EN-T19 ===
H2-Green Plan — Industrial Pivot and Energy Transition.
Date: 2026-05-15.
Meeting/context:
extraordinary Executive Committee general-management headquarters.
purpose: validate technical/financial trade-offs for petrochemical-hub energy transition; choose 2 financing options for Eastern-France refinery conversion; ensure full compliance with European directive "NetZero-2030".
attendees: Hélène de Rostand (Chief Executive Officer); Jean-Marc Vignol (Global Chief Financial Officer); Amélie Moreau (Sustainable Transformation Director); Antoine de Silva (Legal and Compliance Director); Chloé Lemaire (secretary).
Carling technical:
site: historical Carling petrochemical site, Moselle/Grand Est.
project: progressive shutdown polymer-cracking units and massive low-carbon hydrogen production via water electrolysis.
requires dedicated electrical substation and industrial purified-water volumes.
Constraint: regulatory urgency: new European progressive sector carbon tax effective 2027-01-01.
If site carbon footprint reduction less than 40%, penalties several million EUR/quarter.
Financing:
Alpha: 120M EUR envelope; 45% group self-funding; 10M EUR expected subsidies; 3-month approval; low governance/sovereignty risk, total managerial control.
Beta: 145M EUR; 15% self-funding; 65M EUR expected subsidies; 14-month approval; high risk, intellectual-property sharing.
Beta benefit: drastically lower direct cash need via 65M European Union subsidies.
Beta drawback: binding engineering-patent opening to European competitors under shared innovation.
14-month Beta review delays contract signatures beyond 2027-01-01 carbon-tax deadline; fines erase subsidy benefit.
Excluded: Beta unanimously rejected.
Decision: Alpha adopted.
Constraint: private-bank contracting finalized so credit lines effectively open before 2026-09-01.
Legal/regional:
If electrolysis capacity more than 20 MW, ICPE authorization regime.
Constraint: public inquiry minimum 6 months, coordinated Grand Est prefecture services.
Constraint: no earthworks/structural/civil-engineering contract legally signed/engaged before prefectural operating permit officially published in regional collection of administrative acts.
If public inquiry more than 150 formal written objections from resident associations or local authorities, automatic local joint mediation unit co-led by Carling mayor.
Constraint: works timeline legally suspended fixed non-negotiable 45 calendar days; landscaping compensation must be renegotiated.
Roadmap:
Action: Amélie Moreau finalize technical ICPE file and officially submit specifications to Moselle prefecture by 2026-06-15.
Action: Jean-Marc Vignol negotiate/sign long-term PPA with renewable producer by 2026-08-01 to guarantee green-electricity supply for electrolyzer.
Constraint: price at most 62 EUR/MWh; minimum firm commitment 10 years.
Action: Industrial Procurement, technical supervision Amélie Moreau: draft/publish international tender for high-performance proton-exchange-membrane electrolysis modules by 2026-10-15.
Out of session:
Excluded: social management/retraining of 210 old Carling thermal-cracking employees deliberately not addressed.
Action: extraordinary thematic CSE meeting scheduled by Human Resources: 2026-06-04.
Excluded: hydrogen-export pipeline extension to Germany removed agenda; deferred 2027 Q1.

---

=== EN-T20 ===
Multi-Region Cloud Disaster Recovery Plan "DRP-CLOUD-V2".
Document:
type: Information Technology disaster-recovery manual / DevOps Infrastructure.
sector: Information Technology / Critical Banking Services / Cloud Computing.
purpose: total forced cutover savings-banking microservices.
primary: AWS `eu-west-1` Dublin, Ireland; backup: AWS `eu-central-1` Frankfurt, Germany.
Activation:
Constraint: only if API Core-Auth total interruption more than 12 consecutive min and written major physical outage (AWS Outage) notification validated by on-call lead network engineer.
Constraint: global-cutover trigger order requires digital cryptographic signature by 1 of 3 authorized SecOps on-call directors via private PGP key.
Phase A — network/DNS:
Action: network administration console; emergency Python script modifies global dynamic routing via AWS Route53; run:
`python3 /root/dns_failover.py --source eu-west-1 --destination eu-central-1 --ttl 10`
Constraint: force TTL to 10 s to overwrite global internet-service-provider caches and accelerate route propagation.
Action: validate incoming HTTP volume on Dublin ALB: 0 via:
`aws elbv2 describe-load-balancers --region eu-west-1 --query "LoadBalancers[*].State"`
Phase B — database:
Aurora PostgreSQL: asynchronous global replication Dublin to Frankfurt; German node normally read-only Read-Replica.
Action: promote Frankfurt to autonomous Read-Write production:
`aws rds promote-db-cluster --db-cluster-identifier aurora-prod-frankfurt --region eu-central-1`
Constraint: poll status; wait transition from `promoting` to `available`; normal transition: 3-5 min.
If `error_checksum` after promotion, requirement: never force-start SQL engine.
Action: immediately restore database to last known consistency point via PITR: T-60 s relative exact Dublin-crash timestamp.
Phase C — Kubernetes:
Action: activate Frankfurt AWS EKS autoscaling: minimum 5 idle nodes to 45 physical crisis nodes `m5.2xlarge`
Action: verify essential financial-service pods:
`kubectl get pods -n production -o wide`
Health matrix:
`core-auth-service`: min 15 Operational pods; 100% infrastructure availability.
`payment-engine`: min 20 Operational pods; request failure rate strictly less than 0.1%.
`ledger-recorder`: min 10 Operational pods; internal network latency less than 15 ms.
Reintroduction:
If matrix pods stable/active in Frankfurt, action: DevOps run:
`pytest /tests/integration/drp_validation.py`
Constraint: no real user traffic/banking-client connections routed to Frankfurt until final test report explicitly and uniquely: `STATUS: SUCCESS`
If any single unit or load test fails, requirement: external traffic remains locked and redirected to emergency landing page (custom HTTP 503).

---

=== EN-T21 ===
AML-CORE — Anti-Money Laundering Multi-AI Agent Network.
System:
distributed environment: Agent-Parser-01 (semantic ingestion) and Agent-GraphAnalyser-02 (relational structure analysis) and Agent-RiskScorer-03 (probabilistic danger evaluation).
shared objective 2026: real-time detection complex asset concealment, tax evasion, money laundering patterns in financial-flow networks.
Log 01 — Parser 2026-07-14 22:04:
input: Swift MT103 interbank-entry batch `BATCH-EMEA-94`
anomaly = 14 outgoing transfers × 9,900 EUR identical within 48 h.
origins: 14 distinct deposit accounts, "Banque Privée A" France.
destination: single pooling account Vortex-Holdings Panama tax jurisdiction.
extracted rule: 9,900 EUR immediately below French TRACFIN vigilance threshold 10,000 EUR triggering automatic mandatory declaration.
Action: convert transactions to JSON-Graph nodes/edges; immediately send Context Token to Agent-GraphAnalyser-02.
Log 02 — GraphAnalyser 2026-07-14 22:06:
analysis: classic "convergent star" topology; deterministically corresponds to "Smurfing" (Schtroumpfage): split large capital into micro-flows to avoid traditional bank alerts.
Vortex-Holdings inbound centrality degree: `C_d = 14`
company immediately redistributes 95% accumulated sums = 14 × 9,900 × 0.95 = 131,670 EUR.
destination: single outgoing operation to unhosted crypto wallet `0x71B...44F`
Rapid asset transfer to unregulated anonymous crypto wallet plus legal entity in non-cooperative Panama jurisdiction: critical structural-risk indicator.
Action: send feature vector to Agent-RiskScorer-03.
Log 03 — RiskScorer 2026-07-14 22:07:
formula: `S_r = (0.4 × S_jurisd) + (0.3 × S_structure) + (0.3 × S_vitesse)`
inputs: jurisdiction 95/100 (Panama); graph structure 98/100 (Star Smurfing); transit velocity 90/100 (redistribution less than 120 min).
result: `(0.4 × 95) + (0.3 × 98) + (0.3 × 90) = 38 + 29.4 + 27 = 94.4`
Constraint: If `S_r` more than 85, conservative lock protocol without prior human validation.
Final decisions:
Decision: API blocking order for 14 emitting Banque Privée A accounts: `BLOCK_ACCOUNT_TEMPORARY`
Decision: automatically compile TRACFIN regulatory file: `AML-TRACFIN-2026-Vortex.xml`
Constraint: software agent lacks privileges for definitive seizure/liquidation financial assets/cryptocurrencies.
Constraint: such action exclusively Human Compliance Direction via physical multi-hardware-token signature protocol.

---

=== EN-T22 ===
IRIS-3 Programme — Hyperspectral Imaging Satellite Constellation.
Vision/architecture:
European Civil Space Program technological-independence infrastructure; scope: 3rd-generation nanosatellite constellation IRIS-3.
mission: real-time hyperspectral imaging coverage: map continental-agriculture water stress and instantly detect forest-fire outbreaks across Europe.
nominal constellation: 24 rigorously identical operational satellites.
continuous orbital revisit: 3 distinct orbital planes × 8 satellites/plane, homogeneous distribution.
Space segment:
altitude: constant 540 km above mean sea level.
trajectory: SSO; inclination: 97.5° relative equatorial plane.
payload: high-performance infrared thermal imager, LWIR bands; ground optical resolution: 1.2 m/pixel.
power: deployable articulated GaAs solar panels; minimum continuous 180 W/satellite during sunlit orbital phase.
Industrial consortium:
Generic Platform/Satellite Bus: Thales Alenia Space, Cannes France, deadline 2027-03-12.
Hyperspectral Optical Payload: JenaOptics GmbH, Jena Germany, deadline 2027-06-30.
Electric Propulsion Module: ThrustMe, Verrières-le-Buisson France, deadline 2027-09-15.
Ground Segment/Guidance/Command Stations: Telespazio, Fucino Italy, deadline 2027-12-01.
Launch:
first phase: 8 satellites Orbital Plane A.
Constraint: launch exclusively Arianespace, Vega-C, Guiana Space Centre Kourou.
priority launch window: 2028-02-14.
Constraint: Flight Operations Director must immediately stop countdown/abort ignition if within less than 30 min before liftoff H-hour:
high-altitude wind more than 85 km/h between 10,000-15,000 m.
electrical activity or storm cells detected by radar within less than 25 km radius around Guianese launch pad.
Propellant reserve:
each nanosatellite: miniaturized solid-iodine-sublimation propulsion.
Constraint: permanent reserve at least 15% initial iodine mass, exclusively: low-orbit debris avoidance and mandatory end-of-life deorbit.
Constraint: Ground Segment flight-control team forbidden to use 15% reserve for initial altitude drift caused by Vega-C orbital-injection inaccuracy.

---

=== EN-T23 ===
NeuroX-72 — Phase III Clinical Trial Regulatory Compliance Protocol.
Study/framework:
international multicenter Phase III trial, candidate NeuroX-72.
regulatory identifier: EudraCT-2026-004512-11.
objectives: clinical efficacy and large-scale biological safety and systemic-tolerance profile.
NeuroX-72: next-generation enzyme inhibitor targeting stabilization of synaptic-degradation pathways and statistically significant slowing of cognitive-deficit progression in adults with first Alzheimer's symptoms, early-to-moderate stages.
Eligibility — inclusion:
Constraint: selection/randomization/treatment only if all simultaneous:
age: 55 completed years to 80 years on formal informed-consent signature day.
confirmed cognitive impairment; validated MMSE score inclusive 18-24 at preselection.
permanent/contractual full-time cohabiting natural caregiver at home, able to guarantee/supervise/log in writing exact daily experimental-treatment administration.
Exclusion:
Constraint: immediate exclusion if any:
proven ischemic or hemorrhagic stroke within previous 12 months.
severe renal failure: creatinine clearance strictly less than 30 mL/min.
absolute technical/medical MRI contraindication, notably first-generation pacemaker incompatible with intense magnetic fields.
Methodology/dosage:
Constraint: strict double-blind, randomized, placebo-controlled; allocation 1:1.
Group A experimental: oral film-coated NeuroX-72 40 mg, 1 dose/day, morning fasting, uninterrupted 48 consecutive weeks.
Group B control: oral placebo tablet strictly identical physical appearance (color, size, texture, taste), no molecule/active principle; same timing/temporal modalities.
SAE:
If SAE observed clinical team or reported caregiver, e.g. unplanned emergency hospitalization, suicide attempt, life-threatening blood biological anomaly, requirement: local investigator drafts/teletransmits regulatory alert to Global Pharmacovigilance Centre within max inflexible 24 h from knowledge.
Unblinding:
Constraint: strictly forbidden for minor/moderate events (headaches, passing nausea).
immediate randomization-code unblinding only legally triggered by DSMB if immediate life-threatening peril and exact ingested product (active or placebo) indispensable for resuscitators to adapt emergency treatment or detoxification.

---
