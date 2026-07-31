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

end QOU.AppendixSurreals
