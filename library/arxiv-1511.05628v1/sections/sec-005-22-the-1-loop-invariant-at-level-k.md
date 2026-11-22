---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-005-22-the-1-loop-invariant-at-level-k
section_title: "The 1-loop invariant at level k"
section_number: 2.2
pages: 6-7
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.899
latex_coverage_ratio: 0.935
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
