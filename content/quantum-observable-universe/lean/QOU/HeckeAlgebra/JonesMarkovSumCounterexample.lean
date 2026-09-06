/-
# `Σ_λ y_λ(q) = 1` is false — the Jones-Markov normalisation counterexample

`QOU.HeckeAlgebra.MarkovTrace` used to carry

```lean
axiom JonesMarkovCoefficient_sum_eq_one :
    ∀ (n : ℕ) (q : ℝ),
    (∑ lam ∈ partitions_as_finset n, JonesMarkovCoefficient lam q) = 1
```

cited to Wenzl 1988 Lemma 3.2 (the central-element normalisation). **The
proposition is false**, and this module proves its negation rather than
deriving `False` from the axiom, so the result survives the axiom's deletion
and blocks the statement from being restated.

## Why it fails

Take `q = 1`. `qInteger k q` is
`(q^(k/2) - q^(-k/2)) / (q^(1/2) - q^(-1/2))` with **real** exponents, so at
`q = 1` every `rpow` is `1` and the quotient is `(1-1)/(1-1) = 0/0`, which Lean
evaluates to `0` — for **every** `k`, not just `k = 0`. Its inverse is then `0`
too, so each cell contributes a factor of zero and the first row's fold
collapses. Every partition of every `n ≥ 1` therefore has coefficient `0`, and
the sum is `0`, not `1`.

## What the real normalisation is, and what this does NOT establish

Wenzl's Lemma 3.2 is a statement about a *normalised* trace, where the weights
enter against their dimensions — `Σ_λ y_λ · d_λ`, not the bare `Σ_λ y_λ`. Two
further mismatches are visible in the formalisation and are worth recording
because they are independent of the `q = 1` collapse:

* `wenzlClosedForm` carries the prefactor `QSubstrate.markovParameter ^ (n-1)`,
  and `markovParameter` is a **bare constant** pinned at the substrate `q_0`.
  It does not depend on the `q` the statement quantifies over, so the claimed
  identity would have to hold for a `q`-varying sum against a `q`-independent
  prefactor.
* `AGENTS.md` records the measured fact that the q-deformed weights do **not**
  sum to 1 away from `q = 1` either (0.987 / 0.982 / 0.982 / 0.991 / 1.111 /
  1.517 at `n = 3/4/5/6/9/12` at the proton pin).

This module establishes only the first point — that the stated proposition is
false. It does **not** supply the corrected statement; naming the right
normalisation is a separate question and is deliberately left open rather than
guessed at.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 Lemma 3.2
-/
import QOU.HeckeAlgebra.MarkovTrace

set_option autoImplicit false

namespace QOU.HeckeAlgebra.JonesMarkovSumCounterexample

open QOU.HeckeAlgebra QOU.HeckeAlgebra.JonesMarkovWenzl QOU.HeckeAlgebra.MarkovTrace

/-- At `q = 1` the q-integer's numerator and denominator both vanish, so Lean's
    `0/0 = 0` makes it zero for **every** `k`. -/
theorem qInteger_one_eq_zero (k : ℕ) : qInteger k 1 = 0 := by
  unfold qInteger
  split
  · rfl
  · simp [Real.one_rpow]

/-- Once a row accumulator is `0` it stays `0`, over any list of columns. -/
theorem foldl_zero {n : ℕ} (lam : Nat.Partition n) (i : ℕ) (l : List ℕ) :
    l.foldl (fun a j => a * (qInteger (cellHookLength lam i j) 1)⁻¹
        * (1 : ℝ) ^ ((n : ℝ) * (cellContent lam i j : ℝ))) 0 = 0 := by
  induction l with
  | nil => rfl
  | cons hd tl ih => simpa using ih

/-- A nonempty row folds to `0` at `q = 1`. -/
theorem inner_fold_zero {n : ℕ} (lam : Nat.Partition n) (i L : ℕ) (hL : L ≠ 0) :
    (List.range L).foldl
      (fun a j => a * (qInteger (cellHookLength lam i j) 1)⁻¹
        * (1 : ℝ) ^ ((n : ℝ) * (cellContent lam i j : ℝ))) 1 = 0 := by
  obtain ⟨L', rfl⟩ : ∃ m, L = m + 1 := ⟨L - 1, by omega⟩
  rw [List.range_succ_eq_map, List.foldl_cons]
  simpa [qInteger_one_eq_zero] using foldl_zero lam i ((List.range L').map Nat.succ)

/-- For `n ≠ 0` the first row is nonempty: the parts sum to `n` and are positive. -/
theorem rowLen_zero_ne_zero {n : ℕ} (lam : Nat.Partition n) (hn : n ≠ 0) :
    rowLen lam 0 ≠ 0 := by
  unfold rowLen partsList
  cases h : (lam.parts.sort (· ≥ ·))[0]? with
  | none =>
      exfalso
      have hnil : lam.parts.sort (· ≥ ·) = [] := by
        rcases hl : lam.parts.sort (· ≥ ·) with _ | ⟨a, t⟩
        · rfl
        · rw [hl] at h; simp at h
      have : lam.parts = 0 := by
        have := Multiset.sort_eq (· ≥ ·) lam.parts
        rw [hnil] at this
        simpa using this.symm
      exact hn (by simpa [this] using lam.parts_sum.symm)
  | some x =>
      simp only [Option.getD]
      have hx : x ∈ lam.parts.sort (· ≥ ·) := List.mem_of_getElem? h
      have hpos : 0 < x := lam.parts_pos (by simpa using hx)
      omega

theorem partsList_length_ne_zero {n : ℕ} (lam : Nat.Partition n) (hn : n ≠ 0) :
    (partsList lam).length ≠ 0 := by
  intro hlen
  apply hn
  have hnil : partsList lam = [] := List.length_eq_zero_iff.mp hlen
  have : lam.parts = 0 := by
    have := Multiset.sort_eq (· ≥ ·) lam.parts
    unfold partsList at hnil
    rw [hnil] at this
    simpa using this.symm
  simpa [this] using lam.parts_sum.symm

theorem outer_foldl_zero {n : ℕ} (lam : Nat.Partition n) (l : List ℕ) :
    l.foldl (fun acc i => acc * (List.range (rowLen lam i)).foldl
      (fun a j => a * (qInteger (cellHookLength lam i j) 1)⁻¹
        * (1 : ℝ) ^ ((n : ℝ) * (cellContent lam i j : ℝ))) 1) 0 = 0 := by
  induction l with
  | nil => rfl
  | cons hd tl ih => simpa using ih

/-- **Every Wenzl coefficient of every partition of `n ≥ 1` vanishes at `q = 1`.** -/
theorem wenzlClosedForm_one_eq_zero {n : ℕ} (hn : n ≠ 0) (lam : Nat.Partition n) :
    wenzlClosedForm lam 1 = 0 := by
  unfold wenzlClosedForm
  obtain ⟨m, hm⟩ : ∃ m, (partsList lam).length = m + 1 :=
    ⟨(partsList lam).length - 1, by have := partsList_length_ne_zero lam hn; omega⟩
  rw [hm, List.range_succ_eq_map, List.foldl_cons,
      inner_fold_zero lam 0 _ (rowLen_zero_ne_zero lam hn), mul_zero,
      outer_foldl_zero, mul_zero]

/-- **`JonesMarkovCoefficient_sum_eq_one` is FALSE.**

    At `n = 1`, `q = 1` every summand is `0`, so the sum is `0 ≠ 1`. -/
theorem not_jonesMarkovCoefficient_sum_eq_one :
    ¬ (∀ (n : ℕ) (q : ℝ),
        (∑ lam ∈ partitions_as_finset n, JonesMarkovCoefficient lam q) = 1) := by
  intro h
  have hz : ∀ lam ∈ partitions_as_finset 1, JonesMarkovCoefficient lam 1 = 0 :=
    fun lam _ => wenzlClosedForm_one_eq_zero (n := 1) one_ne_zero lam
  have h1 := h 1 1
  rw [Finset.sum_eq_zero hz] at h1
  norm_num at h1

end QOU.HeckeAlgebra.JonesMarkovSumCounterexample
