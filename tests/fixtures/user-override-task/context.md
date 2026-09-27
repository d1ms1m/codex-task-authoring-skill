# Repository context

- Project documentation and the existing Projects page copy are in Russian.
- The frontend already has a Projects page that fetches `GET /api/projects`; a successful response returns an array of projects.
- The page already has loading and request-error presentation. With an empty successful array it currently renders an empty content area.
- The shared `EmptyState` component supports a heading and body. No new API call, permission, or backend change is needed.
