# Frontend tasking

Apply only the checks that affect the requested client experience.

## Navigation and state

- Identify roles, entry points, routes, query or path parameters, and the default view.
- For URL-backed state, define direct opening, reload, unknown values, and Back/Forward behavior.
- Preserve stable deep links and existing navigation unless change is in scope.

## Rendered behavior

- Cover applicable loading, empty, error, partial-data, permission, stale, and success states.
- Define relevant mouse, keyboard, confirmation, disabled, and hidden-control behavior.
- For lists and tables, decide applicable columns, ordering, filters, pagination, row selection, stable identity, and scroll restoration.
- State responsive, accessibility, focus, and keyboard expectations when the surface requires them.
- Use mockups for intended observable behavior, but follow current approved decisions when they conflict and do not carry incidental or stale visual details into the task.

## Composition and data boundaries

Reuse project UI wrappers and shared presentation. When roles or views share layout but expose different operations, prefer data-driven actions, slots, or callbacks over copied markup. Separate role-specific components only when they are intentional divergence points, and keep their shared internals below that boundary.

Keep transport DTOs at the API boundary. Use existing mappers, adapters, or view models where the project already separates server shape from presentation.

Do not introduce a new endpoint or field merely to complete a client task. If a required capability is missing, route to the API-delta reference.

## Verification

Choose the project's established component, integration, browser, accessibility, and visual tests according to risk. Acceptance should exercise observable routing and state behavior, not just the presence of components. Multi-view or deep-link work needs direct URL and reload coverage.
