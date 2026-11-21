---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-012-112-hypothesis-approximate-factorization-of-char
section_title: "Hypothesis: approximate factorization of characters"
section_number: 1.12
pages: 6-7
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 0.776
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
[]{#sec:partitions label="sec:partitions"}

In the following we will use the following convention. If $\chi_n\colon\mathcal{P}_{n}\to\mathbb{R}$ is a function on the set of partitions of $n$, we will extend its domain to the set $$\mathcal{P}_{\leq n}:=\bigsqcup_{0\leq k\leq n} \mathcal{P}_{k}$$ of partitions of smaller numbers by setting $$\label{eq:extended-character}
\chi_n(\pi):= \chi_n( \pi,1^{n-|\pi|}) \qquad \text{for } |\pi|\leq n,$$ i.e. we extend the partition $\pi$ by adding an appropriate number of parts, each equal to $1$.

In this way the cumulant $k^{\chi_n}_\ell (l_1,\dots,l_\ell)$ is well defined if $n\geq l_1+\cdots+l_\ell$ is large enough.

::: definition
[]{#def:approx-factorization-charactersA label="def:approx-factorization-charactersA"} Assume that for each integer $n\geq 1$ we are given a function $\chi_n\colon\mathcal{P}_{n}\to\mathbb{R}$. We say that the sequence $(\chi_n)$ has *approximate factorization property* [@Sniady2006c] if for each integer $\ell\geq 1$ and all integers $l_1,\dots,l_\ell\geq 2$ the limit

$$\label{eq:aprox-fact-property}
    \lim_{n\to\infty} k^{\chi_n}_\ell (l_1,\dots,l_\ell)\ n^{\frac{l_1+\cdots+l_\ell+\ell-2}{2}}$$

exists and is finite.

We say that the sequence $(\chi_n)$ has *enhanced approximate factorization property* if, additionally, in the case $\ell=1$ the rate of convergence in [\[eq:aprox-fact-property\]](#eq:aprox-fact-property){reference-type="eqref" reference="eq:aprox-fact-property"} takes the following explicit form:

for each $l\geq 2$ there exist some constants $a_{l+1},b_{l+1}\in\mathbb{R}$ such that $$\label{eq:refined-asymptotics-characters}
    k^{\chi_n}_1(l) \ n^{\frac{l-1}{2}} =  \chi_n(l) \ n^{\frac{l-1}{2}}  =
    a_{l+1}+ \frac{b_{l+1}+o(1)}{\sqrt{n}} \qquad \text{for }n\to\infty$$ and $$\label{eq:what-is-m}
    \sup_{l\geq 2} \frac{\sqrt[l]{|a_l|}}{l^m} < \infty,
    \qquad
    \text{where }
    m = \begin{cases}2 &\text{for } g \neq 0,\\
    1 & \text{for } g=0,\end{cases}$$ where $g$ is given by [\[eq:double-scaling-refined\]](#eq:double-scaling-refined){reference-type="eqref" reference="eq:double-scaling-refined"}.
:::

::: example
[]{#example:plancherel label="example:plancherel"} It is easy to check that for $\chi_{\mathop{\mathrm{reg}}}$ from [\[eq:regular\]](#eq:regular){reference-type="eqref" reference="eq:regular"} all higher cumulants vanish: $$k^{\chi_{\mathop{\mathrm{reg}}}}_\ell (l_1,\dots,l_\ell) = 0 \qquad \text{for $\ell\geq 2$}$$ and the first cumulant takes a particularly simple form $$k^{\chi_{\mathop{\mathrm{reg}}}}_1 (l) = \chi_{\mathop{\mathrm{reg}}} (l) =
    \begin{cases} 
    1 & \text{if } l=1, \\ 
    0 & \text{otherwise.}
    \end{cases}$$ It follows that that the sequence $(\chi_n)$ for which $\chi_n:=\chi_{\mathop{\mathrm{reg}}}$ fulfills the enhanced approximate factorization property.
:::
