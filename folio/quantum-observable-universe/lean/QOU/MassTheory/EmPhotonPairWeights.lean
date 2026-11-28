/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MassTheory.EmThetaClassicalThree

/-!
# Vertex-pair weights: mixed vs same chirality (bean `qou-l4t2`)

At one convention-D generator `σ` (`σ² = hσ + 1`) split the four chiral two-vertex
histories into the two **mixed-chirality** ones (`σσ⁻¹`, `σ⁻¹σ`) and the two
**same-chirality** ones (`σ²`, `σ⁻²`):

1. `mixedPair_eq`: `M = σσ⁻¹ + σ⁻¹σ = 2`.
2. `samePair_eq`: `S = σ² + σ⁻² = 2 + h²`.
3. `weightedPair_eq`: with weight `a` on the mixed histories and `b` on the
   same-chirality ones, `aM + bS = (2a + 2b) + b h²`.
4. `weightedPair_classical_zero_iff`: the classical part `2a + 2b` vanishes iff
   `a = −b`; in a ring without 2-torsion these are exactly the multiples of Form B's
   signed weights (`fourTopology = M − S = −h²`, `signed_eq_mixed_sub_same`).
5. `photonTerm_weights_classical`: the weights the ruled photon form shows on its
   own two-crossing term `σ₀σ₁⁻¹` (mixed `1`, same-chirality `0`; the `σ₀σ₁` form is
   ruled out) give the constant `2` and no `h²`.

Reading (prose, not a theorem). The three weightings in play are Form B
`(a, b) = (1, −1)`, value `−h²`; the θ-graph `(1, 1)` less the singlet, value
`3 + h²`; and the photon form's own two-crossing term `(1, 0)`, value `2`. The ruled
photon form fixes the weights of its **own** degree-two term, and those match
neither reading. It does not by itself say what weights a pair of **separate**
photon vertices on one fermion loop carries; that needs a propagator rule the corpus
does not yet state. No measured value enters this file.
-/

set_option autoImplicit false

namespace QOU.MassTheory
namespace EmPhotonPairWeights

open EmVertexPairScalarChain

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Mixed-chirality histories at one position. -/
def mixedPair {h : R} (g : HeckeGen (A := A) h) : A :=
  g.σ * g.σinv + g.σinv * g.σ

/-- Same-chirality histories at one position. -/
def samePair {h : R} (g : HeckeGen (A := A) h) : A :=
  g.σ * g.σ + g.σinv * g.σinv

theorem mixedPair_eq {h : R} (g : HeckeGen (A := A) h) : mixedPair g = 2 := by
  unfold mixedPair; rw [g.mul_inv, g.inv_mul]; norm_num

theorem samePair_eq {h : R} (g : HeckeGen (A := A) h) :
    samePair g = algebraMap R A (2 + h ^ 2) := by
  have hu := EmThetaClassicalThree.unsignedPair_eq_two_sq g
  have e : EmThetaClassicalThree.unsignedPair g = mixedPair g + samePair g := by
    unfold EmThetaClassicalThree.unsignedPair mixedPair samePair; abel
  rw [e, mixedPair_eq] at hu
  have : samePair g = algebraMap R A (4 + h ^ 2) - 2 := by rw [← hu]; abel
  rw [this, show (4 : R) + h ^ 2 = (2 + h ^ 2) + 2 by ring, map_add, map_ofNat]; abel

/-- Form B's signed sum is mixed minus same. -/
theorem signed_eq_mixed_sub_same {h : R} (g : HeckeGen (A := A) h) :
    vertexPair g g = mixedPair g - samePair g := by
  unfold vertexPair fourTopology mixedPair samePair; abel

/-- Weighted pair: weight `a` on mixed, `b` on same-chirality histories. -/
theorem weightedPair_eq {h : R} (g : HeckeGen (A := A) h) (a b : R) :
    a • mixedPair g + b • samePair g = algebraMap R A ((2 * a + 2 * b) + b * h ^ 2) := by
  rw [mixedPair_eq, samePair_eq, Algebra.algebraMap_eq_smul_one,
    Algebra.algebraMap_eq_smul_one]
  rw [show (2 : A) = (2 : R) • (1 : A) by rw [two_smul, one_add_one_eq_two]]
  rw [smul_smul, smul_smul, ← add_smul]; congr 1; ring

/-- The classical (`h = 0`) part `2a + 2b` vanishes iff `a = −b`, when `2` is
not a zero divisor. -/
theorem weightedPair_classical_zero_iff [IsDomain R] [CharZero R] (a b : R) :
    2 * a + 2 * b = 0 ↔ a = -b := by
  constructor
  · intro h
    have : (2 : R) * (a + b) = 0 := by linear_combination h
    rcases mul_eq_zero.mp this with h2 | h2
    · exact absurd h2 two_ne_zero
    · linear_combination h2
  · intro h; rw [h]; ring

/-- The photon form's own two-crossing weights (mixed `1`, same `0`) give `2`. -/
theorem photonTerm_weights_classical {h : R} (g : HeckeGen (A := A) h) :
    (1 : R) • mixedPair g + (0 : R) • samePair g = 2 := by
  rw [one_smul, zero_smul, add_zero, mixedPair_eq]

end EmPhotonPairWeights
end QOU.MassTheory
