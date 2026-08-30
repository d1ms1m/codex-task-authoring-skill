# {{feature_name}} API delta

> Include only absent or changed backend capability. Remove guidance, unused sections, and all `{{...}}` tokens before delivery.

## Feature dependency

{{why_the_current_contract_cannot_complete_the_user_outcome}}

## Existing contract reference

{{stable_reference_without_reproducing_unchanged_schema}}

## Required deltas

### {{operation_or_schema_fragment}}

- Purpose: {{feature_requirement}}
- Contract change: {{method_path_event_or_changed_fragment}}
- Authorization and states: {{authority_and_valid_conditions}}
- Errors and repeated requests: {{observable_failure_idempotency_and_concurrency_behavior}}
- Compatibility: {{mixed_version_behavior_and_safe_absence}}
- Readiness: {{backend_completion_evidence_and_blocking_status}}

## Acceptance criteria

- {{observable_contract_condition}}

## Approved temporary fallback

{{include_only_when_explicitly_agreed}}
