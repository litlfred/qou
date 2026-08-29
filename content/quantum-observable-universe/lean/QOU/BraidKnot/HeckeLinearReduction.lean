/-
# Linear reduction in a single Hecke generator, and the sym/alt ratio quantum

Two facts that were used numerically before they were proved.

`hecke_linear_mul` is the algebra behind the `per_generator_V_hat_3A`
rewrite (`23b9c4f5ba`, merged in #5622): a product of factors
`c • sigma + d` in the SAME generator collapses to `alpha • sigma + beta`
by a scalar recursion, so no matrix product is needed. That change landed on
numerical agreement (9.107e-16 over 171 fields); this is the proof it rested on.

`symAltRatio_*` explain the integer quantisation of the chirality invariant
`Phi_3 = sum_i log |lambda_sym_i / lambda_alt_i|`. Each chain factor's ratio is
`-q^2`, `-q^(-2)` or `-1`, so the exponent moves in steps of two and
`Phi_3 / log q` is an EVEN integer. Measured before it was proved: 6 and 2 for
the two nucleon chains, and 4, 6, 6, 12, 12 for H-1, D, T, 3He, 4He. All even.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot

/-! ## Linear reduction in one generator -/

/-- Two elements linear in the same Hecke generator multiply to a linear
element, with the coefficients given by an explicit scalar recursion.

`s` is the generator, subject only to the Hecke quadratic relation
`s^2 = delta * s + 1` (with `delta = q - q⁻¹` in the intended reading).
Stated over a generic `CommRing`: no ordering, no square root, nothing
archimedean is used, per the §7c base-ring convention. -/
theorem hecke_linear_mul {R : Type*} [CommRing R] (s delta a b c d : R)
    (hs : s ^ 2 = delta * s + 1) :
    (a * s + b) * (c * s + d)
      = (a * c * delta + a * d + b * c) * s + (a * c + b * d) := by
  have expand : (a * s + b) * (c * s + d)
      = a * c * s ^ 2 + (a * d + b * c) * s + b * d := by ring
  rw [expand, hs]; ring

/-- The recursion is exactly the one the compute uses: folding a chain factor
`(c, d)` onto an accumulated `(a, b)` sends it to
`(a*c*delta + a*d + b*c, a*c + b*d)`. Starting from the identity `(0, 1)`
reproduces the factor itself, which is the base case of that fold. -/
theorem hecke_linear_mul_id {R : Type*} [CommRing R] (s delta c d : R)
    (hs : s ^ 2 = delta * s + 1) :
    ((0 : R) * s + 1) * (c * s + d)
      = (0 * c * delta + 0 * d + 1 * c) * s + (0 * c + 1 * d) :=
  hecke_linear_mul s delta 0 1 c d hs

/-! ## The sym/alt ratio is a power of `q^2`, up to sign

On a chain factor `c • sigma + d`, the one-dimensional symmetric rep sends
`sigma ↦ q` and the alternating rep sends `sigma ↦ -q⁻¹`. The three factor
shapes occurring in the atomic chains are `d = 0`, `d = -h` and `d = -h/2`,
with `h = q - q⁻¹`.

The `d = -h/2` case needs `q^2 + 1 ≠ 0` as a hypothesis. It is NOT provable
without one: over a field with `q^2 = -1` the denominator `-(q + q⁻¹)/2`
vanishes and the ratio is undefined. Carried as an explicit hypothesis rather
than specialised to `ℝ`, per the §7c base-ring convention — the substrate
reading has `q` real and `> 1`, where it holds, but nothing here needs the
ordering. -/

variable {K : Type*} [Field K]

/-- `d = 0`: the ratio is `-q^2`. -/
theorem symAltRatio_zero (q : K) (hq : q ≠ 0) :
    (1 * q + 0) / (-(1 / q) + 0) = -q ^ 2 := by
  field_simp
  ring

/-- `d = -h` with `h = q - q⁻¹`: the ratio is `-q⁻²`.

Both sides simplify first: `q - h = q⁻¹` and `-q⁻¹ - h = -q`. -/
theorem symAltRatio_full (q : K) (hq : q ≠ 0) :
    (1 * q + -(q - 1 / q)) / (-(1 / q) + -(q - 1 / q)) = -(1 / q ^ 2) := by
  have hn : (1 * q + -(q - 1 / q)) = 1 / q := by ring
  have hd : (-(1 / q) + -(q - 1 / q)) = -q := by ring
  rw [hn, hd, div_neg]
  congr 1
  field_simp

/-- `d = -h/2`: the ratio is `-1`, because numerator and denominator differ
only by sign — `q - h/2 = (q + q⁻¹)/2` and `-q⁻¹ - h/2 = -(q + q⁻¹)/2`.

This is the factor carrying NO chirality: it contributes `0` to `Phi_3`, which
is why the two `(1, -h/2)` factors present in every chain drop out of the count.

Needs BOTH hypotheses, and neither is removable:
* `(2 : K) ≠ 0` — in characteristic two `2⁻¹ = 0` and the halving identity
  `q - h/2 = (q + q⁻¹)/2` is simply false;
* `q ^ 2 + 1 ≠ 0` — where `q ^ 2 = -1` the denominator vanishes and the ratio
  is undefined.
Both hold in the substrate reading (`q` real, `q > 1`), but the ordering is not
what makes them true, so they are carried as hypotheses rather than by
specialising to `ℝ` — §7c. -/
theorem symAltRatio_half (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0)
    (hq1 : q ^ 2 + 1 ≠ 0) :
    (1 * q + -((q - 1 / q) / 2)) / (-(1 / q) + -((q - 1 / q) / 2)) = -1 := by
  have hn : (1 * q + -((q - 1 / q) / 2)) = (q + 1 / q) / 2 := by
    field_simp
    ring
  have hd : (-(1 / q) + -((q - 1 / q) / 2)) = -((q + 1 / q) / 2) := by
    field_simp
    ring
  have key : q + 1 / q = (q ^ 2 + 1) / q := by
    field_simp
  have hsum : q + 1 / q ≠ 0 := by
    rw [key]; exact div_ne_zero hq1 hq
  have hX : (q + 1 / q) / 2 ≠ 0 := div_ne_zero hsum h2
  rw [hn, hd, div_neg, div_self hX]

end QOU.BraidKnot
