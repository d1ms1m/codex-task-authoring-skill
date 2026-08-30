# Forward-test report

Date: 2026-08-29
Skill version: 0.1.0 candidate

This report records the manual behavioral checks required by the design. It is
evidence from model evaluations, not a deterministic CI transcript. CI verifies
the fixture set, routing contract, metadata, and this report; it does not pretend
to rerun a language model deterministically.

## Method

- A fresh reviewer received `SKILL.md`, only the references routed for the
  selected profile, and one fixture's `request.md` plus `context.md`.
- The reviewer drafted or reviewed the requested artifact **blind**: it did not
  read `expected-behavior.md` or the shared rubric before producing the result.
- The reviewer then opened the expected behavior and rubric, evaluated every
  invariant, and reported failures without editing repository files.
- Failed first-pass fixtures were corrected only when the fixture context had
  omitted a decision assumed by its expected behavior. Fresh reviewers reran
  those fixtures after the context was made decision-complete.

## Fixture results

| Fixture | Routed behavior | Result | Recorded evidence |
| --- | --- | --- | --- |
| `frontend-task` | Frontend profile only | PASS | Preserved the canonical `view` URL state, direct links, reload and history behavior, shared UI, stale-response isolation, existing API, action states, and observable component/browser criteria. |
| `backend-task` | Backend profile only | PASS | Used the supplied approve operation and DTO, resource-scoped authorization, submitted-only transition, idempotent replay, one concurrency winner, atomic audit persistence, rollback, and no migration. |
| `fullstack-task` | Frontend + backend + fullstack references; API delta | PASS | Kept ownership boundaries explicit and limited the API delta to the supplied additive fields and mutation while referring to unchanged contracts. Mixed-version behavior and rollout compatibility remained explicit. |
| `ambiguous-task` | Blocking ambiguity path | PASS | Identified the contract-changing contradiction, asked one focused question, and stopped without producing a final task or inventing a contract. |
| `review-task` | Read-only Review mode | PASS | Separated blockers from revision gaps, identified the API-contract blocker, ended with one focused decision question, and preserved non-mutation because revision was not authorized. |

Across all five fixtures, the shared rubric found no remaining failed invariant.
In particular, the final runs preserved facts versus decisions, labeled safe
assumptions, excluded irrelevant profile checklists, kept task specification
separate from implementation planning, and passed the two-implementer test.

## Trigger-selection audit

The ten cases in [`trigger-cases.md`](trigger-cases.md) were evaluated from the
frontmatter description and invocation metadata.

| Case class | Count | Result |
| --- | ---: | --- |
| Expected activation: author/revise/review task or API delta | 4 | PASS: 4 true positives |
| Expected non-activation: implementation, generic docs, discovery, execution plan | 6 | PASS: 6 true negatives |

Observed false positive count: **0**. Observed false negative count: **0**.

## Review and limitations

- Independent review confirmed the profile-specific acceptance criteria,
  ambiguity stop behavior, API delta minimality, and Review-mode non-mutation.
- The checks are reproducible from the versioned fixture inputs and rubric, but
  language-model output can vary; future releases should rerun the blind review.
- Pilots against external frontend, backend, and fullstack repositories remain a
  release-owner gate because no such repositories were placed in this workspace.
