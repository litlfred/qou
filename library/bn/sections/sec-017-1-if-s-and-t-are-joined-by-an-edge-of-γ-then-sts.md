---
doc_id: bn
doc_title: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009"
section_id: sec-017-1-if-s-and-t-are-joined-by-an-edge-of-γ-then-sts
section_title: "If s and t are joined by an edge of Γ, then sts = tst (we say s and t"
section_number: 1
pages: 22-27
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009 — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove"
---
braid);
2. Otherwise, s and t commute.
21
A
A
n−1
n
 
~
*
Figure 8. The braid groups of n points in C and C∗ correspond to the Coxeter
diagrams An−1 and ~An.
(For weighted graphs one allows longer relations of the form stst · · ·s =
tsts · · ·t, but we will only need the simply-laced systems above.)
Complex reﬂections. LetV be a ﬁnite-dimensional complex vector space,
and suppose q ∈S1, q ⁄= −1. A linear map T :V →V is a q-reﬂection if it
acts by v ↦→ −qv on a 1-dimensional subspace of V , and by the identity on
a complementary subspace.
Every Artin group admits a ﬁnite-dimensional representati on
~ρq :A(Γ) → GL(CS)
such that each s ∈S acts by a q-reﬂection through es. One such represen-
tation is given by the action
s(x) = x − (q + 1) ⟨x,e s⟩
⟨es,e s⟩es (5.1)
with respect to the (possibly degenerate) real-valued inne r product satisfying
⟨es,e t⟩ =





2 if s =t,
0 if s and t commute, and
− sec(θ/2) if s and t braid.
Here θ = argq ∈ (−π,π ). The value − sec(θ/2) is determined (up to sign)
by the condition that the braid relation sts = tst holds in the subspace
C{s,t }.
Phase shift. More generally, we can modify this representation of A(Γ) by
specifying a phase shift φ(s,t ) ∈S1 whenevers and t braid (cf. [Mos1]), to
obtain a new inner product
⟨es,e t⟩ =φ(s,t ) sec(θ/2).
22
We assume φ(s,t ) = φ(t,s ), so this inner product is Hermitian. Then the
action deﬁned by (5.1) for the new inner product still respec ts the braiding
and commutation relations.
The shifted representation ofA(Γ) depends only on q and the cohomology
class of φ inH 1(D,S 1) (represented by the cochain sending the edge [ s,t ] to
φ(s,t ) ∈S1.) In particular, if Γ is a tree, then the q-reﬂection representation
is unique up to conjugacy, and we refer to its image as a complex reﬂection
group of type Γ( q).
Reduction. The quotient of CS by the subspace N = {x : ⟨x,y ⟩ = 0 ∀y}
yields the reduced complex reﬂection representation
ρq :A(Γ) → U(CS/N).
Proposition 5.1 If Γ is connected, then ρq is irreducible for all q ⁄= −1.
Proof. Let V ⊃ N be an invariant subspace of CS with V ⁄= N . Then
⟨v,e s⟩ ⁄= 0 for some v ∈V ands ∈S. Therefore v −sv = (q +1)⟨v,e s⟩es ∈V
and hence es ∈ V . Now if s and t braid, then ⟨es,e t⟩ ⁄= 0 and thus et ∈V
as well. Connectivity of Γ then implies V = CS.
Coxeter groups and Shephard groups. The Shephard group A(Γ,d ) is
the quotient of A(Γ) by the relations sd = 1 for all s ∈S (cf. [KM]). Note
that ρq factors through A(Γ,d ) whenever ( −q)d = 1. The quotient A(Γ, 2)
is the usual Coxeter group associated to Γ, and ρ1 is its usual reﬂection
representation.
Braid groups. Recall that the Coxeter diagrams An and ~An are simply
an interval and a circle, each with n vertices. The braid group Bn, with its
standard generators, can be identiﬁed with the Artin group o f type An−1.
Other spherical and aﬃne Coxeter diagrams arise from braid g roups for
other orbifolds [Al1]. In particular, the Artin group of the type ~An can
be identiﬁed with the braid group ~Bn of n points in C∗ moving with total
winding number (about z = 0) equal to zero (see Figure 8).
Theorem 5.2 The braid group acts on H 1(X)q as a reduced complex re-
ﬂection group of type An−1(q) with generators si =~τ ∗
i .
Proof. The inner product on H 1(X)q given in Theorem 4.1 satisﬁes
|⟨ei,e i+1⟩|
|⟨ei,e i⟩| = |1 −q|
2| Imq| = 1
|1 +q| = 1
2 secθ
2,
23
so it is proportional to the inner product for An−1(q) up to phase factor;
but this phase factor determines an equivalent representat ion, since An−1 is
a tree.
Corollary 5.3 The action of Bn on H 1(X)q is irreducible.
The lifted representation. If we declare that the vectors (ei)n
1 are linearly
independent, the formulas in Theorem 4.1 give a lifting of ~τ ∗
i to a matrix
Ti ∈ GLn(C) for i = 1,...,n . It is given explicitly by
T2 =




1 0 0
1 −q q
0 0 1



 ⊕In−3
and Ti = P i−2T2P 2−i, where P is a cyclic permutation of the coordinates
(e1,...,e n). The cyclically ordered braid relations are still satisﬁe d, so we
obtain a lifted representation
~ρq : ~Bn → GLn(C);
and the same inner product considerations show:
Theorem 5.4 The lifted representation ~ρq gives a complex reﬂection group
of type ~An(q), with phase shift φ(si,s i+1) = √
−1(1 −q)/|1 −q|.
Note however that ~ρq does not in general factor through Bn, because the
relation (τ1 · · ·τn−1)τn = τ1(τ1 · · ·τn−1) does not lift to a relation between
the matrices Ti.
The Burau representation. The classical Burau representation~β :Bn →
GLn(Z[t,t −1]) is given by
~β(τi) = Ii−1 ⊕
(
1 −t t
1 0
)
⊕In−i−1.
These matrices preserve the vector (1 , 1, 1,..., 1); taking the quotient yields
the reduced Burau representation β.
Theorem 5.5 Forqn ⁄= 1, the representation ρq :Bn → U(H 1(X)q) is dual
to the reduced Burau representation specialized to t =q.
24
(When qn = 1, the reduced Burau representation has an extra trivial su m-
mand of dimension one.)
Proof. Lett =q. Then ~β(τ1) is a q-reﬂection through v1 = (1, −q, 0,..., 0),
and similarly for ~β(τi). When qn ⁄= 1 the vectors ( v1,...,v n−1) are linearly
independent modulo (1 , 1, 1,..., 1), so the reduced Burau representation,
like ρq, gives a complex reﬂection group of type An−1(q). Note, however,
that ρq(τi) = ( ~τ ∗
i )−1, because the braid group is acting on cohomology
(see equation (2.3)). Thus ρq(τi) is actually a
q-reﬂection, and hence the
representationsρq and β are dual.
One can also see this duality by noting that the reduced Burau represen-
tation gives the action of Mod c(C,B ) on the ﬁrst homology of the associated
inﬁnite cyclic covering of C −B.
Examples: n = 3. For n = 3 and p > 6, the image of An−1(−ζp)
in PU(1, 1) is simply the (2 , 3,p )-triangle group acting on the hyperbolic
plane. It has the presentation
Γ(2, 3,p ) = {a,b : a2 =b3 = (a−1b)p =e},
wherea is the image of τ1τ2τ1 andb is the image of τ1τ2. (Note that a2 =b3
is the image of the central element ( τ1τ2)3 ∈ B3, so it is trivial by irre-
ducibility.) This group arises as ρq(B3) when q =ζ −k
d andk/d = 1/2 ± 1/p.
Forp = 3, 4, 5, we obtain the Platonic symmetry groups A4, S4 and A5 in
PU(2); while for p = 6, the reduction of An−1(−ζp) lies in PU(1), so it is
trivial.
Question 5.6 For what values of n and q is the An(q) reﬂection group a
lattice in U(r,s )?
This question is open even for An(ζ3) with n ≥ 7. For related questions,
see §11.
Notes. A Hermitian form preserved by the Burau representation is gi ven in
[Sq]; see also [Pe] and [KT, Ch.3]. It is known that the Burau r epresentation
is unfaithful for n ≥ 5 [Bg1].
The reﬂection groups An(q) are particular representations of the Hecke
algebras Hn(q). For more on complex reﬂection groups, Coxeter diagrams
and braids, see e.g. [Sh], [Cox], [Mos1], [Mos2], [Al1], [J] and [BMR].
25
