---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-004-2-the-zeta-function-of-a-graph-and-the-quantum-m
section_title: "The zeta function of a graph and the quantum MacMahon Master Theorem"
section_number: 2
pages: 4-5
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.976
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
\lbl{sec.zeta}

One of main ingredients in our result is combinatorics of non-negative
integer flows on digraphs. They appear in an expression of the zeta function.

Let us recall what is the zeta function of a digraph. We will consider
digraphs (that is, graphs with oriented edges) with weights on their edges.

Let $G=(V,E)$ be a digraph with vertex set $V$ and directed edges $E \subset
V \times V$, and let $B=(\b_e)_{e\in E}$ be a weight matrix for the edges of 
$G$.
For edge $e$ we denote by $s(e), t(e)$ the starting and terminal vertex of $e$.
Bass-Ihara-Selberg defined
a zeta function of a graph in analogy with number theory and dynamical
systems, where the analogue of a prime number is a nonperiodic cycle.
Let us define the latter.

A {\em pointed walk} on a digraph is a 
sequence $(e_1, \dots, e_k)$ of edges such that the end of one coincides with 
the beginning of the next; we say that it is pointed at the beginning of $e_1$,
which is also called a {\em base point}. A {\em pointed closed walk} 
is a path whose beginning and end vertex coincide. 
Two pointed closed walks are {\em equivalent} if they differ on the choice
of base point only. By a {\em cycle} we will mean an equivalence class 
of pointed closed walks. A  cycle $c$ is {\em periodic} if $c=d^n$ for 
some closed walk $d$ and some integer $n>1$. Otherwise, it is called
{\em nonperiodic}. Let $\P(G)$ denote the set of {\em nonperiodic cycles}
of a digraph $G$. Using the weight function, we may define the weight $\b(c)$
of a cycle $c$ by $\b(c)= \prod_{e\in c}\b(e)$.

With the above preliminaries, Bass-Ihara-Selberg \cite{B} define

\begin{definition}
\lbl{def.zeta}
The {\em zeta function} $\zeta(G,B)$ of a weighted digraph $(G,B)$ is defined
by:
$$
\zeta(G,B)=\prod_{c \in \P(G)} \frac{1}{1-\b(c)}.
$$
\end{definition}

It follows by definition that
$$
\zeta(G,B)= \sum_{c \, \text{multisubsets of} \, \P(G)} \b(c)
$$

The actual definition of Bass-Ihara-Selberg uses more special
weights for the edges (each edge is given the same weight), and is used
to digraphs which are doubles (in the sense of replacing an unoriented edge
by a pair of oppositely oriented edges) of undirected graphs.
 
Foata-Zeilberger proved that the zeta function is a
rational function, and in fact given by the inverse of a determinant. Moreover,
the zeta function is given by a sum over flows. 

\begin{definition}
\lbl{def.flow}  
A {\em flow} $f$ on a digraph $G$ is a function $f:
\mathrm{Edges}(G)\longto \BN$
of the edges of $G$ that satisfies the (Kirkhoff) {\em conservation law}
$$
\sum_{e \, \text{begins at} \, v} f(e)=\sum_{e \, \text{ends at} \, v}
f(e)
$$
at all vertices $v$ of $G$. Let $f(v)$ denote this quantity and let $\F(G)$ 
denote the {\em set of flows} of a digraph $G$.  
\end{definition}

If $\beta$ is a weight function on
the set of edges of $G$ and $f$ is a flow on $G$, then
\begin{itemize}
\item
the {\em weight} $\b(f)$ of $f$ is given by
$\b(f)=\prod_e \b(e)^{f(e)}$, where 
$\b(e)$ is the weight of the edge $e$. 
\item
The {\em multiplicity} at a vertex $v$ with outgoing edges $e_1,e_2,\dots$ is 
given by $\mult_v(f)=\binom{f(e_1)+f(e_2)+
\dots}{f(e_1),f(e_2),\dots}$, and the {\em multiplicity} of $f$ is given by
$\mult(f)=\prod_v \mult_v(f)$. 
\item
If $A$ is a subset of edges then we let $f(A)=\sum_{e\in A} f(e)$.
\end{itemize}


Let us summarize Foata-Zeilberger's theorem \cite[Theorem 1.1]{FZ} here. For 
the sake of completeness we include its proof in Appendix \ref{sec.FZ}.

\begin{theorem}
\lbl{thm.FZ}
If $(G,B)$ is a weighted digraph, then
\begin{eqnarray}
\lbl{eq.zeta1}
\zeta(G,B) 

&=& \frac{1}{\det(I-B)} \\
\lbl{eq.zeta2}
&=& \sum_{f \in \F(G)} \b(f)\, \mult(f) .
\end{eqnarray}
\end{theorem}

\begin{remark}
\lbl{rem.comb}
For $r=1$, the above Theorem states that
$$
\frac{1}{1-x}=\sum_{n=0}^\infty x^n
$$
where $x=b_{11}$. Thus, Theorem \ref{thm.FZ} is a version of the geometric
series summation.
\end{remark}

Another formula for the inverse of a determinant, the MacMahon Master Theorem, 
has been mentioned 
in the introduction. We will need its quantum version, proved in \cite{GLZ}.

In $r$-dimensional {\em quantum algebra} we have $r$ indeterminates 
$x_i$ ($1\leq i\leq r$),
satisfying the commutation relations $x_jx_i=qx_ix_j$ for all 
$1\leq i<j\leq r$. 
Further we are given a right-quantum matrix $A$. We assume
that the indeterminates of $A$ commute with the $x_i$'s. The following 
theorem has been proven
recently in \cite{GLZ}. 

\begin{theorem}
\lbl{thm.qMM}
Let $A$ be a right-quantum matrix of size $r$. For $1\leq i\leq r$ let 
$X_i=\sum_{j=1}^ra_{ij}x_j$,
and for any vector $(m_1,\dots, m_r)$ of non-negative integers let 
$G_A(m_1,\dots, m_r)$ be
the coefficient of $x_1^{m_1}x_2^{m_2}\dots x_r^{m_r}$ in 
$\prod_{i=1}^rX_i^{m_i}$. Then
$$
\sum_{m_1,\dots, m_r=0}^{\infty}G_A(m_1,\dots, m_r)=1/\Ferm(A).
$$
\end{theorem}
