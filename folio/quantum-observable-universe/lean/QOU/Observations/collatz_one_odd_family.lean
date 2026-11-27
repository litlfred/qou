import Mathlib.Tactic

/-!
# One-odd-step Skein-Collatz cycles are excluded at every period (Front B, B2)

Period-1/2/3/4 exclusion (elsewhere) proceeds word-by-word and does not scale.
This file proves the first **infinite family** by a genuine height obstruction —
the `q`-analog of the Steiner cycle-value bound, made rigorous for the
one-odd-step words `E^{k-1}O`.

A period-`k` cycle with exactly **one** odd step (the last) satisfies an even
chain `Pᵢ₊₁·(q+1) = Pᵢ` (`i < k-1`) then one odd step
`P₀·(q+1) = (q²+q+1)·P_{k-1} + 1`. The chain collapses
(`even_chain_collapse`) to `P₀ = (q+1)^{k-1}·P_{k-1}`, and the odd step then
forces

    ((q+1)^k − (q²+q+1)) · P_{k-1} = 1.

Over the Skein ring `ℤ[q^{±1}]` — or any ring carrying a `q = 1` evaluation
`φ : R →+* ℤ` — apply `φ`: the denominator becomes `2^k − 3`, so
`(2^k − 3)·φ(P) = 1`, i.e. `2^k − 3` is a unit of `ℤ`. But `2^k − 3 ∉ {±1}` for
`k ≥ 3`. **Contradiction — no one-odd-step cycle of period `k ≥ 3`.** (`k = 2` is
`EO`, the fundamental `{q⁻¹, 1+q⁻¹}`, where `(q+1)² − [3] = q` is a unit — the
one admissible case.)

This is the honest `q`-Steiner obstruction: the cycle denominator
`D_w = (q+1)^k − (q²+q+1)` has `q = 1` height `2^k − 3`, which the numerator
`n_w = 1` cannot match once `k ≥ 3`.
-/

namespace QOU.AppendixSurreals

/-- **Even chain collapse.** A chain of even steps `Pᵢ₊₁·(q+1) = Pᵢ` for `i < k`
    telescopes to `P₀ = (q+1)^k · P_k`. -/
theorem even_chain_collapse {R : Type*} [CommRing R] (q : R) (P : ℕ → R) :
    ∀ k : ℕ, (∀ i, i < k → P (i + 1) * (q + 1) = P i) →
      P 0 = (q + 1) ^ k * P k := by
  intro k
  induction k with
  | zero => intro _; simp
  | succ n ih =>
    intro hchain
    have hn : P (n + 1) * (q + 1) = P n := hchain n (Nat.lt_succ_self n)
    have h0 : P 0 = (q + 1) ^ n * P n :=
      ih (fun i hi => hchain i (Nat.lt_succ_of_lt hi))
    rw [h0, ← hn]
    ring

/-- **One-odd-step cycle forces the denominator equation.** The even chain plus
    the single odd step force `((q+1)^k − (q²+q+1))·P_{k-1} = 1`. -/
theorem qcollatz_one_odd_forces {R : Type*} [CommRing R] (q : R) (P : ℕ → R)
    (k : ℕ) (hk : 1 ≤ k)
    (hchain : ∀ i, i < k - 1 → P (i + 1) * (q + 1) = P i)
    (hodd : P 0 * (q + 1) = (q ^ 2 + q + 1) * P (k - 1) + 1) :
    ((q + 1) ^ k - (q ^ 2 + q + 1)) * P (k - 1) = 1 := by
  have hcollapse : P 0 = (q + 1) ^ (k - 1) * P (k - 1) :=
    even_chain_collapse q P (k - 1) hchain
  have hk' : (k - 1) + 1 = k := Nat.succ_pred_eq_of_pos hk
  have hpow : (q + 1) ^ k = (q + 1) * (q + 1) ^ (k - 1) := by
    rw [← pow_succ', hk']
  linear_combination hodd - (q + 1) * hcollapse + P (k - 1) * hpow

/-- **No one-odd-step cycle of period `k ≥ 3`.** Given any `q = 1` evaluation
    `φ : R →+* ℤ`, the forced denominator equation `((q+1)^k−(q²+q+1))·P = 1`
    maps to `(2^k − 3)·φ(P) = 1`, making `2^k − 3` a unit of `ℤ`; but
    `2^k − 3 ∉ {±1}` for `k ≥ 3`. So the family `E^{k-1}O` has no nontrivial
    cycle at any period `k ≥ 3` — an infinite family, via the `q = 1` height. -/
theorem qcollatz_no_one_odd_cycle {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (q P : R) (hq : φ q = 1) (k : ℕ) (hk : 3 ≤ k)
    (h : ((q + 1) ^ k - (q ^ 2 + q + 1)) * P = 1) : False := by
  have hcong := congrArg φ h
  simp only [map_mul, map_sub, map_pow, map_add, map_one, hq] at hcong
  norm_num at hcong
  -- hcong : (2 ^ k - 3) * φ P = 1
  have hu : IsUnit ((2 : ℤ) ^ k - 3) := isUnit_of_mul_eq_one _ _ hcong
  rw [Int.isUnit_iff] at hu
  have h8 : (8 : ℤ) ≤ 2 ^ k := by
    calc (8 : ℤ) = 2 ^ 3 := by norm_num
      _ ≤ 2 ^ k := pow_le_pow_right₀ (by norm_num) hk
  omega

/-! ### The generic `q = 1` height obstruction, and the two-odd-step family

The `q = 1` evaluation is the reusable engine: a cycle forcing `D·P = n` maps to
`φ(D) ∣ φ(n)` in `ℤ`, so a `q = 1` height with `φ(D) ∤ φ(n)` excludes it. -/

/-- **Generic `q = 1` height obstruction.** If a cycle forces `D·P = n` and some
    `q = 1` evaluation `φ : R →+* ℤ` has `φ(D) ∤ φ(n)`, there is no such cycle. -/
theorem no_cycle_of_q_one_height {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (D P n : R) (h : D * P = n) (hnd : ¬ (φ D ∣ φ n)) : False :=
  hnd ⟨φ P, by rw [← map_mul, h]⟩

/-- **Two adjacent odd steps force their denominator equation.** The word
    `E^{k-2}OO` forces `((q+1)^k − (q²+q+1)²)·P_{k-2} = q²+2q+2`. -/
theorem qcollatz_two_odd_adj_forces {R : Type*} [CommRing R] (q : R) (P : ℕ → R)
    (k : ℕ) (hk : 2 ≤ k)
    (hchain : ∀ i, i < k - 2 → P (i + 1) * (q + 1) = P i)
    (hodd1 : P (k - 1) * (q + 1) = (q ^ 2 + q + 1) * P (k - 2) + 1)
    (hodd2 : P 0 * (q + 1) = (q ^ 2 + q + 1) * P (k - 1) + 1) :
    ((q + 1) ^ k - (q ^ 2 + q + 1) ^ 2) * P (k - 2) = q ^ 2 + 2 * q + 2 := by
  have hcollapse : P 0 = (q + 1) ^ (k - 2) * P (k - 2) :=
    even_chain_collapse q P (k - 2) hchain
  have hk2 : 2 + (k - 2) = k := by omega
  have hpow : (q + 1) ^ k = (q + 1) ^ 2 * (q + 1) ^ (k - 2) := by
    rw [← pow_add, hk2]
  linear_combination -(q + 1) ^ 2 * hcollapse + (q ^ 2 + q + 1) * hodd1
    + (q + 1) * hodd2 + P (k - 2) * hpow

/-- **No two-adjacent-odd-step cycle of period `k ≥ 4`.** The `q = 1` height of the
    denominator `(q+1)^k − (q²+q+1)²` is `2^k − 9`, against numerator height `5`;
    but `2^k − 9 ∤ 5` for `k ≥ 4` (`|2^k − 9| ≥ 7 > 5`). A second infinite family,
    by the same height engine. (`k = 3` is `EOO`, handled by the period-3
    word-elimination, where `2³ − 9 = −1` is a unit.) -/
theorem qcollatz_no_two_odd_adj_cycle {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (q P : R) (hq : φ q = 1) (k : ℕ) (hk : 4 ≤ k)
    (h : ((q + 1) ^ k - (q ^ 2 + q + 1) ^ 2) * P = q ^ 2 + 2 * q + 2) : False := by
  refine no_cycle_of_q_one_height φ _ P _ h ?_
  intro hdvd
  simp only [map_sub, map_pow, map_add, map_mul, map_ofNat, map_one, hq] at hdvd
  norm_num at hdvd
  -- hdvd : (2 ^ k - 9) ∣ 5
  have h16 : (16 : ℤ) ≤ 2 ^ k := by
    calc (16 : ℤ) = 2 ^ 4 := by norm_num
      _ ≤ 2 ^ k := pow_le_pow_right₀ (by norm_num) hk
  have hle := Int.le_of_dvd (by norm_num) hdvd
  omega

/-! ### The general adjacent-tail family `E^{k-m}O^m`

Both families above are the `m = 1, 2` cases of the tail of `m` consecutive odd
steps. In general it forces `((q+1)^k − (q²+q+1)^m)·P = Sₘ`, where
`Sₘ = Σ_{j<m} (q²+q+1)^j (q+1)^{m-1-j}` has `q=1` height `3^m − 2^m`. The
denominator height is `2^k − 3^m`; since `|3^m − 2^m| < 3^m < 2^k − 3^m` once
`2^k > 2·3^m` (enough even steps to be contractive), the divisibility fails —
**the whole family `E^{k-m}O^m` is excluded when `2^k > 2·3^m`.** -/

/-- `Sₘ = Σ_{j<m} [3]^j (q+1)^{m-1-j}`, via `Sₘ₊₁ = [3]·Sₘ + (q+1)^m`, `S₀ = 0`. -/
def oddTailSum {R : Type*} [CommRing R] (q : R) : ℕ → R
  | 0 => 0
  | m + 1 => (q ^ 2 + q + 1) * oddTailSum q m + (q + 1) ^ m

/-- **Odd chain closed form.** An `m`-step odd chain `Qⱼ₊₁(q+1) = [3]Qⱼ + 1`
    satisfies `(q+1)^m · Q_m = [3]^m · Q₀ + Sₘ`. -/
theorem odd_chain_collapse {R : Type*} [CommRing R] (q : R) (Q : ℕ → R) :
    ∀ m : ℕ, (∀ j, j < m → Q (j + 1) * (q + 1) = (q ^ 2 + q + 1) * Q j + 1) →
      (q + 1) ^ m * Q m = (q ^ 2 + q + 1) ^ m * Q 0 + oddTailSum q m := by
  intro m
  induction m with
  | zero => intro _; simp [oddTailSum]
  | succ n ih =>
    intro hodd
    have hn : Q (n + 1) * (q + 1) = (q ^ 2 + q + 1) * Q n + 1 :=
      hodd n (Nat.lt_succ_self n)
    have hprev := ih (fun j hj => hodd j (Nat.lt_succ_of_lt hj))
    simp only [oddTailSum, pow_succ]
    linear_combination (q + 1) ^ n * hn + (q ^ 2 + q + 1) * hprev

/-- **`q=1` height of `Sₘ` is `3^m − 2^m`.** -/
theorem oddTailSum_map {R : Type*} [CommRing R] (φ : R →+* ℤ) (q : R) (hq : φ q = 1) :
    ∀ m : ℕ, φ (oddTailSum q m) = 3 ^ m - 2 ^ m := by
  intro m
  induction m with
  | zero => simp [oddTailSum]
  | succ n ih =>
    simp only [oddTailSum, map_add, map_mul, map_pow, map_one, hq]
    rw [ih]; ring

/-- **General adjacent-tail forcing.** For an `m`-step odd chain `Q` closing via an
    even tail of length `k−m` (`Q_m = (q+1)^{k-m}·Q₀`), the cycle forces
    `((q+1)^k − (q²+q+1)^m)·Q₀ = Sₘ`. -/
theorem qcollatz_adj_tail_forces {R : Type*} [CommRing R] (q : R) (Q : ℕ → R)
    (k m : ℕ) (hmk : m ≤ k)
    (hodd : ∀ j, j < m → Q (j + 1) * (q + 1) = (q ^ 2 + q + 1) * Q j + 1)
    (hclose : Q m = (q + 1) ^ (k - m) * Q 0) :
    ((q + 1) ^ k - (q ^ 2 + q + 1) ^ m) * Q 0 = oddTailSum q m := by
  have hcol := odd_chain_collapse q Q m hodd
  rw [hclose] at hcol
  have hpow : (q + 1) ^ m * (q + 1) ^ (k - m) = (q + 1) ^ k := by
    rw [← pow_add]; congr 1; omega
  rw [← mul_assoc, hpow] at hcol
  linear_combination hcol

/-- **No adjacent-tail cycle when `2^k > 2·3^m`.** The `q=1` height of the
    denominator is `2^k − 3^m`, against numerator height `3^m − 2^m`; the
    contractive bound `2·3^m < 2^k` forces `2^k − 3^m > 3^m − 2^m > 0`, so the
    divisibility fails. Excludes the entire `E^{k-m}O^m` family in that range —
    the general infinite result subsuming the one- and two-odd-step cases. -/
theorem qcollatz_no_adj_tail_cycle {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (q Q0 : R) (hq : φ q = 1) (k m : ℕ) (hm : 1 ≤ m) (hbig : 2 * 3 ^ m < 2 ^ k)
    (h : ((q + 1) ^ k - (q ^ 2 + q + 1) ^ m) * Q0 = oddTailSum q m) : False := by
  refine no_cycle_of_q_one_height φ _ Q0 _ h ?_
  intro hdvd
  rw [oddTailSum_map φ q hq] at hdvd
  simp only [map_sub, map_pow, map_add, map_one, hq] at hdvd
  norm_num at hdvd
  -- hdvd : (2^k - 3^m) ∣ (3^m - 2^m)
  have hbigZ : (2 : ℤ) * 3 ^ m < 2 ^ k := by exact_mod_cast hbig
  have h23 : (2 : ℤ) ^ m < 3 ^ m := by
    apply pow_lt_pow_left₀ (by norm_num) (by norm_num) (by omega)
  have hpos : (0 : ℤ) < 3 ^ m - 2 ^ m := by omega
  have h2m : (0 : ℤ) < 2 ^ m := by positivity
  have hle := Int.le_of_dvd hpos hdvd
  omega

/-! ### Non-adjacent two-odd words `E^a O E^b O`

Beyond the adjacent tail: two odd steps separated by even runs of any lengths
`a, b`. This forces `((q+1)^{a+b+2} − (q²+q+1)²)·x = (q²+q+1) + (q+1)^{b+1}`, whose
`q=1` height is `3 + 2^{b+1}` against denominator height `2^{a+b+2} − 9`. Once the
period `k = a+b+2 ≥ 5`, the denominator height exceeds the (positive) numerator
height for **every** arrangement `b`, so the divisibility fails — **all two-odd
words of period `k ≥ 5` are excluded**, adjacent or not. -/

/-- **Two separated odd steps force their denominator equation.** `E^a O E^b O`
    forces `((q+1)^{a+b+2} − (q²+q+1)²)·x = (q²+q+1) + (q+1)^{b+1}`. -/
theorem qcollatz_two_odd_forces {R : Type*} [CommRing R] (q x m1 m2 P0 : R)
    (a b : ℕ)
    (heven1 : P0 = (q + 1) ^ a * x)
    (hodd1 : m1 * (q + 1) = (q ^ 2 + q + 1) * x + 1)
    (heven2 : m1 = (q + 1) ^ b * m2)
    (hodd2 : P0 * (q + 1) = (q ^ 2 + q + 1) * m2 + 1) :
    ((q + 1) ^ (a + b + 2) - (q ^ 2 + q + 1) ^ 2) * x
      = (q ^ 2 + q + 1) + (q + 1) ^ (b + 1) := by
  have ha1 : (q + 1) ^ (a + 1) = (q + 1) * (q + 1) ^ a := by rw [pow_succ']
  have hb1 : (q + 1) ^ (b + 1) = (q + 1) * (q + 1) ^ b := by rw [pow_succ']
  have hpow : (q + 1) ^ (a + b + 2) = (q + 1) ^ (a + 1) * (q + 1) ^ (b + 1) := by
    rw [← pow_add]; congr 1; omega
  have e1 : (q + 1) ^ (a + 1) * x = (q ^ 2 + q + 1) * m2 + 1 := by
    have h2 := hodd2
    rw [heven1] at h2
    rw [ha1]; linear_combination h2
  have e2 : (q + 1) ^ (b + 1) * m2 = (q ^ 2 + q + 1) * x + 1 := by
    have h1 := hodd1
    rw [heven2] at h1
    rw [hb1]; linear_combination h1
  linear_combination (q + 1) ^ (b + 1) * e1 + (q ^ 2 + q + 1) * e2 + x * hpow

/-- **No two-odd-step cycle of period `k ≥ 5`.** The `q=1` height of the
    denominator `2^{a+b+2} − 9` exceeds the numerator height `3 + 2^{b+1}` for
    every arrangement `b` once `a+b+2 ≥ 5`, so the divisibility fails. This
    excludes **all** two-odd-step words (adjacent or separated) of period `≥ 5`. -/
theorem qcollatz_no_two_odd_cycle {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (q x : R) (hq : φ q = 1) (a b : ℕ) (hk : 5 ≤ a + b + 2)
    (h : ((q + 1) ^ (a + b + 2) - (q ^ 2 + q + 1) ^ 2) * x
      = (q ^ 2 + q + 1) + (q + 1) ^ (b + 1)) : False := by
  refine no_cycle_of_q_one_height φ _ x _ h ?_
  intro hdvd
  simp only [map_sub, map_pow, map_add, map_one, hq] at hdvd
  norm_num at hdvd
  -- hdvd : (2^(a+b+2) - 9) ∣ (3 + 2^(b+1))
  have hk2 : (2 : ℤ) ^ (a + b + 2) = 2 * 2 ^ (a + b + 1) := by rw [pow_succ]; ring
  have hbc : (2 : ℤ) ^ (b + 1) ≤ 2 ^ (a + b + 1) :=
    pow_le_pow_right₀ (by norm_num) (by omega)
  have h16 : (16 : ℤ) ≤ 2 ^ (a + b + 1) := by
    calc (16 : ℤ) = 2 ^ 4 := by norm_num
      _ ≤ 2 ^ (a + b + 1) := pow_le_pow_right₀ (by norm_num) (by omega)
  have hle := Int.le_of_dvd (by positivity) hdvd
  omega

/-! ### Three-odd words `E^a O E^b O E^c O`

Three odd steps separated by even runs `a, b, c`. Chaining the three odd steps
through the even runs (via the same collapse mechanism) forces

    ((q+1)^{a+b+c+3} − (q²+q+1)³)·x
        = (q²+q+1)² + (q²+q+1)·(q+1)^{b+1} + (q+1)^{b+c+2}.

At `q = 1` (`s = q+1 ↦ 2`, `t = q²+q+1 ↦ 3`) the denominator height is
`2^k − 27` (`k = a+b+c+3`) and the numerator height is
`9 + 3·2^{b+1} + 2^{b+c+2}`.

**Honest wall (why three-odd is not a uniform one-shot like one/two-odd).**
For the one- and two-odd families the numerator height stayed *uniformly below*
the denominator height for every arrangement once the period cleared a small
threshold, so a single `k ≥ k₀` excluded the whole family. That fails here: the
worst arrangement `a = c = 0` gives numerator `9 + 3·2^{k-2} + 2^{k-1}
= 9 + 5·2^{k-2}`, which *exceeds* the denominator `2^k − 27 = 4·2^{k-2} − 27`.
Those worst cases are exactly the **clustered** words — `O E^{k-3} O O` and its
kin are rotations of the adjacent tail `E^{k-3}O³`, already excluded by
`qcollatz_no_adj_tail_cycle` (a cycle is a *cyclic* word: `D_w` is
rotation-invariant, so one representative per rotation class suffices). What the
`q = 1` height obstruction adds here is the **spread** arrangements: a leading
even run `a ≥ 3` makes the denominator dominate `16×` the top numerator term, so
the divisibility fails and the word is excluded. The two lemmas below give the
general forced equation and the honest exclusion (conditional height, then the
clean `a ≥ 3` corollary). -/

/-- **Three separated odd steps force their denominator equation.**
    `E^a O E^b O E^c O` (even runs `a, b, c`, three odd steps) forces
    `((q+1)^{a+b+c+3} − (q²+q+1)³)·x
        = (q²+q+1)² + (q²+q+1)·(q+1)^{b+1} + (q+1)^{b+c+2}`. The variables
    `m2, m4` are the two intermediate cycle values entering the second and third
    odd steps; `heven*`/`hodd*` are the even-collapse and odd-step relations. -/
theorem qcollatz_three_odd_forces {R : Type*} [CommRing R]
    (q x m1 m2 m3 m4 P0 : R) (a b c : ℕ)
    (heven1 : P0 = (q + 1) ^ a * x)
    (hodd1 : m1 * (q + 1) = (q ^ 2 + q + 1) * x + 1)
    (heven2 : m1 = (q + 1) ^ b * m2)
    (hodd2 : m3 * (q + 1) = (q ^ 2 + q + 1) * m2 + 1)
    (heven3 : m3 = (q + 1) ^ c * m4)
    (hodd3 : P0 * (q + 1) = (q ^ 2 + q + 1) * m4 + 1) :
    ((q + 1) ^ (a + b + c + 3) - (q ^ 2 + q + 1) ^ 3) * x
      = (q ^ 2 + q + 1) ^ 2 + (q ^ 2 + q + 1) * (q + 1) ^ (b + 1)
        + (q + 1) ^ (b + c + 2) := by
  have ha1 : (q + 1) ^ (a + 1) = (q + 1) * (q + 1) ^ a := by rw [pow_succ']
  have hb1 : (q + 1) ^ (b + 1) = (q + 1) * (q + 1) ^ b := by rw [pow_succ']
  have hc1 : (q + 1) ^ (c + 1) = (q + 1) * (q + 1) ^ c := by rw [pow_succ']
  have hP2 : (q + 1) ^ (a + b + c + 3) = (q + 1) ^ (a + 1) * (q + 1) ^ (b + c + 2) := by
    rw [← pow_add]; congr 1; omega
  have hP1 : (q + 1) ^ (b + c + 2) = (q + 1) ^ (b + 1) * (q + 1) ^ (c + 1) := by
    rw [← pow_add]; congr 1; omega
  -- e1 : s^{a+1}·x = t·m4 + 1  (leading even run + last odd step)
  have e1 : (q + 1) ^ (a + 1) * x = (q ^ 2 + q + 1) * m4 + 1 := by
    have h3 := hodd3; rw [heven1] at h3; rw [ha1]; linear_combination h3
  -- e2 : s^{b+1}·m2 = t·x + 1  (first odd step + its even run)
  have e2 : (q + 1) ^ (b + 1) * m2 = (q ^ 2 + q + 1) * x + 1 := by
    have h1 := hodd1; rw [heven2] at h1; rw [hb1]; linear_combination h1
  -- e3 : s^{c+1}·m4 = t·m2 + 1  (second odd step + its even run)
  have e3 : (q + 1) ^ (c + 1) * m4 = (q ^ 2 + q + 1) * m2 + 1 := by
    have h2 := hodd2; rw [heven3] at h2; rw [hc1]; linear_combination h2
  linear_combination (q + 1) ^ (b + c + 2) * e1 + (q ^ 2 + q + 1) ^ 2 * e2
    + (q ^ 2 + q + 1) * (q + 1) ^ (b + 1) * e3
    + x * hP2 + (q ^ 2 + q + 1) * m4 * hP1

/-- **No three-odd-step cycle when the height obstruction fires.** Given the
    explicit `q = 1` height gap `9 + 3·2^{b+1} + 2^{b+c+2} < 2^{a+b+c+3} − 27`
    (numerator height strictly below denominator height), the forced equation has
    no solution: `2^{a+b+c+3} − 27` cannot divide the smaller positive numerator.
    This is the honest general application — it fires for the *spread*
    arrangements; the clustered ones are rotations of tails (see
    `qcollatz_no_adj_tail_cycle`). -/
theorem qcollatz_no_three_odd_cycle {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (q x : R) (hq : φ q = 1) (a b c : ℕ)
    (hcond : (9 : ℤ) + 3 * 2 ^ (b + 1) + 2 ^ (b + c + 2) < 2 ^ (a + b + c + 3) - 27)
    (h : ((q + 1) ^ (a + b + c + 3) - (q ^ 2 + q + 1) ^ 3) * x
      = (q ^ 2 + q + 1) ^ 2 + (q ^ 2 + q + 1) * (q + 1) ^ (b + 1)
        + (q + 1) ^ (b + c + 2)) : False := by
  refine no_cycle_of_q_one_height φ _ x _ h ?_
  intro hdvd
  simp only [map_sub, map_pow, map_add, map_mul, map_one, hq] at hdvd
  norm_num at hdvd
  -- hdvd : (2^(a+b+c+3) - 27) ∣ (9 + 3·2^(b+1) + 2^(b+c+2))
  have hpos : (0 : ℤ) < 9 + 3 * 2 ^ (b + 1) + 2 ^ (b + c + 2) := by positivity
  have hle := Int.le_of_dvd hpos hdvd
  omega

/-- **No three-odd-step cycle with leading even run `a ≥ 3`.** A clean
    unconditional exclusion: when the leading run is `a ≥ 3` the denominator
    height `2^{a+b+c+3} − 27` dominates the numerator height (`2^{a+1} ≥ 16` times
    the top term), so the height gap of `qcollatz_no_three_odd_cycle` holds for
    every `b, c`. By rotation-invariance of cycles this excludes every three-odd
    word possessing an even run of length `≥ 3` — the generic spread regime. -/
theorem qcollatz_no_three_odd_cycle_of_lead {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (q x : R) (hq : φ q = 1) (a b c : ℕ) (ha : 3 ≤ a)
    (h : ((q + 1) ^ (a + b + c + 3) - (q ^ 2 + q + 1) ^ 3) * x
      = (q ^ 2 + q + 1) ^ 2 + (q ^ 2 + q + 1) * (q + 1) ^ (b + 1)
        + (q + 1) ^ (b + c + 2)) : False := by
  refine qcollatz_no_three_odd_cycle φ q x hq a b c ?_ h
  have hexp : a + 1 + (b + c + 2) = a + b + c + 3 := by omega
  have hsplit : (2 : ℤ) ^ (a + b + c + 3) = 2 ^ (a + 1) * 2 ^ (b + c + 2) := by
    rw [← pow_add, hexp]
  have h16 : (16 : ℤ) ≤ 2 ^ (a + 1) := by
    calc (16 : ℤ) = 2 ^ 4 := by norm_num
      _ ≤ 2 ^ (a + 1) := pow_le_pow_right₀ (by norm_num) (by omega)
  have hC2 : (4 : ℤ) ≤ 2 ^ (b + c + 2) := by
    calc (4 : ℤ) = 2 ^ 2 := by norm_num
      _ ≤ 2 ^ (b + c + 2) := pow_le_pow_right₀ (by norm_num) (by omega)
  have hB1 : (2 : ℤ) ^ (b + 1) ≤ 2 ^ (b + c + 2) :=
    pow_le_pow_right₀ (by norm_num) (by omega)
  have hAC : (16 : ℤ) * 2 ^ (b + c + 2) ≤ 2 ^ (a + b + c + 3) := by
    rw [hsplit]; exact mul_le_mul_of_nonneg_right h16 (by positivity)
  omega

/-! ### Four separated odd steps (`k_odd = 4`)

One more rung of the `q`-Steiner ladder, by the same telescoping. The forced
equation and the leading-run exclusion carry over verbatim with `m = 4`; the
denominator height is `2^k − 3⁴ = 2^k − 81` and the leading-run threshold rises
to `a ≥ 4` (since `3⁴ = 81 ≤ 2^{a+3}` needs `a + 3 ≥ 7`). This closes another
infinite family of spread four-odd words. The **uniform-`m`** statement — a
single theorem over every `k_odd` — is the remaining `q`-Steiner endgame; each
rung here (`m = 1, 2, 3, 4`) is one instance of it. -/

/-- **Four separated odd steps force their denominator equation.**
    `E^a O E^b O E^c O E^d O` (four odd steps, even runs `a, b, c, d`) forces
    `((q+1)^{a+b+c+d+4} − (q²+q+1)⁴)·x
        = (q²+q+1)³ + (q²+q+1)²·(q+1)^{b+1} + (q²+q+1)·(q+1)^{b+c+2}
          + (q+1)^{b+c+d+3}`. The `mᵢ` are the intermediate cycle values;
    `heven*`/`hodd*` are the even-collapse and odd-step relations, chained
    cyclically. Same telescoping as `qcollatz_three_odd_forces`, one level
    deeper. -/
theorem qcollatz_four_odd_forces {R : Type*} [CommRing R]
    (q x m1 m2 m3 m4 m5 m6 P0 : R) (a b c d : ℕ)
    (heven1 : P0 = (q + 1) ^ a * x)
    (hodd1 : m1 * (q + 1) = (q ^ 2 + q + 1) * x + 1)
    (heven2 : m1 = (q + 1) ^ b * m2)
    (hodd2 : m3 * (q + 1) = (q ^ 2 + q + 1) * m2 + 1)
    (heven3 : m3 = (q + 1) ^ c * m4)
    (hodd3 : m5 * (q + 1) = (q ^ 2 + q + 1) * m4 + 1)
    (heven4 : m5 = (q + 1) ^ d * m6)
    (hodd4 : P0 * (q + 1) = (q ^ 2 + q + 1) * m6 + 1) :
    ((q + 1) ^ (a + b + c + d + 4) - (q ^ 2 + q + 1) ^ 4) * x
      = (q ^ 2 + q + 1) ^ 3 + (q ^ 2 + q + 1) ^ 2 * (q + 1) ^ (b + 1)
        + (q ^ 2 + q + 1) * (q + 1) ^ (b + c + 2) + (q + 1) ^ (b + c + d + 3) := by
  have ha1 : (q + 1) ^ (a + 1) = (q + 1) * (q + 1) ^ a := by rw [pow_succ']
  have hb1 : (q + 1) ^ (b + 1) = (q + 1) * (q + 1) ^ b := by rw [pow_succ']
  have hc1 : (q + 1) ^ (c + 1) = (q + 1) * (q + 1) ^ c := by rw [pow_succ']
  have hd1 : (q + 1) ^ (d + 1) = (q + 1) * (q + 1) ^ d := by rw [pow_succ']
  -- e1 : s^{a+1}·x = t·m6 + 1  (leading even run + last odd step)
  have e1 : (q + 1) ^ (a + 1) * x = (q ^ 2 + q + 1) * m6 + 1 := by
    have h4 := hodd4; rw [heven1] at h4; rw [ha1]; linear_combination h4
  -- e2 : s^{b+1}·m2 = t·x + 1
  have e2 : (q + 1) ^ (b + 1) * m2 = (q ^ 2 + q + 1) * x + 1 := by
    have h1 := hodd1; rw [heven2] at h1; rw [hb1]; linear_combination h1
  -- e3 : s^{c+1}·m4 = t·m2 + 1
  have e3 : (q + 1) ^ (c + 1) * m4 = (q ^ 2 + q + 1) * m2 + 1 := by
    have h2 := hodd2; rw [heven3] at h2; rw [hc1]; linear_combination h2
  -- e4 : s^{d+1}·m6 = t·m4 + 1
  have e4 : (q + 1) ^ (d + 1) * m6 = (q ^ 2 + q + 1) * m4 + 1 := by
    have h3 := hodd3; rw [heven4] at h3; rw [hd1]; linear_combination h3
  -- Power-split helpers so `ring` can reconcile summed vs product exponents.
  have hPA : (q + 1) ^ (a + b + c + d + 4)
      = (q + 1) ^ (a + 1) * (q + 1) ^ (b + c + d + 3) := by rw [← pow_add]; congr 1; omega
  have hPB : (q + 1) ^ (b + c + 2)
      = (q + 1) ^ (b + 1) * (q + 1) ^ (c + 1) := by rw [← pow_add]; congr 1; omega
  have hPC : (q + 1) ^ (b + c + d + 3)
      = (q + 1) ^ (b + c + 2) * (q + 1) ^ (d + 1) := by rw [← pow_add]; congr 1; omega
  linear_combination (q + 1) ^ (b + c + d + 3) * e1 + (q ^ 2 + q + 1) ^ 3 * e2
    + (q ^ 2 + q + 1) ^ 2 * (q + 1) ^ (b + 1) * e3
    + (q ^ 2 + q + 1) * (q + 1) ^ (b + c + 2) * e4
    + x * hPA + (q ^ 2 + q + 1) ^ 2 * m4 * hPB + (q ^ 2 + q + 1) * m6 * hPC

/-- **No four-odd-step cycle when the height obstruction fires.** Given the
    explicit `q = 1` height gap
    `27 + 9·2^{b+1} + 3·2^{b+c+2} + 2^{b+c+d+3} < 2^{a+b+c+d+4} − 81`, the forced
    equation has no solution: the denominator `2^{a+b+c+d+4} − 81` cannot divide
    the strictly-smaller positive numerator. Fires for the spread arrangements. -/
theorem qcollatz_no_four_odd_cycle {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (q x : R) (hq : φ q = 1) (a b c d : ℕ)
    (hcond : (27 : ℤ) + 9 * 2 ^ (b + 1) + 3 * 2 ^ (b + c + 2) + 2 ^ (b + c + d + 3)
      < 2 ^ (a + b + c + d + 4) - 81)
    (h : ((q + 1) ^ (a + b + c + d + 4) - (q ^ 2 + q + 1) ^ 4) * x
      = (q ^ 2 + q + 1) ^ 3 + (q ^ 2 + q + 1) ^ 2 * (q + 1) ^ (b + 1)
        + (q ^ 2 + q + 1) * (q + 1) ^ (b + c + 2) + (q + 1) ^ (b + c + d + 3)) : False := by
  refine no_cycle_of_q_one_height φ _ x _ h ?_
  intro hdvd
  simp only [map_sub, map_pow, map_add, map_mul, map_one, hq] at hdvd
  norm_num at hdvd
  have hpos : (0 : ℤ) < 27 + 9 * 2 ^ (b + 1) + 3 * 2 ^ (b + c + 2) + 2 ^ (b + c + d + 3) := by
    positivity
  have hle := Int.le_of_dvd hpos hdvd
  omega

/-- **No four-odd-step cycle with leading even run `a ≥ 4`.** Unconditional: when
    the leading run is `a ≥ 4` the denominator height `2^{a+b+c+d+4} − 81`
    dominates (`2^{a+1} ≥ 32` times the top numerator term), so the height gap of
    `qcollatz_no_four_odd_cycle` holds for every `b, c, d`. By rotation-invariance
    this excludes every four-odd word possessing an even run of length `≥ 4` — the
    generic spread regime for `k_odd = 4`. -/
theorem qcollatz_no_four_odd_cycle_of_lead {R : Type*} [CommRing R] (φ : R →+* ℤ)
    (q x : R) (hq : φ q = 1) (a b c d : ℕ) (ha : 4 ≤ a)
    (h : ((q + 1) ^ (a + b + c + d + 4) - (q ^ 2 + q + 1) ^ 4) * x
      = (q ^ 2 + q + 1) ^ 3 + (q ^ 2 + q + 1) ^ 2 * (q + 1) ^ (b + 1)
        + (q ^ 2 + q + 1) * (q + 1) ^ (b + c + 2) + (q + 1) ^ (b + c + d + 3)) : False := by
  refine qcollatz_no_four_odd_cycle φ q x hq a b c d ?_ h
  have hsplit : (2 : ℤ) ^ (a + b + c + d + 4) = 2 ^ (a + 1) * 2 ^ (b + c + d + 3) := by
    rw [← pow_add]; congr 1; omega
  have h32 : (32 : ℤ) ≤ 2 ^ (a + 1) := by
    calc (32 : ℤ) = 2 ^ 5 := by norm_num
      _ ≤ 2 ^ (a + 1) := pow_le_pow_right₀ (by norm_num) (by omega)
  have hM8 : (8 : ℤ) ≤ 2 ^ (b + c + d + 3) := by
    calc (8 : ℤ) = 2 ^ 3 := by norm_num
      _ ≤ 2 ^ (b + c + d + 3) := pow_le_pow_right₀ (by norm_num) (by omega)
  have hB1 : (2 : ℤ) ^ (b + 1) ≤ 2 ^ (b + c + d + 3) :=
    pow_le_pow_right₀ (by norm_num) (by omega)
  have hBC : (2 : ℤ) ^ (b + c + 2) ≤ 2 ^ (b + c + d + 3) :=
    pow_le_pow_right₀ (by norm_num) (by omega)
  have hAM : (32 : ℤ) * 2 ^ (b + c + d + 3) ≤ 2 ^ (a + b + c + d + 4) := by
    rw [hsplit]; exact mul_le_mul_of_nonneg_right h32 (by positivity)
  omega

/-! ### Uniform `q`-Steiner forced equation (any number of odd steps)

The rungs above (`m = 1, 2, 3, 4`) are instances of one statement. Encoding the
even runs as a function `r : ℕ → ℕ` and the cycle values as `v : ℕ → R`, the same
telescoping proves the forced equation for **every** `m` at once: a cyclic word
with `m` odd steps and runs `r 0, …, r (m-1)` pins its value by
`((q+1)^{S+m} − [3]^m)·v₀ = N_m`, where `S = runSum m = Σ_{i<m} r i` and `N_m` is
the `q`-Steiner numerator with recursion `N_{m+1} = [3]·N_m + (q+1)^{S_m + m}`.
This subsumes `qcollatz_{one,two,three,four}_odd_forces` (e.g. `m = 2` gives
`[3] + (q+1)^{r₀+1}`, matching `qcollatz_two_odd_forces`). Only the arithmetic
height bound on `N_m` stays arrangement-dependent — the algebra is uniform. -/

/-- Partial sum of the first `m` even runs, `runSum r m = r 0 + ⋯ + r (m-1)`. -/
def runSum (r : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | m + 1 => runSum r m + r m

/-- The `q`-Steiner numerator for a cyclic word of `m` odd steps with runs `r`:
    `N₀ = 0`, `N_{m+1} = [3]·N_m + (q+1)^{runSum m + m}`. -/
def genSteinerNum {R : Type*} [CommRing R] (q : R) (r : ℕ → ℕ) : ℕ → R
  | 0 => 0
  | m + 1 => (q ^ 2 + q + 1) * genSteinerNum q r m + (q + 1) ^ (runSum r m + m)

/-- **General odd-chain collapse (arbitrary even runs).** Given the per-step
    relations `(q+1)^{r i + 1}·v(i+1) = [3]·v i + 1`, the chain of `m` odd steps
    telescopes to `(q+1)^{runSum m + m}·v m = [3]^m·v 0 + N_m`. -/
theorem genOddChain {R : Type*} [CommRing R] (q : R) (v : ℕ → R) (r : ℕ → ℕ)
    (hrel : ∀ i, (q + 1) ^ (r i + 1) * v (i + 1) = (q ^ 2 + q + 1) * v i + 1) :
    ∀ m, (q + 1) ^ (runSum r m + m) * v m
      = (q ^ 2 + q + 1) ^ m * v 0 + genSteinerNum q r m := by
  intro m
  induction m with
  | zero => simp [genSteinerNum, runSum]
  | succ n ih =>
    have hsplit : runSum r (n + 1) + (n + 1) = (runSum r n + n) + (r n + 1) := by
      simp only [runSum]; omega
    have key : (q + 1) ^ (runSum r (n + 1) + (n + 1)) * v (n + 1)
        = (q ^ 2 + q + 1) * ((q + 1) ^ (runSum r n + n) * v n)
          + (q + 1) ^ (runSum r n + n) := by
      rw [hsplit, pow_add, mul_assoc, hrel n]; ring
    rw [key, ih]
    simp only [genSteinerNum, pow_succ]
    ring

/-- **Uniform `q`-Steiner forced equation.** A cyclic word (`v m = v 0`) of `m`
    odd steps with even runs `r` pins its value:
    `((q+1)^{runSum m + m} − [3]^m)·v 0 = N_m`. Specialises to every rung above. -/
theorem genForced {R : Type*} [CommRing R] (q : R) (v : ℕ → R) (r : ℕ → ℕ)
    (hrel : ∀ i, (q + 1) ^ (r i + 1) * v (i + 1) = (q ^ 2 + q + 1) * v i + 1)
    (m : ℕ) (hcyc : v m = v 0) :
    ((q + 1) ^ (runSum r m + m) - (q ^ 2 + q + 1) ^ m) * v 0 = genSteinerNum q r m := by
  have hchain := genOddChain q v r hrel m
  rw [hcyc] at hchain
  linear_combination hchain

/-- The `q = 1` image of the `q`-Steiner numerator: `M₀ = 0`,
    `M_{m+1} = 3·M_m + 2^{runSum m + m}`. This is `φ(N_m)` for any `q = 1`
    evaluation `φ` (see `genSteinerNum_map`). -/
def genSteinerNumZ (r : ℕ → ℕ) : ℕ → ℤ
  | 0 => 0
  | m + 1 => 3 * genSteinerNumZ r m + 2 ^ (runSum r m + m)

/-- **The `q = 1` evaluation sends `N_m` to `M_m`.** For any ring hom
    `φ : R →+* ℤ` with `φ q = 1`, `φ (genSteinerNum q r m) = genSteinerNumZ r m`. -/
theorem genSteinerNum_map {R : Type*} [CommRing R] (φ : R →+* ℤ) (q : R) (r : ℕ → ℕ)
    (hq : φ q = 1) (m : ℕ) : φ (genSteinerNum q r m) = genSteinerNumZ r m := by
  induction m with
  | zero => simp [genSteinerNum, genSteinerNumZ]
  | succ n ih =>
    simp only [genSteinerNum, genSteinerNumZ, map_add, map_mul, map_pow, map_one, hq]
    rw [ih]; norm_num

/-- **Uniform `q`-Steiner exclusion.** For any cyclic word of `m` odd steps whose
    `q = 1` numerator height `M_m = genSteinerNumZ r m` is positive and strictly
    below the denominator height `2^{runSum m + m} − 3^m`, there is no cycle: the
    denominator cannot divide the smaller positive numerator. This is the uniform
    engine — every rung's `no_*_cycle` is an instance (compute `M_m` and check the
    gap). The remaining `q`-Steiner content is purely arithmetic: which
    arrangements satisfy the gap. -/
theorem genNoCycle {R : Type*} [CommRing R] (φ : R →+* ℤ) (q : R) (v : ℕ → R)
    (r : ℕ → ℕ) (hq : φ q = 1)
    (hrel : ∀ i, (q + 1) ^ (r i + 1) * v (i + 1) = (q ^ 2 + q + 1) * v i + 1)
    (m : ℕ) (hcyc : v m = v 0)
    (hpos : 0 < genSteinerNumZ r m)
    (hlt : genSteinerNumZ r m < 2 ^ (runSum r m + m) - 3 ^ m) : False := by
  refine no_cycle_of_q_one_height φ _ (v 0) _ (genForced q v r hrel m hcyc) ?_
  intro hdvd
  simp only [map_sub, map_pow, map_add, map_one, hq,
    genSteinerNum_map φ q r hq] at hdvd
  norm_num at hdvd
  have hle := Int.le_of_dvd hpos hdvd
  omega

/-! ### Uniform spread exclusion — a large leading run excludes any `k_odd`

The per-rung `of_lead` corollaries (`qcollatz_no_{three,four}_odd_cycle_of_lead`)
all instantiate one fact: the `q = 1` numerator `M_{m+1} = genSteinerNumZ r (m+1)`
does **not** depend on the last even run `r m` (its recursion only reaches
`runSum r m`), while the denominator height `2^{runSum (m+1) + (m+1)} − 3^{m+1}`
grows with `r m`. So a large last run forces the height gap for **every**
arrangement of the other runs. Threshold: `3^{m+1} ≤ 2^{r m + m}`. This is the
uniform spread half of the `q`-Steiner endgame; the clustered case (all runs
small) is the finite residue. -/

/-- `0 ≤ M_m`. -/
theorem genSteinerNumZ_nonneg (r : ℕ → ℕ) (m : ℕ) : 0 ≤ genSteinerNumZ r m := by
  induction m with
  | zero => simp [genSteinerNumZ]
  | succ n ih =>
    have h2 : (0 : ℤ) ≤ 2 ^ (runSum r n + n) := by positivity
    simp only [genSteinerNumZ]; linarith

/-- `0 < M_{m+1}` — the numerator of a nonempty cyclic word is positive
    (discharges the `hpos` hypothesis of `genNoCycle`). -/
theorem genSteinerNumZ_pos (r : ℕ → ℕ) (m : ℕ) : 0 < genSteinerNumZ r (m + 1) := by
  have h2 : (0 : ℤ) < 2 ^ (runSum r m + m) := by positivity
  have h0 := genSteinerNumZ_nonneg r m
  simp only [genSteinerNumZ]; linarith

/-- **Loose bound** `M_m ≤ 2^{runSum m}·(3^m − 2^m)` (clean induction). -/
theorem genSteinerNumZ_le (r : ℕ → ℕ) (m : ℕ) :
    genSteinerNumZ r m ≤ 2 ^ runSum r m * (3 ^ m - 2 ^ m) := by
  induction m with
  | zero => simp [genSteinerNumZ]
  | succ n ih =>
    simp only [genSteinerNumZ]
    have e3 : (3 : ℤ) ^ (n + 1) = 3 * 3 ^ n := by rw [pow_succ]; ring
    have e2 : (2 : ℤ) ^ (n + 1) = 2 * 2 ^ n := by rw [pow_succ]; ring
    have hp : (2 : ℤ) ^ (runSum r n + n) = 2 ^ runSum r n * 2 ^ n := by rw [pow_add]
    have hmono : (2 : ℤ) ^ runSum r n ≤ 2 ^ runSum r (n + 1) := by
      apply pow_le_pow_right₀ (by norm_num); simp only [runSum]; omega
    have hge : (0 : ℤ) ≤ 3 ^ (n + 1) - 2 ^ (n + 1) := by
      have h23 : (2 : ℤ) ^ (n + 1) ≤ 3 ^ (n + 1) := by
        gcongr
        norm_num
      linarith
    have step1 : 3 * genSteinerNumZ r n + (2 : ℤ) ^ (runSum r n + n)
        ≤ 2 ^ runSum r n * (3 ^ (n + 1) - 2 ^ (n + 1)) := by
      rw [e3, e2, hp]
      nlinarith [ih, pow_nonneg (by norm_num : (0 : ℤ) ≤ 2) (runSum r n)]
    have step2 : (2 : ℤ) ^ runSum r n * (3 ^ (n + 1) - 2 ^ (n + 1))
        ≤ 2 ^ runSum r (n + 1) * (3 ^ (n + 1) - 2 ^ (n + 1)) :=
      mul_le_mul_of_nonneg_right hmono hge
    linarith [step1, step2]

/-- **Tight bound** `M_{m+1} ≤ 2^{runSum m}·(3^{m+1} − 2^{m+1})` — the numerator is
    bounded independently of the last run `r m` (only `runSum r m` enters). -/
theorem genSteinerNumZ_le_lead (r : ℕ → ℕ) (m : ℕ) :
    genSteinerNumZ r (m + 1) ≤ 2 ^ runSum r m * (3 ^ (m + 1) - 2 ^ (m + 1)) := by
  simp only [genSteinerNumZ]
  have ih := genSteinerNumZ_le r m
  have e3 : (3 : ℤ) ^ (m + 1) = 3 * 3 ^ m := by rw [pow_succ]; ring
  have e2 : (2 : ℤ) ^ (m + 1) = 2 * 2 ^ m := by rw [pow_succ]; ring
  have hp : (2 : ℤ) ^ (runSum r m + m) = 2 ^ runSum r m * 2 ^ m := by rw [pow_add]
  rw [e3, e2, hp]
  nlinarith [ih, pow_nonneg (by norm_num : (0 : ℤ) ≤ 2) (runSum r m)]

/-- **Uniform spread exclusion.** A cyclic word of `m + 1` odd steps whose last
    even run `r m` is large enough — `3^{m+1} ≤ 2^{r m + m}` — has **no cycle**,
    for ANY arrangement of the other runs. Subsumes every per-rung `of_lead`
    corollary at once (the spread half of the `q`-Steiner endgame). -/
theorem genNoCycle_of_lead {R : Type*} [CommRing R] (φ : R →+* ℤ) (q : R) (v : ℕ → R)
    (r : ℕ → ℕ) (hq : φ q = 1)
    (hrel : ∀ i, (q + 1) ^ (r i + 1) * v (i + 1) = (q ^ 2 + q + 1) * v i + 1)
    (m : ℕ) (hcyc : v (m + 1) = v 0)
    (hlead : (3 : ℤ) ^ (m + 1) ≤ 2 ^ (r m + m)) : False := by
  refine genNoCycle φ q v r hq hrel (m + 1) hcyc (genSteinerNumZ_pos r m) ?_
  have htight := genSteinerNumZ_le_lead r m
  have hden : (2 : ℤ) ^ (runSum r (m + 1) + (m + 1))
      = 2 ^ runSum r m * (2 * 2 ^ (r m + m)) := by
    have : runSum r (m + 1) + (m + 1) = runSum r m + (r m + m) + 1 := by
      simp only [runSum]; omega
    rw [this, pow_succ, pow_add]; ring
  rw [hden]
  have hP0 : (0 : ℤ) ≤ 2 ^ runSum r m := by positivity
  have hP1 : (1 : ℤ) ≤ 2 ^ runSum r m := by
    simpa using pow_le_pow_right₀ (by norm_num : (1 : ℤ) ≤ 2) (Nat.zero_le (runSum r m))
  have hAmul : (2 : ℤ) ^ runSum r m * 3 ^ (m + 1)
      ≤ 2 ^ runSum r m * 2 ^ (r m + m) := mul_le_mul_of_nonneg_left hlead hP0
  have hAle : (2 : ℤ) ^ (r m + m) ≤ 2 ^ runSum r m * 2 ^ (r m + m) := by
    nlinarith [hP1, pow_nonneg (by norm_num : (0 : ℤ) ≤ 2) (r m + m)]
  have h2pos : (0 : ℤ) < 2 ^ runSum r m * 2 ^ (m + 1) := by positivity
  have e2 : (2 : ℤ) ^ (m + 1) = 2 * 2 ^ m := by rw [pow_succ]; ring
  nlinarith [htight, hAmul, hAle, h2pos, hlead, e2,
             pow_nonneg (by norm_num : (0 : ℤ) ≤ 2) (r m + m)]

/-! ### Clustered-residue finiteness, lower height bound, and divisibility exclusion (`qou-4ocd`)

When `genNoCycle_of_lead` does not fire on any rotation of a cyclic word of `m`
odd steps, every even run `r i` satisfies `2 ^ (r i + m - 1) < 3 ^ m`, so each
`r i` is bounded above by a constant `B` depending only on `m`. The theorem
`runSum_le_of_bounded` bounds the total even-run sum `runSum r m ≤ m * B`,
certifying that the clustered residue for each fixed `m` is finite. Within that
finite clustered residue, `genSteinerNumZ_ge_lower` proves `3^m - 2^m ≤ M_m`,
and `genNoCycle_of_nondiv` discharges any clustered word whose `q = 1` height
fails integer divisibility `(2^{runSum r m + m} - 3^m) ∣ M_m`. -/

/-- If every even run is bounded by `B`, the total even-run sum over `m` odd
    steps obeys `runSum r m ≤ m * B`. -/
theorem runSum_le_of_bounded (r : ℕ → ℕ) (B : ℕ) (hb : ∀ i, r i ≤ B) (m : ℕ) :
    runSum r m ≤ m * B := by
  induction m with
  | zero =>
    simp only [runSum, Nat.zero_mul, le_refl]
  | succ n ih =>
    have hn := hb n
    simp only [runSum]
    calc runSum r n + r n ≤ n * B + B := Nat.add_le_add ih hn
      _ = (n + 1) * B := by ring

/-- Exact lower bound `3^m - 2^m ≤ genSteinerNumZ r m` for any even-run profile `r`. -/
theorem genSteinerNumZ_ge_lower (r : ℕ → ℕ) (m : ℕ) :
    (3 : ℤ) ^ m - 2 ^ m ≤ genSteinerNumZ r m := by
  induction m with
  | zero =>
    simp only [genSteinerNumZ, pow_zero, sub_self, le_refl]
  | succ n ih =>
    simp only [genSteinerNumZ]
    have hpow : (2 : ℤ) ^ n ≤ 2 ^ (runSum r n + n) :=
      pow_le_pow_right₀ (by norm_num) (by omega)
    have e3 : (3 : ℤ) ^ (n + 1) = 3 * 3 ^ n := by rw [pow_succ]; ring
    have e2 : (2 : ℤ) ^ (n + 1) = 2 * 2 ^ n := by rw [pow_succ]; ring
    linarith

/-- **Clustered-residue divisibility exclusion.** Even when a word lies inside
    the clustered regime (`2^{r m + m} < 3^{m+1}`) where `genNoCycle_of_lead`
    does not apply, if `(2^{runSum r m + m} - 3^m)` does not divide
    `genSteinerNumZ r m` in `ℤ`, then no cycle exists. -/
theorem genNoCycle_of_nondiv {R : Type*} [CommRing R] (φ : R →+* ℤ) (q : R) (v : ℕ → R)
    (r : ℕ → ℕ) (hq : φ q = 1)
    (hrel : ∀ i, (q + 1) ^ (r i + 1) * v (i + 1) = (q ^ 2 + q + 1) * v i + 1)
    (m : ℕ) (hcyc : v m = v 0)
    (hndvd : ¬ ((2 : ℤ) ^ (runSum r m + m) - 3 ^ m ∣ genSteinerNumZ r m)) : False := by
  refine no_cycle_of_q_one_height φ _ (v 0) _ (genForced q v r hrel m hcyc) ?_
  intro hdvd
  simp only [map_sub, map_pow, map_add, map_one, hq,
    genSteinerNum_map φ q r hq] at hdvd
  norm_num at hdvd
  exact hndvd hdvd

end QOU.AppendixSurreals
