---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-008-6-distinct-5-regular-partitions
section_title: "Distinct 5-regular partitions."
section_number: 6
pages: 16-18
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.661
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on truncated"
---
[]{#distinct-reg label="distinct-reg"}

Proving identities (6.8), (6.9), (6.11), and (6.14) in [@M1] combinatorially is still an open problem. The difficulty consists in finding a combinatorial proof of the Weierstrass addition formula [@KMR Identity (8.1)] used in [@KMR] to prove these identities.

In this section, we use the Weierstrass addition formula to prove Theorem [\[d5\]](#d5){reference-type="ref" reference="d5"} below, an interesting identity involving the number of distinct $5$-regular partitions of $n$. This is sequence A096938 in [@OEIS] where several other interpretations of this sequence are discussed.

We denote by $\mathcal D_5(n)$ the set of distinct $5$-regular partitions of $n$, i.e., partitions of $n$ into distinct parts not divisible by $5$. If $a, b$ are integers such that $0<a,b<10$ and $a \not \equiv \pm b \pmod{10}$, we denote by $\mathcal C_{a,b}(n)$ the set of pairs of partitions $(\lambda, \mu)\vdash n$ such that $\lambda$ is a partition with distinct parts not congruent to $\pm a$ or $\pm b$ modulo $10$ and $\mu$ is a distinct partition with all parts divisible by $5$.

::: theorem
[]{#d5 label="d5"} For $n\geq 1$, $$|\mathcal D_5(n)|=| \mathcal C_{1,2}(n)|+| \mathcal C_{3,4}(n-1)|.$$
:::

::: proof
*Proof.* If $m\geq 2$ and $0<s<m$, we use the notation $$\theta(q^s;q^m):=(q^s;q^m)_\infty(q^{m-s};q^s)_\infty.$$

As explained in [@KMR pg. 225], if we first replace $q$ by $q^{10}$ and then take $u=-q^3$, $v=q$, $x=q^4$ and $y=q^3$, in [@KMR Identity (8.1)], we obtain $$\begin{aligned}
   \notag \theta(q^2;q^{10})\theta(q^4;q^{10})& \theta(-q;q^{10})\theta(-q^3;q^{10})\\\notag  &  + \theta(q;q^{10})\theta(q^3;q^{10})\theta(-q^2;q^{10})\theta(-q^4;q^{10})\\ \label{WSF1} &\ \ \  = \theta(q^3;q^{10})\theta(-q^4;q^{10})\theta(q^5;q^{10})\theta(-1;q^{10}).
\end{aligned}$$

We give a combinatorial interpretation of [\[WSF1\]](#WSF1){reference-type="eqref" reference="WSF1"}. The $q$-series $$\theta(q^2;q^{10})\theta(q^4;q^{10})\theta(-q;q^{10})\theta(-q^3;q^{10})$$ is the generating function for $$\begin{aligned}
& |\{\lambda \in \mathcal D_5(n) \mid \ell_e(\lambda) \text{ even}\}|-|\{\lambda \in \mathcal D_5(n) \mid \ell_e(\lambda) \text{ odd}\}|\\ & \ \ \ \ \ = (-1)^n\left(|\{\lambda \in \mathcal D_5(n) \mid \ell(\lambda) \text{ even}\}|-|\{\lambda \in \mathcal D_5(n) \mid \ell(\lambda) \text{ odd}\}|\right),
\end{aligned}$$ and the $q$-series $$\theta(q;q^{10})\theta(q^3;q^{10})\theta(-q^2;q^{10})\theta(-q^4;q^{10})$$ is the generating function for $$|\{\lambda \in \mathcal D_5(n) \mid \ell_o(\lambda) \text{ even}\}|-|\{\lambda \in \mathcal D_5(n) \mid \ell_o(\lambda) \text{ odd}\}|=(-1)^n |\mathcal D_5(n)|.$$ Here, we used the fact that $\ell_0(\lambda)\equiv |\lambda|\mod 2$.

The $q$-series $$\begin{aligned}
& \theta(q^3;q^{10})\theta(-q^4;q^{10})\theta(q^5;q^{10})\theta(-1;q^{10})\\ & =  2(q^3; q^{10})_\infty(q^7; q^{10})_\infty(-q^4; q^{10})_\infty(-q^6; q^{10})_\infty(q^5; q^{10})^2_\infty(-q^{10}; q^{10})^2_\infty
\end{aligned}$$ is the generating function for $$\begin{aligned}
2 (|\{(\lambda, \mu)\in \mathcal C_{1,2}(n) \mid \ell_o(\lambda)+\ell_o(\mu) \text{ even}\}|&-|\{(\lambda, \mu)\in \mathcal C_{1,2}(n) \mid \ell_o(\lambda)+\ell_o(\mu) \text{ odd}\}|)\\ & = 2(-1)^n | \mathcal C_{1,2}(n)|.
\end{aligned}$$

Hence, the combinatorial interpretation of [\[WSF1\]](#WSF1){reference-type="eqref" reference="WSF1"} is $$|\{\lambda \in \mathcal D_5(n) \mid \ell(\lambda) \text{ even}\}|=| \mathcal C_{1,2}(n)|.$$

If we now follow [@KMR pg. 226] and first replace $q$ by $q^{10}$ and then take $u=q^5$, $v=q^2$, $x=q^6$ and $y=q^4$, in [@KMR Identity (8.1)], we obtain $$\begin{aligned}
   \notag \theta(q^2;q^{10})\theta(q^4;q^{10})& \theta(-q;q^{10})\theta(-q^3;q^{10})\\\notag  &  - \theta(q;q^{10})\theta(q^3;q^{10})\theta(-q^2;q^{10})\theta(-q^4;q^{10})\\ \label{WSF2} &\ \ \  = q\theta(-q^2;q^{10})\theta(-1;q^{10})\theta(q^5;q^{10})\theta(q;q^{10}).
\end{aligned}$$ By the same argument as above, $$\begin{aligned}
\theta(-q^2;q^{10})\theta(-1;q^{10})\theta(q^5;q^{10})\theta(q;q^{10})
\end{aligned}$$ is the generating function for $2(-1)^n|\mathcal C_{3,4}(n)|$ and the combinatorial interpretation of [\[WSF2\]](#WSF2){reference-type="eqref" reference="WSF2"} is $$|\{\lambda \in \mathcal D_5(n) \mid \ell(\lambda) \text{ odd}\}|=| \mathcal C_{3,4}(n-1)|.$$ ◻
:::
