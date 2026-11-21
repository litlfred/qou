---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum"
section_id: sec-002-3-anderson-transition-in-the-dirac-spectrum
section_title: "Anderson transition in the Dirac spectrum"
section_number: 3
pages: 2-4
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.926
doc_brief: "Poisson - Random Matrix transition in the QCD Dirac spectrum — 12 sections: Front matter; Introduction; Simulation details"
---
[]{#se:AtitDs label="se:AtitDs"}

Previously it was seen that in the high temperature deconfining phase of $SU(2)$ Yang-Mills theory there is a transition in the staggered Dirac spectrum from localized low modes to delocalized modes higher up in the spectrum [@Kovacs:2010wx]. The question we ask here is whether such a transition also occurs in real QCD with light dynamical quarks. This is a non-trivial question since light quarks suppress low Dirac modes through the fermion determinant in the functional integral and in the quenched case it is exactly the lowest Dirac modes that are localized.

The hallmark of a transition from localized to delocalized modes in terms of spectral statistics is a change from Poisson statistics to random matrix statistics in the spectrum. Intuitively speaking, localized modes are such because they cannot mix with other modes; typical gauge field fluctuations do not mix them. Localized modes close in the spectrum are peaked at spatially distant locations and they are sensitive only to gauge field fluctuations there. As a result the corresponding eigenvalues are statistically independent and the level spacings obey Poisson statistics. Delocalized modes, in contrast, are mixed by typical gauge field fluctuations. Gauge field fluctuations change several delocalized modes together which introduces delicate correlations in the spectrum and as a result the eigenvalue statistics is described by Random Matrix Theory (RMT).

The simplest way to detect a transition in the spectrum from Poisson to RMT statistics is to consider the so called unfolded level spacing distribution. Unfolding is essentially a local rescaling of the eigenvalues to have unit spectral density throughout the spectrum. We did the unfolding by ordering all eigenvalues in the given ensemble and replacing them with their rank order normalized by the total number of configurations. On a few ensembles we also checked unfolding by using local spline approximations to the spectral density but there was no discrepancy between the two methods of unfolding.

Since the unfolded level spacing distribution (ULSD) is known analytically for both the Poisson and the RMT statistics it can be easily used to distinguish between the two cases. For Poisson statistics the ULSD is a simple exponential,

$$P\ensuremath _{\mbox{\scriptsize Poisson}}(s)=\exp(-s).$$

In the RMT case the unfolded level spacing distribution depends on the universality class which in the case of staggered fermions in the fundamental representation of the $SU(3)$ gauge group is the Chiral Unitary Ensemble (ChUE) [@Verbaarschot:2000dy]. The corresponding ULSD is very precisely approximated by the chiral unitary Wigner surmise,

$$P\ensuremath _{\mbox{\scriptsize ChUE}}(s) = \dfrac{32}{\pi^{2}}s^{2}\cdot
                       \exp\left(-\dfrac{4}{\pi}s^{2}\right).
  \label{eq:wigner_chu}$$

To demonstrate the transition in the spectrum in Fig. [1](#fig:ulsd){reference-type="ref" reference="fig:ulsd"} we plot the ULSD in different regions of the spectrum of ensemble C3; $0.15 \leq
\lambda a \leq 0.19$ (a), $0.29 \leq \lambda a \leq 0.32$ (b), $0.34 \leq
\lambda a \leq 0.35$ (c) and $0.375 \leq \lambda a \leq 0.385$ (d). We also indicate in the same Figure the distributions corresponding to the Poisson (localized) and the RMT (delocalized) case. The transition from localized modes at the edge of the spectrum to delocalized modes in the bulk can be clearly seen. This shows that light dynamical fermions do not change the picture observed in the quenched case earlier and the transition also occurs in QCD with quarks of physical masses.

<figure id="fig:ulsd">
<div class="center">
<table>
<tbody>
<tr class="odd">
<td style="text-align: center;"><embed src="0_15_0_19_324.eps" /></td>
<td style="text-align: center;"><embed src="0_29_0_32_324.eps" /></td>
</tr>
<tr class="even">
<td style="text-align: center;"><embed src="0_34_0_35_324.eps" /></td>
<td style="text-align: center;"><embed src="0_375_0_385_324.eps" /></td>
</tr>
</tbody>
</table>
</div>
<figcaption><span id="fig:ulsd" label="fig:ulsd"></span>The unfolded level spacing distribution in different regions of the spectrum of ensemble C3. The figures correspond to the spectral regions <span class="math inline">0.15 ≤ <em>λ</em><em>a</em> ≤ 0.19</span> (a), <span class="math inline">0.29 ≤ <em>λ</em><em>a</em> ≤ 0.32</span> (b), <span class="math inline">0.34 ≤ <em>λ</em><em>a</em> ≤ 0.35</span> (c) and <span class="math inline">0.375 ≤ <em>λ</em><em>a</em> ≤ 0.385</span> (d). The dashed line indicates the exponential distribution corresponding to the localized (Poisson) case and the dotted line indicates the chiral unitary Wigner surmise expected in the delocalized (RMT) case.</figcaption>
</figure>
