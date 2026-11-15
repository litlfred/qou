---
doc_id: helicity03mmj
doc_title: "Geometry of higher helicities"
section_id: sec-001-2-what-is-helicity
section_title: "What is Helicity?"
section_number: 2
pages: 2-5
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
toc_source: outline
doc_brief: "Geometry of higher helicities — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
Let M be a simply connected three-dimensional manifold with a volume form
µ, and ξ a divergence-free vector ﬁeld on M. The divergence-free property means
that the Lie derivative of µ along ξ vanishes: Lξµ = 0, or, which is the same,
the substitution ωξ := iξµ of the ﬁeld ξ to the volume form µ, is a closed 2-form:
dωξ = 0. On a simply connected manifold M (or, even, for an M with H1(M) = 0)
the latter implies that ωξ is exact: ωξ = dα for some 1-form α, called a potential (or,
primitive) 1-form. If M has boundary, we require ξ to be tangent to the boundary.
(If H1(M)̸ = 0 for the manifold M, we conﬁne ourselves to null-homologous ﬁelds
ξ, i. e., such ﬁelds that the 2-form ωξ is exact.)
GEOMETRY OF HIGHER HELICITIES
991
In this section we always follow [1] for the deﬁnitions and results, unless otherwise
is cited.
Deﬁnition 2.1. The helicity H(ξ) of a null-homologous ﬁeld ξ on a three-dimen-
sional manifold M (possibly with boundary) equipped with a volume element µ is
the integral of the wedge product of the form ωξ := iξµ and its potential:
H(ξ) =
Z
M
ωξ ∧d−1ωξ.
An immediate consequence of this deﬁnition is the following
Theorem 2.2 [1]. The helicity H(ξ) is preserved under the action on ξ of a volume-
preserving diﬀeomorphism of M.
Indeed, the helicity H(ξ) was deﬁned without coordinates or metric.
Hence,
H(ξ) is the same for all ﬁelds that diﬀer only by a volume-preserving change of
coordinates. In this sense, helicity is a topological invariant.
The word “helicity” was coined by K. Moﬀatt in [19] and it reveals the topological
meaning of this characteristic of a vector ﬁeld (see also [20] for a historical survey).
Example 2.3. In a simply connected domain M ⊂R3 one can rewrite the helicity
of a ﬁeld ξ (tangent to the boundary of M) as follows:
H(ξ) =
Z
M
(ξ, curl−1 ξ) d3x,
where ( , ) is the Euclidean inner product, and A = curl−1 ξ is a divergence-free
vector potential of the ﬁeld ξ, i. e., ∇×A = ξ. (One can easily see that the integral
is independent of the choice of A deﬁned up to an addition of a gradient ∇f.)
For instance, consider a divergence-free ﬁeld ξ which is identically zero except
in two narrow ﬂux tubes whose axes are two linked closed curves C1 and C2. Sup-
pose that there is no net twist within each tube or, more precisely, that the ﬁeld
trajectories foliate each of the tubes into pairwise unlinked circles. Then one can
show (see [19]) that the helicity of such a ﬁeld is given by
H(ξ) = 2 lk(C1, C2) · |Flux1| · |Flux2|,
where Fluxi is the magnetic ﬂux of the ﬁeld in the ith tube and lk(C1, C2) is the
linking number of C1 and C2.
Recall, that the (Gauss) linking number lk(C1, C2) of two oriented closed curves
C1, C2 in R3 is the signed number of the intersection points of one curve with an
arbitrary (oriented) surface spanning the other curve. If the curves Ci : S1 →R3
are parameterized by parameters in [0, 2π] the linking number can be given by the
following Gauss integral:
lk(C1, C2) = 1
4π
Z 2π
0
Z 2π
0
( ˙C1(t1) × ˙C2(t2), C1(t1) −C2(t2))
|C1(t1) −C2(t2)|3
dt1 dt2.
(1)
V. Arnold proposed the following ergodic interpretation of helicity for any diver-
gence-free ﬁeld as the average linking number of the ﬁeld’s trajectories.
Let ξ be a divergence-free ﬁeld on M and {gt : M →M} its phase ﬂow. We will
associate to each pair of points in M a number that characterizes the “asymptotic
992
B. KHESIN
Γτ1(x1)
Γτ2(x2)
x1
x2
Figure 1. The long segments of the trajectories are closed by the
“short paths”
linking” of the trajectories of the ﬂow {gt} passing through these points. Given
any two points x1, x2 in M and two large numbers T1 and T2, we consider “long
segments” gtx1 (0 ≤t ≤T1) and gtx2 (0 ≤t ≤T2) of the trajectories of ξ issuing
from x1 and x2. Close up these long pieces by the shortest geodesics between gTkxk
and xk. We obtain two closed curves, ΓT1(x1) and ΓT2(x2); see Fig.1. Assume that
these curves do not intersect (which is true for almost all pairs x1, x2 and for almost
all T1, T2). Then the linking number lkξ(x1, x2; T1, T2) := lk(ΓT1(x1), ΓT2(x2)) of
the curves ΓT1(x1) and ΓT2(x2) is well-deﬁned.
Deﬁnition 2.4. The asymptotic linking number of the pair of trajectories gtx1 and
gtx2 (x1, x2 ∈M) of the ﬁeld ξ is deﬁned as the limit
λξ(x1, x2) =
lim
T1,T2→∞
lkξ(x1, x2; T1, T2)
T1 · T2
,
where T1 and T2 are to vary so that ΓT1(x1) and ΓT2(x2) do not intersect.
It turns out that this limit exists (as an element of the space L1(M × M) of
the Lebesgue-integrable functions on M × M) and is independent of the system of
geodesics (i. e., of the Riemannian metric), see Remark 2.6 below.
Theorem 2.5 [1]. Helicity of a divergence-free vector ﬁeld ξ on a simply connected
manifold M with a volume element µ is equal to the average pairwise linking of tra-
jectories of this ﬁeld, i. e., to the asymptotic linking number λξ(x1, x2) of trajectory
pairs integrated over M × M:
H(ξ) =
Z
M
Z
M
λξ(x1, x2) µ1µ2.
Remark 2.6. In the original paper [1], instead of segments of shortest geodesics,
one considered “systems of short paths” between every two points of the manifold
M.
These systems have to satisfy some conditions to provide the existence of
λξ(x1, x2) almost everywhere as a pointwise limit as T1, T2 →∞. Such a system
of “short paths” would, generally speaking, depend on a vector ﬁeld. In [25] T. Vogel
suggested to use the L1-convergence, rather than the pointwise one, and showed
that in the L1-approach it is suﬃcient to use the system of shortest geodesics for any
vector ﬁeld, see Section 3.4. His approach settled in a universal way the existence
GEOMETRY OF HIGHER HELICITIES
993
question for the short paths systems. It might also shed some light on the following
long-standing problem.
Problem 2.7 [1]. Is the helicity of a divergence-free vector ﬁeld invariant under
the action of homeomorphisms preserving the measure on the manifold?
Here,
a measure-preserving homeomorphism is supposed to transform the ﬂow of one
smooth divergence-free vector ﬁeld into the ﬂow of the other, both ﬁelds having
well-deﬁned helicities.
The above problem is a counterpart of the homotopy invariance of the classical
Hopf invariant for maps π: S3 →S2. The latter (integral-valued) invariant is also
equal to the helicity of a vector ﬁeld tangent to the levels of π (so that all orbits of
this ﬁeld are closed).
The homeomorphism invariance was proved in [10] for a ﬁeld in a solid torus
with nonzero longitude component. Note that for such a ﬁeld there is an alter-
native deﬁnition of short path systems as paths that are “no longer than half
the circumference,” which is applicable after the action of a homeomorphism as
well, see the discussion in Section 3.4. One should also mention that the class of
measure-preserving homeomorphisms that are not diﬀeomorphisms is apparently
very limited, where just few examples are known [14].
Remark 2.8. Just like the two deﬁnitions of the Hopf invariant manifest the
Poincare duality, the ergodic interpretation of the helicity-type integrals in dimen-
sion three and higher can be thought of in similar terms. The “Poincare duality”
here is as follows. Consider foliations of codimension k with transverse holonomy-
invariant measure, and the corresponding Ruelle–Sullivan currents. (If the measure
is represented by a smooth form, the kernel distribution of the form spans the
foliation leaves.)
The operations ∧and d−1 on currents (or forms) correspond,
respectively, to the intersection and “ﬁlling” of the submanifolds. The ﬁnal inte-
gration of a volume form over the ambient manifold corresponds to the total sum
of signed intersection points of submanifolds, similar to considering the deﬁnition
of linking. Thus, the invariants under consideration become properly understood
average linking numbers.
