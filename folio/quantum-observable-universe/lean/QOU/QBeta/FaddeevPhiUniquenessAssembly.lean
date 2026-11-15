import QOU.QBeta.FaddeevRigidityMeromorphic
import QOU.QBeta.PeriodLatticeBasis
import QOU.QBeta.CyclicDilogPentagon

/-!
# Route-B assembly for concrete `Φ_b`: proportionality modulo the entire ratio

Instantiates the abstract meromorphic reduction
`FaddeevRigidityMeromorphic.uniqueUpToScalar_of_ratio_dense_periodic` for two
concrete `FaddeevPhi` solutions. The two dense-set periodicities of the ratio are
**derived** from `CyclicDilogPentagon.ratio_ib_periodic` / `ratio_ibinv_periodic`
(valid off the two prefactor lattices) together with the `{ib, i/b}` `ℝ`-basis
`PeriodLatticeBasis.exists_period_basis` (needs `(b²).im ≠ 0`).

**What is discharged.** The two prefactor-lattice complements are dense
(`Common.dense_primaryPole_compl`, `Common.dense_dualPole_compl` — the two
discreteness facts). The double periodicity of the ratio is no longer an input:
it is composed here from the `FaddeevPhi` quasi-period ratio lemmas and the period
basis.

**What remains open (honest, not axiomatized).**

* `hr_entire` — the ratio extends to an **entire** function. This is the
  divisor-rigidity wall (bricks b/c); it is *not* derivable from the difference
  equations (the elliptic ratio may be nonconstant — Weierstrass `℘`), so the
  "same divisor" step is exactly this input, **not** a consequence of double
  periodicity.
* The loci `S₀, S₁` are dense — carried as hypotheses. To use `r = Φ₁/Φ₂` on
  them, they must avoid `Φ₂`'s zeros as well as the prefactor lattice; that
  `Φ_b`-zero discreteness is gated on the `PhiBProd` construction and folded into
  the `Dense Sᵢ` + membership hypotheses, **not** axiomatized.

So this is the §3b-cond reduction: proportionality is *derived* from `hr_entire`
plus the (gated, non-axiomatized) locus density; the conjecture
`conj:algebraic-geometric-dilog-equivalence` stays open until `hr_entire` is
proved for `Φ_b`. Verified `lean`-direct against pinned Mathlib (exit 0).
-/

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm

namespace QOU.QBeta.FaddeevPhiUniquenessAssembly

/-- **Route-B assembly (concrete `Φ_b`).** For two `FaddeevPhi` solutions at `b`
with nondegenerate period lattice (`(b²).im ≠ 0`): if the ratio `r` is entire
(`hr_entire`, the open bricks-b/c input) and equals `Φ₁/Φ₂` off `Φ₂`'s zeros
(`hr_ratio`), and the loci `S₀, S₁` — where the respective prefactor is nonzero
**and** `Φ₂` is nonzero at `z` and at its shift — are dense, then the two
solutions are proportional on `Φ₂`'s nonvanishing locus. The double periodicity
of `r` is *derived* from `ratio_ib_periodic` / `ratio_ibinv_periodic`; only
`hr_entire` and the locus density remain inputs. -/
theorem faddeevPhi_proportional_of_ratio_entire
    {b : ℂ} (hb2 : (b ^ 2).im ≠ 0)
    {Φ₁ Φ₂ r : ℂ → ℂ} [FaddeevPhi b Φ₁] [FaddeevPhi b Φ₂]
    (hr_entire : Differentiable ℂ r)
    (hr_ratio : ∀ z, Φ₂ z ≠ 0 → r z = Φ₁ z / Φ₂ z)
    {S₀ S₁ : Set ℂ} (hS₀ : Dense S₀) (hS₁ : Dense S₁)
    (hmem₀ : ∀ z ∈ S₀,
      (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I * b) ≠ 0)
    (hmem₁ : ∀ z ∈ S₁,
      (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0
        ∧ Φ₂ z ≠ 0 ∧ Φ₂ (z + I / b) ≠ 0) :
    ∃ c, ∀ z, Φ₂ z ≠ 0 → Φ₁ z = c * Φ₂ z := by
  obtain ⟨bas, hbas0, hbas1⟩ := QOU.QBeta.PeriodLatticeBasis.exists_period_basis hb2
  refine QOU.QBeta.FaddeevRigidityMeromorphic.uniqueUpToScalar_of_ratio_dense_periodic
    (bas := bas) hr_entire hr_ratio hS₀ hS₁ ?_ ?_
  · intro z hz
    obtain ⟨hpre, hΦ2, hΦ2s⟩ := hmem₀ z hz
    rw [hbas0, hr_ratio (z + I * b) hΦ2s, hr_ratio z hΦ2,
      QOU.QBeta.CyclicDilogPentagon.ratio_ib_periodic z hpre]
  · intro z hz
    obtain ⟨hpre, hΦ2, hΦ2s⟩ := hmem₁ z hz
    rw [hbas1, hr_ratio (z + I / b) hΦ2s, hr_ratio z hΦ2,
      QOU.QBeta.CyclicDilogPentagon.ratio_ibinv_periodic z hpre]

end QOU.QBeta.FaddeevPhiUniquenessAssembly
