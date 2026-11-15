import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.BraidsAndKnots.CombinerBranchingCompleteness
  — the operator-valued combiner reaches every Wedderburn block

The operator-valued combiner (`a_operator_recursive.py :: interface_blocks`,
narrative `hecke-branching-trace-decomposition.md`) decomposes a per-block
character along `H_{n_inner}(q) ⊗ H_{n_block}(q) ↪ H_n(q)`:

      χ^λ(β₁ · I · β₂) = Σ_{ξ⊢n_inner, ν⊢n_block} c^λ_{ξν} · Tr(A^λ_{ξν}(I) · …).

The **per-λ** completeness (the sum captures all of `Res(V_λ)`) is already
established in the corpus: the trace is the sum over the orthogonal `(ξ,ν)`-
isotypic components, and `H_n(q) ≅ ⊕_{λ⊢n} End(V_λ)` (Wenzl 1988;
`QOU/Hecke/Wedderburn.lean`).

This file formalizes the **dual** guarantee — that the enumeration is
**non-degenerate**: `interface_blocks` returns at least one child for *every*
`λ ⊢ n`, so the production trace `tr_M = Σ_λ y_λ χ^λ` drops no block.  By
Frobenius reciprocity `V_λ ⊆ Ind(V_ξ ⊠ V_ν) ⟺ c^λ_{ξν} > 0`, and any skew shape
admits an LR filling, so non-degeneracy reduces to the purely combinatorial fact

      every λ ⊢ n with n ≥ k has a SUB-PARTITION of size n − k  (ξ ⊆ λ).

Proved here sorry-free (`exists_subpartition_of_size`) by removing one Young box
at a time from the last row.  The empirical completeness over the actual combiner
splits (6, 9, 12) is verified in `combiner_branching_completeness.py`.

Refs:
- [wenzl1988] Hecke algebras of type A_n and subfactors, Invent. Math. 92
- [halverson-ram1998] Murnaghan–Nakayama rule for the Hecke algebra
- [leitner2026] content/.../mass-endomorphism/hecke-branching-trace-decomposition.md
-/

open QOU.MathlibExt.QPartitionCombinatorics

namespace QOU.BraidsAndKnots.CombinerBranchingCompleteness

/-- Young-diagram containment `ξ ⊆ λ`, pointwise: `ξ.getD i 0 ≤ λ.getD i 0`. -/
def IsSubPartition (mu lam : Partition) : Prop :=
  ∀ i, mu.getD i 0 ≤ lam.getD i 0

theorem IsSubPartition.refl (lam : Partition) : IsSubPartition lam lam :=
  fun _ => le_refl _

theorem IsSubPartition.trans {a b c : Partition}
    (hab : IsSubPartition a b) (hbc : IsSubPartition b c) : IsSubPartition a c :=
  fun i => le_trans (hab i) (hbc i)

/-- Remove one Young box from the last nonempty row (drop it if it was a unit
    row).  On a canonical positive partition this lowers the size by exactly 1. -/
def dropLastBox : List ℕ → List ℕ
  | [] => []
  | [a] => if a ≤ 1 then [] else [a - 1]
  | a :: b :: t => a :: dropLastBox (b :: t)

/-- `dropLastBox l ⊆ l` (pointwise; no positivity needed). -/
theorem dropLastBox_sub : ∀ (l : List ℕ), IsSubPartition (dropLastBox l) l
  | [] => by intro i; simp [dropLastBox]
  | [a] => by
      intro i
      simp only [dropLastBox]
      split
      · simp
      · cases i with
        | zero => simp
        | succ i => simp
  | a :: b :: t => by
      intro i
      cases i with
      | zero => simp [dropLastBox]
      | succ i =>
        simp only [dropLastBox, List.getD_cons_succ]
        exact dropLastBox_sub (b :: t) i

/-- `dropLastBox` preserves positivity of the parts. -/
theorem dropLastBox_pos : ∀ (l : List ℕ), (∀ x ∈ l, 1 ≤ x) →
    ∀ x ∈ dropLastBox l, 1 ≤ x
  | [], _ => by simp [dropLastBox]
  | [a], _ => by
      simp only [dropLastBox]
      split
      · simp
      · rename_i hgt
        intro x hx
        simp only [List.mem_singleton] at hx
        subst hx; omega
  | a :: b :: t, hp => by
      simp only [dropLastBox]
      intro x hx
      simp only [List.mem_cons] at hx
      rcases hx with rfl | hx
      · exact hp x (by simp)
      · exact dropLastBox_pos (b :: t) (fun y hy => hp y (by simp [hy])) x hx

/-- On a canonical positive partition with at least one box, `dropLastBox`
    lowers the size by exactly one. -/
theorem dropLastBox_sum : ∀ (l : List ℕ), (∀ x ∈ l, 1 ≤ x) → 1 ≤ l.sum →
    (dropLastBox l).sum + 1 = l.sum
  | [], _, h => by simp at h
  | [a], hp, _ => by
      have ha : 1 ≤ a := hp a (by simp)
      simp only [dropLastBox]
      split
      · rename_i hle
        have : a = 1 := by omega
        subst this; simp
      · rename_i hgt
        simp only [List.sum_cons, List.sum_nil]
        omega
  | a :: b :: t, hp, _ => by
      have hbt : 1 ≤ (b :: t).sum := by
        have hb : 1 ≤ b := hp b (by simp)
        simp only [List.sum_cons]; omega
      have hp' : ∀ x ∈ b :: t, 1 ≤ x := fun x hx => hp x (by simp [hx])
      have ih := dropLastBox_sum (b :: t) hp' hbt
      have hd : dropLastBox (a :: b :: t) = a :: dropLastBox (b :: t) := rfl
      rw [hd, List.sum_cons, List.sum_cons]
      omega

/-- **Combiner non-degeneracy (Frobenius reciprocity completeness).**  Every
    canonical positive partition `λ` of size `≥ k` has a sub-partition `μ ⊆ λ` of
    size `|λ| − k` — so the branching `H_{|λ|−k}(q) ⊗ H_k(q) ↪ H_{|λ|}(q)`
    reaches `λ` (its `interface_blocks` enumeration is non-empty), and the
    operator-valued combiner drops no Wedderburn block. -/
theorem exists_subpartition_of_size :
    ∀ (k : ℕ) (lam : Partition), (∀ x ∈ lam, 1 ≤ x) → k ≤ lam.sum →
      ∃ mu : Partition, mu.sum + k = lam.sum ∧ IsSubPartition mu lam
  | 0, lam, _, _ => ⟨lam, by simp, IsSubPartition.refl lam⟩
  | k + 1, lam, hp, hk => by
      have hsum1 : 1 ≤ lam.sum := by omega
      have hstep : (dropLastBox lam).sum + 1 = lam.sum := dropLastBox_sum lam hp hsum1
      have hp' : ∀ x ∈ dropLastBox lam, 1 ≤ x := dropLastBox_pos lam hp
      have hk' : k ≤ (dropLastBox lam).sum := by omega
      obtain ⟨mu, hmu, hsub⟩ := exists_subpartition_of_size k (dropLastBox lam) hp' hk'
      exact ⟨mu, by omega, hsub.trans (dropLastBox_sub lam)⟩

end QOU.BraidsAndKnots.CombinerBranchingCompleteness
