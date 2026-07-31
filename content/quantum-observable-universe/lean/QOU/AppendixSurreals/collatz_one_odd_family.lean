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

end QOU.AppendixSurreals
