---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-008-18-the-main-result-proof-of-some-conjectures-of
section_title: "The main result: proof of some conjectures of Lassalle"
section_number: 1.8
pages: 6-7
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.99
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
Lassalle announced as a conjecture [@Lassalle-preprint2007] that there is an additional structure in the genus expansion of Kerov polynomials. He claimed that for a fixed genus $g$ there exists a symmetric function $f_g$ which describes polynomials $K_{k,k+1-2g}$ and which is independent of $k$. Before presenting his conjectures we need to prepare some notations.

A partition $\mu=(\mu_1\geq \mu_2\geq \cdots)$ is a weakly decreasing sequence of nonnegative integers with finitely many non-zero elements. The non-zero $\mu_i$ in a partition $\mu$ are called the parts of $\mu$. We will denote by $m_i(\mu)$ the number of parts of $\mu$ equal to $i$; by $l(\mu)$ the number of parts of $\mu$; and denote $|\mu|=\mu_1+\mu_2+\cdots$. Following Lassalle, we define $R_1 = 0$ and for a strictly positive integer $i$ we define $$\begin{aligned}
\nonumber
\mathcal{R}_i &= (i-1)R_i, \\
\nonumber
\mathcal{R}_\mu &= \prod_{i}
\frac{\mathcal{R}_i^{m_i(\mu)}}{m_i(\mu)!}, \\
\label{eq:qi}
Q_i &= \sum_{|\mu|=i}\big(l(\mu)-1\big)!\ \mathcal{R}_\mu, \\
\nonumber
\mathcal{Q}_\mu &= \prod_{i} \frac{Q_i^{m_i(\mu)}}{m_i(\mu)!}.
\end{aligned}$$

As usual, we denote by $e_i$ the elementary symmetric functions, by $h_i$ the complete symmetric functions and by $p_i$ the power-sum symmetric functions. For any partition $\mu$, we denote by $e_{\mu}$, $h_{\mu}$ or $p_{\mu}$ their product over the parts of $\mu$, and by $m_{\mu}$ the monomial symmetric function --- the sum of all distinct monomials whose exponent is a permutation of $\mu$.

The main result of this article is a proof of the following results which were stated as the first and the sixth conjecture in the paper [@Lassalle-preprint2007] by Lassalle.

::: theorem
[]{#theo:main label="theo:main"} For any $g\geq 1$ there exist inhomogeneous symmetric functions $f_g$ and $h_g$, having maximal degree $4(g-1)$, such that $$\begin{aligned}
\label{eq:lassalle1}
K_{k,k+1-2g} &= \binom{k+1}{3}  \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)!\ f_g(\mu)\ \mathcal{R}_\mu \\
\label{eq:lassalle6}
 &= \binom{k+1}{3}  \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ h_g(\mu)\ \mathcal{Q}_\mu,
\end{aligned}$$ where $f_g(\mu) = f_g(\mu_1,\mu_2,\dots)$ and $h_g(\mu_1,\mu_2,\dots)$. These symmetric functions are independent of $k$.
:::

This result sheds some light on the structure of Kerov polynomials but it also leads to many new open problems, in particular the positivity conjectures of Lassalle [@Lassalle-preprint2007] and his questions concerning combinatorial interpretations of the coefficients in the expansions of the above symmetric functions.
