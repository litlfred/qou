import Mathlib.Algebra.BigOperators.NatAntidiagonal
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import QOU.Common.MagicNumbers

/-!
# QOU.ShellCondensation.SelectorPrune

Formalize-first step for `conj:homological-shell-condensation` (bean `qou-6qbv`).

1. **Purity.** For a first-quadrant limit page with finite-dimensional entries
   `E p q`, abutting to `H k = Σ_{p+q=k} dim E p q`, the conjectured vanishing
   `E p q = 0` for all `q > 0` holds iff every `H k` is concentrated in filtration
   degree `k` (`H k = E k 0`). So the conjecture is a purity statement about the
   filtration that the grading induces on cohomology.

2. **No monotone selector.** The magic set `{2, 8, 20, 28, 50, 82, 126}` agrees on
   `0..126` with no predicate that is preserved by `n ↦ n + 1`, and with none
   preserved by `n + 1 ↦ n`. Semisimplicity of `H_n(q)` is such a predicate (it
   fails from the first `n` reaching the order of `q²`, and stays failed), so it
   cannot be what selects the magic numbers.

-- Ref: [leitner2026] conj:homological-shell-condensation
-/

namespace QOU.ShellCondensation.SelectorPrune

open Finset

/-- Total dimension in degree `k` of a first-quadrant page. -/
def total (E : ℕ → ℕ → ℕ) (k : ℕ) : ℕ :=
  ∑ x ∈ antidiagonal k, E x.1 x.2

/-- **Purity.** Vanishing above the `q = 0` row is equivalent to every total
    degree being carried by its top filtration piece. -/
theorem offDiag_vanish_iff_pure (E : ℕ → ℕ → ℕ) :
    (∀ p q, 0 < q → E p q = 0) ↔ ∀ k, total E k = E k 0 := by
  constructor
  · intro h k
    unfold total
    rw [Finset.sum_eq_single (k, 0)]
    · rintro ⟨p, q⟩ hx hne
      rw [mem_antidiagonal] at hx
      have hq : 0 < q := by
        rcases Nat.eq_zero_or_pos q with h0 | h0
        · subst h0; simp at hx; subst hx; exact absurd rfl hne
        · exact h0
      exact h p q hq
    · intro hk; exact absurd (by simp) hk
  · intro h p q hq
    have hk := h (p + q)
    unfold total at hk
    set f : ℕ × ℕ → ℕ := fun x => E x.1 x.2 with hf
    have hmem : (p, q) ∈ antidiagonal (p + q) := by simp
    have hmem0 : (p + q, 0) ∈ antidiagonal (p + q) := by simp
    have hne : (p, q) ≠ (p + q, 0) := by
      intro e; simp [Prod.ext_iff] at e; omega
    have hsplit : f (p + q, 0) + ∑ x ∈ (antidiagonal (p + q)).erase (p + q, 0), f x
        = ∑ x ∈ antidiagonal (p + q), f x :=
      Finset.add_sum_erase _ f hmem0
    have hle : f (p, q) ≤ ∑ x ∈ (antidiagonal (p + q)).erase (p + q, 0), f x :=
      Finset.single_le_sum (fun _ _ => Nat.zero_le _) (Finset.mem_erase.mpr ⟨hne, hmem⟩)
    have hk' : ∑ x ∈ antidiagonal (p + q), f x = f (p + q, 0) := hk
    have : f (p, q) = 0 := by omega
    simpa [hf] using this

open QOU.Common

/-- Saturation at three small values, by direct evaluation of a finite set. -/
theorem sat_two : Saturated 2 := by simp [Saturated, magicSet]
theorem not_sat_three : ¬ Saturated 3 := by simp [Saturated, magicSet]
theorem sat_eight : Saturated 8 := by simp [Saturated, magicSet]

/-- **No upward-closed selector.** -/
theorem not_upward_closed (P : ℕ → Prop) (hup : ∀ n, P n → P (n + 1)) :
    ¬ (∀ n, n ≤ 126 → (P n ↔ Saturated n)) := by
  intro h
  have h2 : P 2 := (h 2 (by omega)).mpr sat_two
  exact not_sat_three ((h 3 (by omega)).mp (hup 2 h2))

/-- **No downward-closed selector.** -/
theorem not_downward_closed (P : ℕ → Prop) (hdown : ∀ n, P (n + 1) → P n) :
    ¬ (∀ n, n ≤ 126 → (P n ↔ Saturated n)) := by
  intro h
  have h8 : P 8 := (h 8 (by omega)).mpr sat_eight
  have h3 : P 3 := hdown 3 (hdown 4 (hdown 5 (hdown 6 (hdown 7 h8))))
  exact not_sat_three ((h 3 (by omega)).mp h3)

end QOU.ShellCondensation.SelectorPrune

