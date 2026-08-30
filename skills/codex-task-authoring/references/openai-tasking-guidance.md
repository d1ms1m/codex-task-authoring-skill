# OpenAI tasking guidance

Last verified: 2026-08-29.

Official sources:

- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)

## Stable guidance used by this skill

- Keep the entrypoint focused and disclose conditional detail through references.
- Make the skill description concise and discriminating because it controls implicit selection.
- Favor lean instructions: state a rule once, retain domain context and hard constraints, and omit generic process noise.
- Define authorization and autonomy boundaries so safe read-only analysis can continue while external, destructive, costly, or scope-expanding work stops for approval.
- Tell the model which ambiguities require a question and define observable success criteria.

When the user requests current OpenAI behavior, model properties, API details, Codex behavior, or installation guidance, use `$openai-docs` when it is available; otherwise fetch the current official page directly before asserting it. Use official OpenAI documentation rather than community material for those claims. Do not treat this dated summary as evidence of current pricing, availability, limits, aliases, or defaults.
