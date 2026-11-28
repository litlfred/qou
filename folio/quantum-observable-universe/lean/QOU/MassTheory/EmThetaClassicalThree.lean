/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MassTheory.EmThetaGraphSkeinSplit

/-!
# Where the classical `3` of the θ-graph comes from (bean `qou-l4t2`)

`EmThetaGraphSkeinSplit` shows `[3]_q = 3 + h² = 3 − V`, where `V` is the
**signed** (bar-Hermitian, weight `−ε₁ε₂`) chirality-summed vertex pair. The
constant `3` is not produced by any skein chain. This module finds what does
produce it: the **unsigned** sum over the same four chiral histories.

At one generator `σ` (convention D, `σ² = hσ + 1`):

1. `sum_eq_two_sigma_sub`: `σ + σ⁻¹ = 2σ − h`.
2. `unsignedPair_eq_two_sq`: the unsigned four-history sum
   `Σ_{ε₁,ε₂} σ^{ε₁} σ^{ε₂} = (σ + σ⁻¹)²` equals the scalar `4 + h²`. With
   `q q⁻¹ = 1` this is `[2]_q²` (`unsignedPair_eq_qInt2_sq`).
3. `qInt3_eq_unsignedPair_sub_one`: `[3]_q = (unsigned pair) − 1`. This is the
   Clebsch–Gordan split `[2]² = [3] + [1]`: the spin-1 (photon) channel is all four
   histories with the singlet removed.

Reading (prose, not a theorem). At `q = 1` the unsigned pair is `4`, the number of
chiral histories. The θ-graph's classical `3 = 4 − 1` is that count minus the
singlet. The signed bar-Hermitian weights `−ε₁ε₂`, which Form B uses, cancel the
count and keep only `−h²`. So the two readings differ by which weights the
two-vertex photon insertion carries: unsigned and projected to spin 1 (θ-graph),
or signed (Form B). That choice is not made here. Unlike the signed pair, the
unsigned pair is a scalar only at one position: at two different generators
`(2σ − h)(2τ − h)` is not central in general. No measured value enters this file.
-/

set_option autoImplicit false

namespace QOU.MassTheory
namespace EmThetaClassicalThree

open EmVertexPairScalarChain EmThetaGraphSkeinSplit

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- `σ + σ⁻¹ = 2σ − h`. -/
theorem sum_eq_two_sigma_sub {h : R} (g : HeckeGen (A := A) h) :
    g.σ + g.σinv = 2 * g.σ - algebraMap R A h := by
  have hs := skein_scalar g
  have : g.σinv = g.σ - algebraMap R A h := by rw [← hs]; abel
  rw [this, two_mul]; abel

/-- The unsigned sum over the four chiral two-vertex histories at one position. -/
def unsignedPair {h : R} (g : HeckeGen (A := A) h) : A :=
  g.σ * g.σ + g.σ * g.σinv + g.σinv * g.σ + g.σinv * g.σinv

/-- The unsigned pair is the scalar `4 + h²`. -/
theorem unsignedPair_eq_two_sq {h : R} (g : HeckeGen (A := A) h) :
    unsignedPair g = algebraMap R A (4 + h ^ 2) := by
  have e : unsignedPair g = (g.σ + g.σinv) * (g.σ + g.σinv) := by
    unfold unsignedPair; noncomm_ring
  have hc : Commute (algebraMap R A h) g.σ := Algebra.commutes h g.σ
  rw [e, sum_eq_two_sigma_sub]
  have hq := g.quad
  rw [pow_two] at hq
  calc (2 * g.σ - algebraMap R A h) * (2 * g.σ - algebraMap R A h)
      = 4 * (g.σ * g.σ) - 2 * (algebraMap R A h * g.σ) - 2 * (g.σ * algebraMap R A h)
          + algebraMap R A h * algebraMap R A h := by noncomm_ring
    _ = 4 * (algebraMap R A h * g.σ + 1) - 2 * (algebraMap R A h * g.σ)
          - 2 * (algebraMap R A h * g.σ) + algebraMap R A h * algebraMap R A h := by
        rw [hq, ← hc.eq]
    _ = algebraMap R A (4 + h ^ 2) := by
        rw [map_add, map_pow, map_ofNat, pow_two]; noncomm_ring; simp [add_comm]

/-- With `q q⁻¹ = 1` and `h = q − q⁻¹`, the unsigned pair is `[2]_q²`. -/
theorem unsignedPair_eq_qInt2_sq {q qi h : R} (hq : q * qi = 1) (hh : h = q - qi)
    (g : HeckeGen (A := A) h) :
    unsignedPair g = algebraMap R A ((q + qi) ^ 2) := by
  rw [unsignedPair_eq_two_sq, hh]; congr 1; linear_combination (-4) * hq

/-- **Clebsch–Gordan.** `[3]_q = (unsigned pair) − 1`. -/
theorem qInt3_eq_unsignedPair_sub_one {q qi h : R} (hq : q * qi = 1) (hh : h = q - qi)
    (g : HeckeGen (A := A) h) :
    algebraMap R A (qInt3 q qi) = unsignedPair g - 1 := by
  rw [unsignedPair_eq_two_sq, ← map_one (algebraMap R A), ← map_sub]
  congr 1
  rw [qInt3_eq_three_add_hsq q qi hq, hh]; ring

end EmThetaClassicalThree
end QOU.MassTheory
