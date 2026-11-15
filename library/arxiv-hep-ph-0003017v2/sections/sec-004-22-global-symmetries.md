---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-004-22-global-symmetries
section_title: "Global Symmetries"
section_number: 2.2
pages: 15-16
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
In the spirit of the invariant
random matrix ensembles, we construct a model with eigenfunctions distributed
uniformly over the unitary unit sphere. This is achieved by choosing Gaussian-
distributed random matrix elements. We thus arrive at the following chRMT
[20, 24]:
Zβ
Nf ,ν(m1, . . . , mNf ) =
Z
DW
Nf
Y
f=1
det(D + mf)e−Nβ
4 Tr v(W †W ) ,
(28)
where β is the Dyson index,
D =

0
iW
iW †
0

,
(29)
and W is an n × m matrix with ν = m −n and N = n + m. The interpretation
of this model is that N low-lying modes interact via a random interaction. A
natural representation of this model is in the form of gauge ﬁeld conﬁgurations
given by a liquid of instantons. Then the low-lying modes are the zero modes
of each instanton. We assume that ν does not exceed
√
N so that, to a good
approximation, n = N/2 for large N. The parameter N is identiﬁed as the di-
mensionless volume of spacetime. For the formulation of this model with explicit
factors of N/V included, see Ref. [31]. The potential v is deﬁned by
v(φ) =
X
k≥1
akφk .
(30)
16
J.J.M. Verbaarschot and T. Wettig
The simplest case is the Gaussian case, where v(φ) = Σ2φ. It can be shown (see
Sec. 3.5) that the microscopic spectral density does not depend on the higher-
order terms in this potential provided that the average spectral density near zero
remains nonzero. The matrix elements of W are either real [β = 1, chiral Gaus-
sian Orthogonal Ensemble (chGOE)], complex [β = 2, chiral Gaussian Unitary
Ensemble (chGUE)], or quaternion real [β = 4, chiral Gaussian Symplectic En-
semble (chGSE)]. In the latter case, the eigenvalues of D are doubly degenerate,
and the use of Majorana fermions is implemented by replacing the determinant
by its square root. For a non-Gaussian potential v(φ), we will omit the G in the
abbreviations and use chOE, chUE, and chSE, respectively. Two earlier attempts
to describe QCD Dirac eigenvalues used the Wigner-Dyson ensembles instead of
the above chiral ensembles [32].
This model reproduces the following symmetries of the QCD partition function:
• The UA(1) symmetry. All eigenvalues of the random matrix Dirac operator
occur in pairs ±iλn or are zero.
• The topological structure of the QCD partition function. The Dirac matrix
has exactly |ν| = |n −m| zero eigenvalues. This identiﬁes ν as the topological
sector of the model.
• The ﬂavor symmetry, which is the same as in QCD. For β = 2 it is SU(Nf) ×
SU(Nf), for β = 1 it is SU(2Nf), and for β = 4 it is SU(Nf) (each Majorana
ﬂavor counts as 1/2 Dirac ﬂavor).
• The chiral symmetry, which is broken spontaneously with a chiral condensate
given by
Σ = lim
N→∞πρ(0)/N .
(31)
(N is interpreted as the dimensionless volume of spacetime.) The symmetry-
breaking pattern is [25] SU(Nf) × SU(Nf) →SU(Nf), SU(2Nf) →Sp(2Nf),
and SU(Nf) →O(Nf) for β = 2, 1, and 4, respectively — the same as in QCD
[22].
