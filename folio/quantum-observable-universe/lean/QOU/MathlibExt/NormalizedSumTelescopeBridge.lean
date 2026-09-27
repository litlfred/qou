import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.MathlibExt.NormalizedSumTelescopeBridge — bricks for closing `normalizedSum n q = 1`

The general-`n` fake-degree residual `normalizedSum n q = 1` closes via the corpus general-X
telescope `MacdonaldTelescopeGeneralX.telescope_generalX` at `X = 0`, through the per-λ **convention
bridge** `q^{−κ_λ}/hookProd_q(λ) = jonesMarkovCoeff(q², 0, λ)` (route verified exact `n≤5` in
`computations/qbeta/fake_degree_via_telescope_probe.py`; audit
`docs/audits/2026-08-29-normalizedsum-closes-via-telescope.md`).

This file lands the **per-cell algebraic brick** the convention bridge turns on: the Macdonald
denominator factor `1 − q^{2h}` (i.e. `1 − Q^{h}` at `Q = q²`, the per-cell denominator of
`schurElement`) in terms of the balanced hook bracket `[h]_q = qBracket q h` (the per-cell factor of
`hookProd_q`). This is the exact term-by-term relation that, multiplied over the cells of `λ` and
combined with the `Q^{n(λ)}`, `wenzlNormalisation` and the n-statistic identity
`κ_λ = Σ_x h_x − |λ| − 2 n(λ)`, yields the convention bridge.

Base ring: generic `[Field R]` with `q ≠ 0`, `q − q⁻¹ ≠ 0` (§7c — purely algebraic).

-- Ref: computations/qbeta/fake_degree_via_telescope_probe.py (closure route, exact n≤5)
-- Ref: content/.../QOU/MathlibExt/MacdonaldTelescopeGeneralX.lean (telescope_generalX, all X)
-/

namespace QOU.MathlibExt.NormalizedSumTelescopeBridge

open QOU.MathlibExt.QPartitionCombinatorics

variable {R : Type*} [Field R]

/-- **Per-cell denominator bridge.** The Macdonald per-cell denominator factor `1 − q^{2h}` (the
`1 − Q^{h}` of `schurElement` at `Q = q²`) equals `−q^{h}·(q − q⁻¹)·[h]_q` in terms of the balanced
hook bracket. Chained over the cells of `λ`, this converts `∏_x 1/(1 − q^{2 h_x})` into
`(−1)^{|λ|} q^{−Σh} (q − q⁻¹)^{−|λ|} / hookProd_q(λ)`, the numerator side of the convention bridge. -/
theorem one_sub_qsq_pow_eq (q : R) (hq0 : q ≠ 0) (hden : q - q⁻¹ ≠ 0) (h : ℕ) :
    (1 : R) - q ^ (2 * h) = -(q ^ h) * (q - q⁻¹) * qBracket q h := by
  have ha : q ^ h ≠ 0 := pow_ne_zero h hq0
  have hb : qBracket q h * (q - q⁻¹) = q ^ h - (q ^ h)⁻¹ := by
    rw [qBracket_eq_formula, zpow_neg, zpow_natCast]
    exact div_mul_cancel₀ _ hden
  have hcomm : -(q ^ h) * (q - q⁻¹) * qBracket q h
      = -(q ^ h) * (qBracket q h * (q - q⁻¹)) := by ring
  rw [hcomm, hb, mul_comm 2 h, pow_mul]
  linear_combination -mul_inv_cancel₀ ha
