import QOU.QBeta.PhiBProdUniquenessFinal
import QOU.QBeta.PhiBProdHrRatio

/-!
# `phiBProd` uniqueness — `hr_ratio` and `hΦ₂_iso` both discharged (G5 near-final)

Combines the two discharges — zero-isolation (`PhiBProdZeroIsolation`, merged) and the
normal-form identity (`PhiBProdHrRatio`) — into a `phiBProd` uniqueness statement whose only
remaining inputs are the honest regularity hypothesis `MeromorphicNFOn Φ₁` (the physical second
solution is in normal form) and the density of the two periodicity loci.

`phiBProd_uniqueUpToScalar` — any substrate `FaddeevPhi` + `FaddeevPhiStripGrowth` solution `Φ₁`
in meromorphic normal form, with the two dense periodicity loci, is proportional to `phiBProd`.
Everything analytic is now a theorem: input 1 (`MeromorphicOn phiBProd`), the elliptic-freedom
exclusions, the strip-growth `hbdd`, the zero-isolation `hΦ₂_iso`, and the normal-form identity
`hr_ratio`. The sole non-structural input left is `Dense S₀`, `Dense S₁` for the periodicity
loci (mechanically gated on `phiBProd`'s now-established zero discreteness).

Verified `lean`-direct against the merged G5 chain + `PhiBProdHrRatio`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-26-faddeev-keystone-7xvy-canonical-arc.md
-/

open Complex Filter Topology Set
open QOU.MathlibExt.PhiBProd
open QOU.MathlibExt.FaddeevQuantumDilogarithm

namespace QOU.QBeta.PhiBProdUniquenessComplete

/-- **`phiBProd` uniqueness up to scalar (substrate; `hr_ratio` + `hΦ₂_iso` discharged).**
Any `FaddeevPhi` solution `Φ₁` at the substrate that is `FaddeevPhiStripGrowth` (comparable to
`phiBProd`) and in meromorphic normal form, with the two dense periodicity loci, is proportional
to `phiBProd`. The strip-growth `hbdd`, the zero-isolation, and the normal-form identity are all
internalized as theorems; only the loci-density hypotheses remain. -/
theorem phiBProd_uniqueUpToScalar {t : ℝ} (ht : 0 < t) {Φ₁ : ℂ → ℂ}
    [FaddeevPhi (substrateB t) Φ₁] [FaddeevPhiStripGrowth (substrateB t) Φ₁]
    (hΦ₁NF : MeromorphicNFOn Φ₁ Set.univ)
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
    ∃ c, ∀ z, phiBProd (substrateB t) z ≠ 0 → Φ₁ z = c * phiBProd (substrateB t) z :=
  PhiBProdUniquenessFinal.phiBProd_uniqueUpToScalar_of_stripGrowth ht
    (fun z hz => PhiBProdHrRatio.hr_ratio_phiBProd (substrateB t) z (substrateB_sq_im_pos ht)
      hΦ₁NF hz)
    hS₀ hS₁ hmem₀ hmem₁

end QOU.QBeta.PhiBProdUniquenessComplete
