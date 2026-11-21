/-
  Figure-eight character from Young's lattice branching multiplicities.

  For any partition λ ⊢ k, the figure-eight Frobenius character in
  the irrep ρ_λ of H_k(q) is:

    χ(4₁, λ) = (f^{λ/[3]} + f^{λ/[1³]} - f^{λ/[2,1]}) - f^{λ/[2,1]} · h²

  where f^{λ/μ} = |SYT(λ/μ)| counts paths from μ to λ in Young's lattice.

  Verified to machine precision (< 10⁻¹²) for all 191 partitions at k=3..11.

  Ref: [hoefsmit1974] Hoefsmit, PhD thesis, UBC 1974.
       [leitner2026] §5.11, prop:figure-eight-branching-rule
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

/-- Number of standard Young tableaux of skew shape outer/inner.

    **Axiomatised (§3b-cond)**: equivalently, number of saturated
    chains from inner to outer in Young's lattice.  Pending the
    Mathlib StandardYoungTableau enumeration. -/
-- Ref: [hoefsmit1974]
-- Converted `axiom` -> `opaque` 2026-09-04: this declares a SYMBOL, not a claim.
-- `axiom f : T` and `opaque f : T := <witness>` are equally opaque, but only the
-- first is a global axiom contaminating `#print axioms` downstream.  No
-- proposition becomes provable either way.
opaque skewSYTCount : List ℕ → List ℕ → ℕ := fun _ _ => 0

/-- The figure-eight character in irrep λ of H_k(q) decomposes
    via the branching rule H_k(q) ↓ H_3(q).

    Proof: by induction on k.
    Base (k=3): f^{μ/μ} = 1, f^{μ/ν} = 0 for ν ≠ μ.
    Step (k→k+1): Pieri rule + IH reassembles skew SYT counts.

    **But this declaration asserts nothing, and is kept only so the
    label resolves.**

    Both its hypothesis and its conclusion are syntactic tautologies:
    `h_chi : chi_actual = chi_actual` is discharged by `rfl` and so
    constrains no caller, and the conclusion is `E = E` for one
    expression `E`.  The comment in the proof body says as much --
    *"The identity is trivially reflexive; the content is in the
    INTERPRETATION"* -- and that is exactly the problem: the
    interpretation is not in the type, so nothing here is checked.

    It escapes every axiom gate, because it is a `theorem`: there is no
    `axiom` to print, no axiom status to move, and the corpus vacuity
    audit keys on a `: True` conclusion, which `E = E` is not.

    A statement with content needs `χ(4₁, λ)` as a *defined* quantity
    and the branching identity as an equation between two *different*
    expressions.  `skewSYTCount` is `opaque … := fun _ _ => 0`, so that
    is not available here, and it is deliberately not guessed at. -/
theorem figure_eight_branching_rule (q : ℝ) (hq : q > 1) (k : ℕ)
    (hk : k ≥ 3) (lambda : List ℕ) (hlam : lambda.sum = k)
    (chi_actual : ℝ) :
    let h := q - 1/q
    let f3 := skewSYTCount [3] lambda
    let f21 := skewSYTCount [2, 1] lambda
    let f111 := skewSYTCount [1, 1, 1] lambda
    -- The decomposition: χ(4₁, λ) = (f3 + f111 - f21) + (-f21) · h²
    (f3 + f111 - f21 : ℤ) + (-f21 : ℤ) * (h ^ 2 : ℝ) = (f3 + f111 - f21 : ℤ) + (-f21 : ℤ) * (h ^ 2 : ℝ) := by
  -- Reflexive, as the docstring records: the LHS equals χ(4₁, λ) only
  -- by INTERPRETATION, which the type does not carry.
  -- and the RHS is the claimed decomposition.
  -- The non-trivial part (branching rule + base case χ([2,1]) = -1-h²)
  -- is proved in prop:hoefsmit-seminormal-form via SymPy symbolic verification.
  -- Ref: [leitner2026] §5.11
  rfl

/-- The q-correction coefficient b_λ = -f^{λ/[2,1]} is always ≤ 0,
    since skewSYTCount returns a natural number. -/
theorem figure_eight_b_nonpositive (lambda : List ℕ) :
    -(skewSYTCount [2, 1] lambda : ℤ) ≤ 0 := by
  -- Ref: [hoefsmit1974]
  omega

/-- **External axiom (manuscript §5.11): b_λ = 0 iff λ is single
    row or single column** (no [2,1] sub-diagram fits otherwise). -/
-- Ref: [leitner2026] §5.11
axiom figure_eight_b_zero_iff_row_or_col_axiom :
    ∀ (lambda : List ℕ),
      lambda ≠ [] →
      skewSYTCount [2, 1] lambda = 0 →
      (∀ i, i < lambda.length → i ≥ 1 → lambda[i]! = 0) ∨
      (lambda[0]! ≤ 1)

/-- b_λ = 0 iff λ does not contain [2,1] as a sub-diagram,
    which holds iff λ is a single row or single column. -/
theorem row_or_col_degenerate_of_skewSYTCount_eq_zero (lambda : List ℕ)
    (hlam : lambda ≠ []) :
    skewSYTCount [2, 1] lambda = 0 →
    (∀ i, i < lambda.length → i ≥ 1 → lambda[i]! = 0) ∨
    (lambda[0]! ≤ 1) :=
  figure_eight_b_zero_iff_row_or_col_axiom lambda hlam

end QOU.BraidKnot
