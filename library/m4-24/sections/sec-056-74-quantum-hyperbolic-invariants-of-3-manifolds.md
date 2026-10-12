---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-056-74-quantum-hyperbolic-invariants-of-3-manifolds
section_title: "Quantum hyperbolic invariants of 3-manifolds"
section_number: 7.4
pages: 113-116
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
toc_source: inferred
---
The main references for this section are [42, 43, 44], a review being [46]. In [44]
the ideas of sections 7-9 in [43] are developed with some important diﬀerences
in the way they are concretized.
Let W be a compact closed oriented 3-manifold, L ⊂W be a non-empty link,
ρ be a ﬂat principal B-bundle on W ; B is the upper triangular Borel subgroup
of SL(2, C). In [43] one constructs a family of “quantum hyperbolic invariants”
(QHI) KN(W, L, ρ) ∈C, where N > 1 is any odd integer. This consists of two
main steps:
(1) For every triple (W, L, ρ), the construction of so-called D-triangulations
T = (T, H, D), where: (T, H) is a (singular) triangulation of (W, L) such
that each edge has distinct vertices and H contains all the vertices of T ;
the “decoration” D is made of a full simplicial B-1-cocycle representing
ρ on W , a branching (for instance one induced by a total ordering of the
vertices of T ), and an integral charge. For these notions, see [46].
(2) The proof that a suitable state sum HN(T ) does not depend on the choice
of the D-triangulation T up to multiplication by N -th roots of unity, so
that KN(W, L, ρ) = KN(T ) = HN(T )N actually deﬁnes an invariant.
The proof of the existence of D-triangulations is diﬃcult essentially due to
strong global constraints in D. The main building-blocks of the state sums
HN(T ) are the “quantum-dilogarithm” 6j-symbols of the N -dimensional cyclic
representations of a quantum Borel subalgebra of Uω(sl(2, C)), where ω =
exp(2πi/N).
Kashaev proposed in [195] a conjectural purely topological in-
variant KN(W, L) which should have been expressed by a state sum of this
kind (although in his proposal there were no ﬂat bundles and no notion of
D-triangulation); in fact, KN(W, L) appears as a special case of KN(W, L, ρ)
when ρ is the trivial ﬂat B-bundle on W .
The algebraic properties of the
6j-symbols ensure the invariance of KN(T ) up to certain elementary moves on
D-triangulations. Then, the proof of the full invariance of KN(T ) consists in
connecting by such elementary moves any two D-triangulations of (W, L, ρ),
which is not so easy to achieve.
Problem 7.18
(S. Baseilhac, R. Benedetti) Generalize the construction of
the QHI for ﬂat principal G-bundles, for Lie groups G diﬀerent from B.
Section 7.4 was written by S. Baseilhac and R. Benedetti.
Geometry & Topology Monographs, Volume 4 (2002)
486
T. Ohtsuki (Editor)
Remark A basic ingredient of the B-QHI is the relationship between the
cyclic representation theory of a quantum Borel subalgebra of Uω(sl(2, C)),
and ﬂat B-bundles encoded by simplicial full 1-cocycles.
This relationship
relies on the theory of quantum coadjoint action of [105], which holds for other
Lie groups such as G = SL(2, C).
Problem 7.19
(S. Baseilhac, R. Benedetti) Fix (W, L) and vary ρ. Study
KN as a function of the bundle, that is as a function deﬁned on the character
variety of W with respect to B: regularity, ﬁbers, and so on.
Remark Denote by z the B-1-cocycle in T that represents ρ. The state sum
KN(T ) is a rational function of the upper diagonal entries of the whole set of
values of z. Moreover, the 6j-symbols are rational functions of the moduli of
the idealized triangulation bF(T ) deﬁned below.
Every α ∈H1(W; C) leads to two ﬂat B-bundles ρα and ρ′
α deﬁned as fol-
lows. The ﬁrst one is obtained via the natural identiﬁcation of (C, +) with the
parabolic subgroup Par(B) of B. The second one is obtained by means of the
exponential map of (C, +) onto the multiplicative C∗, and the identiﬁcation of
C∗with the diagonal Cartan subgroup C(B) of B. Similarly, every class in
H1(W; Z/pZ) leads to a B-bundle by the natural embedding of Z/pZ into the
group S1 ⊂C∗.
Problem 7.20 (S. Baseilhac, R. Benedetti) Specialize Problem 7.19 to bun-
dles coming from the ordinary cohomology as above. For real additive ones,
analyze the behaviour of the QHI with respect to Thurston’s norm. Are they
constant on the faces of the corresponding unit sphere ?
Remark The “projective invariance” property of the QHI (see [43, 46]) implies
in particular that they are constant on the rays of H1(W; R).
Problem 7.21
(S. Baseilhac, R. Benedetti) Understand the ‘phase factor’
(i.e. the ambiguity due to N -th roots of unity) of the state sum HN(T ). Possi-
bly derive from it an invariant for (W, L, ρ) endowed with some extra-structure,
thus reﬁning KN(W, L, ρ).
Remark The phase factor uniquely depends on the branching and the integral
charge in the decoration D. On one hand, it is known that branchings can be
used to encode, for instance, combings, framings, spin structures and so on.
On another hand, combings induce the extra-structure that allows Turaev’s
reﬁnement of Reidemeister torsions.
Geometry & Topology Monographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds
487
Problem 7.22
(S. Baseilhac, R. Benedetti) Determine a suitable (2 + 1)
‘decorated’ cobordism theory supporting a (non purely topological) QFT con-
taining the already deﬁned QHI. Study in particular the behaviour of the QHI
with respect to connected sums.
Problem 7.23 (S. Baseilhac, R. Benedetti) Develop a 4-dimensional theory
of QHI based on Turaev’s shadow theory.
Remark A ﬁrst step should be to determine the right notion of D-shadow
together with a geometric interpretation. In this direction, F. Costantino is
completing his PhD thesis at Pisa, where he shows in particular that ‘branched
shadows’ do encode Spinc structures.
Problem 7.24
(S. Baseilhac, R. Benedetti) Determine the actual relation-
ship between KN(S3, ·) and the coloured Jones polynomial JN(·) (evaluated at
ω = exp(2iπ/N) and normalized by JN(unknot) = 1), as functions of links.
Remark (1) In [296] it is shown that JN may be deﬁned by means of usual
(1, 1)-tangle presentations (as for the Alexander polynomial), using an enhanced
Yang-Baxter operator whose R-matrix is derived from the quantum-dilogarithm
6j-symbols. This suggests that there could be a relationship between KN(S3, ·)
(necessarily associated to the trivial ﬂat B-bundle on S3) and JN(·)N . The
most immediate guess would be that KN(S3, L) = JN(L)N for each L. In
fact, one can give an R-matrix formulation of KN(S3, ·) involving R-matrices
depending on parameters. These parameters are speciﬁed in terms of the dec-
orations of special D-triangulations adapted to planar link diagrams [45]. So
KN(S3, ·) can be computed by using suitably decorated link diagrams, and the
decoration must satisfy non trivial global constraints.
In this setup, (1, 1)-
tangle presentations do not play any role. On another side, the constant R-
matrix used for JN corresponds to one ﬁxed particular choice in the parameters.
This is not enough to conﬁrm the above guess.
(2) A motivation of Problem 7.24 is also to make working for JN a theory of
scissors congruence classes, as described below for the QHI.
The so-called Volume Conjectures concern the asymptotic behaviour of the
invariants constructed on the base of the quantum dilogarithm 6j-symbols,
that is of KN(W, L, ρ) or JN(L) (for L ⊂S3), when N →∞.
They are
originally motivated by the asymptotic behaviour of the quantum dilogarithm
6j-symbols, whose dominant term involves dilogarithm functions that may be
Geometry & Topology Monographs, Volume 4 (2002)
488
T. Ohtsuki (Editor)
used to compute the volume of oriented ideal hyperbolic tetrahedra. In the
case of JN(L) there are also some numerical computations (sometimes using
formal manipulations) - see for instance the ﬁrst section of the present volume
for details. In the case of QHI, we develop in [43, 44] (see also [46]) a theory of
scissors congruence classes for triples (W, L, ρ) which gives a natural framework
for a formulation of a volume conjecture.
This goes roughly as follows. One constructs a ‘Bloch-like’ group P(D) based
on D-decorated tetrahedra, which maps via an explicit idealization map bF onto
an enriched version P(I) of the classical Bloch group, built on hyperbolic ideal
tetrahedra. Any D-triangulation T of (W, L, ρ) leads to elements cD(W, L, ρ) ∈
P(D) and cI(W, L, ρ) = bF(cD(W, L, ρ)) ∈P(I). They are respectively called
the D- and I-scissors congruence classes of (W, L, ρ).
The QHI essentially
depend on the D-class, and for any given D-triangulation T the 6j-symbols
occurring in HN(T ) depend on the moduli of the hyperbolic tetrahedra of the
idealization bF(T ) of T . By using the classical Rogers dilogarithm one can also
deﬁne a dilogarithmic invariant R(W, L, ρ) which only depends on the I-class.
Conjecture 7.25 (S. Baseilhac, R. Benedetti) (Real Volume Conjecture for
QHI) For any triple (W, L, ρ) one has:
lim
N→∞(2π/N 2) log(|KN(W, L, ρ)|) = Im R
 cI(W, L, ρ)

.
Remark From the explicit formula of HN(T ) one easily shows that the left-
hand side of Conjecture 7.25, if it exists, only depends on the moduli of the
hyperbolic tetrahedra of bF(T ).
A natural problem is to ﬁnd a geometric
interpretation of the dilogarithmic invariant. Indeed, for scissors congruence
classes built with ideal triangulations of genuine (non-compact ﬁnite volume)
hyperbolic 3-manifolds M , a similar dilogarithmic invariant gives i(Vol(M) +
iCS(M)), where Vol is the Volume and CS is the Chern-Simons invariant (see
[309]).
In [46] one proposes a complex version of Conjecture 7.25, for the whole KN
(not only its modulus).
7.5
