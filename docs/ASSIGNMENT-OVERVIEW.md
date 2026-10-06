# HW3 / PS3 assignment overview

This summary describes the supplied assignment. The [original assignment](assignment-original.txt) remains the authoritative source. Implementation status and limitations are recorded separately in [validation](VALIDATION.md).

## Decision problem

Create an AI datacenter investment website for a university consortium. Compare building, leasing, and a phased hybrid using traceable evidence. The initial baseline is 20 MW IT load and PUE 1.25, giving 25 MW total facility demand and 219 GWh at full load over 8,760 hours. This is a baseline calculation, not verified demand or a forecast.

Long-term member commitments, grid connection prices, upgrade charges, energization dates, workload needs, and allocation rules are not established. A smaller facility, deferral, or rejection must remain possible outcomes.

## Investment and engineering scope

- Explain research and teaching demand, productive GPU-hours, peak concurrency, availability, security, and scheduling.
- Describe power distribution, backup, UPS, cooling, networking, storage, and GPU procurement. Analyze the largest electrical-component failure and a 48-hour grid outage.
- Compare ten-year cash flows with facility and GPU assets separated. Include grid work, energy, staffing, maintenance, financing, equipment replacement, leases, and idle capacity.
- Explain financing conditions, ownership, member commitments, withdrawal risk, compute allocation, and fair access for smaller institutions.
- Consider alternative providers and locations, energy and water impacts, permitting, and effects on other utility customers.

For each strategy, report the base case, a one-year delay in full grid power, and half the expected GPU utilization. Each case needs pre-opening cash, annual operating cost, cost per productive GPU-hour, and capital at risk. Define productive hours and capital risk explicitly. Do not treat annual renewable generation as guaranteed power during an outage.

## Functional requirements

| ID | Requirement |
| --- | --- |
| FR1 | Present the proposed location and preliminary design. |
| FR2 | Compare at least three countries. |
| FR3 | Persist evidence, sources and design assumptions. |
| FR4 | Fetch data from at least one genuine external API. |
| FR5 | Allow registered users to ask the AI adviser questions. |
| FR6 | Reject unregistered AI requests at the backend. |
| FR7 | Cite supporting evidence in substantive AI responses. |
| FR8 | Distinguish facts, estimates, calculations and unknowns. |
| FR9 | Retain the last valid data when an external source fails. |
| FR10 | Display update times for data. |

The assignment requires Sites, a backend, D1 persistence, sign-in, and server-side AI calls. Visitors may inspect the public design; registered users may ask questions; authorized editors refresh data; administrators manage assumptions and roles. Users must not assign themselves elevated privileges. Secrets remain server-side.

At least three manually verified source records are required. Record value, units, scope, reporting year, publisher, source URL, retrieval time, definitions and limitations. Missing data stays NULL. The AI should read current saved records, use controlled tools, acknowledge missing facts, and track token use under rate limits.

## Submission materials

- Published website URL entered in the course shared document.
- Visible assumptions, sensitivities, three strategies and three scenarios.
- One-page power, cooling, networking and failure diagram.
- Five-minute investment committee presentation and Q&A preparation.
- Two-page investment memorandum with a recommendation and three findings that could change it.
- Software architecture diagram and individual browser-to-D1-to-OpenAI request explanation.
- D1 schema and migration, source/API list, initial design, requirements table and test evidence.
- Two-minute website demonstration.

## Interpretation and outstanding course information

The assignment's earlier section explicitly requires ten-year cash flow, even though a later non-goal example mentions financial modeling. This project retains the explicit cash-flow requirement. The five-minute presentation and two-minute website demonstration are separate deliverables.

The student selected the United States, China and Singapore, an individual submission, and English deliverables. The deadline and shared course document URL were not supplied. The original suggested classroom/homework durations are guidance, not a completion guarantee.
