/-
# The convolution flow `σ^t` and the parity of feasible bridge letters

Owner, 2026-10-12: "flow by the knot convolution operator" (bean `qou-jfx8`, after the ruling that
strands follow the fibre Reeb flow). The bridge letter `σ` satisfies `(σ − q)(σ + q⁻¹) = 0`, so it
splits into the two fundamental channels with projectors

    P_S = (σ + q⁻¹)/(q + q⁻¹),   P_A = (q − σ)/(q + q⁻¹),

and its powers are `σ^m = q^m P_S + (−q⁻¹)^m P_A`. Continued to real `t`, this is the flow
`σ^t = q^t P_S + q^{−t} e^{± iπ t} P_A`: on the Alt channel each crossing is a rotation by `π`, and
`σ²` (the full twist) is one full turn. The branch `±` is a chirality choice; the real part,
`q^{−t} cos(π t)`, is branch-independent.

Proved here (scalar form; the operator form follows because `σ` is semisimple with these two
eigenvalues, and is checked numerically to 1e-60 in `convolution_flow_parity_probe.py`):

* `pow_interp_at_q`, `pow_interp_at_neg_inv`: `x^m = q^m p_S(x) + (−q⁻¹)^m p_A(x)` at both
  eigenvalues;
* `odd_power_negative_iff` (odd `m`, `q > 0`): `q^m a_S + (−q⁻¹)^m a_A < 0 ⇔ q^{2m} a_S < a_A`;
* `even_power_nonneg`: for even `m` and `a_S, a_A ≥ 0` the character is `≥ 0`.

**Consequence for the A = 2 composition program** (scope (a)): the earlier finding "every odd power
fails on (5,1)" was measured for `|m| ≤ 3` only. With `a_S = χ_(5,1)(W P_S) = 0.02179…` and
`a_A = 0.70043…`, an odd power fails iff `q^{2m} < a_A/a_S ≈ 32.1`, i.e. for odd `m ≤ 15`, and odd
`m ≥ 17` is feasible. The parity is the `cos(π t)` of the convolution flow, and it wins only until
the Sym channel's growth `q^{2m}` overtakes the Alt/Sym weight ratio.

§7c: generic ordered field for the sign lemmas; generic field for the interpolation.

-- Ref: [manuscript] bean qou-jfx8, qou-8r6b; composition_feasibility_a2_probe.py (the |m| ≤ 3 scan).
-/
import Mathlib.Tactic

namespace QOU.MassTheory.ConvolutionFlow

section Interp

variable {K : Type*} [Field K]

/-- `p_S(x) = (x + q⁻¹)/(q + q⁻¹)`. -/
def pS (q x : K) : K := (x + q⁻¹) / (q + q⁻¹)
/-- `p_A(x) = (q − x)/(q + q⁻¹)`. -/
def pA (q x : K) : K := (q - x) / (q + q⁻¹)

theorem pow_interp_at_q (q : K) (hq2 : q + q⁻¹ ≠ 0) (m : ℕ) :
    q ^ m = q ^ m * pS q q + (-q⁻¹) ^ m * pA q q := by
  unfold pS pA; rw [div_self hq2]; simp

theorem pow_interp_at_neg_inv (q : K) (hq2 : q + q⁻¹ ≠ 0) (m : ℕ) :
    (-q⁻¹) ^ m = q ^ m * pS q (-q⁻¹) + (-q⁻¹) ^ m * pA q (-q⁻¹) := by
  unfold pS pA
  rw [show q - -q⁻¹ = q + q⁻¹ by ring, div_self hq2]; simp

end Interp

section Signs

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Odd powers**: the character is negative iff the Sym growth has not yet overtaken the
Alt/Sym ratio. -/
theorem odd_power_negative_iff (q aS aA : K) (hq : 0 < q) (k : ℕ) :
    q ^ (2 * k + 1) * aS + (-q⁻¹) ^ (2 * k + 1) * aA < 0 ↔
      q ^ (2 * (2 * k + 1)) * aS < aA := by
  have hp : 0 < q ^ (2 * k + 1) := pow_pos hq _
  have hneg : (-q⁻¹) ^ (2 * k + 1) = -(q ^ (2 * k + 1))⁻¹ := by
    rw [Odd.neg_pow ⟨k, rfl⟩, inv_pow]
  rw [hneg, show q ^ (2 * (2 * k + 1)) = q ^ (2 * k + 1) * q ^ (2 * k + 1) by ring]
  set p := q ^ (2 * k + 1) with hpdef
  have key : p * (p * aS + -p⁻¹ * aA) = p * p * aS - aA := by
    field_simp
    ring
  constructor
  · intro h
    have := mul_neg_of_pos_of_neg hp h
    rw [key] at this
    linarith
  · intro h
    have h2 : p * (p * aS + -p⁻¹ * aA) < 0 := by rw [key]; linarith
    exact neg_of_mul_neg_right h2 hp.le

/-- **Even powers** are nonnegative when both channel weights are. -/
theorem even_power_nonneg (q aS aA : K) (haS : 0 ≤ aS) (haA : 0 ≤ aA) (k : ℕ) :
    0 ≤ q ^ (2 * k) * aS + (-q⁻¹) ^ (2 * k) * aA := by
  rw [pow_mul, pow_mul, neg_sq]
  exact add_nonneg (mul_nonneg (pow_nonneg (sq_nonneg _) _) haS)
    (mul_nonneg (pow_nonneg (sq_nonneg _) _) haA)

end Signs

end QOU.MassTheory.ConvolutionFlow
