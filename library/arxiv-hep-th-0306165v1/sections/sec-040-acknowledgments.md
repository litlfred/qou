---
doc_id: arxiv-hep-th-0306165v1
doc_title: "which has many interesting connections with three-dimensi onal quantum gravity and ge- ometry of hyperbolic 3-manifolds. We show that, in the prese nce of a single knotted Wilson l"
section_id: sec-040-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 53-56
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting connections with three-dimensi onal quantum gravity"
---
It is a pleasure to thank D. Bar-Natan, R. Dijkgraaf, N. Dunﬁe ld, S. Garoufalidis,
R. Gopakumar, G. Horowitz, D. Long, M. Mari˜ no, S. Minwalla, H. Ooguri, F. Rodriguez-
Villegas, L. Rozansky, C. Vafa, E. Witten, S.-T. Yau, and esp ecially K. Krasnov, G. Moore,
A. Strominger, and D. Thurston for valuable and stimulating discussions. This research was
conducted during the period S.G. served as a Clay Mathematic s Institute Long-Term Prize
Fellow. This work is also supported in part by RFBR grant 01-0 1-00549 and RFBR grant
for Young Scientists 02-01-06322. I would also like to thank the University of California
at Santa Barbara, Stanford University, California Institu te of Technology, and Rutgers
University for kind hospitality while this work was in progr ess.
Appendix A. The BTZ Black Hole
The metric of the Lorentzian BTZ black hole is described by th e line element 21 [96]:
ds2 =−
(
r2−M
)
dt2 +
(
r2−M
) −1
dr2 +r2dφ2 (A.1)
Analytic continuation leads to the Euclidean metric
ds2 =
(
r2−M
)
dt2 +
(
r2−M
) −1
dr2 +r2dφ2 (A.2)
This is a special case of a more general metric corresponding to a rotating BTZ black hole.
Namely, a solution corresponding to a black hole with mass M and angular momentum J
assumes the following form:
ds2 =N 2dτ 2 +N −2dr2 +r2
(
dφ2 +N φdτ
) 2
N =
√
r2−M− J 2
4r2 , N φ =− J
2r2
r2
± = M
2
[
1±
√
1 +
( J
M
) 2]
(A.3)
This geometry can be represented as a quotient (2.8) of the hy perbolic 3-space,
M = I H3/Γ
21 We remind that, in our notations, ℓ = 1.
52
by a discrete group Γ. The explicit change of variables, whic h brings the Euclidean metric
(A.3) to the standard hyperbolic metric (2.7) on I H 3, is given by
x =
√
r2−r2
+
r2−r2
−
· cos
(
r+τ +|r−|φ
)
·er+φ −|r−|τ
y =
√
r2−r2
+
r2−r2
−
· sin
(
r+τ +|r−|φ
)
·er+φ −|r−|τ
z =
√
r2
+−r2
−
r2−r2
−
·er+φ −|r−|τ
(A.4)
In order to identify the quotient group Γ, it is convenient to write (x,y,z ) in terms of
the spherical coordianates,
x =R cosθ cosχ
y =R sinθ cosχ
z =R sinχ
(A.5)
In these variables, the black hole metric has the form
ds2 = 1
sin2χ
( dR
R
) 2
+ cot2χ dθ2 + 1
sin2χdχ2 (A.6)
and the identiﬁcations on I H 3 that generate the holonomy group Γ are
(a) : ( R,θ,χ )∼ (R·e2πr +,θ + 2π|r−|,χ )
(b) : ( R,θ,χ )∼ (R,θ + 2π,χ )
(A.7)
γm
χ=0γl
M
horizon
χ = π/2
unknot
Fig. 12: The Euclidean BTZ black hole has a geometry of the solid torus , M ∼
=
D2 × S1. We can also view M as a complement of the unknot (the trivial knot) in
the 3-sphere.
53
Using (A.5) and (A.7), it is easy to see that the resulting geo metry is a solid torus,
M∼
= D2× S1, shown on ﬁg. 12. The core of the torus (the circle χ = π/2) corresponds
to the position of the “horizon”. The solid torus M can be also viewed as a complement
of the unknot (the trivial knot) in the 3-sphere, M = S3\K. The tubular neighborhood
of the trivial knot K is itself homeomorphic to a solid torus, cf. ﬁg. 5. Thus, a union of
these two solid tori joined along a common torus boundary giv es back the 3-sphere.
Notice, that the longitude γl of the unknot is contractible in M , whereas the meridian
γm is a non-trivial cycle in M . Therefore, it follows that the holonomy l must be trivial,
whereas the value of m can be arbitrary. Hence, we conclude that the A-polynomial o f the
unknot has the following simple form, cf. (2.16),
Aunknot(l,m ) = l− 1 (A.8)
It turns out that this result has a nice physical interpretat ion. Namely, the vanishing of
the polynomial (A.8) can be viewed as a “mass shell” conditio n for the so-called oﬀ-shell
BTZ black hole, which we are going to describe next.
The geometry of the oﬀ-shell BTZ black hole can be obtained fr om (A.7) by replacing
the second identiﬁcation with a more general condition [49, 50,51,28]:
(b′) : ( R,θ,χ )∼ (eΣ ·R,θ + Θ ,χ ) (A.9)
The resulting identiﬁcations (A.7) - (A.9) can be represent ed by the elements of the
SL(2,
C) group,
ρ(a) =
(
eπ (r++i|r−|) 0
0 e−π (r++i|r−|)
)
, ρ (b′) =
(
e(Σ+ iΘ) / 2 0
0 e−(Σ+ iΘ) / 2
)
(A.10)
acting on the hyperbolic 3-space as in (2.9). These two eleme nts generate the holonomy
group Γ ⊂SL(2,C), such that the quotient space M = I H3/Γ is a solid torus with a conical
singularity at the “horizon”, which resembles the space-ti me geometry around the spinning
particle in 2+1 dimensions [13]. In this more general family of solutions, the usual BTZ
black hole metric without a conical singularity is reproduc ed when
Σ = 0 , Θ = 2 π (A.11)
Following the standard terminology, we refer to this condition as the “mass shell” condition.
54
In what follows, our goal will be to construct a ﬂat SL(2,C) connection corresponding
to the more general class of BTZ black home geometries and, in particular, to demonstrate
that the mass shell condition (A.11) is equivalent to the van ishing of the A-polynomial
(A.8). For this, we need to evaluate the holonomies of the gau ge connection,
ρ(γ) = P exp
∮
γ
A, (A.12)
along the longitude, γl, and the meridian, γm. One can choose to parameterize these cycles
by a real variable s∈ [0, 1], such that
γm : s↦→(R0e2πr +s,θ 0 + 2π|r−|s,χ 0)
γl : s↦→(R0esΣ ,θ 0 +sΘ ,χ 0)
(A.13)
Notice, that due to the identiﬁcations (A.7) - (A.9), the cur ves γm and γl are manifestly
closed.
In order to evaluate the holonomies (A.12), we also need to co nstruct the complex
valued gauge connection, Aa = wa +iea, from the components of the vielbein and the
spin connection in the Euclidean BTZ black hole geometry. Th e latter can be taken, for
example, in the following form [50,51]:
e1 = 1
sinχ
dR
R
e2 = 1
sinχdχ
e3 = cotχ·dθ
w1 =− 1
sinχdθ
w2 = 0
w3 = cotχ· dR
R
(A.14)
It is easy to verify that the corresponding SL(2,C) gauge connection is indeed ﬂat. How-
ever, as we shall see in a moment, this choice of the vielbein a nd the spin connection leads
to a singular connection 22,A. Indeed, even though (A.14) deﬁnes a smooth metric (A.6),
it corresponds to a singular gauge ﬁeld, A1 =w1 +ie1, which is not well deﬁned near the
center of the solid torus, χ =π/2, where the angular variable θ is ill-deﬁned and w1≈−dθ.
Another way to see that (A.14) does not correspond to a smooth SL(2,C) connection
over M is to evaluate the holonomies (A.12) around the 1-cycles (A. 13). The resulting
holonomies turn out to be in the same conjugacy class as the ge nerating elements (A.10)
