import QOU.QBeta.BoundedMeromorphicLiouville
import QOU.QBeta.FaddeevPhiUniquenessAssembly

/-!
# A_ω uniqueness leg — the boundedness-route capstone

The growth-bound twin of `FaddeevUniquenessCapstone.faddeevPhi_proportional_of_same_divisor`.
Both discharge the `hr_entire` input of
`FaddeevPhiUniquenessAssembly.faddeevPhi_proportional_of_ratio_entire`, closing the
Faddeev–Volkov uniqueness leg conditional on a **single named, non-axiomatised**
analytic endowment of the concrete `Φ_b`:

| capstone | endowment | brick |
|---|---|---|
| `FaddeevUniquenessCapstone` (#4155) | same divisor (`PhiBProd`) | `RatioEntire.entire_toMeromorphicNFOn_div_of_same_order` |
| **this file** | **state-integral strip boundedness** | `BoundedMeromorphicLiouville.entire_toMeromorphicNFOn_of_bounded` |

The boundedness route is the natural one from the **resurgence / state-integral
vantage**: `Φ_b`'s Écalle–Borel / state-integral representation makes it analytic
with controlled growth in a fundamental strip, so the prefactor-cancelled ratio of
two genuine solutions is **bounded** on `ℂ`; a nonconstant elliptic ℘-factor (the
`FaddeevPhiEllipticFreedom` obstruction) has poles and is **unbounded**, so
boundedness excludes it directly — no divisor matching needed.

`hbdd` is honestly a **hypothesis on the concrete `Φ_b`**, not a class axiom and not
the conclusion: it is a growth bound the total-function class does not encode, and
constancy/proportionality is strictly stronger than boundedness. Verified
`lean`-direct against the Meromorphic cone (exit 0).
-/

open Complex MeromorphicOn
open QOU.MathlibExt.FaddeevQuantumDilogarithm

namespace QOU.QBeta.FaddeevUniquenessBoundedCapstone

/-- **Boundedness-route capstone: bounded ratio ⇒ proportional.** Two `FaddeevPhi`
solutions at `b` (nondegenerate lattice `(b²).im ≠ 0`) whose normal-form ratio
`toMeromorphicNFOn (Φ₁/Φ₂) univ` is **bounded** (the state-integral endowment) are
proportional on `Φ₂`'s nonvanishing locus — provided the normal-form representative
agrees with `Φ₁/Φ₂` there (`hr_ratio`) and the two `FaddeevPhi` periodicity loci are
dense off `Φ₂`'s zeros (`hmem₀/hmem₁`). The `hr_entire` input is discharged
internally by `entire_toMeromorphicNFOn_of_bounded`; the remaining hypotheses are the
same honest, non-axiomatised residual analytic inputs as the divisor-route capstone,
with the same-divisor premise replaced by a strip growth bound. -/
theorem faddeevPhi_proportional_of_bounded_ratio
    {b : ℂ} (hb2 : (b ^ 2).im ≠ 0)
    {Φ₁ Φ₂ : ℂ → ℂ} [FaddeevPhi b Φ₁] [FaddeevPhi b Φ₂]
    {C : ℝ}
    (hbdd : ∀ z, ‖toMeromorphicNFOn (Φ₁ / Φ₂) Set.univ z‖ ≤ C)
    (hr_ratio : ∀ z, Φ₂ z ≠ 0 →
      toMeromorphicNFOn (Φ₁ / Φ₂) Set.univ z = Φ₁ z / Φ₂ z)
    {S₀ S₁ : Set ℂ} (hS₀ : Dense S₀) (hS₁ : Dense S₁)
    (hmem₀ : ∀ z ∈ S₀,
      (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I * b) ≠ 0)
    (hmem₁ : ∀ z ∈ S₁,
      (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I / b) ≠ 0) :
    ∃ c, ∀ z, Φ₂ z ≠ 0 → Φ₁ z = c * Φ₂ z := by
  have hentire := BoundedMeromorphicLiouville.entire_toMeromorphicNFOn_of_bounded hbdd
  exact FaddeevPhiUniquenessAssembly.faddeevPhi_proportional_of_ratio_entire
    hb2 hentire hr_ratio hS₀ hS₁ hmem₀ hmem₁

end QOU.QBeta.FaddeevUniquenessBoundedCapstone
