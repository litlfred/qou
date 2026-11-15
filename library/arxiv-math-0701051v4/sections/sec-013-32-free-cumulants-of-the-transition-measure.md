---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-013-32-free-cumulants-of-the-transition-measure
section_title: "Free cumulants of the transition measure"
section_number: 3.2
pages: 10-11
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.987
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
[]{#subsec:cumulants label="subsec:cumulants"}

For a (continuous) Young diagram $\lambda$ we denote by $\mu^{\lambda}$ its transition measure (which is a probability measure on the real line) [@Kerov1993; @Biane1998] and by $R_{m}^{\lambda}:=R_m(\mu^{\lambda})$ we denote the $m$-th free cumulant of $\mu^{\lambda}$. The importance of free cumulants $R_m^{\lambda}$ in the study of the asymptotics of symmetric groups was pointed out by Biane [@Biane1998]. The following theorem gives a new formula for the free cumulants $R_m^{\lambda}$. It has a big advantage that it does not involve the notion of the transition measure and it is related directly with the shape of a Young diagram.

::: theorem
[]{#theo:cumulants label="theo:cumulants"} For any Young diagram $\lambda$ $$\label{eq:freecumulants-come}
R_{l+1}^{\lambda}= \sum_{\substack{\sigma_1,\sigma_2\in S_l,\\
\sigma_1 \sigma_2=(1,2,\dots,l), \\
|\sigma_1|+|\sigma_2|=|(1,2,\dots,l)|}} (-1)^{|\sigma_1|}\
N^{\lambda}(\sigma_1,\sigma_2),$$ where the sum runs over minimal factorizations of a cycle of length $l$.
:::

::: proof
*Proof.* For a Young diagram $\lambda$ and $c>0$ we denote by $c\lambda$ the (generalized) Young diagram obtained from $\lambda$ by similarity with scale $c$. A function $f$ on the set of (generalized) Young diagrams is said to be homogeneous of degree $m$ if $$f(c \lambda)= c^m f(\lambda)$$ holds true for all choices of $\lambda$ and $c$. Each free cumulant $R_m$ is homogenous of degree $m$.

The value of the normalized character $\Sigma^{\lambda}(1,2,\dots,l)$ on a cycle can be expressed as a polynomial (known as Kerov polynomial) in free cumulants $(R^{\lambda}_{m}: m\in\{2,3,\dots\} )$: $$\Sigma^{\lambda}(1,2,\dots,l)= R_{l+1}^{\lambda} + (\text{terms of lower
degree})$$ therefore $R^\lambda_{l+1}$ is the homogeneous part of $\Sigma^{\lambda}(1,2,\dots,l)$ with degree $l+1$. We apply [\[eq:main-theorem\]](#eq:main-theorem){reference-type="eqref" reference="eq:main-theorem"} for $\pi=(1,2,\dots,l)$; it is easy to see that each summand on the right-hand side is homogeneous of degree $|C(\sigma_1)|+|C(\sigma_2)|$ which finishes the proof. ◻
:::
