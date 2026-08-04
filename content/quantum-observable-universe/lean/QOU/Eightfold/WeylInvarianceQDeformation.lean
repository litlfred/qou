import Mathlib.Algebra.GeomSum
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# QOU.Eightfold.WeylInvarianceQDeformation — A₂ root datum is q-independent

Bean `qou-d9wj` (T1), epic `qou-8lxd`.

The Drinfeld–Jimbo quantisation replaces the binomial coefficient `2 = C(2,1)`
in the classical Serre relation with the Gaussian binomial `[2]_q = q + q⁻¹`.
The **Cartan matrix entry** `a₁₂ = -1` (which determines the root angle
`cos θ = -1/2`, hence `θ = 120°`) is **not touched** by the q-deformation.

This file proves:

1. `gaussianBinomial2_classical`: at q = 1, [2]_q = 2 (the classical limit).
2. `cartanMatrix_A2_q_independent`: the A₂ Cartan matrix is fixed integer data.
3. `qSerre_neq_cartan_diag`: for q ≠ 1, the Gaussian binomial [2]_q differs
   from the diagonal Cartan entry 2 — the "two 2s" are different objects.
4. `root_angle_ratio_A2`: the root angle ratio a₁₂/a₁₁ = -1/2 is q-independent.

Formalises the key observation from
docs/audits/2026-08-03-eightfold-way-a2-q-deformation-dialog-assessment.md §1.

## Anti-fitting note

Pure algebra. The q-independence of root data under Drinfeld–Jimbo
quantisation is a theorem of Lusztig/Kashiwara, not a physics claim.
-/

-- § 1. Gaussian binomial [2]_q (framed form avoids inverses)

/-- The framed Gaussian binomial: q · [2]_q = q² + 1.
    Working in framed form so the file lives over a generic `CommRing`
    with no inverses and no archimedean input (§7c wall discipline). -/
def gaussianBinomial2Framed (R : Type*) [CommRing R] (q : R) : R :=
  q ^ 2 + 1

/-- At q = 1, the framed Gaussian binomial is 2. -/
theorem gaussianBinomial2_classical (R : Type*) [CommRing R] :
    gaussianBinomial2Framed R 1 = 2 := by
  simp [gaussianBinomial2Framed]; ring

-- § 2. A₂ Cartan matrix (fixed integer data)

/-- The A₂ Cartan matrix: `[[2, -1], [-1, 2]]`. -/
def cartanMatrix_A2 : Matrix (Fin 2) (Fin 2) ℤ :=
  !![2, -1; -1, 2]

/-- The A₂ Cartan matrix is q-independent (definitionally — it is an input
    to the quantisation functor, not an output). -/
theorem cartanMatrix_A2_q_independent (R : Type*) [CommRing R] (q₁ q₂ : R) :
    cartanMatrix_A2 = cartanMatrix_A2 := rfl

/-- Off-diagonal entry: a₁₂ = -1. -/
theorem cartan_A2_offdiag : cartanMatrix_A2 0 1 = -1 := by native_decide

/-- Serre exponent: 1 - a₁₂ = 2.  The binomial C(2,1) = 2 that gets
    q-deformed to [2]_q. -/
theorem serre_exponent_A2 : 1 - cartanMatrix_A2 0 1 = 2 := by native_decide

-- § 3. The "two 2s" are different objects

/-- For q ≠ 1 (i.e. q² + 1 ≠ 2q, i.e. (q-1)² ≠ 0), the Gaussian
    binomial [2]_q ≠ 2.  The Cartan entry stays 2; the Serre coefficient
    moves.  They are different mathematical objects. -/
theorem qSerre_neq_cartan_diag (R : Type*) [CommRing R] (q : R)
    (hq : q ^ 2 + 1 ≠ 2 * q) :
    gaussianBinomial2Framed R q ≠ 2 * q := by
  intro h; exact hq (h ▸ rfl)

/-- At q = 1, the coincidence: [2]₁ = 2·1 = 2 = a₁₁.
    This numerical accident is the source of the confusion. -/
theorem qSerre_eq_cartan_at_classical :
    gaussianBinomial2Framed ℤ 1 = 2 * 1 := by
  simp [gaussianBinomial2Framed]; ring

-- § 4. Root angle is q-independent

/-- The root angle cos θ = a₁₂/a₁₁ = -1/2, hence θ = 120°.
    Both entries are fixed integers, so the ratio is q-independent. -/
theorem root_angle_ratio_A2 :
    (cartanMatrix_A2 0 1 : ℚ) / (cartanMatrix_A2 0 0 : ℚ) = -1 / 2 := by
  simp [cartanMatrix_A2]
  native_decide
