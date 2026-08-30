# Behavioral validation

This directory defines observable behavior for `codex-task-authoring`. It does not prescribe exact headings or compare complete generated documents.

## Automated repository checks

Run the standard-library contract tests from the repository root:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

These checks cover packaging, resource discoverability, invocation metadata, fixture completeness, and public-artifact hygiene. They do not claim that static text checks prove model behavior.

## Forward-test procedure

For each directory under `fixtures/`:

1. Start a fresh Codex task with the built skill available.
2. Provide only `request.md`, `context.md`, and any additional input file in that fixture.
3. Do not provide `expected-behavior.md` to the authoring run.
4. Evaluate the result against `expected-behavior.md` and `rubrics/task-quality.md`.
5. Record pass/fail and concrete evidence outside the fixture source; do not rewrite an expectation to excuse a failure.

For implicit invocation, use the prompts in `trigger-cases.md` without naming the skill. A positive case passes only if task-authoring behavior is visible. A negative case passes only if the skill does not divert an implementation, debugging, discovery, or generic editing request into specification authoring.

Generated wording and section order may differ. Judge routing, decisions, boundaries, and testability.
