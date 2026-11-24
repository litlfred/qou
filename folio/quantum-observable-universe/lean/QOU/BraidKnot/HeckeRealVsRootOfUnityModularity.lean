import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Hecke / Temperley–Lieb Modularity Split: Real `q > 1` vs Root-of-Unity Quotient (`hkmt`)

Resolves the mathematical bifurcation identified in the applicability review of bean `hkmt`
(`BWH-1: the Hecke category as a modular tensor category (S, T from Markov trace)`):

1. **Exact root-of-unity truncation criterion (`symQInt_eq_zero_iff_pow_two_mul_eq_one`, §7c
   over any `[Field K]`).** For `q ≠ 0` with `q - q⁻¹ ≠ 0`, the symmetric quantum integer
   `[n]_q = (q^n - q⁻ⁿ)/(q - q⁻¹)` satisfies `(q - q⁻¹) · [n]_q = q^n - (q⁻¹)^n`, and hence
   vanishes (`[ℓ]_q = 0`, killing the `(ℓ - 1)`-st Jones–Wenzl idempotent so the
   semisimplified Temperley–Lieb / `U_q(𝔰𝔩₂)` quotient truncates to the `(ℓ - 1)`-object
   modular tensor category `SU(2)_{ℓ-2}`) **if and only if** `q^(2ℓ) = 1`.
2. **Non-truncation and unbounded global dimension at real `q > 1`
   (`natCast_le_symQInt_of_one_lt`, `jonesWenzl_qDim_ne_zero_of_one_lt`,
   `globalDimSq_prefix_ge`, §7c over any ordered field).** Whenever `1 < q`,
   `2 < q + q⁻¹`, `[n]_q ≥ n` for every `n : ℕ` (strictly `[n]_q > n` for `n ≥ 2`), every
   Jones–Wenzl quantum dimension `d_q(V_k) = [k + 1]_q ≥ k + 1 ≥ 1` is strictly positive,
   and the partial global-dimension sum `∑_{k < N} d_q(V_k)² ≥ N` grows without bound.
   Consequently, at generic real `q₀ > 1` the full Hecke / Temperley–Lieb category has
   infinitely many non-negligible simple objects and is **not** a finite-rank modular tensor
   category; `KeystoneHeckeMTC.heckeMTC` restricts to an explicit finite conjugate-closed
   block set `P`, whereas genuine category-level finiteness requires a root-of-unity
   semisimplified quotient (`q^(2ℓ) = 1`).

## Scope & Honest Non-Claims

* Proves the exact algebraic/order dichotomy on `d_q(V_k) = [k + 1]_q`; does **not** claim
  that Beasley–Witten localization equals the Hecke MTC (`bwse` / `bwhk`, open physics
  identification) and does **not** select between restricting `hkmt` to root-of-unity
  quotients vs finite block truncations (owner scope question on `hkmt`).

-- Ref: [bakalovkirillov2001] Ch. 1–3 (semisimplified `U_q(𝔰𝔩₂)` MTC at `q = e^{iπ/ℓ}`).
-- Ref: [turaev1994] Ch. XII (Temperley–Lieb / Jones–Wenzl negligible ideal at `[ℓ]_q = 0`).
-/

namespace QOU.BraidKnot.HeckeModularitySplit

open scoped BigOperators

/-! ## §1 — Symmetric quantum integers `[n]_q` via Chebyshev recurrence (`[Field K]`) -/

/-- Symmetric quantum integer `[n]_q` over any field `K`, defined via the Chebyshev
two-term recurrence `[0]_q = 0`, `[1]_q = 1`, `[n + 2]_q = (q + q⁻¹)[n + 1]_q - [n]_q` so no
division by `q - q⁻¹` is needed and specialization at `q = ±1` is regular (`[n]_1 = n`). -/
def symQInt {K : Type*} [Field K] (q : K) : ℕ → K
  | 0 => 0
  | 1 => 1
  | n + 2 => (q + q⁻¹) * symQInt q (n + 1) - symQInt q n

@[simp]
theorem symQInt_zero {K : Type*} [Field K] (q : K) : symQInt q 0 = 0 := rfl

@[simp]
theorem symQInt_one {K : Type*} [Field K] (q : K) : symQInt q 1 = 1 := rfl

theorem symQInt_two {K : Type*} [Field K] (q : K) : symQInt q 2 = q + q⁻¹ := by
  simp [symQInt]

theorem symQInt_three {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    symQInt q 3 = q ^ 2 + 1 + (q⁻¹) ^ 2 := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  calc symQInt q 3
      = (q + q⁻¹) * (q + q⁻¹) - 1 := by simp [symQInt]
    _ = q ^ 2 + (2 * (q * q⁻¹) - 1) + (q⁻¹) ^ 2 := by ring
    _ = q ^ 2 + 1 + (q⁻¹) ^ 2 := by rw [hqi]; ring

private theorem symQInt_at_one_pair (K : Type*) [Field K] :
    ∀ n : ℕ, symQInt (1 : K) n = (n : K) ∧ symQInt (1 : K) (n + 1) = ((n + 1 : ℕ) : K)
  | 0 => by simp [symQInt]
  | n + 1 => by
      obtain ⟨ih0, ih1⟩ := symQInt_at_one_pair K n
      refine ⟨ih1, ?_⟩
      simp only [symQInt, ih0, ih1, inv_one]
      push_cast
      ring

/-- Classical limit `q = 1`: `[n]_1 = n` in any field `K`. -/
theorem symQInt_at_one {K : Type*} [Field K] (n : ℕ) :
    symQInt (1 : K) n = (n : K) :=
  (symQInt_at_one_pair K n).1

/-! ## §2 — Clearing denominators and exact root-of-unity vanishing (`q^(2n) = 1`) -/

private theorem sub_inv_mul_symQInt_pair {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    ∀ n : ℕ,
      (q - q⁻¹) * symQInt q n = q ^ n - (q⁻¹) ^ n ∧
      (q - q⁻¹) * symQInt q (n + 1) = q ^ (n + 1) - (q⁻¹) ^ (n + 1)
  | 0 => by simp [symQInt]
  | n + 1 => by
      obtain ⟨ih0, ih1⟩ := sub_inv_mul_symQInt_pair hq n
      refine ⟨ih1, ?_⟩
      have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
      calc (q - q⁻¹) * symQInt q (n + 2)
          = (q + q⁻¹) * ((q - q⁻¹) * symQInt q (n + 1)) - (q - q⁻¹) * symQInt q n := by
              simp only [symQInt]; ring
        _ = (q + q⁻¹) * (q ^ (n + 1) - (q⁻¹) ^ (n + 1)) - (q ^ n - (q⁻¹) ^ n) := by
              rw [ih1, ih0]
        _ = q ^ (n + 2) - (q⁻¹) ^ (n + 2)
              + (q * q⁻¹ - 1) * (q ^ n - (q⁻¹) ^ n) := by
              simp only [pow_succ]; ring
        _ = q ^ (n + 2) - (q⁻¹) ^ (n + 2) := by
              rw [hqi]; ring

/-- **Telescoping identity** `(q - q⁻¹) · [n]_q = q^n - (q⁻¹)^n` over any field `K`. -/
theorem sub_inv_mul_symQInt {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (n : ℕ) :
    (q - q⁻¹) * symQInt q n = q ^ n - (q⁻¹) ^ n :=
  (sub_inv_mul_symQInt_pair hq n).1

/-- **Root-of-unity truncation criterion (`hkmt`).** Over any field `K` with `q ≠ 0` and
`q - q⁻¹ ≠ 0` (`q² ≠ 1`), the symmetric quantum integer `[n]_q` vanishes if and only if
`q^(2n) = 1`. In particular, the `(ℓ - 1)`-st Jones–Wenzl simple object `V_{ℓ-1}` becomes
negligible (`d_q(V_{ℓ-1}) = [ℓ]_q = 0`, truncating the category to `ℓ - 1` simple objects)
if and only if `q^(2ℓ) = 1`. -/
theorem symQInt_eq_zero_iff_pow_two_mul_eq_one
    {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (hq1 : q - q⁻¹ ≠ 0) (n : ℕ) :
    symQInt q n = 0 ↔ q ^ (2 * n) = 1 := by
  have hqn : q ^ n ≠ 0 := pow_ne_zero n hq
  have hprod : q ^ n * (q⁻¹) ^ n = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
  have hsq : q ^ n * q ^ n = q ^ (2 * n) := by
    rw [← pow_add, two_mul]
  calc symQInt q n = 0
      ↔ (q - q⁻¹) * symQInt q n = 0 := (mul_eq_zero_iff_left hq1).symm
    _ ↔ q ^ n - (q⁻¹) ^ n = 0 := by rw [sub_inv_mul_symQInt hq n]
    _ ↔ q ^ n * (q ^ n - (q⁻¹) ^ n) = 0 := (mul_eq_zero_iff_left hqn).symm
    _ ↔ q ^ (2 * n) - 1 = 0 := by rw [mul_sub, hsq, hprod]
    _ ↔ q ^ (2 * n) = 1 := sub_eq_zero

/-! ## §3 — Ordered-field lower bounds and non-truncation at `q > 1` -/

/-- For `1 < q` in any strict ordered field, `2 < q + q⁻¹` (AM–GM strictness via `(q - 1)² > 0`). -/
theorem two_lt_add_inv_of_one_lt
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 1 < q) : 2 < q + q⁻¹ := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hqne : q ≠ 0 := ne_of_gt hq0
  have hsq : 0 < (q - 1) ^ 2 := sq_pos_of_pos (sub_pos.mpr hq)
  have hid : q * ((q + q⁻¹) - 2) = (q - 1) ^ 2 := by
    calc q * ((q + q⁻¹) - 2)
        = q ^ 2 + q * q⁻¹ - 2 * q := by ring
      _ = (q - 1) ^ 2 := by rw [mul_inv_cancel₀ hqne]; ring
  by_contra hle
  push_neg at hle
  have hnonpos : q * ((q + q⁻¹) - 2) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos (le_of_lt hq0) (by linarith)
  linarith

private theorem symQInt_growth_pair
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 1 < q) :
    ∀ n : ℕ, (n : K) ≤ symQInt q n ∧ symQInt q n + 1 ≤ symQInt q (n + 1)
  | 0 => by simp [symQInt]
  | n + 1 => by
      obtain ⟨ih_le, ih_step⟩ := symQInt_growth_pair hq n
      have hcast : ((n + 1 : ℕ) : K) ≤ symQInt q (n + 1) := by
        push_cast; linarith
      refine ⟨hcast, ?_⟩
      have h2 : 2 ≤ q + q⁻¹ := le_of_lt (two_lt_add_inv_of_one_lt hq)
      have hn0 : (0 : K) ≤ (n : K) := Nat.cast_nonneg n
      have hpos1 : 0 ≤ symQInt q (n + 1) := by linarith
      have hmul : 2 * symQInt q (n + 1) ≤ (q + q⁻¹) * symQInt q (n + 1) :=
        mul_le_mul_of_nonneg_right h2 hpos1
      simp only [symQInt]
      linarith

/-- For `1 < q`, `[n]_q ≥ n` for every natural number `n`. -/
theorem natCast_le_symQInt_of_one_lt
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 1 < q) (n : ℕ) : (n : K) ≤ symQInt q n :=
  (symQInt_growth_pair hq n).1

/-- For `1 < q` and `n ≥ 2`, `[n]_q > n` strictly. -/
theorem natCast_lt_symQInt_of_one_lt
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 1 < q) : ∀ {n : ℕ}, 2 ≤ n → (n : K) < symQInt q n
  | 2, _ => by
      rw [symQInt_two]
      simpa using two_lt_add_inv_of_one_lt hq
  | n + 3, _ => by
      have ih : ((n + 2 : ℕ) : K) < symQInt q (n + 2) :=
        natCast_lt_symQInt_of_one_lt hq (by omega)
      have hstep := (symQInt_growth_pair hq (n + 2)).2
      push_cast at ih ⊢
      linarith

/-- For `1 < q` and `n ≥ 1`, `[n]_q > 0`. -/
theorem symQInt_pos_of_one_lt
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 1 < q) {n : ℕ} (hn : 1 ≤ n) : 0 < symQInt q n := by
  have hle := natCast_le_symQInt_of_one_lt hq n
  have hn_pos : (0 : K) < (n : K) := Nat.cast_pos.mpr (Nat.pos_of_ne_zero (by omega))
  exact lt_of_lt_of_le hn_pos hle

/-- **No negligible Jones–Wenzl object at `q > 1` (`hkmt`).** Every `V_k` (`k : ℕ`) has
quantum dimension `d_q(V_k) = [k + 1]_q ≠ 0`, so no root-of-unity MTC truncation occurs on
the real ray `q > 1`. -/
theorem jonesWenzl_qDim_ne_zero_of_one_lt
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 1 < q) (k : ℕ) : symQInt q (k + 1) ≠ 0 :=
  ne_of_gt (symQInt_pos_of_one_lt hq (Nat.succ_le_succ (Nat.zero_le k)))

/-- **Divergence of the global quantum dimension squared at `q > 1` (`hkmt`).**
The partial sum of squared Jones–Wenzl quantum dimensions over the first `N` simple objects
satisfies `∑_{k < N} [k + 1]_q² ≥ N`, ruling out a finite global dimension `D² = ∑_k d_q(V_k)²`
over the un-truncated category at any `q > 1`. -/
theorem globalDimSq_prefix_ge
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 1 < q) :
    ∀ N : ℕ, (N : K) ≤ ∑ k ∈ Finset.range N, (symQInt q (k + 1)) ^ 2
  | 0 => by simp
  | N + 1 => by
      rw [Finset.sum_range_succ]
      have ih := globalDimSq_prefix_ge hq N
      have h1 : (1 : K) ≤ symQInt q (N + 1) := by
        have hle := natCast_le_symQInt_of_one_lt hq (N + 1)
        have hN1 : (1 : K) ≤ ((N + 1 : ℕ) : K) := by
          exact_mod_cast Nat.succ_le_succ (Nat.zero_le N)
        exact le_trans hN1 hle
      have hsq : (1 : K) ≤ (symQInt q (N + 1)) ^ 2 := by
        have hmul : (1 : K) * 1 ≤ symQInt q (N + 1) * symQInt q (N + 1) :=
          mul_le_mul h1 h1 zero_le_one (by linarith)
        simpa [sq] using hmul
      push_cast
      linarith

end QOU.BraidKnot.HeckeModularitySplit
