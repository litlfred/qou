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
