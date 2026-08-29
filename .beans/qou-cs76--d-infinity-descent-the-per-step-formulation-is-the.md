---
# qou-cs76
title: 'D-infinity descent: the per-step formulation is the wrong shape — block descent reduction + candidate heights'
status: completed
type: task
priority: normal
created_at: 2026-08-29T18:44:37Z
updated_at: 2026-08-29T18:50:30Z
parent: qou-ifot
---

LANDED 2026-08-29, PR #6042, commit b62f18df8a. Files: content/quantum-observable-universe/lean/QOU/AppendixSurreals/collatz_block_descent.lean + computations/qcollatz_block_structure_probe.py.

THE FINDING. Every termination lemma in the corpus is PER-STEP (corpus-grepped: no multi-step variant exists anywhere). That is the wrong shape. The orbit decomposes into blocks -- one odd step, then v even steps -- with net change 1 - v, contractive exactly when v >= 2. And v >= 2 IS the contact-boundary condition <v_[2]> >= 2 the paper already states. So the framework's own convergence criterion is about BLOCKS while every available reduction was per-STEP: candidate measures were being tested against a requirement the problem never had.

DELIVERED (sorry-free): reaches_of_block_descent (descent somewhere ahead suffices; step count varies per point, unbounded); per_step_is_block_descent (the n=1 case, so it SUBSUMES reaches_of_descent_of_forward); block_length_ne_zero (the 0 < n hypothesis is automatic, so omitted); domainStable_iterate (D_inf closed under iteration, not just one step); reaches_cycle_of_block_descent_domainStable -- now the sharpest reduction of the convergence half in the corpus.

DOES NOT RESCUE v_[2], and the file says so. block_descent_measure_pos_off_target: mu is N-valued so mu(f^[n] P) < mu P is impossible wherever mu P = 0, for every n. qou-4atn's refutation survives the weakening verbatim. Weakening buys nothing for any measure vanishing off the attractor -- the search is over HEIGHTS, not valuations.

MEASURED: all three natural heights (L1, span, L1+span) rise on exactly 30 of 742 steps -- precisely the 30 odd steps, one per block -- and descend across ALL 30 blocks (0 flat, 0 up). Per-step fails where per-block succeeds, on identical data. Block lengths v in {6,12,18}; zero blocks with v=0, so no two consecutive odd steps occurred in this sample.

SCOPE -- two limits, both real. (1) This is a REDUCTION, not a proof: one open requirement replaced by a weaker open requirement, no mu supplied. Supplying one closes q-Collatz-on-a-QOU. (2) The probe CANNOT be evidence for the conjecture -- the backward tree is generated FROM the attractor, so every element converges by construction and no counterexample can appear in it. What it shows is that block descent is the right SHAPE, not that any height descends in general.

NEXT for whoever picks this up: the open question is now 'does some height descend per block on all of D_inf', and the honest sub-question that is actually attackable is whether block length v is bounded below on D_inf (the sample says v >= 6, but the sample is the attractor's own backward tree and proves nothing). A proof that v >= 2 always would close convergence via this reduction.
