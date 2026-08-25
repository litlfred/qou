---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-005-21-the-reidemeister-torsion-we-review-the-basic
section_title: "The Reidemeister torsion. We review the basic notions and results about the"
section_number: 2.1
pages: 3-5
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — W e study a computational method of the hyperbolic Reidemeister torsion (also called in the"
---
sign–determined Reidemeister torsion introduced by V. Turaev whic h are needed in
this paper. Details can be found in Milnor’s survey [Mil66] and in Turaev’s mono-
graph [Tur02].
Torsion of a chain complex. Let C∗ = (0 → Cn
dn
− →Cn−1
dn−1
− − − → · · ·
d1
− →C0 → 0) be a
chain complex of ﬁnite dimensional vector spaces over a ﬁeld F. Choose a basis c(i) of
Ci and a basis hi of the i-th homology group Hi(C∗). The torsion of C∗ with respect to
these choices of bases is deﬁned as follows.
For each i, let bi be a set of vectors in Ci such that di(bi) is a basis of Bi−1 =
im(di : Ci → Ci−1) and let ˜hi denote a lift of hi in Zi = ker( di : Ci → Ci−1). The
set of vectors di+1(bi+1)˜hibi is a basis of Ci. Let [ di+1(bi+1)˜hibi/ci] ∈ F∗ denote the
determinant of the transition matrix between those bases (the en tries of this matrix are
coordinates of vectors in di+1(bi+1)˜hibi with respect to ci). The sign-determined Reide-
meister torsion of C∗ (with respect to the bases c∗ and h∗) is the following alternating
product (see [Tur01, Deﬁnition 3.1]):
(1) Tor( C∗, c∗, h∗) = ( −1)|C∗| ·
n∏
i=0
[di+1(bi+1)˜hibi/ci](−1)i+1
∈ F∗.
3
Here
|C∗| =
∑
k/greaterorequalslant0
αk(C∗)βk(C∗),
where αk(C∗) = ∑ k
i=0 dim Ci and βk(C∗) = ∑ k
i=0 dim Hi(C∗).
The torsion Tor( C∗, c∗, h∗) does not depend on the choices of bi nor on the lifts ˜hi.
Note that if C∗ is acyclic ( i.e. if Hi = 0 for all i), then |C∗| = 0.
Torsion of a CW-complex. Let W be a ﬁnite CW-complex and ( V, ρ) be a pair of a vector
space with an inner product over F and a homomorphism of π1(W ) into Aut(V ). The
vector space V turns into a right Z[π1(W )]-module denoted Vρ by using the right action
of π1(W ) on V given by v · γ = ρ(γ)−1(v), for v ∈ V and γ ∈ π1(W ). The complex of the
universal cover with integer coeﬃcients C∗(~W ; Z) also inherits a left Z[π1(W )]-module
via the action of π1(W ) on ~W as the covering group. We deﬁne the Vρ-twisted chain
complex of W to be
C∗(W ; Vρ) = Vρ ⊗Z[π1(W )] C∗(~W ; Z).
The complex C∗(W ; Vρ) computes the Vρ-twisted homology of W which we denote as
H∗(W ; Vρ).
Let
{
ei
1, . . . , ei
ni
}
be the set of i-dimensional cells of W . We lift them to the uni-
versal cover and we choose an arbitrary order and an arbitrary o rientation for the cells{
˜ei
1, . . . ,˜ei
ni
}
. If we let {v1, . . . ,vm} be an orthonormal basis of V , then we consider the
corresponding basis
ci =
{
v1 ⊗ ˜ei
1, . . . ,vm ⊗ ˜ei
1, · · · , v1 ⊗ ˜ei
ni, . . . ,vm ⊗ ˜ei
ni
}
of Ci(W ; Vρ) = Vρ ⊗Z[π1(W )] C∗(~W ; Z). We call the basis c∗ = ⊕ici a geometric basis of
C∗(W ; Vρ). Now choosing for each i a basis hi of the Vρ-twisted homology Hi(W ; Vρ),
we can compute the torsion
Tor(C∗(W ; Vρ), c∗, h∗) ∈ F∗.
The cells
{
˜ei
j
⏐
⏐ 0 ⩽ i ⩽ dim W, 1 ⩽ j ⩽ ni
}
are in one–to–one correspondence with the
cells of W , their order and orientation induce an order and an orientation for the cells{
˜ei
j
⏐
⏐ 0 ⩽ i ⩽ dim W, 1 ⩽ j ⩽ ni
}
. Again, corresponding to these choices, we get a basis
ci
R over R of Ci(W ; R).
Choose an homology orientation of W , which is an orientation of the real vector
space H∗(W ; R) = ⨁
i/greaterorequalslant0 Hi(W ; R). Let o denote this chosen orientation. Provide each
vector space Hi(W ; R) with a reference basis hi
R such that the basis
{
h0
R, . . . ,hdim W
R
}
of H∗(W ; R) is positively oriented with respect to o. Compute the sign–determined
Reidemeister torsion Tor( C∗(W ; R), c∗
R, h∗
R) ∈ R∗ of the resulting based and homology
based chain complex and consider its sign
τ0 = sgn (Tor(C∗(W ; R), c∗
R, h∗
R)) ∈ {±1}.
We deﬁne the sign–reﬁned twisted Reidemeister torsion of W (with respect to h∗ and
o) to be
(2) τ0 · Tor(C∗(W ; Vρ), c∗, h∗) ∈ F∗.
This deﬁnition only depends on the combinatorial class of W , the conjugacy class of ρ,
the choice of h∗ and the homology orientation o. It is independent of the orthonormal
basis of V , of the choice of the lifts ˜ei
j, and of the choice of the positively oriented basis of
H∗(W ; R). Moreover, it is independent of the order and orientation of the c ells (because
they appear twice).
Remark 1. In particular, if the Euler characteristic χ(W ) is zero, then we can use any
basis of V . If we change the basis of V by another one, then the torsion is multiplicated
by the determinant of the bases change matrix to the power χ(W ).
4
One can prove that the sign–reﬁned Reidemeister torsion is invarian t under cellular
subdivision, homeomorphisms and simple homotopy equivalences. In f act, it is precisely
the sign ( −1)|C∗| in Equation (1) which ensures all these important invariance proper ties
to hold (see [Tur02]).
