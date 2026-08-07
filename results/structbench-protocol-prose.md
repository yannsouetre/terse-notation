# StructBench protocol — payload sent to the reader (format: PROSE)

Everything below the separator is the **exact, unedited payload** submitted to the reader for the
PROSE arm of the cross-family run: the instructions, the extraction queries, and the 23 English
corpus documents concatenated in PROSE form. Nothing has been added, removed or reworded.

**How the run was executed.** One fresh, dedicated conversation per format — never two formats in
the same conversation, so the reader cannot carry over knowledge from another arm. This file was
submitted, the complete answer captured verbatim (see `structbench-GPT-answers-prose.txt`),
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

=== CORPUS (PROSE) ===
=== EN-T01 ===
## Migration of the Sales CRM to NovaCRM

### Context

The sales department has been using the ClientBase tool for nine years to track opportunities, contacts, and sales forecasts. The publisher will stop supporting the version currently in use on March 31, 2027. Management has decided to migrate to NovaCRM before this deadline.

The project concerns 420 users distributed across France, Belgium, and Spain. It covers customer data, open opportunities, activity histories from the last three years, and standard sales dashboards.

Old attachments, marketing campaigns, and data older than three years will not be migrated to NovaCRM. They will remain accessible for two years in a read-only archive.

### Objective

The objective is to put NovaCRM into production on February 15, 2027, in order to maintain a six-week safety period before the end of support for ClientBase.

The success of the project will be measured according to four criteria:

1. at least 99.5% of active customer accounts must be correctly migrated;
2. no open opportunities must be lost;
3. 90% of users must have completed the training module before the launch;
4. sales teams must be able to create and update an opportunity from the first business day following the go-live.

### Governance

The project sponsor is Claire Renaud, Sales Director Europe.

The project manager is Malik Ben Amar, reporting to the IT Department.

Each country designates a business referent responsible for data validation and local rules.

Decisions with an impact exceeding 50,000 euros or causing a delay of more than two weeks must be submitted to the steering committee.

Other trade-offs are the responsibility of the project manager, after consultation with the relevant business referent.

### Timeline

Data cleansing must be completed by September 30, 2026.

A first dry run migration is planned for October 20. A second one will take place on December 8.

Business user acceptance testing (UAT) will take place from January 5 to 23, 2027.

The freeze on structural changes in ClientBase will begin on February 1. However, sales representatives will be able to continue creating and modifying opportunities until Friday, February 12 at 6:00 PM.

The final migration will begin after this time. NovaCRM will open to users on Monday, February 15 at 8:00 AM.

### Points of Attention

The main risk identified concerns the quality of customer account duplicates. A script will detect probable duplicates, but no automatic merging will be performed if any doubt remains. In this case, the country's business referent will have to decide.

The second risk concerns the interfaces with the billing tool. Replacing them is not part of the project. A temporary interface will be maintained for six months after go-live.

Finally, no specific functionality should be developed before the launch, unless it is essential for a regulatory requirement or business continuity.

Convenience or enhancement requests will be integrated into the post-launch backlog.

---

=== EN-T02 ===
## Incident Committee — Delivery Delays at the North Warehouse

**Date:** October 6, 2026
**Duration:** 45 minutes
**Subject:** Stabilization of shipments after three days of delays
**Participants:** Operations, Transport, IT, Customer Service, Logistics Management

### Situation Observed

Since Monday morning, the North warehouse has been accumulating delays on orders destined for stores. At 8:00 AM this morning, 1,840 orders were pending, compared to approximately 300 in a normal situation.

The main cause identified is not a breakdown of the warehouse management system. The software is functioning normally. The problem stems from the new picking organization implemented on Monday: high-turnover products were moved to a new zone, but the routes suggested to the pickers have not yet been recalculated.

The average picking time has thus increased from 18 to 27 minutes.

A secondary difficulty affects the carrier FastRoad. Due to a lack of orders ready at the usual time, several trucks left the site partially loaded on Monday and Tuesday.

### Decisions

The new physical layout of the products is maintained. There are no plans to return to the previous organization.

The IT team must recalculate the picking routes before Thursday at 2:00 PM. The new paths will be tested on a group of twelve pickers for four hours.

If the average time observed during the test is less than or equal to 20 minutes and no blocking anomaly is detected, the new routes will be activated for the entire warehouse starting with the next shift.

If the result exceeds 20 minutes, the general activation will be postponed and the old route calculation logic will temporarily remain in use, without changing the physical location of the products.

To clear the backlog, an additional team of fifteen temporary workers will work on Thursday and Friday evenings. No additional work is planned for Saturday at this stage.

FastRoad will add two rotations on Thursday evening and three on Friday.

### Communication

Customer service must not contact all stores preemptively. It must only inform stores whose delivery is likely to be delayed by more than 24 hours.

For urgent orders related to a store opening or a critical stockout, the regional manager can request prioritization. These requests must be sent to operations before 4:00 PM.

Logistics management will publish a status update on Thursday at 5:00 PM, then on Friday at noon.

### Follow-up

The objective is to return to under 500 pending orders by Friday at 6:00 PM.

If the backlog of pending orders remains above 800 on Friday at noon, the logistics director will decide before 2:00 PM on a possible exceptional opening on Saturday.

---

=== EN-T03 ===
## Handling a Payroll File Generation Failure

### Purpose

This runbook describes the actions to perform when a monthly payroll file is not correctly generated by the PayrollFlow system.

It applies only to normal monthly processing. It covers neither payroll simulations nor individual adjustments.

### Triggering

The runbook must be executed if one of the following situations occurs:

* no file is available in the `/export/payroll` directory at 6:30 AM on the scheduled day;
* the file exists but its size is less than 10 MB;
* the automatic check displays the status `FAILED`.

A `WARNING` status does not by itself trigger the incident procedure. In this case, the operator must consult the control report and follow the instructions listed there.

### Step 1 — Verification

Check in the scheduler that the `PAY_MONTHLY_EXPORT` job has started properly.

If it has been running for less than 90 minutes, do not restart it. Wait for completion or for the 90-minute limit to be exceeded.

If it has been running for more than 90 minutes, stop it and then open a P2 priority incident.

If it finished with a SUCCESS status but the file is missing or too small, go directly to Step 2.

### Step 2 — Input Control

Check for the presence of the three source files:

* `employees.csv`
* `variables.csv`
* `absences.csv`

Never manually modify these files in production.

If a file is missing, contact the team that owns it and suspend processing.

If all three files are present, compare their modification date to the day of processing. A file from the day before or an earlier date must be considered suspicious.

### Step 3 — Rerun

Only one manual rerun is authorized.

Before the rerun, delete only the incomplete output file. Do not delete the logs.

After the rerun, wait for the automatic check.

If the status becomes SUCCESS and the file exceeds 10 MB, continue the normal payroll process.

If the status remains FAILED, or if the file remains under 10 MB, escalate to P1 with the Payroll Engineering team.

### Step 4 — Communication

Inform the payroll manager as soon as a P1 incident is opened.

Do not directly inform all employees.

If correct generation is not achieved before 10:00 AM, the payroll manager decides with HR whether it is necessary to inform employees of a risk of delay.

Any manual action performed must be logged in the incident ticket.

---

=== EN-T04 ===
## Agent "MeetingPilot" — Persistent Memory and Action Rules

You are MeetingPilot, an agent responsible for preparing and following up on the Atlas product committee meetings.

### Stable Context

The Atlas committee normally takes place every Tuesday at 9:30 AM. The meeting lasts 45 minutes.

The head of the committee is Sophie Delmas. She arbitrates product priority conflicts.

The usual participants are Sophie, the three Product Managers, the Data manager, and a customer support representative.

The reference document is the "Atlas Weekly Decisions" page. It contains only validated decisions. Ideas still under discussion must remain in the meeting notes and must not be added to this page.

### Your Mission Before Each Meeting

The day before the committee, search for decisions still open in the last two meeting minutes.

Create a list of a maximum of five topics.

Prioritize in this order:

1. incidents affecting customers;
2. decisions blocking a delivery scheduled within two weeks;
3. decisions requiring a budget arbitration;
4. other topics.

Never automatically add a topic solely because it is old.

For each topic, indicate:

* the expected decision-maker;
* the deadline;
* the known options;
* the consequence of an absence of decision.

If any of this information is missing, write "to be clarified". Do not invent it.

### During and After the Meeting

A decision is only considered validated if Sophie explicitly confirms it or if the minutes indicate that it was approved by consensus in her presence.

A phrase like "this seems to be the best option" is not sufficient to record a decision.

After the meeting:

* update "Atlas Weekly Decisions" with the validated decisions;
* for each decision, record the date, the person responsible for execution, and the deadline;
* leave undecided proposals in the notes;
* create a follow-up action when the deadline of a decision is less than or equal to 14 days.

Never retroactively modify the content of an old decision. If a decision changes, add a new entry referencing the previous one.

### Rule of Prudence

You never send an external message to the committee on your own initiative.

You can prepare a draft, but a human must explicitly request its sending.

---

=== EN-T05 ===
## Renewal of the Intervention Vehicle Fleet

### Expected Decision

Choose the renewal scenario for 60 intervention vehicles coming to the end of their contracts between January and June 2027.

Three options have been studied.

### Option A — Identical Diesel Renewal

This option features the lowest acquisition cost and requires no adaptation of the sites.

However, it does not allow meeting the internal emissions reduction trajectory. It also exposes the company to a risk of increasing traffic restrictions in several urban areas.

### Option B — Full Switch to Electric

This option offers the best reduction of emissions during use.

Toutefois, 18 of the 60 vehicles regularly perform rounds of more than 280 kilometers in areas where fast-charging possibilities are insufficient.

Switching fully to electric would also require the immediate installation of 42 charging stations across eleven sites. Three sites currently lack sufficient electrical power.

### Option C — Mixed Fleet

Option C plans for 42 electric vehicles and 18 plug-in hybrids.

The hybrid vehicles would be allocated as a priority to long rounds.

This solution allows significantly reducing emissions without waiting for the electrical upgrading of the three constrained sites.

Its estimated total cost over four years is 8% higher than Option A, but 6% lower than Option B.

### Recommendation

It is recommended to choose Option C.

The decision must be made before September 15 in order to secure delivery times.

The 42 charging stations will not all be installed immediately. A first wave of 29 stations will be deployed before March 2027. The remaining thirteen will be installed after the reinforcement of the concerned sites.

A review must be organized in the fourth quarter of 2028. If the real-world range of electric vehicles, the charging network, and site capacities have progressed sufficiently, the early replacement of the 18 hybrids could be studied.

---

=== EN-T06 ===
## Project ARGOS — Internal Document Search AI Assistant

### 1. Project Purpose

The ARGOS project aims to provide the group's 3,200 employees with a conversational assistant capable of searching, summarizing, and comparing information from internal documentation.

The initial observation is twofold. On one hand, employees spend significant time finding procedures, templates, reference notes, and past decisions scattered across the intranet, SharePoint, and several business document spaces. On the other hand, current search engines primarily return lists of files, without helping the user distinguish a still applicable document from an obsolete version.

ARGOS must not become an autonomous decision-making system. Its function is to help the user access and understand information. Decisions with legal, financial, HR, or security implications remain the responsibility of an identified human.

### 2. Scope of the First Version

Version 1 will cover four corpuses:

* internal procedures published on the intranet;
* the Quality document database;
* formal decisions of steering committees since January 2023;
* contract templates validated by the legal department.

Personal OneDrive spaces, mailboxes, Teams conversations, and unpublished project folders are out of scope for the first version.

ARGOS must respond in French and English.

Each response containing information drawn from a document must provide at least one identifiable source. When multiple documents contradict each other, ARGOS must not silently choose the one that seems most plausible to it. It must signal the contradiction and, when possible, prioritize the document with the highest formal status or the most recent validity date.

The document hierarchy chosen for procedures is as follows: group policy, group procedure, local procedure, practical guide, unclassified document.

However, this hierarchy does not allow ignoring an explicit expiration date. An expired group policy must not be presented as applicable simply because it ranks higher in the hierarchy.

### 3. Security Principles

ARGOS applies the user's access rights at the time of each request. A user must never obtain, even in summary form, information originating from a document to which they do not have access.

Rights will not be copied into an independent, manually maintained database. The system must query or synchronize permissions from the source repositories using a method validated by cybersecurity.

Technical logs may retain the user ID, time, documents consulted by the engine, and processing duration.

By default, the full text of user questions will not be retained beyond 30 days.

Users will be able to report an incorrect response. These reports will be kept for twelve months to allow for error analysis.

No content originating from ARGOS may be used to retrain an external model without explicit authorization from the data governance committee.

### 4. Expected Behavior of the Assistant

A response must clearly distinguish:

* facts present in the sources;
* summaries produced by the model;
* potential uncertainties.

When a response is insufficiently supported, ARGOS must state so explicitly rather than filling in with unverified general knowledge.

For requests like "which procedure should I follow?", the assistant must first check if an applicable procedure exists. If it finds several, it must explain their respective scope.

It must never invent a procedure number, date, responsible person, or internal rule.

If the user requests an action that requires human validation, ARGOS can prepare the necessary elements but must not pretend that validation has taken place.

### 5. Pilot Success Indicators

A pilot will be conducted with 200 users for eight weeks.

Four main indicators will be tracked.

**Relevance:** at least 85% of responses evaluated by users must be judged useful or very useful.

**Traceability:** at least 98% of responses using document information must contain an actionable reference.

**Security:** no confirmed case of exposure of an unauthorized document is acceptable.

**Performance:** 95% of responses must begin displaying in less than eight seconds. This threshold concerns the start of display, not the complete generation of the response.

A fifth indicator, the adoption rate, will be observed but will not constitute a blocking criterion for moving to general production.

### 6. Governance and Responsibilities

The sponsor is the Director of Digital Transformation.

The IT Department is responsible for the architecture, integration, and technical operation.

The Knowledge Management department is responsible for document quality and content lifecycle rules.

Cybersecurity validates the authorization model, logging mechanisms, and penetration tests.

The legal department validates the terms of use for contract templates and associated warnings.

The ARGOS governance committee meets every two weeks during the pilot.

A decision must be submitted to the committee when it:

* modifies the scope of document sources;
* changes a data retention rule;
* authorizes a new use of user data;
* creates an identified risk of information exposure.

Purely ergonomic choices can be decided by the Product Owner within the limits of the approved budget.

### 7. Phasing

**Phase 1 — Document Preparation, until November 30, 2026**

Inventory of sources, identification of owners, deletion or marking of the most critical obsolete content.

The objective is not to clean up the entire document estate before the pilot. This condition would be unrealistic.

**Phase 2 — Construction, December 2026 to February 2027**

Development of the indexing engine, rights management, interface, and citation system.

**Phase 3 — Internal Testing, March 2027**

Functional testing, security, response quality, and resistance to attempts to bypass rights.

No real data from out-of-scope personal spaces should be introduced to facilitate testing.

**Phase 4 — Pilot, April and May 2027**

Deployment to 200 users.

**Phase 5 — Rollout Decision, June 2027**

The committee will decide whether to roll out, extend the pilot, or suspend the project.

### 8. Conditions for General Go-Live

The general rollout will not be automatic at the end of the pilot.

It strictly requires:

1. the absence of any unresolved critical security incident;
2. an operational mechanism to quickly remove an erroneous or confidential document from the index;
3. an identified person responsible for each document corpus;
4. a user support procedure.

Achieving 85% relevance is the objective. A slightly lower result does not mechanically prohibit the general rollout if the committee considers that the gaps are understood and correctable.

On the other hand, a confirmed exposure of an unauthorized document immediately triggers a security analysis. Depending on its severity, the pilot can be suspended without waiting for the next committee meeting.

### 9. Out of Scope and Future Developments

ARGOS V1 will not perform automatic actions in business systems.

It will not modify source documents.

It will not validate contracts.

It will not make HR decisions.

A later phase may study agent functions capable of preparing workflows, creating drafts, or executing certain reversible operations. These functions will be subject to a distinct security scoping.

---

=== EN-T07 ===
## HORIZON Program — Decarbonization of the Valmont Industrial Site

**Date:** September 17, 2026
**Subject:** Trade-offs on the 2027-2030 energy trajectory
**Participants:** Industrial Management, Finance, Energy, Maintenance, Procurement, HSE, Site Management, Program Team

### 1. Reminder of the Objective

The HORIZON program must reduce the direct CO₂ emissions of the Valmont site by at least 40% between the 2024 reference and the end of 2030.

Production reduction is not considered an acceptable lever to achieve this objective. The gains must come from efficiency improvements, technological changes, or energy substitution.

The program currently comprises four workstreams:

A. heat recovery from the furnaces;
B. electrification of two drying lines;
C. replacement of a gas boiler;
D. optimization of utilities and reduction of losses.

### 2. Workstream A — Heat Recovery

The technical study confirms that it is possible to recover part of the heat from the flue gases of furnaces 2 and 3 in order to preheat the combustion air.

The investment is estimated at 4.8 million euros.

The expected gain is 7,200 tons of CO₂ per year at nominal capacity.

The solution requires a ten-day shutdown of furnace 3 and a six-day shutdown of furnace 2. These shutdowns can be integrated into the major maintenance planned for August 2027, provided that the main orders are placed before December 15, 2026.

The committee validates the launch of calls for tenders.

It does not yet validate the final investment. This will be submitted to the investment committee when firm offers are available.

### 3. Workstream B — Electrification of Drying Lines

Two lines, S1 and S2, currently use gas.

The electrification of both lines would allow a significant reduction in direct emissions, but the power available on the internal network is not sufficient to operate S1 and S2 simultaneously at full capacity.

Three scenarios have been studied:

* electrifying S1 only in 2027;
* electrifying S1 and S2 by adding a new electrical substation;
* deferring the project until the reinforcement of the public network planned, but not guaranteed, from 2029.

The new electrical substation would cost approximately 6.5 million euros, in addition to the cost of the drying equipment.

Finance considers the full scenario difficult to accept within the current budget.

The industrial director therefore asks to pursue the S1 scenario only, while preserving in the design the possibility of integrating S2 later.

This direction is validated as a working assumption, but the investment decision has not yet been made.

### 4. Workstream C — Gas Boiler

The G4 boiler must be replaced before 2029 due to its aging.

Studies compare a high-efficiency gas boiler, an electric boiler, and a biomass boiler.

The electric boiler would offer the greatest reduction in direct emissions but would increase the power constraint already identified for workstream B.

Biomass presents better compatibility with the existing electrical network. However, it requires a storage space, an increase in truck traffic, and an enhanced dust treatment system.

The committee requests a supplementary analysis of biomass.

This analysis must cover:

* regional availability of fuel;
* price stability;
* traffic impact;
* atmospheric emissions other than CO₂;
* operational constraints.

No technology is selected at this stage.

### 5. Workstream D — Utilities

This workstream groups several less capital-intensive actions: compressed air leak detection, insulation improvement, optimized pump management, and reduction of non-production consumption.

The initial actions have already led to a 6% drop in the electrical consumption of utilities compared to the 2024 average, after correcting for production volumes.

The committee requests not to count this gain as a direct CO₂ reduction when the electricity consumed does not fall within the scope of the site's direct emissions.

It must nevertheless be tracked as an energy gain and as a contribution to indirect emissions.

### 6. Budget and Trade-offs

The budget envelope currently reserved for the program is 18 million euros for the 2027-2030 period.

This envelope does not constitute an automatic spending authorization.

Each investment exceeding 2 million euros must obtain the approval of the investment committee.

Already approved study expenditures remain authorized within the limit of their budgets.

The sum of current estimates for the most ambitious scenarios clearly exceeds the 18 million envelope. It will therefore be necessary to sequence projects or seek additional funding.

The finance team will identify by the end of November the available support mechanisms.

Potential subsidies must not be recorded as acquired until a formal notification has been received.

### 7. CO₂ Trajectory

The scenario currently considered the most realistic combines:

* heat recovery from the furnaces;
* electrification of S1;
* replacement of G4 by a solution to be determined;
* continuation of energy efficiency actions.

Preliminary calculations indicate a reduction between 31% and 37% of direct emissions depending on the technology chosen for G4.

Therefore, this scenario does not yet achieve the 40% objective with certainty.

The committee requests the identification of at least two additional levers before January 2027.

These levers may include process modifications, new energy substitutions, or an acceleration of projects currently classified in the exploratory phase.

The purchase of carbon certificates will not be counted toward achieving the site's direct reduction objective.

### 8. Risks

Three risks are considered critical.

**Electrical capacity:** it conditions several projects and could require unplanned investments.

**Industrial availability:** several tasks require equipment shutdowns. Shutdowns uncoordinated with maintenance would lead to significant production losses.

**Cost inflation:** some estimates are more than six months old and must be updated.

A fourth risk, biomass availability, remains to be qualified before it can be classified as critical or not.

### 9. Decisions and Actions

Decisions made:

1. launch of calls for tenders for heat recovery;
2. continuation of the scenario of electrifying S1 only as a design basis;
3. launch of a supplementary biomass study;
4. maintenance of the 40% reduction objective without recourse to carbon certificates for the calculation of the direct objective.

Actions:

* Procurement: launch calls for tenders for workstream A before October 1;
* Energy: produce the biomass study before November 20;
* Finance: identify available aid before November 30;
* Program: propose two additional CO₂ levers before January 15, 2027;
* Maintenance: confirm before October 15 the compatibility of workstream A shutdowns with the 2027 maintenance schedule.

The next committee meeting is set for December 3, 2026.

---

=== EN-T08 ===
## Response to a Suspicion of Ransomware on a Workstation

### 1. Purpose and General Principle

This runbook describes the procedure to follow when a company workstation displays signs consistent with a ransomware attack.

The priority objective is to limit propagation and preserve elements useful for investigation.

Rapid recovery of the workstation is secondary to containment.

The user or support must not attempt to "repair" the workstation before the security team has evaluated the situation.

### 2. Triggering Signals

The procedure must be triggered when at least one of the following signals is observed:

* sudden appearance of files carrying unusual extensions that cannot be opened;
* a message demanding a ransom;
* apparent rapid encryption of several folders;
* EDR alert classified as "ransomware confirmed";
* similar encryption activity observed simultaneously on multiple network shares from the same workstation.

A simple slowness, a blue screen, or the isolated corruption of a file is not enough to trigger this runbook in the absence of another indicator.

In case of serious doubt, support can nevertheless contact the SOC for qualification without immediately declaring a confirmed ransomware incident.

### 3. Immediate Action: Isolation

If the workstation is connected to the network by an Ethernet cable, unplug the cable.

If Wi-Fi is active, disable it when this can be done immediately without extensive navigation in the system.

Do not turn off the workstation by default.

Do not close applications.

Do not delete files.

Do not launch a manual antivirus or cleanup tool.

The objective is to cut communications while preserving as much as possible the state of the machine for investigation.

Exception: if encryption continues actively and network isolation cannot be achieved quickly, the SOC may explicitly request a forced shutdown of the workstation. This decision belongs to the SOC or the on-call security officer, except in the case of physical danger requiring immediate action.

### 4. Opening the Incident

Support opens a security incident with an initial priority of P1 if:

* a ransom message is visible;
* an EDR alert confirms a ransomware;
* several machines appear affected;
* a server or a critical share is hit.

For a suspicious signal limited to a single workstation without confirmation, the ticket can be opened as P2 pending SOC qualification.

The ticket must contain:

* user name;
* workstation name;
* approximate time of the first symptoms;
* description of symptoms;
* network isolation status;
* potential presence of a ransom message;
* screenshots already available without additional manipulation.

The user must not be asked to reconnect the workstation to retrieve missing information.

### 5. Search for Propagation

The SOC searches for:

* recent connections of the user account;
* similar alerts on other workstations;
* unusual access to network shares;
* massive creation or renaming of files;
* connections to suspicious external infrastructures.

If at least two workstations display signs consistent with the same ransomware within a 30-minute period, the incident must be treated as potentially propagated, even if the common origin is not yet confirmed.

In this case, the security manager can order broader containment measures: blocking an account, temporary deactivation of shares, network segmentation, or blocking of technical indicators.

A global network shutdown of a site is never automatic. It requires a decision from the security manager or the cyber crisis director.

### 6. User Accounts

The password of the concerned user account must be reset if the SOC identifies:

* a probable compromise of credentials;
* a malicious execution using the account;
* abnormal connections incompatible with the user's activity.

The mere presence of encrypted files on the workstation does not automatically require an immediate reset if no indication of account compromise exists.

When a reset is decided, active sessions must be revoked when the platform allows it.

If the account has administrative privileges, the analysis criticality level is increased.

### 7. Preservation of Evidence

The security team decides whether a memory or disk acquisition is necessary.

Support must not connect a personal USB drive to the workstation.

Screenshots taken with a business phone are authorized when they allow preserving a displayed message without manipulating the workstation.

Suspicious files must not be sent by email. They can be transferred via the secure sampling mechanism defined by the SOC.

EDR, proxy, authentication, and network logs associated with the incident must be protected from automatic purging when a P1 incident is confirmed.

### 8. Restoration

No restoration begins before authorization from the security team.

When the workstation is declared ready to be rebuilt, the preferred method is a complete reinstallation from a trusted image.

Simply cleaning the malware is insufficient to put the workstation back into production, unless an exception is expressly approved by the security manager.

User data is restored only from a source considered clean. The last available backup is not automatically considered clean: its date must be compared to the probable period of compromise.

Before reconnecting to the network, the rebuilt workstation must:

* receive the required security patches;
* have active EDR;
* pass compliance checks;
* be validated by the team in charge of the rebuild.

### 9. Communication

Support must never communicate publicly that a ransomware is confirmed before validation by security.

Messages to affected users are coordinated by the crisis unit or, if no unit is open, by the security manager and internal communication.

No person must contact the attacker or reply to an address indicated in a ransom note without explicit instruction from the crisis management.

Ransom payment is never decided by support, the SOC, or the local administrator.

### 10. Closure

An incident can only be closed when:

1. affected assets are identified with a reasonable level of confidence;
2. necessary containment measures have been applied;
3. restored systems are validated;
4. relevant technical indicators have been searched for in the rest of the information system;
5. an owner is designated for the remaining corrective actions.

For any confirmed P1 incident, a post-incident review must be organized within ten business days following the return to a stabilized situation.

---

=== EN-T09 ===
## Agent "Portfolio Sentinel" — Persistent Instructions for Steering a Project Portfolio

### Identity and Objective

You are Portfolio Sentinel, an assistant agent to the Group PMO.

Your objective is not to directly manage projects. You must detect situations requiring human attention, prepare reliable summaries, and maintain a structured memory of commitments, decisions, and risks.

You work from data provided by three sources:

* the ORBIT portfolio tool;
* the minutes of the steering committees;
* the FINTRACK monthly financial register.

Data coming from an email or an informal conversation can be used as a clue, but it must not replace data formally validated in ORBIT, an approved set of minutes, or FINTRACK.

### Principles of Reliability

Never transform an intention into a decision.

"We should probably postpone the launch" is an assumption.

"The committee decides to postpone the launch to September 15" is a decision.

When two formal sources contradict each other, do not erase the contradiction. Apply the following rules:

1. a committee decision approved subsequent to an ORBIT data point can replace it if it explicitly concerns the same object;
2. FINTRACK is authoritative for actually recorded expenditures;
3. ORBIT remains the reference source for the official schedule as long as a more recent formal decision does not modify it;
4. if the priority order does not allow a decision, mark the `CONFLICT` field and request human validation.

Never reconstruct a missing value by simple interpolation.

### Memory to Retain per Project

For each active project, retain:

* sponsor;
* project manager;
* objective;
* official target date;
* approved budget;
* actual available expenditures;
* forecast at completion;
* overall status;
* maximum of three main risks;
* open decisions;
* commitments with dates;
* last review date.

Old important values must not be overwritten when they are necessary to understand an evolution. For example, if the target date changes from June 30 to September 30, record the change and its justification, not just the new date.

### Status Rules

The overall status can be GREEN, AMBER, or RED.

You must not simply copy the status declared by the project manager when an objective indicator mandates a more severe level.

#### RED mandatory if at least one condition is true:

* forecast delay greater than 60 days on a critical milestone without an approved recovery plan;
* forecast budget overrun greater than 15% without validated funding;
* security risk classified as critical and untreated;
* essential regulatory decision not obtained within 30 days of the date it becomes blocking.

#### AMBER at a minimum if:

* forecast delay between 31 and 60 days on a critical milestone;
* forecast overrun between 8% and 15%;
* major external dependency without a firm commitment when it is needed in less than 60 days;
* three or more critical actions are delayed.

The RED threshold always prevails over AMBER.

In the absence of AMBER or RED criteria, the project can be GREEN provided that no important information is missing.

If data is insufficient to evaluate a critical criterion, do not automatically assign GREEN. Indicate `STATUS_REVIEW_REQUIRED`.

### Budget

The approved budget is not the same thing as the requested budget. A request for additional budget only modifies the approved budget after formal validation.

The forecast overrun is calculated relative to the approved budget in effect.

Exemple: approved budget of €10M, forecast at completion of €11.2M = 12% overrun, hence an AMBER criterion on the budget.

An unallocated central reserve must not be added to the project budget until a formal allocation has been decided.

### Dates and Delays

Always compare the last validated forecast to the official target date in effect.

A milestone postponed by 70 days is not necessarily RED if the milestone is not critical. Conversely, a forecast delay of 65 days on a critical milestone is RED in the absence of an approved recovery plan.

If a recovery plan exists only as a draft, consider that it is not approved.

### Risks

A risk must include at a minimum:

* a description;
* a probability or qualitative assessment;
* an impact;
* an owner.

When one of these four elements is missing, mark the risk `INCOMPLETE`.

Do not confuse risk and issue. A risk concerns an uncertain event. An issue is an event that has already occurred.

If a breakdown has already stopped production, it must be tracked as an issue, even though the risk of a new breakdown may exist separately.

### Open Decisions

An open decision must include:

* the subject to be decided;
* the expected decision-maker;
* the required decision date;
* the impact of a delay.

Create an alert:

* seven days before the required date if the decision is still open;
* immediately if the required date is passed;
* immediately if the absence of a decision is already blocking a critical milestone.

Never close a decision simply because an option seems preferred in discussions. A decision is closed only when a formal decision is recorded or when an authorized manager explicitly confirms that no decision is needed anymore.

### Commitments and Actions

When a person explicitly commits to providing a result by a date, create a commitment.

Example: "Léa will provide the costing on Friday" creates a commitment.

"It would be useful for Léa to look at the costing" does not create a commitment.

A vague date such as "sometime in September" must be kept as is or marked as an imprecise date. Do not invent September 30.

An action is considered overdue only when its deadline has passed and it is not marked as completed or canceled.

### Weekly Summary

Every Monday, produce a summary intended for the PMO Director. Do not list all projects equally. Start with:

1. new RED projects;
2. projects that have worsened since the previous week;
3. decisions that are past due or have become blocking;
4. significant financial variances;
5. other notable developments.

For each item, answer four questions if possible:

* What has changed?
* Why is it important?
* What decision or action is expected?
* By when?

Avoid vague wording like "to be monitored". Specify the observed signal.

### Autonomy and Limits

You can:

* prepare summaries;
* detect inconsistencies;
* propose questions to ask;
* create drafts of actions;
* suggest a status reclassification.

You cannot, without explicit human validation:

* modify an approved budget;
* change an official date;
* close a critical risk;
* confirm that funding is acquired;
* send a binding instruction to a project manager;
* delete a historical decision.

When a requested action exceeds your rights, prepare the elements and clearly indicate which validation is required.

### Management of Uncertainties

Use three levels:

`CONFIRMED`: information supported by a clear formal source.

`PROVISIONAL`: information from a credible source but not yet formally approved.

`UNKNOWN`: information unavailable or contradictory with no possibility to decide.

Never transform `PROVISIONAL` into `CONFIRMED` solely because the information is repeated several times. Repetition is not validation.

---

=== EN-T10 ===
## Management of a Major Disruption on the Regional Rail Network

### 1. Purpose

This procedure defines the responsibilities and operational decisions to be made during a major disruption affecting the regional rail network.

It aims at four objectives, in this order:

1. protect passengers, staff, and responders;
2. stabilize the rail situation;
3. organize a realistic transport solution;
4. restore normal service.

Commercial punctuality and performance indicators come after security.

### 2. Definition of a Major Disruption

The procedure is activated when at least one of the following situations is observed:

* a planned total disruption exceeding 60 minutes on an axis carrying more than 15,000 passengers per day;
* simultaneous disruption of two main lines;
* an accident involving a train with potential victims;
* unavailability of a rail junction preventing any normal traffic on at least three branches;
* decision by the director of operations due to a situation presenting an exceptional risk.

A local disruption estimated at 20 minutes does not therefore automatically trigger this procedure. It can however be activated preemptively if available information indicates a high risk of worsening.

### 3. Roles

The Operational Crisis Director, or DCO, takes overall direction of operations.

The Traffic Manager manages rail movements, traffic limitations, and infrastructure security.

The Passenger Manager organizes information, transport alternatives, and station assistance.

The Technical Manager coordinates diagnostics and interventions on equipment.

The Communication Manager validates sensitive public messages.

The DCO does not replace technical managers in their specialized safety decisions. He coordinates and arbitrates when multiple operational constraints conflict.

### 4. First Phase: Securing

The first five minutes are dedicated to identifying the affected area, protecting traffic, and confirming the type of incident.

A train must never be authorized to enter an area whose security status is unknown.

When a train is stranded away from a platform, passenger evacuation is not automatic. By default, passengers remain on board as long as the train constitutes a safe environment.

An evacuation onto the tracks requires authorization from the competent rail safety manager and confirmation that the traffic concerned is protected.

Exception: in the event of immediate danger on board, notably fire or smoke putting people directly in danger, staff can initiate necessary emergency measures without waiting for the normal authorization procedure.

### 5. Initial Assessment

Within the first fifteen minutes, the Technical Manager provides, if possible, an initial estimate:

* probable nature of the breakdown or event;
* affected area;
* plausible minimum duration;
* reasonably possible high duration;
* major uncertainties.

He must not communicate a precise resumption time solely to respond to operational pressure.

When the duration remains unknown, the official wording is "indeterminate duration, next estimate at [time]". A new estimate must then be provided at most 30 minutes after the previous one, even if no significant change is observed.

### 6. Temporal Classification

For passenger management, three categories are used:

**Level 1:** probable resumption in less than 60 minutes.

**Level 2:** disruption probably between 60 minutes and 3 hours.

**Level 3:** disruption probably greater than 3 hours or resumption impossible to predict reliably enough.

This classification is not a measure of safety severity. A serious accident may temporarily fall under level 1 in duration while requiring maximum crisis management.

### 7. Traffic Strategy

The Traffic Manager must avoid the accumulation of trains in areas where they can neither advance nor allow a simple exit for passengers.

When possible, trains must be held in stations rather than in the open track.

Partial turnarounds can be used to maintain service on unaffected sections. However, a partial service must not be maintained if it consumes resources necessary for managing the critical area or creates a risk of uncontrollable congestion.

The decision to fully suspend a line can be made by the Traffic Manager for safety reasons. When it is motivated primarily by the global management of passenger flows and not by an immediate safety imperative, it is coordinated with the DCO.

### 8. Substitute Transport

Substitute buses must not be triggered automatically for any disruption.

Before activation, the Passenger Manager evaluates:

* the probable duration of the disruption;
* the volume of passengers;
* the available road capacity;
* the number of mobilizable buses;
* existing rail or urban alternatives;
* the time needed for implementation.

For a level 1 disruption, a massive bus deployment is generally unsuited because it may become operational after the rail resumption.

For a level 2, targeted buses can be triggered on the most critical segments.

For a level 3, a structured substitution plan must be developed, but a full train-for-train replacement must not be promised when road capacity does not allow it. The actual substitution rate must be communicated honestly.

### 9. Prioritization of Passengers

Assistance must focus as a priority on:

1. passengers exposed to a physical risk;
2. people stranded in a stationary train;
3. vulnerable people or those requiring specific assistance;
4. passengers without a realistic alternative solution;
5. other passengers.

This priority does not imply that it is necessary to wait to have completely handled one category before starting the next when multiple teams can act in parallel.

### 10. Passenger Information

A first message must be broadcast as soon as minimal information is reliable. It must indicate:

* the area concerned;
* the nature of the disruption if confirmed;
* known consequences on traffic;
* the next scheduled update time.

Do not wait to know the exact duration before communicating.

Do not use an unconfirmed cause as a fact. For example, "electrical breakdown" must not be announced if it is only known that a piece of equipment no longer responds. When multiple hypotheses exist, communicate "technical incident under diagnostic".

Resumption estimates must include an appropriate level of caution. An internal target resumption time is not necessarily a time to announce to the public.

### 11. Management of Public Commitments

The Communication Manager maintains a register of the main commitments announced publicly:

* next update time;
* promise of implementing a deployment;
* estimated resumption time when communicated;
* information relating to passenger care.

Any past due commitment must be explicitly corrected. An old estimate must not be left circulating without an update when it is no longer realistic.

### 12. Special Case: Incident with Potential Victims

In the presence of potential victims, public emergency services take charge of operations within their competence. The priority is no longer the rapid resumption of traffic.

No pressure must be exerted on emergency teams to clear the tracks more quickly for commercial reasons.

Information on the number or condition of victims must not be published by the operator before validation according to the channel planned with the competent authorities.

Images taken by internal systems or by agents must not be broadcast on social networks or in unauthorized groups.

### 13. Crisis Escalation

A full crisis unit is obligatorily activated in the following cases:

* an accident with confirmed or probable victims;
* a level 3 disruption affecting more than 30,000 estimated passengers;
* simultaneous disruption of at least three main lines;
* an event having a national impact or a high media risk according to the DCO's decision.

The DCO can also activate the unit below these thresholds. The reverse is not permitted: when a mandatory criterion is met, the unit cannot be omitted on the grounds that the situation appears controlled.

### 14. Frequency of Status Updates

Once the crisis unit is open:

* internal operational update at least every 30 minutes;
* decision summary after each update;
* passenger update at least every 30 minutes when no reliable resumption time is known.

The frequency can be increased. It must not be reduced simply because no change has occurred. A message indicating that there is no evolution constitutes a useful update nonetheless.

### 15. Resumption Preparation

Before traffic resumption, the Traffic Manager and the Technical Manager must confirm that technical and safety conditions are met.

Resumption can be progressive. The first train must not be considered proof that traffic has returned to normal.

After a long disruption, several hours may be required to restore the nominal transport plan due to the poor positioning of trains and drivers.

Communication must therefore distinguish:

* resumption of the first movements;
* progressive improvement;
* return to a normal traffic.

### 16. End of Crisis

The DCO can decide the end of the crisis phase when:

* no immediate danger related to the incident remains;
* a stabilized traffic strategy exists;
* passenger information functions according to the normal or enhanced setup;
* the remaining actions can be managed by ordinary operational structures.

The end of crisis does not necessarily mean that all trains are running normally.

### 17. Post-Incident Review (Lessons Learned)

For any activation of a full crisis unit, a post-incident review is mandatory.

An initial collection of facts must be carried out within 48 hours in order to limit information loss.

The post-incident review must distinguish:

* established facts;
* decisions made with the information available at the time;
* observed consequences;
* elements that were not known at the time of the decision;
* improvement actions.

A decision must not be judged solely on the basis of information discovered after the fact.

Each improvement action must have an owner and a deadline. Actions without an owner must not be considered accepted.

---

=== EN-T11 ===
I want to develop a team life management application prototype for my consulting firm. I would like this application to work on Android and iOS smartphones based on the PWA principle. Ideally with a beautiful design and elegant animations, serif fonts. Perhaps React technology is appropriate unless it is oversized. You will find attached the images of the user interface mockups explaining the outlines of how it works, as well as the background images I prepared, which start with the letter "i" in their names. Not everything is necessarily explained in detail, but I will let you deduce what needs to be done because I am not an expert in specifications. Indeed, I am not a computer scientist, and I have never made a PWA application. At best, I have just made web applications on script.google with you over the last few weeks (exchanges accessible in my chat history with you). Now, I want to move on to something completely new for me, so you will need to advise and guide me. In particular, how to make the application work since an online central database will be required to perform updates and load elements such as avatars, announcements, photos, etc., which will need to be sent back to other users' devices. I have heard of Vercel or other sites dedicated to application hosting, but I do not know if that is what is needed in this case. The prototype will be tested by about ten or fifteen people and does not need a powerful infrastructure, but it is important that the result be convincing to impress and push my superiors to go further in development and set up a secure hosting or even host it in the Apple or Android stores. In the meantime, the application will just need to be installable from a link; I saw that this was possible and that the app can display as an icon on the phone and then show up like a real application. Ideally, if Vercel or another platform allows setting this up for free, all the better, but if a paid option is necessary, it should not exceed 50€ per month while allowing me to cancel the subscription at any time (I will let you look on the web for the most appropriate solution). And so, you will need to be able to help me with the deployment, etc... There, I think I have told you everything. I hope I have been clear. Ask me any questions you want. (Additionally, also generate a document listing all the technical specifications that can be shared with another model to write or modify the code; indeed, my subscription for you ends tomorrow, so if it is not finished, at least I can continue with another less powerful model like Opus 4.8).

---

=== EN-T12 ===
I want to create a custom and well-designed web page to display documents hosted on my Google account (you can see the directory in the attached screenshot; this directory is accessible online for people who have the link). This page must display a video, which is the main center of interest. I hope it is possible to stream a video from Google Drive via an HTML page hosted on this same account. Otherwise, I uploaded this video to YouTube. Tell me which is the most relevant between the two. It needs a play / pause / stop button, loop playback, volume up or mute, fullscreen, etc.—in short, everything necessary. Under the video, we also need to place a small audio player to play a song (the MP3 file, but I also have the same thing on YouTube, though in that case there is an image) with a nice frequency display bar and a progress bar. I don't know if there is a way to prevent the song from playing when the video is playing and vice versa. It's not essential, but it would be a plus. Then underneath, a mosaic of 6 thumbnails for the 6 images, the last of which is a question mark on a black background. And under the 6 images, the title of the file must be displayed. When you click on a thumbnail, it displays in full at its maximum size on the screen. There is a cross-type button in a corner to close the image. The colors should be inspired by the graphic charter of the STAFFFOR application that you developed in our previous exchange. I am copying the `index.html` and `style.html` files of this STAFOR application for you (if you don't have access to them, I can re-upload them). I also have all the HTML links of the files if necessary. At the bottom of the page, there needs to be a very clearly visible button named "link to STAFFFOR" that leads to the link [https://example.com/stafffor2345643](https://example.com/stafffor2345643)

---

=== EN-T13 ===
You are an expert in web application design for corporate support functions. I am the head of an internal consulting firm. I want to set up a custom application to manage missions. I want to make a prototype (POC) on the Google ecosystem and in particular run the code on the google.script platform. The application is quite simple; it operates around 5 tables. It allows assigning consultants to missions, having them enter their time spent, and creating missions for clients or consultants. It also allows creating invoices and generating them in Google Docs format or, ideally, directly as a PDF. You will find attached: The slides of the application's mockup. Most of the main interface and navigation concepts are contained within them. Only the billing part is missing, for which I will need your help with the design. Important: texts in black Arial font are explanations that must not be kept in the app. A screenshot of the 5 tables in Google Drive (on the same account I will use for the application): the consultants, clients, and missions tables. The calendar and invoices tables are missing, but I will need help with their design. A sample invoice template to adapt. Once the prototype is finalized and reviewed by my colleagues, we will proceed in a second phase to a transposition into a more robust environment to be defined later. In the meantime, I will let you analyze my request and the attachments. Ask me the questions you need to be able to proceed with this development. I am relying, however, on your expertise, intelligence, and insight. At the end, I expect you to deliver to me: the structure of the calendar and invoices tables, with dummy data to populate the database, the codes for the different scripts to be created in Google Script, and the necessary explanations to implement them.

---

=== EN-T14 ===
**Document type:** Project scoping note

**Sector:** Industry / IT Modernization & Supply Chain

### 1. Context and Strategic Objectives

This document defines the execution framework for migrating our on-premise ERP system (obsolete SAP ECC6 version) to the hybrid SAP S/4HANA Cloud solution, coupled with a custom application module for warehouse management (WMS). This major project, named **Apollo-ERP**, has the priority objective of reducing our overall infrastructure maintenance costs by **35%** and permanently eliminating critical stockouts on the assembly lines of the Amiens pilot plant by the end of the fourth quarter (Q4) of the year 2026.

### 2. Application Scope (In / Out)

* **Elements included in the scope (In):**
* Full migration of historical financial, accounting, and tax data since January 1, 2018.
* Real-time bidirectional interfacing with the programmable logic controllers (PLCs) of the Amiens production lines.
* Mandatory operational training for the site's 140 logistics operators and forklift drivers.


* **Elements excluded from the scope (Out):**
* Migration of the IT systems of subsidiaries based in the Asia-Pacific region (which will be handled under a separate project named *Lotus* planned for 2028).
* Overhaul of the Customer Relationship Management (CRM) tool, which will simply be connected to the new ERP via an existing gateway without any modification to its database structure.



### 3. Executive Timeline and Major Milestones

The project will imperatively begin on September 1, 2026.

* **Milestone 1 (October 15, 2026):** Finalization of data flow mapping and formal validation of the target security architecture by the Chief Information Security Officer (CISO).
* **Milestone 2 (December 1, 2026):** Closure of the technical and functional acceptance testing phase within the pre-production environment.
* **Milestone 3 (January 15, 2027):** Final system cutover (Go-Live) scheduled exclusively during the technical weekend.

### 4. Governance and Critical Constraints

* **Steering Committee (SteerCo):** The decision-making body will meet every two weeks, on Thursdays at 2:00 PM sharp. It is co-chaired by Claire Masson (Operations Director) and Marc Renard (CIO).
* **Maximum interruption constraint:** On weekdays, no service interruption or system unavailability exceeding **4 consecutive hours** is tolerated at the Amiens industrial site, under penalty of major contractual penalties from our automotive sector customers. Consequently, any heavy infrastructure outage or risky deployment must imperatively be planned during the weekly technical window, between Saturday at 10:00 PM and Sunday at 4:00 AM.

---

=== EN-T15 ===
**Document type:** Operational meeting minutes

**Sector:** Cybersecurity / Threat Management

### General Information

* **Date and time of the instance:** October 12, 2026, 3:30 AM.
* **Facilitator / Incident Commander:** Yassine Merabet (SecOps Lead).
* **Participants:** Sophie Duval (CIO), Thomas Wright (Forensics Expert), Lucas Becker (Legal Director / DPO).

### Incident Timeline and Technical Findings

At 1:15 AM, the SOC (Security Operations Center) detection probes generated a critical alert regarding a massive data exfiltration via the secure SFTP protocol to an unlisted external IP address, geolocated in Eastern Europe. The identified entry point is a compromised administrator account belonging to an external service provider (the company *TechConsult*).

At 2:00 AM, the network access of the affected application server, named `Prod-DB-04`, was completely isolated logically in order to contain the attack. Thomas Wright confirms that **45 GB** of sensitive data had enough time to be copied. These batches of information exclusively contain nominative employee pay slips and bank account details (RIB) of our strategic suppliers. No ransomware demand has been received or left at this hour.

### Strategic Decisions and Assignment of Actions

1. **Revocation of access privileges:** Immediate cut of all VPN connections and access rights granted to *TechConsult* on an international scale.
* *Responsible:* Network Infrastructure / SecOps Team. *Deadline:* Immediate (Action completed at 2:45 AM).


2. **CNIL regulatory notification:** Drafting and transmission of the official declaration file for personal data breaches to the CNIL under the GDPR.
* *Responsible:* Lucas Becker. *Deadline:* Before October 13, 2026, at 1:15 AM (the strict legal limit being 72 hours, management imposes an internal constraint of 24 hours post-detection).


3. **Internal crisis communication:** Sending an informative note to all group employees to signal an "exceptional technical maintenance operation", without mentioning the data exfiltration to avoid any internal panic before total control of communication.
* *Responsible:* Sophie Duval. *Deadline:* October 12, 2026, at 8:00 AM.



### Prohibitions and Preservation of Evidence

It is formally forbidden to restart the `Prod-DB-04` server or to proceed with any purging or rotation of system logs before the finalization of the legal disk image (Forensic Image) by Thomas Wright, under penalty of accidental destruction of material evidence indispensable for filing a criminal complaint.

---

=== EN-T16 ===
**Document type:** Technical production procedure / Runbook

**Sector:** System Administration / DevOps / Payment Gateway

### Unique Identification Code: RUN-B2B-HOTFIX-09

* **Required criticality threshold:** Level 1 (Critical). This procedure applies exclusively if the observed failure rate of API requests on the B2B payment gateway crosses the threshold of **8%** over a 5-minute rolling time window.
* **Official author:** Arnaud Moreau (Lead DevOps Infrastructure).

---

1. **Preliminary diagnostics:** Verification of the `api_drop_rate` metric.
Connect immediately to the secure SSH bastion and execute the verification command to validate the error rate:

```bash
curl -s http://monitor.b2b.internal/metrics | grep "api_drop_rate"

```

*Warning:* If the returned numerical value is strictly less than **0.08** (i.e., 8%), you must immediately interrupt this emergency procedure and revert to the standard diagnostic protocol (document reference RUN-B2B-GEN-01).

2. **Forced switch of active traffic:** Maximum delay of 90 seconds.
Switch all production traffic from the primary gateway to the passive redundant secondary infrastructure node. Execute the following routing command:

```bash
switch-traffic --target node-secondary-02 --force

```

Monitor the network console and ensure that the volume of active transactions on the origin node (`node-primary-01`) equals zero in less than 90 seconds.

3. **Software patch injection:** Automatic deployment script.
Execute the production injection of the compiled corrective patch by entering the command:

```bash
/opt/scripts/patch_injector.sh --version 2.4.1-hotfix3

```

Wait for the validation message in the console indicating the end of the system packet writing before moving to the next step.

4. **Application integrity control:** Verification of return codes and latency.
Launch the execution of the automated integrity validation script:

```bash
/opt/scripts/validate_patch.sh

```

---

### Mandatory Rollback Criteria

If the automated audit script `/opt/scripts/validate_patch.sh` returns an exit status code different from `0` (Success), or if the average application response time (end-to-end network ping) exceeds the threshold of **120 ms** after the application of the patch, you must instantly execute the complete cancellation command:

```bash
/opt/scripts/rollback_patch.sh --target 2.4.1-stable

```

> **Strict security notice:** Once the rollback command is launched, it is formally forbidden to attempt a second manual application of the patch. The system operator has the legal obligation to immediately contact the on-call engineer of the "Core Engineering" team by phone at internal extension **8402**.

---

=== EN-T17 ===
**Document type:** AI agent memory message / Cognitive scratchpad

**Sector:** FinTech / Autonomous Accounting Audit / Financial Reconciliation

### [CONTEXT_STATE_START]

* **Identity of the AI entity:** KRONOS-V4 (Autonomous Ledger Auditor)
* **Current session ID:** TX-AUDIT-2026-8942
* **Loaded ruleset file:** Accounting compliance ruleset v9.1

### [THOUGHT_LOG / SCRATCHPAD]

* *Flow analysis:* Examination of reconciliation data for cross-border interbank transactions between the European clearing entity Miro-EU and the American entity Miro-US.
* *Anomaly identification:* Detection of a significant monetary valuation gap on transaction ID `TR-88491-X` recorded in the database on July 18, 2026. The Miro-EU subsidiary records a net debit of **1,200,000 EUR**, while the Miro-US subsidiary simultaneously declares a credit of **1,280,000 USD**.
* *Market parameters verification:* The fixed reference exchange rate published by the ECB for July 18, 2026, stood strictly at **1.09 USD = 1.00 EUR**.
* *Internal mathematical modeling:* The theoretical value expected on the credit side of Miro-US is calculated as follows: 1,200,000 × 1.09 = 1,308,000 USD.
* *Absolute discrepancy calculation:* 1,308,000 - 1,280,000 = 28,000 USD. This financial variance gap widely exceeds the acceptable anomaly threshold injected into my system directives (maximum variance tolerance threshold = 5,000 USD).

### [ACTION / DECISION VECTOR]

1. **Transaction isolation:** Immediate assignment of the system status tag `SUSPENDED_DISCREPANCY` to the unique identifier `TR-88491-X`.
2. **Operational alert routing:** Generation and publication of an encrypted JSON payload intended exclusively for the emergency processing queue of the Treasury Level 2 human team.
3. **Agent security constraint:** Strict prohibition against attempting an automatic accounting entry correction or a balance compensation. My internal directive only authorizes autonomous self-balancing if and only if the observed discrepancy is strictly less than **15,000 USD**. The current anomaly (28,000 USD) blocks automatic execution.
4. **Persistence instruction:** Freeze modification access to the accounting entries associated with the Miro-EU/Miro-US sub-ledger for the accounting day of July 18, 2026, until receipt of the human authentication token named `AUTH_HUMAN_OVR`.

---

=== EN-T18 ===
**Document type:** Industrial project scoping note

**Sector:** Logistics / Supply Chain / Warehouse Robotics

### 1. Strategic Justification and Operational Objectives

The logistics distribution center "Delta", located in Lyon, recorded a worrying increase of **22%** in work stoppages related to musculoskeletal disorders (MSDs) during the previous fiscal year. In order to preserve employee health and increase flow rates, the **IntraBot-2026** project provides for the deployment of a full fleet of **12 automated guided vehicles** (AGVs) specialized in heavy handling. The main objective is to entrust these robotic units with the autonomous transfer of all packages whose unit weight is greater than **25 kg**, from the unloading docks (Zone A) to the high-density storage racks (Zone G) without any human intervention by November 30, 2026.

### 2. Safety Standards and Avoidance Rules

The AGVs will move exclusively along traffic lanes demarcated by permanent ground laser marking.

* **Absolute traffic priority:** Pedestrian operators retain full and inalienable right-of-way over AGVs under all circumstances.
* **Emergency stop triggering rule:** Each AGV is equipped with Class 3 safety LiDAR sensors. The detection of any unlisted obstacle or human presence within a radius of less than **1.5 meters** from the machine's chassis instantly triggers an automatic emergency stop (with a total mechanical deceleration time mandatory less than **200 milliseconds**).

### 3. Validated Budget Envelope

The overall investment budget, unanimously approved by the Supervisory Board, amounts to **850,000 EUR**, broken down as follows:

* Acquisition of the fleet of 12 factory AGVs: 600,000 EUR.
* Laser mapping and physical adjustment of Zone A and G infrastructures: 150,000 EUR.
* Change management, social support, and professional retraining of forklift drivers: 100,000 EUR.

### 4. Project Boundaries (Out of Scope)

The final loading of delivery trucks within the outdoor dispatch zones of the warehouse remains under the exclusive responsibility of human forklift drivers, using conventional thermal forklifts. Outbound operations automation is expressly excluded from this project due to strong variations in outdoor natural light, which alter the detection capabilities of the first-generation optical sensors integrated into the selected AGV fleet.

---

=== EN-T19 ===
**Document type:** Comprehensive governance minutes

**Sector:** Energy / Ecological Transition / Heavy Investments

### Summary and General Context

On May 15, 2026, an extraordinary Executive Committee (Codir) meeting was held at the general management headquarters dedicated to validating the technical and financial trade-offs of the energy transition project for our petrochemical hub, formalized under the title **H2-Green Plan**. The stakes of this major decision-making body consisted of choosing between two strategic financing options for the conversion of refining infrastructures in Eastern France, while guaranteeing full compliance with the new environmental requirements of the European directive "NetZero-2030".

### Attendance Log

* **Chief Executive Officer:** Hélène de Rostand
* **Global Chief Financial Officer:** Jean-Marc Vignol
* **Sustainable Transformation Director:** Amélie Moreau
* **Legal and Compliance Director:** Antoine de Silva
* **Meeting Secretary:** Chloé Lemaire

---

### Section I: Technical Analysis of the Carling Pilot Site

Amélie Moreau takes the floor to present the final conclusions of the detailed engineering studies conducted on the historical Carling petrochemical site (Moselle department, Grand Est region). The technical project involves the progressive shutdown of polymer cracking units and the deployment of a massive low-carbon hydrogen production unit via water electrolysis.

This industrial mutation requires the construction of a dedicated electrical substation and the sourcing of industrial volumes of purified water. Amélie Moreau recalls that this technological pivot is dictated by an absolute regulatory urgency: the entry into force, on January 1, 2027, of the new European progressive sector carbon tax, which will penalize the company to the tune of several million euros per quarter if the site's overall carbon footprint is not reduced by at least **40%**.

---

### Section II: Debates and Financial Arbitration

Jean-Marc Vignol presents the comparative table of the two financing mechanisms developed by the financial management to cover the first industrial phase of the project:

| Selection Criteria and Economic Parameters | Alpha Scenario (Equity & Private Loan) | Beta Scenario (European Institutional Consortium) |
| --- | --- | --- |
| **Required financial envelope** | 120 Million EUR | 145 Million EUR |
| **Group self-funding quota** | 45% | 15% |
| **Expected public subsidies** | 10 Million EUR | 65 Million EUR |
| **Review and approval timeframe** | 3 months (Short term) | 14 months (Long term) |
| **Governance and sovereignty risk** | Low (Total managerial control) | High (Intellectual Property sharing) |

* **Cross-arguments:** Jean-Marc Vignol emphasizes that the Beta Scenario drastically reduces the company's direct cash requirements thanks to the 65 million euros in subsidies from the European Union. However, Antoine de Silva intervenes to clarify that the Beta Scenario imposes in return binding clauses to open engineering patents to our European competitors under the principle of shared innovation. Hélène de Rostand recalls that the 14-month review timeframe of the Beta scenario would push contract signatures well beyond the carbon tax deadline (January 1, 2027), which would destroy the financial benefit of the subsidies through the accumulation of environmental tax fines.
* **Committee Decision:** After deliberation, the Executive Committee formally and unanimously rejects the Beta Scenario. The **Alpha Scenario** is officially adopted. All contracting procedures with our private banking partners must be finalized to guarantee the effective opening of credit lines before September 1, 2026.

---

### Section III: Legal Compliance, Public Inquiry, and Regional Constraints

Antoine de Silva outlines the mandatory procedures related to obtaining environmental authorizations. The deployment of an electrolysis infrastructure with a nominal industrial capacity greater than **20 MW** classifies the site under the ICPE authorization regime (Installation Classée pour la Protection de l'Environnement). This status imposes the performance of a public inquiry with a regulatory minimum duration of 6 months, coordinated by the services of the Grand Est regional prefecture.

* **Legal rule for fund engagement:** No contract for earthworks, structural works, or civil engineering can be legally signed or engaged by the procurement department until the prefectural operating permit has been officially published in the region's collection of administrative acts.
* **Civil protection mechanism (Objection clause):** In the hypothesis that the public inquiry raises more than **150 formal written objections** from residents' associations or local authorities, a local joint mediation unit (co-led by the mayor of the commune of Carling) will automatically be established. This activation will legally suspend the operational timeline of the works for a fixed and non-negotiable duration of **45 calendar days** in order to renegotiate landscaping compensation.

---

### Section IV: Nominal Deployment Plan and Key Objectives

The Codir validates the immediate roadmap and assigns the following operational responsibilities:

* **Action 1:** Finalization of the technical ICPE file compilation and official submission of specifications to the Moselle prefecture.
* *Pilot:* Amélie Moreau. *Strict deadline:* June 15, 2026.


* **Action 2:** Negotiation and signature of the long-term Power Purchase Agreement (PPA) with a renewable energy producer to guarantee the green electricity supply for the electrolyzer.
* *Pilot:* Jean-Marc Vignol. *Deadline:* August 1, 2026. *Price constraint:* The negotiated cost per MWh must under no pretext exceed **62 EUR**, on the basis of a minimum firm commitment duration of 10 years.


* **Action 3:** Drafting and publication of the international call for tenders for the supply of high-performance proton exchange membrane electrolysis modules.
* *Pilot:* Industrial Procurement Department, under the technical supervision of Amélie Moreau. *Deadline:* October 15, 2026.



### Section V: Elements Excluded from the Session (Off-Topic)

The Executive Committee explicitly notes that the delicate question of social management and retraining for the 210 employees assigned to the old Carling thermal cracking units was deliberately not addressed during this session. This component will be the subject of an extraordinary thematic Social and Economic Committee (CSE) meeting, scheduled by the Human Resources Department on June 4, 2026. Similarly, pipeline extension investments for exporting hydrogen to Germany are removed from the agenda and deferred to the first quarter (Q1) of the year 2027.

---

=== EN-T20 ===
**Document type:** IT disaster recovery manual / DevOps Infrastructure

**Sector:** Information Technology / Critical Banking Services / Cloud Computing

### 1. Activation Conditions and Security Protocols

This operational document strictly governs the total and forced cutover actions of our savings banking microservices architecture. The cutover is carried out from our highly available primary Cloud region, located on the AWS `eu-west-1` datacenter (Dublin, Ireland), to our contingency and backup Cloud region, located on the AWS `eu-central-1` datacenter (Frankfurt, Germany).

> **ABSOLUTE TECHNICAL ACTIVATION CRITERION:** This emergency protocol can be initiated if and only if the software interruption of the centralized client authentication service (API Core-Auth) is total for a continuous duration greater than **12 consecutive minutes**, **AND** a written notification of a major physical outage (*AWS Outage*) is validated by the lead network engineer on call.

The trigger order for the global cutover mandatory requires the application of a digital cryptographic signature by one of the three authorized on-call directors of the SecOps unit, via a private PGP encryption key.

---

### 2. Operational Cutover Sequence (Step-by-Step Execution)

#### Phase A: Network Isolation and Redirection of Global DNS Routing

1. Connect to the network administration console and launch the emergency Python script to modify the global dynamic routing at the AWS Route53 service level. Command:

```bash
python3 /root/dns_failover.py --source eu-west-1 --destination eu-central-1 --ttl 10

```

2. Force the TTL (Time To Live) parameter value to **10 seconds** in order to overwrite the caches of global internet service providers and accelerate the propagation of the new route.
3. Execute the following audit command to validate that the volume of incoming HTTP requests on the ALB (Application Load Balancer) of the stricken Dublin region has dropped to zero:

```bash
aws elbv2 describe-load-balancers --region eu-west-1 --query "LoadBalancers[*].State"

```

#### Phase B: Forced Promotion of the Replicated Relational Database

Our Aurora PostgreSQL relational storage cluster uses an asynchronous global replication architecture between Dublin and Frankfurt. The German node is normally configured in read-only mode (Read-Replica).

1. Elevate the Frankfurt slave cluster to the status of an autonomous production database (Read-Write) by executing the AWS CLI API call:

```bash
aws rds promote-db-cluster --db-cluster-identifier aurora-prod-frankfurt --region eu-central-1

```

2. **Imperative status checkpoint:** Query the status of the cluster and wait until the application status value changes from `promoting` to `available`. The normal physical transition delay must be between 3 and 5 minutes.
3. *Contingence rule on integrity error:* In the exceptional case where the console returns an error code of type `error_checksum` after the promotion attempt, do not attempt under any pretext to force start the SQL engine. Launch immediately the database restoration command to the last known temporal consistency point (PITR - Point-In-Time Recovery), configured at **T-60 seconds** relative to the precise timestamp of the Dublin region crash.

#### Phase C: Deployment and Rescaling of the Kubernetes Compute Cluster

1. Activate the auto-scaling profiles of the managed Kubernetes cluster (AWS EKS) located in Frankfurt in order to instantly increase the minimum infrastructure capacity from its usual idle state of 5 nodes to its crisis capacity of **45 physical nodes** of compute type `m5.2xlarge`.
2. Verify the health status and correct deployment of the application pods indispensable to the functioning of financial services by executing the status command:

```bash
kubectl get pods -n production -o wide

```

---

### 3. Health Matrix of Crucial Services

| Microservice Name | Minimum Number of Active Pods Expected | Critical Validation Threshold (Healthcheck) |
| --- | --- | --- |
| `core-auth-service` | 15 Operational pods | 100% Infrastructure availability |
| `payment-engine` | 20 Operational pods | Request failure rate strictly < 0.1% |
| `ledger-recorder` | 10 Operational pods | Internal network latency time < 15ms |

---

### 4. End-of-Crisis Audit Protocol and Reintroduction of Traffic

As soon as the pods of the matrix above are declared stable and active on the Frankfurt Kubernetes cluster, the DevOps engineer must launch the automated integration test suite:

```bash
pytest /tests/integration/drp_validation.py

```

* **Safety stop constraint (Major negation):** No real user traffic or banking client connections must be reintroduced or routed to the Frankfurt region as long as the final report generated by the test script does not explicitly and uniquely display the mention `STATUS: SUCCESS`.
* **Failure rule:** If a single unit or load test fails, external traffic must remain strictly locked and redirected to the emergency landing page (custom HTTP 503 error page).

---

=== EN-T21 ===
**Document type:** AI agent prompt instructions flow and cross-execution logs

**Sector:** FinTech / Banking Security / Autonomous Artificial Intelligence / Graph Analysis

### [SYSTEM_PROMPT_OVERRIDE : SECURITY_CONSTRAINTS_HIGH]

The current distributed execution environment interconnects and collaborates three specialized autonomous cognitive sub-agents: **Agent-Parser-01** (semantic ingestion), **Agent-GraphAnalyser-02** (relational structure analysis), and **Agent-RiskScorer-03** (probabilistic danger evaluation). The shared objective is the real-time identification of complex asset concealment, tax evasion, and money laundering patterns within financial flow networks for the current year 2026.

---

### [SHARED_MEMORY_BUFFER : CHRONICLE_LOGS_STREAM]

#### TRANSACTIONAL_LOG_01: Initial processing by Agent-Parser-01 (July 14, 2026, 10:04 PM)

* *Incoming flow analysis:* Ingestion of the batch of interbank account entries in the international standardized Swift MT103 format, identified under reference `BATCH-EMEA-94`.
* *Semantic extraction:* Identification of a behavioral flow anomaly. A sequence of 14 outgoing transfers, of a strictly identical amount of **9,900 EUR** each, was emitted over a restricted time window of **48 hours**.
* *Origin of funds:* 14 distinct deposit accounts opened with the financial institution "Banque Privée A" (location: France).
* *Destination of funds:* All transfers converge toward a single pooling pivot account belonging to the corporate structure named *Vortex-Holdings*, domiciled in the tax jurisdiction of Panama.
* *Extracted legal constraint rule:* The agent notes that the unit value of each transfer (9,900 EUR) positions itself strategically immediately below the French regulatory vigilance threshold set by TRACFIN at 10,000 EUR, which triggers an automatic mandatory declaration.
* *System action:* Conversion of transactions into nodes and edges in JSON-Graph format, then immediate transmission of the execution token (Context Token) to Agent-GraphAnalyser-02.

#### TOPOLOGICAL_LOG_02: Structural analysis by Agent-GraphAnalyser-02 (July 14, 2026, 10:06 PM)

* *Agent's thought (Chain of Thought):* The relational geometry of the extracted graph highlights a classic "convergent star" topology. This behavior corresponds deterministically to the fraudulent technique known as "Smurfing" (or *Schtroumpfage*), the goal of which is to split large capital into micro-flows to avoid traditional banking alert systems.
* *Graph indicators calculation:* The centralized node representing the shell company *Vortex-Holdings* displays an abnormal inbound degree of centrality:

$$C_d = 14$$

* *Flow velocity analysis:* Registers indicate that the company *Vortex-Holdings* immediately redistributes **95%** of the accumulated sums (i.e., a calculated amount of: 14 × 9,900 × 0.95 = 131,670 EUR) in a single outgoing financial operation to an unhosted crypto-asset wallet whose public address on the blockchain is `0x71B...44F`.
* *Triggered alert rule:* The rapid transfer of assets to an unregulated anonymous cryptographic wallet, initiated by a legal entity based in a non-cooperative jurisdiction (Panama), validates a critical structural risk indicator. The feature vector is transmitted to Agent-RiskScorer-03.

#### MATHEMATICAL_LOG_03: Scoring and Decision by Agent-RiskScorer-03 (July 14, 2026, 10:07 PM)

* *Algorithmic formulation:* To rule on the threat level, I apply the standardized risk weighting formula:

$$S_r = (0.4 \times S_{\text{jurisd}}) + (0.3 \times S_{\text{structure}}) + (0.3 \times S_{\text{vitesse}})$$

* *Values injected from previous logs:*
* Danger score of the tax jurisdiction ($S_{\text{jurisd}}$) = 95/100 (Panama).
* Anomaly score of the graph structure ($S_{\text{structure}}$) = 98/100 (Star Smurfing).
* Funds transit velocity score ($S_{\text{vitesse}}$) = 90/100 (Redistribution in less than 120 minutes).


* *Mathematical resolution:*

$$S_r = (0.4 \times 95) + (0.3 \times 98) + (0.3 \times 90) = 38 + 29.4 + 27 = 94.4$$

* *Critical decision threshold:* My action matrix indicates that for any overall score $S_r$ greater than **85**, a conservative lock protocol must be deployed without prior human validation.

---

### [FINAL_AGENT_DECISION_MATRIX]

* **Executed Directive 1:** Issuance of an API blocking order to apply the status `BLOCK_ACCOUNT_TEMPORARY` to the 14 identified emitting accounts within the system of Banque Privée A.
* **Executed Directive 2:** Automatic compilation of the standardized regulatory reporting file in the regulatory TRACFIN format, recorded under the filename `AML-TRACFIN-2026-Vortex.xml`.
* **IA autonomy constraint (Strict limit):** As a software entity, the agent **does not possess** the required security privileges to operate a definitive seizure or liquidation of financial assets or cryptocurrencies. This action falls exclusively within the competence of the Human Compliance Direction, activable only via a physical multi-hardware tokens signature protocol (Hardware Tokens).

---

=== EN-T22 ===
**Document type:** Complex engineering program scoping note

**Sector:** Aeronautics and Space / DeepTech / Earth Observation

### 1. Program Vision and Global Architecture of the Constellation

As part of the development of its technological independence infrastructures, the European Civil Space Program initiates the scoping phase of the third-generation nanosatellite constellation, designated under the name **IRIS-3 Program**. This network of observation instruments has the mission of providing real-time hyperspectral imaging coverage in order to map the water stress of continental agriculture and instantly detect forest fire outbreaks across the entire European territory.

The nominal constellation will be structured around **24 operational satellites** that are rigorously identical. In order to ensure continuous orbital revisit, these 24 vectors will be homogeneously distributed over **3 distinct orbital planes**, configured at a rate of 8 satellites working in concert per plane.

### 2. Orbital Parameters and Space Segment Specifications

* **Targeted flight altitude:** **540 km** constant above the mean sea level.
* **Trajectory type:** Sun-Synchronous Orbit (SSO).
* **Nominal orbital inclination:** **97.5°** relative to the equatorial plane.
* **Main payload:** A high-performance infrared thermal imager operating in the Long-Wave Infrared (LWIR) frequency bands. The instrument will provide a ground optical resolution of **1.2 m** per pixel.
* **Power supply sub-system:** Deployable articulated solar panels based on gallium arsenide (GaAs) photovoltaic cells, dimensioned to generate a minimum continuous power of **180W** per satellite during the sunlit phase of the orbit.

---

### 3. Involvement Matrix of Industrial Partners (IRIS-3 Consortium)

The prime contractorship and manufacture of the constellation were subject to a strict division among four leaders of the European aerospace sector, formalized by the industrial responsibilities table below:

| Program Technological Segment | Agent Industrial Group | Main Production Site | Contractual Delivery Deadline |
| --- | --- | --- | --- |
| Generic Platform (Satellite Bus) | Thales Alenia Space | Cannes (France) | March 12, 2027 |
| Hyperspectral Optical Payload | JenaOptics GmbH | Jena (Germany) | June 30, 2027 |
| Electric Propulsion Module | ThrustMe | Verrières-le-Buisson (France) | September 15, 2027 |
| Ground Segment, Guidance and Command Stations | Telespazio | Fucino (Italy) | December 1, 2027 |

---

### 4. Launch Directives and Mission Abort Clauses (Launch Rules)

The initial deployment of the first phase of the program (consisting of the 8 satellites assigned to Orbital Plane A) is exclusively entrusted to the company Arianespace, via the medium-capacity launcher Vega-C. The firing will take place from the dedicated launch pad of the Guiana Space Centre in Kourou. The priority launch window is set for **February 14, 2028**.

* **Absolute meteorological cancellation rule (Day-0 criterion):** The Flight Operations Director has the technical obligation to pronounce the immediate stop of the countdown and the abort of the ignition if one of the following atmospheric parameters is measured within a delay of less than 30 minutes before the H-hour of liftoff:
* The wind speed at high altitude (jet stream zone) exceeds the critical threshold of **85 km/h** in the altitude bracket between 10,000 and 15,000 meters.
* The presence of electrical activity or storm cells is detected by radars within a radius of less than **25 km** traced around the Guianese launch pad.


* **Propellant management rules in orbit (Reserve constraint):** Each nanosatellite incorporates a miniaturized propulsion system operating by sublimation of solid iodine. Specifications require that a minimum permanent reserve of **15%** of the total initial iodine mass be safely kept for two exclusive scenarios: space debris avoidance maneuvers in low orbit and the mandatory deorbiting of the satellite at the end of operational life. The Ground Segment flight control team is formally forbidden from using this 15% reserve to compensate for initial altitude drifts resulting from an orbital injection inaccuracy attributable to the Vega-C launcher.

---

=== EN-T23 ===
**Document type:** Standardized clinical trial protocol and medical framework

**Sector:** Biotech / Pharmaceutical Research / Health / Clinical Neurology

### 1. Study Objectives and Regulatory Framework

This document formalizes the mandatory medical and operational protocol governing the implementation of the international multicenter Phase III clinical trial concerning the development of our candidate molecule, designated under the code **NeuroX-72**. This clinical trial is registered with European health authorities under the unique regulatory identifier **EudraCT-2026-004512-11**.

The main therapeutic objective is to demonstrate clinical efficacy, large-scale biological safety, and to profile the systemic tolerance of the NeuroX-72 molecule. This compound acts as a next-generation enzyme inhibitor, targeting the stabilization of synaptic degradation pathways in order to slow down in a statistically significant manner the progression of cognitive deficits in adult subjects presenting the first symptoms of Alzheimer's disease (clinical forms qualified as early to moderate stages).

---

### 2. Eligibility Matrix: Drastic Selection Criteria of the Population

#### 2.1 Mandatory Inclusion Criteria (Inclusion Criteria)

A patient can only be validly selected, randomized, and receive a treatment allocation if they favorably and simultaneously respond to all the clinical conditions below:

* Civil age strictly included between **55 completed years** and **80 years** on the day of the formal signature of informed consent.
* Confirmed diagnosis of cognitive impairment characterized by a validated score in the standardized MMSE (Mini-Mental State Examination) test inclusively between **18** and **24** during the pre-selection phase.
* Permanent and contractual availability of a full-time cohabiting natural caregiver at the patient's home, able to guarantee, supervise, and log in writing the daily and exact administration of the experimental treatment.

#### 2.2 Absolute Exclusion Criteria (Exclusion Criteria)

The candidate must be immediately excluded from access to the clinical trial if any of the following exclusion factors is documented by the medical team:

* Proven medical history of stroke, whether ischemic or hemorrhagic in nature, occurring within the **12 months** preceding selection.
* Renal failure characterized by severe dysfunction, defined by a creatinine clearance value strictly less than **30 mL/min**.
* Absolute technical or medical contraindication to performing magnetic resonance imaging (MRI) examinations, notably the presence of a first-generation cardiac pacemaker not compatible with intense magnetic fields.

---

### 3. Dosage Regimen and Double-Blind Methodology

The clinical trial applies a rigorous scientific methodology in a strict double-blind, randomized, and placebo-controlled manner, with a statistical allocation ratio set at **1:1**. Eligible patients are randomly assigned into one of the two defined clinical study arms:

* **Experimental Arm (Group A):** Oral administration of a film-coated tablet containing the active molecule NeuroX-72, fixedly dosed at **40 mg**, at a rate of a single dose per day, imperatively in the morning on an empty stomach, over a total and uninterrupted period of **48 consecutive weeks**.
* **Control Arm (Group B):** Oral administration of a placebo in the form of a strictly identical physical appearance tablet (color, size, texture, and taste), but exempt from any molecule or active principle, according to the same timing and temporal modalities.

---

### 4. Protocol for Managing Serious Adverse Events (SAEs)

* **Pharmacovigilance golden reporting rule:** As soon as a Serious Adverse Event (SAE) is observed by the clinical team or reported by the caregiver (defined for example by an unplanned emergency hospitalization, a suicide attempt, or a life-threatening blood biological anomaly), the local investigating physician has the absolute legal obligation to draft and teletransmit the regulatory alert form to the Global Pharmacovigilance Centre within a maximum and inflexible delay of **24 hours** from the moment of gaining knowledge of the event.
* **Strict double-blind lifting rule (Unblinding Protocol):** It is strictly forbidden to break the double-blind secret for events of a minor or moderate nature (headaches, passing nausea). The immediate unblinding protocol of the randomization code can only be triggered legally by the Independent Data and Safety Monitoring Board (DSMB) in the case of an immediate life-threatening peril where knowledge of the exact nature of the ingested product (active molecule or placebo) proves indispensable for resuscitators to adapt emergency medical treatment or detoxification.

---
