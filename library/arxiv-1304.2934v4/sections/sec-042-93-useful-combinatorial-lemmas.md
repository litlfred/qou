---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-042-93-useful-combinatorial-lemmas
section_title: "Useful combinatorial lemmas"
section_number: 9.3
pages: 73-76
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.974
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
We start our proof of Theorem \ref{thm:dependencygraphsrefined} by stating a few lemmas on graphs and spanning trees.


\subsubsection{A functional on graphs}
In this section, we consider graphs $H$ with multiple edges and loops. We use the standard notation $V(H)$ and $E(H)$ for their vertex and edge sets. For a graph $H$ and a set partition $\pi$ of $V(H)$, we denote $\pi \perp H$ when the following holds: for any edge $\{i,j\} \in E(H)$, the elements $i$ and $j$ lie in different parts of $\pi$ (in this case we use the notation $i \nsim_\pi j$). We introduce the following functional on graphs $H$:
$$\SF_{H}=(-1)^{|V(H)|-1}\sum_{\pi \perp H}\mu(\pi).$$

\begin{lemma}
For any graph $H$, one has
$$\SF_{H}= \sum_{\substack{E \subset E(H) \\ (V(H),E)\text{ connected}}} (-1)^{|E|-|V(H)|+1}.$$
\end{lemma}

\begin{proof}
To simplify notation, suppose $V(H)=[r]$. We denote $\mathbbm{1}_{(P)}$ the characteristic function of the property $(P)$. By inclusion-exclusion,
\begin{align*}
(-1)^{|V(H)|-1}\,\SF_{H}&= \sum_{\pi \in \qym(r)} \!\left( \prod_{(i,j) \in E(H)}
\mathbbm{1}_{i \nsim_{\pi} j} \right) \mu(\pi)=\sum_{\pi \in \qym(r)}\!
\left( \prod_{(i,j) \in E(H)} (1- \mathbbm{1}_{i \sim_{\pi} j})\right) \mu(\pi)\\
&= \sum_{E \subset E(H)} \sum_{\pi \in \qym(r)} (-1)^{|E|} \left( \prod_{(i,j) \in E}  \mathbbm{1}_{i \sim_{\pi} j} \right)  \mu(\pi) \\
&= \sum_{E \subset E(H)} (-1)^{|E|} \left[ \sum_{\substack{\pi \text{ such that } \\ \forall (i,j) \in E,\,\, i \sim_\pi j}} \mu(\pi) \right].
\end{align*}
But the quantity in the bracket is $0$ unless the only partition in the sum is the maximal partition $\big\{[r]\big\}$, in which case it is $1$. This corresponds to the case where the edges in $E$ form a connected subgraph of $H$.
\end{proof}
\medskip

\begin{corollary}
The functional $\SF_H$ fulfills the deletion-contraction induction, \emph{i.e.}, if $e$ is an edge of $H$ which is not a loop, then
$$\SF_H = \SF_{H / e} + \SF_{H \setminus e},$$
where $H \setminus e$ (respectively $H / e$) are the graphs obtained from $H$ by deleting (resp. contracting) the edge $e$.
\end{corollary}

\begin{proof}
The first term corresponds to sets of edges containing $e$, and the second to those that do not contain $e$.
\end{proof}
\bigskip

This induction (over-)determines $\SF_H$ together with the initial conditions:
$$\begin{cases}
&\SF_{\includegraphics{node.pdf}}=1, \\
&\SF_{\! \!\! \GraphOneLoop } \! =\SF_{\!  \!\! \!\GraphTwoLoops } \!=\cdots=0,\phantom{}\vspace{2mm}\\
&\SF_{H}=0\quad\text{ if $H$ is disconnected}.
\end{cases}$$

\begin{corollary}\label{cor:ineq_SFST}
For any graph $H$, the quantity $\SF_H$ is nonnegative and less or equal than the number $\ST_H$ of spanning trees in $H$.
\end{corollary}

\begin{proof}
The quantity $\ST_H$ fulfills the same induction as $\SF_H$ with initial conditions:
$$\hspace{2cm}\begin{cases}
&\ST_{\includegraphics{node.pdf}}=1, \\
&\ST_{\! \! \GraphOneLoop } \!=\ST_{ \! \! \GraphTwoLoops } \!=\cdots=1, \phantom{}\vspace{2mm}\\
&\ST_{H}=0\quad\text{ if $H$ is disconnected}.
\end{cases}\vspace*{-7mm}$$
\end{proof}
\medskip

\begin{remark}
If $H$ is connected, both $\SF_H$ and $\ST_{H}$ are actually specializations of the bivariate \emph{Tutte polynomial} $T_{H}(x,y)$ of $H$ (\emph{cf.} \cite[Chapter X]{Bol98}):
$$\SF_{H}=T_{H}(1,0)\qquad;\qquad\ST_{H}=T_{H}(1,1).$$
This explains the deletion-contraction relation. As the bivariate Tutte polynomials has non-negative coefficients, it also explains the inequality $0 \le \SF_H \le \ST_H$.
\end{remark}
\bigskip



\subsubsection{Induced graphs containing spanning trees}
Fix a graph $G$ (typically the dependency graphs of our family of variables). For a list $(v_1,\dots,v_r)$ of $r$ vertices of $G$, we define the induced graph $G[v_1,\dots,v_r]$ as follows:\vspace{2mm}
\begin{itemize}
    \item its vertex set is $[r]$;\vspace{2mm}
    \item there is an edge between $i$ and $j$ if and only if 
        $v_i=v_j$ or $v_i$ and $v_j$ are linked in $G$.\vspace{2mm}
\end{itemize}
We will be interested in spanning trees of induced graphs. As the vertex set is $[r]$, these spanning trees may be seen as {\em Cayley trees}. Recall that a Cayley tree of size $r$ is by definition a tree with vertex set $[r]$ (Cayley trees are neither rooted, nor embedded in the plane, they are only specified by an adjacency matrix). These objects are enumerated by the well-known Cayley formula established by C. Borchardt in \cite{Borchardt60}: there are exactly $r^{r-2}$ Cayley trees of size $r$.

\begin{lemma}
    Fix a Cayley tree $T$ of size $r$ and a graph $G$ with $N$ vertices and maximal degree $D$.
    Fix a vertex $v_1$ of $G$.
    The number of lists $(v_1,\dots,v_r)$ of $r$ vertices of $G$
    such that $T$ is contained in the induced subgraph $G[v_1,\dots,v_r]$ is bounded from above by
    \[ (D+1)^{r-1}. \]
\end{lemma}

\begin{proof}
    Lists $(v_1,\dots,v_r)$ as in the lemma are constructed as follows. First consider a neighbor $j$ of $1$ in $T$. As we require $G[v_1,\dots,v_r]$ to contain $T$, the vertices $1$ and $j$ must also be neighbors in $G[v_1,\dots,v_r]$, {\it i.e.} $v_j=v_1$ or $v_j$ is a neighbor of $v_1$ in $T$. Thus, once $v_1$ is fixed, there are at most $D+1$ possible values for $v_j$. The same is true for all neighbors of $1$ and then for all neighbors of neighbors of $1$ and so on.
\end{proof}
\medskip

We have the following immediate consequence.
\begin{corollary}
    \label{cor:countingcouplessequences_ST}
    Let $G$ be a graph with $n$ vertices and maximal degree $D$ and $r\ge 1$.
    Fix a vertex $v_1$ of $G$.
    The number of couples 
    $\big( (v_1,\dots,v_r), T  \big) $
    where each $v_i$ is a vertex of $V$ and $T$ a spanning tree of
    the induced subgraph $G[v_1,\dots,v_r]$ is bounded above by
    \[r^{r-2} \, (D+1)^{r-1}.\]
\end{corollary}\bigskip


\subsubsection{Spanning trees and set partitions of vertices}
Recall that $\ST_H$ denotes the number of spanning trees of a graph $H$. Consider now a graph $H$ with vertex set $[r]$ and a set partition $\pi=(\pi_1,\dots,\pi_t)$ of $[r]$. For each $i$, we denote $\ST^{\pi_i}(H)=\ST_{H[\pi_i]}$ the number of spanning trees of the graph induced by $H$ on the vertex set $\pi_i$. We also use the multiplicative notation
$$\ST^\pi(H) = \prod_{j=1}^t \ST^{\pi_j}(H).$$
We can also consider the contraction $H/\pi$ of $H$ with respect to $\pi$. By definition, it is the multigraph ({\em i.e.} graph with multiple edges, but no loops) defined as follows. Its vertex set is the index set $[t]$ of the parts of $\pi$ and, for $i \neq j$, there are as many edges between $i$ and $j$ as  edges between a vertex of $\pi_i$ and a vertex of $\pi_j$ in $H$. Denote $\ST_{\pi}(H)=\ST_{H/\pi}$ the number of spanning trees of this contracted graph (multiple edges are here important). This should not be confused with $\ST^\pi(H)$: in the latter, $\pi$ is placed as an exponent because the quantity is multiplicative with respect to the part of $\pi$.
\bigskip

Note that the union of a spanning tree $\overline{T}$ of $H/\pi$ and  of spanning trees $T_i$ of $H[\pi_i]$ (one for each $1 \le i \le t$) gives a spanning tree $T$ of $H$. Conversely, take a spanning tree $T$ on $H$ and a bicoloration of its edges. Edges of color $1$ can be seen as a subgraph of $H$ with the same vertex set $[r]$. This graph is of course acyclic. Its connected components define a partition $\pi=\{\pi_1,\dots,\pi_t\}$ of $[r]$ and edges of color $1$ correspond to a collection of spanning trees $T_i$ of $H[\pi_i]$ (for $1 \le i \le t$). Besides, edges of color $2$ define a spanning tree $\overline{T}$ on $H/\pi$.\bigskip

Therefore, we have described a bijection between spanning trees $T_0$ of $H$ with a bicoloration of their edges and triples $(\pi,\overline{T},(T_i)_{1\le i \le t})$ where:\vspace{2mm}
\begin{itemize}
    \item $\pi$ is a set partition of the vertex set $[r]$ of $H$ (we denote $t$ its number of parts);\vspace{2mm}
    \item $\overline{T}$ is a spanning tree of the contracted graph $H/\pi$;\vspace{2mm}
    \item for each $1 \le i \le t$,  $T_i$ is a spanning tree of the induced graph $H[\pi_i]$.\vspace{2mm}
\end{itemize}
Before giving a detailed example, let us state the numerical corollary of this bijection:
\begin{equation}\label{eq:coloredpseudotree}
    2^{r-1} \,\ST_H = \sum_{\pi} \ST_\pi(H) \,\ST^\pi(H),
\end{equation}
where the sum runs over all set partitions $\pi$ of $[r]$.

\begin{center}
\begin{figure}[ht]
    $$T=\begin{array}{c}
        \begin{tikzpicture}
    \tikzstyle{vertex1}=[circle,draw,inner sep=0.5pt,minimum size=1mm]
    \tikzstyle{vertex2}=[rectangle,draw,inner sep=1.5pt,minimum size=1mm]
    \tikzstyle{rededge}=[red, dotted,thick,line width=1.2pt]
    \tikzstyle{blueedge}=[blue!90!white,thick,line width=1.2pt]
    \tikzstyle{greenedge}=[ForestGreen!80!white, dashed,thick,line width=1.2pt]
    \node (v1) at (0:1) [vertex1] {\footnotesize $1$};
    \node (v2) at (60:1) [vertex1] {\footnotesize $2$};
    \node (v3) at (120:1) [vertex1] {\footnotesize $3$};
    \node (v4) at (180:1) [vertex1] {\footnotesize $4$};
    \node (v5) at (240:1) [vertex1] {\footnotesize $5$};
    \node (v6) at (300:1) [vertex1] {\footnotesize $6$};
    \draw [blueedge] (v1) to (v2);
    \draw [blueedge] (v2) to (v3);
    \draw [blueedge] (v4) to (v5);
    \draw [blueedge] (v4) to (v6);
    \draw [greenedge] (v3) to (v5);
    \draw [rededge] (v3) to (v1);
    \draw [rededge] (v1) to (v4);
    \draw [rededge] (v2) to (v6);
    \draw [rededge] (v1) to (v6);
\end{tikzpicture} \end{array}\,\,\leftrightarrow\,\,
        \begin{cases}
        \,\,\,\,\pi=\{\pi_1,\pi_2\} \text{ with }\pi_1=\{1,2,3\},\ \pi_2=\{4,5,6\};\\
        \\
        \,\,\,\,T_1=\begin{array}{c}
        \begin{tikzpicture}
    \tikzstyle{vertex1}=[circle,draw,inner sep=0.5pt,minimum size=1mm]
    \tikzstyle{vertex2}=[rectangle,draw,inner sep=1.5pt,minimum size=1mm]
    \tikzstyle{rededge}=[red, dotted,thick,line width=1.2pt]
    \tikzstyle{blueedge}=[blue!90!white,thick,line width=1.2pt]
    \tikzstyle{greenedge}=[ForestGreen!80!white, dashed,thick,line width=1.2pt]
    \node (v1) at (0:1) [vertex1] {\footnotesize $1$};
    \node (v2) at (60:1) [vertex1] {\footnotesize $2$};
    \node (v3) at (120:1) [vertex1] {\footnotesize $3$};
    \draw [blueedge] (v1) to (v2);
    \draw [blueedge] (v2) to (v3);
    \draw [rededge] (v3) to (v1);
        \end{tikzpicture} 
        \end{array},\quad 
        T_2=\begin{array}{c}
        \begin{tikzpicture}
    \tikzstyle{vertex1}=[circle,draw,inner sep=0.5pt,minimum size=1mm]
    \tikzstyle{vertex2}=[rectangle,draw,inner sep=1.5pt,minimum size=1mm]
    \tikzstyle{rededge}=[red, dotted,thick,line width=1.2pt]
    \tikzstyle{blueedge}=[blue!90!white,thick,line width=1.2pt]
    \tikzstyle{greenedge}=[ForestGreen!80!white, dashed,thick,line width=1.2pt]
    \node (v4) at (180:1) [vertex1] {\footnotesize $4$};
    \node (v5) at (240:1) [vertex1] {\footnotesize $5$};
    \node (v6) at (300:1) [vertex1] {\footnotesize $6$};
    \draw [blueedge] (v4) to (v5);
    \draw [blueedge] (v4) to (v6);
        \end{tikzpicture} 
        \end{array};\\
        \\
        \,\,\,\,\overline{T}=\begin{array}{c}
        \begin{tikzpicture}
    \tikzstyle{vertex1}=[circle,draw,inner sep=0.5pt,minimum size=1mm]
    \tikzstyle{vertex2}=[rectangle,draw,inner sep=1.5pt,minimum size=1mm]
    \tikzstyle{rededge}=[red, dotted,thick,line width=1.2pt]
    \tikzstyle{blueedge}=[blue!90!white,thick,line width=1.2pt]
    \tikzstyle{greenedge}=[ForestGreen!80!white, dashed,thick,line width=1.2pt]
    \node (v123) at (60:1) [vertex1] {\footnotesize $\pi_1$};
    \node (v456) at (240:1) [vertex1] {\footnotesize $\pi_2$};
    \draw [rededge] (v123) to [bend right=-60] (v456);
    \draw [rededge] (v123) to [bend right=20] (v456);
    \draw [rededge] (v123) to [bend right=-20] (v456);
    \draw [greenedge] (v123) to [bend right=60] (v456);
\end{tikzpicture}
        \end{array}.
        \end{cases}
$$
    \caption{Bijection explaining Identity \eqref{eq:coloredpseudotree}.}
    \label{fig:partitionspanningtrees}
\end{figure}
\end{center}
Our bijection is illustrated on Figure \ref{fig:partitionspanningtrees}, with the following conventions.\vspace{1.5mm}
\begin{itemize}
    \item On the left, blue plain edges are edges of color $1$ in the tree $T_0$; on the right, these blue plain edges are the edges of the spanning trees $T_i$.\vspace{1.5mm}
    \item On the left, green dashed edges are edges of color $2$ in the tree $T_0$; on the right, these green dashed edges are edges of the spanning tree $\overline{T}$.\vspace{1.5mm}
    \item Red dotted edges belong to the graphs $H$, $H/\pi$, $H[\pi_i]$ but not to their spanning tree $T_0,\overline{T},T_i$.\vspace{1.5mm}
\end{itemize}
Note that in this example the graph $H/\pi$ has two vertices linked by four edges. These four edges correspond to the edges $(1,4)$, $(1,6)$, $(2,6)$ and $(3,5)$ of $H$. In the example, the spanning tree $\overline{T}$ is the edge $\{(3,5)\}$. If we had chosen another edge, the tree $T$ on the left-hand side would have been different. Hence, in the Equality \eqref{eq:coloredpseudotree}, the multiple edges of $H/\pi$ must be taken into account: in our example, $\ST_\pi(H)=4$.\bigskip
