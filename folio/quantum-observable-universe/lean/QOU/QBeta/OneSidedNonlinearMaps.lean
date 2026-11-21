import QOU.QBeta.OneSidedReading

/-!
# Nonlinear energy maps for the one-sided lepton factor

Thread "Find where the n–p mass error comes from", 2026-11-21. Audit
`docs/audits/2026-11-21-qbeta-np-error-budget.md` §13. Owner, 2026-11-21: "Q_beta I don't think is
a linear map". `OneSidedReading` tested the linear and log maps. Here the map `g` is arbitrary.

## Setting

A state's energy is `E(X) = g(ε(X))`, a function of its trace, with the final-state trace
multiplicative: `ε(p e⁻ ν̄) = ε_p·f`. The `Q_β` reading needs both
* lepton pair `g(ε_p·f) − g(ε_p) > 0` (it carries `m_e + E_ν̄`), and
* `Q_β = g(ε_n) − g(ε_p·f) > 0`.

## What is proved (on `1 < q ≤ 23/20`)

1. `ordering`: `ε_p·f < ε_n < ε_p`. The `q`-content: `f < q⁻²` (`leptonFactor_lt_inv_sq`, every
   `q > 1`, since `q³ < [2]⁴`) and `ε_n = ε_p/q²` (`epsN_V3B_eq`).
2. `monotone_excluded`: for **every** monotone or antitone `g`, the two conditions cannot both hold.
   This covers the linear map, `|·|`, `±log`, `1/x` (the `ℏ/𝔇` form), every power, and every
   additive map `g(xy) = g(x) + g(y)` that is monotone (the continuous ones are `c·log`).
3. `nonmonotone_needed`: any `g` meeting both conditions has `g(ε_n) > g(ε_p f) > g(ε_p)` at three
   points with `ε_p f < ε_n < ε_p`: it rises then falls. No such map is on record.
4. `weighted_needs_density_jump`: for the corpus form `E(X) = c·ρ_X·ε(X)` (`m = m_e ρ_K |tr_M|`,
   `c > 0`), the lepton-pair condition forces `ρ_final > ρ_p / f`, a density jump by the factor
   `[2]⁴/q` that no density rule on record supplies.

## Scope

Scope (b) for item 2 (invariant: the ordering of item 1); scope (a) beyond it. It does not
exclude an energy that is not a function of the trace (e.g. one additive over components with the
electron's own `m_e`, which is the two-sided kinematic reading already on record).
-/

namespace QOU.QBeta.OneSidedNonlinearMaps

open QOU.QBeta.FlavourWeightSplit
open QOU.QBeta.OneSidedLeptonFactor
open QOU.QBeta.OneSidedReading
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-- `ε_n(V³) = ε_p(V³)/q²`. -/
theorem epsN_V3B_eq {q : ℝ} (hq : q ≠ 0) :
    epsN q (borromeanV3B q) = epsP q (borromeanV3A q) / q ^ 2 := by
  unfold epsN epsP
  rw [trace_borromeanV3A q hq, trace_borromeanV3B q hq]
  field_simp

/-- `f = q/[2]⁴ < q⁻²` for `q > 1`. -/
theorem leptonFactor_lt_inv_sq {q : ℝ} (hq1 : 1 < q) : leptonFactor q < 1 / q ^ 2 := by
  unfold leptonFactor qd2
  have hq0 : 0 < q := by linarith
  have hgt : q < q + q⁻¹ := by have := inv_pos.mpr hq0; linarith
  have h4 : q ^ 4 < (q + q⁻¹) ^ 4 := pow_lt_pow_left₀ hgt hq0.le (by norm_num)
  have hq3 : q ^ 3 < q ^ 4 := pow_lt_pow_right₀ hq1 (by norm_num)
  rw [div_lt_div_iff₀ (by positivity) (by positivity)]
  nlinarith

/-- **`ε_p·f < ε_n < ε_p`.** -/
theorem ordering {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    epsP q (borromeanV3A q) * leptonFactor q < epsN q (borromeanV3B q) ∧
      epsN q (borromeanV3B q) < epsP q (borromeanV3A q) := by
  have hq0 : 0 < q := by linarith
  have hp := epsP_V3A_pos hq1 hq2
  have hf := leptonFactor_lt_inv_sq hq1
  have hq2' : 1 < q ^ 2 := one_lt_pow₀ hq1 (by norm_num)
  rw [epsN_V3B_eq hq0.ne']
  constructor
  · have : epsP q (borromeanV3A q) * leptonFactor q < epsP q (borromeanV3A q) * (1 / q ^ 2) :=
      mul_lt_mul_of_pos_left hf hp
    rwa [mul_one_div] at this
  · rw [div_lt_iff₀ (by positivity)]
    nlinarith

/-- **No monotone or antitone energy map gives both a positive lepton pair and a positive `Q_β`.** -/
theorem monotone_excluded {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) (g : ℝ → ℝ)
    (hg : Monotone g ∨ Antitone g) :
    ¬ (g (epsP q (borromeanV3A q)) < g (epsP q (borromeanV3A q) * leptonFactor q) ∧
       g (epsP q (borromeanV3A q) * leptonFactor q) < g (epsN q (borromeanV3B q))) := by
  obtain ⟨h1, h2⟩ := ordering hq1 hq2
  rintro ⟨hpair, hQ⟩
  rcases hg with hm | ha
  · have := hm (h1.trans h2).le
    linarith
  · have := ha h1.le
    linarith

/-- **A map meeting both conditions rises then falls across `ε_p f < ε_n < ε_p`.** -/
theorem nonmonotone_needed {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) (g : ℝ → ℝ)
    (hpair : g (epsP q (borromeanV3A q)) < g (epsP q (borromeanV3A q) * leptonFactor q))
    (hQ : g (epsP q (borromeanV3A q) * leptonFactor q) < g (epsN q (borromeanV3B q))) :
    ¬ Monotone g ∧ ¬ Antitone g :=
  ⟨fun hm => monotone_excluded hq1 hq2 g (Or.inl hm) ⟨hpair, hQ⟩,
   fun ha => monotone_excluded hq1 hq2 g (Or.inr ha) ⟨hpair, hQ⟩⟩

/-- **Density-weighted map: a positive lepton pair needs `ρ_final > ρ_p / f`.** -/
theorem weighted_needs_density_jump {q c ρp ρf : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (hc : 0 < c)
    (hpair : c * ρp * epsP q (borromeanV3A q) <
      c * ρf * (epsP q (borromeanV3A q) * leptonFactor q)) :
    ρp < ρf * leptonFactor q := by
  have hp := epsP_V3A_pos hq1 hq2
  have : c * epsP q (borromeanV3A q) * ρp < c * epsP q (borromeanV3A q) * (ρf * leptonFactor q) := by
    nlinarith
  exact lt_of_mul_lt_mul_left this (by positivity)

end QOU.QBeta.OneSidedNonlinearMaps
