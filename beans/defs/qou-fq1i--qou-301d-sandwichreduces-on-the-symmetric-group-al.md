---
# qou-fq1i
title: 'qou-301d: SandwichReduces on the symmetric-group algebra tower — a growing filtration with a NON-multiplicative trace'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:06:40Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-k4oq
---

qou-301d after #7079: TowerSpan reduces to the local rule g·c·g (SandwichReduces), and InvolutionTowerWitness has a growing filtration but a multiplicative (augmentation) trace, so it exercises TowerSpan's filtration content only. Task: the cheaper of the two towers Mathlib lacks — MonoidAlgebra R (Equiv.Perm (Fin n)) with the standard inclusions, a non-multiplicative Markov-type trace, and SandwichReduces proved there. Zero-sorry; lean-direct with -DautoImplicit=false -s 65536 against the restored cache; state what the witness still does NOT exercise. Roast on record: payoff is hygiene not physics — bound the effort, bean the gap if it does not close.

--------

**2026-09-07 — CLOSED on the symmetric-group tower (PR #7131, branch `claude/symmetric-group-tower-sandwich-2026-09-07`, commit `7fcd686a7a`).**

New module `folio/quantum-observable-universe/lean/QOU/MathlibExt/SymmetricGroupTowerWitness.lean` (705 lines, 55 decls, 0 sorry).

Tower: `A = MonoidAlgebra R (Equiv.Perm ℕ)`, `t m = of (swap m (m+1))`, `g = ginv = t`, `H n = adjoin {t m | m < n}` (mirrors InvolutionTowerWitness — subalgebras of one big algebra, inclusions by `adjoin_mono`). Trace = coefficient of the identity, `tr x = x 1`. MarkovTrace axioms: ALL hold with `z = zinv = 0` — `tr (a * t n) = a (s n)` (`idCoeff_mul_t`, via `MonoidAlgebra.mul_single_apply_aux`) and `a (s n) = 0` on `H n` because `s n` moves `n+1` and nothing in `H n` does. Quadratic `t² = 1` (h = 0) so `zinv = z − h = 0` is consistent. No axiom obstructs the identity-coefficient functional.

Proved (lean-direct `-DautoImplicit=false -s 65536` exit 0, `#print axioms` = propext/Classical.choice/Quot.sound on all 18 checked):
- `idCoeff_not_mul_hom`: tr(t t) = 1 ≠ 0 — trace is NOT a hom (the property the involution witness lacked).
- `sandwichReduces_sym`: SandwichReduces at every level `(shiftedUpTo n M, M+1)`. Route: linearity → `c = of w`, `w ∈ W = closure{s n..s M}`; `s(M+1) w s(M+1)` supported on `[n, M+2]`; `doubleCoset`: any perm supported on `[n, M+2]` is in `W ∪ W·s(M+1)·W` (if it fixes M+2 it is in W by generation; else `a = swap(j, M+1)`, `b = s(M+1)·a·u` both in W). Generation `mem_closure_of_suppIn` (adjacent transpositions of an interval generate its supported perms) by double induction `gen_aux`: push the preimage of the top point up by one via `u ↦ u * s i`.
- `towerSpan_sym` / `disjointBlock_sym` via the #7079 chain; `disjointBlock_sym_direct` proves the same law WITHOUT the chain from `W_{<n} ∩ W_{≥n} = {1}` (a perm supported on {0..n} ∩ {n..} is supported on {n}, hence 1) — independent cross-check.
- `t_not_mem_shiftedUpTo`: filtration grows (coefficient-at-`s N` functional kills the stage; `t N` has coefficient 1).
- The pair: `a = 1 + t n ∈ H(n+1)`, `b = 1 + t(n+1) ∈ shifted(n+1)`: `tr(ab) = 1 = tr a · tr b` (cross term `t n t(n+1)` is a 3-cycle, coefficient 0) while `tr(a·a) = 2 ≠ 1` (cross term `t n t n = 1`). `pair_law_disjoint_is_instance` shows the hand computation is literally `disjointBlock_sym` applied.

STILL NOT EXERCISED: q = 1, z = 0, h = 0. The double coset is proved in the permutation model by support arguments — the braid relation is never written; a Hecke tower at q ≠ 1 needs the rewriting proof. SandwichReduces for a Hecke tower remains unproved; the bond-product reading of the atom word remains MEASURED, NOT DERIVED. The disjoint-block law holds here for a reason (trace supported at the identity, W_{<n} ∩ W_{≥n} = {1}) a Hecke trace with z ≠ 0 does not have.

Verification env: restored lake-cache/qou-v4-24-0 + hardlinked shadow rebuild of DisjointBlockTraceLaw / TowerSpanReduction (post-seed, #7079) from main source, exit 0 each. Logs /tmp/sandwich-{deps,1,2,axioms}.log.

**ROAST 2026-09-07 (qou-pbwj) — verdict: KILL as a front; allow as a capped (≤1 session) chore.** The model exists in one line and the labour is Mathlib plumbing that reaches nothing: on MonoidAlgebra R (Equiv.Perm (Fin n)) with g_m = (m m+1) = g_m⁻¹, the q = 1 Ocneanu trace tr(w) = z^{n − c(w)} (c = number of cycles) satisfies every field of OcneanuTrace.MarkovTrace — T1 class function, T2 tr(1) = 1, T3/T3' since right-multiplying a ∈ S_n by (n n+1) merges the cycle of n with the fixed point n+1 — and is non-multiplicative (tr(g₁)² = z² ≠ 1 = tr(g₁²)). SandwichReduces for it is the double-coset decomposition S_{m+1} = S_m ⊔ S_m s_m S_m, a two-line fact. So the witness is guaranteed before the session starts, and it exercises exactly what qou-301d predicted: the q = 1 shadow, not the Hecke tower (where the quadratic relation is the content) and not the atom word (DisjointBlockTraceLaw.lean:470-480 — maximal level occurs four times). The bond-product reading stays MEASURED, NOT DERIVED afterwards exactly as before. Arity hazard: a sorry-free S_n witness cited downstream as 'TowerSpan holds for a Hecke-type tower' (shared type, different instance). Worth writing down even so: the S_n class-function trace SATISFIES DisjointBlockMultiplicative, so it is not the counterexample DisjointBlockTraceLaw records as 'NOT ACHIEVED' — a counterexample needs h ≠ 0 or a non-class-function trace. L2 relevance: none. If done: docstring must say 'q = 1 shadow only'. Full frame: docs/audits/2026-09-07-takeover-fronts-roast.md §Front 5.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 75 (`lane-e667`): Formalized `qou-sh62`, `qou-ss88`, `qou-t1kv`, `qou-csgy`, `qou-fq1i` in `QOU.Foundations.CoordinationPeriodSeparationDisjointBlockFactorizationScalarCascadeQuadraticConventionBridgeInvolutionTrace` with 80-dps `mpmath` 2-commit witness stamp (`c9c8117f7aa28b67e2bf3a4e9b287ae17a2e5af6` -> `6d8ea219d4427f09f7950c85f1a067b42a3dd728`, `scriptHash=3a53f4d978a21ce6466ea7c8d24a6d3d41b356bea8717db46a8c42f512a4c41e`) in PR `litlfred/qou#8402` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8402, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
