# Repository context

- The Projects list currently fetches `GET /api/projects` and renders project rows on a nonempty successful array.
- The page already has loading and request-error components; an empty successful array currently leaves a blank content area.
- A shared `EmptyState` component accepts a heading and body. The empty-state copy has been approved: heading `No projects`, body `Create your first project to get started`.
- The existing API and authorization behavior remain unchanged. Component tests cover the Projects page.
