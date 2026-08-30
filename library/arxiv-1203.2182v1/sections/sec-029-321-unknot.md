---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-029-321-unknot
section_title: "Unknot"
section_number: 3.2.1
pages: 32-34
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
such reﬁned relations exist and can be explicitly written do wn is already nontrivial. Having
found these examples, we have no doubt that their generalization to the entire family of torus
knots, and even more general knots, exists. Moreover, an imp ortant hint about the general
structure of reﬁned quantum curves for (2 , 2p + 1) torus knots is given in the next section,
where the analysis of the asymptotics of their colored super polynomials reveals the form of
the reﬁned classical curves Aref(x,y ;t) = 0. To ﬁnd the full quantum curves in this class of
examples, one should “just” reintroduce the dependence on q.
We will derive reﬁned quantum curves from the analysis of thehomological knot invariants
found in section 3. It would also be interesting to ﬁnd genera l methods of deriving reﬁned
recursion relations, similar to [7, 19] in the unreﬁned case , which a priori do not rely on the
knowledge of homological invariants. We plan to address thi s problem in the follow-up work.
3.2.1 Unknot
As we already mentioned in (3.34) and (3.59), in every approa ch to knot homologies based
on the reﬁned BPS invariants [35, 26] the colored superpolyn omial of the unknot is given
essentially by the Macdonald polynomial [36]. In particula r, after the change of variables
(3.58), the Sr-colored superpolynomial reads:
P
Sr
( ;a,q,t ) = ( −1)
r
2a− r
2q
r
2t− 3r
2
(−at3;q)r
(q;q)r
. (3.98)
Note that when we talk about the unknot, only the unreduced su perpolynomial (resp. ho-
mology) is non-trivial; the reduced one is trivial by deﬁnit ion (which involves normalizing by
the unknot). Specializing further to a =q2 we ﬁnd
Pn=r+1( ;q,t ) = ( −1)
r
2q− r
2t− 3r
2
(−q2t3;q)r
(q;q)r
. (3.99)
Note, at t = −1 this expression reduces to the n-colored Jones polynomial of the unknot
Jn( ;q) = q
n
2 −q− n
2
q
1
2 −q− 1
2
(3.100)
– 31 –
which can be written as the partition function of the SU (2) Chern-Simons theory on a solid
torus S1 × D2 ∼
= S3 \ unknot,
Z CS
SU (2)(S1 × D2;q) =
√
−ℏ
2πi
(
x −x−1)
(3.101)
normalized by the partition function of the Chern-Simons th eory on S3,
Z CS
SU (2)(S3;q) =
√
−ℏ
2πi
(
eℏ −e−ℏ
)
(3.102)
where we used x =eu and u =nℏ, cf. (3.18).
As the homological knot invariant (3.99) has a product struc ture, we can immediately
write down the recursion relation it satisﬁes
Pn+1( ;q,t ) = 1 +t3qn+1
1 −qn (−q−1t−3)1/2Pn( ;q,t ). (3.103)
This means that Pn( ;q,t ) obeys the reﬁned version (2.1a) of the quantum volume conje c-
ture with
ˆAref (ˆx,ˆy;q,t ) = (1 + t3qˆx)(−q−1t−3)1/2 − (1 −ˆx)ˆy. (3.104)
In the classical limit q → 1 this recursion relation reduces to the reﬁned classical cu rve
Aref(x,y ;t) = 0 deﬁned by
Aref (x,y ;q = 1,t ) = (1 + t3x)(−t−3)1/2 − (1 −x)y. (3.105)
On the other hand, in the unreﬁned limit t = −1 the relation (3.104) takes the form
ˆAref (ˆx,ˆy;q) = q−1/2(1 −qˆx) − (1 −ˆx)ˆy, (3.106)
and specializing further to q = 1 we get the classical A-polynomial
A (x,y ) = (1 −x)(1 −y). (3.107)
It is also interesting to consider the second order equation satisﬁed by (3.99). Writing
the three consecutive colored polynomials it is not hard to s ee that the following equation is
satisﬁed
Pn+1 − (−qt3)1/2 1 −qt3 + 2xt3 −x2t3 + 2qxt3 +qx2t6
q(x − 1)t3(1 +xt3) Pn +Pn−1 = 0, (3.108)
with x = qn. Interestingly, in the unreﬁned limit t = −1 the dependence on x cancels and
Jn( ;q) satisﬁes the recursion relation
Jn+1 − [2]qJn +Jn−1 = 0 (3.109)
– 32 –
with [2] q = q1/2 +q−1/2. This means that in the quantum volume conjecture (1.5) for t he
unknot we have
ˆA (ˆx,ˆy;q) = ˆy − (q1/2 +q−1/2) +ˆy−1. (3.110)
In the classical limit q → 1 this becomes equivalent to
A (x,y ) = ( y − 1)2. (3.111)
On the other hand, we can also write the classical limit of (3. 108) in the polynomial form as
Aref (x,y ;t) = (1 −x)(1 +t3x)y2 − (−t−3)1/2(
1 +t6x2 −t3(1 − 4x +x2)
)
y + (1 −x)(1 +t3x).
(3.112)
Starting from this form the unreﬁned limit readsA (x,y ) = (x−1)2(y −1)2, which captures
the cases (3.107) and (3.111) which we considered above.
