# Repository context

- The application is a web React client with an existing `/orders` route.
- `OrdersTable` already renders order rows and accepts columns, empty-state content, and row actions.
- The API client already exposes `listOrders({ state })`, `cancelOrder(id)`, and `reorder(id)`.
- Active maps to `state=open`; History maps to `state=closed`.
- The agreed URL contract is `/orders?view=active` and `/orders?view=history`. A missing or unknown `view` value selects Active and replaces the URL with the canonical Active value without adding a history entry.
- Active rows may expose Cancel when `canCancel` is true. History rows may expose Reorder when `canReorder` is true.
- Existing row actions disable while their request is pending. Success shows the existing success announcement and refetches the current view; failure keeps the row and selection unchanged, shows the existing request-error toast, and permits retry by invoking the action again.
- The current page has loading, empty, request-error, and permission-denied components that should be reused.
- Project tests use component tests plus Playwright for routing scenarios.
