---
# qou-gh8l
title: Six new Eightfold/QOU Lean files are unreachable from QOU.lean, so lake build never compiles them
status: completed
type: task
priority: normal
created_at: 2026-09-04T09:36:45Z
updated_at: 2026-09-05T05:49:04Z
---

MEASURED 2026-09-04 on branch claude/lean-prove-assertions-2026-09-04. QOU.lean carries 848 imports and NONE of this PR's six new files: ContactDistributionRank, SelfDualityDegree, CalculusDimensionObstruction, CoveringDegreeRamification, HyperbolicVolumeFormType, CommutativeImageDegeneration. Confirmed by grep on QOU.lean.

WHY IT MATTERS. A standalone library .lean with no .ts/.md sibling has no <block>.qa.json and escapes every per-block checker (AGENTS.md 'QA is agent-owned; CI is a backup' says this explicitly). Being unreachable from the library root ADDS a second layer: lake build QOU would never elaborate them either, so the only thing that has ever checked them is an agent running lean-direct by hand. That is the documented gate today - CI auto-triggers are disabled repo-wide - but it means a later refactor upstream can break these files and nothing will say so.

NOT A DEFECT OF THIS PR SPECIFICALLY - it is the existing pattern; all five pre-existing files on this branch are in the same state, which is why the sixth matches them rather than being wired in unilaterally. Wiring one in without the others would be inconsistent, and wiring all six in cannot be verified here (the tree carries .lake/RESTORED-NO-TRACES; lake build would evict the restored oleans, bean qou-r13s).

WHAT TO DO, and it is a judgement call for the author: (a) add all six imports to QOU.lean in one commit, on a machine that can run lake build QOU to confirm the root still elaborates - cheap there, unverifiable here; (b) leave them standalone and rely on the lean-direct gate, which is what the corpus does today; (c) decide the Eightfold tree should have its own root module. DEFAULT if nothing is done: they stay as they are, verified by hand, exactly like every other file in this tree.

CORRECTION 2026-09-04: it is SIX files, not 'six/seven'. The seventh, mass-theory/algebraic-geometric-dilog-equivalence.lean, is a CONTENT-BLOCK SIBLING - it lives outside the lean/ Lake root, is resolved through its block's lean.ref, and is not a Lake module at all. It cannot be imported into QOU.lean and was never a candidate.

MEASURED, and it changes the risk assessment: all six are MATHLIB-ONLY LEAVES. grep '^import QOU' over all six returns NOTHING. Imports are Nat.Choose.Basic / Tactic.Linarith / Tactic.NormNum (four of them), Algebra.Ring.Defs + RingTheory.Ideal.Span + Mathlib.Tactic (CommutativeImageDegeneration), GroupTheory.Perm.Sign + Perm.Cycle.Type (CoveringDegreeRamification). With no intra-QOU dependency, adding six import lines CANNOT create a cycle, CANNOT impose an ordering constraint, and CANNOT change the elaboration of anything already in QOU.lean.

So the mathematical risk is gone and only a VERIFICATION risk remains, and it is an artifact of this container rather than of the change: the tree carries .lake/RESTORED-NO-TRACES, so lake build would evict the restore (qou-r13s: 6990 -> 334 mathlib oleans in ten minutes, silently). Full analysis with options: docs/audits/2026-09-04-two-decisions-bdpo-gh8l.md.

RE-MEASURED 2026-09-04 after a mid-session merge, and the blocking premise is STALE.

main landed scripts/lake-restore-trace-check.sh (bean qou-r13s), which records that lake-cache/qou-v4-24-0 was reseeded 2026-08-31 with full trace coverage, so the old recipe's unconditional 'touch .lake/RESTORED-NO-TRACES' now asserts something false in the blocking direction.

Measured on this tree in --report mode: oleans 6173, traced 6170 (100.0%), threshold 90%, exit 0. The marker file is present anyway (touched 2026-09-03 04:36 by the old recipe). So the blanket never-lake-build rests on a stale assertion and the eviction hazard is not present here.

BUT THIS DOES NOT MAKE lake build SAFE, and the script says so itself: present traces are NECESSARY for Lake to accept a restored olean, not demonstrated SUFFICIENT - a trace records input hashes, so Lake rebuilds anyway if the source tree it hashes differs from the one that produced them. This branch has merged ~250 commits from main since the restore, so the source tree HAS diverged. That is exactly the case where full coverage does not protect you.

NET: recommendation C stands but for a sharper reason - not 'we cannot build' but 'a build here would hash a tree ~250 commits ahead of the traces and would likely rebuild anyway'. Do NOT clear the marker on a tree this diverged; re-measure with the script instead of trusting either the marker or this note.


## RESOLVED 2026-09-05 — owner chose A ("2A if you can prove"), and it is NINE not six

This bean and its brief both say SIX. Measured at the time of the edit: NINE
library files on the branch were absent from QOU.lean. The audit predates
ConnectedSumAnnihilator, IndecomposableQuotientPrune and
AmbientInvolutionDoesNotDecideType.

WHAT WAS PROVED, in this container, without lake build:
  - each of the nine, lean-direct, exit 0
  - all nine elaborated TOGETHER in one environment, exit 0
  - 116 FQNs declared by the nine against 39,665 elsewhere in the QOU library:
    ZERO collisions (the "environment already contains" un-importable-module
    error class that check-duplicate-decls exists for)
  - nothing anywhere imports any of the nine, so no cycle is possible
  - 8 of 9 are Mathlib-only leaves; the ninth imports
    QOU.Eightfold.Sym2GateFSTrichotomy, which is ITSELF not in QOU.lean, so the
    edit gains build coverage of that file too

NOT PROVED, and it is the honest residual: `import QOU` cannot be elaborated in
this container at all. QOU/PhotonThreading.lean imports UGB and the UGB oleans
are not in the restored lake-cache, so `lean` fails with "unknown module prefix
'UGB'" before reaching anything of mine. The literal post-edit root build has
NOT been run. What has been proved is each of the three properties that adding
an import can break, separately and directly.

Option C's premise is therefore only half right. C said "defer to a machine that
can build". The measurement says the risk C was hedging against -- cycle, FQN
collision, elaboration failure -- is discharged here; what remains is only that
nobody has watched `lake build QOU` go green with these lines in. Worth doing on
a build-capable machine, but not a blocker.

QOU.lean: 855 -> 864 imports.
