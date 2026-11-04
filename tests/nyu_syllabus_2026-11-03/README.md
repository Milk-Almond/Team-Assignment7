# NYU syllabus-checking question test record

Tested agent: Adoption 1.0-team-review at commit 970af738df5272d57674370d7d95c39c03dbc6ac. Instructions unchanged. Source questions and source PDF hash are preserved.

| Question | Recorded answer | Evaluation |
|---|---|---|
| 1 Business context | B | Higher-education administrative syllabus review |
| 2 Technology/application | C | Leading edge is the classroom assumption; local fitness remains unknown |
| 3 Action now | A | Supervised bounded pilot versus manual checklist; staff approval retained |
| 4 Organizational posture | D | A may pilot; B defers live trial pending independent application evidence |
| 5 Expansion evidence | B | Representative quality and net time-saving results, review and rollback |

Result: 5/5 aligned with the case-based answer key inferred by this reviewer. The provided PDF contains questions/options, not an official answer key. Q4 has two frozen-contract responses (A/B), so six response files are saved. This is not an instructor-issued score.

## Method and limits
The current interactive Codex model read the agent instructions and applied them to these questions. Responses were composed in this session and written into JSON files; Python builds packets and checks records, not model inference. This is an AI-assisted same-session walkthrough, not isolated fresh-chat execution, a blind test, or independent/repeated benchmarking. The same model generated and evaluated responses. Do not interpret 5/5 as measured reliability. Original responses were retained without a post-score rewrite. No real NYU trial or policy was observed.

Each case has intake JSON, complete prompt packet, frozen-schema JSON response, and selected-option/reasoning sidecar. Sidecars keep quiz labels out of the frozen output schema. Proposed numerical pilot bounds are clearly distinguished from given facts. No new external vendor or legal claim was needed: leading-edge status is explicitly a classroom assumption.

## Informative weakness preserved
Q4 reveals an instruction ambiguity: the existing MONITOR rule prefers monitoring when external comparative evidence is the binding prerequisite, while DEFER postpones an activity pending a prerequisite. Both could appear to fit Program B. The response selects DEFER for the live trial and describes monitoring as its evidence-gathering activity, matching option D. Record this as **qualified pass / category ambiguity**, not proof the ambiguity is solved in repeated runs. Proposed future clarification: an explicit authorization gate blocks the named activity -> DEFER; external observation is the supporting task. Do not silently revise the tested version.
Q3 is also conditional: approved environment/documents and staff review support pilot direction, but owner/budget must be confirmed before execution. Numerical design suggestions are not teacher facts.

## Five supplied student inputs
The user reconfirmed all five links as the designated student inputs. All remain attributed and preserved in provenance and records/candidate_comparison.md. The fourth supplied repository currently contains a Diffusion specialist. It counts as an inspected supplied input; it does not demonstrate a fifth Adoption implementation. This test set evaluates the integrated team Adoption agent, not five independently executed individual agents.

## Reproduce checks
Run `python tests/nyu_syllabus_2026-11-03/verify.py`. For independent behavioral evidence, open each saved prompt in a separate ChatGPT conversation and preserve its raw response without replacing this run. No such independent execution is claimed here.
