---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-006-16-kerov-character-polynomials
section_title: "Kerov character polynomials"
section_number: 1.6
pages: 4-5
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
It turns out that free cumulants can be used not only to provide asymptotic approximations for the characters of symmetric groups, but also for exact formulas. Kerov during a talk in Institut Henri Poincaré in January 2000 [@Kerov2000talk] announced the following result (the first published proof was given by Biane [@Biane2003]): for each permutation $\pi$ there exists a unique universal polynomial $K_{\pi}$ with integer coefficients, called *Kerov character polynomial*, with a property that

$$\Sigma^{\lambda}_\pi =
K_{\pi}(R_2^{\lambda},R_3^\lambda,\dots)$$

holds true for any

Young diagram $\lambda$. We say that the Kerov polynomial is universal because it does not depend on the choice of $\lambda$. In order to simplify notation we suppress the $\lambda$-dependence of characters and free cumulants, writing $$\Sigma_\pi = K_{\pi}(R_2,R_3,\dots).$$

As usual, we are mostly concerned with the values of the characters on cycles, therefore we introduce special notation for such Kerov polynomials $$\Sigma_k = K_{k}(R_2,R_3,\dots).$$

The first few Kerov polynomials $K_k$ are as follows [@Biane2001]: $$\begin{aligned}
\Sigma_1 &= R_2, \\
\Sigma_2 &= R_3, \\
\Sigma_3 &= R_4 + R_2,   \\
\Sigma_4 &= R_5 + 5R_3,    \\
\Sigma_5 &= R_6 + 15R_4 + 5R_2^2 + 8R_2, \\
\Sigma_6 &= R_7 + 35R_5 + 35R_3 R_2 + 84R_3.
\end{aligned}$$

The primary motivation for investigation of this subject is the asymptotic representation theory, namely a good understanding of Kerov character polynomials might in the future shed some light on asymptotics of characters, also in the most difficult scaling when the length of the permutation on which we evaluate the character grows with the number of boxes of the Young diagram, see [@{F'eray'Sniady2011}].

The second motivation --- which is key for the purposes of this article --- is related to *algebraic combinatorics*. The last decade has seen a number of research papers which stated (sometimes conjecturally) several very surprising combinatorial properties of Kerov polynomials. For example, it was conjectured by Kerov [@Kerov2000talk] that the coefficients of Kerov polynomials are non-negative integers. These papers showed not only the richness of the combinatorial and the analytic structures of the Kerov character polynomials but also the difficulty in fully understanding these polynomials. Since the results proved in most of these papers will be necessary for the purposes of this article we decided to postpone the presentation of these papers until they are needed. A more complete presentation of the history of the subject and bibliography can be found in the paper [@{DolegaF'eray'Sniady2008}].
