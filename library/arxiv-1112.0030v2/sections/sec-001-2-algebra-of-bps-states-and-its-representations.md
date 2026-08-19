---
doc_id: arxiv-1112.0030v2
doc_title: "Homological algebra of knots and BPS states"
section_id: sec-001-2-algebra-of-bps-states-and-its-representations
section_title: "Algebra of BPS states and its representations"
section_number: 2
pages: 7-10
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
doc_brief: "Homological algebra of knots and BPS states — It is known that knot homologies admit a physical descriptio n as spaces of open BPS states. W e study operators and algebras acting on these spaces."
---
Diﬀerentials in knot homology form a part of a larger algebraic struct ure that
has an elegant interpretation in the geometric / physical framewor k. Because this
algebraic structure has analogs in more general string / M-theory compactiﬁcations,
in this section we shall consider aspects of such structure for an a rbitrary Calabi-
Yau 3-fold X with extra branes supported on a general Lagrangian submanifold
L⊂ X, e.g.
space-time : R× X× M4(2.1)
M5-brane : R× L× D
For applications to knot homologies, one should take X to be the total space of
theO(−1)⊕O (−1) bundle over CP1 and LK to be the Lagrangian submanifold
determined by a knot K [15, 28, 29 ]. Then, (2.1) becomes precisely the setup
(1.6), in which homological knot invariants are realized as spaces of r eﬁned BPS
states, cf. (1.2).
In fact, there are two spaces of BPS states relevant to this particular problem
and its variants based on a more general 3-fold X. One is the space of reﬁned closed
BPS states, denoted as Hclosed
BPS , and the other is called the space of reﬁned open
BPS states, Hopen
BPS . The diﬀerence is that, while the latter contains BPS particles
in the presence of defects 3, the former comprises only those BPS states which are
still present in a theory when all defects are removed. In the desc ription [ 11] via
equivariant instanton counting on a 4-manifold M4, the defect (M5-brane) corre-
sponds to a particular ramiﬁcation along the divisor D⊂ M4, the so-called surface
operator.
On the other hand, if one looks at the general setup (2.1) from the vantage
point of the Calabi-Yau space X, then Hclosed
BPS andHopen
BPS can be formulated in
terms of enumerative invariants of X and ( X, L) that “count”, respectively, closed
holomorphic curves embedded in X and bordered holomorphic Riemann surfaces
(Σ , ∂Σ)֒→( X, L) with boundary on the Lagrangian submanifold L. As a way to
remember this, it is convenient to keep in mind that
3M5-branes in the M-theory setup (2.1)
8 SERGEI GUKOV AND MARKO STO ˇSI ´C
• Hclosed
BPS depends only on the Calabi-Yau space X
• Hopen
BPS depends on both the Calabi-Yau space X and the Lagrangian sub-
manifold L⊂ X
In applications to knots, open (resp. closed) BPS states are repr esented by open
(resp. closed) membranes in the M-theory setup (1.6) or by bound states of D0
and D2 branes in its reduction to type IIA string theory. It is the sp ace of open
BPS states that depends on the choice of the knot K and, therefore, provides a
candidate for homological knot invariant in (1.2).
In general, the space of BPS states is Γ ⊕ Z-graded, where Γ is the “charge
lattice” and the extra Z-grading comes from the (half-integer) spin of BPS states,
such that 2 j3∈ Z. For example, in the case of closed BPS states, the charge lattice
is usually just the cohomology lattice of the corresponding Calabi-Ya u 3-fold X,
(2.2) Γ = H even(X; Z) .
In the case of open BPS states, Γ also depends on the choice of the Lagrangian
submanifold L⊂ X.
When X is the total space of the O(−1)⊕O (−1) bundle over CP1 and L = LK,
as in application to knot homologies, the lattice Γ is two-dimensional fo r both open
and closed BPS states. As a result, both Hclosed
BPS andHopen
BPS are Z⊕ Z⊕ Z-graded.
In particular, the space of open BPS states is graded by spin 2 j3 ∈ Z and by
charge γ = ( n, β)∈ Γ, where the degree β∈ H2(X, LK)∼
= Z is sometimes called
the “D2-brane charge” and n∈ Z is the “D0-brane charge.” In relation to knot
homologies (1.2), these become the three gradings of the theory c ategorifying the
colored HOMFLY polynomial:
(2.3)
“a− grading” = β∈ H2(X, LK)∼
= Z
“q− grading” = n∈ Z
“t− grading” = 2 j3∈ Z
Now, let us discuss the algebraic structure that will help us underst and the
origin of diﬀerentials acting on the triply-graded vector space Hknot =Hopen
BPS . The
fact that Hclosed
BPS forms an algebra is well appreciated in physics [ 30] as well as in
math literature [ 31]. Less appreciated, however, is the fact that Hopen
BPS forms a
representation of the algebra Hclosed
BPS :
(2.4)
reﬁned open BPS states : Hopen
BPS
⟲
reﬁned closed BPS states : Hclosed
BPS
Indeed, two closed BPS states, B1 andB2, of charge γ1, γ2∈ Γ can form a bound
state,B12 of charge γ1 + γ2, as a sort of “extension” of B1 andB2,
(2.5) 0 → B2 → B12 → B1 → 0 ,
thereby deﬁning a product on Hclosed
BPS :
(2.6)
Hclosed
BPS ⊗ Hclosed
BPS −→ Hclosed
BPS
(B1 , B2 ) ↦→ B12
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 9
. =
Similarly, a bound state of a closed BPS state Bclosed
1 ∈H closed
BPS with an open BPS
stateBopen
2 ∈H open
BPS is another open BPS state Bopen
12 ∈H open
BPS :
(2.7) ( Bclosed
1 , Bopen
2 ) ↦→ Bopen
12
=.
This deﬁnes an action of the algebra of closed BPS states on the spa ce of open BPS
states.
The process of formation or fragmentation of a bound state in (2.6 ) and (2.7)
takes place when the binding energy vanishes. Since the energy of a BPS state is
given by the absolute value of the central charge 4 functionZ : Γ→ C this condition
can be written as
(2.8)
⏐
⏐Z(γ1 + γ2)
⏐
⏐−
⏐
⏐Z(γ1)
⏐
⏐−
⏐
⏐Z(γ2)
⏐
⏐ = 0
for a process that involves either B12→B 1 +B2 or its inverse B1 +B2→B 12. A
particular instance of the relation (2.8) is when the central charge of the fragment
vanishes:
(2.9) Z(γfragment) = 0
Then, a fragment becomes massless and potentially can bind to any o ther BPS state
of charge γ. When combined with (2.4), it implies that closed BPS states of zero
mass correspond to operators acting on the space of open BPS st atesHopen
BPS . The
degree of the operator is determined by the spin and charge of the corresponding
BPS state, as in (2.3).
For example, when X is the total space of the O(−1)⊕O (−1) bundle over
CP1, as in application to knot homologies, we have
(2.10) exp( Z) = aβ qn ,
where we used the relation (1.8) between a and Vol(CP1). Therefore, for special
values of a and q we have the following massless fragments, cf. (1.9):
(2.11)
a = q−N : D2/D0 fragments
a = qN :
D2/D0 fragments
q = 1 : D0 fragments
Moreover, the D2/D0 fragments obey the Fermi-Dirac statistics ( see e.g. [18, 23 ])
and, therefore, lead to anti-commuting operators ( i.e. diﬀerentials) on Hopen
BPS .
To summarize, we conclude that various specializations of the param eters (sta-
bility conditions) are accompanied by the action of commuting and ant i-commuting
operators onHopen
BPS . The algebra of these operators is precisely the algebra of closed
BPS states Hclosed
BPS . Mathematical candidates for the algebra of closed BPS states
include variants of the Hall algebra [ 32], which by deﬁnition encodes the structure
of the space of extensions (2.5):
(2.12) [ B1]· [B2] =
∑
B12
|0→B 2→B 12→B 1→ 0| [B12]
4The central charge function is a linear function in the sense that Z(γ1 +γ2) = Z(γ1)+ Z(γ2),
i.e. it deﬁnes a homomorphism Z ∈ Hom(Γ , C).
10 SERGEI GUKOV AND MARKO STO ˇSI ´C
In the present case, the relevant algebras include the motivic Hall a lgebra [ 17], the
cohomological Hall algebra [ 31], and its various ramiﬁcations, e.g. cluster algebras.
Therefore, the problem can be approached by studying represen tations of these
algebras, as will be described elsewhere.
