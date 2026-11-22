---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-008-25-the-2-loop-invariant-in-detail
section_title: "The 2-loop invariant in detail"
section_number: 2.5
pages: 9-11
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.836
latex_coverage_ratio: 0.825
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.2loop label="sub.2loop"}

The six diagrams that contribute to $S_{\gamma,2}$ are shown in Figure [1](#fig.diags2intro){reference-type="ref" reference="fig.diags2intro"}, together with their symmetry factors. Their evaluation gives the following formula for $S_{\gamma,2,k}$:

$$\begin{aligned}
 \label{2loopexplicit}
S_{\gamma,2,k} &= \mathrm{Av}\left( \mathrm{coeff}\left[\Gamma^{(0)}+ 
\frac18  \Gamma^{(4)}_i (\Pi_{ii})^2 
+ \frac18\Pi_{ii}\Gamma^{(3)}_i\Pi_{ij}\Gamma^{(3)}_j\Pi_{jj} 
+ \frac{1}{12}\Gamma^{(3)}_i(\Pi_{ij})^3\Gamma^{(3)}_j \right. \right.\\
&\hspace{1in}
\left.\left. + \frac12 \Gamma^{(1)}_i\Pi_{ij}\Gamma^{(3)}_j\Pi_{jj} 
+ \frac12 \Gamma^{(2)}_i\Pi_{ii} 
+ \frac12\Gamma^{(1)}_i\Pi_{ij}\Gamma^{(1)}_j ,\; \hbar\right]
\right) \,, 
\notag
\end{aligned}$$

where the dependence of vertex factors on $m$ is suppressed; all the indices $i$ and $j$ are implicitly summed from $1$ to $N$; and $\mathrm{coeff}[f(\hbar),\,\hbar^k]$ denotes the coefficient of $\hbar^k$ in a power series $f(\hbar)$.

![Diagrams contributing to $S_{\gamma,2}$ with symmetry factors. The top row of diagrams have exactly two loops, while the bottom row have fewer loops and additional $1$-vertices and $2$-vertices.](draws/diags2.pdf){#fig.diags2intro width="4in"}

Concretely, the 2-loop contribution from the vacuum energy is $$\Gamma^{(0)}=\frac{1}{8k}f \mathbf B^{-1}\nu-\frac12
\sum_{s=1}^k(\frac{s^2}{k^2}-\frac{s}{k}+\frac16)
\sum_{i=1}^N(1-\zeta^{-m_i-s}\theta_i)^{-1} \,.$$ The four other vertices contribute only at leading order; abbreviating $\tilde\theta_i=\zeta^{-m_i-s}\theta_i$ and $\tilde \theta_i' = (1-\zeta^{-m_i-s}\theta_i)^{-1}$, they are

$$\notag  \Gamma^{(1)}_i=-\frac{1}{2k}(\mathbf B^{-1}\nu)_i + 
\frac1k\sum_{s=1}^k\Big(\frac sk-\frac12\Big)\tilde\theta_i'\,,$$ $$\notag \Gamma^{(2)}_i = \frac{1}{k^2}\sum_{s=1}^k \Big(\frac sk-\frac12\Big) 
\tilde\theta_i\tilde\theta_i'{}^2\,,
\qquad
\Gamma^{(3)}_i = -\frac{\tilde\theta_i\tilde\theta_i'^2}{k\hbar}\,,\qquad 
\Gamma^{(4)}_i= 
-\frac{\tilde\theta_i(1+\tilde\theta_i)\tilde\theta_i'{}^3}{k\hbar}\,.$$

![Diagrams with three loops contributing to $S_3$.](draws/diags3wide.pdf){#fig.diags3 width="6.5in"}

![Diagrams with $1$-vertices and $2$-vertices contributing to $S_3$.](draws/diags3dotwide.pdf){#fig.diags3dot width="6.5in"}
