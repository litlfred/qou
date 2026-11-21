---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-005-a-collection-of-sum-formulas
section_title: "A collection of sum formulas"
section_number: null
pages: 6-7
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.934
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
To summarize, we can reproduce the whole collection of the single-Schur sums from [@Mac secs.1.5,3.4,3.5].

They are naturally divided in three blocks, and the formulas are given also in terms of symmetric variables $x_i$ such that $p_k=\sum_ix_i^k$.

**1.** The first one is already familiar $$\begin{aligned}
\label{1}
\sum_RS_R=\prod_i{1\over 1-x_i}\prod_{i<j}{1\over 1-x_ix_j}
= \exp\left\{\sum_{k=1}^\infty \left({p_k^2\over 2k}+{p_{2k-1}\over 2k-1}\right)\right\}\\
\sum_{R\ even}S_R=\prod_i{1\over 1-x_i^2}\prod_{i<j}{1\over 1-x_ix_j}
=\exp\left\{\sum_{k=1}^\infty\left({p_k^2\over 2k}+{p_{2k}\over 2k}\right)\right\}\\
\sum_{R^\vee\ even}S_R=\prod_{i<j}{1\over 1-x_ix_j}=
\exp\left\{\sum_{k=1}^\infty\left({p_k^2\over 2k}-{p_{2k}\over 2k}\right)\right\}\\
\sum_R(-1)^{\nu_R}S_R=\prod_i{1\over 1-x_i}\prod_{i<j}{1\over 1+x_ix_j}=
\exp\left\{\sum_{k=1}^\infty\left((-1)^k{p_k^2\over 2k}+{p_{2k-1}\over 2k-1}+{p_{4k-2}\over 2k-1}\right)\right\}\\
\sum_Rt^{c_R}S_R=\prod_i{1\over 1-tx_i}\prod_{i<j}{1\over 1-x_ix_j}
=\exp\left\{\sum_{k=1}^\infty\left({p_k^2\over 2k}+t^{2k-1}{p_{2k-1}\over 2k-1}+(t^{2k}-1){p_{2k}\over 2k}\right)\right\}\\
\sum_Rt^{r_R}S_R=\prod_i{1+tx_i\over 1-x_i^2}\prod_{i<j}{1\over 1-x_ix_j}
=\exp\left\{\sum_{k=1}^\infty\left({p_k^2\over 2k}+t^{2k-1}{p_{2k-1}\over 2k-1}+(1-t^{2k}){p_{2k}\over 2k}\right)\right\}
\end{aligned}$$ where $c_R$ ($r_R$) is the number of rows (lines) of odd length, and $\nu_R=\sum_i(i-1)R_i$. The first three lines follow from the last two lines upon putting $t=0,1$.

**2.** The second block involves the skew Schur functions: $$\begin{aligned}
\sum_RS_{R/Q}=\prod_i{1\over 1-x_i}\prod_{i<j}{1\over 1-x_ix_j}\sum_PS_{Q/P}
=\exp\left\{\sum_{k=1}^\infty\left({p_k^2\over 2k}+{p_{2k-1}\over 2k-1}\right)\right\}\sum_PS_{Q/P}\\
\sum_{R\ even}S_{R/Q}=\prod_i{1\over 1-x_i^2}\prod_{i<j}{1\over 1-x_ix_j}\sum_{P\ even}S_{Q/P}
=\exp\left\{\sum_{k=1}^\infty\left({p_k^2\over 2k}+{p_{2k}\over 2k}\right)\right\}\sum_{P\ even}S_{Q/P}\\
\sum_{R^\vee\ even}S_{R/Q}=\prod_{i<j}{1\over 1-x_ix_j}\sum_{P^\vee\ even}S_{Q/P}
=\exp\left\{\sum_{k=1}^\infty\left({p_k^2\over 2k}-{p_{2k}\over 2k}\right)\right\}\sum_{P^\vee\ even}S_{Q/P}
\end{aligned}$$ for arbitrary $Q$.

**3.** The third direction is generalizations of these formulas to the Macdonald polynomials. We do not provide relevant averages for this case in order to avoid overloading the text with unnecessary complicated formulas. Still, we list the results. Denote $$\begin{aligned}
H_R^{el}:=\prod_{{(i,j)\in R}\atop{R_j^\vee-i\ even}}{1-q^{R_i-j}t^{R_j^\vee-i+1}\over 1-q^{R_i-j+1}t^{R_j^\vee-i}},
\ \ \ \ \ H_R^{oa}:=\prod_{{(i,j)\in R}\atop{R_i-j\ odd}}{1-q^{R_i-j}t^{R_j^\vee-i+1}\over 1-q^{R_i-j+1}t^{R_j^\vee-i}}
\end{aligned}$$ The full product $H_R$ is just the coefficient that stands in the sum of the Cauchy identity: $$\begin{aligned}
\sum_RH_RM_R\{p_k\}M_R\{\bar p_k\}=
\prod_{i,j}{(tx_i\bar x_j;q)_\infty\over (x_i\bar x_j;q)_\infty}=\exp\left\{\sum_{k=1}^\infty\left({1-t^k\over 1-q^k}{p_k\bar p_k\over k}\right)
\right\}
\end{aligned}$$ with $p_k=\sum_ix_i^k$, $\bar p_k=\sum_i\bar x_i^k$. Then, $$\begin{aligned}
\sum_RH_R^{el}M_R=\prod_i{(tx_i;q)_\infty\over (x_i;q)_\infty}\prod_{i<j}{(tx_ix_j;q)_\infty\over (x_ix_j;q)_\infty}=
\exp\left\{\sum_{k=1}^\infty {1-t^k\over 1-q^k}\left({p_k^2\over 2k}+{p_{2k-1}\over 2k-1}\right)\right\}\\
\sum_RH_R^{oa}M_R=\prod_i{(qtx_i^2;q^2)_\infty\over (1-x_i)(q^2x_i^2;q^2)_\infty}
\prod_{i<j}{(tx_ix_j;q)_\infty\over (x_ix_j;q)_\infty}=
\exp\left\{\sum_{k=1}^\infty\left({1-t^k\over 1-q^k}{p_k^2\over 2k}+{t^k-q^k\over 1+q^k}{p_{2k}\over 2k}+{p_{2k-1}\over 2k-1}\right)
\right\}\\
\sum_{R^\vee\ even}H_R^{el}M_R=\prod_{i<j}{(tx_ix_j;q)_\infty\over (x_ix_j;q)_\infty}=
\exp\left\{\sum_{k=1}^\infty {1-t^k\over 1-q^k}\left({p_k^2\over 2k}-{p_{2k}\over 2k}\right)\right\}\\
\sum_{R\ even}H_R^{oa}M_R=\prod_i{(qtx_i^2;q^2)_\infty\over (x_i^2;q^2)_\infty}
\prod_{i<j}{(tx_ix_j;q)_\infty\over (x_ix_j;q)_\infty}=\prod_{i<j}{(tx_ix_j;q)_\infty\over (x_ix_j;q)_\infty}=
\exp\left\{\sum_{k=1}^\infty\left({1-t^k\over 1-q^k}{p_k^2\over 2k}+{1+t^k\over 1+q^k}{p_{2k}\over 2k}\right)\right\}
\end{aligned}$$
