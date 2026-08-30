---
# qou-cs76
title: 'D-infinity descent: the per-step formulation is the wrong shape — block descent reduction + candidate heights'
status: completed
type: task
priority: normal
created_at: 2026-08-29T18:44:37Z
updated_at: 2026-08-30T02:40:32Z
parent: qou-ifot
---

LANDED 2026-08-29, PR #6042, commit b62f18df8a. Files: content/quantum-observable-universe/lean/QOU/AppendixSurreals/collatz_block_descent.lean + computations/qcollatz_block_structure_probe.py.

THE FINDING. Every termination lemma in the corpus is PER-STEP (corpus-grepped: no multi-step variant exists anywhere). That is the wrong shape. The orbit decomposes into blocks -- one odd step, then v even steps -- with net change 1 - v, contractive exactly when v >= 2. And v >= 2 IS the contact-boundary condition <v_[2]> >= 2 the paper already states. So the framework's own convergence criterion is about BLOCKS while every available reduction was per-STEP: candidate measures were being tested against a requirement the problem never had.

DELIVERED (sorry-free): reaches_of_block_descent (descent somewhere ahead suffices; step count varies per point, unbounded); per_step_is_block_descent (the n=1 case, so it SUBSUMES reaches_of_descent_of_forward); block_length_ne_zero (the 0 < n hypothesis is automatic, so omitted); domainStable_iterate (D_inf closed under iteration, not just one step); reaches_cycle_of_block_descent_domainStable -- now the sharpest reduction of the convergence half in the corpus.

DOES NOT RESCUE v_[2], and the file says so. block_descent_measure_pos_off_target: mu is N-valued so mu(f^[n] P) < mu P is impossible wherever mu P = 0, for every n. qou-4atn's refutation survives the weakening verbatim. Weakening buys nothing for any measure vanishing off the attractor -- the search is over HEIGHTS, not valuations.

MEASURED: all three natural heights (L1, span, L1+span) rise on exactly 30 of 742 steps -- precisely the 30 odd steps, one per block -- and descend across ALL 30 blocks (0 flat, 0 up). Per-step fails where per-block succeeds, on identical data. Block lengths v in {6,12,18}; zero blocks with v=0, so no two consecutive odd steps occurred in this sample.

SCOPE -- two limits, both real. (1) This is a REDUCTION, not a proof: one open requirement replaced by a weaker open requirement, no mu supplied. Supplying one closes q-Collatz-on-a-QOU. (2) The probe CANNOT be evidence for the conjecture -- the backward tree is generated FROM the attractor, so every element converges by construction and no counterexample can appear in it. What it shows is that block descent is the right SHAPE, not that any height descends in general.

NEXT for whoever picks this up: the open question is now 'does some height descend per block on all of D_inf', and the honest sub-question that is actually attackable is whether block length v is bounded below on D_inf (the sample says v >= 6, but the sample is the attractor's own backward tree and proves nothing). A proof that v >= 2 always would close convergence via this reduction.

FOLLOW-ON, same PR, commit 7001595736: the block SHAPE is not automatic, and the trichotomy is now proved.

The reduction assumed 'one odd step then a run of evens'. That is not a theorem about the map. A q-odd element is P = -1 + [2]_q A, and the odd branch then simplifies to one ring identity, oddStep_of_qOdd_form: [3]P + 1 = [2](-q + [3]A), so C(P) = -q + [3]A. Evaluating at the divisor (oddStep_next_residue) gives residue 1 + A(-1), hence:
  A(-1) = -1 -> residue  0 -> next step EVEN (block continues)
  A(-1) = -2 -> residue -1 -> next step ODD  (a v = 0 block)
  otherwise               -> orbit LEAVES the domain
That trichotomy is what makes 'block' well defined.

consecutive_odd_steps_exist (A = -2) shows two consecutive odd steps ARE possible: over Z[q], P = -2q-3 |-> -2q^2-3q-2, both residue -1. Derived by hand from the identity BEFORE probing; the probe then reproduced the predicted image exactly.

MEASURED with its limit stated: 1420 consecutive-odd starts (degree <= 3, coeffs in [-6,6]) -- NONE reached the cycle, all left the domain, 1320 within two steps, longest prefix 6. Bounded coefficient-box search, NOT a proof.

SO THE OPEN SUB-QUESTION IS NOW SHARP: can a v = 0 block occur inside D_inf? If not, the block decomposition is total on D_inf and 'v >= 1' is free; if so, the decomposition needs a third case. Either answer is progress and neither is currently known.

Pattern worth noting: this repeats qou-4atn exactly -- the phenomenon exists in the domain and every witness found escapes D_inf. Two different questions, same shape of answer. That is now twice, which suggests D_inf is much thinner than the domain in a way nobody has characterised; a characterisation of D_inf would likely settle both.

Verified: lean-direct exit 0 (one first-pass error, an unreduced phi 2 numeral cast, fixed with map_ofNat). Axioms: oddStep_of_qOdd_form [propext, Quot.sound], the other two standard. No sorryAx.

SELF-CORRECTION 2026-08-29, before anyone acts on it. At the end of the previous turn I recommended characterising D_inf as the next target, saying it 'isn't obviously equivalent to the whole conjecture'. THAT IS WRONG, and qcz7 says so in the very route I was pointing at. A1 reads verbatim: 'Conjecture from the probe: D_inf = backward-orbit tree union_k C^{-k}(cycle). If proved, convergence is immediate (tautological).'

Why it is equivalent: the backward-orbit tree IS {P : exists k, C^[k] P = attractor}. So 'D_inf subset of tree' is literally reaches_cycle on D_inf -- the conjecture. Only the reverse inclusion (tree subset of D_inf) is the easy half. Characterising D_inf is therefore not a stepping stone; it is the same problem wearing a different name.

Deliberately NOT formalized as a Lean theorem: the equivalence is Iff.rfl once both sides are unfolded, and a rfl theorem asserting a tautology is precisely what AGENTS.md 'no trivial trues / no tautologies' bans. It is an observation about framing, so it belongs in prose, here.

So the scoreboard for this arc is now: descent measure (any mu closes the conjecture), D_inf characterisation (equivalent to the conjecture), q=1 height (provably cannot reach the critical ratio, qou-n3xf), any valuation (provably cannot descend, qou-4atn). Three routes are the whole problem and one is provably dead.

THE ONE GENUINELY BOUNDED OPEN ITEM LEFT in this arc is the v=0 question from the trichotomy: can two consecutive odd steps occur inside D_inf? It is not equivalent to the conjecture -- a NO makes the block decomposition total on D_inf (strengthening reaches_cycle_of_block_descent_domainStable's applicability), a YES forces a third case in the block accounting. Either answer is informative and neither closes anything. That is the honest recommendation, replacing the wrong one.

v=0 QUESTION ATTACKED 2026-08-29, commit 3735ba33f1. Answer to 'is it Lean-provable': PARTLY, and the split is the point.

PROVED (sorry-free; axioms [propext, Quot.sound] only -- not even Classical.choice):
- cubeRoot_one_add_mul_neg: (w+1) is a unit with inverse -w, when w^2+w+1=0.
- oddPreimage_forces_eval_cubeRoot: evaluating the odd step [2]P = [3]Q + 1 at a primitive cube root w kills the [3] term outright, ELIMINATING Q and pinning P(w) = -w. So P(w) = -w is necessary for an odd-preimage to exist.
- attractor_no_oddPreimage: q^-1 evaluates to w^2, and w^2 = -w would force 1 = 0. So NO q-odd element maps to the attractor under the odd branch -- the attractor is reached ONLY by even steps. This is the structural reason odd-preimages are so rare in the backward tree (6 of 154 nodes at depth 40, 20 of 1260 at depth 120), now proved rather than observed.
All stated over generic CommRing with w a ring element satisfying w^2+w+1=0, rather than constructing Z[w] -- nothing specialises (7c).

NOT PROVED, and flagged as such in the file, the commit and here: the measured obstruction is a CONGRUENCE. Across 1260 backward-tree nodes every node admitting an odd-preimage has P'(w) = -w (mod 6), whereas a chained odd-preimage needs P'(w) = 2, and 2 is not congruent to -w mod 6 because N(2+w)=3 does not divide N(6)=36. That is an OBSERVED PATTERN over a finite sample. It is not a theorem and must not be cited as one.

WHY IT IS NOT TRIVIALLY PROVABLE: the pair (P(w), P'(w)) is NOT closed under the odd branch-inverse -- computing the preimage's derivative at w needs P''(w), so the natural two-coordinate invariant does not close. The even branch-inverse does act cleanly ((u,v) -> ((1+w)u, u+(1+w)v), and 1+w is a unit so N(u) is preserved), which is presumably where the mod-6 regularity comes from; but the odd branch divides by (1+2w), of norm 3, and that is what breaks the closure. A proof likely needs the full jet, not the 1-jet.

STATUS OF v=0: still OPEN. Now with a proved necessary criterion, a proved fact about the attractor, and a precisely stated congruence conjecture whose proof would settle the case for the backward TREE. The step from the tree to all of D_inf is the convergence conjecture itself (qcz7 A1), so even proving the congruence would not close v=0 on D_inf.
