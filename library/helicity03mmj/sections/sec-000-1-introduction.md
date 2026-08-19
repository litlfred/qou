---
doc_id: helicity03mmj
doc_title: "MOSCOW MA THEMA TICAL JOURNAL"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
doc_brief: "MOSCOW MATHEMATICAL JOURNAL — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
The helicity of a vector ﬁeld in a three-dimensional space can be thought of as
a real-valued version of the integral-valued Hopf invariant for a continuous map
S3 → S2. The latter has two well-known deﬁnitions: topological or analytic ones.
Topologically, the Hopf invariant of a map S3 → S2 is deﬁned as the linking number
in S3 of the curves which are preimages of two arbitrary generic points in S2.
Alternatively, the Hopf invariant can be deﬁned as the integral∫
S3
ω ∧ d−1ω,
where a 2-form ω is the pullback to S3 of any area form on S2, normalized by the
condition that the area of S2 equals 1. The equivalence of these two deﬁnitions is
a manifestation of the Poincare duality.
The integral above can serve as a deﬁnition of an invariant for any exact 2-form
ω on S3 [1]. This invariant is called the helicity or asymptotic Hopf invariant of
the form ω (or of the corresponding divergence-free vector ﬁeld, in the presence of a
volume form). It is invariant with respect to (volume-preserving) diﬀeomorphisms
of S3 and it is independent of the choice of a primitive d−1ω.
The asymptotic Hopf invariant is not necessarily an integer, if ω does not come
from a map of S3 to S2, as well as there is no straightforward analog of the homotopy
Received April 4, 2003.
Supported in part by the ESI, PREA, and NSERC research grants.
c©2003 Independent University of Moscow
989
990 B. KHESIN
invariance of the Hopf invariance for map after this generalization. However, its
importance is related to the fact that helicity of the vorticity ﬁeld curl v is invariant
as a divergence-free ﬁeld v evolves according to the Euler equation for an ideal 3D
ﬂuid
∂tv + (v · ∇)v = −∇p.
In such a ﬂow the ﬁeld ξ = curl v satisﬁes the equation of “frozenness” in the ideal
ﬂuid: ∂tξ = {v, ξ }, i. e., it is transported by domain diﬀeomorphisms. Similarly, in
the setting of magnetohydrodynamics, the magnetic ﬁeld B in a perfectly conduct-
ing medium is transported by the medium ﬂow: ∂tB = {v, B }, which implies the
preservation of its helicity.
In [ 1] Arnold showed that for an arbitrary exact 2-form ω its helicity integral
is equal to the asymptotic linking number of the trajectories of the divergence-free
vector ﬁeld naturally associated with this form (in the presence of a ﬁxed volume
form on S3).
This elegant result prompted numerous generalizations in the recent literature.
In this paper we relate to each other some of these new directions. In particular,
we give a Brownian ergodic description of higher helicities, inspired in part by the
paper [ 22] on Novikov’s invariants. We also survey various related results, mostly
concentrating on the new developments. A review and guide to the preceding
literature, as well as various tools and other details not covered in this paper, can
be found in [ 2], [ 20].
One of motivations for this paper was the recent discovery of the impact of
topological invariants of ﬂuid ﬂows on the characteristics of developed turbulence,
see [ 6]. One can hope that a better understanding of the topological nature of
ideal ﬂows could explain the meaning and give more precise corrections to the
Kolmogorov exponents for correlators of the velocity ﬁeld of a turbulent ﬂow.
The topics covered in this note include a survey of the energy estimates for vector
ﬁelds in the three-dimensional case by means of helicity and asymptotic crossing
number [9], the modiﬁcation of the latter for a solid torus and an ergodic meaning
of Calabi invariant [ 10], [ 12], as well as the short path problem [ 25]. For higher
dimensions we discuss the linking of a vector ﬁeld with a foliation with transverse
invariant measure [ 16], [ 17], the mutual linking of several foliation with transverse
invariant measures, as well as an interpretation of the Hopf and Novikov invariants
[21], [ 16], [ 22] by means of the Brownian ergodic theorem for foliations [ 13].
