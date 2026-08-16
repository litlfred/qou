---
doc_id: helicity03mmj
doc_title: "MOSCOW MA THEMA TICAL JOURNAL"
section_id: sec-008-41-linking-of-a-curve-with-a-foliation
section_title: "Linking of a curve with a foliation"
section_number: 4.1
pages: 12-14
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
doc_brief: "MOSCOW MATHEMATICAL JOURNAL — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
foliation of codimension 2 and a divergence-free vector ﬁeld is a direct generaliza-
tion of the cross-helicity, cf. [ 2], [ 16], [ 17]. The corresponding helicity invariants in
higher dimensions are similar to those appearing in higher-dimensional ideal hy-
drodynamics, an odd-dimensional ideal incompressible ﬂuid moving according to
the Euler equations. It should be mentioned however, that they do not seem to be
related to higher-dimensional physical problems, similar, e. g. to the helicity-energy
interaction in the MHD theory in two and three dimensions.
Let M be a closed manifold with b1(M ) = 0 and equipped with a volume form µ.
Consider an oriented codimension 2 foliation F with a holonomy-invariant trans-
verse measure β. To such a foliation one can associate a current C(F) : Ωn−2(M ) →
R, which sends any smooth ( n − 2)-form θ on M to its integral against β:
C(F) : θ ↦→
∫
M
θ ∧ β.
(The integral here can be deﬁned via a partition of unity subordinated to a folia-
tion chart for F: one integrates the summands over the leaf plaques in the charts,
and then integrates the result over transversals using the measure β.) This current
is closed and is called the Ruelle–Sullivan cycle of the invariant measure β [23].
Assume that this cycle is null-homologous: [ C(F)] = 0 ∈ Hn−2(M, R). (Geometri-
cally one might think of this condition that the “leaves would be boundaries if they
were compact manifolds,” cf. Remark 2.8.)
If we imagine that the measure β is represented by a smooth 2-form on M ,
then necessarily this form is exact, since [ C(F)] = 0. Moreover, the foliation F is
spanned by the distribution of kernels of this form: β = iF µ. In the sequel we will
be often dealing with the measure β as it were a smooth 2-form, while one has to
use the language of the Ruelle–Sullivan cycles to furnish the details, see the careful
study in [ 17].
Deﬁnition 4.1. The average linking of a curve Γ with the measured foliation F
is the β-measure of an arbitrary surface ∂−1Γ bounded by Γ. In other words, it is
the ﬂux of the 2-form β = iF µ through ∂−1Γ:
lk(Γ, F) =
∫
∂−1Γ
β =
∫
Γ
d−1β.
The motivation of this deﬁnition is as follows. Suppose, that we are given a mea-
sured foliation F, where the total weight is supported on a single (null-homologous)
compact leaf N of codimension 2. Then
∫
Γ d−1β is equal to the linking number of
N and the curve Γ. Similarly, for a foliation with compact nonsingular ﬁbers, the
number lk(Γ, F) gives the average for the linking numbers of the curve Γ with every
ﬁber, cf. [ 16], [ 2].
4.2. Linking of a vector ﬁeld with a foliation. By analogy with the three-
dimensional case, we can now deﬁne an asymptotic and average linking numbers
for a vector ﬁeld and a measured foliation. For a ﬁeld ξ on M denote by Γ T (x) a
GEOMETRY OF HIGHER HELICITIES 1001
closed curve consisting of the long segment (for time 0 ≤ t ≤ T ) of the ξ-trajectory
gt
ξx starting at x ∈ M and of a short closing path (e. g., geodesic).
Deﬁnition 4.2. An asymptotic linking lkξ(x, F) of the trajectory of a vector ﬁeld
ξ emanating from a point x ∈ M with the measured foliation F is the time-average
of the linking number of the curve Γ T (x) with F:
lkξ(x, F) = lim
T →∞
1
T lk(ΓT (x), F).
The average linking number of the vector ﬁeld ξ and the measured foliation F
on the manifold M equipped with the volume form µ is
lkξ(F) =
∫
M
lkξ(x, F)µ.
Deﬁnition 4.3. The cross-helicity of a vector ﬁeld ξ and a codimension 2 foliation
F with transverse holonomy-invariant measure β is
H(ξ, F) :=
∫
M
β ∧ d−1(iξµ),
cf. the 3D case ( 2).
Theorem 4.4 [16], [17]. Let ξ be a divergence-free vector ﬁeld on M with a volume
form µ, and F a foliation of codimension 2 with a transverse holonomy-invariant
measure β. Then the average linking number of the vector ﬁeld ξ with the foliation
F is equal to the cross-helicity of ξ and F:
lkξ(F) = H(ξ, F).
Proof.
lkξ(F) =
∫
M
lkξ(x, F) µ =
∫
M
[
lim
T →∞
1
T lk(ΓT (x), F)
]
µ
=
∫
M
[
lim
T →∞
1
T lk(g[0,T ]
x , F)
]
µ =
∫
M
[
lim
T →∞
1
T
(∫
g[0,T ]
x
d−1β
)]
µ
=
∫
M
[
lim
T →∞
1
T
∫ T
0
iξ(d−1β)dt
]
µ.
The latter integrand is the time average of the function iξ(d−1β). By the Birkhoﬀ
ergodic theorem applied to the µ-preserving ﬂow of the ﬁeld ξ, the time average is
equal to the space average of the same function:∫
M
iξ(d−1β) µ =
∫
M
d−1β ∧ iξµ =
∫
M
β ∧ d−1(iξµ) = H(ξ, F).
On the way, we replaced the integral over a closed curve Γ T (x) by the integral over
a non-closed piece of trajectory g[0,T ]
x . Indeed, the diﬀerence of the two integrals is
the integral of an L1 1-form d−1β over the short path (a shortest geodesic) from
x to the other endpoint of g[0,T ]
x . It is uniformly bounded by the product of the
diameter of M and the norm of d−1β (note that d−1 is a compact operator). Hence
it can be neglected after division by T and considering the limit T → ∞. □
1002 B. KHESIN
Remark 4.5. Note that the proof of Arnold’s theorem 2.5 is achieved similarly
by applying the Birkhoﬀ ergodic theorem to the ﬁeld ξ × ξ on M × M , and using
the short path properties (Section 3.4). For more details on the case of a general
transverse holonomy-invariant measure we refer to [ 17].
