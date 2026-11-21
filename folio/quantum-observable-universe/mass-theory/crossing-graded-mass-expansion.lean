/-
  Crossing-graded mass expansion (conjecture).

  For an atomic braid with c crossings, the categorical mass
  endomorphism decomposes as

      m(K; q) = Σ_{n=0}^{c} ξ(q)^n · m^{(n)}_GB(K)

  where ξ(q) = D(z_q) / ℏ_q² is the universal depth scalar and
  m^{(n)}_GB is the Gröbner-Shirshov normal form restricted to
  subsets of n "lifted" crossings.  The n = 0 term reproduces
  the existing GB mass.

  This is axiomatized as a class; instances encode the expansion
  for a given atomic-link configuration.  The coefficient fields
  are the conjectural content.

  Ref: [leitner2026] Ch 11 §8 / crossing-graded-mass-expansion
  Ref: [thurston1978] http://library.msri.org/books/gt3m/
-/

import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

namespace QOU.ParticleInteractions

/-- Per-crossing universal depth scalar.  In the paper,
    ξ(q) = D(λ(ℰ_q)) / ℏ_q², where D is the Bloch-Wigner
    dilogarithm and λ the Legendre invariant of the Descartes
    elliptic curve.  Here kept abstract. -/
structure DepthScalar where
  value : ℝ

/-- **Crossing-graded mass expansion** (conjectural class).
    Packages the claim that the categorical mass of an atomic
    link has the perturbative expansion indexed by subsets of
    lifted crossings. -/
class CrossingGradedMassExpansion (K : Type*) where
  crossingCount : K → Nat
  depth         : K → DepthScalar
  gbCoeff       : K → Nat → ℝ              -- m^{(n)}_GB
  mass          : K → ℝ
  /-- The standard Gröbner-Shirshov mass — an independent datum
      provided per instance, used to anchor the `n = 0` term. -/
  groebnerMass  : K → ℝ
  /-- At `n = 0`, the graded coefficient IS the Gröbner-Shirshov
      mass (definitional; connects the abstract grading to the
      existing GB pipeline). -/
  gbCoeffZero_eq_groebner : ∀ k : K, gbCoeff k 0 = groebnerMass k
  /-- Horner-form expansion: evaluates the depth polynomial in
      O(c) multiplications, numerically more stable than the
      naive power-based sum. -/
  expansion :
    ∀ k : K,
      mass k =
        (List.range (crossingCount k + 1)).reverse.foldl
          (fun acc n => acc * (depth k).value + gbCoeff k n) 0
  -- Ref: [thurston1978] http://library.msri.org/books/gt3m/
  -- Ref: [leitner2026] Ch 11 §8 / crossing-graded-mass-expansion
  -- The `expansion` field is the conjectural claim; instances must
  -- verify it per atomic-link configuration via explicit GB reduction
  -- and volume computation (SnapPy).

/-! ## Helper: foldl with a constant-update rule -/

/-- For a foldl whose updater ignores the accumulator
    (`fun _ x => f x`), the final value on a non-empty list is
    `f` applied to the list's last element.  Proved by induction
    on the list (peeling off one element at a time). -/
private lemma foldl_const_update_eq_last
    {α β : Type*} (f : α → β) :
    ∀ (xs : List α) (init : β) (h : xs ≠ []),
      xs.foldl (fun _ x => f x) init = f (xs.getLast h)
  | [], _, h => (h rfl).elim
  | [a], _, _ => by simp
  | a :: b :: rest, init, _ => by
      rw [List.foldl_cons]
      have htail : (b :: rest) ≠ [] := List.cons_ne_nil _ _
      rw [foldl_const_update_eq_last f (b :: rest) (f a) htail]
      rw [List.getLast_cons htail]

/-- The reversed range `(List.range (c+1)).reverse = [c, c-1, …, 0]`
    is non-empty and ends at `0`. -/
private lemma reverse_range_succ_getLast (c : ℕ) :
    ((List.range (c + 1)).reverse).getLast
      (by
        intro hcontra
        have : List.range (c + 1) = [] := List.reverse_eq_nil_iff.mp hcontra
        simp at this)
      = 0 := by
  -- The last element of `(range (c+1)).reverse` is the head of
  -- `range (c+1)`, which is `0`.  Phrasing the goal through
  -- `getLast?`/`head?` avoids a dependent-proof `rw` motive issue.
  rw [List.getLast_eq_iff_getLast?_eq_some, List.getLast?_reverse,
      List.head?_range]
  simp

/-- Classical-limit recovery: at zero depth, the total mass equals
    the Gröbner-Shirshov mass.  This is the substantive recovery
    statement: at `(depth k).value = 0`, the expansion collapses
    to its `n = 0` term, which by `gbCoeffZero_eq_groebner` is
    the GB mass.

    Proof: substitute `h` into `expansion`; the Horner foldl with
    `acc * 0 + gbCoeff k n = gbCoeff k n` becomes a constant-update
    foldl, so its value on the reversed range is `gbCoeff k`
    applied to the range's last element, which is `0`.

    Ref: [leitner2026] Ch 11 §8 / crossing-graded-mass-expansion -/
theorem mass_at_zero_depth
    {K : Type*} [CrossingGradedMassExpansion K]
    (k : K) (h : (CrossingGradedMassExpansion.depth k).value = 0) :
    CrossingGradedMassExpansion.mass k
      = CrossingGradedMassExpansion.groebnerMass k := by
  rw [CrossingGradedMassExpansion.expansion, h]
  -- Goal: (List.range (c+1)).reverse.foldl
  --         (fun acc n => acc * 0 + gbCoeff k n) 0
  --       = groebnerMass k
  -- Step 1: rewrite the lambda to drop the accumulator.
  -- Step 1: the Horner update collapses to a constant update
  -- (`acc * 0 + gbCoeff k n = gbCoeff k n`), so replace the update
  -- function with the accumulator-ignoring one.
  have rewrite_lambda :
      (fun (acc : ℝ) (n : ℕ) =>
          acc * 0 + CrossingGradedMassExpansion.gbCoeff k n)
        = (fun (_ : ℝ) (n : ℕ) => CrossingGradedMassExpansion.gbCoeff k n) := by
    funext acc n
    ring
  rw [rewrite_lambda]
  -- Step 2: foldl with the constant updater = update applied to last.
  have nonempty :
      (List.range (CrossingGradedMassExpansion.crossingCount k + 1)).reverse
        ≠ [] := by
    intro hcontra
    have : List.range (CrossingGradedMassExpansion.crossingCount k + 1) = [] :=
      List.reverse_eq_nil_iff.mp hcontra
    simp at this
  rw [foldl_const_update_eq_last (CrossingGradedMassExpansion.gbCoeff k)
      _ 0 nonempty]
  rw [reverse_range_succ_getLast]
  exact CrossingGradedMassExpansion.gbCoeffZero_eq_groebner k

/-! ## Classical-limit (`q → 1`) analysis of the Descartes cubic and `ξ(q)` (`qou-s39m`)

At `q = 1` (`ℏ_q = 1 − 1/q = 0`), the Descartes cubic `27x³ + 18x + 20` factors
over `ℚ` as `(3x + 2)(9x² − 6x + 10)` with `9x² − 6x + 10 = (3x − 1)² + 9`.
Thus its roots are `x₀ = −2/3` and `x_{1,2} = 1/3 ∓ i`, whose cross-ratio shape
parameter is `z₁ = ((1/3 + i) − (−2/3)) / ((1/3 − i) − (−2/3)) = (1 + i)/(1 − i) = i`,
the regular ideal octahedron shape with Bloch–Wigner volume `D(z₁) = G > 0`.

Consequently:
* Under the quotient definition `ξ_div(D, ℏ) = D / ℏ²`, `ξ_div · ℏ² = D` for
  `ℏ ≠ 0`, so a non-zero limiting dilogarithm `D₁ ≠ 0` is incompatible with
  `ξ_div = 0`.
* Under the product reading (R2) `ξ_mul(D, ℏ) = D · ℏ²`, `ξ_mul(D₁, 0) = 0` at
  `ℏ = 0`, which feeds directly into `mass_at_zero_depth` above. -/

/-- **Exact rational factorization of the Descartes cubic at `q = 1` (`qou-s39m`).** -/
theorem descartes_cubic_at_q_one_factorization (x : ℝ) :
    27 * x ^ 3 + 18 * x + 20 = (3 * x + 2) * (9 * x ^ 2 - 6 * x + 10) := by
  ring

/-- **Completed-square decomposition of the quadratic factor at `q = 1` (`qou-s39m`).**
Shows `9x² − 6x + 10 = (3x − 1)² + 3²`, pinning the conjugate root pair at
real part `1/3` and imaginary part `±1`. -/
theorem descartes_quadratic_factor_complete_sq (x : ℝ) :
    9 * x ^ 2 - 6 * x + 10 = (3 * x - 1) ^ 2 + 9 := by
  ring

/-- **Real root `x₀ = −2/3` of the Descartes cubic at `q = 1` (`qou-s39m`).** -/
theorem descartes_cubic_eval_neg_two_thirds :
    27 * (-2 / 3 : ℝ) ^ 3 + 18 * (-2 / 3 : ℝ) + 20 = 0 := by
  ring

/-- **Cross-ratio identity `(1 + i) = i · (1 − i)` at `q = 1` in `(Re, Im)` coordinates (`qou-s39m`).**
For `x₂ − x₀ = (1/3 + 2/3) + i = 1 + i` and `x₁ − x₀ = (1/3 + 2/3) − i = 1 − i`,
multiplying `1 − i` by `z₁ = 0 + 1·i` produces `1 + i`, certifying `z₁ = i`. -/
theorem descartes_cross_ratio_eq_I_coords :
    ((1 : ℝ) / 3 - (-2 / 3 : ℝ) = 0 * 1 - 1 * (-1))
      ∧ ((1 : ℝ) = 0 * (-1) + 1 * 1) := by
  constructor <;> ring

/-- **Product reading (R2) vanishes at `ℏ_q = 0` (`qou-s39m`).** -/
theorem xi_product_at_zero_hbar (D₁ : ℝ) :
    D₁ * (0 : ℝ) ^ 2 = 0 := by
  ring

/-- **Cleared-denominator obstruction for the quotient formula (`qou-s39m`).**
Whenever `ξ · ℏ² = D₁` and `D₁ ≠ 0`, `ξ` cannot vanish (`ξ ≠ 0`). -/
theorem xi_ne_zero_of_mul_hbar_sq_eq {xi hbar D₁ : ℝ}
    (hrel : xi * hbar ^ 2 = D₁) (hD : D₁ ≠ 0) :
    xi ≠ 0 := by
  intro hxi
  apply hD
  rw [← hrel, hxi]
  ring

end QOU.ParticleInteractions
