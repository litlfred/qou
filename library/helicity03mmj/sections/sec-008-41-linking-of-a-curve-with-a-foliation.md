---
doc_id: helicity03mmj
doc_title: "Geometry of higher helicities"
section_id: sec-008-41-linking-of-a-curve-with-a-foliation
section_title: "Linking of a curve with a foliation"
section_number: 4.1
pages: 12-12
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
toc_source: outline
doc_brief: "Geometry of higher helicities — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
foliation of codimension 2 and a divergence-free vector ﬁeld is a direct generaliza-
tion of the cross-helicity, cf. [2], [16], [17]. The corresponding helicity invariants in
higher dimensions are similar to those appearing in higher-dimensional ideal hy-
drodynamics, an odd-dimensional ideal incompressible ﬂuid moving according to
the Euler equations. It should be mentioned however, that they do not seem to be
related to higher-dimensional physical problems, similar, e. g. to the helicity-energy
interaction in the MHD theory in two and three dimensions.
Let M be a closed manifold with b1(M) = 0 and equipped with a volume form µ.
Consider an oriented codimension 2 foliation F with a holonomy-invariant trans-
verse measure β. To such a foliation one can associate a current C(F): Ωn−2(M) →
R, which sends any smooth (n −2)-form θ on M to its integral against β:
C(F): θ 7→
Z
M
θ ∧β.
(The integral here can be deﬁned via a partition of unity subordinated to a folia-
tion chart for F: one integrates the summands over the leaf plaques in the charts,
and then integrates the result over transversals using the measure β.) This current
is closed and is called the Ruelle–Sullivan cycle of the invariant measure β [23].
Assume that this cycle is null-homologous: [C(F)] = 0 ∈Hn−2(M, R). (Geometri-
cally one might think of this condition that the “leaves would be boundaries if they
were compact manifolds,” cf. Remark 2.8.)
If we imagine that the measure β is represented by a smooth 2-form on M,
then necessarily this form is exact, since [C(F)] = 0. Moreover, the foliation F is
spanned by the distribution of kernels of this form: β = iFµ. In the sequel we will
be often dealing with the measure β as it were a smooth 2-form, while one has to
use the language of the Ruelle–Sullivan cycles to furnish the details, see the careful
study in [17].
Deﬁnition 4.1. The average linking of a curve Γ with the measured foliation F
is the β-measure of an arbitrary surface ∂−1Γ bounded by Γ. In other words, it is
the ﬂux of the 2-form β = iF µ through ∂−1Γ:
lk(Γ, F) =
Z
∂−1Γ
β =
Z
Γ
d−1β.
The motivation of this deﬁnition is as follows. Suppose, that we are given a mea-
sured foliation F, where the total weight is supported on a single (null-homologous)
compact leaf N of codimension 2. Then
R
Γ d−1β is equal to the linking number of
N and the curve Γ. Similarly, for a foliation with compact nonsingular ﬁbers, the
number lk(Γ, F) gives the average for the linking numbers of the curve Γ with every
ﬁber, cf. [16], [2].
