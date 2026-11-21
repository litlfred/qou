import QOU.QBeta.FaddeevUniquenessBoundedCapstone
import QOU.QBeta.FaddeevPhiStripGrowth
import QOU.QBeta.MeromorphicPuncturedBounded

/-!
# Strip-growth ⇒ proportionality: the G5 assembly

Brick **G5** of the Faddeev growth-estimate epic (`qou-mz4f`). It removes the analytic
`hbdd` input of `FaddeevUniquenessBoundedCapstone.faddeevPhi_proportional_of_bounded_ratio`,
**deriving** it from the strip-growth class (G4) via the removable-singularity extension
(G5 crux, `MeromorphicPuncturedBounded`).

`faddeevPhi_proportional_of_stripGrowth` — two `FaddeevPhi` solutions that are both
`FaddeevPhiStripGrowth` (comparable to `phiBProd`), with `Φ₂`'s zeros isolated
(`hΦ₂_iso`) and the normal-form identity off `Φ₂`'s zeros (`hr_ratio`), and the two dense
periodicity loci, are proportional. The `hbdd` bound the capstone needed is now a theorem:
`ratio_bounded_of_stripGrowth` (G4) bounds the raw ratio on `{Φ₂ ≠ 0}`; `Φ₂`'s zeros being
isolated makes that a *punctured-neighborhood* bound at every point; and
`norm_le_of_bounded_on_punctured` (G5 crux) promotes it to the global bound.

So the boundedness capstone's three analytic inputs (`hbdd`, `hr_ratio`, loci) reduce to two
(`hr_ratio`, loci) plus the structural strip-growth class — `hbdd` is derived, no longer an
endowment. What remains to fully close `qou-7xvy` for the concrete `phiBProd` (assembly, no
Mathlib gap): discharge `hΦ₂_iso` from `meromorphicOrderAt (phiBProd b) ≠ ⊤` (PR #4225), and
`hr_ratio` from the meromorphic normal-form identity on the analytic locus.

Verified `lean`-direct against the pinned Mathlib `Meromorphic` cone + the merged G4/G5-crux +
`PhiBProd`. Sorry-free.

-- Ref: [leitner2026] docs/workplans/2026-07-26-faddeev-growth-estimate-epic-scope.md
-/

open Complex Filter Topology
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.QBeta.MeromorphicPuncturedBounded

namespace QOU.QBeta.FaddeevStripGrowthUniqueness

/-- **Strip-growth ⇒ proportionality (G5).** For two `FaddeevPhi` solutions at `b`
(nondegenerate lattice `(b²).im ≠ 0`) that are both `FaddeevPhiStripGrowth` — i.e. comparable
in modulus to `phiBProd b` — with `Φ₂`'s zeros isolated and the normal-form-vs-ratio identity
holding off `Φ₂`'s zeros, and the two dense periodicity loci: the solutions are proportional
on `Φ₂`'s nonvanishing locus. The analytic `hbdd` input of the boundedness capstone is
**derived** here from the strip-growth class, not assumed. -/
theorem faddeevPhi_proportional_of_stripGrowth
    {b : ℂ} (hb2 : (b ^ 2).im ≠ 0)
    {Φ₁ Φ₂ : ℂ → ℂ} [FaddeevPhi b Φ₁] [FaddeevPhi b Φ₂]
    [FaddeevPhiStripGrowth b Φ₁] [FaddeevPhiStripGrowth b Φ₂]
    (hr_ratio : ∀ z, Φ₂ z ≠ 0 →
      toMeromorphicNFOn (Φ₁ / Φ₂) Set.univ z = Φ₁ z / Φ₂ z)
    (hΦ₂_iso : ∀ z, ∀ᶠ w in 𝓝[≠] z, Φ₂ w ≠ 0)
    {S₀ S₁ : Set ℂ} (hS₀ : Dense S₀) (hS₁ : Dense S₁)
    (hmem₀ : ∀ z ∈ S₀,
      (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I * b) ≠ 0)
    (hmem₁ : ∀ z ∈ S₁,
      (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I / b) ≠ 0) :
    ∃ c, ∀ z, Φ₂ z ≠ 0 → Φ₁ z = c * Φ₂ z := by
  obtain ⟨C, _hC0, hCbound⟩ := ratio_bounded_of_stripGrowth b Φ₁ Φ₂
  -- The raw-ratio bound on `{Φ₂ ≠ 0}` + isolated zeros ⇒ a punctured-neighborhood bound.
  have hpunc : ∀ z, ∀ᶠ w in 𝓝[≠] z,
      ‖toMeromorphicNFOn (Φ₁ / Φ₂) Set.univ w‖ ≤ C := by
    intro z
    filter_upwards [hΦ₂_iso z] with w hw
    rw [hr_ratio w hw]
    exact hCbound w hw
  -- G5 crux: promote to the global `hbdd` the capstone needs.
  have hbdd : ∀ z, ‖toMeromorphicNFOn (Φ₁ / Φ₂) Set.univ z‖ ≤ C :=
    norm_le_of_bounded_on_punctured (meromorphicNFOn_toMeromorphicNFOn _ _) hpunc
  exact FaddeevUniquenessBoundedCapstone.faddeevPhi_proportional_of_bounded_ratio
    hb2 hbdd hr_ratio hS₀ hS₁ hmem₀ hmem₁

end QOU.QBeta.FaddeevStripGrowthUniqueness
