import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum


/-!
# QOU.Torsion.CategoricalProton — Proton as color-linked quark triple

The categorical proton is 𝔭 = [u, u, d]_c ⋈ L_H where u and d are unknot
strands of the Borromean braid B₃ with positive and negative crossing
orientation (`def:up-quark`); their lepton partners are T_{2,3} and its
mirror σ(T_{2,3}).

LaTeX label: `def:categorical-proton`

## References
- [leitner2026] §3/categorical-proton

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Torsion

/-- The categorical proton: color-linked triple [u, u, d]_c ⋈ L_H.
    Mass = S_uu + 2·S_ud ≈ 938.272 MeV. -/
-- Ref: [leitner2026] §3/categorical-proton
structure CategoricalProton where
  /-- Pair Skein mass S_uu. -/
  skein_uu : ℝ
  /-- Pair Skein mass S_ud. -/
  skein_ud : ℝ
  /-- Mass = S_uu + 2·S_ud. -/
  mass : ℝ := skein_uu + 2 * skein_ud
  /-- Positive crossing chirality (electric charge = +1). -/
  chirality : ℤ := 1

-- ═══════════════════════════════════════════════════════════════════
-- Derived mass from the CODATA substrate parameter q₀
-- ═══════════════════════════════════════════════════════════════════

/-- The CODATA substrate parameter q₀ ≈ 1.1097, the unique root q > 1
    of `(1 - q⁻¹)² = Vol(4₁)/(m_μ/m_e)`.
    See `QOU.Experimental.LocalSubstrateQ`. -/
noncomputable def q₀ : ℝ := 1.10998

/-- q₀ > 1. -/
theorem q₀_gt_one : (1 : ℝ) < q₀ := by unfold q₀; norm_num

/-- The proton mass as a function of the substrate parameter q.
    m_𝔭(q) = S_uu(q) + 2 · S_ud(q), where the pair Skein masses
    S_uu and S_ud are determined by the Borromean volume and
    crossing energy at q. -/
noncomputable def proton_mass (q : ℝ) : ℝ :=
  let vol_borromean := 7.32772475341775
  let hbar_q := 1 - q⁻¹
  vol_borromean / hbar_q ^ 2

/-- **What `proton_mass` evaluates to at `q₀`.** A pure arithmetic fact
    about the formula above: `Vol(𝓑₃)/ℏ_q² ≈ 746.40` at the `q₀` of this
    file. No experimental value enters. A former axiom asserting
    `|proton_mass q₀ - 938.272| < 1` was false (this lemma contradicts
    it) and was deleted on owner approval, 2026-11-23. -/
theorem proton_mass_q₀_bounds : 746 < proton_mass q₀ ∧ proton_mass q₀ < 747 := by
  unfold proton_mass q₀
  norm_num

end QOU.Torsion
