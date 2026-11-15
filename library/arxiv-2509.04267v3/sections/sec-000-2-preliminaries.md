---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-000-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 3-4
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.956
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
[]{#sec:prelim label="sec:prelim"}

In this section we review two approaches for defining quantum knot invariants, one via traces and the other via height functions and maxima/minima. We follow these two approaches to construct quantum cocycle invariants in later sections. Unless otherwise specified, we use the notation $\mathbb k$ for a unital ring, and $V$ for a module over $\mathbb k$.

Recall that for an invertible map $R: V \otimes V \rightarrow V \otimes V$ of a ${\mathbb k}$-module $V$, the equation $$(R \otimes {\mathbb 1}) ({\mathbb 1} \otimes R) (R \otimes {\mathbb 1}) 
=({\mathbb 1} \otimes R) (R \otimes {\mathbb 1}) ({\mathbb 1} \otimes R)$$ is called the *Yang-Baxter* equation (YBE), and an invertible solution $R$ of it is called a Yang-Baxter (YB) operator, or R-matrix. We will also say YBO for short. YBE is diagrammatically represented as in Figure [1](#YBE){reference-type="ref" reference="YBE"}, where $R$ is represented by a crossing. Diagrams are read from top to bottom, and the right most term of maps that acts first, corresponds to the top portion of a diagram. For example, the rightmost term $(R \otimes \mathbb 1)$ in the left-hand side of YBE above represents the top left crossing with a straight line to its right, in the left-hand side of Figure [1](#YBE){reference-type="ref" reference="YBE"}.

If $R$ satisfies the YBE but is not assumed to be invertible, then $R$ is called *pre-Yang-Baxter operator*, or pre-YBO for short. If $R$ is invertible the inverse is denoted by $R^{-1}$, and to indicate that either $R$ or its inverse are used, we employ the notation $R^{\pm}$ for short. In Figure [1](#YBE){reference-type="ref" reference="YBE"}, when all strings are oriented downwards, crossings are defined to be positive. If $R$ corresponds to a positive crossing, $R^{-1}$ is represented by a negative crossing.

<figure id="YBE">
<div class="center">
<img src="YBE" style="width:1in" />
</div>
<figcaption></figcaption>
</figure>
