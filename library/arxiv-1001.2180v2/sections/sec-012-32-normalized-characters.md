---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-012-32-normalized-characters
section_title: "Normalized characters"
section_number: 3.2
pages: 9-10
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.948
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
Another graded algebraic basis may be considered: the normalized characters $(\varSigma_k)_{k \geq 1}$. If $\rho$ and $\lambda$ are two partitions of respective sizes $k$ and $n$, we define the following function on $\mathscr{Y}$: $$\varSigma_\rho(\lambda)=\begin{cases}
                      n^{\downarrow k}\,\chi^\lambda(\sigma_{\rho\,1^{n-k}})&\text{if }k\leq n\\
                          0 & \text{if } k>n,
                          \end{cases}$$ where $n^{\downarrow k}=n(n-1)\cdots(n-k+1)$ is the $k$-th falling factorial of $n$, the notation $\chi^\lambda$ stands for the normalized character of the symmetric group, the partition $\rho'=\rho\,1^{n-k}$ is the partition $\rho$ completed with parts of size $1$, and $\sigma_{\rho'}$ is any permutation in $\mathfrak{S}_n$ with cycle decomposition of type $\rho'$.

In the case where $\lambda$ has only one part (character values on cycles), by using the Frobenius formula $\varsigma^\lambda(\rho)=\left\langle s_\lambda\vphantom{p_\rho}\,\right |\left.p_\rho \vphantom{s_\lambda}\right\rangle$ (*cf.* [@Mac95 §1.7], and in particular the corollary 1.7.7), it can be shown that $\varSigma_k$ is a polynomial in the $(p_l)_{l \leq k}$. To compute these polynomials, one can use the following Proposition (see [@IO02 Propositions 3.3 and 3.4, 4.4 and 4.5]):

::: proposition
[]{#prop:sigma_pk label="prop:sigma_pk"} If $k\geq 1$, the observable $\varSigma_k$ can be expressed in terms of power sums *via* the following formula $$\label{eq:p_fct_sigma}
\varSigma_k=[t^{k+1}] \left\{-\frac{1}{k}\,\prod_{j=1}^k (1-(j-1/2)t)\,\cdot\,\exp\left(\sum_{j=1}^\infty \frac{p_j\,t^j}{j}\,(1-(1-kt)^{-j}) \right)\right\}.$$ As a consequence, the top homogeneous component of $\varSigma_k$ is $p_k$, and $(\varSigma_k)_{k \geq 1}$ is an algebraic basis of the algebra $\mathscr{O}$.
:::

::: examples
$\varSigma_{1}=p_{1}$, $\varSigma_{2}=p_{2}$, $\varSigma_{3}=p_{3}-\frac{3}{2} p_{11}+\frac{5}{4}p_{1}$, $\varSigma_{4}=p_{4}-4p_{21}+\frac{11}{2}p_{2}$.
:::
