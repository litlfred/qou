---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-003-22-the-1-loop-invariant-at-level-k
section_title: "The 1-loop invariant at level k"
section_number: 2.2
pages: 6-8
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.969
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
Fix a $\mathbb Z$-non-degenerate Neumann-Zagier datum $\gamma$ and a positive integer $k$. We use the notation of the previous section. For $m\in (\mathbb Z/k\mathbb Z)^N$, we define

$$\label{eq.amth}
a_m(\theta) = e^{-i\pi\, m\cdot\mathbf B^{-1}\mathbf A m} 
\zeta^{\frac12 \big[m\cdot \mathbf B^{-1}\mathbf A m+ m\cdot \mathbf B^{-1}\nu\big]}
\prod_{i=1}^N
\frac{\theta_i^{-(\mathbf B^{-1} \mathbf A m)_i}}{
(\zeta \theta_i^{-1};\zeta )_{m_i}}\,.$$

We also recall the *cyclic quantum dilogarithm* defined by $$D_k(x)=\prod_{s=1}^{k-1}(1-\zeta^{s}x)^s \qquad
D^*_k(x)=\prod_{s=1}^{k-1}(1-\zeta^{-s}x)^s \,.$$ This function appears in [@Kashaev:star Eqn.C.3] and [@Kashaev:quantum.hyper Eqn.2.30].

::: definition
[]{#def.1loop label="def.1loop"} With the above assumptions, the level $k$ 1-loop invariant of $\gamma$ is $$\label{eq.tau}
\tau_{\gamma,k} :=  \frac{1}{k^{N/2}\sqrt{\det(\mathbf A\Delta_z''
+\mathbf B\Delta_z^{-1}) z^{f''/k}z''^{-f/k}}} 
\prod_{i=1}^N D_k^*(\theta_i^{-1})^{1/k} \sum_{m\in (\mathbb{Z}/k\mathbb{Z})^N} a_m(\theta)\,,$$ where $\Delta_z = \text{diag}(z_1,...,z_N)$ and $\Delta_{z''}=\text{diag}(z_1'',...,z_N'')$ are diagonal matrices.
:::

Note that $\tau_{\gamma,k}$ depends on the Neumann-Zagier datum $\gamma$, the $k$-th root of unity $\zeta$ but also on the choice of $k$-th roots $\theta_i$ of $z_i$. The next theorem implies that $\tau_{\gamma,k}^{2k}$ depends only on $\gamma$ and $\zeta$, and therefore that $\tau_{\gamma,k}$ is well defined modulo multiplication by a $2k$-th root of unity. The proof (given in Section [\[sec.proofs\]](#sec.proofs){reference-type="ref" reference="sec.proofs"}) follows from results of Zagier and the second author [@GZ1] via a a comparison of an arithmetic to a geometric mean over the Galois group of $F_{G,k}/F_k$, reminiscent of Hilbert's theorem 90.

::: theorem
[]{#thm.1loop label="thm.1loop"} We have $\tau_{\gamma,k}^{2k} \in F_k$.
:::

::: remark
[]{#rem.Sunit label="rem.Sunit"} It is easy to see that $\tau_k^{2k}/\tau_1^{2k}$ is an $S$-unit of the ring of integers of $F_k$ where $S=\langle z,1-z\rangle\subset F_K^*$. For an illustration, see Section [\[sec.data\]](#sec.data){reference-type="ref" reference="sec.data"}.
:::

::: remark
[]{#rem.tau.alternative label="rem.tau.alternative"} After replacing $\zeta$ by $\zeta^{-1}$, We can give an alternative formula for the $1$-loop invariant at level $k$ as follows: $$\label{eq.tau.alternative}
\tau_{\gamma,k} :=  \frac{1}{k^{N/2}\sqrt{\det(\mathbf- A\Delta_z''
-\mathbf B\Delta_z^{-1}) z^{f''/k}z''^{-f/k}}}
\prod_{i=1}^N \frac{z_i^{\frac{k-1}{2k}} (z_i'')^{\frac{k-1}{k}}}{

D_k(\zeta^{-1}\theta_i)^{1/k}} 
\sum_{m\in (\mathbb{Z}/k\mathbb{Z})^N} b_m(\theta)\,,$$ where $$\label{eq.alt.amth}
b_m(\theta) = e^{i\pi\, L \cdot m} 

\zeta^{-\frac12 \big[m^T Q m+ L \cdot m\big]}
\prod_{i=1}^N
\frac{\theta_i^{ Q_i \cdot m}}{

(\zeta^{-1} \theta_i;\zeta^{-1} )_{m_i}}\,$$ and $$\label{eq.QL}
L= -\mathbf B^{-1} \nu + (1,\dots,1)^T, \qquad Q=I-\mathbf B^{-1}\mathbf A \,.$$
:::

## The $n$-loop invariants at level $k$ for $n \geq 2$ {#sub.all}

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
