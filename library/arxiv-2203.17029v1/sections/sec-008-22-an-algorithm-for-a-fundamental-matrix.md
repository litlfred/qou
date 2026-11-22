---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-008-22-an-algorithm-for-a-fundamental-matrix
section_title: "An algorithm for a fundamental matrix"
section_number: 2.2
pages: 13-14
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.97
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.algorithm}

In this section we review an algorithm to obtain a fundamental matrix solution
to a $q$-holonomic module given by Dreyfus~\cite{Dreyfus:building} using the
$q$-Borel and the $q$-Laplace transform. Let us describe the main steps here.

\noindent $\bullet$
Choose a cyclic vector to present a $q$-holonomic module in the form of a linear
$q$-difference equation

\be
\label{qdiffeqn}
\sum_{j=0}^r a_j \s^j f =0
\ee
where $f=f(t,q)$, $(\s f)(t,q)=f(qt,q)$ and $a_j(t,q) \in \BQ(q)[t^{\pm 1}]$,
with $a_r \neq 0$. The rest of the algorithm depends on~\eqref{qdiffeqn} alone.

\noindent $\bullet$
The lower Newton polygon of~\eqref{qdiffeqn} is the lower convex hull
of the points $(j, v_0(a_j))$ for $j=0,\dots,r$, where $v_0(p)$ denotes the
minimum $t$-exponent of a Laurent polynomial $p(t)$ (with the convention that
$v_0(0)=\infty$). The boundary of the lower Newton
polygon is a finite sequence of edges with increasing slopes. 

\noindent $\bullet$
For each edge of the lower Newton polygon, we replace our function by a ratio
of theta functions times a new function, so that the corresponding edge is now
horizontal, and then apply the Frobenius method to get $t$-formal power
series solutions, once for each root of the indicial polynomial of the edge.
If $\kappa$ is the slope of the edge and an integer, the solutions have the form
\be
\theta(t;q)^{\kappa}
\sum_{k=0}^{\infty}\alpha_{k}(q)t^{k}\frac{\theta(\rind^{-1}t;q)}{\theta(t;q)}
\ee
where $\rind$ is determined by the roots of the indicial polynomial of the edge.
A special feature in the equations that we study is that the roots of the indicial
polynomials are roots of unity times a fractional power of $q$ times a monomial
in any additional variables.

\noindent $\bullet$
If a solution is not convergent at $t=0$, apply a $q$-Borel transform, followed by
an iterated $q$-Laplace transform (defined below), to construct a fundamental matrix
$U(t,q)$ of analytic solutions at $t=0$.
The $q$-Borel and $q$-Laplace transforms preserve linear $q$-difference equations
and change their Newton polygons by an affine linear transformation.

\noindent $\bullet$
Repeat the above steps using the upper Newton polygon of~\eqref{qdiffeqn}, that
is the upper convex hull of the points $(j, v_\infty(a_j))$ for $j=0,\dots,r$,
where $v_\infty(p)$ denotes the maximum $t$-exponent of a Laurent polynomial $p(t)$
(with the convention that $v_\infty(0)=-\infty$). Call the corresponding fundamental
matrix $V(t,q)$.

The ratio $M = V^{-1} U$ is a matrix of elliptic functions. These functions depend
on additional elliptic parameters that come from the $q$-Laplace transform,
a feature of $q$-difference equations which is absent in the world of linear
differential equations. The connection problem, i.e., the determination of this
matrix, is largely unsolved, with partial success for the case of many
$q$-hypergeometric difference equations; see Ohyama, Morita
~\cite{Morita:stokes-qdiff, Morita:stokes-rama,Ohyama:talk,Ohyama:connection}.
