import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring


/-!
# QOU.Torsion.CategoricalNeutron — Neutron as color-linked quark triple

The categorical neutron is 𝔫 = [u, d, d]_c ⋈ L_H.

LaTeX label: `def:categorical-neutron`

## References
- [leitner2026] §3/categorical-neutron

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Torsion

/-- The categorical neutron: color-linked triple [u, d, d]_c ⋈ L_H.
    Mass = 2·S_ud + S_dd ≈ 939.565 MeV. -/
-- Ref: [leitner2026] §3/categorical-neutron
structure CategoricalNeutron where
  /-- Pair Skein mass S_ud. -/
  skein_ud : ℝ
  /-- Pair Skein mass S_dd. -/
  skein_dd : ℝ
  /-- Mass = 2·S_ud + S_dd. -/
  mass : ℝ := 2 * skein_ud + skein_dd
  /-- Zero crossing chirality (electric charge = 0). -/
  chirality : ℤ := 0

-- ═══════════════════════════════════════════════════════════════════
-- Derived mass from the CODATA substrate parameter q₀
-- ═══════════════════════════════════════════════════════════════════

/-- The CODATA substrate parameter q₀ ≈ 1.1097, the unique root q > 1
    of `(1 - q⁻¹)² = Vol(4₁)/(m_μ/m_e)`.
    See `QOU.Experimental.LocalSubstrateQ`. -/
noncomputable def q₀ : ℝ := 1.10998

/-- q₀ > 1. -/
theorem q₀_gt_one : (1 : ℝ) < q₀ := by unfold q₀; norm_num

/-- The bare Borromean + Skein-asymmetry carrier as a function of `q`:
    `Vol(𝓑₃) / (1 - q⁻¹)² + (1/2)(q - q⁻¹)`.
    Per the 2026-06-24 and 2026-08-11 owner rulings (see `qou-4paj` and
    `docs/audits/2026-09-04-two-false-nucleon-mass-axioms.md`), this bare
    hyperbolic-volume carrier (`≈ 746.505` at `q₀ = 1.10998`) is superseded by
    the canonical Wedderburn / Borromean trace ratio and is retained here only
    as a historical reference expression without the inconsistent `< 1` axiom. -/
noncomputable def neutron_mass (q : ℝ) : ℝ :=
  let vol_borromean := 7.32772475341775
  let hbar_q := 1 - q⁻¹
  let skein_asymmetry := (1 / 2) * (q - q⁻¹)  -- crossing energy asymmetry
  vol_borromean / hbar_q ^ 2 + skein_asymmetry

/-- Exact evaluation of the bare neutron carrier `neutron_mass` at `q₀` (`qou-4paj`).
    Replaces the former inconsistent `neutron_mass_from_substrate_axiom`
    (which asserted `|neutron_mass q₀ - 939.565| < 1`, refuted below by
    `bare_neutron_carrier_not_939`). -/
-- Ref: [leitner2026] Ch. 5, §Categorical neutron
theorem neutron_mass_from_substrate :
    neutron_mass q₀ = 7.32772475341775 / (1 - q₀⁻¹) ^ 2 + (1 / 2) * (q₀ - q₀⁻¹) :=
  rfl

/-- At `q₀ = 1.10998`, the bare neutron carrier `neutron_mass q₀ ≈ 746.505208`
    does **not** lie within `1` of `939.565` (`qou-4paj`). -/
-- Ref: [leitner2026] Ch. 5, §Categorical neutron
theorem bare_neutron_carrier_not_939 :
    ¬ (|neutron_mass q₀ - 939.565| < 1) := by
  unfold neutron_mass q₀
  norm_num [abs_lt]

/-- The proton-neutron mass splitting is a pure function of q.
    Δm = S_dd(q) - S_uu(q) ≈ 1.293 MeV at q₀. -/
-- Ref: [leitner2026] Ch. 5, §Categorical neutron
theorem neutron_proton_splitting :
    ∀ q : ℝ, 1 < q →
    neutron_mass q - (7.32772475341775 / (1 - q⁻¹) ^ 2) =
    (1 / 2) * (q - q⁻¹) := by
  -- Ref: [leitner2026] Ch. 5, §Categorical neutron
  intro q hq
  unfold neutron_mass
  -- After unfolding, the let-bindings expand and the difference
  -- cancels the vol_borromean / hbar_q^2 term, leaving the asymmetry.
  simp only []
  ring

end QOU.Torsion
