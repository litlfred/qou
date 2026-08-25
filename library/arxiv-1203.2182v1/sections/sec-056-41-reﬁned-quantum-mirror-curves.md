---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-056-41-reﬁned-quantum-mirror-curves
section_title: "Reﬁned quantum mirror curves"
section_number: 4.1
pages: 58-60
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
In this section we derive the reﬁned quantum curves relevant in the context of the open BPS
state counting (or topological string theory). They can be r egarded as reﬁned and quantum
versions of mirror curves A(x,y ) = 0 which appear in the mirror geometry (4.1) for toric
three-folds. Speciﬁcally, we consider open reﬁned topolog ical string amplitudes for branes
along preferred directions, in general framing, for C3 and conifold geometries. It brings only
some technical, but no conceptual challenges to generalize the computations below to the case
of “generalized conifolds” ( i.e. toric three-folds without compact 4-cycles). To ﬁnd quantu m
curves in the present context, in this section we derive the r eﬁned open topological string
amplitudes Z open
BPS and ﬁnd diﬀerence equations which they satisfy. Then, in the n ext section
we consider the classical limit q2 → 1 of the quantum curve, show that it is equivalent to the
saddle point analysis of Z open
BPS , and describe properties of the resulting reﬁned mirror cur ves.
C3 or tetrahedron
To start with, we consider the simplest toric geometry of C3, in arbitrary framing f. Its ordi-
nary mirror curve – which is equivalent to the “single tetrahedron” curve from the perspective
of hyperbolic geometry and knot theory – takes the form [19]:
Aref(x,y ;q1 = 1) = 1 −y +x(−y)f = 0. (4.8)
To ﬁnd the reﬁned and quantum generalization of this curve we consider the reﬁned BPS
partition function in C3 geometry with a D-brane located along the preferred directi on. In
arbitrary framing such an amplitude reads
Z open
BPS =
∑
R
fR(q1,q 2)−fC••R(q−1
1 ,q −1
2 )sR(x). (4.9)
Performing the summation we get
Z open
BPS =
∞∑
k=0
(−1)(f +1)kq
f
2 k(k−1)
2
(
x q1√q2
) k k∏
i=1
1
1 −q1qi−1
2
. (4.10)
Forf = 0 this result reduces, as it should, to the brane amplitude i n C3 in phase III found
in [76] (after identifying x = −Q). If we write now
Z open
BPS =
∞∑
k=0
ak,
we can easily determine the ratio of the consecutive coeﬃcie nts, ak+1
ak
, so that
(1 −q1qk
2)ak+1 = −x(−1)fqf k q1√q2
ak. (4.11)
– 57 –
Performing the summation over k on both sides of this equation we ﬁnd that the open string
amplitude satisﬁes the following inhomogeneous diﬀerence e quation
(
1 −q1
q2
ˆy + q1√q2
ˆx(−ˆy)f
)
Z open
BPS = 1 − q1
q2
. (4.12)
This is the reﬁned and quantum version of the ordinary mirror curve (4.8). Because the
inhomogeneous term is independent of x, acting on it by ˆy leaves it invariant. Therefore, if
we multiply both sides of the above equation by (1 −ˆy), the inhomogeneity on the right hand
side vanishes, while the degree inˆy of the left hand side increases. Commuting all ˆy operators
to the right we obtain the following homogeneous equation of a higher degree
(
1 −
(
1 +q1
q2
)
ˆy + q1
q2
ˆy2 + q1√q2
ˆx(−ˆy)f +q1
√q2ˆx(−ˆy)f +1
)
Z open
BPS = 0 . (4.13)
We note the similarity of the factor (1 −ˆy), which brings the equation to the homogeneous
form, to the factor representing abelian ﬂat connection in SL(2, C) Chern-Simons theory.
Conifold
We now repeat the above calculation for the conifold, whose o rdinary mirror curve in general
framing takes the form [19]:
Aref(x,y ;q1 = 1) = 1 −y +x(−y)f +Qx(−y)f +1 = 0 . (4.14)
To ﬁnd the reﬁned and quantum version of this curve, we again c onsider the brane located
along the preferred direction of the conifold. More precise ly, we wish to consider the brane
amplitude normalized by the closed string partition functi on. Such an amplitude can be
written as
Z open
BPS =
∞∑
k=0
ak =
∑
R=(k)
sR(x)fR(q1,q 2)−fbR
b•
, (4.15)
where
bR =
∑
P
(−Q)|P |CP •R(q−1
1 ,q −1
2 )CP t••(q−1
2 ,q −1
1 )
=
(q1
q2
) ||R||2/2
PRt(qρ
1;q−1
2 ,q −1
1 )
∞∏
i,j=1
(1 −Qq−i+1/2
1 q−j+1/2+Ri
2 ) (4.16)
andQ denotes the K¨ ahler parameter of the conifold. The normalization factor in this case is
nothing but
Z closed
BPS =b• =
∑
P
(−Q)|P |CP ••(q−1
1 ,q −1
2 )CP t••(q−1
2 ,q −1
1 )
=
∞∏
i,j=1
(1 −Qq−i+1/2
1 q−j+1/2
2 ), (4.17)
– 58 –
and it follows that for representation R = (k), cf. (4.3):
b(k)
b•
=C••(k)(q−1
1 ,q −1
2 )
k∏
j=1
(
1 −Qq−1/2
1 q−j+k+1/2
2
)
=
(
− q1
√q2
) k k∏
i=1
1 −Qq−1/2
1 qi−1/2
2
1 −q1qi−1
2
.
Collecting the above ingredients, we ﬁnd the following stru cture of the open BPS state par-
tition function
Z open
BPS =
∞∑
k=0
ak =
∞∑
k=0
(−1)(f +1)kq
f
2 k(k−1)
2
(
x q1√q2
) k k∏
i=1
1 −Qq−1/2
1 qi−1/2
2
1 −q1qi−1
2
. (4.18)
We also ﬁnd that the consecutive terms ak are related as
(1 −q1qk
2)ak+1 = ( −1)f +1qf k q1√q2
x(1 −Qq−1/2
1 qk+1/2
2 )ak. (4.19)
Summing both sides over k gives rise to the inhomogeneous equation
(
1 − q1
q2
ˆy + q1
√q2
ˆx(−ˆy)f +Qq1/2
1 ˆx(−ˆy)f +1
)
Z open
BPS = 1 − q1
q2
. (4.20)
This is the reﬁned and quantum version of the conifold mirror curve (4.14). We can also
bring this equation to the homogeneous form at the expense of increasing its degree in ˆy, by
multiplying both sides with (1 −ˆy). Commuting all ˆy operators to the right gives
(
1−
(
1+q1
q2
)
ˆy+q1
q2
ˆy2+ q1
√q2
ˆx(−ˆy)f +
(
Q√q1+q1
√q2
)
ˆx(−ˆy)f +1+Q√q1q2ˆx(−ˆy)f +2
)
Z open
BPS = 0.
(4.21)
