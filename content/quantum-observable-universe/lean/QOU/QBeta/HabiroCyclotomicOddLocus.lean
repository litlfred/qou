import QOU.QBeta.HabiroTailAction
import Mathlib.Tactic.Ring

/-!
# The odd-channel Habiro datum lives in the cyclotomic coefficient's bar-asymmetry

A knot's Kashaev/Habiro cyclotomic tail has the general form
  `S_K(q) = Σ_n C_{K,n}(q) · ∏_{j=1}^n (1 - q^j)(1 - q^{-j})`,
with `C_{K,n}` the cyclotomic coefficient (`C_n = 1` for `4_1`; nontrivial and
`q`-dependent for other knots, e.g. the twist knots).  The tail *factor*
`∏ (1 - q^j)(1 - q^{-j})` is bar-even (`habiroFactor_bar_even`,
`QOU.QBeta.HabiroTailAction`).  Therefore the entire bar-odd (`q ↔ q⁻¹`
antisymmetric) content of the tail is carried by the bar-asymmetry of the
coefficient `C_{K,n}` alone:

  `C_n(q)·f_n(q) − C_n(q⁻¹)·f_n(q⁻¹) = (C_n(q) − C_n(q⁻¹))·f_n(q)`.

Consequences, all sorry-free:

* `4_1` has `C_n = 1`, bar-symmetric ⇒ **zero** bar-odd datum (bar-even tail;
  the `π²/5` action is entirely bar-even) — consistent with `4_1` amphichirality
  and the `#3923` odd-phase null.
* For a **chiral** knot with a bar-asymmetric `C_{K,n}(q) ≠ C_{K,n}(q⁻¹)`, the
  bar-odd Habiro datum is nonzero and equals `(C_n(q) − C_n(q⁻¹))` times the
  (bar-even) factor.  So the `Q_β` odd-channel resurgence (b3ix) is located
  precisely in the cyclotomic-coefficient asymmetry — for `5_2` this is the
  Masbaum twist-knot coefficient, the concrete next input.

This is the general structural locator; it does not require the explicit
`5_2` coefficient (which must come from Masbaum's twist-knot formula, not be
invented).
-/

namespace QOU.QBeta.HabiroCyclotomicOddLocus

open QOU.QBeta.HabiroTailAction

/-- **Odd-locus identity.** With a general cyclotomic coefficient `C : ℝ → ℝ`
    (the value `C_{K,n}` as a function of `q`), the bar-odd (`q ↔ q⁻¹`
    antisymmetric) part of the `n`-th Habiro term is exactly the bar-asymmetry
    of the coefficient times the (bar-even) factor:

      `C q · f_j(q) − C q⁻¹ · f_j(q⁻¹) = (C q − C q⁻¹) · f_j(q)`. -/
theorem habiroTerm_bar_odd_eq_coeff_asymmetry (C : ℝ → ℝ) (q : ℝ) (j : ℕ) :
    C q * habiroFactor q j - C q⁻¹ * habiroFactor q⁻¹ j
      = (C q - C q⁻¹) * habiroFactor q j := by
  rw [← habiroFactor_bar_even q j]
  ring

/-- **Bar-symmetric coefficient ⇒ bar-even term.** If `C q = C q⁻¹` (the `4_1`
    case `C = 1` in particular), the `n`-th Habiro term is `q ↔ q⁻¹` invariant:
    no bar-odd datum. -/
theorem habiroTerm_bar_even_of_coeff_symmetric (C : ℝ → ℝ) (q : ℝ) (j : ℕ)
    (hC : C q = C q⁻¹) :
    C q * habiroFactor q j = C q⁻¹ * habiroFactor q⁻¹ j := by
  have h := habiroTerm_bar_odd_eq_coeff_asymmetry C q j
  rw [hC] at h ⊢
  -- h : C q⁻¹ * f q − C q⁻¹ * f q⁻¹ = (C q⁻¹ − C q⁻¹) * f q = 0
  linarith [h]

/-- **`4_1` case: the constant coefficient `C ≡ 1` gives a bar-even term.**
    The `4_1` Habiro tail (`C_n = 1`) carries no bar-odd datum. -/
theorem fourOne_habiroTerm_bar_even (q : ℝ) (j : ℕ) :
    (1 : ℝ) * habiroFactor q j = (1 : ℝ) * habiroFactor q⁻¹ j :=
  habiroTerm_bar_even_of_coeff_symmetric (fun _ => 1) q j rfl

/-! ## Concrete chiral instance: the leading `5_2` cyclotomic coefficient

`C_{5_2,1}(t) = -(t^{-2} + t^{-4})`, extracted self-calibrating from the
validated Jones polynomials as `(V_{5_2}-1)/(V_{4_1}-1)` (an exact Laurent
polynomial, `C_{4_1,1}=1`; probe `qbeta_5two_leading_odd_datum`, det checks
5, 7).  Unlike `4_1`'s `C_n = 1`, it is bar-asymmetric — the first genuine
`5_2` bar-odd datum. -/

/-- Leading `5_2` cyclotomic coefficient `C_{5_2,1}(t) = -(t^{-2} + t^{-4})`. -/
noncomputable def c52_1 (t : ℝ) : ℝ := -((t ^ 2)⁻¹ + (t ^ 4)⁻¹)

/-- **The leading `5_2` bar-odd Habiro term** is the coefficient's bar-asymmetry
    times the (bar-even) factor — the odd-locus, instantiated on the real `5_2`. -/
theorem c52_1_bar_odd_term (t : ℝ) (j : ℕ) :
    c52_1 t * habiroFactor t j - c52_1 t⁻¹ * habiroFactor t⁻¹ j
      = (c52_1 t - c52_1 t⁻¹) * habiroFactor t j :=
  habiroTerm_bar_odd_eq_coeff_asymmetry c52_1 t j

/-- The explicit bar-asymmetry of the leading `5_2` coefficient:
    `C_{5_2,1}(t) - C_{5_2,1}(t^{-1}) = t^4 + t^2 - t^{-2} - t^{-4}` (for `t ≠ 0`),
    a nonzero Laurent polynomial — chirality made explicit. -/
theorem c52_1_asymmetry (t : ℝ) (ht : t ≠ 0) :
    c52_1 t - c52_1 t⁻¹ = t ^ 4 + t ^ 2 - (t ^ 2)⁻¹ - (t ^ 4)⁻¹ := by
  unfold c52_1
  field_simp
  ring

end QOU.QBeta.HabiroCyclotomicOddLocus
