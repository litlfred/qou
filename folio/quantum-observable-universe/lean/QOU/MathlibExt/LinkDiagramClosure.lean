import QOU.MathlibExt.LinkDiagramStateSum
import Mathlib.Data.Matrix.Mul
import Mathlib.Algebra.BigOperators.Fin

/-!
# The state-sum value of a braid closure

For a braid word `w` on `m + 1` strands, the letter at level `k` acts on the labels of one row of
edges by the level matrix `levelMat M x`: the crossing tensor on the two positions the letter
touches, the identity on the others. The closing arcs each turn once, so they insert `K` on every
position. The value of the closure is the weighted trace

    value M (braidClosure w) = Σ_a (∏_p K (a p)) · (∏_k levelMat M (w k)) a a

(`value_braidClosure`). The proof sums over the rows of labels one at a time (`sum_path`).

-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links", Invent. Math. 92
-- Ref: [kassel2008] Kassel–Turaev, "Braid Groups", GTM 247, Ch. 2–3 (closure, Markov)
-/

namespace QOU.MathlibExt.PL.Diagram

open Finset

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι]

/-! ### Sums over paths -/

section Path

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- **A sum over paths is a matrix product.** Summing `f (start) (end) · ∏_k A_k (s_k) (s_{k+1})`
over all paths `s : Fin (L + 1) → S` gives `Σ_{a,c} f a c · (A_0 ⋯ A_{L-1}) a c`. -/
theorem sum_path : ∀ (L : ℕ) (A : Fin L → Matrix S S R) (f : S → S → R),
    ∑ s : Fin (L + 1) → S, f (s 0) (s (Fin.last L)) * ∏ k : Fin L, A k (s k.castSucc) (s k.succ) =
      ∑ a, ∑ c, f a c * (List.ofFn A).prod a c
  | 0, A, f => by
      simp only [Finset.univ_eq_empty, Finset.prod_empty, mul_one, List.ofFn_zero,
        List.prod_nil, Matrix.one_apply, mul_ite, mul_zero, Finset.sum_ite_eq, Finset.mem_univ,
        if_true]
      exact (Equiv.funUnique (Fin 1) S).sum_comp (fun a => f a a)
  | L + 1, A, f => by
      rw [← (Fin.snocEquiv fun _ => S).sum_comp, Fintype.sum_prod_type]
      have key : ∀ (s' : Fin (L + 1) → S) (x : S),
          f ((Fin.snocEquiv fun _ => S) (x, s') 0)
              ((Fin.snocEquiv fun _ => S) (x, s') (Fin.last (L + 1))) *
            ∏ k : Fin (L + 1), A k ((Fin.snocEquiv fun _ => S) (x, s') k.castSucc)
              ((Fin.snocEquiv fun _ => S) (x, s') k.succ) =
          (f (s' 0) x * A (Fin.last L) (s' (Fin.last L)) x) *
            ∏ k : Fin L, A k.castSucc (s' k.castSucc) (s' k.succ) := by
        intro s' x
        rw [Fin.prod_univ_castSucc]
        simp only [Fin.snocEquiv_apply, Fin.snoc_last, Fin.snoc_castSucc, Fin.succ_last]
        have h0 : (Fin.snoc s' x : Fin (L + 2) → S) 0 = s' 0 := by
          simp
        have hs : ∀ k : Fin L, (Fin.snoc s' x : Fin (L + 2) → S) k.castSucc.succ = s' k.succ := by
          intro k
          rw [Fin.succ_castSucc]
          exact Fin.snoc_castSucc (α := fun _ => S) x s' k.succ
        rw [h0]
        simp only [hs]
        ring
      simp only [key]
      rw [Finset.sum_comm]
      have := sum_path L (fun k => A k.castSucc)
        (fun a c => ∑ x, f a x * A (Fin.last L) c x)
      simp only [Finset.sum_mul] at this ⊢
      rw [this, List.ofFn_succ', List.prod_concat]
      simp only [Matrix.mul_apply, Finset.mul_sum]
      refine Finset.sum_congr rfl fun a _ => ?_
      rw [Finset.sum_comm]
      refine Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun x _ => ?_
      ring

end Path

/-! ### The level matrices -/

variable (M : Model R ι)

/-- The level matrix of the letter `(i, b)` on `m + 1` strands: the crossing tensor of
`letterCrossing` on positions `i, i + 1`, and the identity elsewhere. -/
def levelMat {m : ℕ} (x : Fin m × Bool) : Matrix (Fin (m + 1) → ι) (Fin (m + 1) → ι) R :=
  Matrix.of fun a c =>
    if ∀ p, p ≠ x.1.castSucc → p ≠ x.1.succ → a p = c p then
      (if x.2 then M.X true (a x.1.succ) (c x.1.castSucc) (a x.1.castSucc) (c x.1.succ)
       else M.X false (a x.1.castSucc) (c x.1.succ) (a x.1.succ) (c x.1.castSucc))
    else 0

omit [Fintype ι] in
theorem levelMat_apply {m : ℕ} (x : Fin m × Bool) (a c : Fin (m + 1) → ι) :
    levelMat M x a c =
      (if x.2 then M.X true (a x.1.succ) (c x.1.castSucc) (a x.1.castSucc) (c x.1.succ)
       else M.X false (a x.1.castSucc) (c x.1.succ) (a x.1.succ) (c x.1.castSucc)) *
        ∏ p ∈ Finset.univ.filter (fun p : Fin (m + 1) => p ≠ x.1.castSucc ∧ p ≠ x.1.succ),
          (if a p = c p then 1 else 0) := by
  rw [Finset.prod_boole, levelMat, Matrix.of_apply]
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, and_imp]
  split_ifs <;> simp

/-! ### The closure -/

/-- Every edge of a braid closure occurs in it. -/
theorem braidClosure_occurs {m : ℕ} (w : List (Fin m × Bool))
    (e : Fin (w.length + 1) × Fin (m + 1)) : (braidClosure w).Occurs e := by
  obtain ⟨k, p⟩ := e
  refine Fin.cases ?_ (fun j => ?_) k
  · refine Or.inr ⟨((Fin.last _, p), (0, p), 1), ?_, Or.inr rfl⟩
    simp only [braidClosure, Multiset.mem_add, Multiset.mem_map]
    exact Or.inr ⟨p, Finset.mem_univ_val _, rfl⟩
  · by_cases hp : p = (w.get j).1.castSucc ∨ p = (w.get j).1.succ
    · refine Or.inl ⟨letterCrossing j (w.get j).1 (w.get j).2, by simp [braidClosure], ?_⟩
      unfold letterCrossing Crossing.Mentions
      rcases hp with rfl | rfl <;> cases (w.get j).2 <;> simp
    · refine Or.inr ⟨((j.castSucc, p), (j.succ, p), 0), ?_, Or.inr rfl⟩
      simp only [braidClosure, Multiset.mem_add, Multiset.mem_bind, Multiset.mem_map]
      refine Or.inl ⟨j, Finset.mem_univ_val _, ?_⟩
      unfold letterJoins
      simp only [Multiset.mem_map]
      refine ⟨p, ?_, rfl⟩
      simp only [Finset.mem_val, Finset.mem_filter, Finset.mem_univ, true_and]
      push_neg at hp
      exact hp

/-- **The value of a braid closure is a weighted trace.** -/
theorem value_braidClosure {m : ℕ} (w : List (Fin m × Bool)) :
    value M (braidClosure w) =
      ∑ a : Fin (m + 1) → ι, (∏ p, (M.K (a p) : R)) * (w.map (levelMat M)).prod a a := by
  classical
  unfold value
  rw [← (Equiv.curry (Fin (w.length + 1)) (Fin (m + 1)) ι).symm.sum_comp]
  have hw : ∀ s : Fin (w.length + 1) → Fin (m + 1) → ι,
      weight M (braidClosure w) ((Equiv.curry _ _ _).symm s) =
        (if s (Fin.last w.length) = s 0 then ∏ p, (M.K (s 0 p) : R) else 0) *
          ∏ k : Fin w.length, levelMat M (w.get k) (s k.castSucc) (s k.succ) := by
    intro s
    have huf : ∏ e, uf M (braidClosure w) e ((Equiv.curry _ _ _).symm s) = 1 :=
      Finset.prod_eq_one fun e _ => by simp [uf, braidClosure_occurs w e]
    rw [weight, huf, mul_one]
    simp only [xw, jw, braidClosure, Multiset.map_add, Multiset.prod_add, Multiset.map_map,
      Multiset.map_bind, Multiset.prod_bind, Finset.prod_map_val, Function.comp_def]
    have hclose : ∏ p : Fin (m + 1),
        (if (Equiv.curry _ _ _).symm s (Fin.last w.length, p) = (Equiv.curry _ _ _).symm s (0, p) then
          ((M.K ((Equiv.curry _ _ _).symm s (Fin.last w.length, p)) ^ (1 : ℤ) : Rˣ) : R) else 0) =
        if s (Fin.last w.length) = s 0 then ∏ p, (M.K (s 0 p) : R) else 0 := by
      simp only [Equiv.curry_symm_apply, Function.uncurry_apply_pair, zpow_one]
      by_cases h : s (Fin.last w.length) = s 0
      · rw [if_pos h]
        exact Finset.prod_congr rfl fun p _ => by rw [if_pos (congrFun h p), congrFun h p]
      · rw [if_neg h]
        obtain ⟨p, hp⟩ := Function.ne_iff.1 h
        exact Finset.prod_eq_zero (Finset.mem_univ p) (if_neg hp)
    rw [hclose, ← mul_assoc, mul_comm, ← Finset.prod_mul_distrib]
    congr 1
    refine Finset.prod_congr rfl fun k _ => ?_
    rw [levelMat_apply]
    congr 1
    · generalize w.get k = x
      obtain ⟨i, b⟩ := x
      cases b <;> rfl
    · unfold letterJoins
      rw [Multiset.map_map, Finset.prod_map_val]
      refine Finset.prod_congr rfl fun p _ => ?_
      simp
  simp only [hw]
  rw [sum_path w.length (fun k => levelMat M (w.get k))
    (fun a c => if c = a then ∏ p, (M.K (a p) : R) else 0)]
  have hl : List.ofFn (fun k => levelMat M (w.get k)) = w.map (levelMat M) := by
    simp [List.ofFn_getElem_eq_map]
  rw [hl]
  simp only [ite_mul, zero_mul, Finset.sum_ite_eq', Finset.mem_univ, if_true]

end QOU.MathlibExt.PL.Diagram
