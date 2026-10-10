import QOU.Hecke.HeckeDimension
import QOU.Hecke.TwIndependent
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# QOU.Hecke.TwBasisField — over a field, the `T_w` ARE a basis

The end of the type-`A` route (bean `qou-twwf`).  Two independent halves meet:

* `QOU.Hecke.HeckeDimension.exists_spanning_finset` — `H_n(q)` is spanned by at
  most `(n+1)!` elements, so `dim_K H_n(q) ≤ (n+1)!`;
* `QOU.Hecke.TwBasis.orbitMap_surjective` — the action on `T_1` is onto the free
  module of rank `(n+1)!`, so `dim_K H_n(q) ≥ (n+1)!`.

Equal finite dimension turns the surjection into an isomorphism, which is
exactly the hypothesis `QOU.Hecke.TwBasis.basisTw` was left carrying.

## What is proved

* `finrank_eq_factorial` — `dim_K H_n(q) = (n+1)!`.
* `orbitMap_injective` — the hypothesis of `basisTw`, discharged.
* `basisTwOfField` — **the `T_w` are a basis of `H_n(q)`**, unconditionally.

## Why a field

Only here.  Everything upstream — the Coxeter bridge, the `Rs` relations, the
representation, the spanning bound, the independence — holds over an arbitrary
commutative ring.  The dimension squeeze is the one step that uses invertibility,
so if the basis is ever wanted over `ℤ[q,q⁻¹]` this is the file to redo, and
nothing before it.

Matsumoto's theorem is never used; see `QOU.Hecke.TwIndependent` for why the
choice of reduced word does not matter.
-/

namespace QOU.Hecke.TwBasis

open QOU.Hecke.IwahoriHecke

variable (K : Type*) [Field K] (q : K) (n : ℕ)

instance instFiniteIwahoriHecke : Module.Finite K (QOU.Hecke.IwahoriHecke K q n) := by
  obtain ⟨s, _, hspan⟩ := exists_spanning_finset K q n
  exact ⟨⟨s, hspan⟩⟩

theorem finrank_le_factorial :
    Module.finrank K (QOU.Hecke.IwahoriHecke K q n) ≤ Nat.factorial (n + 1) := by
  obtain ⟨s, hcard, hspan⟩ := exists_spanning_finset K q n
  calc Module.finrank K (QOU.Hecke.IwahoriHecke K q n)
      = Module.finrank K (Submodule.span K (s : Set (QOU.Hecke.IwahoriHecke K q n))) := by
        rw [hspan, finrank_top]
    _ ≤ s.card := finrank_span_finset_le_card s
    _ ≤ Nat.factorial (n + 1) := hcard

theorem finrank_finsupp_perm :
    Module.finrank K (Equiv.Perm (Fin (n + 1)) →₀ K) = Nat.factorial (n + 1) := by
  rw [Module.finrank_finsupp_self, Fintype.card_perm, Fintype.card_fin]

theorem factorial_le_finrank :
    Nat.factorial (n + 1) ≤ Module.finrank K (QOU.Hecke.IwahoriHecke K q n) := by
  have hrange : LinearMap.range (orbitMap K q n) = ⊤ :=
    LinearMap.range_eq_top.mpr (orbitMap_surjective K q n)
  calc Nat.factorial (n + 1)
      = Module.finrank K (Equiv.Perm (Fin (n + 1)) →₀ K) :=
        (finrank_finsupp_perm K n).symm
    _ = Module.finrank K (LinearMap.range (orbitMap K q n)) := by rw [hrange, finrank_top]
    _ ≤ Module.finrank K (QOU.Hecke.IwahoriHecke K q n) := LinearMap.finrank_range_le _

/-- **`dim_K H_n(q) = (n+1)!`.** -/
theorem finrank_eq_factorial :
    Module.finrank K (QOU.Hecke.IwahoriHecke K q n) = Nat.factorial (n + 1) :=
  le_antisymm (finrank_le_factorial K q n) (factorial_le_finrank K q n)

/-- **The action on `T_1` is faithful** — the hypothesis `basisTw` was carrying. -/
theorem orbitMap_injective : Function.Injective (orbitMap K q n) := by
  have heq : Module.finrank K (QOU.Hecke.IwahoriHecke K q n)
      = Module.finrank K (Equiv.Perm (Fin (n + 1)) →₀ K) := by
    rw [finrank_eq_factorial, finrank_finsupp_perm K n]
  exact (LinearMap.injective_iff_surjective_of_finrank_eq_finrank heq).mpr
    (orbitMap_surjective K q n)

/-- **The `T_w` are a basis of `H_n(q)`**, over a field, with no hypothesis and
    no appeal to Matsumoto's theorem. -/
noncomputable def basisTwOfField :
    Module.Basis (Equiv.Perm (Fin (n + 1))) K (QOU.Hecke.IwahoriHecke K q n) :=
  basisTw K q n (orbitMap_injective K q n)

@[simp] theorem coe_basisTwOfField : ⇑(basisTwOfField K q n) = Tw K q n :=
  coe_basisTw K q n _

end QOU.Hecke.TwBasis
