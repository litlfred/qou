/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MassTheory.EmVertexPairScalarChain

/-!
# The two-loop θ-graph splits as `3 + (one vertex pair)` (bean `qou-l4t2`)

The corpus's two-loop candidate (audit 2026-07-14, θ-graph) evaluates the unique
1PI two-loop vacuum graph as `θ(1,1,2) = [3]_q = q² + 1 + q⁻²`. Form B instead
carries the skein-chain term `-N₁ h² H` with `h = q - q⁻¹`
(`EmVertexPairScalarChain.skeinChain_two_loop_coeff`). This module relates them.

1. `qInt3_eq_three_add_hsq`: `[3]_q = 3 + h²` in any commutative ring with
   `q q⁻¹ = 1`.
2. `qInt3_eq_three_sub_vertexPair`: in any `R`-algebra, `[3]_q = 3 - V` where `V`
   is the chirality-summed vertex pair at any two convention-D generators. So the
   θ-graph value is a classical constant `3` plus exactly **one** vertex pair
   (`N₁ = 1`).
3. `theta_two_loop_split`: `-[3]_q x² = -3 x² + (-h²) x²`.
4. `qInt3_not_skein_multiple`: no integer multiple of `h²` equals `[3]_q` as a
   function of `q`. Every skein-chain coefficient `(-h²)^k`, `k ≥ 1`, vanishes at
   `q = 1`, while `[3]_1 = 3`. The classical part of the θ-graph is therefore not
   produced by any skein chain.

Reading (prose, not a theorem): the θ-graph and Form B agree on the placement
count, `N₁ = 1`. They differ in two other places: the θ-graph has the classical
constant `3`, and it carries the measure `x² = (α/(8π))²` where Form B carries
`H α² = [2]_q α²/(8π)`. No measured value and no transcendental constant enter
this file.
-/

set_option autoImplicit false

namespace QOU.MassTheory
namespace EmThetaGraphSkeinSplit

open EmVertexPairScalarChain

section Ring

variable {R : Type*} [CommRing R]

/-- `[3]_q = q² + 1 + q⁻²`, with `q⁻¹` passed as `qi`. -/
def qInt3 (q qi : R) : R := q ^ 2 + 1 + qi ^ 2

/-- `[3]_q = 3 + h²`, `h = q - q⁻¹`. -/
theorem qInt3_eq_three_add_hsq (q qi : R) (hq : q * qi = 1) :
    qInt3 q qi = 3 + (q - qi) ^ 2 := by
  unfold qInt3; linear_combination 2 * hq

/-- The θ-graph two-loop term splits into a classical part and one skein unit. -/
theorem theta_two_loop_split (q qi x : R) (hq : q * qi = 1) :
    -(qInt3 q qi) * x ^ 2 = -3 * x ^ 2 + (-(q - qi) ^ 2) * x ^ 2 := by
  rw [qInt3_eq_three_add_hsq q qi hq]; ring

end Ring

/-- In any algebra over `R`, `[3]_q = 3 - V` for the chirality-summed vertex pair
`V` at any two convention-D generators with skein parameter `h = q - q⁻¹`. -/
theorem qInt3_eq_three_sub_vertexPair {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    {q qi h : R} (hq : q * qi = 1) (hh : h = q - qi)
    (g g' : HeckeGen (A := A) h) :
    algebraMap R A (qInt3 q qi) = 3 - vertexPair g g' := by
  rw [vertexPair_eq_neg_hsq, qInt3_eq_three_add_hsq q qi hq, hh]
  simp [map_add, map_neg, map_pow, map_ofNat]

/-- **Exclusion.** No integer `N` makes `N h² = [3]_q` for every invertible `q`:
at `q = 1` the left side is `0` and the right side is `3`. -/
theorem qInt3_not_skein_multiple :
    ¬ ∃ N : ℤ, ∀ q qi : ℤ, q * qi = 1 → N * (q - qi) ^ 2 = qInt3 q qi := by
  rintro ⟨N, hN⟩
  have h := hN 1 1 (by norm_num)
  norm_num [qInt3] at h

end EmThetaGraphSkeinSplit
end QOU.MassTheory
