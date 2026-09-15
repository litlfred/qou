import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Conv
import Mathlib.CategoryTheory.Monoidal.Hopf_

/-!
# The antipode is determined, and `S² = id` is not

Companion to `QOU.AntipodeIndependence`, which records the state of
`def:frobenius-hopf-substrate` **before** 2026-09-14: `S` was named by the
definition and constrained by no law, so every question about it was
*independent* rather than open.

The antipode axioms `antipode_left` / `antipode_right` were added on owner
decision (beans `qou-c64q`, `qou-qjhc`). This file records what that buys and
what it does not.

## What it buys: `S` stops being data

`antipode_unique` — an antipode, if one exists, is **unique**. So `antipode`
is no longer a free field: it is determined by `(μ, η, Δ, ε)`, and a
`FrobeniusHopfData` cannot carry a "wrong" one.

The proof is the standard convolution argument, and it is exactly why the six
algebra / coalgebra laws had to be added alongside the two antipode laws: the
convolution product `f * g = Δ ≫ f ▷ A ≫ A ◁ g ≫ μ` is a **monoid** only
given associativity, coassociativity and the four unit/counit laws, and
inverses are unique only in a monoid. Mathlib supplies that monoid
(`CategoryTheory.Conv`); `toMonObj` / `toComonObj` below are the field-for-field
transports that make it applicable.

## What it does NOT buy: `S² = id`

`S² = id` does **not** follow from the antipode axioms. Two independent
pieces of evidence, neither of them this file's own reasoning:

1. **Mathlib's own theorem carries the hypothesis.**
   `HopfObj.antipode_antipode` is stated *"In a commutative
   Hopf algebra, the antipode squares to the identity"* and takes
   `comm : (β_ A A).hom ≫ μ[A] = μ[A]` as an explicit argument.
   `antipode_sq_of_comm` below re-exports it so the dependence on `comm` is
   visible from inside this corpus rather than asserted about it.
2. **The standard counterexamples are q-deformations.** For `U_q(𝔤)` the
   antipode satisfies `S²(x) = K_{2ρ} x K_{2ρ}⁻¹ ≠ x`; for the Taft algebra of
   dimension `n²` the antipode has order `2n`. So `S² = id` is not a mild
   extra hypothesis for this framework — it is close to the negation of
   q-deformation, and `def:quantum-universe` says its category is *braided
   monoidal, not symmetric* precisely to keep the braiding non-trivial.

**A scope correction to my own earlier theorem.**
`AntipodeIndependence.id_eq_zero_of_antipode_sq_eq_id` derived a zero object
from `S ≫ S = 𝟙` by substituting `g = 0` for the antipode. That substitution
required `antipode` to be free data and is **no longer available** — with the
axioms in place `S` is determined, so one cannot choose it. That theorem
remains true of the pre-axiom structure it is stated over, and says nothing
about the current one.

## What is still missing, and is NOT fixed here

`FrobeniusHopfData` is **not** asserted to be a bialgebra. The bimonoid
compatibility — `Δ ∘ μ = (μ ⊗ μ) ∘ tensorμ ∘ (Δ ⊗ Δ)`, i.e.
`CategoryTheory.BimonObj` — appears nowhere in `def:frobenius-hopf-substrate`,
whose axiom 2 asks only for a coalgebra object. The Frobenius relation is a
*different* compatibility and does not imply it. Consequently this structure
does not extend to a `HopfObj` and `antipode_sq_of_comm` cannot be applied to
it directly; it is stated for Mathlib's `HopfObj` and recorded here as the
answer to the `S² = id` question, not as a theorem about the substrate.

**🛑 Superseded 2026-09-14, same day: the bialgebra axiom must NOT be added.**
This paragraph left it as the owner's call. It is not a decision — it is
settled by proof. `QOU.FrobeniusHopfData.counit_comp_unit`
(`FrobeniusBialgebraCollapse.lean`, sorry-free) shows that one of the four
bimonoid axioms *on its own*, `Δ ∘ η = η ⊗ η`, forces `ε ≫ η = 𝟙_A` — the
substrate object becomes a retract of the tensor unit, and with the second
unit-side axiom an isomorphism `A ≅ 𝟙_C`. The Frobenius relation makes `Δ` a
bimodule map, hence determined by `Δ(1)`; the bimonoid axiom makes `Δ(1)`
degenerate; the counit law finishes it.

So the substrate is a Frobenius monoid carrying an antipode, and cannot be
promoted to a Hopf monoid on this `Δ`. That is the expected state of affairs —
a finite-dimensional Hopf algebra is Frobenius, but its Frobenius
comultiplication is not its Hopf comultiplication — and it is why
`antipode_sq_of_comm` below is stated for Mathlib's `HopfObj` rather than
transported to `FrobeniusHopfData`.

**🛑 And the axioms this file is about do more than that, with no hypothesis at
all.** `QOU.FrobeniusHopfData.scalar_id_eq_counit_unit` (same file, sorry-free,
`[propext, Quot.sound]`) shows that `antipode_left` together with the Frobenius
relation forces `ε(1)·x = ε(x)·1` for every `x`. So a **non-trivial** substrate
has a **non-unital counit** — `ε(1) ≠ 1`, Mathlib's `BimonObj.one_counit`, the
normalisation every bialgebra and Hopf algebra assumes without comment. Both
unit-side bimonoid axioms are therefore individually excluded.

`ε(1) = 1` is not a field here, so this is not a proof that the axioms force
`A = 𝟙_C`; it is the identity above and its contrapositive. What it does mean is
that the antipode axiom is not neutral with respect to the rest of the
definition. Bean `qou-aawz`.

## References

- [kassel1995] C. Kassel, *Quantum Groups*, Springer 1995, Ch. III
  (antipode uniqueness; `S²` for `U_q(𝔤)`).
- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

variable {C : Type u} [CategoryTheory.Category.{v} C]
  [CategoryTheory.MonoidalCategory C]

namespace FrobeniusHopfData

/-! ### Transport to Mathlib's monoid / comonoid objects -/

/-- The algebra half of a `FrobeniusHopfData` is a Mathlib `MonObj`.
    Field-for-field: the six laws were given Mathlib's exact shapes so that
    this is a transport rather than a proof. -/
def toMonObj (F : FrobeniusHopfData C) : MonObj F.obj where
  one := F.unit
  mul := F.mul
  one_mul := F.one_mul
  mul_one := F.mul_one
  mul_assoc := F.mul_assoc

/-- The coalgebra half of a `FrobeniusHopfData` is a Mathlib `ComonObj`. -/
def toComonObj (F : FrobeniusHopfData C) : ComonObj F.obj where
  counit := F.counit
  comul := F.comul
  counit_comul := F.counit_comul
  comul_counit := F.comul_counit
  comul_assoc := F.comul_assoc

/-! ### The antipode is determined -/

/-- **Uniqueness of the antipode.**  Any morphism satisfying the two antipode
    axioms *is* the antipode.

    This is what the 2026-09-14 axiom addition buys: `antipode` stops being
    free data.  Before it, `S` could be replaced by any endomorphism whatever
    and every law still held (`AntipodeIndependence.withAntipode`); now it is
    pinned by `(μ, η, Δ, ε)`.

    Proof: `S'` is a left convolution inverse of `𝟙` and `F.antipode` is a
    right one, and in a monoid left and right inverses coincide.  The monoid
    is `CategoryTheory.Conv F.obj F.obj`, whose `Monoid` instance is exactly
    where the associativity, coassociativity and unit/counit laws are spent. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 Ch. III
--      (the antipode is the convolution inverse of the identity, hence unique)
theorem antipode_unique_of_left (F : FrobeniusHopfData C) (S' : F.obj ⟶ F.obj)
    (hl : F.comul ≫ S' ▷ F.obj ≫ F.mul = F.counit ≫ F.unit) :
    S' = F.antipode := by
  letI : MonObj F.obj := F.toMonObj
  letI : ComonObj F.obj := F.toComonObj
  apply left_inv_eq_right_inv (M := CategoryTheory.Conv F.obj F.obj)
    (a := CategoryTheory.CategoryStruct.id F.obj) (b := S') (c := F.antipode)
  · rw [CategoryTheory.Conv.mul_eq, CategoryTheory.Conv.one_eq]
    simpa [toMonObj, toComonObj] using hl
  · rw [CategoryTheory.Conv.mul_eq, CategoryTheory.Conv.one_eq]
    simpa [toMonObj, toComonObj] using F.antipode_right

/-- **Uniqueness of the antipode**, in the usual two-sided form: anything
    satisfying both antipode axioms is the antipode.

    Weaker than `antipode_unique_of_left`, which needs only the left one —
    recorded in that direction because a theorem should not carry a hypothesis
    it does not spend. -/
theorem antipode_unique (F : FrobeniusHopfData C) (S' : F.obj ⟶ F.obj)
    (hl : F.comul ≫ S' ▷ F.obj ≫ F.mul = F.counit ≫ F.unit)
    (_hr : F.comul ≫ F.obj ◁ S' ≫ F.mul = F.counit ≫ F.unit) :
    S' = F.antipode :=
  F.antipode_unique_of_left S' hl

/-- Restated with the sides swapped, for rewriting. -/
theorem antipode_eq_of_left (F : FrobeniusHopfData C) (S' : F.obj ⟶ F.obj)
    (hl : F.comul ≫ S' ▷ F.obj ≫ F.mul = F.counit ≫ F.unit) :
    F.antipode = S' :=
  (F.antipode_unique_of_left S' hl).symm

end FrobeniusHopfData

/-! ### The `S² = id` question -/

/-- **`S² = id` needs commutativity — it does not follow from the Hopf axioms
    alone.**

    A re-export of `HopfObj.antipode_antipode`, so that the
    hypothesis `comm` is visible from inside this corpus.  `comm` says the
    multiplication is invariant under the braiding; for a genuinely
    `q`-deformed substrate it is exactly what fails, which is why `S² = id`
    should not be expected here.

    Stated for Mathlib's `HopfObj` rather than for `FrobeniusHopfData`,
    because the latter carries no bimonoid compatibility (see the module
    docstring) and so is not a Hopf monoid. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 Ch. III
--      (S² = id for commutative or cocommutative Hopf algebras;
--       S²(x) = K_{2ρ} x K_{2ρ}⁻¹ for U_q(𝔤), so S² ≠ id in general)
theorem antipode_sq_of_comm [CategoryTheory.BraidedCategory C] (A : C)
    [HopfObj A]
    (comm : (CategoryTheory.BraidedCategory.braiding A A).hom ≫
        MonObj.mul = MonObj.mul) :
    HopfObj.antipode ≫ HopfObj.antipode =
      CategoryTheory.CategoryStruct.id A :=
  HopfObj.antipode_antipode A comm

end QOU
