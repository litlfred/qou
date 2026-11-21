import QOU.QBeta.FaddeevStripGrowthUniqueness
import QOU.QBeta.PhiBProdZeroIsolation

/-!
# `phiBProd` uniqueness up to scalar (G5 specialization, `hΦ₂_iso` discharged)

Specializes `FaddeevStripGrowthUniqueness.faddeevPhi_proportional_of_stripGrowth` to the
physical substrate `Φ_b = phiBProd (substrateB t)`, discharging the zero-isolation input
`hΦ₂_iso` via `PhiBProdZeroIsolation.phiBProd_eventually_ne_zero`.

`phiBProd_uniqueUpToScalar_of_stripGrowth` — any `FaddeevPhi` solution `Φ₁` at the substrate
that is `FaddeevPhiStripGrowth` (comparable in modulus to `phiBProd`), with the normal-form
identity off `phiBProd`'s zeros (`hr_ratio`) and the two dense periodicity loci, is proportional
to `phiBProd`. The strip-growth boundedness (`hbdd`) and the zero-isolation (`hΦ₂_iso`) are now
**both** theorems: the analytic endowment is fully internalized. The two `FaddeevPhi` /
`FaddeevPhiStripGrowth` instances for `phiBProd` itself are supplied
(`faddeevPhi_phiBProd_substrate`, `instPhiBProd`).

Remaining carried inputs (honest, not axiomatized): `hr_ratio` (the meromorphic
normal-form-vs-ratio identity off `phiBProd`'s zeros) and the density of the two periodicity
loci `S₀, S₁` — both gated on the same `phiBProd`-zero discreteness now available here, and
dischargeable by the meromorphic normal-form API + a Baire/codiscrete density argument.

Verified `lean`-direct against the merged G5 assembly + zero-isolation + `PhiBProd`.
Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-26-faddeev-keystone-7xvy-canonical-arc.md
-/

open Complex Filter Topology Set
open QOU.MathlibExt.PhiBProd
open QOU.MathlibExt.FaddeevQuantumDilogarithm

namespace QOU.QBeta.PhiBProdUniquenessFinal

/-- **`phiBProd` uniqueness up to scalar (substrate, `hΦ₂_iso` discharged).** For the physical
substrate `Φ_b = phiBProd (substrateB t)` (`t > 0`): any `FaddeevPhi` solution `Φ₁` that is
`FaddeevPhiStripGrowth` (comparable to `phiBProd`), with the normal-form identity off
`phiBProd`'s zeros and the two dense periodicity loci, is proportional to `phiBProd`. Both the
`hbdd` growth bound and `phiBProd`'s zero isolation are internalized as theorems. -/
theorem phiBProd_uniqueUpToScalar_of_stripGrowth {t : ℝ} (ht : 0 < t) {Φ₁ : ℂ → ℂ}
    [FaddeevPhi (substrateB t) Φ₁] [FaddeevPhiStripGrowth (substrateB t) Φ₁]
    (hr_ratio : ∀ z, phiBProd (substrateB t) z ≠ 0 →
      toMeromorphicNFOn (Φ₁ / phiBProd (substrateB t)) Set.univ z
        = Φ₁ z / phiBProd (substrateB t) z)
    {S₀ S₁ : Set ℂ} (hS₀ : Dense S₀) (hS₁ : Dense S₁)
    (hmem₀ : ∀ z ∈ S₀,
      (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * (substrateB t) ^ 2)
          * Complex.exp (2 * (Real.pi : ℂ) * (substrateB t) * z) ≠ 0
        ∧ phiBProd (substrateB t) z ≠ 0
        ∧ phiBProd (substrateB t) (z + I * (substrateB t)) ≠ 0)
    (hmem₁ : ∀ z ∈ S₁,
      (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * (substrateB t))) / (substrateB t)) ≠ 0
        ∧ phiBProd (substrateB t) z ≠ 0
        ∧ phiBProd (substrateB t) (z + I / (substrateB t)) ≠ 0) :
    ∃ c, ∀ z, phiBProd (substrateB t) z ≠ 0 → Φ₁ z = c * phiBProd (substrateB t) z := by
  haveI : FaddeevPhi (substrateB t) (phiBProd (substrateB t)) :=
    faddeevPhi_phiBProd_substrate ht
  exact FaddeevStripGrowthUniqueness.faddeevPhi_proportional_of_stripGrowth
    (substrateB_sq_im_pos ht).ne' hr_ratio
    (PhiBProdZeroIsolation.phiBProd_eventually_ne_zero _ (substrateB_sq_im_pos ht))
    hS₀ hS₁ hmem₀ hmem₁

end QOU.QBeta.PhiBProdUniquenessFinal
