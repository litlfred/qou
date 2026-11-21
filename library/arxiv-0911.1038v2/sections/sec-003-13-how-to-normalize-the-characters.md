---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-003-13-how-to-normalize-the-characters
section_title: "How to normalize the characters?"
section_number: 1.3
pages: 2-3
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.967
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
*How should we normalize the characters of the symmetric groups in order to obtain some meaningful asymptotic quantities?* The answer for this question was given by [@Biane2003] who gave the following definition. For any permutation $\pi\in \mathfrak{S}(k)$ and an irreducible representation $\rho^\lambda$ of the symmetric group $\mathfrak{S}(n)$ corresponding to the Young diagram $\lambda$ we define the *normalized character* $$\label{eq:character}
 \Sigma^\lambda_\pi =\begin{cases} \underbrace{n(n-1)\cdots (n-k+1)}_{k \text{
factors}} \frac{\mathop{\mathrm{Tr}}\rho^\lambda(\pi)}{\text{dimension of $\rho^\lambda$}} &
\text{if } k\leq n, \\ 0 & \text{otherwise.} \end{cases}$$ An interesting feature of this definition is that we do not require that $k$, the index of the symmetric group to which $\pi$ belongs, must be equal to $n$, the number of boxes of $\lambda$. In order for $\rho^\lambda(\pi)$ to make sense, for $k<n$ we just declare that the permutation $\pi\in\mathfrak{S}(k)$ can be also regarded as an element of $\mathfrak{S}(n)$; we just add to $\pi$ additional $n-k$ fixpoints. As it was pointed out by Scarabotti [@Scarabotti2011], it would be more appropriate to use the name of *spherical function* instead of *character* for these objects, nevertheless we will stick to this old nomenclature.

Particularly interesting are the values of characters on cycles, therefore we will use the notation $$\Sigma^\lambda_k = \Sigma^\lambda_{(1,2,\dots,k)}.$$

In this article we will study the following problem: *for fixed value of $k$, what can we say about the normalized characters $\Sigma^{\lambda}_k$ when a balanced Young diagram $\lambda$ tends to infinity* or, in a slightly more concrete reformulation, *what can we say about the normalized characters $\Sigma^{s
\lambda}_k$ related to dilated Young diagrams $s\lambda$ in the limit as $s\to\infty$?*
