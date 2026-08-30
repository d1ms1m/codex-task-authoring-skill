# Fullstack tasking

Use this reference after the frontend and backend references. It coordinates the boundary rather than repeating their checklists.

## Partition the delivery

- Assign ownership for client, API, data, and operational changes.
- Identify client work possible against today's contract and work blocked on backend capability.
- Keep one feature-level source for shared behavior; profile tasks should reference it and add only their responsibility.

## Synchronize the contract

- Align field optionality, enums, errors, permissions, ordering, and state-transition semantics across sides.
- Define fixture and contract-test synchronization without copying the whole API schema into the feature task.
- Keep backend authorization authoritative even when the client hides or disables actions.

## Plan compatible delivery

When sides deploy independently, prefer an additive backend-first path unless assigned architecture says otherwise. Define old-client/new-server and new-client/old-server behavior, feature flags or fallbacks when agreed, and the condition for removing temporary compatibility.

End-to-end acceptance must cover the user outcome across the boundary, including failure and permission behavior, while profile acceptance remains scoped to each owner.
