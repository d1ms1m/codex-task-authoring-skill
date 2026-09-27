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

## v0.1.1 — 2026-09-27

**Method.** Each of the six fixture requests and context excerpts was sent to a fresh, ephemeral, read-only `codex exec` session for each of `gpt-6-sol` and `gpt-6-astra`. The selected skill entrypoint, routed references, and (for authoring) template were supplied in the prompt; expected behavior and rubric were *not* supplied to the model. Output was then reviewed against the fixture expectations and shared rubric. The source fixtures and skill remained untouched by the runs. This tests the instructions' output behavior, not installed-skill discovery, real-repository inspection, or implicit trigger selection.

**Before change.** Two independent GPT-6 Astra runs of the original `backend-task` stopped to ask for details of the already established `Idempotency-Key` convention rather than deliver a task. Five original GPT-6 Sol cases reached their intended primary outcomes; the original blocking-ambiguity replies were terse. A first draft of the new `convention-reuse-task` passed on Astra even before the change because its request explicitly said to preserve the convention. It does not by itself prove the regression fix; the original `backend-task` is the discriminating case.

| Fixture | GPT-6 Sol after change | GPT-6 Astra after change | Evidence |
| --- | --- | --- | --- |
| `frontend-task` | PASS | PASS | Reused OrdersTable and existing API; URL canonicalization, reload/history, actions, and stale-response behavior were specified. |
| `backend-task` | PASS | PASS | Delivered Submitted → Approved task, reused the established idempotency convention without stopping, and covered version conflicts and atomic audit rollback. |
| `convention-reuse-task` | PASS | PASS | Described the supplied contract and required reuse of existing header/key rules without inventing missing details or asking a question. |
| `fullstack-task` | PASS | PASS | Split client/server ownership, compatible rollout, fallback, and minimal API delta with end-to-end criteria. |
| `ambiguous-task` | PARTIAL | PARTIAL | One focused member-versus-owner question; both identified the conflict's effect on authorization and acceptance and stopped before authoring. Neither reply explicitly stated that the dialog's exact wording is non-blocking, as required by the fixture; no question about the wording was asked. |
| `review-task` | PASS | PASS | Found API-scope blocker and revision gaps, asked one decision question, and did not edit the reviewed task. |

**Scope and limitations.** The `ambiguous-task` omission fails one fixture expectation; it is not a permission decision or an extra blocker. No v0.1.1 implicit-trigger audit was run: the 4-positive/6-negative counts above belong to v0.1.0 and are not new-model measurements. Read-only ephemeral runs cannot verify write-mode file hygiene or installation in a real project. Model sampling can vary; external-project pilots and actual implicit activation remain outstanding before claiming broader generalization.

## v0.1.1 guidance audit — 2026-09-28

Official current sources: [GPT-6 model and prompting guide](https://developers.openai.com/api/docs/guides/latest-model.md), [Codex skills](https://developers.openai.com/codex/skills), [OpenAI Skill Creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator), and [evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices.md). The Codex skills page was checked through the official OpenAI Developer Docs MCP when ordinary HTTP access was intermittent. These sources informed a targeted instruction-priority rule, concise skill packaging, and proportionate behavioral checks. API-only features such as async tool calling and reasoning configuration do not apply to this documentation skill.

**Blind output checks.** Eight fixtures per model were run in fresh sessions with the entrypoint, only routed references, and fixture input without expected outputs. The six Author fixtures were assessed in the final full-suite run; the two Review fixtures and the blocking `ambiguous-task` were rerun after the final mode-boundary edit. On those latest outputs, both Astra and Sol produced **7/8 full passes** against all fixture expectations. The explicit English instruction in `user-override-task` produced an English task on both models while allowing Russian UI copy, as requested. The blocking Review case identified the API-scope conflict and ended with one question on both models in the latest run. An earlier Sol sample placed the question inside the findings; the new `review-no-blocker` case reported no findings and asked no question on both models. The blocking-permission `ambiguous-task` remained **PARTIAL** for both: one correct permission question and no final task, but neither explicitly named dialog wording as non-blocking. One earlier Sol sample switched to Russian despite English fixture input; the final sample was in English. The omitted dialog note is recorded as a limitation, not a passing fixture.

**Trigger-description audit.** Ten interleaved requests from [`trigger-cases.md`](trigger-cases.md) were classified independently from frontmatter and invocation metadata, without revealing expected labels. GPT-6 Luna and GPT-6 Astra each returned four expected positive and six expected negative selections. This is a metadata-selection simulation, **not proof of implicit activation in a loaded Codex session**.

**Integration boundary.** This environment's separately spawned Windows Codex CLI rejected workspace file reads under both read-only and workspace-write policies; therefore actual skill loading and write-mode behavior were not certified in that CLI. Prompt-provided resources test model behavior rather than Codex filesystem discovery. No unpublished repository version was substituted for the globally installed published skill, and no external-project pilot was claimed.
