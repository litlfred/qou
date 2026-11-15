---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-009-22-forgetting-injectivity
section_title: "Forgetting injectivity"
section_number: 2.2
pages: 7-8
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.972
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
For a pair of permutations $\sigma_1,\sigma_2\in S_l$ we define $\hat{N}^{\lambda}(\sigma_1,\sigma_2)$

as the number of all functions

$f:\{1,\dots,l\}\rightarrow \lambda$ (with values in the set of boxes of $\lambda$) with a property that $r\circ f$ is constant on each cycle of $\sigma_2$ and $c\circ f$ is constant on each cycle of $\sigma_1$.

::: lemma
[]{#lem:kasowanie label="lem:kasowanie"} For any Young diagram $\lambda$ and a permutation $\pi\in S_l$ $$\label{eq:stanley-feray-sniady-2}
\sum_{\substack{\sigma_1,\sigma_2\in S_l\\ \sigma_1 \sigma_2=\pi,}}
  (-1)^{|\sigma_1|} \tilde{N}^{\lambda}(\sigma_1,\sigma_2)=
\sum_{\substack{\sigma_1,\sigma_2\in S_l\\ \sigma_1 \sigma_2=\pi,}}
  (-1)^{|\sigma_1|} \hat{N}^{\lambda}(\sigma_1,\sigma_2).$$
:::

::: proof
*Proof.* For a given function $f:\{1,\dots,l\}\rightarrow \lambda$ we will show that it has the same contribution to the left-hand side and to the right-hand side. Clearly, it is enough to consider the case when $f$ is not a one-to-one function. It follows that there exists a transposition $\mu\in S_l$ with a property that $f$ is constant on the orbits of $\mu$. Function $f$ contributes to the right-hand side

with multiplicity $$\label{eq:contribution}
 \sum_{\substack{\sigma_1,\sigma_2\in S_l\\ \sigma_1 \sigma_2=\pi}} (-1)^{|\sigma_1|},$$ where the sum runs over pairs $(\sigma_1,\sigma_2)$ with a property that $\sigma_1 \sigma_2=\pi$ and $c\circ f$ is constant on each cycle of $\sigma_1$ and $r\circ f$ is constant on each cycle of $\sigma_2$. Map $(\sigma_1,\sigma_2)\mapsto (\sigma_1', \sigma_2')$ with $\sigma'_1=\sigma_1
\mu$, $\sigma_2'=\mu \sigma_2$ is an involution of the pairs $(\sigma_1,\sigma_2)$ which contribute to [\[eq:contribution\]](#eq:contribution){reference-type="eqref" reference="eq:contribution"}; the only less trivial condition which should be verified is that $c\circ f$ is constant on each cycle of $\sigma'_1$ but this is equivalent to $c\circ f$ being constant on each cycle of $\sigma'_1{}^{-1}=\mu \sigma_1^{-1}$.

Since $(-1)^{|\sigma_1|}= (-1)\cdot (-1)^{|\sigma'_1|}$ therefore the contributions of the pairs $(\sigma_1,\sigma_2)$ and $(\sigma_1',\sigma_2')$ to [\[eq:contribution\]](#eq:contribution){reference-type="eqref" reference="eq:contribution"} cancel. In this way we proved that [\[eq:contribution\]](#eq:contribution){reference-type="eqref" reference="eq:contribution"} is equal to zero which finishes the proof. ◻
:::

::: proof
*Proof of Theorem [\[theo:character-sniady\]](#theo:character-sniady){reference-type="ref" reference="theo:character-sniady"}.* Proposition [\[prop:bubu2\]](#prop:bubu2){reference-type="ref" reference="prop:bubu2"} and Lemma [\[lem:kasowanie\]](#lem:kasowanie){reference-type="ref" reference="lem:kasowanie"} show that $$\Sigma^{\lambda}(\pi)= \sum_{\substack{\sigma_1,\sigma_2\in S_l\\ \sigma_1 \sigma_2=\pi}}
(-1)^{|\sigma_1|} \hat{N}^{\lambda}(\sigma_1,\sigma_2).$$ Now it is enough to notice that $N^{\lambda}(\sigma_1,\sigma_2)=\hat{N}^{\lambda}(\sigma_1,\sigma_2)$; the desired bijection is defined as follows: if $m\in\{1,\dots,l\}$ fulfills $m\in c_1\cap c_2$ for $c_i\in C(\sigma_i)$ we set $f(m)=(h(c_1),h(c_2))$. ◻
:::
