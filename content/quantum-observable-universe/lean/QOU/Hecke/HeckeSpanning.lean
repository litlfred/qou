import QOU.Hecke.HeckeStaircase

/-!
# QOU.Hecke.HeckeSpanning — `H_{n+1}(q) = Σ_k incl(H_n(q)) · c_k`

Third brick of the type-`A` spanning argument (bean `qou-twwf`).
`QOU.Hecke.HeckeStaircase` proved the four ways a generator interacts with a
descending run; this file assembles them into the tower decomposition.

## What is proved

* `towerSpan` — the submodule `Σ_{k ≤ n+1} incl(H_n(q)) · c_k`.
* `towerSpan_mul_gen` — it is closed under right multiplication by every
  generator.
* `towerSpan_eq_top` — hence it is everything.

## The case analysis

The foot of `c_k = σ_n ⋯ σ_{n+1-k}` is `σ_{n+1-k}`, and the four cases are
decided by where `i` sits relative to it.  **Order matters**: the fold case is
tested first, because at the full run `k = n+1` truncated subtraction collapses
"one below the foot" onto the foot itself, and reading that as the extend case
would ask for `c_{n+2}`, which is off the end of the tower.
-/

namespace QOU.Hecke.IwahoriHecke

variable (K : Type*) [CommRing K] (q : K) (n : ℕ)

/-- The tower subalgebra: the image of `H_n(q)` inside `H_{n+1}(q)`. -/
noncomputable def towerSub : Subalgebra K (IwahoriHecke K q (n + 1)) :=
  (incl K q n).range

/-- The tower decomposition `Σ_{k ≤ n+1} incl(H_n(q)) · c_k`, as a submodule. -/
noncomputable def towerSpan : Submodule K (IwahoriHecke K q (n + 1)) :=
  ⨆ k : Fin (n + 2),
    Submodule.map (LinearMap.mulRight K (stair K q n (k : ℕ)))
      (towerSub K q n).toSubmodule

theorem mul_stair_mem {a : IwahoriHecke K q (n + 1)} (ha : a ∈ towerSub K q n)
    {k : ℕ} (hk : k ≤ n + 1) : a * stair K q n k ∈ towerSpan K q n := by
  refine Submodule.mem_iSup_of_mem (⟨k, by omega⟩ : Fin (n + 2)) ?_
  exact ⟨a, ha, rfl⟩

theorem one_mem_towerSpan : (1 : IwahoriHecke K q (n + 1)) ∈ towerSpan K q n := by
  have h := mul_stair_mem K q n (a := 1) (one_mem _) (k := 0) (by omega)
  simpa using h

/-- **The four cases, assembled.**  A single summand `a · c_k` times a generator
    stays in the tower decomposition. -/
theorem mul_stair_mul_gen_mem {a : IwahoriHecke K q (n + 1)}
    (ha : a ∈ towerSub K q n) {k : ℕ} (hk : k ≤ n + 1) {i : ℕ} (hi : i ≤ n) :
    a * stair K q n k * gen K q n i ∈ towerSpan K q n := by
  by_cases hfold : i = n - (k - 1)
  · -- fold: `σ_i` is the run's own foot, and the quadratic relation fires
    rcases Nat.eq_zero_or_pos k with hk0 | hk1
    · -- `c_0 = 1`, so the "foot" reads as `σ_n` and this is really `c_1`
      subst hk0
      have hin : i = n := by simpa using hfold
      have hstep : a * stair K q n 0 * gen K q n i = a * stair K q n 1 := by
        rw [hin, stair_succ]; simp
      rw [hstep]
      exact mul_stair_mem K q n ha (by omega)
    · obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
      have hk' : k' ≤ n := by omega
      have hfoldeq : n - (k' + 1 - 1) = n - k' := by omega
      rw [hfold, hfoldeq, mul_assoc, stair_fold K q n k' hk', mul_add,
        mul_smul_comm, mul_smul_comm]
      exact Submodule.add_mem _
        (Submodule.smul_mem _ _ (mul_stair_mem K q n ha (by omega)))
        (Submodule.smul_mem _ _ (mul_stair_mem K q n ha (by omega)))
  · by_cases hext : i = n - k ∧ k ≤ n
    · -- extend: the run grows by one letter
      obtain ⟨hieq, hkn⟩ := hext
      rw [hieq, mul_assoc, ← stair_succ]
      exact mul_stair_mem K q n ha (by omega)
    · by_cases hcom : i + 2 ≤ n - k + 1
      · -- commute: `σ_i` is strictly below the whole run
        rw [mul_assoc, stair_comm K q n k i hcom, ← mul_assoc]
        exact mul_stair_mem K q n
          (mul_mem ha (gen_mem_inclRange K q n (by omega))) hk
      · -- push: `σ_i` is above the foot and comes out with index `i - 1`
        have hpush : n + 1 - k < i := by
          simp only [not_and_or] at hext
          omega
        rw [mul_assoc, stair_push K q n k hk i hi hpush, ← mul_assoc]
        exact mul_stair_mem K q n
          (mul_mem ha (gen_mem_inclRange K q n (by omega))) hk

/-- **The tower decomposition is closed under right multiplication by the
    generators.** -/
theorem towerSpan_mul_gen {x : IwahoriHecke K q (n + 1)} (hx : x ∈ towerSpan K q n)
    {i : ℕ} (hi : i ≤ n) : x * gen K q n i ∈ towerSpan K q n := by
  induction hx using Submodule.iSup_induction' with
  | mem k y hy =>
      obtain ⟨a, ha, rfl⟩ := hy
      exact mul_stair_mul_gen_mem K q n ha (by omega) hi
  | zero => simp
  | add x y _ _ hx hy => rw [add_mul]; exact Submodule.add_mem _ hx hy

/-- The generators of `H_m(q)` generate it as a `K`-algebra.  Stated at every
    `m`, not just `n+1`, because the spanning induction needs the `m = 0` base
    case where the generating set is empty. -/
theorem adjoin_range_σ (m : ℕ) :
    Algebra.adjoin K (Set.range (σ K q m)) = ⊤ := by
  have hcomp : (σ K q m) = (mk K q m) ∘ (FreeAlgebra.ι K) := rfl
  have hrange : Set.range (σ K q m)
      = (mk K q m) '' (Set.range (FreeAlgebra.ι K)) := by
    rw [hcomp, Set.range_comp]
  rw [hrange, ← AlgHom.map_adjoin, FreeAlgebra.adjoin_range_ι, Algebra.map_top,
    AlgHom.range_eq_top]
  exact RingQuot.mkAlgHom_surjective K _

/-- **The tower decomposition is everything.**  `1` is in it and it is closed
    under right multiplication by generators, and those generate the algebra. -/
theorem towerSpan_eq_top : towerSpan K q n = ⊤ := by
  have hspan := Algebra.adjoin_eq_span (R := K) (Set.range (σ K q (n + 1)))
  rw [adjoin_range_σ K q (n + 1)] at hspan
  have htop : (⊤ : Submodule K (IwahoriHecke K q (n + 1)))
      = Submodule.span K (Submonoid.closure (Set.range (σ K q (n + 1))) : Set _) := by
    rw [← hspan]; simp
  refine top_unique ?_
  rw [htop]
  refine Submodule.span_le.mpr ?_
  intro x hx
  induction hx using Submonoid.closure_induction_right with
  | one => exact one_mem_towerSpan K q n
  | mul_right x _ y hy ih =>
      obtain ⟨j, rfl⟩ := hy
      have hgen : σ K q (n + 1) j = gen K q n (j : ℕ) := by
        rw [gen_eq_σ K q n j.isLt, Fin.eta]
      rw [hgen]
      exact towerSpan_mul_gen K q n ih (Nat.lt_succ_iff.mp j.isLt)

end QOU.Hecke.IwahoriHecke
