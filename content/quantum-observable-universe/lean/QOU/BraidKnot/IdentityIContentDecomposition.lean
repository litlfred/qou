import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.BigOperators.Intervals

/-!
# Identity I, content decomposition — Lean formalization (partial)

Companion to `docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md`
and `WLambdaDefectClosedForm.lean`.  Identity I — the one carried representation-
theoretic input to the keystone `W_λ` defect cubic `144·C(n) = −n(n−1)(2n−13)` — is

    M(n) := (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} h_c²  =  n(3n−1)/2 ,

and it factors **without the Frame–Robinson–Thrall hook-length formula** as
`M(n) = binom(n,2) + n²` via

  (A)  per-partition  `Σ_c h_c² = Σ_c c(c)² + n²`   (a single-Young-diagram fact), and
  (B)  the Jucys–Murphy / Plancherel content-square mean `E_Planch[Σ c²] = binom(n,2)`.

Mathlib (as of the pinned toolchain) carries **no** hook-length, content, or
Jucys–Murphy infrastructure, so the *general* (A) and (B) are multi-session infra
builds.  This file delivers what is feasible **today**, sorry-free where possible:

* (A) is given a self-contained computable model (partition = weakly-decreasing
  `List ℕ`) and **machine-checked on all partitions `n ≤ 9`** (kernel `decide`);
  the general statement is carried honestly with `sorry` + `-- Ref:` to the proof.
* (B)'s computational heart — the identity coefficient of the central Jucys–Murphy
  element `Σ_k X_k²`, namely `Σ_{k<n} k = binom(n,2)` — is **proved sorry-free**;
  the full Plancherel-mean statement is carried with `sorry` + `-- Ref:`.

Base ring `ℤ` throughout; nothing archimedean (no `q₀`, no 210 ppb).  No fit.
-/

namespace QOU.BraidKnot.IdentityI

/-! ## (A) self-contained computable model on `List ℕ` -/

/-- Column length of a partition (a weakly-decreasing `List ℕ`) at column `j`:
the number of parts exceeding `j` (`= λ'_{j+1}`, 0-indexed). -/
def colLen (l : List ℕ) (j : ℕ) : ℕ := (l.filter (fun p => j < p)).length

/-- `Σ_{cells} h(c)²` with hook `h(i,j) = (λ_i − j) + (colLen j − i) − 1`
(`0`-indexed `i,j`; for a weakly-decreasing `l` and a genuine cell both summands are
`≥ 1`, so the `ℕ` subtraction is exact). -/
def sumSqHooks (l : List ℕ) : ℤ :=
  ((List.range l.length).map fun i =>
    ((List.range (l.getD i 0)).map fun j =>
      (((l.getD i 0 - j) + (colLen l j - i) - 1 : ℕ) : ℤ) ^ 2).sum).sum

/-- `Σ_{cells} c(c)²` with content `c(i,j) = j − i`.  The inner binder is annotated
`(j : ℕ)` so the cast `(j : ℤ)` lives inside a single `ℕ → ℤ` map (matching `sumSqHooks`),
keeping the def reducible for the closed-form lemmas below; the values are unchanged. -/
def sumSqContents (l : List ℕ) : ℤ :=
  ((List.range l.length).map fun i =>
    ((List.range (l.getD i 0)).map fun (j : ℕ) => ((j : ℤ) - (i : ℤ)) ^ 2).sum).sum

/-- Size `n = Σ λ_i`. -/
def sz (l : List ℕ) : ℕ := l.sum

/-- `Σ_{cells} arm(c)²` with arm `a(i,j) = λ_i − 1 − j` (cells of row `i` are
`j = 0 … λ_i − 1`).  One of the six terms of the hook square `h² = (a+l+1)²`. -/
def sumSqArms (l : List ℕ) : ℤ :=
  ((List.range l.length).map fun i =>
    ((List.range (l.getD i 0)).map fun (j : ℕ) => ((l.getD i 0 - 1 - j : ℕ) : ℤ) ^ 2).sum).sum

/-- `Σ_{cells} arm(c)` with arm `a(i,j) = λ_i − 1 − j`.  Carries the `2a` cross term of
`h² = (a+l+1)²`. -/
def sumArms (l : List ℕ) : ℤ :=
  ((List.range l.length).map fun i =>
    ((List.range (l.getD i 0)).map fun (j : ℕ) => ((l.getD i 0 - 1 - j : ℕ) : ℤ)).sum).sum

/-- `Σ_{cells} leg(c)²` with leg `l(i,j) = colLen(j) − 1 − i`, summed by **columns**
`j = 0 … λ_1 − 1` (`λ_1 = l.headD 0`).  The `l²` term of `h² = (a+l+1)²`. -/
def sumSqLegs (l : List ℕ) : ℤ :=
  ((List.range (l.headD 0)).map fun j =>
    ((List.range (colLen l j)).map fun (i : ℕ) => ((colLen l j - 1 - i : ℕ) : ℤ) ^ 2).sum).sum

/-- `Σ_{cells} leg(c)` with leg `l(i,j) = colLen(j) − 1 − i`, summed by columns.
Carries the `2l` cross term of `h² = (a+l+1)²`. -/
def sumLegs (l : List ℕ) : ℤ :=
  ((List.range (l.headD 0)).map fun j =>
    ((List.range (colLen l j)).map fun (i : ℕ) => ((colLen l j - 1 - i : ℕ) : ℤ)).sum).sum

/-! ### (A) machine-checked for ALL partitions `n ≤ 9` (sorry-free)

`Σ_c h_c² = Σ_c c(c)² + n²` verified by kernel `decide` over **every** partition with
`n ≤ 9` (96 of them) — a uniform bounded-universal, strengthening earlier hand-picked
instances.  Genuine native computation, not stubs. -/

/-- All integer partitions for `1 ≤ n ≤ 9` (96 of them), as weakly-decreasing lists. -/
def allPartsLE9 : List (List ℕ) :=
  [[1], [2], [1, 1], [3], [2, 1], [1, 1, 1], [4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1],
   [5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1],
   [6], [5, 1], [4, 2], [4, 1, 1], [3, 3], [3, 2, 1], [3, 1, 1, 1], [2, 2, 2], [2, 2, 1, 1],
   [2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
   [7], [6, 1], [5, 2], [5, 1, 1], [4, 3], [4, 2, 1], [4, 1, 1, 1], [3, 3, 1], [3, 2, 2],
   [3, 2, 1, 1], [3, 1, 1, 1, 1], [2, 2, 2, 1], [2, 2, 1, 1, 1], [2, 1, 1, 1, 1, 1],
   [1, 1, 1, 1, 1, 1, 1],
   [8], [7, 1], [6, 2], [6, 1, 1], [5, 3], [5, 2, 1], [5, 1, 1, 1], [4, 4], [4, 3, 1], [4, 2, 2],
   [4, 2, 1, 1], [4, 1, 1, 1, 1], [3, 3, 2], [3, 3, 1, 1], [3, 2, 2, 1], [3, 2, 1, 1, 1],
   [3, 1, 1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 1, 1], [2, 2, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1],
   [1, 1, 1, 1, 1, 1, 1, 1],
   [9], [8, 1], [7, 2], [7, 1, 1], [6, 3], [6, 2, 1], [6, 1, 1, 1], [5, 4], [5, 3, 1], [5, 2, 2],
   [5, 2, 1, 1], [5, 1, 1, 1, 1], [4, 4, 1], [4, 3, 2], [4, 3, 1, 1], [4, 2, 2, 1], [4, 2, 1, 1, 1],
   [4, 1, 1, 1, 1, 1], [3, 3, 3], [3, 3, 2, 1], [3, 3, 1, 1, 1], [3, 2, 2, 2], [3, 2, 2, 1, 1],
   [3, 2, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 1], [2, 2, 2, 1, 1, 1],
   [2, 2, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]

/-- **(A) for all partitions `n ≤ 9`** — sorry-free kernel `decide` over `allPartsLE9`. -/
theorem identityA_verified_le9 :
    ∀ l ∈ allPartsLE9, sumSqHooks l = sumSqContents l + (sz l : ℤ) ^ 2 := by
  decide

/-- **Building block for the general (A) proof — sum of squares (sorry-free).**
`6·Σ_{k<N} k² = N(N−1)(2N−1)`.  Together with the Gauss sum `Σ_{k<N} k` it gives the
single-row content closed form `Σ_{j<λ_i}(j−i)²` in the β-set/arm-leg assembly. -/
theorem six_mul_sum_range_sq (N : ℕ) :
    6 * ∑ k ∈ Finset.range N, (k : ℤ) ^ 2 = (N : ℤ) * (N - 1) * (2 * N - 1) := by
  induction N with
  | zero => simp
  | succ m ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    push_cast
    ring

/-- **Gauss sum over `ℤ` (sorry-free).** `2·Σ_{k<N} k = N(N−1)`.  The linear companion
of `six_mul_sum_range_sq`; feeds the arm/content linear pieces below. -/
theorem two_mul_sum_range_int (N : ℕ) :
    2 * ∑ k ∈ Finset.range N, (k : ℤ) = (N : ℤ) * ((N : ℤ) - 1) := by
  induction N with
  | zero => simp
  | succ m ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    push_cast
    ring

/-! ### Content side of (A), closed form (sorry-free)

The content half of (A) needs **no** β-set / hook-length / Jucys–Murphy machinery:
`Σ_c c(c)²` reduces to an explicit cubic summed over the rows.  These three lemmas
carry that reduction end to end, so the only remaining work for the general (A)
(`sumSqHooks_eq_sumSqContents_add_sq` below) is the **hook side** (L1)+(Lal). -/

/-- Bridge a `List.range`-mapped sum to the corresponding `Finset.range` sum, so the
closed-form algebra lemmas apply to the computable `List`-based models above. -/
theorem list_range_map_sum (n : ℕ) (f : ℕ → ℤ) :
    ((List.range n).map f).sum = ∑ i ∈ Finset.range n, f i := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.map_append, List.sum_append, ih, Finset.sum_range_succ]
    simp

/-- **Per-row content-square closed form (sorry-free).** For a row of length `m` at
row index `i`, `6·Σ_{j<m}(j−i)² = m(m−1)(2m−1) − 6i·m(m−1) + 6m·i²`.  This is the
content analogue of `six_mul_sum_range_sq`: the `Σ k²` cubic and the Gauss `Σ k`
assembled with the `−i` content shift. -/
theorem six_mul_sum_range_content_sq (m i : ℕ) :
    6 * ∑ j ∈ Finset.range m, ((j : ℤ) - (i : ℤ)) ^ 2
      = (m : ℤ) * ((m : ℤ) - 1) * (2 * (m : ℤ) - 1)
        - 6 * (i : ℤ) * ((m : ℤ) * ((m : ℤ) - 1)) + 6 * (m : ℤ) * (i : ℤ) ^ 2 := by
  induction m with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    push_cast
    ring

/-- **Content side of (A), closed form (sorry-free).** The full squared-content sum
`Σ_c c(c)²` equals an explicit cubic summed over the rows — no hook-length, β-set, or
Jucys–Murphy infrastructure.  Multiplying by `6` clears the `Σ k²` / `Σ k`
denominators: `6·Σ_c c(c)² = Σ_i [λ_i(λ_i−1)(2λ_i−1) − 6i·λ_i(λ_i−1) + 6λ_i·i²]`,
the rows indexed `0 ≤ i < length` with `λ_i = l.getD i 0`. -/
theorem six_mul_sumSqContents (l : List ℕ) :
    6 * sumSqContents l
      = ∑ i ∈ Finset.range l.length,
          ((l.getD i 0 : ℤ) * ((l.getD i 0 : ℤ) - 1) * (2 * (l.getD i 0 : ℤ) - 1)
            - 6 * (i : ℤ) * ((l.getD i 0 : ℤ) * ((l.getD i 0 : ℤ) - 1))
            + 6 * (l.getD i 0 : ℤ) * (i : ℤ) ^ 2) := by
  unfold sumSqContents
  rw [list_range_map_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [list_range_map_sum]
  exact six_mul_sum_range_content_sq (l.getD i 0) i

/-! ### Hook side of (A): arm + leg pieces, closed form (sorry-free)

Writing the hook as `h(c) = a(c) + l(c) + 1` expands the hook square into the six terms
`h² = a² + l² + 1 + 2·a·l + 2·a + 2·l`.  Four of them are per-row (arm) / per-column (leg)
independent and close by the reflection `Σ_{j<m}(m−1−j)^k = Σ_{k<m} k^k`: `a²`
(`six_mul_sumSqArms`), `l²` (`six_mul_sumSqLegs`), `2a` (`two_mul_sumArms`), `2l`
(`two_mul_sumLegs`).  The constant `1` sums to the cell count `n = sz`.  The **only**
genuinely 2-D piece left is the **arm·leg cross term** `Σ_c a(c)·l(c)` — the reindex
(Lal) — after which (A) reduces to `ring` / `Finset.sum` glue against the content closed
form `six_mul_sumSqContents`. -/

/-- **Arm-square side, closed form (sorry-free).** `6·Σ_c a(c)² = Σ_i λ_i(λ_i−1)(2λ_i−1)`,
reflecting each row's arm sum onto `Σ_{k<λ_i} k²`. -/
theorem six_mul_sumSqArms (l : List ℕ) :
    6 * sumSqArms l = ∑ i ∈ Finset.range l.length,
      (l.getD i 0 : ℤ) * ((l.getD i 0 : ℤ) - 1) * (2 * (l.getD i 0 : ℤ) - 1) := by
  unfold sumSqArms
  rw [list_range_map_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [list_range_map_sum, Finset.sum_range_reflect (fun k => ((k : ℤ)) ^ 2)]
  exact six_mul_sum_range_sq (l.getD i 0)

/-- **Arm-linear side, closed form (sorry-free).** `2·Σ_c a(c) = Σ_i λ_i(λ_i−1)`,
reflecting each row's arm sum onto the Gauss sum `Σ_{k<λ_i} k`. -/
theorem two_mul_sumArms (l : List ℕ) :
    2 * sumArms l = ∑ i ∈ Finset.range l.length,
      (l.getD i 0 : ℤ) * ((l.getD i 0 : ℤ) - 1) := by
  unfold sumArms
  rw [list_range_map_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [list_range_map_sum, Finset.sum_range_reflect (fun k => ((k : ℤ)))]
  exact two_mul_sum_range_int (l.getD i 0)

/-- **Leg-square side, closed form (sorry-free).** `6·Σ_c l(c)² = Σ_j colLen(j)(colLen(j)−1)(2·colLen(j)−1)`,
the column transpose of `six_mul_sumSqArms` (reflect each column's leg sum onto `Σ_{k<colLen j} k²`). -/
theorem six_mul_sumSqLegs (l : List ℕ) :
    6 * sumSqLegs l = ∑ j ∈ Finset.range (l.headD 0),
      (colLen l j : ℤ) * ((colLen l j : ℤ) - 1) * (2 * (colLen l j : ℤ) - 1) := by
  unfold sumSqLegs
  rw [list_range_map_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  rw [list_range_map_sum, Finset.sum_range_reflect (fun k => ((k : ℤ)) ^ 2)]
  exact six_mul_sum_range_sq (colLen l j)

/-- **Leg-linear side, closed form (sorry-free).** `2·Σ_c l(c) = Σ_j colLen(j)(colLen(j)−1)`,
the column transpose of `two_mul_sumArms`. -/
theorem two_mul_sumLegs (l : List ℕ) :
    2 * sumLegs l = ∑ j ∈ Finset.range (l.headD 0),
      (colLen l j : ℤ) * ((colLen l j : ℤ) - 1) := by
  unfold sumLegs
  rw [list_range_map_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  rw [list_range_map_sum, Finset.sum_range_reflect (fun k => ((k : ℤ)))]
  exact two_mul_sum_range_int (colLen l j)

/-! ### Hook side of (A): cell-membership duality + Fubini transpose (sorry-free)

The (L1)/(Lal) "2-D reindex" the roadmap names as the crux is, concretely, the ability to
transpose a **row**-indexed cell sum `Σ_{i<length} Σ_{j<λ_i}` into a **column**-indexed one
`Σ_{j<λ_1} Σ_{i<colLen j}`.  Its gateway is the **cell-membership duality**
`i < colLen(j) ↔ j < λ_i` (for weakly-decreasing `l`); `Finset.sum_comm'` then gives the
Fubini swap.  This is the machinery that discharges the leg terms (`l²`, `2l`) of the hook
square against the per-column `sumSqLegs` / `sumLegs` closed forms above. -/

/-- `colLen` recursion on a cons: prepending `a` adds a column-`j` cell iff `j < a`. -/
theorem colLen_cons (a : ℕ) (t : List ℕ) (j : ℕ) :
    colLen (a :: t) j = if j < a then colLen t j + 1 else colLen t j := by
  unfold colLen
  rw [List.filter_cons]
  by_cases h : j < a <;> simp [h]

/-- If every part is `≤ j`, column `j` is empty. -/
theorem colLen_eq_zero (t : List ℕ) (j : ℕ) (h : ∀ b ∈ t, b ≤ j) : colLen t j = 0 := by
  unfold colLen
  simp only [List.length_eq_zero_iff]
  rw [List.filter_eq_nil_iff]
  intro b hb
  simp only [decide_eq_true_eq]
  exact Nat.not_lt.mpr (h b hb)

/-- **Cell-membership duality (sorry-free).** For a weakly-decreasing partition, row `i`
reaches column `j` iff column `j` reaches row `i`: `i < colLen(j) ↔ j < λ_i`.  The gateway
to the Fubini transpose; an induction on the parts using the column-empty lemma at the head. -/
theorem colLen_duality : ∀ (l : List ℕ), l.Sorted (· ≥ ·) → ∀ (i j : ℕ),
    (i < colLen l j ↔ j < l.getD i 0)
  | [], _, i, j => by simp [colLen]
  | a :: t, hl, i, j => by
    obtain ⟨hat, ht⟩ := List.sorted_cons.mp hl
    rw [colLen_cons]
    cases i with
    | zero =>
      simp only [List.getD_cons_zero]
      by_cases h : j < a
      · simp [h]
      · have hz : colLen t j = 0 :=
          colLen_eq_zero t j (fun b hb => le_trans (hat b hb) (Nat.not_lt.mp h))
        simp [h, hz]
    | succ i' =>
      simp only [List.getD_cons_succ]
      by_cases h : j < a
      · simp only [h, if_true, Nat.succ_lt_succ_iff]
        exact colLen_duality t ht i' j
      · have hz : colLen t j = 0 :=
          colLen_eq_zero t j (fun b hb => le_trans (hat b hb) (Nat.not_lt.mp h))
        simp only [h, if_false]
        rw [hz, ← colLen_duality t ht i' j, hz]
        omega

/-- `colLen ≤ length` (a column has at most as many cells as there are rows). -/
theorem colLen_le_length (l : List ℕ) (j : ℕ) : colLen l j ≤ l.length := by
  unfold colLen
  exact List.length_filter_le _ _

/-- Every part is `≤` the first (largest) part, for a weakly-decreasing partition. -/
theorem getD_le_headD (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (i : ℕ) :
    l.getD i 0 ≤ l.headD 0 := by
  cases l with
  | nil => simp
  | cons a t =>
    rw [List.headD_cons]
    cases i with
    | zero => simp
    | succ i' =>
      rw [List.getD_cons_succ]
      obtain ⟨hat, _⟩ := List.sorted_cons.mp hl
      rcases lt_or_ge i' t.length with hlen | hlen
      · rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hlen, Option.getD_some]
        exact hat _ (List.getElem_mem hlen)
      · rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none hlen, Option.getD_none]
        exact Nat.zero_le a

/-- **Fubini transpose (sorry-free).** A row-indexed cell sum equals the column-indexed one,
for any cell function `g`.  This is the (L1)/(Lal) 2-D reindex, via `Finset.sum_comm'` and the
cell-membership duality.  The leg terms of `Σ_c h²` become per-column sums under it. -/
theorem cell_fubini (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (g : ℕ → ℕ → ℤ) :
    ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), g i j
      = ∑ j ∈ Finset.range (l.headD 0), ∑ i ∈ Finset.range (colLen l j), g i j := by
  apply Finset.sum_comm'
  intro i j
  simp only [Finset.mem_range]
  constructor
  · rintro ⟨hi, hj⟩
    exact ⟨(colLen_duality l hl i j).mpr hj, lt_of_lt_of_le hj (getD_le_headD l hl i)⟩
  · rintro ⟨hi, hj⟩
    exact ⟨lt_of_lt_of_le hi (colLen_le_length l j), (colLen_duality l hl i j).mp hi⟩

/-! ### Hook side of (A): the min-sum bridge (cross-term gateway, sorry-free)

The arm·leg **cross term** `Σ_c a·l` (the last open piece of (A)) couples rows and columns;
tracing it through `cell_fubini` produces `Σ_{j<λ_i} colLen(j)` inner sums, which equal the
**min-sum** `Σ_k min(λ_i, λ_k)`.  That identity — `colLen` as a sum of row-indicators, then
`Finset.sum_comm`, then the indicator/`min` count — is the bridge that turns the cross term
into a closed form over ordered row-pairs. -/

/-- `colLen` as a sum of row-indicators: `colLen(j) = Σ_k [j < λ_k]`. -/
theorem colLen_eq_indicator_sum (l : List ℕ) (j : ℕ) :
    colLen l j = ∑ k ∈ Finset.range l.length, (if j < l.getD k 0 then 1 else 0) := by
  induction l with
  | nil => simp [colLen]
  | cons a t ih =>
    rw [colLen_cons, List.length_cons, Finset.sum_range_succ']
    simp only [List.getD_cons_succ, List.getD_cons_zero]
    rw [← ih]
    by_cases h : j < a <;> simp [h, add_comm]

/-- `Σ_{j<a} [j < b] = min a b`. -/
theorem sum_indicator_lt_eq_min (a b : ℕ) :
    ∑ j ∈ Finset.range a, (if j < b then (1 : ℕ) else 0) = min a b := by
  induction a with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    by_cases h : n < b <;> simp only [h, if_true, if_false] <;> omega

/-- **Atomic min-sum bridge (sorry-free).** The row sum of column-heights over a row equals
the min-sum: `Σ_{j<λ_i} colLen(j) = Σ_k min(λ_i, λ_k)`.  Gateway to the arm·leg cross term
(its `Σ_{i,k} λ_i·min(λ_i,λ_k)` closed form, via an order-split on `λ_i` vs `λ_k`). -/
theorem sum_colLen_eq_sum_min (l : List ℕ) (i : ℕ) :
    ∑ j ∈ Finset.range (l.getD i 0), colLen l j
      = ∑ k ∈ Finset.range l.length, min (l.getD i 0) (l.getD k 0) := by
  simp_rw [colLen_eq_indicator_sum l]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro k _
  exact sum_indicator_lt_eq_min (l.getD i 0) (l.getD k 0)

/-! ### Hook side of (A): order-split machinery (sorry-free)

With the parts weakly decreasing, `min(λ_i, λ_k) = λ_{max(i,k)}`, so each column power-moment
`Σ_j colLen(j)^d` collapses to a **row** closed form — no genuine triple-min needed.  The
order-split below is the engine: it turns `Σ_{i,k} min(λ_i,λ_k)` into `Σ_i (2i+1)·λ_i`. -/

/-- For a weakly-decreasing list, `getD` is antitone in the index. -/
theorem getD_antitone (l : List ℕ) (hl : l.Sorted (· ≥ ·)) {i k : ℕ} (hik : i ≤ k) :
    l.getD k 0 ≤ l.getD i 0 := by
  rcases lt_or_ge k l.length with hk | hk
  · have hi : i < l.length := lt_of_le_of_lt hik hk
    rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hk, Option.getD_some,
        List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi, Option.getD_some]
    exact hl.rel_get_of_le (Fin.mk_le_mk.mpr hik)
  · rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none hk, Option.getD_none]
    exact Nat.zero_le _

/-- **Min order-split (sorry-free).** For an antitone sequence,
`Σ_{i,k<r} min(a i, a k) = Σ_{i<r} (2i+1)·a i` — each new index `n` contributes a full
row + column of `a n` (it is the smallest, so the min on the new cross terms).  This is the
row closed form of the column moment `Σ_j colLen(j)²`. -/
theorem antitone_min_sum (a : ℕ → ℕ) (h : ∀ i k, i ≤ k → a k ≤ a i) (r : ℕ) :
    ∑ i ∈ Finset.range r, ∑ k ∈ Finset.range r, min (a i) (a k)
      = ∑ i ∈ Finset.range r, (2 * i + 1) * a i := by
  induction r with
  | zero => simp
  | succ n ih =>
    have h1 : ∑ i ∈ Finset.range n, min (a i) (a n) = n * a n := by
      rw [Finset.sum_congr rfl (fun i hi => min_eq_right (h i n (le_of_lt (Finset.mem_range.mp hi))))]
      rw [Finset.sum_const, Finset.card_range, smul_eq_mul]
    have h2 : ∑ k ∈ Finset.range n, min (a n) (a k) = n * a n := by
      rw [Finset.sum_congr rfl (fun k hk => min_eq_left (h k n (le_of_lt (Finset.mem_range.mp hk))))]
      rw [Finset.sum_const, Finset.card_range, smul_eq_mul]
    rw [Finset.sum_range_succ]
    simp_rw [Finset.sum_range_succ, Finset.sum_add_distrib]
    rw [ih, h1, h2, min_self]
    ring

/-- Product of two `<`-indicators is the indicator of the `min`. -/
theorem indicator_mul (j a b : ℕ) :
    (if j < a then (1 : ℕ) else 0) * (if j < b then 1 else 0) = if j < min a b then 1 else 0 := by
  simp only [lt_min_iff]
  split_ifs <;> simp_all

/-- `Σ_j colLen(j)² = Σ_{i,k} min(λ_i, λ_k)` (expand each `colLen` to row-indicators,
`Finset.sum_comm` the column index inward, then the indicator/`min` count). -/
theorem sum_colLen_sq_eq_sum_min (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ j ∈ Finset.range (l.headD 0), (colLen l j) ^ 2
      = ∑ i ∈ Finset.range l.length, ∑ k ∈ Finset.range l.length,
          min (l.getD i 0) (l.getD k 0) := by
  simp_rw [pow_two, colLen_eq_indicator_sum l, Finset.sum_mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro k _
  simp_rw [indicator_mul]
  rw [sum_indicator_lt_eq_min]
  exact min_eq_right (le_trans (min_le_left _ _) (getD_le_headD l hl i))

/-- **`K2` as a row form (sorry-free).** `Σ_j colLen(j)² = Σ_i (2i+1)·λ_i`. -/
theorem sum_colLen_sq_row_form (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ j ∈ Finset.range (l.headD 0), (colLen l j) ^ 2
      = ∑ i ∈ Finset.range l.length, (2 * i + 1) * (l.getD i 0) := by
  rw [sum_colLen_sq_eq_sum_min l hl,
    antitone_min_sum (fun i => l.getD i 0) (fun i k hik => getD_antitone l hl hik) l.length]

/-- **`K1` as a row form (sorry-free).** `Σ_j colLen(j) = Σ_i λ_i` (both count cells). -/
theorem sum_colLen_eq_sum_parts (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ j ∈ Finset.range (l.headD 0), colLen l j = ∑ i ∈ Finset.range l.length, l.getD i 0 := by
  simp_rw [colLen_eq_indicator_sum l]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _
  rw [sum_indicator_lt_eq_min]
  exact min_eq_right (getD_le_headD l hl i)

/-- The size `n = Σ λ_i` is the `Finset.range` sum of the parts. -/
theorem sum_range_getD_eq_sz (l : List ℕ) :
    ∑ i ∈ Finset.range l.length, l.getD i 0 = sz l := by
  unfold sz
  induction l with
  | nil => simp
  | cons a t ih =>
    rw [List.length_cons, Finset.sum_range_succ', List.sum_cons]
    simp only [List.getD_cons_succ, List.getD_cons_zero]
    rw [ih]; ring

/-- **Triple min order-split (sorry-free).** For an antitone sequence,
`Σ_{i,k,m<r} min(min(a i,a k),a m) = Σ_{i<r}(3i²+3i+1)·a i` — each new index `n` is the
smallest, so all 7 "shell" tuples touching it contribute `a n`
(`(n+1)³−n³ = 3n²+3n+1`).  Row closed form of the column moment `Σ_j colLen(j)³`. -/
theorem antitone_min3_sum (a : ℕ → ℕ) (h : ∀ i k, i ≤ k → a k ≤ a i) (r : ℕ) :
    ∑ i ∈ Finset.range r, ∑ k ∈ Finset.range r, ∑ m ∈ Finset.range r,
        min (min (a i) (a k)) (a m)
      = ∑ i ∈ Finset.range r, (3 * i ^ 2 + 3 * i + 1) * a i := by
  induction r with
  | zero => simp
  | succ n ih =>
    have hL : ∀ x ∈ Finset.range n, a n ≤ a x :=
      fun x hx => h x n (le_of_lt (Finset.mem_range.mp hx))
    rw [Finset.sum_range_succ]
    simp_rw [Finset.sum_range_succ, Finset.sum_add_distrib]
    rw [ih]
    have t2 : ∑ x ∈ Finset.range n, ∑ k ∈ Finset.range n, min (min (a x) (a k)) (a n)
        = n ^ 2 * a n := by
      have e : ∀ x ∈ Finset.range n, ∑ k ∈ Finset.range n, min (min (a x) (a k)) (a n) = n * a n := by
        intro x hx
        rw [Finset.sum_congr rfl (fun k hk => min_eq_right (le_min (hL x hx) (hL k hk)))]
        simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]
      rw [Finset.sum_congr rfl e]
      simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]; ring
    have t3 : ∑ x ∈ Finset.range n, ∑ m ∈ Finset.range n, min (min (a x) (a n)) (a m)
        = n ^ 2 * a n := by
      have e : ∀ x ∈ Finset.range n, ∑ m ∈ Finset.range n, min (min (a x) (a n)) (a m) = n * a n := by
        intro x hx
        rw [Finset.sum_congr rfl (fun m hm => by rw [min_eq_right (hL x hx), min_eq_left (hL m hm)])]
        simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]
      rw [Finset.sum_congr rfl e]
      simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]; ring
    have t4 : ∑ x ∈ Finset.range n, min (min (a x) (a n)) (a n) = n * a n := by
      rw [Finset.sum_congr rfl (fun x hx => by rw [min_eq_right (hL x hx), min_self])]
      simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]
    have t5 : ∑ x ∈ Finset.range n, ∑ m ∈ Finset.range n, min (min (a n) (a x)) (a m)
        = n ^ 2 * a n := by
      have e : ∀ x ∈ Finset.range n, ∑ m ∈ Finset.range n, min (min (a n) (a x)) (a m) = n * a n := by
        intro x hx
        rw [Finset.sum_congr rfl (fun m hm => by rw [min_eq_left (hL x hx), min_eq_left (hL m hm)])]
        simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]
      rw [Finset.sum_congr rfl e]
      simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]; ring
    have t6 : ∑ x ∈ Finset.range n, min (min (a n) (a x)) (a n) = n * a n := by
      rw [Finset.sum_congr rfl (fun x hx => by rw [min_eq_left (hL x hx), min_self])]
      simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]
    have t7 : ∑ m ∈ Finset.range n, min (min (a n) (a n)) (a m) = n * a n := by
      rw [Finset.sum_congr rfl (fun m hm => by rw [min_self, min_eq_left (hL m hm)])]
      simp only [Finset.sum_const, Finset.card_range, smul_eq_mul]
    rw [t2, t3, t4, t5, t6, t7, min_self, min_self]
    ring

/-- `Σ_c colLen(c)³ = Σ_{x,i,m} min3(λ_x,λ_i,λ_m)` (cube each `colLen` into row-indicators,
`sum_comm` the column index inward, then the triple-indicator/`min` count).  Right-associated
`min` to match the natural product expansion. -/
theorem sum_colLen_cube_eq_sum_min3 (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ c ∈ Finset.range (l.headD 0), (colLen l c) ^ 3
      = ∑ x ∈ Finset.range l.length, ∑ i ∈ Finset.range l.length, ∑ m ∈ Finset.range l.length,
          min (l.getD x 0) (min (l.getD i 0) (l.getD m 0)) := by
  have cube : ∀ c, (colLen l c) ^ 3 = ∑ x ∈ Finset.range l.length, ∑ i ∈ Finset.range l.length,
      ∑ m ∈ Finset.range l.length, (if c < l.getD x 0 then (1 : ℕ) else 0) *
        ((if c < l.getD i 0 then 1 else 0) * (if c < l.getD m 0 then 1 else 0)) := by
    intro c
    rw [pow_three]
    simp_rw [colLen_eq_indicator_sum l]
    rw [Finset.sum_mul_sum]
    simp_rw [Finset.sum_mul, Finset.mul_sum]
  simp_rw [cube]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl; intro x _
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl; intro i _
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl; intro m _
  simp_rw [indicator_mul]
  rw [sum_indicator_lt_eq_min]
  exact min_eq_right (le_trans (min_le_left _ _) (getD_le_headD l hl x))

/-- **`K3` as a row form (sorry-free).** `Σ_j colLen(j)³ = Σ_i (3i²+3i+1)·λ_i`. -/
theorem sum_colLen_cube_row_form (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ c ∈ Finset.range (l.headD 0), (colLen l c) ^ 3
      = ∑ i ∈ Finset.range l.length, (3 * i ^ 2 + 3 * i + 1) * (l.getD i 0) := by
  rw [sum_colLen_cube_eq_sum_min3 l hl]
  simp_rw [← min_assoc]
  exact antitone_min3_sum (fun i => l.getD i 0) (fun i k hik => getD_antitone l hl hik) l.length

/-! ### Hook side of (A): cross-term foundation (sorry-free)

The arm·leg cross term `Σ_c P·Q` (`P = λ_i−j`, `Q = colLen j − i`) needs a `λ_i`-weighted
min-sum and a `j`-weighted column moment.  Two reusable order-split primitives: a **general**
`f`-min-sum (covering the `j`-weighted moment via `f = m↦\binom m2`) and a **per-row** min
split (for the `λ_i`-weighted sum, whose tail is `Σ_{i<k} λ_i λ_k`). -/

/-- General `f`-min-sum: `Σ_{i,k<r} f(min(a i,a k)) = Σ_{i<r}(2i+1)·f(a i)` for antitone `a`.
Generalizes `antitone_min_sum` (`f = id`); also gives `Σ_j j·colLen(j)²` with `f = m↦\binom m2`. -/
theorem antitone_f_min_sum (a : ℕ → ℕ) (f : ℕ → ℕ) (h : ∀ i k, i ≤ k → a k ≤ a i) (r : ℕ) :
    ∑ i ∈ Finset.range r, ∑ k ∈ Finset.range r, f (min (a i) (a k))
      = ∑ i ∈ Finset.range r, (2 * i + 1) * f (a i) := by
  induction r with
  | zero => simp
  | succ n ih =>
    have h1 : ∑ i ∈ Finset.range n, f (min (a i) (a n)) = n * f (a n) := by
      rw [Finset.sum_congr rfl (fun i hi => by
        rw [min_eq_right (h i n (le_of_lt (Finset.mem_range.mp hi)))])]
      rw [Finset.sum_const, Finset.card_range, smul_eq_mul]
    have h2 : ∑ k ∈ Finset.range n, f (min (a n) (a k)) = n * f (a n) := by
      rw [Finset.sum_congr rfl (fun k hk => by
        rw [min_eq_left (h k n (le_of_lt (Finset.mem_range.mp hk)))])]
      rw [Finset.sum_const, Finset.card_range, smul_eq_mul]
    rw [Finset.sum_range_succ]
    simp_rw [Finset.sum_range_succ, Finset.sum_add_distrib]
    rw [ih, h1, h2, min_self]
    ring

/-- Per-row min split: `Σ_{k<r} min(a i,a k) = (i+1)·a i + Σ_{i<k<r} a k` (antitone, `i<r`).
The tail `Σ_{i<k<r} a k`, weighted by `a i` and summed, becomes `Σ_{i<k} a i a k`. -/
theorem per_i_min_split (a : ℕ → ℕ) (h : ∀ i k, i ≤ k → a k ≤ a i) (r i : ℕ) (hir : i < r) :
    ∑ k ∈ Finset.range r, min (a i) (a k)
      = (i + 1) * a i + ∑ k ∈ Finset.Ico (i + 1) r, a k := by
  rw [← Finset.sum_range_add_sum_Ico _ (Nat.succ_le_of_lt hir)]
  congr 1
  · rw [Finset.sum_congr rfl (fun k hk =>
      min_eq_left (h k i (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk))))]
    rw [Finset.sum_const, Finset.card_range, smul_eq_mul]
  · apply Finset.sum_congr rfl
    intro k hk
    exact min_eq_right (h i k (le_of_lt (Finset.mem_Ico.mp hk).1))

/-- `j`-weighted `<`-indicator sum: `Σ_{j<a}(if j<b then j else 0) = Σ_{j<min a b} j`. -/
theorem sum_ite_lt_id (a b : ℕ) :
    ∑ j ∈ Finset.range a, (if j < b then j else 0) = ∑ j ∈ Finset.range (min a b), j := by
  induction a with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    by_cases h : n < b
    · have hm : min (n + 1) b = min n b + 1 := by omega
      have hn : min n b = n := by omega
      rw [hm, Finset.sum_range_succ, hn]; simp [h]
    · have hm : min (n + 1) b = min n b := by omega
      rw [hm]; simp [h]

/-- `Σ_c c·colLen(c)² = Σ_{i,k} Σ_{j<min(λ_i,λ_k)} j` (`j`-weighted analogue of K2). -/
theorem sum_j_colLen_sq_eq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ c ∈ Finset.range (l.headD 0), c * (colLen l c) ^ 2
      = ∑ i ∈ Finset.range l.length, ∑ k ∈ Finset.range l.length,
          ∑ j ∈ Finset.range (min (l.getD i 0) (l.getD k 0)), j := by
  simp_rw [pow_two, colLen_eq_indicator_sum l, Finset.sum_mul_sum, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl; intro i _
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl; intro k _
  simp_rw [indicator_mul, mul_ite, mul_one, mul_zero]
  rw [sum_ite_lt_id, min_eq_right (le_trans (min_le_left _ _) (getD_le_headD l hl i))]

/-- **`j`-weighted K2 as a row form (sorry-free).** `Σ_j j·colLen(j)² = Σ_i (2i+1)·Σ_{j<λ_i} j`. -/
theorem sum_j_colLen_sq_row_form (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ c ∈ Finset.range (l.headD 0), c * (colLen l c) ^ 2
      = ∑ i ∈ Finset.range l.length, (2 * i + 1) * (∑ j ∈ Finset.range (l.getD i 0), j) := by
  rw [sum_j_colLen_sq_eq l hl]
  exact antitone_f_min_sum (fun i => l.getD i 0) (fun m => ∑ j ∈ Finset.range m, j)
    (fun i k hik => getD_antitone l hl hik) l.length

/-- **λ-weighted min-sum (sorry-free).** `2·Σ_i λ_i·Σ_k min(λ_i,λ_k) = Σ_i(2i+1)λ_i² + n²`
(over `ℕ`).  Uses the pointwise identity `(a+b)·min(a,b) = min(a,b)² + a·b` + symmetry,
collapsing to `antitone_f_min_sum` (`f = ·²`) and `(Σλ)² = n²` — no per-row split needed. -/
theorem two_mul_sum_lambda_min (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    2 * ∑ i ∈ Finset.range l.length, (l.getD i 0) *
        (∑ k ∈ Finset.range l.length, min (l.getD i 0) (l.getD k 0))
      = (∑ i ∈ Finset.range l.length, (2 * i + 1) * (l.getD i 0) ^ 2) + (sz l) ^ 2 := by
  have hS : ∑ i ∈ Finset.range l.length, (l.getD i 0) *
        (∑ k ∈ Finset.range l.length, min (l.getD i 0) (l.getD k 0))
      = ∑ i ∈ Finset.range l.length, ∑ k ∈ Finset.range l.length,
        (l.getD i 0) * min (l.getD i 0) (l.getD k 0) := by
    apply Finset.sum_congr rfl; intro i _; rw [Finset.mul_sum]
  have sym : ∑ i ∈ Finset.range l.length, ∑ k ∈ Finset.range l.length,
        (l.getD i 0) * min (l.getD i 0) (l.getD k 0)
      = ∑ i ∈ Finset.range l.length, ∑ k ∈ Finset.range l.length,
        (l.getD k 0) * min (l.getD i 0) (l.getD k 0) := by
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl; intro i _
    apply Finset.sum_congr rfl; intro k _
    rw [min_comm]
  have key : ∀ i k : ℕ, (l.getD i 0) * min (l.getD i 0) (l.getD k 0)
      + (l.getD k 0) * min (l.getD i 0) (l.getD k 0)
      = (min (l.getD i 0) (l.getD k 0)) ^ 2 + (l.getD i 0) * (l.getD k 0) := by
    intro i k
    rcases le_total (l.getD i 0) (l.getD k 0) with h | h
    · rw [min_eq_left h]; ring
    · rw [min_eq_right h]; ring
  rw [hS, two_mul]
  nth_rewrite 2 [sym]
  rw [← Finset.sum_add_distrib]
  simp_rw [← Finset.sum_add_distrib]
  simp_rw [key]
  simp_rw [Finset.sum_add_distrib]
  rw [← Finset.sum_mul_sum, sum_range_getD_eq_sz,
    antitone_f_min_sum (fun i => l.getD i 0) (fun m => m ^ 2)
      (fun i k hik => getD_antitone l hl hik) l.length]
  ring

/-- Reflected square sum: `6·Σ_{j<M}((M:ℤ)−j)² = M(M+1)(2M+1)` (the `Σ_{m=1}^M m²` form). -/
theorem six_mul_sum_range_refl_sq (M : ℕ) :
    6 * ∑ j ∈ Finset.range M, ((M : ℤ) - j) ^ 2 = (M : ℤ) * ((M : ℤ) + 1) * (2 * (M : ℤ) + 1) := by
  have h1 : ∑ j ∈ Finset.range M, ((M : ℤ) - j) ^ 2 = ∑ j ∈ Finset.range M, ((j : ℤ) + 1) ^ 2 := by
    rw [← Finset.sum_range_reflect (fun j => ((M : ℤ) - j) ^ 2) M]
    apply Finset.sum_congr rfl
    intro j hj
    have hjM := Finset.mem_range.mp hj
    have : ((M - 1 - j : ℕ) : ℤ) = (M : ℤ) - 1 - j := by omega
    rw [this]; ring
  have h2 : ∑ j ∈ Finset.range (M + 1), (j : ℤ) ^ 2 = ∑ j ∈ Finset.range M, ((j : ℤ) + 1) ^ 2 := by
    rw [Finset.sum_range_succ']; simp
  rw [h1, ← h2, six_mul_sum_range_sq (M + 1)]; push_cast; ring

/-- Reflected linear sum: `2·Σ_{j<M}((M:ℤ)−j) = M(M+1)` (the `Σ_{m=1}^M m` form). -/
theorem two_mul_sum_range_refl (M : ℕ) :
    2 * ∑ j ∈ Finset.range M, ((M : ℤ) - j) = (M : ℤ) * ((M : ℤ) + 1) := by
  have h1 : ∑ j ∈ Finset.range M, ((M : ℤ) - j) = ∑ j ∈ Finset.range M, ((j : ℤ) + 1) := by
    rw [← Finset.sum_range_reflect (fun j => (M : ℤ) - j) M]
    apply Finset.sum_congr rfl
    intro j hj
    have hjM := Finset.mem_range.mp hj
    have : ((M - 1 - j : ℕ) : ℤ) = (M : ℤ) - 1 - j := by omega
    rw [this]; ring
  have h2 : ∑ j ∈ Finset.range (M + 1), (j : ℤ) = ∑ j ∈ Finset.range M, ((j : ℤ) + 1) := by
    rw [Finset.sum_range_succ']; simp
  rw [h1, ← h2, two_mul_sum_range_int (M + 1)]; push_cast; ring

/-- ℤ form of the K1 row moment. -/
theorem sum_colLen_parts_int (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ c ∈ Finset.range (l.headD 0), (colLen l c : ℤ)
      = ∑ i ∈ Finset.range l.length, (l.getD i 0 : ℤ) := by
  exact_mod_cast sum_colLen_eq_sum_parts l hl

/-- ℤ form of the K2 row moment. -/
theorem sum_colLen_sq_row_int (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ c ∈ Finset.range (l.headD 0), (colLen l c : ℤ) ^ 2
      = ∑ i ∈ Finset.range l.length, (2 * (i : ℤ) + 1) * (l.getD i 0 : ℤ) := by
  exact_mod_cast sum_colLen_sq_row_form l hl

/-- ℤ form of the K3 row moment. -/
theorem sum_colLen_cube_row_int (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    ∑ c ∈ Finset.range (l.headD 0), (colLen l c : ℤ) ^ 3
      = ∑ i ∈ Finset.range l.length, (3 * (i : ℤ) ^ 2 + 3 * (i : ℤ) + 1) * (l.getD i 0 : ℤ) := by
  exact_mod_cast sum_colLen_cube_row_form l hl

/-! ### Hook side of (A): the six per-term cell sums (sorry-free)

`H = P + Q − 1` with `P = λ_i − j` (arm+1), `Q = colLen j − i` (leg+1); `H² = P²+Q²+1+2PQ
−2P−2Q`.  The six cell sums below each reduce to a row form: `P` terms by row reflection,
`Q` terms by `cell_fubini` then the K-moment row forms, and the `PQ` cross via the
λ-weighted min-sum (`AC`) and the j-weighted K2 (`BC`). -/

/-- `P²` term. -/
theorem cellP_sq_eq (l : List ℕ) :
    6 * ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), ((l.getD i 0 : ℤ) - j) ^ 2
      = ∑ i ∈ Finset.range l.length,
          (l.getD i 0 : ℤ) * ((l.getD i 0 : ℤ) + 1) * (2 * (l.getD i 0 : ℤ) + 1) := by
  rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intro i _
  exact six_mul_sum_range_refl_sq (l.getD i 0)

/-- `P` term. -/
theorem cellP_eq (l : List ℕ) :
    2 * ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), ((l.getD i 0 : ℤ) - j)
      = ∑ i ∈ Finset.range l.length, (l.getD i 0 : ℤ) * ((l.getD i 0 : ℤ) + 1) := by
  rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intro i _
  exact two_mul_sum_range_refl (l.getD i 0)

/-- `Q²` term (`cell_fubini` + column reflection + K-moment row forms). -/
theorem cellQ_sq_eq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    6 * ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), ((colLen l j : ℤ) - i) ^ 2
      = ∑ i ∈ Finset.range l.length,
          (6 * (i : ℤ) ^ 2 + 12 * (i : ℤ) + 6) * (l.getD i 0 : ℤ) := by
  rw [cell_fubini l hl (fun i j => ((colLen l j : ℤ) - (i : ℤ)) ^ 2)]
  have hcol : 6 * ∑ j ∈ Finset.range (l.headD 0), ∑ i ∈ Finset.range (colLen l j),
        ((colLen l j : ℤ) - (i : ℤ)) ^ 2
      = ∑ j ∈ Finset.range (l.headD 0),
          (colLen l j : ℤ) * ((colLen l j : ℤ) + 1) * (2 * (colLen l j : ℤ) + 1) := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intro j _
    exact six_mul_sum_range_refl_sq (colLen l j)
  rw [hcol]
  simp_rw [show ∀ M : ℤ, M * (M + 1) * (2 * M + 1) = 2 * M ^ 3 + 3 * M ^ 2 + M from fun M => by ring]
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib]
  simp_rw [← Finset.mul_sum]
  rw [sum_colLen_cube_row_int l hl, sum_colLen_sq_row_int l hl, sum_colLen_parts_int l hl]
  simp_rw [Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl; intro i _; ring

/-- `Q` term (`cell_fubini` + column reflection + K-moment row forms). -/
theorem cellQ_eq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    2 * ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), ((colLen l j : ℤ) - i)
      = ∑ i ∈ Finset.range l.length, (2 * (i : ℤ) + 2) * (l.getD i 0 : ℤ) := by
  rw [cell_fubini l hl (fun i j => ((colLen l j : ℤ) - (i : ℤ)))]
  have hcol : 2 * ∑ j ∈ Finset.range (l.headD 0), ∑ i ∈ Finset.range (colLen l j),
        ((colLen l j : ℤ) - (i : ℤ))
      = ∑ j ∈ Finset.range (l.headD 0), (colLen l j : ℤ) * ((colLen l j : ℤ) + 1) := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intro j _
    exact two_mul_sum_range_refl (colLen l j)
  rw [hcol]
  simp_rw [show ∀ M : ℤ, M * (M + 1) = M ^ 2 + M from fun M => by ring]
  rw [Finset.sum_add_distrib, sum_colLen_sq_row_int l hl, sum_colLen_parts_int l hl,
    ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl; intro i _; ring

/-- `AC` cross piece `Σ_c λ_i·colLen j` (λ-weighted min-sum). -/
theorem cellAC_eq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    2 * ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
        (l.getD i 0 : ℤ) * (colLen l j : ℤ)
      = ∑ i ∈ Finset.range l.length, (2 * (i : ℤ) + 1) * (l.getD i 0 : ℤ) ^ 2 + (sz l : ℤ) ^ 2 := by
  have step1 : ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
        (l.getD i 0 : ℤ) * (colLen l j : ℤ)
      = ∑ i ∈ Finset.range l.length, (l.getD i 0 : ℤ) *
          (∑ k ∈ Finset.range l.length, (min (l.getD i 0) (l.getD k 0) : ℤ)) := by
    apply Finset.sum_congr rfl; intro i _
    rw [← Finset.mul_sum]
    congr 1
    exact_mod_cast sum_colLen_eq_sum_min l i
  rw [step1]
  exact_mod_cast two_mul_sum_lambda_min l hl

/-- `BC` cross piece `Σ_c j·colLen j` (j-weighted K2; `2·` clears the inner Gauss sum). -/
theorem cellBC_eq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    2 * ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), (j : ℤ) * (colLen l j : ℤ)
      = ∑ i ∈ Finset.range l.length, (2 * (i : ℤ) + 1) * ((l.getD i 0 : ℤ) * ((l.getD i 0 : ℤ) - 1)) := by
  have hbase : ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), (j : ℤ) * (colLen l j : ℤ)
      = ∑ i ∈ Finset.range l.length, (2 * (i : ℤ) + 1) * (∑ j ∈ Finset.range (l.getD i 0), (j : ℤ)) := by
    rw [cell_fubini l hl (fun i j => (j : ℤ) * (colLen l j : ℤ))]
    have hcol : ∑ j ∈ Finset.range (l.headD 0), ∑ i ∈ Finset.range (colLen l j), (j : ℤ) * (colLen l j : ℤ)
        = ∑ j ∈ Finset.range (l.headD 0), (j : ℤ) * (colLen l j : ℤ) ^ 2 := by
      apply Finset.sum_congr rfl; intro j _
      rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]; ring
    rw [hcol]
    have h := congrArg (fun n : ℕ => (n : ℤ)) (sum_j_colLen_sq_row_form l hl)
    push_cast at h
    exact h
  rw [hbase, Finset.mul_sum]
  apply Finset.sum_congr rfl; intro i _
  rw [show (2 : ℤ) * ((2 * (i : ℤ) + 1) * ∑ j ∈ Finset.range (l.getD i 0), (j : ℤ))
      = (2 * (i : ℤ) + 1) * (2 * ∑ j ∈ Finset.range (l.getD i 0), (j : ℤ)) from by ring,
    two_mul_sum_range_int]

/-- **Identity (A), general (carried — proof in progress).** For a weakly-decreasing
partition `l`, `Σ_c h_c² = Σ_c c(c)² + n²`.  Machine-checked for all `n ≤ 9`
(`identityA_verified_le9`) and exhaustively in Python for `n ≤ 22`.

Proof roadmap (β-set / arm-leg, audit doc §"Proof of (A)").  The hook-square expansion
`h² = a² + l² + 1 + 2·a·l + 2·a + 2·l` reduces (A) to its six per-term sums; the
infrastructure below is now in place to discharge all but one of them:
* arm terms `a²`, `2a` — closed over rows (`six_mul_sumSqArms`, `two_mul_sumArms`);
* leg terms `l²`, `2l` — closed over columns (`six_mul_sumSqLegs`, `two_mul_sumLegs`),
  reached from the row-indexed `Σ_c h²` by the **Fubini transpose** (`cell_fubini`, via the
  cell-membership duality `colLen_duality`);
* the constant `1` sums to `n = sz`; the content side is `six_mul_sumSqContents`.

The single remaining gap is the **arm·leg cross term** `Σ_c a·l` (the (Lal) row-pair
closed form `Σ_{i,k} λ_i·min(λ_i,λ_k) − …`), which couples rows and columns and needs a
`Σ min` reindex beyond the present transpose; the rest is `ring`/`Finset.sum` glue. -/
theorem sumSqHooks_eq_sumSqContents_add_sq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqHooks l = sumSqContents l + (sz l : ℤ) ^ 2 := by
  -- Ref: [manuscript] docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md §"Proof of (A)"
  -- Step 1: bridge to Finset double sum + cast the ℕ hook to its ℤ form (exact on cells).
  have hook_eq : sumSqHooks l = ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
      ((l.getD i 0 : ℤ) - j + (colLen l j : ℤ) - i - 1) ^ 2 := by
    unfold sumSqHooks
    simp_rw [list_range_map_sum]
    apply Finset.sum_congr rfl; intro i _
    apply Finset.sum_congr rfl; intro j hj
    have hj' := Finset.mem_range.mp hj
    have hi' : i < colLen l j := (colLen_duality l hl i j).mpr hj'
    have hcast : (((l.getD i 0 - j) + (colLen l j - i) - 1 : ℕ) : ℤ)
        = (l.getD i 0 : ℤ) - j + (colLen l j : ℤ) - i - 1 := by omega
    rw [hcast]
  -- Step 2 (remaining): expand `H² = P²+Q²+1+2PQ−2P−2Q` (P = λ_i−j, Q = colLen j−i), split,
  -- and plug in the verified term lemmas (six_mul_sum_range_refl_sq for P; cell_fubini +
  -- the K-moment row forms for Q; two_mul_sum_lambda_min + sum_j_colLen_sq_row_form for PQ;
  -- six_mul_sumSqContents for the content side), then `ring`.
  -- Ref: [manuscript] docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md §"Proof of (A)"
  sorry

/-! ## (B) Jucys–Murphy content-square mean -/

/-- **Identity (B), Jucys–Murphy core (sorry-free).** The Plancherel mean of the
squared-content sum equals the identity coefficient of the central element
`p₂(X) = Σ_{k=1}^n X_k²` of `ℂ[S_n]` (each `X_k` a Jucys–Murphy element), namely
`Σ_{k=1}^n (k−1) = Σ_{k<n} k`, and that coefficient is `binom(n,2)` — i.e.
`(Σ_{k<n} k)·2 = n(n−1)`.  Here is that arithmetic core, proved outright (Gauss). -/
theorem jm_identity_coeff_two (n : ℕ) :
    (∑ k ∈ Finset.range n, k) * 2 = n * (n - 1) := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [Finset.sum_range_succ, add_mul, ih]
    cases m with
    | zero => simp
    | succ p => simp only [Nat.add_sub_cancel]; ring

/-!
**Identity (B), general (carried — no faithful Lean statement yet).** The full
result `(1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} c(c)² = binom(n,2)` cannot even be *stated*
faithfully without `ℂ[S_n]` Wedderburn-dimension / Jucys–Murphy infrastructure
(partition-indexed block dimensions `dim(λ)`, `Σ_λ dim(λ)² = n!`, the central
`Σ_k X_k²`) — none of which is in the pinned Mathlib.  The reduction is:
the central `Σ_k X_k²` acts on block `V_λ` by `Σ_{c∈λ} c(c)²`, so the Plancherel
average of that scalar is its identity coefficient, `= Σ_{k<n}(k) = binom(n,2)`
(`jm_identity_coeff_two` above is exactly that identity coefficient).
Ref: docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md §"Proof of (B)".
-/

end QOU.BraidKnot.IdentityI
