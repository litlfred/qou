import QOU.BraidKnot.SpechtIrreducible
import QOU.BraidKnot.SpechtCrossKappa
import QOU.BraidKnot.SpechtClassification

/-!
# QOU.BraidKnot.SpechtAbsolutelyIrreducible — the commutant of `S^μ` is the base field

**W2 of the Wedderburn epic (`qou-bxw4`)**: the division rings `𝔇 i` appearing in the abstract
Wedderburn split `WedderburnSn.sn_wedderburnArtin_alg` collapse to the base field `R`. That collapse
is exactly *absolute irreducibility* of the Specht modules, and its module-theoretic content is the
statement proved here:

> every `S_n`-equivariant `k`-linear endomorphism of `S^μ` is a scalar multiple of the identity.

Mathlib supplies the collapse only over an algebraically closed base
(`IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed`, via Schur + algebraic closure); over a
general characteristic-zero field it is a genuine `S_n` fact, and it is the first of the four items
listed as the residual of `SnWedderburnPartitionBridge.sn_isotypic_specht_split`.

## The proof (James/Sagan, on the corpus' own `κ_t` machinery)

No rationality argument and no character theory is needed — the column antisymmetrizer does all the
work, over **any** field of characteristic zero:

1. `κ_t` maps *all* of `M^μ` into the line `k·e_t` (`SpechtIrreducible.kapL_mem_line`, James §4.6 —
   already sorry-free in this corpus, it is the core of the submodule theorem).
2. `κ_t e_t = |C_t| · e_t` (`SpechtCrossKappa.kapL_polytabloid`, from `κ_t² = |C_t| κ_t`).
3. `κ_t` is a `ℤ`-combination of the group action, so an equivariant `θ` commutes with it. Hence
   `|C_t| · θ(e_t) = θ(κ_t e_t) = κ_t (θ e_t) ∈ k·e_t`, and `|C_t| ≠ 0` in characteristic zero gives
   `θ(e_t) = c · e_t` for a single scalar `c`.
4. The polytabloids are a single `S_n`-orbit (`tableau_transitive` +
   `polytabloid_rep_equivariant`), so equivariance propagates that same `c` to every `e_s`; they span
   `S^μ`, so `θ = c · id`.

Step 3 is the step that avoids extending `θ` to `M^μ` — the same manoeuvre
`SpechtClassification.dom_of_kapCross` uses for the cross-shape dominance theorem. This file reuses
that pattern rather than re-deriving it.

## Scope

* Characteristic zero only (step 3 divides by `|C_t|`). Nothing here needs simplicity of `S^μ`, the
  standard basis, dominance, or Garnir straightening.
* This is the **commutant** statement. Turning it into the block-level `𝔇 i ≃ R` of
  `sn_isotypic_specht_split` also needs the labelling (W1) and the block-size identification (W3);
  those are separate items of the epic and are not claimed here.

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]` — matching `SpechtIrreducible` / `SpechtClassification`.
No `ℝ`, no ordering, no `Real.*`: the argument is algebraic.

## References
- [james1984representation] James, *The Representation Theory of the Symmetric Groups*, §4
  (the column antisymmetrizer and the submodule theorem).
- [sagan2001] Sagan, *The Symmetric Group*, §2.4 (Thm 2.4.4 and the `κ_t` manoeuvre).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtAbsolutelyIrreducible

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open Equiv (Perm)

variable {k : Type} [Field k] [CharZero k]

/-- **The commutant computation at one tableau.** An equivariant endomorphism of `S^μ` scales the
polytabloid `e_t`.

This is the whole mathematical content: `κ_t` lands in the line `k·e_t` for *every* input
(`kapL_mem_line`), while on `e_t` itself it acts by the nonzero scalar `|C_t|`
(`kapL_polytabloid`). Equivariance moves `θ` past `κ_t`, and characteristic zero divides. -/
theorem endo_polytabloid_smul {μ : YoungDiagram} (t : Tableau μ)
    (θ : SpechtSubmodule (k := k) μ →ₗ[k] SpechtSubmodule (k := k) μ)
    (hθ : ∀ (σ : Perm (Fin (nOf μ))) (x : SpechtSubmodule (k := k) μ),
      θ (spechtRep (k := k) μ σ x) = spechtRep (k := k) μ σ (θ x)) :
    ∃ c : k, θ ⟨polytabloid (k := k) t, polytabloid_mem_specht t⟩
      = c • (⟨polytabloid (k := k) t, polytabloid_mem_specht t⟩ : SpechtSubmodule (k := k) μ) := by
  classical
  set y : SpechtSubmodule (k := k) μ :=
    ⟨polytabloid (k := k) t, polytabloid_mem_specht t⟩ with hy
  -- `Θ` is `θ` followed by the inclusion `S^μ ↪ M^μ`; working in `M^μ` lets `map_sum` /
  -- `map_nsmul` do the coercion bookkeeping.
  set Θ : SpechtSubmodule (k := k) μ →ₗ[k] Mtab (k := k) μ :=
    (SpechtSubmodule (k := k) μ).subtype ∘ₗ θ with hΘ
  have hΘeq : ∀ (σ : Perm (Fin (nOf μ))) (x : SpechtSubmodule (k := k) μ),
      Θ (spechtRep (k := k) μ σ x) = Mtab.rep μ σ (Θ x) := by
    intro σ x
    show ((θ (spechtRep (k := k) μ σ x) : SpechtSubmodule (k := k) μ) : Mtab (k := k) μ) = _
    rw [hθ, spechtRep_apply_coe]
    rfl
  -- inside `S^μ`, the signed `C_t`-sum of the action on `e_t` is `|C_t| • e_t`.
  have hsum : (∑ π : colStab t,
        (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
          spechtRep (k := k) μ (π : Perm (Fin (nOf μ))) y)
      = (Fintype.card (colStab t)) • y := by
    refine Subtype.ext ?_
    have hL : (((∑ π : colStab t,
          (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
            spechtRep (k := k) μ (π : Perm (Fin (nOf μ))) y) :
              SpechtSubmodule (k := k) μ) : Mtab (k := k) μ)
        = ∑ π : colStab t,
            (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
              Mtab.rep μ (π : Perm (Fin (nOf μ))) (polytabloid (k := k) t) := by
      rw [Submodule.coe_sum]
      exact Finset.sum_congr rfl (fun π _ => rfl)
    rw [hL, ← SpechtIrreducible.kapL_apply, SpechtCrossKappa.kapL_polytabloid]
    simp [hy]
  -- therefore `κ_t (Θ y) = |C_t| • Θ y`: equivariance moves `θ` past the antisymmetrizer.
  have hkap : SpechtIrreducible.kapL (k := k) μ t (Θ y)
      = (Fintype.card (colStab t)) • Θ y := by
    rw [SpechtIrreducible.kapL_apply]
    have hterm : ∀ π : colStab t,
        (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
            Mtab.rep μ (π : Perm (Fin (nOf μ))) (Θ y)
          = Θ ((Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
              spechtRep (k := k) μ (π : Perm (Fin (nOf μ))) y) := by
      intro π
      rw [map_zsmul, hΘeq]
    rw [Finset.sum_congr rfl (fun π _ => hterm π), ← map_sum, hsum, map_nsmul]
  -- but `κ_t` lands in the line `k·e_t` for every input.
  obtain ⟨a, ha⟩ := Submodule.mem_span_singleton.mp
    (SpechtIrreducible.kapL_mem_line (k := k) μ t (Θ y))
  -- so `|C_t| • Θ y = a • e_t`, and `|C_t| ≠ 0` in characteristic zero.
  have hcard : ((Fintype.card (colStab t) : ℕ) : k) ≠ 0 := by
    haveI : Nonempty (colStab t) := ⟨1⟩
    exact Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  have hmain : ((Fintype.card (colStab t) : ℕ) : k) • Θ y = a • polytabloid (k := k) t := by
    rw [Nat.cast_smul_eq_nsmul, ← hkap, ha]
  refine ⟨((Fintype.card (colStab t) : ℕ) : k)⁻¹ * a, ?_⟩
  refine Subtype.ext ?_
  show Θ y = _
  have : Θ y = ((Fintype.card (colStab t) : ℕ) : k)⁻¹ •
      (((Fintype.card (colStab t) : ℕ) : k) • Θ y) := by
    rw [smul_smul, inv_mul_cancel₀ hcard, one_smul]
  rw [this, hmain, smul_smul]
  rfl

/-- **Absolute irreducibility of `S^μ` (the W2 content).** Over a characteristic-zero field, every
`S_n`-equivariant `k`-linear endomorphism of the Specht module `S^μ` is a scalar.

Equivalently: the commutant `End_{k[S_n]}(S^μ)` is `k` itself — no genuine division ring appears,
which is precisely the collapse `𝔇 i ≃ k` that the abstract Wedderburn split
(`WedderburnSn.sn_wedderburnArtin_alg`) leaves open over a non-algebraically-closed base.

`-- Ref: [james1984representation] §4; [sagan2001] §2.4` -/
theorem specht_end_scalar {μ : YoungDiagram}
    (θ : SpechtSubmodule (k := k) μ →ₗ[k] SpechtSubmodule (k := k) μ)
    (hθ : ∀ (σ : Perm (Fin (nOf μ))) (x : SpechtSubmodule (k := k) μ),
      θ (spechtRep (k := k) μ σ x) = spechtRep (k := k) μ σ (θ x)) :
    ∃ c : k, ∀ x : SpechtSubmodule (k := k) μ, θ x = c • x := by
  classical
  obtain ⟨t⟩ := nonempty_tableau μ
  obtain ⟨c, hc⟩ := endo_polytabloid_smul (k := k) t θ hθ
  refine ⟨c, ?_⟩
  -- the polytabloids form a single `S_n`-orbit, so the scalar propagates to all of them.
  have hgen : ∀ s : Tableau μ,
      θ ⟨polytabloid (k := k) s, polytabloid_mem_specht s⟩
        = c • (⟨polytabloid (k := k) s, polytabloid_mem_specht s⟩ :
            SpechtSubmodule (k := k) μ) := by
    intro s
    obtain ⟨σ, hσ⟩ := SpechtIrreducible.tableau_transitive t s
    have hcoe : (⟨polytabloid (k := k) s, polytabloid_mem_specht s⟩ :
          SpechtSubmodule (k := k) μ)
        = spechtRep (k := k) μ σ ⟨polytabloid (k := k) t, polytabloid_mem_specht t⟩ := by
      refine Subtype.ext ?_
      rw [spechtRep_apply_coe]
      show polytabloid (k := k) s = Mtab.rep μ σ (polytabloid (k := k) t)
      rw [SpechtIrreducible.polytabloid_rep_equivariant, hσ]
    rw [hcoe, hθ, hc, map_smul]
  -- and they span `S^μ`.
  have key : ∀ (v : Mtab (k := k) μ) (hv : v ∈ SpechtSubmodule (k := k) μ),
      θ ⟨v, hv⟩ = c • (⟨v, hv⟩ : SpechtSubmodule (k := k) μ) := by
    intro v hv
    induction hv using Submodule.span_induction with
    | mem w hw =>
        obtain ⟨s, rfl⟩ := hw
        exact hgen s
    | zero =>
        show θ 0 = c • (0 : SpechtSubmodule (k := k) μ)
        rw [map_zero, smul_zero]
    | add u w hu hw ihu ihw =>
        show θ (⟨u, hu⟩ + ⟨w, hw⟩) = c • ((⟨u, hu⟩ : SpechtSubmodule (k := k) μ) + ⟨w, hw⟩)
        rw [map_add, ihu, ihw, smul_add]
    | smul r u hu ihu =>
        show θ (r • (⟨u, hu⟩ : SpechtSubmodule (k := k) μ))
          = c • (r • (⟨u, hu⟩ : SpechtSubmodule (k := k) μ))
        rw [map_smul, ihu, smul_comm]
  intro x
  exact key x.1 x.2

/-- The scalar in `specht_end_scalar` is **unique**: `S^μ` is nonzero (it contains a nonzero
polytabloid), so two scalars agreeing on it are equal. -/
theorem specht_end_scalar_unique {μ : YoungDiagram} {c d : k}
    (h : ∀ x : SpechtSubmodule (k := k) μ, c • x = d • x) : c = d := by
  classical
  obtain ⟨t⟩ := nonempty_tableau μ
  have hx := h ⟨polytabloid (k := k) t, polytabloid_mem_specht t⟩
  have hcoe : c • polytabloid (k := k) t = d • polytabloid (k := k) t :=
    congrArg (fun z : SpechtSubmodule (k := k) μ => (z : Mtab (k := k) μ)) hx
  have hsub : (c - d) • polytabloid (k := k) t = 0 := by
    rw [sub_smul, hcoe, sub_self]
  rcases smul_eq_zero.mp hsub with h0 | h0
  · exact sub_eq_zero.mp h0
  · exact absurd h0 (SpechtCrossKappa.polytabloid_ne_zero (K := k) μ t)

/-- **The commutant is commutative.** An immediate consequence of `specht_end_scalar`: any two
equivariant endomorphisms of `S^μ` commute, since both are scalars. This is the form in which the
Wedderburn block collapse consumes absolute irreducibility — a noncommutative division ring `𝔇 i`
would supply a noncommuting pair. -/
theorem specht_end_comm {μ : YoungDiagram}
    (θ ψ : SpechtSubmodule (k := k) μ →ₗ[k] SpechtSubmodule (k := k) μ)
    (hθ : ∀ (σ : Perm (Fin (nOf μ))) (x : SpechtSubmodule (k := k) μ),
      θ (spechtRep (k := k) μ σ x) = spechtRep (k := k) μ σ (θ x))
    (hψ : ∀ (σ : Perm (Fin (nOf μ))) (x : SpechtSubmodule (k := k) μ),
      ψ (spechtRep (k := k) μ σ x) = spechtRep (k := k) μ σ (ψ x)) :
    θ ∘ₗ ψ = ψ ∘ₗ θ := by
  obtain ⟨c, hc⟩ := specht_end_scalar (k := k) θ hθ
  obtain ⟨d, hd⟩ := specht_end_scalar (k := k) ψ hψ
  refine LinearMap.ext fun x => ?_
  show θ (ψ x) = ψ (θ x)
  rw [hc, hd, hc, map_smul, hd, smul_comm]

/-! ## The division-ring collapse, at module level

`specht_end_scalar` is a statement about Specht modules. The Wedderburn blocks are indexed by the
*simple* `k[S_n]`-modules, and a block's division ring `𝔇 i` **is** the commutant of the
corresponding simple. Composing with the classification theorem
(`SpechtClassification.specht_exhausts_irreducibles` — every simple `k[S_n]`-module is a Specht
module, closed by a sibling in the 2026-08 window) upgrades the Specht statement to the general one:
**no simple `k[S_n]`-module admits a non-scalar equivariant endomorphism**, over any
characteristic-zero field. That is item (a) of the residual listed in
`SnWedderburnPartitionBridge`, in module-theoretic form.

What it is *not*: the block-level `𝔇 i ≃ R` inside a specific `∏ Matrix` split still needs the
index↔partition labelling (W1) to say *which* simple sits in block `i`. That is a separate epic
item; nothing here claims it. -/

/-- **No simple `k[S_n]`-module has a non-scalar commutant.** Over a characteristic-zero field, every
`S_n`-equivariant `k`-linear endomorphism of a simple `k[S_n]`-module is a scalar.

Proof: transport an equivariant endomorphism along the classification isomorphism to the Specht
model, apply `specht_end_scalar`, and transport back. The intertwiner is a `k`-linear equivalence, so
the scalar is preserved.

This is the module-theoretic form of the division-ring collapse: the commutant of a simple module is
its Wedderburn block's division ring, and here it is the base field itself. -/
theorem simple_end_scalar {n : ℕ} {W : Type} [AddCommGroup W] [Module k W]
    (ρ : Representation k (Perm (Fin n)) W)
    (hsimple : IsSimpleModule (MonoidAlgebra k (Perm (Fin n))) ρ.asModule)
    (θ : W →ₗ[k] W)
    (hθ : ∀ (g : Perm (Fin n)) (x : W), θ (ρ g x) = ρ g (θ x)) :
    ∃ c : k, ∀ x : W, θ x = c • x := by
  classical
  obtain ⟨μ, h, hiso⟩ := specht_exhausts_irreducibles (k := k) ρ hsimple
  obtain ⟨e, he⟩ := hiso.exists_intertwiner
  -- `ψ = e ∘ θ ∘ e⁻¹` is an equivariant endomorphism of the Specht model.
  set ψ : SpechtSubmodule (k := k) μ →ₗ[k] SpechtSubmodule (k := k) μ :=
    (e : W →ₗ[k] SpechtSubmodule (k := k) μ) ∘ₗ θ ∘ₗ (e.symm : _ →ₗ[k] W) with hψdef
  have hψ : ∀ (σ : Perm (Fin (nOf μ))) (y : SpechtSubmodule (k := k) μ),
      ψ (spechtRep (k := k) μ σ y) = spechtRep (k := k) μ σ (ψ y) := by
    intro σ y
    obtain ⟨g, rfl⟩ := transportPermHom_surjective h.symm σ
    -- `e⁻¹` intertwines the other way: `e⁻¹ (ρ' g y) = ρ g (e⁻¹ y)`.
    have hback : e.symm (spechtRep (k := k) μ (transportPermHom h.symm g) y)
        = ρ g (e.symm y) := by
      have := he g (e.symm y)
      rw [e.apply_symm_apply] at this
      exact (e.symm_apply_eq).mpr this.symm
    show e (θ (e.symm (spechtRep (k := k) μ (transportPermHom h.symm g) y)))
      = spechtRep (k := k) μ (transportPermHom h.symm g) (e (θ (e.symm y)))
    rw [hback, hθ]
    exact he g (θ (e.symm y))
  obtain ⟨c, hc⟩ := specht_end_scalar (k := k) ψ hψ
  refine ⟨c, fun x => ?_⟩
  have hx : e (θ x) = e (c • x) := by
    have := hc (e x)
    rw [hψdef] at this
    simpa [LinearEquiv.symm_apply_apply, map_smul] using this
  exact e.injective hx

/-- Any equivariant endomorphism of a simple `S_n`-module has a scalar multiple from which its pointwise difference vanishes. -/
theorem simple_end_sub_scalar_eq_zero {n : ℕ} {W : Type} [AddCommGroup W] [Module k W]
    (ρ : Representation k (Perm (Fin n)) W)
    (hsimple : IsSimpleModule (MonoidAlgebra k (Perm (Fin n))) ρ.asModule)
    (θ : W →ₗ[k] W)
    (hθ : ∀ (g : Perm (Fin n)) (x : W), θ (ρ g x) = ρ g (θ x)) :
    ∃ c : k, ∀ x : W, θ x - c • x = 0 := by
  obtain ⟨c, hc⟩ := simple_end_scalar (k := k) ρ hsimple θ hθ
  exact ⟨c, fun x => sub_eq_zero.mpr (hc x)⟩

end QOU.BraidKnot.SpechtAbsolutelyIrreducible
