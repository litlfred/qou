---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-007-23-realization-in-terms-of-counting-solutions-of
section_title: "Realization in terms of counting solutions of diﬀerential equations"
section_number: 2.3
pages: 14-16
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
In the previous section we deﬁned homological invariants of 3-manifolds Ha[M3] as Hilbert
spaces of 6d (2,0) theory on M3×D2× R where R is the time direction. It is possible to
give another deﬁnition that, in a sense, is closer to the deﬁnition of instanton [2] or monopole
(Seiberg-Witten) Floer homology of 3-manifolds [1] familiar to many topologists. We will
mostly follow [18], where the detailed discussion can be found.
Let us represent D2 as a cigar ﬁbered over R+ with ﬁbers being the orbits of the U(1)
action rotating the disc (see Figure 2).13 The tip of the cigar is a degenerate ﬁber projected
to the origin of R+. The 6d (2,0) theory corresponding to the Lie algebra Lg := Lie(LG) on
M3×D2× R then can be eﬀectively described as 5d maximally supersymmetric Yang-Mills
theory with gauge group LG on M3× R+× R, topologically twisted along M3. One can
further reduce it to the 2d N = (2, 2) LG theory on R+× R with the target space being the
space of LGC ﬂat connections modulo gauge transformations and the superpotential being the
holomorphic Chern-Simons functional CS(A) whereA = (Aµ+iφµ)dxµ is theLGC connection
1-form [32]. The imaginary part φµ originates from three (out of ﬁve) adjoint scalar ﬁelds in
5d theory that transform as a vector underSO(3)R⊂SO(5)R R-symmetry group and become
a one-form on M3 after topological twisting [33,34]. The boundary condition at the origin of
R+ (the image of the cigar under projection) is a Nahm-pole type boundary condition that
requires a certain singular behavior ofφµ, which in local coordinates takes the following form:
φµ =
∑3
i=1ei
µti
y +..., y → 0 (2.23)
where ei
µ is the vierbein for some choice of metric on M3, ti are the images of the standard
generators of su(2) under a principal embedding su(2)→ Lg,14 andy is the coordinate along
R+. The real part of the LGC connection obeys the Dirichlet boundary condition that ﬁxes it
at y = 0 to be equal to the spin-connection on M3 via the principal embedding su(2)→ Lg.
There is also a choice of boundary condition at the inﬁnite end of R+ that corresponds
to the choice of the boundary condition at the boundary of the disk. As in any 2d N = (2, 2)
13Exchanging the circle ﬁber of D2 with S1 in ( 2.16) has the eﬀect of replacing the group G with its
GNO/Langlands dual LG.
14For LG =SU (N) (or U(N)) the principal embedding is such that fundamental representation of SU (N)
restricts to an irreducible N-dimensional representation of SU (2).
– 13 –
Landau-Ginzburg model, there is a natural family of boundary conditions labeled by con-
nected components of the critical points of the superpotential [35]. They are given by La-
grangian branes supported on Lefschetz thimbles associated to those connected components.
The BPS Hilbert space Ha[M3] labeled by the connected component
a∈π0Mﬂat(M3,LGC) (2.24)
then can be constructed as a Floer homology as follows. As usual, classically the BPS states
of the 2dN = (2, 2) Landau-Ginzburg model on R+× R, where R is the time direction, are
given by solutions of time-independent BPS equations, that is gradient ﬂows with respect
to CS functional on R+ with speciﬁed boundary conditions. On the quantum level the BPS
Hilbert space is given by the cohomology of Morse-Witten complex of such classical BPS
states graded by the Morse index. The diﬀerential is given in terms of counting solutions
of BPS equations interpolating between two time-independent solutions at ±∞ in the time
direction. Such diﬀerential equations, when written in terms of 5d theory on M3× R× R+
are often referred as Haydys-Witten equations [18, 36]. The Hilbert space Ha[M3] has two
gradings. One is the usual Morse-index/R-charge/homological grading. The other grading,
corresponding to the generating variable q in the index ˆZa(q) = TrHa[M3](−1)RqL0, is given
by the instanton number
L0 = 1
32π2
∫
R+×M3
TrF∧F− CSgrav ∈ Z + Re CS(a). (2.25)
Here CSgrav is the action of the gravitational CS on M3, which, taking into the account the
boundary condition at the origin of R+, makes the instanton number well deﬁned. Note
that this, at least naively, deﬁnesHa[M3] for connected components of all ﬂat connections.15
However, in the previous sections, when discussing categoriﬁcation of WRT invariant, we used
only a subset of spaces Ha[M3] labeled by connected components of abelian ﬂat connections.
The deep reasoning for this phenomenon is yet to be understood, but resurgence theory
provides some explanation on the decategoriﬁed level at least for some class of 3-manifolds [22].
The deﬁnition ofHa[M3] given in this section, although quite explicit, is still on the phys-
ical level of rigor, and in order to make it mathematically accurate one still has to overcome
various problems, such as singularities and compactness of the corresponding moduli spaces.
When moduli spaces are not compact, one needs either to ﬁnd a suitable compactiﬁcation
(which, in the present context, does not spoil topological invariance) or supplement the stan-
dard Morse-Floer theory with more powerful tools. Indeed, even at the decategoriﬁed level,
the “counting” of solutions requires integration over moduli spaces and, even if all problems
are solved, may not produce integers. A familiar example is the calculation of Gromov-Witten
15On a closer look, though, there is a signiﬁcant diﬀerence between solutions with abelian and non-abelian
ﬂat connections at y = +∞. When the ﬂat connection is irreducible, the y-component of the adjoint-valued
Higgs ﬁeld φy vanishes and remains zero for all values of y, while it is not the case when the ﬂat connection
at y = +∞ is reducible.
– 14 –
invariants via integration over the moduli spaces of stable maps, where maps with non-trivial
stabilizers lead to rational rather than integer invariants.
The present problem, however, is much more challenging than compactness issues that
one encounters in Gromov-Witten or Donaldson-Witten theory. One standard tool that
replaces Morse theory in the non-compact setting is the Conley index. While its application
to the current problem will be discussed elsewhere, here we can make a few brief comments
that resonate with the rest of the present paper. The moduli spaces in question, M(M3,B),
depend on the choice of a 3-manifoldM3 and the boundary conditionB aty = +∞. A generic
choice of the boundary condition, of course, will not result in integer invariants (even at the
decategoriﬁed level) and only particular choices of boundary conditions will lead to moduli
spaces where one might hope to address compactness issue without destroying integrality
and topological invariance. Our present study suggests that boundary conditions labeled by
abelian ﬂat connections are precisely the ones which have this property.
Another issue is that counting the number of solutions of such diﬀerential equations,
even if properly deﬁned, is computationally very hard. Therefore one should explore other
possibilities to mathematically deﬁne Ha[M3].
