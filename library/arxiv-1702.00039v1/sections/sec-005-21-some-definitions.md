---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-005-21-some-definitions
section_title: "Some definitions"
section_number: 2.1
pages: 3-3
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
[]{#Some definitions label="Some definitions"}

A *Coxeter matrix* is a symmetric matrix with entries in $\{1,2,\ldots\}\cup \{\infty\}$, diagonal entries $1$ and off-diagonal entries at least $2$.

::: defi
A pair $(W,S)$, where $W$ is a group and $S$ is a finite subset of $W,$ is called a *Coxeter system* if $W$ admits a presentation by generators and relations given by $$\langle s\in S\ \vert \ (sr)^{m_{sr}}=e\ \ \mathrm{if}\  s,r \in S \ \mathrm{and}\  m_{sr} \ \mathrm{is}\ \ \mathrm{finite} \rangle,$$ where $(m_{sr})_{s,r\in S}$ is a Coxeter matrix and $e$ is the identity element.
:::

We then say that $W$ is a *Coxeter group*. One can prove that in the Coxeter system defined above, the order of the element $sr$ is $m_{sr}$ (it is obvious that it divides $m_{sr}$). The *rank* of the Coxeter system is the cardinality of $S$. If $s\neq r,$ the relation $(sr)^{m_{sr}}=e$ is equivalent to $$\underbrace{srs\cdots}_{m_{sr}}=\underbrace{rsr\cdots}_{m_{sr}}$$ This is called a *braid relation*. On the other hand, as $m_{ss}=1,$ we have that $s^2=e.$ This is called a *quadratic relation*. An *expression* of an element $x\in W$, is a tuple $\underline{x}=(s,r,\ldots, t)$ with $s,r,\ldots, t \in S$ such that $x=sr\cdots t$. The expression is *reduced* if the length of the tuple is minimal. We denote $l(x)$ this length.
