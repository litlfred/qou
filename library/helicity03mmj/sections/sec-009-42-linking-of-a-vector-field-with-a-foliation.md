---
doc_id: helicity03mmj
doc_title: "Geometry of higher helicities"
section_id: sec-009-42-linking-of-a-vector-field-with-a-foliation
section_title: "Linking of a vector field with a foliation."
section_number: 4.2
pages: 12-14
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
toc_source: outline
doc_brief: "Geometry of higher helicities — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
dimensional case, we can now deﬁne an asymptotic and average linking numbers
for a vector ﬁeld and a measured foliation. For a ﬁeld ξ on M denote by ΓT (x) a
GEOMETRY OF HIGHER HELICITIES
1001
closed curve consisting of the long segment (for time 0 ≤t ≤T) of the ξ-trajectory
gt
ξx starting at x ∈M and of a short closing path (e. g., geodesic).
Deﬁnition 4.2. An asymptotic linking lkξ(x, F) of the trajectory of a vector ﬁeld
ξ emanating from a point x ∈M with the measured foliation F is the time-average
of the linking number of the curve ΓT (x) with F:
lkξ(x, F) = lim
T →∞
1
T lk(ΓT (x), F).
The average linking number of the vector ﬁeld ξ and the measured foliation F
on the manifold M equipped with the volume form µ is
lkξ(F) =
Z
M
lkξ(x, F)µ.
Deﬁnition 4.3. The cross-helicity of a vector ﬁeld ξ and a codimension 2 foliation
F with transverse holonomy-invariant measure β is
H(ξ, F) :=
Z
M
β ∧d−1(iξµ),
cf. the 3D case (2).
Theorem 4.4 [16], [17]. Let ξ be a divergence-free vector ﬁeld on M with a volume
form µ, and F a foliation of codimension 2 with a transverse holonomy-invariant
measure β. Then the average linking number of the vector ﬁeld ξ with the foliation
F is equal to the cross-helicity of ξ and F:
lkξ(F) = H(ξ, F).
Proof.
lkξ(F) =
Z
M
lkξ(x, F) µ =
Z
M

lim
T →∞
1
T lk(ΓT (x), F)

µ
=
Z
M

lim
T →∞
1
T lk(g[0,T ]
x
, F)

µ =
Z
M

lim
T →∞
1
T
Z
g[0,T ]
x
d−1β

µ
=
Z
M
"
lim
T →∞
1
T
Z T
0
iξ(d−1β)dt
#
µ.
The latter integrand is the time average of the function iξ(d−1β). By the Birkhoﬀ
ergodic theorem applied to the µ-preserving ﬂow of the ﬁeld ξ, the time average is
equal to the space average of the same function:
Z
M
iξ(d−1β) µ =
Z
M
d−1β ∧iξµ =
Z
M
β ∧d−1(iξµ) = H(ξ, F).
On the way, we replaced the integral over a closed curve ΓT (x) by the integral over
a non-closed piece of trajectory g[0,T ]
x
. Indeed, the diﬀerence of the two integrals is
the integral of an L1 1-form d−1β over the short path (a shortest geodesic) from
x to the other endpoint of g[0,T ]
x
. It is uniformly bounded by the product of the
diameter of M and the norm of d−1β (note that d−1 is a compact operator). Hence
it can be neglected after division by T and considering the limit T →∞.
□
1002
B. KHESIN
Remark 4.5. Note that the proof of Arnold’s theorem 2.5 is achieved similarly
by applying the Birkhoﬀergodic theorem to the ﬁeld ξ × ξ on M × M, and using
the short path properties (Section 3.4). For more details on the case of a general
transverse holonomy-invariant measure we refer to [17].
