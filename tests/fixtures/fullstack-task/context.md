# Repository context

- `GET /api/projects/{id}` currently returns `id`, `name`, and `status`.
- The client already fetches that endpoint and has shared loading, not-found, and forbidden states.
- The current DTO has no owner display data and no allowed-transition information.
- No endpoint currently changes project status.
- Existing authorization is resource-scoped, but the exact roles allowed to transition status are defined in `docs/project-lifecycle.md` supplied as an authoritative source: Owner and ProjectAdmin.
- Backend enums already define the allowed status graph.
- The web and API services deploy separately and support additive contract rollout.
- The approved additive GET delta is `version: number`, `owner: { id: string, displayName: string } | null`, and `allowedTransitions: ProjectStatus[]` ordered by the lifecycle graph. Existing `id`, `name`, and `status` are unchanged and remain documented only in the current API specification.
- The approved mutation is `PATCH /api/projects/{id}/status` with `{ "targetStatus": ProjectStatus, "expectedVersion": number }`. Success returns `{ "status": ProjectStatus, "version": number, "allowedTransitions": ProjectStatus[] }`.
- The mutation reuses the standard error envelope: forbidden access is HTTP 403, stale version is HTTP 409, and a transition disallowed by the lifecycle graph is HTTP 422. After a timeout, the client refetches before offering another attempt.
- Before the additive GET fields are available, the client may render the existing status but uses an em dash for owner and does not render the transition control. Explicit `owner: null` also renders an em dash; it does not mean the backend is unavailable.
