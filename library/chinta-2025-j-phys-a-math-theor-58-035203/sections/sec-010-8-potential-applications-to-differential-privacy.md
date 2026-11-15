---
doc_id: chinta-2025-j-phys-a-math-theor-58-035203
doc_title: "The discrete analogue of the Gaussian"
section_id: sec-010-8-potential-applications-to-differential-privacy
section_title: "Potential applications to differential privacy"
section_number: 8
pages: 20-21
source_pdf: Chinta_2025_J._Phys._A__Math._Theor._58_035203.pdf
source_sha256: baba83ca76c773d4
toc_source: outline
doc_brief: "The discrete analogue of the Gaussian — 13 sections: Front matter; The discrete analogue of the Gauss; Introduction"
---
Differential privacy is a mathematically rigorous criterion by which an algorithm that acts on
a dataset can be assessed. We refer to the article [CKS22] and references therein for an excel-
lent presentation. In practice, as described in [CKS22], one alters the output of a Z-valued
algorithm M which produces results from a given dataset D by adding a random amount. The
main results of [CKS22] are that one can use a discretized Gaussian random (6) (using our ter-
minology) to create algorithms which satisfy differential privacy, and that one can effectively
and efficiently sample from a discretized Gaussian random variable.
It would be interesting to determine if the discrete Gaussian (3) also satisfies the criterion
established in [CKS22] for random ‘noise’ as required by differential privacy. It should be
noted that other authors have pointed out the potential usefulness of (3) and distinguished the
difference between (3) and (6); see section 2.6 of [Li24] who refers to earlier work by the
same author in [Li90]. One can reasonably expect that, indeed, (3) will fulfill the conditions
needed for differential privacy, if for no reason other than the triangle inequality, the results
from [CKS22] and Proposition 1. However, it would be better to establish differential privacy
associated to (3) without appealing to [CKS22]. We will leave this study for a later time.
From the point of view of probability, one can state several advantages that (3) has over (1).
First, we note that the (quite impressive) analysis of [CKS22] includes, for example, estimates
for the moment generating function and variance of the discretized Gaussian (6); see lemma 8
and corollary 9 of [CKS22]. By contrast, note that the characteristic function of (3) is explicitly
computed; see (16). As such, one has elementary closed-form expressions for all moments
of (3). See also [AGMP24]. Second, the sum of two independent discretized Gaussian random
variables (6) is close to, but not equal to, a discretized Gaussian random variable; see the
19
J. Phys. A: Math. Theor. 58 (2025) 035203
G Chinta et al
comment after remark 3.7 in [AA19] and theorem 1.1 of [AR24]. By comparison, the sum
of two independent discrete Gaussians (3) is a discrete Gaussian, and the convolution of the
probability density functions is, in effect, computed in the above-cited Chapman–Kolmogorov
equation; see section 4. Finally, let us point out that one application of theorem 5 is a means
by which one can sample from a discrete Gaussian is a manner similar to a sampling method
for a continuous Gaussian random variable. In doing so, one has, at least the beginning of, an
analogue to the sampling algorithms developed in [CKS22]. Other sampling methods could
be developed based on numerical evaluations of Bessel functions; to this end, we found the
articles [Am74] and [GS81] to be interesting.
Finally, let us note that the articles [AA19] and [AR24] consider discretized Gaussian ran-
dom variables on any d-dimensional lattice Λ in Rd. Certainly, our point of view is amenable
to such a setting; see, for example, [CJK10] and more generally [CJK12]. The probability
density function is simply the heat kernel on Λ, and we assert that one can prove an analogue
of theorem 5. Again, these considerations will be undertaken elsewhere.
Data availability statement
No new data were created or analysed in this study.
ORCID iDs
Gautam Chinta https://orcid.org/0000-0002-2672-3819
Jay Jorgenson https://orcid.org/0000-0002-9765-0944
Anders Karlsson https://orcid.org/0000-0002-1886-6780
Lejla Smajlovi´c https://orcid.org/0000-0002-2709-5535
