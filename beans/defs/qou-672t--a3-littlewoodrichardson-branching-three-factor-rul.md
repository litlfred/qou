---
# qou-672t
title: 'A=3 Littlewood–Richardson branching: three-factor rule + weight identity at H_9 on committed T/³He characters (iterated BranchingData in Lean + probe)'
status: completed
type: task
priority: normal
created_at: 2026-09-16T05:49:42Z
updated_at: 2026-09-16T06:17:07Z
---


## 2026-09-16 — built and measured (PR #7434 branch)

Lean: BranchingPushforwardMultiplicativity.lean section Iterated — c₃ (Σ_κ c^κ_{μν} c^λ_{κρ}), branching₃, weight_branching₃, trM_tensor₃; sorry-free, lean-direct -DautoImplicit=false exit 0, axioms propext/Classical.choice/Quot.sound. Probe computations/probes/lr_a3_three_factor_branching_probe.py (8/8): at H_9 the three-factor rule reproduces the committed free products of T and 3He on all 30 blocks (worst 2.6e-49); (6,3)→9 weight identity on 33 pairs (2.5e-51); iterated identity on 27 triples (2.0e-51); Σyδ pinned by the bond product; cos(angle between T and 3He unit deviation directions) = 0.99114 (≈7.6°). Doc: docs/audits/2026-09-16-bean-up-and-roast-lr-a3-mobius-composition-reeb-datum.md §2. Completed: the branching is built and checked; what remains (the letter that produces the deviation) is qou-8r6b.
