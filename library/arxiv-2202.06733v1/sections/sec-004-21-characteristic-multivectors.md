---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-004-21-characteristic-multivectors
section_title: "Characteristic Multivectors"
section_number: 2.1
pages: 3-3
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.964
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
\label{sect:char-mult}

The essential objects here are the {\em simplicial derivatives}\cite{hestenessobczyk}. If $f$ is a vector-valued linear function of a vector $a$ living in an $m$-dimensional space, $V_m$, and the output $f(a)$ lives in the same space (the simplest case) then we can define the $r$th simplicial derivative of $f$ as follows.

We let $\{a_k\}$, $k=1,\ldots,m$ be a {\em frame} for the space and $\{a^k\}$ its reciprocal frame, which is defined by the requirement $a^i \dt a_j= \delta^i_j$ for all $i$, $j$, and where $\delta^i_j$ is the Kronecker delta. We further define $b_k=f(a_k)$. Then the $r$th simplicial derivative is

\be
\partial_{(r)} f_{(r)} = \sum \left(a^{j_r} \wdg \ldots \wdg a^{j_1}\right) \left(b_{j_1} \wdg \ldots \wdg b_{j_r}\right)
\label{eqn:char-mult-def}
\ee

where the sum over the repeated indices is restricted by $0<j_1<\ldots<j_r\leq m$.

The point about these multivector quantities is that they provide {\em invariant} information about the function $f$. The invariance is in the sense that any frame $\{a_k\}$ could be chosen, and we would still get the same objects --- they are therefore in some sense `intrinsic' to the space $V_m$ and the function $f$.
