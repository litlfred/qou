/-
Copyright (c) 2026 litlfred. All rights reserved.

# P-C15 — the 4₁ order-2 Casoratian ratio is bar-self-reciprocal

The Lean certificate for probe **P-C15**
(`computations/qbeta/qbeta_pc15_casoratian_bar_parity_probe.py`,
audit `docs/audits/2026-07-03-qbeta-pc15-casoratian-bar-parity.md`).

The newly-landed 4₁ colored-Jones **order-2 qZeilberger operator**
(`computations/aj_figure_eight_certificate.py`, exact) is a candidate for the
Q_β fibre kernel `R(q,ξ)`. With `x := q^N`, its leading/trailing coefficients are
`a₀ = (x−1)(x²q³−1)/x⁶` and `a₂ = (xq²−1)(x²q−1)/x⁶`, so the Casoratian of two
solutions obeys the first-order recurrence (Abel–Heine; see
`QOU.QBeta.casoratian_abel`)

    W_{N+1}/W_N = a₀/a₂ = (q³x³ − q³x² − x + 1) / (q³x³ − q²x − qx² + 1).

For this operator to be a bar-covariant fibre object at all, that ratio must be
bar-even up to a single monomial twist (cf. `QBesselBarCovariance`). This file
proves the sharper fact P-C15 found symbolically: under the **fibre bar
involution** `q ↦ q⁻¹, x ↦ x⁻¹` the numerator and denominator each scale by the
*same* factor `(q³x³)⁻¹`, so the ratio is **exactly invariant** (twist = 1) —
the 4₁ Casoratian ratio is bar-self-reciprocal, hence not excluded as `R(q,ξ)`.

**Scope (honesty).** This certifies the bar-parity *gate* P-C15 clears; it is a
scope-(a) structural positive, **not** a closure and **not** a `c_k` value.
Advancing to the anchor-level Casoratian `W₃/W₂` is gated on a genuine `c₄` rung
(H₄ Hoefsmit `c₄^even`, bean `8we6`); see `StageCSigma3LiftObligation`.

Base ring is a `Field` — the bar involution genuinely inverts the formal fibre
parameters `q, x` (`q ↦ q⁻¹`), so a field is the natural, minimal setting
(CLAUDE.md §7c: inverse-requiring construction; no archimedean structure).
Sorry-free.

`-- Ref:` [garoufalidis2005] https://doi.org/10.2140/gt.2005.9.1253
(Garoufalidis–Lê, the colored-Jones function is q-holonomic — the order-2
recurrence whose Casoratian this file studies).
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

variable {K : Type*} [Field K]

/-- Numerator of the 4₁ order-2 qZeilberger Casoratian ratio `a₀/a₂`
    (with `x = q^N`): `q³x³ − q³x² − x + 1`. -/
def casNum (q x : K) : K := q ^ 3 * x ^ 3 - q ^ 3 * x ^ 2 - x + 1

/-- Denominator of the ratio: `q³x³ − q²x − qx² + 1`. -/
def casDen (q x : K) : K := q ^ 3 * x ^ 3 - q ^ 2 * x - q * x ^ 2 + 1

/-- **Numerator reciprocity.** Under the fibre bar involution `q ↦ q⁻¹, x ↦ x⁻¹`
    the numerator scales by the monomial factor `(q³x³)⁻¹`. -/
theorem casNum_bar (q x : K) (hq : q ≠ 0) (hx : x ≠ 0) :
    casNum q⁻¹ x⁻¹ = casNum q x * (q ^ 3 * x ^ 3)⁻¹ := by
  unfold casNum
  field_simp
  ring

/-- **Denominator reciprocity.** The denominator scales by the *same* factor
    `(q³x³)⁻¹` under `q ↦ q⁻¹, x ↦ x⁻¹` — which is why the twist cancels. -/
theorem casDen_bar (q x : K) (hq : q ≠ 0) (hx : x ≠ 0) :
    casDen q⁻¹ x⁻¹ = casDen q x * (q ^ 3 * x ^ 3)⁻¹ := by
  unfold casDen
  field_simp
  ring

/-- **P-C15 (Lean certificate).** The 4₁ order-2 Casoratian ratio
    `a₀/a₂ = casNum/casDen` is **invariant** (twist = 1) under the fibre bar
    involution `q ↦ q⁻¹, x ↦ x⁻¹`: numerator and denominator both scale by
    `(q³x³)⁻¹`, which cancels. Sorry-free; the bar-parity gate P-C15 clears. -/
theorem casoratian_ratio_bar_self_reciprocal (q x : K) (hq : q ≠ 0) (hx : x ≠ 0) :
    casNum q⁻¹ x⁻¹ / casDen q⁻¹ x⁻¹ = casNum q x / casDen q x := by
  have hs : (q ^ 3 * x ^ 3 : K) ≠ 0 := mul_ne_zero (pow_ne_zero 3 hq) (pow_ne_zero 3 hx)
  rw [casNum_bar q x hq hx, casDen_bar q x hq hx,
      mul_div_mul_right _ _ (inv_ne_zero hs)]

end QOU.QBeta
