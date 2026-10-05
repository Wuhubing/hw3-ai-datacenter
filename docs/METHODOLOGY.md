# Model, evidence and decision methodology

## Evidence

The initial source register and metrics are in `lib/seed.ts`. The raw World Bank 2015 response is retained in `data/raw/`. USA, China and Singapore are user-selected comparison countries. Massachusetts is an explicitly assumed domestic candidate for an illustrative US consortium. No signed demand, tariff, site, permits or procurement quote has been established.

Official sources were opened and checked on October 5, 2026. US DOE's 176 TWh figure is the 2024 report's historical 2023 estimate, not the latest inventory. EIA/China NBS/EMA figures describe 2024 national generation and different fuel categories. These are context, not site capacity. The WDI API 2022 query returned null, so the working external refresh uses 2015 and labels it historical. API updates check revisions to that fixed year. An editor can refresh without rebuilding.

Missing site values remain SQL NULL. Their research-source link is a starting point and is not evidence of a value. National electricity totals should not be scored as superior site suitability. Current comparable datacenter counts, carbon intensity, water allocation and tariffs remain unresolved.

## Deterministic calculation

`lib/model.ts` is the shared source for browser and AI tool computations. Inputs are all illustrative assumptions unless explicitly marked otherwise. Downloaded JSON freezes the initial baseline for the memo and slides.

- Site power = IT MW x PUE. Full-load annual GWh = site MW x 8.76.
- Equivalent GPU count = floor(IT MW x 1,000 x GPU power share / kW per equivalent GPU).
- Productive hours = equivalent GPUs x 8,760 x utilization x availability x job efficiency.
- Modeled electricity = total site MW x owned share x (idle fraction + (1-idle fraction) x utilization) x 8,760 x 1,000 kWh/MWh x electricity price.
- Annual opex = electricity + staffing + maintenance + leased compute. IT acquisition includes allocated hosts/network/storage. Facility cost includes conceptual electrical/cooling/backup infrastructure. Scope and contingency need contractor quotes.
- Lease billing is allocated GPU-hours, so productive lease hours are divided by availability x efficiency before applying rate. This uses equal equivalent performance, not unverified cross-generation equivalence.
- Build owns 100%, hybrid owns 25% and leases the balance, lease owns 0%. The hybrid comparison models only phase one. Expansion is an option subject to evidence, not automatically purchased in a later year.
- Ten calendar years begin at planned opening. One-year grid delay uses leased bridge compute for the full demand in year one, then the owned facility opens in year two. Demand does not vanish during delay.
- Fleet replacements occur after four and eight operating years. Constant USD, zero tax/inflation/residual, constant performance. These simplifications are disclosed and material.
- Levelized cost = discounted upfront plus project operating/replacement/delay cost / discounted productive hours. Discount rate represents cost of capital. Interest and principal are separately shown in financing cash flow and excluded from levelized project cost.
- Equal annual debt principal over ten years, facility/grid financing only. First draw occurs at year zero. Equity cash = project cost + interest + principal. No signed revenue is assumed.
- Pre-opening cash is gross asset purchase plus bridge-year opex/holding cost/interest when delayed, plus three months of operational lease prepayment. Prepaid rent is part of the displayed annual rent, not extra lifecycle expense. This metric is gross funding, not equity after debt financing.
- Capital at risk = 80% facility/grid + 70% IT fleet + three months of operating lease commitment. These are scenario recovery assumptions, not market appraisals or a probability-weighted loss.

Changing IT MW also changes the hypothetical demand pool. Capacity optimization against fixed real demand requires job traces and a richer scheduler model. Financing feasibility requires member contracts, not just a low levelized unit cost.

## Decision and governance

Defer 25 MW construction. Run a bounded cancellable lease pilot after agreeing a budget; acquire measured job traces and comparable quotes. Only pursue the 6.25 MW option if binding demand, grid agreement and bids pass a refreshed model. A member nonprofit owns facility assets and contracts qualified design, construction and operation. Quotas and cost allocation are published, with a teaching reservation for smaller institutions and appeals. No proposed governance rule is represented as already agreed.

## Limits to resilience

The first-phase transformer, UPS, generator and fuel quantities on the system diagram are design assumptions. They require engineering derating, protection coordination, witnessed transfer/black-start tests, fuel permits/logistics and cooling evidence. No solar/wind/storage contribution counts as firm 48-hour energy. 99% availability is a model target, not a verified result.

Unused owned-capacity burden is shown separately: fixed staffing/maintenance times the idle fraction of allocated hours, plus baseline idle power during unused hours. It is already included in opex and is not added again. Capital is fully charged in lifecycle costs.
