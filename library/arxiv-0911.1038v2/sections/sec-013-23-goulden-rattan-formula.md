---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-013-23-goulden-rattan-formula
section_title: "Goulden-Rattan formula"
section_number: 2.3
pages: 12-12
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
[]{#sec:Goulden-Rattan label="sec:Goulden-Rattan"} For a partition $\lambda$ let $m_{\lambda}$ denote the monomial symmetric function in variables $x_1,x_2,\dots$. In this paper we consider the particular evaluation of the monomial symmetric function at $x_i=i$, for $i=1,\dots ,k-1$, and $x_i=0$, for $i\geq k$, and write this as $\hat{m}_{\lambda}$. Let $A(t)$ be a formal power series. We denote the coefficient of $t^k$ in $A(t)$ by $[t^k]A(t)$.

::: theorem
[]{#theo:g-r label="theo:g-r"} For $g\geq 1$, $k\geq 2g-1$, $$\label{eq:G-R}
\Sigma_{k,k+1-2g}=-\frac{1}{k}[t^{k+1-2g}]
\sum_{|\lambda| = 2g}\hat{m}_{\lambda}
\frac{P_{\lambda}(t)}{C(t)}.$$
:::

## Proof of Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"}

::: proof
*Proof of Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"}.* Equation [\[eq:G-R\]](#eq:G-R){reference-type="eqref" reference="eq:G-R"} can be written in the form $$k\
\Sigma_{k,k+1-2g}=-[t^{k+1-2g}]
\sum_{|\lambda| = 2g}\hat{m}_{\lambda}
\frac{P_{\lambda}(t)}{C(t)}.$$

The evaluation of the power sum symmetric function $$\hat{p}_s = 1^s + \cdots + (k-1)^s$$ analogous to that for $\hat{m}_\lambda$ is a polynomial in $k$ of degree $s+1$; it follows immediately that the evaluation of the power-sum symmetric function $\hat{p}_\lambda$ is a polynomial in $k$ of degree $|\lambda|+l(\lambda)$. The monomial symmetric function $m_{\lambda}$ is a linear combination of power-sum symmetric functions $p_{\mu}$, where each partition $\mu$ which appears in this linear combination is obtained from partition $\lambda$ by gluing some of their parts (see for example [@Macdonald1995]). It means that for each such $\mu$ we have $$|\lambda|+l(\lambda) \geq  |\mu|+l(\mu),$$ and for this reason also $\hat{m}_\lambda$ is a polynomial in $k$ of degree at most $|\lambda|+l(\lambda)$.

For any partition $\mu$ such that $|\mu| = k + 1-  2g$ we have $k =
p_1(\mu) + 2g -1$, where $p_1$ is a power symmetric function, hence there exists a symmetric function $f_{\lambda}$ of degree $|\lambda|+l(\lambda)$ which does not depend on $k$ such that $\hat{m}_{\lambda}
= f_{\lambda}(\mu)$. Proposition [\[prop:it-is-nice\]](#prop:it-is-nice){reference-type="ref" reference="prop:it-is-nice"} finishes the proof. ◻
:::
