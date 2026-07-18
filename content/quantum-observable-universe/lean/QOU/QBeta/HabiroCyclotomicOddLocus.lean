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

/-! ## Concrete chiral instance: the `5_2` cyclotomic coefficients (Masbaum)

`5_2 = K_2` is the twist knot with two full twists.  Its cyclotomic coefficients
are given AUTHORITATIVELY by Masbaum's twist-knot formula (Theorem 4.5 + 5.1 +
Remark 5.2 of `masbaum2003`, "Skein-theoretical derivation of some formulas of
Habiro", Algebr. Geom. Topol. 3 (2003) 537–556, DOI 10.2140/agt.2003.3.537):
for `p = 2`,
  `c'_{n,2} = (-1)^n a^{(5n²+7n)/2} Σ_{k=0}^n a^{k²-2k-3nk} [n,k]_a`,
  `f̃_{K2,n} = (-1)^n q^{-n(n+1)/2} a^{n(n+3)/2} c'_{n,2}`   (`q = a²`).

**Basis bridge** (derived, verified on `4_1`).  Masbaum's basis is the
color-dependent `(q^{1-N})_n(q^{1+N})_n`, which at the Kashaev point `q^N = 1`
becomes `(q;q)_n²`; the framework's tail basis is the bar-even
`f_n(q) = (q;q)_n (q^{-1};q^{-1})_n`.  Since
`(q^{-1};q^{-1})_n / (q;q)_n = (-1)^n q^{-n(n+1)/2}`, the two bases give the same
tail with `C_{K,n}(q) = (-1)^n q^{n(n+1)/2} · f̃_{K,n}(q)`.  On `4_1 = K_{-1}`,
`f̃_{4_1,n} = (-1)^n q^{-n(n+1)/2}` ⇒ `C_n = 1` (Kashaev's figure-eight), so the
bridge is exact.  This gives the framework coefficients in `q`:
  `C_{5_2,1}(q) = -(q⁴+q²)`,
  `C_{5_2,2}(q) = q¹¹+q⁸+q⁷+q⁵`,
  `C_{5_2,3}(q) = -(q²¹+q¹⁷+q¹⁶+q¹⁵+q¹³+q¹²+q¹¹+q⁹)`.

Below, `t` is the ordinary Jones variable (`t = q^{-1}`, the mirror of the
substrate `q`), so `C_{5_2,n}` is written with `q = t^{-1}`; e.g.
`C_{5_2,1}(t) = -(t^{-2} + t^{-4})`, matching `-(q⁴+q²)` at `t = q^{-1}`.  The
leading `C_{5_2,1}` was first extracted self-calibrating as `(V_{5_2}-1)/
(V_{4_1}-1)`; probe `qbeta_5two_masbaum_cyclotomic` CROSS-CHECKS that the
heuristic equals Masbaum's authoritative value EXACTLY (and that Masbaum
reproduces the standard Jones polynomial `V_{5_2}` at `N = 2`).  Unlike `4_1`'s
`C_n = 1`, every `C_{5_2,n}` (`n ≥ 1`) is bar-asymmetric — the genuine `5_2`
bar-odd data. -/

/-- Leading `5_2` cyclotomic coefficient `C_{5_2,1}(t) = -(t^{-2} + t^{-4})`
    (Masbaum `C_{5_2,1}(q) = -(q⁴+q²)` at `t = q^{-1}`). -/
noncomputable def c52_1 (t : ℝ) : ℝ := -((t ^ 2)⁻¹ + (t ^ 4)⁻¹)

/-- Second `5_2` cyclotomic coefficient `C_{5_2,2}(t) = t^{-5}+t^{-7}+t^{-8}+t^{-11}`
    (Masbaum `C_{5_2,2}(q) = q⁵+q⁷+q⁸+q¹¹` at `t = q^{-1}`). -/
noncomputable def c52_2 (t : ℝ) : ℝ :=
  (t ^ 5)⁻¹ + (t ^ 7)⁻¹ + (t ^ 8)⁻¹ + (t ^ 11)⁻¹

/-- Third `5_2` cyclotomic coefficient
    `C_{5_2,3}(t) = -(t^{-9}+t^{-11}+t^{-12}+t^{-13}+t^{-15}+t^{-16}+t^{-17}+t^{-21})`
    (Masbaum `C_{5_2,3}(q) = -(q⁹+q¹¹+q¹²+q¹³+q¹⁵+q¹⁶+q¹⁷+q²¹)` at `t = q^{-1}`). -/
noncomputable def c52_3 (t : ℝ) : ℝ :=
  -((t ^ 9)⁻¹ + (t ^ 11)⁻¹ + (t ^ 12)⁻¹ + (t ^ 13)⁻¹
    + (t ^ 15)⁻¹ + (t ^ 16)⁻¹ + (t ^ 17)⁻¹ + (t ^ 21)⁻¹)

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

/-- **The second `5_2` bar-odd Habiro term** is the coefficient's bar-asymmetry
    times the (bar-even) factor — the odd-locus on the authoritative Masbaum
    `C_{5_2,2}`. -/
theorem c52_2_bar_odd_term (t : ℝ) (j : ℕ) :
    c52_2 t * habiroFactor t j - c52_2 t⁻¹ * habiroFactor t⁻¹ j
      = (c52_2 t - c52_2 t⁻¹) * habiroFactor t j :=
  habiroTerm_bar_odd_eq_coeff_asymmetry c52_2 t j

/-- **The third `5_2` bar-odd Habiro term** — the odd-locus on the authoritative
    Masbaum `C_{5_2,3}`. -/
theorem c52_3_bar_odd_term (t : ℝ) (j : ℕ) :
    c52_3 t * habiroFactor t j - c52_3 t⁻¹ * habiroFactor t⁻¹ j
      = (c52_3 t - c52_3 t⁻¹) * habiroFactor t j :=
  habiroTerm_bar_odd_eq_coeff_asymmetry c52_3 t j

end QOU.QBeta.HabiroCyclotomicOddLocus
