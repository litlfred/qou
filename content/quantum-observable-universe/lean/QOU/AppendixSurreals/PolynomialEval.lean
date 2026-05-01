import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.StandardPart
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Induction

/-!
# QOU.AppendixSurreals.PolynomialEval — surreal evaluation of real polynomials

This module provides the polynomial-evaluation infrastructure that
turns real polynomials into surreal-valued functions:

  `polySurrealEval p x := p.eval₂ SurrealField.ofReal x`

with two key compatibility lemmas:

* `polySurrealEval_ofReal` — agreement with classical evaluation on
  the real subfield (so the surreal lift is **conservative**).
* `polySurrealEval_isInfinitesimal_diff` — the surreal lift sends
  infinitesimal perturbations of finite arguments to infinitesimal
  perturbations of values.

The second lemma is the **automatic-witness lemma** for
`ClassicalLimitIsStandardPart`: it shows that for any polynomial
`f : ℝ[X]`, the polynomial-induced surreal extension `F` satisfies
hypothesis (2) of the conjecture (`F (1 + ε) - ofReal (f 1)`
infinitesimal) **without further assumptions**.

This is a baby Berarducci–Mantova-style theorem: BM-continuity holds
unconditionally for polynomials.  Extending to formal power series
requires the surreal convergence framework (not yet in Mathlib).

LaTeX label: `def:poly-surreal-eval`
-/

namespace QOU.AppendixSurreals

open SurrealField Polynomial

universe u

variable {K : Type u} [SurrealField K]

/-- The **polynomial surreal evaluation map**: lifts a real polynomial
    `p : ℝ[X]` to a function `K → K` via the canonical real-to-surreal
    embedding `ofReal : ℝ →+* K`.

    This is `Polynomial.eval₂` specialized to `ofReal`. -/
-- Ref: [conway1976] §1 (real subfield of `No`); [berarducci2018]
noncomputable def polySurrealEval (p : ℝ[X]) (x : K) : K :=
  p.eval₂ (SurrealField.ofReal (K := K)) x

/-- `polySurrealEval` of the constant polynomial. -/
@[simp]
theorem polySurrealEval_C (c : ℝ) (x : K) :
    polySurrealEval (C c) x = SurrealField.ofReal c := by
  unfold polySurrealEval
  exact Polynomial.eval₂_C _ _

/-- `polySurrealEval` of the indeterminate. -/
@[simp]
theorem polySurrealEval_X (x : K) :
    polySurrealEval (X : ℝ[X]) x = x := by
  unfold polySurrealEval
  exact Polynomial.eval₂_X _ _

/-- `polySurrealEval` is additive in the polynomial. -/
@[simp]
theorem polySurrealEval_add (p q : ℝ[X]) (x : K) :
    polySurrealEval (p + q) x = polySurrealEval p x + polySurrealEval q x := by
  unfold polySurrealEval
  exact Polynomial.eval₂_add _ _

/-- `polySurrealEval` is multiplicative in the polynomial. -/
@[simp]
theorem polySurrealEval_mul (p q : ℝ[X]) (x : K) :
    polySurrealEval (p * q) x = polySurrealEval p x * polySurrealEval q x := by
  unfold polySurrealEval
  exact Polynomial.eval₂_mul _ _

/-- `polySurrealEval` of zero. -/
@[simp]
theorem polySurrealEval_zero (x : K) :
    polySurrealEval (0 : ℝ[X]) x = 0 := by
  unfold polySurrealEval
  exact Polynomial.eval₂_zero _ _

/-- `polySurrealEval` of one. -/
@[simp]
theorem polySurrealEval_one (x : K) :
    polySurrealEval (1 : ℝ[X]) x = 1 := by
  unfold polySurrealEval
  exact Polynomial.eval₂_one _ _

/-! ### Real-compatibility (conservativity) -/

/-- **Real-compatibility.**  On real arguments, the surreal evaluation
    matches the classical evaluation: the diagram

      ℝ[X] × ℝ  ─eval→  ℝ
            │              │
            │              │ ofReal
            ↓              ↓
      ℝ[X] × K  ─polySurrealEval→ K

    commutes. -/
-- Ref: [conway1976] §1
theorem polySurrealEval_ofReal (p : ℝ[X]) (r : ℝ) :
    polySurrealEval p (SurrealField.ofReal (K := K) r) =
      SurrealField.ofReal (p.eval r) := by
  refine Polynomial.induction_on' p ?_ ?_
  · -- additivity
    intro p q hp hq
    simp only [polySurrealEval_add, eval_add, map_add, hp, hq]
  · -- monomials
    intro n c
    simp only [polySurrealEval, eval₂_monomial, eval_monomial, map_mul,
      map_pow]

/-! ### Finite-stability and infinitesimal-stability -/

/-- A finite power of a finite surreal is finite. -/
theorem IsFinite.pow {x : K} (hx : IsFinite x) (n : ℕ) :
    IsFinite (x ^ n) := by
  induction n with
  | zero =>
      simp only [pow_zero]
      refine ⟨1, ?_⟩
      simp
  | succ n ih =>
      rw [pow_succ]
      exact ih.mul hx

/-- The surreal evaluation of a real polynomial at a finite argument
    is finite.  Crucial finiteness lemma for the difference estimate
    below. -/
theorem polySurrealEval_isFinite (p : ℝ[X]) {x : K} (hx : IsFinite x) :
    IsFinite (polySurrealEval p x) := by
  refine Polynomial.induction_on' p ?_ ?_
  · intro p q hp hq
    rw [polySurrealEval_add]
    exact hp.add hq
  · intro n c
    simp only [polySurrealEval, eval₂_monomial]
    exact (ofReal_isFinite (K := K) c).mul (hx.pow n)

/-- **Infinitesimal-stability for powers.**  If `δ` is infinitesimal
    and `a` is finite, then `(a + δ)^n - a^n` is infinitesimal.

    This is the `n`-fold extension of `IsInfinitesimal.mul_finite`
    via the algebraic identity
    `xⁿ⁺¹ - yⁿ⁺¹ = x · (xⁿ - yⁿ) + (x - y) · yⁿ`. -/
theorem isInfinitesimal_pow_diff
    {a δ : K} (ha : IsFinite a) (hδ : IsInfinitesimal δ) (n : ℕ) :
    IsInfinitesimal ((a + δ) ^ n - a ^ n) := by
  induction n with
  | zero =>
      simp only [pow_zero, sub_self]
      exact zero_isInfinitesimal
  | succ n ih =>
      have hd_fin : IsFinite δ := hδ.isFinite
      have ha_plus : IsFinite (a + δ) := ha.add hd_fin
      -- Key identity: (a+δ)^(n+1) - a^(n+1)
      --             = (a+δ) · ((a+δ)^n - a^n) + δ · a^n
      have hidentity :
          (a + δ) ^ (n + 1) - a ^ (n + 1)
            = (a + δ) * ((a + δ) ^ n - a ^ n) + δ * a ^ n := by
        ring
      rw [hidentity]
      have hfirst : IsInfinitesimal ((a + δ) * ((a + δ) ^ n - a ^ n)) := by
        rw [mul_comm]
        exact ih.mul_finite ha_plus
      have hsecond : IsInfinitesimal (δ * a ^ n) :=
        hδ.mul_finite (ha.pow n)
      exact hfirst.add hsecond

/-- **Polynomial infinitesimal-stability** (the main lemma).

    For any polynomial `p : ℝ[X]`, finite `a : K`, and infinitesimal
    `δ : K`, the difference

      `polySurrealEval p (a + δ) - polySurrealEval p a`

    is infinitesimal.  In particular, the surreal evaluation of a real
    polynomial is "BM-continuous at every finite point".

    This is the **automatic-witness lemma** for
    `ClassicalLimitIsStandardPart`: applied with `a := ofReal r` and
    `δ := ε`, it shows that polynomial extensions of real polynomials
    automatically satisfy hypothesis (2) of the conjecture. -/
-- Ref: [berarducci2018] §2
theorem polySurrealEval_isInfinitesimal_diff (p : ℝ[X])
    {a δ : K} (ha : IsFinite a) (hδ : IsInfinitesimal δ) :
    IsInfinitesimal (polySurrealEval p (a + δ) - polySurrealEval p a) := by
  refine Polynomial.induction_on' p ?_ ?_
  · intro p q hp hq
    rw [polySurrealEval_add, polySurrealEval_add]
    have heq : polySurrealEval p (a + δ) + polySurrealEval q (a + δ)
                - (polySurrealEval p a + polySurrealEval q a)
              = (polySurrealEval p (a + δ) - polySurrealEval p a)
                + (polySurrealEval q (a + δ) - polySurrealEval q a) := by
      ring
    rw [heq]
    exact hp.add hq
  · intro n c
    simp only [polySurrealEval, eval₂_monomial]
    have hcoeff_fin : IsFinite (SurrealField.ofReal (K := K) c) :=
      ofReal_isFinite c
    have heq : SurrealField.ofReal (K := K) c * (a + δ) ^ n
                - SurrealField.ofReal c * a ^ n
              = SurrealField.ofReal c * ((a + δ) ^ n - a ^ n) := by
      ring
    rw [heq, mul_comm]
    exact (isInfinitesimal_pow_diff ha hδ n).mul_finite hcoeff_fin

/-! ### Application: automatic witness for `ClassicalLimitIsStandardPart` -/

/-- **Automatic-witness corollary.**  For any real polynomial
    `f : ℝ[X]` and any infinitesimal `δ : K`, the surreal lift
    evaluated at `1 + δ` differs from `ofReal (f.eval 1)` by an
    infinitesimal — i.e., hypothesis (2) of
    `ClassicalLimitIsStandardPart` is automatic for the polynomial
    surreal lift `polySurrealEval f`.

    Combined with the unconditional continuity of polynomials at
    every real point (hypothesis (1) of the conjecture), this gives
    `ClassicalLimitIsStandardPart` for **every polynomial real
    function**, with no further assumptions. -/
theorem polySurrealEval_witness (f : ℝ[X])
    {δ : K} (hδ : IsInfinitesimal δ) :
    IsInfinitesimal
      (polySurrealEval f (1 + δ) - SurrealField.ofReal (f.eval 1)) := by
  -- (1 : K) = ofReal 1
  have h1 : (1 : K) = SurrealField.ofReal (K := K) 1 := by
    rw [map_one]
  -- polySurrealEval f (1 + δ) - ofReal (f.eval 1)
  --   = polySurrealEval f (ofReal 1 + δ) - polySurrealEval f (ofReal 1)
  -- by polySurrealEval_ofReal.
  have hreal : polySurrealEval f (SurrealField.ofReal (K := K) 1)
                = SurrealField.ofReal (f.eval 1) :=
    polySurrealEval_ofReal f 1
  rw [h1, ← hreal]
  exact polySurrealEval_isInfinitesimal_diff f
    (ofReal_isFinite (K := K) 1) hδ

end QOU.AppendixSurreals
