---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a ﬁnite set of points(: GalMot ⟳cMot 1 (-−(,E 0)"
section_id: sec-017-applications
section_title: "Applications"
section_number: null
pages: 79-82
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a finite set of points(: GalMot ⟳cMot 1 (-−(,E 0). (1) — On the"
---
Additive shuﬄe relation
Specializing allF8 to 1 in the second shuﬄe relation, where all=8 = 0, we extract anadditivesecond shuﬄe
relation, which does not have lower-depth terms:
Corollary 2.25.Let<,=> 0. The additive shuﬄe
Õ
f∈Σ<,=
CorH(Yf−1(1),Y f−1(1)+Yf−1(2),...,Y f−1(1)+···+ Yf−1(<+=), 0).
is a constant independent of(Y1,...,Y =)∈ C=\ 0.
71
Proof. This is a specialization of the second shuﬄe relation withF8 = 1+CY8 asC→ 0. The terms are the
specializations of those in the second shuﬄe relation arising from proper shuﬄes. The specializations of the
lower-depth terms are independent of theY8, as not all arguments of the correlators are equal atC= 0. □
Itiseasytoseethatthisconstantis0if <+=iseven. If<+=isodd,itisequal, inparticular,toasumof
Hodge correlators at roots of unity.
Proofs of Corollaries 2.2 and 2.3
Recall Corollary 2.2:
Corollary([GR], Proposition 2.8). For=> 2, every Hodge correlator of weight= is a linear combination of
Hodge correlators of weight= and depth at most=− 2. Explicitly, forI1,...,I =∈ C∗, we have
CorH(I1,...,I =, 0)=
=Õ
8=1
CorH
(
I1,...,I 8−1,I8,I8
I1
I=
,...,I =−1
I1
I=
,I=
I1
I=
)
−
=Õ
8=2
CorH
(
I1,...,I 8−1, 0,I8
I1
I=
,...,I =−1
I1
I=
,I=
I1
I=
)
−CorH
(
I1,I 1· I1
I=
, 0,..., 0
)
. (2.111)
Proof. By multiplicative invariance, we may assumeI1 = 1. Then this is precisely the(=− 1, 1)-second
shuﬄe relation applied to the segments
(I2/I1| 0),(I3/I2| 0),..., (I=/I=−1| 0)
and
(I1/I=| 0),
where the segment(1| 0) is left ﬁxed. Indeed, the two summations come from the= shuﬄes and the=− 1
additional quasishuﬄes, with the remaining terms giving the left side and the last summand.
All terms on the right side have at least two coinciding arguments. After an additive shift, they have at
least two arguments equal to 0, so they are equal to those of depth at most=− 2. □
Recall Corollary 2.3:
72
Corollary. The Hodge correlators in weight 3 satisfy the relations:
CorH(1, 0, 0,G)+ CorH(1, 0, 0, 1−G)+ CorH(1, 0, 0, 1−G−1)= CorH(1, 0, 0, 1), (2.112)
CorH(0,G, 1,H)=−CorH(1, 0, 0, 1−G−1)− CorH(1, 0, 0, 1−H−1)− CorH
(
1, 0, 0, H
G
)
−CorH
(
1, 0, 0, 1−H
1−G
)
+CorH
(
1, 0, 0, 1−H−1
1−G−1
)
+CorH(1, 0, 0, 1). (2.113)
Proof. Apply the(1, 1)-second shuﬄe relation to the segments(G| 0) and (G−1| 1), keeping the segment
(1| 1) ﬁxed:
CorH(1,G, 0, 0)+ CorH(1, 0,G−1, 1)− CorH(1, 0, 0, 1)
−CorH(1,G, 0, 0)− CorH(1, 0,G−1, 0) = 0.
Multiplicative invariance and the ﬁrst shuﬄe relation imply
−CorH(1,G, 0, 0)− CorH(1, 0,G−1, 0)= Cor(1, 0, 0,G).
Rearranging terms and applying additive invariance gives (2.112).
Nowapply(2.111)toCor H(G, 1,H, 0) andapplythedihedralsymmetryandadditiveinvariancetochange
all terms to the form CorH(1, 0, 0,I):
CorH(0,G, 1,H)= CorH
(
1, 0, 0, 1−H
G−H
)
+CorH
(
1, 0, 0, 1−G−1
1−H−1
)
+CorH
(
1, 0, 0,G− 1
G−H
)
−CorH
(
1, 0, 0, 1−H−1
)
−CorH
(
1, 0, 0,G−1
)
−CorH
(
1, 0, 0,G
H
)
.
Finally, by (2.112),
CorH
(
1, 0, 0, 1−H
G−H
)
+CorH
(
1, 0, 0,G− 1
G−H
)
= CorH(1, 0, 0, 1)−CorH
(
1, 0, 0, 1−G
1−H
)
,
which gives the result. □
73
Chapter 3
Motivicc1 of CM elliptic curves and
geometry of Bianchi hyperbolic
threefolds
The results of this chapter have appeared in [M1].
