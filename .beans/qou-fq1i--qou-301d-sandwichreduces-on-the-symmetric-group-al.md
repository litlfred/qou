---
# qou-fq1i
title: 'qou-301d: SandwichReduces on the symmetric-group algebra tower — a growing filtration with a NON-multiplicative trace'
status: in-progress
type: task
created_at: 2026-09-07T18:06:40Z
updated_at: 2026-09-07T20:30:00Z
parent: qou-6g7j
---

qou-301d after #7079: TowerSpan reduces to the local rule g·c·g (SandwichReduces), and InvolutionTowerWitness has a growing filtration but a multiplicative (augmentation) trace, so it exercises TowerSpan's filtration content only. Task: the cheaper of the two towers Mathlib lacks — MonoidAlgebra R (Equiv.Perm (Fin n)) with the standard inclusions, a non-multiplicative Markov-type trace, and SandwichReduces proved there. Zero-sorry; lean-direct with -DautoImplicit=false -s 65536 against the restored cache; state what the witness still does NOT exercise. Roast on record: payoff is hygiene not physics — bound the effort, bean the gap if it does not close.

--------

**2026-09-07 — CLOSED on the symmetric-group tower (PR #7131, branch `claude/symmetric-group-tower-sandwich-2026-09-07`, commit `7fcd686a7a`).**

New module `content/quantum-observable-universe/lean/QOU/MathlibExt/SymmetricGroupTowerWitness.lean` (705 lines, 55 decls, 0 sorry).

Tower: `A = MonoidAlgebra R (Equiv.Perm ℕ)`, `t m = of (swap m (m+1))`, `g = ginv = t`, `H n = adjoin {t m | m < n}` (mirrors InvolutionTowerWitness — subalgebras of one big algebra, inclusions by `adjoin_mono`). Trace = coefficient of the identity, `tr x = x 1`. MarkovTrace axioms: ALL hold with `z = zinv = 0` — `tr (a * t n) = a (s n)` (`idCoeff_mul_t`, via `MonoidAlgebra.mul_single_apply_aux`) and `a (s n) = 0` on `H n` because `s n` moves `n+1` and nothing in `H n` does. Quadratic `t² = 1` (h = 0) so `zinv = z − h = 0` is consistent. No axiom obstructs the identity-coefficient functional.

Proved (lean-direct `-DautoImplicit=false -s 65536` exit 0, `#print axioms` = propext/Classical.choice/Quot.sound on all 18 checked):
- `idCoeff_not_mul_hom`: tr(t t) = 1 ≠ 0 — trace is NOT a hom (the property the involution witness lacked).
- `sandwichReduces_sym`: SandwichReduces at every level `(shiftedUpTo n M, M+1)`. Route: linearity → `c = of w`, `w ∈ W = closure{s n..s M}`; `s(M+1) w s(M+1)` supported on `[n, M+2]`; `doubleCoset`: any perm supported on `[n, M+2]` is in `W ∪ W·s(M+1)·W` (if it fixes M+2 it is in W by generation; else `a = swap(j, M+1)`, `b = s(M+1)·a·u` both in W). Generation `mem_closure_of_suppIn` (adjacent transpositions of an interval generate its supported perms) by double induction `gen_aux`: push the preimage of the top point up by one via `u ↦ u * s i`.
- `towerSpan_sym` / `disjointBlock_sym` via the #7079 chain; `disjointBlock_sym_direct` proves the same law WITHOUT the chain from `W_{<n} ∩ W_{≥n} = {1}` (a perm supported on {0..n} ∩ {n..} is supported on {n}, hence 1) — independent cross-check.
- `t_not_mem_shiftedUpTo`: filtration grows (coefficient-at-`s N` functional kills the stage; `t N` has coefficient 1).
- The pair: `a = 1 + t n ∈ H(n+1)`, `b = 1 + t(n+1) ∈ shifted(n+1)`: `tr(ab) = 1 = tr a · tr b` (cross term `t n t(n+1)` is a 3-cycle, coefficient 0) while `tr(a·a) = 2 ≠ 1` (cross term `t n t n = 1`). `pair_law_disjoint_is_instance` shows the hand computation is literally `disjointBlock_sym` applied.

STILL NOT EXERCISED: q = 1, z = 0, h = 0. The double coset is proved in the permutation model by support arguments — the braid relation is never written; a Hecke tower at q ≠ 1 needs the rewriting proof. SandwichReduces for a Hecke tower remains unproved; the bond-product reading of the atom word remains MEASURED, NOT DERIVED. The disjoint-block law holds here for a reason (trace supported at the identity, W_{<n} ∩ W_{≥n} = {1}) a Hecke trace with z ≠ 0 does not have.

Verification env: restored lake-cache/qou-v4-24-0 + hardlinked shadow rebuild of DisjointBlockTraceLaw / TowerSpanReduction (post-seed, #7079) from main source, exit 0 each. Logs /tmp/sandwich-{deps,1,2,axioms}.log.
