# Assignment 6 — agent development and test record (2026-11-02)

This is an instructional test using hypothetical organizations, NOT a measured bank deployment.

- v1.0 weakness (constructed diagnostic draft): “Banks are highly regulated, so reject machine-learning credit tools.” This generic answer fails to distinguish human-support POC from autonomous denials and ignores local controls. It is a deliberate negative test example, not a fabricated earlier model execution.
- v1.1 revision: added consequence gate, alternatives, reversible POC/shadow options, strong evidence labels, stop rules and explicit triggers.
- Primary (risk-averse regional bank; human-supervised): PROOF OF CONCEPT, offline and non-production.
- Contrast 1 (same ET/application, digital bank with controls): BOUNDED EXPERIMENT, 90-day shadow mode.
- Contrast 2 (autonomous denials; missing reasons): DEFER live use.
- Stable: general uncertainty about model-specific maturity, relevance of validation and CFPB adverse-action standards.
- Changed: experiment feasibility, action category and severity of safeguards.
- Qualification case: Without vendor validation and explainability evidence, abstain from recommending production adoption even if management wants it.
- Test method: response JSONs drafted through reasoned ChatGPT analysis of the scenarios, then checked against the frozen local validator. These are representative simulated runs; actual model/vendor measurements remain unavailable.
- Independent judgment: pursue an offline POC at the regional bank, with advancement contingent on audited local results, capability and compliance approval.
- Team handoff: pass staffing, training and change-readiness assessment to Organizational Adoption Agent; adoption agent must not claim to resolve it.
- Repo: https://github.com/sawulya/Lab-6---SubAgent-5-Adoption
Branch: main
Commit: See latest commit on main.
