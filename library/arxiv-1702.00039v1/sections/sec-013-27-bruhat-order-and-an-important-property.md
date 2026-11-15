---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-013-27-bruhat-order-and-an-important-property
section_title: "Bruhat order and an important property"
section_number: 2.7
pages: 11-12
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 1.0
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
[]{#imp label="imp"}

One important concept about Coxeter systems is the *Bruhat order*. It is defined by $x\leq y$ if some substring of some (or every) reduced word for $y$ is a reduced word for $x$.

For example, in the case of $S_3$, the Bruhat order is represented in the following diagram

<figure>
<div class="center">
<img src="Bruhat.png" />
</div>
</figure>

We see that in this example, the only couples of non-comparable elements are $(s, r)$ and $(sr,rs)$.

A beautiful and important property (proved by Hideya Matsumoto in 1964 [@Ma]) about Coxeter systems is that, if $x\in W$, one can obtain any reduced expression of $x$ from any other, just by applying braid relations. Moreover, if $sx<x$ there is an expression of $x$ that has $s$ in the left, i.e. $x$ admits an expression of the form $sr\cdots t$. Of course, if $xs<x$ then there is an expression of $x$ that has $s$ in the right.
