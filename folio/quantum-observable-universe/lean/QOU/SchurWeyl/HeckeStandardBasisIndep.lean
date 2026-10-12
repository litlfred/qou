import QOU.SchurWeyl.HeckeMultiplicationRule
import QOU.SchurWeyl.HeckeWedderburnGeneral

/-!
# QOU.SchurWeyl.HeckeStandardBasisIndep — the `T_w` form a basis at generic `q`

Over a field `K` of characteristic zero, with `q ≠ 0` not a root of unity and `qi = q⁻¹`, the
elements `T_w = stdElt m w` for `w ∈ S_{m+1}` are linearly independent, so they form a basis of
`H_{m+1}(q)` (`stdBasis`).

## Proof

* The `T_w` span: they are the coset family reindexed by permutations
  (`HeckeCoset.span_cosetFam_eq_top`).
* There are `(m+1)!` of them, and `dim H_{m+1}(q) = (m+1)!` at generic `q`
  (`finrank_hecke_eq_factorial`, via the Wedderburn surjection).
* A spanning family whose size is the dimension is a basis.

## Scope

This is the generic-parameter statement only.  Over an arbitrary commutative ring (for example
`ℤ[q, q⁻¹]`, or `q` a root of unity) linear independence is not proved here; that needs the
regular representation, and is not done.

## Base ring (§7c)

`[Field K] [CharZero K]`, the hypotheses of `finrank_hecke_eq_factorial`.  Nothing archimedean.

LaTeX label: `thm:hecke-standard-basis-generic`

-- Ref: [geckpfeiffer2000] https://doi.org/10.1093/oso/9780198502500.001.0001 (Thm 4.4.6: the `T_w` form a basis)
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke Equiv

/-- The `T_w` span `H_{m+1}(q)`, over any commutative ring. -/
theorem span_stdElt_eq_top {K : Type*} [CommRing K] {q qi : K} (m : ℕ) :
    Submodule.span K (Set.range (stdElt (K := K) (q := q) (qi := qi) m)) = ⊤ := by
  have h : stdElt (K := K) (q := q) (qi := qi) m = cosetFam m ∘ (permOfEquiv m).symm := rfl
  rw [h, (permOfEquiv m).symm.surjective.range_comp]
  exact span_cosetFam_eq_top m

variable {K : Type*} [Field K] [CharZero K] (q : K) (hq0 : q ≠ 0)
  (hq2 : GenericParameter.NotRootOfUnity q)

include hq0 hq2 in
/-- **The `T_w` are linearly independent** at generic `q`. -/
theorem stdElt_linearIndependent (m : ℕ) :
    LinearIndependent K (stdElt (K := K) (q := q) (qi := q⁻¹) m) := by
  haveI := finiteDimensional_hecke q q⁻¹ m
  refine linearIndependent_of_top_le_span_of_card_eq_finrank (span_stdElt_eq_top m).ge ?_
  rw [Fintype.card_perm, Fintype.card_fin, finrank_hecke_eq_factorial q hq0 hq2 m]

include hq0 hq2 in
/-- **The standard basis** `{T_w : w ∈ S_{m+1}}` of `H_{m+1}(q)` at generic `q`. -/
noncomputable def stdBasis (m : ℕ) : Module.Basis (Perm (Fin (m + 1))) K (Hecke K q q⁻¹ m) :=
  haveI := finiteDimensional_hecke q q⁻¹ m
  basisOfLinearIndependentOfCardEqFinrank (stdElt_linearIndependent q hq0 hq2 m)
    (by rw [Fintype.card_perm, Fintype.card_fin, finrank_hecke_eq_factorial q hq0 hq2 m])

include hq0 hq2 in
theorem stdBasis_apply (m : ℕ) (w : Perm (Fin (m + 1))) :
    stdBasis q hq0 hq2 m w = stdElt m w := by
  simp only [stdBasis, coe_basisOfLinearIndependentOfCardEqFinrank]

end HeckeCoset
end QOU.SchurWeyl
