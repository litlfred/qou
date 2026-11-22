---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-020-521-brief-introduction-to-lattice-qcd
section_title: "BRIEF INTRODUCTION TO LATTICE QCD"
section_number: 5.2.1
pages: 32-33
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
BRIEF INTRODUCTION TO LATTICE QCD
QCD is a renormalizable quantum ﬁeld theory that must be regularized. This
can be done by formulating the theory on a discrete lattice with lattice spacing a
[139]. The largest momentum is then π/a. The quark ﬁelds live on the sites and
the gauge ﬁelds on the links of the lattice. If the lattice is ﬁnite, one can simulate
the theory on a computer. This can be done eﬃciently only in Euclidean space,
where the gluonic weight function is exp(−SYM) with SYM real. The discretized
form of the Yang-Mills action SYM is the Wilson action SW. The full weight
function of QCD also contains the fermion determinants, which can be expressed
in terms of the gauge ﬁelds. Observables are computed by generating gauge ﬁeld
conﬁgurations in a Monte Carlo update procedure and averaging an observable
over many conﬁgurations. Since the inclusion of the fermion determinants is very
time consuming, it is common to use only the gluonic part of the weight function
in the Monte Carlo updates. This is called the quenched approximation, which
corresponds to the limit Nf = 0 or, equivalently, to the limit of inﬁnitely heavy
sea quarks. To make contact with continuum physics, the results of lattice sim-
ulations must be extrapolated to inﬁnite lattice size (the thermodynamic limit)
and to zero lattice spacing (the continuum limit).
Lattice simulations are the main source of nonperturbative information about
QCD. Unfortunately, the naive discretization of fermions on a lattice leads to the
so-called doubling problem: The quark propagator has poles at each corner of
Random Matrix Theory and Chiral Symmetry in QCD
33
the Brillouin zone, which gives rise to a total of 2d species in d dimensions. The
unwanted 2d −1 species can be eliminated by adding to the Dirac operator an
additional term, the Wilson term, which removes the doublers in the continuum
limit. However, this term breaks chiral symmetry explicitly. Another possibility
is the use of staggered (or Kogut-Susskind) fermions where one has only one
spinor component per lattice site.
This maintains a residual chiral symmetry
but only partially reduces the number of species to 2d/2 in the a →0 limit.
A no-go theorem by Nielsen and Ninomiya [140] states that it is not possible
simultaneously to solve the doubling problem and have exact chiral symmetry on
the lattice with a local action.
Fortunately, there is a way around this theorem: the remnant chiral symmetry
condition of Ginsparg and Wilson [141],
Dγ5 + γ5D = 2aDγ5RD ,
(99)
where R is a spatially local operator that is trivial in Dirac space. In contrast to
{D, γ5} = 0, chiral symmetry is not exact but is recovered only in the continuum
limit a →0. Thus, with Dirac operators satisfying Eq. (99), it is possible to get
rid of the doublers even at ﬁnite lattice spacing without violating the Nielsen-
Ninomiya theorem. Recently, several solutions of Eq. (99) have been found in the
overlap formalism [142], in the domain-wall formulation in ﬁve dimensions [143],
and in the perfect action approach [144].
As mentioned in Sec. 2.2.3, there may be cases in which the anti-unitary sym-
metries of the various lattice discretizations of the Dirac operator diﬀer from those
of the continuum operator. In particular, this is true for staggered fermions. In
SU(2) color, staggered fermions are in the symmetry class of the chSE, whereas
continuum fermions are in the chOE symmetry class. Staggered fermions in the
adjoint representation of the gauge group (for any Nc) have the symmetries of the
chOE, whereas in the continuum limit the symmetries are those of the chSE. The
Wilson Dirac operator DW does not anticommute with γ5 and is therefore not de-
scribed by any of the chiral ensembles. However, the Hermitian operator γ5DW
has the same anti-unitary symmetries as the continuum Dirac operator and is
described by the corresponding nonchiral ensembles (see also Ref. [145]). Finally,
Dirac operators obeying the Ginsparg-Wilson condition, Eq. (99), have the same
anti-unitary symmetries as the continuum Dirac operator, but the eigenvalues
are located on the complex unit circle [62].
