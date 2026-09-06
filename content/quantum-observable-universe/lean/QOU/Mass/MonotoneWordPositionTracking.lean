/-
QOU.Mass.MonotoneWordPositionTracking — the observation the whole tier-1 argument rests
on, proved: in a monotone word, when run `R_g` begins, position `g+1` still holds strand
`g+1`, and position `g` holds `pStart e g`.

Arc context (carrier derivation, route 3; beans `qou-768r`, `qou-2g9j`).
`MonotoneWordComponentStructure.lean` derives tier 1 of `eps_eq` from two one-line
recursions, `pStart` and `compIdx`, and names its own remainder: *"that `pStart` and
`compIdx` really do describe a monotone braid closure's strand positions and cycles …
needs braid words, position permutations and cycle decomposition as Lean objects, and is
not attempted."* This file attempts the **`pStart` half**, and it goes through.

**The model.** A monotone word is `R_0 R_1 … R_{n-2}` with `R_g = σ_g^{e_g}`, so the
position→strand map after runs `0 … g-1` is `posAfter e g`, built by pre-composing a
swap of positions `g` and `g+1` once per crossing. `e_g` crossings compose to the
identity when `e_g` is even and to one swap when it is odd — which is the whole reason
only parity appears below, and it is why `posAfter` can be defined by the one-step
recursion rather than by iterating `e_g` times.

**What is proved.**

`posAfter_of_le` — everything at or beyond position `g+1` is **untouched** after `g`
runs. This is the invariant, and it is where "ascending order" is used: run `h < g`
moves only positions `h, h+1 ≤ g`, so it cannot reach `g+1` or beyond.

`posAfter_succ_self` — hence position `g+1` still holds **strand `g+1`** when run `R_g`
begins. Every crossing of that run is therefore between the *same* pair of strands, and
the pair is fixed before the run starts.

`posAfter_self` — position `g` holds `pStart e g`, i.e. the `pStart` recursion in
`MonotoneWordComponentStructure` is the correct one: an even run restores the pair so
the next run's left strand is `g+1`; an odd run swaps them so it is carried over.

`crossing_pair_of_run` puts the two together: **run `g` crosses exactly the strands
`(pStart e g, g+1)`**. That is the sentence tier 1 was resting on.

**That last gap is now closed too (2026-09-05).** This said `compIdx` counting
components was "not attempted here" and would need "the cycle decomposition of a product
of ascending adjacent transpositions". It needs no such thing.
`MonotoneWordCycleStructure.lean` gets it from the lemmas above: with `π = posAfter e N`,

    e i odd   →  π i = i + 1        (`posAfter_of_odd`, from `posAfter_stab` + this file)
    e i even  →  π i = pStart e i   (`posAfter_of_even`, from `posAfter_self` above)

so `π` is the **cyclic shift on each `compIdx` class**, and both inclusions drop out —
`compIdx_posAfter` puts every cycle inside a class, and the odd steps traverse a class
upward so every class sits inside a cycle. Cycles **are** the classes.

**What remains is the modelling step itself**, one level below everything here: that
`posAfter` *is* a monotone braid word's position map and that the closure's components
*are* its cycles. "Braid word" and "closure" are not Lean objects anywhere in this arc,
so that is a definition rather than a theorem. It is measured: the companion probe checks
that this recursion reproduces `analyse`'s `perm` array **exactly**, 414/414 — entry for
entry, not merely agreeing on the component partition, which a reimplementation could do
by sharing an assumption.

**A modelling caveat worth stating.** `posAfter` is defined on all of `ℕ`, with no bound
`n`, and the closure is not modelled at all — this file is about the *braid*, not its
closure. Nothing below needs a bound (the invariant is one-sided), and the closure only
enters through `compIdx`, which is exactly the half left open.

SCOPE — the theorems are unconditional. The claim that `posAfter` models a monotone
braid word's positions is a **definition** here, checkable against `analyse` in the
probe by eye; the claim that `compIdx` models its cycles is **scope-(a)**, 414/414.

Base ring: none — `ℕ` bookkeeping throughout (AGENTS.md §7c).
-/
import QOU.Mass.MonotoneWordComponentStructure

namespace QOU.Mass.MonotoneWordPositionTracking

open QOU.Mass.MonotoneWordComponentStructure

/-- Transposition of positions `g` and `g+1`, as a function on position indices. -/
def swapAt (g j : ℕ) : ℕ := if j = g then g + 1 else if j = g + 1 then g else j

@[simp] theorem swapAt_left (g : ℕ) : swapAt g g = g + 1 := by simp [swapAt]

@[simp] theorem swapAt_right (g : ℕ) : swapAt g (g + 1) = g := by
  simp [swapAt]

/-- A position beyond the pair is fixed by the swap. -/
theorem swapAt_of_gt {g j : ℕ} (h : g + 1 < j) : swapAt g j = j := by
  unfold swapAt
  rw [if_neg (by omega), if_neg (by omega)]

/-- The position→strand map after runs `0, …, g-1` have executed.

`e_g` crossings of one adjacent pair compose to the identity when `e_g` is even and to a
single swap when it is odd, so only the parity of the exponent survives — which is why
this is a one-step recursion rather than an iteration. -/
def posAfter (e : ℕ → ℕ) : ℕ → ℕ → ℕ
  | 0, j => j
  | g + 1, j => if e g % 2 = 0 then posAfter e g j else posAfter e g (swapAt g j)

/-- **The invariant, and it is where ascending order is used.** After `g` runs, every
position at or beyond `g+1` still holds its original strand: run `h < g` moves only
positions `h` and `h+1`, both `≤ g`, so it cannot reach that far. -/
theorem posAfter_of_le (e : ℕ → ℕ) {g j : ℕ} (h : g + 1 ≤ j) : posAfter e g j = j := by
  induction g generalizing j with
  | zero => rfl
  | succ g ih =>
    by_cases hp : e g % 2 = 0
    · rw [posAfter, if_pos hp]; exact ih (by omega)
    · rw [posAfter, if_neg hp, swapAt_of_gt (by omega)]; exact ih (by omega)

/-- **Position `g+1` still holds strand `g+1` when run `R_g` begins.** The observation
the entire tier-1 argument rests on: the pair that run `g` will cross is fixed before it
starts, so all `e_g` of its crossings are between the same two strands. -/
theorem posAfter_succ_self (e : ℕ → ℕ) (g : ℕ) : posAfter e g (g + 1) = g + 1 :=
  posAfter_of_le e (le_refl _)

/-- **`pStart` is the correct recursion.** Position `g` holds `pStart e g` when run `R_g`
begins — an even run restores the pair so the next run's left strand is `g+1`, an odd
run swaps them so the left strand is carried over unchanged.

This is what `MonotoneWordComponentStructure` assumed about its own definition. -/
theorem posAfter_self (e : ℕ → ℕ) (g : ℕ) : posAfter e g g = pStart e g := by
  induction g with
  | zero => rfl
  | succ g ih =>
    by_cases hp : e g % 2 = 0
    · rw [posAfter, if_pos hp, posAfter_succ_self, pStart, if_pos hp]
    · rw [posAfter, if_neg hp, swapAt_right, ih, pStart, if_neg hp]

/-- **The two together: run `g` crosses exactly the strands `(pStart e g, g+1)`.**

Tier 1 of `eps_eq` was resting on this sentence; it is now a theorem about the position
recursion rather than a reading of the probe. -/
theorem crossing_pair_of_run (e : ℕ → ℕ) (g : ℕ) :
    posAfter e g g = pStart e g ∧ posAfter e g (g + 1) = g + 1 :=
  ⟨posAfter_self e g, posAfter_succ_self e g⟩

/-- **Not vacuous, and it exercises both branches.** With all exponents odd (`e ≡ 1`)
every run swaps, so the left strand is carried the whole way and stays `0`; the sibling
`allOdd_compIdx` says all strands are then in one component, so this is the
maximally-fused case. -/
theorem allOdd_posAfter_self (g : ℕ) : posAfter (fun _ => 1) g g = 0 := by
  rw [posAfter_self]
  induction g with
  | zero => rfl
  | succ g ih => rw [pStart]; norm_num [ih]

/-- …and with all exponents even (`e ≡ 2`) no run swaps, so position `g` still holds
strand `g` — the maximally-split case, matching `allEven_compIdx`'s singleton
components. -/
theorem allEven_posAfter_self (g : ℕ) : posAfter (fun _ => 2) g g = g := by
  rw [posAfter_self]
  cases g with
  | zero => rfl
  | succ g => rw [pStart]; norm_num

end QOU.Mass.MonotoneWordPositionTracking
