---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-005-3-the-arc-graph-of-a-knot-projection
section_title: "The arc-graph of a knot projection"
section_number: 3
pages: 5-7
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.99
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
\lbl{sec.arcgraph}

Given a knot projection $K$, we define the arc-graph $G_{\K}$ as follows:
\begin{itemize}
\item
The vertices of $G_{\K}$ are in 1-1 correspondence with the arcs of $\K$.
\item
The edges of $G_{\K}$ are in 1-1 correspondence with {\em transitions}
of $\K$, when we walk along $\K$ and we either go under a crossing 
(blue edges), 
or jump up at a crossing (red edges) according to Figure \ref{planarG2K}.
\end{itemize}

\begin{figure}[htpb]
$$ 
\psdraw{planar2GK}{3in}
$$
\caption{From a planar projection to the arc-graph. Transitions in 
the planar projection are indicated by dashed paths, and the corresponding 
edges in the arc-graph are blue (depicted with a small circle on them)
or red}\lbl{planarG2K}
\end{figure}

More formally, $G_{\K}$ is a weighted digraph defined as follows.

\begin{definition}
\lbl{def.arcgraph}
The {\em arc-graph} $G_{\K}$ has $r+1$ vertices $1,\dots, r+1$, $r+1$ {\em blue
directed edges} $(v,v+1)$ ($v$ taken modulo $r+1$) and $r+1$ {\em red 
directed edges} $(u,v)$, where at the crossing $u$ the arc that crosses over 
is labeled by $a_v$.

The vertices of $G_{\K}$ are equipped with a sign, where $\sign(v)$ is the
sign of the corresponding crossing $v$ of $\K$, and the edges of $G_{\K}$ are
equipped with a weight. The edge-weights are specified by matrix 
$W_{\K}= (\b_{ij})$
where 
$$
\b_{e}=
\begin{cases}
t^{-\sign(v)} & \text{if} \quad e=(v,v+1) \\
1-t^{-\sign(v)} & \text{if} \quad e=(v,u)
\end{cases}
$$
Here $t$ is a variable. Let $W_K$ denote the matrix obtained from $W_{\K}$
by deleting the last row and column.
Notice that $W_{\K}$ is formally stochastic
(i.e., the sum of the rows of $I-W_{\K}$ is zero), but $W_K$ is not.

Let $(G_K,W_K)$ denote the weighted digraph obtained by deleting the $r+1$ 
vertex
from $G_{\K}$, together with all edges to and from it. We let $V_K$ and $E_K$
denote the set of vertices and edges of $G_K$.
\end{definition}

It is clear from the definition that from every vertex of $G_{\K}$, the blue
outdegree is $1$, the red outdegree is $1$, and the blue indegree is $1$.
It is also clear that $G_{\K}$ has a Hamiltonian cycle that consists of all
the blue edges. We denote by $e_i^b$ ($e_i^r$) the blue (red) edge {\em leaving
vertex} $i$.

\begin{example}
\lbl{ex.1}
For the figure 8 knot we have:
$$
\psdraw{figure8}{1.5in}
$$
Its arc-graph $G_{\K}$ with the ordering and signs
of its vertices and  $G_K=G_{\K}-\{4\}$ are given by 
$$
\hspace{-1cm}
G_{\K}=
\psdraw{arc-graph2}{1.3in} \qquad G_K=
\psdraw{arc-graph-broken2}{0.3in}
$$  
where the blue edges are the ones with circles on them. Moreover, 
$$
W_{\K}=
\left[
\begin{matrix}
 0 & t & 0   & 1-t \\
 1-\bt & 0     & \bt & 0   \\
 0 & 1-t   & 0   & t \\
 \bt & 0   & 1-\bt   & 0   
\end{matrix}
\right] .
$$

\end{example}

\begin{definition}
\lbl{def.jj}
Let $\K$ be a knot projection. The {\em writhe} of $\K$, $\w(\K)$, is the 
sum of the signs of the
crossings of $\K$, and $\rot(K)$ is the {\em rotation number} of $K$, 
defined as follows: {\em smoothen} all crossings of $\K$, and consider the 
oriented circles that appear; one of them is special, marked by $\star$. 
The number of 
circles different from the special one whose orientation agrees with the 
special one, minus the number of circles whose orientation is opposite to the
special one is defined to be $\rot(K)$. 
We further let $\d(K,n)= 1/2 (n^2\w(\K)+n\rot(K))$, and $\d(K)= \d(K,1)$.
\end{definition}

We remark that we define $\rot(e)$ for each edge $e$ of $G_{\K}$ in 
Definition \ref{def.jjj}.
