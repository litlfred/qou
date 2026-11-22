---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-020-82-circuit-augmentation-algorithms
section_title: "Circuit augmentation algorithms"
section_number: 8.2
pages: 29-30
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.9
latex_coverage_ratio: 0.983
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
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
