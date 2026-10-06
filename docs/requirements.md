# Functional requirements and acceptance

| Requirement | Implementation | Verification |
| --- | --- | --- |
| FR1 Location and initial design | Massachusetts scenario; 20 MW IT / 25 MW baseline; fixed 6.25 MW first-phase concept | Hosted UI and 19 D1 claims reviewed |
| FR2 Compare at least three countries | USA, China, Singapore; explicit national/site distinction | D1/UI checked; unavailable values stay unknown |
| FR3 Persistent evidence and assumptions | D1 countries, sources, metrics, designs and typed claims | Saved PUE reload; engineering claims persist; production UI verified |
| FR4 At least one external API | Fixed historical World Bank WDI endpoint | Real route and production administrator refresh passed |
| FR5 Registered users can ask AI | Protected Responses API route, controlled read/calculation tools | Real owner registration and model questions passed |
| FR6 Reject unregistered AI calls | Server identity plus users record | Anonymous 401 and signed-in/unregistered 403 in route harness |
| FR7 Cite substantive external claims | Real D1 source links and source-ID enum/validation | Singapore answer returns S3; entailment remains bounded, not guaranteed |
| FR8 Distinguish evidence types | Typed claims; answer assumptions/uncertainties; server-computed energy fact line | UI and live answers reviewed |
| FR9 Preserve last valid data | Validate all external observations before atomic batch | Simulated 503 preserves every metric row; real refresh separately passed |
| FR10 Visible update times | Metric retrieval timestamps and saved-design timestamp | Production refresh and changed design verified |

Additional acceptance: viewer cannot edit/refresh/assign roles; admin can save assumptions; real AI follows a changed PUE; missing facts and certification limits are stated; deliberately malicious source instruction is rejected in a disposable-database live test. See VALIDATION.md for scope and known model limitations.

The website implements build/lease/hybrid comparisons, all required stress cases and four metrics, a ten-year facility/GPU cash-flow model, governance, financing gates, first-phase failure paths and visible sensitivity assumptions. The original assignment allows a smaller proposed facility; the fixed engineering concept is not silently resized by economic sliders.

Non-goals: construction certification, real-time grid operation, procurement authorization, financial advice and measured institutional demand. The ten-year illustrative scenario model is implemented.

The website is public by owner instruction. Signed-out browser access and the login requirement on the adviser page were verified. GitHub remains private. Unauthenticated API rejection is covered by actual route tests; the raw command-line client encountered a Cloudflare 1010 filter during production checks, so it did not independently verify application endpoint statuses.
