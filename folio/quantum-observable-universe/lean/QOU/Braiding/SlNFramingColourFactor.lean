import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.Algebra.Defs

/-!
# The sl_N framing and the one-gluon colour factors

The Hecke generator `σ`, with eigenvalues `q` on `Sym² V` and `-q⁻¹` on
`Λ² V`, is the **gl_N** braiding. Colour is SU(N), whose braiding is
`q^(-1/N) σ`. This file proves:

* `slExp_sym_eq` / `slExp_anti_eq`: the sl_N exponents `1 - 1/N` and
  `-(1 + 1/N)` are exactly `2 c_R`, where
  `c_R = (C₂(R) - 2 C_F)/2` is the one-gluon colour factor. This uses the
  standard Casimir values `C_F = (N²-1)/(2N)`,
  `C₂(Sym²) = (N-1)(N+2)/N` and `C₂(Λ²) = (N+1)(N-2)/N`.
* `glExp_sym_eq` / `glExp_anti_eq`: the gl_N (Hecke) exponents `±1` are
  `2 c_R + 1/N`. The u₁ part shifts both channels by the same `1/N`.
* `sl_ratio_eq_two_iff`: the channel ratio `(1+1/N)/(1-1/N)` equals `2`
  iff `N = 3`.
* `forced_framing_eq_inv`: if the colour singlet `Λ^N V` must braid
  trivially with `V`, so that `c^(2N) · q² = 1` with `q = x^N`, `x, c > 0`,
  then `c = x⁻¹`, i.e. `c = q^(-1/N)`.

The algebraic identities are stated over a generic field (`§7c`). Only the
forcing lemma needs an ordering, because it picks the positive root.

-- Ref: [kassel1995] Kassel, *Quantum Groups*, ch. VIII (Jimbo R-matrix) and
   ch. XIV (ribbon element `θ_V = q^{C₂(V)}`)
-- Ref: [leitner2026] computations/probes/sl_n_framing_colour_factor_probe.py
-/

namespace QOU.Braiding.SlNFraming

section Generic

variable {K : Type*} [Field K]

/-- Fundamental Casimir `C_F = (N² - 1)/(2N)` (normalisation `T_F = 1/2`). -/
def casimirF (N : K) : K := (N ^ 2 - 1) / (2 * N)

/-- Casimir of `Sym² V`: `(N-1)(N+2)/N`. -/
def casimirSym (N : K) : K := (N - 1) * (N + 2) / N

/-- Casimir of `Λ² V`: `(N+1)(N-2)/N`. -/
def casimirAnti (N : K) : K := (N + 1) * (N - 2) / N

/-- One-gluon-exchange colour factor `(C₂(R) - 2 C_F)/2` on a summand `R`
of `V ⊗ V`. -/
def colourFactor (C₂ N : K) : K := (C₂ - 2 * casimirF N) / 2

/-- The sl_N symmetric exponent `1 - 1/N` is twice the sextet colour factor. -/
theorem slExp_sym_eq (N : K) (hN : N ≠ 0) (h2 : (2 : K) ≠ 0) :
    1 - 1 / N = 2 * colourFactor (casimirSym N) N := by
  unfold colourFactor casimirSym casimirF
  field_simp
  ring

/-- The sl_N antisymmetric exponent `-(1 + 1/N)` is twice the antitriplet
colour factor. -/
theorem slExp_anti_eq (N : K) (hN : N ≠ 0) (h2 : (2 : K) ≠ 0) :
    -(1 + 1 / N) = 2 * colourFactor (casimirAnti N) N := by
  unfold colourFactor casimirAnti casimirF
  field_simp
  ring

/-- The gl_N (Hecke) symmetric exponent `1` is `2 c_sym + 1/N`. -/
theorem glExp_sym_eq (N : K) (hN : N ≠ 0) (h2 : (2 : K) ≠ 0) :
    (1 : K) = 2 * colourFactor (casimirSym N) N + 1 / N := by
  rw [← slExp_sym_eq N hN h2]; ring

/-- The gl_N (Hecke) antisymmetric exponent `-1` is `2 c_anti + 1/N`. -/
theorem glExp_anti_eq (N : K) (hN : N ≠ 0) (h2 : (2 : K) ≠ 0) :
    (-1 : K) = 2 * colourFactor (casimirAnti N) N + 1 / N := by
  rw [← slExp_anti_eq N hN h2]; ring

/-- At `N = 3` the colour factors are `+1/3` (sextet) and `-2/3`
(antitriplet). -/
theorem colourFactor_three (h3 : (3 : K) ≠ 0) (h2 : (2 : K) ≠ 0) :
    colourFactor (casimirSym (3 : K)) 3 = 1 / 3 ∧
      colourFactor (casimirAnti (3 : K)) 3 = -2 / 3 := by
  unfold colourFactor casimirSym casimirAnti casimirF
  constructor <;> (field_simp; ring)

/-- The sl_N channel ratio `(1 + 1/N)/(1 - 1/N)` equals `2` iff `N = 3`
(for `N ≠ 0, 1`). In gl_N the same ratio is `1` for every `N`. -/
theorem sl_ratio_eq_two_iff (N : K) (hN : N ≠ 0) (hN1 : N - 1 ≠ 0) :
    (1 + 1 / N) / (1 - 1 / N) = 2 ↔ N = 3 := by
  have h1 : 1 - 1 / N ≠ 0 := by
    rw [one_sub_div hN]; exact div_ne_zero hN1 hN
  rw [div_eq_iff h1]
  constructor
  · intro h
    field_simp at h
    linear_combination -h
  · rintro rfl
    field_simp
    ring

/-- The sum of the two sl_N log-exponents is `-2/N`, not `0`. The gl_N
cancellation `|det σ| = 1` is the u₁ shift `2 · (1/N)`. -/
theorem sl_exponent_sum (N : K) :
    (1 - 1 / N) + (-(1 + 1 / N)) = -(2 / N) := by ring

/-- Rescaling preserves a quadratic Hecke-type relation: if
`(σ - a)(σ - b) = 0` in an algebra, then `(cσ - ca)(cσ - cb) = 0`.
The sl_N generator `q^(-1/N) σ` therefore satisfies a Hecke relation with
eigenvalues `q^(1-1/N)` and `-q^(-1-1/N)`. -/
theorem rescale_hecke {A : Type*} [Ring A] [Algebra K A] (σ : A) (a b c : K)
    (h : (σ - algebraMap K A a) * (σ - algebraMap K A b) = 0) :
    (c • σ - algebraMap K A (c * a)) * (c • σ - algebraMap K A (c * b)) = 0 := by
  have e1 : c • σ - algebraMap K A (c * a) =
      algebraMap K A c * (σ - algebraMap K A a) := by
    rw [Algebra.smul_def, map_mul, mul_sub]
  have e2 : c • σ - algebraMap K A (c * b) =
      algebraMap K A c * (σ - algebraMap K A b) := by
    rw [Algebra.smul_def, map_mul, mul_sub]
  rw [e1, e2, mul_assoc, ← mul_assoc (σ - algebraMap K A a),
    ← Algebra.commutes c (σ - algebraMap K A a), mul_assoc, h, mul_zero, mul_zero]

end Generic

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Forcing.** With `q = x^N` (`x > 0`) the gl_N monodromy of `V` around
the q-antisymmetric line `Λ^N_q V` is `q² = x^(2N)`. A rescaling `σ ↦ cσ`
multiplies it by `c^(2N)` (2N crossings). Requiring the colour singlet to
braid trivially, `c^(2N) · x^(2N) = 1`, forces the unique positive solution
`c = x⁻¹ = q^(-1/N)`. -/
theorem forced_framing_eq_inv (n : ℕ) (hn : n ≠ 0) (c x : K) (hc : 0 < c)
    (hx : 0 < x) (h : c ^ (2 * n) * (x ^ n) ^ 2 = 1) : c = x⁻¹ := by
  have h' : (c * x) ^ (2 * n) = 1 := by
    rw [mul_pow, ← h]; ring
  have hcx : 0 ≤ c * x := (mul_pos hc hx).le
  have h2n : 2 * n ≠ 0 := by omega
  have : c * x = 1 := (pow_eq_one_iff_of_nonneg hcx h2n).1 h'
  exact eq_inv_of_mul_eq_one_left this

end Ordered

end QOU.Braiding.SlNFraming
