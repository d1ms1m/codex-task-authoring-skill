# Expected behavior

## Required

- Route to the frontend profile without loading backend-specific delivery requirements.
- Preserve the existing API as unchanged and omit an API delta.
- Define URL encoding, default and invalid-value behavior, direct opening, reload, Back, and Forward.
- Prefer one shared table presentation with view-specific action data or callbacks rather than duplicated markup.
- Cover loading, empty, error, permission, disabled-action, and successful-action behavior when relevant.
- Provide observable component and browser-level acceptance criteria.

## Forbidden

- Inventing a new endpoint, DTO field, role, or state value.
- Producing file-by-file implementation steps or a commit sequence.
- Adding backend concurrency, transaction, or migration checklists to this client-only task.
