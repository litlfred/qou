---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: sec-017-51-theorem-51-will-follow-once-it-has-been-estab
section_title: "Theorem 5.1 will follow once it has been established that C(M) is invariant"
section_number: 5.1
pages: 19-22
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
doc_brief: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state"
---
under bistellar moves of orders 2 and 3. The bistellar moves of order 1 and 0 are
the inverses of these moves.
The simplicial invariant can be decomposed as Z(M,lM )=t r ( Z(X),Z (D1))
andZ(N,lN )=t r (Z(X),Z (D2)), where D1 andD2 are the simplicial disks in the
bistellar moves,D1∪D2 =∂(01234),M =X∪D1,N =X∪D2,a n dX∪(01234) is
labelled with restriction lM toM andlN toN. The linear map Z(X) is deﬁned to
be the partial trace over the state spaces of all triangles not in the boundary ofX of
the tensor product of the partition functions for each oriented labelled tetrahedron
inX. The linear maps Z(D1)a n dZ(D2) are deﬁned likewise.
The invariance of C(M) under bistellar moves follows by establishing that
K−v1 ∑
l
(
Z(D1)
∏
e
(dimq(l(e)))
)
=K−v2 ∑
l
(
Z(D2)
∏
e
(dimq(l(e)))
)
.
In this formula, v1, v2 are the number of vertices internal to D1, D2 (i.e., not on
the boundary); the product is over edges internal to D1 orD2, and the summation
is over labellings which are ﬁxed on ∂D1 =∂D2 but range over all values in J for
all edges internal to D1 or D2.
For the bistellar move of order 2, there are no internal vertices and the equality
is the Biedenharn-Elliot identity of Proposition 5.2.
For the bistellar move of order 3, the required identity is
4016 JOHN W. BARRETT AND BRUCE W. WESTBURY
Lemma 5.3.
Z(0234) =K−1 ∑
e01,e12,
e13,e14∈J
(
tr3
((
1⊗Z(0123)
)(
P⊗ 1
)(
1⊗Z(0134)
)(
P⊗ 1
)
·
(
Z(1234)⊗ 1
)(
1⊗Z(−0124)
)) ∏
n=0,2,3,4
dimq(e1n)
)
,
in which tr3 is the partial trace over the third factor:
(α⊗β⊗γ)↦→α⊗β tr(γ).
Proof. Follow the linear maps on each side of the Biedenharn-Elliot relation with
the linear map
K−1 dimq (e01)d i mq (e12)d i mq (e14)( 1⊗Z(−0124)),
take the partial trace on the third factor and sum overe01∈J,e12∈J,a n de14∈J.
The right-hand side of the Biedenharn-Elliot identity becomes the right-hand side
of the equation in the statement of the lemma. The left-hand side becomes
K−1 ∑
e01,e12,e14∈J
tr3
((
Z(0234)⊗ 1
)(
1⊗Z(0124)
)(
1⊗Z(−0124)
))
dimq (e01)
· dimq (e12)d i mq (e14).
Using the orthogonality relation of Proposition 5.2, this is equal to
K−1
dimq(e02)
∑
e01,e12∈J
tr3
((
Z(0234)⊗ 1
))
dimq (e01)d i mq (e12).
Also,
tr3
((
Z(0234)⊗ 1
))
=Z(0234) dim Hom(e02,e 12⊗e01),
using the ordinary vector space dimension dim. From the symmetry conditions and
Lemma 2.14, it follows that
∑
e01
dimq(e01)d i mH o m (e02,e 12⊗e01)=
∑
e01
dimq(e01)d i mH o m (e01, ˆe12⊗e02)
=d i mq(e12)d i mq(e02).
Thus the left-hand side of the relation is equal to
K−1Z(0234)
∑
e12∈J
(dimq (e12))2 =Z(0234).
Thus the lemma is proved.
To complete the proof of Theorem 5.1, it remains to prove Proposition 5.2. The
ﬁrst step is
Lemma 5.4 (Crossing). The following diagram is commutative:
⨁
e02∈J
H(e23,e03,e02)⊗H(e12,e02,e01)
Φ
−−−−→
⨁
e13∈J
H(e23,e13,e12)⊗H(e13,e 03,e01)
α⊗β↦→α(1⊗β)
↓ α⊗β↦→β(α⊗1)
↓
Hom(e03,e23⊗ (e12⊗e01)) Hom(e03, (e23⊗e12)⊗e01)
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 4017
where the linear map
Φ=
⨁
e02∈J
e13∈J
dimq(e13)
{
e01 e02 e12
e23 e13 e03
}
+
.
Also, the linear map
Ψ=
⨁
e02∈J
e13∈J
dimq(e02)
{e01 e02 e12
e23 e13 e03
}
−
is the inverse of Φ.
Proof. The semisimple condition implies that the vertical arrows are isomorphisms.
Consider an element α⊗β in the top left-hand space. Taking the trace of the two
images of this element in the bottom right-hand space with ( γ⊗ 1)δ for arbitrary
γ∈ Hom(e23⊗e12,e 13)a n dδ∈ Hom(e13⊗e01,e 03) yields two elements ofF which
are equal. This shows that the diagram commutes. Replacing the map Φ with the
inverse of Ψ also yields a commutative diagram, by a similar argument. Combining
these two diagrams shows that Φ = Ψ−1.
Proof of Proposition 5.2. The proof of the orthogonality relation is a direct conse-
quence of Lemma 5.4. The Biedenharn-Elliot identity follows from the fact that
the following diagram commutes (in this diagram the shorthand notation (012) is
used for the state space of this triangle, Hom( e02,e 12⊗e01)):
⨁
e02,e03∈J
(034)⊗ (023)⊗ (012)
1⊗Z(0123)
−−−−−−−→
⨁
e03,e13∈J
(034)⊗ (123)⊗ (013)
Z(0234)⊗1
↓
↓(P⊗1)(1⊗Z(0134))
⨁
e13,e14∈J
(123)⊗ (134)⊗ (014)
↓PZ (1234)⊗1
⨁
e02,e24∈J
(234)⊗ (024)⊗ (012)
1⊗Z(0124)
−−−−−−−→
⨁
e14,e24∈J
(234)⊗ (124)⊗ (014)
Applying Lemma 5.4 ﬁve times shows that this diagram commutes.
Remarks . The idea of using a state sum model to construct manifold invariants
is due to [25], where an invariant is constructed from the 6 j-symbols of Uqsl2,
for q a root of unity. Every state space H(a,b,c )i s0o r C and every map
θ(σ): Vσ (a,b,c )→ V (a,b,c ) is the identity. Hence the partition function of a
labelled tetrahedron is simply a number, and these numbers are equal under permu-
tations of the labels. These numbers are the quantum analogues of the 6j-symbols.
The identities of Proposition 5.2 are the quantum analogues of the well-known
Biedenharn-Elliot and orthogonality identities, as proved in [18].
This example satisiﬁes some extra conditions, which entail ﬁrstly that the in-
variant is deﬁned for unoriented manifolds, and secondly that there is a topological
quantum ﬁeld theory associated to the invariant.
The ﬁrst condition is that each space H(a,b,c ) is an inner product space and
that the partition function of−A is the adjoint of the partition function of A with
4018 JOHN W. BARRETT AND BRUCE W. WESTBURY
respect to these inner products. This condition implies that the invariant is deﬁned
for unoriented manifolds.
The second condition is that each self-dual simple object in the category is
orthogonal and not symplectic. If a is a self-dual simple object, then there is an
isomorphism φ: a→ ˆa. This object is called orthogonal if φ = ˆφ, or symplectic if
φ =−ˆφ. These are the only possibilities, as ˆ is an involution. This classiﬁcation
does not depend on the choice of isomorphism φ,a sH o m (a, ˆa)∼=F andˆ is linear.
This condition is necessary for the construction of a topological ﬁeld theory by
a construction similar to that of [25], because it is necessary for the isomorphisms
of naturality (Deﬁnition 3.1) and symmetry (Deﬁnition 3.7) on the state space
of a triangle to commute. The condition is a suﬃcient condition because it is a
coherence condition which allows the construction of a strict spherical category in
which ˆa =a for all self-dual objects.
For the example of Uqsl2, there are exactly two choices of the element w which
make this Hopf algebra spherical. The topological ﬁeld theory of [25] is constructed
with the element for which every simple module is orthogonal. At the value q =1 ,
this elementw takes the value 1 on the even (integer spin) representations and −1
on the odd (odd half-integer spin) representations.
