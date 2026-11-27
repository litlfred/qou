/-
# Mass comparison: where the norm and the logarithm live

Bean `qou-5o1v` (constructive item 2.1). Owner ruling 2026-11-27: *mass is valued in the ring*;
norm and logarithm are applied only at the comparison with measured data.

The model quantities are ring elements:

* the mass of a braid class, `massClass c ∈ R` (`def:mass-identity`;
  `BraidKnotOctonion/MassClassRingHom.lean` proves it natural in `R`);
* the binding factor `b = tr_M(β) ∈ R` of a bound composite, which is multiplicative over
  disjoint pieces because the Markov trace is.

A comparison is a ring homomorphism `φ : R →+* ℝ` (for `R = ℚ(q)`, evaluation at a point where no
denominator vanishes) followed by one of two maps that need the order on `ℝ`:

* `comparedMass φ m = |φ m|`;
* `comparedBinding α φ b = −α · log |φ b|`, the 2026-09-04 working form of the binding law
  (bean `qou-2pnv`).

This file proves the algebraic facts that make these the only places the norm and the logarithm
are needed:

* `comparedMass_mul`, `comparedMass_scale` — the absolute value is multiplicative, so the scaling
  law of `prop:mass-identity-unique` (`m₁ = c · m₂` in `R`) becomes `|φ m₁| = |φ c| · |φ m₂|`
  only at comparison.
* `comparedBinding_mul` — the logarithm turns the ring's multiplication into addition. A product
  of binding factors in `R` compares to a sum of binding energies. Additivity of binding energy is
  a property of the comparison map, not an extra postulate on the model.
* `comparedBinding_one` — the unbound factor `b = 1` compares to zero binding.
* `comparedMass_neg` — the sign of the ring element is lost only at comparison.

No numerical value of `q`, of `α` or of any measured constant enters.
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.Transcendental.MassTheory.MassComparison

variable {R : Type*} [CommRing R] (φ : R →+* ℝ)

/-- **Compared mass.** Evaluate the ring-valued mass, then take the absolute value. -/
noncomputable def comparedMass (m : R) : ℝ := |φ m|

/-- **Compared binding.** Evaluate the ring-valued binding factor, then take `−α log |·|`. -/
noncomputable def comparedBinding (α : ℝ) (b : R) : ℝ := -α * Real.log |φ b|

theorem comparedMass_nonneg (m : R) : 0 ≤ comparedMass φ m := abs_nonneg _

/-- The absolute value is multiplicative. -/
theorem comparedMass_mul (a b : R) :
    comparedMass φ (a * b) = comparedMass φ a * comparedMass φ b := by
  simp [comparedMass, abs_mul]

/-- **Scaling law at comparison.** If `m₁ = c · m₂` in the ring (rescaling the Frobenius form by
`c`), the compared masses satisfy `|φ m₁| = |φ c| · |φ m₂|`. -/
theorem comparedMass_scale (c m₁ m₂ : R) (h : m₁ = c * m₂) :
    comparedMass φ m₁ = |φ c| * comparedMass φ m₂ := by
  rw [h, comparedMass_mul]
  rfl

/-- A ring element and its negative compare equal: the sign is dropped only here. -/
theorem comparedMass_neg (m : R) : comparedMass φ (-m) = comparedMass φ m := by
  simp [comparedMass]

/-- **The logarithm turns the ring product into a sum.** For binding factors whose images do not
vanish, `B(b₁ b₂) = B(b₁) + B(b₂)`. -/
theorem comparedBinding_mul (α : ℝ) (b₁ b₂ : R) (h₁ : φ b₁ ≠ 0) (h₂ : φ b₂ ≠ 0) :
    comparedBinding φ α (b₁ * b₂) = comparedBinding φ α b₁ + comparedBinding φ α b₂ := by
  unfold comparedBinding
  rw [map_mul, abs_mul, Real.log_mul (abs_ne_zero.mpr h₁) (abs_ne_zero.mpr h₂)]
  ring

/-- The unbound factor compares to zero binding. -/
theorem comparedBinding_one (α : ℝ) : comparedBinding φ α (1 : R) = 0 := by
  simp [comparedBinding]

/-- The compared binding of a power is the power times the compared binding. -/
theorem comparedBinding_pow (α : ℝ) (b : R) (n : ℕ) :
    comparedBinding φ α (b ^ n) = n * comparedBinding φ α b := by
  unfold comparedBinding
  rw [map_pow, abs_pow, Real.log_pow]
  ring

end QOU.Transcendental.MassTheory.MassComparison
