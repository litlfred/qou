---
doc_id: arxiv-2007.15570v1
doc_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_id: sec-005-c-nucleon-nucleon-interaction-algorithm
section_title: "C Nucleon-nucleon interaction algorithm"
section_number: null
pages: 5-5
source_pdf: 2007.15570v1.pdf
source_sha256: 6e46f4346a29fd83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.976
doc_brief: "A quantum Monte Carlo based approach to intranuclear cascades — 16 sections: Front matter; A quantum Monte Carlo based approa; I Introduction"
---
To check if an interaction between nucleons occurs, an accept-reject test is performed on the closest nucleon according to a probability distribution $P(b)$ (see e.g. Ref. [@Sjostrand:1987su] for similar considerations) where $b$ is the impact parameter. We impose two conditions on this probability, $$\label{eq:int_prob_conds}
    P(0)=1\quad\textrm{and}\quad
    \int_0^{2\pi}\int_0^\infty d\varphi \,b db P(b) = \sigma,$$ where the cross section $\sigma$ depends on the incoming particle content and the center-of-mass energy, which is sampled from the nuclear configuration. The second condition ensures that the mean free path of a nucleon traveling in a medium of uniform density is $\lambda_{\rm mfp} = 1/\sigma \bar{\rho}$, where $\bar{\rho}$ is the number density.

Two implementations of $P(b)$ have been studied here. The first we dub the *cylinder* interaction probability, $$P_{\rm cyl}(b) = \Theta(\sigma/\pi-b^2),
\label{prob:cyl}$$ where $\Theta(x)=1$ if $x\ge 0$, else $\Theta(x)=0$. This probability mimics a more classical, billiard ball like system, where each billiard ball has a radius $\approx \sqrt{\sigma/\pi}$. The second implementation is the *Gaussian* interaction probability $$P_{\rm Gau}(b) \equiv \exp\left(- \frac{\pi b^2}{\sigma}\right),
\label{prob:gauss}$$ which is inspired by the work of Ref. [@Sjostrand:1987su]. Both $P_{\rm cyl}$ and $P_{\rm Gau}$ satisfy the conditions in Eq. [\[eq:int_prob_conds\]](#eq:int_prob_conds){reference-type="eqref" reference="eq:int_prob_conds"}. We use the nucleon-nucleon cross sections from the SAID database [@SAID] obtained using `GEANT4` [@Agostinelli:2002hh], or from the NASA parametrization [@Norbury:2008].
