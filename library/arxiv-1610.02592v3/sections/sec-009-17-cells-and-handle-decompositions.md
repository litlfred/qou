---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-009-17-cells-and-handle-decompositions
section_title: "Cells and handle decompositions"
section_number: 1.7
pages: 45-53
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.959
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
Many nice topological spaces can be constructed iteratively starting from finitely many points and then attaching some discs of increasing dimension called \emph{cells}. When the topological space is a differentiable manifold one typically thickens the cells to \emph{handles}. 

Cells and handles are beautifully introduced by Hatcher \cite{HAT} and Kosinksi \cite{K}, respectively.


\subsection{Cell complexes}
A \emph{finite cell complex} of dimension $n$ (briefly, a $n$-complex) is a topological space obtained iteratively in the following manner:
\begin{itemize}
\item a $0$-complex $X^0$ is a finite set of points, 
\item a $n$-complex $X^n$ is obtained from a $(n-1)$-complex $X^{n-1}$ by attaching finitely many \emph{$n$-cells}, that is copies of $D^n$ glued along continuous maps $\varphi\colon \partial D^n \to X^{n-1}$.
\end{itemize}
The closed subset $X^k\subset X^n$ is the \emph{$k$-skeleton} of $X^n$, for all $k<n$.  \index{cell complex}

\begin{prop}
Let $X$ be a $n$-complex. The inclusion map $X^k \hookrightarrow X$ induces an isomorphism $\pi_{j}(X^k) \to \pi_j(X)$ for all $j<k$.
\end{prop}
\begin{proof}
By transversality, maps $S^j\to X$ and homotopies between them can be homotoped away from cells of dimension $\geqslant j+2$. 
\end{proof}

In particular, the space $X$ is connected if and only if $X^1$ is, and its fundamental group is captured by $X^2$.

\begin{teo} Every differentiable compact $n$-manifold may be realised topologically as a finite $n$-complex.
\end{teo}

A presentation for the fundamental group of a cell complex $X$ can be constructed as follows.
If $x_0\in X^0$, we fix a maximal tree $T\subset X^1$ containing $x_0$ and equip the $k$ arcs in $X^1\setminus T$ with some arbitrary orientations. These arcs determine some generators $g_1,\ldots, g_k\in\pi_1(X,x_0)$. The boundary of a $2$-cell makes a circular path in $X^1$: every time it crosses an arc $g_i$ in some direction (entering from one side and exiting from the other) we write the corresponding letter $g_i^{\pm 1}$ and get a word. The $s$ two-cells produce $s$ word relations. We have constructed a presentation for $\pi_1(X)$.


\subsection{Euler characteristic}
The \emph{Euler characteristic} of a $n$-complex $X$ is the integer  \index{Euler characteristic}
$$\chi (X) = \sum_{i=0}^n (-1)^i C_i$$
where $C_i$ is the number of $i$-cells in $X$. It is also equal to 
$$\chi(X) = \sum_{i=0}^n (-1)^i b_i(X)$$
where $b_i(X)$ is the $i$-th Betti number of $X$. Therefore $\chi(X)$ is a number which depends only on the topology of $X$, that can be easily calculated from any cell decomposition of $X$.

\begin{prop} If $\tilde X \to X$ is a degree-$d$ covering of finite complexes then $\chi(\tilde X) = d\cdot \chi(X)$.
\end{prop}
\begin{proof}
A $k$-cell in $X$ is simply-connected and hence lifts to $d$ distinct $k$-cells in $\tilde X$. A cell decomposition of $X$ thus induces one of $\tilde X$ where the numbers $C_i$ are all multiplied by $d$.
\end{proof}

It is much harder to control homology under coverings. The Euler characteristic of a closed manifold measures the obstruction of constructing a nowhere-vanishing vector field.

\begin{teo} A closed differentiable manifold $M$ has a nowhere-vanishing vector field if and only if $\chi(M)=0$.
\end{teo}


\subsection{Aspherical cell-complexes}
A finite cell complex is locally contractible and hence has a universal cover $\tilde X$. If $\tilde X$ is contractible the complex  $X$ is called \emph{aspherical}. \index{cell complex!aspherical cell complex}

\begin{example}
If a closed manifold $M$ is covered by $\matR^n$, it is aspherical. 
\end{example}

By a theorem of Whitehead, a finite cell complex $X$ is aspherical if and only if all its higher homotopy groups $\pi_i(X)$ with $i\geqslant 2$ vanish.

The following theorem says that maps to aspherical spaces are determined (up to homotopy) by homomorphisms between fundamental groups.

\begin{teo} \label{complessi:omotopia:teo}
Let $(X,x_0), (Y,y_0)$ be pointed connected finite cellular complexes. If $Y$ is aspherical, every homomorphism $\pi_1(X,x_0) \to \pi_1(Y,y_0)$ is induced by a continuous map $(X,x_0)\to (Y,y_0)$, unique up to homotopy.
\end{teo}
\begin{proof}
We construct a continuous map $f\colon X^k \to Y^k$ iteratively on the $k$-skeleta, starting from $k=1$. 

Let $T$ be a maximal tree in $X^1$. The oriented 1-cells $g_1,\ldots, g_k$ in $X^1\setminus T$ define generators in $\pi_1(X,x_0)$. We define $f\colon X^1 \to Y^1$ by sending $T$ to $y_0$ and each $g_i$ to any loop in $Y$ representing the image of $g_i$ along the given homomorphism $\pi_1(X,x_0) \to \pi_1(Y,y_0)$.

The map $f$ sends the boundary of each 2-cell to a homotopically trivial loop in $Y$ and hence extends to a map $f\colon X^2 \to Y^2$. Since $Y$ is aspherical, the higher homotopy groups $\pi_i(Y)$ with $i\geqslant 2$ vanish and hence $f$ extends to a map $f\colon X^k \to Y^k$ iteratively for all $k\geqslant 3$.

We prove that $f$ is unique up to homotopy. Let $f'$ be a map that realises the given homomorphism on fundamental groups. We can construct a homotopy between $f$ and $f'$ iteratively on $X^k$ as follows. 

For $k=1$, we can suppose that both $f$ and $f'$ send $T$ to $y_0$. By hypothesis they send the generators $g_i$ to homotopic loops, hence we can homotope $f'$ to $f$ on $X^1$. For $k\geqslant 2$, the maps $f$ and $f'$ on each $k$-cell are homotopic because they glue to a map $S^k \to Y$, which is null-homotopic because $\pi_k(Y)$ is trivial.
\end{proof}

\begin{cor} \label{aspherical:cor}
Let $X$ and $Y$ be connected finite aspherical complexes. Every isomorphism $\pi_1(X) \to \pi_1(Y)$ is realised by a homotopic equivalence $X \to Y$, unique up to homotopy.
\end{cor}

In particular the homotopy type of an aspherical manifold is fully determined by its fundamental group.

\begin{cor}
Two aspherical closed manifolds of distinct dimension have non-isomorphic fundamental groups.
\end{cor}
\begin{proof}
Two closed manifolds of different dimension cannot be homotopically equivalent because they have non-isomorphic homology groups.
\end{proof}

We cite for completeness this result, although we will never use it. \index{Cartan--Hadamard theorem}

\begin{teo}[Cartan--Hadamard] A complete Riemannian manifold $M$ with sectional curvature everywhere $\leqslant 0$ has a universal covering diffeomorphic to $\matR^n$ and is hence aspherical.
\end{teo}
\begin{proof}[Sketch of the proof]
Pick a point $x\in M$. Since $M$ is complete, the exponential map $\exp_x\colon T_xM \to M$ is defined on $T_xM$. The fact that the sectional curvatures are $\leqslant 0$ imply that $(d\exp_x)_y$ is invertible for any $y\in T_x$ and $\exp_x$ is a covering.
\end{proof}

At a single point in this book we will need the following theorem.
\begin{teo} \label{no:torsion:aspherical:teo}
The fundamental group of an aspherical manifold $M$ has no torsion.
\end{teo}
\begin{proof}[Sketch of the proof]
Up to passing to a cover, it suffices to consider the case $\pi_1(M) \isom \matZ/_{n\matZ}$ for some $n\geqslant 2$. This case is excluded because the cohomology of $M$ is isomorphic to the (suitably defined) cohomology of $\matZ/_{n\matZ}$, which has however infinite dimension.
\end{proof}


\subsection{Gluing portion of boundaries}
Every compact differentiable $n$-manifold $M$ can be obtained topologically as a finite complex. The finite complex structure is however not designed to describe the smooth structure of $M$, and for that purpose it is better to replace $k$-cells with some thickened objects called \emph{$k$-handles}. These handles are $n$-discs glued iteratively along portions of their boundaries. Before describing them, we briefly explain how smooth manifolds can be glued along portions of their boundaries.

Let $M$ and $N$ be two $n$-manifolds with boundary and $X\subset \partial M$, $Y\subset \partial N$ be two compact $(n-1)$-submanifolds with boundary. A diffeomorphism $\varphi\colon X\to Y$ defines a topological space
$$M \cup_{\varphi} N$$
that may be promoted to a differentiable manifold: it suffices to use a collar as in Section \ref{cut:subsection}, see Figure \ref{boundary_glue:fig}.
The glued manifold depends (up to diffeomorphism) only on the isotopy class of $\varphi$.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{boundary_glue-BW}{boundary_glue}}
\nota{To glue two smooth manifolds along portions of their boundaries (left) we pick a collar for these portions (centre), then we remove $X,Y$ and identify the interiors of the collars (right).}
\label{boundary_glue:fig}
\end{center}
\end{figure}



\subsection{Handles} \label{handles:subsection}
Let $M$ be a (possibly empty or disconnected) $n$-manifold with boundary and $0\leqslant k \leqslant n$. A \emph{$k$-handle} is a manifold $D^k\times D^{n-k}$ attached to $M$ along some diffeomorphism $\varphi\colon \partial D^k \times D^{n-k}\to Y\subset \partial M$, hence producing a new manifold $M'$. 

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{handles-BW}{handles}}
\nota{Two 0-handles\iftoggle{BW}{}{ (yellow)}, two 1-handles\iftoggle{BW}{}{ (orange)}, and one 2-handle\iftoggle{BW}{}{ (red)} in dimension 2 (left). Two 0-handles\iftoggle{BW}{}{ (yellow)} and one 1-handle\iftoggle{BW}{}{ (orange)} in dimension 3 (right).}
\label{handles:fig}
\end{center}
\end{figure}

For instance, a $0$-handle is a $D^0 \times D^n = D^n$ attached to nothing, since $\partial D^0 = \varnothing$. This means that attaching a 0-handle to $M$ consists of adding a disjoint disc $D^n$ to it. For instance, by attaching a 0-handle to the empty set we create a disc $D^n$ out of nothing. 

A $1$-handle is a $D^1\times D^{n-1}$ attached along $\partial D^1 \times D^{n-1} = S^0 \times D^{n-1}$, that is two copies of $D^{n-1}$. Some examples in dimension $n=2,3$ are shown in Figure \ref{handles:fig}. A $2$-handle is a $D^2\times D^{n-2}$ attached along $\partial D^2 \times D^{n-2} = S^1\times D^{n-2}$. When $n=2$ this is a disc attached along its boundary, see Figure \ref{handles:fig}-(left).


\subsection{Handle decompositions}
A sequence of handle attachments \index{handle decomposition}
$$\emptyset \rightsquigarrow M_1 \rightsquigarrow \ldots \rightsquigarrow M_k = M$$
starting from the empty set and producing a compact manifold $M$ with (possibly empty) boundary is called a \emph{handle decomposition} for $M$. Using Morse theory one proves the following.

\begin{teo} Every compact manifold (possibly with boundary) can be obtained from a handle decomposition.
\end{teo}

\begin{example}
The disc $D^n$ has an obvious handle decomposition consisting of a single $0$-handle. It also has more complicate handle decompositions, as Figure \ref{handles:fig} shows.
\end{example}

By transversality, handles may always be reordered so that the lower index handles are attached first, and handles of the same index are attached simultaneously. So we can think of a decomposition as the appearing of some 0-handles, then the simultaneous attaching of some 1-handles, then of some 2-handles, and so on. 

A handle decomposition of a closed manifold may be turned upside down, by reversing all arrows and interpreting every $k$-handle as a $(n-k)$-handle. 

\begin{prop} \label{0:handle:prop}
Every compact connected manifold $M$ has a handle decomposition with one $0$-handle and at most one $n$-handle.
\end{prop}

If $M$ has a handle decomposition with $n_i$ handles of index $i$ then
$$\chi(M) = \sum_{i=0}^n (-1)^i n_i.$$


\subsection{Triangulations} \label{triangulations:subsection}
Instead of decomposing a manifold into handles, one may decide to decompose it into simplexes as in Figure \ref{Torus-triang:fig}. One such decomposition is called a triangulation: we now give a formal definition.

\begin{figure}
\begin{center}
\includegraphics[width = 7 cm] {Torus-triang.png}
\nota{A triangulated torus.}
\label{Torus-triang:fig}
\end{center}
\end{figure}

An (abstract and finite) \emph{simplicial complex} is a finite set $S$ of \emph{vertices} together with a set $X$ of subsets of $S$, called \emph{faces}, which contains all singletons and such that every subset of a face is also a face. A face of cardinality $k+1$ has \emph{dimension} $k$. \index{simplicial complex}

A simplicial complex $X$ has a topological realisation $|X|$, in which every face $F\in X$ of dimension $k$ transforms into a $k$-simplex with vertices in $F$ (we get a cell complex). The complex $X$ is \emph{purely $n$-dimensional} if every face is contained in a face of dimension $n$. This implies that $|X|$ is the union of its $n$-simplexes.

Let now $M$ be a differentiable $n$-manifold. A \emph{smooth $k$-simplex} in $M$ is a subset $\Delta \subset M$ diffeomorphic to a $k$-simplex in $\matR^n$ (we mean that there is a diffeomorphism between open neighbourhoods of $\Delta$ and of the simplex sending the first to the second). A \emph{smooth triangulation} of $M$ is a pure $n$-dimensional simplicial complex $X$ together with a homeomorphism between $|X|$ and $M$ that transforms every $k$-simplex in $X$ into a smooth $k$-simplex in $M$. \index{triangulation}

\begin{teo} Every compact manifold with (possibly empty) boundary has a smooth triangulation.
\end{teo}

Handle decompositions are often more flexible and efficient than triangulations, but triangulations have a more combinatorial nature and can for instance be handled by a computer. Both constructions are widely used.

On a simplicial complex $X$, the \emph{star} of a vertex $v$ is the set of all simplexes containing $v$ plus all their sub-simplexes; the \emph{link} of $v$ is the subset of the star consisting of the simplexes that do not contain $v$. Topologically, the star of $v$ is a closed neighbourhood of $v$ homeomorphic to a cone on its link.
\index{star of a vertex} \index{link of a vertex}


\subsection{Hypersurfaces and cohomology}
The techniques introduced in this chapter furnish another characterisation of the first cohomology group of a manifold. Let $[X,Y]$ denote the homotopy classes of continuous maps $X \to Y$.

\begin{prop}
Let $X$ be a cell complex. There is a canonical identification
$$H^1(X;\matZ) = [X,S^1].$$
\end{prop}
\begin{proof}
We know that $H^1(X;\matZ) = \Hom(\pi_1(X),\matZ)$.
The circle $S^1$ is aspherical with $\pi_1(S^1)=\matZ$, so by Theorem \ref{complessi:omotopia:teo} every homomorphism $\pi_1(X) \to \pi_1(S^1)$ is realised by a map $X\to S^1$, unique up to homotopy.
\end{proof}

We have noted that an oriented $k$-submanifold $S\subset M$ determines a class $[S]\in H_k(M,\matZ)$. It is natural to ask whether every homology class may be represented by an oriented submanifold: this is false in general, but it is true in codimension one.

\begin{prop} \label{homology:prop}
Let $M$ be a compact oriented $n$-manifold with (possibly empty) boundary. Every class in $H_{n-1}(M,\partial M;\matZ)$ is represented by an oriented properly embedded hypersurface $S\subset M$.
\end{prop}
\begin{proof}
We have
$$H_{n-1}(M,\partial M;\matZ) = H^1(M;\matZ) = \Hom (\pi_1(M), \matZ) = [M, S^1].$$
Every map $M\to S^1$ is homotopic to a smooth map, hence each class $\alpha \in H^1(M,\matZ)$ is represented by a smooth map $f\colon M\to S^1$. By Sard's lemma there is a regular value $x\in S^1$, whose counter-image $S = f^{-1}(x)$ is a hypersurface, transversely oriented by $f$ and hence oriented (since $M$ is).

To prove that $[S] = \alpha$ we verify that $[S]$ and $\alpha$ act on $\pi_1(M)$ in the same way. Pick a loop $\gamma \in \pi_1(M)$ transverse to $S$. The number $\alpha(\gamma)$ is the degree of $f\circ\gamma$, that is the number of times $f\circ \gamma$ crosses $x$ counted with signs, which equals the number of times $\gamma$ crosses $S$ counted with signs.
\end{proof}

\begin{prop}
An oriented connected properly embedded hypersurface $S\subset M$ is separating if and only if $[S]\in H_{n-1}(M,\partial M; \matZ)$ is trivial.
\end{prop}
\begin{proof}
The surface $S$ is separating if and only if $S \cdot \alpha = 0$ for every loop $\alpha$ transverse to $S$ (exercise). Since $\omega([S], [\alpha]) = S \cdot \alpha$ and $\omega$ is non-degenerate (see Section \ref{intersection:subsection}), this holds precisely when $[S]=0$.
\end{proof}


\subsection{Topological discs}
Finally, we mention a purely topological theorem that will be used only at one point in this book, in Chapter \ref{automorfismi:chapter}.

\begin{teo} \label{topological:disc:teo}
Let $M$ be a compact topological manifold, whose interior and boundary are homeomorphic respectively to $B^n$ and $S^{n-1}$. Then $M$ is homeomorphic to $D^n$.
\end{teo}
\begin{proof}
We use two important theorems on topological manifolds, whose proofs can be found in the first chapter of the book \emph{Topological embeddings} of Rushing \cite{Ru}.

As in every compact topological manifold, the boundary $\partial M$ has a topological collar by a theorem of Brown (see Theorem 1.7.4 in that book). The interior boundary sphere of the collar is contained in $\interior M \cong B^n$ and hence bounds a closed disc by the Generalised Sch\"onflies Theorem (see Theorem 1.8.2 there). The manifold $M$ is obtained by collaring a closed disc and is hence a closed disc.
\end{proof}



\chapter{Hyperbolic space} \label{spazio:chapter} \label{space:chapter}
In every dimension $n\geqslant 2$ there exists a unique simply connected complete Riemannian manifold with constant sectional curvature $1$, $0$, or $-1$. These are the sphere $S^n$, the Euclidean space $\matR^n$, and the hyperbolic space $\matH^n$. 

These manifolds are the three most important spaces in Riemannian geometry. We introduce in this chapter the least familiar and the most interesting of the three: hyperbolic space.
