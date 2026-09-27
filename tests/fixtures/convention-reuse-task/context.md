# Repository context

- Approval is an agreed backend-only operation: `POST /api/orders/{id}/approve` with `{ "expectedVersion": number }`; it moves a Submitted order to Approved and returns the existing Order DTO with its incremented `version`.
- Existing command endpoints accept `Idempotency-Key` and persist command outcomes. Their detailed header-absence and key-reuse rules are not included in this excerpt, and no change to that convention is requested.
- An order's numeric `version` participates in optimistic concurrency; a competing approval against a stale version uses the existing stale-version error envelope.
- The agreed resource-scoped approval role is `OrderManager`. Approval and its audit event commit in one transaction; an audit failure rolls both back.
