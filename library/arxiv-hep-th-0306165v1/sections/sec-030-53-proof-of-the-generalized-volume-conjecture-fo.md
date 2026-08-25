---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-030-53-proof-of-the-generalized-volume-conjecture-fo
section_title: "Proof of the Generalized Volume Conjecture for the Figu re-Eight Knot 41"
section_number: 5.3
pages: 41-44
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting"
---
The N -colored Jones polynomial of the ﬁgure-eight knot has the fo llowing form, see
e.g. [84]:
JN (41,q ) =
N−1∑
i=0
i∏
j=1
(
q(N+j)/ 2−q−(N+j)/ 2
)(
q(N−j)/ 2−q−(N−j)/ 2
)
(5.14)
Notice, that at the N -th root of unity, q = exp(2πi/N), it is indeed equal to the Kashaev’s
invariant of the ﬁgure-eight knot [34]:
⟨41⟩N =
N−1∑
i=0
i∏
j=1
(
1−qj)(
1−qj)
In the limit (5.11), the asymptotic behavior of the colored J ones polynomial (5.14)
can be obtained using the saddle-point approximation. The r esult has the following form,
cf. [85]:
lim
k,N →∞
logJN (41,e 2πi/k )
k = 1
πV (a) (5 .15)
where the function
V (a) = Λ( aπ +θ(a)/2)− Λ( aπ−θ(a)/2) (5 .16)
is deﬁned via θ(a) = arccos (cos(2πa)− 1/2) and the Lobachevsky function,
Λ( z) =−
∫ z
0
log|2 sinx|dx = 1
2
∞∑
n=1
sin(2nz)
n2 (5.17)
The graph of V (a) is shown on the ﬁgure below:
40
0.8 0.9 1.1 1.2
0.6
0.8
1.2
1.4
1.6
1.8
2
Fig. 9: The graph of the volume function V (a) near a = 1.
Notice, that at the special value a = 1 corresponding to the complete hyperbolic
structure on the knot complement, we have
2π lim
N→∞
logJN (41,e 2πi/N )
N = 2
(
Λ (7 π/6)− Λ (5π/6)
)
(5.18)
Using the π-periodicity of the Lobachevsky function and the identity
Λ( nz) = n
∑
j (mod n)
Λ
(
z + πj
n
)
one can check that (5.18) is indeed equal to the volume of the ﬁ gure-eight knot complement,
Vol(41) = 6Λ( π/3)≈ 2.0298832... (5.19)
Now, let us study the limit (5.15) as a function of the paramet er a, near the point
a = 1. For reasons that will become clear in a moment, it is conve nient to introduce a new
parameter y, such that
a = 1 + y
π (5.20)
According to the relation (5.13), we have
m = exp(iy) (5 .21)
It is clear that y is a good expansion parameter near m = 1 ( i.e. near y = 0).
Since we already know that fory = 0 the volume conjecture is true, we need to compare
only the y-dependent terms on both sides in (5.12), say, by diﬀerentia ting with respect to
41
y. On the left-hand side, this leads to a derivative of the func tion (5.16), representing the
limiting behavior of the colored Jones polynomial. Explici tly, we ﬁnd
dV
dy =
(
1− sin(2y)√
1− (cos(2y)− 1/2)2
)
log|2 sin
(
y− 1
2 arccos (cos(2y)− 1/2)
)
|−
−
(
1 + sin(2y)√
1− (cos(2y)− 1/2)2
)
log|2 sin
(
y + 1
2 arccos (cos(2y)− 1/2)
)
|
(5.22)
It is easy to see that this is an odd function of y, which has the following power series
expansion,
dV
dy =−2
√
3y + 8√
3
y3− 184
15
√
3
y5 + 1424
45
√
3
y7− 86248
945
√
3
y9 +... (5.23)
The graph of the function dV/dy is shown on the ﬁgure below:
-1 -0.5 0.5 1
-1
-0.5
0.5
1
Fig. 10: The graph of the function dV /dy.
Now, let us look at the right-hand side of the proposed relati on (5.12). It involves
the volume function, Vol( l,m ), and the Chern-Simons function, CS (l,m ), deﬁned by the
integrals (5.7) on the zero-locus of the A-polynomial. For t he ﬁgure-eight knot, the A-
polynomial has the following form [46]:
A(l,m ) =−2 +m4 +m−4−m2−m−2−l−l−1 (5.24)
For simplicity, let us take y to be real. Then, using the fact that CS (41) = 0, we can
write the integrals (5.7) in the following simple form,
Vol(m) = Vol(41)− 2
∫ y
0
log|l|d(argm) (5 .25)
42
and
CS (m) =− 1
π2
∫ y
0
(argl)d(argm) (5 .26)
where log|l| and arg l should be determined from the equation A(l,e iy) = 0. Since the
A-polynomial (5.24) is quadratic in l, it is easy to solve this equation. One ﬁnds
l = cos(4y)− cos(2y)− 1±
√
(cos(4y)− cos(2y)− 1)2− 1 (5 .27)
It is the second root (with the “ −” sign) that corresponds to the geometric branch of the
moduli space of ﬂat SL(2,C) connections. Choosing this root, we ﬁnd that l is real for
real values of y (suﬃciently close to y = 1). Hence, the Chern-Simons integral (5.26) is
identically zero. This agrees with the fact that the functio nV , that describes the limiting
behavior of the colored Jones polynomial in (5.15) – (5.16) i s also real. Therefore, the
imaginary part of the proposed relation (5.12) is true — both sides vanish identically —
and we only need to verify the real part.
Fortunately, we do not need to evaluate the integral (5.25) e xplicitly in order to check
the real part of the generalized volume conjecture (5.12). S ince we are interested only
in y-dependent terms, we only have to compare (5.22) with the der ivative of the volume
function (5.25),
− log|l| =− log
[
cos(4y)− cos(2y)− 1−
√
(cos(4y)− cos(2y)− 1)2− 1
]
(5.28)
It is amusing to verify that the functions (5.22) and (5.28) a re indeed identical.
