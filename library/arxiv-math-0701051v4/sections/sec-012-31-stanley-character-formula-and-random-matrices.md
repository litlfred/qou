---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-012-31-stanley-character-formula-and-random-matrices
section_title: "Stanley character formula and random matrices"
section_number: 3.1
pages: 8-10
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.962
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
Let $\lambda$ be a Young diagram and $N\geq r(\lambda),c(\lambda)$. We consider a random matrix $T_\lambda=(t_{ij})_{1\leq i,j\leq N}$ such that

-   its entries $(t_{ij})$ are independent random variables;

-   if $(i,j) \in \lambda$ then $t_{ij}$ is a complex centered Gaussian variable, that is to say that $$\mathbb{E}(t_{ij}) =0, \quad 
    \mathbb{E}(t_{ij} \overline{t_{ij}}) = 1, \quad
    \mathbb{E}(t_{ij}^2) =0;$$

-   otherwise, if $(i,j) \notin \lambda$ then $t_{ij}=0$.

The moments of $T_\lambda
T_\lambda^\star$ are given by a formula which is very similar to the Stanley formula for characters (Theorem [\[theo:character-sniady\]](#theo:character-sniady){reference-type="ref" reference="theo:character-sniady"}):

::: theorem
[]{#theo:random-matrices label="theo:random-matrices"} With the definitions above and $\pi \in S_l$ with a cycle decomposition $k_1,\ldots,k_r$ $$\label{eq:moments-matrix}
\mathbb{E}\big(\mathop{\mathrm{Tr}}(T_\lambda T_\lambda^\star)^{k_1} \cdots \mathop{\mathrm{Tr}}(T_\lambda
T_\lambda^\star)^{k_r} \big)=\sum_{\substack{\sigma_1,\sigma_2 \in S_l \\
\sigma_1 \sigma_2=\pi}} N^\lambda(\sigma_1,\sigma_2).$$
:::

::: proof
*Proof.* The first step is to expand the product and the trace on the left-hand side: $$\begin{aligned}
\mathbb{E}\big(\mathop{\mathrm{Tr}}(T_\lambda T_\lambda^\star)^{k_1} \ldots \mathop{\mathrm{Tr}}(T_\lambda T_\lambda^\star)^{k_r} \big) \hspace{-5cm}\\
&=&\mathbb{E}\Bigg[ \Big(\sum_{i^1_1,j^1_1,\ldots,i^1_{k_1},j^1_{k_1}} t_{i^1_1 j^1_1}
\overline{t_{i^1_2 j^1_1}} \ldots t_{i^1_{k_1} j^1_{k_1}} \overline{t_{i^1_1
j^1_{k_1}}} \Big)\\
& &\hspace{1,5cm} \ldots \Big(\sum_{i^r_1,j^r_1,\ldots,i^r_{k_r},j^r_{k_r}}
t_{i^r_1 j^r_1} \overline{t_{i^r_2 j^r_1}} \ldots t_{i^r_{k_r} j^r_{k_r}}
\overline{t_{i^r_1 j^r_{k_r}}} \Big) \Bigg]\\
&= &


\sum_{i_1,j_1,\ldots,i_l,j_l} \mathbb{E}\left[
\prod_{m=1}^l t_{i_m j_m} \overline{t_{i_{\pi(m)} j_m}} \right].
\end{aligned}$$ Since random variables $(t_{ij})$ are Gaussian, we can apply Wick formula (see [@Zvonkin1997]) to each summand; in order to do this we need to consider all ways of pairing factors $(t_{i_m,j_m})$ with factors $(\overline{t_{i_{\pi(m)} j_m}})$. Each such a pairing can be identified with a permutation $\sigma\in S_l$: therefore

$$\mathbb{E}\left[ \prod_{m=1}^l t_{i_m j_m} \overline{t_{i_{\pi(m)}
j_m}} \right]=\sum_{\sigma \in S_l} \left[ \prod_{m=1}^l
\mathbb{E}\left(t_{i_{\sigma(m)} j_{\sigma(m)}} \overline{t_{i_{\pi(m)} j_m}}\right)
\right]$$

Using the definition of $T$, this is equal to $$\sum_{\sigma \in S_l} \prod_{m=1}^l  [i_{\sigma(m)}=i_{\pi(m)}] \  [j_{\sigma(m)}=j_m] \
[(i_{\sigma(m)},j_{\sigma(m)}) \in \lambda].$$

If we plug this in our calculation, the left-hand side of [\[eq:moments-matrix\]](#eq:moments-matrix){reference-type="eqref" reference="eq:moments-matrix"} is equal to $$\begin{gathered}





\sum_{\sigma \in S_l} \sum_{i_1,j_1,\ldots,i_l,j_l} \left( \prod_{m=1}^l
[i_{\sigma(m)}=i_{\pi(m)}] \  [j_{\sigma(m)}=j_m] \
[(i_{\sigma(m)},j_{\sigma(m)}) \in \lambda] \right).
\end{gathered}$$ If we denote $\sigma_1=\pi \sigma_2^{-1}$, $\sigma_2=\sigma$ then the sum over $\sigma$ can be seen as a sum over all $\sigma_1,\sigma_2\in S_l$ such that $\sigma_1\sigma_2=\pi$. If a sequence $i_1,\dots,i_l$ (respectively, sequence $j_1,\dots,j_l$) contributes to the above sum then it must be constant on each cycle of $\sigma_1$ (respecively, each cycle of $\sigma_2$). It follows that there is a bijective correspondence between sequences $i_1,j_1,\dots,i_l,j_l$ which contribute to the above sum and colorings of the cycles of $\sigma_1$ and $\sigma_2$ which are compatible with $\lambda$. ◻
:::

By comparing the above result with Theorem [\[theo:character-sniady\]](#theo:character-sniady){reference-type="ref" reference="theo:character-sniady"}, we obtain the following corollary.

::: corollary
Let $\lambda$ be a Young diagram.

Then for any permutation $\pi\in S_l$ with a cycle decomposition $k_1,\dots,k_r$ $$|\Sigma^{\lambda}(\pi)| \leq  \mathbb{E}\big(\mathop{\mathrm{Tr}}(T_\lambda T_\lambda^\star)^{k_1}
\cdots \mathop{\mathrm{Tr}}(T_\lambda
T_\lambda^\star)^{k_r} \big).$$
:::

We shall not follow this idea in this article and we will prove all estimates from scratch, but it is worth noticing that the above Corollary shows that the asymptotics of characters of symmetric groups can be deduced from the corresponding asymptotics of random matrices. In particular it follows that

when the lengths $k_1,\dots,k_r$ of the cycles of $\pi$ are big enough then the asymptotics of the corresponding character is related to the limit distribution of the largest eigenvalue of $T_{\lambda}T^\ast_{\lambda}$ [@SinaiSoshnikov1998]. Notice, however, that due to the minus sign in Theorem [\[theo:character-sniady\]](#theo:character-sniady){reference-type="ref" reference="theo:character-sniady"} and the resulting cancelations the character $|\Sigma^{\lambda}(\pi)|$ could, at least in priciple, be much smaller than the appropriate moment of the random matrix $T_{\lambda}T_{\lambda}^\ast$.
