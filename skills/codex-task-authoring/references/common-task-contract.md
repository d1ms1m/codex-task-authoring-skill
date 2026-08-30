# Common task contract

Use these semantics without forcing the same headings onto every artifact. Include a section only when it carries a decision, constraint, risk, or verification rule.

## Evidence labels

- **Fact:** observed in code, tests, an assigned artifact, or primary documentation.
- **Decision:** explicitly selected by the user or an authorized source.
- **Assumption:** a reversible working choice that does not alter scope or a public contract.
- **Blocker:** missing or conflicting information that permits incompatible outcomes.

Do not blur a fact about today's implementation with a decision about the target state. Cite paths, symbols, document sections, or links when they make an assertion auditable.

## Required meaning

Capture the following when relevant:

- **Outcome:** the new user or system capability, stated before mechanics.
- **Baseline:** current observable behavior and the evidence establishing it.
- **Scope:** included behavior, surfaces, roles, systems, and artifacts.
- **Exclusions:** neighboring work deliberately deferred or prohibited.
- **Behavior:** entry conditions, actions, state transitions, errors, retries, and terminal results.
- **Unchanged behavior:** compatibility or existing flows at meaningful regression risk.
- **Contracts:** existing interfaces to reuse and only the changes actually required.
- **Dependencies:** owners, ordering, blocking status, rollout constraints, and agreed fallbacks.
- **Architecture constraints:** project rules, reuse boundaries, compatibility requirements, and justified extension points.
- **Verification:** test levels proportionate to risk plus observable acceptance criteria.
- **Open items:** only remaining assumptions and blockers.

Empty sections, generic reassurance, research diaries, and lists of files without a decision do not improve a task.

## Scope and implementation freedom

Prefer the smallest change that achieves the outcome and preserves unrelated behavior. Reuse existing components, models, adapters, requests, and state unless separation is an explicit extension point or evidence supports divergence. Do not turn a feature task into a hidden cleanup or migration.

Calibrate specificity to risk. Keep local reversible work compact; record more decisions when permissions, migrations, concurrent or asynchronous behavior, cross-system delivery, irreversibility, or failure cost increase.

Specify internal structure only when it is a compatibility boundary, project rule, required reuse point, or otherwise changes the observable result. Equivalent internal implementations should remain possible.

## Acceptance criteria

Each criterion should be pass/fail from observable behavior or a verifiable contract. When material, include actor or permission, starting state, action, and expected result. Cover relevant negative, error, retry, stale-data, reload, and partial-failure cases rather than adding a generic requirement to handle edge cases.

Every criterion must trace to a requirement. Avoid internal function names unless they are themselves a required interface.
