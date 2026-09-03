---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-000-i-introduction
section_title: "INTRODUCTION"
section_number: I
pages: 1-2
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 8 sections: INTRODUCTION; COMPLETE DIRAC SPECTRA IN SU(2) GA; DATA ANALYSIS"
---
It is now well established that Random Matrix Theory (RMT) accurately models spectral ﬂuctuations in an abun-
dant variety of diﬀerent systems, such as chaotic, disordered and many–body systems, see the review in Ref. [1]. In
recent years, RMT has in addition been successfully introduced into the study of certain aspects of Quantum Chro-
modynamics (QCD). The interest focuses on the spectral properties of the Euclidean Dirac operator. The eigenvalue
equation under consideration reads
i/D[A]ψk = λk[A]ψk ,
(1)
where i/D[A] = i/∂+ g/Aata is the massless Euclidean Dirac operator. The coupling constant is denoted by g and the
ta are the generators of the gauge group. The distribution of the color gauge ﬁelds /Aa is given by the Euclidean QCD
partition function. As these gauge ﬁelds vary over the ensemble of gauge ﬁeld conﬁgurations, the eigenvalues ﬂuctuate
about their average positions. The average spectral density is deﬁned as
ρ(λ) =
DX
k δ(λ −λk[A])
E
A .
(2)
The average has to be performed over all gauge ﬁeld conﬁgurations.
In contrast to most other systems, however, there are two diﬀerent regimes in QCD spectra which can be addressed
in an RMT approach, the microscopic region and the bulk region. Since the Dirac operator only couples states of
opposite chirality, the eigenvalues are pairwise positive and negative. This is the reason why two types of spectral
ﬂuctuations can be distinguished, namely spectral ﬂuctuations in the microscopic limit near zero virtuality, λ = 0,
and in the bulk of the spectrum.
Concerning the microscopic region, chiral Random Matrix Theory (chRMT) [2] incorporates the global symmetry
properties, in particular chiral symmetry, of i/D. It predicts level repulsion between positive and negative eigenvalues
which results in a distinct behavior of the eigenvalue density and correlations near the origin. It is possible to calculate
spectral correlators analytically in the microscopic limit [3–5], and to compare the predictions of chRMT with complete
spectra of the lattice QCD Dirac operator on reasonably large lattices. Indeed, remarkable agreement is found [6–10]
at the edge of the spectrum.
Suﬃciently far away from the origin, however, the repulsion of negative and positive eigenvalues should become
unimportant.
Therefore the chiral structure of the theory is not expected to be of relevance in the bulk of the
spectrum. This is the region we will address on in this work. By comparing with lattice data, it has already been
shown that conventional RMT properly models these ﬂuctuations in the bulk [11,12,10]. It is important to go beyond
these statistical analyses made so far in order to see to what scales RMT does apply. The identiﬁcation of such scales
1
gives a fundamental insight into a system. Investigations of this type have been performed in great detail in disordered
systems and in many–body systems. There, the Thouless energy Ec or the spreading width Γ determine the scale
Ec/D where D is the level spacing, in which the ﬂuctuation are of RMT type [13,14]. Beyond this scale, deviations
from the RMT behavior occur, see Ref. [1] for a detailed discussion and further references.
Recently, theoretical studies [15–17] established a link between disordered systems and QCD. The range of validity
of RMT, λRMT, was introduced as an equivalent of a Thouless energy Ec. A scaling λRMT/D ∝
√
V was proposed
where V is the four–volume of the system. Indeed, such a scaling behavior was found very recently in the microscopic
region [18] for deviation from RMT behavior. As argued in [16] a corresponding eﬀect should also be seen in the bulk
of the spectrum. This is what we will investigate.
The identiﬁcation of this scale λRMT/D in QCD spectra could lead to an improved understanding of certain features
of QCD and allows us to separate the stochastic noise of the short range ﬂuctuations from the true dynamics of the
QCD vacuum. Eventually, it could be possible to set up eﬀective models or simplify the presently used simulation
algorithms in lattice gauge theories. In this work, we search for such a universal scale λRMT/D in the bulk region by
analyzing lattice data. In contrast to the microscopic region, the bulk of the spectrum is expected to have a translation
invariant analogue of the Thouless energy. We emphasize that our analysis is self–consistent. Advantageously, it does
not depend on any model that aims at an explanation for the occurrence of this universal scale.
The high amount and quality of the data sets which exceed the existing ones by far enable us to considerably extend
the energy range for our analysis. Moreover, the wealth of data makes it possible to directly address bare correlation
functions which cannot be analyzed in most systems. Furthermore, in doing so we discuss some technical aspects,
which are of general interest for the investigation of spectral ﬂuctuations.
This paper is organized as follows: In Sec. II the data under investigation is presented. A detailed analysis of
the statistical properties is given in Sec. III. This includes the introduction of the numerical unfolding approaches,
a statistical analysis of the nearest neighbor spacing distribution, two–point spectral correlations and higher order
spectral correlations. Deviations from the RMT predictions are found and interpreted. Summary and discussion are
given in Sec. IV.
