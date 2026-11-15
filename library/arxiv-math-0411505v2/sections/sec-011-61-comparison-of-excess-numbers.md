---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-011-61-comparison-of-excess-numbers
section_title: "Comparison of excess numbers"
section_number: 6.1
pages: 11-12
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.976
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
\lbl{sub.coexcess}

Given an admissible subgraph $c$ in $G_K^{(n)}$, let $f$ be the 
corresponding flow in $G_K$, to which $c$ projects, under the projection
$$
\pi: G_K^{(n)} \to G_K.
$$ 
In this section, we 
compare $\exc(f)$ (in Definition \ref{def.rotten}) with
$\exc(c)$.

As we will see, the two excess numbers do not agree. In this section
we will determine their difference.

We begin by introducing a partial ordering $\prec$ on the set of edges
of $G_K^{(n)}$. We warn the reader that this ordering is different 
from the ordering $<_v$ of the edges of $G_K$ entering vertex $v$,
introduced in Definition \ref{def.rotten}.

\begin{definition}
\lbl{def.orderf}
Consider two edges $e$ and $e'$ of $G_K^{(n)}$ which start at the vertices
$a^i_j$ and $a^{i'}_{j'}$  of $G_K^{(n)}$. We say that
$e \prec e'$ if
\begin{itemize}
\item
$e,e'$ end at the same vertex $v$ and $\pi(e) <_v \pi(e')$ in $G_K$, or
\item
$i=i'$ and $\sign(i)=+$ and $j < j'$, or
\item
$i=i'$ and $\sign(i)=-$ and $j' < j$
\end{itemize}
\end{definition}

Recall that $c\in \Sev_n(G_K)$ ($c$ admissible) if and only if
 $c$ is a collection of vertex disjoint directed cycles of $G_K^{(n)}$.
Hence the ordering on the edges of $c$ defined in Definition \ref{def.orderf}
induces a total ordering on each $\pi^{-1}(e)$, $e$  edge of $G_K$.

This total ordering may be seen from the cabling of the knot in the same way 
as the ordering $<_v$ of Definition \ref{def.rotten} may be seen from the knot:
if we travel along an arc $a^i_j$, we see one by one the arcs corresponding
to the starting vertices of edges of $\pi^{-1}(e)$, where $e$ is an edge of 
$G_K$.
This agrees with the total ordering on $\pi^{-1}(e)$ induced by $\prec$;
see Figure before \ref{lem.evenn}.


\begin{definition}
\lbl{def.XY}
Consider two edges $e$ and $e'$ of $G_K^{(n)}$ which end at the vertices
$a^i_j$ and $a^{i'}_{j'}$  of $G_K^{(n)}$. 
$$
X(e,e')=
\begin{cases}
1 & \text{if} \quad e, e'= \text{ red}, \quad 
e' \prec e, \quad \sign(s(e))= +, \quad j < j' \\
1 & \text{if} \quad e=\text{red}, \,\, e'=\text{blue},\,\, \\
& \pi(e), \pi(e') \,\, \text{do not start at the same vertex}, \\ 
& e' \prec e, \quad \sign(s(e))= +, \quad j < j' \\
1 & \text{if} \quad e,e'= \text{ red}, \quad
 e' \prec e, \quad \sign(s(e))= -, \quad 
j' <  j \\
1 & \text{if} \quad e=\text{red}, \,\, e'=\text{blue},\,\, \\
& \pi(e), \pi(e') \,\, \text{do not start at the same vertex}, \\ 
&  e' \prec e, \quad \sign(s(e))= -, \quad 
j' <  j \\
0 & \text{otherwise}
\end{cases}
$$
$$
Y(e,e')=
\begin{cases}
1 & \text{if} \quad e=\text{red}, \,\, e'=\text{blue},\,\, \\
& \pi(e), \pi(e') \,\, \text{start at the same vertex}, \quad e \prec e' \\
0 & \text{otherwise}
\end{cases}
$$
\end{definition}



\begin{lemma}
\lbl{lem.exc2}
Let $c$ be an admissible subgraph of $G_K^{(n)}$. 
Denote by $f$ the flow on $G_K$
which is the projection of $c$ to $G_K$. Then 
$$
\exc(c)=\exc(f) + \sum_{e}\sign(s(e)) \left(\sum_{e'}
X(e,e')+Y(e,e') \right) 
$$
where the summations of $e$ and $e'$ are over the set of edges of $c$ and
$s(e)$ denotes the starting vertex of $e$. 
\end{lemma}


\begin{proof}
Consider a crossing $v$ of $K$, and the corresponding $n^2$ crossings
of $K^n$. 
We count the contribution to  
$\exc(c)$ of pairs $(e,e')$ of edges of $c$ such that
\begin{itemize}
\item
$e$ projects to $e^b_v$ (the blue edge that starts at $v$),
and $e'$ does not project 
 to $e^r_v$ (the red edge that starts at $v$). This
gives $\exc(f)$.
\item
$e$ projects to $e^r_v$, and $e'$ does not project to $e^b_v$. This
gives the $X$-term in the formula. 
\item
$e$ projects to $e^r_v$, and $e'$  projects to $e^b_v$. 
This gives the $Y$-term in the formula. 
\end{itemize}
\end{proof}
