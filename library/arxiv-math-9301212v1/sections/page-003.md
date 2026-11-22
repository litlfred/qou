---
doc_id: arxiv-math-9301212v1
doc_title: "arXiv:math/9301212v1 [math.GT] 1 Jan 1993"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 9301212v1.pdf
source_sha256: 029787800ddf73e5
toc_source: undetermined
doc_brief: "arXiv:math/9301212v1 [math.GT] 1 Jan 1993 — A physically natural potential energy for simple closed curves in R3 is shown to be invariant under M¨obius transformations."
---
M ¨OBIUS INVARIANCE OF KNOT ENERGY
3
of radius ε, Bε, only in its boundary Sε, then γK∩Sε consists of (at most) one point.
The idea is that if γK ∩Sε is disconnected, inverting an arc of γK\Sε into Bε will
lower energy while preserving the knot type. Thus there is a continuous projection
from the ε-neighborhood of γK to γK given by “closest point” π: Nε(γK) →γK.
We prove that the ﬁbers π−1(pt) are all geometric planar disks of radius ε. The
disjointness of these “normal” ﬁbers to distance ε is equivalent to the existence of
a continuously turning tangent to γk whose generalized derivative is in L∞.
□
A detailed proof of Theorem C will appear elsewhere.
Proof of Theorem D. Theorem 2.5 of [FH] gives the inequality
c([γ]) ≤c(γ) ≤E(γ)/2π
for proper rectiﬁable lines. According to the M¨obius Invariance Property, the energy
will increase by exactly 4 if a M¨obius transformation is used to move the line oﬀ
inﬁnity and into closed position.
□
Proof of M¨obius Invariance Property. It is suﬃcient to consider how I, an inversion
in a sphere, transforms energy. Let u be the arc length parameter of a rectiﬁable
closed curve γ, u ∈R/lZ. Let
(1)
Eε(γ) =
ZZ
|u−v|≥ε

1
|γ(u) −γ(v)|2 −
1
(D(γ(u), γ(v)))2

du dv
and
(2)
Eε(I ◦γ) =
ZZ
|u−v|≥ε

1
|I ◦γ(u) −I ◦γ(v)|2 −
1
(D(I ◦γ(u), I ◦γ(v)))2

× ∥I′(γ(u))∥· ∥I′(γ(v))∥du dv.
Clearly E(γ) = limε→0 Eε(γ) and E(I ◦γ) = limε→0 Eε(I ◦γ).
It is a short calculation (using the law of cosines) that the ﬁrst terms transform
correctly, i.e.,
∥I′(γ(u))∥· ∥I′(γ(v))∥
|I(γ(u)) −I(γ(v))|2
=
1
|γ(u) −γ(v)|2 .
Since u is arclength for γ, the regularization term of (1) is the elementary integral
(3)
Z l
u=0
"
2
Z l/2
v=ε
1
v2 dv
#
du = 4 −2l
ε .
Let s be an arclength parameter for I ◦γ. Then ds(u)/du = ∥I′(γ(u))∥where
∥I′(γ(u))∥= f(u) denotes the linear expansion factor of I′. Since γ(u) is a lipschitz
function and I′ is smooth, f(u) is lipschitz, hence, it has a generalized derivative
f ′(u) ∈L∞.
(4)
regularization (2) =
Z
u∈R/lZ
"Z
|v−u|≥ε
|(I ◦γ)′(v)| dv
D(I ◦γ(u), I ◦γ(v))2
#
|(I ◦γ)′(u)| du
=
Z
R/lZ
 4
L −1
ε+
−1
ε−

ds,
