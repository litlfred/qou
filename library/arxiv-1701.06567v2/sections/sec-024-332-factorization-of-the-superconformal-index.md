---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-024-332-factorization-of-the-superconformal-index
section_title: "Factorization of the superconformal index"
section_number: 3.3.2
pages: 48-50
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
The superconformal index of 3d N = 2 theory (3.120) reads
IT[M3](q, t) =
X
m≥0
1
|Wm|
Z
|z|=1
dz
2πiz z2pm (1 −z±2qm) q−2m(1−g) t−2m(1−g)×
(z±2qmt−1; q)∞(t−1; q)∞
(z±2qm+1t)∞(qt; q)∞
×
g
Y
i=1
(z±2u−1
i qm+1; q)∞(u−1
i q; q)∞
(z±2uiqm; q)∞(ui; q)∞
·
(z±2tuiqm+1; q)∞(tuiq; q)∞
(z±2t−1u−1
i qm; q)∞(t−1u−1
i ; q)∞
.
(3.129)
Unlike in the case of Lens spaces (g = 0), now there is some ambiguity in the choice of the
contour, because if |t| = 1 there are poles at |z| = 1. The natural physical choice assumes that
|q| < 1 and |ui| = |t−1u−1
i | = qϵ with ϵ > 0, which corresponds to choosing an inﬁnitesimally
small R-charge for adjoint hypers. However, such choice of the contour is diﬀerent from the
one in (3.122) and (3.127), illustrated in Figure 4.
Next, we would like to show that
IT[M3](q, t, u) =
X
a
|Wa| bZa(q, t, u) bZa(1/q, 1/t, 1/u).
(3.130)
– 47 –
1/2
1/2
°
jzj=1
z2
jzj2¼q-1
jzj2¼q-2
jzj2¼q
jzj2¼q2
Figure 4: Pole structure of the integrands in (3.122) and (3.129). The green contour corresponds to
a choice of the contour γ such that in the t →1 limit it agrees with the principal-value prescription
in (3.127) which reproduces the WRT invariant. The blue contour is the standard physical choice of
contour for the superconformal index (3.129).
As before, the problem with checking it directly is that we only have the expression for bZa(q, t)
which is valid inside a unit disc |q| < 1, without any systematic way of analytically continuing
it outside. Again, we can instead try to check (3.130) in a particular limit of ﬂavor fugacities
such that bZa(q, t) becomes a rational function and has canonical analytic continuation outside
of |q| < 1. However, one ﬁnds that there are several new technical complications compared
to the case of Lens spaces (g = 0). First, there is an ambiguity in the choice of the contours
(i.e. whether we encircle the poles at z2 = t±1/2 or not), illustrated in Figure 4. Second, for
g > 1 the limit ui →1, t →qβ with β ∈Z≥0 does not give a rational function, but rather a
lacunary function that cannot be analytically continued outside |q| < 1 due to the Fabry gap
theorem. In particular, one cannot repeat the trick with the cyclotomic expansion due to the
absence of closed form expression for t = 1.
However, one can avoid all these problems by taking the limit ui →1, t →qβ, with β < 0.
In this limit, all poles at |z| ≈1 disappear and the contour ambiguity becomes irrelevant.
Namely, for β ∈Z−, let us deﬁne
bZ(β)
a (q) ≡
bZa(q, t) (qt; q)∞
g
Y
i=1
(ui; q)∞
(tuiq; q)∞

t=qβ,ui=1
(3.131)
and
I(β)(q) ≡I(q, t) (qt; q)∞
(1/t; q)∞
g
Y
i=1
(ui; q)∞(t−1u−1
i ; q)∞
(u−1
i q; q)∞(tuiq; q)∞

t=qβ,ui=1
.
(3.132)
Then, one can check for various values of g, p, β < 0 that indeed
I(β)(q) =
X
a
|Wa| bZ(β)
a (q) bZ(β)
a (1/q).
(3.133)
For example, let us take g = 2 and p = 5. Then, we have the following.
– 48 –
β = −1:
2 bZ(−1)
0
(q) = 1 ,
bZ(−1)
1
(q) = 0 ,
bZ(−1)
2
(q) = 0.
2I(−1)(q) = 1.
(3.134)
β = −2:
2 bZ(−2)
0
(q) = q−2 + 1 ,
bZ(−2)
1
(q) = q−4/5 ,
bZ(−2)
2
(q) = 0.
2I(−2)(q) = 4 + q2 + 1
q2 .
(3.135)
β = −3:
2 bZ(−3)
0
(q) = 1
q6 + 1
q4 + 2
q3 + 1
q2 + 1, bZ(−3)
1
(q) = −
(q+1)2(q2−q+1)
q24/5
, bZ(−3)
2
(q) =
1
q11/5 .
2I(−3)(q) = q6 + 1
q6 + 4q4 + 4
q4 + 8q3 + 8
q3 + 5q2 + 5
q2 + 8q + 8
q + 18.
. . .
(3.136)
And indeed one can verify that in each case
I(β)(q) = 2 bZ(β)
0
(q) bZ(β)
0
(1/q) + bZ(β)
1
(q) bZ(β)
1
(1/q) + bZ(β)
2
(q) bZ(β)
2
(1/q).
(3.137)
Note, when g > 1 the fundamental group π1(M3) is non-abelian and Mﬂat(M3, SL(2, C)) has
irreducible ﬂat connections. We conﬁrmed, however, that the WRT invariant and the super-
conformal index both have a natural decomposition into contributions labelled by connected
components of abelian ﬂat connections.41 This “completeness” of the homological blocks is
a striking and highly non-trivial phenomenon. Its physical origin was already discussed in
section 2 from the viewpoint of resurgent analysis and charges which label BPS states / enu-
merative invariants in the physical system (2.13). It would be interesting to explore it further
in various duality frames and from other vantage points.
