---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-008-21-young-symmetrizer
section_title: "Young symmetrizer"
section_number: 2.1
pages: 5-7
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.958
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
Let $\lambda$ be a Young diagram consisting of $n$ boxes. In the following we will distinguish the symmetric group $S_n$ which permutes the elements $\{1,\dots,n\}$ and the symmetric group $\tilde{S}_n$ which permutes the boxes of $\lambda$.

For a box $\Box\in\lambda$ we denote by $r(\Box)\in\mathbb{N}$ (respectively, $c(\Box)\in\mathbb{N}$) the row (respectively, the column) of $\Box$; in this way $\Box=(c(\Box),r(\Box))$.

If $\sigma\in \tilde{S}_n$ has a property that if two different boxes $\Box_1,\Box_2$ are in the same row then their images $\sigma(\Box_1),\sigma(\Box_2)$ are not in the same column

then we define its number of column inversions $\mathop{\mathrm{cinv}}(\sigma)$ as the number of pairs $\Box_1,\Box_2$ such that $\sigma(\Box_1),\sigma(\Box_2)$ are in the same column, $r(\Box_1)<r(\Box_2)$ and $r(\sigma(\Box_1))>r(\sigma(\Box_2))$. If $\sigma\in \tilde{S}_n$ does not have this property, then we define $(-1)^{\mathop{\mathrm{cinv}}(\sigma)}=0$.

The following theorem gives a very esthetically appealing formula for the characters of the symmetric groups.

::: theorem
[]{#theo:bubu label="theo:bubu"} Let a Young diagram $\lambda$ having $n$ boxes and $\pi\in S_n$ be given. Let $\hat{\pi}\in \tilde{S}_n$ be a random permutation distributed with the uniform distribution on the conjugacy class defined by $\pi$. Then $$\chi^{\lambda}(\pi)= \mathbb{E}[(-1)^{\mathop{\mathrm{cinv}}(\hat{\pi})}].$$
:::

::: proof
*Proof.* We denote $$\begin{aligned}
P_{\lambda}=& \{\sigma\in \tilde{S}_n \colon \sigma \text{ preserves each row
of }\lambda \}, \\
Q_{\lambda}=& \{\sigma\in \tilde{S}_n \colon \sigma \text{ preserves each column
of }\lambda \}
\end{aligned}$$ and define $$\begin{aligned}
a_{\lambda} = & \sum_{\sigma\in P_{\lambda}} \sigma \in \mathbb{C}[\tilde{S}_n],\\
b_{\lambda} = & \sum_{\sigma\in Q_{\lambda}} (-1)^{|\sigma|} \sigma \in \mathbb{C}[\tilde{S}_n],\\
c_{\lambda} = &  b_{\lambda} a_{\lambda}.
\end{aligned}$$

It is well-known that $p_{\lambda}=\alpha_{\lambda} c_{\lambda}$ is an idempotent for a constant $\alpha_\lambda$ which will be specified later. Its image $V_{\lambda} = \mathbb{C}[\tilde{S_n}] p_{\lambda}$ under multiplication from the right on the regular representation gives a representation $\rho^{\lambda}$ (where the symmetric group acts by left multiplication) associated to a Young diagram $\lambda$. It turns out that $\alpha_{\lambda}=\frac{\mathop{\mathrm{dim}}V_{\lambda}}{n!}$.

It follows that for $\tilde{\pi}\in \tilde{S}_n$ $$\begin{gathered}
\label{eq:charakter-babab} 
n! \frac{\mathop{\mathrm{Tr}}\rho^{\lambda}(\tilde{\pi})}{\mathop{\mathrm{dim}}V_{\lambda}}
= \frac{\mathop{\mathrm{Tr}}\rho^{\lambda}(\tilde{\pi}^{-1})}{\alpha_{\lambda}} = 

\frac{1}{\alpha_{\lambda}} \sum_{\mu\in \tilde{S}_n} 
 \langle \delta_{\mu}, \tilde{\pi}^{-1} \delta_\mu p_{\lambda}\rangle
= \\
\sum_{\mu\in \tilde{S}_n} \sum_{\tilde{\sigma}_1\in Q_{\lambda}} 
\sum_{\tilde{\sigma}_2\in P_{\lambda}}
(-1)^{|\tilde{\sigma}_1|} [\mu =\tilde{\pi}^{-1} \mu \tilde{\sigma}_1 \tilde{\sigma}_2].
\end{gathered}$$

We define $\hat{\pi}=\mu^{-1} \tilde{\pi} \mu$. For such a permutation $\hat{\pi}$ there exists at most one factorization $\hat{\pi}=\tilde{\sigma}_1 \tilde{\sigma}_2$; by Young lemma this factorization exists if and only if $(-1)^{\mathop{\mathrm{cinv}}(\hat{\pi})}\neq 0$. Furthermore, if such a factorization exists then $(-1)^{|\sigma_1|}=(-1)^{\mathop{\mathrm{cinv}}(\hat{\pi})}$. It follows that $$n! \frac{\mathop{\mathrm{Tr}}\rho^{\lambda}(\tilde{\pi})}{\mathop{\mathrm{dim}}V_{\lambda}}=
\sum_{\mu\in \tilde{S}_n} 
(-1)^{\mathop{\mathrm{cinv}}(\mu^{-1} \tilde{\pi} \mu)}.$$ As $\mu$ runs over all permutations, $\hat{\pi}=\mu^{-1} \tilde{\pi} \mu$ runs over all elements of the conjugacy class defined by $\pi$ which finishes the proof. ◻
:::

For permutations $\sigma_1,\sigma_2\in S_l$ we define $\tilde{N}^{\lambda}(\sigma_1,\sigma_2)$ as the number of one-to-one functions $f$ from $\{1,\dots,l\}$ to the set of boxes of $\lambda$ with a property that $r\circ f$ is constant on each cycle of $\sigma_2$ and $c\circ f$ is constant on each cycle of $\sigma_1$.

::: proposition
[]{#prop:bubu2 label="prop:bubu2"} Let $\lambda$ be a Young diagram having $n$ boxes. For any permutation $\pi\in S_l$ (where $l\leq n$) $$\Sigma^{\lambda}(\pi)= \sum_{\substack{\sigma_1,\sigma_2\in S_l\\ \sigma_1 \sigma_2=\pi}}
(-1)^{|\sigma_1|} \tilde{N}^{\lambda}(\sigma_1,\sigma_2).$$
:::

::: proof
*Proof.* Let us consider the case $l=n$. Let $\tilde{\pi}\in\tilde{S}_n$ be any permutation with the same cycle structure as $\pi\in S_n$. Our starting point is the analysis of [\[eq:charakter-babab\]](#eq:charakter-babab){reference-type="eqref" reference="eq:charakter-babab"}. Notice that the multliset of the values of $\mu^{-1} \tilde{\pi} \mu$ (over $\mu\in \tilde{S}_n$) coincides with the multiset of the values of $f \circ \pi \circ f^{-1}$ (over bijections $f$). We define $\sigma_i=f^{-1} \circ \tilde{\sigma_i} \circ f$; then condition $\mu =\tilde{\pi}^{-1} \mu \tilde{\sigma}_1 \tilde{\sigma}_2$ is equivalent to $\pi=\sigma_1 \sigma_2$. It is easy to check that $\tilde{\sigma}_1\in Q_{\lambda}$ if and only if $c\circ f$ is constant on each cycle of $\sigma_1$ and $\tilde{\sigma}_2\in P_{\lambda}$ if and only if $r\circ f$ is constant on each cycle of $\sigma_2$. Thus $$\label{eq:ppp}
 n! \frac{\mathop{\mathrm{Tr}}\rho^{\lambda}(\tilde{\pi})}{\mathop{\mathrm{dim}}V_{\lambda}}
= \sum_{\substack{\sigma_1,\sigma_2\in S_n,\\ \sigma_1\sigma_2=\pi}} 
(-1)^{|\sigma_1|} \tilde{N}^{\lambda}(\sigma_1,\sigma_2)$$ and the proof in the case when $l=n$ is finished.

For a permutation $\sigma\in S_n$ we denote by $\mathop{\mathrm{supp}}\sigma\subseteq\{1,\dots,n\}$ the support of a permutation (the set of non-fixed points). We claim that a factorization $\pi=\sigma_1 \sigma_2$ has a non-zero contribution to [\[eq:ppp\]](#eq:ppp){reference-type="eqref" reference="eq:ppp"} only if $\mathop{\mathrm{supp}}\sigma_1,\mathop{\mathrm{supp}}\sigma_2\subseteq \mathop{\mathrm{supp}}\pi$. Indeed, if $m\in \mathop{\mathrm{supp}}\sigma_1\setminus
\mathop{\mathrm{supp}}\pi=\mathop{\mathrm{supp}}\sigma_2\setminus \mathop{\mathrm{supp}}\pi$ then for any bijection $f$ at least one of the following conditions hold true: $r(f(m))\neq r(f(\sigma_2(m)))$ (in this case $r\circ f$ is not constant on the cycles of $\sigma_2$) or $c(f(m))\neq c(f(\sigma_2(m)))$ (in this case $c(f(\sigma_1(\sigma_2(m))))\neq c(f(\sigma_2(m)))$ hence $c\circ f$ is not constant on the cycles of $\sigma_1$).

It follows that if $\pi\in S_l$ then we may restrict the sum in [\[eq:ppp\]](#eq:ppp){reference-type="eqref" reference="eq:ppp"} to factorizations $\pi=\sigma_1 \sigma_2$, where $\sigma_1,\sigma_2\in S_l$. It remains to notice that $$\tilde{N}_{S_n}^{\lambda}(\sigma_1,\sigma_2) =
(n-l)! \ \tilde{N}_{S_l}^{\lambda}(\sigma_1,\sigma_2),$$ where the quantity on the left-hand side regards $\sigma_1,\sigma_2$ as elements of $S_n$ while on the quantity on the right-hand side regards them as elements of $S_l$ and that the analogous relation holds between $\Sigma^\lambda(\pi)$ for $\pi\in S_n$ and $\pi\in S_l$. ◻
:::
