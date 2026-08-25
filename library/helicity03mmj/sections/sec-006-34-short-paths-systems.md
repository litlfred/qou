---
doc_id: helicity03mmj
doc_title: "Geometry of higher helicities"
section_id: sec-006-34-short-paths-systems
section_title: "Short paths systems."
section_number: 3.4
pages: 10-12
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
doc_brief: "Geometry of higher helicities — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
one needs to pass to linkings of non-closed curves. A way to do this is to introduce
a “linking form.”
Deﬁnition 3.13. A linking form on an n-dimensional compact manifold M is
a ( k, l )-form LF ∈ Ω∗(M × M ) satisfying the condition: the linking number of
any two non-intersecting closed oriented compact submanifolds P and Q of linking
dimensions k and l (with k + l = n − 1) is given by the double integral
∫ ∫
P ×Q⊂M ×M
LF.
For instance, the Gauss linking form in R3 is a linking (1 , 1)-form, whose value
at a point ( x, y ) ∈ R3 × R3 on a pair of vectors v and w is
LF (x, y )|(v,w) = 1
4π
(v × w, x − y)
|x − y|3 ,
cf. the Gauss formula ( 1). One can show that a linking form exists on a manifold M
provided that bk(M ) = bk+1(M ) = 0, see details in [ 2]. The linking form LF can
be chosen to have a singularity 1 /rn−1, where r is the distance to the diagonal in
M × M (similar to the Gauss LF , see formula ( 1) for n = 3), i. e. to be integrable:
LF ∈ L1(M × M ), since the diagonal is of codimension n in M × M .
The introduction of such a form allows one to consider “linking of non-closed
submanifolds.” In particular, we deﬁne the linking of non-closed segments γ1 and
γ2 in R3 by
lk(γ1, γ 2) :=
∫ ∫
γ1×γ2
LF. (3)
Recall that the linking of trajectories of a vector ﬁeld ξ issuing from the points
x and y is the limit
λξ(x1, x 2) = lim
T1,T2→∞
1
T1 · T2
lk(ΓT1(x1), ΓT2(x2)).
GEOMETRY OF HIGHER HELICITIES 999
Each curve Γ Tj (xj) = g[0,Tj ]
xj ∪ ∆xj consists of a long piece of a trajectory g[0,Tj ]
xj and
a short closing segment ∆ xj . The systems of short paths (SSP) {∆} should satisfy
the following conditions ensuring the limit existence, see [ 1]. Due to the additivity
of the linking number (as the double integral ( 3) of the linking form), we have:
lk(ΓT1(x1), ΓT2(x2)) = lk( g[0,T1]
x1 ∪ ∆x1, g [0,T2]
x2 ∪ ∆x2)
= lk(g[0,T1]
x1 , g [0,T2]
x2 ) + lk(g[0,T1]
x1 , ∆x2) + lk(∆x1, g [0,T2]
x2 ) + lk(∆x1, ∆x2).
The ﬁrst term describes the average linking (after the division by T1 · T2) of the
corresponding trajectories. Therefore, one has to ensure that the contribution of
any of the remaining three summands is negligible. For instance, one could require
that each of them does not grow faster than a linear function of T1 or T2 for almost
all points x1, x 2 ∈ M , and hence, after taking the time average (i. e., after dividing
by T1 · T2) their contributions to lk(Γ T1(x1), ΓT2(x2)) tend to 0 as T1 and T2 go to
inﬁnity.
Remark 3.14. In [ 1] it was discussed that there are plenty of SSP which pro-
vide this bound for almost all pairs x1 and x2. Note that there might be some
exceptional values of x1 and x2, where, e. g., the ξ-trajectory through x1 winds
exponentially fast on a short path for x2. Then, of course, lk( g[0,T1]
x1 , ∆x2) grows
also exponentially, as T1 → ∞ , even after the division by T1. One can see that a
small perturbation of such a system {∆} destroys this exponential winding. This
way, however, the deﬁnition of the SSP might depend on the ﬁeld ξ. T. Vogel in
[25] suggested to replace the convergence almost everywhere by the L1 convergence,
which allowed one to present some universal SSPs.
Deﬁnition 3.15 [25]. A system {∆} is a system of short paths on M if for any
pair of points x1, x 2 ∈ M there is a piecewise diﬀerentiable path ∆ x1,x2 ∈ {∆} such
that the limits
lim
T1,T2→∞
1
T1 · T2
∫ ∫
g[0,T1]
x1 ×∆x2
|LF |
for g[0,T1]
x1 × ∆x2, as well as those for ∆ x1 × g[0,T2]
x2 and ∆ x1 × ∆x2, vanish in the L1
sense.
Theorem 3.16 [25]. On any compact Riemannian manifold M a system of shortest
geodesics joining any pair of points x1 and x2 is a system of short paths for any
vector ﬁeld ξ.
Note that the description of the SSP might be related to the problem of the
helicity invariance with respect to volume-preserving homeomorphisms. While for
a ﬁeld in a solid torus (the only case where this invariance was proved [ 10]) there
is a natural system of short paths, in general one has to be sure that a SSP is
not spoiled too much by a homeomorphism, in order to apply the homeomorphism
invariance of the linking number for closed curves.
1000 B. KHESIN
