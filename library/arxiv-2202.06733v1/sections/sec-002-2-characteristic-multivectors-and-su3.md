---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-002-2-characteristic-multivectors-and-su3
section_title: "Characteristic multivectors and SU(3)"
section_number: 2
pages: 2-3
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.992
---
\label{sect:first-su3}

In a paper also in these proceedings, Lasenby \etal\cite{lasenby-char-multi} discuss the role of `characteristic multivectors' in finding the rotor that corresponds to the finite rotation from one frame of vectors to another. 

Here, where we are concerned overall with a {\em particle physics} context, we want to start by looking at how characteristic multivectors relate to the {\em infinitesimal generators} that correspond to a generalised rotation. This will enable us to make contact with recent developments in the decomposition of bivectors into sums of mutually commuting blades as recently discussed in papers by Roelfs\cite{roelfs2021geometric} and by Roelfs and de Keninck\cite{roelfs2021graded}, whilst also allowing us to lay the groundwork for our discussions of the group $SU(3)$, which will be a central theme of this paper.

We start with a brief introduction to characteristic multivectors, and their role in the Cayley-Hamilton Theorem, by giving a summary of the relevant parts of the introduction to these in \cite{lasenby-char-multi}. Please see \cite{lasenby-char-multi} for further details.


\subsection{Characteristic Multivectors}

\label{sect:char-mult}

The essential objects here are the {\em simplicial derivatives}\cite{hestenessobczyk}. If $f$ is a vector-valued linear function of a vector $a$ living in an $m$-dimensional space, $V_m$, and the output $f(a)$ lives in the same space (the simplest case) then we can define the $r$th simplicial derivative of $f$ as follows.

We let $\{a_k\}$, $k=1,\ldots,m$ be a {\em frame} for the space and $\{a^k\}$ its reciprocal frame, which is defined by the requirement $a^i \dt a_j= \delta^i_j$ for all $i$, $j$, and where $\delta^i_j$ is the Kronecker delta. We further define $b_k=f(a_k)$. Then the $r$th simplicial derivative is

\be
\partial_{(r)} f_{(r)} = \sum \left(a^{j_r} \wdg \ldots \wdg a^{j_1}\right) \left(b_{j_1} \wdg \ldots \wdg b_{j_r}\right)
\label{eqn:char-mult-def}
\ee

where the sum over the repeated indices is restricted by $0<j_1<\ldots<j_r\leq m$.

The point about these multivector quantities is that they provide {\em invariant} information about the function $f$. The invariance is in the sense that any frame $\{a_k\}$ could be chosen, and we would still get the same objects --- they are therefore in some sense `intrinsic' to the space $V_m$ and the function $f$.
