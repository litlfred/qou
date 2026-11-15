---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-002-21-the-path-2-groupoid-of-a-smooth-manifold
section_title: "The Path 2-Groupoid of a Smooth Manifold"
section_number: 2.1
pages: 6-7
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec:path2groupoid}

The basic idea of the path 2-groupoid is very simple: for a smooth manifold $X$, it is a strict 2-category whose objects are the points of $X$, whose 1-morphisms are smooth  paths in~$X$, and whose 2-morphisms are smooth homotopies between these paths. We recall some definitions from \cite{schreiber3,schreiber5}.

For points $x,y\in X$, a \emph{path} $\gamma:x \to y$ is a smooth map $\gamma:[0,1] \to X$ with $\gamma(0)=x$ and $\gamma(1)=y$. Since the composition $\gamma_2 \circ \gamma_1$ of two  paths $\gamma_1:x \to y$ and $\gamma_2:y \to z$  should again be a smooth map we require sitting instants for all paths: a number $0 < \varepsilon <\frac{1}{2}$ with
$\gamma(t)=\gamma(0)$ for $0 \leq t < \varepsilon$ and $\gamma(t)=\gamma(1)$ for $1-\varepsilon
< t \leq 1$. The set of these paths is denoted by $PX$. In order to make the composition associative and to make paths invertible, we  consider the following equivalence relation on $PX$: two paths $\gamma,\gamma':x \to y$ are called \emph{thin homotopy equi\-va\-lent}
if there exists a smooth map
$h:[0,1]^2 \to X$ 
such that 
\begin{enumerate}
\item[(1)]
$h$ is a homotopy from $\gamma$ to $\gamma'$ through paths $x \to y$ and has sitting instants at $\gamma$ and $\gamma'$.

\item[(2)]
the differential of $h$ has at most rank 1. 
\end{enumerate}
The set of equivalence classes is denoted by $P^1X$.
We remark that any path $\gamma$ is thin homotopy equivalent to any orientation-preserving reparameterization of $\gamma$.
The composition of paths induces a well-defined associative composition on $P^1X$ for which the constant paths $\id_x$ are identities and the reversed paths $\gamma^{-1}$ are inverses; see \cite[Section 2.1]{schreiber3} for more details.



A homotopy $h$ between two paths $\gamma_0$ and $\gamma_1$ like above but without condition (2) on the rank of its differential is called a \emph{bigon} in $X$ and denoted by $\Sigma: \gamma_0 \Rightarrow \gamma_1$. These bigons  form the 2-morphisms of the path 2-groupoid of $X$.
We denote the set
of  bigons in $X$ by $BX$. Bigons can be composed in two natural ways. For two bigons $\Sigma:\gamma_1
\Rightarrow \gamma_2$ and $\Sigma':\gamma_2 \Rightarrow \gamma_3$ 
we have a \emph{vertical composition} 
\begin{equation*}
\Sigma'\bullet\Sigma: \gamma_1 \Rightarrow \gamma_3\text{.}
\end{equation*}
If two bigons $\Sigma_1: \gamma_1 \Rightarrow \gamma_1'$ and $\Sigma_2:\gamma_2 \Rightarrow \gamma_2'$ are such  that $\gamma_1(1)=\gamma_2(0)$, we have a \emph{horizontal composition }
\begin{equation*}
\Sigma_2 \circ \Sigma_1: \gamma_2 \circ \gamma_1 \Rightarrow \gamma_2' \circ \gamma_1'\text{.}
\end{equation*}
Like in the case of paths, we  consider an equivalence relation on $BX$ in order to make the two compositions associative and to make bigons invertible:
two bigons $\Sigma:\gamma_0 \Rightarrow \gamma_1$ and $\Sigma':\gamma'_0 \Rightarrow \gamma'_1$
are called \emph{thin ho\-mo\-to\-py equivalent} if there exists a smooth
map $h: [0,1]^{3} \to X$ such that
\begin{enumerate}
\item[(1)] 
$h$ is a homotopy from $\Sigma$ to $\Sigma'$ through bigons and has sitting instants at $\Sigma$ and $\Sigma'$.

\item[(2)]
the induced  homotopies $\gamma_0 \Rightarrow \gamma_0'$ and $\gamma_1\Rightarrow \gamma_1'$ are thin.

\item[(3)]
the differential of $h$ has at most rank 2.
\end{enumerate}
Condition (1) assures that we have defined an equivalence
relation on $BX$, and  condition (2) asserts that two thin homotopy equivalent bigons $\Sigma:\gamma_0 \Rightarrow \gamma_1$ and $\Sigma'\maps\gamma_0' \Rightarrow \gamma_1'$ start and end on thin homotopy equivalent paths
$\gamma_0 \sim \gamma_0'$ and $\gamma_1 \sim \gamma_1'$. We denote the set of equivalence classes by $B^2X$.
The two compositions $\circ$ and $\bullet$ between bigons  induce a well-defined composition on $B^2X$. The \emph{path 2-groupoid $\mathcal{P}_2(X)$} is  the 2-category whose set of objects is $X$, whose set of 1-morphisms is $P^1X$ and whose set of 2-morphisms is $B^2X$. The path 2-groupoid is strict and all 1-morphisms are strictly invertible. We refer the reader to \cite[Section 2.1]{schreiber5} for a detailed discussion.


In this article we describe connections on gerbes by transport 2-functors --  certain (not necessarily strict) 2-functors
\begin{equation*}
F: \mathcal{P}_2(X) \to T\text{,}
\end{equation*}
for some 2-category $T$,  the \emph{target 2-category}. 
We note that 2-functors can be pulled back along smooth maps $f:M \to X$: such a map induces  a strict 2-functor $f_{*}\maps\mathcal{P}_2(M) \to \mathcal{P}_2(X)$, and we write
\begin{equation*}
f^{*}F := F \circ f_{*}\text{.}
\end{equation*}

If we drop condition (3) from the definition of thin homotopy equivalence between bigons we would still get a strict 2-groupoid, which we denote by $\Pi_2(X)$ and  which we call the \emph{fundamental 2-groupoid} of $X$. The projection defines a strict 2-functor $\mathcal{P}_2(X) \to \Pi_2(X)$. We say that a 2-functor $F\maps\mathcal{P}_2(M) \to T$ is \emph{flat} if it factors through the 2-functor $\mathcal{P}_2(M) \to \Pi_2(M)$. We  show in Section  \ref{sec5_1} that this abstract notion of flatness is equivalent to the vanishing of a certain curvature 3-form.
