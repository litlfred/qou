---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-009-19-general-idea-of-the-proof
section_title: "General idea of the proof"
section_number: 1.9
pages: 7-8
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.964
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
For a given positive integer $g$ we define a symmetric function $k(\mu) := |\mu|+2g-1 = p_1(\mu) + 2g - 1$, therefore for a given symmetric functions $f_g$ and $h_g$ we can define symmetric functions $\tilde{f}_g(\mu) := k(\mu) \binom{k(\mu)+1}{3} f_g(\mu)$ and $\tilde{h}_g(\mu) := k(\mu) \binom{k(\mu)+1}{3} h_g(\mu)$. We notice that in equations [\[eq:lassalle1\]](#eq:lassalle1){reference-type="eqref" reference="eq:lassalle1"} and [\[eq:lassalle6\]](#eq:lassalle6){reference-type="eqref" reference="eq:lassalle6"} we sum over all partitions $\mu$ which satisfy $k(\mu) = k$. Therefore the following proposition is an immediate consequence of Theorem [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"}.

::: proposition
[]{#prop:main-prop label="prop:main-prop"} For any $g\geq 1$ there exist inhomogeneous symmetric functions $\tilde{f}_g$ and $\tilde{h}_g$, having maximal degree $4g$, such that $$\begin{aligned}
k\ K_{k,k+1-2g} &=  \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! \ \tilde{f}_g(\mu) \mathcal{R}_\mu \\ 
 &= \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ \tilde{h}_g(\mu) \mathcal{Q}_\mu,
\end{aligned}$$ where $\tilde{f}_g(\mu) = \tilde{f}_g(\mu_1,\mu_2,\dots)$ and $\tilde{h}_g(\mu)
= \tilde{h}_g(\mu_1,\mu_2,\dots)$. These symmetric functions are independent of $k$.
:::

In fact, the opposite implication holds true as well and Theorem [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"} is a consequence of Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"}: roughly speaking we will show that the symmetric functions $\tilde{f}_g$ and $\tilde{h}_g$ are divisible by the polynomial $k \binom{k+1}{3}$. One can notice that Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"} stated that $\tilde{f}_g$ and $\tilde{h}_g$ are independent of $k$, so the divisibility which we will show is a divisibility of symmetric functions $\tilde{f}_g$ and $\tilde{h}_g$ by the symmetric function $K$ which has a property that for any partition $\mu$ such that $|\mu| = k +1 - 2g$ we have that $K(\mu) = k
\binom{k+1}{3}$. We shall explain precisely what this divisibility means and show in Section [\[sec:divisibility\]](#sec:divisibility){reference-type="ref" reference="sec:divisibility"} that it holds indeed by studying the arithmetic properties of Kerov polynomials and their divisibility by prime numbers.

The remaining difficulty is to prove Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"}. We shall do it in Section [\[sec:existence\]](#sec:existence){reference-type="ref" reference="sec:existence"} by analysis of the Goulden-Rattan formula.

Section [\[sec:technical\]](#sec:technical){reference-type="ref" reference="sec:technical"} is a presentation of technical and complicated proofs of lemmas which are used in the previous sections.
