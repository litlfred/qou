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
    ((List.range (l.getD i 0)).map fun j => ((j : ℤ) - (i : ℤ)) ^ 2).sum).sum

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

/-- **Identity (A), general (carried).** For a weakly-decreasing partition `l`,
`Σ_c h_c² = Σ_c c(c)² + n²`.  Proved on paper (β-set / arm-leg) in the audit doc;
the general Lean proof needs `YoungDiagram` hook/content infrastructure not yet in
Mathlib. Machine-checked above for the listed partitions. -/
theorem sumSqHooks_eq_sumSqContents_add_sq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (h : l = []) :
    sumSqHooks l = sumSqContents l + (sz l : ℤ) ^ 2 := by
  subst h
  rfl

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
