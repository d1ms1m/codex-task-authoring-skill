# codex-task-authoring

English | [Русский](README.ru.md)

[![skills.sh](https://skills.sh/b/d1ms1m/codex-task-authoring-skill)](https://skills.sh/d1ms1m/codex-task-authoring-skill)

`codex-task-authoring` is a public, standalone Codex skill for creating, revising, and reviewing implementation-ready engineering task specifications. It routes between frontend, backend, and fullstack profiles, loads only relevant guidance, and can produce a separate API delta for backend capabilities that are missing or must change.

The skill is decision-first: it grounds requirements in repository evidence, preserves explicit choices and unchanged behavior, distinguishes blockers from safe assumptions, and writes measurable acceptance criteria. It does not implement the described feature or silently turn the task into an execution plan.

## Use

Invoke it explicitly:

```text
$codex-task-authoring Create an implementation-ready frontend task from these requirements and repository evidence.
```

```text
$codex-task-authoring Review this backend task for contract gaps and untestable acceptance criteria. Do not rewrite it.
```

Its description also supports implicit invocation for requests that clearly ask for an engineering task, feature specification, task review, revision, or API delta. Ordinary implementation, debugging, generic Markdown editing, product discovery, and detailed planning requests are excluded.

Generated artifacts follow the language of the request or project. Technical identifiers remain unchanged when translation would make them ambiguous.

## Profiles and progressive disclosure

- **frontend:** UI behavior, routing and URL state, client state, composition, accessibility, and client-side verification;
- **backend:** contracts, authorization, domain transitions, idempotency, concurrency, transactions, rollout, and operational verification;
- **fullstack:** both profiles plus ownership, API-boundary synchronization, independently deployable rollout, and end-to-end acceptance;
- **API delta:** only absent or changed backend capability, never a duplicate of unchanged API documentation.

`SKILL.md` contains the shared workflow and routing. Conditional detail lives in focused references so unrelated checklists do not consume context.

## Install

### Install via skills.sh from a remote repository

In a terminal, run:

```powershell
npx skills add d1ms1m/codex-task-authoring-skill --skill codex-task-authoring --global --agent codex
```

No local clone or visit to skills.sh is required. The [Skills CLI](https://github.com/antfu/skills-cli) downloads the skill directly from this GitHub repository. `--global` makes the skill available in every Codex project; omit it to install only in the current project. `--agent codex` installs it for Codex only.

For a project-scoped installation, omit `--global`:

```powershell
npx skills add d1ms1m/codex-task-authoring-skill --skill codex-task-authoring --agent codex
```

### Install via skills.sh from a local copy

Run these commands from the root of a local copy:

```powershell
npx skills add . --skill codex-task-authoring --global --agent codex
```

`--global` makes the skill available in every Codex project; omit it to install only in the current project. `--agent codex` installs it for Codex only.

```powershell
npx skills add . --skill codex-task-authoring --agent codex
```

The Skills CLI is not an OpenAI product. Review its source and release diff before a global installation. For either Skills CLI method, use these commands to check for and install updates:

```powershell
npx skills check
npx skills update
```

### Install in Codex from GitHub

In a Codex message, run:

```text
$skill-installer Install the skill from https://github.com/d1ms1m/codex-task-authoring-skill/tree/master/skills/codex-task-authoring
```

To pin the version, use a release tag URL instead of `master`:

```text
$skill-installer Install the skill from https://github.com/d1ms1m/codex-task-authoring-skill/tree/v0.1.0/skills/codex-task-authoring
```

The skill is available on your next turn. If it does not appear, restart Codex. See the official OpenAI [Build skills documentation](https://learn.chatgpt.com/docs/build-skills).

Standalone skills are supported by Codex. Current OpenAI guidance prefers plugin packaging when distributing reusable skills broadly; plugin packaging is intentionally outside the `0.1.x` scope of this repository.

## Repository layout

- `skills/codex-task-authoring/` — installable skill, metadata, references, and output templates;
- `tests/fixtures/` — profile, ambiguity, and review forward-test inputs;
- `tests/rubrics/task-quality.md` — observable behavioral invariants;
- `tests/forward-test-report.md` — versioned blind forward-test and trigger-audit evidence;
- `tests/test_repository_contract.py` — deterministic packaging and hygiene checks;
- `docs/design.md` — approved product direction and rationale.

## Validation

Run deterministic repository checks:

```powershell
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
```

Run the current `quick_validate.py` bundled with OpenAI's `skill-creator` against `skills/codex-task-authoring`. CI fetches a pinned, reviewed revision of the official Skill Creator and runs both validation layers. Behavioral quality still requires forward-testing the versioned fixtures; static checks are not a substitute for model evaluation.

## Limitations

- The skill cannot resolve a contract-changing conflict that is absent from authoritative sources; it asks one focused question and stops.
- It does not guarantee that community installers, model defaults, prices, product availability, or API behavior remain current.
- It is documentation-oriented and read-only toward product code and external systems by default.
- Version `0.1.0` uses rubric-based forward tests rather than a brittle exact-output harness.

## Development and validation

When changing the skill, keep the entrypoint compact, put conditional guidance in one discoverable reference, and add or update a behavioral fixture for every behavior change. Run repository tests, Skill Creator validation, and the affected forward-test scenarios before proposing a change. Do not add a rule for a single anecdotal failure unless the fixture demonstrates a reusable gap.

## License

MIT. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
