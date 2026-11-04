# Adoption specialist

This is an interactive ChatGPT agent built from the frozen course scaffold. The specialist instructions are its analytical logic; the Python tools only assemble prompts and validate saved responses. No API key is needed. It is not an autonomous purchasing system.

Run from the repository root:

```bash
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json
```

Read the resulting work/adoption_agent_primary_prompt.txt into ChatGPT. Save its JSON-only response as agents/adoption_agent/responses/primary_response.json, then run:

```bash
python tools/validate_response.py agents/adoption_agent/responses/primary_response.json
python scripts/verify_submission.py
```

Repeat for contrast_1 and contrast_2. Prompt construction does not execute the model. Saved examples are from the interactive creation session; later outputs can vary. Before reuse, verify dated evidence and replace synthetic assumptions with authorized organizational facts.

See records/test_record.md for observed behavior and limitations, records/evidence_register.md for sources, records/agent_record.md for the complete submission record, and records/team_handoff.md for integration.
