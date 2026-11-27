import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Totient
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum.Prime
import Mathlib.Tactic.NormNum.DivMod
import Mathlib.Tactic.ComputeDegree
import QOU.MassTheory.CyclotomicBoundaryKeystone
import HeckeTemperleyLieb.QIntegerCanonical

/-!
# QOU.Mass.CyclotomicBoundaryCertified — the Habiro tail `D(n)`, derived and certified

`conj:cyclotomic-boundary-at-keystone` concerns

```
S(n) = Σ_{λ ⊢ n} dim_q(λ),   dim_q(λ) = [n]_q! / ∏_{c ∈ λ} [h(c)]_q,
D(n) = S(n) − S(n−1) − [n−1]_q · S(n−2),
```

with `[k]_q = (q^k − q^{−k})/(q − q⁻¹)` the balanced quantum integer, and claims that `D(n)`,
cleared of its `q`-monomial, is a product of cyclotomic polynomials exactly when `n ≤ 5`.

The sibling module `QOU.Mass.CyclotomicBoundaryKeystone` proves facts about the polynomials
`D4`, `D5`, `C6core`, but those are **literals**: nothing there connects them to `S(n)`.  This
module closes that gap and extends the converse.

## What is proved (no `sorry`, no axiom)

1. **Derivation from the definition** (`tail_n`, `2 ≤ n ≤ 9`).  Over a generic field `K` with
   `q ≠ 0` and `1 + q² + ⋯ + q^{2(k−1)} ≠ 0` for `k ≤ n` (the hook denominators do not vanish), the
   definition above, with partitions enumerated by `partitionsList` and hook lengths computed by
   `hooksOf`, gives `q^{m_n} · D(n) = P_n(q)` for an explicit integer polynomial `P_n` with
   `P_n(0) ≠ 0`.  In particular `D(2) = D(3) = 0`.
2. **The forward direction** (`P4_cyclo`, `P5_cyclo`): `P_4 = Φ₁²Φ₃`, `P_5 = 2Φ₁²Φ₂²Φ₃Φ₆`.
3. **The converse through `n = 20`** (`Pn_not_cyclo`, `6 ≤ n ≤ 20`): `P_n` is not
   `c · X^j · ∏ Φ_k` for any `c`, `j`, multiset of `k`.
4. **The boundary** (`cyclotomic_boundary`): for `2 ≤ n ≤ 20`,
   `IsCycloProduct (tailPoly n) ↔ n ≤ 5`.

## The non-cyclotomicity certificate (finite, checkable, no analysis)

`not_isCycloProduct_of_witness`: if `P = c · X^j · ∏ Φ_k` and a prime `p` and an integer `a` satisfy
`p ∣ P(a)`, `p ∤ a`, and `p ∤ P(b)` for some `b`, then some `Φ_k(a) ≡ 0 (mod p)`, so
`a^k ≡ 1`, so the multiplicative order `m` of `a` mod `p` divides `k`, so
`φ(m) ≤ φ(k) = deg Φ_k ≤ deg P`.  A witness with `φ(m) > deg P` therefore refutes the
factorisation.  Each witness `(p, a, m, b)` is found by a finite search
(`computations/cyclotomic_boundary_certificates.py`) and every arithmetic fact about it is
re-checked here by `norm_num` / `decide`.  This replaces the `C6core` route (reciprocal transform,
quartic discriminant, complex roots) by integer arithmetic, and it scales: one lemma serves every
`n`.

## What is not proved

The all-`n` converse (`D(n)` non-cyclotomic for **every** `n ≥ 6`) stays open.  The certificate
needs a witness per `n`; no uniform family of witnesses is known.

## Erratum fixed

The audit table in `computations/lever1_cyclotomic_boundary_keystone_conjecture.py` lists
`D(3) = (q−1)²Φ₃`.  The definition gives `D(3) = 0` (`tail_3`); `(q−1)²Φ₃/q²` is `D(4)`.

## Base ring

Part 1 is over a generic field `K` (division by hook brackets is genuine; genericity is the
hypothesis `hB`).  Since the identities hold in `ℚ(q)` with `q` transcendental, `P_n` is *the*
cleared tail, and it lies in `ℤ[q]`.  Parts 2–4 are over `ℤ[X]` and `ZMod p`.  Nothing archimedean.

LaTeX label: `thm:cyclotomic-boundary-certified`
-/

set_option linter.unusedSimpArgs false
set_option maxRecDepth 100000
set_option exponentiation.threshold 1000

namespace QOU.Mass.CyclotomicBoundaryCertified

open Polynomial

/-! ## Part 1 — the definition, over a generic field -/

section Derivation

variable {K : Type*} [Field K] (q : K)

/-- `B_k(q) = 1 + q² + ⋯ + q^{2(k−1)}`, the numerator of the balanced quantum integer. -/
def qb2 (k : ℕ) : K := ∑ i ∈ Finset.range k, q ^ (2 * i)

/-- The balanced quantum integer `[k]_q = q^{−(k−1)} · B_k(q)`. -/
noncomputable def qbal (k : ℕ) : K := qb2 q k / q ^ (k - 1)

/-- `qbal` is the corpus's canonical `qIntBalZ` on natural indices. -/
theorem qbal_eq_qIntBalZ (hq : q ≠ 0) (h1 : q ^ 2 ≠ 1) (k : ℕ) :
    qbal q k = QOU.QInteger.qIntBalZ q (k : ℤ) := by
  rcases Nat.eq_zero_or_pos k with rfl | hk
  · simp [qbal, qb2]
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  have hgeom : (∑ i ∈ Finset.range (j + 1), (q ^ 2) ^ i) * (q ^ 2 - 1) = (q ^ 2) ^ (j + 1) - 1 :=
    geom_sum_mul _ _
  have hs : qb2 q (j + 1) = ∑ i ∈ Finset.range (j + 1), (q ^ 2) ^ i := by
    simp only [qb2, ← pow_mul]
  have hq21 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr h1
  have hqq : q - q⁻¹ ≠ 0 := by
    intro h
    apply hq21
    have : q * (q - q⁻¹) = q ^ 2 - 1 := by field_simp
    rw [← this, h, mul_zero]
  rw [qbal, QOU.QInteger.qIntBalZ_def, hs, show j + 1 - 1 = j by omega]
  rw [div_eq_div_iff (pow_ne_zero _ hq) hqq]
  have hz : q ^ ((↑(j + 1) : ℤ)) - q ^ (-(↑(j + 1) : ℤ)) =
      ((q ^ 2) ^ (j + 1) - 1) / q ^ (j + 1) := by
    rw [zpow_neg, zpow_natCast]
    field_simp
    ring
  rw [hz, ← hgeom]
  field_simp
  ring

/-- `dim_q(λ) = [n]_q! / ∏ [h]_q`, for a partition of `n` given by its list of hook lengths. -/
noncomputable def dimq (n : ℕ) (hooks : List ℕ) : K :=
  (((List.range n).map (· + 1)).map (qbal q)).prod / (hooks.map (qbal q)).prod

variable {q}

theorem pow_mul_qbal (hq : q ≠ 0) (k : ℕ) : q ^ (k - 1) * qbal q k = qb2 q k := by
  rw [qbal, mul_div_cancel₀ _ (pow_ne_zero _ hq)]

/-- Clearing the `q`-powers of a product of balanced brackets. -/
theorem pow_mul_prod_qbal (hq : q ≠ 0) (ls : List ℕ) :
    q ^ (ls.map (· - 1)).sum * (ls.map (qbal q)).prod = (ls.map (qb2 q)).prod := by
  induction ls with
  | nil => simp
  | cons x xs ih =>
    simp only [List.map_cons, List.sum_cons, List.prod_cons, pow_add]
    rw [← pow_mul_qbal hq x, ← ih]
    ring

/-- **A division-free certificate for `dim_q`.**  If `[n]!_B = G · ∏_h B_h` as polynomials in `q`
(`B_k = 1 + q² + ⋯`), then `q^e · dim_q = G`, where `e = Σ_{k ≤ n}(k−1) − Σ_h (h−1)`. -/
theorem dimq_eq (hq : q ≠ 0) {n : ℕ} {hs : List ℕ} (hBs : ∀ h ∈ hs, qb2 q h ≠ 0) (e : ℕ) (G : K)
    (nums : List ℕ) (hnum : (List.range n).map (· + 1) = nums)
    (he : e + (hs.map (· - 1)).sum = (nums.map (· - 1)).sum)
    (hpoly : (nums.map (qb2 q)).prod = G * (hs.map (qb2 q)).prod) :
    q ^ e * dimq q n hs = G := by
  have hA := pow_mul_prod_qbal hq nums
  have hB := pow_mul_prod_qbal hq hs
  have hBne : (hs.map (qb2 q)).prod ≠ 0 :=
    List.prod_ne_zero (by simp only [List.mem_map, not_exists, not_and]; exact fun h hh heq => hBs h hh heq)
  have hden : (hs.map (qbal q)).prod ≠ 0 := by
    intro h0; rw [h0, mul_zero] at hB; exact hBne hB.symm
  rw [dimq, hnum, mul_div_assoc', div_eq_iff hden]
  apply mul_left_cancel₀ (pow_ne_zero (hs.map (· - 1)).sum hq)
  have e1 : q ^ (hs.map (· - 1)).sum * (q ^ e * (nums.map (qbal q)).prod)
      = q ^ (nums.map (· - 1)).sum * (nums.map (qbal q)).prod := by
    rw [← he, pow_add]; ring
  rw [e1, hA, hpoly, ← hB]
  ring

end Derivation

/-- Partitions of `n` with parts at most `m`, weakly decreasing (fuel-bounded recursion). -/
def partsB : ℕ → ℕ → ℕ → List (List ℕ)
  | 0, n, _ => if n = 0 then [[]] else []
  | fuel + 1, n, m =>
    if n = 0 then [[]] else
      (List.range (min n m)).flatMap (fun i =>
        (partsB fuel (n - (i + 1)) (i + 1)).map (fun r => (i + 1) :: r))

/-- All partitions of `n`, as weakly decreasing lists of positive parts. -/
def partitionsList (n : ℕ) : List (List ℕ) := partsB n n n

/-- Length of column `j` of the Young diagram with row lengths `l`. -/
def conjAt (l : List ℕ) (j : ℕ) : ℕ := (l.filter (fun r => decide (j < r))).length

/-- Hook lengths of the Young diagram with row lengths `l` (row `i`, column `j`):
`h(i,j) = (λ_i − j) + (λ'_j − i) − 1`. -/
def hooksOf (l : List ℕ) : List ℕ :=
  (List.range l.length).flatMap (fun i =>
    (List.range (l.getD i 0)).map (fun j => (l.getD i 0 - j) + (conjAt l j - i) - 1))

/-- Sanity: `partitionsList` has `p(n)` entries for small `n`. -/
theorem partitionsList_length :
    ((List.range 10).map (fun n => (partitionsList n).length)) =
      [1, 1, 2, 3, 5, 7, 11, 15, 22, 30] := by decide

section Derivation2

variable {K : Type*} [Field K] (q : K)

/-- `S(n) = Σ_{λ ⊢ n} dim_q(λ)`. -/
noncomputable def S (n : ℕ) : K := (((partitionsList n).map hooksOf).map (dimq q n)).sum

/-- The Habiro tail `D(n) = S(n) − S(n−1) − [n−1]_q S(n−2)`. -/
noncomputable def D (n : ℕ) : K := S q n - S q (n - 1) - qbal q (n - 1) * S q (n - 2)

variable {q}

theorem S_0 : S q 0 = 1 := by
  simp [S, partitionsList, partsB, hooksOf, dimq]

theorem S_1 : S q 1 = 1 := by
  simp [S, partitionsList, partsB, hooksOf, conjAt, dimq, qbal, qb2]

/-- The hook multisets of the partitions of `2`, as `partitionsList` enumerates them. -/
theorem hookTable_2 : (partitionsList 2).map hooksOf =
    [[2, 1], [2, 1]] := by decide

theorem dimq_2_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 2 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 2 [2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_2_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 2 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 2 [2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

set_option maxHeartbeats 8000000 in
theorem S_2_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 2 → qb2 q k ≠ 0) :
    q ^ 0 * S q 2 = q ^ 0 * (1)
      + q ^ 0 * (1) := by
  rw [S, hookTable_2]
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  have h0 := dimq_2_0 hq hB
  have h1 := dimq_2_1 hq hB
  linear_combination q ^ 0 * h0 + q ^ 0 * h1

/-- The hook multisets of the partitions of `3`, as `partitionsList` enumerates them. -/
theorem hookTable_3 : (partitionsList 3).map hooksOf =
    [[3, 2, 1], [3, 1, 1], [3, 2, 1]] := by decide

theorem dimq_3_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 3 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 3 [3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_3_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 3 → qb2 q k ≠ 0) :
    q ^ 1 * dimq q 3 [3, 1, 1] = 1 + q ^ 2 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 1 _
    [1, 2, 3] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_3_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 3 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 3 [3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

set_option maxHeartbeats 8000000 in
theorem S_3_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 3 → qb2 q k ≠ 0) :
    q ^ 1 * S q 3 = q ^ 1 * (1)
      + q ^ 0 * (1 + q ^ 2)
      + q ^ 1 * (1) := by
  rw [S, hookTable_3]
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  have h0 := dimq_3_0 hq hB
  have h1 := dimq_3_1 hq hB
  have h2 := dimq_3_2 hq hB
  linear_combination q ^ 1 * h0 + q ^ 0 * h1 + q ^ 1 * h2

/-- The hook multisets of the partitions of `4`, as `partitionsList` enumerates them. -/
theorem hookTable_4 : (partitionsList 4).map hooksOf =
    [[4, 3, 2, 1], [4, 1, 2, 1], [3, 2, 2, 1], [4, 2, 1, 1], [4, 3, 2, 1]] := by decide

theorem dimq_4_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 4 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 4 [4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_4_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 4 → qb2 q k ≠ 0) :
    q ^ 2 * dimq q 4 [4, 1, 2, 1] = 1 + q ^ 2 + q ^ 4 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 2 _
    [1, 2, 3, 4] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_4_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 4 → qb2 q k ≠ 0) :
    q ^ 2 * dimq q 4 [3, 2, 2, 1] = 1 + q ^ 4 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 2 _
    [1, 2, 3, 4] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_4_3 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 4 → qb2 q k ≠ 0) :
    q ^ 2 * dimq q 4 [4, 2, 1, 1] = 1 + q ^ 2 + q ^ 4 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 2 _
    [1, 2, 3, 4] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_4_4 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 4 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 4 [4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

set_option maxHeartbeats 8000000 in
theorem S_4_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 4 → qb2 q k ≠ 0) :
    q ^ 2 * S q 4 = q ^ 2 * (1)
      + q ^ 0 * (1 + q ^ 2 + q ^ 4)
      + q ^ 0 * (1 + q ^ 4)
      + q ^ 0 * (1 + q ^ 2 + q ^ 4)
      + q ^ 2 * (1) := by
  rw [S, hookTable_4]
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  have h0 := dimq_4_0 hq hB
  have h1 := dimq_4_1 hq hB
  have h2 := dimq_4_2 hq hB
  have h3 := dimq_4_3 hq hB
  have h4 := dimq_4_4 hq hB
  linear_combination q ^ 2 * h0 + q ^ 0 * h1 + q ^ 0 * h2 + q ^ 0 * h3 + q ^ 2 * h4

/-- The hook multisets of the partitions of `5`, as `partitionsList` enumerates them. -/
theorem hookTable_5 : (partitionsList 5).map hooksOf =
    [[5, 4, 3, 2, 1], [5, 1, 3, 2, 1], [4, 2, 3, 1, 1], [5, 2, 1, 2, 1], [4, 3, 1, 2, 1], [5, 3, 2, 1, 1], [5, 4, 3, 2, 1]] := by decide

theorem dimq_5_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 5 [5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_5_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 3 * dimq q 5 [5, 1, 3, 2, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 3 _
    [1, 2, 3, 4, 5] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_5_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 4 * dimq q 5 [4, 2, 3, 1, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 4 _
    [1, 2, 3, 4, 5] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_5_3 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 4 * dimq q 5 [5, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + q ^ 6 + q ^ 8 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 4 _
    [1, 2, 3, 4, 5] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_5_4 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 4 * dimq q 5 [4, 3, 1, 2, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 4 _
    [1, 2, 3, 4, 5] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_5_5 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 3 * dimq q 5 [5, 3, 2, 1, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 3 _
    [1, 2, 3, 4, 5] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_5_6 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 5 [5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

set_option maxHeartbeats 8000000 in
theorem S_5_4 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 4 * S q 5 = q ^ 4 * (1)
      + q ^ 1 * (1 + q ^ 2 + q ^ 4 + q ^ 6)
      + q ^ 0 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8)
      + q ^ 0 * (1 + q ^ 2 + 2 * q ^ 4 + q ^ 6 + q ^ 8)
      + q ^ 0 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8)
      + q ^ 1 * (1 + q ^ 2 + q ^ 4 + q ^ 6)
      + q ^ 4 * (1) := by
  rw [S, hookTable_5]
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  have h0 := dimq_5_0 hq hB
  have h1 := dimq_5_1 hq hB
  have h2 := dimq_5_2 hq hB
  have h3 := dimq_5_3 hq hB
  have h4 := dimq_5_4 hq hB
  have h5 := dimq_5_5 hq hB
  have h6 := dimq_5_6 hq hB
  linear_combination q ^ 4 * h0 + q ^ 1 * h1 + q ^ 0 * h2 + q ^ 0 * h3 + q ^ 0 * h4 + q ^ 1 * h5 + q ^ 4 * h6

/-- The hook multisets of the partitions of `6`, as `partitionsList` enumerates them. -/
theorem hookTable_6 : (partitionsList 6).map hooksOf =
    [[6, 5, 4, 3, 2, 1], [6, 1, 4, 3, 2, 1], [5, 2, 4, 1, 2, 1], [4, 3, 3, 2, 2, 1], [6, 2, 1, 3, 2, 1], [5, 3, 1, 3, 1, 1], [4, 3, 2, 3, 2, 1], [6, 3, 2, 1, 2, 1], [5, 4, 2, 1, 2, 1], [6, 4, 3, 2, 1, 1], [6, 5, 4, 3, 2, 1]] := by decide

theorem dimq_6_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 6 [6, 5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 4 * dimq q 6 [6, 1, 4, 3, 2, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 4 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 6 * dimq q 6 [5, 2, 4, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + q ^ 6 + 2 * q ^ 8 + q ^ 10 + q ^ 12 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 6 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_3 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 6 * dimq q 6 [4, 3, 3, 2, 2, 1] = 1 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 12 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 6 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_4 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 6 * dimq q 6 [6, 2, 1, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + q ^ 10 + q ^ 12 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 6 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_5 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 7 * dimq q 6 [5, 3, 1, 3, 1, 1] = 1 + 2 * q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 7 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_6 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 6 * dimq q 6 [4, 3, 2, 3, 2, 1] = 1 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 12 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 6 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_7 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 6 * dimq q 6 [6, 3, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + q ^ 10 + q ^ 12 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 6 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_8 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 6 * dimq q 6 [5, 4, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + q ^ 6 + 2 * q ^ 8 + q ^ 10 + q ^ 12 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 6 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_9 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 4 * dimq q 6 [6, 4, 3, 2, 1, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 4 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_6_10 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 6 [6, 5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5, 6] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

set_option maxHeartbeats 8000000 in
theorem S_6_7 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 7 * S q 6 = q ^ 7 * (1)
      + q ^ 3 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8)
      + q ^ 1 * (1 + q ^ 2 + 2 * q ^ 4 + q ^ 6 + 2 * q ^ 8 + q ^ 10 + q ^ 12)
      + q ^ 1 * (1 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 12)
      + q ^ 1 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + q ^ 10 + q ^ 12)
      + q ^ 0 * (1 + 2 * q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14)
      + q ^ 1 * (1 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 12)
      + q ^ 1 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + q ^ 10 + q ^ 12)
      + q ^ 1 * (1 + q ^ 2 + 2 * q ^ 4 + q ^ 6 + 2 * q ^ 8 + q ^ 10 + q ^ 12)
      + q ^ 3 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8)
      + q ^ 7 * (1) := by
  rw [S, hookTable_6]
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  have h0 := dimq_6_0 hq hB
  have h1 := dimq_6_1 hq hB
  have h2 := dimq_6_2 hq hB
  have h3 := dimq_6_3 hq hB
  have h4 := dimq_6_4 hq hB
  have h5 := dimq_6_5 hq hB
  have h6 := dimq_6_6 hq hB
  have h7 := dimq_6_7 hq hB
  have h8 := dimq_6_8 hq hB
  have h9 := dimq_6_9 hq hB
  have h10 := dimq_6_10 hq hB
  linear_combination q ^ 7 * h0 + q ^ 3 * h1 + q ^ 1 * h2 + q ^ 1 * h3 + q ^ 1 * h4 + q ^ 0 * h5 + q ^ 1 * h6 + q ^ 1 * h7 + q ^ 1 * h8 + q ^ 3 * h9 + q ^ 7 * h10

/-- The hook multisets of the partitions of `7`, as `partitionsList` enumerates them. -/
theorem hookTable_7 : (partitionsList 7).map hooksOf =
    [[7, 6, 5, 4, 3, 2, 1], [7, 1, 5, 4, 3, 2, 1], [6, 2, 5, 1, 3, 2, 1], [5, 3, 4, 2, 3, 1, 1], [7, 2, 1, 4, 3, 2, 1], [6, 3, 1, 4, 1, 2, 1], [5, 4, 1, 3, 2, 2, 1], [5, 3, 2, 4, 2, 1, 1], [7, 3, 2, 1, 3, 2, 1], [6, 4, 2, 1, 3, 1, 1], [5, 4, 3, 1, 3, 2, 1], [7, 4, 3, 2, 1, 2, 1], [6, 5, 3, 2, 1, 2, 1], [7, 5, 4, 3, 2, 1, 1], [7, 6, 5, 4, 3, 2, 1]] := by decide

theorem dimq_7_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 7 [7, 6, 5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 5 * dimq q 7 [7, 1, 5, 4, 3, 2, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 5 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 8 * dimq q 7 [6, 2, 5, 1, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 8 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_3 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 9 * dimq q 7 [5, 3, 4, 2, 3, 1, 1] = 1 + q ^ 2 + q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16 + q ^ 18 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 9 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_4 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 8 * dimq q 7 [7, 2, 1, 4, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 8 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_5 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 10 * dimq q 7 [6, 3, 1, 4, 1, 2, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + q ^ 20 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 10 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_6 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 10 * dimq q 7 [5, 4, 1, 3, 2, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 10 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_7 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 10 * dimq q 7 [5, 3, 2, 4, 2, 1, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 10 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_8 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 9 * dimq q 7 [7, 3, 2, 1, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + q ^ 16 + q ^ 18 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 9 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_9 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 10 * dimq q 7 [6, 4, 2, 1, 3, 1, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + q ^ 20 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 10 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_10 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 9 * dimq q 7 [5, 4, 3, 1, 3, 2, 1] = 1 + q ^ 2 + q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16 + q ^ 18 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 9 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_11 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 8 * dimq q 7 [7, 4, 3, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 8 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_12 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 8 * dimq q 7 [6, 5, 3, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 8 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_13 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 5 * dimq q 7 [7, 5, 4, 3, 2, 1, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 5 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_7_14 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 7 [7, 6, 5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5, 6, 7] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

set_option maxHeartbeats 8000000 in
theorem S_7_10 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 10 * S q 7 = q ^ 10 * (1)
      + q ^ 5 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10)
      + q ^ 2 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16)
      + q ^ 1 * (1 + q ^ 2 + q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16 + q ^ 18)
      + q ^ 2 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16)
      + q ^ 0 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + q ^ 20)
      + q ^ 0 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20)
      + q ^ 0 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20)
      + q ^ 1 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + q ^ 16 + q ^ 18)
      + q ^ 0 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + q ^ 20)
      + q ^ 1 * (1 + q ^ 2 + q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16 + q ^ 18)
      + q ^ 2 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16)
      + q ^ 2 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 2 * q ^ 12 + q ^ 14 + q ^ 16)
      + q ^ 5 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10)
      + q ^ 10 * (1) := by
  rw [S, hookTable_7]
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  have h0 := dimq_7_0 hq hB
  have h1 := dimq_7_1 hq hB
  have h2 := dimq_7_2 hq hB
  have h3 := dimq_7_3 hq hB
  have h4 := dimq_7_4 hq hB
  have h5 := dimq_7_5 hq hB
  have h6 := dimq_7_6 hq hB
  have h7 := dimq_7_7 hq hB
  have h8 := dimq_7_8 hq hB
  have h9 := dimq_7_9 hq hB
  have h10 := dimq_7_10 hq hB
  have h11 := dimq_7_11 hq hB
  have h12 := dimq_7_12 hq hB
  have h13 := dimq_7_13 hq hB
  have h14 := dimq_7_14 hq hB
  linear_combination q ^ 10 * h0 + q ^ 5 * h1 + q ^ 2 * h2 + q ^ 1 * h3 + q ^ 2 * h4 + q ^ 0 * h5 + q ^ 0 * h6 + q ^ 0 * h7 + q ^ 1 * h8 + q ^ 0 * h9 + q ^ 1 * h10 + q ^ 2 * h11 + q ^ 2 * h12 + q ^ 5 * h13 + q ^ 10 * h14

/-- The hook multisets of the partitions of `8`, as `partitionsList` enumerates them. -/
theorem hookTable_8 : (partitionsList 8).map hooksOf =
    [[8, 7, 6, 5, 4, 3, 2, 1], [8, 1, 6, 5, 4, 3, 2, 1], [7, 2, 6, 1, 4, 3, 2, 1], [6, 3, 5, 2, 4, 1, 2, 1], [5, 4, 4, 3, 3, 2, 2, 1], [8, 2, 1, 5, 4, 3, 2, 1], [7, 3, 1, 5, 1, 3, 2, 1], [6, 4, 1, 4, 2, 3, 1, 1], [6, 3, 2, 5, 2, 1, 2, 1], [5, 4, 2, 4, 3, 1, 2, 1], [8, 3, 2, 1, 4, 3, 2, 1], [7, 4, 2, 1, 4, 1, 2, 1], [6, 5, 2, 1, 3, 2, 2, 1], [6, 4, 3, 1, 4, 2, 1, 1], [5, 4, 3, 2, 4, 3, 2, 1], [8, 4, 3, 2, 1, 3, 2, 1], [7, 5, 3, 2, 1, 3, 1, 1], [6, 5, 4, 2, 1, 3, 2, 1], [8, 5, 4, 3, 2, 1, 2, 1], [7, 6, 4, 3, 2, 1, 2, 1], [8, 6, 5, 4, 3, 2, 1, 1], [8, 7, 6, 5, 4, 3, 2, 1]] := by decide

theorem dimq_8_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 8 [8, 7, 6, 5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 6 * dimq q 8 [8, 1, 6, 5, 4, 3, 2, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 6 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 10 * dimq q 8 [7, 2, 6, 1, 4, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 10 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_3 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 8 [6, 3, 5, 2, 4, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_4 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 8 [5, 4, 4, 3, 3, 2, 2, 1] = 1 + q ^ 4 + q ^ 6 + 2 * q ^ 8 + q ^ 10 + 2 * q ^ 12 + q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_5 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 10 * dimq q 8 [8, 2, 1, 5, 4, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 10 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_6 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 13 * dimq q 8 [7, 3, 1, 5, 1, 3, 2, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 8 * q ^ 12 + 8 * q ^ 14 + 7 * q ^ 16 + 6 * q ^ 18 + 5 * q ^ 20 + 3 * q ^ 22 + 2 * q ^ 24 + q ^ 26 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 13 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_7 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 14 * dimq q 8 [6, 4, 1, 4, 2, 3, 1, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 8 * q ^ 12 + 8 * q ^ 14 + 8 * q ^ 16 + 7 * q ^ 18 + 6 * q ^ 20 + 4 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 14 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_8 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 14 * dimq q 8 [6, 3, 2, 5, 2, 1, 2, 1] = 1 + q ^ 2 + 3 * q ^ 4 + 3 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 6 * q ^ 14 + 7 * q ^ 16 + 5 * q ^ 18 + 5 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + q ^ 26 + q ^ 28 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 14 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_9 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 14 * dimq q 8 [5, 4, 2, 4, 3, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 4 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 5 * q ^ 16 + 4 * q ^ 18 + 4 * q ^ 20 + 2 * q ^ 22 + 2 * q ^ 24 + q ^ 26 + q ^ 28 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 14 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_10 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 8 [8, 3, 2, 1, 4, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 4 * q ^ 16 + 3 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_11 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 14 * dimq q 8 [7, 4, 2, 1, 4, 1, 2, 1] = 1 + 2 * q ^ 2 + 4 * q ^ 4 + 5 * q ^ 6 + 8 * q ^ 8 + 9 * q ^ 10 + 11 * q ^ 12 + 10 * q ^ 14 + 11 * q ^ 16 + 9 * q ^ 18 + 8 * q ^ 20 + 5 * q ^ 22 + 4 * q ^ 24 + 2 * q ^ 26 + q ^ 28 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 14 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_12 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 14 * dimq q 8 [6, 5, 2, 1, 3, 2, 2, 1] = 1 + q ^ 2 + 3 * q ^ 4 + 3 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 6 * q ^ 14 + 7 * q ^ 16 + 5 * q ^ 18 + 5 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + q ^ 26 + q ^ 28 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 14 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_13 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 14 * dimq q 8 [6, 4, 3, 1, 4, 2, 1, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 8 * q ^ 12 + 8 * q ^ 14 + 8 * q ^ 16 + 7 * q ^ 18 + 6 * q ^ 20 + 4 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 14 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_14 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 8 [5, 4, 3, 2, 4, 3, 2, 1] = 1 + q ^ 4 + q ^ 6 + 2 * q ^ 8 + q ^ 10 + 2 * q ^ 12 + q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_15 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 8 [8, 4, 3, 2, 1, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 4 * q ^ 16 + 3 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_16 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 13 * dimq q 8 [7, 5, 3, 2, 1, 3, 1, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 8 * q ^ 12 + 8 * q ^ 14 + 7 * q ^ 16 + 6 * q ^ 18 + 5 * q ^ 20 + 3 * q ^ 22 + 2 * q ^ 24 + q ^ 26 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 13 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_17 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 8 [6, 5, 4, 2, 1, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_18 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 10 * dimq q 8 [8, 5, 4, 3, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 10 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_19 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 10 * dimq q 8 [7, 6, 4, 3, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 10 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_20 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 6 * dimq q 8 [8, 6, 5, 4, 3, 2, 1, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 6 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_8_21 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 8 [8, 7, 6, 5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5, 6, 7, 8] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

set_option maxHeartbeats 8000000 in
theorem S_8_14 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 14 * S q 8 = q ^ 14 * (1)
      + q ^ 8 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12)
      + q ^ 4 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20)
      + q ^ 2 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24)
      + q ^ 2 * (1 + q ^ 4 + q ^ 6 + 2 * q ^ 8 + q ^ 10 + 2 * q ^ 12 + q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 + q ^ 24)
      + q ^ 4 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20)
      + q ^ 1 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 8 * q ^ 12 + 8 * q ^ 14 + 7 * q ^ 16 + 6 * q ^ 18 + 5 * q ^ 20 + 3 * q ^ 22 + 2 * q ^ 24 + q ^ 26)
      + q ^ 0 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 8 * q ^ 12 + 8 * q ^ 14 + 8 * q ^ 16 + 7 * q ^ 18 + 6 * q ^ 20 + 4 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28)
      + q ^ 0 * (1 + q ^ 2 + 3 * q ^ 4 + 3 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 6 * q ^ 14 + 7 * q ^ 16 + 5 * q ^ 18 + 5 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + q ^ 26 + q ^ 28)
      + q ^ 0 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 4 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 5 * q ^ 16 + 4 * q ^ 18 + 4 * q ^ 20 + 2 * q ^ 22 + 2 * q ^ 24 + q ^ 26 + q ^ 28)
      + q ^ 2 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 4 * q ^ 16 + 3 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24)
      + q ^ 0 * (1 + 2 * q ^ 2 + 4 * q ^ 4 + 5 * q ^ 6 + 8 * q ^ 8 + 9 * q ^ 10 + 11 * q ^ 12 + 10 * q ^ 14 + 11 * q ^ 16 + 9 * q ^ 18 + 8 * q ^ 20 + 5 * q ^ 22 + 4 * q ^ 24 + 2 * q ^ 26 + q ^ 28)
      + q ^ 0 * (1 + q ^ 2 + 3 * q ^ 4 + 3 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 6 * q ^ 14 + 7 * q ^ 16 + 5 * q ^ 18 + 5 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + q ^ 26 + q ^ 28)
      + q ^ 0 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 8 * q ^ 12 + 8 * q ^ 14 + 8 * q ^ 16 + 7 * q ^ 18 + 6 * q ^ 20 + 4 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28)
      + q ^ 2 * (1 + q ^ 4 + q ^ 6 + 2 * q ^ 8 + q ^ 10 + 2 * q ^ 12 + q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20 + q ^ 24)
      + q ^ 2 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 4 * q ^ 14 + 4 * q ^ 16 + 3 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24)
      + q ^ 1 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 8 * q ^ 12 + 8 * q ^ 14 + 7 * q ^ 16 + 6 * q ^ 18 + 5 * q ^ 20 + 3 * q ^ 22 + 2 * q ^ 24 + q ^ 26)
      + q ^ 2 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24)
      + q ^ 4 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20)
      + q ^ 4 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 2 * q ^ 10 + 3 * q ^ 12 + 2 * q ^ 14 + 2 * q ^ 16 + q ^ 18 + q ^ 20)
      + q ^ 8 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12)
      + q ^ 14 * (1) := by
  rw [S, hookTable_8]
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  have h0 := dimq_8_0 hq hB
  have h1 := dimq_8_1 hq hB
  have h2 := dimq_8_2 hq hB
  have h3 := dimq_8_3 hq hB
  have h4 := dimq_8_4 hq hB
  have h5 := dimq_8_5 hq hB
  have h6 := dimq_8_6 hq hB
  have h7 := dimq_8_7 hq hB
  have h8 := dimq_8_8 hq hB
  have h9 := dimq_8_9 hq hB
  have h10 := dimq_8_10 hq hB
  have h11 := dimq_8_11 hq hB
  have h12 := dimq_8_12 hq hB
  have h13 := dimq_8_13 hq hB
  have h14 := dimq_8_14 hq hB
  have h15 := dimq_8_15 hq hB
  have h16 := dimq_8_16 hq hB
  have h17 := dimq_8_17 hq hB
  have h18 := dimq_8_18 hq hB
  have h19 := dimq_8_19 hq hB
  have h20 := dimq_8_20 hq hB
  have h21 := dimq_8_21 hq hB
  linear_combination q ^ 14 * h0 + q ^ 8 * h1 + q ^ 4 * h2 + q ^ 2 * h3 + q ^ 2 * h4 + q ^ 4 * h5 + q ^ 1 * h6 + q ^ 0 * h7 + q ^ 0 * h8 + q ^ 0 * h9 + q ^ 2 * h10 + q ^ 0 * h11 + q ^ 0 * h12 + q ^ 0 * h13 + q ^ 2 * h14 + q ^ 2 * h15 + q ^ 1 * h16 + q ^ 2 * h17 + q ^ 4 * h18 + q ^ 4 * h19 + q ^ 8 * h20 + q ^ 14 * h21

/-- The hook multisets of the partitions of `9`, as `partitionsList` enumerates them. -/
theorem hookTable_9 : (partitionsList 9).map hooksOf =
    [[9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 1, 7, 6, 5, 4, 3, 2, 1], [8, 2, 7, 1, 5, 4, 3, 2, 1], [7, 3, 6, 2, 5, 1, 3, 2, 1], [6, 4, 5, 3, 4, 2, 3, 1, 1], [9, 2, 1, 6, 5, 4, 3, 2, 1], [8, 3, 1, 6, 1, 4, 3, 2, 1], [7, 4, 1, 5, 2, 4, 1, 2, 1], [6, 5, 1, 4, 3, 3, 2, 2, 1], [7, 3, 2, 6, 2, 1, 3, 2, 1], [6, 4, 2, 5, 3, 1, 3, 1, 1], [5, 4, 3, 4, 3, 2, 3, 2, 1], [9, 3, 2, 1, 5, 4, 3, 2, 1], [8, 4, 2, 1, 5, 1, 3, 2, 1], [7, 5, 2, 1, 4, 2, 3, 1, 1], [7, 4, 3, 1, 5, 2, 1, 2, 1], [6, 5, 3, 1, 4, 3, 1, 2, 1], [6, 4, 3, 2, 5, 3, 2, 1, 1], [9, 4, 3, 2, 1, 4, 3, 2, 1], [8, 5, 3, 2, 1, 4, 1, 2, 1], [7, 6, 3, 2, 1, 3, 2, 2, 1], [7, 5, 4, 2, 1, 4, 2, 1, 1], [6, 5, 4, 3, 1, 4, 3, 2, 1], [9, 5, 4, 3, 2, 1, 3, 2, 1], [8, 6, 4, 3, 2, 1, 3, 1, 1], [7, 6, 5, 3, 2, 1, 3, 2, 1], [9, 6, 5, 4, 3, 2, 1, 2, 1], [8, 7, 5, 4, 3, 2, 1, 2, 1], [9, 7, 6, 5, 4, 3, 2, 1, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1]] := by decide

theorem dimq_9_0 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 9 [9, 8, 7, 6, 5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_1 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 7 * dimq q 9 [9, 1, 7, 6, 5, 4, 3, 2, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 + q ^ 14 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 7 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 9 [8, 2, 7, 1, 5, 4, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_3 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 15 * dimq q 9 [7, 3, 6, 2, 5, 1, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 3 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 5 * q ^ 14 + 5 * q ^ 16 + 5 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 15 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_4 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 16 * dimq q 9 [6, 4, 5, 3, 4, 2, 3, 1, 1] = 1 + q ^ 2 + q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 4 * q ^ 14 + 4 * q ^ 16 + 4 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30 + q ^ 32 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 16 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_5 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 9 [9, 2, 1, 6, 5, 4, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_6 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 16 * dimq q 9 [8, 3, 1, 6, 1, 4, 3, 2, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 7 * q ^ 8 + 8 * q ^ 10 + 10 * q ^ 12 + 11 * q ^ 14 + 11 * q ^ 16 + 11 * q ^ 18 + 10 * q ^ 20 + 8 * q ^ 22 + 7 * q ^ 24 + 5 * q ^ 26 + 3 * q ^ 28 + 2 * q ^ 30 + q ^ 32 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 16 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_7 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [7, 4, 1, 5, 2, 4, 1, 2, 1] = 1 + 2 * q ^ 2 + 4 * q ^ 4 + 5 * q ^ 6 + 8 * q ^ 8 + 10 * q ^ 10 + 13 * q ^ 12 + 14 * q ^ 14 + 16 * q ^ 16 + 16 * q ^ 18 + 16 * q ^ 20 + 14 * q ^ 22 + 13 * q ^ 24 + 10 * q ^ 26 + 8 * q ^ 28 + 5 * q ^ 30 + 4 * q ^ 32 + 2 * q ^ 34 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_8 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [6, 5, 1, 4, 3, 3, 2, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 7 * q ^ 14 + 8 * q ^ 16 + 8 * q ^ 18 + 8 * q ^ 20 + 7 * q ^ 22 + 7 * q ^ 24 + 5 * q ^ 26 + 4 * q ^ 28 + 3 * q ^ 30 + 2 * q ^ 32 + q ^ 34 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_9 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [7, 3, 2, 6, 2, 1, 3, 2, 1] = 1 + q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 10 * q ^ 12 + 10 * q ^ 14 + 12 * q ^ 16 + 12 * q ^ 18 + 12 * q ^ 20 + 10 * q ^ 22 + 10 * q ^ 24 + 7 * q ^ 26 + 6 * q ^ 28 + 4 * q ^ 30 + 3 * q ^ 32 + q ^ 34 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_10 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 19 * dimq q 9 [6, 4, 2, 5, 3, 1, 3, 1, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 7 * q ^ 8 + 9 * q ^ 10 + 12 * q ^ 12 + 14 * q ^ 14 + 15 * q ^ 16 + 16 * q ^ 18 + 16 * q ^ 20 + 15 * q ^ 22 + 14 * q ^ 24 + 12 * q ^ 26 + 9 * q ^ 28 + 7 * q ^ 30 + 5 * q ^ 32 + 3 * q ^ 34 + 2 * q ^ 36 + q ^ 38 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 19 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_11 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [5, 4, 3, 4, 3, 2, 3, 2, 1] = 1 + q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 4 * q ^ 16 + 4 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 4 * q ^ 24 + 2 * q ^ 26 + 2 * q ^ 28 + 2 * q ^ 30 + q ^ 32 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_12 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 15 * dimq q 9 [9, 3, 2, 1, 5, 4, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 5 * q ^ 10 + 6 * q ^ 12 + 6 * q ^ 14 + 6 * q ^ 16 + 6 * q ^ 18 + 5 * q ^ 20 + 4 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 15 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_13 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [8, 4, 2, 1, 5, 1, 3, 2, 1] = 1 + 2 * q ^ 2 + 4 * q ^ 4 + 6 * q ^ 6 + 9 * q ^ 8 + 12 * q ^ 10 + 15 * q ^ 12 + 17 * q ^ 14 + 19 * q ^ 16 + 19 * q ^ 18 + 19 * q ^ 20 + 17 * q ^ 22 + 15 * q ^ 24 + 12 * q ^ 26 + 9 * q ^ 28 + 6 * q ^ 30 + 4 * q ^ 32 + 2 * q ^ 34 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_14 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 19 * dimq q 9 [7, 5, 2, 1, 4, 2, 3, 1, 1] = 1 + 2 * q ^ 2 + 4 * q ^ 4 + 6 * q ^ 6 + 9 * q ^ 8 + 12 * q ^ 10 + 15 * q ^ 12 + 18 * q ^ 14 + 20 * q ^ 16 + 21 * q ^ 18 + 21 * q ^ 20 + 20 * q ^ 22 + 18 * q ^ 24 + 15 * q ^ 26 + 12 * q ^ 28 + 9 * q ^ 30 + 6 * q ^ 32 + 4 * q ^ 34 + 2 * q ^ 36 + q ^ 38 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 19 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_15 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 19 * dimq q 9 [7, 4, 3, 1, 5, 2, 1, 2, 1] = 1 + 2 * q ^ 2 + 4 * q ^ 4 + 6 * q ^ 6 + 9 * q ^ 8 + 12 * q ^ 10 + 15 * q ^ 12 + 18 * q ^ 14 + 20 * q ^ 16 + 21 * q ^ 18 + 21 * q ^ 20 + 20 * q ^ 22 + 18 * q ^ 24 + 15 * q ^ 26 + 12 * q ^ 28 + 9 * q ^ 30 + 6 * q ^ 32 + 4 * q ^ 34 + 2 * q ^ 36 + q ^ 38 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 19 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_16 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 19 * dimq q 9 [6, 5, 3, 1, 4, 3, 1, 2, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 7 * q ^ 8 + 9 * q ^ 10 + 12 * q ^ 12 + 14 * q ^ 14 + 15 * q ^ 16 + 16 * q ^ 18 + 16 * q ^ 20 + 15 * q ^ 22 + 14 * q ^ 24 + 12 * q ^ 26 + 9 * q ^ 28 + 7 * q ^ 30 + 5 * q ^ 32 + 3 * q ^ 34 + 2 * q ^ 36 + q ^ 38 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 19 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_17 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [6, 4, 3, 2, 5, 3, 2, 1, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 7 * q ^ 14 + 8 * q ^ 16 + 8 * q ^ 18 + 8 * q ^ 20 + 7 * q ^ 22 + 7 * q ^ 24 + 5 * q ^ 26 + 4 * q ^ 28 + 3 * q ^ 30 + 2 * q ^ 32 + q ^ 34 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_18 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 16 * dimq q 9 [9, 4, 3, 2, 1, 4, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 7 * q ^ 14 + 8 * q ^ 16 + 7 * q ^ 18 + 7 * q ^ 20 + 5 * q ^ 22 + 5 * q ^ 24 + 3 * q ^ 26 + 2 * q ^ 28 + q ^ 30 + q ^ 32 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 16 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_19 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [8, 5, 3, 2, 1, 4, 1, 2, 1] = 1 + 2 * q ^ 2 + 4 * q ^ 4 + 6 * q ^ 6 + 9 * q ^ 8 + 12 * q ^ 10 + 15 * q ^ 12 + 17 * q ^ 14 + 19 * q ^ 16 + 19 * q ^ 18 + 19 * q ^ 20 + 17 * q ^ 22 + 15 * q ^ 24 + 12 * q ^ 26 + 9 * q ^ 28 + 6 * q ^ 30 + 4 * q ^ 32 + 2 * q ^ 34 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_20 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [7, 6, 3, 2, 1, 3, 2, 2, 1] = 1 + q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 10 * q ^ 12 + 10 * q ^ 14 + 12 * q ^ 16 + 12 * q ^ 18 + 12 * q ^ 20 + 10 * q ^ 22 + 10 * q ^ 24 + 7 * q ^ 26 + 6 * q ^ 28 + 4 * q ^ 30 + 3 * q ^ 32 + q ^ 34 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_21 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 18 * dimq q 9 [7, 5, 4, 2, 1, 4, 2, 1, 1] = 1 + 2 * q ^ 2 + 4 * q ^ 4 + 5 * q ^ 6 + 8 * q ^ 8 + 10 * q ^ 10 + 13 * q ^ 12 + 14 * q ^ 14 + 16 * q ^ 16 + 16 * q ^ 18 + 16 * q ^ 20 + 14 * q ^ 22 + 13 * q ^ 24 + 10 * q ^ 26 + 8 * q ^ 28 + 5 * q ^ 30 + 4 * q ^ 32 + 2 * q ^ 34 + q ^ 36 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 18 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_22 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 16 * dimq q 9 [6, 5, 4, 3, 1, 4, 3, 2, 1] = 1 + q ^ 2 + q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 4 * q ^ 14 + 4 * q ^ 16 + 4 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30 + q ^ 32 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 16 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_23 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 15 * dimq q 9 [9, 5, 4, 3, 2, 1, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 5 * q ^ 10 + 6 * q ^ 12 + 6 * q ^ 14 + 6 * q ^ 16 + 6 * q ^ 18 + 5 * q ^ 20 + 4 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 15 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_24 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 16 * dimq q 9 [8, 6, 4, 3, 2, 1, 3, 1, 1] = 1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 7 * q ^ 8 + 8 * q ^ 10 + 10 * q ^ 12 + 11 * q ^ 14 + 11 * q ^ 16 + 11 * q ^ 18 + 10 * q ^ 20 + 8 * q ^ 22 + 7 * q ^ 24 + 5 * q ^ 26 + 3 * q ^ 28 + 2 * q ^ 30 + q ^ 32 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 16 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_25 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 15 * dimq q 9 [7, 6, 5, 3, 2, 1, 3, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 3 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 5 * q ^ 14 + 5 * q ^ 16 + 5 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 15 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_26 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 9 [9, 6, 5, 4, 3, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_27 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 12 * dimq q 9 [8, 7, 5, 4, 3, 2, 1, 2, 1] = 1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 12 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_28 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 7 * dimq q 9 [9, 7, 6, 5, 4, 3, 2, 1, 1] = 1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 + q ^ 14 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 7 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

theorem dimq_9_29 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 0 * dimq q 9 [9, 8, 7, 6, 5, 4, 3, 2, 1] = 1 :=
  dimq_eq hq (fun h hh => hB h (by simp at hh; omega) (by simp at hh; omega)) 0 _
    [1, 2, 3, 4, 5, 6, 7, 8, 9] (by decide) (by decide)
    (by simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, qb2,
          Finset.sum_range_succ, Finset.sum_range_zero]; ring)

set_option maxHeartbeats 8000000 in
theorem S_9_19 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 19 * S q 9 = q ^ 19 * (1)
      + q ^ 12 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 + q ^ 14)
      + q ^ 7 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24)
      + q ^ 4 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 3 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 5 * q ^ 14 + 5 * q ^ 16 + 5 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30)
      + q ^ 3 * (1 + q ^ 2 + q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 4 * q ^ 14 + 4 * q ^ 16 + 4 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30 + q ^ 32)
      + q ^ 7 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24)
      + q ^ 3 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 7 * q ^ 8 + 8 * q ^ 10 + 10 * q ^ 12 + 11 * q ^ 14 + 11 * q ^ 16 + 11 * q ^ 18 + 10 * q ^ 20 + 8 * q ^ 22 + 7 * q ^ 24 + 5 * q ^ 26 + 3 * q ^ 28 + 2 * q ^ 30 + q ^ 32)
      + q ^ 1 * (1 + 2 * q ^ 2 + 4 * q ^ 4 + 5 * q ^ 6 + 8 * q ^ 8 + 10 * q ^ 10 + 13 * q ^ 12 + 14 * q ^ 14 + 16 * q ^ 16 + 16 * q ^ 18 + 16 * q ^ 20 + 14 * q ^ 22 + 13 * q ^ 24 + 10 * q ^ 26 + 8 * q ^ 28 + 5 * q ^ 30 + 4 * q ^ 32 + 2 * q ^ 34 + q ^ 36)
      + q ^ 1 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 7 * q ^ 14 + 8 * q ^ 16 + 8 * q ^ 18 + 8 * q ^ 20 + 7 * q ^ 22 + 7 * q ^ 24 + 5 * q ^ 26 + 4 * q ^ 28 + 3 * q ^ 30 + 2 * q ^ 32 + q ^ 34 + q ^ 36)
      + q ^ 1 * (1 + q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 10 * q ^ 12 + 10 * q ^ 14 + 12 * q ^ 16 + 12 * q ^ 18 + 12 * q ^ 20 + 10 * q ^ 22 + 10 * q ^ 24 + 7 * q ^ 26 + 6 * q ^ 28 + 4 * q ^ 30 + 3 * q ^ 32 + q ^ 34 + q ^ 36)
      + q ^ 0 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 7 * q ^ 8 + 9 * q ^ 10 + 12 * q ^ 12 + 14 * q ^ 14 + 15 * q ^ 16 + 16 * q ^ 18 + 16 * q ^ 20 + 15 * q ^ 22 + 14 * q ^ 24 + 12 * q ^ 26 + 9 * q ^ 28 + 7 * q ^ 30 + 5 * q ^ 32 + 3 * q ^ 34 + 2 * q ^ 36 + q ^ 38)
      + q ^ 1 * (1 + q ^ 4 + 2 * q ^ 6 + 2 * q ^ 8 + 2 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 4 * q ^ 16 + 4 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 4 * q ^ 24 + 2 * q ^ 26 + 2 * q ^ 28 + 2 * q ^ 30 + q ^ 32 + q ^ 36)
      + q ^ 4 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 5 * q ^ 10 + 6 * q ^ 12 + 6 * q ^ 14 + 6 * q ^ 16 + 6 * q ^ 18 + 5 * q ^ 20 + 4 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30)
      + q ^ 1 * (1 + 2 * q ^ 2 + 4 * q ^ 4 + 6 * q ^ 6 + 9 * q ^ 8 + 12 * q ^ 10 + 15 * q ^ 12 + 17 * q ^ 14 + 19 * q ^ 16 + 19 * q ^ 18 + 19 * q ^ 20 + 17 * q ^ 22 + 15 * q ^ 24 + 12 * q ^ 26 + 9 * q ^ 28 + 6 * q ^ 30 + 4 * q ^ 32 + 2 * q ^ 34 + q ^ 36)
      + q ^ 0 * (1 + 2 * q ^ 2 + 4 * q ^ 4 + 6 * q ^ 6 + 9 * q ^ 8 + 12 * q ^ 10 + 15 * q ^ 12 + 18 * q ^ 14 + 20 * q ^ 16 + 21 * q ^ 18 + 21 * q ^ 20 + 20 * q ^ 22 + 18 * q ^ 24 + 15 * q ^ 26 + 12 * q ^ 28 + 9 * q ^ 30 + 6 * q ^ 32 + 4 * q ^ 34 + 2 * q ^ 36 + q ^ 38)
      + q ^ 0 * (1 + 2 * q ^ 2 + 4 * q ^ 4 + 6 * q ^ 6 + 9 * q ^ 8 + 12 * q ^ 10 + 15 * q ^ 12 + 18 * q ^ 14 + 20 * q ^ 16 + 21 * q ^ 18 + 21 * q ^ 20 + 20 * q ^ 22 + 18 * q ^ 24 + 15 * q ^ 26 + 12 * q ^ 28 + 9 * q ^ 30 + 6 * q ^ 32 + 4 * q ^ 34 + 2 * q ^ 36 + q ^ 38)
      + q ^ 0 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 7 * q ^ 8 + 9 * q ^ 10 + 12 * q ^ 12 + 14 * q ^ 14 + 15 * q ^ 16 + 16 * q ^ 18 + 16 * q ^ 20 + 15 * q ^ 22 + 14 * q ^ 24 + 12 * q ^ 26 + 9 * q ^ 28 + 7 * q ^ 30 + 5 * q ^ 32 + 3 * q ^ 34 + 2 * q ^ 36 + q ^ 38)
      + q ^ 1 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 7 * q ^ 14 + 8 * q ^ 16 + 8 * q ^ 18 + 8 * q ^ 20 + 7 * q ^ 22 + 7 * q ^ 24 + 5 * q ^ 26 + 4 * q ^ 28 + 3 * q ^ 30 + 2 * q ^ 32 + q ^ 34 + q ^ 36)
      + q ^ 3 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 5 * q ^ 8 + 5 * q ^ 10 + 7 * q ^ 12 + 7 * q ^ 14 + 8 * q ^ 16 + 7 * q ^ 18 + 7 * q ^ 20 + 5 * q ^ 22 + 5 * q ^ 24 + 3 * q ^ 26 + 2 * q ^ 28 + q ^ 30 + q ^ 32)
      + q ^ 1 * (1 + 2 * q ^ 2 + 4 * q ^ 4 + 6 * q ^ 6 + 9 * q ^ 8 + 12 * q ^ 10 + 15 * q ^ 12 + 17 * q ^ 14 + 19 * q ^ 16 + 19 * q ^ 18 + 19 * q ^ 20 + 17 * q ^ 22 + 15 * q ^ 24 + 12 * q ^ 26 + 9 * q ^ 28 + 6 * q ^ 30 + 4 * q ^ 32 + 2 * q ^ 34 + q ^ 36)
      + q ^ 1 * (1 + q ^ 2 + 3 * q ^ 4 + 4 * q ^ 6 + 6 * q ^ 8 + 7 * q ^ 10 + 10 * q ^ 12 + 10 * q ^ 14 + 12 * q ^ 16 + 12 * q ^ 18 + 12 * q ^ 20 + 10 * q ^ 22 + 10 * q ^ 24 + 7 * q ^ 26 + 6 * q ^ 28 + 4 * q ^ 30 + 3 * q ^ 32 + q ^ 34 + q ^ 36)
      + q ^ 1 * (1 + 2 * q ^ 2 + 4 * q ^ 4 + 5 * q ^ 6 + 8 * q ^ 8 + 10 * q ^ 10 + 13 * q ^ 12 + 14 * q ^ 14 + 16 * q ^ 16 + 16 * q ^ 18 + 16 * q ^ 20 + 14 * q ^ 22 + 13 * q ^ 24 + 10 * q ^ 26 + 8 * q ^ 28 + 5 * q ^ 30 + 4 * q ^ 32 + 2 * q ^ 34 + q ^ 36)
      + q ^ 3 * (1 + q ^ 2 + q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 4 * q ^ 14 + 4 * q ^ 16 + 4 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30 + q ^ 32)
      + q ^ 4 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 4 * q ^ 8 + 5 * q ^ 10 + 6 * q ^ 12 + 6 * q ^ 14 + 6 * q ^ 16 + 6 * q ^ 18 + 5 * q ^ 20 + 4 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30)
      + q ^ 3 * (1 + 2 * q ^ 2 + 3 * q ^ 4 + 5 * q ^ 6 + 7 * q ^ 8 + 8 * q ^ 10 + 10 * q ^ 12 + 11 * q ^ 14 + 11 * q ^ 16 + 11 * q ^ 18 + 10 * q ^ 20 + 8 * q ^ 22 + 7 * q ^ 24 + 5 * q ^ 26 + 3 * q ^ 28 + 2 * q ^ 30 + q ^ 32)
      + q ^ 4 * (1 + q ^ 2 + 2 * q ^ 4 + 3 * q ^ 6 + 3 * q ^ 8 + 4 * q ^ 10 + 5 * q ^ 12 + 5 * q ^ 14 + 5 * q ^ 16 + 5 * q ^ 18 + 4 * q ^ 20 + 3 * q ^ 22 + 3 * q ^ 24 + 2 * q ^ 26 + q ^ 28 + q ^ 30)
      + q ^ 7 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 4 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24)
      + q ^ 7 * (1 + q ^ 2 + 2 * q ^ 4 + 2 * q ^ 6 + 3 * q ^ 8 + 3 * q ^ 10 + 3 * q ^ 12 + 3 * q ^ 14 + 3 * q ^ 16 + 2 * q ^ 18 + 2 * q ^ 20 + q ^ 22 + q ^ 24)
      + q ^ 12 * (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 + q ^ 14)
      + q ^ 19 * (1) := by
  rw [S, hookTable_9]
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  have h0 := dimq_9_0 hq hB
  have h1 := dimq_9_1 hq hB
  have h2 := dimq_9_2 hq hB
  have h3 := dimq_9_3 hq hB
  have h4 := dimq_9_4 hq hB
  have h5 := dimq_9_5 hq hB
  have h6 := dimq_9_6 hq hB
  have h7 := dimq_9_7 hq hB
  have h8 := dimq_9_8 hq hB
  have h9 := dimq_9_9 hq hB
  have h10 := dimq_9_10 hq hB
  have h11 := dimq_9_11 hq hB
  have h12 := dimq_9_12 hq hB
  have h13 := dimq_9_13 hq hB
  have h14 := dimq_9_14 hq hB
  have h15 := dimq_9_15 hq hB
  have h16 := dimq_9_16 hq hB
  have h17 := dimq_9_17 hq hB
  have h18 := dimq_9_18 hq hB
  have h19 := dimq_9_19 hq hB
  have h20 := dimq_9_20 hq hB
  have h21 := dimq_9_21 hq hB
  have h22 := dimq_9_22 hq hB
  have h23 := dimq_9_23 hq hB
  have h24 := dimq_9_24 hq hB
  have h25 := dimq_9_25 hq hB
  have h26 := dimq_9_26 hq hB
  have h27 := dimq_9_27 hq hB
  have h28 := dimq_9_28 hq hB
  have h29 := dimq_9_29 hq hB
  linear_combination q ^ 19 * h0 + q ^ 12 * h1 + q ^ 7 * h2 + q ^ 4 * h3 + q ^ 3 * h4 + q ^ 7 * h5 + q ^ 3 * h6 + q ^ 1 * h7 + q ^ 1 * h8 + q ^ 1 * h9 + q ^ 0 * h10 + q ^ 1 * h11 + q ^ 4 * h12 + q ^ 1 * h13 + q ^ 0 * h14 + q ^ 0 * h15 + q ^ 0 * h16 + q ^ 1 * h17 + q ^ 3 * h18 + q ^ 1 * h19 + q ^ 1 * h20 + q ^ 1 * h21 + q ^ 3 * h22 + q ^ 4 * h23 + q ^ 3 * h24 + q ^ 4 * h25 + q ^ 7 * h26 + q ^ 7 * h27 + q ^ 12 * h28 + q ^ 19 * h29

set_option maxHeartbeats 8000000 in
/-- The cleared Habiro tail at `n = 2`, derived from the definition: `q^0 · D(2) = P_2(q)`. -/
theorem tail_2 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 2 → qb2 q k ≠ 0) :
    q ^ 0 * D q 2 = 0 := by
  have hS00 := S_2_0 hq hB
  have hS0 := (show q ^ 0 * S q 2 = q ^ 0 * (q ^ 0 * S q 2) by ring).trans
    (congrArg (q ^ 0 * ·) hS00)
  have hS1 : q ^ 0 * S q 1 = q ^ 0 := by rw [S_1, mul_one]
  have hS2 : q ^ 0 * S q 0 = q ^ 0 := by rw [S_0, mul_one]
  have hb := pow_mul_qbal hq (q := q) 1
  simp only [qb2, Finset.sum_range_succ, Finset.sum_range_zero] at hb
  apply mul_left_cancel₀ (pow_ne_zero 0 hq)
  rw [D, show (2 : ℕ) - 1 = 1 from rfl, show (2 : ℕ) - 2 = 0 from rfl]
  linear_combination hS0 - hS1 - (q ^ 0 * S q 0) * hb - (1) * hS2

set_option maxHeartbeats 8000000 in
/-- The cleared Habiro tail at `n = 3`, derived from the definition: `q^0 · D(3) = P_3(q)`. -/
theorem tail_3 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 3 → qb2 q k ≠ 0) :
    q ^ 0 * D q 3 = 0 := by
  have hS00 := S_3_1 hq hB
  have hS0 := (show q ^ 1 * S q 3 = q ^ 0 * (q ^ 1 * S q 3) by ring).trans
    (congrArg (q ^ 0 * ·) hS00)
  have hS10 := S_2_0 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS1 := (show q ^ 1 * S q 2 = q ^ 1 * (q ^ 0 * S q 2) by ring).trans
    (congrArg (q ^ 1 * ·) hS10)
  have hS2 : q ^ 0 * S q 1 = q ^ 0 := by rw [S_1, mul_one]
  have hb := pow_mul_qbal hq (q := q) 2
  simp only [qb2, Finset.sum_range_succ, Finset.sum_range_zero] at hb
  apply mul_left_cancel₀ (pow_ne_zero 1 hq)
  rw [D, show (3 : ℕ) - 1 = 2 from rfl, show (3 : ℕ) - 2 = 1 from rfl]
  linear_combination hS0 - hS1 - (q ^ 0 * S q 1) * hb - (1 + q ^ 2) * hS2

set_option maxHeartbeats 8000000 in
/-- The cleared Habiro tail at `n = 4`, derived from the definition: `q^2 · D(4) = P_4(q)`. -/
theorem tail_4 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 4 → qb2 q k ≠ 0) :
    q ^ 2 * D q 4 = 1 - q - q ^ 3 + q ^ 4 := by
  have hS00 := S_4_2 hq hB
  have hS0 := (show q ^ 2 * S q 4 = q ^ 0 * (q ^ 2 * S q 4) by ring).trans
    (congrArg (q ^ 0 * ·) hS00)
  have hS10 := S_3_1 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS1 := (show q ^ 2 * S q 3 = q ^ 1 * (q ^ 1 * S q 3) by ring).trans
    (congrArg (q ^ 1 * ·) hS10)
  have hS20 := S_2_0 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS2 := (show q ^ 0 * S q 2 = q ^ 0 * (q ^ 0 * S q 2) by ring).trans
    (congrArg (q ^ 0 * ·) hS20)
  have hb := pow_mul_qbal hq (q := q) 3
  simp only [qb2, Finset.sum_range_succ, Finset.sum_range_zero] at hb
  apply mul_left_cancel₀ (pow_ne_zero 0 hq)
  rw [D, show (4 : ℕ) - 1 = 3 from rfl, show (4 : ℕ) - 2 = 2 from rfl]
  linear_combination hS0 - hS1 - (q ^ 0 * S q 2) * hb - (1 + q ^ 2 + q ^ 4) * hS2

set_option maxHeartbeats 8000000 in
/-- The cleared Habiro tail at `n = 5`, derived from the definition: `q^4 · D(5) = P_5(q)`. -/
theorem tail_5 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 5 → qb2 q k ≠ 0) :
    q ^ 4 * D q 5 = 2 - 2 * q ^ 2 - 2 * q ^ 6 + 2 * q ^ 8 := by
  have hS00 := S_5_4 hq hB
  have hS0 := (show q ^ 4 * S q 5 = q ^ 0 * (q ^ 4 * S q 5) by ring).trans
    (congrArg (q ^ 0 * ·) hS00)
  have hS10 := S_4_2 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS1 := (show q ^ 4 * S q 4 = q ^ 2 * (q ^ 2 * S q 4) by ring).trans
    (congrArg (q ^ 2 * ·) hS10)
  have hS20 := S_3_1 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS2 := (show q ^ 1 * S q 3 = q ^ 0 * (q ^ 1 * S q 3) by ring).trans
    (congrArg (q ^ 0 * ·) hS20)
  have hb := pow_mul_qbal hq (q := q) 4
  simp only [qb2, Finset.sum_range_succ, Finset.sum_range_zero] at hb
  apply mul_left_cancel₀ (pow_ne_zero 0 hq)
  rw [D, show (5 : ℕ) - 1 = 4 from rfl, show (5 : ℕ) - 2 = 3 from rfl]
  linear_combination hS0 - hS1 - (q ^ 1 * S q 3) * hb - (1 + q ^ 2 + q ^ 4 + q ^ 6) * hS2

set_option maxHeartbeats 8000000 in
/-- The cleared Habiro tail at `n = 6`, derived from the definition: `q^7 · D(6) = P_6(q)`. -/
theorem tail_6 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 6 → qb2 q k ≠ 0) :
    q ^ 7 * D q 6 = 1 + 3 * q + 2 * q ^ 2 - 4 * q ^ 3 - q ^ 5 + q ^ 6 - 4 * q ^ 7 + q ^ 8 - q ^ 9 - 4 * q ^ 11 + 2 * q ^ 12 + 3 * q ^ 13 + q ^ 14 := by
  have hS00 := S_6_7 hq hB
  have hS0 := (show q ^ 7 * S q 6 = q ^ 0 * (q ^ 7 * S q 6) by ring).trans
    (congrArg (q ^ 0 * ·) hS00)
  have hS10 := S_5_4 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS1 := (show q ^ 7 * S q 5 = q ^ 3 * (q ^ 4 * S q 5) by ring).trans
    (congrArg (q ^ 3 * ·) hS10)
  have hS20 := S_4_2 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS2 := (show q ^ 3 * S q 4 = q ^ 1 * (q ^ 2 * S q 4) by ring).trans
    (congrArg (q ^ 1 * ·) hS20)
  have hb := pow_mul_qbal hq (q := q) 5
  simp only [qb2, Finset.sum_range_succ, Finset.sum_range_zero] at hb
  apply mul_left_cancel₀ (pow_ne_zero 0 hq)
  rw [D, show (6 : ℕ) - 1 = 5 from rfl, show (6 : ℕ) - 2 = 4 from rfl]
  linear_combination hS0 - hS1 - (q ^ 3 * S q 4) * hb - (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8) * hS2

set_option maxHeartbeats 8000000 in
/-- The cleared Habiro tail at `n = 7`, derived from the definition: `q^10 · D(7) = P_7(q)`. -/
theorem tail_7 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 7 → qb2 q k ≠ 0) :
    q ^ 10 * D q 7 = 4 + 8 * q ^ 2 - 4 * q ^ 3 + 4 * q ^ 4 - 8 * q ^ 5 + 8 * q ^ 6 - 8 * q ^ 7 + 4 * q ^ 8 - 12 * q ^ 9 + 8 * q ^ 10 - 12 * q ^ 11 + 4 * q ^ 12 - 8 * q ^ 13 + 8 * q ^ 14 - 8 * q ^ 15 + 4 * q ^ 16 - 4 * q ^ 17 + 8 * q ^ 18 + 4 * q ^ 20 := by
  have hS00 := S_7_10 hq hB
  have hS0 := (show q ^ 10 * S q 7 = q ^ 0 * (q ^ 10 * S q 7) by ring).trans
    (congrArg (q ^ 0 * ·) hS00)
  have hS10 := S_6_7 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS1 := (show q ^ 10 * S q 6 = q ^ 3 * (q ^ 7 * S q 6) by ring).trans
    (congrArg (q ^ 3 * ·) hS10)
  have hS20 := S_5_4 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS2 := (show q ^ 5 * S q 5 = q ^ 1 * (q ^ 4 * S q 5) by ring).trans
    (congrArg (q ^ 1 * ·) hS20)
  have hb := pow_mul_qbal hq (q := q) 6
  simp only [qb2, Finset.sum_range_succ, Finset.sum_range_zero] at hb
  apply mul_left_cancel₀ (pow_ne_zero 0 hq)
  rw [D, show (7 : ℕ) - 1 = 6 from rfl, show (7 : ℕ) - 2 = 5 from rfl]
  linear_combination hS0 - hS1 - (q ^ 5 * S q 5) * hb - (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10) * hS2

set_option maxHeartbeats 8000000 in
/-- The cleared Habiro tail at `n = 8`, derived from the definition: `q^14 · D(8) = P_8(q)`. -/
theorem tail_8 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 8 → qb2 q k ≠ 0) :
    q ^ 14 * D q 8 = 6 + q + 9 * q ^ 2 + q ^ 3 + 10 * q ^ 4 - 2 * q ^ 5 + q ^ 6 - q ^ 7 + 6 * q ^ 8 - 5 * q ^ 9 - 3 * q ^ 10 - 8 * q ^ 11 - 2 * q ^ 12 - 8 * q ^ 13 - 10 * q ^ 14 - 8 * q ^ 15 - 2 * q ^ 16 - 8 * q ^ 17 - 3 * q ^ 18 - 5 * q ^ 19 + 6 * q ^ 20 - q ^ 21 + q ^ 22 - 2 * q ^ 23 + 10 * q ^ 24 + q ^ 25 + 9 * q ^ 26 + q ^ 27 + 6 * q ^ 28 := by
  have hS00 := S_8_14 hq hB
  have hS0 := (show q ^ 14 * S q 8 = q ^ 0 * (q ^ 14 * S q 8) by ring).trans
    (congrArg (q ^ 0 * ·) hS00)
  have hS10 := S_7_10 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS1 := (show q ^ 14 * S q 7 = q ^ 4 * (q ^ 10 * S q 7) by ring).trans
    (congrArg (q ^ 4 * ·) hS10)
  have hS20 := S_6_7 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS2 := (show q ^ 8 * S q 6 = q ^ 1 * (q ^ 7 * S q 6) by ring).trans
    (congrArg (q ^ 1 * ·) hS20)
  have hb := pow_mul_qbal hq (q := q) 7
  simp only [qb2, Finset.sum_range_succ, Finset.sum_range_zero] at hb
  apply mul_left_cancel₀ (pow_ne_zero 0 hq)
  rw [D, show (8 : ℕ) - 1 = 7 from rfl, show (8 : ℕ) - 2 = 6 from rfl]
  linear_combination hS0 - hS1 - (q ^ 8 * S q 6) * hb - (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12) * hS2

set_option maxHeartbeats 8000000 in
/-- The cleared Habiro tail at `n = 9`, derived from the definition: `q^19 · D(9) = P_9(q)`. -/
theorem tail_9 (hq : q ≠ 0) (hB : ∀ k, 1 ≤ k → k ≤ 9 → qb2 q k ≠ 0) :
    q ^ 19 * D q 9 = 4 + 9 * q + 4 * q ^ 2 + 14 * q ^ 3 + 4 * q ^ 4 + 22 * q ^ 5 - 4 * q ^ 6 + 25 * q ^ 7 - 12 * q ^ 8 + 30 * q ^ 9 - 24 * q ^ 10 + 38 * q ^ 11 - 40 * q ^ 12 + 34 * q ^ 13 - 52 * q ^ 14 + 33 * q ^ 15 - 64 * q ^ 16 + 33 * q ^ 17 - 72 * q ^ 18 + 36 * q ^ 19 - 72 * q ^ 20 + 33 * q ^ 21 - 64 * q ^ 22 + 33 * q ^ 23 - 52 * q ^ 24 + 34 * q ^ 25 - 40 * q ^ 26 + 38 * q ^ 27 - 24 * q ^ 28 + 30 * q ^ 29 - 12 * q ^ 30 + 25 * q ^ 31 - 4 * q ^ 32 + 22 * q ^ 33 + 4 * q ^ 34 + 14 * q ^ 35 + 4 * q ^ 36 + 9 * q ^ 37 + 4 * q ^ 38 := by
  have hS00 := S_9_19 hq hB
  have hS0 := (show q ^ 19 * S q 9 = q ^ 0 * (q ^ 19 * S q 9) by ring).trans
    (congrArg (q ^ 0 * ·) hS00)
  have hS10 := S_8_14 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS1 := (show q ^ 19 * S q 8 = q ^ 5 * (q ^ 14 * S q 8) by ring).trans
    (congrArg (q ^ 5 * ·) hS10)
  have hS20 := S_7_10 hq (fun k h1 h2 => hB k h1 (by omega))
  have hS2 := (show q ^ 12 * S q 7 = q ^ 2 * (q ^ 10 * S q 7) by ring).trans
    (congrArg (q ^ 2 * ·) hS20)
  have hb := pow_mul_qbal hq (q := q) 8
  simp only [qb2, Finset.sum_range_succ, Finset.sum_range_zero] at hb
  apply mul_left_cancel₀ (pow_ne_zero 0 hq)
  rw [D, show (9 : ℕ) - 1 = 8 from rfl, show (9 : ℕ) - 2 = 7 from rfl]
  linear_combination hS0 - hS1 - (q ^ 12 * S q 7) * hb - (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 + q ^ 14) * hS2

end Derivation2

/-! ## Part 2 — the cyclotomic-product predicate and the finite certificate -/

/-- `P` is a product of cyclotomic polynomials up to a constant and a power of `X`. -/
def IsCycloProduct (P : ℤ[X]) : Prop :=
  ∃ (c : ℤ) (j : ℕ) (s : Multiset ℕ), P = C c * X ^ j * (s.map (fun k => cyclotomic k ℤ)).prod

theorem intCast_pow_eq_one_iff {p : ℕ} (a : ℤ) (k : ℕ) :
    ((a : ZMod p) ^ k = 1) ↔ ((p : ℤ) ∣ a ^ k - 1) := by
  rw [← ZMod.intCast_zmod_eq_zero_iff_dvd, Int.cast_sub, Int.cast_pow, Int.cast_one, sub_eq_zero]

theorem mem_of_prime_dvd_prod (ps : List ℕ) (hps : ∀ r ∈ ps, r.Prime) {r m : ℕ}
    (hr : r.Prime) (h : r ∣ m) (hm : m = ps.prod) : r ∈ ps := by
  subst hm
  induction ps with
  | nil => simp at h; exact absurd h hr.one_lt.ne'
  | cons x xs ih =>
    rw [List.prod_cons] at h
    rcases (Nat.Prime.dvd_mul hr).mp h with h1 | h1
    · have hx := hps x (by simp)
      rw [(Nat.prime_dvd_prime_iff_eq hr hx).mp h1]; simp
    · exact List.mem_cons_of_mem _ (ih (fun y hy => hps y (by simp [hy])) h1)

/-- **The finite non-cyclotomicity certificate.**  See the module docstring. -/
theorem not_isCycloProduct_of_witness (P : ℤ[X]) (d : ℕ) {p : ℕ} [Fact p.Prime] (a b : ℤ) (m : ℕ)
    (hm0 : 0 < m) (hd : P.natDegree ≤ d) (ha : (p : ℤ) ∣ P.eval a) (hb : ¬ (p : ℤ) ∣ P.eval b)
    (ha0 : ¬ (p : ℤ) ∣ a) (ham : (a : ZMod p) ^ m = 1)
    (hpr : ∀ r : ℕ, r.Prime → r ∣ m → ¬ (a : ZMod p) ^ (m / r) = 1)
    (htot : d < Nat.totient m) : ¬ IsCycloProduct P := by
  rintro ⟨c, j, s, hP⟩
  have hord : orderOf (a : ZMod p) = m := orderOf_eq_of_pow_and_pow_div_prime hm0 ham hpr
  set Pp : (ZMod p)[X] := P.map (Int.castRingHom (ZMod p)) with hPpdef
  have key : ∀ x : ℤ, ((P.eval x : ℤ) : ZMod p) = Pp.eval (x : ZMod p) := by
    intro x
    rw [hPpdef, Polynomial.eval_map, show ((x : ZMod p)) = Int.castRingHom (ZMod p) x from rfl,
      Polynomial.eval₂_hom]
    rfl
  have hPa : Pp.eval (a : ZMod p) = 0 := by
    rw [← key]; exact (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).mpr ha
  have hPb : Pp.eval (b : ZMod p) ≠ 0 := by
    rw [← key]; intro h; exact hb ((ZMod.intCast_zmod_eq_zero_iff_dvd _ _).mp h)
  have hPp : Pp = C (c : ZMod p) * X ^ j * (s.map (fun k => cyclotomic k (ZMod p))).prod := by
    rw [hPpdef, hP, Polynomial.map_mul, Polynomial.map_mul, Polynomial.map_pow, Polynomial.map_C,
      Polynomial.map_X, Polynomial.map_multiset_prod, Multiset.map_map]
    congr 2
    refine Multiset.map_congr rfl fun k _ => ?_
    simp [Polynomial.map_cyclotomic]
  rw [hPp] at hPa hPb
  simp only [eval_mul, eval_C, eval_pow, eval_X, eval_multiset_prod, Multiset.map_map,
    Function.comp_def] at hPa hPb
  have hc : (c : ZMod p) ≠ 0 := by
    intro h; apply hPb; rw [h]; ring
  have ha0' : (a : ZMod p) ≠ 0 := by
    intro h; exact ha0 ((ZMod.intCast_zmod_eq_zero_iff_dvd _ _).mp h)
  have hprod : (s.map fun k => (cyclotomic k (ZMod p)).eval (a : ZMod p)).prod = 0 := by
    rcases mul_eq_zero.mp hPa with h | h
    · rcases mul_eq_zero.mp h with h' | h'
      · exact absurd h' hc
      · exact absurd h' (pow_ne_zero _ ha0')
    · exact h
  obtain ⟨k, hks, hk0⟩ : ∃ k ∈ s, (cyclotomic k (ZMod p)).eval (a : ZMod p) = 0 := by
    have := Multiset.prod_eq_zero_iff.mp hprod
    simpa using this
  have hk_ne : k ≠ 0 := by rintro rfl; simp at hk0
  have hak : (a : ZMod p) ^ k = 1 := by
    obtain ⟨g, hg⟩ := cyclotomic.dvd_X_pow_sub_one k (ZMod p)
    have hev : (X ^ k - 1 : (ZMod p)[X]).eval (a : ZMod p) = 0 := by
      rw [hg, eval_mul, hk0, zero_mul]
    simpa [sub_eq_zero] using hev
  have hmk : m ∣ k := hord ▸ orderOf_dvd_of_pow_eq_one hak
  have htk : Nat.totient m ≤ Nat.totient k :=
    Nat.le_of_dvd (Nat.totient_pos.2 (Nat.pos_of_ne_zero hk_ne)) (Nat.totient_dvd_of_dvd hmk)
  have hP0 : P ≠ 0 := by rintro rfl; simp at hb
  have hdvdP : cyclotomic k ℤ ∣ P := by
    rw [hP]
    exact Dvd.dvd.mul_left (Multiset.dvd_prod (Multiset.mem_map_of_mem _ hks)) _
  have hdeg := natDegree_le_of_dvd hdvdP hP0
  rw [natDegree_cyclotomic] at hdeg
  omega

/-! ## Part 3 — the cleared tails and their certificates -/

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_4 = q^2·D(4)` as an integer polynomial (degree 4). -/
noncomputable def P4 : ℤ[X] :=
  1 - X - X ^ 3 + X ^ 4

set_option maxHeartbeats 4000000 in
theorem P4_map_eval {K : Type*} [Field K] (q : K) :
    (P4.map (Int.castRingHom K)).eval q = 1 - q - q ^ 3 + q ^ 4 := by
  simp only [P4, Polynomial.map_add, Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_pow,
    Polynomial.map_X, Polynomial.map_ofNat, Polynomial.map_one, Polynomial.map_neg,
    eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_5 = q^4·D(5)` as an integer polynomial (degree 8). -/
noncomputable def P5 : ℤ[X] :=
  2 - 2 * X ^ 2 - 2 * X ^ 6 + 2 * X ^ 8

set_option maxHeartbeats 4000000 in
theorem P5_map_eval {K : Type*} [Field K] (q : K) :
    (P5.map (Int.castRingHom K)).eval q = 2 - 2 * q ^ 2 - 2 * q ^ 6 + 2 * q ^ 8 := by
  simp only [P5, Polynomial.map_add, Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_pow,
    Polynomial.map_X, Polynomial.map_ofNat, Polynomial.map_one, Polynomial.map_neg,
    eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_6 = q^7·D(6)` as an integer polynomial (degree 14). -/
noncomputable def P6 : ℤ[X] :=
  1 + 3 * X + 2 * X ^ 2 - 4 * X ^ 3 - X ^ 5 + X ^ 6 - 4 * X ^ 7 + X ^ 8 - X ^ 9 - 4 * X ^ 11 + 2 * X ^ 12 + 3 * X ^ 13 + X ^ 14

set_option maxHeartbeats 4000000 in
theorem P6_map_eval {K : Type*} [Field K] (q : K) :
    (P6.map (Int.castRingHom K)).eval q = 1 + 3 * q + 2 * q ^ 2 - 4 * q ^ 3 - q ^ 5 + q ^ 6 - 4 * q ^ 7 + q ^ 8 - q ^ 9 - 4 * q ^ 11 + 2 * q ^ 12 + 3 * q ^ 13 + q ^ 14 := by
  simp only [P6, Polynomial.map_add, Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_pow,
    Polynomial.map_X, Polynomial.map_ofNat, Polynomial.map_one, Polynomial.map_neg,
    eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_7 = q^10·D(7)` as an integer polynomial (degree 20). -/
noncomputable def P7 : ℤ[X] :=
  4 + 8 * X ^ 2 - 4 * X ^ 3 + 4 * X ^ 4 - 8 * X ^ 5 + 8 * X ^ 6 - 8 * X ^ 7 + 4 * X ^ 8 - 12 * X ^ 9 + 8 * X ^ 10 - 12 * X ^ 11 + 4 * X ^ 12 - 8 * X ^ 13 + 8 * X ^ 14 - 8 * X ^ 15 + 4 * X ^ 16 - 4 * X ^ 17 + 8 * X ^ 18 + 4 * X ^ 20

set_option maxHeartbeats 4000000 in
theorem P7_map_eval {K : Type*} [Field K] (q : K) :
    (P7.map (Int.castRingHom K)).eval q = 4 + 8 * q ^ 2 - 4 * q ^ 3 + 4 * q ^ 4 - 8 * q ^ 5 + 8 * q ^ 6 - 8 * q ^ 7 + 4 * q ^ 8 - 12 * q ^ 9 + 8 * q ^ 10 - 12 * q ^ 11 + 4 * q ^ 12 - 8 * q ^ 13 + 8 * q ^ 14 - 8 * q ^ 15 + 4 * q ^ 16 - 4 * q ^ 17 + 8 * q ^ 18 + 4 * q ^ 20 := by
  simp only [P7, Polynomial.map_add, Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_pow,
    Polynomial.map_X, Polynomial.map_ofNat, Polynomial.map_one, Polynomial.map_neg,
    eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_8 = q^14·D(8)` as an integer polynomial (degree 28). -/
noncomputable def P8 : ℤ[X] :=
  6 + X + 9 * X ^ 2 + X ^ 3 + 10 * X ^ 4 - 2 * X ^ 5 + X ^ 6 - X ^ 7 + 6 * X ^ 8 - 5 * X ^ 9 - 3 * X ^ 10 - 8 * X ^ 11 - 2 * X ^ 12 - 8 * X ^ 13 - 10 * X ^ 14 - 8 * X ^ 15 - 2 * X ^ 16 - 8 * X ^ 17 - 3 * X ^ 18 - 5 * X ^ 19 + 6 * X ^ 20 - X ^ 21 + X ^ 22 - 2 * X ^ 23 + 10 * X ^ 24 + X ^ 25 + 9 * X ^ 26 + X ^ 27 + 6 * X ^ 28

set_option maxHeartbeats 4000000 in
theorem P8_map_eval {K : Type*} [Field K] (q : K) :
    (P8.map (Int.castRingHom K)).eval q = 6 + q + 9 * q ^ 2 + q ^ 3 + 10 * q ^ 4 - 2 * q ^ 5 + q ^ 6 - q ^ 7 + 6 * q ^ 8 - 5 * q ^ 9 - 3 * q ^ 10 - 8 * q ^ 11 - 2 * q ^ 12 - 8 * q ^ 13 - 10 * q ^ 14 - 8 * q ^ 15 - 2 * q ^ 16 - 8 * q ^ 17 - 3 * q ^ 18 - 5 * q ^ 19 + 6 * q ^ 20 - q ^ 21 + q ^ 22 - 2 * q ^ 23 + 10 * q ^ 24 + q ^ 25 + 9 * q ^ 26 + q ^ 27 + 6 * q ^ 28 := by
  simp only [P8, Polynomial.map_add, Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_pow,
    Polynomial.map_X, Polynomial.map_ofNat, Polynomial.map_one, Polynomial.map_neg,
    eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_9 = q^19·D(9)` as an integer polynomial (degree 38). -/
noncomputable def P9 : ℤ[X] :=
  4 + 9 * X + 4 * X ^ 2 + 14 * X ^ 3 + 4 * X ^ 4 + 22 * X ^ 5 - 4 * X ^ 6 + 25 * X ^ 7 - 12 * X ^ 8 + 30 * X ^ 9 - 24 * X ^ 10 + 38 * X ^ 11 - 40 * X ^ 12 + 34 * X ^ 13 - 52 * X ^ 14 + 33 * X ^ 15 - 64 * X ^ 16 + 33 * X ^ 17 - 72 * X ^ 18 + 36 * X ^ 19 - 72 * X ^ 20 + 33 * X ^ 21 - 64 * X ^ 22 + 33 * X ^ 23 - 52 * X ^ 24 + 34 * X ^ 25 - 40 * X ^ 26 + 38 * X ^ 27 - 24 * X ^ 28 + 30 * X ^ 29 - 12 * X ^ 30 + 25 * X ^ 31 - 4 * X ^ 32 + 22 * X ^ 33 + 4 * X ^ 34 + 14 * X ^ 35 + 4 * X ^ 36 + 9 * X ^ 37 + 4 * X ^ 38

set_option maxHeartbeats 4000000 in
theorem P9_map_eval {K : Type*} [Field K] (q : K) :
    (P9.map (Int.castRingHom K)).eval q = 4 + 9 * q + 4 * q ^ 2 + 14 * q ^ 3 + 4 * q ^ 4 + 22 * q ^ 5 - 4 * q ^ 6 + 25 * q ^ 7 - 12 * q ^ 8 + 30 * q ^ 9 - 24 * q ^ 10 + 38 * q ^ 11 - 40 * q ^ 12 + 34 * q ^ 13 - 52 * q ^ 14 + 33 * q ^ 15 - 64 * q ^ 16 + 33 * q ^ 17 - 72 * q ^ 18 + 36 * q ^ 19 - 72 * q ^ 20 + 33 * q ^ 21 - 64 * q ^ 22 + 33 * q ^ 23 - 52 * q ^ 24 + 34 * q ^ 25 - 40 * q ^ 26 + 38 * q ^ 27 - 24 * q ^ 28 + 30 * q ^ 29 - 12 * q ^ 30 + 25 * q ^ 31 - 4 * q ^ 32 + 22 * q ^ 33 + 4 * q ^ 34 + 14 * q ^ 35 + 4 * q ^ 36 + 9 * q ^ 37 + 4 * q ^ 38 := by
  simp only [P9, Polynomial.map_add, Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_pow,
    Polynomial.map_X, Polynomial.map_ofNat, Polynomial.map_one, Polynomial.map_neg,
    eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_10 = q^25·D(10)` as an integer polynomial (degree 50). -/
noncomputable def P10 : ℤ[X] :=
  1 + 12 * X + 6 * X ^ 2 + 18 * X ^ 3 + 9 * X ^ 4 + 37 * X ^ 5 + 11 * X ^ 6 + 34 * X ^ 7 + 15 * X ^ 8 + 49 * X ^ 9 + 9 * X ^ 10 + 34 * X ^ 11 + 12 * X ^ 12 + 39 * X ^ 13 + 7 * X ^ 14 + 8 * X ^ 15 - X ^ 16 - 6 * X ^ 17 - 10 * X ^ 18 - 42 * X ^ 19 - 20 * X ^ 20 - 50 * X ^ 21 - 27 * X ^ 22 - 84 * X ^ 23 - 28 * X ^ 24 - 66 * X ^ 25 - 28 * X ^ 26 - 84 * X ^ 27 - 27 * X ^ 28 - 50 * X ^ 29 - 20 * X ^ 30 - 42 * X ^ 31 - 10 * X ^ 32 - 6 * X ^ 33 - X ^ 34 + 8 * X ^ 35 + 7 * X ^ 36 + 39 * X ^ 37 + 12 * X ^ 38 + 34 * X ^ 39 + 9 * X ^ 40 + 49 * X ^ 41 + 15 * X ^ 42 + 34 * X ^ 43 + 11 * X ^ 44 + 37 * X ^ 45 + 9 * X ^ 46 + 18 * X ^ 47 + 6 * X ^ 48 + 12 * X ^ 49 + X ^ 50

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_11 = q^31·D(11)` as an integer polynomial (degree 62). -/
noncomputable def P11 : ℤ[X] :=
  5 + 12 * X + 18 * X ^ 2 + 20 * X ^ 3 + 27 * X ^ 4 + 46 * X ^ 5 + 44 * X ^ 6 + 58 * X ^ 7 + 49 * X ^ 8 + 90 * X ^ 9 + 58 * X ^ 10 + 94 * X ^ 11 + 50 * X ^ 12 + 130 * X ^ 13 + 34 * X ^ 14 + 126 * X ^ 15 + 5 * X ^ 16 + 142 * X ^ 17 - 37 * X ^ 18 + 114 * X ^ 19 - 96 * X ^ 20 + 116 * X ^ 21 - 159 * X ^ 22 + 74 * X ^ 23 - 222 * X ^ 24 + 68 * X ^ 25 - 273 * X ^ 26 + 24 * X ^ 27 - 315 * X ^ 28 + 36 * X ^ 29 - 340 * X ^ 30 + 4 * X ^ 31 - 340 * X ^ 32 + 36 * X ^ 33 - 315 * X ^ 34 + 24 * X ^ 35 - 273 * X ^ 36 + 68 * X ^ 37 - 222 * X ^ 38 + 74 * X ^ 39 - 159 * X ^ 40 + 116 * X ^ 41 - 96 * X ^ 42 + 114 * X ^ 43 - 37 * X ^ 44 + 142 * X ^ 45 + 5 * X ^ 46 + 126 * X ^ 47 + 34 * X ^ 48 + 130 * X ^ 49 + 50 * X ^ 50 + 94 * X ^ 51 + 58 * X ^ 52 + 90 * X ^ 53 + 49 * X ^ 54 + 58 * X ^ 55 + 44 * X ^ 56 + 46 * X ^ 57 + 27 * X ^ 58 + 20 * X ^ 59 + 18 * X ^ 60 + 12 * X ^ 61 + 5 * X ^ 62

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_12 = q^38·D(12)` as an integer polynomial (degree 76). -/
noncomputable def P12 : ℤ[X] :=
  10 + 6 * X + 40 * X ^ 2 + 13 * X ^ 3 + 72 * X ^ 4 + 23 * X ^ 5 + 132 * X ^ 6 + 37 * X ^ 7 + 197 * X ^ 8 + 43 * X ^ 9 + 280 * X ^ 10 + 46 * X ^ 11 + 349 * X ^ 12 + 44 * X ^ 13 + 444 * X ^ 14 + 28 * X ^ 15 + 491 * X ^ 16 - 15 * X ^ 17 + 562 * X ^ 18 - 61 * X ^ 19 + 564 * X ^ 20 - 140 * X ^ 21 + 548 * X ^ 22 - 240 * X ^ 23 + 476 * X ^ 24 - 349 * X ^ 25 + 420 * X ^ 26 - 468 * X ^ 27 + 275 * X ^ 28 - 600 * X ^ 29 + 186 * X ^ 30 - 708 * X ^ 31 + 61 * X ^ 32 - 805 * X ^ 33 - 14 * X ^ 34 - 882 * X ^ 35 - 107 * X ^ 36 - 912 * X ^ 37 - 92 * X ^ 38 - 912 * X ^ 39 - 107 * X ^ 40 - 882 * X ^ 41 - 14 * X ^ 42 - 805 * X ^ 43 + 61 * X ^ 44 - 708 * X ^ 45 + 186 * X ^ 46 - 600 * X ^ 47 + 275 * X ^ 48 - 468 * X ^ 49 + 420 * X ^ 50 - 349 * X ^ 51 + 476 * X ^ 52 - 240 * X ^ 53 + 548 * X ^ 54 - 140 * X ^ 55 + 564 * X ^ 56 - 61 * X ^ 57 + 562 * X ^ 58 - 15 * X ^ 59 + 491 * X ^ 60 + 28 * X ^ 61 + 444 * X ^ 62 + 44 * X ^ 63 + 349 * X ^ 64 + 46 * X ^ 65 + 280 * X ^ 66 + 43 * X ^ 67 + 197 * X ^ 68 + 37 * X ^ 69 + 132 * X ^ 70 + 23 * X ^ 71 + 72 * X ^ 72 + 13 * X ^ 73 + 40 * X ^ 74 + 6 * X ^ 75 + 10 * X ^ 76

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_13 = q^46·D(13)` as an integer polynomial (degree 92). -/
noncomputable def P13 : ℤ[X] :=
  10 + 12 * X + 36 * X ^ 2 + 34 * X ^ 3 + 81 * X ^ 4 + 66 * X ^ 5 + 144 * X ^ 6 + 122 * X ^ 7 + 248 * X ^ 8 + 180 * X ^ 9 + 358 * X ^ 10 + 258 * X ^ 11 + 515 * X ^ 12 + 330 * X ^ 13 + 669 * X ^ 14 + 406 * X ^ 15 + 850 * X ^ 16 + 450 * X ^ 17 + 1014 * X ^ 18 + 480 * X ^ 19 + 1192 * X ^ 20 + 442 * X ^ 21 + 1289 * X ^ 22 + 356 * X ^ 23 + 1389 * X ^ 24 + 196 * X ^ 25 + 1373 * X ^ 26 - 44 * X ^ 27 + 1331 * X ^ 28 - 362 * X ^ 29 + 1196 * X ^ 30 - 720 * X ^ 31 + 1033 * X ^ 32 - 1156 * X ^ 33 + 774 * X ^ 34 - 1594 * X ^ 35 + 554 * X ^ 36 - 2020 * X ^ 37 + 271 * X ^ 38 - 2422 * X ^ 39 + 54 * X ^ 40 - 2752 * X ^ 41 - 155 * X ^ 42 - 2976 * X ^ 43 - 241 * X ^ 44 - 3110 * X ^ 45 - 322 * X ^ 46 - 3110 * X ^ 47 - 241 * X ^ 48 - 2976 * X ^ 49 - 155 * X ^ 50 - 2752 * X ^ 51 + 54 * X ^ 52 - 2422 * X ^ 53 + 271 * X ^ 54 - 2020 * X ^ 55 + 554 * X ^ 56 - 1594 * X ^ 57 + 774 * X ^ 58 - 1156 * X ^ 59 + 1033 * X ^ 60 - 720 * X ^ 61 + 1196 * X ^ 62 - 362 * X ^ 63 + 1331 * X ^ 64 - 44 * X ^ 65 + 1373 * X ^ 66 + 196 * X ^ 67 + 1389 * X ^ 68 + 356 * X ^ 69 + 1289 * X ^ 70 + 442 * X ^ 71 + 1192 * X ^ 72 + 480 * X ^ 73 + 1014 * X ^ 74 + 450 * X ^ 75 + 850 * X ^ 76 + 406 * X ^ 77 + 669 * X ^ 78 + 330 * X ^ 79 + 515 * X ^ 80 + 258 * X ^ 81 + 358 * X ^ 82 + 180 * X ^ 83 + 248 * X ^ 84 + 122 * X ^ 85 + 144 * X ^ 86 + 66 * X ^ 87 + 81 * X ^ 88 + 34 * X ^ 89 + 36 * X ^ 90 + 12 * X ^ 91 + 10 * X ^ 92

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_14 = q^55·D(14)` as an integer polynomial (degree 110). -/
noncomputable def P14 : ℤ[X] :=
  5 + 24 * X + 18 * X ^ 2 + 68 * X ^ 3 + 48 * X ^ 4 + 166 * X ^ 5 + 93 * X ^ 6 + 294 * X ^ 7 + 172 * X ^ 8 + 516 * X ^ 9 + 273 * X ^ 10 + 782 * X ^ 11 + 408 * X ^ 12 + 1155 * X ^ 13 + 576 * X ^ 14 + 1550 * X ^ 15 + 772 * X ^ 16 + 2051 * X ^ 17 + 988 * X ^ 18 + 2532 * X ^ 19 + 1208 * X ^ 20 + 3067 * X ^ 21 + 1440 * X ^ 22 + 3470 * X ^ 23 + 1631 * X ^ 24 + 3860 * X ^ 25 + 1785 * X ^ 26 + 4012 * X ^ 27 + 1866 * X ^ 28 + 4030 * X ^ 29 + 1860 * X ^ 30 + 3698 * X ^ 31 + 1754 * X ^ 32 + 3219 * X ^ 33 + 1545 * X ^ 34 + 2336 * X ^ 35 + 1224 * X ^ 36 + 1304 * X ^ 37 + 812 * X ^ 38 - 102 * X ^ 39 + 311 * X ^ 40 - 1502 * X ^ 41 - 234 * X ^ 42 - 3164 * X ^ 43 - 810 * X ^ 44 - 4650 * X ^ 45 - 1363 * X ^ 46 - 6218 * X ^ 47 - 1872 * X ^ 48 - 7387 * X ^ 49 - 2283 * X ^ 50 - 8438 * X ^ 51 - 2572 * X ^ 52 - 8965 * X ^ 53 - 2727 * X ^ 54 - 9272 * X ^ 55 - 2727 * X ^ 56 - 8965 * X ^ 57 - 2572 * X ^ 58 - 8438 * X ^ 59 - 2283 * X ^ 60 - 7387 * X ^ 61 - 1872 * X ^ 62 - 6218 * X ^ 63 - 1363 * X ^ 64 - 4650 * X ^ 65 - 810 * X ^ 66 - 3164 * X ^ 67 - 234 * X ^ 68 - 1502 * X ^ 69 + 311 * X ^ 70 - 102 * X ^ 71 + 812 * X ^ 72 + 1304 * X ^ 73 + 1224 * X ^ 74 + 2336 * X ^ 75 + 1545 * X ^ 76 + 3219 * X ^ 77 + 1754 * X ^ 78 + 3698 * X ^ 79 + 1860 * X ^ 80 + 4030 * X ^ 81 + 1866 * X ^ 82 + 4012 * X ^ 83 + 1785 * X ^ 84 + 3860 * X ^ 85 + 1631 * X ^ 86 + 3470 * X ^ 87 + 1440 * X ^ 88 + 3067 * X ^ 89 + 1208 * X ^ 90 + 2532 * X ^ 91 + 988 * X ^ 92 + 2051 * X ^ 93 + 772 * X ^ 94 + 1550 * X ^ 95 + 576 * X ^ 96 + 1155 * X ^ 97 + 408 * X ^ 98 + 782 * X ^ 99 + 273 * X ^ 100 + 516 * X ^ 101 + 172 * X ^ 102 + 294 * X ^ 103 + 93 * X ^ 104 + 166 * X ^ 105 + 48 * X ^ 106 + 68 * X ^ 107 + 18 * X ^ 108 + 24 * X ^ 109 + 5 * X ^ 110

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_15 = q^65·D(15)` as an integer polynomial (degree 130). -/
noncomputable def P15 : ℤ[X] :=
  1 + 20 * X + 22 * X ^ 2 + 60 * X ^ 3 + 58 * X ^ 4 + 168 * X ^ 5 + 137 * X ^ 6 + 332 * X ^ 7 + 254 * X ^ 8 + 630 * X ^ 9 + 431 * X ^ 10 + 1052 * X ^ 11 + 679 * X ^ 12 + 1680 * X ^ 13 + 989 * X ^ 14 + 2490 * X ^ 15 + 1355 * X ^ 16 + 3590 * X ^ 17 + 1761 * X ^ 18 + 4910 * X ^ 19 + 2185 * X ^ 20 + 6562 * X ^ 21 + 2554 * X ^ 22 + 8430 * X ^ 23 + 2823 * X ^ 24 + 10638 * X ^ 25 + 2893 * X ^ 26 + 12964 * X ^ 27 + 2683 * X ^ 28 + 15542 * X ^ 29 + 2073 * X ^ 30 + 18084 * X ^ 31 + 970 * X ^ 32 + 20738 * X ^ 33 - 747 * X ^ 34 + 23132 * X ^ 35 - 3119 * X ^ 36 + 25470 * X ^ 37 - 6236 * X ^ 38 + 27364 * X ^ 39 - 10126 * X ^ 40 + 29072 * X ^ 41 - 14748 * X ^ 42 + 30150 * X ^ 43 - 20023 * X ^ 44 + 31008 * X ^ 45 - 25901 * X ^ 46 + 31190 * X ^ 47 - 32165 * X ^ 48 + 31236 * X ^ 49 - 38639 * X ^ 50 + 30658 * X ^ 51 - 45094 * X ^ 52 + 30100 * X ^ 53 - 51269 * X ^ 54 + 29112 * X ^ 55 - 56900 * X ^ 56 + 28376 * X ^ 57 - 61771 * X ^ 58 + 27392 * X ^ 59 - 65625 * X ^ 60 + 26878 * X ^ 61 - 68299 * X ^ 62 + 26296 * X ^ 63 - 69686 * X ^ 64 + 26312 * X ^ 65 - 69686 * X ^ 66 + 26296 * X ^ 67 - 68299 * X ^ 68 + 26878 * X ^ 69 - 65625 * X ^ 70 + 27392 * X ^ 71 - 61771 * X ^ 72 + 28376 * X ^ 73 - 56900 * X ^ 74 + 29112 * X ^ 75 - 51269 * X ^ 76 + 30100 * X ^ 77 - 45094 * X ^ 78 + 30658 * X ^ 79 - 38639 * X ^ 80 + 31236 * X ^ 81 - 32165 * X ^ 82 + 31190 * X ^ 83 - 25901 * X ^ 84 + 31008 * X ^ 85 - 20023 * X ^ 86 + 30150 * X ^ 87 - 14748 * X ^ 88 + 29072 * X ^ 89 - 10126 * X ^ 90 + 27364 * X ^ 91 - 6236 * X ^ 92 + 25470 * X ^ 93 - 3119 * X ^ 94 + 23132 * X ^ 95 - 747 * X ^ 96 + 20738 * X ^ 97 + 970 * X ^ 98 + 18084 * X ^ 99 + 2073 * X ^ 100 + 15542 * X ^ 101 + 2683 * X ^ 102 + 12964 * X ^ 103 + 2893 * X ^ 104 + 10638 * X ^ 105 + 2823 * X ^ 106 + 8430 * X ^ 107 + 2554 * X ^ 108 + 6562 * X ^ 109 + 2185 * X ^ 110 + 4910 * X ^ 111 + 1761 * X ^ 112 + 3590 * X ^ 113 + 1355 * X ^ 114 + 2490 * X ^ 115 + 989 * X ^ 116 + 1680 * X ^ 117 + 679 * X ^ 118 + 1052 * X ^ 119 + 431 * X ^ 120 + 630 * X ^ 121 + 254 * X ^ 122 + 332 * X ^ 123 + 137 * X ^ 124 + 168 * X ^ 125 + 58 * X ^ 126 + 60 * X ^ 127 + 22 * X ^ 128 + 20 * X ^ 129 + X ^ 130

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_16 = q^75·D(16)` as an integer polynomial (degree 150). -/
noncomputable def P16 : ℤ[X] :=
  6 + 30 * X + 32 * X ^ 2 + 93 * X ^ 3 + 84 * X ^ 4 + 258 * X ^ 5 + 193 * X ^ 6 + 525 * X ^ 7 + 377 * X ^ 8 + 1028 * X ^ 9 + 674 * X ^ 10 + 1726 * X ^ 11 + 1112 * X ^ 12 + 2852 * X ^ 13 + 1746 * X ^ 14 + 4292 * X ^ 15 + 2594 * X ^ 16 + 6326 * X ^ 17 + 3713 * X ^ 18 + 8782 * X ^ 19 + 5113 * X ^ 20 + 11975 * X ^ 21 + 6825 * X ^ 22 + 15564 * X ^ 23 + 8842 * X ^ 24 + 19922 * X ^ 25 + 11165 * X ^ 26 + 24481 * X ^ 27 + 13720 * X ^ 28 + 29644 * X ^ 29 + 16455 * X ^ 30 + 34575 * X ^ 31 + 19279 * X ^ 32 + 39688 * X ^ 33 + 22059 * X ^ 34 + 43913 * X ^ 35 + 24659 * X ^ 36 + 47748 * X ^ 37 + 26928 * X ^ 38 + 49887 * X ^ 39 + 28694 * X ^ 40 + 50968 * X ^ 41 + 29810 * X ^ 42 + 49567 * X ^ 43 + 30139 * X ^ 44 + 46640 * X ^ 45 + 29549 * X ^ 46 + 40622 * X ^ 47 + 27964 * X ^ 48 + 32853 * X ^ 49 + 25379 * X ^ 50 + 21857 * X ^ 51 + 21784 * X ^ 52 + 9405 * X ^ 53 + 17258 * X ^ 54 - 5901 * X ^ 55 + 11962 * X ^ 56 - 21842 * X ^ 57 + 6058 * X ^ 58 - 39762 * X ^ 59 - 215 * X ^ 60 - 57004 * X ^ 61 - 6572 * X ^ 62 - 74910 * X ^ 63 - 12753 * X ^ 64 - 90698 * X ^ 65 - 18462 * X ^ 66 - 105759 * X ^ 67 - 23397 * X ^ 68 - 117237 * X ^ 69 - 27354 * X ^ 70 - 126846 * X ^ 71 - 30109 * X ^ 72 - 131884 * X ^ 73 - 31511 * X ^ 74 - 134356 * X ^ 75 - 31511 * X ^ 76 - 131884 * X ^ 77 - 30109 * X ^ 78 - 126846 * X ^ 79 - 27354 * X ^ 80 - 117237 * X ^ 81 - 23397 * X ^ 82 - 105759 * X ^ 83 - 18462 * X ^ 84 - 90698 * X ^ 85 - 12753 * X ^ 86 - 74910 * X ^ 87 - 6572 * X ^ 88 - 57004 * X ^ 89 - 215 * X ^ 90 - 39762 * X ^ 91 + 6058 * X ^ 92 - 21842 * X ^ 93 + 11962 * X ^ 94 - 5901 * X ^ 95 + 17258 * X ^ 96 + 9405 * X ^ 97 + 21784 * X ^ 98 + 21857 * X ^ 99 + 25379 * X ^ 100 + 32853 * X ^ 101 + 27964 * X ^ 102 + 40622 * X ^ 103 + 29549 * X ^ 104 + 46640 * X ^ 105 + 30139 * X ^ 106 + 49567 * X ^ 107 + 29810 * X ^ 108 + 50968 * X ^ 109 + 28694 * X ^ 110 + 49887 * X ^ 111 + 26928 * X ^ 112 + 47748 * X ^ 113 + 24659 * X ^ 114 + 43913 * X ^ 115 + 22059 * X ^ 116 + 39688 * X ^ 117 + 19279 * X ^ 118 + 34575 * X ^ 119 + 16455 * X ^ 120 + 29644 * X ^ 121 + 13720 * X ^ 122 + 24481 * X ^ 123 + 11165 * X ^ 124 + 19922 * X ^ 125 + 8842 * X ^ 126 + 15564 * X ^ 127 + 6825 * X ^ 128 + 11975 * X ^ 129 + 5113 * X ^ 130 + 8782 * X ^ 131 + 3713 * X ^ 132 + 6326 * X ^ 133 + 2594 * X ^ 134 + 4292 * X ^ 135 + 1746 * X ^ 136 + 2852 * X ^ 137 + 1112 * X ^ 138 + 1726 * X ^ 139 + 674 * X ^ 140 + 1028 * X ^ 141 + 377 * X ^ 142 + 525 * X ^ 143 + 193 * X ^ 144 + 258 * X ^ 145 + 84 * X ^ 146 + 93 * X ^ 147 + 32 * X ^ 148 + 30 * X ^ 149 + 6 * X ^ 150

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_17 = q^86·D(17)` as an integer polynomial (degree 172). -/
noncomputable def P17 : ℤ[X] :=
  15 + 22 * X + 81 * X ^ 2 + 68 * X ^ 3 + 213 * X ^ 4 + 188 * X ^ 5 + 518 * X ^ 6 + 398 * X ^ 7 + 1054 * X ^ 8 + 774 * X ^ 9 + 1996 * X ^ 10 + 1324 * X ^ 11 + 3442 * X ^ 12 + 2182 * X ^ 13 + 5704 * X ^ 14 + 3334 * X ^ 15 + 8905 * X ^ 16 + 4878 * X ^ 17 + 13478 * X ^ 18 + 6790 * X ^ 19 + 19576 * X ^ 20 + 9122 * X ^ 21 + 27731 * X ^ 22 + 11730 * X ^ 23 + 38077 * X ^ 24 + 14582 * X ^ 25 + 51270 * X ^ 26 + 17362 * X ^ 27 + 67259 * X ^ 28 + 19850 * X ^ 29 + 86739 * X ^ 30 + 21538 * X ^ 31 + 109536 * X ^ 32 + 21962 * X ^ 33 + 136220 * X ^ 34 + 20326 * X ^ 35 + 166286 * X ^ 36 + 16010 * X ^ 37 + 200300 * X ^ 38 + 7966 * X ^ 39 + 237287 * X ^ 40 - 4620 * X ^ 41 + 277743 * X ^ 42 - 22840 * X ^ 43 + 320317 * X ^ 44 - 47574 * X ^ 45 + 365358 * X ^ 46 - 79890 * X ^ 47 + 411165 * X ^ 48 - 120378 * X ^ 49 + 458154 * X ^ 50 - 169868 * X ^ 51 + 504231 * X ^ 52 - 228584 * X ^ 53 + 550006 * X ^ 54 - 296732 * X ^ 55 + 593273 * X ^ 56 - 373948 * X ^ 57 + 634855 * X ^ 58 - 459784 * X ^ 59 + 672533 * X ^ 60 - 553008 * X ^ 61 + 707627 * X ^ 62 - 652428 * X ^ 63 + 737882 * X ^ 64 - 756128 * X ^ 65 + 765165 * X ^ 66 - 862100 * X ^ 67 + 787394 * X ^ 68 - 967906 * X ^ 69 + 806806 * X ^ 70 - 1071120 * X ^ 71 + 821462 * X ^ 72 - 1168912 * X ^ 73 + 834039 * X ^ 74 - 1258804 * X ^ 75 + 842504 * X ^ 76 - 1338182 * X ^ 77 + 849778 * X ^ 78 - 1404750 * X ^ 79 + 853834 * X ^ 80 - 1456542 * X ^ 81 + 857487 * X ^ 82 - 1492020 * X ^ 83 + 858539 * X ^ 84 - 1510000 * X ^ 85 + 859746 * X ^ 86 - 1510000 * X ^ 87 + 858539 * X ^ 88 - 1492020 * X ^ 89 + 857487 * X ^ 90 - 1456542 * X ^ 91 + 853834 * X ^ 92 - 1404750 * X ^ 93 + 849778 * X ^ 94 - 1338182 * X ^ 95 + 842504 * X ^ 96 - 1258804 * X ^ 97 + 834039 * X ^ 98 - 1168912 * X ^ 99 + 821462 * X ^ 100 - 1071120 * X ^ 101 + 806806 * X ^ 102 - 967906 * X ^ 103 + 787394 * X ^ 104 - 862100 * X ^ 105 + 765165 * X ^ 106 - 756128 * X ^ 107 + 737882 * X ^ 108 - 652428 * X ^ 109 + 707627 * X ^ 110 - 553008 * X ^ 111 + 672533 * X ^ 112 - 459784 * X ^ 113 + 634855 * X ^ 114 - 373948 * X ^ 115 + 593273 * X ^ 116 - 296732 * X ^ 117 + 550006 * X ^ 118 - 228584 * X ^ 119 + 504231 * X ^ 120 - 169868 * X ^ 121 + 458154 * X ^ 122 - 120378 * X ^ 123 + 411165 * X ^ 124 - 79890 * X ^ 125 + 365358 * X ^ 126 - 47574 * X ^ 127 + 320317 * X ^ 128 - 22840 * X ^ 129 + 277743 * X ^ 130 - 4620 * X ^ 131 + 237287 * X ^ 132 + 7966 * X ^ 133 + 200300 * X ^ 134 + 16010 * X ^ 135 + 166286 * X ^ 136 + 20326 * X ^ 137 + 136220 * X ^ 138 + 21962 * X ^ 139 + 109536 * X ^ 140 + 21538 * X ^ 141 + 86739 * X ^ 142 + 19850 * X ^ 143 + 67259 * X ^ 144 + 17362 * X ^ 145 + 51270 * X ^ 146 + 14582 * X ^ 147 + 38077 * X ^ 148 + 11730 * X ^ 149 + 27731 * X ^ 150 + 9122 * X ^ 151 + 19576 * X ^ 152 + 6790 * X ^ 153 + 13478 * X ^ 154 + 4878 * X ^ 155 + 8905 * X ^ 156 + 3334 * X ^ 157 + 5704 * X ^ 158 + 2182 * X ^ 159 + 3442 * X ^ 160 + 1324 * X ^ 161 + 1996 * X ^ 162 + 774 * X ^ 163 + 1054 * X ^ 164 + 398 * X ^ 165 + 518 * X ^ 166 + 188 * X ^ 167 + 213 * X ^ 168 + 68 * X ^ 169 + 81 * X ^ 170 + 22 * X ^ 171 + 15 * X ^ 172

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_18 = q^98·D(18)` as an integer polynomial (degree 196). -/
noncomputable def P18 : ℤ[X] :=
  20 + 20 * X + 108 * X ^ 2 + 72 * X ^ 3 + 296 * X ^ 4 + 192 * X ^ 5 + 724 * X ^ 6 + 453 * X ^ 7 + 1524 * X ^ 8 + 909 * X ^ 9 + 2919 * X ^ 10 + 1691 * X ^ 11 + 5168 * X ^ 12 + 2924 * X ^ 13 + 8705 * X ^ 14 + 4801 * X ^ 15 + 13869 * X ^ 16 + 7495 * X ^ 17 + 21321 * X ^ 18 + 11307 * X ^ 19 + 31531 * X ^ 20 + 16429 * X ^ 21 + 45253 * X ^ 22 + 23189 * X ^ 23 + 63118 * X ^ 24 + 31836 * X ^ 25 + 85977 * X ^ 26 + 42667 * X ^ 27 + 114230 * X ^ 28 + 55839 * X ^ 29 + 148776 * X ^ 30 + 71607 * X ^ 31 + 189780 * X ^ 32 + 89926 * X ^ 33 + 237726 * X ^ 34 + 110811 * X ^ 35 + 292277 * X ^ 36 + 134038 * X ^ 37 + 353484 * X ^ 38 + 159225 * X ^ 39 + 420115 * X ^ 40 + 185744 * X ^ 41 + 491630 * X ^ 42 + 212953 * X ^ 43 + 565864 * X ^ 44 + 239752 * X ^ 45 + 641366 * X ^ 46 + 265068 * X ^ 47 + 715224 * X ^ 48 + 287542 * X ^ 49 + 785417 * X ^ 50 + 305736 * X ^ 51 + 847958 * X ^ 52 + 318026 * X ^ 53 + 900750 * X ^ 54 + 323021 * X ^ 55 + 939587 * X ^ 56 + 319034 * X ^ 57 + 962235 * X ^ 58 + 304732 * X ^ 59 + 964835 * X ^ 60 + 278923 * X ^ 61 + 946154 * X ^ 62 + 240674 * X ^ 63 + 902873 * X ^ 64 + 189349 * X ^ 65 + 835409 * X ^ 66 + 124970 * X ^ 67 + 741896 * X ^ 68 + 47654 * X ^ 69 + 624321 * X ^ 70 - 41708 * X ^ 71 + 482924 * X ^ 72 - 141748 * X ^ 73 + 321918 * X ^ 74 - 250716 * X ^ 75 + 142870 * X ^ 76 - 366393 * X ^ 77 - 47766 * X ^ 78 - 485945 * X ^ 79 - 246710 * X ^ 80 - 606560 * X ^ 81 - 446602 * X ^ 82 - 724992 * X ^ 83 - 643152 * X ^ 84 - 837851 * X ^ 85 - 828152 * X ^ 86 - 941965 * X ^ 87 - 997887 * X ^ 88 - 1034270 * X ^ 89 - 1144393 * X ^ 90 - 1111776 * X ^ 91 - 1264908 * X ^ 92 - 1172204 * X ^ 93 - 1353303 * X ^ 94 - 1213637 * X ^ 95 - 1408422 * X ^ 96 - 1234620 * X ^ 97 - 1426162 * X ^ 98 - 1234620 * X ^ 99 - 1408422 * X ^ 100 - 1213637 * X ^ 101 - 1353303 * X ^ 102 - 1172204 * X ^ 103 - 1264908 * X ^ 104 - 1111776 * X ^ 105 - 1144393 * X ^ 106 - 1034270 * X ^ 107 - 997887 * X ^ 108 - 941965 * X ^ 109 - 828152 * X ^ 110 - 837851 * X ^ 111 - 643152 * X ^ 112 - 724992 * X ^ 113 - 446602 * X ^ 114 - 606560 * X ^ 115 - 246710 * X ^ 116 - 485945 * X ^ 117 - 47766 * X ^ 118 - 366393 * X ^ 119 + 142870 * X ^ 120 - 250716 * X ^ 121 + 321918 * X ^ 122 - 141748 * X ^ 123 + 482924 * X ^ 124 - 41708 * X ^ 125 + 624321 * X ^ 126 + 47654 * X ^ 127 + 741896 * X ^ 128 + 124970 * X ^ 129 + 835409 * X ^ 130 + 189349 * X ^ 131 + 902873 * X ^ 132 + 240674 * X ^ 133 + 946154 * X ^ 134 + 278923 * X ^ 135 + 964835 * X ^ 136 + 304732 * X ^ 137 + 962235 * X ^ 138 + 319034 * X ^ 139 + 939587 * X ^ 140 + 323021 * X ^ 141 + 900750 * X ^ 142 + 318026 * X ^ 143 + 847958 * X ^ 144 + 305736 * X ^ 145 + 785417 * X ^ 146 + 287542 * X ^ 147 + 715224 * X ^ 148 + 265068 * X ^ 149 + 641366 * X ^ 150 + 239752 * X ^ 151 + 565864 * X ^ 152 + 212953 * X ^ 153 + 491630 * X ^ 154 + 185744 * X ^ 155 + 420115 * X ^ 156 + 159225 * X ^ 157 + 353484 * X ^ 158 + 134038 * X ^ 159 + 292277 * X ^ 160 + 110811 * X ^ 161 + 237726 * X ^ 162 + 89926 * X ^ 163 + 189780 * X ^ 164 + 71607 * X ^ 165 + 148776 * X ^ 166 + 55839 * X ^ 167 + 114230 * X ^ 168 + 42667 * X ^ 169 + 85977 * X ^ 170 + 31836 * X ^ 171 + 63118 * X ^ 172 + 23189 * X ^ 173 + 45253 * X ^ 174 + 16429 * X ^ 175 + 31531 * X ^ 176 + 11307 * X ^ 177 + 21321 * X ^ 178 + 7495 * X ^ 179 + 13869 * X ^ 180 + 4801 * X ^ 181 + 8705 * X ^ 182 + 2924 * X ^ 183 + 5168 * X ^ 184 + 1691 * X ^ 185 + 2919 * X ^ 186 + 909 * X ^ 187 + 1524 * X ^ 188 + 453 * X ^ 189 + 724 * X ^ 190 + 192 * X ^ 191 + 296 * X ^ 192 + 72 * X ^ 193 + 108 * X ^ 194 + 20 * X ^ 195 + 20 * X ^ 196

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_19 = q^111·D(19)` as an integer polynomial (degree 222). -/
noncomputable def P19 : ℤ[X] :=
  15 + 40 * X + 73 * X ^ 2 + 154 * X ^ 3 + 219 * X ^ 4 + 438 * X ^ 5 + 528 * X ^ 6 + 1040 * X ^ 7 + 1153 * X ^ 8 + 2216 * X ^ 9 + 2229 * X ^ 10 + 4290 * X ^ 11 + 4054 * X ^ 12 + 7786 * X ^ 13 + 6874 * X ^ 14 + 13336 * X ^ 15 + 11152 * X ^ 16 + 21884 * X ^ 17 + 17263 * X ^ 18 + 34534 * X ^ 19 + 25818 * X ^ 20 + 52710 * X ^ 21 + 37248 * X ^ 22 + 78094 * X ^ 23 + 52258 * X ^ 24 + 112830 * X ^ 25 + 71186 * X ^ 26 + 159180 * X ^ 27 + 94604 * X ^ 28 + 219966 * X ^ 29 + 122555 * X ^ 30 + 298096 * X ^ 31 + 155158 * X ^ 32 + 396984 * X ^ 33 + 191703 * X ^ 34 + 519970 * X ^ 35 + 231518 * X ^ 36 + 670840 * X ^ 37 + 272674 * X ^ 38 + 852972 * X ^ 39 + 313112 * X ^ 40 + 1070250 * X ^ 41 + 349289 * X ^ 42 + 1325652 * X ^ 43 + 377324 * X ^ 44 + 1622442 * X ^ 45 + 391578 * X ^ 46 + 1962730 * X ^ 47 + 386188 * X ^ 48 + 2348798 * X ^ 49 + 353228 * X ^ 50 + 2781106 * X ^ 51 + 284783 * X ^ 52 + 3260444 * X ^ 53 + 171052 * X ^ 54 + 3785302 * X ^ 55 + 2431 * X ^ 56 + 4354552 * X ^ 57 - 232175 * X ^ 58 + 4964518 * X ^ 59 - 542892 * X ^ 60 + 5612002 * X ^ 61 - 940982 * X ^ 62 + 6291080 * X ^ 63 - 1435827 * X ^ 64 + 6996974 * X ^ 65 - 2037025 * X ^ 66 + 7721864 * X ^ 67 - 2751581 * X ^ 68 + 8459618 * X ^ 69 - 3585668 * X ^ 70 + 9201420 * X ^ 71 - 4541783 * X ^ 72 + 9940758 * X ^ 73 - 5621132 * X ^ 74 + 10668310 * X ^ 75 - 6820173 * X ^ 76 + 11378216 * X ^ 77 - 8133365 * X ^ 78 + 12061726 * X ^ 79 - 9550390 * X ^ 80 + 12714240 * X ^ 81 - 11058366 * X ^ 82 + 13328620 * X ^ 83 - 12639601 * X ^ 84 + 13902098 * X ^ 85 - 14274480 * X ^ 86 + 14429312 * X ^ 87 - 15938920 * X ^ 88 + 14910168 * X ^ 89 - 17607504 * X ^ 90 + 15341152 * X ^ 91 - 19251980 * X ^ 92 + 15724186 * X ^ 93 - 20843590 * X ^ 94 + 16057848 * X ^ 95 - 22352289 * X ^ 96 + 16345720 * X ^ 97 - 23749467 * X ^ 98 + 16587314 * X ^ 99 - 25006647 * X ^ 100 + 16787426 * X ^ 101 - 26098267 * X ^ 102 + 16945848 * X ^ 103 - 27001266 * X ^ 104 + 17067396 * X ^ 105 - 27696370 * X ^ 106 + 17151640 * X ^ 107 - 28168314 * X ^ 108 + 17202506 * X ^ 109 - 28407021 * X ^ 110 + 17218424 * X ^ 111 - 28407021 * X ^ 112 + 17202506 * X ^ 113 - 28168314 * X ^ 114 + 17151640 * X ^ 115 - 27696370 * X ^ 116 + 17067396 * X ^ 117 - 27001266 * X ^ 118 + 16945848 * X ^ 119 - 26098267 * X ^ 120 + 16787426 * X ^ 121 - 25006647 * X ^ 122 + 16587314 * X ^ 123 - 23749467 * X ^ 124 + 16345720 * X ^ 125 - 22352289 * X ^ 126 + 16057848 * X ^ 127 - 20843590 * X ^ 128 + 15724186 * X ^ 129 - 19251980 * X ^ 130 + 15341152 * X ^ 131 - 17607504 * X ^ 132 + 14910168 * X ^ 133 - 15938920 * X ^ 134 + 14429312 * X ^ 135 - 14274480 * X ^ 136 + 13902098 * X ^ 137 - 12639601 * X ^ 138 + 13328620 * X ^ 139 - 11058366 * X ^ 140 + 12714240 * X ^ 141 - 9550390 * X ^ 142 + 12061726 * X ^ 143 - 8133365 * X ^ 144 + 11378216 * X ^ 145 - 6820173 * X ^ 146 + 10668310 * X ^ 147 - 5621132 * X ^ 148 + 9940758 * X ^ 149 - 4541783 * X ^ 150 + 9201420 * X ^ 151 - 3585668 * X ^ 152 + 8459618 * X ^ 153 - 2751581 * X ^ 154 + 7721864 * X ^ 155 - 2037025 * X ^ 156 + 6996974 * X ^ 157 - 1435827 * X ^ 158 + 6291080 * X ^ 159 - 940982 * X ^ 160 + 5612002 * X ^ 161 - 542892 * X ^ 162 + 4964518 * X ^ 163 - 232175 * X ^ 164 + 4354552 * X ^ 165 + 2431 * X ^ 166 + 3785302 * X ^ 167 + 171052 * X ^ 168 + 3260444 * X ^ 169 + 284783 * X ^ 170 + 2781106 * X ^ 171 + 353228 * X ^ 172 + 2348798 * X ^ 173 + 386188 * X ^ 174 + 1962730 * X ^ 175 + 391578 * X ^ 176 + 1622442 * X ^ 177 + 377324 * X ^ 178 + 1325652 * X ^ 179 + 349289 * X ^ 180 + 1070250 * X ^ 181 + 313112 * X ^ 182 + 852972 * X ^ 183 + 272674 * X ^ 184 + 670840 * X ^ 185 + 231518 * X ^ 186 + 519970 * X ^ 187 + 191703 * X ^ 188 + 396984 * X ^ 189 + 155158 * X ^ 190 + 298096 * X ^ 191 + 122555 * X ^ 192 + 219966 * X ^ 193 + 94604 * X ^ 194 + 159180 * X ^ 195 + 71186 * X ^ 196 + 112830 * X ^ 197 + 52258 * X ^ 198 + 78094 * X ^ 199 + 37248 * X ^ 200 + 52710 * X ^ 201 + 25818 * X ^ 202 + 34534 * X ^ 203 + 17263 * X ^ 204 + 21884 * X ^ 205 + 11152 * X ^ 206 + 13336 * X ^ 207 + 6874 * X ^ 208 + 7786 * X ^ 209 + 4054 * X ^ 210 + 4290 * X ^ 211 + 2229 * X ^ 212 + 2216 * X ^ 213 + 1153 * X ^ 214 + 1040 * X ^ 215 + 528 * X ^ 216 + 438 * X ^ 217 + 219 * X ^ 218 + 154 * X ^ 219 + 73 * X ^ 220 + 40 * X ^ 221 + 15 * X ^ 222

set_option maxHeartbeats 4000000 in
/-- The cleared tail `P_20 = q^125·D(20)` as an integer polynomial (degree 250). -/
noncomputable def P20 : ℤ[X] :=
  6 + 50 * X + 48 * X ^ 2 + 190 * X ^ 3 + 158 * X ^ 4 + 588 * X ^ 5 + 422 * X ^ 6 + 1384 * X ^ 7 + 980 * X ^ 8 + 3052 * X ^ 9 + 2034 * X ^ 10 + 6001 * X ^ 11 + 3914 * X ^ 12 + 11181 * X ^ 13 + 7059 * X ^ 14 + 19451 * X ^ 15 + 12082 * X ^ 16 + 32586 * X ^ 17 + 19793 * X ^ 18 + 52188 * X ^ 19 + 31261 * X ^ 20 + 81149 * X ^ 21 + 47769 * X ^ 22 + 121937 * X ^ 23 + 70945 * X ^ 24 + 178954 * X ^ 25 + 102670 * X ^ 26 + 255768 * X ^ 27 + 145204 * X ^ 28 + 358344 * X ^ 29 + 201004 * X ^ 30 + 491272 * X ^ 31 + 272975 * X ^ 32 + 662109 * X ^ 33 + 363989 * X ^ 34 + 876127 * X ^ 35 + 477327 * X ^ 36 + 1141939 * X ^ 37 + 616059 * X ^ 38 + 1464650 * X ^ 39 + 783360 * X ^ 40 + 1853247 * X ^ 41 + 981930 * X ^ 42 + 2311456 * X ^ 43 + 1214290 * X ^ 44 + 2847221 * X ^ 45 + 1481912 * X ^ 46 + 3461109 * X ^ 47 + 1785849 * X ^ 48 + 4158644 * X ^ 49 + 2125668 * X ^ 50 + 4935509 * X ^ 51 + 2499948 * X ^ 52 + 5792845 * X ^ 53 + 2905375 * X ^ 54 + 6719586 * X ^ 55 + 3337439 * X ^ 56 + 7711218 * X ^ 57 + 3789229 * X ^ 58 + 8748555 * X ^ 59 + 4252550 * X ^ 60 + 9820585 * X ^ 61 + 4716759 * X ^ 62 + 10899157 * X ^ 63 + 5169779 * X ^ 64 + 11966983 * X ^ 65 + 5597403 * X ^ 66 + 12987883 * X ^ 67 + 5984536 * X ^ 68 + 13939490 * X ^ 69 + 6314132 * X ^ 70 + 14779128 * X ^ 71 + 6569297 * X ^ 72 + 15482553 * X ^ 73 + 6732061 * X ^ 74 + 16004188 * X ^ 75 + 6785341 * X ^ 76 + 16321346 * X ^ 77 + 6712428 * X ^ 78 + 16390016 * X ^ 79 + 6498805 * X ^ 80 + 16194363 * X ^ 81 + 6131297 * X ^ 82 + 15696631 * X ^ 83 + 5600424 * X ^ 84 + 14892850 * X ^ 85 + 4899319 * X ^ 86 + 13756207 * X ^ 87 + 4025658 * X ^ 88 + 12298982 * X ^ 89 + 2980933 * X ^ 90 + 10509735 * X ^ 91 + 1772033 * X ^ 92 + 8419538 * X ^ 93 + 409661 * X ^ 94 + 6033755 * X ^ 95 - 1089605 * X ^ 96 + 3403752 * X ^ 97 - 2705252 * X ^ 98 + 551714 * X ^ 99 - 4411943 * X ^ 100 - 2453062 * X ^ 101 - 6180770 * X ^ 102 - 5574461 * X ^ 103 - 7979191 * X ^ 104 - 8729301 * X ^ 105 - 9772881 * X ^ 106 - 11872989 * X ^ 107 - 11525222 * X ^ 108 - 14914828 * X ^ 109 - 13199664 * X ^ 110 - 17809030 * X ^ 111 - 14759848 * X ^ 112 - 20465664 * X ^ 113 - 16171172 * X ^ 114 - 22844803 * X ^ 115 - 17401420 * X ^ 116 - 24865915 * X ^ 117 - 18422485 * X ^ 118 - 26503418 * X ^ 119 - 19210198 * X ^ 120 - 27692568 * X ^ 121 - 19745955 * X ^ 122 - 28427984 * X ^ 123 - 20017141 * X ^ 124 - 28667022 * X ^ 125 - 20017141 * X ^ 126 - 28427984 * X ^ 127 - 19745955 * X ^ 128 - 27692568 * X ^ 129 - 19210198 * X ^ 130 - 26503418 * X ^ 131 - 18422485 * X ^ 132 - 24865915 * X ^ 133 - 17401420 * X ^ 134 - 22844803 * X ^ 135 - 16171172 * X ^ 136 - 20465664 * X ^ 137 - 14759848 * X ^ 138 - 17809030 * X ^ 139 - 13199664 * X ^ 140 - 14914828 * X ^ 141 - 11525222 * X ^ 142 - 11872989 * X ^ 143 - 9772881 * X ^ 144 - 8729301 * X ^ 145 - 7979191 * X ^ 146 - 5574461 * X ^ 147 - 6180770 * X ^ 148 - 2453062 * X ^ 149 - 4411943 * X ^ 150 + 551714 * X ^ 151 - 2705252 * X ^ 152 + 3403752 * X ^ 153 - 1089605 * X ^ 154 + 6033755 * X ^ 155 + 409661 * X ^ 156 + 8419538 * X ^ 157 + 1772033 * X ^ 158 + 10509735 * X ^ 159 + 2980933 * X ^ 160 + 12298982 * X ^ 161 + 4025658 * X ^ 162 + 13756207 * X ^ 163 + 4899319 * X ^ 164 + 14892850 * X ^ 165 + 5600424 * X ^ 166 + 15696631 * X ^ 167 + 6131297 * X ^ 168 + 16194363 * X ^ 169 + 6498805 * X ^ 170 + 16390016 * X ^ 171 + 6712428 * X ^ 172 + 16321346 * X ^ 173 + 6785341 * X ^ 174 + 16004188 * X ^ 175 + 6732061 * X ^ 176 + 15482553 * X ^ 177 + 6569297 * X ^ 178 + 14779128 * X ^ 179 + 6314132 * X ^ 180 + 13939490 * X ^ 181 + 5984536 * X ^ 182 + 12987883 * X ^ 183 + 5597403 * X ^ 184 + 11966983 * X ^ 185 + 5169779 * X ^ 186 + 10899157 * X ^ 187 + 4716759 * X ^ 188 + 9820585 * X ^ 189 + 4252550 * X ^ 190 + 8748555 * X ^ 191 + 3789229 * X ^ 192 + 7711218 * X ^ 193 + 3337439 * X ^ 194 + 6719586 * X ^ 195 + 2905375 * X ^ 196 + 5792845 * X ^ 197 + 2499948 * X ^ 198 + 4935509 * X ^ 199 + 2125668 * X ^ 200 + 4158644 * X ^ 201 + 1785849 * X ^ 202 + 3461109 * X ^ 203 + 1481912 * X ^ 204 + 2847221 * X ^ 205 + 1214290 * X ^ 206 + 2311456 * X ^ 207 + 981930 * X ^ 208 + 1853247 * X ^ 209 + 783360 * X ^ 210 + 1464650 * X ^ 211 + 616059 * X ^ 212 + 1141939 * X ^ 213 + 477327 * X ^ 214 + 876127 * X ^ 215 + 363989 * X ^ 216 + 662109 * X ^ 217 + 272975 * X ^ 218 + 491272 * X ^ 219 + 201004 * X ^ 220 + 358344 * X ^ 221 + 145204 * X ^ 222 + 255768 * X ^ 223 + 102670 * X ^ 224 + 178954 * X ^ 225 + 70945 * X ^ 226 + 121937 * X ^ 227 + 47769 * X ^ 228 + 81149 * X ^ 229 + 31261 * X ^ 230 + 52188 * X ^ 231 + 19793 * X ^ 232 + 32586 * X ^ 233 + 12082 * X ^ 234 + 19451 * X ^ 235 + 7059 * X ^ 236 + 11181 * X ^ 237 + 3914 * X ^ 238 + 6001 * X ^ 239 + 2034 * X ^ 240 + 3052 * X ^ 241 + 980 * X ^ 242 + 1384 * X ^ 243 + 422 * X ^ 244 + 588 * X ^ 245 + 158 * X ^ 246 + 190 * X ^ 247 + 48 * X ^ 248 + 50 * X ^ 249 + 6 * X ^ 250

set_option maxHeartbeats 8000000 in
/-- `P_6` is **not** a product of cyclotomic polynomials: witness `p = 47`, `a = 28`
    (order `23` mod `47`, `φ(23) = 22 > 14 = deg P_6`), `b = 2`. -/
theorem P6_not_cyclo : ¬ IsCycloProduct P6 := by
  haveI : Fact (Nat.Prime 47) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P6 14 (p := 47) 28 2 23 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P6]; compute_degree
  · simp only [P6, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P6, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [23]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_7` is **not** a product of cyclotomic polynomials: witness `p = 47`, `a = 10`
    (order `46` mod `47`, `φ(46) = 22 > 20 = deg P_7`), `b = 2`. -/
theorem P7_not_cyclo : ¬ IsCycloProduct P7 := by
  haveI : Fact (Nat.Prime 47) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P7 20 (p := 47) 10 2 46 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P7]; compute_degree
  · simp only [P7, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P7, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 23]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_8` is **not** a product of cyclotomic polynomials: witness `p = 83`, `a = 43`
    (order `82` mod `83`, `φ(82) = 40 > 28 = deg P_8`), `b = 2`. -/
theorem P8_not_cyclo : ¬ IsCycloProduct P8 := by
  haveI : Fact (Nat.Prime 83) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P8 28 (p := 83) 43 2 82 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P8]; compute_degree
  · simp only [P8, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P8, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 41]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_9` is **not** a product of cyclotomic polynomials: witness `p = 83`, `a = 17`
    (order `41` mod `83`, `φ(41) = 40 > 38 = deg P_9`), `b = 2`. -/
theorem P9_not_cyclo : ¬ IsCycloProduct P9 := by
  haveI : Fact (Nat.Prime 83) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P9 38 (p := 83) 17 2 41 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P9]; compute_degree
  · simp only [P9, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P9, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [41]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_10` is **not** a product of cyclotomic polynomials: witness `p = 149`, `a = 79`
    (order `148` mod `149`, `φ(148) = 72 > 50 = deg P_10`), `b = 2`. -/
theorem P10_not_cyclo : ¬ IsCycloProduct P10 := by
  haveI : Fact (Nat.Prime 149) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P10 50 (p := 149) 79 2 148 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P10]; compute_degree
  · simp only [P10, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P10, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 2, 37]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_11` is **not** a product of cyclotomic polynomials: witness `p = 137`, `a = 24`
    (order `136` mod `137`, `φ(136) = 64 > 62 = deg P_11`), `b = 2`. -/
theorem P11_not_cyclo : ¬ IsCycloProduct P11 := by
  haveI : Fact (Nat.Prime 137) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P11 62 (p := 137) 24 2 136 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P11]; compute_degree
  · simp only [P11, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P11, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 2, 2, 17]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl | rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl | rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_12` is **not** a product of cyclotomic polynomials: witness `p = 227`, `a = 11`
    (order `113` mod `227`, `φ(113) = 112 > 76 = deg P_12`), `b = 2`. -/
theorem P12_not_cyclo : ¬ IsCycloProduct P12 := by
  haveI : Fact (Nat.Prime 227) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P12 76 (p := 227) 11 2 113 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P12]; compute_degree
  · simp only [P12, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P12, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [113]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_13` is **not** a product of cyclotomic polynomials: witness `p = 227`, `a = 61`
    (order `226` mod `227`, `φ(226) = 112 > 92 = deg P_13`), `b = 2`. -/
theorem P13_not_cyclo : ¬ IsCycloProduct P13 := by
  haveI : Fact (Nat.Prime 227) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P13 92 (p := 227) 61 2 226 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P13]; compute_degree
  · simp only [P13, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P13, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 113]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_14` is **not** a product of cyclotomic polynomials: witness `p = 227`, `a = 17`
    (order `226` mod `227`, `φ(226) = 112 > 110 = deg P_14`), `b = 2`. -/
theorem P14_not_cyclo : ¬ IsCycloProduct P14 := by
  haveI : Fact (Nat.Prime 227) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P14 110 (p := 227) 17 2 226 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P14]; compute_degree
  · simp only [P14, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P14, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 113]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_15` is **not** a product of cyclotomic polynomials: witness `p = 293`, `a = 66`
    (order `292` mod `293`, `φ(292) = 144 > 130 = deg P_15`), `b = 2`. -/
theorem P15_not_cyclo : ¬ IsCycloProduct P15 := by
  haveI : Fact (Nat.Prime 293) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P15 130 (p := 293) 66 2 292 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P15]; compute_degree
  · simp only [P15, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P15, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 2, 73]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_16` is **not** a product of cyclotomic polynomials: witness `p = 317`, `a = 75`
    (order `316` mod `317`, `φ(316) = 156 > 150 = deg P_16`), `b = 2`. -/
theorem P16_not_cyclo : ¬ IsCycloProduct P16 := by
  haveI : Fact (Nat.Prime 317) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P16 150 (p := 317) 75 2 316 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P16]; compute_degree
  · simp only [P16, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P16, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 2, 79]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_17` is **not** a product of cyclotomic polynomials: witness `p = 359`, `a = 16`
    (order `179` mod `359`, `φ(179) = 178 > 172 = deg P_17`), `b = 2`. -/
theorem P17_not_cyclo : ¬ IsCycloProduct P17 := by
  haveI : Fact (Nat.Prime 359) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P17 172 (p := 359) 16 2 179 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P17]; compute_degree
  · simp only [P17, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P17, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [179]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_18` is **not** a product of cyclotomic polynomials: witness `p = 557`, `a = 242`
    (order `556` mod `557`, `φ(556) = 276 > 196 = deg P_18`), `b = 2`. -/
theorem P18_not_cyclo : ¬ IsCycloProduct P18 := by
  haveI : Fact (Nat.Prime 557) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P18 196 (p := 557) 242 2 556 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P18]; compute_degree
  · simp only [P18, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P18, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 2, 139]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_19` is **not** a product of cyclotomic polynomials: witness `p = 479`, `a = 33`
    (order `239` mod `479`, `φ(239) = 238 > 222 = deg P_19`), `b = 2`. -/
theorem P19_not_cyclo : ¬ IsCycloProduct P19 := by
  haveI : Fact (Nat.Prime 479) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P19 222 (p := 479) 33 2 239 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P19]; compute_degree
  · simp only [P19, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P19, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [239]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

set_option maxHeartbeats 8000000 in
/-- `P_20` is **not** a product of cyclotomic polynomials: witness `p = 557`, `a = 200`
    (order `556` mod `557`, `φ(556) = 276 > 250 = deg P_20`), `b = 2`. -/
theorem P20_not_cyclo : ¬ IsCycloProduct P20 := by
  haveI : Fact (Nat.Prime 557) := ⟨by norm_num⟩
  refine not_isCycloProduct_of_witness P20 250 (p := 557) 200 2 556 (by norm_num) ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · simp only [P20]; compute_degree
  · simp only [P20, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · simp only [P20, eval_add, eval_sub, eval_mul, eval_pow, eval_X, eval_ofNat, eval_one, eval_neg]; norm_num
  · norm_num
  · rw [intCast_pow_eq_one_iff]; norm_num
  · intro r hr hdvd
    have hmem := mem_of_prime_dvd_prod [2, 2, 139]
      (by intro r hr; simp only [List.mem_cons, List.not_mem_nil, or_false] at hr
          rcases hr with rfl | rfl | rfl <;> norm_num) hr hdvd (by norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
    rcases hmem with rfl | rfl | rfl <;> rw [intCast_pow_eq_one_iff] <;> norm_num
  · decide

/-! ## Part 4 — the forward direction and the boundary -/

theorem P4_cyclo : IsCycloProduct P4 := by
  refine ⟨1, 0, {1, 1, 3}, ?_⟩
  have h := QOU.Mass.CyclotomicBoundaryKeystone.D4_cyclotomic
  simp only [QOU.Mass.CyclotomicBoundaryKeystone.D4] at h
  simp only [Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
    Multiset.prod_cons, Multiset.prod_singleton, C_1, one_mul, pow_zero]
  rw [P4, ← mul_assoc, ← sq, ← h]
  ring

theorem P5_cyclo : IsCycloProduct P5 := by
  refine ⟨2, 0, {1, 1, 2, 2, 3, 6}, ?_⟩
  have h := QOU.Mass.CyclotomicBoundaryKeystone.D5_cyclotomic
  simp only [QOU.Mass.CyclotomicBoundaryKeystone.D5] at h
  simp only [Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
    Multiset.prod_cons, Multiset.prod_singleton, pow_zero, mul_one]
  have e : (C (2 : ℤ) : ℤ[X]) = 2 := rfl
  rw [e, P5]
  linear_combination h

theorem zero_cyclo : IsCycloProduct 0 := ⟨0, 0, 0, by simp⟩

/-- The cleared tail `P_n` for `2 ≤ n ≤ 20` (`0` for `n = 2, 3`); outside that range this table
carries no meaning and is set to `0`. -/
noncomputable def tailPoly : ℕ → ℤ[X]
  | 4 => P4
  | 5 => P5
  | 6 => P6
  | 7 => P7
  | 8 => P8
  | 9 => P9
  | 10 => P10
  | 11 => P11
  | 12 => P12
  | 13 => P13
  | 14 => P14
  | 15 => P15
  | 16 => P16
  | 17 => P17
  | 18 => P18
  | 19 => P19
  | 20 => P20
  | _ => 0

/-- **The cyclotomic boundary, `2 ≤ n ≤ 20`.**  The cleared Habiro tail is a product of
cyclotomic polynomials exactly when `n ≤ 5`. -/
theorem cyclotomic_boundary (n : ℕ) (h2 : 2 ≤ n) (hN : n ≤ 20) :
    IsCycloProduct (tailPoly n) ↔ n ≤ 5 := by
  interval_cases n
  all_goals first
    | (simp only [tailPoly]; exact iff_of_true zero_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_true P4_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_true P5_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P6_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P7_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P8_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P9_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P10_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P11_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P12_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P13_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P14_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P15_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P16_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P17_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P18_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P19_not_cyclo (by norm_num))
    | (simp only [tailPoly]; exact iff_of_false P20_not_cyclo (by norm_num))

/-- `tailPoly n` really is the cleared tail of the definition, for `2 ≤ n ≤ 9`. -/
theorem tailPoly_spec {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (n : ℕ) (h2 : 2 ≤ n)
    (hN : n ≤ 9) (hB : ∀ k, 1 ≤ k → k ≤ n → qb2 q k ≠ 0) :
    ∃ m : ℕ, q ^ m * D q n = ((tailPoly n).map (Int.castRingHom K)).eval q := by
  interval_cases n
  · refine ⟨0, ?_⟩
    have h := tail_2 hq hB
    rw [h]; simp [tailPoly]
  · refine ⟨0, ?_⟩
    have h := tail_3 hq hB
    rw [h]; simp [tailPoly]
  · exact ⟨2, by rw [tail_4 hq hB]; simp only [tailPoly]; rw [P4_map_eval]⟩
  · exact ⟨4, by rw [tail_5 hq hB]; simp only [tailPoly]; rw [P5_map_eval]⟩
  · exact ⟨7, by rw [tail_6 hq hB]; simp only [tailPoly]; rw [P6_map_eval]⟩
  · exact ⟨10, by rw [tail_7 hq hB]; simp only [tailPoly]; rw [P7_map_eval]⟩
  · exact ⟨14, by rw [tail_8 hq hB]; simp only [tailPoly]; rw [P8_map_eval]⟩
  · exact ⟨19, by rw [tail_9 hq hB]; simp only [tailPoly]; rw [P9_map_eval]⟩

end QOU.Mass.CyclotomicBoundaryCertified
