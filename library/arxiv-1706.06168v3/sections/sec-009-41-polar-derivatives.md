---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-009-41-polar-derivatives
section_title: "Polar Derivatives"
section_number: 4.1
pages: 11-13
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
---
A crucial tool of classical stability theory is the polar derivative. In particular, this notion leads to Laguerre’s
theorem (Proposition 4.6), which is the main lemma toward Grace’s theorem. By passing to homo geneous
polynomials the polar derivative becomes conceptually simpler, and th is in turn sheds further light on the
general connection to SL 2(C)-invariance and the D map. One example of this, as we will see below, is that
the polar derivative can be deﬁned as the conjugation of ∂x by some SL 2(C) action.
Given some “pole” x0 ∈ C, the polar derivative with respect to x0 of f ∈ Cn[x] is classically deﬁned as
follows.
(dx0f )(x) := nf (x) − (x −x0)f ′(x)
Noticing that the term of degree n cancels out, the resulting polynomial is of degree n − 1. It is typically
said that this operator generalizes the ordinary derivative in the se nse that lim x0→∞x−1
0 dx0f (x) = f ′(x).
However, this operator also generalizes the ordinary derivative in m ore natural way, which we see by passing
to V (n).
Fix any φ =
[ a b
c d
]
∈ SL2(C). Deﬁne the pole of φ to be ( −d :c) ∈ CP1. For p ∈V (n), we then deﬁne
the polar derivative with respect to φ as follows.
dφp := (φ−1∂xφ)p = −(−d∂x +c∂y)p
Notice that dφ depends only on φ−1( −1
0
)
=
( −d
c
)
. With this, the pole of φ should be interpreted as the
element of CP1 that φ sends to ∞ = (−1 : 0).
This deﬁnition of the polar derivative with respect to φ is at very least a natural one, as it can be simply
described as the conjugation of ∂x by the action of φ. The following result then shows that this is actually
the correct deﬁnition.
Proposition 4.1. Fix φ ≡
[ a b
c d
]
∈ SL2(C) with pole (−d :c), and deﬁne x0 := −d
c (for c ⁄= 0). Then:
dφ ◦ Hmgn = Hmg n−1 ◦(−c ·dx0 )
That is, the polar derivative dφ on V (n) is the homogenization of the classical polar derivative dx0 on Cn[x]
(up to scalar).
Proof. Straightforward computation.
11
As mentioned above, dφ depends only on ( −d : c), the pole of φ. So given any pole in CP1, we can
actually choose φ ∈ SL2(C) to be a rotation of the Riemann sphere (i.e., CP1). This then gives the following
intuitive description of the polar derivative.
Remark 4.2. Fix a rotation φ ∈ SL2(C) with pole ( −d :c). The polar derivative dφ then acts on p ∈V (n)
in the following way. First, consider the zeros of p as being placed in the Riemann sphere via stereographic
projection. Next, rotate the sphere via φ, which moves ( −d :c) to inﬁnity at the top of the sphere. Apply
the derivative to the new polynomial given by the new locations of the zeros. Finally, undo the original
rotation via φ−1, which moves inﬁnity back to the pole ( −d :c).
4.2 Projective Convexity and Laguerre’s Theorem
Circular regions play a key role in Grace’s theorem and its corollaries. T he main reason for this is Laguerre’s
theorem, which essentially says that polar derivatives with respect to points of a circular region preserve
stability for that circular region. This theorem in turn relies on the Ga uss-Lucas theorem, which deals with
convex regions.
A circular region in C is deﬁned to be a disc, half-plane, or complement of a disc, and such a circular
region can be either open or closed. The generalization of circular re gions to CP1 is the obvious one. A
circular region in CP1 is deﬁned to be the sets in CP1 for which the stereographic projection is a circular
region in C. Note that SL 2(C) acts transitively on the set of all circular regions in C or in CP1. We now
state a lemma to Laguerre’s theorem, which gets at the heart of th e importance of circular regions.
Lemma 4.3. LetC ⊆ CP1 be a circular region, and let φ ∈ SL2(C) be such that its pole is not in C. Then,
the stereographic projection of φ ·C is convex.
Proof. Let (x0 : y0) /∈ C be the pole of φ. Then, φ maps (x0 : y0) to ∞ ∈ CP1 and maps C to another
circular region. Since ( x0 :y0) /∈C implies ∞ /∈φ ·C, the sterographic projection of φ ·C is either an open
half-plane or is bounded away from ∞. Since φ ·C is a circular region, it must be convex.
This then leads to a natural extension of the notion of a circular reg ion.
Deﬁnition 4.4. GivenC ⊆ CP1, we say that C is projectively convex if for every φ ∈ SL2(C) with pole not
in C, the stereographic projection of φ ·C is convex.
We now classify all projectively convex sets in CP1 in the following. This result has been demonstrated
before in [ Zer60], where projectively convex regions are referred to as generalize d circular regions.
Proposition 4.5 (Zervos). Let C ⊆ CP1 be projectively convex. Then, C = C◦ ∪γ, where C◦ is an open
circular region which is the interior of C, and γ is a connected subset of the boundary of C◦. In particular,
projective convexity is preserved under taking complement s.
So, one example of a projectively convex set which is not quite a circu lar region is H+ ∪ R+. Another
is H+ ∪ [0, 1]. Yet another (albeit after a bit of consideration) is H+ ∪ (−∞, 0) ∪ (1, ∞]. We now state a
homogeneous version of Laguerre’s theorem, extended to proje ctively convex sets.
Proposition 4.6 (Laguerre). LetC ⊆ CP1 be projectively convex, and ﬁx φ ∈ SL2(C). If the pole of φ is in
C, then dφ preserves strong C-stability.
Proof. Gauss-Lucas and the fact that CP1 \C is projectively convex give the result. Speciﬁcally, for C-stable
p ∈V (n) considerφ·p, which is stable in φ·C ∋ ∞. Letting B be the complement of C, the dehomogenization
of this polynomial is then of degree exactly n with all of its roots in the stereographic projection of φ ·B.
By projective convexity, φ ·B is convex and therefore Gauss-Lucas implies ∂x(φ ·p) is φ ·C-stable and not
identically zero. Applying φ−1 then implies dφp = (φ−1∂xφ)p is C-stable.
Corollary 4.7. LetCk ⊆ CP1 be projectively convex regions for k ∈ [m], and ﬁx φ ∈ SL2(C). If the pole of
φ is in Ck0 , then dφ acting on the variables (xk0,y k0 ) preserves strong (C1 × · · · ×Cm)-stability.
12
Proof. Follows from the fact that taking derivatives in some variables commu tes with evaluation in the
others. Speciﬁcally, p ∈ V (λ) is ( C1 × · · · ×Cm)-stable iﬀ p ⁄= 0 for all evaluations in C1 × · · · ×Cm. So,
evaluating p in all variables in that product of sets except ( xk0,y k0) gives us a Ck0 -stable polynomial in
V (λk0 ). Applying the previous proposition then gives the result.
