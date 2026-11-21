---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
Introduction
The application of random matrix theory (RMT) to Quantum Chromodynamics (QCD) ﬁrst intro-
duced in [1] has become much more sophisticated in the recent past. Starting from a Gaussian RMT
with Nf massless ﬂavours [1, 2], the so-called chiral Gaussian unitary ensemble (chGUE), several
milestones have been taken from which we mention only a few, see [3] for recent reviews and more ref-
erences. After the universality of the microscopic origin limit for non-Gaussian RMT was understood
[4], the computation of unquenched density correlation functions of the QCD Dirac operator with
non-vanishing quark masses followed [5, 6], as well as the computation of individual Dirac eigenvalues
[6, 7, 8, 9]. It was understood [10] that the RMT approach is in one to one correspondence to the
epsilon regime of chiral perturbation theory (chPT) [11] as a limiting theory of low-energy QCD. Cor-
rections to this regime were computed by including ﬁnite volume corrections to the chiral condensate
Σ [11], or to the Pion decay constant F [12] (see [13] and[14] for recent discussions). However, the
latter only appears in RMT when extending it to a two-matrix model, by coupling to a real [15] or
imaginary chemical potential [16, 17]. Otherwise meson correlation functions have to be considered
in chPT to be sensitive to F, by coupling to the non-zero momentum modes of the Pions. Most
of the RMT predictions have been checked using Lattice QCD, ranging from checks of the topology
dependence of algorithms with good chiral properties on small Lattices [18], up to fully unquenched
two-ﬂavour simulations leading to realistic values of Σ and F [19], to where we refer as well as to [3]
for more references.
Very recently a further extension of RMT for QCD has been proposed in [20] in order to include
also the eﬀect of ﬁnite lattice spacing a close to the continuum. The corresponding RMT is again a
two-matrix model, as it was discussed in more detail in [21]. It is the aim of this paper to investigate
this RMT further - in fact in a slightly modiﬁed version - and to show its integrability by computing
all density correlation functions.
The corresponding framework in continuum eﬀective ﬁeld theory is Wilson chiral perturbation
theory (WchPT), see [22] for introductory lectures and references. Here, in addition to Σ and F three
further low energy constants W6,7,8 appear to leading order in the inﬁnite volume limit, that have to
be determined non-perturbatively. The spectral properties of the Wilson Dirac operator were put into
focus in [23], and the epsilon regime in WchPT was ﬁrst analysed in [24]. The computation of the
quenched spectral density in the epsilon regime - both for the Hermitian Wilson Dirac operator as well
as for the real eigenvalues of the non-Hermitian Wilson Dirac operator - was performed in [20] (see also
[25] for more recent results in the p-regime). The presentation in [20, 21] was in fact solely based on
the WchPT Lagrangian and corresponding generating resolvents, and not on an RMT computation,
although the two become equivalent in the microscopic limit once the graded or supersymmetric
approach is taken. The extension to the Nf = 1 [26] and to Nf > 1 [27] ﬂavoured spectral densities
followed also the supersymmetric approach.
Our aim is to partly extend these results and to compute all spectral densities from RMT. The
advantage of the approach presented here using skew-orthogonal polynomials is that an explicit eigen-
value basis can be found for the Hermitian Wilson Dirac operator. All spectral correlations then follow
both for ﬁnite- and large-N, where N = 2n + ν is the size of the matrices, given the corresponding
skew-orthogonal polynomials can be constructed. We have succeeded in this program in the quenched
approximation and for ν = 0, 1 as a ﬁrst step, where ν counts the number of exact zero-modes at
a = 0. We will come back to the open challenges left to our RMT approach in the conclusions.
Our investigations presented here have a second motivation. So-called parametric density correla-
tions have been studied in the RMT literature for several decades. The reason of interest is that the
classical Wigner-Dyson ensembles, the Gaussian unitary, orthogonal and symplectic ensemble (GUE,
GOE and GSE, respectively) correspond to Hamiltonian systems without (GUE) or with time-reversal
symmetry (GOE or GSE, depending on the spin). For that reason the symmetry breaking has been
studied in terms of a two-matrix model that interpolates between two classes, see [28] for the classical
papers, or chapter 14 in [29] for a more comprehensive presentation of the GUE-GOE and GUE-GSE
transition. Several such transitions have been studied since, including the chiral versions of these
transitions [30].
A crucial step is to be able to perform the angular integrations in the term coupling the two
random matrices. This is done using the Harish-Chandra-Itzykson-Zuber (HCIZ) integral [31] and
explains, why in all given examples (at least) one of the two classes has to possess unitary symmetry.
Once an eigenvalue basis is determined the standard (skew)-orthogonal polynomial approach can be
taken, where in [32] a more general framework for general, non-Gaussian weight functions has been
developed.
These two-matrix models also called transitive ensembles include also transitions within the same
symmetry class, that is from the GUE to GUE or chGUE to chGUE, see e.g. [17] including their
extensions with Nf ﬂavours, in the context of QCD with imaginary isospin chemical potential in three
and four dimensions. As we will show below the RMT corresponding to WchPT in the epsilon regime
in [20, 21] corresponds (after a minor extension) to the symmetry transition from the chGUE to the
GUE. Our paper thus serves also to close a gap within RMT by studying this transition class. Because
of the ubiquity of RMT we expect that applications in totally diﬀerent areas may follow.
The presentation of the remaining chapters is organised as follows. In section 2 we present our
two-matrix model, show its relation to WchPT in the epsilon regime (see also appendix A for details)
and discuss the relation to the RMT proposed in [20, 21]. In section 3 we derive the joint probability
density function for the Hermitian Wilson Dirac operator for a general Nf-ﬂavour content and general
ν ≥0. The solution of our two-matrix model for all density correlation functions is presented in section
4 in terms of skew-orthogonal polynomials for Nf = 0 and ν = 0, 1, see also appendix C for further
details. These are given in terms of Gaussian integral transforms of standard Laguerre polynomials
as they appear in the chGUE [1]. The microscopic large-N limit at the origin close to the chGUE is
then presented in section 5 illustrated with several examples, before we present our conclusions and
open problems in section 6.
