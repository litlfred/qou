---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-027-appendix-a-the-btz-black-hole
section_title: "The BTZ Black Hole"
section_number: Appendix A
pages: 53-59
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
toc_source: inferred
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with complex gauge group SL(2,C), which has many interesting connections"
---
The metric of the Lorentzian BTZ black hole is described by the line element21 [96]:
ds2 = −

r2 −M

dt2 +

r2 −M
−1
dr2 + r2dφ2
(A.1)
Analytic continuation leads to the Euclidean metric
ds2 =

r2 −M

dt2 +

r2 −M
−1
dr2 + r2dφ2
(A.2)
This is a special case of a more general metric corresponding to a rotating BTZ black hole.
Namely, a solution corresponding to a black hole with mass M and angular momentum J
assumes the following form:
ds2 = N 2dτ 2 + N −2dr2 + r2
dφ2 + N φdτ
2
N =
r
r2 −M −J2
4r2
,
N φ = −J
2r2
r2
± = M
2
h
1 ±
r
1 +
 J
M
2i
(A.3)
This geometry can be represented as a quotient (2.8) of the hyperbolic 3-space,
M = IH3/Γ
21 We remind that, in our notations, ℓ= 1.
52
by a discrete group Γ. The explicit change of variables, which brings the Euclidean metric
(A.3) to the standard hyperbolic metric (2.7) on IH3, is given by
x =
s
r2 −r2
+
r2 −r2
−
· cos

r+τ + |r−|φ

· er+φ−|r−|τ
y =
s
r2 −r2
+
r2 −r2
−
· sin

r+τ + |r−|φ

· er+φ−|r−|τ
z =
s
r2
+ −r2
−
r2 −r2
−
· er+φ−|r−|τ
(A.4)
In order to identify the quotient group Γ, it is convenient to write (x, y, z) in terms of
the spherical coordianates,
x = R cos θ cos χ
y = R sin θ cos χ
z = R sin χ
(A.5)
In these variables, the black hole metric has the form
ds2 =
1
sin2 χ
dR
R
2
+ cot2 χ dθ2 +
1
sin2 χdχ2
(A.6)
and the identiﬁcations on IH3 that generate the holonomy group Γ are
(a) :
(R, θ, χ) ∼(R · e2πr+, θ + 2π|r−|, χ)
(b) :
(R, θ, χ) ∼(R, θ + 2π, χ)
(A.7)
γm
χ=0
γl
M
horizon
χ= π/2
unknot
Fig. 12: The Euclidean BTZ black hole has a geometry of the solid torus, M ∼=
D2 × S1. We can also view M as a complement of the unknot (the trivial knot) in
the 3-sphere.
53
Using (A.5) and (A.7), it is easy to see that the resulting geometry is a solid torus,
M ∼= D2 × S1, shown on ﬁg. 12. The core of the torus (the circle χ = π/2) corresponds
to the position of the “horizon”. The solid torus M can be also viewed as a complement
of the unknot (the trivial knot) in the 3-sphere, M = S3 \ K. The tubular neighborhood
of the trivial knot K is itself homeomorphic to a solid torus, cf. ﬁg. 5. Thus, a union of
these two solid tori joined along a common torus boundary gives back the 3-sphere.
Notice, that the longitude γl of the unknot is contractible in M, whereas the meridian
γm is a non-trivial cycle in M. Therefore, it follows that the holonomy l must be trivial,
whereas the value of m can be arbitrary. Hence, we conclude that the A-polynomial of the
unknot has the following simple form, cf. (2.16),
Aunknot(l, m) = l −1
(A.8)
It turns out that this result has a nice physical interpretation. Namely, the vanishing of
the polynomial (A.8) can be viewed as a “mass shell” condition for the so-called oﬀ-shell
BTZ black hole, which we are going to describe next.
The geometry of the oﬀ-shell BTZ black hole can be obtained from (A.7) by replacing
the second identiﬁcation with a more general condition [49,50,51,28]:
(b′) :
(R, θ, χ) ∼(eΣ · R, θ + Θ, χ)
(A.9)
The resulting identiﬁcations (A.7) - (A.9) can be represented by the elements of the
SL(2,C) group,
ρ(a) =

eπ(r++i|r−|)
0
0
e−π(r++i|r−|)

,
ρ(b′) =

e(Σ+iΘ)/2
0
0
e−(Σ+iΘ)/2

(A.10)
acting on the hyperbolic 3-space as in (2.9). These two elements generate the holonomy
group Γ ⊂SL(2,C), such that the quotient space M = IH3/Γ is a solid torus with a conical
singularity at the “horizon”, which resembles the space-time geometry around the spinning
particle in 2+1 dimensions [13]. In this more general family of solutions, the usual BTZ
black hole metric without a conical singularity is reproduced when
Σ = 0
,
Θ = 2π
(A.11)
Following the standard terminology, we refer to this condition as the “mass shell” condition.
54
In what follows, our goal will be to construct a ﬂat SL(2,C) connection corresponding
to the more general class of BTZ black home geometries and, in particular, to demonstrate
that the mass shell condition (A.11) is equivalent to the vanishing of the A-polynomial
(A.8). For this, we need to evaluate the holonomies of the gauge connection,
ρ(γ) = P exp
I
γ
A,
(A.12)
along the longitude, γl, and the meridian, γm. One can choose to parameterize these cycles
by a real variable s ∈[0, 1], such that
γm :
s 7→(R0e2πr+s, θ0 + 2π|r−|s, χ0)
γl :
s 7→(R0esΣ, θ0 + sΘ, χ0)
(A.13)
Notice, that due to the identiﬁcations (A.7) - (A.9), the curves γm and γl are manifestly
closed.
In order to evaluate the holonomies (A.12), we also need to construct the complex
valued gauge connection, Aa = wa + iea, from the components of the vielbein and the
spin connection in the Euclidean BTZ black hole geometry. The latter can be taken, for
example, in the following form [50,51]:
e1 =
1
sin χ
dR
R
e2 =
1
sin χdχ
e3 = cot χ · dθ
w1 = −
1
sin χdθ
w2 = 0
w3 = cot χ · dR
R
(A.14)
It is easy to verify that the corresponding SL(2,C) gauge connection is indeed ﬂat. How-
ever, as we shall see in a moment, this choice of the vielbein and the spin connection leads
to a singular connection22, A. Indeed, even though (A.14) deﬁnes a smooth metric (A.6),
it corresponds to a singular gauge ﬁeld, A1 = w1 + ie1, which is not well deﬁned near the
center of the solid torus, χ = π/2, where the angular variable θ is ill-deﬁned and w1 ≈−dθ.
Another way to see that (A.14) does not correspond to a smooth SL(2,C) connection
over M is to evaluate the holonomies (A.12) around the 1-cycles (A.13). The resulting
holonomies turn out to be in the same conjugacy class as the generating elements (A.10)
22
I am endebted to G. Moore and A. Strominger for very helpful comments and suggestions
on these points.
55
of the group Γ. Therefore, comparing (A.10) with (2.10), we conclude that in the present
case the holonomies l and m are given by
l = e(Σ+iΘ)/2
,
m = eπ(r++i|r−|)
(A.15)
In particular, we ﬁnd that, with the choice (A.14), the “mass shell” condition (A.11) looks
like
l + 1 = 0
(A.16)
and has the ‘wrong’ sign compared to (A.8). This result does not agree with the fact that
the 1-cycle γl becomes contractible in the on-shell BTZ black hole geometry and, therefore,
the corresponding holonomy should be trivial. Finally, let us remark that this problem can
not be ﬁxed by applying a gauge transformation to (A.14) since any (non-singular) gauge
transformation can not change the holonomy.
Therefore, we need to construct a ﬂat SL(2,C) gauge connection that would be non-
singular everywhere inside M. It is convenient to introduce a new set of coordinates:̺
= log R
ξ = f(χ) cos θ
η = f(χ) sin θ
(A.17)
where the function,
f(χ) =
cos χ
1 + sin χ,
(A.18)
is chosen such that the metric induced in the (ξ, η)-plane is conformal to the usual Eu-
clidean metric, ds2 = dξ2 + dη2. Speciﬁcally, rewriting the BTZ black hole metric (A.6) in
the coordinates (A.17), we ﬁnd
ds2 =
1 + f 2
1 −f 2
2 h
d̺ 2 +
4
(1 + f 2)2 (dξ2 + dη2)
i
(A.19)
The corresponding components of the vielbein and the spin connection can be written
as
e1 = 1 + f 2
1 −f 2 d̺
e2 =
2
1 −f 2 dξ
e3 =
2
1 −f 2 dη
w1 = ξe3 −ηe2
w2 =
2η
1 + f 2 e1
w3 = −
2ξ
1 + f 2 e1
(A.20)
56
Combining these together we ﬁnd the explicit expression for the components of the ﬂat
SL(2,C) gauge connection, Aa = wa + iea,
A1 =
2ξ
1 −f 2 dη −
2η
1 −f 2 dξ + i1 + f 2
1 −f 2 d̺
A2 =
2η
1 −f 2 d̺ + i
2
1 −f 2 dξ
A3 = −
2ξ
1 −f 2 d̺ + i
2
1 −f 2 dη
(A.21)
which is non-singular everywhere in the interior of the solid torus, M = S1 × D2.
Now let us evaluate the SL(2,C) holonomies (A.12). For simplicity, let us consider
a non-rotating BTZ black hole, with J = 0. Then, the second identiﬁcation in (A.7) is
trivially realized in the coordinates (A.17), whereas the ﬁrst one reads:
(a) :
(̺ , ξ, η) ∼(̺ + 2πr+, ξ, η)
(A.22)
Therefore, we can choose the cycles γl and γm to be parametrized in the following way, cf.
(A.13),
γm :
s 7→(̺ 0 + 2πr+s, ξ = 0, η = 0)
γl :
s 7→(̺ 0, ξ = ξ0 cos 2πs, η = ξ0 sin 2πs)
(A.23)
Since only the A1-component of the gauge connection is non-trivial along the curve
γm, we can easily ﬁnd the corresponding holonomy,
ρ(γm) =

eπr+
0
0
e−πr+

(A.24)
Comparing this result with (A.15), we ﬁnd that the holonomy of the gauge connection
(A.21) around γm is the same as in the previous calculation, based on the singular gauge
connection (A.14). On the other hand, since the connection (A.21) is ﬂat and non-singular
everywhere in the interior of the solid torus, the holonomy around a contractible cycle γl
is guaranteed to vanish automatically,
l = 1
However, since many components of the gauge connection (A.21) do not vanish along the
curve γl, to verify this directly would require some work. Perhaps the best way to approach
this problem would be to ﬁnd a gauge transformation, which removes non-commuting
components of the gauge connection, and allows to write the holonomy (A.12) in a simple
form.
57
