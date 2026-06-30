import QOU.BraidKnot.Specht

/-!
# QOU.BraidKnot.SpechtGarnirCore — toward the Garnir straightening (brick-4 spanning)

The spanning half of the standard-basis theorem (`polytabloid_garnir_core` in
`SpechtSpanningCore`) is the straightening algorithm: every polytabloid is a
combination of *standard* polytabloids. The first, easy ingredient — peeling off
**column standardisation** — is the *column-alternating property* of polytabloids,
proved here sorry-free:

> `polytabloid_rep_colStab` — for a column permutation `σ ∈ C_t`,
> `rep σ (e_t) = sgn(σ) · e_t`. Equivalently (`rep_polytabloid`)
> `e_{σ·t} = sgn(σ) · e_t`: sorting the columns of `t` only changes `e_t` by a sign.

This reduces the straightening obligation to **column-standard** tableaux (the
genuine Garnir-relation residual). The proof reindexes the column-stabiliser sum
by left-multiplication by `σ` (legitimate since `σ ∈ C_t` makes `C_t` invariant)
and uses `sgn(σ)² = 1`.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtGarnirCore

open QOU.BraidKnot.Specht
open Equiv (Perm)

variable {k : Type} [CommRing k]
variable {μ : YoungDiagram}

/-- **Column-alternating property.** A column permutation acts on `e_t` by its sign:
`rep σ (e_t) = sgn(σ) · e_t` for `σ ∈ C_t`. -/
theorem polytabloid_rep_colStab (t : Tableau μ) {σ : Perm (Fin (nOf μ))}
    (hσ : σ ∈ colStab t) :
    Mtab.rep μ σ (polytabloid (k := k) t) = (Equiv.Perm.sign σ : ℤ) • polytabloid (k := k) t := by
  unfold polytabloid
  rw [map_sum, Finset.smul_sum]
  refine Fintype.sum_bijective (fun π : colStab t => (⟨σ, hσ⟩ * π : colStab t))
    (Equiv.mulLeft (⟨σ, hσ⟩ : colStab t)).bijective _ _ (fun π => ?_)
  -- LHS summand at π = RHS summand at σ·π
  have hsq : (Equiv.Perm.sign σ : ℤ) * (Equiv.Perm.sign σ : ℤ) = 1 := by
    simp [← Units.val_mul, Int.units_mul_self]
  have hco : ((⟨σ, hσ⟩ * π : colStab t) : Perm (Fin (nOf μ))) = σ * (π : Perm (Fin (nOf μ))) := by
    rw [Subgroup.coe_mul]
  rw [map_zsmul, Mtab.rep_of,
    ← mul_smul (Equiv.Perm.sign σ : ℤ)
      (Equiv.Perm.sign ((⟨σ, hσ⟩ * π : colStab t) : Perm (Fin (nOf μ))) : ℤ)
      (Mtab.of (k := k) (((⟨σ, hσ⟩ * π : colStab t) : Perm (Fin (nOf μ))) • t)),
    hco, map_mul, Units.val_mul, ← mul_assoc, hsq, one_mul, mul_smul]

end QOU.BraidKnot.SpechtGarnirCore
