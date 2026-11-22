---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-021-522-bulk-correlations
section_title: "BULK CORRELATIONS"
section_number: 5.2.2
pages: 33-34
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
BULK CORRELATIONS
To measure the bulk spectral correlations, one needs all eigenvalues of the Dirac
operator, which is represented on the lattice by a ﬁnite sparse matrix whose
dimension is proportional to the lattice volume and to Nc. The eigenvalues of
such a matrix can be obtained using special algorithms, e.g. by the Cullum-
Willoughby version of the Lanczos algorithm [146]. On the lattice, this was ﬁrst
done by Kalkreuter [147]. The numerical eﬀort of this method scales with the
square of the matrix dimension.
For example, in SU(3) on a 104 lattice, the
Dirac matrix has 15,000 distinct positive eigenvalues, which can be computed
on a typical workstation in about 40 minutes. There are exact sum rules for
the sum of the squares of all Dirac eigenvalues, which can be used to check the
numerical accuracy. Because the number of eigenvalues per conﬁguration is very
large and because the ensemble average can be replaced by a spectral average
34
J.J.M. Verbaarschot and T. Wettig
Figure 3: Number variance Σ2(n), spectral rigidity ∆3(n), and nearest-neighbor
spacing distribution P(s) of the lattice Dirac operator with gauge group SU(2).
Top: Wilson fermions, V = 83 × 12, Nf = 2.
Bottom: staggered fermions,
V = 124, Nf = 4, ma = 0.05. (From Ref. [149]. Note that in Ref. [149], the
ﬁgure of P(s) for Wilson fermions shows data points for staggered fermions. This
has been corrected in the present ﬁgure.)
under the assumption of spectral ergodicity and stationarity, one needs only a
few conﬁgurations to construct the bulk spectral correlations with great accuracy.
The bulk correlations have been measured in a number of lattice studies for
all three symmetry classes [148, 149, 150, 135, 151, 152] and in instanton liquid
simulations [137] for β = 2. As mentioned above, they are insensitive to the
number of ﬂavors and the topological charge. In all cases, excellent agreement
with the predictions of the appropriate random matrix ensemble was obtained
(see e.g. Fig. 3). The agreement is perfect not only in the strong-coupling regime
but also at weak coupling. In fact, the bulk spectral correlations are given by
RMT even in the deconﬁnement phase [150, 151], indicating that the gauge ﬁelds
retain a suﬃcient degree of randomness in this region of the phase diagram.
Spectral ergodicity was investigated in Ref. [135], and the equivalent of a Thou-
less energy was found for ensemble averaging, whereas spectral averaging resulted
in complete agreement with RMT correlations over distances as long as several
hundred average level spacings.
