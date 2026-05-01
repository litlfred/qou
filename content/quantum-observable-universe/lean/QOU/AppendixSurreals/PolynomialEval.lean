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

/-- **General witness corollary.**  Generalises `polySurrealEval_witness`
    to any real base point `r`: the surreal lift of a polynomial at
    `ofReal r + δ` (any infinitesimal perturbation of any real) is
    infinitesimally close to the classical value `ofReal (p.eval r)`. -/
theorem polySurrealEval_witness_at (p : ℝ[X]) (r : ℝ)
    {δ : K} (hδ : IsInfinitesimal δ) :
    IsInfinitesimal
      (polySurrealEval p (SurrealField.ofReal r + δ)
        - SurrealField.ofReal (p.eval r)) := by
  have hreal : polySurrealEval (K := K) p (SurrealField.ofReal r)
                = SurrealField.ofReal (p.eval r) :=
    polySurrealEval_ofReal p r
  rw [← hreal]
  exact polySurrealEval_isInfinitesimal_diff p
    (ofReal_isFinite (K := K) r) hδ

/-- **Standard-part of a polynomial-in-(real + infinitesimal).**
    The standard-part of the surreal evaluation of a real polynomial
    at any infinitesimal perturbation of a real argument equals the
    classical real value.

    This is the cleanest form of the substrate identity: every
    polynomial substrate function is "stable under infinitesimal
    perturbation" at every real base point. -/
theorem standardPart_polySurrealEval (p : ℝ[X]) (r : ℝ)
    {δ : K} (hδ : IsInfinitesimal δ) :
    standardPart (polySurrealEval (K := K) p
        (SurrealField.ofReal r + δ)) = p.eval r := by
  -- The lift at the perturbed point is finite (it differs from ofReal
  -- (p.eval r) by an infinitesimal, and ofReal is finite).
  have hwitness :
      IsInfinitesimal (polySurrealEval (K := K) p
          (SurrealField.ofReal r + δ)
        - SurrealField.ofReal (p.eval r)) :=
    polySurrealEval_witness_at p r hδ
  have hfin : IsFinite (polySurrealEval (K := K) p
                (SurrealField.ofReal r + δ)) := by
    have hfin_ofReal : IsFinite (SurrealField.ofReal (K := K) (p.eval r)) :=
      ofReal_isFinite _
    have hsum := hfin_ofReal.add hwitness.isFinite
    have heq : SurrealField.ofReal (K := K) (p.eval r)
                + (polySurrealEval (K := K) p
                    (SurrealField.ofReal r + δ)
                  - SurrealField.ofReal (p.eval r))
              = polySurrealEval (K := K) p
                  (SurrealField.ofReal r + δ) := by ring
    rwa [heq] at hsum
  -- Use uniqueness of standard-part decomposition.
  have hspec := standardPart_spec hfin
  exact (isFinite_decomposition hfin).unique hspec hwitness

/-! ### Substrate-evaluation API (`q := 1 + ε`)

Convenience layer wrapping `polySurrealEval` at the substrate
parameter `q := 1 + ε`, which is the canonical perturbation of `1`
used throughout the QOU paper. -/

/-- The **substrate parameter** `q := 1 + ε` viewed as a surreal
    in `K`.  Infinitesimally close to the real number `1`.

    This is the canonical perturbation of `1` that the QOU paper's
    formulas evaluate at; the surreal lift makes the perturbation
    type-stable. -/
noncomputable def substrateQ : K := 1 + epsilonSurreal K

/-- Evaluate a real polynomial at the substrate parameter.  This is
    the master "substrate evaluation" map used by the paper:

      `polySubstrateEval p ≈ p.eval 1` (modulo infinitesimals). -/
noncomputable def polySubstrateEval (p : ℝ[X]) : K :=
  polySurrealEval p (substrateQ K)

/-- The substrate parameter is finite: `1 + ε` differs from `1` by
    an infinitesimal, hence is finite. -/
theorem substrateQ_isFinite : IsFinite (substrateQ (K := K)) := by
  unfold substrateQ
  exact one_isFinite.add (epsilonSurreal_isInfinitesimal K).isFinite

/-- The substrate parameter has standard part `1`. -/
theorem standardPart_substrateQ :
    standardPart (substrateQ (K := K)) = 1 := by
  unfold substrateQ
  -- 1 + ε - ofReal 1 = ε is infinitesimal
  have h1 : (1 : K) = SurrealField.ofReal (K := K) 1 := by rw [map_one]
  have hwit : IsInfinitesimal
      (1 + epsilonSurreal K - SurrealField.ofReal (K := K) 1) := by
    rw [← h1]
    have heq : (1 : K) + epsilonSurreal K - 1 = epsilonSurreal K := by ring
    rw [heq]
    exact epsilonSurreal_isInfinitesimal K
  have hfin : IsFinite (1 + epsilonSurreal K : K) :=
    one_isFinite.add (epsilonSurreal_isInfinitesimal K).isFinite
  exact (isFinite_decomposition hfin).unique
    (standardPart_spec hfin) hwit

/-- **Master substrate-evaluation identity.**  For any real polynomial
    `p`, `standardPart (polySubstrateEval p) = p.eval 1`.

    This is the core "every real prediction is the standard-part of a
    surreal computation" theorem of the QOU framework. -/
theorem standardPart_polySubstrateEval (p : ℝ[X]) :
    standardPart (polySubstrateEval (K := K) p) = p.eval 1 := by
  unfold polySubstrateEval substrateQ
  -- Rewrite 1 = ofReal 1 to apply standardPart_polySurrealEval.
  have h1 : (1 : K) = SurrealField.ofReal (K := K) 1 := by rw [map_one]
  rw [h1]
  exact standardPart_polySurrealEval p 1 (epsilonSurreal_isInfinitesimal K)

/-! ### `HahnSeries`-shaped: polynomial-in-`ε` (finite-support Hahn lift)

The map `p ↦ Σ_n p.coeff n · ε^n`, viewed as the finite-support
restriction of a Hahn-series embedding `HahnSeries ℕ ℝ → K`.

This is a `RingHom` `ℝ[X] →+* K` packaged via `Polynomial.eval₂RingHom`,
giving the canonical "polynomial-as-Hahn-series-in-ε" interpretation of
the substrate. -/

/-- The **polynomial-in-`ε` evaluator** as a ring homomorphism
    `ℝ[X] →+* K`.  Sends `p` to `Σ_n p.coeff n · ε^n`, the canonical
    finite-support Hahn-series presentation of `p` lifted to `K`. -/
noncomputable def polynomialInEpsilon : ℝ[X] →+* K :=
  Polynomial.eval₂RingHom (SurrealField.ofReal (K := K))
    (epsilonSurreal K)

/-- Unfolding: `polynomialInEpsilon p = p.eval₂ ofReal ε`. -/
theorem polynomialInEpsilon_apply (p : ℝ[X]) :
    polynomialInEpsilon (K := K) p
      = polySurrealEval p (epsilonSurreal K) := rfl

/-- **Standard-part of `polynomialInEpsilon p` is the constant term**
    (`p.coeff 0`).  Algebraic content: in the Hahn-series view, the
    standard-part picks out the coefficient at exponent `0`. -/
theorem standardPart_polynomialInEpsilon (p : ℝ[X]) :
    standardPart (polynomialInEpsilon (K := K) p) = p.coeff 0 := by
  rw [polynomialInEpsilon_apply]
  -- ε = ofReal 0 + ε
  have hε : epsilonSurreal K =
      SurrealField.ofReal (K := K) 0 + epsilonSurreal K := by
    rw [map_zero, zero_add]
  rw [hε]
  -- standardPart (polySurrealEval p (ofReal 0 + ε)) = p.eval 0 = p.coeff 0
  rw [standardPart_polySurrealEval p 0 (epsilonSurreal_isInfinitesimal K)]
  exact (Polynomial.coeff_zero_eq_eval_zero p).symm

/-! ### `IsClose`-preservation: surreal evaluation is "continuous"

The polynomial surreal lift sends `IsClose`-equivalent finite
arguments to `IsClose`-equivalent values.  This is the proximity-
relation form of `polySurrealEval_isInfinitesimal_diff` and is the
cleanest "BM-continuous on monads" statement available without a
full topology on `K`. -/

/-- **`polySurrealEval` preserves `IsClose` on finite arguments.**
    If `a` is finite and `IsClose a b`, then `IsClose (polySurrealEval p a)
    (polySurrealEval p b)`.

    Equivalently: every real polynomial extends to a function on `K`
    that is constant on `IsClose`-equivalence classes (modulo the
    finiteness restriction). -/
theorem polySurrealEval_isClose (p : ℝ[X]) {a b : K}
    (ha : IsFinite a) (hab : IsClose a b) :
    IsClose (polySurrealEval p a) (polySurrealEval p b) := by
  -- IsClose a b means a - b is infinitesimal.
  -- Then -(a - b) = b - a is infinitesimal, and b = a + (b - a).
  unfold IsClose at *
  have hδ : IsInfinitesimal (-(a - b)) := hab.neg
  have hb_eq : b = a + -(a - b) := by ring
  rw [hb_eq]
  -- polySurrealEval_isInfinitesimal_diff gives (a + δ) - a infinitesimal;
  -- we want a - (a + δ) infinitesimal, which is the negation.
  have hdiff :=
    polySurrealEval_isInfinitesimal_diff p ha hδ
  have hnegeq : polySurrealEval p a - polySurrealEval p (a + -(a - b))
                = -(polySurrealEval p (a + -(a - b)) - polySurrealEval p a) := by
    ring
  rw [hnegeq]
  exact hdiff.neg

/-- **Substrate parameter `q := 1 + ε` is close to `1`.**  Direct
    consequence of `epsilonSurreal_isInfinitesimal`. -/
theorem substrateQ_isClose_one : IsClose (substrateQ (K := K)) 1 := by
  unfold IsClose substrateQ
  have heq : (1 : K) + epsilonSurreal K - 1 = epsilonSurreal K := by ring
  rw [heq]
  exact epsilonSurreal_isInfinitesimal K

/-- **Polynomial substrate evaluation is close to its archimedean
    value.**  For every real polynomial `p`,
    `polySubstrateEval p` is `IsClose` to `ofReal (p.eval 1)`. -/
theorem polySubstrateEval_isClose_ofReal (p : ℝ[X]) :
    IsClose (polySubstrateEval (K := K) p)
            (SurrealField.ofReal (p.eval 1)) := by
  unfold polySubstrateEval substrateQ
  have h1 : (1 : K) = SurrealField.ofReal (K := K) 1 := by rw [map_one]
  rw [h1]
  unfold IsClose
  exact polySurrealEval_witness_at p 1
    (epsilonSurreal_isInfinitesimal K)

end QOU.AppendixSurreals
