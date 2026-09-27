# Expected behavior

## Required

- Produce the requested frontend task in English, despite Russian-language repository conventions.
- Return the task in the response without attempting to create or edit any file.
- Define the empty-success state using the existing shared `EmptyState`; preserve existing populated, loading, and error behavior and the GET contract.
- Use observable acceptance for zero and nonzero project results; leave the nonessential headline wording to project convention without asking for copy approval.

## Forbidden

- A question about translation, copy approval, or whether to write a file.
- Invented backend capability, API field, or detailed implementation plan.
