# StructBench protocol — payload sent to the reader (format: TERSE)

Everything below the separator is the **exact, unedited payload** submitted to the reader for the
TERSE arm of the cross-family run: the instructions, the extraction queries, and the 23 English
corpus documents concatenated in TERSE form. Nothing has been added, removed or reworded.

**How the run was executed.** One fresh, dedicated conversation per format — never two formats in
the same conversation, so the reader cannot carry over knowledge from another arm. This file was
submitted, the complete answer captured verbatim (see `structbench-GPT-answers-terse.txt`),
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

=== CORPUS (TERSE) ===
=== EN-T01 ===
CTX: sales CRM migration ClientBase -> NovaCRM
MODE: strict
LEX: CRM=Customer Relationship Management; IT=Information Technology; UAT=User Acceptance Testing

context:
  ClientBase used 9 years (sales dept): opportunities, contacts, sales forecasts
  publisher support ends (current version) = 2027-03-31
  ! migration -> NovaCRM before deadline
  scope = 420 users (France, Belgium, Spain); customer data, open opportunities, activity histories 3 years, standard sales dashboards
  x old attachments, marketing campaigns, data > 3 years (not migrated)
    read-only archive, accessible 2 years
objective:
  ! NovaCRM production = 2027-02-15 <- 6-week safety period before support end
  !! 4 success criteria: >=99.5% active customer accounts correctly migrated; no open opportunity lost; 90% users trained before launch; opportunity creation/update possible from 1st business day after go-live
governance:
  sponsor = Claire Renaud (Sales Director Europe)
  project manager = Malik Ben Amar (IT Department)
  1 business referent / country: data validation, local rules
  impact > 50k EUR | delay > 2 weeks => steering committee decision
  other trade-offs = project manager, after consultation relevant business referent
timeline:
  > data cleansing complete, 2026-09-30
  dry run migration #1 = 2026-10-20; #2 = 2026-12-08
  UAT = 2027-01-05 -> 2027-01-23
  ClientBase structural-change freeze from 2027-02-01; opportunity creation/modification allowed until 2027-02-12 18:00
  final migration after 18:00 -> NovaCRM opens 2027-02-15 08:00
attention:
  risk #1 = customer-account duplicates
    script detects probable duplicates
    !! doubt on duplicate => no automatic merge; decision = country business referent
  risk #2 = billing-tool interfaces (replacement out of scope)
    > temporary interface maintained 6 months after go-live
  !! no specific functionality before launch, except essential regulatory requirement | business continuity
  convenience | enhancement requests -> post-launch backlog

=== EN-T02 ===
CTX: Incident Committee — Delivery Delays at the North Warehouse
AS-OF: 2026-10-06
MODE: strict
LEX: IT=Information Technology

meeting:
  45 min; subject = shipment stabilization after 3 days delays
  participants = Operations, Transport, IT, Customer Service, Logistics Management
situation:
  North warehouse store-order delays since Monday
  @08:00 = 1,840 pending vs ~300 normal
  x main cause = warehouse-management-system breakdown; software normal
  cause = Monday picking reorganization: high-turnover products moved; routes not recalculated
  average picking = 18 -> 27 min
  FastRoad issue: orders not ready usual time -> several trucks partly loaded Monday/Tuesday
decisions:
  ! new physical layout maintained; x previous organization return
  > IT recalculate routes before Thursday 14:00
  > test = 12 pickers, 4 h
  test <=20 min and no blocking anomaly => activate all warehouse next shift
  test >20 min => postpone; temporarily old route logic; no physical relocation
  > +15 temporary workers Thursday/Friday evenings
  x extra Saturday work at this stage
  > FastRoad +2 rotations Thursday evening; +3 Friday
communication:
  !! no preemptive contact all stores
  > only stores likely >24 h delay
  urgent store opening | critical stockout => regional manager may request priority; send Operations before 16:00
  > status Thursday 17:00; Friday 12:00
follow-up:
  objective = <500 pending Friday 18:00
  >800 pending Friday 12:00 => Logistics Director decides by 14:00 possible exceptional Saturday opening

=== EN-T03 ===
CTX: Handling a Payroll File Generation Failure
MODE: strict
LEX: HR=Human Resources; MB=megabytes; P1=priority 1; P2=priority 2

scope:
  monthly payroll-file failure, PayrollFlow; normal monthly processing only
  x payroll simulations; individual adjustments
trigger:
  !! if: no `/export/payroll` file @06:30 scheduled day | file <10 MB | auto check `FAILED`
  `WARNING` alone != trigger => operator consult report/follow instructions
1 verification:
  > verify scheduler `PAY_MONTHLY_EXPORT` started
  running <90 min => !! no restart; wait completion | >90 min
  running >90 min => > stop; open P2
  SUCCESS + file missing/too small => > step 2
2 inputs:
  > verify `employees.csv`, `variables.csv`, `absences.csv`
  !! never manually modify in production
  missing => > contact owner team; suspend
  all present => compare modification date; previous day/earlier = suspicious
3 rerun:
  !! max 1 manual rerun
  > delete only incomplete output
  !! keep logs
  > wait auto check
  SUCCESS + file >10 MB => normal payroll
  FAILED | file <10 MB => > P1 Payroll Engineering
4 communication:
  > inform payroll manager when P1 opens
  !! no direct all-employee information
  no correct generation before 10:00 => payroll manager + HR decide employee delay-risk communication
  !! log every manual action in incident ticket

=== EN-T04 ===
CTX: Agent "MeetingPilot" — Persistent Memory and Action Rules
MODE: strict

identity:
  MeetingPilot = prepare/follow Atlas product committee
context:
  committee = Tuesdays 09:30, 45 min
  head = Sophie Delmas; arbitrates product-priority conflicts
  usual = Sophie, 3 Product Managers, Data manager, customer-support representative
  reference = "Atlas Weekly Decisions"; validated decisions only
  !! discussion ideas stay meeting notes, not reference
before:
  > day before: open decisions from last 2 minutes
  > max 5 topics; priority: 1 customer incidents; 2 decisions blocking delivery within 2 weeks; 3 budget arbitration; 4 others
  !! age alone never auto-adds topic
  > each: expected decision-maker, deadline, known options, no-decision consequence
  missing => "to be clarified"; !! do not invent
validation/after:
  valid only if Sophie explicitly confirms | minutes say consensus approved in her presence
  "this seems to be the best option" != valid decision
  > update "Atlas Weekly Decisions" with validated decisions
  > record date, execution owner, deadline
  > undecided proposals stay notes
  deadline <=14 days => > follow-up action
  !! never retroactively modify old decision
  changed => > new entry referencing previous
prudence:
  !! never external message on own initiative
  draft allowed; sending requires explicit human request

=== EN-T05 ===
CTX: Renewal of the Intervention Vehicle Fleet
MODE: strict

decision:
  choose renewal scenario for 60 intervention vehicles, contracts ending 2027-01 -> 2027-06
  3 options studied
option A — identical diesel:
  benefit = lowest acquisition cost; no site adaptation
  drawback = does not meet internal emissions-reduction trajectory
  risk = increasing traffic restrictions in several urban areas
option B — full electric:
  benefit = best use-phase emissions reduction
  constraint = 18/60 vehicles regularly >280 km rounds where fast charging insufficient
  constraint = immediate 42 charging stations across 11 sites; 3 sites insufficient electrical power
option C — mixed fleet:
  42 electric + 18 plug-in hybrids
  hybrids priority = long rounds
  benefit = significant emissions reduction without waiting electrical upgrade of 3 constrained sites
  ~ 4-year total cost = +8% vs A; -6% vs B
recommendation:
  ! choose option C
  !! decision before 09-15 <- secure delivery times
  !! 42 stations not all installed immediately
    > wave 1 = 29 before 2027-03
    > remaining 13 after reinforcement of concerned sites
  > review = 2028 fourth quarter
  sufficient progress in real-world electric-vehicle range, charging network, site capacities => ~ early replacement of 18 hybrids may be studied

=== EN-T06 ===
CTX: Project ARGOS — Internal Document Search AI Assistant
MODE: strict
LEX: AI=Artificial Intelligence; HR=Human Resources; ID=identifier; IT=Information Technology; V1=Version 1

purpose:
  ARGOS -> conversational assistant for 3,200 group employees: search, summarize, compare internal documentation
  observation: significant time finding procedures, templates, reference notes, past decisions across intranet, SharePoint, business document spaces; current search engines return file lists, do not distinguish applicable vs obsolete
  !! ARGOS not autonomous decision system; function = access/understand information
  !! legal, financial, HR, security decisions remain identified-human responsibility
V1 scope:
  corpuses = intranet internal procedures; Quality document database; formal steering-committee decisions since 2023-01; legal-validated contract templates
  x personal OneDrive, mailboxes, Teams conversations, unpublished project folders
  !! responses = French and English
  document-derived response => !! >=1 identifiable source
  contradictory documents => !! signal contradiction, no silent plausibility choice; when possible prioritize highest formal status | most recent validity date
  procedure hierarchy = group policy > group procedure > local procedure > practical guide > unclassified document
  !! explicit expiration overrides hierarchy; expired group policy not presented applicable solely due higher rank
security:
  !! apply user access rights at each request; never expose, even summary, inaccessible-document information
  x rights copied into independent manually maintained database
  !! permissions queried/synchronized from source repositories via cybersecurity-validated method
  technical logs may retain user ID, time, engine-consulted documents, processing duration
  default full user-question retention <=30 days
  incorrect-response reports retained 12 months for error analysis
  !! no ARGOS content for external-model retraining without explicit data-governance-committee authorization
assistant behavior:
  !! clearly distinguish source facts, model summaries, uncertainties
  insufficient support => explicitly state; x fill with unverified general knowledge
  request "which procedure should I follow?" => first check applicable procedure; several found => explain respective scope
  !! never invent procedure number, date, responsible person, internal rule
  human-validation-required action => may prepare elements; !! never pretend validation occurred
pilot:
  200 users, 8 weeks
  indicators: relevance >=85% useful/very useful; traceability >=98% document-information responses with actionable reference; security = 0 confirmed unauthorized-document exposure; performance = 95% begin display <8 s (start, not full generation)
  adoption rate observed; not blocking criterion for general production
governance:
  sponsor = Director of Digital Transformation
  IT = architecture, integration, technical operation
  Knowledge Management = document quality, content-lifecycle rules
  Cybersecurity = authorization model, logging mechanisms, penetration tests validation
  legal = contract-template terms of use, associated warnings validation
  ARGOS governance committee = every 2 weeks during pilot
  modify source scope | retention rule | new user-data use | identified information-exposure risk => !! committee submission
  purely ergonomic choices = Product Owner within approved budget
phasing:
  Phase 1 document preparation, until 2026-11-30: source inventory, owners, delete/mark most critical obsolete content
    !! objective not full document-estate cleanup before pilot; unrealistic
  Phase 2 construction, 2026-12 -> 2027-02: indexing engine, rights management, interface, citation system
  Phase 3 internal testing, 2027-03: functional, security, response quality, rights-bypass resistance
    !! no real data from out-of-scope personal spaces for testing
  Phase 4 pilot, 2027-04 -> 2027-05: 200 users
  Phase 5 rollout decision, 2027-06: committee chooses rollout | extend pilot | suspend project
general go-live:
  !! not automatic after pilot
  !! requires: no unresolved critical security incident; operational rapid removal of erroneous/confidential indexed document; identified owner per corpus; user-support procedure
  relevance target = 85%; slightly lower does not mechanically block rollout if committee judges gaps understood/correctable
  confirmed unauthorized-document exposure => immediate security analysis; severity may suspend pilot before next committee
out of scope/future:
  x V1 automatic actions in business systems; source-document modification; contract validation; HR decisions
  ~ later phase may study agent functions: prepare workflows, create drafts, execute some reversible operations; distinct security scoping required

=== EN-T07 ===
CTX: HORIZON Program — Decarbonization of the Valmont Industrial Site
AS-OF: 2026-09-17
MODE: strict
LEX: CO₂=carbon dioxide; HSE=Health, Safety and Environment

meeting:
  subject = 2027-2030 energy-trajectory trade-offs
  participants = Industrial Management, Finance, Energy, Maintenance, Procurement, HSE, Site Management, Program Team
objective:
  !! direct CO₂ reduction >=40% between 2024 reference and end-2030
  x production reduction as lever
  gains = efficiency improvements | technological changes | energy substitution
  workstreams: A furnace heat recovery; B electrification 2 drying lines; C gas-boiler replacement; D utilities optimization/loss reduction
A — heat recovery:
  study confirms recover flue-gas heat furnaces 2,3 -> preheat combustion air
  ~ investment = 4.8M EUR; expected gain = 7,200 t CO₂/year at nominal capacity
  shutdowns = furnace 3 10 days; furnace 2 6 days
  main orders before 2026-12-15 => shutdowns integrable into major maintenance 2027-08
  ! launch calls for tenders
  x final investment validation now; > submit investment committee when firm offers available
B — drying-line electrification:
  S1,S2 currently gas
  both electrified -> significant direct-emission reduction; internal-network power insufficient for simultaneous full-capacity S1+S2
  scenarios = S1 only in 2027 | S1+S2 with new electrical substation | defer until public-network reinforcement planned, not guaranteed, from 2029
  ~ new substation = ~6.5M EUR + drying equipment; Finance: full scenario difficult within current budget
  > Industrial Director asks pursue S1-only; preserve design option for later S2
  ! direction validated as working assumption
  x investment decision made
C — gas boiler:
  !! G4 replacement before 2029 <- aging
  studies = high-efficiency gas | electric | biomass
  electric: greatest direct-emission reduction; worsens B power constraint
  biomass: better existing-grid compatibility; requires storage, more truck traffic, enhanced dust treatment
  > supplementary biomass analysis: regional fuel availability, price stability, traffic impact, non-CO₂ atmospheric emissions, operational constraints
  x technology selected at this stage
D — utilities:
  actions = compressed-air leak detection, insulation improvement, optimized pump management, non-production-consumption reduction
  initial actions -> 6% lower utilities electricity vs 2024 average, production-volume corrected
  !! do not count as direct CO₂ reduction when electricity outside site direct-emission scope
  > track as energy gain and indirect-emission contribution
budget:
  reserved envelope = 18M EUR, 2027-2030
  !! envelope != automatic spending authorization
  investment >2M EUR => investment-committee approval
  already-approved studies remain authorized within budgets
  ambitious-scenario estimates clearly >18M => sequence projects | seek additional funding
  > Finance identify available support mechanisms by end-2026-11
  !! subsidies not recorded acquired before formal notification
CO₂ trajectory:
  current most-realistic scenario = furnace heat recovery + S1 electrification + G4 replacement to be determined + continued efficiency actions
  ~ preliminary direct-emission reduction = 31-37%, depending G4 technology
  !! does not yet ensure 40% objective
  > identify >=2 additional levers before 2027-01
    possible = process changes, new energy substitutions, accelerate exploratory projects
  x carbon certificates counted toward site direct-reduction objective
risks:
  critical = electrical capacity (conditions projects, may require unplanned investment); industrial availability (shutdowns; uncoordinated with maintenance -> significant production losses); cost inflation (estimates >6 months old, update required)
  ~ biomass availability = to qualify before critical/noncritical classification
decisions/actions:
  ! calls for tenders heat recovery; S1-only design basis; supplementary biomass study; maintain 40% objective without carbon certificates in direct-objective calculation
  > Procurement calls for tenders A before 2026-10-01
  > Energy biomass study before 2026-11-20
  > Finance available aid before 2026-11-30
  > Program propose 2 additional CO₂ levers before 2027-01-15
  > Maintenance confirm A shutdown compatibility with 2027 schedule before 2026-10-15
  next committee = 2026-12-03

=== EN-T08 ===
CTX: Response to a Suspicion of Ransomware on a Workstation
MODE: strict
LEX: EDR=Endpoint Detection and Response; P1=priority 1; P2=priority 2; SOC=Security Operations Center; USB=Universal Serial Bus

purpose:
  company-workstation ransomware-consistent signs
  priority = limit propagation + preserve evidence; rapid recovery secondary
  !! user/support must not "repair" before security-team evaluation
triggers:
  !! trigger if >=1: sudden unusual unreadable file extensions; ransom-demand message; apparent rapid encryption multiple folders; EDR "ransomware confirmed"; similar simultaneous encryption multiple network shares from same workstation
  simple slowness | blue screen | isolated file corruption alone => x trigger
  serious doubt => support may contact SOC for qualification without immediate confirmed-ransomware declaration
immediate isolation:
  > Ethernet connected => unplug cable
  > Wi-Fi active => disable if immediate without extensive system navigation
  !! default: do not power off; do not close apps; do not delete files; do not launch manual antivirus/cleanup
  objective = cut communications while preserving state
  exception: active encryption + network isolation not quickly achievable => SOC may explicitly request forced shutdown
    decision = SOC | on-call security officer; except physical danger requiring immediate action
incident opening:
  !! initial P1 if ransom message visible | EDR confirms ransomware | several machines affected | server/critical share hit
  single-workstation suspicious signal without confirmation => P2 pending SOC qualification
  !! ticket: user name, workstation name, approximate first-symptom time, symptom description, isolation status, possible ransom message, available screenshots without extra manipulation
  !! never ask user to reconnect workstation to retrieve missing information
propagation search:
  > SOC searches recent user-account connections, similar alerts, unusual network-share access, massive file creation/renaming, suspicious external-infrastructure connections
  >=2 workstations with consistent signs within 30 min => !! treat potentially propagated even common origin unconfirmed
  security manager may order broader containment: account block, temporary share disablement, segmentation, technical-indicator block
  !! site-wide network shutdown never automatic; requires security manager | cyber crisis director
user accounts:
  probable credential compromise | malicious execution using account | abnormal connections incompatible with user activity => !! reset concerned-user password
  encrypted files alone != automatic immediate reset absent account-compromise indicator
  reset decided => > revoke sessions when platform allows
  admin privileges => increased analysis criticality
evidence:
  security team decides memory/disk acquisition need
  !! support not connect personal USB
  business-phone screenshots allowed to preserve displayed message without workstation manipulation
  !! suspicious files not emailed; transfer via SOC secure sampling
  confirmed P1 => !! protect EDR/proxy/authentication/network logs from automatic purge
restoration:
  !! no restoration before security authorization
  ready for rebuild => preferred = full reinstall trusted image
  !! malware cleaning alone insufficient for production return, except security-manager expressly approved exception
  user data restore only from clean source
  !! latest backup not automatically clean; compare date with probable compromise period
  before network reconnect => !! required patches, active EDR, compliance checks passed, rebuild-team validation
communication:
  !! support never publicly confirms ransomware before security validation
  affected-user messages = crisis unit; if none open, security manager + internal communication
  !! no contact attacker/reply ransom-note address without explicit crisis-management instruction
  !! ransom payment never decided by support, SOC, local administrator
closure:
  !! close only when: affected assets identified with reasonable confidence; containment applied; restored systems validated; relevant indicators searched rest of information system; owner assigned remaining corrective actions
  confirmed P1 => > post-incident review within 10 business days after stabilized situation restored

=== EN-T09 ===
CTX: Agent "Portfolio Sentinel" — Persistent Instructions for Steering a Project Portfolio
MODE: strict
LEX: PMO=Project Management Office

identity:
  Portfolio Sentinel = Group PMO assistant; !! not direct project manager
  objective = detect human-attention cases, reliable summaries, structured commitments/decisions/risks memory
  formal sources = ORBIT; approved steering minutes; FINTRACK monthly financial register
  email/informal conversation = clue only; !! not substitute validated formal data
reliability:
  !! never intention -> decision
  "We should probably postpone the launch" = assumption
  "The committee decides to postpone the launch to September 15" = decision
  formal-source conflict => preserve contradiction
    later approved committee decision may replace ORBIT only if explicitly same object
    FINTRACK authoritative for recorded expenditures
    ORBIT = official schedule unless newer formal decision modifies
    unresolved priority => `CONFLICT` + human validation
  !! no missing-value interpolation
project memory:
  each active project: sponsor; project manager; objective; official target; approved budget; actual available expenditures; forecast at completion; overall status; max 3 main risks; open decisions; dated commitments; last review
  !! retain old important values for evolution
    target 06-30 -> 09-30 => change + justification, not new date only
status:
  GREEN | AMBER | RED
  !! objective indicator can override declared project-manager status to more severe
  !! RED if >=1: critical-milestone delay >60d without approved recovery; forecast overrun >15% without validated funding; untreated critical security risk; essential regulatory decision absent >30d after becoming blocking
  !! >=AMBER if: critical delay 31-60d; overrun 8-15%; major external dependency without firm commitment needed <60d; >=3 critical actions delayed
  RED overrides AMBER
  no AMBER/RED => GREEN only with no important info missing
  insufficient critical-criterion data => `STATUS_REVIEW_REQUIRED`, !! not automatic GREEN
budget:
  approved != requested; extra request changes approved only after formal validation
  forecast overrun vs approved budget in force
  example: €10M approved, €11.2M forecast = +12% => AMBER budget
  !! unallocated central reserve excluded until formal allocation
dates:
  !! latest validated forecast vs official target in force
  milestone delay 70d not necessarily RED if noncritical; critical delay 65d => RED absent approved recovery
  draft recovery plan = not approved
risks:
  minimum = description, probability/qualitative assessment, impact, owner; missing => `INCOMPLETE`
  !! risk = uncertain event; issue = occurred event
  production-stopping breakdown = issue; separate recurrence risk possible
open decisions:
  fields = subject, expected decision-maker, required date, delay impact
  > alert 7d before if open; immediately if overdue | already blocking critical milestone
  !! preference in discussions never closes decision
  close only formal decision | authorized manager explicit no-decision-needed confirmation
commitments/actions:
  explicit person + deliverable + date => commitment
  "Léa will provide the costing on Friday" = commitment
  "It would be useful for Léa to look at the costing" = no commitment
  "sometime in September" => keep | mark imprecise; !! no September 30 invention
  overdue only deadline passed and not completed/canceled
weekly:
  > Monday summary for PMO Director; order = new RED; worsened; overdue/blocking decisions; significant financial variances; other notable developments
  > each if possible: What changed? Why important? Expected decision/action? By when?
  x "to be monitored"; state observed signal
autonomy:
  can = summaries, inconsistency detection, questions, action drafts, status-reclassification suggestion
  !! without explicit human validation: no approved-budget change, official-date change, critical-risk closure, funding confirmation, binding project-manager instruction, historical-decision deletion
  out-of-rights request => prepare elements + required validation
uncertainty:
  `CONFIRMED` = clear formal source; `PROVISIONAL` = credible not formally approved; `UNKNOWN` = unavailable | unresolved contradiction
  !! repetition alone never `PROVISIONAL` -> `CONFIRMED`; repetition != validation

=== EN-T10 ===
CTX: Management of a Major Disruption on the Regional Rail Network
MODE: strict
LEX: DCO=Operational Crisis Director

purpose:
  major regional-rail disruption responsibilities/operational decisions
  priority order = 1 protect passengers/staff/responders; 2 stabilize rail situation; 3 realistic transport solution; 4 restore normal service
  !! commercial punctuality/performance after safety
activation:
  !! activate if >=1: planned total disruption >60 min on axis >15,000 passengers/day; simultaneous disruption 2 main lines; train accident with potential victims; rail-junction unavailable preventing normal traffic on >=3 branches; Operations Director decision for exceptional risk
  local ~20-min disruption => not automatic
  ~ preemptive activation possible if high worsening risk indicated
roles:
  DCO = overall operations direction
  Traffic Manager = rail movements, traffic limits, infrastructure safety
  Passenger Manager = information, alternatives, station assistance
  Technical Manager = diagnostics/equipment interventions
  Communication Manager = validates sensitive public messages
  !! DCO does not replace technical managers' specialized safety decisions; coordinates/arbitrates conflicting operational constraints
phase 1 — securing:
  first 5 min = identify affected area, protect traffic, confirm incident type
  !! never authorize train into area with unknown safety status
  stranded away from platform => evacuation not automatic; default passengers onboard while train safe
  track evacuation => !! competent rail-safety-manager authorization + confirmation relevant traffic protected
  immediate onboard danger, especially fire/smoke directly endangering people => staff may initiate emergency measures without normal authorization
initial assessment:
  > within first 15 min Technical Manager provides if possible: probable breakdown/event nature; affected area; plausible minimum duration; reasonably possible high duration; major uncertainties
  !! no precise resumption time solely under operational pressure
  duration unknown => official wording = "indeterminate duration, next estimate at [time]"
  > new estimate max 30 min after previous, even no significant change
temporal classification:
  Level 1 = probable resumption <60 min
  Level 2 = probable disruption 60 min-3 h
  Level 3 = probable >3 h | resumption not reliably predictable
  !! classification != safety severity; serious accident may temporarily Level 1 duration while requiring maximum crisis management
traffic strategy:
  !! avoid train accumulation where neither advance nor simple passenger exit
  when possible hold trains in stations vs open track
  partial turnarounds may maintain unaffected-section service
  !! no partial service if consumes critical-area resources | creates uncontrollable-congestion risk
  full line suspension for safety = Traffic Manager
  primarily passenger-flow management, not immediate safety => coordinate DCO
substitute transport:
  !! buses not automatic for any disruption
  Passenger Manager evaluates duration, passenger volume, road capacity, mobilizable buses, rail/urban alternatives, implementation time
  Level 1: massive buses generally unsuitable <- may become operational after rail resumption
  Level 2: targeted buses possible on critical segments
  Level 3: !! structured substitution plan required; no full train-for-train promise if road capacity insufficient; communicate actual substitution rate honestly
passenger priority:
  1 physical-risk passengers; 2 people stranded stationary train; 3 vulnerable/specific-assistance people; 4 no realistic alternative; 5 others
  priority != wait to fully finish one category before next when teams can act in parallel
passenger information:
  > first message as soon as minimal information reliable: area, disruption nature if confirmed, known traffic consequences, next-update time
  !! do not wait exact duration
  !! no unconfirmed cause as fact
  "electrical breakdown" not announced when only equipment nonresponse known
  multiple hypotheses => "technical incident under diagnostic"
  resumption estimates = appropriate caution; internal target != necessarily public announcement time
public commitments:
  Communication Manager register: next-update time; deployment promise; communicated estimated resumption; passenger-care information
  !! overdue commitment explicitly corrected
  !! obsolete unrealistic estimate not left circulating without update
potential victims:
  public emergency services lead within competence
  priority != rapid traffic resumption
  !! no pressure on emergency teams to clear tracks faster for commercial reasons
  !! victim number/condition not published before validation via channel agreed with authorities
  !! internal-system/agent images not broadcast on social networks/unauthorized groups
crisis escalation:
  !! full crisis unit mandatory if: confirmed/probable victims; Level 3 affecting >30,000 estimated passengers; simultaneous >=3 main lines; national-impact/high-media-risk event by DCO decision
  DCO may activate below thresholds
  !! mandatory criterion met => unit cannot be omitted because situation seems controlled
status frequency after unit opens:
  !! internal operational update >= every 30 min
  > decision summary after each update
  !! passenger update >= every 30 min when no reliable resumption time
  frequency may increase; !! not reduce merely because no change
  "no evolution" message still useful update
resumption:
  !! before resumption Traffic + Technical Managers confirm technical/safety conditions
  progressive resumption possible
  !! first train != proof normal traffic restored
  long disruption => several hours may be needed for nominal plan due poor train/driver positioning
  communication distinguish first movements | progressive improvement | normal traffic
end crisis:
  DCO may end crisis when no immediate incident danger; stabilized traffic strategy; passenger information functioning normal/enhanced; remaining actions manageable by ordinary operations
  end crisis != necessarily all trains normal
post-incident:
  !! full crisis-unit activation => mandatory review
  > initial facts collection within 48 h
  review distinguish established facts; decisions with information available then; observed consequences; information unknown at decision time; improvement actions
  !! decision not judged solely with hindsight information
  !! each improvement action owner + deadline; ownerless action not accepted

=== EN-T11 ===
CTX: Team Life Application Prototype
MODE: strict
LEX: iOS=iPhone Operating System; PWA=Progressive Web App; UI=User Interface

goal:
  develop team-life management prototype for consulting firm
  platform = Android + iOS smartphones via PWA
  desired = beautiful design, elegant animations, serif fonts
  ? React appropriate unless oversized
inputs/context:
  attached UI mockup images = main operation outlines
  attached backgrounds = filenames starting letter "i"
  details incomplete => deduce needed work; user not specifications expert
  user = non-computer-scientist, never built PWA; only web apps on script.google with assistant in recent weeks, chats accessible in history
  new domain => !! advise and guide user
architecture/questions:
  online central database required for updates + loading avatars, announcements, photos etc. back to other users' devices
  user heard of Vercel/other app-hosting sites; unsure suitable
prototype:
  testers = ~10-15; no powerful infrastructure required
  !! result convincing enough to impress superiors -> further development + secure hosting | Apple/Android stores
  meanwhile installable from link; icon on phone; behaves like real app
hosting:
  preference = free via Vercel | other platform
  if paid => !! <=€50/month + cancel anytime
  > search web for most appropriate solution
  > help with deployment etc.
interaction/deliverable:
  user believes all explained; hopes clear; asks any needed questions
  > additionally generate technical-specifications document shareable with another model for code writing/modification
    reason = subscription ends tomorrow; if unfinished, continue with less powerful model like Opus 4.8

=== EN-T12 ===
CTX: Creation of a Web Page
MODE: strict
LEX: HTML=HyperText Markup Language; MP3=MPEG-1 Audio Layer III

goal:
  custom designed page for documents on user's Google account; attached directory screenshot, online to link holders
video:
  main focus
  ? Google Drive streaming via HTML page on same account vs YouTube upload; advise best
  controls = play / pause / stop, loop, volume/mute, fullscreen, all necessary
audio:
  below = small song player, MP3 or YouTube-with-image
  desired frequency-display + progress bars
  ~ mutual exclusion video/song playback = optional plus
images:
  below = 6-thumbnail mosaic; last = question mark on black
  file title under 6 images
  click => full image max screen size; corner cross closes
design:
  colors from previous STAFFFOR graphic charter
  provided STAFOR `index.html`, `style.html`; user can re-upload if inaccessible
  all file HTML links also available if needed
footer:
  !! clearly visible button "link to STAFFFOR" -> https://example.com/stafffor2345643

=== EN-T13 ===
CTX: Creation of a Web Application
MODE: strict
LEX: PDF=Portable Document Format; POC=Proof of Concept

context:
  assistant = corporate-support web-app expert; user = head internal consulting firm
goal:
  custom mission-management prototype/POC on Google ecosystem, code google.script; ~5 tables
functions:
  assign consultants to missions; time entry; create missions for clients/consultants; invoices -> Google Docs, ideally PDF
attachments:
  mockup slides = most interface/navigation concepts; billing missing => help design
  !! black Arial explanatory text not kept in app
  screenshot 5 Google Drive tables on same account: consultants, clients, missions shown; calendar/invoices missing => help design
  sample invoice template to adapt
phases:
  1 finalize/review prototype with colleagues
  2 transpose later to more robust environment, to be defined
next/deliverables:
  > analyze request/attachments; ask necessary questions, using expertise/intelligence/insight
  > calendar + invoice table structures with dummy database data
  > Google Script codes + implementation explanations

=== EN-T14 ===
CTX: "Apollo-ERP" Project — Migration & Hybridization
MODE: strict
LEX: CISO=Chief Information Security Officer; CIO=Chief Information Officer; CRM=Customer Relationship Management; ERP=Enterprise Resource Planning; IT=Information Technology; PLC=Programmable Logic Controller; Q4=Quarter 4; SteerCo=Steering Committee; WMS=Warehouse Management System

document:
  type = project scoping note; sector = Industry / IT Modernization & Supply Chain
context/objectives:
  Apollo-ERP = migrate on-premise obsolete SAP ECC6 ERP -> hybrid SAP S/4HANA Cloud + custom WMS module
  priority by end 2026 Q4: infrastructure-maintenance cost -35%; permanently eliminate critical assembly-line stockouts @Amiens pilot
scope in:
  full historical financial/accounting/tax data since 2018-01-01
  real-time bidirectional interface with Amiens production-line PLCs
  !! operational training for 140 site logistics operators + forklift drivers
scope out:
  x Asia-Pacific subsidiaries' IT-system migration -> separate *Lotus* project planned 2028
  x CRM overhaul; only connect existing gateway to new ERP, no database-structure modification
timeline:
  !! project starts 2026-09-01
  milestone 1 = 2026-10-15: finalize data-flow mapping + formal target-security-architecture validation by CISO
  milestone 2 = 2026-12-01: close technical/functional acceptance in pre-production
  milestone 3 = 2027-01-15: final cutover/Go-Live exclusively technical weekend
governance/constraints:
  SteerCo = biweekly Thursday 14:00 sharp; co-chairs Claire Masson (Operations Director), Marc Renard (CIO)
  !! weekdays Amiens: no service interruption/system unavailability >4 consecutive h <- major contractual penalties automotive customers
  !! heavy infrastructure outage | risky deployment only weekly technical window Saturday 22:00 -> Sunday 04:00

=== EN-T15 ===
CTX: SecOps Crisis Unit — Incident "SecOps-2026-A"
AS-OF: 2026-10-12 03:30
MODE: strict
LEX: CIO=Chief Information Officer; CNIL=Commission Nationale de l'Informatique et des Libertés; DPO=Data Protection Officer; GDPR=General Data Protection Regulation; GB=gigabytes; IP=Internet Protocol; RIB=bank account details; SecOps=Security Operations; SFTP=secure file transfer protocol; SOC=Security Operations Center; VPN=Virtual Private Network

document:
  operational cybersecurity/threat-management minutes
meeting:
  commander = Yassine Merabet (SecOps Lead)
  participants = Sophie Duval (CIO), Thomas Wright (Forensics Expert), Lucas Becker (Legal Director / DPO)
incident:
  01:15 SOC -> critical mass exfiltration via secure SFTP to unlisted external IP @Eastern Europe
  entry = compromised admin account, external provider *TechConsult*
  02:00 `Prod-DB-04` network access fully logically isolated
  Thomas Wright: 45 GB sensitive data copied, exclusively nominative employee payslips + strategic-supplier RIB
  no ransomware demand received/left yet
actions:
  ! all *TechConsult* VPN/access worldwide revoked; owner Network Infrastructure/SecOps; completed 02:45
  > Lucas Becker CNIL GDPR personal-data-breach declaration before 2026-10-13 01:15
    legal max = 72 h; management internal = 24 h post-detection
  > Sophie Duval all-employee note by 2026-10-12 08:00: "exceptional technical maintenance operation"
    !! no exfiltration mention <- avoid panic before communication fully controlled
evidence:
  !! no `Prod-DB-04` restart | system-log purge/rotation before Thomas Wright final legal disk Forensic Image
  reason = avoid accidental destruction evidence indispensable for criminal complaint

=== EN-T16 ===
CTX: Emergency Hotfix Deployment on B2B Gateway
MODE: strict
LEX: API=Application Programming Interface; B2B=Business-to-Business; SSH=Secure Shell

document:
  type = technical production procedure/runbook; sector = System Administration / DevOps / Payment Gateway
  code = RUN-B2B-HOTFIX-09
  author = Arnaud Moreau (Lead DevOps Infrastructure)
trigger:
  !! Level 1 Critical only; B2B payment-gateway API failure rate >8% over rolling 5 min
1 diagnostics:
  > secure SSH bastion; run:
  `curl -s http://monitor.b2b.internal/metrics | grep "api_drop_rate"`
  returned value <0.08 (8%) => !! stop emergency procedure immediately; revert standard diagnostic RUN-B2B-GEN-01
2 traffic switch:
  !! max delay = 90 s
  > switch all production traffic primary -> passive redundant secondary:
  `switch-traffic --target node-secondary-02 --force`
  > monitor network console; ensure active transactions on `node-primary-01` = 0 within <90 s
3 patch injection:
  > production inject compiled patch:
  `/opt/scripts/patch_injector.sh --version 2.4.1-hotfix3`
  > wait console validation message confirming end system-packet writing before next step
4 integrity:
  > run automated integrity validation:
  `/opt/scripts/validate_patch.sh`
rollback:
  exit status != `0` (Success) | average end-to-end response time >120 ms after patch => !! immediately run:
  `/opt/scripts/rollback_patch.sh --target 2.4.1-stable`
  !! after rollback launched: no second manual patch attempt
  !! operator must immediately phone on-call "Core Engineering" engineer, internal extension 8402

=== EN-T17 ===
CTX: AI Agent "KRONOS-V4" — Reflection Log and Flash Memory
MODE: strict
LEX: AI=Artificial Intelligence; ECB=European Central Bank; EUR=euro; ID=identifier; JSON=JavaScript Object Notation; USD=United States dollar

context state:
  entity = KRONOS-V4 (Autonomous Ledger Auditor)
  session ID = TX-AUDIT-2026-8942
  ruleset = Accounting compliance ruleset v9.1
scratchpad:
  flow = reconciliation of cross-border interbank transactions Miro-EU vs Miro-US
  anomaly = transaction `TR-88491-X`, database date 2026-07-18
    Miro-EU net debit = 1,200,000 EUR
    Miro-US simultaneous credit = 1,280,000 USD
  ECB fixed reference rate @2026-07-18 = 1.09 USD = 1.00 EUR
  theoretical Miro-US credit = 1,200,000 × 1.09 = 1,308,000 USD
  discrepancy = 1,308,000 - 1,280,000 = 28,000 USD
  !! acceptable anomaly threshold max = 5,000 USD; observed 28,000 widely exceeds
action/decision:
  ! immediately tag `TR-88491-X` = `SUSPENDED_DISCREPANCY`
  > generate/publish encrypted JSON payload exclusively to Treasury Level 2 human emergency-processing queue
  !! no automatic accounting-entry correction | balance compensation
    autonomous self-balancing only if discrepancy <15,000 USD; current 28,000 blocks automatic execution
  !! freeze modification access to Miro-EU/Miro-US sub-ledger entries for accounting day 2026-07-18 until human authentication token `AUTH_HUMAN_OVR` received

=== EN-T18 ===
CTX: IntraBot-2026 — Logistics Automation via AGV
MODE: strict
LEX: AGV=Automated Guided Vehicle; LiDAR=Light Detection and Ranging; MSD=musculoskeletal disorder

context/objectives:
  Delta logistics distribution center @Lyon: previous fiscal year MSD-related work stoppages +22%
  IntraBot-2026 -> deploy 12 heavy-handling AGVs
  objective by 2026-11-30 = autonomously transfer all packages >25 kg, unloading docks Zone A -> high-density racks Zone G, no human intervention
  purpose = preserve employee health + increase flow rates
safety:
  !! AGVs only permanent ground-laser-marked traffic lanes
  !! pedestrians always full/inalienable right-of-way over AGVs
  each AGV = Class 3 safety LiDAR
  unlisted obstacle | human <1.5 m from chassis => immediate automatic emergency stop
    !! total mechanical deceleration <200 ms
budget:
  ! Supervisory Board unanimously approved total = 850,000 EUR
  12 factory AGVs = 600,000 EUR
  laser mapping + physical adjustment Zones A,G = 150,000 EUR
  change management + social support + forklift-driver retraining = 100,000 EUR
out of scope:
  x automation final delivery-truck loading in outdoor dispatch zones
  !! remains exclusively human forklift drivers using conventional thermal forklifts
  reason = strong outdoor natural-light variation alters first-generation optical sensors in selected AGV fleet

=== EN-T19 ===
CTX: H2-Green Plan — Industrial Pivot and Energy Transition
AS-OF: 2026-05-15
MODE: strict
LEX: CSE=Social and Economic Committee; ICPE=Installation Classée pour la Protection de l'Environnement; MW=megawatt; MWh=megawatt-hour; PPA=Power Purchase Agreement; Q1=Quarter 1

meeting/context:
  extraordinary Executive Committee @general-management headquarters
  purpose = validate technical/financial trade-offs for petrochemical-hub energy transition; choose 2 financing options for Eastern-France refinery conversion; ensure full compliance with European directive "NetZero-2030"
  attendees = Hélène de Rostand (Chief Executive Officer); Jean-Marc Vignol (Global Chief Financial Officer); Amélie Moreau (Sustainable Transformation Director); Antoine de Silva (Legal and Compliance Director); Chloé Lemaire (secretary)
Carling technical:
  site = historical Carling petrochemical site, Moselle/Grand Est
  project = progressive shutdown polymer-cracking units + massive low-carbon hydrogen production via water electrolysis
  requires dedicated electrical substation + industrial purified-water volumes
  !! regulatory urgency: new European progressive sector carbon tax effective 2027-01-01
  site carbon footprint reduction <40% => penalties several million EUR/quarter
financing:
  Alpha = 120M EUR envelope; 45% group self-funding; 10M EUR expected subsidies; 3-month approval; low governance/sovereignty risk, total managerial control
  Beta = 145M EUR; 15% self-funding; 65M EUR expected subsidies; 14-month approval; high risk, intellectual-property sharing
  Beta benefit = drastically lower direct cash need via 65M European Union subsidies
  Beta drawback = binding engineering-patent opening to European competitors under shared innovation
  14-month Beta review -> contract signatures after 2027-01-01 carbon-tax deadline -> fines erase subsidy benefit
  x Beta unanimously rejected
  ! Alpha adopted
  !! private-bank contracting finalized -> credit lines effectively open before 2026-09-01
legal/regional:
  electrolysis capacity >20 MW => ICPE authorization regime
  !! public inquiry minimum 6 months, coordinated Grand Est prefecture services
  !! no earthworks/structural/civil-engineering contract legally signed/engaged before prefectural operating permit officially published in regional collection of administrative acts
  public inquiry >150 formal written objections from resident associations | local authorities => automatic local joint mediation unit co-led by Carling mayor
    !! works timeline legally suspended fixed non-negotiable 45 calendar days -> renegotiate landscaping compensation
roadmap:
  > Amélie Moreau finalize technical ICPE file + officially submit specifications to Moselle prefecture by 2026-06-15
  > Jean-Marc Vignol negotiate/sign long-term PPA renewable producer by 2026-08-01 -> guarantee green-electricity supply for electrolyzer
    !! price <=62 EUR/MWh; minimum firm commitment 10 years
  > Industrial Procurement, technical supervision Amélie Moreau: draft/publish international tender for high-performance proton-exchange-membrane electrolysis modules by 2026-10-15
out of session:
  x social management/retraining of 210 old Carling thermal-cracking employees deliberately not addressed
    > extraordinary thematic CSE meeting scheduled by Human Resources = 2026-06-04
  x hydrogen-export pipeline extension to Germany removed agenda; deferred 2027 Q1

=== EN-T20 ===
CTX: Multi-Region Cloud Disaster Recovery Plan "DRP-CLOUD-V2"
MODE: strict
LEX: ALB=Application Load Balancer; API=Application Programming Interface; AWS=Amazon Web Services; DNS=Domain Name System; EKS=Elastic Kubernetes Service; HTTP=HyperText Transfer Protocol; ISP=Internet Service Provider; PGP=Pretty Good Privacy; PITR=Point-In-Time Recovery; SQL=Structured Query Language; TTL=Time To Live

document:
  type = Information Technology disaster-recovery manual / DevOps Infrastructure
  sector = Information Technology / Critical Banking Services / Cloud Computing
  purpose = total forced cutover savings-banking microservices
  primary = AWS `eu-west-1` Dublin, Ireland; backup = AWS `eu-central-1` Frankfurt, Germany
activation:
  !! only if API Core-Auth total interruption >12 consecutive min and written major physical outage (*AWS Outage*) notification validated by on-call lead network engineer
  !! global-cutover trigger order requires digital cryptographic signature by 1 of 3 authorized SecOps on-call directors via private PGP key
Phase A — network/DNS:
  > network administration console; emergency Python script modifies global dynamic routing via AWS Route53; run:
  `python3 /root/dns_failover.py --source eu-west-1 --destination eu-central-1 --ttl 10`
  !! force TTL = 10 s -> overwrite global ISP caches/accelerate route propagation
  > validate incoming HTTP volume on Dublin ALB = 0 via:
  `aws elbv2 describe-load-balancers --region eu-west-1 --query "LoadBalancers[*].State"`
Phase B — database:
  Aurora PostgreSQL = asynchronous global replication Dublin -> Frankfurt; German node normally read-only Read-Replica
  > promote Frankfurt to autonomous Read-Write production:
  `aws rds promote-db-cluster --db-cluster-identifier aurora-prod-frankfurt --region eu-central-1`
  !! poll status; wait `promoting` -> `available`; normal transition = 3-5 min
  `error_checksum` after promotion => !! never force-start SQL engine
    > immediately restore database to last known consistency point via PITR = T-60 s relative exact Dublin-crash timestamp
Phase C — Kubernetes:
  > activate Frankfurt AWS EKS autoscaling: minimum 5 idle nodes -> 45 physical crisis nodes `m5.2xlarge`
  > verify essential financial-service pods:
  `kubectl get pods -n production -o wide`
health matrix:
  `core-auth-service` = min 15 Operational pods; 100% infrastructure availability
  `payment-engine` = min 20 Operational pods; request failure rate strictly <0.1%
  `ledger-recorder` = min 10 Operational pods; internal network latency <15 ms
reintroduction:
  matrix pods stable/active in Frankfurt => > DevOps run:
  `pytest /tests/integration/drp_validation.py`
  !! no real user traffic/banking-client connections routed to Frankfurt until final test report explicitly and uniquely = `STATUS: SUCCESS`
  any single unit | load test fails => !! external traffic remains locked + redirected to emergency landing page (custom HTTP 503)

=== EN-T21 ===
CTX: AML-CORE — Anti-Money Laundering Multi-AI Agent Network
MODE: strict
LEX: AI=Artificial Intelligence; AML=Anti-Money Laundering; API=Application Programming Interface; EUR=euro; JSON=JavaScript Object Notation; TRACFIN=Traitement du renseignement et action contre les circuits financiers clandestins

system:
  distributed environment = Agent-Parser-01 (semantic ingestion) + Agent-GraphAnalyser-02 (relational structure analysis) + Agent-RiskScorer-03 (probabilistic danger evaluation)
  shared objective @2026 = real-time detection complex asset concealment, tax evasion, money laundering patterns in financial-flow networks
log 01 — Parser @2026-07-14 22:04:
  input = Swift MT103 interbank-entry batch `BATCH-EMEA-94`
  anomaly = 14 outgoing transfers × 9,900 EUR identical within 48 h
  origins = 14 distinct deposit accounts, "Banque Privée A" @France
  destination = single pooling account *Vortex-Holdings* @Panama tax jurisdiction
  extracted rule = 9,900 EUR immediately below French TRACFIN vigilance threshold 10,000 EUR triggering automatic mandatory declaration
  > convert transactions to JSON-Graph nodes/edges; immediately send Context Token -> Agent-GraphAnalyser-02
log 02 — GraphAnalyser @2026-07-14 22:06:
  analysis = classic "convergent star" topology; deterministically corresponds to "Smurfing" (*Schtroumpfage*): split large capital into micro-flows to avoid traditional bank alerts
  *Vortex-Holdings* inbound centrality degree = `C_d = 14`
  company immediately redistributes 95% accumulated sums = 14 × 9,900 × 0.95 = 131,670 EUR
  destination = single outgoing operation to unhosted crypto wallet `0x71B...44F`
  rapid assets -> unregulated anonymous crypto wallet + legal entity non-cooperative jurisdiction Panama => critical structural-risk indicator
  > feature vector -> Agent-RiskScorer-03
log 03 — RiskScorer @2026-07-14 22:07:
  formula = `S_r = (0.4 × S_jurisd) + (0.3 × S_structure) + (0.3 × S_vitesse)`
  inputs = jurisdiction 95/100 (Panama); graph structure 98/100 (Star Smurfing); transit velocity 90/100 (redistribution <120 min)
  result = `(0.4 × 95) + (0.3 × 98) + (0.3 × 90) = 38 + 29.4 + 27 = 94.4`
  !! `S_r` >85 => conservative lock protocol without prior human validation
final decisions:
  ! API blocking order: 14 emitting Banque Privée A accounts -> `BLOCK_ACCOUNT_TEMPORARY`
  ! automatically compile TRACFIN regulatory file = `AML-TRACFIN-2026-Vortex.xml`
  !! software agent lacks privileges for definitive seizure/liquidation financial assets/cryptocurrencies
  !! such action exclusively Human Compliance Direction via physical multi-hardware-token signature protocol

=== EN-T22 ===
CTX: IRIS-3 Programme — Hyperspectral Imaging Satellite Constellation
MODE: strict
LEX: GaAs=gallium arsenide; LWIR=Long-Wave Infrared; SSO=Sun-Synchronous Orbit

vision/architecture:
  European Civil Space Program technological-independence infrastructure -> scope 3rd-generation nanosatellite constellation IRIS-3
  mission = real-time hyperspectral imaging coverage: map continental-agriculture water stress + instantly detect forest-fire outbreaks across Europe
  nominal constellation = 24 rigorously identical operational satellites
  continuous orbital revisit -> 3 distinct orbital planes × 8 satellites/plane, homogeneous distribution
space segment:
  altitude = constant 540 km above mean sea level
  trajectory = SSO; inclination = 97.5° relative equatorial plane
  payload = high-performance infrared thermal imager, LWIR bands; ground optical resolution = 1.2 m/pixel
  power = deployable articulated GaAs solar panels; minimum continuous 180 W/satellite during sunlit orbital phase
industrial consortium:
  Generic Platform/Satellite Bus = Thales Alenia Space, Cannes France, deadline 2027-03-12
  Hyperspectral Optical Payload = JenaOptics GmbH, Jena Germany, deadline 2027-06-30
  Electric Propulsion Module = ThrustMe, Verrières-le-Buisson France, deadline 2027-09-15
  Ground Segment/Guidance/Command Stations = Telespazio, Fucino Italy, deadline 2027-12-01
launch:
  first phase = 8 satellites Orbital Plane A
  !! launch exclusively Arianespace, Vega-C, Guiana Space Centre @Kourou
  priority launch window = 2028-02-14
  !! Flight Operations Director must immediately stop countdown/abort ignition if within <30 min before liftoff H-hour:
    high-altitude wind >85 km/h between 10,000-15,000 m
    electrical activity | storm cells detected by radar within <25 km radius around Guianese launch pad
propellant reserve:
  each nanosatellite = miniaturized solid-iodine-sublimation propulsion
  !! permanent reserve >=15% initial iodine mass, exclusively: low-orbit debris avoidance + mandatory end-of-life deorbit
  !! Ground Segment flight-control team forbidden to use 15% reserve for initial altitude drift caused by Vega-C orbital-injection inaccuracy

=== EN-T23 ===
CTX: NeuroX-72 — Phase III Clinical Trial Regulatory Compliance Protocol
MODE: strict
LEX: DSMB=Independent Data and Safety Monitoring Board; MMSE=Mini-Mental State Examination; MRI=Magnetic Resonance Imaging; SAE=Serious Adverse Event

study/framework:
  international multicenter Phase III trial, candidate NeuroX-72
  regulatory identifier = EudraCT-2026-004512-11
  objectives = clinical efficacy + large-scale biological safety + systemic-tolerance profile
  NeuroX-72 = next-generation enzyme inhibitor targeting stabilization of synaptic-degradation pathways -> statistically significant slowing cognitive-deficit progression in adults with first Alzheimer's symptoms, early-to-moderate stages
eligibility — inclusion:
  !! selection/randomization/treatment only if all simultaneous:
    age = 55 completed years to 80 years on formal informed-consent signature day
    confirmed cognitive impairment; validated MMSE score inclusive 18-24 at preselection
    permanent/contractual full-time cohabiting natural caregiver at home, able to guarantee/supervise/log in writing exact daily experimental-treatment administration
exclusion:
  !! immediate exclusion if any:
    proven ischemic | hemorrhagic stroke within previous 12 months
    severe renal failure = creatinine clearance strictly <30 mL/min
    absolute technical/medical MRI contraindication, notably first-generation pacemaker incompatible with intense magnetic fields
methodology/dosage:
  !! strict double-blind, randomized, placebo-controlled; allocation 1:1
  Group A experimental = oral film-coated NeuroX-72 40 mg, 1 dose/day, morning fasting, uninterrupted 48 consecutive weeks
  Group B control = oral placebo tablet strictly identical physical appearance (color, size, texture, taste), no molecule/active principle; same timing/temporal modalities
SAE:
  SAE observed clinical team | reported caregiver, e.g. unplanned emergency hospitalization, suicide attempt, life-threatening blood biological anomaly => !! local investigator drafts/teletransmits regulatory alert to Global Pharmacovigilance Centre within max inflexible 24 h from knowledge
unblinding:
  !! strictly forbidden for minor/moderate events (headaches, passing nausea)
  immediate randomization-code unblinding only legally triggered by DSMB if immediate life-threatening peril and exact ingested product (active | placebo) indispensable for resuscitators to adapt emergency treatment | detoxification
