---
# qou-ken6
title: Serre-Leray spectral sequence of the colour fibration — unexplored, aimed at N=3
status: todo
type: task
priority: normal
created_at: 2026-08-25T21:13:28Z
updated_at: 2026-08-25T21:14:34Z
parent: qou-8lxd
---

Owner prompt 2026-08-25: 'we have fibration and serre-leray spectral sequence - check corpus'.

CORPUS-GREP RESULT — the tool is ABSENT, and the fibrations are PRESENT.

Serre-Leray: ZERO hits for the spectral sequence of a fibration, anywhere in
content/ or docs/. Every 'Serre' hit is the q-SERRE RELATIONS of a quantum group
(fred2005, UGB Groebner-Shirshov). Every 'Leray' hit is a LERAY SELF-SIMILAR
PROFILE in the Navier-Stokes blowup chapter. Different objects sharing the names.
The corpus DOES have one spectral sequence, in mass-theory/
spectral-sequence-collapse-proof.md, but it is HOCHSCHILD (HH^k = 0 by
Whitehead for semisimple algebras), not Serre-Leray of a fibration.

Fibrations, by contrast, are everywhere:
  brings-surface/color-tube-interpretation.md  the COLOUR FIBRATION over P^1(C),
      whose fibre is a curve inside the THREE-DIMENSIONAL colour space A^3 with
      c = (c_r, c_g, c_b)
  brings-surface/t-duality-elliptic.md         elliptic fibration S -> P^1(C)
  brings-surface/radial-projection.md          fibration over the base manifold M
  klein-bring-icosahedral-bridge.md            Seifert fibration S^3/2I -> S^2(2,3,5)
  knot-particle-generation-interpretation.md   Hopf fibration S^3 -> S^2
  virtual-particles-exceptional-divisor.md     Reeb bundle U(1) -> S^3 -> S_p

WHY THIS IS AIMED AT N=3, stated as a reason to look and NOT as a result.

The Sym^2 parity exclusion (merged, b457b8ad57) is a statement about objects of
the SINGLE-FIBRE TENSOR CATEGORY: any such object passing the gate has even
vector-space dimension, so none is 3-dimensional. The corpus's own conclusion is
that N=3 must therefore come from GROUPOID-LEVEL structure -- multi-strand,
framing, or inter-fibre.

A fibration total space is assembled from base AND fibre. It is not obviously an
object of the single-fibre tensor category, so the exclusion does not obviously
apply to it. And the Serre-Leray spectral sequence is precisely the machine that
computes the total space from the two. The colour fibration already carries a
three-dimensional colour space.

That is a SHAPE MATCH, and shape matches are exactly what the anti-laundering
discipline exists to catch. NOTHING IS CLAIMED HERE. I have not computed an E_2
page, not identified what would play the role of the fibre's cohomology, and not
checked whether anything the SS produces would pass the Sym^2 gate. The honest
status is: a standard tool, never applied, pointed at a live gap, with a stated
reason it might evade an exclusion that kills the obvious routes.

FIRST CONCRETE STEP for whoever takes this: for the colour fibration over
P^1(C), identify the fibre and base cohomology the corpus can actually supply,
and write the E_2 page. If E_2 cannot even be written down from existing corpus
objects, that is the answer and it is cheap to reach.

CAUTION: 'three-dimensional colour space A^3' is an AMBIENT affine space in which
a curve sits -- it is NOT a 3-dimensional representation of anything. Reading it
as the missing flavour triple would be precisely the dimension-vs-object
conflation this epic keeps having to retract.


## CORRECTION 2026-08-25, same session — "ABSENT" WAS WRONG. Owner caught it.

Owner: "double check corpus - should be pages there already. maybe only in lean
and not exposition?" Correct on both counts; the central claim above is retracted.

MY ERROR: the grep behind "ZERO hits" did cover .md AND .lean, but I read it
through `head -15` and all fifteen lines were .md. The .lean hits sat below the
cutoff. I concluded absence from a truncated list.

WHAT ACTUALLY EXISTS — a real spectral-sequence layer, mostly in Lean:

  QOU/Mathlib/SpectralSequence.lean          29 decls, ZERO sorry, zero axiom
      Abstract E_r-page API: pages indexed by N x Z x Z, differential of bidegree
      (r, 1-r) cohomological, CollapsesAt r0, convergesTo. Its docstring states
      the gap it fills: "Mathlib has homological-algebra primitives
      (HomotopyCategory, DerivedCategory, ChainComplex) but no E_r-page
      abstraction with collapse criteria." EXPOSITION-FREE — exactly the owner's
      guess: this piece exists only in Lean.

  QOU/Machinery/SpectralSequenceBasic.lean    3 decls, 3 sorry (by design)
      Scaffold for the GB (Groebner-Shirshov) filtration SS; d_1, d_2 sorry'd,
      docstring calls the instances "the open infrastructure work".

  QOU/BraidKnot/spectral_sequence_h3_explicit.lean   2 decls, 0 sorry
  QOU/BraidKnot/e_infinity_identifications.lean      2 decls, 4 sorry (6-term E_inf)
  QOU/WedderburnMass/curvature_rank_gb_stratification.lean
  exposition: mass-theory/spectral-sequence-collapse-proof.md,
              appendix-mass-binding-algorithms/mba-step07-gb-filtration.md

WHAT SURVIVES, precisely: the corpus SS is the GB-FILTRATION / HOCHSCHILD-KLR
one, claiming CollapsesAt 2 — the Wedderburn block decomposition IS the E_2 page.
That is a filtration spectral sequence OF AN ALGEBRA. It is not the Serre-Leray
SS OF A FIBRATION, which relates H*(base), H*(fibre), H*(total). Serre-Leray in
that sense still does not appear.

BUT THE GAP IS FAR SMALLER, AND BETTER SHAPED: the E_r machinery already exists
and is sorry-free. Applying it to a fibration means INSTANTIATING AN EXISTING
API, not building one.

REVISED FIRST STEP (supersedes the one above): instantiate
QOU.Mathlib.SpectralSequence on the colour fibration over P^1(C) — identify what
plays E_2^{p,q} from base and fibre cohomology the corpus can actually supply.
If the existing API cannot be instantiated on it, that is the answer, cheaply.

CAUTIONS, both live: (1) the colour fibration's ambient A^3 is a space a curve
sits in, NOT a 3-dimensional representation; (2) the GB SS's own differentials
are sorry'd, so "the corpus has a spectral sequence" must not be read as "the
corpus has a PROVED spectral sequence".
