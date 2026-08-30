# Backend tasking

Apply only the server concerns that can change the contract, integrity, access, or operational result.

## Contract and authority

- Establish operation owner, protocol or method, path/topic, changed request and response semantics, error mapping, and compatibility.
- Define authentication and authorization by role and resource; UI visibility never substitutes for server enforcement.
- Preserve existing envelopes, versioning, and conventions unless their change is explicitly required.

## Domain integrity

- Name valid starting states, transitions, validation rules, invariants, and terminal outcomes.
- Define what a repeated command means and whether an existing idempotency mechanism applies.
- For concurrent writers, specify the observable winner, stale-request behavior, conflict response, and retry boundary without inventing a locking strategy unsupported by evidence.
- State transaction boundaries and what must roll back together. Cover partial failure across database writes, queues, notifications, audit records, or other side effects.

## Delivery and operations

- When data shape changes, address migration/backfill need, mixed-version compatibility, rollout order, and rollback.
- For asynchronous work, cover retry ownership, deduplication, poison/failure behavior, and completion evidence.
- Include relevant audit, logs, metrics, tracing, performance limits, pagination, and security constraints when risk or project rules require them.

## Verification

Select unit, contract, authorization, integration, concurrency, migration, and failure-injection tests according to the change. Acceptance criteria should make permission denials, invalid states, duplicate requests, stale versions, and rollback observable when applicable.
