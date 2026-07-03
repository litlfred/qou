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

P-C15 found symbolically that under the **fibre bar involution** `q ↦ q⁻¹, x ↦ x⁻¹`
the numerator and denominator each scale by the *same* factor `(q³x³)⁻¹`, so the
ratio is invariant (twist = 1).

**This is a `CommRing` fact, division-free.** The reciprocity is a polynomial
identity over `ℤ[q,x]`; it needs no field and no inverses — only that `q, x` are
units, witnessed by `q·qi = 1`, `x·xi = 1` (CLAUDE.md §7c: state over the weakest
base ring; the earlier `Field`-only version imposed structure the mathematics does
not use). The invariance of the *ratio* is likewise stated division-free, as the
cross-multiplied identity `casNum qi xi · casDen q x = casNum q x · casDen qi xi`.
A `Field` corollary in literal `a/b` form is derived at the end for convenience.

**Scope (honesty).** This certifies the bar-parity *gate* P-C15 clears; it is a
scope-(a) structural positive, **not** a closure and **not** a `c_k` value.
Advancing to the anchor-level Casoratian `W₃/W₂` is gated on a genuine `c₄` rung
(H₄ Hoefsmit `c₄^even`, bean `8we6`); see `StageCSigma3LiftObligation`.

Sorry-free.

`-- Ref:` [garoufalidis2005] https://doi.org/10.2140/gt.2005.9.1253
(Garoufalidis–Lê, the colored-Jones function is q-holonomic — the order-2
recurrence whose Casoratian this file studies).
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

variable {R : Type*} [CommRing R]

/-- Numerator of the 4₁ order-2 qZeilberger Casoratian ratio `a₀/a₂`
    (with `x = q^N`): `q³x³ − q³x² − x + 1`. Over a generic commutative ring. -/
def casNum (q x : R) : R := q ^ 3 * x ^ 3 - q ^ 3 * x ^ 2 - x + 1

/-- Denominator of the ratio: `q³x³ − q²x − qx² + 1`. -/
def casDen (q x : R) : R := q ^ 3 * x ^ 3 - q ^ 2 * x - q * x ^ 2 + 1

/-- **Numerator reciprocity (division-free, over any `CommRing`).** If `q, x` are
    units — witnessed by `q·qi = 1`, `x·xi = 1` — then the bar-involved numerator,
    scaled by the monomial `q³x³`, returns the numerator:

        casNum qi xi · (q³x³) = casNum q x.

    (Exact `linear_combination` certificate; no field, no `field_simp`.) -/
theorem casNum_reciprocal (q x qi xi : R) (hq : q * qi = 1) (hx : x * xi = 1) :
    casNum qi xi * (q ^ 3 * x ^ 3) = casNum q x := by
  simp only [casNum]
  linear_combination
    (q ^ 2 * qi ^ 2 * x ^ 3 * xi ^ 3 - q ^ 2 * qi ^ 2 * x ^ 3 * xi ^ 2
      + q * qi * x ^ 3 * xi ^ 3 - q * qi * x ^ 3 * xi ^ 2
      + x ^ 3 * xi ^ 3 - x ^ 3 * xi ^ 2) * hq
    + (-q ^ 3 * x ^ 2 + x ^ 2 * xi ^ 2 - x ^ 2 * xi + x * xi - x + 1) * hx

/-- **Denominator reciprocity.** Same monomial factor `q³x³` — which is why the
    twist cancels in the ratio. -/
theorem casDen_reciprocal (q x qi xi : R) (hq : q * qi = 1) (hx : x * xi = 1) :
    casDen qi xi * (q ^ 3 * x ^ 3) = casDen q x := by
  simp only [casDen]
  linear_combination
    (q ^ 2 * qi ^ 2 * x ^ 3 * xi ^ 3 - q ^ 2 * qi * x ^ 3 * xi
      - q ^ 2 * x ^ 3 * xi ^ 2 + q * qi * x ^ 3 * xi ^ 3
      - q * x ^ 3 * xi + x ^ 3 * xi ^ 3) * hq
    + (-q ^ 2 * x ^ 2 * xi - q ^ 2 * x - q * x ^ 2 + x ^ 2 * xi ^ 2 + x * xi + 1) * hx

/-- **P-C15 (Lean certificate, division-free `CommRing` form).** The 4₁ order-2
    Casoratian ratio `a₀/a₂ = casNum/casDen` is **invariant** under the fibre bar
    involution `q ↦ q⁻¹, x ↦ x⁻¹`, expressed without division as the
    cross-multiplied identity

        casNum qi xi · casDen q x = casNum q x · casDen qi xi.

    Both numerator and denominator scale by the *same* monomial `q³x³` under the
    involution (`casNum_reciprocal`, `casDen_reciprocal`), so the shared factor
    cancels. Holds over any commutative ring with `q, x` units. Sorry-free. -/
theorem casoratian_ratio_bar_invariant (q x qi xi : R)
    (hq : q * qi = 1) (hx : x * xi = 1) :
    casNum qi xi * casDen q x = casNum q x * casDen qi xi := by
  have hN := casNum_reciprocal q x qi xi hq hx
  have hD := casDen_reciprocal q x qi xi hq hx
  linear_combination casDen qi xi * hN - casNum qi xi * hD

/-- **`Field` corollary (literal ratio form).** Over a field, with `q, x ≠ 0`, the
    bar-involution `q ↦ q⁻¹, x ↦ x⁻¹` fixes the ratio `casNum/casDen`. Derived from
    the division-free `casoratian_ratio_bar_invariant` above; a convenience
    restatement, not the primary result. -/
theorem casoratian_ratio_bar_self_reciprocal {K : Type*} [Field K]
    (q x : K) (hq : q ≠ 0) (hx : x ≠ 0) (hd : casDen q x ≠ 0)
    (hd' : casDen q⁻¹ x⁻¹ ≠ 0) :
    casNum q⁻¹ x⁻¹ / casDen q⁻¹ x⁻¹ = casNum q x / casDen q x := by
  rw [div_eq_div_iff hd' hd]
  linear_combination casoratian_ratio_bar_invariant q x q⁻¹ x⁻¹
    (mul_inv_cancel₀ hq) (mul_inv_cancel₀ hx)

end QOU.QBeta
