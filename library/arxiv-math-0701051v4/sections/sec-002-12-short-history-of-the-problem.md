---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS"
section_id: sec-002-12-short-history-of-the-problem
section_title: "Short history of the problem"
section_number: 1.2
pages: 1-2
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.987
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS — We prove an upper bound for characters of the symmetric groups."
---
Unfortunately, the canonical tool for calculating characters, the Murnaghan--Nakayama rule, quickly becomes cumbersome and hence intractable for computing characters corresponding to large Young diagrams. Nevertheless Roichman [@Roichman1996] showed that it is possible to use it to find an upper bound for characters, namely he proved that there exist constants $0<q<1$ and $b>0$ such that $$\label{eq:roichman}
 |\chi^{\lambda}(\pi) | \leq 
\left[\max\left(\frac{r(\lambda)}{n},\frac{c(\lambda)}{n},q\right) \right]^{b\ |\mathop{\mathrm{supp}}\pi|},$$ where $r(\lambda)$, $c(\lambda)$ denote the numbers of rows and columns of $\lambda$ and $\mathop{\mathrm{supp}}\pi$ denotes the support of a permutation $\pi$ (the set of its non-fixed points). Inequality [\[eq:roichman\]](#eq:roichman){reference-type="eqref" reference="eq:roichman"} is not satisfactory for many practical purposes (such as [@MooreRussellSniady]) since it provides rather weak estimates in the case when the Young diagram $\lambda$ is *balanced*, i.e. $r(\lambda),c(\lambda)=O(\sqrt{n})$.

Another approach to this problem was initiated by Biane [@Biane1998; @Biane2003] who showed that the value of the normalized character $\Sigma^{\lambda}(\pi)$

can be expressed as a polynomial (called Kerov polynomial) in *free cumulants* of the *transition measure* of a Young diagram $\lambda$. The work of Biane was based on previous contributions of Kerov [@Kerov1993; @Kerov1999] and Vershik. Free cumulants of the transition measure have a nice geometric interpretation therefore Kerov polynomials are a perfect tool for study of the character $\chi^{\lambda}(\pi)$ in the limit when the permutation $\pi$ is fixed and the Young diagram $\lambda$ tends in some sense to infinity.

Unfortunately, despite much progress in this field ([@{DolegaF'eray'Sniady2008}] and references therein) our understanding of Kerov polynomials is still not satisfactory; in particular it is not clear how to use Kerov polynomials in order to obtain non-trivial estimates on the characters $\chi^{\lambda}(\pi)$ when the length $|\pi|$ of the permutation $\pi\in S_n$ is comparable with $n$.

In a recent work of one of us with Rattan [@{Rattan'Sniady2008}] we took yet another approach: thanks to the generalized Frobenius formula we showed that the value of a normalized character of a given Young diagram $\lambda$ can be bounded from above by the value of the normalized character of a rectangular Young diagram $p\times q$ for suitably chosen $p,q$. For such a rectangular Young diagram the value of the normalized character can be explicitly calculated thanks to the formula of Stanley [@Stanley2003/04]. In this way we proved that for each $C$ there exists a constant $D$ with a property that if $r(\lambda),c(\lambda)< C \sqrt{n}$ then $$\label{eq:rattan-sniady}
|\chi^{\lambda}(\pi)|< \left( \frac{D \max( 1, \frac{|\pi|^2}{n})}{\sqrt{n}} \right)^{|\pi|},$$ where $|\pi|$ denotes the minimal number of factors necessary to write $\pi$ as a product of transpositions. Inequality [\[eq:rattan-sniady\]](#eq:rattan-sniady){reference-type="eqref" reference="eq:rattan-sniady"} gives a much better estimate than [\[eq:roichman\]](#eq:roichman){reference-type="eqref" reference="eq:roichman"} for balanced Young diagrams and a quite short permutation ($|\pi|=o(\sqrt{n})$) but a careful analysis of its proof shows that it gives non-trivial estimates only if $\max\big(r(\lambda),c(\lambda)\big) < O(n^{3/4})$.
