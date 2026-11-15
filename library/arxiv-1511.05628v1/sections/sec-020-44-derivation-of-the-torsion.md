---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-020-44-derivation-of-the-torsion
section_title: "Derivation of the torsion"
section_number: 4.4
pages: 19-20
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.925
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.derivation.torsion label="sub.derivation.torsion"}

To illustrate how the formal Gaussian integration works, let us derive the $k$-twisted torsion or "1-loop invariant" $\tau_{\gamma,k}$ of [\[eq.tau\]](#eq.tau){reference-type="eqref" reference="eq.tau"}, starting from [\[SSk\]](#SSk){reference-type="eqref" reference="SSk"}. Let us set $\zeta=e^{\frac{2\pi i}{k}}$ and $\theta_i = z_i^{1/k} = e^{Z_i^*/k}$ as usual, and work at fixed $m\in (\mathbb Z/k \mathbb Z)^N$ to start.

There are two contributions to the torsion. First there is the integrand itself, evaluated at $Z=Z^*$, keeping only terms of order $\hbar^0$ in the exponent:

$$\frac{\zeta^{\frac14 f\mathbf B^{-1}\nu}}{k^N (-2\pi i \hbar)^{\frac N2}
\sqrt{\det \mathbf B}} \times (-\zeta^{\frac12})^{m\mathbf B^{-1}\mathbf Am}
e^{-\frac1{2k}Z^*\mathbf B^{-1}\nu} \prod_{i=1}^N \prod_{s=1}^{k} 
(1-\zeta^{m_i+s}e^{-Z_i^*/k})^{\frac12-\frac sk} \,,$$

where we have used that ${\rm Li}_1(x) = -\log(1-x)$. Second, there is the determinant of the Hessian, coming from the leading-order Gaussian integration,

$$\big[\det  \tfrac{1}{2\pi k\hbar}
(-\mathbf B^{-1}\mathbf A + \Delta_z)\big]^{-\frac12}\,.$$

Combining these terms, using $\mathbf Af+\mathbf Bf''=\nu$ and $\mathbf AZ^*+\mathbf B(Z^*)''=i\pi \nu$ to rewrite $Z^*\mathbf B^{-1}\nu$ as $Z^*\cdot f'' - (Z^*)''\cdot f+i\pi f\mathbf B^{-1}\nu$, and observing that $\prod_{i=1}^N\prod_{s=1}^k(1-\zeta^{m_i+s}e^{-Z_i^*/k})^{\frac12} 
= \prod_{i=1}^N (1-e^{-Z_i^*})^{\frac12} = (\det \Delta_{z''})^{\frac12}$, we arrive at

$$\tau_{\gamma,k} = \frac{1}{(ik)^{\frac N2}
\sqrt{\det(\mathbf A\Delta_z''+\mathbf B\Delta_{z'}^{-1})z^{f''/k}z''{}^{f/k}}} 
(-\zeta^{\frac12})^{m\mathbf B^{-1}\mathbf Am}
\prod_{i=1}^N \prod_{s=0}^{k-1} (1-\zeta^{m_i-s}\theta_i^{-1})^{s/k}\,.$$

The product may be manipulated further using

$$\begin{aligned}
 & \prod_{s=0}^{k-1}(1-\zeta^{m_i-s}\theta_i^{-1})^{\frac sk} 
= \prod_{s=-m_i}^{k-1-m_i}(1-\zeta^{-s}\theta_i^{-1})^{\frac {s+m_i}{k}}  \\
&\hspace{.8in}
= z_i''{}^{\frac {m_i}{k}} \prod_{s=k-m_i}^{k-1}
(1-\zeta^{-s}\theta_i^{-1})^{\frac sk-1}\prod_{s=0}^{k+m_i}
(1-\zeta^{-s}\theta_i^{-1})^{\frac sk} = z_i''{}^{\frac {m_i}{k}} 
D_k^*(\theta_i^{-1})^{\frac 1k} (\zeta\theta_i^{-1};\zeta)_{m_i}^{-1}\,.
\end{aligned}$$

Finally, setting $\prod_i z_i''{}^{\frac {m_i}k} = \exp[\frac1k (Z^*)''\cdot m] 
= \exp[\frac {i\pi}k m\mathbf B^{-1}\nu-\frac 1k m\mathbf B^{-1}\mathbf AZ]
=\zeta^{\frac12 m\mathbf B^{-1}\nu}\theta^{-\mathbf B^{-1}\mathbf Am}$, and summing the whole expression over $m\in (\mathbb Z/k\mathbb Z)^N$, we recover [\[eq.tau\]](#eq.tau){reference-type="eqref" reference="eq.tau"}.
