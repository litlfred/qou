---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-002-the-hurwitz-theory-at-fixed-degree
section_title: "The Hurwitz Theory at Fixed Degree"
section_number: null
pages: 4-4
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.98
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
The Hurwitz theory is the topological quantum field theory in two dimensions with gauge group equal to the symmetric group $S_d$.[^1] The operators of the Hurwitz theory are in one-to-one correspondence with the conjugacy classes of the symmetric group $S_d$, or equivalently, with the partitions of $d$. The algebra of operators is the algebra $\mathcal{C}_d$ of conjugacy classes of the symmetric group $S_d$, which is the center of the group algebra $\mathbb{C}[S_d]$. There is a basis of operators $C_{\xi}$ which is the sum of permutation elements in a given conjugacy class $\xi$. One can also think of operator insertions as adding boundaries to the surface. A given operator then corresponds to a particular holonomy condition on this boundary up to conjugacy. To study the correlators of Hurwitz theory, it is useful to introduce a Fourier transformation on the space of conjugacy classes of the symmetric group. The Fourier space is the space of shifted-symmetric functions, and the Fourier map sends a conjugacy class sum $C_{\xi}$ to the shifted-symmetric polynomial $$f_{\xi}(\lambda):=\lvert C_{\xi} \rvert\cdot  \frac{\chi_{\lambda}(\xi)}{d_\lambda} \, ,
   \label{GeneralizedCharacters}$$ where $\chi_{\lambda}(\xi)$ is the character of an element in the conjugacy class $\xi$ in the representation $\lambda$ of the symmetric group $S_d$, $d_{\lambda}$ is the dimension of this representation and $\lvert C_{\xi} \rvert$ is the number of elements in the conjugacy class. The correlators of the theory on a Riemann surface $M_G$ of genus $G$ are given by Hurwitz numbers and can be written, up to an overall normalization by the partition function $Z[M_{G}]$ [@Benizri:2024mpx], as: $$\begin{aligned}
Z[M_{G},\xi_i] &= H_{G,d}(C_{\xi_1},\dots, C_{\xi_k}) \label{OnePointBasic}\\
               &=\sum_{\lambda \vdash d}\left(\frac{d_{\lambda}}{d!}\right)^{2-2G}
                \prod_{i=1}^k f_{\xi_i}(\lambda)\,.
      
               
\label{PartitionFunctions}
\end{aligned}$$ These observables can be interpreted as a sum on the Fourier space labeled by representations $\lambda$ with a generalized Plancherel measure. Furthermore, the operator algebra can be exploited to reduce correlation functions to the calculation of structure constants and one-point functions. In principle, the one-point function should be normalized by the partition function of the manifold in the absence of insertions. However, to simplify the comparison between the various theories, we will ignore the issue of normalizations and refer to $$\langle C_{\xi} \rangle_{G,d} := Z[M_{G},\xi]$$ as the one-point function of the theory.

[^1]: Alternatively, it is the topological symmetric orbifold of a trivial theory, which contains only the identity operator.
