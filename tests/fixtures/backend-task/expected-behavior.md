# Expected behavior

## Required

- Route to the backend profile only.
- Define the Submitted-to-Approved transition, authorization boundary, invalid source states, and existing error-envelope reuse.
- Specify retry semantics through the existing idempotency mechanism.
- Specify the concurrency winner/stale-request outcome using the existing version mechanism without inventing a new lock strategy.
- Make order mutation and audit persistence atomic and state the rollback expectation.
- Include contract, authorization, idempotency, concurrency, and transaction-failure acceptance scenarios.

## Forbidden

- UI requirements, frontend component guidance, or URL-state checks.
- A new authentication scheme or error format.
- Vague requirements such as handling concurrency safely without an observable result.
