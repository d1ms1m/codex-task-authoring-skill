# Projects list empty state

## Outcome

When `GET /api/projects` succeeds with an empty array, display the existing shared `EmptyState` component with heading `No projects` and body `Create your first project to get started` instead of the blank content area.

## Boundaries

Reuse the existing Projects fetch and `EmptyState`. Preserve nonempty-row rendering, loading, request-error, API contract, and authorization behavior. No backend change or unrelated page redesign is in scope.

## Acceptance

- Given an empty successful response, the page displays the approved heading and body through `EmptyState` and does not display project rows.
- Given a nonempty successful response, the existing project rows appear and `EmptyState` does not.
- While the request is loading or when it fails, the existing corresponding component appears, not `EmptyState`.
- Component tests verify each of these states; no additional API request is introduced.
