---
doc_id: chinta-2025-j-phys-a-math-theor-58-035203
doc_title: "The discrete analogue of the Gaussian"
section_id: sec-006-6-application-3-asymptotics-by-passing-from-the
section_title: "Application 3: asymptotics by passing from the discrete to the continuous"
section_number: 6
pages: 15-16
source_pdf: Chinta_2025_J._Phys._A__Math._Theor._58_035203.pdf
source_sha256: baba83ca76c773d4
toc_source: outline
doc_brief: "The discrete analogue of the Gaussian — 13 sections: Front matter; The discrete analogue of the Gauss; Introduction"
---
Consider a discrete tori in d dimensions, or equivalently, a rectangular box in the standard
lattice Zd equipped with periodic boundary conditions, see figure 2. The question is how does
the determinant of the (finite) graph Laplacian grows as the rectangular box becomes larger.
This invariant counts the number of rooted spanning trees. (We note that arbitrary tori can also
be treated; see [CJK12].) In thermodynamics one speaks of the infinite volume limit and the
continuum limit. These are both visible in our asymptotics which extends what was known in
dimension 2 by work of Kasteleyn, Barber, Duplantier-David [Ka61, Ba70, DD88]. In short,
among the key ideas in our approach are, first, to use a discrete version of the Poisson summa-
tion formula in order to encode the spectral data of the graph in terms of discrete Gaussians,
then second, in the asymptotic analysis to relate the discrete to the continuous via proposition
1 above. The following is one of the main results from [CJK10, CJK12].
Theorem 7. ([CJK10, CJK12]) Let An be a sequence of integral d × d matrices with detAn →
∞and An/(detAn)1/d →A ∈SL(d,R). As n →∞,
logdet∆Zd/AnZd = logdet∆Zd detAn + 2
d logdetAn + logdet∆Rd/AZd + o(1).
14
J. Phys. A: Math. Theor. 58 (2025) 035203
G Chinta et al
Figure 2. Spectral asymptotics of a discretized torus as the mesh goes to zero.
In the above theorem, ∆Zd/AnZd is the Laplacian on the discrete torus; ∆Zd is the Laplacian on
the lattice Zd and ∆Rd/AZd is the Laplacian on the (continuous) torus Rd/AZd. The determinant
of the Laplacian on the discrete torus is a finite determinant, in the sense of linear algebra.
However, the determinant of the Laplacian on the continuous torus is obtained through zeta
regularization, which adds an entirely new level of complexity to the matter.
Let us briefly explain how the discrete Gaussian comes into play in this setting. Following
the usual formalism, logdet∆Zd/AnZd is related to the Mellin transform of the trace of the heat
kernel. The trace of the heat kernel is the theta function, which in our discrete setting involves
a sum of products of discrete Gaussians
dQ
j=1
e−2tInjkj(2t). A careful analysis of the asymptotics
of the discrete Gaussian is the key ingredient in the proof of theorem 7.
Theorem 7 is of interest in combinatorics, statistical physics and quantum field theory
(QFT). Several recent papers in mathematical physics, notably [HK20, IK22, Gr23], have
extended theorem 7. A problem is raised in [RV15] in connection with their approach to a
combinatorial QFT which theorem 7 addresses just a part, aside from the 2D case that was
already known as just mentioned.
We point out that in higher dimensions d > 2 the lead terms in the asymptotics of theorem 7
were established in [SW00, SS01, Ly05]; see also their bibliographies for further references.
In particular, the formula of Sokal-Starinets involves the I-Bessel function in the same way
as in [CJK10], but Sokal-Starinets have another way of interpreting the appearance of the I-
Bessel, presumably not as a discrete Gaussian. Detailed asymptotics for more general lattice
domains in 2D are obtained in the work of Kenyon, see [Ke00].
For other contexts in physics where recent similar considerations of discrete heat kernels
appear, see [KS18, KS23].
