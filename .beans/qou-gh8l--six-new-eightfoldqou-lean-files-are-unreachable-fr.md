---
# qou-gh8l
title: Six new Eightfold/QOU Lean files are unreachable from QOU.lean, so lake build never compiles them
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:36:45Z
updated_at: 2026-09-04T09:36:45Z
---

MEASURED 2026-09-04 on branch claude/lean-prove-assertions-2026-09-04. QOU.lean carries 848 imports and NONE of this PR's six new files: ContactDistributionRank, SelfDualityDegree, CalculusDimensionObstruction, CoveringDegreeRamification, HyperbolicVolumeFormType, CommutativeImageDegeneration. Confirmed by grep on QOU.lean.

WHY IT MATTERS. A standalone library .lean with no .ts/.md sibling has no <block>.qa.json and escapes every per-block checker (AGENTS.md 'QA is agent-owned; CI is a backup' says this explicitly). Being unreachable from the library root ADDS a second layer: lake build QOU would never elaborate them either, so the only thing that has ever checked them is an agent running lean-direct by hand. That is the documented gate today - CI auto-triggers are disabled repo-wide - but it means a later refactor upstream can break these files and nothing will say so.

NOT A DEFECT OF THIS PR SPECIFICALLY - it is the existing pattern; all five pre-existing files on this branch are in the same state, which is why the sixth matches them rather than being wired in unilaterally. Wiring one in without the others would be inconsistent, and wiring all six in cannot be verified here (the tree carries .lake/RESTORED-NO-TRACES; lake build would evict the restored oleans, bean qou-r13s).

WHAT TO DO, and it is a judgement call for the author: (a) add all six imports to QOU.lean in one commit, on a machine that can run lake build QOU to confirm the root still elaborates - cheap there, unverifiable here; (b) leave them standalone and rely on the lean-direct gate, which is what the corpus does today; (c) decide the Eightfold tree should have its own root module. DEFAULT if nothing is done: they stay as they are, verified by hand, exactly like every other file in this tree.
