# Quality review

Run this review before returning an authored, revised, API-delta, or review result. Fix non-blocking defects directly. Ask only when a required decision cannot be established from assigned evidence.

## Consistency gate

- Outcome appears before implementation detail.
- Scope, exclusions, target behavior, and unchanged behavior agree.
- Explicit decisions remain present and baseline is not presented as target.
- Existing contracts are referenced accurately; changed contracts are isolated.
- No endpoint, field, role, state, permission, or current behavior is invented.
- Profile concerns appear only when relevant.
- Review findings distinguish release-blocking decisions from gaps that can be resolved in an authorized revision.
- Acceptance criteria are observable and traceable to requirements.
- Test levels match project convention and change risk.
- No empty section, unresolved template token, secret, personal data, or local absolute path remains.
- The artifact does not drift into implementation or detailed execution planning.

## Ambiguity scan

Check six failure modes:

1. **Reference:** unclear target behind terms such as this, old, same, or previous.
2. **Default:** missing initial role, state, sort, timezone, fallback, or selection.
3. **Scope:** uncertain ownership of adjacent UI, API, data, migration, platform, or device work.
4. **Sequence:** unspecified ordering, retry, race, reload, expiry, or asynchronous completion.
5. **Measurement:** subjective terms without an observable baseline or threshold.
6. **Authority:** unclear actor for an action, decision, transition, or override.

Do not turn every ambiguity into a question. Search authoritative evidence first. A question is blocking only when plausible answers create incompatible scope, contracts, permissions, persistence, or user-visible behavior.

## Two-implementer test

Ask whether two competent implementers could satisfy every stated criterion while delivering materially different observable behavior or public contracts. If yes, add the missing decision or report a blocker. Differences in equivalent internal implementation do not fail this test.
