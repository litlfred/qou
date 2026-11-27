import Mathlib.Tactic

/-!
# General-word cycle forcing for `q`-Collatz (Front B, B2 — the arbitrary parity word)

Every cycle-exclusion result already in the corpus is stated either for one
*named* parity word or for one *shape* of word:

* period 2/3/4 word-by-word (`qcollatz_period2_*`, `qcollatz_period3_*`,
  `qcollatz_period4_*`);
* the **adjacent-tail** shape `Oᵐ E^{k-m}` — an `m`-step odd chain closed by an
  even tail — in `collatz_one_odd_family.lean`.

Nothing states the forcing equation for an **arbitrary** parity word. This file
supplies it, together with the `q = 1` height bounds every word obeys, and
derives a cycle-exclusion family that strictly contains the adjacent-tail one.

## The uniform step

Both branches of the Skein-Collatz map divide by `[2]_q = q + 1`, so a step is
uniformly affine:

    [2]_q · P_{i+1} = a_i · P_i + b_i,    (a_i, b_i) = (1, 0)     even
                                          (a_i, b_i) = ([3]_q, 1) odd

with `[3]_q = q² + q + 1`. A parity word is therefore just a `w : ℕ → Bool`
(`w i = true` ⟺ step `i` is odd), and iterating `k` steps gives
`word_collapse`:

    (q+1)^n · Pₙ = wordHol · P₀ + wordNum.

A period-`k` cycle (`P k = P 0`) then forces (`qcollatz_word_forces`)

    ((q+1)^k − [3]_q^m) · P₀ = n_w,      m = #{i < k : w i}.

## The height bounds

Applying a `q = 1` evaluation `φ : R →+* ℤ` — the engine
`no_cycle_of_q_one_height` of `collatz_one_odd_family.lean` — the denominator
has height `2^k − 3^m`, and the numerator obeys, at `n` steps with `m` odd ones,

    3^m − 2^m  ≤  φ(n_w)  ≤  3^m·2^{n−m} − 2^n.

Both are proved here by induction on the word, in the multiplied forms
`3^m ≤ φ(n_w) + 2^m` and `2^m·(φ(n_w) + 2^n) ≤ 3^m·2^n`, which avoids truncated
`ℕ`-subtraction inside an exponent. The lower bound is attained exactly by the
adjacent-tail word — `3^m − 2^m` is precisely the height that file computes for
its `oddTailSum` — so the landed family reappears here as the extreme case.

## Scope — what this does and does not do (AGENTS.md (a)/(b))

This is a **scope-(a)** result. The upper bound is sharp, and on its own it is
*too weak* to exclude a general word: `3^m·2^{k−m} − 2^k < 2^k − 3^m` forces
`m ≤ 1`. That is not a defect of the argument — the general cycle problem is
open classically, and this is its `q`-analog. What the bound *does* buy is an
exclusion whenever the odd steps are **front-loaded**: if every odd step occurs
before position `D`, the numerator stops growing at `D`, and the height
obstruction fires under a contractivity hypothesis relating `D`, `m` and `k`
(`qcollatz_no_front_loaded_cycle`). `D = m` recovers the adjacent-tail case;
every `D > m` is new, and `front_loaded_beyond_adjacent_tail` exhibits a
concrete such word (`O E O` then evens) that no existing lemma covers.

No invariant is fabricated, and no word is excluded that the height does not
exclude.

Base ring: generic `[CommRing R]` (§7c — no ordering, no radical, no `Real.*`).
-/

namespace QOU.AppendixSurreals.CollatzGeneralWord

variable {R : Type*} [CommRing R]

/-! ## The word, its holonomy and its numerator -/

/-- The multiplier of step `i`: `[3]_q` on an odd step, `1` on an even step. -/
def stepMul (q : R) (w : ℕ → Bool) (i : ℕ) : R :=
  if w i then q ^ 2 + q + 1 else 1

/-- The additive constant of step `i`: `1` on an odd step, `0` on an even step. -/
def stepAdd (_q : R) (w : ℕ → Bool) (i : ℕ) : R :=
  if w i then (1 : R) else 0

/-- **Holonomy after `n` steps** — the product of the step multipliers, i.e.
    `[3]_q` raised to the number of odd steps. -/
def wordHol (q : R) (w : ℕ → Bool) : ℕ → R
  | 0 => 1
  | n + 1 => stepMul q w n * wordHol q w n

/-- **Numerator after `n` steps** — the accumulated `+1`s, each carried through
    the later odd multipliers and weighted by the `[2]_q`-power at its position. -/
def wordNum (q : R) (w : ℕ → Bool) : ℕ → R
  | 0 => 0
  | n + 1 => stepMul q w n * wordNum q w n + stepAdd q w n * (q + 1) ^ n

/-- **Number of odd steps among the first `n`.** -/
def oddCount (w : ℕ → Bool) : ℕ → ℕ
  | 0 => 0
  | n + 1 => oddCount w n + (if w n then 1 else 0)

theorem oddCount_le (w : ℕ → Bool) : ∀ n, oddCount w n ≤ n := by
  intro n
  induction n with
  | zero => simp [oddCount]
  | succ n ih =>
    simp only [oddCount]
    split <;> omega

/-! ## The general-word transfer identity -/

/-- **General-word collapse.** For any parity word `w`, an orbit satisfying the
    uniform affine step relation obeys
    `(q+1)^n · Pₙ = wordHol · P₀ + wordNum` after `n` steps. This is the
    arbitrary-word generalisation of `even_chain_collapse` and
    `odd_chain_collapse`, which are its all-even and all-odd specialisations. -/
theorem word_collapse (q : R) (w : ℕ → Bool) (P : ℕ → R)
    (hstep : ∀ i, P (i + 1) * (q + 1) = stepMul q w i * P i + stepAdd q w i) :
    ∀ n, (q + 1) ^ n * P n = wordHol q w n * P 0 + wordNum q w n := by
  intro n
  induction n with
  | zero => simp [wordHol, wordNum]
  | succ n ih =>
    have hn := hstep n
    simp only [wordHol, wordNum, pow_succ]
    linear_combination (q + 1) ^ n * hn + stepMul q w n * ih

/-- **General-word cycle forcing.** A period-`k` orbit of any parity word `w`
    forces `((q+1)^k − [3]_q^m)·P₀ = n_w`, the holonomy being `[3]_q^m` for `m`
    the number of odd steps. Specialises to every named period-2/3/4 forcing
    lemma and to `qcollatz_adj_tail_forces`. -/
theorem qcollatz_word_forces (q : R) (w : ℕ → Bool) (P : ℕ → R) (k : ℕ)
    (hstep : ∀ i, P (i + 1) * (q + 1) = stepMul q w i * P i + stepAdd q w i)
    (hcyc : P k = P 0) :
    ((q + 1) ^ k - wordHol q w k) * P 0 = wordNum q w k := by
  have h := word_collapse q w P hstep k
  rw [hcyc] at h
  linear_combination h

/-! ## The `q = 1` heights

A `q = 1` evaluation `φ : R →+* ℤ` sends `[2]_q ↦ 2` and `[3]_q ↦ 3`. -/

variable (φ : R →+* ℤ)

/-- **Holonomy height is `3^m`.** -/
theorem wordHol_map (q : R) (w : ℕ → Bool) (hq : φ q = 1) :
    ∀ n, φ (wordHol q w n) = 3 ^ oddCount w n := by
  intro n
  induction n with
  | zero => simp [wordHol, oddCount]
  | succ n ih =>
    by_cases h : w n = true
    · have hs : stepMul q w n = q ^ 2 + q + 1 := by simp [stepMul, h]
      have ho : oddCount w (n + 1) = oddCount w n + 1 := by simp [oddCount, h]
      rw [ho]
      show φ (stepMul q w n * wordHol q w n) = _
      rw [hs, map_mul, ih]
      simp only [map_add, map_pow, map_one, hq]
      ring
    · have hs : stepMul q w n = 1 := by simp [stepMul, h]
      have ho : oddCount w (n + 1) = oddCount w n := by simp [oddCount, h]
      rw [ho]
      show φ (stepMul q w n * wordHol q w n) = _
      rw [hs, map_mul, ih, map_one, one_mul]

/-- Numerator recursion at `q = 1`, odd step. -/
theorem wordNum_map_succ_odd (q : R) (w : ℕ → Bool) (hq : φ q = 1) (n : ℕ)
    (h : w n = true) :
    φ (wordNum q w (n + 1)) = 3 * φ (wordNum q w n) + 2 ^ n := by
  have hs : stepMul q w n = q ^ 2 + q + 1 := by simp [stepMul, h]
  have ha : stepAdd q w n = (1 : R) := by simp [stepAdd, h]
  show φ (stepMul q w n * wordNum q w n + stepAdd q w n * (q + 1) ^ n) = _
  rw [hs, ha, map_add, map_mul, map_mul, map_pow, map_one, one_mul]
  simp only [map_add, map_pow, map_one, hq]
  ring

/-- Numerator recursion at `q = 1`, even step. -/
theorem wordNum_map_succ_even (q : R) (w : ℕ → Bool) (n : ℕ) (h : w n = false) :
    φ (wordNum q w (n + 1)) = φ (wordNum q w n) := by
  have hs : stepMul q w n = 1 := by simp [stepMul, h]
  have ha : stepAdd q w n = (0 : R) := by simp [stepAdd, h]
  show φ (stepMul q w n * wordNum q w n + stepAdd q w n * (q + 1) ^ n) = _
  rw [hs, ha, map_add, map_mul, map_mul, map_one, one_mul, map_zero, zero_mul,
    add_zero]

/-- **The numerator height is non-negative.** -/
theorem wordNum_map_nonneg (q : R) (w : ℕ → Bool) (hq : φ q = 1) :
    ∀ n, 0 ≤ φ (wordNum q w n) := by
  intro n
  induction n with
  | zero => simp [wordNum]
  | succ n ih =>
    by_cases h : w n = true
    · rw [wordNum_map_succ_odd φ q w hq n h]; positivity
    · rw [wordNum_map_succ_even φ q w n (by simpa using h)]; exact ih

/-- **Lower height bound `3^m ≤ φ(n_w) + 2^m`**, i.e. `φ(n_w) ≥ 3^m − 2^m`,
    stated without `ℕ`-subtraction. The bound is *attained* by the adjacent-tail
    word, whose numerator `oddTailSum` has height exactly `3^m − 2^m`. -/
theorem wordNum_map_lower (q : R) (w : ℕ → Bool) (hq : φ q = 1) :
    ∀ n, (3 : ℤ) ^ oddCount w n ≤ φ (wordNum q w n) + 2 ^ oddCount w n := by
  intro n
  induction n with
  | zero => simp [wordNum, oddCount]
  | succ n ih =>
    by_cases h : w n = true
    · have ho : oddCount w (n + 1) = oddCount w n + 1 := by simp [oddCount, h]
      have hpow : (2 : ℤ) ^ oddCount w n ≤ 2 ^ n :=
        pow_le_pow_right₀ (by norm_num) (oddCount_le w n)
      rw [ho, wordNum_map_succ_odd φ q w hq n h]
      have e3 : (3 : ℤ) ^ (oddCount w n + 1) = 3 * 3 ^ oddCount w n := by ring
      have e2 : (2 : ℤ) ^ (oddCount w n + 1) = 2 * 2 ^ oddCount w n := by ring
      rw [e3, e2]
      linarith
    · have ho : oddCount w (n + 1) = oddCount w n := by simp [oddCount, h]
      rw [ho, wordNum_map_succ_even φ q w n (by simpa using h)]
      exact ih

/-- **Upper height bound `2^m·(φ(n_w) + 2^n) ≤ 3^m·2^n`**, i.e.
    `φ(n_w) ≤ 3^m·2^{n−m} − 2^n`, stated without `ℕ`-subtraction in the exponent.
    Sharp: equality holds for the word whose odd steps all sit at the end. -/
theorem wordNum_map_upper (q : R) (w : ℕ → Bool) (hq : φ q = 1) :
    ∀ n, (2 : ℤ) ^ oddCount w n * (φ (wordNum q w n) + 2 ^ n)
        ≤ 3 ^ oddCount w n * 2 ^ n := by
  intro n
  induction n with
  | zero => simp [wordNum, oddCount]
  | succ n ih =>
    by_cases h : w n = true
    · have ho : oddCount w (n + 1) = oddCount w n + 1 := by simp [oddCount, h]
      rw [ho, wordNum_map_succ_odd φ q w hq n h]
      have e1 : (2 : ℤ) ^ (oddCount w n + 1)
            * (3 * φ (wordNum q w n) + 2 ^ n + 2 ^ (n + 1))
          = 6 * (2 ^ oddCount w n * (φ (wordNum q w n) + 2 ^ n)) := by ring
      have e2 : (3 : ℤ) ^ (oddCount w n + 1) * 2 ^ (n + 1)
          = 6 * (3 ^ oddCount w n * 2 ^ n) := by ring
      rw [e1, e2]
      exact mul_le_mul_of_nonneg_left ih (by norm_num)
    · have ho : oddCount w (n + 1) = oddCount w n := by simp [oddCount, h]
      have hnn := wordNum_map_nonneg φ q w hq n
      have h2 : (0 : ℤ) < 2 ^ oddCount w n := by positivity
      rw [ho, wordNum_map_succ_even φ q w n (by simpa using h)]
      have e1 : (2 : ℤ) ^ oddCount w n * (φ (wordNum q w n) + 2 ^ (n + 1))
          = 2 * (2 ^ oddCount w n * (φ (wordNum q w n) + 2 ^ n))
            - 2 ^ oddCount w n * φ (wordNum q w n) := by ring
      have e2 : (3 : ℤ) ^ oddCount w n * 2 ^ (n + 1)
          = 2 * (3 ^ oddCount w n * 2 ^ n) := by ring
      rw [e1, e2]
      nlinarith [ih, hnn, h2]

/-! ## Front-loaded words: an exclusion family strictly containing adjacent-tail -/

/-- **Past the last odd step nothing accumulates.** If every step from `D` on is
    even, the numerator and the odd-count are constant from `D` onwards. -/
theorem wordNum_const_of_front (q : R) (w : ℕ → Bool) (D : ℕ)
    (hfront : ∀ i, D ≤ i → w i = false) :
    ∀ n, D ≤ n → wordNum q w n = wordNum q w D ∧ oddCount w n = oddCount w D := by
  intro n
  induction n with
  | zero =>
    intro hn
    have hD : D = 0 := Nat.le_zero.mp hn
    subst hD; exact ⟨rfl, rfl⟩
  | succ n ih =>
    intro hn
    rcases Nat.eq_or_lt_of_le hn with h | h
    · rw [← h]; exact ⟨rfl, rfl⟩
    · have hDn : D ≤ n := by omega
      obtain ⟨h1, h2⟩ := ih hDn
      have hw : w n = false := hfront n hDn
      refine ⟨?_, ?_⟩
      · show stepMul q w n * wordNum q w n + stepAdd q w n * (q + 1) ^ n = _
        have hs : stepMul q w n = 1 := by simp [stepMul, hw]
        have ha : stepAdd q w n = (0 : R) := by simp [stepAdd, hw]
        rw [hs, ha, one_mul, zero_mul, add_zero, h1]
      · show oddCount w n + (if w n then 1 else 0) = _
        rw [hw]; simpa using h2

/-- **No front-loaded cycle under the contractivity bound.** Suppose every odd
    step of the word occurs before position `D`, there is at least one, and the
    period-`k` cycle equation is forced. Then the `q = 1` height obstruction
    fires whenever

        3^m·2^D  <  2^m·2^k − 2^m·3^m + 2^m·2^D        (`m = oddCount w D`),

    and no such cycle exists.

    Taking `D = m` (all odd steps first, then evens) the hypothesis reduces to
    `2·3^m − 2^m < 2^k`, so this **subsumes** `qcollatz_no_adj_tail_cycle`, whose
    hypothesis is the very slightly stronger `2·3^m < 2^k`; every `D > m` is a
    word shape no existing lemma reaches.

    **Scope (a).** This excludes the front-loaded words, not all words: the
    general upper bound alone forces `m ≤ 1`, and the general cycle problem is
    open classically. -/
theorem qcollatz_no_front_loaded_cycle (q P0 : R) (w : ℕ → Bool) (hq : φ q = 1)
    (k D : ℕ) (hDk : D ≤ k) (hfront : ∀ i, D ≤ i → w i = false)
    (hm : 1 ≤ oddCount w D)
    (hcontract : (3 : ℤ) ^ oddCount w D * 2 ^ D
        < 2 ^ oddCount w D * 2 ^ k - 2 ^ oddCount w D * 3 ^ oddCount w D
          + 2 ^ oddCount w D * 2 ^ D)
    (hforce : ((q + 1) ^ k - wordHol q w k) * P0 = wordNum q w k) :
    False := by
  obtain ⟨hnum, hcnt⟩ := wordNum_const_of_front q w D hfront k hDk
  -- the forced equation, evaluated at `q = 1`
  have hmap := congrArg φ hforce
  rw [map_mul, map_sub, map_pow, map_add, map_one, hq,
    wordHol_map φ q w hq k, hcnt, hnum] at hmap
  norm_num at hmap
  -- so `2^k − 3^m` divides the numerator height
  have hdvd : ((2 : ℤ) ^ k - 3 ^ oddCount w D) ∣ φ (wordNum q w D) :=
    ⟨φ P0, hmap.symm⟩
  -- positivity of the numerator height, from the lower bound
  have hlow := wordNum_map_lower φ q w hq D
  have h23 : (2 : ℤ) ^ oddCount w D < 3 ^ oddCount w D :=
    pow_lt_pow_left₀ (by norm_num) (by norm_num) (by omega)
  have hpos : 0 < φ (wordNum q w D) := by linarith
  -- strict upper bound against the denominator height, from the upper bound
  have hup := wordNum_map_upper φ q w hq D
  have h2m : (0 : ℤ) < 2 ^ oddCount w D := by positivity
  have hlt : φ (wordNum q w D) < 2 ^ k - 3 ^ oddCount w D := by
    have hstep : (2 : ℤ) ^ oddCount w D * φ (wordNum q w D)
        < 2 ^ oddCount w D * (2 ^ k - 3 ^ oddCount w D) := by nlinarith [hup]
    exact lt_of_mul_lt_mul_left hstep (le_of_lt h2m)
  exact absurd (Int.le_of_dvd hpos hdvd) (not_le.mpr hlt)

/-! ## A front-loaded word outside the adjacent-tail family

`w = O E O E E …` has its odd steps at positions `0` and `2` — not contiguous, so
neither `qcollatz_no_one_odd_cycle` nor `qcollatz_no_adj_tail_cycle` applies. It
is front-loaded with `D = 3`, `m = 2`, and the contractivity hypothesis holds at
`k = 5`: `3²·2³ = 72 < 2²·2⁵ − 2²·3² + 2²·2³ = 128 − 36 + 32 = 124`. -/

/-- The word `O E O` followed by even steps. -/
def oeoWord : ℕ → Bool := fun i => decide (i = 0 ∨ i = 2)

theorem oeoWord_front : ∀ i, 3 ≤ i → oeoWord i = false := by
  intro i hi
  simp only [oeoWord, decide_eq_false_iff_not]
  omega

theorem oeoWord_oddCount : oddCount oeoWord 3 = 2 := by
  have h0 : oeoWord 0 = true := rfl
  have h1 : oeoWord 1 = false := rfl
  have h2 : oeoWord 2 = true := rfl
  simp only [oddCount, h0, h1, h2]
  decide

/-- **The hypotheses of `qcollatz_no_front_loaded_cycle` are satisfiable outside
    the adjacent-tail family** — witnessing that the new exclusion is not vacuous
    and not a restatement of what is already proved. -/
theorem front_loaded_beyond_adjacent_tail :
    1 ≤ oddCount oeoWord 3 ∧
    (3 : ℤ) ^ oddCount oeoWord 3 * 2 ^ 3
      < 2 ^ oddCount oeoWord 3 * 2 ^ 5
        - 2 ^ oddCount oeoWord 3 * 3 ^ oddCount oeoWord 3
        + 2 ^ oddCount oeoWord 3 * 2 ^ 3 := by
  rw [oeoWord_oddCount]
  norm_num


/-! ## The exact height, and a computable exclusion criterion for any word

The two bounds above are enough for the front-loaded family but throw information
away. The numerator's `q = 1` height has an exact closed form: each odd step at
position `i` contributes `2^i`, carried through the `[3]_q` of every *later* odd
step. Writing `m_i` for the number of odd steps after `i`,

    φ(n_w) = Σ_{i < k, w i} 3^{m_i} · 2^i.

With that, the height engine gives an exclusion criterion computable directly
from the word — no shape hypothesis at all. `wordNum_map_lower` and
`wordNum_map_upper` are then the two extreme cases of this sum (all odd steps as
early, resp. as late, as possible). -/

theorem oddCount_mono (w : ℕ → Bool) {a b : ℕ} (h : a ≤ b) :
    oddCount w a ≤ oddCount w b := by
  induction b with
  | zero => simp_all
  | succ n ih =>
    rcases Nat.eq_or_lt_of_le h with rfl | hlt
    · exact le_rfl
    · have hn : a ≤ n := by omega
      have := ih hn
      simp only [oddCount]
      split <;> omega

/-- **Exact `q = 1` height of the numerator.** Each odd step at position `i`
    contributes `2^i`, tripled once for every odd step strictly after it. -/
theorem wordNum_map_closed (q : R) (w : ℕ → Bool) (hq : φ q = 1) :
    ∀ n, φ (wordNum q w n)
      = ∑ i ∈ Finset.range n,
          (if w i then (3 : ℤ) ^ (oddCount w n - oddCount w (i + 1)) * 2 ^ i else 0) := by
  intro n
  induction n with
  | zero => simp [wordNum]
  | succ n ih =>
    rw [Finset.sum_range_succ]
    by_cases h : w n = true
    · have ho : oddCount w (n + 1) = oddCount w n + 1 := by simp [oddCount, h]
      have hlast :
          (if w n then (3 : ℤ) ^ (oddCount w (n + 1) - oddCount w (n + 1)) * 2 ^ n else 0)
            = 2 ^ n := by simp [h]
      have hrest : ∑ i ∈ Finset.range n,
            (if w i then (3 : ℤ) ^ (oddCount w (n + 1) - oddCount w (i + 1)) * 2 ^ i else 0)
          = 3 * ∑ i ∈ Finset.range n,
            (if w i then (3 : ℤ) ^ (oddCount w n - oddCount w (i + 1)) * 2 ^ i else 0) := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl (fun i hi => ?_)
        have hin : i + 1 ≤ n := Finset.mem_range.mp hi
        have hle : oddCount w (i + 1) ≤ oddCount w n := oddCount_mono w hin
        by_cases hw : w i = true
        · simp only [hw, if_true, ho]
          have hsub : oddCount w n + 1 - oddCount w (i + 1)
              = (oddCount w n - oddCount w (i + 1)) + 1 := by omega
          rw [hsub, pow_succ]
          ring
        · simp [hw]
      rw [wordNum_map_succ_odd φ q w hq n h, hlast, hrest, ih]
    · have ho : oddCount w (n + 1) = oddCount w n := by simp [oddCount, h]
      have hlast :
          (if w n then (3 : ℤ) ^ (oddCount w (n + 1) - oddCount w (n + 1)) * 2 ^ n else 0)
            = 0 := by simp [h]
      rw [wordNum_map_succ_even φ q w n (by simpa using h), hlast, add_zero, ho, ih]

/-- **General-word exclusion, by the exact height.** For *any* parity word: if the
    numerator's height is positive and strictly below the denominator's height
    `2^k − 3^m`, the divisibility `φ(D) ∣ φ(n_w)` demanded by a cycle fails, so no
    such cycle exists.

    Unlike `qcollatz_no_front_loaded_cycle` this carries **no shape hypothesis** —
    the criterion is evaluated directly from the word. Both hypotheses are finite
    integer computations for a concrete `w` and `k`.

    **Scope (a), unchanged.** This is a criterion, not a proof that the criterion
    is always met: for a general word the height can exceed `2^k − 3^m`, and
    deciding when it does not is the open problem. It systematises the two
    existing families rather than superseding the question. -/
theorem qcollatz_no_cycle_of_height_lt (q P0 : R) (w : ℕ → Bool) (hq : φ q = 1) (k : ℕ)
    (hpos : 0 < ∑ i ∈ Finset.range k,
      (if w i then (3 : ℤ) ^ (oddCount w k - oddCount w (i + 1)) * 2 ^ i else 0))
    (hlt : (∑ i ∈ Finset.range k,
      (if w i then (3 : ℤ) ^ (oddCount w k - oddCount w (i + 1)) * 2 ^ i else 0))
        < 2 ^ k - 3 ^ oddCount w k)
    (hforce : ((q + 1) ^ k - wordHol q w k) * P0 = wordNum q w k) :
    False := by
  have hmap := congrArg φ hforce
  rw [map_mul, map_sub, map_pow, map_add, map_one, hq, wordHol_map φ q w hq k,
    wordNum_map_closed φ q w hq k] at hmap
  norm_num at hmap
  have hdvd : ((2 : ℤ) ^ k - 3 ^ oddCount w k) ∣
      ∑ i ∈ Finset.range k,
        (if w i then (3 : ℤ) ^ (oddCount w k - oddCount w (i + 1)) * 2 ^ i else 0) :=
    ⟨φ P0, hmap.symm⟩
  exact absurd (Int.le_of_dvd hpos hdvd) (not_le.mpr hlt)


/-! ## Orbit-level form

Every exclusion above takes the *forced cycle equation* as a hypothesis, matching
the style of the landed `qcollatz_no_adj_tail_cycle`. Composing each with
`qcollatz_word_forces` removes that intermediate step, giving statements phrased
purely in terms of an orbit: a step relation and a return. These are what a
consumer actually has in hand. -/

/-- **No periodic orbit of any word whose exact height is below the denominator
    height.** The orbit-level form of `qcollatz_no_cycle_of_height_lt`: the forced
    cycle equation is discharged internally, so the hypotheses are just the step
    relation, the return `P k = P 0`, and two finite integer computations. -/
theorem qcollatz_no_periodic_orbit_of_height_lt (q : R) (w : ℕ → Bool) (P : ℕ → R)
    (hq : φ q = 1) (k : ℕ)
    (hstep : ∀ i, P (i + 1) * (q + 1) = stepMul q w i * P i + stepAdd q w i)
    (hcyc : P k = P 0)
    (hpos : 0 < ∑ i ∈ Finset.range k,
      (if w i then (3 : ℤ) ^ (oddCount w k - oddCount w (i + 1)) * 2 ^ i else 0))
    (hlt : (∑ i ∈ Finset.range k,
      (if w i then (3 : ℤ) ^ (oddCount w k - oddCount w (i + 1)) * 2 ^ i else 0))
        < 2 ^ k - 3 ^ oddCount w k) :
    False :=
  qcollatz_no_cycle_of_height_lt φ q (P 0) w hq k hpos hlt
    (qcollatz_word_forces q w P k hstep hcyc)

/-- **No front-loaded periodic orbit under the contractivity bound.** The
    orbit-level form of `qcollatz_no_front_loaded_cycle`. -/
theorem qcollatz_no_front_loaded_periodic_orbit (q : R) (w : ℕ → Bool) (P : ℕ → R)
    (hq : φ q = 1) (k D : ℕ) (hDk : D ≤ k)
    (hstep : ∀ i, P (i + 1) * (q + 1) = stepMul q w i * P i + stepAdd q w i)
    (hcyc : P k = P 0)
    (hfront : ∀ i, D ≤ i → w i = false)
    (hm : 1 ≤ oddCount w D)
    (hcontract : (3 : ℤ) ^ oddCount w D * 2 ^ D
        < 2 ^ oddCount w D * 2 ^ k - 2 ^ oddCount w D * 3 ^ oddCount w D
          + 2 ^ oddCount w D * 2 ^ D) :
    False :=
  qcollatz_no_front_loaded_cycle φ q (P 0) w hq k D hDk hfront hm hcontract
    (qcollatz_word_forces q w P k hstep hcyc)


/-! ## Where the criterion stops — a proved limitation

`qcollatz_no_cycle_of_height_lt` is evaluable for every word, and
`computations/qcollatz_height_criterion_coverage.py` evaluates it over all `2^k`
words for `k ≤ 18`. Two facts come out of that sweep, and the second is provable
rather than merely observed.

*Measured.* The excluded fraction does not grow with `k` — it **declines**,
`0.375` at `k = 3` down to `0.319` at `k = 18`, monotonically from `k = 5` on. So
the criterion does not asymptotically cover the word space.

*Proved, below.* More sharply, the criterion **cannot fire at all** unless
`2^k > 2·3^m − 2^m`. The reason is the lower height bound: every word has
`φ(n_w) ≥ 3^m − 2^m`, so once the denominator height `2^k − 3^m` drops to that
level there is no room left.

The consequence is the useful part. A genuine cycle needs its holonomy near one,
i.e. `2^k/3^m ≈ 1`; the criterion needs `2^k/3^m > 2 − (2/3)^m`, i.e. roughly
`2^k > 2·3^m`. **Those two regimes are disjoint.** The criterion is strong away
from the critical ratio `m/k ≈ log 2 / log 3` and empty at it — which the sweep
sees directly: at `k = 18` exclusion reaches `m ≤ 10` while the denominator stays
positive to `m = 11`, and that critical band of 31824 words has *no* exclusions.

This bounds the whole height approach, `qcollatz_no_adj_tail_cycle` and
`qcollatz_no_front_loaded_cycle` included: pushing the criterion further cannot
reach cycle candidates. Closing the cycle question needs an invariant that
survives at `2^k ≈ 3^m`, which the `q = 1` height provably does not. -/

/-- **The height criterion is vacuous below the threshold.** If
    `2^k ≤ 2·3^m − 2^m` then no word satisfies `φ(n_w) < 2^k − 3^m`, so
    `qcollatz_no_cycle_of_height_lt` cannot fire for any word at all.

    Complementary to `qcollatz_no_front_loaded_cycle`, whose hypothesis at
    `D = m` is exactly `2·3^m − 2^m < 2^k`: the criterion is available above the
    threshold and provably unavailable below it. -/
theorem height_criterion_vacuous_below_threshold (q : R) (w : ℕ → Bool)
    (hq : φ q = 1) (n : ℕ)
    (hthr : (2 : ℤ) ^ n ≤ 2 * 3 ^ oddCount w n - 2 ^ oddCount w n) :
    ¬ (φ (wordNum q w n) < 2 ^ n - 3 ^ oddCount w n) := by
  have hlow := wordNum_map_lower φ q w hq n
  intro hlt
  linarith

/-- **A cycle's own regime is below that threshold.** If the holonomy ratio is
    near one in the sense `2^k < 2 · 3^m − 2^m` — which includes every
    `2^k ≤ 3^m`, and more generally everything up to nearly twice `3^m` — the
    criterion is unavailable. Since a bounded cycle value forces `2^k` close to
    `3^m`, cycle candidates sit inside this regime. -/
theorem cycle_regime_is_below_threshold (m k : ℕ) (hm : 1 ≤ m)
    (hnear : (2 : ℤ) ^ k ≤ 3 ^ m) :
    (2 : ℤ) ^ k ≤ 2 * 3 ^ m - 2 ^ m := by
  have h2 : (2 : ℤ) ^ m < 3 ^ m :=
    pow_lt_pow_left₀ (by norm_num) (by norm_num) (by omega)
  linarith

/-! ## Contractive-word (`2^k < 3^m`) positivity exclusion (`qcz8`)

In the contractive sub-family where `2^k < 3^m` and `1 ≤ m = oddCount w k`, the
denominator height `2^k - 3^m` is strictly negative while `wordNum_map_lower`
forces the numerator height `φ(wordNum q w k) ≥ 3^m - 2^m > 0`. Consequently,
any cycle solution must satisfy `φ(P₀) < 0`, excluding every periodic orbit with
non-negative `q = 1` evaluation `0 ≤ φ(P₀)`. -/

/-- Any word with at least one odd step (`1 ≤ oddCount w n`) has strictly
    positive `q = 1` numerator height `0 < φ(wordNum q w n)`. -/
theorem wordNum_map_pos_of_oddCount_pos (q : R) (w : ℕ → Bool)
    (hq : φ q = 1) (n : ℕ) (hm : 1 ≤ oddCount w n) :
    0 < φ (wordNum q w n) := by
  have hlow := wordNum_map_lower φ q w hq n
  have h23 : (2 : ℤ) ^ oddCount w n < 3 ^ oddCount w n :=
    pow_lt_pow_left₀ (by norm_num) (by norm_num) (by omega)
  linarith

/-- In the contractive regime `2^k < 3^m` with `1 ≤ m = oddCount w k`, the cycle
    forcing equation forces `φ P0 < 0`. -/
theorem qcollatz_contractive_forces_neg_at_one (q P0 : R) (w : ℕ → Bool)
    (hq : φ q = 1) (k : ℕ) (hm : 1 ≤ oddCount w k)
    (hcontr : (2 : ℤ) ^ k < 3 ^ oddCount w k)
    (hforce : ((q + 1) ^ k - wordHol q w k) * P0 = wordNum q w k) :
    φ P0 < 0 := by
  have hmap := congrArg φ hforce
  rw [map_mul, map_sub, map_pow, map_add, map_one, hq, wordHol_map φ q w hq k] at hmap
  norm_num at hmap
  have hnum_pos := wordNum_map_pos_of_oddCount_pos φ q w hq k hm
  by_contra hge
  push_neg at hge
  have hden_neg : (2 : ℤ) ^ k - 3 ^ oddCount w k < 0 := by linarith
  have hprod_nonpos : ((2 : ℤ) ^ k - 3 ^ oddCount w k) * φ P0 ≤ 0 :=
    mul_nonpos_of_nonpos_of_nonneg (le_of_lt hden_neg) hge
  linarith

/-- **No non-negative periodic orbit in the contractive sub-family `2^k < 3^m`.**
    If `1 ≤ oddCount w k`, `2^k < 3^(oddCount w k)`, and `0 ≤ φ (P 0)`, then no
    period-`k` cycle exists. -/
theorem qcollatz_no_nonneg_cycle_of_contractive (q : R) (w : ℕ → Bool) (P : ℕ → R)
    (hq : φ q = 1) (k : ℕ)
    (hstep : ∀ i, P (i + 1) * (q + 1) = stepMul q w i * P i + stepAdd q w i)
    (hcyc : P k = P 0)
    (hm : 1 ≤ oddCount w k)
    (hcontr : (2 : ℤ) ^ k < 3 ^ oddCount w k)
    (hnonneg : 0 ≤ φ (P 0)) : False := by
  have hneg := qcollatz_contractive_forces_neg_at_one φ q (P 0) w hq k hm hcontr
    (qcollatz_word_forces q w P k hstep hcyc)
  linarith

end QOU.AppendixSurreals.CollatzGeneralWord
