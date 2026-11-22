---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-018-42-a-singular-limit
section_title: "A singular limit"
section_number: 4.2
pages: 16-17
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 1.0
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.singular.limit label="sub.singular.limit"}

At present we are interested in a very different limit in complex Chern-Simons theory, namely $(t,\tilde t) \to (2k,0)$, or equivalently $\sigma \to k$ with $k\in \mathbb{Z}$ held fixed. This is a singular limit rather than a weak coupling limit. We propose

::: conjecture
[]{#conj.CS label="conj.CS"} In the limit $(t,\tilde t) \to (2k,0)$, the partition function of complex Chern-Simons theory has an asymptotic expansion

$$\label{CSexp} 
\mathcal Z \sim \sum_{\text{flat $\mathcal A^*$}} 
\tau_k(\mathcal A^*) \exp\bigg[\frac1{k\hbar}I_{CS}(\mathcal A^*) 
+ \delta(\mathcal A^*)\log(k\hbar) + \sum_{n=2}^\infty \hbar^{n-1} 
S_{n,k}(\mathcal A^*)\bigg]\,,$$

where $\hbar = 2\pi i\, \tilde t/t= 2\pi i(\frac{k-\sigma}{k+\sigma})$ and $I_{CS}$ is the holomorphic classical Chern-Simons action. Moreover, if $M=S^3\backslash K$ is a hyperbolic knot complement, $G_\mathbb{C}=SL(2,\mathbb{C})$, and $\mathcal A^*$ is the hyperbolic flat connection on $M$, then $\delta(\mathcal A^*)=-\frac32$ and the series in the Quantum Modularity Conjecture [\[eq.QMF\]](#eq.QMF){reference-type="eqref" reference="eq.QMF"} at $\zeta = e^{2\pi i\alpha} = e^{2\pi i/k}$ is

$$\label{CSmod} 
\phi_{K,\zeta}(\hbar) = \tau_k (\mathcal A^*) 
\exp\bigg[\sum_{n=2}^\infty \hbar^{n-1} S_{n,k}(\mathcal A^*)\bigg]\,.$$
:::

Note that, by definition, $I_{CS}(\mathcal A^*)$ already equals the complex hyperbolic volume $V$, so the exponential term $\exp(\frac{1}{k\hbar}V)$ already matches on the right hand side of Equations [\[CSexp\]](#CSexp){reference-type="eqref" reference="CSexp"} and [\[eq.QMF\]](#eq.QMF){reference-type="eqref" reference="eq.QMF"}.

The existence of the expansion [\[CSexp\]](#CSexp){reference-type="eqref" reference="CSexp"} is physically far from obvious. One explanation for [\[CSexp\]](#CSexp){reference-type="eqref" reference="CSexp"} comes from the so-called 3d-3d correspondence [@Yamazaki-3d; @DGG]. An extension of the original correspondence relates Chern-Simons theory at level $k$ on $M$ to the supersymmetric partition function of an associated 3d $\mathcal N=2$ theory $T[M]$ on a lens space $L(k,1)\simeq S^3/\mathbb{Z}_k$ [@CJ; @D-levelk]. The lens space is a $\mathbb{Z}_k$ orbifold of a sphere, whose geometry has been ellipsoidally deformed such that the ratio of minimum to maximum radii is $b=\sqrt{\tilde t/t} = 
\sqrt{\frac{k-\sigma}{k+\sigma}}$. It is well known that as $b\to 0$ the partition function of $T[M]$ on a sphere $L(1,1)\simeq S^3$ has an expansion of the form [\[CSexp\]](#CSexp){reference-type="eqref" reference="CSexp"}, whose leading exponential term is $\frac1\hbar I_{CS}(\mathcal A^*)$, see [@DG-Sdual; @Yamazaki-3d; @DGG]. One then expects the $L(k,1)$ partition function to have a similar expansion as $b\to 0$, with leading term $\frac1{k\hbar} I_{CS}(\mathcal A^*)$, just as in [\[CSexp\]](#CSexp){reference-type="eqref" reference="CSexp"}.

There are also some preliminary hints that the existence and structure of [\[CSexp\]](#CSexp){reference-type="eqref" reference="CSexp"} may be explained using electric-magnetic duality in four-dimensional Yang-Mills theory, with Chern-Simons theory on its boundary along the lines of [@Witten-q; @Witten-5]. Indeed, the electric-magnetic duality group $SL(2,\mathbb Z)$ can relate a singular limit such as $(t,\tilde t)\to(2k,0)$ to a more standard weak-coupling limit. Electric-magnetic duality has been linked to modular phenomena in the past [@VafaWitten], and it is tempting to believe that it could provide a physical basis for Quantum Modularity as well. We aim to explore this further in the future.
