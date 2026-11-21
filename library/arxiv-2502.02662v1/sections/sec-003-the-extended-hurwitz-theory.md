---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-003-the-extended-hurwitz-theory
section_title: "The Extended Hurwitz Theory"
section_number: null
pages: 4-6
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.982
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
[]{#ExtendedHurwitz label="ExtendedHurwitz"} In the context of the string description of two-dimensional Yang-Mills theory, one needs to sum over covering maps of all degrees $d$ [@Gross:1992tu; @Gross:1993hu]. This motivates the introduction of an overarching grand canonical version of the Hurwitz theories with gauge groups $S_d$ that takes into account coverings of all degrees simultaneously [@IvanovKerov; @OP1; @Benizri:2024mpx].[^1]

In the process, we move from a two-dimensional Dijkgraaf-Witten theory with a finite gauge group to a topological quantum field theory defined by a Frobenius algebra only.

To treat all degrees $d$ simultaneously, we introduce an operator algebra which is the algebra of orbits of partial permutations $\mathcal{A}_{\infty}$ of an infinite set [@IvanovKerov; @Benizri:2024mpx]. We provide a brief review of partial permutations here and refer the reader to [@IvanovKerov; @Benizri:2024mpx] for more details.

A partial permutation is a pair $(d,\rho)$, where $d$ is a subset of ${\mathbb N}$ and $\rho$ is a permutation of elements in $d$. We refer to $d$ as the support of the partial permutation.[^2] An element $\sigma$ of the symmetric group $S_{\infty}$ acts on partial permutations as $$\sigma\cdot (d,\rho)=(\sigma(d), \sigma \rho \sigma^{-1})\, .$$ The orbits $A_r$ of the algebra of partial permutations $\mathcal{A}_{\infty}$ under this action are of the form $$A_{r}=\sum_{(d,\rho)\in [r]} (d,\rho)\, ,$$ where $[r]$ denotes an orbit of partial permutations that is indexed by partitions of integers. The product of partial permutations is defined by concatenating their supports and multiplying their permutations $$(d_1,\rho_1)\cdot (d_2, \rho_2) = (d_1\cup d_2, \rho_1 \rho_2)\, .$$ The product of orbits is defined accordingly. Once the algebra is fixed, we only further need to define the one-point functions on the algebra of partial permutations $\mathcal{A}_{\infty}$ to fix all correlation functions. To that end, we first introduce a fixed-degree one-point function on a Riemann surface of genus $G$: $$\langle A_r \rangle_{d,G} := \binom{m_{1}(\rho)}{m_{1}(r)} \langle C_{\rho} \rangle_{d,G}\, ,
     \label{FixedDegreeOnePoint}$$ where $\rho$ denotes the permutation obtained by trivially completing the partial permutation $r$ and $m_{1}(r)$ (respectively $m_{1}(\rho)$) is the number of inert entries of the partial permutation (respectively permutation).

Note that $m_{1}(\rho)-m_{1}(r)=d-\lvert d_r \rvert$, where $d_r$ is the support of a partial permutation in the orbit $A_r$. The definition [\[FixedDegreeOnePoint\]](#FixedDegreeOnePoint){reference-type="eqref" reference="FixedDegreeOnePoint"} is valid for $\lvert d_r \rvert < d$. For $\lvert d_r \rvert>d$, we set $\langle A_r \rangle_{d,G}=0$.

We now define the physical one-point function as $$\langle A_r \rangle_G = \sum_d p^d  \langle A_r \rangle_{d,G}\, .
    \label{ppOnePoint}$$

Importantly, our grand canonical formulation of a Hurwitz theory allows for the introduction of a chemical potential $p$ which explicitly keeps track of the degree of the maps that contribute to a given correlator. The sum over degrees can be traded for a sum over the genus of the covering surface by using the Riemann-Hurwitz formula. Let us study this for the example of partial permutations $r$ that consist of a single cycle $k$. The correlation functions of the grand canonical symmetric orbifold theory on a Riemann surface of genus $G$ are then shown to exhibit the structure of string correlators $$\langle A_{k_1}\cdots A_{k_n} \rangle_G  = \sum_g g_s^{2g-2} \langle g_s^{-k_1+1} A_{k_1}\cdots g_s^{-k_n+1}  A_{k_n} \rangle_{g,G}\,$$

provided that we make the identification $p=g_s^{2G-2}$ and that we define normalized partial permutations $A'_r:=g_s^{\lvert d_r \rvert} A_r$.[^3] This observation is consistent with the behavior of a general symmetric orbifold theory on the sphere [@Aharony:2024fid].

With this normalization, the generic correlation function becomes $$\langle A'_{r_1}\cdots A'_{r_n} \rangle  = \sum_g g_s^{2g-2} \langle g_s^{\ell(r_1)} A_{r_1}\cdots g_s^{\ell(r_n)} A_{r_n} \rangle_{g}\, ,$$ where the length $l(r)$ of a partial permutation $r$ counts the number of parts in the partition $[r]$ of $|d_r|$.

[^1]: This is a first essential supplementary tool that will distinguish our treatment of two-dimensional Yang-Mills theory from those in the literature.

[^2]: For a given cover, the set $d$ labels the sheets of the cover. The permutation codes a reshuffling of sheets due to ramification. Some sheets may not be shuffled.

[^3]: Note that on the torus, the genus of the Riemann surface is determined solely by the insertions. The identification $p=g_s^{2G-2}$ yields a trivial chemical potential $p=1$ and the normalization of partial permutations must be put in by hand.
