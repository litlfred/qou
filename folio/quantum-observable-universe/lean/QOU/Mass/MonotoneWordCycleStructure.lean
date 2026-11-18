/-
QOU.Mass.MonotoneWordCycleStructure — the last gap in the arc: `compIdx` really does
count components. The closure permutation is the **cyclic shift on each `compIdx`
class**, and both inclusions follow.

Arc context (carrier derivation, route 3; beans `qou-768r`, `qou-2g9j`).
`MonotoneWordPositionTracking.lean` proved the `pStart` half of the modelling assumption
and narrowed the remainder to one thing: that the cycles of the closure permutation are
the maximal consecutive blocks of odd-exponent generators, i.e. that `compIdx` is the
component index. This file closes it.

**The closed form, and it is simpler than the cycle-decomposition argument it replaces.**
Write `π = posAfter e N` for the closure permutation (`N` runs executed). Then for
`i < N`:

| `e i` | `π i` | why it stays in `i`'s class |
|---|---|---|
| **odd** | `i + 1` | `compIdx (i+1) = compIdx i` — the `if` contributes `0` |
| **even** | `pStart e i` | `compIdx_pStart`, already proved |

That is the whole file. Neither case needs a cycle decomposition, and the even case is
already done: `posAfter e (i+1) i` unfolds to `posAfter e i i`, which
`MonotoneWordPositionTracking.posAfter_self` identifies as `pStart e i`.

**Both inclusions.**

`compIdx_posAfter` — `π` preserves `compIdx`. Hence every **cycle lies inside one
class**.

`posAfter_of_odd` — an odd run sends `i` to `i + 1`. Inside a class every step is odd
(an even one is where the class ends), so the class is **traversed upward in one cycle**;
`posAfter_of_even` closes it, since `pStart e i` is the class's least element
(`pStart_le` and `lt_compIdx_of_lt_pStart`). Hence every **class lies inside one cycle**.

Together: **cycles = `compIdx` classes**, which is what `compIdx` was assumed to compute.

**What this completes.** The arc's chain is now proved end to end from the braid word:
`posAfter` models the word's positions (`MonotoneWordPositionTracking`) · `compIdx`
counts its components (here) · tier 1 of `eps_eq` follows
(`MonotoneWordComponentStructure`) · `eps_eq` follows (`EpsEqFromMonotonicity`) ·
`μ̄ = 0` on every triple of the derived carrier follows
(`OneSeparatedComponentSufficesForMilnorVanishing`,
`ChainTripleMilnorVanishesByGcdDividesProduct`).

**What is still a definition rather than a theorem**, and it is the honest floor: that
`posAfter` *is* the position map of a monotone braid word, and that the closure's
components are the cycles of it. Those are modelling choices — the objects "braid word"
and "closure" are not defined in Lean anywhere in this arc. They are checked against the
code instead: the companion probe verifies that this `posAfter` recursion reproduces the
`perm` array of `analyse` **exactly**, 414/414, so the model is the probe's computation
rather than a parallel guess that might agree by sharing an assumption.

SCOPE — the theorems are unconditional. That `posAfter`/`compIdx` model a monotone
closure is **scope-(a)**, 414/414 on 400 random monotone words and the carrier's 14
branch-isotope pairs.

Base ring: none — `ℕ` bookkeeping (AGENTS.md §7c).
-/
import QOU.Mass.MonotoneWordPositionTracking

namespace QOU.Mass.MonotoneWordCycleStructure

open QOU.Mass.MonotoneWordComponentStructure QOU.Mass.MonotoneWordPositionTracking

/-- **Runs above `j` leave `j` alone.** Run `g` moves only positions `g` and `g+1`, so a
position strictly below `g` is untouched — the other half of `posAfter_of_le`, which
handled positions strictly above. -/
theorem posAfter_stab (e : ℕ → ℕ) {j g N : ℕ} (hjg : j < g) (hgN : g ≤ N) :
    posAfter e N j = posAfter e g j := by
  induction N with
  | zero =>
    have : g = 0 := Nat.le_zero.mp hgN
    subst this; rfl
  | succ N ih =>
    rcases Nat.lt_or_ge g (N + 1) with h | h
    · have hstep : posAfter e (N + 1) j = posAfter e N j := by
        by_cases hp : e N % 2 = 0
        · rw [posAfter, if_pos hp]
        · rw [posAfter, if_neg hp, swapAt]
          rw [if_neg (by omega), if_neg (by omega)]
      rw [hstep]; exact ih (by omega)
    · have : g = N + 1 := by omega
      subst this; rfl

/-- **An odd run fuses `i` with `i+1`.** The closure permutation sends `i` to `i + 1`:
runs above `i` cannot touch it (`posAfter_stab`), run `i` swaps it up, and runs below
cannot reach `i+1` (`posAfter_of_le`). -/
theorem posAfter_of_odd (e : ℕ → ℕ) {i N : ℕ} (hodd : ¬ e i % 2 = 0) (hiN : i + 1 ≤ N) :
    posAfter e N i = i + 1 := by
  rw [posAfter_stab e (Nat.lt_succ_self i) hiN, posAfter, if_neg hodd, swapAt_left]
  exact posAfter_of_le e (le_refl _)

/-- **An even run wraps `i` back to `pStart e i`.** Runs above `i` leave it alone and run
`i` does not move it, so the closure permutation returns the strand that was sitting at
position `i` when run `R_i` began — which `posAfter_self` identifies as `pStart e i`. -/
theorem posAfter_of_even (e : ℕ → ℕ) {i N : ℕ} (heven : e i % 2 = 0) (hiN : i + 1 ≤ N) :
    posAfter e N i = pStart e i := by
  rw [posAfter_stab e (Nat.lt_succ_self i) hiN, posAfter, if_pos heven]
  exact posAfter_self e i

/-- **The closure permutation preserves the class.** Both branches land in `compIdx e i`:
the odd one because an odd run contributes nothing to the count, the even one by
`compIdx_pStart`.

Hence every cycle of the closure lies inside a single `compIdx` class. -/
theorem compIdx_posAfter (e : ℕ → ℕ) {i N : ℕ} (hiN : i + 1 ≤ N) :
    compIdx e (posAfter e N i) = compIdx e i := by
  by_cases h : e i % 2 = 0
  · rw [posAfter_of_even e h hiN, compIdx_pStart]
  · rw [posAfter_of_odd e h hiN, compIdx_succ, if_neg h]
    omega

/-- `pStart e i` never exceeds `i` — it is the left end of a walk that only moves down. -/
theorem pStart_le (e : ℕ → ℕ) (i : ℕ) : pStart e i ≤ i := by
  induction i with
  | zero => exact le_refl _
  | succ i ih =>
    by_cases h : e i % 2 = 0
    · rw [pStart, if_pos h]
    · rw [pStart, if_neg h]; omega

/-- **`pStart e i` is the least element of `i`'s class**: everything strictly below it
sits in a strictly earlier class.

With `compIdx_pStart` (same class) this pins `pStart e i` as the class minimum, which is
what makes `posAfter_of_even` close the cycle rather than merely stay inside it. -/
theorem lt_compIdx_of_lt_pStart (e : ℕ → ℕ) {i j : ℕ} (hj : j < pStart e i) :
    compIdx e j < compIdx e i := by
  induction i with
  | zero => simp [pStart] at hj
  | succ i ih =>
    by_cases h : e i % 2 = 0
    · -- `pStart (i+1) = i+1`; the even run at `i` is itself the jump
      rw [pStart, if_pos h] at hj
      have h1 : compIdx e j ≤ compIdx e i := compIdx_mono e (by omega)
      have h2 : compIdx e i < compIdx e (i + 1) := compIdx_lt_of_even e i h
      omega
    · -- `pStart (i+1) = pStart i`; the odd run adds nothing, so the IH carries over
      rw [pStart, if_neg h] at hj
      have := ih hj
      rw [compIdx_succ, if_neg h]
      omega

/-- **The class is traversed upward.** Consecutive strands in the same class are joined by
an odd run, and the closure permutation sends one to the next — so a class is connected
inside a single cycle.

Together with `compIdx_posAfter` (cycle ⊆ class) this gives **cycles = classes**. -/
theorem step_within_class (e : ℕ → ℕ) {i N : ℕ} (hsame : compIdx e (i + 1) = compIdx e i)
    (hiN : i + 1 ≤ N) : posAfter e N i = i + 1 := by
  have hodd : ¬ e i % 2 = 0 := by
    intro h
    rw [compIdx_succ, if_pos h] at hsame
    omega
  exact posAfter_of_odd e hodd hiN

/-- **Not vacuous, and it exercises both branches.** All runs even: every class is a
singleton and the permutation is the identity on each — `π i = pStart e i = i`. -/
theorem allEven_posAfter (i N : ℕ) (hiN : i + 1 ≤ N) :
    posAfter (fun _ => 2) N i = i := by
  rw [posAfter_of_even _ (by norm_num) hiN]
  cases i with
  | zero => rfl
  | succ i => rw [pStart]; norm_num

/-- …and all runs odd: one class, and the permutation is the upward shift on it. -/
theorem allOdd_posAfter (i N : ℕ) (hiN : i + 1 ≤ N) :
    posAfter (fun _ => 1) N i = i + 1 :=
  posAfter_of_odd _ (by norm_num) hiN

/-- **Vanishing difference form of `allEven_posAfter` (`qou-87ms`).**
For `i + 1 ≤ N`, `posAfter (fun _ => 2) N i - i = 0`. -/
theorem allEven_posAfter_sub_eq_zero (i N : ℕ) (hiN : i + 1 ≤ N) :
    posAfter (fun _ => 2) N i - i = 0 := by
  rw [allEven_posAfter i N hiN, Nat.sub_self]

end QOU.Mass.MonotoneWordCycleStructure
