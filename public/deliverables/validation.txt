# Validation status

Date: 2026-10-05. Local preview uses the starter's test identity, not a real hosted user.

## Passed

- 12 deterministic unit tests: power/energy, equal strategy demand, delay bridging and replacements, half-use behavior, lease independence, cash flow/debt arithmetic, independent first-year calculation, zero-hour handling, invalid inputs, external validation, failure preservation and invalid source-ID rejection.
- TypeScript check passed before final publication build.
- 16 local HTTP integration checks in `api-test-results.json`: public D1 evidence, anonymous denial on four write endpoints, local sign-in, registration consent/persistence, same-origin writes, explicit missing-AI response, admin persistence/reload, stale-write rejection, baseline restoration and a real external API refresh.
- Browser interaction checks passed: scenario change, utilization slider, PUE/reset, evidence search and local sign-in. WebMCP API was absent, so its optional integration remains unverified.
- Browser desktop/mobile surface check: all seven views rendered without uncaught page errors; 390px layout had no document-wide overflow.
- Two-page memo and one-page request architecture PDF rendered and visually reviewed. Five presentation slides visually reviewed; native charts and PPTX structure validated. Not tested in Microsoft PowerPoint.

## Pending or limited

- Real OpenAI request, factual entailment of citations, missing-fact behavior and malicious-source prompt-injection evaluation: hosted key not configured. Policy and schema checks are not substitutes for live model tests.
- Real hosted sign-in and role bootstrap require an actual authenticated Site user ID. The local admin test identity is never a production administrator.
- Logged-in but unregistered and registered-viewer endpoint checks require a fresh local/hosted test identity; anonymous rejection and admin flow are already tested.
- WebMCP registration is feature-detected. Validation is unavailable in the preview browser if it lacks `document.modelContext`; this optional facility does not gate normal website use.
- Private hosted audience prevents anonymous production browsing. The owner must explicitly authorize a public audience or supply reviewer access for grading.
- Real demand, site utility terms, vendor prices, water permits and engineering availability remain unknown. Numerical sensitivity tests do not validate those assumptions.
- Demo uses actual local UI with synthetic English narration and clearly states the AI activation gap. Refresh the final segment after live AI verification for final course submission.

## Reproduce

Run `node --experimental-strip-types --test tests/core.test.mjs`, `npx tsc --noEmit`, and with the local preview running, `python3 scripts/verify-api.py`. The API checks mutate and restore local PUE. No paid model calls occur.
