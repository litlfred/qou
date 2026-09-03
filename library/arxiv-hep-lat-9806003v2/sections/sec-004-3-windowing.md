---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-004-3-windowing
section_title: "Windowing"
section_number: 3
pages: 5-6
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 8 sections: INTRODUCTION; COMPLETE DIRAC SPECTRA IN SU(2) GA; DATA ANALYSIS"
---
Ideally, an unfolding procedure should only remove the global variations of the spectral density, i.e. in our case the
overall behavior seen in Fig. 1. For reasons which will become clearer later, it is diﬃcult to numerically distinguish
the global variations from the local ﬂuctuations. This is in particular the case for data of large lattice size. In other
words, we might have removed too much by some of the unfolding procedures, while we might have removed too little
by others. This will be discussed in great detail below, especially in Sec. III E.
One has to ensure that any deviations seen in the spectral statistics are not due to global variations in the average
density which were not removed adequately. One way is to use diﬀerent unfolding approaches and compare the results
carefully. Another way is to take only a small window of the spectra in which the global variation of the density is
expected to be small. Thus we choose an interval [λ, λ + δλ] and calculate the ensemble averaged mean level spacing
D for it. We then rescale the eigenvalues in this interval as
ξi = λi/D
,
λ < λi < λ + δλ .
(13)
This is done in the same manner as in [8] where the microscopic region was considered. However, it is not clear
beforehand that a scale in the spectra, if any, does not exceed the interval length δλ. Unfolding, if done correctly,
allows to make investigations to much larger scales.
This approach is closely related to ensemble unfolding deﬁned above. Indeed, the results coincide, but with a less
statistical signiﬁcance by only rescaling. By using this approach, we intended to avoid any unfolding procedures. As
we will see later, there are a slight, but still systematic variations of the spectral density within the small window.
B. Nearest Neighbor Spacing Distribution
The nearest neighbor spacing distribution P(s) probes the ﬂuctuations on short scales in the spectra. It is the
probability of ﬁnding the distance s between adjacent level on the unfolded scale. It contains all correlations of order
k ≥2. In the case of completely uncorrelated levels which is referred to as Poisson regularity [1], it is given by
P(s) = exp(−s). In the case of GSE type correlations, Wigner surmized the shape
P(s) = 262144
729π3 s4 exp

−64
9π s2

,
(14)
5
which is very close to the exact GSE result. As shown in Fig. 4, the data is in perfect agreement with the prediction.
This is as well true for the large lattice, V = 164 (left part), as for the small lattice, V = 44 (right part). The
spacing distribution of the intermediate lattice sizes are not distinguishable from the both shown. We have complete
agreement between theory and lattice data for any choice of lattice size and coupling constant.
