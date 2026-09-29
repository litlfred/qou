/-
Measurement-limited floor: the L2 100x gate arithmetic.

The 2026-07-18 precision-goals ceiling record states that four of the five L2
misses (Q_beta, m_n, Delta_pn via c_3; m_p, m_mu via q_0) are gated on the
experimental neutron Q_beta measurement, not on framework compute. The two
heavy inputs are already sorry-free:

  * `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`
    (SRigidityPrune.lean) — no anchor-invariant datum realizes the c_3
    carrier's 2.44% proton/muon swing, so the prediction error of a
    c_3-routed observable inherits the anchor's experimental uncertainty;
  * `PinRobustnessOfRatios.lean` (#3847) — every ratio observable is
    pin-blind (nu_hbar = 0), so no ratio route moves the absolute misses.

This file supplies the missing *gate arithmetic* that composes with them:
an observable whose prediction error is at least one experimental sigma
automatically misses the 100x target (sigma/100) by a factor >= 100. The
premise `sigma <= err` is exactly what the anchor-dependence theorems
establish structurally (absent a substrate-q_0 derivation) and what the L2
dashboard measures concretely for Q_beta (err = 1248 ppb >= sigma = 779.7
ppb). Nothing here claims the premise; the theorems make the *consequence*
("the 100x target is out of reach by >= 100x") a one-step composition
rather than prose.

Archimedean file (ordering + division on measured ppb values) — base ring
`Real` per AGENTS.md section 7c.

Ref: docs/precision-goals.md, "Measurement-limited ceiling" (2026-07-18);
docs/audits/2026-07-18-1ppq-action-plan.md.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.QBeta.MeasurementFloor

/-- **Gate arithmetic.** If a prediction's error is at least one experimental
sigma (`sigma <= err`), the miss factor against the 100x target `sigma/100`
is at least `100`. This is the arithmetic backbone of the measurement-limited
ceiling: the anchor-dependence theorems supply `sigma <= err` for the
c_3-routed observables; this lemma converts it into the L2-dashboard
statement "misses 100x by >= 100x". -/
theorem miss_factor_ge_100 (σ err : ℝ) (hσ : 0 < σ) (h : σ ≤ err) :
    100 ≤ err / (σ / 100) := by
  rw [le_div_iff₀ (by positivity)]
  linarith

/-- The 100x target itself is strictly unreachable under the same premise:
`sigma/100 < err` whenever `0 < sigma <= err`. -/
theorem hundredfold_target_unreachable (σ err : ℝ) (hσ : 0 < σ) (h : σ ≤ err) :
    σ / 100 < err := by
  linarith

/-- Contrapositive, the actionable reading: beating the 100x target forces the
prediction error strictly below one experimental sigma — i.e. below the
measurement floor. Absent a substrate-q_0 derivation, the anchor-dependence
theorems exclude exactly this for the c_3-routed observables. -/
theorem err_lt_sigma_of_beats_target (σ err : ℝ) (hσ : 0 < σ)
    (hbeat : err < σ / 100) : err < σ := by
  linarith

/-- **Concrete Q_beta instance** (2026-07-06/18 L2 dashboard values, in ppb):
`sigma_exp = 779.7`, prediction error `1248`; the measured miss factor
`1248 / (779.7/100) = 160.06...` is `>= 100`. Pure `norm_num` — records the
dashboard arithmetic as a checked fact, not a new measurement. -/
theorem qbeta_dashboard_miss_ge_100 :
    (100 : ℝ) ≤ 1248 / ((7797 / 10) / 100) := by
  norm_num

/-- The Q_beta dashboard premise itself: the measured error exceeds one
experimental sigma (`779.7 <= 1248` ppb), so `miss_factor_ge_100` applies. -/
theorem qbeta_dashboard_err_ge_sigma : (7797 / 10 : ℝ) ≤ 1248 := by
  norm_num

end QOU.QBeta.MeasurementFloor
