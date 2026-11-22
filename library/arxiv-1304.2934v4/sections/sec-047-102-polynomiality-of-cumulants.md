---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-047-102-polynomiality-of-cumulants
section_title: "Polynomiality of cumulants"
section_number: 10.2
pages: 83-85
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.962
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\subsubsection{Dealing with several arrangements}
Consider a list $(A^1,\dots,A^r)$ of arrangements. We associate to this data two graphs  (unless said explicitly, we always consider loopless simple graphs, and $V(G)$ and $E(G)$ denote respectively the edge and vertex sets of a graph $G$):\vspace{2mm}
\begin{itemize}
 \item the graph $G_\AA$ has vertex set
   $$V_{\Bbbk}=V(G_{\AA})= \{ (t,i) \,\,|\,\, 1 \le i \le r, 1 \le t \le k_i \}$$
and an edge between $(t,i)$ and $(s,j)$ if and only if $a^i_t=a^j_s$. It is always a disjoint union of cliques. If the $A^i$'s are arrangements, then the graph $G_\AA$ is endowed with a natural proper $r$-coloring, $(t,i)$ being of color $i$.\vspace{2mm}
\item the graph $H^m_\AA$  has vertex set $[r]$ and an edge between $i$ and $j$ if $|A^i \cap A^j| \geq m$. \vspace{2mm}
\end{itemize}
Notice that $H^1_{\AA}$ is the \emph{contraction} of the graph $G_{\AA}$ by the map $\varphi : (t,i) \mapsto i$ from the vertex set of $G_\AA$ to the vertex of $H^1_\AA$. Indeed,
$$(i,j) \in E(H^1_\AA) \ \Leftrightarrow \ \exists v_i \in \varphi^{-1}(i), v_j  \in \varphi^{-1}(j) \text{ such that } (v_i,v_j) \in E(G_\AA).$$
An example of a graph $G_\AA$ and of its 1- and 2-contractions $H^1_\AA$ and $H^2_\AA$ is drawn on Figure \ref{fig:graphsGandH}. For $m \ge 2$, the definition of $H^m_\AA$ is less common. We call it the $m$-contraction of $G_\AA$. The $2$-contraction is interesting for us. It corresponds exactly to the graph induced by the dependency graph $\B$ on the list of arrangement $\AA$, considered in the proof of Theorem~\ref{thm:dependencygraphsrefined}.

\begin{figure}[ht]
\includegraphics{color.pdf}
\caption{The graphs $G_\AA$, $H^1_\AA$ and $H^{2}_{\AA}$ corresponding to the family of arrangements $(15,13,14,11,12)$, $(2,5,6,4,1)$, $(2,7,9,4)$, $(4,16,3)$,  and $(8,10,5)$.}
\label{fig:graphsGandH}
\end{figure}

\begin{remark}
Graphs associated to families of arrangements are a practical way to encode some information and should not be confused with the random graphs or their induced subgraphs. Therefore we used greek letters for the latter and latin letter for graphs $G_\AA$ and their contractions. The dependency graph will always be called $\B$ to avoid confusions.
\end{remark}
\bigskip



\subsubsection{Exploiting symmetries}
The dependency graph of our model has much more structure than a general dependency graph. In particular, all variables $\delta_\gamma(A)$ are identically distributed. More generally, the joint distribution of
\[ \left( \delta_\gamma(A^1),\dots,\delta_\gamma(A^r) \right) \]
depends only on $G_\AA$. Here, we state a few consequences of this invariance property that will be useful
in the next Section.

\begin{lemma}\label{lem:indjointmoments}
Fix a graph $\gamma$ of size $k$, the quantity
$$\esper\!\left[ \delta_{\gamma}(A^1) \cdots \delta_{\gamma}(A^r) \right]$$
depends only on the graph $G_\AA$ associated to the family of arrangements $(A^1,\dots,A^r)$. The same is true for the joint cumulant $\kappa\left( \delta_{\gamma}(A^1), \dots, \delta_{\gamma}(A^r) \right).$
\end{lemma}

\begin{proof}
The first statement follows immediately  from the invariance of the model $\Gamma(n,p)$ by relabelling of the vertices. The second is a corollary, using the moment-cumulant relation \eqref{eq:moment2cumulant}.
\end{proof}
\medskip 

\begin{corollary}
Fix some graph $\gamma$.
Then the joint cumulant $\kappa(\SubGraph_{\gamma},\dots,\SubGraph_{\gamma})$ is a polynomial in $n$.
\label{cor:jointcumulantpoly}
\end{corollary}

\begin{proof}
Using Lemma \ref{lem:indjointmoments}, we can rewrite the expansion \eqref{eq:expcumulant} as
\begin{equation}
    \kappa(\SubGraph_{\gamma},\dots,\SubGraph_{\gamma}) = \sum_G \kappa(G) N_G,
    \label{eq:expansioncumulantgraphs}
\end{equation}
where:\vspace{2mm}
\begin{itemize}
    \item the sum runs over graphs $G$ of vertex set $V_\Bbbk$ that correspond to some arrangements (that is $G$ is a disjoint union of cliques and, for any $s$, $t$ and $i$, there is no edge between $(s,i)$ and $(t,i)$);\vspace{2mm}
    \item $\kappa(G)$ is the common value of $\kappa\left( \delta_{\gamma}(A^1), \dots, \delta_{\gamma}(A^r) \right)$, where $(A^1,\dots,A^r)$ is any list of arrangements with associated graph $G$;\vspace{2mm}
    \item $N_G$ is the number of lists of arrangements with associated graph $G$.\vspace{2mm}
\end{itemize}
But it is clear that the sum index is finite and that neither the summation index nor the quantity $\kappa(G)$ depend on $n$. Besides, the number $N_G$ is simply the falling factorial $n(n-1)\dots(n-c_G+1)$, where $c_G$ is the number of connected components of $G$. The corollary follows from these observations.
\end{proof}
\bigskip
