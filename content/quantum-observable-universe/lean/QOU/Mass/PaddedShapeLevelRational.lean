import QOU.MathlibExt.QPartitionCombinatorics
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Mass.PaddedShapeLevelRational — level-rationality of padded-shape q-dimensions

Lean face of the §8/§10 decisive probe of
`docs/audits/2026-07-03-parabolic-cylinder-channel-interpolation.md`
(`computations/deligne_stable_range_binding_period_probe.py`, 99/99 exact): for a fixed
shape `μ`, the padded family `n ↦ dim_q(μ[n])`, `μ[n] = (n − |μ|, μ)`, is a fixed
rational function of `(q, qⁿ)` — the per-shape restriction property of the Deligne/TL
interpolated level.

The identity factors into two inputs of different kinds, and this file formalizes the
division of labor explicitly:

* **Algebraic content (proved here, sorry-free).** The q-factorial telescope
  `[n]_q! = [n−K]_q! · ∏_{i<K} [n−i]_q` (`qFactorial_telescope`, induction on `K`) and
  its division form (`qFactorial_div_telescope`, at `1 < q` where `[·]_q! ≠ 0`).
* **Combinatorial input — now PROVED in general (§HookSplit below).** The hook multiset
  of the padded shape splits as
  `hooks(μ[n]) = {1, …, n−|μ|−μ₁} ⊎ {n − c_j}_{j ≤ μ₁} ⊎ hooks(μ)` with
  `c_j = |μ| + j − 1 − leg_j(μ)` — equivalently `hookProd q (μ[n]) = [n−K]_q! · D` with
  `K = |μ| + μ₁` and `D` the fixed shifted-bracket × `H_q(μ)` factor. Originally
  probe-verified (99/99) and carried as the named hypothesis `hsplit` of
  `qdim_level_rational_of_hook_split`; the general combinatorial proof is
  `hookProd_cons_split` (prepending a first row leaves lower-row hooks unchanged —
  definitionally, `hookLength_cons_succ := rfl` — and the new row-0 hooks split at the
  column bound `B` into shifted brackets and a tail q-factorial). The unconditional
  closed form is `qDim_cons_level_rational`. To dodge ℕ-subtraction rewriting, the
  first row is parametrized as `B + t` (instantiate `t := r − B`); the shape hypothesis
  is only `∀ p ∈ μ, p ≤ B` — no sortedness of `μ` is needed.

Together: `qDim q (μ[n]) = ∏_{i<K} [n−i]_q / D` — numerator a fixed window of
`K = |μ|+μ₁` brackets sliding with the level, denominator level-independent. Each
`[n−i]_q` is Laurent in `qⁿ`, so the family is rational in `(q, qⁿ)` of degree bounded
by `K` — "polynomial in the level", the q-dimension face of Deligne interpolation
\cite{deligne2007}.

Ground ring: `ℝ`, matching the canonical `QPartitionCombinatorics` infrastructure this
file consumes (its nonvanishing lemmas live at `1 < q`); the telescope itself is
ordering-free and would state over any field — kept here to avoid duplicating the
q-bracket stack (§7c note).
-/

namespace QOU.Mass.PaddedShapeLevelRational

open QOU.MathlibExt.QPartitionCombinatorics

/-- The hook product `∏_{x ∈ λ} [h_x]_q` — the denominator fold of `qDim`, named. -/
noncomputable def hookProd (q : ℝ) (lam : Partition) : ℝ :=
  (List.range lam.length).foldl
    (fun acc i =>
      acc * (List.range ((lam.get? i).getD 0)).foldl
        (fun a j => a * qBracket q (Partition.hookLength lam i j))
        1)
    1

/-- `qDim` is definitionally the q-factorial over the named hook product. -/
theorem qDim_eq_fact_div_hookProd (q : ℝ) (lam : Partition) :
    qDim q lam = qFactorial q lam.size / hookProd q lam := rfl

/-- **q-factorial telescope**: `[n]_q! = [n−k]_q! · ∏_{i<k} [n−i]_q` for `k ≤ n`.
The algebraic heart of padded-shape level-rationality: the last `k` brackets of the
q-factorial form a fixed-size window sliding with `n`. -/
theorem qFactorial_telescope (q : ℝ) (n : ℕ) :
    ∀ k : ℕ, k ≤ n →
      qFactorial q n = qFactorial q (n - k) * ∏ i ∈ Finset.range k, qBracket q (n - i) := by
  intro k
  induction k with
  | zero => intro _; simp
  | succ k ih =>
    intro h
    have hk : k ≤ n := Nat.le_of_succ_le h
    rw [ih hk, Finset.prod_range_succ,
      show n - k = n - (k + 1) + 1 from by omega, qFactorial_succ]
    ring

/-- Division-free form of the telescope, for downstream `rw` without nonzero
hypotheses. -/
theorem qFactorial_mul_telescope (q : ℝ) (n K : ℕ) (h : K ≤ n) (D : ℝ) :
    qFactorial q n * D =
      qFactorial q (n - K) * ((∏ i ∈ Finset.range K, qBracket q (n - i)) * D) := by
  rw [qFactorial_telescope q n K h]; ring

/-- Division form at `1 < q` (where `[n−K]_q! ≠ 0`):
`[n]_q! / ([n−K]_q! · D) = ∏_{i<K} [n−i]_q / D`. -/
theorem qFactorial_div_telescope {q : ℝ} (hq : 1 < q) (n K : ℕ) (h : K ≤ n) (D : ℝ) :
    qFactorial q n / (qFactorial q (n - K) * D) =
      (∏ i ∈ Finset.range K, qBracket q (n - i)) / D := by
  rw [qFactorial_telescope q n K h,
    mul_div_mul_left _ _ (qFactorial_ne_zero hq (n - K))]

/-- **Level-rationality of the padded q-dimension** (conditional on the hook split).
If the hook product of `λ = μ[n]` splits off the tail q-factorial —
`hookProd q λ = [|λ|−K]_q! · D` with `K = |μ|+μ₁` and `D` the level-independent
shifted-bracket × `H_q(μ)` factor (the probe-verified combinatorial input, 99/99 exact
for `|μ| ≤ 4`, `n ≤ 12`) — then

  `qDim q λ = ∏_{i<K} [|λ|−i]_q / D`,

a fixed rational function of `(q, q^{|λ|})`: the per-shape Deligne/TL restriction
property. The interpolation-vs-feasibility verdict (audit §10): this per-shape
rationality is exact, while the *sum* over the growing shape set escapes it — the
stable truncation captures a collapsing fraction of `T_q(n)` at `q₀`. -/
theorem qdim_level_rational_of_hook_split {q : ℝ} (hq : 1 < q) (lam : Partition)
    (K : ℕ) (hK : K ≤ lam.size) (D : ℝ)
    (hsplit : hookProd q lam = qFactorial q (lam.size - K) * D) :
    qDim q lam = (∏ i ∈ Finset.range K, qBracket q (lam.size - i)) / D := by
  rw [qDim_eq_fact_div_hookProd, hsplit,
    qFactorial_div_telescope hq lam.size K hK D]

/-! ## HookSplit — the general combinatorial hook decomposition, proved

Discharges the `hsplit` hypothesis of `qdim_level_rational_of_hook_split` for every
padded shape `(B + t) :: μ` with all parts of `μ` bounded by `B`. Structure:

* prepending a row leaves lower-row hooks untouched (`hookLength_cons_succ`, a `rfl` —
  legs count rows *below*, and `get?`/`drop` on a cons reduce structurally);
* row-0 hooks are `(first − j − 1) + leg_j(μ) + 1` (`hookLength_cons_zero`), and the
  legs vanish beyond the column bound `B` (`legCount_eq_zero`), so columns `≥ B`
  contribute the tail q-factorial `[t]_q!` (`prod_desc_eq_qFactorial`);
* fold-to-product plumbing (`foldl_mul_eq_prod`, `hookProd_eq_prod`) converts the
  `hookProd` fold into `Finset.prod` form where the range splits
  (`Finset.prod_range_succ'`, `Finset.prod_range_add`) apply. -/

/-- Leg count of column `j` (0-indexed) in `μ`: the number of parts exceeding `j` —
exactly the `legLen` filter of `Partition.hookLength`. -/
def legCount (mu : Partition) (j : ℕ) : ℕ := (mu.filter (· > j)).length

/-- Legs vanish beyond a column bound: if every part of `μ` is `≤ B` and `B ≤ j`,
column `j` has no legs. -/
theorem legCount_eq_zero {B j : ℕ} (hj : B ≤ j) :
    ∀ mu : Partition, (∀ p ∈ mu, p ≤ B) → legCount mu j = 0 := by
  intro mu
  induction mu with
  | nil => intro _; rfl
  | cons p l ih =>
    intro hB
    have hp : ¬(p > j) := by
      have := hB p (List.mem_cons_self p l)
      omega
    simp only [legCount, List.filter_cons]
    rw [if_neg (by simpa using hp)]
    exact ih fun p' hp' => hB p' (List.mem_cons_of_mem p hp')

/-- **Prepending a first row leaves lower-row hooks unchanged** — definitionally:
`get?` and `drop` on a cons reduce structurally, and legs only count rows below. -/
theorem hookLength_cons_succ (r : ℕ) (mu : Partition) (i j : ℕ) :
    Partition.hookLength (r :: mu) (i + 1) j = Partition.hookLength mu i j := rfl

/-- Row-0 hook of the padded shape at column `j < r`:
`arm + leg + 1 = (r − j − 1) + leg_j(μ) + 1`. -/
theorem hookLength_cons_zero (r : ℕ) (mu : Partition) (j : ℕ) (hj : j < r) :
    Partition.hookLength (r :: mu) 0 j = (r - j - 1) + legCount mu j + 1 := by
  show (if j < r then (r - j - 1) + (mu.filter (· > j)).length + 1 else 0) = _
  rw [if_pos hj]
  rfl

/-- Fold-to-product bridge: the multiplicative `List.range` fold is a `Finset.prod`. -/
theorem foldl_mul_eq_prod (f : ℕ → ℝ) :
    ∀ (N : ℕ) (a : ℝ),
      (List.range N).foldl (fun acc j => acc * f j) a = a * ∏ j ∈ Finset.range N, f j := by
  intro N
  induction N with
  | zero => intro a; simp
  | succ N ih =>
    intro a
    rw [List.range_succ, List.foldl_append, ih a]
    show (a * ∏ j ∈ Finset.range N, f j) * f N = _
    rw [Finset.prod_range_succ, mul_assoc]

/-- `hookProd` in `Finset.prod` form. -/
theorem hookProd_eq_prod (q : ℝ) (lam : Partition) :
    hookProd q lam =
      ∏ i ∈ Finset.range lam.length,
        ∏ j ∈ Finset.range ((lam.get? i).getD 0),
          qBracket q (Partition.hookLength lam i j) := by
  unfold hookProd
  rw [foldl_mul_eq_prod (fun i =>
      (List.range ((lam.get? i).getD 0)).foldl
        (fun a j => a * qBracket q (Partition.hookLength lam i j)) 1) lam.length 1,
    one_mul]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [foldl_mul_eq_prod (fun j => qBracket q (Partition.hookLength lam i j))
      ((lam.get? i).getD 0) 1, one_mul]

/-- `[N]_q!` as a range product of brackets. -/
theorem qFactorial_eq_prod_range (q : ℝ) (N : ℕ) :
    qFactorial q N = ∏ j ∈ Finset.range N, qBracket q (j + 1) := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [qFactorial_succ, ih, Finset.prod_range_succ]
    ring

/-- The descending bracket product is the q-factorial:
`∏_{j<T} [T−j]_q = [T]_q!`. -/
theorem prod_desc_eq_qFactorial (q : ℝ) (T : ℕ) :
    (∏ j ∈ Finset.range T, qBracket q (T - j)) = qFactorial q T := by
  rw [qFactorial_eq_prod_range, ← Finset.prod_range_reflect]
  refine Finset.prod_congr rfl fun j hj => ?_
  have hjT : j < T := Finset.mem_range.mp hj
  congr 1
  omega

/-- **The general hook split** (the §10 probe's 99/99 fact, proved for every shape):
for `μ` with all parts `≤ B` and first row `B + t`,

  `hookProd q ((B+t) :: μ) = (∏_{j<B} [hook₀(j)]_q · [t]_q!) · hookProd q μ`,

where `hook₀(j)` is the row-0 hook. The first row is parametrized as `B + t` (rather
than `r` with `B ≤ r`) so no ℕ-subtraction rewriting is needed; no sortedness of `μ`
is assumed. -/
theorem hookProd_cons_split (q : ℝ) (mu : Partition) (B t : ℕ)
    (hB : ∀ p ∈ mu, p ≤ B) :
    hookProd q ((B + t) :: mu) =
      ((∏ j ∈ Finset.range B, qBracket q (Partition.hookLength ((B + t) :: mu) 0 j)) *
        qFactorial q t) * hookProd q mu := by
  rw [hookProd_eq_prod q ((B + t) :: mu), hookProd_eq_prod q mu,
    show ((B + t) :: mu : Partition).length = mu.length + 1 from rfl,
    Finset.prod_range_succ', mul_comm]
  congr 1
  · -- row 0: split the column range at B; the tail is the descending q-factorial
    show (∏ j ∈ Finset.range (B + t),
        qBracket q (Partition.hookLength ((B + t) :: mu) 0 j)) = _
    rw [Finset.prod_range_add]
    have h2 : (∏ k ∈ Finset.range t,
        qBracket q (Partition.hookLength ((B + t) :: mu) 0 (B + k))) = qFactorial q t := by
      rw [← prod_desc_eq_qFactorial q t]
      refine Finset.prod_congr rfl fun k hk => ?_
      have hk' : k < t := Finset.mem_range.mp hk
      rw [hookLength_cons_zero (B + t) mu (B + k) (by omega),
        legCount_eq_zero (by omega : B ≤ B + k) mu hB]
      congr 1
      omega
    rw [h2]
  · -- rows ≥ 1: hooks agree definitionally with the hooks of μ
    refine Finset.prod_congr rfl fun i _ => ?_
    rfl

/-- **Unconditional level-rationality of the padded q-dimension**: for every `μ` with
parts `≤ B` and first row `B + t` (i.e. `μ[n]` at level `n = |μ| + B + t`),

  `qDim q ((B+t) :: μ) = ∏_{i<K} [n − i]_q / D`,   `K = |μ| + B`,

with `D` the level-independent row-0-window × `hookProd μ` factor. The hook-split
hypothesis of `qdim_level_rational_of_hook_split` is discharged by
`hookProd_cons_split` — no conditional input remains. -/
theorem qDim_cons_level_rational {q : ℝ} (hq : 1 < q) (mu : Partition) (B t : ℕ)
    (hB : ∀ p ∈ mu, p ≤ B) :
    qDim q ((B + t) :: mu) =
      (∏ i ∈ Finset.range (mu.sum + B),
        qBracket q (((B + t) :: mu : Partition).size - i)) /
      ((∏ j ∈ Finset.range B, qBracket q (Partition.hookLength ((B + t) :: mu) 0 j)) *
        hookProd q mu) := by
  have hsize : ((B + t) :: mu : Partition).size = (B + t) + mu.sum := by
    simp [Partition.size]
  have hK : mu.sum + B ≤ ((B + t) :: mu : Partition).size := by
    rw [hsize]; omega
  have hsplit : hookProd q ((B + t) :: mu) =
      qFactorial q (((B + t) :: mu : Partition).size - (mu.sum + B)) *
        ((∏ j ∈ Finset.range B, qBracket q (Partition.hookLength ((B + t) :: mu) 0 j)) *
          hookProd q mu) := by
    rw [hookProd_cons_split q mu B t hB,
      show ((B + t) :: mu : Partition).size - (mu.sum + B) = t from by rw [hsize]; omega]
    ring
  exact qdim_level_rational_of_hook_split hq ((B + t) :: mu) (mu.sum + B) hK _ hsplit

end QOU.Mass.PaddedShapeLevelRational
