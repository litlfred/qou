---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-006-the-observables-of-two-dimensional-yang-mills-th
section_title: "The Observables of Two-dimensional Yang-Mills Theory"
section_number: null
pages: 9-10
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 1.0
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
[]{#YMObservables label="YMObservables"} Two-dimensional Yang-Mills theory is invariant under area-preserving diffeomorphisms [@Witten:1991we] and therefore has no local observables. It is a prototypical example of an area dependent quantum field theory [@Runkel:2018uls], which is a mild generalization of a topological quantum field theory.

The observables of two-dimensional Yang-Mills theory are Wilson loops on the one hand and on the other hand partition functions on Riemann surfaces with boundaries with prescribed holonomies. From the point of view of topological field theories, the former corresponds to line defects and the latter to insertions of local operators. Indeed, the boundary holonomies are indexed by conjugacy classes of the unitary group. In a topological setting, one can proceed to shrink the boundaries down to singular points characterized by corresponding insertions of conjugacy classes of the unitary group. The situation is akin to the treatment of closed string vertex operators on the world-sheet in string theory. We will adopt this same point of view here, and treat the partition functions of Yang-Mills with boundaries as correlators of local insertions.[^1] In this paper, we focus on this class of observables. We remark on Wilson loops in section [\[WilsonLoops\]](#WilsonLoops){reference-type="ref" reference="WilsonLoops"}.

The correlators of pure Yang-Mills theory with gauge group $U(N)$ and coupling constant $g_{YM}$ on a Riemann surface of genus $G$ and area $A$ read -- see e.g. [@Blau:1991mp] for a pedagogical derivation -- : $$Z[M_G,U_i]=\sum_{\lambda\in Y_N} \left(\prod_{i=1}^{k} s_{\lambda}(U_i)\right) (\dim W_N^{\lambda})^{2-2G-k} \exp\left(-\frac{g_{YM}^2A}{2N}\, c_{2}(\lambda)\right)\, ,
    \label{YMPartitions}$$ where the sum runs over representations $W_N^{\lambda}$ of the unitary group which are indexed by Young diagrams $\lambda$ with at most $N$ rows.

The set of such diagrams is denoted $Y_N$. Moreover, the partition functions are functions of the holonomy classes $U_i$ of the gauge field on the boundaries. We denoted by $s_{\lambda}(U_i)$ the character of an element of the conjugacy class $U_i$ in the representation $W^{\lambda}_N$. Finally, $c_{2}(\lambda)$ is the quadratic Casimir of the representation $W^{\lambda}_N$. Note that the coupling constant $g_{YM}$ and the area $A$ always appear in the correlators (and in the Wilson lines) in the combination $g_{YM}^2A$. In other words, the dimensionless coupling constant of the theory is $g_{YM}^2A$.

It will be useful to split the sum over representations into two parts and write $$\sum_{\lambda\in Y_N} = \sum_d \sum_{\lambda\in Y^d_N}\, ,$$ where $Y^d_N$ is the set of Young diagrams of less than $N$ rows and with $d$ boxes. We refer to the quantities obtained by only carrying out the second sum, i.e. by restricting the sum in equation [\[YMPartitions\]](#YMPartitions){reference-type="eqref" reference="YMPartitions"} to Young diagrams with exactly $d$ boxes, as fixed-degree correlators. We will denote these correlators $Z_d$.

Let us argue that fixed-degree correlators are sensible in the whole theory -- they manifestly suffice to compute the whole theory. Indeed, the quantities $Z_d$ are observables. To prove this, we can take a dual perspective on boundaries and associate to each boundary of the manifold an irreducible representation of the gauge group $U(N)$ -- see e.g. [@Witten:1991we]. The representations must coincide to ensure that resulting correlators do not vanish [@Witten:1991we]. We index the unique irreducible representation at hand by a Young diagram $\mu$ and write $$\begin{aligned}
    Z_{\mu}[M_{g,k}] &=\int dU_1\dots dU_k\cdot Z[U_1,\dots, U_k]\cdot s_{\mu}(U_1^{-1})\cdots  s_{\mu}(U_k^{-1})\\
    &=(\dim W_N^{\mu})^{2-2G-k} \exp\left(-\frac{g_{YM}^2A}{2N}\, c_{2}(\mu)\right)\, .
\end{aligned}$$ The fixed-degree correlators $Z_d$ are linear combinations of the partition functions $Z_{\mu}$, which implies that they are observables. This proves that these correlators are necessary and sufficient ingredients to describe the full theory. From here on out, we refer to the set of partition functions $Z_d$ of Yang-Mills correlators at fixed-degree $d$ as the degree $d$ sector of the theory.

[^1]: In particular, one can define a hole operator algebra. Holonomies $U_1$ and $U_2$ may be replaced in all correlation functions by linear combinations of a single holonomy $U_3$. This perspective is developed further at the end of section [\[TheDualityMap\]](#TheDualityMap){reference-type="ref" reference="TheDualityMap"}.
