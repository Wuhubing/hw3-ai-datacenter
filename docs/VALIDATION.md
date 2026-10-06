# Validation status

Updated: 2026-10-06 UTC (2026-10-05 evening, America/New_York).

## Passed and evidence

- 12 deterministic tests in `core-test-results.txt`: energy boundaries; equivalent strategy demand; grid-delay bridging and replacements; half utilization; debt/cash-flow arithmetic; idle costs; input validation; external-response validation; failed refresh preservation; invented source-ID rejection.
- `complete-test-results.json`: 24 checks of the actual application route handlers using disposable SQLite with a D1 API adapter and mocked platform identity. World Bank and OpenAI calls are real. Tests cover anonymous rejection; signed-in/unregistered rejection; registration; viewer rejection for design/refresh/roles; admin save; PUE 1.30 -> 26 MW -> 227.76 GWh; real AI reading the changed value; baseline restoration; external failure; actual refresh; engineering concept answers; missing facts; certification refusal; Singapore source citations; a malicious source; token audit.
- The final full live route run used 30,314 tokens. Earlier development calls and production UI calls are additional; these numbers are not an account-wide billing total. Production successful/failed model usage is recorded in D1 events; each answer displays its tokens.
- `route-test-results.json`: 17 non-model checks after strengthening failure verification to compare the complete metric rows before and after simulated API failure, rather than row count alone.
- `injection-retest-results.json`: 19 checks including an additional real malicious-source test (4,317 tokens). This fixture inserted the assignment's malicious instruction into a source title in the disposable database, then restored it. No malicious source was inserted into production.
- TypeScript check and publication build pass.

## Actual hosted UI checks

- Real ChatGPT identity and registration were verified. The owner is now an application administrator through a hosted allowlist; the local test identity has no production privilege.
- Saved PUE 1.30 in production, asked the adviser, and received the saved 1.30 and 227.76 GWh. Restored 1.25 and verified a subsequent answer and its server-calculated fact line showed 25 MW and 219 GWh.
- The adviser now reads 19 persisted claims including the fixed first-phase transformer, generator, UPS, cooling, network/storage, governance and 48-hour fuel assumptions. It returns five generators, 300 MWh and 90,000 L as assumptions, not certified endurance.
- Real hosted missing-tariff/date and professional-certification questions were tested; the adviser identifies unknowns and declines certification.
- A real hosted Singapore answer cites S3 and identifies 94% in 2024, while stating that this does not establish available site capacity or supply reliability.
- Administrator external refresh succeeded at 2026-10-06T00:24:47.821Z; all three historical observations and their new retrieval times appeared in the interface.
- Browser WebMCP scenario control changed the visible half-use case, rejected utilization 1.5, then restored the base case. It does not save the design.
- Previously reviewed: all seven views, main sensitivity controls, evidence search and 390px layout. The current deployment's adviser, model, evidence and deliverables were exercised again.

## Corrections and limits

Initial live testing exposed two important failures: internal claim IDs in external citations, and an AI full-load-energy answer incorrectly applying utilization. Citation enums now restrict external IDs; every request includes deterministic full-load energy and every answer displays the server-calculated saved PUE, facility MW and GWh. Regression tests use the previously failing combined question.

Review also caught unsupported inference from gas share to supply stability, and one narrative reference to 6.25 MW as IT rather than total facility load. Instructions now expressly prohibit these conflations. The latter wording refinement does not constitute a general entailment guarantee; verify consequential numerical statements against the visible deterministic facts and persisted concept. A valid source ID proves source existence, not every sentence's correctness. Model answers remain nondeterministic.

The anonymous, unregistered and non-admin role matrix was tested against actual route code with test identities, not separate real production accounts. Hosted owner sign-in/admin actions are separately verified. The private Sites access gate still prevents an anonymous user from viewing the published website; teacher access requires an explicit audience decision or invitation. No audience was changed during validation.

Real signed demand, utility terms, comparable vendor quotes, permits, water allocation, component derating and engineering availability remain unknown. They are intentionally labeled assumptions or missing facts. Fixed 2015 World Bank values are historical context, not current site conditions.

## Submission artifacts

- Investment memo: 2 pages; unchanged analytical content, visually reviewed.
- System diagram: one-page SVG plus vector PDF; power/cooling/network/failure paths reviewed.
- Software architecture: one-page graphical request flow PDF; reviewed.
- Presentation: 5-slide editable PPTX with a five-minute speaker outline, plus a reviewed five-page PDF export. Native PowerPoint execution is not tested.
- Demo: 120-second edited sequence of actual hosted website captures with synthetic English narration, not a continuous screen recording or the student's voice. See `DEMO.md` for the transcript and disclosures.

## Reproduce

No paid model calls:

```sh
node --experimental-strip-types --test tests/core.test.mjs
node scripts/verify-complete.mjs
npx tsc --noEmit
```

With explicit access to an existing key, real model tests read it into process memory only:

```sh
node scripts/verify-complete.mjs --live-key-file /absolute/path/to/existing-key-file
```

The route harness never touches production D1. It uses a disposable in-memory database and the checked-in migration. The older `api-test-results.json` is retained as the initial local-preview record; it is not the final live-AI report.
