# API delta requirements

Create a separate API delta only when the requested behavior needs backend capability that is absent or when an existing contract must change. Do not use it as a catalog of every API the client calls.

## Exclude unchanged contracts

Reference existing endpoints, schemas, and documentation by stable identifier. Repeat an unchanged field only when needed to locate or explain the changed fragment. Never invent a future field and label it current.

## Describe each delta

Include the applicable subset of:

- user outcome and why current capability is insufficient;
- new or changed operation identifier, method/path/topic, or event;
- changed request and response fragments, including required and nullable semantics;
- authorization, valid states, errors, ordering, filtering, or pagination;
- idempotency, concurrency, transaction, and side-effect behavior;
- old-client compatibility and safe absence during mixed-version rollout;
- backend readiness criterion and dependency status;
- explicitly approved temporary client fallback.

If an optional field is not required for the first slice, preserve its safe absence and describe later work separately rather than fabricating availability.

Validate each delta item against the backend profile and keep it traceable to a feature requirement.
