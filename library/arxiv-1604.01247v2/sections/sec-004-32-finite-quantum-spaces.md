---
doc_id: arxiv-1604.01247v2
doc_title: "EXCEPTIONAL QUANTUM GEOMETRY"
section_id: sec-004-32-finite-quantum-spaces
section_title: "Finite quantum spaces"
section_number: 3.2
pages: 12-16
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
doc_brief: "EXCEPTIONAL QUANTUM GEOMETRY — Based on an interpretation of the quark-lepton symmetry in t erms of the unimodularity of the color group SU (3) and on the existence of 3 generations, we develop an"
---
The notion of ﬁnite-dimensional Euclidean (or formally real) Jordan a lgebra
was introduced and analyzed in [28] under the name r-number algebra in
order to formalize the properties of the observables of ﬁnite quan tum sys-
tems. A minimal set of requirement for the observables of a ﬁnite qu antum
system is that it is a ﬁnite-dimensional real vector space J such that one
can consistently deﬁne powers of any element and that if a sum of sq uares
of elements vanishes it implies that each of these elements vanishes. Given
the square x ↦→x2, one deﬁnes a symmetric bilinear product on J by setting
x · y = 1/ 2((x + y)2 − x2 − y2) for x, y ∈ J.
So let J be a ﬁnite-dimensional real vector space endowed with a sym-
metric bilinear product
(x, y ) ↦→x.y = y.x (3.1)
for x, y ∈ J and assume that the following condition is satisﬁed
∑
i∈I
(xi)2 = 0 ⇒ xi = 0, ∀i ∈ I (3.2)
for any ﬁnite family ( xi)∈I in J, where ( x)2 = x.x for x ∈ J. The above
condition for the product is refered to as formal reality condition . One has
the following result [28].
Theorem 1. Let J be as above and deﬁne xn ∈ J for x ∈ J and n ∈ N+ by
induction on n as x1 = x and xn+1 = x.x n.
Then the following conditions (i) and (ii) are equivalent :
(i) xr.x s = xr+s, for any x ∈ J and r, s ∈ N+
(ii) ( x2.y ).x = x2. (y.x ), for any x, y ∈ J
A ﬁnite-dimensional real commutative algebra satisfying (3.2) and t he
equivalent conditions (i) and (ii) of the theorem is referred to as a ﬁn ite-
dimensional Euclidean (or formally real ) Jordan algebra , [6], [34], [26].
Condition (i) of Theorem 1 is referred to as power associativity while
Condition (ii) is referred to as the Jordan identity. It is well known and easy
12
to show that the Jordan identity implies the power associativity but it is a
very nontrivial result that in the above context the power associa tivity com-
bined with the formal reality condition imply the Jordan identity [28]. On e
can ﬁnd in [3] other natural conditions on commutative power-asso ciative
algebras leading to the Jordan identity.
It is worth noticing that Condition (3.2) and Condition (i) of Theorem 1
(i.e. power associativity) are exactly the conditions needed to have spectral
resolutions of the elements of J. Indeed a ﬁnite-dimensional Euclidean Jor-
dan algebra J has a unit 1 l ∈ J such that 1 l.x = x for any x ∈ J and any
x ∈ J has a ﬁnite spectral resolution
x =
∑
r∈Ix
λ rer (3.3)
where Ix is a ﬁnite set, λ r ∈ R and e2
r = er ∈ J for any r ∈ Ix, er.e s = 0 for
r, s ∈ Ix with r ⁄= s and
1 l =
∑
r∈Ix
er (3.4)
i.e. ( er) is a ﬁnite family of orthogonal idempotents in J the sum of which
is the unit 1 l ∈ J. Furthermore the number of elements of Ix, card( Ix),
is bounded by a ﬁnite number which only depends on J that is one has
supx∈J(card(Ix)) < ∞.
This means that one can set
x0 = 1 l (3.5)
and that
P ↦→P (x) =
∑
r
P (λ r)er (3.6)
deﬁnes a homomorphism of unital algebras from the algebra R[X] of real
polynomials into J for any x ∈ J.
These ﬁnite-dimensional Euclidean Jordan algebras were classiﬁed in [28]
where the following theorem is proved.
13
Theorem 2. Any ﬁnite-dimensional Euclidean Jordan algebra is a direct sum
of a ﬁnite number of simple ideals. A ﬁnite-dimensional simp le Euclidean
Jordan algebra is isomorphic to one of
R and JSpin n+2 = R1 l⊕ Rn+2,
J 1
n+3 = Hn+3(R), J 2
n+3 = Hn+3(C),
J 4
n+3 = Hn+3(H), with n ∈ N
and J 8
3 = H3(O).
In the above statement JSpin n+1 = R1 l⊕ Rn+1 is endowed with the
product
(r1 l⊕ v). (r′1 l⊕ v′) = ( rr′ + ⟨v, v ′⟩)1 l⊕ (rv ′ + r′v)
where ⟨, ⟩ is the scalar product of the Euclidean space Rn+1 and, for any
involutive algebra A, Hn(A) denotes the space of hermitian n × n-matrices
with entries in A endowed with the product
A.B = 1
2 (AB + BA) (3.7)
where ( A, B ) ↦→AB is the product in Mn(A).
The absence of JSpin 1 in the above list comes from the fact that JSpin 1
is not simple but is isomorphic to the commutative associative algebra R ⊕ R
of the real functions on a two-points set. Furthermore, notice t hat one has
the following coincidence
H1(R) = H1(C) = H1(H) = H1(O) = R,
H2(R) = JSpin 2, H2(C) = JSpin 3, H2(H) = JSpin 5,
H2(O) = JSpin 9
and that the Hn(O) are not Jordan algebras for n ≥ 4.
In each ﬁnite-dimensional simple Euclidean Jordan algebra J, its unit 1 l
admits a decomposition
1 l =
c(J)∑
i=1
ei
14
with ei.e j = 0 for i ⁄= j (orthogonality) where the ei are primitive idem-
potents. The number c(J) does only depend on J and is refered to as
the capacity (or the degree) of J. One has c(R) = 1, c(JSpin n+2) = 2,
c(J 1
3 ) = c(J 2
3 ) = c(J 4
3 ) = c(J 8
3 ) = 3 and c(J 1
n) = c(J 2
n) = c(J 4
n) = n for n ≥ 4.
Note the obvious fact that a ﬁnite-dimensional Euclidean Jordan alg e-
bra J which is associative is the algebra of real functions on a ﬁnite space
K which can be identiﬁed to the set of characters of J, that is the set of
homomorphisms
χ : J → R
of unital algebras. More generally, it will be convenient in the following to
consider that a ﬁnite-dimensional Euclidean Jordan algebra J is the algebra
of “real function” on some associated “ ﬁnite quantum space ” (a dual object).
This is justiﬁed by the above spectral properties as well as by the f act that
J is the set of observable of a ﬁnite quantum system (see below). Ind eed the
pure states on J are the primitive idempotents in J and the transition prob-
abilities between two states are the appropriate traces of the cor responding
product of idempotents.
Recall ﬁnally that a Jordan algebra over a commutative ﬁeld K is a K-
vector space endowed with a symmetric bilinear product ( x, y ) ↦→x.y satisfy-
ing Property (ii) of Theorem 1. For inﬁnite-dimensional real Jordan algebras,
there are various generalizations of the formal reality condition (3 .2). In this
frame there are (bounded) generalizations of Theorem 1, see [25] for the
JB -algebra version and [39] for a weak version.
3.3 The exceptional ﬁnite quantum space
Apart J 8
3 , all the other ﬁnite-dimensional simple Euclidean Jordan alge-
bras can be realized as real vector spaces of self-adjoint operat ors in ﬁnite-
dimensional Hilbert spaces, stable by the anticommutator of the as sociative
composition of linear operators. They can therefore be considere d as algebras
of observabes of some ﬁnite quantum systems.These special algeb ras enter in
the frame of noncommutative geometry based on associative ∗-algebras and
each nonexceptional simple Lie algebra occurs as Lie algebra of deriv ations
of one of these special simple Euclidean Jordan algebras.
15
However, as proved in [2] the Jordan algebra J 8
3 is exceptional which
means that it cannot be inbedded in an associative algebra as a subsp ace
stable by the anticommutator of the associative product as Jorda n product.
Let us recall that if A is an associative algebra with product ( x, y ) ↦→xy,
then the anticommutator ( x, y ) ↦→x.y = 1
2(xy + yx) is a Jordan product on
A and one denotes by AJ ord the corresponding Jordan algebra. A Jordan
algebra which is isomorphic to a Jordan subalgebra of some AJ ord as above
is said to be special, otherwise it is said to be exceptional.
In spite of the fact that J 8
3 is exceptional it can be consistently consid-
ered as the algebra of observable of a ﬁnite quantum system, see e .g. [28],
[23]. Thus it corresponds to an exceptional quantum space which is in fact
unique [42], [43]. Notice that since dim R(J 8
3 ) = 27 < ∞, we consider that
the “corresponding quantum space” is “ﬁnite”.
The group of all automorphisms of J 8
3 is the exceptional Lie group F4
with Lie algebra Lie( F4) = f4 which is the Lie algebra of all derivations of
J 8
3 . Therefore at ﬁrst sight F4 plays the role of diﬀeomorphism group of the
exceptional quantum space while the exceptional simple Lie algebra f4 plays
the role of the Lie algebra of vector ﬁelds on this exceptional quant um space.
Remark. Notice that these actions are inner. It follows that F4 and its Lie
algebra f4 admit an alternative interpretation in terms of gauge group and
Lie algebra. This applies as well for their subgroups and Lie subalgebr as. Of
particular interest in view of the analysis of Section 2 is the subgroup of F4
which preserves the representation of the octonion algebra O as C ⊕ C3, (see
in Section 4).
