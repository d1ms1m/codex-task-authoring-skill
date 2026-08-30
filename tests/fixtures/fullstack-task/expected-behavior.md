# Expected behavior

## Required

- Route to fullstack and apply common, frontend, backend, and fullstack guidance.
- Separate immediately buildable layout/current-status work from owner, permission, and transition work blocked on backend changes.
- Reuse the current GET contract by reference; the API delta lists only additive owner/allowed-transition data and the new transition operation.
- Define ownership, compatible backend-first rollout, temporary client behavior before new fields exist, and end-to-end acceptance.
- Preserve backend authority even when the client hides unavailable actions.

## Forbidden

- Restating unchanged `id`, `name`, and `status` schemas in the API delta.
- Inventing role rules that conflict with the assigned lifecycle source.
- Assuming simultaneous deployment or exposing the transition optimistically before backend confirmation.
