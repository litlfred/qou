import Mathlib.Tactic

/-!
# QOU.MassCore.PairGraphRegime — the combinatorial trichotomy behind `A = 2 / 3–4 / ≥ 5`

Companion to the demoted `conj:mass-formula-regime-switching`
(`folio/quantum-observable-universe/mass-theory/mass-formula-regime-switching.md`).

The demoted block dispatches the binding evaluation on `A` with cut-offs `A ≤ 2`, `3 ≤ A ≤ 4`,
`A ≥ 5`, and the cut-offs were chosen per `A` by closeness to AME (a fit, AGENTS.md §NO FITTING).
This file proves the **only** thing in that dispatch that is mathematics: the three ranges are
exactly the sign/zero pattern of two integers that depend on `A` alone,

* `A.choose 3`              — number of triangles of the complete pair graph `K_A`;
* `A.choose 2 − (3A − 6)`   — complete-graph edges minus triangulated-2-sphere edges (Euler),

through the identity `2·(C(A,2) − (3A − 6)) = (A − 3)(A − 4)`.  Nothing here refers to AME, to a
mass, or to which evaluation formula is used in which range.  Pure ℕ/ℤ arithmetic; no analysis.
-/

namespace QOU.MassCore.PairGraphRegime

/-- `2·C(A,2) = A(A−1)` over `ℤ` (no truncated subtraction). -/
theorem two_mul_choose_two (A : ℕ) : 2 * (A.choose 2 : ℤ) = (A : ℤ) * ((A : ℤ) - 1) := by
  induction A with
  | zero => simp
  | succ n ih =>
    rw [Nat.choose_succ_succ, Nat.choose_one_right]
    push_cast
    linarith [ih]

/-- **Key identity.** `2·(C(A,2) − (3A − 6)) = (A − 3)(A − 4)` over `ℤ`. -/
theorem choose_two_sub_euler (A : ℕ) :
    2 * ((A.choose 2 : ℤ) - (3 * (A : ℤ) - 6)) = ((A : ℤ) - 3) * ((A : ℤ) - 4) := by
  have h := two_mul_choose_two A
  linarith [h]

/-- The complete pair graph `K_A` has a triangle iff `A ≥ 3`. -/
theorem choose_three_eq_zero_iff (A : ℕ) : A.choose 3 = 0 ↔ A < 3 :=
  Nat.choose_eq_zero_iff

/-- For `A ≥ 2`, `3A − 6` (truncated in ℕ) casts to the integer `3A − 6`. -/
theorem cast_euler (A : ℕ) (hA : 2 ≤ A) : ((3 * A - 6 : ℕ) : ℤ) = 3 * (A : ℤ) - 6 := by
  have : 6 ≤ 3 * A := by omega
  push_cast [Nat.cast_sub this]
  ring

/-- `C(A,2) = 3A − 6` for `A ∈ {3, 4}`. -/
theorem choose_two_eq_euler_of (A : ℕ) (h : A = 3 ∨ A = 4) : A.choose 2 = 3 * A - 6 := by
  rcases h with rfl | rfl <;> decide

/-- `C(A,2) > 3A − 6` for `A ≥ 5`. -/
theorem euler_lt_choose_two (A : ℕ) (h : 5 ≤ A) : 3 * A - 6 < A.choose 2 := by
  have hk := choose_two_sub_euler A
  have hc := cast_euler A (by omega)
  have hA : (5 : ℤ) ≤ (A : ℤ) := by exact_mod_cast h
  have hpos : (0 : ℤ) < ((A : ℤ) - 3) * ((A : ℤ) - 4) := by nlinarith
  have : ((3 * A - 6 : ℕ) : ℤ) < (A.choose 2 : ℤ) := by rw [hc]; linarith
  exact_mod_cast this

/-- **Regime trichotomy.** For every `A ≥ 2` exactly the following holds:
  * `A = 2`         and `K_A` has no triangle;
  * `A ∈ {3, 4}`    and `K_A` has a triangle and `C(A,2) = 3A − 6`;
  * `A ≥ 5`         and `K_A` has a triangle and `3A − 6 < C(A,2)`. -/
theorem regime_trichotomy (A : ℕ) (hA : 2 ≤ A) :
    (A = 2 ∧ A.choose 3 = 0) ∨
    ((A = 3 ∨ A = 4) ∧ 0 < A.choose 3 ∧ A.choose 2 = 3 * A - 6) ∨
    (5 ≤ A ∧ 0 < A.choose 3 ∧ 3 * A - 6 < A.choose 2) := by
  rcases (by omega : A = 2 ∨ (A = 3 ∨ A = 4) ∨ 5 ≤ A) with h | h | h
  · left; exact ⟨h, (choose_three_eq_zero_iff A).2 (by omega)⟩
  · right; left
    exact ⟨h, Nat.choose_pos (by omega), choose_two_eq_euler_of A h⟩
  · right; right
    exact ⟨h, Nat.choose_pos (by omega), euler_lt_choose_two A h⟩

/-- The demoted block's cut-offs are the structural predicates (for `A ≥ 2`):
  `A ≤ 2 ↔ C(A,3) = 0`, and `3 ≤ A ≤ 4 ↔ (C(A,3) > 0 ∧ C(A,2) ≤ 3A − 6)`. -/
theorem cutoffs_eq_structural (A : ℕ) (hA : 2 ≤ A) :
    (A ≤ 2 ↔ A.choose 3 = 0) ∧
    ((3 ≤ A ∧ A ≤ 4) ↔ (0 < A.choose 3 ∧ A.choose 2 ≤ 3 * A - 6)) := by
  refine ⟨?_, ?_⟩
  · rw [choose_three_eq_zero_iff]; omega
  · constructor
    · rintro ⟨h3, h4⟩
      refine ⟨Nat.choose_pos h3, ?_⟩
      exact le_of_eq (choose_two_eq_euler_of A (by omega))
    · rintro ⟨hpos, hle⟩
      have h3 : 3 ≤ A := by
        by_contra hlt
        have : A.choose 3 = 0 := (choose_three_eq_zero_iff A).2 (by omega)
        omega
      refine ⟨h3, ?_⟩
      by_contra h5
      have := euler_lt_choose_two A (by omega)
      omega

/-- The corpus's deltahedral max-contact count
(`computations/gap1_max_contact_a5plus.py::max_contacts`). -/
def maxContacts (A : ℕ) : ℕ := if A = 2 then 1 else 3 * A - 6

/-- The deltahedral contact graph is the complete graph `K_A` exactly for `2 ≤ A ≤ 4`. -/
theorem maxContacts_eq_choose_two_iff (A : ℕ) (hA : 2 ≤ A) :
    maxContacts A = A.choose 2 ↔ A ≤ 4 := by
  unfold maxContacts
  constructor
  · intro h
    by_contra h5
    have hlt := euler_lt_choose_two A (by omega)
    rw [if_neg (by omega)] at h
    omega
  · intro h
    rcases (by omega : A = 2 ∨ A = 3 ∨ A = 4) with rfl | rfl | rfl <;> decide

end QOU.MassCore.PairGraphRegime

