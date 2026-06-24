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
  `List ℕ`) and **machine-checked on representative partitions** (`native_decide`);
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

/-- `Σ_{cells} c(c)²` with content `c(i,j) = j − i`. -/
def sumSqContents (l : List ℕ) : ℤ :=
  ((List.range l.length).map fun i =>
    ((List.range (l.getD i 0)).map fun (j : ℕ) => ((j : ℤ) - (i : ℤ)) ^ 2).sum).sum

/-- Size `n = Σ λ_i`. -/
def sz (l : List ℕ) : ℕ := l.sum

/-! ### (A) machine-checked instances (sorry-free)

`Σ_c h_c² = Σ_c c(c)² + n²` for representative partitions across `n = 1..8`,
including the self-conjugate `[3,1,1]` (electron block) and a two-row and a
three-row case.  These are genuine kernel/native computations, not stubs. -/

example : sumSqHooks [1] = sumSqContents [1] + (sz [1] : ℤ) ^ 2 := by native_decide
example : sumSqHooks [2] = sumSqContents [2] + (sz [2] : ℤ) ^ 2 := by native_decide
example : sumSqHooks [1, 1] = sumSqContents [1, 1] + (sz [1, 1] : ℤ) ^ 2 := by native_decide
example : sumSqHooks [2, 1] = sumSqContents [2, 1] + (sz [2, 1] : ℤ) ^ 2 := by native_decide
example : sumSqHooks [3, 1, 1] = sumSqContents [3, 1, 1] + (sz [3, 1, 1] : ℤ) ^ 2 := by
  native_decide
example : sumSqHooks [3, 2] = sumSqContents [3, 2] + (sz [3, 2] : ℤ) ^ 2 := by native_decide
example : sumSqHooks [4, 2, 1] = sumSqContents [4, 2, 1] + (sz [4, 2, 1] : ℤ) ^ 2 := by
  native_decide
example : sumSqHooks [3, 3, 2] = sumSqContents [3, 3, 2] + (sz [3, 3, 2] : ℤ) ^ 2 := by
  native_decide

/-! ### (A) exhaustive check — *every* partition through `n = 12` (sorry-free)

Rather than rely on hand-picked partitions, enumerate **all** partitions and check
(A) on each.  `partAux cap n` lists the partitions of `n` with every part `≤ cap`
(weakly decreasing); `partitions n = partAux n n`.  `partitionCounts` proves the
enumerator is *complete* (`p(n) = 1,2,3,5,7,11,15,22,30,42,56,77` for `n = 1..12`),
and `identityA_exhaustive_n12` checks `Σh² = Σc² + n²` on every one of the 271
partitions through `n = 12` — dodge-proof (no tabulated results; hooks/contents are
computed from the partition structure). -/

/-- Partitions of `n` with each part `≤ cap`, as weakly-decreasing `List ℕ`. -/
def partAux : ℕ → ℕ → List (List ℕ)
  | _, 0 => [[]]
  | 0, _ + 1 => []
  | cap + 1, n + 1 =>
    (if cap + 1 ≤ n + 1 then (partAux (cap + 1) (n + 1 - (cap + 1))).map ((cap + 1) :: ·)
      else []) ++ partAux cap (n + 1)
  termination_by cap n => (n, cap)
  decreasing_by · simp_wf; omega
                · simp_wf; omega

/-- All partitions of `n`. -/
def partitions (n : ℕ) : List (List ℕ) := partAux n n

/-- **Enumerator completeness.** `|partitions n| = p(n)` for `n = 1..12`. -/
theorem partitionCounts :
    (List.range' 1 12).map (fun n => (partitions n).length)
      = [1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77] := by native_decide

/-- **Identity (A), exhaustive.** `Σ_c h_c² = Σ_c c(c)² + n²` for **every** partition
through `n = 12` (271 partitions).  Hooks and contents are computed from the partition
structure, not tabulated. -/
theorem identityA_exhaustive_n12 :
    ((List.range' 1 12).all fun n =>
      (partitions n).all fun l =>
        decide (sumSqHooks l = sumSqContents l + (sz l : ℤ) ^ 2)) = true := by
  native_decide

/-! ### (A) algebraic core — `Σh² = Σc² + n²` from six finite reduction identities

The per-partition (A) reduces, **without the Frame–Robinson–Thrall hook-length
formula**, to a pure ℤ combination of six finite sub-identities (full derivation:
`docs/audits/2026-06-24-keystone-identity-I-armleg-reduction.md`).  With totals
`a1,a2 = Σarm, Σarm²`; `l1,l2 = Σleg, Σleg²`; `al = Σarm·leg`; `c2,h2 = Σc², Σh²`;
and row data `n = Σλ_i`, `p2 = Σλ_i²`, `q1 = Σ i·λ_i`, `q2 = Σ i²·λ_i`,
`s2 = Σ i·λ_i²`:

* **(E)**   `h2 = a2 + l2 + n + 2·al + 2·a1 + 2·l1`  (per-cell `h=a+ℓ+1` square expansion);
* **(Arm)** `2·a1 = p2 − n`                          (`Σ_c a = Σ_i binom(λ_i,2)`);
* **(Cont)** `c2 = a2 − s2 + q1 + q2`                (`Σ_{j<λ_i}(j−i)²` per row);
* **(Leg1)** `l1 = q1`,  **(Leg2)** `l2 = q2`        (conjugate column-sums of `colLen`);
* **(Cross)** `2·al = n² − p2 − s2 − q1`             (sorted L-triple count — uses `λ_i ≥ λ_{i'}`).

The collapse is `linarith`; the result is **sorry-free** and **non-vacuous** (the
hypotheses are genuine intermediate sums, not the conclusion — AGENTS.md §1a). -/
theorem identityA_algebra
    (n p2 q1 q2 s2 a1 a2 l1 l2 al c2 h2 : ℤ)
    (hHook  : h2 = a2 + l2 + n + 2 * al + 2 * a1 + 2 * l1)
    (hArm   : 2 * a1 = p2 - n)
    (hCont  : c2 = a2 - s2 + q1 + q2)
    (hLeg1  : l1 = q1)
    (hLeg2  : l2 = q2)
    (hCross : 2 * al = n ^ 2 - p2 - s2 - q1) :
    h2 = c2 + n ^ 2 := by
  subst hLeg1; subst hLeg2; linarith

/-! ### Foundational lemma for the residual fill (lemma 1 of 6, sorry-free)

The six reduction lemmas (E)/(Leg1)/(Leg2)/(Cross) all hinge on the fact that, for a
weakly-decreasing `l`, a **genuine cell** `(i,j)` (`i < len`, `j < λ_i`) has
`i < colLen l j` — i.e. the leg `colLen_j − 1 − i ≥ 0`, so the `ℕ`-subtraction in the
hook def is exact and `hook = arm + leg + 1`.  The rows with part `> j` form a prefix
(sortedness), so the first `i+1` rows all qualify. -/

/-- For a weakly-decreasing `l`, every genuine cell `(i,j)` satisfies `i < colLen l j`. -/
theorem lt_colLen_of_cell (l : List ℕ) (hl : l.Sorted (· ≥ ·)) {i j : ℕ}
    (hi : i < l.length) (hj : j < l.getD i 0) : i < colLen l j := by
  have hmem : ∀ x ∈ l.take (i + 1), j < x := by
    intro x hx
    rw [List.mem_iff_getElem] at hx
    obtain ⟨k, hk, rfl⟩ := hx
    rw [List.length_take] at hk
    have hkl : k < l.length := by omega
    rw [List.getElem_take]
    have hgi : l.getD i 0 = l[i] := by
      rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi]; rfl
    rcases Nat.lt_or_ge k i with hki | hki
    · have := (List.pairwise_iff_getElem.mp hl) k i hkl hi hki
      simp only [ge_iff_le] at this; omega
    · have hke : k = i := by omega
      subst hke; omega
  have hfilt : (l.take (i + 1)).filter (fun p => j < p) = l.take (i + 1) :=
    List.filter_eq_self.mpr (by intro a ha; simpa using hmem a ha)
  have hsub : List.Sublist ((l.take (i + 1)).filter (fun p => j < p))
      (l.filter (fun p => j < p)) := (List.take_sublist _ _).filter _
  have hlen : (l.take (i + 1)).length ≤ colLen l j := by
    have h := hsub.length_le; rwa [hfilt] at h
  rw [List.length_take] at hlen; omega

/-- **Per-cell hook cast (sorry-free).** For a genuine cell of a weakly-decreasing
partition the `ℕ` hook `(λ_i − j) + (colLen_j − i) − 1` equals `arm + leg + 1` over ℤ,
with `arm = λ_i − 1 − j ≥ 0` and `leg = colLen_j − 1 − i ≥ 0` (the latter by
`lt_colLen_of_cell`). This makes the `ℕ`-subtraction exact. -/
theorem hook_cast (l : List ℕ) (hl : l.Sorted (· ≥ ·)) {i j : ℕ}
    (hi : i < l.length) (hj : j < l.getD i 0) :
    (((l.getD i 0 - j) + (colLen l j - i) - 1 : ℕ) : ℤ)
      = ((l.getD i 0 : ℤ) - 1 - j) + ((colLen l j : ℤ) - 1 - i) + 1 := by
  have h2 : i < colLen l j := lt_colLen_of_cell l hl hi hj
  omega

/-- **Hook-square expansion, step 1 (sorry-free).** Rewrite `sumSqHooks` cell-by-cell
into the `(arm + leg + 1)²` form — the payoff of `lt_colLen_of_cell`/`hook_cast`. This
is the entry point to the reduction lemma (E): expanding the square and splitting the
double sum yields `a2 + l2 + n + 2·al + 2·a1 + 2·l1`. -/
theorem sumSqHooks_armleg (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqHooks l = ((List.range l.length).map fun i =>
      ((List.range (l.getD i 0)).map fun j =>
        (((l.getD i 0 : ℤ) - 1 - j) + ((colLen l j : ℤ) - 1 - i) + 1) ^ 2).sum).sum := by
  unfold sumSqHooks
  refine congrArg List.sum (List.map_congr_left ?_)
  intro i hi; rw [List.mem_range] at hi
  refine congrArg List.sum (List.map_congr_left ?_)
  intro j hj; rw [List.mem_range] at hj
  rw [hook_cast l hl hi hj]

/-! ### Young-diagram cell-sum framework + reduction lemma (E) (sorry-free)

To do the arm/leg algebra cleanly, move the nested `List` sums to `Finset` double
sums (`cellSum`).  Linearity (`cellSum_add`, `cellSum_const_mul`) then splits the
expanded hook square into the six cell-sums of reduction lemma **(E)** (`hookE`). -/

/-- list-map-sum over `List.range` = `Finset.range` sum. -/
theorem list_sum_range (n : ℕ) (f : ℕ → ℤ) :
    ((List.range n).map f).sum = ∑ i ∈ Finset.range n, f i := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.map_append, List.sum_append, Finset.sum_range_succ, ih]; simp

/-- Young-diagram cell sum `∑_{i<len} ∑_{j<λ_i} f i j`. -/
def cellSum (l : List ℕ) (f : ℕ → ℕ → ℤ) : ℤ :=
  ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), f i j

theorem cellSum_add (l) (f g : ℕ → ℕ → ℤ) :
    cellSum l (fun i j => f i j + g i j) = cellSum l f + cellSum l g := by
  unfold cellSum
  rw [← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl (fun i _ => by rw [← Finset.sum_add_distrib])

theorem cellSum_const_mul (l) (c : ℤ) (f : ℕ → ℕ → ℤ) :
    cellSum l (fun i j => c * f i j) = c * cellSum l f := by
  unfold cellSum
  rw [Finset.mul_sum]
  exact Finset.sum_congr rfl (fun i _ => by rw [Finset.mul_sum])

theorem cellSum_congr (l) (f g : ℕ → ℕ → ℤ) (h : ∀ i ∈ Finset.range l.length,
    ∀ j ∈ Finset.range (l.getD i 0), f i j = g i j) : cellSum l f = cellSum l g := by
  unfold cellSum
  exact Finset.sum_congr rfl (fun i hi => Finset.sum_congr rfl (fun j hj => h i hi j hj))

/-- General nested list→Finset bridge for a Young-diagram double sum. -/
theorem nested_bridge (l : List ℕ) (g : ℕ → ℕ → ℤ) :
    ((List.range l.length).map fun i =>
      ((List.range (l.getD i 0)).map (fun j => g i j)).sum).sum = cellSum l g := by
  unfold cellSum
  rw [list_sum_range]
  exact Finset.sum_congr rfl (fun i _ => list_sum_range _ (g i))

theorem sumSqContents_cellSum (l : List ℕ) :
    sumSqContents l = cellSum l (fun i j => ((j : ℤ) - (i : ℤ)) ^ 2) := by
  unfold sumSqContents; exact nested_bridge l _

/-- Number of cells `= sz l`. -/
theorem cellSum_one (l : List ℕ) : cellSum l (fun _ _ => 1) = (sz l : ℤ) := by
  unfold cellSum sz
  simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_one]
  induction l with
  | nil => simp
  | cons a t ih =>
    rw [List.length_cons, Finset.sum_range_succ']
    simp only [List.getD_cons_succ]
    rw [ih]
    simp only [List.getD_cons_zero, List.sum_cons, Nat.cast_add]; ring

/-- Six-term square expansion of `cellSum (A+B+1)²` by linearity. -/
theorem cellSum_expand (l : List ℕ) (A B : ℕ → ℕ → ℤ) :
    cellSum l (fun i j => (A i j + B i j + 1) ^ 2)
      = cellSum l (fun i j => A i j ^ 2) + cellSum l (fun i j => B i j ^ 2)
        + cellSum l (fun _ _ => 1) + 2 * cellSum l (fun i j => A i j * B i j)
        + 2 * cellSum l A + 2 * cellSum l B := by
  rw [cellSum_congr l (fun i j => (A i j + B i j + 1) ^ 2)
      (fun i j => A i j ^ 2 + B i j ^ 2 + 1 + 2 * (A i j * B i j) + 2 * A i j + 2 * B i j)
      (by intro i _ j _; ring)]
  rw [cellSum_add, cellSum_add, cellSum_add, cellSum_add, cellSum_add,
      cellSum_const_mul, cellSum_const_mul, cellSum_const_mul]

theorem sumSqHooks_cellSum (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqHooks l = cellSum l (fun i j =>
      (((l.getD i 0 : ℤ) - 1 - j) + ((colLen l j : ℤ) - 1 - i) + 1) ^ 2) := by
  rw [sumSqHooks_armleg l hl]; exact nested_bridge l _

/-- **Reduction lemma (E) (sorry-free).** The hook-square expansion: `sumSqHooks`
equals `a2 + l2 + n + 2·al + 2·a1 + 2·l1` (matching `identityA_algebra`'s `hHook`),
with `arm = λ_i−1−j`, `leg = colLen_j−1−i`, and the constant cell-sum `= sz l`. -/
theorem hookE (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqHooks l
      = cellSum l (fun i j => ((l.getD i 0 : ℤ) - 1 - j) ^ 2)
        + cellSum l (fun i j => ((colLen l j : ℤ) - 1 - i) ^ 2)
        + cellSum l (fun _ _ => 1)
        + 2 * cellSum l (fun i j => ((l.getD i 0 : ℤ) - 1 - j) * ((colLen l j : ℤ) - 1 - i))
        + 2 * cellSum l (fun i j => (l.getD i 0 : ℤ) - 1 - j)
        + 2 * cellSum l (fun i j => (colLen l j : ℤ) - 1 - i) := by
  rw [sumSqHooks_cellSum l hl]
  exact cellSum_expand l (fun i j => (l.getD i 0 : ℤ) - 1 - j)
    (fun i j => (colLen l j : ℤ) - 1 - i)

/-! ### Young-diagram Fubini swap (sum over cells = sum over columns) (sorry-free)

The leg/cross reduction lemmas all need the *sum-over-cells → sum-over-columns*
reorganization.  `cellSum_swap` provides it once: for sorted `l`, cell `(i,j)` lies in
the diagram (`i < len ∧ j < λ_i`) iff `j < sz l ∧ i < colLen_j`, so `Finset.sum_comm'`
flips the order.  Both membership directions use sortedness: `λ_i ≤ j ⇒ colLen_j ≤ i`
(`colLen_le_of_le`) and its contrapositive `i < colLen_j ⇒ j < λ_i`. -/

/-- Converse cell bound: for sorted `l`, `λ_i ≤ j ⇒ colLen_j ≤ i`. -/
theorem colLen_le_of_le (l : List ℕ) (hl : l.Sorted (· ≥ ·)) {i j : ℕ}
    (h : l.getD i 0 ≤ j) : colLen l j ≤ i := by
  have hdrop : ∀ a ∈ l.drop i, ¬ (j < a) := by
    intro a ha
    rw [List.mem_iff_getElem] at ha
    obtain ⟨k, hk, rfl⟩ := ha
    rw [List.length_drop] at hk
    have hidx : i < l.length := by omega
    rw [List.getElem_drop]
    have hil : l.getD i 0 = l[i] := by
      rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hidx]; rfl
    have hle : l[i + k] ≤ l[i] := by
      rcases Nat.eq_or_lt_of_le (Nat.le_add_right i k) with he | hlt
      · have hk0 : k = 0 := by omega
        subst hk0; simp
      · have := (List.pairwise_iff_getElem.mp hl) i (i + k) hidx (by omega) hlt
        simpa using this
    omega
  have hfilt : (l.drop i).filter (fun p => j < p) = [] :=
    List.filter_eq_nil_iff.mpr (by simpa using hdrop)
  have hsplit : l.filter (fun p => j < p) = (l.take i).filter (fun p => j < p) := by
    conv_lhs => rw [← List.take_append_drop i l]
    rw [List.filter_append, hfilt, List.append_nil]
  unfold colLen
  rw [hsplit]
  calc ((l.take i).filter (fun p => j < p)).length
      ≤ (l.take i).length := List.length_filter_le _ _
    _ ≤ i := by rw [List.length_take]; omega

/-- Converse of `lt_colLen_of_cell`: for sorted `l`, `i < colLen_j ⇒ j < λ_i`. -/
theorem lt_part_of_lt_colLen (l : List ℕ) (hl : l.Sorted (· ≥ ·)) {i j : ℕ}
    (h : i < colLen l j) : j < l.getD i 0 := by
  by_contra hc
  push_neg at hc
  exact absurd (colLen_le_of_le l hl hc) (by omega)

/-- **Young-diagram Fubini (sorry-free).** Sum over cells (rows then columns) equals
sum over columns then rows; column index bounded by `sz l ≥ max part`, row index by
`colLen_j`. -/
theorem cellSum_swap (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (F : ℕ → ℕ → ℤ) :
    cellSum l F = ∑ j ∈ Finset.range (sz l), ∑ i ∈ Finset.range (colLen l j), F i j := by
  unfold cellSum
  refine Finset.sum_comm' ?_
  intro i j
  simp only [Finset.mem_range]
  constructor
  · rintro ⟨hi, hj⟩
    refine ⟨lt_colLen_of_cell l hl hi hj, ?_⟩
    have hpart : l.getD i 0 ≤ sz l := by
      unfold sz
      have : l.getD i 0 = l[i] := by
        rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi]; rfl
      rw [this]
      exact List.single_le_sum (by intro x _; exact Nat.zero_le x) _ (List.getElem_mem hi)
    omega
  · rintro ⟨hcol, hsz⟩
    have hpart := lt_part_of_lt_colLen l hl hcol
    have hcl : colLen l j ≤ l.length := List.length_filter_le _ _
    exact ⟨by omega, hpart⟩

/-! ### Row-data sums + the remaining reduction lemmas

`p2 = Σλ_i²`, `q1 = Σ i·λ_i`, `q2 = Σ i²·λ_i`, `s2 = Σ i·λ_i²` (row data).  (Arm)/(Cont)
are proved sorry-free below (single-row Gauss sums via `two_sum_id`/`rowArm`/
`rowSq_reflect`/`sz_eq`).  (Leg1)/(Leg2)/(Cross) — the `colLen` conjugate column-sums
and the sorted L-triple count — are the genuine residual double-counts, carried with
`sorry` + `-- Ref:` (machine-checked for the assembled identity through `n = 12` by
`identityA_exhaustive_n12`; exact-integer `n ≤ 22` in the audit). -/

noncomputable def p2 (l : List ℕ) : ℤ := ∑ i ∈ Finset.range l.length, (l.getD i 0 : ℤ) ^ 2
noncomputable def q1 (l : List ℕ) : ℤ := ∑ i ∈ Finset.range l.length, (i : ℤ) * (l.getD i 0)
noncomputable def q2 (l : List ℕ) : ℤ := ∑ i ∈ Finset.range l.length, (i : ℤ) ^ 2 * (l.getD i 0)
noncomputable def s2 (l : List ℕ) : ℤ := ∑ i ∈ Finset.range l.length, (i : ℤ) * (l.getD i 0) ^ 2

theorem two_sum_id (m : ℕ) : 2 * ∑ j ∈ Finset.range m, (j : ℤ) = (m : ℤ) * ((m : ℤ) - 1) := by
  induction m with
  | zero => simp
  | succ k ih => rw [Finset.sum_range_succ, mul_add, ih]; push_cast; ring

theorem rowArm (m : ℕ) :
    2 * ∑ j ∈ Finset.range m, ((m : ℤ) - 1 - (j : ℤ)) = (m : ℤ) ^ 2 - m := by
  have key : ∀ j ∈ Finset.range m, (m : ℤ) - 1 - (j : ℤ) = ((m - 1 - j : ℕ) : ℤ) := by
    intro j hj; rw [Finset.mem_range] at hj; omega
  rw [Finset.sum_congr rfl key, Finset.sum_range_reflect (fun k => (k : ℤ)) m, two_sum_id]; ring

theorem rowSq_reflect (m : ℕ) :
    ∑ j ∈ Finset.range m, ((m : ℤ) - 1 - (j : ℤ)) ^ 2 = ∑ j ∈ Finset.range m, (j : ℤ) ^ 2 := by
  have key : ∀ j ∈ Finset.range m, ((m : ℤ) - 1 - (j : ℤ)) ^ 2 = ((m - 1 - j : ℕ) : ℤ) ^ 2 := by
    intro j hj; rw [Finset.mem_range] at hj
    have : (m : ℤ) - 1 - (j : ℤ) = ((m - 1 - j : ℕ) : ℤ) := by omega
    rw [this]
  rw [Finset.sum_congr rfl key, Finset.sum_range_reflect (fun k => (k : ℤ) ^ 2) m]

theorem sz_eq (l : List ℕ) : (sz l : ℤ) = ∑ i ∈ Finset.range l.length, (l.getD i 0 : ℤ) := by
  unfold sz
  induction l with
  | nil => simp
  | cons a t ih =>
    rw [List.length_cons, Finset.sum_range_succ', List.sum_cons]
    simp only [List.getD_cons_succ, List.getD_cons_zero]
    push_cast [ih]; ring

/-- **Reduction lemma (Arm) (sorry-free).** `2·Σ arm = Σλ_i² − n`. -/
theorem redArm (l : List ℕ) :
    2 * cellSum l (fun i j => (l.getD i 0 : ℤ) - 1 - j) = p2 l - (sz l : ℤ) := by
  unfold cellSum p2
  rw [sz_eq l, Finset.mul_sum, ← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl (fun i _ => by rw [rowArm (l.getD i 0)])

/-- **Reduction lemma (Cont) (sorry-free).** `Σ c² = Σ arm² − s2 + q1 + q2`. -/
theorem redCont (l : List ℕ) :
    sumSqContents l
      = cellSum l (fun i j => ((l.getD i 0 : ℤ) - 1 - j) ^ 2) - s2 l + q1 l + q2 l := by
  rw [sumSqContents_cellSum]
  unfold cellSum s2 q1 q2
  rw [← Finset.sum_sub_distrib, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  rw [rowSq_reflect (l.getD i 0)]
  have hsplit : ∀ M : ℕ, ∑ j ∈ Finset.range M, ((j : ℤ) - (i : ℤ)) ^ 2
      = (∑ j ∈ Finset.range M, (j : ℤ) ^ 2) - 2 * (i : ℤ) * (∑ j ∈ Finset.range M, (j : ℤ))
        + (M : ℤ) * (i : ℤ) ^ 2 := by
    intro M; induction M with
    | zero => simp
    | succ k ih =>
      rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_succ, ih]; push_cast; ring
  rw [hsplit (l.getD i 0)]
  nlinarith [two_sum_id (l.getD i 0)]

/-- Linear reflect: `Σ_{i<m}(m−1−i) = Σ_{i<m} i`. -/
theorem rowReflect_lin (m : ℕ) :
    ∑ i ∈ Finset.range m, ((m : ℤ) - 1 - (i : ℤ)) = ∑ i ∈ Finset.range m, (i : ℤ) := by
  have key : ∀ i ∈ Finset.range m, (m : ℤ) - 1 - (i : ℤ) = ((m - 1 - i : ℕ) : ℤ) := by
    intro i hi; rw [Finset.mem_range] at hi; omega
  rw [Finset.sum_congr rfl key, Finset.sum_range_reflect (fun k => (k : ℤ)) m]

/-- `cellSum (fun i _ => i) = q1` (inner column-constant sum). -/
theorem cellSum_i_eq_q1 (l : List ℕ) : cellSum l (fun i _ => (i : ℤ)) = q1 l := by
  unfold cellSum q1
  exact Finset.sum_congr rfl
    (fun i _ => by rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]; ring)

/-- `cellSum (fun i _ => i²) = q2`. -/
theorem cellSum_isq_eq_q2 (l : List ℕ) : cellSum l (fun i _ => (i : ℤ) ^ 2) = q2 l := by
  unfold cellSum q2
  exact Finset.sum_congr rfl
    (fun i _ => by rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]; ring)

/-- **Reduction lemma (Leg1) (sorry-free).** `Σ leg = Σ i·λ_i`.  Proof: swap to columns
(`cellSum_swap`), reflect each inner column sum (`Σ(colLen_j−1−i)=Σ i`), then swap back
to `cellSum (fun i _ => i) = q1` — no pair double-count needed. -/
theorem redLeg1 (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    cellSum l (fun i j => (colLen l j : ℤ) - 1 - i) = q1 l := by
  rw [cellSum_swap l hl, Finset.sum_congr rfl (fun j _ => rowReflect_lin (colLen l j)),
    ← cellSum_swap l hl (fun i _ => (i : ℤ)), cellSum_i_eq_q1]

/-- **Reduction lemma (Leg2) (sorry-free).** `Σ leg² = Σ i²·λ_i` (swap → `rowSq_reflect`
→ swap back to `cellSum (fun i _ => i²) = q2`). -/
theorem redLeg2 (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    cellSum l (fun i j => ((colLen l j : ℤ) - 1 - i) ^ 2) = q2 l := by
  rw [cellSum_swap l hl, Finset.sum_congr rfl (fun j _ => rowSq_reflect (colLen l j)),
    ← cellSum_swap l hl (fun i _ => (i : ℤ) ^ 2), cellSum_isq_eq_q2]

/-- Square of a sum, prefix-sum form: `(Σ a)² = Σ a² + 2·Σ_{i'} a_{i'}·(Σ_{i<i'} a_i)`. -/
theorem sq_sum_split (n : ℕ) (a : ℕ → ℤ) :
    (∑ i ∈ Finset.range n, a i) ^ 2
      = ∑ i ∈ Finset.range n, (a i) ^ 2
        + 2 * ∑ i' ∈ Finset.range n, (a i' * ∑ i ∈ Finset.range i', a i) := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_succ]
    linear_combination ih

/-- Abel / triangular reorganization: `Σ_{i'<m} Σ_{i<i'} a_i = Σ_{i<m} a_i·(m−1−i)`. -/
theorem abel_tri (m : ℕ) (a : ℕ → ℤ) :
    ∑ i' ∈ Finset.range m, ∑ i ∈ Finset.range i', a i
      = ∑ i ∈ Finset.range m, a i * ((m : ℤ) - 1 - (i : ℤ)) := by
  rw [Finset.sum_comm' (t' := Finset.range m) (s' := fun i => Finset.Ioo i m)
      (fun i' i => by simp only [Finset.mem_range, Finset.mem_Ioo]; omega)]
  apply Finset.sum_congr rfl
  intro i hi; rw [Finset.mem_range] at hi
  rw [Finset.sum_const, Nat.card_Ioo, nsmul_eq_mul]
  have : ((m - i - 1 : ℕ) : ℤ) = (m : ℤ) - 1 - (i : ℤ) := by omega
  rw [this]; ring

/-- **Reduction lemma (Cross) (sorry-free).** `2·Σ arm·leg = n² − p2 − s2 − q1` — the
sorted cross-term.  Unlike the legs (which reflect away), this is a genuine pair count.
Proof: `cellSum_swap` to columns, the Abel identity `abel_tri` (`Σ aᵢ(m−1−i) =
Σ_{i'}Σ_{i<i'} aᵢ`) on each column, swap **back** to a `cellSum` whose summand is the
prefix sum `Σ_{i<i'}(λ_i−1−j)`; the per-row Gauss collapse (`two_sum_id`) then leaves
`2·Σ λ_{i'}·(Σ_{i<i'}λ_i) − q1 − s2`, and the square-of-sum identity `sq_sum_split`
(with `sz_eq`) gives `2·Σ λ·prefix = n² − p2`. -/
theorem redCross (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    2 * cellSum l (fun i j => ((l.getD i 0 : ℤ) - 1 - j) * ((colLen l j : ℤ) - 1 - i))
      = (sz l : ℤ) ^ 2 - p2 l - s2 l - q1 l := by
  -- Ref: [manuscript] docs/audits/2026-06-24-keystone-identity-I-armleg-reduction.md §(Cross)
  have hA : cellSum l (fun i j => ((l.getD i 0 : ℤ) - 1 - j) * ((colLen l j : ℤ) - 1 - i))
      = cellSum l (fun i' j => ∑ i ∈ Finset.range i', ((l.getD i 0 : ℤ) - 1 - (j : ℤ))) := by
    rw [cellSum_swap l hl]
    rw [Finset.sum_congr rfl
      (fun j _ => (abel_tri (colLen l j) (fun i => (l.getD i 0 : ℤ) - 1 - (j : ℤ))).symm)]
    rw [← cellSum_swap l hl (fun i' j => ∑ i ∈ Finset.range i', ((l.getD i 0 : ℤ) - 1 - (j : ℤ)))]
  rw [hA]
  unfold cellSum
  have key : ∀ i' ∈ Finset.range l.length,
      (2 : ℤ) * ∑ j ∈ Finset.range (l.getD i' 0), ∑ i ∈ Finset.range i',
          ((l.getD i 0 : ℤ) - 1 - (j : ℤ))
        = 2 * (l.getD i' 0 : ℤ) * (∑ i ∈ Finset.range i', (l.getD i 0 : ℤ))
          - (i' : ℤ) * (l.getD i' 0 : ℤ) - (i' : ℤ) * (l.getD i' 0 : ℤ) ^ 2 := by
    intro i' _
    rw [Finset.sum_comm]
    have hin : ∀ i, ∑ j ∈ Finset.range (l.getD i' 0), ((l.getD i 0 : ℤ) - 1 - (j : ℤ))
        = (l.getD i' 0 : ℤ) * ((l.getD i 0 : ℤ) - 1)
          - ∑ j ∈ Finset.range (l.getD i' 0), (j : ℤ) := by
      intro i
      rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    rw [Finset.sum_congr rfl (fun i _ => hin i)]
    rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul, ← Finset.mul_sum,
      Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    have h2s := two_sum_id (l.getD i' 0)
    linear_combination (-(i' : ℤ)) * h2s
  rw [Finset.mul_sum, Finset.sum_congr rfl key]
  rw [Finset.sum_sub_distrib, Finset.sum_sub_distrib]
  have hfac : (∑ x ∈ Finset.range l.length,
        2 * (l.getD x 0 : ℤ) * ∑ i ∈ Finset.range x, (l.getD i 0 : ℤ))
      = 2 * ∑ x ∈ Finset.range l.length,
          ((l.getD x 0 : ℤ) * ∑ i ∈ Finset.range x, (l.getD i 0 : ℤ)) := by
    rw [Finset.mul_sum]; exact Finset.sum_congr rfl (fun x _ => by ring)
  rw [hfac]
  have hsq := sq_sum_split l.length (fun i => (l.getD i 0 : ℤ))
  rw [← sz_eq l] at hsq
  unfold p2 s2 q1
  linear_combination -hsq

/-- **Identity (A), general — fully proved, sorry-free.** For a weakly-decreasing
partition `l`, `Σ_c h_c² = Σ_c c(c)² + n²`.  Proved by `identityA_algebra` from the six
reduction lemmas (E) `hookE`, (Arm) `redArm`, (Cont) `redCont`, (Leg1) `redLeg1`,
(Leg2) `redLeg2`, (Cross) `redCross` — **all sorry-free**, resting only on the
Young-diagram Fubini `cellSum_swap`, the Abel identity `abel_tri`, the square-of-sum
`sq_sum_split`, and elementary Gauss sums.  The **Frame–Robinson–Thrall hook-length
formula is off the critical path entirely** (audit
`2026-06-24-keystone-identity-I-armleg-reduction.md`); independently machine-checked for
every partition through `n = 12` (`identityA_exhaustive_n12`), exact-integer `n ≤ 22`. -/
theorem sumSqHooks_eq_sumSqContents_add_sq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqHooks l = sumSqContents l + (sz l : ℤ) ^ 2 :=
  identityA_algebra (sz l : ℤ) (p2 l) (q1 l) (q2 l) (s2 l)
    (cellSum l (fun i j => (l.getD i 0 : ℤ) - 1 - j))
    (cellSum l (fun i j => ((l.getD i 0 : ℤ) - 1 - j) ^ 2))
    (cellSum l (fun i j => (colLen l j : ℤ) - 1 - i))
    (cellSum l (fun i j => ((colLen l j : ℤ) - 1 - i) ^ 2))
    (cellSum l (fun i j => ((l.getD i 0 : ℤ) - 1 - j) * ((colLen l j : ℤ) - 1 - i)))
    (sumSqContents l) (sumSqHooks l)
    (by rw [hookE l hl, cellSum_one]) (redArm l) (redCont l) (redLeg1 l hl) (redLeg2 l hl)
    (redCross l hl)

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
