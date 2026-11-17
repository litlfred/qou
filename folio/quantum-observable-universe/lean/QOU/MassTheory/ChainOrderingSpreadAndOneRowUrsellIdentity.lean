/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# Chain Ordering Spread (`qou-h7mh`) and One-Row Dominant Summand Ursell Identity (`qou-m8f3`)

This module formalizes the algebraic identities of beans `qou-h7mh` and `qou-m8f3`:

1. **`qou-h7mh` (1-D chain ordering spread vs complete-graph pair invariance):**
   - On a 1-D nucleon chain, the bond multiset depends on the nucleon ordering: for `A = 3`,
     contiguous orderings `ppn` (`³He`) and `pnn` (`³H`) have mirror difference
     `(L_pn + L_nn) - (L_pp + L_pn) = L_nn - L_pp`, whereas alternating orderings `pnp` and `npn`
     both have two `p-n` bonds (`2 L_pn`) and mirror difference `0`.
   - On the complete graph `K_A`, the doubled pair counts `Z(Z - 1) + 2 Z N + N(N - 1)` depend
     only on `(Z, N)` and sum to `(Z + N)(Z + N - 1) = A(A - 1)` for every ordering.

2. **`qou-m8f3` (One-row dominant block `[3A]` chain additivity and missing-edge Ursell identity):**
   - Because the one-row character `χ^{[3A]}` is multiplicative over braid letters, its log-weight
     `L_chain(123) = b₁₂ + b₂₃` is strictly additive along the `(1,2)` and `(2,3)` chain edges.
   - Applying the complete-graph 3-body Ursell inversion `b₃ = L(123) - (b₁₂ + b₂₃ + b₁₃)` to
     `L_chain(123)` yields `b₃ = -b₁₃` (the negative of the missing `(1,3)` edge).
   - For both `ppn` (`³He`) and `pnn` (`³H`), the missing `(1,3)` endpoint pair is a `p-n` pair,
     so `b₃(ppn) = b₃(pnn) = -b₂(pn)` identically (`b₃ / b₂(pn) = -1`).
-/

namespace QOU.MassTheory.ChainOrderingSpreadAndOneRowUrsellIdentity

/-- 1-D chain bond sum for contiguous `ppn` (`³He`): one `pp` bond and one `pn` bond (`qou-h7mh`). -/
def chainSumContiguous3He (L_pp L_pn : Int) : Int :=
  L_pp + L_pn

/-- 1-D chain bond sum for contiguous `pnn` (`³H`): one `pn` bond and one `nn` bond (`qou-h7mh`). -/
def chainSumContiguous3H (L_pn L_nn : Int) : Int :=
  L_pn + L_nn

/-- 1-D chain bond sum for alternating `pnp` (`³He`) or `npn` (`³H`): two `pn` bonds (`qou-h7mh`). -/
def chainSumAlternatingA3 (L_pn : Int) : Int :=
  2 * L_pn

/-- The `A = 3` mirror difference equals `L_nn - L_pp` under contiguous ordering (`ppn`/`pnn`) but
collapses to `0` under alternating ordering (`pnp`/`npn`) (`qou-h7mh`). -/
theorem chainMirrorSplit_contiguous_vs_alternating (L_pp L_pn L_nn : Int) :
    chainSumContiguous3H L_pn L_nn - chainSumContiguous3He L_pp L_pn = L_nn - L_pp ∧
    chainSumAlternatingA3 L_pn - chainSumAlternatingA3 L_pn = 0 := by
  dsimp [chainSumContiguous3H, chainSumContiguous3He, chainSumAlternatingA3]
  constructor <;> omega

/-- Doubled pair counts `Z(Z - 1) + 2 Z N + N(N - 1)` on the complete graph `K_{Z+N}` (`qou-h7mh`). -/
def completeGraphTypedPairsDoubled (Z N : Int) : Int :=
  Z * (Z - 1) + 2 * (Z * N) + N * (N - 1)

/-- The typed complete-graph pair counts sum identically to `(Z + N)(Z + N - 1)` (`qou-h7mh`). -/
theorem completeGraphTypedPairsDoubled_eq_total (Z N : Int) :
    completeGraphTypedPairsDoubled Z N = (Z + N) * (Z + N - 1) := by
  unfold completeGraphTypedPairsDoubled
  have hz : Z * (Z - 1) = Z * Z - Z := by rw [Int.mul_sub, Int.mul_one]
  have hn : N * (N - 1) = N * N - N := by rw [Int.mul_sub, Int.mul_one]
  have htot : (Z + N) * (Z + N - 1) = (Z + N) * (Z + N) - (Z + N) := by
    rw [Int.mul_sub, Int.mul_one]
  have hsq : (Z + N) * (Z + N) = Z * Z + 2 * (Z * N) + N * N := by
    have ha : (Z + N) * (Z + N) = Z * (Z + N) + N * (Z + N) := Int.add_mul Z N (Z + N)
    have hb1 : Z * (Z + N) = Z * Z + Z * N := Int.mul_add Z Z N
    have hb2 : N * (Z + N) = Z * N + N * N := by rw [Int.mul_add, Int.mul_comm N Z]
    omega
  omega

/-- Chain-additive 3-body log-weight `b₁₂ + b₂₃` on the one-row block `[3A]` (`qou-m8f3`). -/
def oneRowChainLogWeight3 (b12 b23 : Int) : Int :=
  b12 + b23

/-- Complete-graph 3-body Ursell inversion `L₁₂₃ - (b₁₂ + b₂₃ + b₁₃)` (`qou-m8f3`). -/
def completeGraphUrsellB3 (L123 b12 b23 b13 : Int) : Int :=
  L123 - (b12 + b23 + b13)

/-- On a chain-additive observable, complete-graph Ursell inversion yields `-b₁₃` (the negative of
the missing `(1,3)` edge) (`qou-m8f3`). -/
theorem oneRowChainUrsellB3_eq_neg_missing_edge (b12 b23 b13 : Int) :
    completeGraphUrsellB3 (oneRowChainLogWeight3 b12 b23) b12 b23 b13 = -b13 := by
  dsimp [completeGraphUrsellB3, oneRowChainLogWeight3]
  omega

/-- For both `ppn` (`³He`) and `pnn` (`³H`), the missing `(1,3)` endpoint pair is `p-n`, so
`b₃(ppn) = b₃(pnn) = -b_pn` identically (`qou-m8f3`). -/
theorem oneRowChainUrsellB3_ppn_and_pnn_eq_neg_pn (b_pp b_pn b_nn : Int) :
    completeGraphUrsellB3 (oneRowChainLogWeight3 b_pp b_pn) b_pp b_pn b_pn = -b_pn ∧
    completeGraphUrsellB3 (oneRowChainLogWeight3 b_pn b_nn) b_pn b_nn b_pn = -b_pn := by
  constructor
  · exact oneRowChainUrsellB3_eq_neg_missing_edge b_pp b_pn b_pn
  · exact oneRowChainUrsellB3_eq_neg_missing_edge b_pn b_nn b_pn

end QOU.MassTheory.ChainOrderingSpreadAndOneRowUrsellIdentity
