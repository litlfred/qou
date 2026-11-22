/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLC1Bridge
import QOU.MathlibExt.PLIsotopy

set_option autoImplicit false

/-!
# The Moise–Bing step, stated as a named gap (issue #8902)

A topological ambient isotopy of polygonal links has no regularity: its homeomorphisms need not
be differentiable or piecewise linear anywhere. Before it can be turned into Δ-moves it must be
replaced by a PL one. That replacement is the theorem of Moise and Bing (every homeomorphism of a
3-manifold is approximated by PL homeomorphisms). It is **not** proved here.

## What is a DEFINITION here

* `MoiseBing E` — the statement: topologically ambient isotopic polygonal links in `E` are PL
  ambient isotopic. It is a `Prop` with no instance or proof in this repository.

## What is a THEOREM here

* `AmbientIsotopic.deltaEquiv_of_moiseBing` — `MoiseBing E`, together with the converse of
  `DeltaEquiv.plAmbientIsotopic` (PL ambient isotopy gives Δ-equivalence, issue #8902 stage 2),
  makes topological ambient isotopy imply Δ-equivalence.

## Why not C¹

`C1AmbientIsotopy.deltaEquiv` (in `PLC1Bridge`) is proved, but it cannot stand in for this
step: a C¹ diffeomorphism sends a straight edge to a C¹ curve, so it cannot carry a triangle onto
a square. "Topologically isotopic polygonal links are C¹ ambient isotopic" is false.

## Literature

* E. E. Moise, *Affine structures in 3-manifolds V. The triangulation theorem and Hauptvermutung*,
  Ann. of Math. 56 (1952) 96–114.
* R. H. Bing, *Locally tame sets are tame*, Ann. of Math. 59 (1954) 145–158.
* G. Burde, H. Zieschang, *Knots*, de Gruyter (3rd ed. 2014), §1.A for the reduction of tame
  isotopy to PL isotopy and Δ-moves.

These cover `finrank ℝ E = 3`. The statement is posed for every `E`; other dimensions are not
claimed here.
-/

namespace QOU.MathlibExt.PL

variable (E : Type*) [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- **The Moise–Bing comparison (stated, not proved).** Topologically ambient isotopic polygonal
links are PL ambient isotopic. Classical for `finrank ℝ E = 3` (Moise 1952, Bing 1954). -/
def MoiseBing : Prop :=
  ∀ L L' : PolygonalLink E, AmbientIsotopic L L' → PLAmbientIsotopic L L'

variable {E}

/-- **Topological ambient isotopy gives Δ-equivalence, conditional on `MoiseBing E`** and on the
converse of `DeltaEquiv.plAmbientIsotopic`. -/
theorem AmbientIsotopic.deltaEquiv_of_moiseBing (hMB : MoiseBing E)
    (hPL : ∀ L L' : PolygonalLink E, PLAmbientIsotopic L L' → DeltaEquiv L L')
    {L L' : PolygonalLink E} (h : AmbientIsotopic L L') : DeltaEquiv L L' :=
  hPL L L' (hMB L L' h)

/-- **Link type** (the definition used throughout QOU): the Δ-equivalence class of a polygonal
link, i.e. its PL ambient-isotopy class. A *topological* link enters only through a polygonal
representative; that two topologically ambient isotopic tame links have the same link type is the
Moise–Bing comparison `MoiseBing`, which is cited, not proved here. This type is unrelated to the
two-element toy `QOU.BraidKnot.Link` of `BraidLinkTypes.lean`. -/
abbrev PolygonalLinkType (E : Type*) [NormedAddCommGroup E] [InnerProductSpace ℝ E] : Type _ :=
  Quotient (deltaSetoid (E := E))

/-- The link type of a polygonal link. -/
abbrev PolygonalLink.linkType (L : PolygonalLink E) : PolygonalLinkType E :=
  Quotient.mk _ L

theorem PolygonalLink.linkType_eq_iff {L L' : PolygonalLink E} :
    L.linkType = L'.linkType ↔ DeltaEquiv L L' :=
  Quotient.eq (r := deltaSetoid)

/-- **Topologically ambient isotopic links have the same link type**, conditional on `MoiseBing E`
and on PL ⇒ Δ. -/
theorem AmbientIsotopic.linkType_eq_of_moiseBing (hMB : MoiseBing E)
    (hPL : ∀ L L' : PolygonalLink E, PLAmbientIsotopic L L' → DeltaEquiv L L')
    {L L' : PolygonalLink E} (h : AmbientIsotopic L L') : L.linkType = L'.linkType :=
  PolygonalLink.linkType_eq_iff.2 (h.deltaEquiv_of_moiseBing hMB hPL)

end QOU.MathlibExt.PL
