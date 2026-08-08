import Mathlib.RepresentationTheory.Invariants
import Mathlib.RepresentationTheory.Character
import Mathlib.LinearAlgebra.Contraction
import Mathlib.LinearAlgebra.Trace

/-!
# Characters of a `Representation`, without the category layer

Mathlib's character theory (`FDRep.character`, `char_linHom`,
`average_char_eq_finrank_invariants`, `scalar_product_char_eq_finrank_equivariant`)
is stated for `FDRep k G`, the *category* of finite-dimensional representations.
Code that carries a bare `Representation k G V` — as the Specht cluster does —
cannot use any of it without first building a bridge through
`Rep k G ≌ ModuleCat (MonoidAlgebra k G)` and the full subcategory inclusion
`FDRep ⥤ Rep`, and Mathlib has no lemma relating `CategoryTheory.Simple` in
`FDRep k G` to `IsSimpleModule (MonoidAlgebra k G)`.

This file redevelops the part of the theory that is needed, directly on
`Representation`. Every proof is the `FDRep` one with the category layer removed;
the ingredients (`Representation.dualTensorHom_comm`,
`Representation.isProj_averageMap`, `LinearMap.trace_conj'`,
`trace_tensorProduct'`, `trace_transpose'`) are all already `Representation`- or
`LinearMap`-level.

## Why it is wanted

For the completeness half of the Specht classification the chain is

  `#{pairwise non-isomorphic simples} ≤ #conj classes ≤ #partitions`,

whose left step is linear independence of the characters. That rests on

  `⅟|G| • Σ_g χ_V(g⁻¹) · χ_W(g) = finrank_k Hom_G(V, W)`

— `charPairing_eq_finrank_homG` below. Note it needs **no algebraically closed
field**: only `Invertible (|G| : k)`, which characteristic zero supplies.
`FDRep.char_orthonormal` does carry `[IsAlgClosed k]`, but only to pin the
diagonal to `1`; a *bound* does not need that, and the diagonal being merely
nonzero is enough for independence.
-/

open scoped BigOperators TensorProduct

namespace QOU.MathlibExt.RepresentationCharacter

open Representation LinearMap Module

variable {k G V W : Type*} [Field k] [Group G]
  [AddCommGroup V] [Module k V] [AddCommGroup W] [Module k W]

/-- The **character** of a representation: `g ↦ tr (ρ g)`. -/
noncomputable def charOf (ρ : Representation k G V) (g : G) : k := LinearMap.trace k V (ρ g)

@[simp] theorem charOf_apply (ρ : Representation k G V) (g : G) :
    charOf ρ g = LinearMap.trace k V (ρ g) := rfl

/-- Characters are class functions: `tr` is conjugation-invariant. -/
theorem charOf_conj (ρ : Representation k G V) (g h : G) :
    charOf ρ (h * g * h⁻¹) = charOf ρ g := by
  simp only [charOf, map_mul]
  rw [LinearMap.trace_mul_comm, ← mul_assoc, ← map_mul, inv_mul_cancel, map_one, one_mul]

/-! ## 1. The character of `Hom_k(V, W)`

`linHom ρV ρW` is conjugate to `dual ρV ⊗ ρW` through `dualTensorHomEquiv`, so
its trace is the product of the two traces.  This is `FDRep.char_linHom` with
the monoidal-category step replaced by `Representation.dualTensorHom_comm`. -/

section LinHom

-- `trace` and `trace_comp_comm'` live over `CommRing`. Stating this whole file
-- over `CommRing` rather than `Field` avoids an instance diamond: elaborating
-- against `[Field k]` produces the `Field → Semifield → … → Semiring` path while
-- Mathlib's trace lemmas carry `CommRing → CommSemiring → Semiring`, and `rw`
-- cannot bridge the two.
variable [Module.Free k V] [Module.Finite k V] [Module.Free k W] [Module.Finite k W]

omit [Module.Free k W] [Module.Finite k W] in
/-- `dualTensorHom` intertwines `dual ρV ⊗ ρW` with `linHom ρV ρW` — the
`∘ₗ` form of `Representation.dualTensorHom_comm`, kept as composites rather than
as a `LinearEquiv.conj` because the conjugation form makes `isDefEq` unfold
`dualTensorHomEquiv` and diverge. -/
theorem linHom_comp (ρV : Representation k G V) (ρW : Representation k G W) (g : G) :
    ((linHom ρV ρW) g : (V →ₗ[k] W) →ₗ[k] (V →ₗ[k] W)) ∘ₗ
        (dualTensorHomEquiv k V W : Module.Dual k V ⊗[k] W →ₗ[k] (V →ₗ[k] W))
      = (dualTensorHomEquiv k V W : Module.Dual k V ⊗[k] W →ₗ[k] (V →ₗ[k] W)) ∘ₗ
          TensorProduct.map (ρV.dual g) (ρW g) :=
  (Representation.dualTensorHom_comm ρV ρW g).symm

/-- **`χ_{Hom(V,W)}(g) = χ_V(g⁻¹) · χ_W(g)`.**

The trace is moved across `dualTensorHomEquiv` with `trace_comp_comm'` rather
than `trace_conj'`: the latter needs `Module.End k (V* ⊗ W)` unified with
`(V* ⊗ W) →ₗ[k] (V* ⊗ W)`, which sends `isDefEq` into `dualTensorHomEquiv`'s
definition and does not terminate within a million heartbeats. Composites keep
everything at the `→ₗ` level. -/
theorem charOf_linHom (ρV : Representation k G V) (ρW : Representation k G W) (g : G) :
    charOf (linHom ρV ρW) g = charOf ρV g⁻¹ * charOf ρW g := by
  set e := (dualTensorHomEquiv k V W).toLinearMap with he
  set B := TensorProduct.map (ρV.dual g) (ρW g) with hB
  set e' := (dualTensorHomEquiv k V W).symm.toLinearMap with he'
  have hee : e' ∘ₗ e = LinearMap.id := by
    refine LinearMap.ext (fun x => ?_)
    simp [he, he']
  -- `A = e ∘ₗ B ∘ₗ e'`, so `tr A = tr ((B ∘ₗ e') ∘ₗ e) = tr B`
  have hA : ((linHom ρV ρW) g : (V →ₗ[k] W) →ₗ[k] (V →ₗ[k] W)) = e ∘ₗ (B ∘ₗ e') := by
    refine LinearMap.ext (fun f => ?_)
    have h := congrArg (fun m => m (e' f)) (linHom_comp ρV ρW g)
    simp only [LinearMap.coe_comp, Function.comp_apply] at h ⊢
    rw [show e (e' f) = f from by simp [he, he']] at h
    exact h
  have htr : LinearMap.trace k (V →ₗ[k] W) ((linHom ρV ρW) g)
      = LinearMap.trace k (Module.Dual k V ⊗[k] W) B := by
    have hcyc := LinearMap.trace_comp_comm' (R := k) (M := V →ₗ[k] W)
      (N := Module.Dual k V ⊗[k] W) (B ∘ₗ e') e
    rw [hA, hcyc, LinearMap.comp_assoc, hee, LinearMap.comp_id]
  have hV : LinearMap.trace k (Module.Dual k V) (ρV.dual g) = charOf ρV g⁻¹ :=
    LinearMap.trace_transpose' (ρV g⁻¹)
  have hW : LinearMap.trace k W (ρW g) = charOf ρW g := rfl
  rw [charOf, htr, hB, LinearMap.trace_tensorProduct', hV, hW]

end LinHom

/-! ## 2. Averaging: the mean of the character is the dimension of the invariants

`Representation.isProj_averageMap` says the group average is a projection onto
`invariants`; the trace of a projection is the rank of its image. -/

section Average

variable [Fintype G] [Invertible (Fintype.card G : k)]
  [Module.Free k V] [Module.Finite k V]

omit [Module.Free k V] in
/-- **`⅟|G| • Σ_g χ_ρ(g) = dim_k ρ^G`.**  `FDRep.average_char_eq_finrank_invariants`
without the category layer. -/
theorem average_charOf (ρ : Representation k G V) :
    ⅟(Fintype.card G : k) • ∑ g : G, charOf ρ g = finrank k (invariants ρ) := by
  rw [← (isProj_averageMap ρ).trace]
  simp [charOf, averageMap, GroupAlgebra.average, _root_.map_sum]

end Average

/-! ## 3. `Hom_G(V, W)` as the invariants of `linHom`

`Representation.mem_invariants_iff_comm` identifies the invariants of
`linHom ρV ρW` with the `G`-equivariant maps, so no `Rep`/`FDRep` object is
needed to talk about `Hom_G`. -/

/-- The space of `G`-equivariant `k`-linear maps `V → W`, as a submodule of
`V →ₗ[k] W`. -/
noncomputable def homG (ρV : Representation k G V) (ρW : Representation k G W) :
    Submodule k (V →ₗ[k] W) :=
  invariants (linHom ρV ρW)

theorem mem_homG_iff {ρV : Representation k G V} {ρW : Representation k G W}
    {f : V →ₗ[k] W} :
    f ∈ homG ρV ρW ↔ ∀ (g : G) (v : V), f (ρV g v) = ρW g (f v) := by
  constructor
  · intro hf g v
    have := congrArg (fun m : V →ₗ[k] W => m (ρV g v)) (hf g)
    simpa [linHom] using this.symm
  · intro hf g
    refine LinearMap.ext (fun v => ?_)
    show ρW g (f (ρV g⁻¹ v)) = f v
    rw [hf g⁻¹ v, ← Module.End.mul_apply, ← map_mul, mul_inv_cancel, map_one]
    rfl

/-- **The character pairing computes `dim Hom_G(V, W)`.**

  `⅟|G| • Σ_g χ_V(g⁻¹) · χ_W(g) = dim_k Hom_G(V, W)`

No algebraically closed field, and no `Simple` hypothesis: this is the general
identity from which both the vanishing on non-isomorphic simples and the nonzero
diagonal are read off. -/
theorem charPairing_eq_finrank_homG [Fintype G] [Invertible (Fintype.card G : k)]
    [Module.Free k V] [Module.Finite k V] [Module.Free k W] [Module.Finite k W]
    (ρV : Representation k G V) (ρW : Representation k G W) :
    ⅟(Fintype.card G : k) • ∑ g : G, charOf ρV g⁻¹ * charOf ρW g
      = finrank k (homG ρV ρW) := by
  unfold homG
  rw [← average_charOf (linHom ρV ρW)]
  congr 1
  exact Finset.sum_congr rfl (fun g _ => (charOf_linHom ρV ρW g).symm)

end QOU.MathlibExt.RepresentationCharacter
