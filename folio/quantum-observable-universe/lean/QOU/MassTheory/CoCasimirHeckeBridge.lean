import QOU.SchurWeyl.HeckeWedderburnAnyChar
import QOU.SchurWeyl.MarkovTraceInstance
import QOU.MassTheory.CoCasimirSurvivingBlocks

/-!
# The surviving-block co-Casimir on `H_{n+1}(q)` itself, at convention D

`CoCasimirSurvivingBlocks` defines `C°` and proves its properties on an abstract Wedderburn
model `Π_λ Mat_{d_λ}(K)` with trace `τ(a) = Σ_λ w_λ · Tr(a_λ)`. It takes two inputs as given:
that the Hecke algebra *is* such a product, and that its trace *has* such block weights. Both are
now theorems of the corpus, and this file composes them, so nothing about the model is assumed.

* `AnyChar.heckeWedderburnF` — `H_{n+1}(q) ≅ Π_{λ ⊢ n+1} Mat_{SYT(λ)}(K)` over any field, for
  `q ≠ 0` not a root of unity. The blocks are the seminormal representations.
* `SeminormalRep.eq_wtrace_of_markov` — every Markov trace family at `z_D = q³/(q²+1)` equals
  the seminormal trace weighted by `ocneanuWeight q z_D λ`.

Composing them with a reindexing of each block to `Fin (#SYT λ)` gives an algebra isomorphism
`Ψ : H_{n+1}(q) ≃ₐ Blocks K d` with `T.tr n x = tr w (Ψ x)` for **every** Markov trace family
`T` at `z_D` (`markov_eq_tr`). Transporting along `Ψ`:

* `cHecke_central` — `C° := Ψ⁻¹(coCasimirSurv w dq)` is central in `H_{n+1}(q)`;
* `markov_radical_iff` — `x` is in the radical of the Markov trace form iff it acts by zero in
  every seminormal representation of a partition with at most two rows;
* `tr_cHecke` — `T(C°) = Σ_{λ ⊢ n+1, ℓ(λ) ≤ 2} 1/dim_q(λ)`;
* `tr_of_agree_on_surviving` — any `x` agreeing with `C°` on the ≤ 2-row blocks has the same
  trace, so the value is a property of the class of `C°` in `H/rad τ`.

`dim_q(λ)` stays block data `dq`, as in the abstract file. The only hypothesis on the block
dimensions is `#SYT(λ) ≠ 0` in `K` (`hd`), automatic in characteristic zero.

## Base ring (§7c)

Generic `[Field K]`; no ordering, nothing archimedean, no `ℝ`.

LaTeX label: `thm:cocasimir-surviving-hecke`
-/

namespace QOU.MassTheory.CoCasimirHecke

open Finset QOU.SchurWeyl QOU.MassTheory.CoCasimirSurviving
open QOU.Mathlib (StandardYoungTableau partitionShape)

noncomputable section

variable {K : Type*} [Field K]

/-- Reindexing a square matrix does not change its trace. -/
theorem trace_reindex_self {m n : Type*} [Fintype m] [Fintype n] (e : m ≃ n)
    (M : Matrix m m K) : (Matrix.reindex e e M).trace = M.trace := by
  simp only [Matrix.trace, Matrix.diag, Matrix.reindex_apply, Matrix.submatrix_apply]
  exact Equiv.sum_comp e.symm (fun i => M i i)

variable (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)

/-- Block dimensions: the number of standard tableaux of shape `λ`. -/
def dim (lam : Nat.Partition (n + 1)) : ℕ :=
  Fintype.card (StandardYoungTableau (partitionShape lam))

/-- The convention-D block weights `w_λ = ocneanuWeight q z_D λ`. -/
def wD (lam : Nat.Partition (n + 1)) : K :=
  ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (partitionShape lam)

/-- **The Wedderburn isomorphism in the shape the abstract file uses**:
`H_{n+1}(q) ≃ₐ Π_λ Mat_{#SYT(λ)}(K)` with `Fin`-indexed blocks. -/
def Ψ : Hecke K q q⁻¹ n ≃ₐ[K] Blocks K (dim n) :=
  (AnyChar.heckeWedderburnF q hq0 hq2 n).trans
    (AlgEquiv.piCongrRight fun lam =>
      Matrix.reindexAlgEquiv K K (Fintype.equivFin (StandardYoungTableau (partitionShape lam))))

theorem Ψ_apply (x : Hecke K q q⁻¹ n) (lam : Nat.Partition (n + 1)) :
    Ψ q hq0 hq2 n x lam
      = Matrix.reindex (Fintype.equivFin _) (Fintype.equivFin _)
          (SeminormalRep.seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) x) := rfl

/-- **The weighted block trace of `Ψ x` is the seminormal trace `wtrace`.** -/
theorem tr_Ψ (x : Hecke K q q⁻¹ n) :
    tr (wD q n) (Ψ q hq0 hq2 n x) = SeminormalRep.wtrace q hq0 hq2 n x := by
  rw [SeminormalRep.wtrace_apply]
  unfold tr
  refine Fintype.sum_equiv (QOU.Mathlib.partitionShapeEquiv (n + 1)) _ _ (fun lam => ?_)
  rw [Ψ_apply]
  exact congrArg₂ (· * ·) rfl (trace_reindex_self _ _)

/-- **Every Markov trace at `z_D` is the weighted block trace through `Ψ`.** -/
theorem markov_eq_tr (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2 : K) ^ k ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1))) (x : Hecke K q q⁻¹ n) :
    T.tr n x = tr (wD q n) (Ψ q hq0 hq2 n x) := by
  have hgenN : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1 := fun i hi => by
    have := hgen (i : ℤ) (by exact_mod_cast hi.ne')
    rwa [zpow_natCast] at this
  rw [SeminormalRep.eq_wtrace_of_markov q hq0 hq2 hq21 hgenN T n x, tr_Ψ]

/-- `C°` as an element of the Hecke algebra. -/
def cHecke (dq : Nat.Partition (n + 1) → K) : Hecke K q q⁻¹ n :=
  (Ψ q hq0 hq2 n).symm (coCasimirSurv (d := dim n) (wD q n) dq)

/-- **`C°` is central in `H_{n+1}(q)`.** -/
theorem cHecke_central (dq : Nat.Partition (n + 1) → K) (y : Hecke K q q⁻¹ n) :
    cHecke q hq0 hq2 n dq * y = y * cHecke q hq0 hq2 n dq := by
  apply (Ψ q hq0 hq2 n).injective
  simp only [map_mul, cHecke, AlgEquiv.apply_symm_apply]
  exact coCasimirSurv_central _ _ _

include hq0 in
/-- At convention D a block survives iff its partition has at most two rows. -/
theorem wD_ne_zero_iff (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2 : K) ^ k ≠ 1)
    (lam : Nat.Partition (n + 1)) :
    wD q n lam ≠ 0 ↔ (partitionShape lam).colLen 0 ≤ 2 :=
  conventionD_support_iff q hq0 hq21 hgen _

/-- **The radical of the Markov trace form at `z_D`.** For any Markov trace family `T`,
`x` pairs to zero with all of `H_{n+1}(q)` iff `x` acts by zero in every seminormal
representation of a partition with at most two rows. -/
theorem markov_radical_iff (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2 : K) ^ k ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1))) (x : Hecke K q q⁻¹ n) :
    (∀ y, T.tr n (x * y) = 0) ↔
      ∀ lam : Nat.Partition (n + 1), (partitionShape lam).colLen 0 ≤ 2 →
        SeminormalRep.seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) x = 0 := by
  have h1 : (∀ y, T.tr n (x * y) = 0) ↔
      ∀ b : Blocks K (dim n), tr (wD q n) (Ψ q hq0 hq2 n x * b) = 0 := by
    rw [(Ψ q hq0 hq2 n).surjective.forall]
    refine forall_congr' fun y => ?_
    rw [markov_eq_tr q hq0 hq2 n hq21 hgen T, map_mul]
  rw [h1, mem_traceRadical_iff]
  refine forall_congr' fun lam => ?_
  rw [wD_ne_zero_iff q hq0 n hq21 hgen, Ψ_apply]
  refine imp_congr_right fun _ => ?_
  exact EmbeddingLike.map_eq_zero_iff (f := Matrix.reindexLinearEquiv K K
    (Fintype.equivFin _) (Fintype.equivFin _))

/-- **Term 4 on `H_{n+1}(q)` at convention D.** For every Markov trace family `T` at `z_D`,
`T(C°) = Σ_{λ ⊢ n+1, ℓ(λ) ≤ 2} 1/dim_q(λ)`. -/
theorem tr_cHecke (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2 : K) ^ k ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (dq : Nat.Partition (n + 1) → K) (hd : ∀ lam, (dim n lam : K) ≠ 0)
    (hdq : ∀ lam, (partitionShape lam).colLen 0 ≤ 2 → dq lam ≠ 0) :
    T.tr n (cHecke q hq0 hq2 n dq)
      = ∑ lam ∈ univ.filter (fun lam : Nat.Partition (n + 1) =>
          (partitionShape lam).colLen 0 ≤ 2), 1 / dq lam := by
  rw [markov_eq_tr q hq0 hq2 n hq21 hgen T, cHecke, AlgEquiv.apply_symm_apply,
    tr_coCasimirSurv _ dq hd
      (fun lam hw => hdq lam ((wD_ne_zero_iff q hq0 n hq21 hgen lam).mp hw))]
  unfold support
  congr 1
  ext lam
  simp [wD_ne_zero_iff q hq0 n hq21 hgen]

/-- **Independence of the lift.** Any `x` that agrees with `C°` in every seminormal
representation of a partition with at most two rows has the same Markov trace. -/
theorem tr_of_agree_on_surviving (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2 : K) ^ k ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (dq : Nat.Partition (n + 1) → K) (hd : ∀ lam, (dim n lam : K) ≠ 0)
    (hdq : ∀ lam, (partitionShape lam).colLen 0 ≤ 2 → dq lam ≠ 0) (x : Hecke K q q⁻¹ n)
    (hx : ∀ lam : Nat.Partition (n + 1), (partitionShape lam).colLen 0 ≤ 2 →
      SeminormalRep.seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) x
        = SeminormalRep.seminormalRep q hq0 hq2 n (partitionShape_card_succ lam)
            (cHecke q hq0 hq2 n dq)) :
    T.tr n x = ∑ lam ∈ univ.filter (fun lam : Nat.Partition (n + 1) =>
          (partitionShape lam).colLen 0 ≤ 2), 1 / dq lam := by
  have hrad : ∀ y, T.tr n ((x - cHecke q hq0 hq2 n dq) * y) = 0 := by
    rw [markov_radical_iff q hq0 hq2 n hq21 hgen T]
    intro lam hlam
    rw [map_sub, hx lam hlam, sub_self]
  have h0 := hrad 1
  rw [mul_one, map_sub, sub_eq_zero] at h0
  rw [h0, tr_cHecke q hq0 hq2 n hq21 hgen T dq hd hdq]

end

end QOU.MassTheory.CoCasimirHecke
