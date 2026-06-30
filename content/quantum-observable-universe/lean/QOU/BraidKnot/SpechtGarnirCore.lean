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

/-! ## 2. The abstract antisymmetriser

For a finite group `H ≤ S_n`, the antisymmetriser `b_H x = Σ_{σ∈H} sgn(σ)·(σ·x)`.
Two abstract facts power every Garnir relation:

* `antisym_rep` — `b_H` is *alternating*: `τ·(b_H x) = sgn(τ)·b_H x` for `τ ∈ H`.
* `antisym_eq_zero` — if a sign-`(−1)` involution `τ ∈ H` *fixes* `x`, then `b_H x = 0`
  (the sign-reversing pairing `σ ↦ στ` cancels termwise — no characteristic
  assumption). This is the vanishing that makes a Garnir element kill `e_t`.
-/

/-- The **antisymmetriser** over a finite subgroup `H`. -/
noncomputable def antisym (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    (x : Mtab (k := k) μ) : Mtab (k := k) μ :=
  ∑ σ : H, (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) • Mtab.rep μ (σ : Perm (Fin (nOf μ))) x

/-- **Alternating property.** `τ · (b_H x) = sgn(τ) · b_H x` for `τ ∈ H`. -/
theorem antisym_rep (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    {τ : Perm (Fin (nOf μ))} (hτ : τ ∈ H) (x : Mtab (k := k) μ) :
    Mtab.rep μ τ (antisym (k := k) H x) = (Equiv.Perm.sign τ : ℤ) • antisym (k := k) H x := by
  unfold antisym
  rw [map_sum, Finset.smul_sum]
  refine Fintype.sum_bijective (fun σ : H => (⟨τ, hτ⟩ * σ : H))
    (Equiv.mulLeft (⟨τ, hτ⟩ : H)).bijective _ _ (fun σ => ?_)
  have hsq : (Equiv.Perm.sign τ : ℤ) * (Equiv.Perm.sign τ : ℤ) = 1 := by
    simp [← Units.val_mul, Int.units_mul_self]
  have hco : ((⟨τ, hτ⟩ * σ : H) : Perm (Fin (nOf μ))) = τ * (σ : Perm (Fin (nOf μ))) := by
    rw [Subgroup.coe_mul]
  rw [map_zsmul,
    show Mtab.rep μ τ (Mtab.rep μ (σ : Perm (Fin (nOf μ))) x)
        = Mtab.rep μ (τ * (σ : Perm (Fin (nOf μ)))) x from by rw [map_mul]; rfl,
    ← mul_smul (Equiv.Perm.sign τ : ℤ)
      (Equiv.Perm.sign ((⟨τ, hτ⟩ * σ : H) : Perm (Fin (nOf μ))) : ℤ)
      (Mtab.rep μ ((⟨τ, hτ⟩ * σ : H) : Perm (Fin (nOf μ))) x),
    hco]
  congr 1
  rw [map_mul, Units.val_mul, ← mul_assoc, hsq, one_mul]

/-- **Vanishing.** A sign-`(−1)` involution `τ ∈ H` fixing `x` forces `b_H x = 0`. -/
theorem antisym_eq_zero (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    {τ : Perm (Fin (nOf μ))} (hτ : τ ∈ H) (hτ2 : τ * τ = 1)
    (hsgn : Equiv.Perm.sign τ = -1) (x : Mtab (k := k) μ) (hfix : Mtab.rep μ τ x = x) :
    antisym (k := k) H x = 0 := by
  unfold antisym
  refine Finset.sum_involution (fun σ _ => σ * ⟨τ, hτ⟩) ?_ ?_ (fun σ _ => Finset.mem_univ _) ?_
  · intro σ _
    have hco : ((σ * ⟨τ, hτ⟩ : H) : Perm (Fin (nOf μ))) = (σ : Perm (Fin (nOf μ))) * τ := by
      rw [Subgroup.coe_mul]
    have hsg : (Equiv.Perm.sign ((σ * ⟨τ, hτ⟩ : H) : Perm (Fin (nOf μ))) : ℤ)
        = -(Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) := by
      rw [hco, map_mul, hsgn]; push_cast; ring
    have hre : Mtab.rep μ ((σ * ⟨τ, hτ⟩ : H) : Perm (Fin (nOf μ))) x
        = Mtab.rep μ (σ : Perm (Fin (nOf μ))) x := by
      rw [hco, map_mul]
      show Mtab.rep μ (σ : Perm (Fin (nOf μ))) (Mtab.rep μ τ x) = Mtab.rep μ (σ : Perm (Fin (nOf μ))) x
      rw [hfix]
    rw [hsg, hre, neg_smul, add_neg_cancel]
  · intro σ _ _ hcon
    have hone : (⟨τ, hτ⟩ : H) = 1 := mul_left_cancel (a := σ) (by rw [mul_one]; exact hcon)
    have hτ1 : τ = 1 := by
      have h := congrArg (fun y : H => (y : Perm (Fin (nOf μ)))) hone
      simpa using h
    rw [hτ1, Equiv.Perm.sign_one] at hsgn
    exact absurd hsgn (by decide)
  · intro σ _
    ext1
    rw [Subgroup.coe_mul, Subgroup.coe_mul]
    show (σ : Perm (Fin (nOf μ))) * τ * τ = (σ : Perm (Fin (nOf μ)))
    rw [mul_assoc, hτ2, mul_one]

end QOU.BraidKnot.SpechtGarnirCore
