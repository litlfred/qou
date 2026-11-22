---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-006-23-the-n-loop-invariants-at-level-k-for-n-2
section_title: "The n-loop invariants at level k for n 2"
section_number: 2.3
pages: 7-8
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.966
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.all label="sub.all"}

The definition of the higher-loop invariants $S_{\gamma,n,k}$ is motivated by perturbation theory of the state-integral model for complex Chern-Simons theory, reviewed briefly in Section [\[sec.CCS\]](#sec.CCS){reference-type="ref" reference="sec.CCS"}. In this section we define the higher-loop invariants using formal Gaussian integration, and in the next section we give a Feynman diagram formulation of the higher-loop invariants.

Fix a $\mathbb Z$-non-degenerate Neumann-Zagier datum $\gamma$ and a positive integer $k$. We will use the notation of the previous section. If $f: (\mathbb Z/k\mathbb Z)^N \longrightarrow\mathbb C$, we define $$\label{eq.Avf}
\mathrm{Av}(f)= \frac{\sum_{m\in (\mathbb{Z}/k\mathbb{Z})^N} a_m(\theta) f(m)}{
\sum_{m\in (\mathbb{Z}/k\mathbb{Z})^N} a_m(\theta)}\,,$$ assuming that the denominator is nonzero. Consider the symmetric matrix

$$\mathcal{H}=\frac1k(-\mathbf B^{-1}\mathbf A+\Delta_{z'})\,,$$

where $\Delta_{z'}=\text{diag}(z_1',...,z_N')$. Assuming that $\mathcal{H}$ is invertible, a formal power series $f_\hbar(x)\in \mathbb Q(z)[\![x,\hbar^{\frac12}]\!]$ has a *formal Gaussian integration*, given by

$$\label{formalG}
\langle f_{\hbar}(x)\rangle= \frac{\int dx \, 
e^{-\frac12x^T \mathcal{H}\,x}f_{\hbar}(x)}{\int dx \, e^{-\frac12x^T \mathcal{H}\,x}}\,.$$

This integration, which is a standard tool of perturbation theory in physics, and may be found in numerous texts (e.g. [@BIZ]) is defined by expanding $f_\hbar(x)$ as a series in $x$, and then formally integrating each monomial, using the quadratic form $\mathcal{H}^{-1}$ to contract $x$-indices pairwise.

The building block of each tetrahedron is the power series $$\label{eq.block}
\psi_\hbar(x,\theta,m)=\exp\left(
\sum_{n=1}^\infty\sum_{j=0}^\infty \frac{\hbar^{n-1}(-1)^j}{
n!j!k^j} \sum_{s=1}^k B_n\left(\frac{s}{k}\right) {\rm Li}_{2-n-j}(\zeta^{m+s}
\theta^{-1}) x^j
\right)$$

For an ideal triangulation $\mathcal T$ with $N$ tetrahedra, a natural number $k$, and $m \in (\mathbb{Z}/k\mathbb{Z})^N$, we define

$$\label{eq.fT}
f_{\mathcal T,\hbar}(x;\theta,m)=\exp \bigg(-\frac{\hbar^{\frac12}}{2k} x^T \mathbf B^{-1} 
\nu +\frac\hbar{8k} f^T\mathbf B^{-1}\nu \bigg)
\prod_{i=1}^N \psi_\hbar(x_i,\theta_i,m_i)$$

::: definition
[]{#def.phih label="def.phih"} We define $$\label{eq.defphi}
\phi^+_{\gamma,\zeta}(\hbar)=\mathrm{Av}(\langle f_{\mathcal T,\hbar}(x;\theta,m) \rangle) \in 
1+\hbar\mathbb C[\![\hbar]\!] \,.$$
:::

Thus, we can write $$\label{def.Sn}
\phi^+_{\gamma,\zeta}(\hbar) = 
\exp\left(\sum_{n=1}^\infty S_{\gamma,n+1,k} \hbar^n\right) \,.$$ We call $S_{\gamma,n,k}$ the level $k$, $n$-loop invariant of $\gamma$. We finally define

$$\phi_{\gamma,\zeta}(\hbar) = \tau_{\gamma,\zeta}
\phi^+_{\gamma,\zeta}(\hbar)\,.$$

::: theorem
[]{#thm.1 label="thm.1"} The coefficients of the power series $\phi^+_{\gamma,\zeta}(\hbar)$ are in $F_k$.
:::

In particular, the series $\phi^+_{\gamma,\zeta}(\hbar)$ depends on $\gamma$, the $k$-th root of unity $\zeta$, but it is independent of the choice of $k$-th roots $\theta_i$ of $z_i$. The above theorem is not trivial since $a_m(\theta)$ is an element of the larger field $F_{G,k}$, whereas the coefficients of the above average are claimed to be in the field $F_k$. For the proof, see Section [\[sec.proofs\]](#sec.proofs){reference-type="ref" reference="sec.proofs"}.

::: remark
[]{#rem.primitivek label="rem.primitivek"} Theorems [\[thm.1loop\]](#thm.1loop){reference-type="ref" reference="thm.1loop"} and [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} remain valid if $\zeta$ denotes a fixed primitive $k$-th root of unity instead of $\zeta=e^{2 \pi i/k}$. Probably a better notation is $S_{\gamma,n,\zeta}$ rather than $S_{\gamma,n,k}$ which is valid for all primitive $k$-roots of unity $\zeta$.
:::
