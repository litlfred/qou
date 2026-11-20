import Mathlib.Tactic.LinearCombination
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import QOU.FrobeniusHopfData.PairingVariationalDerivative

/-!
# Pure-gauge fluctuations of a pairing are zero modes of an invariant quadratic action

## Setting

`QOU/FrobeniusHopfData/PairingVariationalDerivative.lean` supplies a quadratic
action calculus on the **field space of pairings** `dual ⊗ obj ⟶ 𝟙_ C`
(`QOU.Variational.fieldSpace`), with the exact Taylor identity
`QuadraticAction.value_add` and the contraction action `contractionAction`.
This file asks the first question one asks of a fluctuation `δλ` of a pairing:
**which fluctuations cost nothing?**

## What is proved

* **§1 (generic linear algebra, any `CommRing R`).**  For a quadratic action
  `Q` on a module `V`, translation invariance along a direction `g`
  (`Q.value (e + g) = Q.value e` for every field `e`) is *equivalent* to
  `Q.value g = 0` together with `Q.variation e g = 0` for every `e`
  (`QuadraticAction.isInvariantAlong_iff`).  So an invariant direction carries
  no quadratic ("mass") term and lies in the radical of the variational
  derivative ("Hessian").  The invariant directions form a submodule
  (`QuadraticAction.invariantSubmodule`).  No hypothesis on `2` is needed:
  the statement is phrased with `variation = 2 • form`, never with `form`.
* **§2 (categorical).**  An endomorphism `D` of `dual ⊗ obj` acts on pairings by
  precomposition, `λ ↦ D ≫ λ`; for `D = f ▷ obj + dual ◁ X` this is the Leibniz
  (infinitesimal-automorphism) variation of `λ` under the pair `(f, X)`.  If a
  co-pairing `η` annihilates `D` (`η ≫ D = 0`), every such variation is in the
  kernel of `contract η`, and hence an invariant direction of every
  `contractionAction d η ε` (`contractionAction_isInvariantAlong`,
  `contractionAction_massless`).
* **§3 (rigid instance).**  If `η` is the coevaluation of an exact pairing
  `ExactPairing d.dual d.obj`, then `η` annihilates the generator
  `f ▷ obj − dual ◁ fᘁ` for **every** `f : dual ⟶ dual`, where `fᘁ` is the right
  adjoint mate (Mathlib's `coevaluation_comp_rightAdjointMate`).  So for the
  coevaluation co-pairing, every pure-gauge fluctuation `(f ▷ obj − dual ◁ fᘁ) ≫ λ`
  of every background pairing `λ` is a zero mode of the contraction action
  (`coevaluation_contractionAction_massless`).

## What is NOT claimed

* No physics enters any statement: no metric signature, no dimension, no
  constant.  "Mass" and "massless" are used only as names for "the quadratic
  form vanishes on a direction" — interpretation is confined to the paper's
  remark block, not to this file.
* `contractionAction` has rank at most one (it factors through the scalar
  `ε (η ≫ T)`), so its radical is far larger than the gauge directions.  The
  result says gauge directions are *among* the zero modes; it does **not** say
  they are the only ones, and so it is not a statement that the remaining
  (physical) fluctuations are massive.
* The handedness caveat of `PairingVariationalDerivative` persists: §3 needs
  `ExactPairing d.dual d.obj` (coevaluation `𝟙 ⟶ dual ⊗ obj`), whereas
  `FrobeniusPairingData.Nondegenerate` produces `ExactPairing d.obj d.dual`.
  No braiding is assumed, so the two are not identified here.
* Nothing about a symmetric/traceless (`V₂`) projection of the fluctuations.

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]` throughout; no `ℝ`.
-/

namespace QOU.Variational

universe v u

/-! ## §1  Invariant directions of a quadratic action -/

section FieldSpace

variable {R V : Type*} [CommRing R] [AddCommGroup V] [Module R V]

namespace QuadraticAction

variable (Q : QuadraticAction R V)

/-- The action of the zero field is zero. -/
@[simp] lemma value_zero : Q.value 0 = 0 := by simp [value]

/-- `Q` is **invariant along** the direction `g` when translating any field by
    `g` leaves the action unchanged.  For a background-dependent gauge
    direction `g`, this is the statement that the linearised gauge
    transformation is a symmetry of the quadratic action. -/
def IsInvariantAlong (g : V) : Prop := ∀ e : V, Q.value (e + g) = Q.value e

/-- **Invariant directions are exactly the massless radical directions.**
    Translation invariance along `g` holds iff `g` has zero action ("no mass
    term") and lies in the radical of the variational derivative
    ("decouples from every field at quadratic order"). -/
theorem isInvariantAlong_iff (g : V) :
    Q.IsInvariantAlong g ↔ Q.value g = 0 ∧ ∀ e : V, Q.variation e g = 0 := by
  constructor
  · intro h
    have hg : Q.value g = 0 := by simpa using h 0
    refine ⟨hg, fun e => ?_⟩
    have hT := Q.value_add e g
    rw [h e, hg] at hT
    linear_combination -hT
  · rintro ⟨hg, hv⟩ e
    rw [Q.value_add, hv e, hg]
    ring

/-- One half of `isInvariantAlong_iff`, in the form used downstream: along an
    invariant direction the variational derivative vanishes at every field. -/
theorem variation_eq_zero_of_isInvariantAlong {g : V} (h : Q.IsInvariantAlong g)
    (e : V) : Q.variation e g = 0 :=
  ((Q.isInvariantAlong_iff g).1 h).2 e

/-- The invariant directions of a quadratic action form a **submodule**: the
    pure-gauge directions are closed under sums and scalar multiples. -/
def invariantSubmodule : Submodule R V where
  carrier := {g | Q.IsInvariantAlong g}
  zero_mem' := by intro e; simp
  add_mem' := by
    intro g h hg hh e
    simp only [Set.mem_setOf_eq] at hg hh
    rw [← add_assoc, hh (e + g), hg e]
  smul_mem' := by
    intro r g hg
    simp only [Set.mem_setOf_eq] at hg ⊢
    rw [Q.isInvariantAlong_iff] at hg ⊢
    obtain ⟨h0, hv⟩ := hg
    refine ⟨?_, fun e => ?_⟩
    · rw [Q.value_smul, h0, mul_zero]
    · rw [map_smul, hv e, smul_zero]

@[simp] lemma mem_invariantSubmodule (g : V) :
    g ∈ Q.invariantSubmodule ↔ Q.IsInvariantAlong g := Iff.rfl

end QuadraticAction

end FieldSpace

/-! ## §2  Pure-gauge variations of a pairing -/

section Categorical

open CategoryTheory MonoidalCategory QOU.FrobeniusHopfData

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
  [Linear R C]
variable (d : FrobeniusPairingData C)

/-- The **Leibniz generator** of the pair `(f, X)` of endomorphisms of `dual`
    and `obj`: the infinitesimal automorphism of `dual ⊗ obj`.  A pairing `λ`
    varies under it to `leibnizGenerator d f X ≫ λ`. -/
def leibnizGenerator (f : d.dual ⟶ d.dual) (X : d.obj ⟶ d.obj) :
    d.dual ⊗ d.obj ⟶ d.dual ⊗ d.obj :=
  f ▷ d.obj + d.dual ◁ X

/-- The **pure-gauge variation** of a background pairing `λ` by a generator
    `D`, as an `R`-linear map of the background. -/
def gaugeVariation (D : d.dual ⊗ d.obj ⟶ d.dual ⊗ d.obj) :
    fieldSpace d →ₗ[R] fieldSpace d where
  toFun lam := D ≫ lam
  map_add' := by intro a b; simp
  map_smul' := by intro r a; simp

@[simp] lemma gaugeVariation_apply (D : d.dual ⊗ d.obj ⟶ d.dual ⊗ d.obj)
    (lam : fieldSpace d) : gaugeVariation (R := R) d D lam = D ≫ lam := rfl

/-- If the co-pairing `η` annihilates the generator `D`, every pure-gauge
    variation by `D` contracts to zero. -/
theorem contract_gaugeVariation (η : 𝟙_ C ⟶ d.dual ⊗ d.obj)
    (D : d.dual ⊗ d.obj ⟶ d.dual ⊗ d.obj) (hη : η ≫ D = 0) (lam : fieldSpace d) :
    contract (R := R) d η (gaugeVariation (R := R) d D lam) = 0 := by
  rw [contract_apply, gaugeVariation_apply, ← Category.assoc, hη,
    Limits.zero_comp]

/-- **Gauge invariance of the contraction action.**  If `η ≫ D = 0`, the
    contraction action is invariant along every pure-gauge variation
    `D ≫ λ`, for every background pairing `λ` and every scalar reading `ε`. -/
theorem contractionAction_isInvariantAlong (η : 𝟙_ C ⟶ d.dual ⊗ d.obj)
    (ε : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (D : d.dual ⊗ d.obj ⟶ d.dual ⊗ d.obj)
    (hη : η ≫ D = 0) (lam : fieldSpace d) :
    (contractionAction (R := R) d η ε).IsInvariantAlong (D ≫ lam) := by
  intro T
  have h0 : η ≫ D ≫ lam = 0 := by
    rw [← Category.assoc, hη, Limits.zero_comp]
  rw [contractionAction_value, contractionAction_value, Preadditive.comp_add,
    h0, add_zero]

/-- **Masslessness of pure-gauge pairing fluctuations.**  Under `η ≫ D = 0`, a
    pure-gauge fluctuation `D ≫ λ` has zero action and lies in the radical of
    the variational derivative of the contraction action at every field `T`. -/
theorem contractionAction_massless (η : 𝟙_ C ⟶ d.dual ⊗ d.obj)
    (ε : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (D : d.dual ⊗ d.obj ⟶ d.dual ⊗ d.obj)
    (hη : η ≫ D = 0) (lam : fieldSpace d) :
    (contractionAction (R := R) d η ε).value (D ≫ lam) = 0 ∧
      ∀ T : fieldSpace d,
        (contractionAction (R := R) d η ε).variation T (D ≫ lam) = 0 :=
  ((contractionAction (R := R) d η ε).isInvariantAlong_iff _).1
    (contractionAction_isInvariantAlong d η ε D hη lam)

/-! ## §3  The rigid instance: the coevaluation annihilates every mate generator -/

/-- An exact pairing `dual ⊣ obj` makes `obj` the right dual of `dual`.
    Registered only locally, for the mate `fᘁ`. -/
@[reducible] def rightDualOfExact [ExactPairing d.dual d.obj] : HasRightDual d.dual :=
  ⟨d.obj⟩

/-- The **mate generator** of `f : dual ⟶ dual`: the Leibniz generator of the
    pair `(f, −fᘁ)`, with `fᘁ : obj ⟶ obj` the right adjoint mate. -/
def mateGenerator [ExactPairing d.dual d.obj] (f : d.dual ⟶ d.dual) :
    d.dual ⊗ d.obj ⟶ d.dual ⊗ d.obj :=
  letI := rightDualOfExact d
  f ▷ d.obj - d.dual ◁ (fᘁ : d.obj ⟶ d.obj)

/-- The coevaluation annihilates every mate generator.  This is Mathlib's
    `coevaluation_comp_rightAdjointMate`, rewritten as a vanishing. -/
theorem coevaluation_comp_mateGenerator [ExactPairing d.dual d.obj]
    (f : d.dual ⟶ d.dual) :
    η_ d.dual d.obj ≫ mateGenerator d f = 0 := by
  letI := rightDualOfExact d
  have h := coevaluation_comp_rightAdjointMate (C := C) f
  unfold mateGenerator
  rw [Preadditive.comp_sub, sub_eq_zero]
  exact h.symm

/-- **Masslessness, rigid form.**  With the coevaluation of an exact pairing
    `dual ⊣ obj` as co-pairing, every pure-gauge fluctuation
    `mateGenerator d f ≫ λ` of every background pairing `λ` is an invariant
    direction of the contraction action: it has zero action and lies in the
    radical of the variational derivative at every field. -/
theorem coevaluation_contractionAction_massless [ExactPairing d.dual d.obj]
    (ε : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (f : d.dual ⟶ d.dual) (lam : fieldSpace d) :
    (contractionAction (R := R) d (η_ d.dual d.obj) ε).value
        (mateGenerator d f ≫ lam) = 0 ∧
      ∀ T : fieldSpace d,
        (contractionAction (R := R) d (η_ d.dual d.obj) ε).variation T
          (mateGenerator d f ≫ lam) = 0 :=
  contractionAction_massless d _ ε _ (coevaluation_comp_mateGenerator d f) lam

/-- The pure-gauge fluctuations of a fixed background `λ` lie in the invariant
    submodule of the coevaluation contraction action. -/
theorem mateGenerator_mem_invariantSubmodule [ExactPairing d.dual d.obj]
    (ε : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (f : d.dual ⟶ d.dual) (lam : fieldSpace d) :
    mateGenerator d f ≫ lam ∈
      (contractionAction (R := R) d (η_ d.dual d.obj) ε).invariantSubmodule :=
  contractionAction_isInvariantAlong d _ ε _ (coevaluation_comp_mateGenerator d f) lam

end Categorical

end QOU.Variational
