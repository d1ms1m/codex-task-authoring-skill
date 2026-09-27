# Expected behavior

## Required

- Produce an implementation-ready backend task, without pausing for missing details of the unchanged `Idempotency-Key` convention.
- Reference the established header and persisted-outcome behavior rather than inventing rules for missing keys or reuse with different payloads.
- Define the supplied authorized transition, same-command retry outcome through the existing convention, stale-version loser, and atomic audit rollback with observable acceptance.
- Preserve the existing response and error formats.

## Forbidden

- A blocking question solely about unspecified edge cases of an unchanged command convention.
- A new idempotency-key policy, header requirement, endpoint, status, or error envelope.
- UI work or a step-by-step implementation plan.
