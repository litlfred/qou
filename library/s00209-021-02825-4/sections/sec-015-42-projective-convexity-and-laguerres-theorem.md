---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-015-42-projective-convexity-and-laguerres-theorem
section_title: "Projective convexity and Laguerre's theorem"
section_number: 4.2
pages: 14-15
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
Circular regions play a key role in Grace’s theorem and its corollaries. The main reason for
this is Laguerre’s theorem, which essentially says that polar derivatives with respect to points
of a circular region preserve stability for that circular region. This theorem in turn relies on
the Gauss–Lucas theorem, which deals with convex regions.
A circular region in C is deﬁned to be a disc, half-plane, or complement of a disc, and
such a circular region can be either open or closed. The generalization of circular regions to
CP1 is the obvious one. A circular region in CP1 is deﬁned to be the sets in CP1 for which
the stereographic projection is a circular region in C. Note that SL2(C) acts transitively on
the set of all circular regions in C or in CP1. We now state a lemma to Laguerre’s theorem,
which gets at the heart of the importance of circular regions.
Lemma 4.3 Let C ⊆CP1 be a circular region, and let φ ∈SL2(C) be such that its pole is
not in C. Then, the stereographic projection of φ · C is convex.
Proof Let (x0 : y0) /∈C be the pole of φ. Then, φ maps (x0 : y0) to ∞∈CP1 and maps C to
another circular region. Since (x0 : y0) /∈C implies ∞/∈φ · C, the sterographic projection
of φ · C is either an open half-plane or is bounded away from ∞. Since φ · C is a circular
region, it must be convex.
⊓⊔
This then leads to a natural extension of the notion of a circular region.
Deﬁnition 4.4 Given C ⊆CP1, we say that C is projectively convex if for every φ ∈SL2(C)
with pole not in C, the stereographic projection of φ · C is convex.
We now classify all projectively convex sets in CP1 in the following. This result has been
demonstrated before in [18], where projectively convex regions are referred to as generalized
circular regions.
Proposition 4.5 (Zervos) Let C ⊆CP1 be projectively convex. Then, C = C◦∪γ , where
C◦is an open circular region which is the interior of C, and γ is a connected subset of the
boundary of C◦. In particular, projective convexity is preserved under taking complements.
So,oneexampleofaprojectivelyconvexsetwhichisnotquiteacircularregionis H+∪R+.
Another is H+ ∪[0, 1]. Yet another (albeit after a bit of consideration) is H+ ∪(−∞, 0) ∪
(1, ∞]. We now state a homogeneous version of Laguerre’s theorem, extended to projectively
convex sets.
Proposition 4.6 (Laguerre) Let C ⊆CP1 be projectively convex, and ﬁx φ ∈SL2(C). If the
pole of φ is in C, then dφ preserves strong C-stability.
Proof Gauss–Lucas and the fact that CP1\C is projectively convex give the result. Specif-
ically, for C-stable p ∈V (n) consider φ · p, which is stable in φ · C ∋∞. Letting B be
the complement of C, the dehomogenization of this polynomial is then of degree exactly n
with all of its roots in the stereographic projection of φ · B. By projective convexity, φ · B is
convex and therefore Gauss–Lucas implies ∂x(φ · p) is φ · C-stable and not identically zero.
Applying φ−1 then implies dφ p = (φ−1∂xφ)p is C-stable.
⊓⊔
Corollary 4.7 Let Ck ⊆CP1 be projectively convex regions for k ∈[m], and ﬁx φ ∈SL2(C).
If the pole of φ is in Ck0, then dφ acting on the variables (xk0, yk0) preserves strong (C1 ×
· · · × Cm)-stability.
A representation theoretic explanation...
1373
Proof Follows from the fact that taking derivatives in some variables commutes with eval-
uation in the others. Speciﬁcally, p ∈V (λ) is (C1 × · · · × Cm)-stable iff p̸ = 0 for all
evaluations in C1 × · · · × Cm. So, evaluating p in all variables in that product of sets except
(xk0, yk0) gives us a Ck0-stable polynomial in V (λk0). Applying the previous proposition
then gives the result.
⊓⊔
