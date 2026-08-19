---
doc_id: arxiv-2208.14188v2
doc_title: "Prepared for submission to JHEP KIAS-P22064 Resurgence in complex Chern-Simons theory at generic levels Zhihao Duana Jie Gub aKorea Institute for Advanced Study 85 Hoegiro, Dongdae"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels Zhihao Duana Jie Gub aKorea Institute for Advanced Study 85 Hoegiro, Dongdaemun-gu, Seoul 02455, Korea bSchool of Phyiscs and Shing-Tung Yau"
---
2 Resurgent structure of complex Chern-Simons theory at generic level 3
2.1 Perturbative complex Chern-Simons theory at generic level 3
2.2 Resurgent structure of complex Chern-Simons theory 9
2.3 Stokes constants and BPS invariants 14
3 Figure eight 15
3.1 Asymptotic series 15
3.2 Holomorphic blocks 18
3.3 Resurgent structure 20
4 Three twists 23
4.1 Asymptotic series 23
4.2 Holomorphic blocks 29
4.3 Resurgent structure 31
5 Conclusion and discussion 33
A Tetrahedron partition function at level k 37
A.1 Fundamental properties 38
A.2 Zeros and poles 38
A.3 Integral identities 39
A.4 Semi-classical limit 39
B Power series of state integrals at diﬀerent levels 39
B.1 Knot 41 39
B.2 Knot 52 41
1 Introduction
Complex Chern-Simons theory remains an active ﬁeld of research that links up many ﬁelds
in both physics and mathematics. From the physics side, sl(2, C) Chern-Simons theory
was ﬁrst considered in [1] as a means to describe three dimensional quantum gravity on
Lorentzian spacetime with positive cosmological constant. Later a beautiful connection
was revealed between sl(N, C) Chern-Simons theory and 3d N = 2 superconformal ﬁeld
theories by the name of the 3d-3d correspondence [2–5] (see [6] for a review), which was
used to deﬁne a large class of 3d SCFTs. Conversely, the BPS sector of the dual 3d SCFT
was used in [7, 8] to deﬁne homological invariants ˆZ for the three manifold.
– 1 –
From the mathematical side, complex Chern-Simons theory plays an important role
in quantum topology. It was found by Witten long time ago [9] that Jones polynomials
of knots, which are Laurent polynomials in q, are vacuum expectation values of Wilson
loops along the knot in SU (2) Chern-Simons theory with q = exp(2πi/(k + 2)), wherek is
the discrete level. It is then natural to consider more general complex values of q, which
translates to the complexiﬁcation of the gauge group [10]. The complex Chern-Simons
theory then provides a new topological invariant for 3d manifolds.
For instance, when M is a knot complement, the partition function of the sl(2, C)
Chern-Simons theory on M is generally believed to reduce to a ﬁnite-dimensional integral
called the state integral, as proposed in [11–15] based on [16, 17], which is constructed based
on an ideal triangulation of the manifold. The saddle points of the state integral in the
weak coupling limit are non-Abeliansl(2, C) ﬂat connections on the three manifold [9], and
the associated asymptotic series ϕ(σj) (j≥ 1) can be obtained by Gaussian expansion [17].
The state integral and thus the asymptotic series are believed to be topological invariants
as they do not change with a diﬀerent triangulation scheme.
On the other hand, the state integral model has the disadvantage that it is incomplete
in the sense that it misses the information of Abelian ﬂat connections [18]. Instead, the
asymptotic series ϕ(σ0)(τ) associated to the Abelian ﬂat connection σ0 can be determined
from the colored Jones polynomials of the knot expanded in terms of h = logq [19–22].
It is natural to study the resurgent structure of these asymptotic series. On the one
hand, complex Chern-Simon theory is a special quantum ﬁeld theory with no renormalons,
and therefore these asymptotic series of saddle points must transform to each other by
Stokes automorphism, forming a so-called resurgent structure. On the other hand, the
resurgence theory tells us that the Stokes constants that control all the Stokes automor-
phisms deﬁne necessarily new invariants which are non-perturbative in nature. The resur-
gence problem in Chern-Simons theory was ﬁrst considered in [23], where it was found
(and later emphasized again in [24]) that the Borel transform of ϕ(σ0)(τ) has poles at
Vol(M) + iCS(M) + 4π2Zi, which can be interpreted as a resurgent formulation of the
Volume Conjecture [25, 26]. Later the resurgent problems of the series ϕ(σj)(τ) (j⁄= 0) for
non-Abelian saddle points were considered in [27–29]. See also [30] on related results on
Faddeev’s quantum dilogarithm which is a crucial ingredient of state integrals.
Recently the resurgent problem for the sl(2, C) Chern-Simons theory at level k = 1 on
the complement of the two simplest hyperbolic knots 41 and 52 were completely solved in
[24, 31, 32]. It was demonstrated that ϕ(σ0)(τ) of the Abelian ﬂat connection is related to
ϕ(σj)(τ) (j⁄= 0) of non-Abelian ﬂat connections by Stokes automoprhisms but not the other
way around, while ϕ(σj)(τ) (j⁄= 0) transform to themselves. The Stokes constants of all
these Stokes automorphisms were computed explicitly. Surprisingly the Stokes constants
relating ϕ(σj)(τ) (j⁄= 0) were found to coincide with the BPS invariants in the dual 3d
N = 2 superconformal ﬁeld theory on S1 [31, 32], providing another interesting entry of
dictionary in the 3d-3d correspondence. Furthermore, Stokes automorphisms were used to
construct a new state integral for the knot 41, which now includes the contribution of the
Abelian ﬂat connection as well [24]. Finally, the statement that the series ϕ(σ0)(τ) Borel
resums to the ˆZ invariant [33] was corrected to include additional contributions from Borel
– 2 –
resummation of ϕ(σj)(τ) [24].
In this work we continue this line of research, and generalise the results of [31, 32] to
sl(2, C) Chern-Simons theories with levels k≥ 1 with small boundary holonomy deforma-
tion x. We ﬁrst demonstrate that the asymptotic series ϕ(k,σj)(x;τ) (j≥ 1) associated to
non-Abelian ﬂat connections are such that their coeﬃcients always live in the trace ﬁeld
of the knot extended by the holonomy parameter x. We then show that these asymptotic
series enjoy universal resurgent structures: Both the distribution of Borel plane singular-
ities and the associated Stokes constants are independent of the level k, despite that the
asymptotic series themselves depend highly non-trivally on the level.
The remainder of the paper is structured as follows. We summarise our results, both
on the properties of the asymptotic series and their resurgent structure in section 2. We
then give details in two example sections 3,4. Finally we conclude and list open questions
in section 5.
