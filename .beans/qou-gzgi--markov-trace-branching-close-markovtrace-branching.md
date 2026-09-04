---
# qou-gzgi
title: 'Markov trace branching: close markovTrace_branching field'
status: in-progress
type: task
priority: normal
tags:
    - lean
created_at: 2026-08-24T06:35:58Z
updated_at: 2026-09-03T22:18:46Z
parent: qou-c8p8
---

MarkovIdentificationContext.markovTrace_branching in markov_identification.lean. May be closable from existing Markov trace infrastructure.



## 2026-09-03 — claimed (branch claude/markov-identification-instance-2026-09-03)
Closable now: MarkovTraceInstance.eq_wtrace_of_markov (every Markov trace at z_D equals the Ocneanu-weighted seminormal trace) + wtrace_apply IS the decomposition tr_M = sum_lam w_lam tr_{S_lam}, general n, sorry-free. Plan: new library file QOU/FeynmanPathIntegrals/MarkovIdentificationInstance.lean with an enumeration of the size-(n+1) diagrams by a natural index (Fintype.equivFin), a constructor MarkovIdentificationContext.ofMarkovTrace T x whose markovTrace_branching field is PROVED from eq_wtrace_of_markov, and the specialised markov_identification. Duplicates to close with it: qou-4pzd, qou-loq3.



## 2026-09-03 20:40Z — CORRECTION of my own verification claim on PR #6526
PR body said 'the import cone was not touched by the intervening commits'. FALSE: 16 SchurWeyl files changed on main between 440c6a164f and 2a7dfce761 (SeminormalRep 167 non-comment lines, SeminormalInequivalence 144, QJucysMurphyEigen 100, ...), several in the cone of MarkovTraceInstance, and my lean-direct run used the restored oleans, which predate them. Banner placed on the PR. Re-verifying by rebuilding every QOU module in the target's transitive cone from current source with lean -o in dependency order (script: scratchpad/rebuild_cone.py, log /tmp/rebuild_cone.log), then recompiling the target. TRAP for memory: 'lean-direct exit 0' certifies against the oleans ON DISK, which after a restore are a snapshot — check git diff <branch-point>..origin/main on the cone before claiming it is untouched.



## re-targeted at the qou-z9ws Prop (2026-09-03 21:5xZ)
main's b34a9c689b removed the class under PR #6526. Rebased; the instance is now the theorem markovTrace_branching_of_markovTrace (Prop proved at the Markov-trace data) + markov_identification_of_markovTrace. Compiles against main's base file, 0 errors, sorry-free, axioms propext/choice/Quot.sound. Sidecar regenerated; validate exit 0.
