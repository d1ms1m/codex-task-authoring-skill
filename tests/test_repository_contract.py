from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "codex-task-authoring"

REQUIRED_SKILL_FILES = {
    "SKILL.md",
    "LICENSE.txt",
    "NOTICE.md",
    "agents/openai.yaml",
    "references/common-task-contract.md",
    "references/frontend-tasking.md",
    "references/backend-tasking.md",
    "references/fullstack-tasking.md",
    "references/api-delta-requirements.md",
    "references/openai-tasking-guidance.md",
    "references/quality-review.md",
    "assets/task-template.md",
    "assets/api-delta-template.md",
}

FIXTURES = {
    "frontend-task": {"request.md", "context.md", "expected-behavior.md"},
    "backend-task": {"request.md", "context.md", "expected-behavior.md"},
    "fullstack-task": {"request.md", "context.md", "expected-behavior.md"},
    "ambiguous-task": {"request.md", "context.md", "expected-behavior.md"},
    "review-task": {
        "request.md",
        "context.md",
        "input-task.md",
        "expected-behavior.md",
    },
}

REQUIRED_REPOSITORY_FILES = {
    ".gitignore",
    ".github/workflows/validate.yml",
    "README.md",
    "README.ru.md",
    "requirements-dev.txt",
    "LICENSE",
    "NOTICE.md",
    "CHANGELOG.md",
    "tests/forward-test-report.md",
}


_MARKDOWN = MarkdownIt("commonmark")


def _markdown_link_targets(text: str) -> list[str]:
    targets: list[str] = []
    pending = list(_MARKDOWN.parse(text))
    while pending:
        token = pending.pop()
        if token.children:
            pending.extend(token.children)
        attribute = "href" if token.type == "link_open" else "src"
        if token.type not in {"link_open", "image"}:
            continue
        target = token.attrGet(attribute)
        if target:
            targets.append(target)
    return targets


class RepositoryContractTests(unittest.TestCase):
    def read_required(self, relative_path: str) -> str:
        path = SKILL_ROOT / relative_path
        self.assertTrue(path.is_file(), f"Required file does not exist: {relative_path}")
        return path.read_text(encoding="utf-8")

    def test_required_skill_files_exist(self) -> None:
        missing = sorted(
            path for path in REQUIRED_SKILL_FILES if not (SKILL_ROOT / path).is_file()
        )
        self.assertEqual([], missing, f"Missing required skill files: {missing}")

    def test_public_repository_files_exist(self) -> None:
        missing = sorted(
            path for path in REQUIRED_REPOSITORY_FILES if not (ROOT / path).is_file()
        )
        self.assertEqual([], missing, f"Missing repository files: {missing}")

    def test_public_docs_cover_use_installation_limits_and_attribution(self) -> None:
        readme = (ROOT / "README.md")
        russian_readme = ROOT / "README.ru.md"
        notice = (ROOT / "NOTICE.md")
        changelog = (ROOT / "CHANGELOG.md")
        license_file = (ROOT / "LICENSE")
        for path in (readme, russian_readme, notice, changelog, license_file):
            self.assertTrue(path.is_file(), f"Required file does not exist: {path.name}")

        readme_text = readme.read_text(encoding="utf-8")
        russian_text = russian_readme.read_text(encoding="utf-8")
        self.assertIn("English | [Русский](README.ru.md)", readme_text)
        self.assertIn("[English](README.md) | Русский", russian_text)
        badge = (
            "[![skills.sh](https://skills.sh/b/d1ms1m/"
            "codex-task-authoring-skill)](https://skills.sh/d1ms1m/"
            "codex-task-authoring-skill)"
        )
        self.assertIn(badge, readme_text)
        self.assertIn(badge, russian_text)
        for concept in (
            "$codex-task-authoring",
            "frontend",
            "backend",
            "fullstack",
            "API delta",
            "Install",
            "Limitations",
            "Development and validation",
        ):
            self.assertIn(concept, readme_text)

        for concept in (
            "$codex-task-authoring",
            "frontend",
            "backend",
            "fullstack",
            "API delta",
            "Установка",
            "Ограничения",
            "Разработка и проверка",
        ):
            self.assertIn(concept, russian_text)

        self.assertIn("docs-ai-prd", notice.read_text(encoding="utf-8"))
        self.assertIn("0.1.0", changelog.read_text(encoding="utf-8"))
        self.assertIn("MIT License", license_file.read_text(encoding="utf-8"))

    def test_readmes_order_remote_local_and_codex_installation(self) -> None:
        english_text = (ROOT / "README.md").read_text(encoding="utf-8")
        russian_text = (ROOT / "README.ru.md").read_text(encoding="utf-8")
        github_master_url = (
            "https://github.com/d1ms1m/codex-task-authoring-skill/tree/master/"
            "skills/codex-task-authoring"
        )
        github_tag_url = github_master_url.replace(
            "/tree/master/", "/tree/v0.1.0/"
        )
        codex_prompts = (
            f"$skill-installer Install the skill from {github_master_url}",
            f"$skill-installer Install the skill from {github_tag_url}",
        )
        remote_commands = (
            "npx skills add d1ms1m/codex-task-authoring-skill "
            "--skill codex-task-authoring --global --agent codex",
            "npx skills add d1ms1m/codex-task-authoring-skill "
            "--skill codex-task-authoring --agent codex",
        )
        local_commands = (
            "npx skills add . --skill codex-task-authoring --global --agent codex",
            "npx skills add . --skill codex-task-authoring --agent codex",
        )
        cli_update_commands = (
            "npx skills check",
            "npx skills update",
        )

        installation_cases = (
            (
                english_text,
                "### Install via skills.sh from a remote repository",
                "### Install via skills.sh from a local copy",
                "### Install in Codex from GitHub",
                (
                    "No local clone or visit to skills.sh is required.",
                    "`--global` makes the skill available in every Codex project; "
                    "omit it to install only in the current project.",
                    "`--agent codex` installs it for Codex only.",
                ),
                (
                    "root of a local copy",
                    "`--global` makes the skill available in every Codex project; "
                    "omit it to install only in the current project.",
                    "`--agent codex` installs it for Codex only.",
                ),
                (
                    "In a Codex message, run:",
                    "To pin the version",
                    "next turn",
                    "restart Codex",
                ),
                "After this repository is published",
                "The Skills CLI is not an OpenAI product.",
            ),
            (
                russian_text,
                "### Установка через skills.sh из удалённого репозитория",
                "### Установка через skills.sh из локальной копии",
                "### Установка в Codex из GitHub",
                (
                    "Клонировать репозиторий или открывать skills.sh не нужно.",
                    "`--global` делает skill доступным во всех проектах Codex; "
                    "уберите флаг, чтобы установить его только в текущий проект.",
                    "`--agent codex` устанавливает skill только для Codex.",
                ),
                (
                    "корня локальной копии",
                    "`--global` делает skill доступным во всех проектах Codex; "
                    "уберите флаг, чтобы установить его только в текущий проект.",
                    "`--agent codex` устанавливает skill только для Codex.",
                ),
                (
                    "В сообщении Codex запустите:",
                    "Чтобы зафиксировать версию",
                    "следующем сообщении",
                    "перезапустите Codex",
                ),
                "После публикации репозитория",
                "Skills CLI не является продуктом OpenAI.",
            ),
        )
        for (
            text,
            remote_heading,
            local_heading,
            codex_heading,
            remote_prose,
            local_prose,
            codex_prose,
            obsolete_prose,
            local_disclaimer,
        ) in installation_cases:
            self.assertIn(remote_heading, text)
            self.assertIn(local_heading, text)
            self.assertIn(codex_heading, text)
            self.assertLess(text.index(remote_heading), text.index(local_heading))
            self.assertLess(text.index(local_heading), text.index(codex_heading))

            after_remote_heading = text.split(remote_heading, 1)[1]
            remote_section, after_local_heading = after_remote_heading.split(
                local_heading, 1
            )
            local_section, after_codex_heading = after_local_heading.split(
                codex_heading, 1
            )
            codex_section = after_codex_heading.split("\n## ", 1)[0]

            for marker in (*remote_commands, *remote_prose):
                self.assertIn(marker, remote_section)
            self.assertNotIn("npx skills add .", remote_section)
            self.assertNotIn("$skill-installer", remote_section)

            for marker in (*local_commands, *local_prose, *cli_update_commands):
                self.assertIn(marker, local_section)
            self.assertNotIn("d1ms1m/codex-task-authoring-skill", local_section)
            self.assertNotIn("$skill-installer", local_section)

            for marker in (*codex_prompts, *codex_prose):
                self.assertIn(marker, codex_section)
            self.assertNotIn("OWNER", codex_section)
            self.assertNotIn(obsolete_prose, codex_section)
            self.assertNotIn("npx skills add", codex_section)

            self.assertIn(local_disclaimer, local_section)

    def test_local_markdown_links_resolve(self) -> None:
        failures: list[str] = []
        for source in ROOT.rglob("*.md"):
            if any(part in {".git", ".serena", ".tmp", "dist"} for part in source.parts):
                continue
            text = source.read_text(encoding="utf-8")
            for target in _markdown_link_targets(text):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                relative_path = unquote(parsed.path)
                if not relative_path:
                    continue
                resolved = (
                    ROOT / relative_path.lstrip("/")
                    if relative_path.startswith("/")
                    else source.parent / relative_path
                ).resolve()
                if not resolved.exists():
                    failures.append(f"{source.relative_to(ROOT)} -> {target}")
        self.assertEqual([], failures, "Broken local Markdown links:\n" + "\n".join(failures))

    def test_unmatched_inline_delimiters_do_not_hide_links_across_paragraphs(self) -> None:
        markdown = (
            "Unmatched ` marker.\n\n"
            "[Real link](missing-real-link.md) followed by ` marker."
        )
        self.assertIn("missing-real-link.md", _markdown_link_targets(markdown))

    def test_unmatched_inline_delimiters_do_not_hide_links_across_heading(self) -> None:
        markdown = (
            "Unmatched ` marker.\n"
            "# [Real link](missing-heading-link.md) followed by ` marker."
        )
        self.assertIn("missing-heading-link.md", _markdown_link_targets(markdown))

    def test_russian_readme_preserves_specific_meaning(self) -> None:
        text = (ROOT / "README.ru.md").read_text(encoding="utf-8")
        self.assertIn("настройки моделей по умолчанию", text)
        self.assertIn("обобщаемый пробел", text)

    def test_ci_runs_repository_and_skill_creator_validation(self) -> None:
        workflow = ROOT / ".github" / "workflows" / "validate.yml"
        self.assertTrue(workflow.is_file(), "Validation workflow is missing")
        text = workflow.read_text(encoding="utf-8")
        self.assertIn("requirements-dev.txt", text)
        self.assertIn("unittest discover -s tests -p 'test_*.py' -v", text)
        self.assertIn("quick_validate.py", text)

    def test_blocking_ambiguity_stops_authoring_until_answered(self) -> None:
        text = self.read_required("SKILL.md").lower()
        self.assertRegex(
            text,
            r"ask one (?:focused )?question[^.]*\.\s*stop and wait for the answer",
        )

    def test_forward_test_evidence_covers_behavioral_contract(self) -> None:
        report = ROOT / "tests" / "forward-test-report.md"
        self.assertTrue(report.is_file(), "Versioned forward-test report is missing")
        text = report.read_text(encoding="utf-8").lower()
        for concept in (
            "frontend-task",
            "backend-task",
            "fullstack-task",
            "ambiguous-task",
            "review-task",
            "api delta",
            "non-mutation",
            "false positive",
            "blind",
            "pass",
        ):
            with self.subTest(concept=concept):
                self.assertIn(concept, text)

    def test_fixture_sets_are_complete(self) -> None:
        fixtures_root = ROOT / "tests" / "fixtures"
        for fixture, required_files in FIXTURES.items():
            with self.subTest(fixture=fixture):
                fixture_root = fixtures_root / fixture
                actual = {path.name for path in fixture_root.glob("*.md")}
                self.assertTrue(
                    required_files <= actual,
                    f"{fixture} is missing {sorted(required_files - actual)}",
                )

    def test_skill_frontmatter_is_discriminating(self) -> None:
        text = self.read_required("SKILL.md")
        frontmatter = re.match(r"\A---\s*\n(.*?)\n---", text, re.DOTALL)
        self.assertIsNotNone(frontmatter, "SKILL.md must start with YAML frontmatter")
        metadata = frontmatter.group(1)
        self.assertRegex(metadata, r"(?m)^name:\s*codex-task-authoring\s*$")
        self.assertRegex(metadata, r"(?m)^description:\s*\S.+$")
        lowered = metadata.lower()
        for concept in ("create", "review", "frontend", "backend", "fullstack"):
            self.assertIn(concept, lowered)
        self.assertIn("do not use", lowered)

    def test_entrypoint_is_compact_and_routes_every_resource(self) -> None:
        text = self.read_required("SKILL.md")
        self.assertLess(len(text), 12_000, "SKILL.md should remain a compact router")
        for path in sorted(REQUIRED_SKILL_FILES):
            if path in {"SKILL.md", "LICENSE.txt", "NOTICE.md", "agents/openai.yaml"}:
                continue
            with self.subTest(path=path):
                self.assertIn(path, text, f"SKILL.md does not route to {path}")

    def test_skill_has_no_executable_scripts(self) -> None:
        self.assertFalse((SKILL_ROOT / "scripts").exists())

    def test_openai_yaml_has_safe_implicit_invocation_metadata(self) -> None:
        text = self.read_required("agents/openai.yaml")
        self.assertRegex(text, r'(?m)^\s*display_name:\s*"Codex Task Authoring"\s*$')
        short = re.search(r'(?m)^\s*short_description:\s*"([^"]+)"\s*$', text)
        self.assertIsNotNone(short)
        self.assertGreaterEqual(len(short.group(1)), 25)
        self.assertLessEqual(len(short.group(1)), 64)
        prompt = re.search(r'(?m)^\s*default_prompt:\s*"([^"]+)"\s*$', text)
        self.assertIsNotNone(prompt)
        self.assertIn("$codex-task-authoring", prompt.group(1))
        self.assertRegex(
            text,
            r"(?m)^\s*allow_implicit_invocation:\s*true\s*$",
        )
        self.assertNotIn("dependencies:", text)

    def test_public_artifacts_have_no_scaffold_placeholders_or_local_paths(self) -> None:
        template_assets = {
            SKILL_ROOT / "assets" / "task-template.md",
            SKILL_ROOT / "assets" / "api-delta-template.md",
        }
        paths = [
            ROOT / "README.md",
            ROOT / "README.ru.md",
            ROOT / "NOTICE.md",
            ROOT / "CHANGELOG.md",
            SKILL_ROOT / "agents" / "openai.yaml",
            *SKILL_ROOT.rglob("*.md"),
            *(ROOT / "tests").rglob("*.md"),
        ]
        forbidden = re.compile(
            r"\b(?:TBD|TODO|FIXME|PLACEHOLDER)\b|"
            r"[A-Z]:\\(?:Users|Documents and Settings)\\[^\\/\s]+\\|"
            r"/(?:Users|home)/[^/\s]+/|/root(?:/|\b)|<owner>",
            re.IGNORECASE,
        )
        template_token = re.compile(r"\{\{[^{}\r\n]+\}\}")
        findings: list[str] = []
        for path in paths:
            if not path.is_file():
                continue
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                if forbidden.search(line) or (
                    path not in template_assets and template_token.search(line)
                ):
                    findings.append(f"{path.relative_to(ROOT)}:{line_number}: {line.strip()}")
        self.assertEqual([], findings, "Forbidden public content:\n" + "\n".join(findings))


if __name__ == "__main__":
    unittest.main()
