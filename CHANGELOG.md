# Changelog

All notable changes to this project are documented here.

## [0.1.1] - 2026-09-28

### Fixed

- Prevented unnecessary blocking questions about unspecified details of unchanged existing contracts; the skill now completes authorized work while referencing established conventions without inventing new rules.
- Kept genuine permission and contract conflicts blocking, with a focused question explaining their effect on the deliverable.

### Changed

- Added a convention-reuse regression fixture and blind GPT-6 Astra/Sol forward-test evidence.
- Audited active instructions against current GPT-6 prompting, Codex Skills, Skill Creator, and evaluation guidance; made explicit user instructions take precedence over skill defaults and kept Review-mode questions to one decision.
- Replaced the installation example for the unpublished tag with a verified published tag, refreshed English/Russian documentation and official sources, and marked the original design as historical.
- Added an explicit-user-instruction fixture, current-model forward-test evidence, and a metadata-only trigger audit. Kept unsupported claims about actual installed-skill activation out of the release evidence.

## [0.1.0] - 2026-08-29

### Added

- Compact `codex-task-authoring` entrypoint with Author, Review, Revise, and API-delta modes.
- Evidence-based frontend, backend, and fullstack profile routing with progressive disclosure.
- Shared task contract, minimal API-delta guidance, official OpenAI guidance, and final quality review.
- Adaptable task and API-delta templates.
- Versioned frontend, backend, fullstack, ambiguity, review, and trigger fixtures.
- Deterministic repository validation, behavioral rubric, public documentation, MIT license, and attribution notice.
- Complete English and Russian README files with reciprocal language navigation.
