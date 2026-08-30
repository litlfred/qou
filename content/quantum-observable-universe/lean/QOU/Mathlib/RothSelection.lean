/-
# The parameter selection: turning an infinite supply of approximations into `Γ_m`'s growth clause

Every other stage of the arc is proved.  What is left is the step that makes Roth's theorem a
statement about *finitely many* solutions rather than a contradiction from assumed data: given
infinitely many good rational approximations to `α`, choose `m` of them whose heights grow fast
enough that `Γ_m`'s clauses hold.

## Why this is the piece that is not bookkeeping

Everything else in the arc composes hypotheses that a caller supplies.  This one *constructs* the
data, and it is the only place where the hypothesis "infinitely many solutions" is consumed.  The
construction is a recursion — pick a denominator past a threshold, raise it to a power, pick
another past *that* — and the recursion is where the "sufficiently large" in the informal proof
actually lives.

## The shape `Γ_m` wants

`rothGammaFull_of_heights` asks for `H j ^ (2q) ≤ H k ^ p` on consecutive indices.  Choosing the
next height beyond `H j ^ (2q)` gives `H j ^ (2q) ≤ H k`, and `H k ≤ H k ^ p` because `p ≥ 1` and
`H k ≥ 2` — so the growth function to iterate is exactly `x ↦ x ^ (2q)`, with the floor `2` carried
along to keep `two_le` true.  The `max` in `growSeq` is what carries it: without it the second
height could be chosen below the floor whenever `f` happened to return something small, and
`two_le` would fail on every index but the first.

## What this does not do

It selects heights and proves the growth clause.  It does not choose `ε`, `δ`, `m` or the degrees
— `rothDegrees` already determines the degrees from the heights, and `slack_pos` already says what
`ε`, `δ` and `m` must satisfy.  Assembling those choices with this selection into the final
statement is the remaining step.
-/
import QOU.Mathlib.RothGammaProducer

namespace MvPolynomial

section Selection

variable {S : Set ℕ}

/-- **The greedy fast-growing selection.**  Each term is chosen from the supply beyond both the
floor `N₀` and the growth function applied to its predecessor. -/
noncomputable def growSeq (hS : ∀ N, ∃ q ∈ S, N ≤ q) (f : ℕ → ℕ) (N₀ : ℕ) : ℕ → ℕ
  | 0 => Classical.choose (hS N₀)
  | (n + 1) => Classical.choose (hS (max N₀ (f (growSeq hS f N₀ n))))

theorem growSeq_mem (hS : ∀ N, ∃ q ∈ S, N ≤ q) (f : ℕ → ℕ) (N₀ : ℕ) :
    ∀ n, growSeq hS f N₀ n ∈ S
  | 0 => (Classical.choose_spec (hS N₀)).1
  | (n + 1) => (Classical.choose_spec (hS (max N₀ (f (growSeq hS f N₀ n))))).1

/-- The floor is respected at every index — this is what keeps `Γ_m`'s `two_le` clause true past
the first term. -/
theorem le_growSeq (hS : ∀ N, ∃ q ∈ S, N ≤ q) (f : ℕ → ℕ) (N₀ : ℕ) :
    ∀ n, N₀ ≤ growSeq hS f N₀ n
  | 0 => (Classical.choose_spec (hS N₀)).2
  | (n + 1) =>
      le_trans (le_max_left N₀ (f (growSeq hS f N₀ n)))
        (Classical.choose_spec (hS (max N₀ (f (growSeq hS f N₀ n))))).2

/-- Each term outruns the growth function applied to its predecessor. -/
theorem growSeq_succ (hS : ∀ N, ∃ q ∈ S, N ≤ q) (f : ℕ → ℕ) (N₀ : ℕ) (n : ℕ) :
    f (growSeq hS f N₀ n) ≤ growSeq hS f N₀ (n + 1) :=
  le_trans (le_max_right N₀ (f (growSeq hS f N₀ n)))
    (Classical.choose_spec (hS (max N₀ (f (growSeq hS f N₀ n))))).2

/-- **Two of `Γ_m`'s clauses, from an unbounded supply.**  Given infinitely many admissible
heights, `m` of them can be chosen from the supply, all beyond an arbitrary floor `N₀`, with
`H j ^ (2q) ≤ H k ^ p` on consecutive indices.

That is `rothGammaFull_of_heights`'s `hgrow` and `hH` at once — and taking `N₀ := 2 ^ F` also gives
its `floor` clause, which is why the floor is a parameter rather than the constant `2`.  Clause 3
is the one that bites hardest (`RothRealLadder`'s witness needed `H = 1024` at `m = 2` because of
it), so having it fall out of the same construction is worth the generality. -/
theorem exists_heights_growing (hS : ∀ N, ∃ q ∈ S, N ≤ q) (m p q : ℕ) (hp : 0 < p)
    (N₀ : ℕ) (hN₀ : 2 ≤ N₀) :
    ∃ H : Fin m → ℕ, (∀ h, H h ∈ S) ∧ (∀ h, N₀ ≤ H h) ∧ (∀ h, 2 ≤ H h) ∧
      ∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → H j ^ (2 * q) ≤ H k ^ p := by
  classical
  refine ⟨fun h => growSeq hS (fun x => x ^ (2 * q)) N₀ (h : ℕ),
    fun h => growSeq_mem hS _ N₀ _, fun h => le_growSeq hS _ N₀ _,
    fun h => le_trans hN₀ (le_growSeq hS _ N₀ _), fun j k hjk => ?_⟩
  have hstep : (growSeq hS (fun x => x ^ (2 * q)) N₀ (j : ℕ)) ^ (2 * q)
      ≤ growSeq hS (fun x => x ^ (2 * q)) N₀ ((j : ℕ) + 1) :=
    growSeq_succ hS (fun x => x ^ (2 * q)) N₀ (j : ℕ)
  rw [hjk] at hstep
  refine le_trans hstep ?_
  exact Nat.le_self_pow hp.ne' _

/-- **The floor clause too.**  At `N₀ = 2 ^ F` the selected heights also satisfy
`rothGammaFull_of_heights`'s `hfloor`. -/
theorem exists_heights_growing_floor (hS : ∀ N, ∃ q ∈ S, N ≤ q) (m p q F : ℕ) (hp : 0 < p)
    (hF : 1 ≤ F) :
    ∃ H : Fin m → ℕ, (∀ h, H h ∈ S) ∧ (∀ h, 2 ≤ H h) ∧
      (∀ j : Fin m, (j : ℕ) = 0 → (2 : ℤ) ^ F ≤ (H j : ℤ)) ∧
      ∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → H j ^ (2 * q) ≤ H k ^ p := by
  have h2F : 2 ≤ 2 ^ F := by
    calc (2 : ℕ) = 2 ^ 1 := (pow_one 2).symm
      _ ≤ 2 ^ F := Nat.pow_le_pow_right (by norm_num) hF
  obtain ⟨H, hmem, hfloor, h2, hgrow⟩ := exists_heights_growing hS m p q hp (2 ^ F) h2F
  refine ⟨H, hmem, h2, fun j _ => ?_, hgrow⟩
  have := hfloor j
  exact_mod_cast this

end Selection

end MvPolynomial
