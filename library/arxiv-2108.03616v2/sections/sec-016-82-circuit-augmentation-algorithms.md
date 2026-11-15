---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-016-82-circuit-augmentation-algorithms
section_title: "Circuit augmentation algorithms"
section_number: 8.2
pages: 29-31
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.989
---
\label{subsec:circ-diameter-algorithms}
The generic \emph{circuit augmentation algorithm} is a circuit walk  $x^{(1)},x^{(2)},\ldots,x^{(k+1)}\in P$ as defined above, such that an initial  feasible $x^{(0)}$ is given, 
and $\pr{c}{x^{(t+1)}}<\pr{c}{x^{(t)}}$, i.e., the objective value decreases in every iteration.
The elementary vector $g$ is an \emph{augmenting direction} for the solution $x^{(t)}$
 if and only if $\pr{c}{g}<0$, $g_i\ge 0$ for every $x^{(t)}_i=0$ and $g_i\le 0$ for every  $x^{(t)}_i=u_i$. By LP duality, $x^{(t)}$ is optimal if and only if no augmenting direction exists. Otherwise, the algorithm proceeds to the next iterate  $x^{(t+1)}$ by a maximal augmentation in an augmenting direction.

The simplex algorithm can be seen as a circuit augmentation algorithm that is restricted to using special elementary vectors corresponding to edges of the polyhedron.\footnote{Simplex may contain degenerate pivots when the basic solution remains the same; we do not count these as augmentation steps.} For the general framework, the iterates $x^{(k)}$ may not be vertices. However, in case of maximal augmentations, they must all lie on the boundary of the polyhedron.

\medskip

In unpublished work, Bland~\cite{Bland76} extended the Edmonds--Karp--Dinic algorithm \cite{dinic1970algorithm,Edmonds72} algorithm for general LP, see also \cite[Proposition 3.1]{Lee89}. Circuit augmentation algorithms were revisited by De Loera, Hemmecke, and Lee in 2015 \cite{DHL15}, analyzing different augmentation rules and extending them to integer programming. We give an overview of their results first for linear programming. In particular, they studied three augmentation rules that use maximal augmentation. Let  $x^{(t)}$ be the current feasible solution, and we aim to select an augmenting direction $g$ as follows.
\begin{itemize}
	\item \emph{Dantzig-descent direction:} Select $g$ such that $-\pr{c}{g}$ is maximized, where $g=g^C$ is the elementary vector with $\lcm(g^C)=1$ for a circuit $C\in \circuits_W$.
	\item \emph{Deepest-descent direction:} Select $g$ such that $-\alpha\pr{c}{g}$ is maximized, where $\alpha$ is the maximal stepsize for $x^{(t)}$ and $g$.
	\item \emph{Steepest-descent direction:} Select $g$ such that $-\pr{c}{g}/\|g\|_1$ is maximized.
\end{itemize}

Computing Dantzig- and deepest-descent directions is in general NP-hard, see \cite{DKS19} and  as detailed below. The steepest-descent direction can be formulated by an LP; but without any restrictions on the input problem, this may not be simpler than the original one. However, it could be easier to solve in practice; Borgwardt and Viss \cite{BorgwardtV2020} exhibits an implementation of a steepest-descent circuit augmentation algorithm with encouraging computational results.


\subsubsection{Augmenting directions for flow problems} 

 It is instructive to consider these algorithms  for the special case of \emph{minimum-cost flows}. Given a directed graph $D=(V,E)$ with capacities $u\in \R^E$, costs $c\in \R^E$, and node demands $b\in \R^V$ with $b(V)= \sum_{i \in V} b_i = 0$. The objective is to find the minimum cost flow $x$ that satisfies the capacity constraints: $0\le x\le u$, and the node demands: for each node $i\in V$, the total incoming minus the total outgoing flow equals $b_i$. This can be written in the form \ref{LP-augment} with $A$ as the node-arc incidence matrix of $D$, a TU matrix. 
Let us define the \emph{residual graph} $D_x=(V,E_x)$, where 
for $(i,j)\in E_x$ we let $(i,j)\in E$ if $x_{ij}<u_{ij}$ and $(j,i)\in E$ if $x_{ij}>0$. The cost of a reverse arc will be defined as $c_{ji}=-c_{ij}$. We will also refer to the \emph{residual capacities} of arcs; these are $u_{ij}-x_{ij}$ in the first case and $x_{ij}$ in the second. 

Let us observe that the augmenting directions correspond to directed cycles in the residual graph. Circuit augmentation algorithms for the primal and dual problems yield the rich classes of cycle cancelling and cut cancelling algorithms, see the survey \cite{Shigeno2000}.

The \emph{maximum flow problem} between a source $s$ and sink $t$ can be formulated as a special case as follows. We add a new arc $(t,s)$ with capacity $\infty$, set the demands $b\equiv 0$, and costs as $c_{ts}=-1$ and $c_{ij}=0$ otherwise. 
Bland's \cite{Bland76} observation was that the steepest-descent direction for this problem corresponds to finding a shortest residual $s$-$t$ path, as chosen in the Edmonds--Karp--Dinic algorithm. 

More generally, a steepest-descent direction amounts to finding a residual cycle $C\subseteq E_x$ that minimizes the mean cycle cost $c(C)/|C|$. Thus, the steepest descent algorithm for minimum-cost flows corresponds to the classical Goldberg--Tarjan algorithm \cite{Goldberg89} that is strongly polynomial with running  time $O(|V|\cdot |E|^2)$ \cite{Radzik-Goldberg}.

Let us now consider the other two variants. A Dantzig-descent direction in this context asks for the most negative cycle, i.e., a cycle maximizing $-c(C)$. A deepest-descent direction asks for a cycle $C$ of arcs that maximizes $-\alpha c(C)$, where $\alpha$ is the residual capacity of $C$. Computing both these directions exactly is NP-complete, since they generalize the  Hamiltonian-cycle problem: for every  directed graph, we can set up a flow problem where $E_x$ coincides with the input graph, all residual capacities are equal to 1, and all costs are $-1$. We note that De Loera, Kafer, and Sanit\`a~\cite{DKS19} showed that computing the Dantzig- and deepest-descent directions is also NP-hard for the fractional matching polytope.

Nevertheless, the deepest-descent direction can be suitably approximated.
Wallacher \cite{Wallacher} proposed selecting a \emph{minimum ratio cycle} in the residual graph. This is a cycle in $E_x$ that minimizes $c(C)/d(C)$, where $d_e=1/u_e$ for every residual arc $e\in E_x$; such a cycle can be found in strongly polynomial time. It is easy to show that this cycle approximates the deepest descent direction within a factor $|E_x|$.
Wallacher's  algorithm can be naturally extended to  linear programming \cite{mccormick-shioura-not-strongly}, and has found several combinatorial applications, e.g. \cite{Wallacher1999,Wayne02}, and has also been used in the context of integer programming \cite{Schulz1999}. We discuss an improved new variant in Section~\ref{sec:log-kappa}.
A different relaxation of the deepest-descent algorithm was given by Barahona and Tardos \cite{Barahona1989}, based on Weintraub's algorithm \cite{Weintraub1974}.
