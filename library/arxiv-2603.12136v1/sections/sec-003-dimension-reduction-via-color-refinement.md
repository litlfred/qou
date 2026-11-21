---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-003-dimension-reduction-via-color-refinement
section_title: "Dimension Reduction via Color Refinement"
section_number: null
pages: 6-6
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
[]{#sec_notation label="sec_notation"}

Let $V$ and $W$ be two disjoint finite sets. Throughout this work, we will index matrices with the sets $V$ and $W$ for the rows and columns, respectively, and denote any matrix $A$ indexed by $V$ and $W$ using $A\in \R^{V\times W}$. Its elements are indexed using $A_{v,w}$ for $v\in V$, $w\in W$. For $P\subseteq V$, $Q\subseteq W$ we use $A_{P,Q}$ to denote the submatrix induced by $P$ and $Q$ that contains all elements $A_{v,w}$ for $(v,w) \in P\times Q$. For vectors, we use similar notation such as $b\in \R^V$ and $b_v$ for $v\in V$ to denote the vector and its elements, respectively. The order of the elements of matrices will not be relevant, unless noted otherwise. For two vectors $y,z \in \R^W$, we use $\max(y,z)$ to be the element-wise maximum of $y$ and $z$, such that for all $w\in W$ we have $\max(y,z)_w \coloneqq \max(y_w,z_w)$. Note that for any vector $x\in \R^W$, we have the identity $x \coloneqq \max(x,\zerovec) - \max(-x,\zerovec)$. For a partition $\MP$ of a set $V$ and some set $V'\subseteq V$, we say that *$\MP$ is compatible with $V'$* if for all $P\in \MP$ either $P\subseteq V'$ or $P\cap V' = \emptyset$ holds.
