/-
Copyright (c) 2026 QOU contributors.
-/
import Mathlib.RingTheory.SimpleModule.Basic
import Mathlib.Algebra.Algebra.Subalgebra.Basic
import Mathlib.LinearAlgebra.Projection
import Mathlib.LinearAlgebra.FiniteDimensional.Defs

/-!
# The bicommutant theorem for a semisimple subalgebra (G3.4-DJ, milestone DJ0)

Let `K` be a field, `V` a finite-dimensional `K`-vector space and `A` a `K`-subalgebra of
`Module.End K V`. If `V` is a semisimple `A`-module (for instance, if `A` is a semisimple ring),
then the commutant of the commutant of `A` is `A`:

  `centralizer (centralizer A) = A`.

No hypothesis on `K` beyond being a field: no characteristic, no ordering, no algebraic closure.
The pinned Mathlib has only `Subalgebra.le_centralizer_centralizer` (the easy inclusion) and no
Jacobson density theorem, so the argument is written out here.

## Proof (Jacobson's density argument, finite-dimensional case)

Fix a basis `b : ι → V` and regard `b` as one vector of `V^ι`, on which `A` acts diagonally.
`V^ι` is a semisimple `A`-module, so the cyclic submodule `W = A·b` has an `A`-stable complement
and hence an `A`-linear projection `π : V^ι → V^ι` onto `W`. If `f` commutes with every
`A`-linear endomorphism of `V`, then `f^ι` commutes with every `A`-linear endomorphism of `V^ι`
(its matrix entries are `A`-linear endomorphisms of `V`), in particular with `π`. Hence
`f^ι b = f^ι (π b) = π (f^ι b) ∈ A·b`, i.e. there is `a ∈ A` with `f (b i) = a (b i)` for all
`i`, so `f = a`.

-- Ref: N. Jacobson, *Basic Algebra II*, 2nd ed., §4.3 (density theorem); the
-- finite-dimensional double-centraliser form. Source not yet held in `library/`; the argument
-- above is complete and is what the Lean below checks.

## Use in G3.4

Milestone DJ0 of `docs/audits/2026-11-15-gl34-dipper-james-scoping.md`. Applied to the image `A`
of the Hecke algebra in `End((K^d)^{⊗n})` (semisimple at generic `q`), it turns
`B = A'` (generation, DJ4) into `B' = A''= A`, which is G3.4.
-/

namespace QOU.MathlibExt.Bicommutant

open Module

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- An `A`-linear endomorphism of `V`, viewed as a `K`-linear one, commutes with every
element of `A`. -/
theorem restrictScalars_mem_centralizer (A : Subalgebra K (Module.End K V)) (g : V →ₗ[A] V) :
    (g.restrictScalars K : Module.End K V) ∈
      Subalgebra.centralizer K (A : Set (Module.End K V)) := by
  rw [Subalgebra.mem_centralizer_iff]
  intro a ha
  ext v
  change a (g v) = g (a v)
  exact (g.map_smul (⟨a, ha⟩ : A) v).symm

/-- The coordinatewise map `f^ι`, as a function on `ι → V`. -/
def diag {ι : Type*} (f : Module.End K V) (x : ι → V) : ι → V := fun i => f (x i)

/-- If `f` lies in the bicommutant of `A`, then `f^ι` commutes with every `A`-linear
endomorphism of `V^ι`. -/
theorem diag_comm {ι : Type*} [Fintype ι] [DecidableEq ι] (A : Subalgebra K (Module.End K V))
    {f : Module.End K V}
    (hf : f ∈ Subalgebra.centralizer K
      (Subalgebra.centralizer K (A : Set (Module.End K V)) : Set (Module.End K V)))
    (g : (ι → V) →ₗ[A] (ι → V)) (x : ι → V) : diag f (g x) = g (diag f x) := by
  -- the `(i, j)` entry of `g`, an `A`-linear endomorphism of `V`
  let e : ι → ι → (V →ₗ[A] V) := fun i j =>
    (LinearMap.proj i : (ι → V) →ₗ[A] V) ∘ₗ g ∘ₗ LinearMap.single A (fun _ : ι => V) j
  have hcomm : ∀ i j (v : V), f (e i j v) = e i j (f v) := by
    intro i j v
    have h := (Subalgebra.mem_centralizer_iff K).1 hf _
      (restrictScalars_mem_centralizer A (e i j))
    exact (congrArg (fun F : Module.End K V => F v) h).symm
  have hexp : ∀ y : ι → V, ∀ i, g y i = ∑ j, e i j (y j) := by
    intro y i
    conv_lhs => rw [← Finset.univ_sum_single y]
    rw [map_sum, Finset.sum_apply]
    rfl
  funext i
  simp only [diag]
  rw [hexp, hexp, map_sum]
  exact Finset.sum_congr rfl fun j _ => hcomm i j (x j)

/-- **Bicommutant theorem (DJ0).** For a subalgebra `A` of `End_K(V)`, `V` finite-dimensional,
with `V` semisimple as an `A`-module, the double commutant of `A` is `A`. Any field `K`. -/
theorem centralizer_centralizer_eq [FiniteDimensional K V] (A : Subalgebra K (Module.End K V))
    [IsSemisimpleModule A V] :
    Subalgebra.centralizer K
      (Subalgebra.centralizer K (A : Set (Module.End K V)) : Set (Module.End K V)) = A := by
  classical
  refine le_antisymm (fun f hf => ?_) (Subalgebra.le_centralizer_centralizer K)
  let b := Module.finBasis K V
  let v : Fin (finrank K V) → V := fun i => b i
  let W : Submodule A (Fin (finrank K V) → V) := Submodule.span A {v}
  obtain ⟨C, hC⟩ := exists_isCompl W
  let π : (Fin (finrank K V) → V) →ₗ[A] (Fin (finrank K V) → V) :=
    W.subtype ∘ₗ Submodule.linearProjOfIsCompl W C hC
  have hπv : π v = v := by
    have hv : v ∈ W := Submodule.subset_span rfl
    simp only [π, LinearMap.comp_apply]
    rw [show v = ((⟨v, hv⟩ : W) : Fin (finrank K V) → V) from rfl,
      Submodule.linearProjOfIsCompl_apply_left]
    rfl
  have hmem : diag f v ∈ W := by
    rw [← hπv, diag_comm A hf π v]
    exact Submodule.coe_mem _
  obtain ⟨a, ha⟩ := Submodule.mem_span_singleton.1 hmem
  have : (a : Module.End K V) = f := by
    refine b.ext fun i => ?_
    exact congrFun ha i
  rw [← this]
  exact a.2

end QOU.MathlibExt.Bicommutant
