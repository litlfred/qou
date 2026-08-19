---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K-THEORY"
section_id: sec-013-42-the-bloch-group-of-fq
section_title: "The Bloch group of Fq"
section_number: 4.2
pages: 23-25
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "BLOCH GROUPS, ALGEBRAICK-THEORY — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F (e2πi/n), well-deﬁned up to n-th"
---
class map to the Bloch group. Let p> 2 and q >2 be odd primes such that q≡− 1 modn,
where n = pm. For a ﬁnite ﬁeld Fq, the group F×
q is cyclic, so ⋀2 F×
q is a 2-torsion group.
Hence the Bloch group B(Fq) coincides with the pre-Bloch group after tensoring with Fp,
where the pre-Bloch group is deﬁned as the quotient of the free abelian group on P1(Fq) by
the 5-term relation (3). By [15], the Bloch group B(Fq) is a cyclic group of order q + 1 up
to 2-torsion. Moreover, following [15], one may relate B(Fq) to the cohomology of SL 2(Fq)
in degree three, as we now discuss.
There is an isomorphism
H3(SL2(Fq), Z)⊗ Z/nZ ≃ Z/nZ.
Let us describe this isomorphism more carefully. By a computation of Quillen, we know that
H3(SL2(Fq), Z) is cyclic of order q2− 1. It follows that the p-part of this group comes from
the p-Sylow subgroup. If one chooses an isomorphism
Fq2≃ (Fq)2
of abelian groups, one gets a well deﬁned map:
F×
q2 = C = Aut Fq(Fq2)→ GL2(Fq)
which is well deﬁned up to conjugation. There is, correspondingly, a map C1→ SL2(Fq),
where
C1 = Ker
(
N : F×
q2→ F×
q
)
.
We refer to bothC andC1 as the non-split Cartan subgroup. By Quillen’s computation, we
deduce that there is a canonical map:
C1 = H3(C1, Z)→H3(SL2(Fq), Z)
24 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
which is an isomorphism after tensoring with Z/nZ. There is a canonical isomorphism
C1[n] = µ, where µ denotes the nth roots of unity. Hence to give an element of order p
in H3(SL2(Fq), Z) up to conjugation is equivalent to giving a primitive nth root of unity
ζ∈C1⊂C = F×
q2. From [15], there is a canonical map:
H3(SL2(Fq), Z)→B(Fq),
at least away from 2-power torsion, which is an isomorphism after tensoring with Z/nZ.
Given a root of unityζ, lett denote the corresponding element of SL2(Fq). The corresponding
element of B(Fq) is given (see [15]) by:
∑
k modn
[t(∞)−tk+1(∞)
t(∞)−tk+2(∞)
]
.
This construction yields the same element forζ andζ−1. We may representt by its conjugacy
class in GL 2(Fq), which has determinant one and trace ζ +ζ−1∈ Fq. The choice of ζ up to
(multiplicative) sign is given by this trace. Note that the congruence condition on q ensures
that the Chebyshev polynomial with roots ζ +ζ−1 has distinct roots which split completely
over Fq. Explicitly, we may choose
t =
(
0 1
−1 ζ +ζ−1
)
=A
(
ζ−1 0
0 ζ
)
A−1, A =
(
ζ ζ−1
1 1
)
.
Let Fk be the Chebyshev polynomials, so Fk(2 cosφ) = sinkφ
sinφ . Then
tk(∞) = Fk−1(ζ +ζ−1)
Fk(ζ +ζ−1) ,
and an elementary computation then shows that the corresponding element in B(Fq)⊗ Zp
is given by
∑
k modn
[
1− 1
Fk(ζ +ζ−1)2
]
=
∑
k modn
[
1−
( ζ−ζ−1
ζk−ζ−k
)2]
, (33)
4.3. The local Chern class map cζ. In this section, q will denote a prime with q ≡
−1 mod pm which splits completely in F . Let q be a prime above q. There is a natural
map B(F )→ B(OF/q) = B(Fq). The reduction map sends [ x] to [x] under the natural
reduction map P1(F )→ P1(Fq).
Lemma 4.4. Let p> 2. There is a commutative diagram as follows:
B(F )/nB(F ) -
⨁
B(Fq)⊗ Z/nZ
K3(F )/nK3(F )
wwwwwwwww
-
⨁
K3(Fq)⊗ Z/nZ
≃
= = = = = =
⨁cζ,q ⨁
F×
q2/F×n
q2 ,
where the product runs over all primes q of normq≡− 1 modn which split completely inF ,
or alternatively all but ﬁnitely many such primes.
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 25
Proof. The isomorphism of the left vertical map is a theorem of Suslin [30, Theorem 5.2]
(taking into account Lemma 2.2), and the isomorphism of the right vertical map follows
from [15]. The fact that the diagram commutes is a consequence of the fact that both
constructions are compatible (and can be seen in group cohomology). □
Recall that an elementx of an abelian groupG isp-saturated ifx⁄∈ [p]G, where [p] :G→G
is the multiplication by p map.
Corollary 4.5. There is an algorithm to prove that a set of generators ofB(F ) isp-saturated
for p> 2.
Proof. ComputingB(Fq) is clearly algorithmically possible. Moreover, we can a priori com-
pute B(F )⊗ Zp as an abstract Zp-module. Hence it suﬃces to ﬁnd suﬃciently many
distinct primes q such that the image of a given set of generators has the same order
as B(F )/nB(F ). □
In light of the commutative diagram of Lemma 4.4, we also use cζ to denote the Chern
class map on B(F )/nB(F ).
4.4. The local Rζ map. Suppose that q≡− 1 modp. It follows that the ﬁeld Fq does not
contain ζp, and so Proposition 2.5 applies to give maps Pζ and Rζ which are well deﬁned
over this ﬁeld. In particular, since ( p,q− 1) = 1, all elements of Fq are p-th powers, and
hence the Kummer extension H is given by H =Fn and Rζ and Pζ coincide.
5. Comparison between the maps cζ and Rζ
The main goal of this section, carried out in the ﬁrst subsection, is to prove Theorem 1.6.
The main result here is Theorem 5.2, which says that that our modn local regulator mapRζ,q
gives an isomorphism from B(Fq)⊗ Z/nZ to F×
q2⊗ Z/nZ for any prime power n and prime
q≡− 1 (mod n). This implies in particular the existence of a curious “mod- p-q dilogarithm
map” from Fq to Z/nZ, and in Section 5.2, we digress brieﬂy to give an explicit formula
for this map. In the ﬁnal subsection, we describe the expected properties of the Chern class
map that would imply the conjectural equality (13) and hence, in conjunction with (12), the
evaluationγ = 2 of the comparison constant γ occurring in Theorem 1.6.
