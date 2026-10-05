# Compute Commons

An investment decision workspace for a hypothetical university AI consortium. Compare **build and own**, **lease capacity**, and a **conditional first-phase hybrid** across a ten-year horizon. Research covers the United States, China and Singapore.

The working recommendation is to lease while validating demand and grid terms. The analysis does not establish that a 25 MW facility is justified. Economic inputs and engineering sizes are clearly labeled assumptions, not vendor quotes or certified designs.

## Project status

Implemented: interactive scenario model, country comparison, source register, D1 persistence and migrations, genuine World Bank API refresh, ChatGPT sign-in integration, registration/roles, protected adviser endpoint, controlled tools, citation checks and token accounting.

**Live AI is not activated:** the Site has no hosted OpenAI credential. The application returns an explicit unavailable state rather than a simulated response. Real AI citation quality, prompt-injection resistance and production identity remain to be verified. New Site and GitHub repository are private; course reviewers require appropriate access before submission.

## Deliverables

- [Two-page investment memo](public/deliverables/investment-memo.pdf)
- [Editable five-minute committee presentation](public/deliverables/presentation.pptx) and [PDF](public/deliverables/presentation.pdf)
- [One-page power, cooling, network and failure diagram](public/system-diagram.svg)
- [Software architecture](docs/ARCHITECTURE.md) and [request-chain explanation](public/deliverables/architecture.pdf)
- [Two-minute demonstration](public/deliverables/demo.mp4), with English synthetic narration and a [transcript/disclosures](docs/DEMO.md)
- [Requirements](docs/requirements.md), [methodology](docs/METHODOLOGY.md), [validation](docs/VALIDATION.md), and [individual request walkthrough](docs/REQUEST-WALKTHROUGH.md)
- [Original assignment](docs/assignment-original.txt), [Chinese summary](docs/ASSIGNMENT-OVERVIEW.zh.md), and [implementation plan](PLAN.md)

## Run locally

Node 22.13+ is required. Use the checked-in lockfile.

```sh
npm ci
npm run build
node --import ./scripts/sites-env.mjs ./node_modules/wrangler/bin/wrangler.js d1 execute DB --local --config dist/server/wrangler.json --persist-to .wrangler/state --file drizzle/0000_giant_jocasta.sql
npm run dev
```

Apply each migration once per local database. Preview uses a loopback-only simulated ChatGPT user; it is not production identity. To test admin actions locally, set `ADMIN_USER_IDS=local_seedy` in an ignored `.dev.vars` file. Do not configure this test ID in production.

Initial evidence is seeded in an idempotent D1 batch on the first read. A saved design is never overwritten by seeding. The platform applies production schema migrations at deployment.

## Verify

```sh
node --experimental-strip-types --test tests/core.test.mjs
npx tsc --noEmit
# With local development server running:
python3 scripts/verify-api.py
```

The integration script changes and restores local model assumptions and refreshes the historical API. It uses only the local test identity. Tests never spend OpenAI tokens.

## Model and data boundaries

All strategies serve equivalent modeled productive hours. Full facility costs and the GPU fleet are separate. A grid delay uses bridge leases. Low utilization leaves fixed and idle-power costs. Debt service is shown separately from discounted project cost. The hybrid models a 6.25 MW first phase, not automatic later expansion. Every economic input remains a sensitivity assumption.

The World Bank API uses a 2015 renewable-electricity series because the queried 2022 values were missing. It is historical context only. The source register also includes 2024 EIA, China NBS and Singapore EMA statistics, a historical DOE data-center estimate and NVIDIA system documentation. National statistics do not establish site-specific capacity or prices.

## Production configuration

`.openai/hosting.json` contains the project ID and logical D1 binding only. Configure `OPENAI_API_KEY` as a hosted secret, `OPENAI_MODEL` as a supported model (default `gpt-4.1-mini`), and `ADMIN_USER_IDS` with an actual authenticated Site user ID. `.env.example` documents these fields; no real secrets are committed. Do not paste keys into GitHub or browser code.

Adviser requests require authenticated identity, application registration, same origin and atomic hourly limits. The server supplies relevant D1 records and permits only approved tools. Citation IDs are validated, but factual entailment still needs live evaluation. Questions are not stored in audit events; token usage is recorded.

The application relies on the Sites dispatcher to inject trusted identity headers. Do not expose the Worker directly on an untrusted endpoint without equivalent header authentication.
