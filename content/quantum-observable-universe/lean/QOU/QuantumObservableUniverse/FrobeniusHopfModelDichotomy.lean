import QOU.QuantumObservableUniverse.FrobeniusBialgebraCollapse
import Mathlib.CategoryTheory.Monoidal.Preadditive

/-!
# Every model of `FrobeniusHopfData` is trivial, in the linear setting

`QOU.FrobeniusBialgebraCollapse` proves `ε(1)·x = ε(x)·1`
(`scalar_id_eq_counit_unit`) and reads off one consequence: if `ε(1) = 1` then
`A ≅ 𝟙_C`. This file pushes the same identity the other way and finds that the
escape it seemed to leave open is not one.

## The dichotomy

Write `σ = η ≫ ε : 𝟙_C ⟶ 𝟙_C` for the scalar `ε(1)`.

* `id_factors_through_unitCounit` — the identity on `A` factors through a
  morphism carrying `σ` in the middle. No hypothesis.
* `retract_of_unit_of_isIso` — if `σ` is **invertible**, `A` is a retract of
  the tensor unit.
* `id_eq_zero_of_unitCounit_eq_zero` — if `σ = 0`, then `𝟙_A = 0`, so `A` is a
  zero object. Needs `MonoidalPreadditive`, and nothing else.

In a preadditive monoidal category whose scalars `End (𝟙_C)` form a **field** —
`ModuleCat k`, `FdRep k G`, any `k`-linear abelian monoidal category with simple
unit — every `σ` is either `0` or invertible, so **every** `FrobeniusHopfData`
has `A` a zero object or a retract of `𝟙_C`.

`dichotomy_of_scalars_field` states exactly that, taking the field property as
the hypothesis `∀ σ, σ = 0 ∨ IsIso σ` rather than importing a field structure,
so it applies wherever that disjunction holds.

## What this answers, and what it does not

Bean `qou-aawz` asked for one of two outcomes: exhibit a non-trivial
`FrobeniusHopfData`, or prove the current axioms already force `A = 𝟙`. **This
is the second outcome, restricted to the linear setting**, and it supersedes
the narrower reading recorded on 2026-09-15 — that a non-trivial model merely
needs a non-unital counit. It needs more than that: it needs `ε(1)` to be
neither invertible nor zero, which no field permits.

Two limits, both real:

1. **The zero case needs `MonoidalPreadditive`.** Over a bare monoidal category
   `σ = 0` is not even statable, and this file proves nothing there. Whether a
   non-linear monoidal category admits a non-trivial model is **open**.
2. **A retract of `𝟙_C` need not be `𝟙_C`.** It is when the unit is
   indecomposable, which holds in `ModuleCat k` and in every category with
   simple unit, but "retract of the unit" is the honest general conclusion and
   is what is stated.

## Why this is not a defect to be repaired

It is the classical fact, made exact. A finite-dimensional Hopf algebra is
Frobenius, but its Frobenius comultiplication is **not** its Hopf
comultiplication. `def:frobenius-hopf-substrate` axiom 3 fixes `Δ` as the
Frobenius one and axiom 2 now demands an antipode against *that* `Δ` — so the
two are being forced to coincide, and the collapse is what that costs.

The group algebra is the worked case. `k[G]` with the dual-basis Frobenius
comultiplication has `Δ(1) = Σ_h h ⊗ h⁻¹`, so the convolution of `S(g) = g⁻¹`
with the identity sends `1 ↦ Σ_h h⁻²`, which equals `1` only for the trivial
group. It is a Frobenius algebra and a Hopf algebra and satisfies neither
antipode axiom here, for exactly the reason this file records.

## References

- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
- [kassel1995] C. Kassel, *Quantum Groups*, Springer 1995, Ch. III.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory
open CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.FrobeniusHopfData

universe u v

variable {C : Type u} [Category.{v} C] [MonoidalCategory C]
variable (F : QOU.FrobeniusHopfData C)

/-! ### The identity factors through the scalar `ε(1)` -/

/-- **The Frobenius loop with `ε ≫ η` inserted is the identity.**

    `Δ ≫ (A ◁ (ε ≫ η)) ≫ μ = 𝟙_A`, in elements `Σ ε(x₂)·x₁ = x`.

    This uses only the right counit law and the right unit law — **no antipode
    axiom** — so it holds of any Frobenius object whatever its `S`. -/
theorem frobeniusLoop_counit_unit :
    F.comul ≫ (F.obj ◁ (F.counit ≫ F.unit)) ≫ F.mul = 𝟙 F.obj := by
  rw [MonoidalCategory.whiskerLeft_comp, ← Category.assoc, ← Category.assoc,
    F.comul_counit, Category.assoc, F.mul_one, Iso.inv_hom_id]

/-- **The identity on `A` factors through the scalar `σ = η ≫ ε`.**

    Substituting `scalar_id_eq_counit_unit` into `frobeniusLoop_counit_unit`.
    No hypothesis beyond the structure's own fields.

    Read in elements: `x = ε(1) · (μ ∘ Δ)(x)`. So the whole identity morphism
    is `ε(1)` times something, which is what makes both branches of the
    dichotomy below work. -/
theorem id_factors_through_unitCounit :
    𝟙 F.obj = F.comul ≫ (F.obj ◁ ((λ_ F.obj).inv
        ≫ ((F.unit ≫ F.counit) ▷ F.obj) ≫ (λ_ F.obj).hom)) ≫ F.mul := by
  conv_lhs => rw [← frobeniusLoop_counit_unit F]
  rw [F.scalar_id_eq_counit_unit]

/-! ### Branch one: `ε(1)` invertible -/

/-- If the scalar `σ = η ≫ ε` is invertible, so is `ε ≫ η`. -/
theorem isIso_counit_comp_unit (h : IsIso (F.unit ≫ F.counit)) :
    IsIso (F.counit ≫ F.unit) := by
  rw [F.scalar_id_eq_counit_unit]
  haveI : IsIso ((F.unit ≫ F.counit) ▷ F.obj) :=
    ⟨⟨inv (F.unit ≫ F.counit) ▷ F.obj, by
        rw [← MonoidalCategory.comp_whiskerRight, IsIso.hom_inv_id,
          MonoidalCategory.id_whiskerRight], by
        rw [← MonoidalCategory.comp_whiskerRight, IsIso.inv_hom_id,
          MonoidalCategory.id_whiskerRight]⟩⟩
  infer_instance

/-- **`A` is a retract of the tensor unit** whenever `ε(1)` is invertible.

    The splitting is `A --ε--> 𝟙_C --η ≫ (ε ≫ η)⁻¹--> A`.

    In `ModuleCat k` the unit is `k`, whose only retracts are `0` and `k`, so
    this says `A` is at most one-dimensional. -/
theorem retract_of_unit_of_isIso (h : IsIso (F.unit ≫ F.counit)) :
    ∃ (i : F.obj ⟶ 𝟙_ C) (r : (𝟙_ C : C) ⟶ F.obj), i ≫ r = 𝟙 F.obj := by
  haveI := F.isIso_counit_comp_unit h
  exact ⟨F.counit, F.unit ≫ inv (F.counit ≫ F.unit), by
    rw [← Category.assoc, IsIso.hom_inv_id]⟩

/-! ### Branch two: `ε(1) = 0` -/

/-- **`A` is a zero object** whenever the scalar `ε(1)` vanishes.

    `𝟙_A = 0`, which in any category with zero morphisms makes `A` a zero
    object. Additivity of whiskering is the only extra ingredient; no
    linearity, no field, no antipode beyond what
    `scalar_id_eq_counit_unit` already spent. -/
theorem id_eq_zero_of_unitCounit_eq_zero [Preadditive C] [MonoidalPreadditive C]
    (h : F.unit ≫ F.counit = 0) : 𝟙 F.obj = 0 := by
  rw [id_factors_through_unitCounit F, h]
  simp

/-! ### The dichotomy -/

/-- **No non-trivial model, when the scalars form a field.**

    The hypothesis `hscal` is exactly "`End (𝟙_C)` has no non-zero
    non-invertible element", which holds in `ModuleCat k` for `k` a field and in
    any `k`-linear category with simple unit. It is taken as a hypothesis rather
    than derived from a field instance so that the statement applies wherever
    the disjunction does.

    The conclusion: `A` is a zero object, or a retract of `𝟙_C`. There is no
    third case, and in particular no non-trivial substrate.

    **This is the negative answer to bean `qou-aawz`** in the linear setting. It
    is silent about a bare monoidal category, where `σ = 0` is not statable. -/
theorem dichotomy_of_scalars_field [Preadditive C] [MonoidalPreadditive C]
    (hscal : ∀ σ : (𝟙_ C : C) ⟶ 𝟙_ C, σ = 0 ∨ IsIso σ) :
    𝟙 F.obj = 0
      ∨ ∃ (i : F.obj ⟶ 𝟙_ C) (r : (𝟙_ C : C) ⟶ F.obj), i ≫ r = 𝟙 F.obj := by
  rcases hscal (F.unit ≫ F.counit) with h | h
  · exact Or.inl (F.id_eq_zero_of_unitCounit_eq_zero h)
  · exact Or.inr (F.retract_of_unit_of_isIso h)

end QOU.FrobeniusHopfData
