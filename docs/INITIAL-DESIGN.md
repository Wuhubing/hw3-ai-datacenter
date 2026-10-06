# Initial datacenter design

Selected country: United States. Massachusetts is a scenario assumption, not a demonstrated best site. Comparison countries: China and Singapore. Full baseline: 20 MW IT x PUE 1.25 = 25 MW total; 8760 hours imply 219 GWh at full load. The investment model is a ten-year constant-USD comparison of build, lease and a conditional hybrid first phase. All prices are illustrative.

## C11 / design decision

The engineering concept and system diagram describe a fixed conditional FIRST PHASE: 5 MW IT and 6.25 MW total facility at PUE 1.25. It is distinct from the 20 MW IT / 25 MW full-scale economic baseline. Slider changes do not resize this engineered concept; a different capacity or PUE requires revalidation.

## C12 / assumption

First-phase power: two independent 8 MVA transformer paths, each proposed to carry 6.25 MW at assumed power factor 0.95. Separate A/B buses, protection, interlocked transfer and rack PDUs are required. Shared upstream utility failure remains possible. Loss of the largest component (one transformer) transfers to the surviving path; protection, derating, overload and transfer tests are not yet verified.

## C13 / assumption

First-phase backup: five 2 MW generators, with four required and one spare before site derating. N+1 UPS provides a proposed 15-minute bridge to generators, at least 1.5625 MWh delivered for 6.25 MW. Cooling pumps and controls must also be on standby power. If transfer fails, checkpoint and shed noncritical jobs, then restore by priority. Fuel, derating, maintenance and black-start capability remain unverified.

## C14 / calculation

At the fixed first-phase 6.25 MW full load, 48 hours without grid power needs 300 MWh (6.25 x 48). Assumed diesel use 0.25 L/kWh gives 75000 L, or 90000 L with 20% reserve. This is a concept fuel-sizing calculation, not verified endurance. No solar, wind or battery energy is credited as firm 48-hour supply. The 25 MW baseline would need a separate backup design.

## C15 / design decision

Cooling concept: direct-to-chip liquid loops, N+1 CDUs/pumps, backed-up controls and dry heat rejection to reduce water use. PUE 1.25 is an assumption, not seasonal proof. Water allocation, hourly weather, heat rejection curves, outage cooling and water permits remain unknown; no zero-water guarantee is made.

## C16 / design decision

Network/storage concept: two physically diverse carriers with redundant switches and separate power paths; high-speed internal fabric sized from synchronized training benchmarks; checkpoint storage, replicated data and tested restore procedures. Specify bandwidth, latency, IOPS, retention and recovery targets from workload traces before procurement. Tenant isolation, least-privilege access, encryption in transit/at rest and data-residency review are proposed requirements, not certified controls.

## C17 / assumption

Users include synchronized training researchers and intermittent teaching/inference users. Illustrative workload split is 60% large training, 25% intermittent research and 15% teaching/inference; training concurrency is assumed 256-1024 GPUs, teaching 1-8 GPUs in scheduled class windows. None is signed demand. About 71 million productive equivalent GPU-hours/year at the initial baseline is modeled demand, not measured demand. Signed commitments, concurrent cluster size and timing, data classes, availability/recovery requirements and teaching reservations must be collected. Initial availability target 99% is unverified; uptime needs component failure/repair data, transfer/black-start testing, fuel logistics, seasonal cooling and maintenance analysis.

## C18 / design decision

A member nonprofit would own the shell, electrical and cooling assets; contract qualified design, construction and operations. Development equity funds capped feasibility and bears early loss. Construction debt needs permits, firm grid costs/date, contingency and enforceable member commitments. Equipment finance needs benchmarks, acceptance, warranty and refresh/resale terms. Minimum-use commitments, withdrawal reserves and negotiated utility/construction delay remedies allocate risk; none is signed.

## C19 / assumption

Governance proposal: one institution-one vote, published quotas and metered variable charges, reclaim idle reservations, reserve 20% of teaching access for smaller institutions and provide an appeal panel. Compare existing university/commercial facilities and geographically distributed leasing. Verify water, emissions, noise, permits and cost shifts to other grid customers before construction.
