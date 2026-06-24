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

/-! ### Hook side of (A): arm pieces, closed form (sorry-free)

Writing the hook as `h(c) = a(c) + l(c) + 1` (arm + leg + 1) expands the hook square into
`h² = a² + l² + 1 + 2·a·l + 2·a + 2·l`.  The **arm** is per-row independent (it depends
only on the position within a row), so — exactly like the content side — its square- and
linear-sums have closed forms over the rows, via the reflection `Σ_{j<m}(m−1−j)^k =
Σ_{k<m} k^k`.  These discharge two of the six terms; the remaining `l²`, `2·a·l`, `2·l`
(leg / arm·leg) terms are the genuinely 2-D `colLen` pieces (L1)+(Lal) still open. -/

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

/-- **Identity (A), general (carried — proof in progress).** For a weakly-decreasing
partition `l`, `Σ_c h_c² = Σ_c c(c)² + n²`.  Machine-checked for all `n ≤ 9`
(`identityA_verified_le9`) and exhaustively in Python for `n ≤ 22`.

Proof roadmap (β-set / arm-leg, audit doc §"Proof of (A)"), being formalized
incrementally below:
* **(L1)** β-set hook-square formula `Σ_c h² = Σ_i Σ_{s≤β_i} s² − Σ_{i<t}(β_i−β_t)²`;
* **(Lc)** per-bead contents along `β_i` are exactly `{j−i}`;
* **(Lal)** arm·leg row-pair closed form
  `Σ_c a·l = Σ_{i,k} λ_i·min(λ_i,λ_k) − Σ_i iλ_i² − Σ_j jλ'_j² + Σ_i i·\binom{λ_i+1}{2}`;
then the elementary single-sum cancellation gives `n²`.  The crux is the 2-D reindex
in (Lal); the rest is `ring`/`Finset.sum` glue. -/
theorem sumSqHooks_eq_sumSqContents_add_sq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqHooks l = sumSqContents l + (sz l : ℤ) ^ 2 := by
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
