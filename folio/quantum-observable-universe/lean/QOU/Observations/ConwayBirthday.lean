/-
  What Conway's two missing axioms buy: lower bounds on the birthday.

  Owner ruling 2026-11-27 ("Split into base + Conway class"; Carl: "Strengthen what you
  can in the surreals").  Beans `qou-6qbv` (`bday`) and `qou-3kkl` (`hypr`).

  `BirthdayField`'s six axioms bound the birthday from above only, so no lower bound
  follows from them: the flat `ℝ*` birthday (`HyperrealTransfer.surrealFieldHyperreal`)
  is `≤ 1` everywhere.  `SurrealField` adds `birthday_natCast` and Conway simplicity.
  This module proves the lower bounds those two give, none of which hold for the flat
  model:

  * `birthday_eq_zero_iff` — only `0` is born on day `0`;
  * `birthday_eq_one_iff` — only `±1` are born on day `1`;
  * `abs_le_natCast_of_birthday_le` — a number born by day `n` has `|x| ≤ n`;
  * `isFinite_of_birthday_lt_omega` — a number of finite birthday is finite;
  * `omega0_le_birthday_of_not_isFinite` — an infinite number is born on day `ω` or later;
  * `omega0_le_birthday_omegaSurreal` — in particular `ω` itself;
  * `exists_older_separating` — two distinct numbers born on the same day are separated
    by an older number.

  All are exact algebra on the axioms; no measured value enters.

  -- Ref: [conway1976] Ch. 2, Theorem 11 (simplicity)
  -- Ref: [gonshor1986] Ch. 2
-/
import QOU.Observations.Basic

namespace QOU.AppendixSurreals

open SurrealField

universe u

namespace SurrealField

variable {K : Type u} [SurrealField K]

/-- **Only `0` is born on day `0`.**  Simplicity at `x = 0` has a vacuous hypothesis
(nothing is older than day `0`), so every `z ≠ 0` is born strictly after `0`. -/
theorem birthday_pos_of_ne_zero {z : K} (hz : z ≠ 0) : 0 < birthday z := by
  have h := SurrealField.simplicity (0 : K) z (fun h => hz h.symm) (by
    intro y hy
    rw [birthday_zero] at hy
    exact absurd hy (Ordinal.not_lt_zero _))
  rwa [birthday_zero] at h

theorem birthday_eq_zero_iff {z : K} : birthday z = 0 ↔ z = 0 := by
  refine ⟨fun h => ?_, fun h => h ▸ birthday_zero⟩
  by_contra hz
  have := birthday_pos_of_ne_zero hz
  rw [h] at this
  exact lt_irrefl _ this

/-- A positive `z ≠ 1` is born after day `1`: the only older number is `0`, which lies
below both `1` and `z`. -/
theorem one_lt_birthday_of_pos {z : K} (hz : 0 < z) (h1 : z ≠ 1) : 1 < birthday z := by
  have h := SurrealField.simplicity (1 : K) z (fun h => h1 h.symm) (by
    intro y hy
    rw [birthday_one, Ordinal.lt_one_iff_zero, birthday_eq_zero_iff] at hy
    subst hy
    exact ⟨fun _ => hz, fun _ => one_pos⟩)
  rwa [birthday_one] at h

/-- **Only `±1` are born on day `1`.** -/
theorem birthday_eq_one_iff {z : K} : birthday z = 1 ↔ z = 1 ∨ z = -1 := by
  constructor
  · intro h
    rcases lt_trichotomy z 0 with hz | hz | hz
    · right
      by_contra hne
      have hpos : 0 < -z := neg_pos.mpr hz
      have hne' : -z ≠ 1 := fun e => hne (by rw [← e, neg_neg])
      have := one_lt_birthday_of_pos hpos hne'
      rw [birthday_neg, h] at this
      exact lt_irrefl _ this
    · subst hz
      rw [birthday_zero] at h
      exact absurd h zero_ne_one
    · left
      by_contra hne
      have := one_lt_birthday_of_pos hz hne
      rw [h] at this
      exact lt_irrefl _ this
  · rintro (rfl | rfl)
    · exact birthday_one
    · rw [birthday_neg, birthday_one]

/-- **A number born by day `n` is at most `n`.**  Induction on `n`.  For the step, a
`y > n + 1` would have every number older than `n + 1` (each `≤ n` by induction) below
both `n + 1` and `y`, so simplicity puts `y` after day `n + 1`. -/
theorem le_natCast_of_birthday_le : ∀ (n : ℕ) {y : K}, birthday y ≤ n → y ≤ n
  | 0, y, h => by
      have h0 : birthday y = 0 := le_antisymm (by simpa using h) (zero_le _)
      rw [birthday_eq_zero_iff.mp h0]
      simp
  | n + 1, y, h => by
      by_contra hy
      push_neg at hy
      have hn : ((n : ℕ) : K) < ((n + 1 : ℕ) : K) := by exact_mod_cast Nat.lt_succ_self n
      have key := SurrealField.simplicity (((n + 1 : ℕ)) : K) y (ne_of_lt hy) (by
        intro w hw
        rw [SurrealField.birthday_natCast, Nat.cast_succ, Ordinal.add_one_eq_succ,
          Order.lt_succ_iff] at hw
        have hwn := le_natCast_of_birthday_le n hw
        exact ⟨fun _ => lt_of_le_of_lt hwn (hn.trans hy), fun _ => lt_of_le_of_lt hwn hn⟩)
      rw [SurrealField.birthday_natCast] at key
      exact lt_irrefl _ (lt_of_le_of_lt h key)

/-- The mirror bound, from `birthday_neg`. -/
theorem neg_natCast_le_of_birthday_le (n : ℕ) {y : K} (h : birthday y ≤ n) :
    -((n : ℕ) : K) ≤ y := by
  have := le_natCast_of_birthday_le n (y := -y) (by rwa [birthday_neg])
  linarith

/-- **A number born by day `n` has `|y| ≤ n`.** -/
theorem abs_le_natCast_of_birthday_le (n : ℕ) {y : K} (h : birthday y ≤ n) :
    |y| ≤ ((n : ℕ) : K) :=
  abs_le.mpr ⟨neg_natCast_le_of_birthday_le n h, le_natCast_of_birthday_le n h⟩

/-- **Finite birthday implies finite.** -/
theorem isFinite_of_birthday_lt_omega {y : K} (h : birthday y < Ordinal.omega0) :
    IsFinite y := by
  obtain ⟨n, hn⟩ := Ordinal.lt_omega0.mp h
  exact ⟨n, abs_le_natCast_of_birthday_le n hn.le⟩

/-- **An infinite number is born on day `ω` or later.** -/
theorem omega0_le_birthday_of_not_isFinite {y : K} (h : ¬ IsFinite y) :
    Ordinal.omega0 ≤ birthday y :=
  not_lt.mp fun h' => h (isFinite_of_birthday_lt_omega h')

/-- `ω` is not finite. -/
theorem not_isFinite_omegaSurreal : ¬ IsFinite (omegaSurreal : K) := by
  rintro ⟨n, hn⟩
  have h1 := omegaSurreal_gt_natCast (K := K) n
  have h2 : (omegaSurreal : K) ≤ |omegaSurreal| := le_abs_self _
  exact lt_irrefl _ (lt_of_le_of_lt (h2.trans hn) h1)

/-- **`ω` is born on day `ω` or later.**  With `BirthdayField` alone this fails: the flat
birthday puts `ω` on day `1`. -/
theorem omega0_le_birthday_omegaSurreal : Ordinal.omega0 ≤ birthday (omegaSurreal : K) :=
  omega0_le_birthday_of_not_isFinite not_isFinite_omegaSurreal

/-- **Distinct numbers born on the same day are separated by an older number.**  The
contrapositive of simplicity, applied with the two birthdays equal. -/
theorem exists_older_separating {x z : K} (hxz : x ≠ z) (h : birthday x = birthday z) :
    ∃ y : K, birthday y < birthday x ∧ ¬ (y < x ↔ y < z) := by
  by_contra hne
  push_neg at hne
  have := SurrealField.simplicity x z hxz (fun y hy => (hne y hy))
  rw [h] at this
  exact lt_irrefl _ this

end SurrealField

end QOU.AppendixSurreals
