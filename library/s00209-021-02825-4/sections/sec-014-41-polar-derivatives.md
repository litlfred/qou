---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-014-41-polar-derivatives
section_title: "Polar derivatives"
section_number: 4.1
pages: 13-14
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
A crucial tool of classical stability theory is the polar derivative. In particular, this notion leads
to Laguerre’s theorem (Proposition 4.6), which is the main lemma toward Grace’s theorem.
By passing to homogeneous polynomials the polar derivative becomes conceptually simpler,
and this in turn sheds further light on the general connection to SL2(C)-invariance and the
D map. One example of this, as we will see below, is that the polar derivative can be deﬁned
as the conjugation of ∂x by some SL2(C) action.
Given some “pole” x0 ∈C, the polar derivative with respect to x0 of f ∈Cn[x] is
classically deﬁned as follows.
(dx0 f )(x) := nf (x) −(x −x0) f ′(x)
Noticing that the term of degree n cancels out, the resulting polynomial is of degree n −1.
It is typically said that this operator generalizes the ordinary derivative in the sense that
limx0→∞x−1
0 dx0 f (x) = f ′(x). However, this operator also generalizes the ordinary deriva-
tive in more natural way, which we see by passing to V (n).
Fix any φ =
a b
c d

∈SL2(C). Deﬁne the pole of φ to be (−d : c) ∈CP1. For p ∈V (n),
we then deﬁne the polar derivative with respect to φ as follows.
dφ p := (φ−1∂xφ)p = −(−d∂x + c∂y)p
Notice that dφ depends only on φ−1−1
0
	
=
−d
c
	
. With this, the pole of φ should be interpreted
as the element of CP1 that φ sends to ∞= (−1 : 0).
This deﬁnition of the polar derivative with respect to φ is at very least a natural one, as
it can be simply described as the conjugation of ∂x by the action of φ. The following result
then shows that this is actually the correct deﬁnition.
Proposition 4.1 Fix φ ≡
a b
c d

∈SL2(C) with pole (−d : c), and deﬁne x0 := −d
c
(for
c̸ = 0). Then:
dφ ◦Hmgn = Hmgn−1 ◦(−c · dx0)
That is, the polar derivative dφ on V (n) is the homogenization of the classical polar derivative
dx0 on Cn[x] (up to scalar).
Proof Straightforward computation.
⊓⊔
As mentioned above, dφ depends only on (−d : c), the pole of φ. So given any pole in
CP1, we can actually choose φ ∈SL2(C) to be a rotation of the Riemann sphere (i.e., CP1).
This then gives the following intuitive description of the polar derivative.
Remark 4.2 Fix a rotation φ ∈SL2(C) with pole (−d : c). The polar derivative dφ then
acts on p ∈V (n) in the following way. First, consider the zeros of p as being placed in the
Riemann sphere via stereographic projection. Next, rotate the sphere via φ, which moves
(−d : c) to inﬁnity at the top of the sphere. Apply the derivative to the new polynomial given
by the new locations of the zeros. Finally, undo the original rotation via φ−1, which moves
inﬁnity back to the pole (−d : c).
1372
J. Leake
