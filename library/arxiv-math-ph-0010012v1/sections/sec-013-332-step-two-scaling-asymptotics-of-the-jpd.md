---
doc_id: arxiv-math-ph-0010012v1
doc_title: "arXiv:math-ph/0010012v1 10 Oct 2000"
section_id: sec-013-332-step-two-scaling-asymptotics-of-the-jpd
section_title: "Step two: scaling asymptotics of the JPD"
section_number: 3.3.2
pages: 5-6
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.955
doc_brief: "arXiv:math-ph/0010012v1 10 Oct 2000 — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
The JPD is a (generalized) Gaussian measure on the complex vector space of 1-jets: $\widetilde{\mathbf D}_{z}^N=\gamma_{\Delta^N(z)}\,,$ where the covariance matrix $\Delta^N(z) = \left(
\begin{array}{cc}
A & B \\
B^* & C
\end{array}\right)$ is given in terms of the Szegö kernel and its covariant derivatives, as follows: $$\begin{array}{ll} A = \big( A^{p}_{p'}\big) =\frac{1}{d_N}\Pi_N(z^p,0;z^{p'},0)\,, & 
B = \big(B^{p}_{p'q'}\big)= \frac{1}{d_N}
\overline{\nabla}^2_{q'}\Pi_N(z^p,0;z^{p'},0)\,, \\ & \\
C = \big(C^{pq}_{p'q'}\big) = 
 \frac{1}{d_N}
\nabla^1_q\overline{\nabla}^2_{q'}\Pi_N(z^p,0;z^{p'},0)\,, &  p,p'=1,\dots,n, \quad q,q'=1,\dots,2m\,.\nonumber
\end{array}$$ Here, $\nabla^1_q$, respectively $\nabla^2_q$, denotes the differential operator on $X\times X$ given by applying $\nabla_q$ to the first, respectively second, factor. The link between the JPD and the Szego kernel stems ultimately from the fact that $\Pi_N$ is the covariance matrix of $\gamma$ on ${\mathcal H}_N.$ Using the scaling asymptotics of the Szegö kernel we obtain (in the complex case):

::: theo
[]{#usljpd label="usljpd"} ([@SZ2], Theorem 5.4) With the same notations and assumptions, we have: $$\widetilde{\mathbf D}^N_{(z^1/\sqrt{N},\dots, z^n/\sqrt{N})} \longrightarrow {\mathbf D}^\infty
_{(z^1,\dots,n^n)}= \gamma_{\Delta^\infty(z)}$$ where ${\mathbf D}^\infty_{(z^1,\dots,z^n)}$ is a universal Gaussian measure, and $\Delta^N(z/\sqrt{N})\to \Delta^\infty(z)$.
:::

The covariance matrix $\Delta^\infty$ is given in terms of the Szegö kernel for the Heisenberg group: $$\label{delta}
\Delta^\infty(z)= \frac{m!}{c_1(L)^m}\left(
\begin{array}{cc}
A^\infty(z) & B^\infty(z) \\
B^{\infty}(z)^* & C^\infty(z)
\end{array}\right)\,,$$ where $$\begin{aligned}
 A^\infty(z)^p_{p'} &=& \Pi_1^{\mathbf H}(z^p,0;z^{p'},0)\,,\\
B^\infty(z)^{p}_{p'q'} &=&\left\{\begin{array}{ll}
(z^p_{q'}-z^{p'}_{q'}) \Pi_1^{\mathbf H}(z^p,0;z^{p'},0) \  &\mbox{for}\quad  1\le
q\le m\\ 0 & \mbox{for}\quad  m+1\le q\le 2m\end{array}\right.\ ,\\
C^\infty(z)^{pq}_{p'q'} &=&\left\{\begin{array}{ll}
(\delta_{qq'} + (\bar z^{p'}_q
-\bar z^p_q) (z^p_{q'}-z^{p'}_{q'}))\Pi_1^{\mathbf H}(z^p,0;z^{p'},0) \ 
&\mbox{for}\quad  1\le q,q'\le m\\ 0 & \mbox{for}\quad  \max(q,q')\ge
m+1\end{array}\right.\ .
\end{aligned}$$

The scaling limit thus gives the correlations between zeros in the 'Heisenberg ensemble', an infinite dimensional Gaussian ensemble. In the real case (i.e. $S^m$), the limit correlations coincide with those in an ensemble related to the Euclidean motion group, and involving the Bessel kernel [@N].
