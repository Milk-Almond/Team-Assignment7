# Team Lab 7 — Emerging Technology Adoption Agent

Version **1.2-team-review**. Technical synthesis and local verification package; actual team approval and workshop-process evidence remain unrecorded.

## Start here
- [Team Agent Record](agents/adoption_agent/records/agent_record.md)
- [Synthesis comparison](records/candidate_comparison.md), [decision](records/decision_log.md), [dissent](records/dissent_and_bias_review.md)
- [Requirements audit](deliverables/requirements_audit.md) and [verification log](deliverables/verification_log.txt)
- [Sources](records/evidence_register.md), [contributions](records/contributions.md), [inventory](records/agent_inventory.md), [handoff](records/integration_issues.md)

## Run and use
Python 3 with `pip install -r requirements.txt` (includes jsonschema for the added full-schema checks).
```sh
python scripts/verify_team.py
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json
```
Open the generated work/adoption_agent_primary_prompt.txt in ChatGPT, run it, save the actual JSON, then validate with tools/validate_response.py and rerun the verifier. No API key is required. Existing responses are explicitly labeled fixtures in the test log, not independent repeat runs.

## Proposed management decision
A four-week synthetic/public-data shadow experiment can test comparative workflow value under assumed permissions, two reviewers and USD 2000 total cap. Decisive factor: authorized reversible learning. Missing controls or a material error changes current action to DEFER. Successful screening permits further evaluation, not automatic ADOPT.

## Submission
Review the requirements audit with all members; record the actual decision, dissent, contribution and workshop evidence, and review all five individual Adoption inputs (sawulya replaces the previously supplied Diffusion link). One designated member submits the team repository/package and Agent Record to Brightspace within the course's one-day posting window. GitHub posting alone does not submit to Brightspace. Do not mark approval or classroom attendance without evidence.

## Classroom-question test records
[NYU syllabus checking: five questions, six context responses](tests/nyu_syllabus_2026-11-03/README.md). Answers B/C/A/D/B align with reviewer-inferred case reasoning; Q4 category ambiguity preserved. Same-session AI walkthrough, not independent benchmarking.

## Version 1.1 integration
All five individual Adoption candidates are now compared, including [sawulya](https://github.com/sawulya/Lab-6---SubAgent-5-Adoption), which replaces the mistaken prior-team Diffusion input. See [concrete source contributions](records/candidate_comparison.md) and [v1.1 NYU regression](tests/nyu_syllabus_v1_1/README.md). Prior v1.0 and NYU records are historical. Current procurement contrast_1 is DEFER for the explicitly blocked experiment; monitoring is supporting evidence collection. All regression responses remain reference examples rather than independently generated model runs.

[Repeat-upload v1.1 test](tests/nyu_repeat_upload_v1_1/README.md): answers B/C/A/D/B; Q4 qualified due to surviving MONITOR/DEFER instruction conflict. Records retained without rewriting earlier runs.

## Current category rule (v1.2)
The historical MONITOR/DEFER conflict is repaired in the active definitions and ordered rule 4. Explicit unmet prerequisite for a named trial -> DEFER; observation-only decision with no named blocked activity -> MONITOR. Old tests retain their original qualified status. See [repair record](records/monitor_defer_v1_2.md).
