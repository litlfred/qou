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

/-- **Identity (A), general (carried — residual is six finite, formula-free facts).**
For a weakly-decreasing partition `l`, `Σ_c h_c² = Σ_c c(c)² + n²`.

The reduction above (`identityA_algebra`) proves this **sorry-free from the six finite
sub-identities** (E)/(Arm)/(Cont)/(Leg1)/(Leg2)/(Cross); the **hook-length formula is
off the critical path** (audit `2026-06-24-keystone-identity-I-armleg-reduction.md`).
The remaining Lean fill is those six identities about the `List ℕ` defs above —
elementary `BigOperators` sums (E/Arm/Cont) plus the `colLen` conjugate column-sums
(Leg1/Leg2) and the sorted L-triple count (Cross).  Machine-checked here for every
partition through `n = 12` (`identityA_exhaustive_n12`) and in exact integer arithmetic
for `n ≤ 22` (audit). -/
theorem sumSqHooks_eq_sumSqContents_add_sq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqHooks l = sumSqContents l + (sz l : ℤ) ^ 2 := by
  -- Ref: [manuscript] docs/audits/2026-06-24-keystone-identity-I-armleg-reduction.md
  -- Proof = `identityA_algebra` applied to the six reduction lemmas (E)/(Arm)/(Cont)/
  -- (Leg1)/(Leg2)/(Cross) about the `List ℕ` defs; those finite-combinatorics lemmas
  -- are the residual fill (no hook-length formula). Exhaustively verified `n ≤ 12`.
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
