# HW3 implementation plan and status

Updated: October 6, 2026. Individual submission; all deliverables are in English. The country comparison covers the United States, China, and Singapore.

## Objective

Build an evidence-based decision workspace for a university AI consortium. Compare ownership, leased capacity, and a conditional phased hybrid without presuming that a 25 MW facility is justified. The recommendation remains lease-first until demand and grid terms are established.

## Implementation stages

1. **Requirements and evidence:** map FR1–FR10 to implementation and tests; distinguish facts, assumptions, calculations, decisions, and unknowns. Preserve reporting periods, units, provenance, and limitations.
2. **Research and design:** compare three countries using primary sources; use a real external API; develop the conditional 5 MW IT / 6.25 MW total first phase. Analyze the largest-component failure and a 48-hour grid outage without claiming certified resilience.
3. **Economics:** compare three strategies and three scenarios over ten years. Separate facility and GPU costs, account for replacement, idle energy and grid-delay bridging, and distinguish financing from project costs.
4. **Website:** implement Decision, Countries, System design, Investment model, Evidence, Adviser, and Deliverables. Make scenario assumptions inspectable and reproducible.
5. **Persistence and refresh:** implement D1 schema, immutable migrations and idempotent seeds; validate World Bank responses and retain prior valid observations after failures.
6. **Identity and roles:** authenticate through Sites, require application registration for AI, and enforce editor/admin privileges on the server. Keep secrets out of client code and Git.
7. **AI adviser:** retrieve current saved design and evidence, provide controlled calculation tools, validate citation IDs, and enforce usage limits. Treat source text as untrusted data.
8. **Verification and delivery:** test calculations, roles, refresh failure, changed saved inputs, missing facts, citations, and injection resistance; publish the website and prepare the memo, diagrams, slides, demonstration, and evidence package.

These stages are implemented. See [validation](docs/VALIDATION.md) for the scope and limits of completed checks rather than treating this plan as test evidence.

## Current release work

- Replace synthetic narration with the student's supplied recording and align the edited website captures with each section.
- Keep the public repository, website and submission documentation in English.
- Publish updated artifacts and verify public repository visibility.

## Remaining student/course actions

The shared course document URL and deadline have not been supplied. Enter the website URL in the course document when available, review course-specific disclosure rules, and deliver the five-minute presentation. No actual course submission is claimed.
