---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-063-45-proof-of-the-main-theorem-87
section_title: "Proof of the main theorem 87"
section_number: 4.5
pages: 95-96
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
whereW is some irreducible representation of the groupH. Then via the
commutative diagram
˜H
∃ //

˜G //

Gl(V1)×Gl(V2)

H   // G   // Gl(V) Gl(V1⊗V2)
we can consider the restrictions ofV1 andV2 to the covering group˜H, and
by construction we have
V1| ˜H⊗V2| ˜H = V| ˜H = W| ˜H⊕
{
1⊕1 if g is even,
1 if g is odd,
whereW| ˜H is irreducible by the general remarks from the beginning of the
proof. This implies that bothVi| ˜H are irreducible because otherwise more
than one non-trivial direct summand would occur. But then, since
Hom˜H(1, V1| ˜H⊗V2| ˜H)⁄= 0,
adjunction showsV1| ˜H is isomorphic to the dual ofV2| ˜H. In particular V1
andV2 have the same dimension. This is impossible since dim(V) = g! is
not the square of a natural number forg > 1.
For g = 4 we can alternatively argue as follows, using only part (3) of
proposition 4.12. Here bothV1 and V2 have dimension at most 12 since
their dimensions must be non-trivial divisors of dim(V) =24. So if instead
of our previous choice we now take the subgroupH ↪→ G to be isogenous
to Sl2g−2(C) =Sl6(C) with the property in part (3) of the proposition, then
by the classiﬁcation of small representations in [3] each Vi| ˜H can contain
only trivial representations and 6-dimensional standard representations as
irreducible constituents. In particular, looking atV1| ˜H⊗V2| ˜H one sees that
the third fundamental representation ofSl6(C) cannot occur as a constituent
ofV|H, and this contradicts our choice of the subgroupH. □
Now recall that the Tannaka groupG = G(δΘ) of a general ppav is in
any case a subgroup of the symplectic or special orthogonal groupG(g),
hence to prove theorem 4.2 it will be enough to show that the connected
componentG0 must be the full groupG(g). Note that by lemma 4.13 this
connected component is an irreducible subgroup ofG(g) in the sense that
for the standard representationV∈ RepC(G(g)), the restrictionV|G0 is still
irreducible. So we are in the situation of the following general lemma.
88 Chapter 4 – The Tannaka group of the theta divisor
LEMMA 4.15. Let H be an irreducible connected subgroup of G(g)
which is simple modulo its center. Then
dim(H)≤ g! or H = G(g).
Proof. Let V denote the standard representation of the symplectic or
special orthogonal groupG(g), and suppose dim(H) > g! = dim(V). Then
by irreducibility the restriction ofV to H must be one of the representations
in table 1 of [3]. Since dim(V) is the factorial of a natural number, one of
the following cases must occur for somer∈ N.
(a) The groupH is of typeAr, Cr or Dr and acts onV via its standard
representation.
(b) The groupH is of typeAr and acts onV via the symmetric or via
the alternating square of its standard representation.
Case (a) can only occur forH = G(g) since G(g) is itself the symplectic
or special orthogonal group withV as its standard representation. To deal
with case(b), note that by the criterion in [46, th. 3.2.14] the symmetric
square of the standard representation ofAr is self-dual only ifr = 1, but
then it has dimension 3⁄= dim(V). In the same vein, the alternating square
of the standard representation ofAr is self-dual of dimensiong! only in the
case(r,g) = (3,3) whereH = G(g) =SO6(C) for dimension reasons.□
To complete the proof of theorem 4.2, all that remains to be done is to
show that on a general ppavX we have
dim(G) > g!
for the groupG = G(δΘ) attached to the theta divisor. But this follows by
induction on the dimensiong = dim(X). Indeed, we already know that the
theorem holds forg≤ 3, so we can assumeg≥ 4. To start the induction,
for g = 4 we can use the subgroup in part (3) of proposition 4.12 since in
that case dim(Sl2g−2(C)) =35 > g! = 24. This being settled, the induction
step from dimensiong−1 to dimensiong is provided by part (1) of the
proposition because dim(G(g−1)) >g! forg≥5. This ﬁnishes the proof of
the theorem. Going through the above arguments, one furthermore checks
that forg =4 all we need is part (3) of proposition 4.12. Hence theorem 4.3
follows with the same proof.
