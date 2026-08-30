# Repository context

- Orders currently move from Draft to Submitted. The persisted status enum already includes Approved, but no Submitted-to-Approved transition or data backfill exists.
- Authenticated principals carry resource-scoped roles. `OrderManager` is the agreed role for approval.
- The agreed public operation is `POST /api/orders/{id}/approve` with body `{ "expectedVersion": number }`. Success returns the existing Order DTO with `status=Approved` and its incremented `version`.
- Existing command endpoints accept an `Idempotency-Key` header and persist command outcomes.
- Order rows have a numeric `version` used by other state-changing commands for optimistic concurrency.
- State changes and audit events can share one database transaction.
- The service maps domain validation, forbidden access, and stale versions to existing error envelopes.
- Adding the transition requires no schema migration or backfill.
- No frontend lives in this repository.
