/-
Copyright (c) 2026 litlfred. All rights reserved.

# SCAFFOLD ONLY — the framed-oriented-tangle category and the Reshetikhin–Turaev ribbon-functor signature

**This file is an honest SKELETON, not a completed formalization.** It is the first structural step
of bean `rttg` (RT-2): the Reshetikhin–Turaev functor `F : Rib(𝒞) → 𝒞` from the category of framed
oriented tangles to a braided right-rigid (ribbon) target. Mathlib has **no** tangle category, so it
must be built from generators and relations. This scaffold lays down the *data* precisely and stops
where the genuine mathematics begins — it does **NOT** close `bwse` or `rttg`.

## What is genuinely PROVED here (sorry-free, real content)

* `TangleObject := List Sign` is a monoid under `++` with unit `[]`: append associativity and the
  two unit laws (`tangleObject_append_assoc`, `nil_append_object`, `append_nil_object`). These are
  real facts, delegated to Mathlib's `List` API.
* The braid-generator images in the target category are **mutually inverse** — the Reidemeister-II
  (regular-isotopy) move at the level of the functor's *images*
  (`braidImg_hom_inv`, `braidImg_inv_hom`), a genuine `Iso` law, not a tautology.

## What is carried as DATA / SIGNATURE (honest scaffold, not proved)

* `TangleMor : TangleObject → TangleObject → Type` — the **free** hom-datatype on the generating
  morphisms (cup, cap, positive/negative crossing, twist) together with formal `id`/`comp`/`tensor`.
  This is the free structure on the tangle generators; it is **not** yet the tangle category — that
  is this quotiented by the Turaev/Reidemeister relations (see "Open" below). No `Category` instance
  is claimed, because the category laws hold only after that quotient.
* `RibbonFunctorData 𝒞` — the **signature** of the RT functor's data on a Mathlib braided
  right-rigid category: a coloring object `V` and a ribbon/balancing `twist` carried as data
  (Mathlib has no ribbon typeclass). The canonical generator images are then *defined* from the
  target's coevaluation `η_`, evaluation `ε_`, braiding `β_`, and this `twist`.

## What remains OPEN (the honest bulk — beans `rttg`, `rtkb`)

Nothing below is proved or wired to production. The open obligations, enumerated for the next agent:

1. **Total functor assembly with coherence.** Extend the per-generator images to a total map
   `TangleMor X Y → (mapObj X ⟶ mapObj Y)` by inserting the associator/unitor coherence isos of
   `𝒞`. The oriented case additionally requires left-vs-right-dual bookkeeping
   (`(Vᘁ)ᘁ ≠ V` definitionally).
2. **Relation invariance / well-definedness (Turaev's theorem).** Prove the assignment descends to
   the quotient by the framed-oriented-tangle relations: the two zig-zag (snake) identities
   (Mathlib's `ExactPairing` coherence supplies these on the categorical side), Reidemeister II
   (braid inverse — image-level done here, diagram-level open), Reidemeister III / Yang–Baxter
   (`β` hexagon), and the framed Reidemeister I with the ribbon twist (`θ`-naturality + balancing).
3. **Link invariance / Kirby moves.** The resulting closed-tangle invariant (colored Jones as `F` of
   a closed braid) and its invariance under the surgery/Kirby moves — bean `rtkb`.

## Honest scope (STRICT, §Axiomatization-is-NOT-a-Proof, §Strict-Lean-Discipline, §14)

This is a scaffold. It fabricates no proofs, launders no fit, wires nothing to any dashboard; L2
accuracy is unchanged (2/7). The `RibbonFunctorData.twist` and generator images are content-bearing
*data*, not `True`; the two proved lemmas are genuine `List`/`Iso` facts. Everything else is an
explicitly-named open obligation, tracked in `.beans/rttg--rt-framed-tangle-functor.md`.

Base ring (§7c): purely categorical over any Mathlib `[BraidedCategory 𝒞] [RightRigidCategory 𝒞]`;
no `ℝ`, no ordering, no archimedean construct. `TangleObject`/`Sign` are `Bool`-combinatorial.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md ; Turaev, *Quantum Invariants of Knots and
   3-Manifolds*, ch. I–II (framed tangle category + RT functor); Reshetikhin–Turaev 1990.
-/
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

namespace QOU.BraidKnot.FramedTangle

open CategoryTheory MonoidalCategory BraidedCategory

/-! ## 1. Objects of the framed-oriented-tangle category

An object is a finite sequence of oriented framed points on the line. A point carries an
orientation `Sign` (`true = +`, an outgoing/up strand; `false = −`, its reverse). Orientation
reversal is Boolean negation. The framing is recorded elsewhere (the twist generator); the object
records only the boundary sign word, as in Turaev's presentation. -/

/-- Orientation of a boundary point: `true = +` (up), `false = −` (down). -/
abbrev Sign : Type := Bool

/-- Orientation reversal (`bar`): swaps `+ ↔ −`. -/
abbrev Sign.bar (s : Sign) : Sign := !s

/-- **An object of the tangle category**: a finite oriented sign word (boundary of a tangle). -/
abbrev TangleObject : Type := List Sign

/-- The empty tangle boundary — the monoidal unit object. -/
abbrev TangleObject.unit : TangleObject := []

/-- Monoidal product on objects = concatenation of sign words. `abbrev` so it unfolds to `++`. -/
abbrev TangleObject.tensor (X Y : TangleObject) : TangleObject := X ++ Y

/-- **(PROVED)** The object monoid is associative — a real fact via `List.append_assoc`. -/
theorem tangleObject_append_assoc (X Y Z : TangleObject) :
    (X ++ Y) ++ Z = X ++ (Y ++ Z) :=
  List.append_assoc X Y Z

/-- **(PROVED)** The empty object is a left unit for the tensor. -/
theorem nil_append_object (X : TangleObject) : TangleObject.unit ++ X = X :=
  List.nil_append X

/-- **(PROVED)** The empty object is a right unit for the tensor. -/
theorem append_nil_object (X : TangleObject) : X ++ TangleObject.unit = X :=
  List.append_nil X

/-! ## 2. Generating morphisms — the free tangle-diagram datatype

`TangleMor X Y` is the **free** collection of tangle diagrams from boundary `X` to boundary `Y`,
generated by the elementary tangles (cup, cap, positive/negative crossing, framing twist) closed
under formal identity, vertical composition (`comp`, stacking) and horizontal composition (`tensor`,
juxtaposition). It is *free*: no Reidemeister/Turaev relation is imposed, so this is a quiver of
generators, **not** the tangle category (which is this quotiented by those relations — open, §Open). -/

/-- **The free datatype of tangle diagrams** on the oriented-framed generators.  Constructors are
the generating morphisms plus formal `id`/`comp`/`tensor`; the geometric relations are **not**
imposed (see the file docstring, obligation 2). -/
inductive TangleMor : TangleObject → TangleObject → Type
  /-- The empty/identity tangle on a boundary `X`. -/
  | id (X : TangleObject) : TangleMor X X
  /-- Vertical composition (stacking one tangle atop another). -/
  | comp {X Y Z : TangleObject} : TangleMor X Y → TangleMor Y Z → TangleMor X Z
  /-- Horizontal composition (side-by-side juxtaposition); boundaries concatenate. -/
  | tensor {X Y X' Y' : TangleObject} :
      TangleMor X Y → TangleMor X' Y' → TangleMor (X ++ X') (Y ++ Y')
  /-- **Cup** (creation / coevaluation): a `∪` of a strand and its reverse, `[] ⟶ [s, s̄]`. -/
  | cup (s : Sign) : TangleMor [] [s, s.bar]
  /-- **Cap** (annihilation / evaluation): a `∩`, `[s, s̄] ⟶ []`. -/
  | cap (s : Sign) : TangleMor [s, s.bar] []
  /-- **Positive crossing** (over-braid) of two adjacent strands, `[s, t] ⟶ [t, s]`. -/
  | braidPos (s t : Sign) : TangleMor [s, t] [t, s]
  /-- **Negative crossing** (under-braid), `[s, t] ⟶ [t, s]`.  Inverse of `braidPos` after the
  Reidemeister-II relation, which is **not** imposed on this free datatype. -/
  | braidNeg (s t : Sign) : TangleMor [s, t] [t, s]
  /-- **Framing twist** `θ` (a `+1` curl) on a single strand, `[s] ⟶ [s]`. -/
  | twist (s : Sign) : TangleMor [s] [s]
  /-- **Inverse framing twist** `θ⁻¹` (a `−1` curl), `[s] ⟶ [s]`. -/
  | twistInv (s : Sign) : TangleMor [s] [s]

/-! ## 3. The Reshetikhin–Turaev ribbon-functor signature

`RibbonFunctorData 𝒞` packages the *data* of the RT functor into a Mathlib braided right-rigid
category `𝒞`: a coloring object `V` and a ribbon/balancing `twist`, carried as data because Mathlib
has no ribbon (balanced) typeclass. From this data the canonical images of the generators are
*defined* (below) via the target's coevaluation `η_`, evaluation `ε_`, and braiding `β_`.

Only the per-generator images are given here.  Assembling them into a total, relation-respecting
functor `TangleMor X Y → (mapObj X ⟶ mapObj Y)` is the open work (file docstring, obligations 1–2). -/

variable (𝒞 : Type*) [Category 𝒞] [MonoidalCategory 𝒞] [BraidedCategory 𝒞] [RightRigidCategory 𝒞]

/-- **The data of a Reshetikhin–Turaev ribbon functor** into a Mathlib braided right-rigid category:
a coloring object `V` and a ribbon/balancing `twist` (an endomorphism family), the latter carried as
*data* since Mathlib provides no ribbon/balanced structure. Content-bearing, not `True`. -/
structure RibbonFunctorData where
  /-- The coloring object attached to a `+` point; a `−` point is colored by its right dual `Vᘁ`. -/
  V : 𝒞
  /-- The ribbon/balancing twist `θ_X : X ⟶ X`, carried as data (no Mathlib ribbon typeclass). -/
  twist : (X : 𝒞) → (X ⟶ X)

namespace RibbonFunctorData

variable {𝒞}

/-- Object coloring: `+ ↦ V`, `− ↦ Vᘁ` (right dual). -/
def colorObj (d : RibbonFunctorData 𝒞) : Sign → 𝒞
  | true  => d.V
  | false => (d.V)ᘁ

/-- Object map on a whole sign word: fold the coloring with the monoidal product, `[] ↦ 𝟙_𝒞`.
This is the intended `F` on objects; the total `F` on morphisms is the open assembly. -/
def mapObj (d : RibbonFunctorData 𝒞) : TangleObject → 𝒞
  | []      => 𝟙_ 𝒞
  | s :: xs => d.colorObj s ⊗ d.mapObj xs

/-- Canonical **cup** image: the coevaluation `η_ V Vᘁ : 𝟙_𝒞 ⟶ V ⊗ Vᘁ`. -/
noncomputable def cupImg (d : RibbonFunctorData 𝒞) : 𝟙_ 𝒞 ⟶ d.V ⊗ (d.V)ᘁ :=
  η_ d.V (d.V)ᘁ

/-- Canonical **cap** image: the evaluation `ε_ V Vᘁ : Vᘁ ⊗ V ⟶ 𝟙_𝒞`. -/
noncomputable def capImg (d : RibbonFunctorData 𝒞) : (d.V)ᘁ ⊗ d.V ⟶ 𝟙_ 𝒞 :=
  ε_ d.V (d.V)ᘁ

/-- Canonical **positive-crossing** image: the braiding `(β_ X Y).hom : X ⊗ Y ⟶ Y ⊗ X`. -/
noncomputable def braidPosImg (_d : RibbonFunctorData 𝒞) (X Y : 𝒞) : X ⊗ Y ⟶ Y ⊗ X :=
  (β_ X Y).hom

/-- Canonical **negative-crossing** image: the inverse braiding `(β_ X Y).inv : Y ⊗ X ⟶ X ⊗ Y`. -/
noncomputable def braidNegImg (_d : RibbonFunctorData 𝒞) (X Y : 𝒞) : Y ⊗ X ⟶ X ⊗ Y :=
  (β_ X Y).inv

/-- Canonical **framing-twist** image: the carried ribbon twist `θ_X : X ⟶ X`. -/
def twistImg (d : RibbonFunctorData 𝒞) (X : 𝒞) : X ⟶ X :=
  d.twist X

omit [RightRigidCategory 𝒞] in
/-- **(PROVED)** Positive- then negative-crossing images compose to the identity — the
Reidemeister-II move at the level of the functor's images. A genuine `Iso` law, not a tautology. -/
theorem braidImg_hom_inv (d : RibbonFunctorData 𝒞) (X Y : 𝒞) :
    d.braidPosImg X Y ≫ d.braidNegImg X Y = 𝟙 (X ⊗ Y) :=
  (β_ X Y).hom_inv_id

omit [RightRigidCategory 𝒞] in
/-- **(PROVED)** Negative- then positive-crossing images compose to the identity (the other
Reidemeister-II direction). -/
theorem braidImg_inv_hom (d : RibbonFunctorData 𝒞) (X Y : 𝒞) :
    d.braidNegImg X Y ≫ d.braidPosImg X Y = 𝟙 (Y ⊗ X) :=
  (β_ X Y).inv_hom_id

end RibbonFunctorData

end QOU.BraidKnot.FramedTangle
