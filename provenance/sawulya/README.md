# Emerging Technology Adoption Agent — Assignment 6

Specialization of frozen MASY1800 scaffold. Student files: `agent_metadata.json`, `specialist_instructions.md`, `cases/*.json`, `responses/*_response.json`, `records/agent_record.md`. Core files unchanged.

Run from scaffold root:
```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json
python tools/validate_response.py agents/adoption_agent/responses/primary_response.json
```

The included JSONs are modeled educational case analyses, not field-measured AI underwriting results. Publish this local working copy to your own GitHub repository and record branch/commit before submitting.
