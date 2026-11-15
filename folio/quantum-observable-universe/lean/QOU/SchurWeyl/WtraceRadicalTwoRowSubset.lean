/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.WtraceRadicalTwoRow
import QOU.SchurWeyl.OcneanuWeightTwoRowNonzero
import QOU.SchurWeyl.HeckeProductSurjective

/-!
# The radical of `wtrace` is EXACTLY the three-row part

`WtraceRadicalTwoRow` has the **⊇** half — anything killed by every at-most-two-row
block is invisible to the Ocneanu trace form.  This file adds **⊆** and so turns an
inclusion into an identification.

## The statement

`notMem_rad_of_twoRow_block_ne_zero` — if some at-most-two-row block does *not* kill
`x`, then some `b` pairs with it: `wtrace (x * b) ≠ 0`.  Contrapositive of ⊆.

`mem_rad_iff_twoRow_blocks_vanish` — the two halves together, as an iff.

## Why this is not blocked (a retraction)

`WtraceRadicalTwoRow`'s docstring, bean `qou-s7z2` and PR #7460's body all recorded
⊆ as blocked on Wenzl's theorem: it needs the ≤2-row Ocneanu weights **nonzero**,
and the corpus's only statement of that was conditional on
`QBeta.IsOcneanuWeightSystem`, a class with no instance (deleted 2026-11-15, bean `qou-gld2`; the weights are now a theorem, `SchurWeyl.JimboGL.markov_tr_blockE`).

That reasoning went through the wrong object.  `IsOcneanuWeightSystem` relates an
**opaque** weight family to `schurPrincipal`; `ocneanuWeight` is a **closed form**, so
the non-vanishing is provable directly — `OcneanuWeightTwoRowNonzero`, from the
genericity `wtrace` already carries.  See that file's docstring.

## The two remaining ingredients, and they are cheap

1. `exists_trace_mul_ne_zero` — a nonzero matrix is seen by *some* matrix under the
   trace form.  Pick an entry `M i j ≠ 0` and pair with the single-entry matrix at
   `(j, i)`; the product's diagonal is supported at `i` and reads off `M i j`.
2. **Block isolation** — `heckeProduct_surjective` realises the tuple
   `Function.update 0 lam₀ N`, so every block but `lam₀` contributes `0` to the
   Frobenius sum.  The surviving term is `w_{d} · (M · N).trace`, a product of two
   nonzero reals.

The sum is indexed by `{ν : YoungDiagram // ν.cells.card = n+1}` while `heckeProduct`
is indexed by `Partition (n+1)`; `partitionShapeEquiv` reindexes one to the other, which
is what lets `Finset.sum_eq_single` see a single surviving block.

## Scope

Convention **D** (`z = q³/(q²+1)`), `ℝ`, and the genericity `wtrace` carries — the same
scope as the ⊇ half.  Under the excised convention C the three-row weight is nonzero and
the whole statement is empty rather than false.
-/

namespace QOU.SchurWeyl.WtraceRadicalTwoRow

open YoungDiagram QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep QOU.SchurWeyl.HeckeInclusion

/-- **A nonzero matrix is seen by the trace form.**

Pick `i j` with `M i j ≠ 0` and pair with the single-entry matrix at `(j, i)`: the
product's diagonal is supported at `i`, where it reads `M i j`. -/
theorem exists_trace_mul_ne_zero {ι : Type*} [Fintype ι] [DecidableEq ι]
    {R : Type*} [CommRing R] {M : Matrix ι ι R} (hM : M ≠ 0) :
    ∃ N : Matrix ι ι R, (M * N).trace ≠ 0 := by
  classical
  obtain ⟨i, j, hij⟩ : ∃ i j, M i j ≠ 0 := by
    by_contra h
    push_neg at h
    exact hM (by ext a b; simpa using h a b)
  refine ⟨Matrix.of fun a b => if a = j ∧ b = i then (1 : R) else 0, ?_⟩
  have key : (M * Matrix.of fun a b => if a = j ∧ b = i then (1 : R) else 0).trace
      = M i j := by
    rw [Matrix.trace]
    rw [Finset.sum_eq_single_of_mem i (Finset.mem_univ i)]
    · simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.of_apply]
      rw [Finset.sum_eq_single_of_mem j (Finset.mem_univ j)]
      · simp
      · intro b _ hb
        simp [hb]
    · intro a _ ha
      simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.of_apply]
      exact Finset.sum_eq_zero fun b _ => by simp [ha]
  rw [key]
  exact hij

/-- **⊆ : a live at-most-two-row block is visible to `wtrace`.**

Contrapositive of "the radical is contained in the `ℓ(λ) ≥ 3` part".  If some shape
with at most two rows does not kill `x`, then `x` is not in the radical. -/
theorem notMem_rad_of_twoRow_block_ne_zero {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ)
    (x : Hecke ℝ q q⁻¹ n) (d : YoungDiagram) (hd : d.cells.card = n + 1)
    (hrow : d.rowLen 2 = 0) (hne : seminormalRep q hq0 hq2 n hd x ≠ 0) :
    ∃ b : Hecke ℝ q q⁻¹ n, wtrace q hq0 hq2 n (x * b) ≠ 0 := by
  classical
  obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq d hd
  -- `subst` rather than transport: `d` is a variable, so the diagram becomes
  -- `partitionShape lam₀` everywhere and no `HEq` is ever created.
  subst hlam₀
  obtain ⟨N, hN⟩ := exists_trace_mul_ne_zero
    (M := seminormalRep q hq0 hq2 n hd x) hne
  -- realise the tuple that is `N` at `lam₀` and `0` elsewhere
  obtain ⟨b, hb⟩ := heckeProduct_surjective q hq0 hq2 n (Function.update 0 lam₀ N)
  refine ⟨b, ?_⟩
  rw [wtrace_apply]
  -- the Frobenius sum is indexed by diagrams; `heckeProduct` by partitions
  rw [← Equiv.sum_comp (partitionShapeEquiv (n + 1))
    (fun ν : {ν : YoungDiagram // ν.cells.card = n + 1} =>
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1
        * (seminormalRep q hq0 hq2 n ν.2 (x * b)).trace)]
  -- the block at `lam` IS the `lam` component of `heckeProduct` — `rfl`, since
  -- `↑(partitionShapeEquiv _ lam) = partitionShape lam` definitionally and the
  -- cardinality proof is a `Prop`
  have hρ : ∀ (lam : Nat.Partition (n + 1)) (y : Hecke ℝ q q⁻¹ n),
      seminormalRep q hq0 hq2 n (partitionShapeEquiv (n + 1) lam).2 y
        = heckeProduct q hq0 hq2 n y lam := fun _ _ => rfl
  rw [Finset.sum_eq_single_of_mem lam₀ (Finset.mem_univ lam₀)]
  · -- the surviving term: a nonzero weight times a nonzero pairing
    have hbN : heckeProduct q hq0 hq2 n b lam₀ = N := by rw [hb]; simp
    have htr : (seminormalRep q hq0 hq2 n (partitionShapeEquiv (n + 1) lam₀).2 (x * b)).trace
        = (seminormalRep q hq0 hq2 n hd x * N).trace := by
      rw [map_mul, hρ lam₀ b, hbN]
      -- the two cardinality proofs differ; `Prop` proof irrelevance closes it
      rfl
    refine mul_ne_zero
      (ocneanuWeight_conventionD_ne_zero_of_two_rows q hq0 hq21 hgen _ hrow) ?_
    rw [htr]; exact hN
  · -- every other block is zeroed by the tuple
    intro lam _ hlam
    have hbz : heckeProduct q hq0 hq2 n b lam = 0 := by rw [hb]; simp [hlam]
    have hz : seminormalRep q hq0 hq2 n (partitionShapeEquiv (n + 1) lam).2 (x * b) = 0 := by
      rw [map_mul, hρ lam b, hbz, mul_zero]
    rw [hz, Matrix.trace_zero, mul_zero]

/-- **The radical of `wtrace` is EXACTLY the three-row part.**

The two halves together: `x` is invisible to the Ocneanu trace form precisely when every
at-most-two-row block kills it.  Equivalently, the radical is the span of the blocks with
`ℓ(λ) ≥ 3` — which at convention D is the Temperley–Lieb ideal. -/
theorem mem_rad_iff_twoRow_blocks_vanish {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    (∀ b : Hecke ℝ q q⁻¹ n, wtrace q hq0 hq2 n (x * b) = 0)
      ↔ ∀ (d : YoungDiagram) (hd : d.cells.card = n + 1), d.rowLen 2 = 0 →
          seminormalRep q hq0 hq2 n hd x = 0 := by
  refine ⟨fun h d hd hrow => ?_, fun h => mem_rad_of_twoRow_blocks_vanish hq0 hq2 hq21 n x h⟩
  by_contra hne
  obtain ⟨b, hb⟩ := notMem_rad_of_twoRow_block_ne_zero hq0 hq2 hq21 hgen n x d hd hrow hne
  exact hb (h b)


/-! ## The tower comparison, unconditionally, at the concrete carrier

`QBeta.TLTowerRadicalDescent` compares the radicals at consecutive ranks and proves
both directions — but every statement there is conditional, in the §3b-cond sense, on
`HeckeConditionalExpectation`, an OPEN class with no instance.  Its docstring explains
why: a bare inclusion says nothing, because membership in the upper radical quantifies
over the *whole* upper algebra, not over the image.

At the concrete `wtrace` carrier the **reflection** direction needs none of that,
because `wtrace_incl` is already unconditional: restricting a test element to the
image is enough, and `heckeIncl` being an `AlgHom` supplies the rest.  Two rewrites.

This is the direction that carries the weight there — it is what makes the quotients a
*tower* (`TL_n ↪ TL_{n+1}`) rather than a sequence of algebras with maps between them.
The forward direction genuinely does need more than the inclusion, and is **not**
claimed here; via `mem_rad_iff_twoRow_blocks_vanish` it reduces to the branching
statement that erasing a corner from an at-most-two-row diagram leaves at most two
rows, which is a separate piece of work.
-/

/-- **Reflection along the tower inclusion, unconditionally.**

If `heckeIncl a` is invisible to `wtrace` at level `m+1`, then `a` is invisible at level
`m`.  Test elements are restricted to the image: `wtrace (heckeIncl a * heckeIncl b) =
wtrace (heckeIncl (a * b)) = wtrace (a * b)`.

No conditional expectation, and no instance of any open class — only the genericity
`wtrace` already carries. -/
theorem mem_rad_of_incl_mem_rad {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (m : ℕ) (a : Hecke ℝ q q⁻¹ m)
    (ha : ∀ x : Hecke ℝ q q⁻¹ (m + 1),
      wtrace q hq0 hq2 (m + 1) (heckeIncl ℝ q q⁻¹ m a * x) = 0) :
    ∀ b : Hecke ℝ q q⁻¹ m, wtrace q hq0 hq2 m (a * b) = 0 := by
  intro b
  have h := ha (heckeIncl ℝ q q⁻¹ m b)
  rwa [← map_mul, wtrace_incl q hq0 hq2 hq21 hgen m] at h

/-- **The tower inclusion is injective on the quotients** — `TL_m ↪ TL_{m+1}`, in the
form "distinct classes stay distinct", unconditionally.

Contrapositive packaging of `mem_rad_of_incl_mem_rad`: an element outside the radical at
level `m` stays outside it after inclusion. -/
theorem notMem_rad_incl_of_notMem_rad {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (m : ℕ) (a : Hecke ℝ q q⁻¹ m)
    (ha : ∃ b : Hecke ℝ q q⁻¹ m, wtrace q hq0 hq2 m (a * b) ≠ 0) :
    ∃ x : Hecke ℝ q q⁻¹ (m + 1),
      wtrace q hq0 hq2 (m + 1) (heckeIncl ℝ q q⁻¹ m a * x) ≠ 0 := by
  obtain ⟨b, hb⟩ := ha
  by_contra hcon
  push_neg at hcon
  exact hb (mem_rad_of_incl_mem_rad hq0 hq2 hq21 hgen m a hcon b)
end QOU.SchurWeyl.WtraceRadicalTwoRow
