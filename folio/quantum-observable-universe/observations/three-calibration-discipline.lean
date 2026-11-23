import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.Observations.CalibrationTriple — the three calibration inputs (definition)

`def:three-calibration-discipline` names the three external calibration
inputs and **defines** the substrate parameter `q₀` from the second one:

* CAL-1 `m_e` — the mass unit;
* CAL-2 — the substrate parameter `q₀`, defined as the unique `q > 1` with
  `(1 - q⁻¹)² = Vol(4₁) / (m_μ/m_e)`; the ratio `m_μ/m_e` is the numerical
  proxy of the ideal CAL-2 observable (the neutron β-decay width);
* CAL-3 `m_π` — the meson-sector scale.

This file states that definition and proves what makes it a definition: for
every ratio `r ∈ (0, 1)` the equation `(1 - q⁻¹)² = r` has exactly one root
`q > 1`, namely `q = 1 / (1 - √r)`.

It asserts nothing about how masses factor through the three inputs. That
claim is `conj:three-calibration-inputs`. Nor does it assert that the three
inputs are the three real moduli of `H¹(Bring)`; that is
`conj:calibration-cohomology-alignment`. Until 2026-11-20 this block carried
the factorisation claim as an assumed class field (bean qou-tm3c).

**Ground ring**: `ℝ`. The construction uses `Real.sqrt` and the ordering
`1 < q`, both archimedean (AGENTS.md §7c).

Ref: [leitner2026] observations/three-calibration-discipline
-/

namespace QOU.Observations

/-- The root `q = 1 / (1 - √r)` of `(1 - q⁻¹)² = r`. -/
noncomputable def calibratedQ (r : ℝ) : ℝ := 1 / (1 - Real.sqrt r)

/-- For `0 < r < 1`, `calibratedQ r` exceeds `1` and solves `(1 - q⁻¹)² = r`. -/
theorem calibratedQ_spec {r : ℝ} (hr0 : 0 < r) (hr1 : r < 1) :
    1 < calibratedQ r ∧ (1 - (calibratedQ r)⁻¹) ^ 2 = r := by
  have hs0 : 0 < Real.sqrt r := Real.sqrt_pos.mpr hr0
  have hs1 : Real.sqrt r < 1 := by
    rw [show (1 : ℝ) = Real.sqrt 1 from Real.sqrt_one.symm]
    exact Real.sqrt_lt_sqrt hr0.le hr1
  have hd : 0 < 1 - Real.sqrt r := by linarith
  refine ⟨?_, ?_⟩
  · unfold calibratedQ
    rw [lt_div_iff₀ hd]
    linarith
  · unfold calibratedQ
    rw [one_div, inv_inv, sub_sub_cancel, Real.sq_sqrt hr0.le]

/-- Uniqueness: any `q > 1` with `(1 - q⁻¹)² = r` equals `calibratedQ r`. -/
theorem calibratedQ_unique {r q : ℝ} (hq : 1 < q) (h : (1 - q⁻¹) ^ 2 = r) :
    q = calibratedQ r := by
  have hq0 : 0 < q := by linarith
  have hinv : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hpos : 0 ≤ 1 - q⁻¹ := by linarith
  have hsq : Real.sqrt r = 1 - q⁻¹ := by
    rw [← h]; exact Real.sqrt_sq hpos
  unfold calibratedQ
  rw [hsq, sub_sub_cancel, one_div, inv_inv]

/-- **The calibration triple** (`def:three-calibration-discipline`).

    The three external inputs, with the substrate parameter `q₀` defined
    from the CAL-2 proxy. `vol41` is the hyperbolic volume of the
    figure-eight knot, `2·Cl₂(π/3)`, supplied as data; `vol41_lt` says the
    ratio `Vol(4₁)/(m_μ/m_e)` lies below `1`, which is the range where the
    defining equation has a root `q > 1`. -/
structure CalibrationTriple where
  /-- CAL-1: the mass unit `m_e`. -/
  m_e : ℝ
  m_e_pos : 0 < m_e
  /-- CAL-2 proxy: the lepton mass ratio `m_μ/m_e`. -/
  mu_over_e : ℝ
  /-- CAL-3: the meson-sector scale `m_π`, in the units of `m_e`. -/
  m_pi : ℝ
  m_pi_pos : 0 < m_pi
  /-- The figure-eight volume `Vol(4₁)`. -/
  vol41 : ℝ
  vol41_pos : 0 < vol41
  vol41_lt : vol41 < mu_over_e

namespace CalibrationTriple

/-- The substrate parameter `q₀` defined by CAL-2:
    the root `q > 1` of `(1 - q⁻¹)² = Vol(4₁)/(m_μ/m_e)`. -/
noncomputable def q0 (c : CalibrationTriple) : ℝ :=
  calibratedQ (c.vol41 / c.mu_over_e)

private theorem ratio_mem (c : CalibrationTriple) :
    0 < c.vol41 / c.mu_over_e ∧ c.vol41 / c.mu_over_e < 1 := by
  have hm : 0 < c.mu_over_e := lt_trans c.vol41_pos c.vol41_lt
  exact ⟨div_pos c.vol41_pos hm, (div_lt_one hm).mpr c.vol41_lt⟩

/-- `q₀ > 1` and it solves the CAL-2 equation. -/
theorem q0_spec (c : CalibrationTriple) :
    1 < c.q0 ∧ (1 - c.q0⁻¹) ^ 2 = c.vol41 / c.mu_over_e :=
  calibratedQ_spec c.ratio_mem.1 c.ratio_mem.2

/-- `q₀` is the only `q > 1` solving the CAL-2 equation. -/
theorem q0_unique (c : CalibrationTriple) {q : ℝ} (hq : 1 < q)
    (h : (1 - q⁻¹) ^ 2 = c.vol41 / c.mu_over_e) : q = c.q0 :=
  calibratedQ_unique hq h

end CalibrationTriple

end QOU.Observations
