/-
# c₃ bar-odd residual `S_leak` — the MAGNITUDE is anchor-offset arithmetic, not a period

Companion to `SLeakZeroCrossing.lean`. That file formalizes the **sign** of the
bar-odd residual `S_leak(q₀) = c₃(q₀) + Vol(4₁)`: a sign flip across the two
substrate anchors forces a zero-crossing at some `q*` strictly between them
(`sleak_zero_between_anchors`), and excludes every sign-definite carrier
(`sign_definite_carrier_excluded`).

This file formalizes the **magnitude** result found by the Bring-embedding probe
(`computations/qbeta/qbeta_bring_embedding_magnitude_probe.py`,
`docs/audits/2026-08-01-bring-embedding-magnitude.md`): the observed
`|S_leak(proton)/S_leak(muon)| ≈ 4.075` is **not** a knot-embedding period — it is
the ratio of anchor offsets from the simple zero `q*`, and the local slope (the only
"period-like" datum at `q*`) *cancels* in that ratio. Two consequences are proved,
both generic (the two anchor magnitudes never enter as fitted constants):

* `linear_ratio_slope_independent` — for the leading-order linearization
  `S_leak(q) = L·(q − q*)` at the simple zero, the ratio
  `S_leak(qp)/S_leak(qm) = (qp − q*)/(qm − q*)` is **independent of the slope `L`**.
  So the magnitude fixes only *where the anchors fall* relative to `q*`; the slope
  `L` — the candidate "Bring period / X5 weight" datum — drops out and cannot be
  read back from the magnitude. This is why the sign is q-insensitive (a stable
  parity) while the magnitude is q-hypersensitive (anchor placement): they are
  different data, and only the sign is a period-carried invariant.

* `smooth_ratio_near_one` + `smooth_period_excluded_as_magnitude` — **scope-(b)
  exclusion.** Any Lipschitz `P` on the anchor interval has ratio
  `|P(qp)/P(qm) − 1| ≤ K·|qp − qm|/|P(qm)|`. When that variation budget is `< 1`
  — the case for any `O(1)` geometric period over the `Δq ≈ 1.3e-8` anchor gap
  (`K ~ O(1)`, `|P(qm)| ~ O(1)` ⇒ budget `~1e-8`) — the ratio lies in `(0,2)` and
  **cannot** equal the observed `|S_leak(proton)/S_leak(muon)| ≈ 4.075` (`|r| ≥ 2`).
  A smooth q₀-evaluated period is `≈` identical at both anchors; only a
  hypersensitive near-degeneracy (the SP2 class) supplies a factor-≈4 ratio. This
  is the SP1 smoothness wall, restated for Bring-intrinsic periods.

Discipline: the magnitude probe returned an honest **negative** (the Bring
X5-weight / SW-period route does not force `4.075`); this file proves the *invariant*
behind that negative (slope cancellation + the smoothness wall), per the
anti-laundering "prove the invariant that would justify a (b)" rule. No `u(q₀)` is
wired, no `c_k` proposed, no `SDeformedVolumeChannel` instance fabricated. The
magnitude stays OPEN (SP2 / `qou-4kr1`).

Archimedean by necessity (ordering + absolute value), so `ℝ` per §7c.

-- Ref: [leitner2026] docs/audits/2026-08-01-bring-embedding-magnitude.md
-/
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith

namespace QOU.QBeta.SLeakMagnitudeOffsetRatio

/-- **Slope cancellation.** For the leading-order linearization of a function at a
simple zero `q*`, `S(q) = L·(q − q*)`, the ratio of two evaluations equals the ratio
of their offsets from `q*`, *independently of the slope* `L ≠ 0`. Applied to the
bar-odd residual `S_leak`, the observed `|S_leak(proton)/S_leak(muon)|` therefore
carries information about anchor placement relative to `q*` — not about the local
slope, so no "period value" can be extracted from it. -/
theorem linear_ratio_slope_independent
    {L qstar qm qp : ℝ} (hL : L ≠ 0) :
    (L * (qp - qstar)) / (L * (qm - qstar)) = (qp - qstar) / (qm - qstar) :=
  mul_div_mul_left (qp - qstar) (qm - qstar) hL

/-- **Lipschitz ratio bound.** A function `P` whose variation over the anchor
interval is bounded by `K·|qp − qm|` has multiplicative ratio within
`K·|qp − qm|/|P(qm)|` of `1`. -/
theorem smooth_ratio_near_one
    {P : ℝ → ℝ} {qm qp K : ℝ}
    (hlip : |P qp - P qm| ≤ K * |qp - qm|)
    (hPm : P qm ≠ 0) :
    |P qp / P qm - 1| ≤ K * |qp - qm| / |P qm| := by
  have heq : P qp / P qm - 1 = (P qp - P qm) / P qm := by
    rw [sub_div, div_self hPm]
  rw [heq, abs_div]
  gcongr

/-- **Scope-(b): a smooth period cannot supply the factor-≈4 magnitude ratio.**
If a Lipschitz `P` on the anchor interval has variation budget
`K·|qp − qm|/|P(qm)| < 1` — the regime of any `O(1)` geometric period over the
`Δq ≈ 1.3e-8` anchor gap — then its ratio `r = P(qp)/P(qm)` satisfies `|r − 1| < 1`,
so `|r| < 2` and it **cannot** equal the observed
`|S_leak(proton)/S_leak(muon)| ≈ 4.075` (which has `|r| ≥ 2`). This is the SP1
smoothness wall for Bring-intrinsic periods: a smooth q₀-evaluated period is nearly
constant across the two anchors, so the factor-≈4 magnitude asymmetry cannot be a
period ratio. -/
theorem smooth_period_excluded_as_magnitude
    {P : ℝ → ℝ} {qm qp K r : ℝ}
    (hlip : |P qp - P qm| ≤ K * |qp - qm|)
    (hPm : P qm ≠ 0)
    (hsmall : K * |qp - qm| / |P qm| < 1)
    (hr : P qp / P qm = r) (hrbig : 2 ≤ |r|) : False := by
  have hb : |r - 1| ≤ K * |qp - qm| / |P qm| := by
    have := smooth_ratio_near_one hlip hPm
    rwa [hr] at this
  have hge : (1 : ℝ) ≤ |r - 1| := by
    rcases le_abs.mp hrbig with h | h
    · exact le_abs.mpr (Or.inl (by linarith))
    · exact le_abs.mpr (Or.inr (by linarith))
  linarith

end QOU.QBeta.SLeakMagnitudeOffsetRatio
