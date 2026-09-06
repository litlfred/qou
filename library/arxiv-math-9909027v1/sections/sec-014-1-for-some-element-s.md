---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California"
section_id: sec-014-1-for-some-element-s
section_title: "(for some element S)"
section_number: 1
pages: 63-66
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
doc_brief: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California — We introduce a notion of planar algebra, the simplest exampl e of which is a vector space of tensors, closed"
---
T
S
=
If the bottom shaded region is assigned a spin a, and the top region a spin
b, the left-hand side gives ub
aTa and the right-hand side gives ub
aSb, so Ta is
independent of a, and dim P u
1 = 1. P u
1,3 is abelian because P1,3 is and P u
2 is
abelian since it is σ−1
u (σu(P2) ∩ P1,3) by 2.11.6. □
So by §4.3, a generalized Hadamard matrix u yields a subfactor whose
planar algebra invariant is P u. In fact such a subfactor was the starting point
of the theory of planar algebras, as the equations for P u are those for the
relative commutants of a spin model commuting square given i n [JS]. Note
that the original subfactor is hyperﬁnite whereas the one ob tained from 4.3
is not! We now determine P u
2 for a generalized Hadamard matrix u.
63
Deﬁnition 2.11.13. Given a Q × Q generalized Hadamard matrix ub
a
we deﬁne the Q2 × Q2 proﬁle matrix Prof(u) by
Prof(u)c,d
a,b =
∑
x
ux
aux
b ux
c ux
d .
The proﬁle matrix is used in the theory of Hadamard matrices. We will see
that it determines P u.
Deﬁnition 2.11.14. Given the Q2 × Q2 matrix Prof( u), deﬁne the
directed graph Γ u on Q2 vertices by ( a, b) → −(c, d) iﬀ Prof( u)c,d
a,b ⁄= 0.
The isomorphism class of Γ u is an invariant of Hadamard equivalence.
Theorem 2.11.15 If u is a Q × Q generalized Hadamard matrix thought
of as a biunitary for the spin model P σ, then the minimal projections of
the abelian C ∗-algebra P u
2 are in bijection with the connected components
of the graph Γ u. Moreover the (normalized) trace of such a projection is
n/Q2 where n is the size of the connected component, which is necessarily a
multiple of Q.
Proof. For matrices xb
a, y b
a, the equations of Theorem 2.11.3 are the
“star-triangle” equations
∑
d
ud
a ud
b xc
d = uc
a uc
b yb
a
which amount to saying that, for each ( a, b), the vector v(a,b) whose dth com-
ponent is the ud
aud
b is an eigenvector of the matrix xc
d with eigenvalue yb
a. The
proﬁle matrix is just the matrix of inner products ⟨v(a,b), v(c,d)⟩ so the or-
thogonal projection onto the linear span of v(a,b)’s in a connected component
is in P u
2 and is necessarily minimal since eigenvectors for distinct minimal
projections are orthogonal.
If the matrix x is an orthogonal projection, yb
a is either 1 or 0 depending
64
on whether v(a,b) is in the connected component or not. Consider the picture
x y=
Applying Reidemeister type II moves and summing we obtain th e assertion
about the trace. (It is a multiple of 1 /Q since x is a Q × Q matrix.) □
If G is a ﬁnite abelian group and g ↦→ˆg is an isomorphism of G with its
dual ˆG (=Hom(G, C∗)), we obtain a generalized Hadamard matrix u, with
Q = |G|, by setting uh
g = 1√Q
ˆh(g). We call this a standard generalized
Hadamard matrix. It is Hadamard if G = ( Z/2Z)n for some n. We leave it
to the reader to check that if u is standard P u is exactly the planar algebra
of §2.9 for the group G. In particular, dim( P u
k ) = Qk. It is well known in
subfactor theory that any subfactor with N ′ ∩ M1 = C[M :N ] comes from a
group. It can also be seen directly from association schemes that if dim(P u
2 ) =
Q then u is standard up to gauge equivalence (recall that P u is always an
assocation scheme as remarked in §2.8).
We have, together with R. Bacher, P. de la Harpe, and M.G.V. Bo gle
performed many computer calculations. So far we have not fou nd a gener-
alized Hadamard matrix u for which dim( P u
2 ) = 2 but dim( P u
3 ) > 5. Such
an example would be a conﬁrmation of our non-group symmetry p rogram as
group-like symmetries tend to show up in P2. In particular the ﬁve 16 × 16
Hadamard matrices have dim P u
2 = 16,8,5,3 and 3, and are completely dis-
tinguished by the trace. There are group-like symmetries in all cases corre-
sponding to the presence of normalizer in the subfactor pict ure.
Haagerup has shown how to construct many interesting exampl es and
given a complete classiﬁcation for Q = 5. In the circulant case he has shown
there are only ﬁnitely many examples for ﬁxed prime Q (see [ ]).
Perhaps somewhat surprisingly, the presence of a lot of symm etry in u can
65
cause P u
2 to be small! The kind of biunitary described in the following result
is quite common — the Paley type Hadamard matrices give an exa mple.
Proposition 2.11.17 Suppose Q−1 is prime and let u be a Q×Q generalized
Hadamard matrix with the following two properties (the ﬁrst of which is
always true up to gauge equivalence):
(i) There is an index ∗ with ua
∗ = u∗
a = 1 for all a.
(ii) The group Z/(Q − 1)Z acts transitively on the spins other
than ∗, and uga
gb = ua
b for all g ∈ Z/(Q − 1)Z.
Then dim( P u
2 ) = 2 or u is gauge equivalent to a standard matrix.
Proof. The nature of the equations 2.11.15 makes it clear that Z/(Q −
1)Z acts by automorphisms on P u
2 , obviously ﬁxing the projection e1 which
is the matrix xb
a = 1/Q. Thus the action preserves (1 − e1)P u
