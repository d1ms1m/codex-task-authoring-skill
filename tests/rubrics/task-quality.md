# Task quality rubric

Score each applicable invariant as pass or fail and cite evidence from the produced artifact or interaction. An invariant marked not applicable needs a short factual reason.

## Routing and scope

- The selected frontend, backend, or fullstack profile matches the requested delivery boundary.
- Review mode reports findings without modifying or silently replacing the input task.
- The result is a task specification, not a detailed implementation sequence.
- Irrelevant profile checklists do not appear merely for completeness.

## Evidence and decisions

- Repository facts, user decisions, assumptions, and blockers are distinguishable.
- Baseline and target behavior are not conflated.
- Explicit user decisions and unchanged behavior are preserved.
- Unknown endpoints, fields, statuses, roles, and constraints are not invented.

## Contracts and ambiguity

- API delta contains only missing or changed backend capabilities.
- A materially contract-changing unknown produces one focused blocking question.
- A safe non-blocking unknown becomes a labeled assumption rather than an interruption.
- Two competent implementers would deliver equivalent observable behavior and contracts.

## Profile behavior

- Relevant frontend work covers URL/deep-link/reload behavior, view state, and shared presentation with variable actions.
- Relevant backend work covers authorization, state transitions, idempotency, concurrency, transaction boundaries, and rollback.
- Fullstack work assigns ownership, separates immediately implementable client work from blocked work, and defines compatible contract rollout.

## Acceptance and hygiene

- Acceptance criteria are observable and binary enough for review.
- Relevant positive, negative, permission, loading, empty, error, retry, or stale-state scenarios are covered.
- No empty sections, invented examples, local paths, secrets, or unresolved scaffold markers remain.
