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

  Ref: [manuscript] Ch 11 §8 / crossing-graded-mass-expansion
  Ref: [thurston1978] http://library.msri.org/books/gt3m/
-/

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
  -- Ref: [manuscript] Ch 11 §8 / crossing-graded-mass-expansion
  -- The `expansion` field is the conjectural claim; instances must
  -- verify it per atomic-link configuration via explicit GB reduction
  -- and volume computation (SnapPy).

/-! ## Helper: foldl with a constant-update rule -/

/-- For a foldl whose updater ignores the accumulator
    (`fun _ x => f x`), the final value on a non-empty list is
    `f` applied to the list's last element.  Proved by induction
    on the list (peeling off one element at a time). -/
private lemma foldl_const_update_eq_last
    {α β : Type*} (f : α → β) (init : β) :
    ∀ (xs : List α) (h : xs ≠ []),
      xs.foldl (fun _ x => f x) init = f (xs.getLast h)
  | [], h => (h rfl).elim
  | [a], _ => by simp [List.foldl, List.getLast]
  | a :: b :: rest, _ => by
      simp only [List.foldl_cons]
      have htail : (b :: rest) ≠ [] := List.cons_ne_nil _ _
      rw [foldl_const_update_eq_last f (f a) (b :: rest) htail]
      simp [List.getLast]

/-- The reversed range `(List.range (c+1)).reverse = [c, c-1, …, 0]`
    is non-empty and ends at `0`. -/
private lemma reverse_range_succ_getLast (c : ℕ) :
    ((List.range (c + 1)).reverse).getLast
      (by
        intro hcontra
        have : List.range (c + 1) = [] := List.reverse_eq_nil_iff.mp hcontra
        simpa using this)
      = 0 := by
  -- (range (c+1)).reverse = (c) :: (range c).reverse, and the
  -- last element is the last of the original range, namely 0.
  induction c with
  | zero => decide
  | succ n ih =>
    -- (range (n+2)).reverse = (n+1) :: (range (n+1)).reverse
    have step : List.range (n + 2) = List.range (n + 1) ++ [n + 1] := by
      simp [List.range_succ]
    rw [step, List.reverse_append, List.reverse_singleton, List.singleton_append]
    -- LHS is now ((n+1) :: (range (n+1)).reverse).getLast _
    -- which equals (range (n+1)).reverse.getLast (since tail ≠ []).
    have htail : (List.range (n + 1)).reverse ≠ [] := by
      intro hcontra
      have : List.range (n + 1) = [] := List.reverse_eq_nil_iff.mp hcontra
      simpa using this
    rw [List.getLast_cons htail]
    exact ih

/-- Classical-limit recovery: at zero depth, the total mass equals
    the Gröbner-Shirshov mass.  This is the substantive recovery
    statement: at `(depth k).value = 0`, the expansion collapses
    to its `n = 0` term, which by `gbCoeffZero_eq_groebner` is
    the GB mass.

    Proof: substitute `h` into `expansion`; the Horner foldl with
    `acc * 0 + gbCoeff k n = gbCoeff k n` becomes a constant-update
    foldl, so its value on the reversed range is `gbCoeff k`
    applied to the range's last element, which is `0`.

    Ref: [manuscript] Ch 11 §8 / crossing-graded-mass-expansion -/
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
  have rewrite_lambda : ∀ (acc : ℝ) (n : ℕ),
      acc * 0 + CrossingGradedMassExpansion.gbCoeff k n =
        CrossingGradedMassExpansion.gbCoeff k n := by
    intro acc n
    ring
  -- Step 2: foldl with constant updater = update applied to last.
  have nonempty :
      (List.range (CrossingGradedMassExpansion.crossingCount k + 1)).reverse
        ≠ [] := by
    intro hcontra
    have : List.range (CrossingGradedMassExpansion.crossingCount k + 1) = [] :=
      List.reverse_eq_nil_iff.mp hcontra
    simpa using this
  -- Apply the helpers.
  have eq_const : ∀ (init : ℝ),
      (List.range (CrossingGradedMassExpansion.crossingCount k + 1)).reverse.foldl
        (fun acc n => acc * 0 + CrossingGradedMassExpansion.gbCoeff k n) init
      = (List.range (CrossingGradedMassExpansion.crossingCount k + 1)).reverse.foldl
        (fun _ n => CrossingGradedMassExpansion.gbCoeff k n) init := by
    intro init
    apply List.foldl_congr
    intro acc n _
    exact rewrite_lambda acc n
  rw [eq_const]
  rw [foldl_const_update_eq_last (CrossingGradedMassExpansion.gbCoeff k) 0
      _ nonempty]
  rw [reverse_range_succ_getLast]
  exact CrossingGradedMassExpansion.gbCoeffZero_eq_groebner k

end QOU.ParticleInteractions
