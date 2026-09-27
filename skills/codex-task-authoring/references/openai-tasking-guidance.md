# OpenAI tasking guidance

Last verified: 2026-09-28.

Official sources:

- [Codex skills](https://developers.openai.com/codex/skills) and [official Skill Creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)
- [Current OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model.md)
- [GPT-6 prompting best practices](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#prompting-best-practices)
- [Prompting](https://developers.openai.com/api/docs/guides/prompting.md) and [evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices.md)

## Stable guidance used by this skill

- Keep the entrypoint focused and disclose conditional detail through references.
- Make the skill description concise and discriminating because it controls implicit selection.
- Favor lean instructions: state a rule once, retain domain context and hard constraints, and omit generic process noise.
- Define authorization and autonomy boundaries so safe read-only analysis can continue while external, destructive, costly, or scope-expanding work stops for approval.
- Treat explicit user instructions as higher priority than skill defaults, subject to platform instructions. Tell the model which ambiguities require a question and define observable success criteria. GPT-6 Astra can ask more clarifying questions and is sensitive to skill instructions: finish authorized in-scope work when an established unchanged convention covers a routine gap; ask only for an unresolved decision that changes the outcome.
- Keep task prose concise and specific; choose verification proportionate to risk. Evaluate prompt changes with representative fixtures rather than presuming one model run guarantees future behavior.

When the user requests current OpenAI behavior, model properties, API details, Codex behavior, or installation guidance, use `$openai-docs` when it is available; otherwise fetch the current official page directly before asserting it. Use official OpenAI documentation rather than community material for those claims. Do not treat this dated summary as evidence of current pricing, availability, limits, aliases, or defaults.
