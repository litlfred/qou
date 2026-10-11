---
doc_id: arxiv-math-ph-0010012v1
doc_title: "From random polynomials to symplectic geometry Steve Zelditch"
section_id: sec-005-3-distribution-of-zeros-and-critical-points
section_title: "Distribution of zeros and critical points"
section_number: 3
pages: 4-5
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
doc_brief: "From random polynomials to symplectic geometry Steve Zelditch — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
text_source: latex
latex_prose_ratio: 0.997
latex_coverage_ratio: 0.988
---
We now state some results on the zeros and critical points of random generalized polynomials. Let $(s_1, \dots, s_k) \in H^0(M, L^N)^k$ or let $(s_1, \dots, s_k) \in {\mathcal H}_N^k$ in the real case. When $k = 1$ we omit the subscript. We will use the following notation.

-   $Z_s = \{x : s(x) = 0\}$ denotes the zero set of $s$, and $|Z_s|$ denotes the $m - k$-submanifold Riemannian volume density induced by $\omega$ in the complex case or by $g$ in the real case. We further denote by $||Z_s||$ the mass of $|Z_s|$ and define the probability measures $\tilde{Z}_s = \frac{|Z_s|}{||Z_s||}.$ When one takes $m$ sections (or functions) in dimension $m$, then the simultaneous zeros are almost surely a discrete set and the measure $\tilde{Z}_s$ is the normalized sum of delta-functions at the zeros.

-   $C_s =\{z: \nabla s(z) = 0\}$ denotes the critical point set of $s$. In the holomorphic case, $\nabla$ is the holomorphic connection compatible with $h$. We note that $C_s$ is almost surely a discrete set. We define $|C_f| = \sum_{z_j: \nabla s(z_j) = 0} \delta (z_j),$ $||C_s|| = \# C_s,$ and $\tilde{C}_s = \frac{|C_s|}{\# C_s}.$

-   By the density of zeros at degree $N$ we mean the coefficient $K^N_{1,k}(z)$ of the measure $K^N_{1,k}(z) dV = {\bf E} |Z_s|,$ i.e. $\int_M \varphi{\bf E} |Z_s| = {\bf E} \int_M \varphi|Z_s|$ for $\varphi\in C(M).$ Similarly, we denote by $K^{crit, N}_{1}(z)$ the density (relative to the given volume form) of ${\bf E}\tilde{C}_s.$

-   More generally, we define the pair correlation densities of zeros (resp. critical points) by $K^N_{2,k}(z^1, z^2) dV = {\bf E} (|Z_s| \times |Z_s|),$ resp. $K^{crit, N}_{2,k}(z^1, z^2) dV = {\bf E} (|C_s|\times |C_s|).$ They are densities of measures on $M \times M.$ Roughly speaking, the two-point correlation gives the probability density of finding a pair of zeros (or critical points) at $(z^1, z^2).$ More generally, there are n-point correlation functions, but for simplicity we only consider $n = 1, 2.$

## Statement of results

We have results on several levels: expected values, almost sure behaviour, and scaling asymptotics. The following theorems are valid on any complex or almost-complex symplectic manifold $(M, \omega)$, equipped with a hermitian complex line bundle of curvature $\omega.$

::: theo
In the complex case, the density of zeros, resp. critical points, satisfies:

-   [@SZ1] Complex zeros: $K^N_{1,k}(z) dV = \omega^k + O(\frac{1}{N}).$

-   [@SZ3] Complex critical points: There exists a universal constant $\gamma_m$ depending only on the dimension such that $K^{crit, N}_1(z) dV = \gamma_m \frac{\omega^m}{m!} N^m + O(N^{m - 1}),$ In particular, the expected number of critical points is given by ${\bf E} \# C_s =  \gamma_m Vol_{\omega}(M) N^m + O(N^{m - 1}).$ Here, $Vol_{\omega}(M) = \frac{c_1(L)^m}{m!}$ is the volume of $(M, \omega)$. The density of critical points is therefore universal.
:::

Thus, zeros and critical points tend to concentrate in regions of high curvature. Similar results should hold in the real case. In the case of $S^m$, such density results are obvious since they must be rotationally invariant.

## Almost sure distribution of zeros

A deeper question on distribution of zeros is whether sequences of individual sections tend to have equidistributed zeros.

::: theo
We have:

-   [@SZ1] For a random sequence in the complex codimension $k$ case, $\{s_N\}$, $\tilde{Z}_{s_N} \to \omega^k$ almost surely.

-   [@N] For a random sequence of spherical harmonics on $S^m, m \geq 6$, we have $\tilde{Z}_{s_N} \to dvol$ almost surely. The same is true in (Cesaro) mean for dimensions $< 6.$
:::

## Universality and scaling of correlations

The next level of results concerns the statistics of zeros and critical points on the length scale $\frac{D}{\sqrt{N}}$ (complex case) or $\frac{D}{N}$ (real case). For brevity we only describe the results in the complex case. Upon magnifying a small ball $B_{\frac{D}{\sqrt{N}}}(z_0)$ around an arbitrary point $z_0$ of this radius, one loses track of the specifics of the geometrical setting and obtains universal limiting correlations. More precisely, such a universal limit occurs if one chooses the coordinates properly.

::: theo
[]{#usls label="usls"} Scaling limits of correlations of zeros and critical points are universal. That is: $$\frac{1}{ N^{2k}} K_{2k}^N\left(\frac{z^1}{\sqrt{N}}, 
\frac{z^2}{\sqrt{N}}\right) \to K_{2km}^{\infty}(z^1,z^2)$$ in the sense of measures.
:::

The limit correlation function denoted $K_{2km}^{\infty}(z^1,z^2)$ is unique within a universality class for each statistic under consideration. In the complex and almost-complex cases, there exists a limit correlation function $K_{2km}^{{\mathbb C}, zeros, \infty}(z^1,z^2)$ of zeros, and another limit correlation function $K_{2km}^{{\mathbb C}, crits, \infty}(z^1,z^2)$ for critical points. There are analogous results in the real case. The limit correlations are explicitly computable. In [@BSZ1] and elsewhere we give explicit formulae for low values of $m$ and graph the results. The result for zeros in dimension one agrees with the formula of Hanny [@Ha] on ${\mathbb C}{\mathbb P}^1$, as it must since the result is universal. We now briefly describe the elements of the proof. The details differ, but the principles are the same, for complex and real cases, and for zeros or critical points. Hence we concentrate on zeros in the complex case.

### Step One: Relating correlations and joint probability distributions

Following an idea due originally to Kac and Rice in the case of real polynomials of one variable, we express the correlation measures in terms of the joint probability distribution of the random variables $s(z^1),\dots,s(z^n),
\nabla s(z^1),\dots,\nabla s(z^n)$. This JPD is defined by $$\widetilde{\mathbf D}_{z}^N:=
\widetilde D_{n}^N(x,\xi,z)dxd\xi=(J_z)_*\nu_N\,,
\;\;J_{z}(s) = (s(z), \nabla s(z)),$$ i.e. it is the push-forward of the Gaussian measure $\gamma_N$ under the linear jet map $J(z)$.

The desired expression for correlations in terms of the JPD is given by the following generalization of the Kac-Rice formula [@K] to the geometric setting of this article:

::: theo
[]{#introdn label="introdn"} [@BSZ1; @BSZ3; @SZ2] In the case of correlations of complex zeros, we have: $$K_{2k}^N(z)=
\int d\xi\,\widetilde D_n^N(0,\xi,z)\prod_{p=1}^n
\det(\xi^{p}\xi^{p*})\,.$$
:::

Analogous formulae exist for critical points, but involve the jet maps $(\nabla s(z), \nabla^2 s(z))$. The real case is similar to the complex case, but is somewhat more complicated because $\Pi_N$ is oscillatory rather than exponentially decaying [@N].

### Step two: scaling asymptotics of the JPD

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

## Hole probabilities

Another application of the scaling applications is to 'hole probabilities', i.e. the probability that a ball $B_{r}(z_0)$ of radius $r$ around a point $z_0 \in M$ is zero-free. The following result combines our scaling asymptotics and Sodin's reformulation (and substantial simplification) of Offord's large deviations results on hole probabilities for entire analytic functions in the plane [@O; @So]. It is based on the Poincare-Lelong formula, so at this time of writing it has only been proved for one holomorphic section, and no comparable results have been proved for random spherical harmonics.

::: theo
Let $P_N(D; z_0) = Prob\{s \in H^0(M, L^N): Z_s \cap B_{\frac{D}{\sqrt{N}}}(z_0) = \emptyset\}.$ Then there exists positive constants $C_1, C_2$ such that, for any $N$, $P_N(D; z_0) \leq C_1 e^{-C_2 D^2}.$
:::
