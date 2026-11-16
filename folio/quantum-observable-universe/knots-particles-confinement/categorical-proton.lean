import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum


/-!
# QOU.Torsion.CategoricalProton — Proton as color-linked quark triple

The categorical proton is 𝔭 = [u, u, d]_c ⋈ L_H where u = T_{2,3}
(trefoil) and d = σ(T_{2,3}) (three-twist, Skein descendant).

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

/-- The bare Borromean volume carrier as a function of the substrate parameter `q`:
    `Vol(𝓑₃) / (1 - q⁻¹)²` with `Vol(𝓑₃) ≈ 7.32772475341775`.
    Per the 2026-06-24 and 2026-08-11 owner rulings (see `qou-4paj` and
    `docs/audits/2026-09-04-two-false-nucleon-mass-axioms.md`), this bare
    hyperbolic-volume carrier (`≈ 746.40` at `q₀ = 1.10998`) is superseded by
    the canonical Wedderburn / Borromean trace ratio and is retained here only
    as a historical reference expression without the inconsistent `< 1` axiom. -/
noncomputable def proton_mass (q : ℝ) : ℝ :=
  let vol_borromean := 7.32772475341775
  let hbar_q := 1 - q⁻¹
  vol_borromean / hbar_q ^ 2

/-- Exact evaluation of the bare Borromean carrier `proton_mass` at `q₀` (`qou-4paj`).
    Replaces the former inconsistent `proton_mass_from_substrate_axiom`
    (which asserted `|proton_mass q₀ - 938.272| < 1`, refuted below by
    `bare_borromean_carrier_not_938`). -/
-- Ref: [leitner2026] Ch. 5, §Categorical proton
theorem proton_mass_from_substrate :
    proton_mass q₀ = 7.32772475341775 / (1 - q₀⁻¹) ^ 2 :=
  rfl

/-- At `q₀ = 1.10998`, the bare Borromean carrier `proton_mass q₀ ≈ 746.400676`
    does **not** lie within `1` of `938.272` (`qou-4paj`). -/
-- Ref: [leitner2026] Ch. 5, §Categorical proton
theorem bare_borromean_carrier_not_938 :
    ¬ (|proton_mass q₀ - 938.272| < 1) := by
  unfold proton_mass q₀
  norm_num [abs_lt]

end QOU.Torsion
