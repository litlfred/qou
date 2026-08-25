---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-022-2-z-ref
section_title: "Z ref"
section_number: 2
pages: 23-26
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
SU (N )(S3,T 2,2p+1
Λ r ;q1,q 2) in terms ofa,q, andt. For ex-
ample, from this identiﬁcation one easily ﬁnds the unreduced superpolynomial P
Sr
( ;a,q,t )
of the unknot, cf. (3.34):
P
Sr
( ;a,q,t ) =
Z ref
SU (N )(S3, Λ r;q1,q 2)
Z ref
SU (N )(S3;q1,q 2) =MΛ r(q̺
2;q1,q 2)
= (−1)rAr/2qr/2
2
(A−1;q2)r
(q2;q2)r
= (−1)
r
2a− r
2q
r
2t− 3r
2
(−at3;q)r
(q;q)r
. (3.59)
Similarly, the reduced colored superpolynomial of a more ge neral (2, 2p + 1) torus knot is
related to the partition function Z ref
SU (N )(S3,T 2,2p+1
Λ r ;q1,q 2) via a reﬁned analogue of (3.3),
P Sr
(T 2,2p+1;a,q,t ) =
(q1
q2
) pr
2 Z ref
SU (N )(S3,T 2,2p+1
Λ r ;q1,q 2)
Z ref
SU (N )(S3, Λ r;q1,q 2) , (3.60)
with the same identiﬁcation of the parameters (3.58). Note h ow the role of R = Sr and
R = Λr is exchanged in this relation, in line with the above discussion. Explicitly, from (3.50)
– 22 –
we ﬁnd
P Sr
(T 2,2p+1;a,q,t ) =
r∑
ℓ=0
(qt2;q)ℓ(−at3;q)r+ℓ(−aq−1t;q)r−ℓ(q;q)r
(q;q)ℓ(q2t2;q)r+ℓ(q;q)r−ℓ(−at3;q)r
(1 −q2ℓ+1t2)
(1 −qt2)
×(−1)ra− r
2q
3r
2 −ℓt−rp−ℓ+ r
2
[
(−1)ℓa
r
2q
r2−ℓ(ℓ+1)
2 t
3r
2 −ℓ
] 2p+1
.(3.61)
This is one of the main results, with these choices of convent ions, that we will use for testing
the reﬁned / categoriﬁed volume conjectures (2.1) and (2.6) .
For completeness, and to illustrate how it is done in general , we also write down the
colored superpolynomial of (2, 2p + 1) torus knots obtained from (3.49). In the same grading
conventions as in the relation (3.60), the role of symmetricand anti-symmetric representations
is reversed and we obtain the Λ r-colored superpolynomial:
P Λ r
(T 2,2p+1;a,q,t ) =
(q2
q1
) pr
2 Z ref
SU (N )(S3,T 2,2p+1
Sr ;q1,q 2)
Z ref
SU (N )(S3, Sr;q1,q 2) , (3.62)
where the parameter identiﬁcation is essentially the same a s in (3.58) with q1 and q2 inter-
changed:
a = A
√ q2
q1
,
q = 1
q1
, (3.63)
t = −
√ q1
q2
.
The exchange q1 ↔ q2 that accompanies R ↔ Rt is familiar in the context of reﬁned BPS
invariants as well as in the equivariant instanton counting which, of course, are not unre-
lated. Hence, from the partition function Z ref
SU (N )(S3, Sr;q1,q 2), we ﬁnd the unreduced
superpolynomial P
Λ r
( ;a,q,t ) of the unknot:
P
Λ r
( ;a,q,t ) =
Z ref
SU (N )(S3, Sr;q1,q 2)
Z ref
SU (N )(S3;q1,q 2) =MSr(q̺
2;q1,q 2)
= A− r
2q
r
2
2
(A;q1)r
(q2;q1)r
= (−1)− r
2a
r
2q
r
2t
3r
2
(−a−1t−1;q)r
(qt2;q)r
, (3.64)
and the reduced colored superpolynomial of the (2 , 2p + 1) torus knot:
P Λ r
(T 2,2p+1;a,q,t ) =
r∑
ℓ=0
(qt2;q)ℓ(q;q)r(−a−1t−1;q)r+ℓ(−a−1q−1t−3;q)r−ℓ(qt2;q)r
(q;q)ℓ(qt2;q)r(q2t2;q)r+ℓ(q;q)r−ℓ(−a−1t−1;q)r
×(1 −q2ℓ+1t2)
(1 −qt2) a
r
2q
3r
2 −ℓt3r−ℓ
[
(−1)ℓa
r
2q
ℓ(ℓ+1)−r2
2 tℓ
] 2p+1
. (3.65)
– 23 –
These results agrees with the earlier calculations of the co lored superpolynomials in [44, 45]
for small values of p and r, and provide a generalization to arbitrary p and r.
Finally, we complete this part by writing the same formulas f or the colored superpolyno-
mials (3.59)–(3.65) in a diﬀerent set of grading conventions that we dub “DGR,” cf. (3.54).
As we pointed out earlier, a simple way to implement this chan ge of conventions, based on
the “mirror symmetry” (3.55), is to changeR ↦→Rt on one side of the relations (3.59), (3.60),
etc. As a result, we obtain a nice relation between the R-colored superpolynomial of T 2,2p+1
and the reﬁned partition function of a line operator colored by the same representation R
(not Rt as e.g. in (3.60)):
P R
DGR(T 2,2p+1;a,q,t ) =
(q2
q1
) pr
2 Z ref
SU (N )(S3,T 2,2p+1
R ;q1,q 2)
ZSU (N )(S3, R;q1,q 2) , (3.66)
where R =Sr or Λr. Using (3.49)–(3.50) and the identiﬁcation of variables [3 5]:
a2 = A
√ q2
q1
,
q = √q2, (3.67)
t = −
√ q1
q2
.
we ﬁnd explicit expressions for P R
DGR(T 2,2p+1) with R =Sr and R = Λr:
P Sr
DGR(T 2,2p+1;a,q,t ) =
r∑
ℓ=0
(q2;q2t2)ℓ(q2t2;q2t2)r(−a2t;q2t2)r+ℓ(−a2q−2t;q2t2)r−ℓ
(q2t2;q2t2)ℓ(−a2t;q2t2)r(q4t2;q2t2)r+ℓ(q2t2;q2t2)r−ℓ
× (1 −q4ℓ+2t4ℓ)
(1 −q2) a−rq3r−2ℓtr−ℓ
[
(−1)r−ℓarqr2−ℓ(ℓ+1)tr2−ℓ2
] 2p+1
(3.68)
P Λ r
DGR(T 2,2p+1;a,q,t ) =
r∑
ℓ=0
(q2t2;q2)ℓ(−a−2t−1;q2)r+ℓ(−a−2q−2t−3;q2)r−ℓ(q2;q2)r
(q2;q2)ℓ(q4t2;q2)r+ℓ(q2;q2)r−ℓ(−a−2t−1;q2)r
× (1 −q4ℓ+2t2)
(1 −q2t2) arq3r−2ℓt3r−ℓ
[
(−1)ℓarq−r2+ℓ(ℓ+1)tℓ
] 2p+1
(3.69)
as well as the unreduced superpolynomials of the unknot P
Sr
DGR( ):
P
Sr
DGR( ;a,q,t ) =
Z ref
SU (N )(S3, Sr;q1,q 2)
Z ref
SU (N )(S3;q1,q 2) = (−1)
r
2a−rqrt− r
2
(−a2t;q2t2)r
(q2;q2t2)r
. (3.70)
P
Λ r
DGR( ;a,q,t ) =
Z ref
SU (N )(S3, Λ r;q1,q 2)
Z ref
SU (N )(S3;q1,q 2) = (−1)
r
2arqrt
r
2
(−a−2t−1;q2)r
(q2;q2)r
. (3.71)
– 24 –
