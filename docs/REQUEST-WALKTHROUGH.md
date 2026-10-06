# Individual explanation: one adviser request

1. The browser sends a question to `/api/adviser`. It never sends an API key or a chosen user role.
2. Sites authenticates ChatGPT identity and forwards trusted identity headers. The application checks a registered users row and enforces its own role/rate policy.
3. The backend loads the current design, relevant country metrics, claims and actual source records from D1 using prepared queries. Browser-only sensitivity changes do not silently change saved evidence.
4. The backend sends the question and relevant records to OpenAI Responses with a narrow evidence policy. The model can request only fixed read/calculation tools. It cannot select arbitrary URLs or write SQL.
5. The server executes any allowed tool and supplies results. Energy and investment results come from application code.
6. The server checks the structured answer and citation IDs against retrieved sources, returns answer/assumptions/unknowns/citations and records token usage. The browser renders text safely through React.
7. Missing identity gives 401, missing registration gives 403, and a missing hosted AI credential gives an explicit 503. No canned answer masquerades as a model response.

A valid citation ID proves that a source exists, not that it supports every sentence. Real saved-input, missing-fact, citation, certification-boundary and malicious-source tests were run; detailed scope is recorded in VALIDATION.md. One malicious-source fixture is not a general prompt-injection guarantee. The server also supplies and displays deterministic full-load energy, preventing reliance on model-generated arithmetic for this value.
