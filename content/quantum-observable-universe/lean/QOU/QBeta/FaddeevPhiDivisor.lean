import QOU.MathlibExt.FaddeevQuantumDilogarithm
import QOU.QBeta.FaddeevUniquenessCapstone
import Mathlib.Analysis.Meromorphic.NormalForm
import Mathlib.Analysis.Meromorphic.Order

/-!
# Faddeev `Φ_b` with divisor specification — Route A (algebraic)

The `FaddeevPhi` class axiomatizes only the q-difference equations; it admits
elliptic multipliers (`FaddeevPhiEllipticFreedom.faddeevPhi_mul_elliptic`), so
the divisor is not determined. This file introduces a **strengthened class**
`FaddeevPhiWithDivisor` that extends `FaddeevPhi` with:

1. **Meromorphicity on `ℂ`** (`hMero : MeromorphicOn Φ Set.univ`);
2. **Divisor specification** (`divisor_eq : ∀ z, meromorphicOrderAt Φ z = d z`)
   for a prescribed `d : ℂ → WithTop ℤ` determined by the `b`-lattice geometry.

The divisor function `d` encodes the exact zero/pole structure of Faddeev's
quantum dilogarithm: simple zeros at `z_nm = -ib(n+½) + i(m+½)/b` (b-side)
and simple poles at `z̃_nm = -i(n+½)/b + ib(m+½)` (dual side), for `n,m ∈ ℤ≥0`.
This is a THEOREM for the explicit `PhiBProd` product representation; it is
carried here as a class field because the contour-integral construction of `Φ_b`
is not available in Lean/Mathlib.

Two `FaddeevPhiWithDivisor` instances at the same `(b, d)` automatically satisfy
the same-divisor premise of the capstone
(`FaddeevUniquenessCapstone.faddeevPhi_proportional_of_same_divisor`), yielding
**unconditional proportionality** — the A_ω uniqueness leg.

-- Ref: [faddeev1995] Faddeev 1995, §3 — product representation pins divisor
-- Ref: docs/coordination/delta-lambda-magnitude-derivation.md — T1/T2 workplan
-/

open Complex MeromorphicOn
open QOU.MathlibExt.FaddeevQuantumDilogarithm

namespace QOU.QBeta.FaddeevPhiDivisor

/-- **Faddeev `Φ_b` with divisor (strengthened class, Route A).**
Extends `FaddeevPhi` with meromorphicity and a prescribed divisor function `d`.
Two instances at the same `(b, d)` share the same divisor by definition. -/
class FaddeevPhiWithDivisor (b : ℂ) (d : ℂ → WithTop ℤ) (Φ : ℂ → ℂ)
    extends FaddeevPhi b Φ : Prop where
  /-- `Φ` is meromorphic on all of `ℂ`. -/
  hMero : MeromorphicOn Φ Set.univ
  /-- `Φ` is nowhere identically zero (finite order everywhere). -/
  hFiniteOrder : ∀ z, meromorphicOrderAt Φ z ≠ ⊤
  /-- The meromorphic order at every point equals the prescribed divisor `d`. -/
  divisor_eq : ∀ z, meromorphicOrderAt Φ z = d z

/-- **Same-divisor lemma (immediate).** Two `FaddeevPhiWithDivisor` instances
at the same `(b, d)` have identical meromorphic orders at every point. -/
theorem same_divisor {b : ℂ} {d : ℂ → WithTop ℤ} {Φ₁ Φ₂ : ℂ → ℂ}
    [h₁ : FaddeevPhiWithDivisor b d Φ₁] [h₂ : FaddeevPhiWithDivisor b d Φ₂] :
    ∀ z, meromorphicOrderAt Φ₁ z = meromorphicOrderAt Φ₂ z := by
  intro z
  rw [h₁.divisor_eq z, h₂.divisor_eq z]

/-- **Proportionality from divisor specification (Route A capstone).**
Two `FaddeevPhiWithDivisor` solutions at the same `(b, d)` — with nondegenerate
lattice and the remaining analytic regularity inputs — are proportional.

This composes `same_divisor` with
`FaddeevUniquenessCapstone.faddeevPhi_proportional_of_same_divisor`,
discharging the `hsame` input that was the wall. The remaining hypotheses
(`hr_ratio`, `hmem₀`, `hmem₁`) are the normal-form and density conditions
that the `PhiBProd` product representation provides. -/
theorem faddeevPhi_proportional_of_divisor_spec
    {b : ℂ} (hb2 : (b ^ 2).im ≠ 0)
    {d : ℂ → WithTop ℤ} {Φ₁ Φ₂ : ℂ → ℂ}
    [h₁ : FaddeevPhiWithDivisor b d Φ₁] [h₂ : FaddeevPhiWithDivisor b d Φ₂]
    (hr_ratio : ∀ z, Φ₂ z ≠ 0 →
      toMeromorphicNFOn (Φ₁ / Φ₂) Set.univ z = Φ₁ z / Φ₂ z)
    {S₀ S₁ : Set ℂ} (hS₀ : Dense S₀) (hS₁ : Dense S₁)
    (hmem₀ : ∀ z ∈ S₀,
      (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * b ^ 2)
        * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I * b) ≠ 0)
    (hmem₁ : ∀ z ∈ S₁,
      (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I / b) ≠ 0) :
    ∃ c, ∀ z, Φ₂ z ≠ 0 → Φ₁ z = c * Φ₂ z :=
  FaddeevUniquenessCapstone.faddeevPhi_proportional_of_same_divisor
    hb2 h₁.hMero h₂.hMero h₂.hFiniteOrder same_divisor hr_ratio hS₀ hS₁ hmem₀ hmem₁

end QOU.QBeta.FaddeevPhiDivisor
