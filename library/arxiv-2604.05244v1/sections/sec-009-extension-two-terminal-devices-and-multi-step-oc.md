---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-009-extension-two-terminal-devices-and-multi-step-oc
section_title: "Extension: two-terminal devices and multi-step occupations"
section_number: null
pages: 11-12
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.976
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
[]{#sec:multi-step label="sec:multi-step"} A standard two-terminal conductor (QPC or tunnel junction) biased at DC voltage $V_{\rm dc}$ has two reservoirs at chemical potentials $\mu_L$ and $\mu_R=\mu_L-eV_{\rm dc}$ [@MoskBuett2002; @PedersenBuett1998]. For a single-channel device with transmission $\mathcal T=|\mathcal U^{\alpha L}|^2$ and reflection $\mathcal R=1-\mathcal T$, the effective occupation is $$\bar f(E_m) = \mathcal T\,\Theta(m_F^L-m) + \mathcal R\,\Theta(m_F^R-m),
  \label{eq:double-step}$$ where $m_F^{L,R}(E)=\lfloor(\mu_{L,R}-E)/\hbar\Omega\rfloor$. This is a double step, not a single step: $\bar f=1$ for $m\le m_F^R$, $\bar f=\mathcal T$ for $m_F^R<m\le m_F^L$, and $\bar f=0$ for $m>m_F^L$. Inserting [\[eq:double-step\]](#eq:double-step){reference-type="eqref" reference="eq:double-step"} into [\[eq:Cgeneral\]](#eq:Cgeneral){reference-type="eqref" reference="eq:Cgeneral"} gives $$C_{np}(E) = \mathcal T\,K_A^{\rm (disc)}(n-m_F^L,\,p-m_F^L) + \mathcal R\,K_A^{\rm (disc)}(n-m_F^R,\,p-m_F^R).
  \label{eq:C-two-terminal}$$ The correlator is a *weighted sum of two shifted discrete Bessel kernels*, each centered at a different Fermi cutoff. At large $A$, each kernel develops its own Airy edge: one near $n\sim m_F^L+A$ with weight $\mathcal T$, and another near $n\sim m_F^R+A$ with weight $\mathcal R$. When the bias window $m_F^L-m_F^R\sim eV_{\rm dc}/\hbar\Omega$ is much larger than the edge width $\kappa_A=O(A^{1/3})$, the two edges are well separated. Near the upper edge ($n\sim m_F^L+A$), the $\mathcal R$-weighted kernel is deep in its exponential tail and negligible; the local rescaled kernel tends cleanly to $\mathcal T\,K_{\mathop{\mathrm{Ai}}}(s,t)$. Near the lower edge ($n\sim m_F^R+A$), the $\mathcal R$-weighted kernel is at its edge, contributing $\mathcal R\,K_{\mathop{\mathrm{Ai}}}(s,t)$, but the $\mathcal T$-weighted kernel is in its oscillatory bulk and contributes a smooth background that varies slowly on the Airy scale. The *edge correlations*---the Airy-kernel part---come from the $\mathcal R$ term alone, but the full local kernel is $\mathcal R\,K_{\mathop{\mathrm{Ai}}}(s,t)$ plus a smooth additive background from $\mathcal T$. In a tunnel junction ($\mathcal T\ll 1$) [@LesovikLevitov1994], this background is suppressed by $\mathcal T$ and both edges are cleanly described by thinned Airy kernels with weights $\approx 1$ and $\approx\mathcal T$ respectively. The corresponding gap probability near either clean edge is $\det(\mathrm{Id}-\tau\, K_{\mathop{\mathrm{Ai}}}|_{[s_0,\infty)})$ with $\tau=\mathcal T$ or $\mathcal R$; in the RMT literature the resulting point process is called a *thinned Airy process*. When the bias window is comparable to $\kappa_A$, the two edges overlap and the correlator is a weighted superposition of two Airy kernels centered at nearby points; the resulting statistics are no longer described by a single Airy process.

This extension shows that the same large-$A$ edge scale persists in standard biased two-terminal transport. In the fixed-$E$ correlator, the two Fermi edges give two isolated thinned-Airy edges when well separated; the PASN calculation of Sec. [\[sec:transport\]](#sec:transport){reference-type="ref" reference="sec:transport"} provides a complementary bias-space realization of the same diagonal discrete Bessel kernel.
