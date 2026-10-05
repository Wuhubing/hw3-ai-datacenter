# Functional requirements and acceptance

| Requirement | Implementation | Verification |
| --- | --- | --- |
| FR1 Location and initial design | Decision / System design | UI reviewed |
| FR2 Three countries | Countries: USA, CHN, SGP | D1 and UI checked |
| FR3 Persistent provenance | D1 countries, sources, metrics, designs, claims | Local migration and restart/read verified |
| FR4 External API | Fixed World Bank WDI endpoint | Real refresh returned three validated records |
| FR5 Registered AI questions | Adviser + Responses API route | Registration checked; live AI pending hosted key |
| FR6 Reject unregistered AI calls | Identity + users query in backend | Anonymous rejection checked; unregistered flow to verify in clean session |
| FR7 Cited substantive answers | Structured answer and source-ID validation | Implementation complete; live entailment/injection tests pending |
| FR8 Fact/assumption/calculation/unknown | Claim types and visible evidence labels | UI reviewed |
| FR9 Preserve last valid record | Validate complete API response before batch | Validator tests passed; simulated external failure confirms zero database writes |
| FR10 Update timestamps | Metric retrieval and design update timestamps | Local refresh checked |

Non-goals: construction certification, real-time grid operation, actual procurement authorization, financial advice, measured institutional demand. The ten-year scenario model remains required and implemented.

The site starts private. Public/anonymous application behavior is tested locally. Anonymous access through the hosted platform must wait for an authorized audience change. Application authentication does not imply course membership.
