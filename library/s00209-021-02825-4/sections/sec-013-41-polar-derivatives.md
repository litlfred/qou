---
doc_id: s00209-021-02825-4
doc_title: "Mathematische Zeitschrift (2022) 300:1359–1400 A representation theoretic explanation of the Borcea–Brändén characterization Jonathan Leake 1 © The Author(s) 2021"
section_id: sec-013-41-polar-derivatives
section_title: "Polar derivatives"
section_number: 4.1
pages: 13-15
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
---
A crucial tool of classical stability theory is the polar derivative. In particular, this notion leads
to Laguerre’s theorem (Proposition 4.6), which is the main lemma toward Grace’s theorem.
By passing to homogeneous polynomials the polar derivative becomes conceptually simpler,
and this in turn sheds further light on the general connection to SL 2(C)-invariance and the
D map. One example of this, as we will see below, is that the polar derivative can be deﬁned
as the conjugation of ∂x by some SL 2(C) action.
Given some “pole” x0 ∈ C,t h e polar derivative with respect to x0 of f ∈ Cn[x] is
classically deﬁned as follows.
(dx0 f )(x) := nf (x) − (x − x0) f ′(x)
Noticing that the term of degree n cancels out, the resulting polynomial is of degree n − 1.
It is typically said that this operator generalizes the ordinary derivative in the sense that
limx0→∞ x−1
0 dx0 f (x) = f ′(x). However, this operator also generalizes the ordinary deriva-
tive in more natural way, which we see by passing to V(n).
Fix any φ =
[ ab
cd
]
∈ SL2(C).D e ﬁ n et h epole of φ to be (−d : c) ∈ CP1.F o r p ∈ V(n),
we then deﬁne the polar derivative with respect to φ as follows.
dφ p := (φ−1∂xφ) p =− (−d∂x + c∂y)p
Notice thatdφ depends only onφ−1(−1
0
)
=
(−d
c
)
. With this, the pole ofφ should be interpreted
as the element of CP1 that φ sends to ∞= (−1 : 0).
This deﬁnition of the polar derivative with respect to φ is at very least a natural one, as
it can be simply described as the conjugation of ∂x by the action of φ. The following result
then shows that this is actually the correct deﬁnition.
Proposition 4.1 Fix φ ≡
[ ab
cd
]
∈ SL2(C) with pole (−d : c), and deﬁne x 0 := −d
c (for
c ⁄= 0). Then:
dφ ◦ Hmgn = Hmgn−1 ◦(−c · dx0 )
That is, the polar derivative dφ on V(n) is the homogenization of the classical polar derivative
dx0 on Cn[x] (up to scalar).
Proof Straightforward computation. ⊓⊔
As mentioned above, dφ depends only on (−d : c), the pole of φ. So given any pole in
CP1, we can actually choose φ ∈ SL2(C) to be a rotation of the Riemann sphere (i.e., CP1).
This then gives the following intuitive description of the polar derivative.
Remark 4.2 Fix a rotation φ ∈ SL2(C) with pole (−d : c). The polar derivative dφ then
acts on p ∈ V(n) in the following way. First, consider the zeros of p as being placed in the
Riemann sphere via stereographic projection. Next, rotate the sphere via φ, which moves
(−d : c) to inﬁnity at the top of the sphere. Apply the derivative to the new polynomial given
by the new locations of the zeros. Finally, undo the original rotation via φ−1, which moves
inﬁnity back to the pole (−d : c).
123
1372 J. Leake
4.2 Projective convexity and Laguerre’s theorem
Circular regions play a key role in Grace’s theorem and its corollaries. The main reason for
this is Laguerre’s theorem, which essentially says that polar derivatives with respect to points
of a circular region preserve stability for that circular region. This theorem in turn relies on
the Gauss–Lucas theorem, which deals with convex regions.
A circular region in C is deﬁned to be a disc, half-plane, or complement of a disc, and
such a circular region can be either open or closed. The generalization of circular regions to
CP1 is the obvious one. A circular region in CP1 is deﬁned to be the sets in CP1 for which
the stereographic projection is a circular region in C.N o t et h a tS L2(C) acts transitively on
the set of all circular regions in C or in CP1. We now state a lemma to Laguerre’s theorem,
which gets at the heart of the importance of circular regions.
Lemma 4.3 Let C ⊆ CP1 be a circular region, and let φ ∈ SL2(C) be such that its pole is
not in C. Then, the stereographic projection of φ · C is convex.
Proof Let (x0 : y0)/∈ C be the pole of φ. Then, φ maps (x0 : y0) to ∞∈ CP1 and maps C to
another circular region. Since (x0 : y0)/∈ C implies ∞ /∈ φ · C, the sterographic projection
of φ · C is either an open half-plane or is bounded away from ∞.S i n c eφ · C is a circular
region, it must be convex. ⊓⊔
This then leads to a natural extension of the notion of a circular region.
Deﬁnition 4.4 Given C ⊆ CP1,w es a yt h a tC is projectively convexif for everyφ ∈ SL2(C)
with pole not in C, the stereographic projection of φ · C is convex.
We now classify all projectively convex sets in CP1 in the following. This result has been
demonstrated before in [18], where projectively convex regions are referred to as generalized
circular regions.
Proposition 4.5 (Zervos) Let C ⊆ CP1 be projectively convex. Then, C = C◦ ∪ γ ,w h e r e
C◦ is an open circular region which is the interior of C, and γ is a connected subset of the
boundary of C◦. In particular, projective convexity is preserved under taking complements.
So, one example of a projectively convex set which is not quite a circular region isH+∪R+.
Another is H+ ∪[ 0, 1]. Y et another (albeit after a bit of consideration) is H+ ∪ (−∞, 0) ∪
(1,∞]. We now state a homogeneous version of Laguerre’s theorem, extended to projectively
convex sets.
Proposition 4.6 (Laguerre) Let C ⊆ CP1 be projectively convex, and ﬁxφ ∈ SL2(C).I ft h e
pole of φ is in C, then dφ preserves strong C-stability.
Proof Gauss–Lucas and the fact that CP1\C is projectively convex give the result. Specif-
ically, for C-stable p ∈ V(n) consider φ · p, which is stable in φ · C ∋∞ . Letting B be
the complement of C, the dehomogenization of this polynomial is then of degree exactly n
with all of its roots in the stereographic projection of φ · B. By projective convexity,φ · B is
convex and therefore Gauss–Lucas implies ∂x(φ · p) is φ · C-stable and not identically zero.
Applying φ−1 then implies dφ p = (φ−1∂xφ) p is C-stable. ⊓⊔
Corollary 4.7 Let Ck ⊆ CP1 be projectively convex regions for k∈[ m], and ﬁxφ ∈ SL2(C).
If the pole of φ is in Ck0 ,t h e ndφ acting on the variables (xk0 , yk0 ) preserves strong (C1 ×
···× Cm)-stability.
123
A representation theoretic explanation... 1373
Proof Follows from the fact that taking derivatives in some variables commutes with eval-
uation in the others. Speciﬁcally, p ∈ V(λ) is (C1 ×···× Cm)-stable iff p ⁄= 0f o ra l l
evaluations in C1 ×···× Cm . So, evaluating p in all variables in that product of sets except
(xk0 , yk0 ) gives us a Ck0 -stable polynomial in V(λk0 ). Applying the previous proposition
then gives the result. ⊓⊔
