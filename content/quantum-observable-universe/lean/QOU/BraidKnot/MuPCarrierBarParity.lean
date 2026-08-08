/-
Copyright (c) 2026 litlfred. All rights reserved.

# μ–p residual on the muon carrier: the bar-parity selection rule (generic)

Bean `qou-6gf9`. Companion audit:
`docs/audits/2026-08-08-mu-p-residual-carrier-order-and-bar-parity-prune.md`.
Probe: `docs/audits/scripts/mu_p_carrier_order_window_probe.py`.
Archimedean half (order window + the `MmuR9V9Closure` exclusions):
`QOU/BraidKnot/MuPCarrierOrderWindow.lean` (split per AGENTS.md §7c).

## Context

The muon carrier is `m_μ/m_e = Vol(4₁)/ℏ_q²`. At the experimental (proton) pin
it overshoots CODATA by `+209.755 ppb = 9.53 σ`, so *if* the carrier is only
the leading term of a series, the first correction must supply the
multiplicative factor `1 − t` with `t ≈ 2.0975e-7`.

The standing precondition on that correction — argued from the amphichirality
of the muon anchor knot `4₁` in
`docs/audits/2026-06-20-keystone-branching-shift-first-crack.md` §Consequence,
and used to disqualify the projector-weight shift in
`docs/audits/2026-06-22-keystone-qdeform-projector-shift.md` §3 — is that it
must be **bar-even**, i.e. fixed by `q ↦ q⁻¹`.

## What this file proves

Under the bar involution the substrate is *not* fixed: `ℏ_{q⁻¹} = −q·ℏ_q`
(`hbarGen_bar`). Hence a monomial `ℏ_q^k · q^m` picks up the factor
`(−1)^k q^{k−m}`, which is `1` for all `q` exactly when `k` is even and
`m = k/2`. So:

> the bar-even part of the `ℏ_q`-monomial family is precisely the tower of
> `w := q·ℏ_q² = q + q⁻¹ − 2 = [2]_q − 2`.

Positive half: `hbarGen_pow_two_mul_eq_wGen_pow` (`ℏ_q^{2j}·q^j = w^j`) with
`wGen_bar`, giving `hbarGen_monomial_bar_even`. Negative half, in witness form:
`hbarGen_monomial_six_one_not_bar_even` shows the `(k,m) = (6,1)` pattern — the
shape of `MmuR9V9Closure.delta_R9` — is not bar-even.

Nothing here is archimedean, so everything is stated over a generic
`{K : Type*} [Field K]` (AGENTS.md §7c).

## What this file does NOT claim

No correction is derived, and nothing is wired. The bar-*mixedness* results are
unconditional; the *exclusion* they license is conditional on the bar-even
precondition, which is **argued** in the corpus, not proved (AGENTS.md
§"Conditional-proved ≠ premise-established"). Scope of the negative: **(b)**
*relative to that precondition*, whose named invariant is bar-parity under
`q ↦ q⁻¹`.
-/
import Mathlib.Tactic

namespace QOU.BraidKnot.MuPCarrier

variable {K : Type*} [Field K]

/-- Substrate `ℏ_q = 1 − q⁻¹`, over a generic field. Agrees with the production
`QOU.BraidKnot.hbarQ` on `ℝ` (see `MuPCarrierOrderWindow.hbarGen_eq_hbarQ`). -/
def hbarGen (q : K) : K := 1 - q⁻¹

/-- `w := [2]_q − 2 = q + q⁻¹ − 2`, over a generic field. -/
def wGen (q : K) : K := q + q⁻¹ - 2

/-- **The bar involution does not fix `ℏ_q`.** Applying `q ↦ q⁻¹` multiplies it
by `−q`:

  `ℏ_{q⁻¹} = −q · ℏ_q`.

This single identity drives the whole selection rule below. -/
theorem hbarGen_bar (q : K) (hq : q ≠ 0) : hbarGen q⁻¹ = -q * hbarGen q := by
  unfold hbarGen
  rw [inv_inv]
  field_simp
  ring

/-- `w` is bar-invariant: `w_{q⁻¹} = w_q`. -/
theorem wGen_bar (q : K) : wGen q⁻¹ = wGen q := by
  unfold wGen
  rw [inv_inv]
  ring

/-- `w` is the `q`-dressed square of the substrate: `w_q = q · ℏ_q²`. -/
theorem wGen_eq_q_mul_hbarGen_sq (q : K) (hq : q ≠ 0) :
    wGen q = q * hbarGen q ^ 2 := by
  unfold wGen hbarGen
  field_simp
  ring

/-- **Selection rule, positive half.** The monomial `ℏ_q^{2j} · q^{j}` — the only
`(k, m)` pattern with `k = 2m` — *is* the `j`-th power of `w`. -/
theorem hbarGen_pow_two_mul_eq_wGen_pow (q : K) (hq : q ≠ 0) (j : ℕ) :
    hbarGen q ^ (2 * j) * q ^ j = wGen q ^ j := by
  rw [wGen_eq_q_mul_hbarGen_sq q hq, mul_pow, pow_mul]
  ring

/-- **Selection rule, corollary.** Consequently every such monomial is bar-even:

  `ℏ_{q⁻¹}^{2j} · (q⁻¹)^j = ℏ_q^{2j} · q^j`.

So the bar-even part of the `ℏ_q`-monomial family is exactly the `w`-tower. -/
theorem hbarGen_monomial_bar_even (q : K) (hq : q ≠ 0) (j : ℕ) :
    hbarGen q⁻¹ ^ (2 * j) * (q⁻¹) ^ j = hbarGen q ^ (2 * j) * q ^ j := by
  rw [hbarGen_pow_two_mul_eq_wGen_pow q⁻¹ (inv_ne_zero hq) j,
    hbarGen_pow_two_mul_eq_wGen_pow q hq j, wGen_bar]

/-- **Selection rule, negative half (witness form).** A monomial whose `q`-power
is *not* half its `ℏ_q`-power is not bar-even. Exhibited on the exponent pattern
`(k, m) = (6, 1)` — exactly the shape of `MmuR9V9Closure.delta_R9` — at `q = 2`:
`ℏ_2⁶·2 = 1/32` while `ℏ_{1/2}⁶·(1/2) = 1/2`. -/
theorem hbarGen_monomial_six_one_not_bar_even :
    hbarGen ((2 : ℚ)⁻¹) ^ 6 * (2 : ℚ)⁻¹ ≠ hbarGen (2 : ℚ) ^ 6 * (2 : ℚ) := by
  unfold hbarGen
  norm_num

/-- **The bar-even repair of the `(6,1)` pattern is `q³`, not `q`.**

The `ℏ_q⁶` prefactor is bar-even only when dressed by `q³`, and `ℏ_q⁶·q³ = w³`.
So the nearest bar-even relative of the R9 rung lives in the `w`-tower at
`j = 3`. (The probe then shows that tower admits no order with a small-height
coefficient: `t/w³ = 0.16211 < 1/5` and `t/w⁴ = 14.877 > 5`.) -/
theorem hbarGen_six_bar_even_dressing (q : K) (hq : q ≠ 0) :
    hbarGen q ^ 6 * q ^ 3 = wGen q ^ 3 :=
  hbarGen_pow_two_mul_eq_wGen_pow q hq 3

-- Verification (2026-08-08, `scripts/lean-verify.sh`, exit 0, 0 sorries):
-- `#print axioms` on every declaration above returns exactly
-- `[propext, Classical.choice, Quot.sound]` — no `sorryAx`.

end QOU.BraidKnot.MuPCarrier
