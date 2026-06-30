import Mathlib.Algebra.Order.Group.Nat


/-!
# QOU.HyperellipticQuintic.minimal_z5_classification

Classification theorem: a smooth projective Riemann surface of
minimal genus that is hyperelliptic and carries a faithful Z_5
automorphism commuting with the hyperelliptic involution has genus
2 and is isomorphic to X_5 : y² = x⁵ - 1.

The arithmetic content of the proof (Riemann–Hurwitz + orbit
analysis forces the branch-set size to be 6) is formalised here
as a finite-Diophantine lemma.  The full geometric classification
(isomorphism with `HyperellipticQuintic`) requires a general
`HyperellipticCurve` class which is beyond the current scope.

LaTeX label: `thm:hyperelliptic-z5-classification`

**Ground ring**: `ℕ` (arithmetic core).
-/

namespace QOU.X5Classification

/-- The admissible sizes of a `C_5`-invariant subset of `ℙ¹(ℂ)`:
    non-negative combinations `a·5 + b·1` where `a ≥ 0` counts
    size-5 generic orbits and `b ∈ {0, 1, 2}` counts fixed-point
    contributions (the two fixed points of `x ↦ ζ₅·x` on `ℙ¹`). -/
-- Ref: [bolza1887] Bolza, "On binary sextics with linear transformations into themselves," Amer. J. Math. 10 (1887)
def AdmissibleBranchSize (n : ℕ) : Prop :=
  ∃ a b : ℕ, b ≤ 2 ∧ n = 5 * a + b

/-- **Arithmetic core of the classification**:
    the smallest even integer ≥ 4 that is an admissible `C_5`-invariant
    branch-set size is `6`.  This is the Diophantine content of the
    Riemann–Hurwitz argument forcing minimal genus to `g = 2`.

    LaTeX: `\label{thm:hyperelliptic-z5-classification}`
    Ref: [bolza1887] https://doi.org/10.2307/2369402 -/
theorem minimal_z5_branch_size
    (n : ℕ) (h_adm : AdmissibleBranchSize n)
    (h_even : Even n) (h_min : 4 ≤ n) : 6 ≤ n := by
  -- Ref: [bolza1887] https://doi.org/10.2307/2369402
  -- Cases n ∈ {4, 5}: n=4 not admissible (b ≤ 2 forces 5a + b ≤ 2 or
  -- 5a + b ≥ 5); n=5 not even.
  by_contra hlt
  push_neg at hlt
  interval_cases n
  · -- n = 4: not admissible since b ≤ 2 and 5a + b = 4 has no nat solution
    obtain ⟨a, b, hb, hab⟩ := h_adm
    omega
  · -- n = 5: not even
    obtain ⟨k, hk⟩ := h_even
    omega

end QOU.X5Classification
