---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-001-1-polyhedra-and-piecewise-smooth-geometry
section_title: "Polyhedra and Piecewise Smooth Geometry"
section_number: 1
pages: 13-25
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.975
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec:pws}
\numberwithin{equation}{subsection}


\subsection{Conventions}
In this paper we work over the field $\mbb{R}$ of
real numbers. We denote by $\mbf{A}^{n} = \mbf{A}^{n}(\R)$
the real $n$-dimensional affine
space, with the usual smooth (i.e.\ $\mrm{C}^{\infty}$
differentiable) manifold structure, and the standard euclidean metric. 
The symbol $\otimes$ stands for $\otimes_{\R}$.
The coordinate functions on
$\mbf{A}^{n}$ are $t_1, \ldots, t_n$.


\subsection{Embedded Polyhedra} \label{subsec:embpoly}
By linear map $f : \mbf{A}^{m} \to \mbf{A}^{n}$ we mean the composition of a
linear homomorphism and a translation. Thus the group of invertible linear
maps of $\mbf{A}^{n}$ is $\mrm{GL}_n(\R) \ltimes \R^{n}$. 
By linear subset $X$ of $\mbf{A}^{n}$ we mean the zero locus of some set of
linear functions (not necessarily homogeneous). In other words $X$ is the
image of some injective linear map
$f : \mbf{A}^{m} \to \mbf{A}^{n}$; and then we let $m$ be the dimension of $X$. 

Given a set $S \subset \mbf{A}^{n}$, its linear (resp.\ convex) hull is the 
smallest linear (resp.\ convex) subset of $\mbf{A}^{n}$ containing $S$.
In case $S$ is finite, say $S = \{ x_1, \ldots, x_m \}$, then a point $x$ is in
the linear (resp.\ convex) hull of $S$ if and only if 
$x = \sum_{i = 1}^m a_i x_i$ for some real numbers $a_1, \ldots, a_m$
satisfying $\sum a_i = 1$ (resp.\ and $a_i \geq 0$). 

By {\em embedded polyhedron} \index{Embedded polyhedron} 
we always mean a convex bounded finite polyhedron
in $\mbf{A}^n$, for some $n$. Namely a polyhedron $X$ in $\mbf{A}^n$ is the
convex hull of a finite subset of $\mbf{A}^n$.
A point $x \in X$ is called a {\em vertex} if it is not in the convex hull of
any finite subset of $X - \{ x \}$. 
If we denote by $S$ the set  of vertices of $X$, then $S$ is finite, and
$X$ is the convex hull of $S$. 
The dimension $\opn{dim} X$ is the dimension of the linear hull of
$X$, and we call $\mbf{A}^n$ the {\em ambient linear space} of $X$.
The standard euclidean metric on $\mbf{A}^{n}$ restricts to a global metric (a
distance function) $\opn{dist}_X$ on $X$.
We denote by $\opn{diam}(X)$ the diameter of $X$, namely the maximal distance
between any two points.
The linear functions on $\mbf{A}^{n}$ (spanned by $t_1, \ldots, t_n$) restrict
to functions $X \to \R$, that we also call linear functions. The $\R$-module 
$\mcal{O}_{\mrm{lin}}(X)$ of linear functions has rank equal to 
$m := \opn{dim} X$. An $\R$-basis $\{ s_i \}_{i = 1, \ldots, m}$
of $\mcal{O}_{\mrm{lin}}(X)$ is called a {\em linear
coordinate system} on $X$. 

We shall mostly encounter two kinds of embedded polyhedra. The first is the 
{\em $n$-dimensional cube} $\mbf{I}^n$. This is the subset of
$\mbf{A}^n$ defined by the inequalities
$0 \leq t_1, \ldots, t_n \leq 1$. 
As a convex set it is spanned by its $2^n$ vertices.
See Figure \ref{fig:75} for an illustration. 

\begin{figure}
\includegraphics[scale=0.25]{fig75.jpg}
\caption{The polyhedra $\bsym{\Delta}^1 \cong \mbf{I}^1$,
$\bsym{\Delta}^2$ and $\mbf{I}^2$, with their vertices and orientations.} 
\label{fig:75}
\end{figure}

The second kind of embedded polyhedron is the {\em $n$-dimensional simplex}
$\bsym{\Delta}^n$, embedded in $\mbf{A}^{n+1}$. We use 
barycentric coordinates $t_0, t_1 \ldots, t_n$ on $\mbf{A}^{n+1}$
when dealing with the simplex. In these coordinates
$\bsym{\Delta}^n$ is the subset of $\mbf{A}^{n+1}$ defined by the
conditions
$0 \leq t_0, \ldots, t_n$ and $\sum_{i=0}^n t_i = 1$.
As a convex set it is spanned by its $n+1$ vertices.

Suppose $X$ and $Y$ are both embedded polyhedra. A {\em linear map} 
$f : X \to Y$ is a function that extends to a linear map between the ambient
linear spaces. Such a map $f$ is determined by its value on a sequence
$(v_0, \ldots, v_n)$ of linearly independent vertices of $X$, 
where $n := \opn{dim} X$. Thus we shall often describe the linear map $f$ as 
\[ f(v_0, \ldots, v_n) = (w_0, \ldots, w_n) , \]
or just $f = (w_0, \ldots, w_n)$, where $w_i := f(v_i)$.

In case $X$ is the cube $\mbf{I}^n$, embedded in
$\mbf{A}^{n}$, we shall look at the following linearly independent vertices: 
$v_0$ is the origin $(0, \ldots, 0)$, and for $i = 1, \ldots, n$ we
take
\begin{equation} \label{eqn:1}
v_i := (0, \ldots, 1, \ldots, 0) ,
\end{equation}
with $1$ in the $i$-th position. In case of the simplex $\bsym{\Delta}^n$,
embedded in $\mbf{A}^{n+1}$ with barycentric coordinates, we look at all its
vertices, and use the notation \lb $(v_0, \ldots, v_n)$, where $v_i$ is as in
equation (\ref{eqn:1}).


\subsection{Smooth Maps and Forms}
The algebra of smooth real functions on
$\mbf{A}^n$ is denoted by $\mcal{O}(\mbf{A}^n)$.
The de Rham DG (differential graded) algebra of smooth differential forms on
$\mbf{A}^n$ is
\[ \Omega(\mbf{A}^n) = \bigoplus_{p = 0}^n \
\Omega^p(\mbf{A}^n) , \]
with differential $\d$ and wedge product $\wedge$.

Let $X$ be an $m$-dimensional polyhedron embedded in $\mbf{A}^n$. The set $X$ is
a compact topological space, its interior $\opn{Int} (X)$ is an $m$-dimensional
manifold, and the boundary $\partial X$ is a finite union of
$(m-1)$-dimensional polyhedra. But $X$ also has a differentiable structure.

\begin{dfn} \label{dfn:500}
Let $X \subset \mbf{A}^n$ be an embedded polyhedron, and let $U \subset X$ be
an open set.
\begin{enumerate}
\item A function $f : U \to \R$ is said to be {\em smooth} if 
it extends to a smooth function $\til{f} : \til{U} \to \R$
on some open neighborhood $\til{U}$ of $U$ in $\mbf{A}^n$.

\item A map $f : U \to \mbf{A}^p$ is called smooth if the functions 
$t_i \circ f : U \to \R$ are  smooth for all $i \in \{ 1, \ldots, p \}$.

\item Suppose $Y \subset \mbf{A}^p$ is an embedded polyhedron, and 
$V \subset Y$ is an open set. A map $f : U \to V$ is called smooth if the
composed map $f : U \to \mbf{A}^p$ is smooth. 

\item Let $V$ be an open subset of an embedded polyhedron. A map $f : U \to V$
is called a {\em diffeomorphism} of it is bijective, and both $f$ and $f^{-1}$
are smooth.
\end{enumerate}
\end{dfn}

We denote by $\mcal{O}(U)$ the $\R$-algebra of all smooth functions 
$U \to \R$.
A smooth map $f : U \to V$ between open subsets of embedded polyhedra induces an
$\R$-algebra homomorphism $f^* : \mcal{O}(V) \to \mcal{O}(U)$, namely pullback. 

Suppose $X$ is an embedded polyhedron and $U \subset X$ is an open set. 
We let $\opn{Int}(U) := U \cap \opn{Int}(X)$ and 
$\partial(U) := U \cap \partial(X)$. Note that $\opn{Int}(U)$ is a
manifold, and it is dense in $U$.

\begin{dfn}  \label{dfn:501}
Let $X \subset \mbf{A}^n$ be an embedded polyhedron,
and let $U \subset X$ be an open set.
A {\em smooth differential $p$-form} on $U$ is a differential form
$\alpha \in \Omega^p(\opn{Int} (U))$, that extends to a form
$\til{\alpha} \in \Omega^p(\til{U})$ on some open neighborhood $\til{U}$ of $U$
in $\mbf{A}^n$. 
\end{dfn}

We denote by $\Omega^p(U)$ the set of differential $p$-forms on
$U$, and we let 
\[ \Omega(U) := \bigoplus_{p \geq 0} \ \Omega^p(U) . \]
This is a DG subalgebra of $\Omega(\opn{Int}(U))$. 

Suppose $U$ and $V$ are open subsets of  embedded polyhedra. 
A smooth map $f : U \to V$  induces a DG algebra homomorphism 
$f^* : \Omega(V) \to \Omega(U)$.
If $f$ is an inclusion then we
usually write $\alpha|_U := f^*(\alpha)$ for $\alpha \in \Omega(V)$. 

Let $X$ be an $m$-dimensional embedded polyhedron, and $U \subset X$ a nonempty
open set. Then $\Omega^p(U)$ is a free $\mcal{O}(U)$-module of rank
$\binom{m}{p}$. Indeed, if we choose a linear coordinate system 
$\{ s_i \}_{i = 1, \ldots, m}$ on $X$, then the family
\begin{equation} \label{eqn:2}
\{ \d s_{i_1} \wedge \cdots \wedge \d s_{i_p} \}_{1 \leq i_1 < \cdots < i_p
\leq m}
\end{equation}
is a basis for $\Omega^p(U)$ as $\mcal{O}(U)$-module.

\begin{dfn} \label{dfn:27}
Let $\bsym{s} =  \{ s_i \}_{i = 1, \ldots, m}$ be a linear coordinate system
on the $m$-dimensional polyhedron $X$. Given a form 
$\alpha \in \Omega^p(X)$, it has a unique expansion as a sum
\[ \alpha = \sum_{\bsym{i}} \, 
\til{\alpha}_{\bsym{i}} \cdot \d s_{i_1} \wedge \cdots \wedge \d s_{i_p} , \]
where 
$\bsym{i} = (i_1, \ldots, i_p)$ runs over the set of strictly increasing
multi-indices in the range $\{ 1, \ldots, m \}$,  and 
$\til{\alpha}_{\bsym{i}} \in \mcal{O}(X)$.
The functions $\til{\alpha}_{\bsym{i}}$ are called the {\em coefficients}
of $\alpha$ with respect to the linear coordinate system 
$\bsym{s}$.
\end{dfn}

Let us denote by $\Omega_{\mrm{const}}(\mbf{A}^{n})$ the $\R$-subalgebra of
$\Omega(\mbf{A}^{n})$
generated by the elements $\d t_1, \ldots, \d t_n$. 
Now suppose $X$ is an $m$-dimensional polyhedron in $\mbf{A}^{n}$.
The image of
$\Omega_{\mrm{const}}(\mbf{A}^{n})$ under the canonical surjection
$\Omega(\mbf{A}^{n})\to \Omega(X)$
is denoted by $\Omega_{\mrm{const}}(X)$, and its elements are called
{\em constant differential forms}. There is an isomorphism of graded algebras
\[ \Omega(X) \cong \mcal{O}(X) \otimes \Omega_{\mrm{const}}(X) . \]
If we choose a linear coordinate system 
$\bsym{s} = \{ s_i \}_{i = 1, \ldots, m}$ on $X$, then (\ref{eqn:2}) is an
$\R$-basis for $\Omega^p_{\mrm{const}}(X)$.

\begin{dfn} \label{dfn:26}
Given a smooth form $\alpha \in \Omega^p(X)$ and a point 
$x \in X$, we define the {\em constant form} associated to $\alpha$ at $x$ to be
\[ \alpha(x) := \sum_{\bsym{i}} \, 
\til{\alpha}_{\bsym{i}}(x) \cdot \d s_{i_1} \wedge \cdots \wedge \d s_{i_p}
\in \Omega^p_{\mrm{const}}(X) , \]
where the functions $\til{\alpha}_{\bsym{i}}$ are the coefficients of $\alpha$
relative to some  linear coordinate system 
$\bsym{s} = \{ s_i \}$, as in 
Definition \ref{dfn:27}. 
\end{dfn}

Note that $\alpha(x)$ is independent of the linear coordinate system.

Let $f : X \to Y$ be a linear map between embedded polyhedra. If $g$ is a linear
function on $Y$, then 
$f^*(g) = g \circ f$ is a linear function on $X$; and if 
$\alpha \in \Omega_{\mrm{const}}(Y)$, then 
$f^*(\alpha) \in \Omega_{\mrm{const}}(X)$.


\subsection{Manifolds with Sharp Corners} \label{subsec:mfld-corners}
Manifolds with corners are modeled on 
$\R_{\geq 0}^n$; cf.\ \cite {Le} or \cite{Jo}. 
However not all polyhedra are manifolds with corners; so we introduce a variant
in which the local model is an embedded polyhedron.
See Remark \ref{rem:506} below. 

\begin{dfn} \label{dfn:510}
Let $X$ be a topological space. 
\begin{enumerate}
\item A {\em smooth chart with sharp corners} on $X$
is a pair $(U, \phi)$, where $U$ is an open subset of an embedded polyhedron,
and $\phi : U \to X$ is a map such that $\phi(U)$ is open in $X$ and 
$\phi : U \to \phi(U)$ is a homeomorphism. 

\item Two smooth charts with sharp corners $(U_1, \phi_1)$ and $(U_2, \phi_2)$
are compatible if 
\[ \phi_2^{-1} \circ \phi_1 : \phi_1^{-1} 
\bigl( \phi_1(U_1) \cap \phi_2(U_2) \bigr) \to 
\phi_2^{-1} \bigl( \phi_1(U_1) \cap \phi_2(U_2) \bigr) \]
is a diffeomorphism.

\item A {\em smooth atlas with sharp corners} on $X$ is a collection 
$\{ (U_i, \phi_i) \}$ of compatible charts with sharp corners, such that 
$X = \bigcup_i \phi_i(U_i)$.
\end{enumerate}
\end{dfn}

\begin{dfn} \label{dfn:505}
A {\em smooth manifold with sharp corners}
\index{Smooth manifold with sharp corners}
is a  Hausdorff second countable
topological space $X$ endowed with a smooth atlas with sharp corners
$\{ (U_i, \phi_i) \}$.
\end{dfn}

\begin{dfn} \label{dfn:506}
Let $X$ and $Y$ be smooth manifolds with sharp corners,
with atlases  $\{ (U_i, \phi_i) \}$ and $\{ (V_j, \psi_j) \}$ respectively. A
map $f : X \to Y$ is called {\em smooth} if for every $i,j$ the map 
\[ \psi_j^{-1} \circ f \circ \phi_i : 
(f \circ \phi_i)^{-1} (\psi_j(V_j)) \to V_j \]
is smooth. 
\end{dfn}

\begin{rem} \label{rem:506}
If we were to restrict the class of polyhedra in Definition \ref{dfn:505} to
cubes (or simplices), then we would recover the usual definition of manifold
with corners.  ``Sharp corners'' occur when too many faces of a polyhedron meet
at a vertex (to
be precise, more than the dimension of the manifold; e.g.\ at the top vertex of
a pyramid with square base). 

There are several notions of smooth maps between manifolds with corners in the
literature. Suppose $X$ and $Y$ are smooth manifolds with corners, and 
$f : X \to Y$ is a smooth map in the sense of Definition
\ref{dfn:506}. Then $f$ is called ``weakly smooth'' in \cite{Jo}. In order for
$f$ to be smooth according to \cite{Jo} it must satisfy a condition involving
the boundary strata of $X$ and $Y$; such a condition can't even be stated
when sharp corners are present.
\end{rem}

\begin{prop} \label{prop:500}
The category of smooth manifolds with sharp corners contains the following
categories as full subcategories:
\begin{enumerate}
\item The category of smooth manifolds (without boundary) and smooth maps
between them.
\item The category of embedded polyhedra and smooth maps
between them (Definition \tup{\ref{dfn:500}(3)}).
\end{enumerate}
\end{prop}

We leave out the easy proof. 

A function $f : X \to \R$ is called smooth if when viewed as a map 
$f : X \to \mbf{A}^1$ it is smooth. We denote by $\mcal{O}(X)$ the $\R$-algebra
of smooth functions.

If $U$ is an open subset of a smooth manifold with sharp corners $X$, then $U$
inherits a structure of smooth manifold with sharp corners.

A smooth manifold with sharp corners $X$  has an intrinsic
decomposition $X = \partial X \coprod \opn{Int} (X)$, where the interior
$\opn{Int} (X)$ is a manifold without boundary, and the
boundary $\partial X$ is a manifold with sharp corners.
The condition for a
point $x \in X$ to belong to $\opn{Int} (X)$ is that it has an open
neighborhood that's isomorphic, as manifold with sharp corners, to a manifold
without boundary.

We say that a manifold with sharp corners $X$ has dimension $n$ if 
the manifold $\opn{Int} (X)$ has dimension $n$. (Of course every connected
component of $X$ has a dimension.)  In this case $\partial X$ has dimension
$n-1$.

Let $X$ be a smooth manifold with sharp corners with atlas 
$\{ (U_i, \phi_i) \}$. For every $i$ we have a diffeomorphism
$\phi_i : \opn{Int}(U_i) \to  \opn{Int}(\phi_i(U_i))$
between manifolds without boundaries, and
$\opn{Int}(\phi_i(U_i)) = \phi_i(U_i) \cap \opn{Int} (X)$.
The module of smooth differentials $\Omega^p(U_i)$ was introduced in Definition 
\ref{dfn:501}.

\begin{dfn}  \label{dfn:511}
Let $X$ be a smooth manifold with sharp corners with atlas 
$\{ (U_i, \phi_i) \}$.
A {\em smooth differential $p$-form} on $X$ is a differential form
$\alpha \in \Omega^p(\opn{Int} (X))$, such that for every $i$ 
the form 
\[ \phi_i^* (\alpha|_{\opn{Int}(\phi_i(U_i))}) \in \Omega^p(\opn{Int}(U_i)) \]
extends to a form $\til{\alpha}_i \in \Omega^p(U_i)$.
\end{dfn}

We denote by $\Omega^p(X)$ the set of differential $p$-forms on
$X$, and we let 
\[ \Omega(X) := \bigoplus_{p \geq 0} \ \Omega^p(X) . \]
This is a DG subalgebra of $\Omega(\opn{Int}(X))$. 
Of course $\Omega^0(X) = \mcal{O}(X)$.

A smooth map $f : X \to Y$ between manifolds with sharp corners induces a DG
algebra homomorphism 
$f^* : \Omega(Y) \to \Omega(X)$.

\begin{conv} \label{conv:500}
For the rest of the paper, by ``manifold'' we always mean a smooth manifold
with sharp corners, as defined in Definition \ref{dfn:505}. 
Smooth maps between manifolds are in the sense of  Definition \ref{dfn:506}. 
\end{conv}


\subsection{Abstract Polyhedra} \label{subsec:abspoly}
It turns out that the geometric structure of a polyhedron is easy to
encode, and it is nicer to work
with polyhedra that are not embedded. 

By a {\em global metric} on a topological space $Z$ we mean a distance function 
$\opn{dist}_Z : Z^2 \to \R_{\geq 0}$ that induces the topology of $Z$. 
Recall that if $Z$ is an embedded polyhedron in $\mbf{A}^m$, then $Z$ inherits
a global metric from the ambient affine space, and also an $\R$-module 
of linear functions 
$\mcal{O}_{\mrm{lin}}(Z) \subset \mcal{O}(Z)$. 

\begin{dfn} \label{dfn:503}
A {\em polyhedron} \index{Polyhedron}
 is a smooth manifold with sharp corners
$X$, together with a global metric $\opn{dist}_X$ and an $\R$-submodule
$\mcal{O}_{\mrm{lin}}(X) \subset \mcal{O}(X)$.
The condition is that there exists an isomorphism 
of smooth manifolds with sharp corners
$f : X \iso Z$ for some embedded
polyhedron $Z \subset \mbf{A}^{m}$, with these two properties:
\begin{enumerate}
\rmitem{i} $f$ is an isometry; i.e.\ 
$f : (X, \opn{dist}_X) \to (Z, \opn{dist}_Z)$ is an isomorphism of metric
spaces.

\rmitem{ii} The $\R$-algebra isomorphism
$f^* : \mcal{O}(Z) \to \mcal{O}(X)$
satisfies \lb
$f^*(\mcal{O}_{\mrm{lin}}(Z)) = \mcal{O}_{\mrm{lin}}(X)$.
\end{enumerate}
The composed map $f : X \to \mbf{A}^{m}$ is called a {\em
linear metric embedding}.
If only property (ii) holds, then $f : X \to \mbf{A}^{m}$ is called a {\em
a linear embedding}.
\end{dfn}

In terms of this definition, an embedded polyhedron is a polyhedron $X$ \lb
equipped with a particular linear metric embedding $f : X \to \mbf{A}^{m}$.

\begin{dfn} \label{dfn:512}
Let $X$ and $Y$ be polyhedra, and let $f : X \to Y$ be a map. 
\begin{enumerate}
\item We say $f$ is {\em smooth} if it is a smooth map of smooth manifolds with
sharp corners (see Definition \ref{dfn:506}).

\item We say $f$ is {\em linear} if 
$f^*(\mcal{O}_{\mrm{lin}}(Y)) \subset \mcal{O}_{\mrm{lin}}(X)$.
\end{enumerate}
\end{dfn}

By {\em linear coordinate system} on $X$ we mean an $\R$-basis of
$\mcal{O}_{\mrm{lin}}(X)$.

\begin{prop} \label{prop:511}
Let $X$ be a polyhedron, and let $\bsym{s} = \{ s_i \}_{i = 1, \ldots, n}$
be linear coordinate system on $X$. Consider
the induced smooth map  $f : X \to \mbf{A}^{n}$.
Then the image $Z := f(X)$ is an $n$-dimensional embedded polyhedron in
$\mbf{A}^{n}$, $f : X \to Z$ is an isomorphism of 
smooth manifolds with sharp corners, and 
$f^*(\mcal{O}_{\mrm{lin}}(Z)) = \mcal{O}_{\mrm{lin}}(X)$.
I.e.\ the map $f : X \to \mbf{A}^{n}$ is a linear embedding. 
\end{prop}

The proof is left as an exercise. 

Suppose we are given linear embeddings $X \to \mbf{A}^{m}$ and 
$Y \to \mbf{A}^{n}$. It is easy to see that a map $f : X \to Y$ is linear in
the sense of Definition \ref{dfn:512} if and only if $f$ extends to a linear
map $\mbf{A}^{m} \to \mbf{A}^{n}$. 

Note that we said nothing about the metrics in Proposition \ref{prop:511}.

\begin{dfn}
An {\em orthonormal linear coordinate system} on $X$ is a linear coordinate
system $\bsym{s}$ such that the induced map 
$f : X \to \mbf{A}^{n}$ is a linear metric embedding.
\end{dfn}

Let $\bsym{s}$ be an orthonormal linear coordinate system on $X$.
Then for any $x, y \in X$ the distance between them is
\[ \opn{dist}_X(x, y) = \Bigl( \bosum_{i = 1}^n \bigl( s_i(x) - s_i(y) \bigr)^2
\Bigr)^{1/2} . \]

We can view our polyhedra as ``Riemannian manifolds'', in the
following sense. First note that we can talk about the DG algebra 
$\Omega_{\mrm{const}}(X)$ of constant forms: it is the DG algebra generated
over $\R$ by the family of forms $\{ \d s_i \}_{i = 1, \ldots, n}$, where 
$\bsym{s} = \{ s_i \}_{i = 1, \ldots, n}$ is a linear coordinate system.
If moreover $\bsym{s}$ is an orthonormal linear coordinate system, then
consider the constant symmetric $2$-form
\[ \omega_X := \sum_{i = 1}^n \, \d s_i \otimes \d s_i \in 
\Omega^1_{\mrm{const}}(X) \otimes_{\R} \Omega^1_{\mrm{const}}(X) \subset 
\Omega^1(X) \otimes_{\mcal{O}(X)} \Omega^1(X) . \]
The form $\omega_X$ is independent of the orthonormal linear coordinate system.
It encodes the global metric (the distance function $\opn{dist}_X$) in the
obvious way. 

Suppose $f : X \to Y$ is a linear map between polyhedra. Then
\[ f^*(\omega_Y) \in 
\Omega^1_{\mrm{const}}(X) \otimes_{\R} \Omega^1_{\mrm{const}}(X) . \]
The map $f$ is conformal if and only if
$f^*(\omega_Y) = a \omega_X$
for some positive real number $a$, which we call the scaling factor.
And $f$ is a linear metric embedding if and only if $a = 1$.

Let $X$ be a polyhedron. The linear functions on $X$, i.e.\ the elements of 
$\mcal{O}_{\mrm{lin}}(X)$, allow us to construct the convex hull of any
subset $S \subset X$ (cf.\ Proposition \ref{prop:511}). A sub-polyhedron $Z$ of
$X$ is by definition the convex
hull of a finite subset of $X$. $Z$ inherits from $X$ (by restriction) a
structure of a polyhedron. The inclusion map $Z \to X$ is also called a linear
metric embedding. 



\subsection{Piecewise Smooth Forms and Maps} \label{subsec:pws}
Let $X$ be an $n$-dimen\-sional polyhedron (Definition \ref{dfn:503}). A
$p$-dimensional linear
simplex in $X$ is by definition the image of an injective linear map 
$\tau : \bsym{\Delta}^p \to X$. 
A {\em linear triangulation of $X$} is a finite collection
$\{ X_j \}_{j \in J}$ of linear simplices in $X$, such that 
$X_j \neq X_k$ if $j \neq k$; each face of
a simplex $X_j$ is the simplex $X_k$ for some $k \in J$; 
for any $j, k \in J$ the intersection $X_j \cap X_k$ is the simplex
$X_l$ for some $l \in J$; and $X = \bigcup_{j \in J} X_j$. 
We let 
$J_p := \{ j \in J \mid \opn{dim} X_j = p \}$,
so 
$J = \coprod_{0 \leq p \leq n} J_p$.
The topological space 
\[ \opn{sk}_p T := \bigcup_{q \leq p} \ \bigcup_{j \in J_{q}} X_j \] 
is called the {\em $p$-skeleton} of the triangulation $T$. 

We shall have to use piecewise smooth differential forms on polyhedra. 
Suppose $T = \{ X_j \}_{j \in J}$ is a linear triangulation of a
polyhedron $X$. A {\em piecewise smooth differential $p$-form on $X$, relative
to the triangulation $T$}, is a collection 
$\{ \alpha_j \}_{j \in J}$ of differential forms, with
$\alpha_j \in \Omega^p(X_j)$,
such that for any inclusion $X_j \subset X_k$ of simplices one has
$\alpha_j |_{X_k} = \alpha_k$.
Let us denote by $\Omega^p_{\mrm{pws}}(X; T)$ the set of 
piecewise smooth differential $p$-form on $X$ relative to $T$, and
\[ \Omega_{\mrm{pws}}(X; T) := 
\bigoplus_{p = 0}^n \ \Omega^p_{\mrm{pws}}(X; T) , \]
where $n := \opn{dim} X$. This is a DG algebra. 

Next suppose $S = \{ Y_k \}_{k \in K}$ is a linear triangulation of 
$X$ which is a subdivision of $T$. This means that each simplex
$Y_k$ is contained in some simplex $X_j$. Take a piecewise smooth differential
form 
$\alpha = \{ \alpha_j \} \in \Omega^p_{\mrm{pws}}(X; T)$.
Then there is a unique piecewise smooth differential form 
$\beta = \{ \beta_k \} \in \Omega^p_{\mrm{pws}}(X; S)$
satisfying 
$\beta_k = \alpha_j|_{Y_k}$
for any inclusion $Y_k \subset X_j$.
In this way we get a DG algebra homomorphism
$\Omega_{\mrm{pws}}(X; T) \to \Omega_{\mrm{pws}}(X; S)$, which is actually
injective. Since any two triangulations have a common subdivision,
the DG algebras $\Omega_{\mrm{pws}}(X; T)$ form a directed system. 

\begin{dfn} \label{dfn:25}
Let $X$ be a polyhedron. The 
{\em algebra of piecewise smooth differential forms} 
\index{Piecewise smooth differential form}
on $X$ is the DG algebra
\[ \Omega_{\mrm{pws}}(X) := \lim_{T \to}\, \Omega_{\mrm{pws}}(X; T) , \]
where $T$ runs over all linear triangulations of $X$.
\end{dfn}

This definition is very similar to Sullivan's PL forms; see \cite{FHT}. 

Note that any element of
$\Omega^p_{\mrm{pws}}(X)$ is represented by 
some $\alpha \in \lb \Omega^p_{\mrm{pws}}(X; T)$, where $T$ is a
linear triangulation of $X$.
Such a triangulation $T$ is called a {\em smoothing triangulation} for 
$\alpha$. There are injective DG algebra homomorphisms
\begin{equation} \label{eqn:17}
\Omega(X) \to \Omega_{\mrm{pws}}(X; T) \to \Omega_{\mrm{pws}}(X) .
\end{equation}

It is an exercise to show that the cohomology of 
$\Omega(X)$ vanishes in positive degrees, and 
$\mrm{H}^0 \, \Omega(X) = \R$ (recall that $X$ is convex).
Also the homomorphisms (\ref{eqn:17}) are quasi-isomorphisms. 
(We shall not use these facts.)

\begin{dfn} \label{dfn:504}
Let $X$ be a polyhedron, and let $Y$ be a manifold (see Convention
\ref{conv:500}). 
\begin{enumerate}
\item  Let $T = \{ X_j \}_{j \in J}$ be a linear triangulation of $X$.
A map $f : X \to Y$ is called a {\em piecewise smooth map relative to $T$}
if $f|_{X_j} : X_j \to Y$ is smooth for every $j \in J$. 

\item A map $f : X \to Y$ is a  {\em piecewise smooth map}
\index{Piecewise smooth map}
if it is piecewise smooth relative to some linear triangulation $T$; and then 
we say that $T$ is a {\em smoothing triangulation} for $f$.
\end{enumerate}
\end{dfn}

Note that a piecewise smooth map $f : X \to \mbf{A}^1$ is
the same as an element of the $\R$-algebra
$\mcal{O}_{\mrm{pws}}(X) := \Omega^0_{\mrm{pws}}(X)$.
Given a piecewise smooth map $f : X \to Y$, there is an induced DG algebra
homomorphism
\[ f^* : \Omega(Y) \to \Omega_{\mrm{pws}}(X) . \]

Next suppose $X$ and $Y$ are both polyhedra. 
Then we can talk about {\em piecewise linear maps}
$f : X \to Y$, using linear triangulations of $X$ as explained in the previous
paragraph. Given a piecewise linear map $f : X \to Y$, there is an induced DG
algebra homomorphism
\[ f^* : \Omega_{\mrm{pws}}(Y) \to \Omega_{\mrm{pws}}(X) . \]
As usual, if $f$ is an embedding, then we write
$\alpha|_X := f^*(\alpha)$ for 
$\alpha \in \Omega_{\mrm{pws}}(Y)$.

Let $\alpha \in \Omega^p_{\mrm{pws}}(X)$.
The form $\alpha$ can be presented as follows. Choose a smoothing triangulation 
$T = \{ X_j \}_{j \in J}$ for $\alpha$; so that 
$\alpha|_{X_j} \in \Omega^p(X_j)$ for every $j$. Let
$\bsym{s} = (s_1, \ldots, s_n)$ be a linear coordinate system on $X$. For any 
$j$ let 
$\til{\alpha}_{j, \bsym{i}} \in \mcal{O}(X_j)$ be the coefficients of 
$\alpha|_{X_j}$ with respect to $\bsym{s}$, as in Definition \ref{dfn:27}.
Then
\begin{equation} \label{eqn:232}
\alpha|_{X_j} = \sum_{\bsym{i}} \, 
\til{\alpha}_{j, \bsym{i}} \cdot \d s_{i_1} \wedge \cdots \wedge \d s_{i_p} 
\in \Omega^p(X_j) , 
\end{equation}
where the multi-index 
$\bsym{i} = (i_1, \ldots, i_p)$ runs through all strictly increasing elements in
$\{ 1, \ldots, n \}^p$. 

Let $X$ be an $n$-dimensional polyhedron. Given a form
$\alpha \in \Omega_{\mrm{pws}}(X)$ and a point $x \in X$, we say that 
{\em $x$ is a smooth point of $\alpha$} if there exists some $n$-dimensional
simplex $Y$ in $X$, such that $x \in \opn{Int} Y$ and
$\alpha|_{Y} \in \Omega(Y)$.
The smooth locus of $\alpha$, i.e.\ the set of all smooth points of $\alpha$,
is open and dense in $X$. Its complement, called
the singular locus of $\alpha$, is contained in a finite union of simplices of
dimensions $< n$. Indeed, given any triangulation $T$ that smooths $\alpha$, the
singular locus of $\alpha$ is contained in the $(n-1)$-skeleton of $T$. 

Let $f : X \to Y$ be a 
piecewise smooth map from a polyhedron to a manifold. 
As above we can talk about the smooth locus of $f$, and whether 
$f|_Z : Z \to Y$ is smooth
for some simplex $Z \subset X$. 



\subsection{Sobolev Norm} \label{subsec:sob}
It shall be very convenient to have a bound for piecewise smooth forms
on polyhedra and some of their derivatives. 

Let $X$ be a polyhedron, with orthonormal linear coordinate
system $\bsym{s} =$ \lb  $(s_1, \ldots, s_n)$. Given a smooth function 
$f \in \mcal{O}(X)$ and a multi-index
\[ \bsym{i}  = (i_1, \ldots, i_q) \in \{ 1, \ldots, n \}^q , \]
we write
\[ \partial_{\bsym{i}} f :=
\smfrac{\partial^q}{\partial s_{i_1} \cdots \partial s_{i_q}} f \in  
\mcal{O}(X) . \]
In the case $q = 0$, so the only sequence is the empty sequence 
$\emptyset$, we write
$\partial_{\emptyset} f := f$. 
We refer to the operators $\partial_{\bsym{i}}$ as the partial derivatives
with respect to $\bsym{s}$.

\begin{dfn}
Let $X$ be a polyhedron of dimension $n$, and let $\bsym{s}$ be an
orthonormal linear coordinate system on $X$. 
\begin{enumerate}
\item Take a smooth differential form $\alpha \in \Omega^p(X)$. 
Consider the coefficients $\til{\alpha}_{\bsym{i}}$ of $\alpha$ with
respect to $\bsym{s}$, as in Definition \ref{dfn:27}. 
Let $\partial_{\bsym{j}}$ be the partial derivatives with respect to
$\bsym{s}$. For a point $x \in X$ and a natural number $q$ we define 
\[ \norm{\alpha}_{\mrm{Sob}; x, q} :=
\Bigl( \bosum_{\bsym{i}, \bsym{j}} \, 
(\partial_{\bsym{j}} \til{\alpha}_{\bsym{i}})(x)^2 \Bigr)^{1/2} \ , \]
where the sum is on all 
$\bsym{j} \in \{ 1, \ldots, n \}^q$ and on all strictly increasing 
$\bsym{i} \in \{ 1, \ldots, n \}^p$.

\item For $\alpha \in \Omega^p(X)$ we define 
\[ \norm{\alpha}_{\mrm{Sob}} :=
\sup_{q = 0, 1, 2} \ \sup_{x \in X} \ \norm{\alpha}_{\mrm{Sob}; x, q} \, . \]

\item Take a piecewise smooth differential form
$\alpha \in \Omega^p_{\mrm{pws}}(X)$. 
Let $\{ X_j \}_{j \in J}$ be some smoothing triangulation for $\alpha$,
and let $\alpha_j := \alpha|_{X_j} \in \Omega^p(X_j)$. Define
\[ \norm{\alpha}_{\mrm{Sob}} :=
\sup_{j \in J} \ \norm{ \alpha_j }_{\mrm{Sob}} \ . \]
\end{enumerate}

The number $\norm{-}_{\mrm{Sob}}$ is called the {\em Sobolev norm to order $2$}.
\end{dfn}

\begin{rem}
Even for a smooth function $f$, our Sobolev norm 
$\norm{f}_{\mrm{Sob}}$ is not the same as the
usual order $2$ Sobolev norm from functional analysis, namely
$\norm{f}_s$ with $s = 2$. But it is in the ``same spirit'', and hence we use
this name.
\end{rem}

\begin{prop}
Let $X$ be an $n$-dimensional polyhedron.
\begin{enumerate}
\item For $\alpha \in \Omega^p(X)$, $x \in X$ and $q \in \N$, the number 
$\norm{\alpha}_{\mrm{Sob}; x, q}$ is  independent of the orthonormal linear
coordinate system $\bsym{s}$ on $X$. Hence the number
$\norm{\alpha}_{\mrm{Sob}}$ is also coordinate independent.

\item Given $\alpha \in \Omega^p_{\mrm{pws}}(X)$, its Sobolev norm 
$\norm{\alpha}_{\mrm{Sob}}$ is independent of the  smoothing triangulation
$\{ X_j \}_{j \in J}$.

\item Let $Z$ be a sub-polyhedron of $X$ and let
$\alpha \in \Omega^p_{\mrm{pws}}(X)$. Then 
$\norm{\alpha|_Z}_{\mrm{Sob}} \leq \norm{\alpha}_{\mrm{Sob}}$.
\end{enumerate}
\end{prop}

\begin{proof}
(1) Let us denote by $V$ the vector space of constant vector fields on $X$.
This is a rank $n$ vector space, endowed with a canonical inner product. The
set $\{ \smfrac{\partial}{\partial s_i} \}_{i = 1, \ldots, n}$
is an orthonormal basis for $V$. 

For $p, q \in \N$ let us denote by $\opn{T}^q(V)$ and $\bwedge^p(V)$ the 
tensor  power and exterior power of $V$, respectively. The vector space
$\opn{T}^q(V) \otimes \bwedge^p(V)$ has an induced  inner product.

For a strictly increasing sequence 
\[ \bsym{i}   = (i_1, \ldots, i_p) \in \{ 1, \ldots, n \}^p \] 
let us write
\[ \pi_{\bsym{i}} := 
\smfrac{\partial}{\partial s_{i_1}} \wedge \cdots \wedge 
\smfrac{\partial}{\partial s_{i_p}} \in \bwedge^p(V) . \]
Then the set 
$\{ \partial_{\bsym{j}} \otimes \pi_{\bsym{i}} \}$,
where the indices run over all $\bsym{j} \in \{ 1, \ldots, n \}^q$ and  all
strictly increasing $\bsym{i} \in \{ 1, \ldots, n \}^p$,
is an orthonormal basis of $\opn{T}^q(V) \otimes \bwedge^p(V)$.

Now $V$ is the linear dual of $\Omega^1_{\mrm{const}}(X)$, so 
$\pi_{\bsym{i}}$ can be viewed as a linear map
$ \Omega^p(X) \to \mcal{O}(X)$.
Given $\alpha \in \Omega^p(X)$, its coefficients with respect to $\bsym{s}$
satisfy
$\til{\alpha}_{\bsym{i}} = \pi_{\bsym{i}}(\alpha)$.
Thus
\[ \partial_{\bsym{j}} \til{\alpha}_{\bsym{i}} = 
(\partial_{\bsym{j}} \circ \pi_{\bsym{i}})(\alpha) \]
in $\mcal{O}(X)$.
  
Suppose $\bsym{s}' = (s'_1, \ldots, s'_n)$ is another orthonormal
linear coordinate system. Let us denote by 
$\partial'_{\bsym{j}}$, $\til{\alpha}'_{\bsym{i}}$ and $\pi'_{\bsym{i}}$ the
new operators and coefficient, namely those with respect to $\bsym{s}'$. The
set 
$\{ \partial'_{\bsym{j}} \otimes \pi'_{\bsym{i}} \}$
is also an orthonormal basis of $\opn{T}^q(V) \otimes \bwedge^p(V)$.
So this set and the set 
$\{ \partial_{\bsym{j}} \otimes \pi_{\bsym{i}} \}$
are related by a constant orthogonal matrix (of size $n^q \cdot \binom{n}{p}$).
It follows that
\[ \sum_{\bsym{i}, \bsym{j}} \, 
(\partial'_{\bsym{j}} \til{\alpha}'_{\bsym{i}})(x)^2 =
\sum_{\bsym{i}, \bsym{j}} \, 
(\partial_{\bsym{j}} \til{\alpha}_{\bsym{i}})(x)^2 
 \]
for any $x \in X$. 

We see that $\norm{\alpha}_{\mrm{Sob}; x, q}$
is independent of coordinates. The assertion for 
$\norm{\alpha}_{\mrm{Sob}}$ is now clear.

\medskip  \noindent
(2) The supremum on $x$ can be restricted to a dense open set in each cell
$X_j$ of the triangulation $\{ X_j \}_{j \in J}$. Therefore we get the same
value by replacing the triangulation $\{ X_j \}_{j \in J}$ with a refinement. 

\medskip  \noindent
(3) Given $Z$, choose an orthonormal linear coordinate system on it, and extend
it to an orthonormal linear coordinate system on $X$. Now it is clear.
\end{proof}


\subsection{Orientation and Integration} \label{subsec:orient}
An orientation on a manifold means a choice of a volume form, up to
multiplication by a positive smooth function. However in the case of a
polyhedron we can normalize the volume form:

\begin{dfn}
Let $X$ be a polyhedron of dimension $n$.
An {\em orientation} on $X$ is a constant form 
$\opn{or}(X) \in \Omega_{\mrm{const}}^n(X)$, 
such that 
\[ \opn{or}(X) =  \d s_1 \wedge \cdots \wedge \d s_n \]
for some orthonormal linear coordinate system 
$(s_1, \ldots, s_n)$ on $X$. 
\end{dfn}

Note that if $(s'_1, \ldots, s'_n)$ is some other orthonormal linear coordinate
system, then 
\[ \opn{or}(X) = \pm \d s'_1 \wedge \cdots \wedge \d s'_n . \]
If the sign is $+$ then $(s'_1, \ldots, s'_n)$ is said to be {\em  positively
oriented}.

For the polyhedron $\mbf{I}^n$ there is a standard orientation, coming from
its embedding in $\mbf{A}^{n}$. It is 
\[ \opn{or}(\mbf{I}^n) := \d t_1 \wedge \cdots \wedge \d t_n , \]
where $(t_1, \ldots, t_n)$ is the standard coordinate system on $\mbf{A}^{n}$.
Likewise for the polyhedron $\bsym{\Delta}^n$:
we let
\[ \opn{or}(\bsym{\Delta}^n) := \d t_1 \wedge \cdots \wedge \d t_n , \]
where $(t_0, \ldots, t_n)$ is the barycentric coordinate system on 
$\mbf{A}^{n+1}$. 
For $n = 1, 2$ the orientations can be also described by arrows -- see Figure
\ref{fig:75}.

\begin{dfn} \label{dfn:24}
Let $X$ be an $n$-dimensional oriented polyhedron and let
$\alpha \in \Omega^n(X)$. 
The {\em coefficient} of $\alpha$ is the function 
$\til{\alpha} \in \mcal{O}(X)$ such that
$\alpha = \til{\alpha} \cdot \opn{or}(X)$.
\end{dfn}

In other words, $\til{\alpha}$ is the coefficient of $\alpha$ with respect to
any positively oriented orthonormal linear coordinate system, in the sense of 
Definition \ref{dfn:27}.

An orientation on $X$ induces an orientation on the $(n-1)$-dimensional 
polyhedra that make up the boundary $\partial X$ (by contracting the
orientation volume form of $X$ with 
a constant outer gradient to the face; cf.\  \cite[Section 4.8]{Wa}).

Let $X$ be an $n$-dimensional oriented polyhedron. Suppose 
$\alpha = \{ \alpha_j \}_{j \in J} \lb \in 
\Omega^n_{\mrm{pws}}(X; T)$,
where $T = \{ X_j \}_{j \in J}$ is some linear
triangulation of $X$. Any $n$-dimen\-sional simplex $X_j$ inherits an
orientation, and hence the integral 
$\int_{X_j} \alpha_j$ is  well-defined. We let 
\[ \int_{X} \alpha := \sum_{j \in J_n } \
\int_{X_j} \alpha_j \in \R \ .  \]
This integration is compatible with subdivisions, and thus we have a
well-defined function
\[ \int_{X} : \Omega^n_{\mrm{pws}}(X) \to \R . \]

\begin{thm}[Stokes Theorem] \label{thm:15}
Let $X$ be an oriented $n$-dimensional polyhedron, and let
$\alpha \in \Omega^{n-1}_{\mrm{pws}}(X)$.
Then
\[ \int_{X} \d \alpha = \int_{\partial X} \alpha \ . \]
\end{thm}

\begin{proof}
Choose a linear triangulation $T = \{ X_j \}_{j \in J}$ of $X$ that smooths
$\alpha$; so that 
$\alpha = \{ \alpha_i \}_{j \in J}$ with
$\alpha_j \in \Omega^{n-1}(X_j)$.
Then by definition of $\int_{\partial X} \alpha$, and by cancellation due to
opposite orientations of inner $(n-1)$-dimensional simplices, we get
\[ \int_{\partial X} \alpha = 
\sum_{j \in J_n} \ \int_{\partial X_j} \alpha_j . \]
And the usual Stokes Theorem tells us that
\[ \int_{\partial X_j} \alpha_j = \int_{X_j} \d \alpha_j \ . \]
\end{proof}




\subsection{Piecewise Continuous Forms} \label{subsec:pwc}
For a polyhedron $X$, let us denote by $\mcal{O}_{\mrm{cont}}(X)$ the set of
continuous $\R$-valued functions on $X$. This is a commutative $\R$-algebra
containing $\mcal{O}_{\mrm{pws}}(X)$.

\begin{dfn} \label{dfn:40}
Let $p$ be a natural number. By {\em piecewise continuous $p$-form} on $X$ we
mean an element 
$\gamma \in \Omega^p_{\mrm{pwc}}(X)$, where we define
\[ \Omega^p_{\mrm{pwc}}(X) :=
\mcal{O}_{\mrm{cont}}(X) \otimes_{\mcal{O}_{\mrm{pws}}(X)}
\Omega^p_{\mrm{pws}}(X) . \]
\end{dfn}

A piecewise continuous $p$-form $\gamma$ can be represented as follows:
there are continuous functions
$f_1, \ldots, f_m \in \mcal{O}_{\mrm{cont}}(X)$,
and piecewise smooth forms
$\alpha_1, \ldots, \alpha_m \in \Omega^p_{\mrm{pws}}(X)$,
such that 
\begin{equation} \label{eqn:220}
\gamma = \sum_{i = 1}^m \, f_i \cdot \alpha_i .
\end{equation}

For $p = 0$ we have 
$\Omega^p_{\mrm{pwc}}(X) = \mcal{O}_{\mrm{cont}}(X)$ of course. 
But for $p > 0$ these forms are much more complicated, as we shall see below.

Warning: the exterior derivative $\d (\gamma)$ is not defined for 
$\gamma \in \Omega^p_{\mrm{pwc}}(X)$; at least not as a piecewise continuous
form (it is a distribution). The problem of course is that the functions $f_i$ 
above cannot be derived.

However, given $\gamma \in \Omega^p_{\mrm{pwc}}(X)$ and a piecewise linear map
$g
: Y \to X$ between polyhedra, the pullback
\[ g^*(\gamma) \in \Omega^p_{\mrm{pwc}}(Y) \]
is well defined. In terms of the expansion (\ref{eqn:220}), the formula is
\[ g^*(\gamma) = \sum_{i = 1}^m \, g^*(f_i) \cdot g^*(\alpha_i) . \]
Here $g^*(f_i) \in \mcal{O}_{\mrm{cont}}(Y)$ and
$g^*(\alpha_i) \in \Omega^p_{\mrm{pws}}(Y)$. 
If $g$ is a closed embedding then we write
$\gamma|_Y := g^*(\gamma)$ as usual.

The presentation (\ref{eqn:220}) of 
$\gamma \in \Omega^p_{\mrm{pwc}}(X)$ can be expanded further. 
Choose a linear triangulation $\{ X_j \}_{j \in J}$ of $X$ that smooths all the
piecewise smooth forms $\alpha_1, \ldots, \alpha_m$. 
Also choose a linear coordinate system $\bsym{s} = (s_1, \ldots, s_n)$ on $X$.
For any $i \in \{ 1, \ldots, m \}$ and $j \in J$ let 
$e_{i, j, \bsym{k}} \in \mcal{O}(X_j)$ be the coefficients of the smooth form
$\alpha_i|_{X_j}$ with respect to $\bsym{s}$, as in Definition \ref{dfn:27}.
Then
\begin{equation} \label{eqn:234}
\gamma|_{X_j} = \sum_{i = 1}^m \ \sum_{\bsym{k}} \ 
f_i \cdot e_{i, j, \bsym{k}} \cdot 
\d s_{k_1} \wedge \cdots \wedge \d s_{k_p} 
\in \Omega^p_{\mrm{pwc}}(X_j) ,
\end{equation}
where as usual the multi-index 
$\bsym{k} = (k_1, \ldots, k_p)$ runs through all strictly increasing elements in
$\{ 1, \ldots, n \}^p$. 

For top degree forms one can say more. 
Let $\gamma \in \Omega^n_{\mrm{pwc}}(X)$. In this case the expansion 
(\ref{eqn:234}) can be simplified to 
\begin{equation} \label{eqn:235}
\gamma|_{X_j} = \sum_{i = 1}^m  \ 
f_i \cdot e_{i, j} \cdot \d s_1 \wedge \cdots \wedge \d s_n
\in \Omega^n_{\mrm{pwc}}(X_j) ,
\end{equation}
with $e_{i, j} \in \mcal{O}(X_j)$.

Now assume that the polyhedron $X$ is oriented. We can choose the coordinate
system $\bsym{s} = (s_1, \ldots, s_n)$ so that it is orthonormal and positively
oriented; and then 
\[ \opn{or}(X) = \d s_1 \wedge \cdots \wedge \d s_n . \]
For any $j \in J_n$ we can integrate the continuous function 
$\sum_{i = 1}^m \, f_i \cdot e_{i, j}$ on the oriented $n$-dimensional
simplex $X_j$, obtaining
\[ \int_{X_j} \gamma := \int_{X_j} \
\sum_{i = 1}^m \, f_i \cdot e_{i, j} \cdot 
\d s_1 \wedge \cdots \wedge \d s_n \in \R . \]
Using this formula we define
\begin{equation} \label{eqn:236}
\int_{X} \gamma := \sum_{j \in J_n}  \ \int_{X_j} \gamma
\in \R . 
\end{equation}

\begin{prop} \label{prop:26}
For an $n$-dimensional oriented polyhedron $X$ and a piecewise continuous form
$\gamma \in \Omega^n_{\mrm{pwc}}(X)$, the number
$\int_{X} \gamma$ is independent of the presentation 
\tup{(\ref{eqn:235})} of $\gamma$.
\end{prop}

We leave out the easy proof. 

More generally, suppose $X$ is an $n$-dimensional polyhedron (not necessarily
oriented), $Z$ is an oriented $p$-dimensional polyhedron, 
$\tau : Z \to X$ is a piecewise linear map, and 
$\gamma \in \Omega^p_{\mrm{pwc}}(X)$. Then 
$\tau^*(\gamma) \in \Omega^p_{\mrm{pwc}}(Z)$, and we can use 
(\ref{eqn:236}) to integrate $\gamma$ along $\tau$ as follows:
\begin{equation} \label{eqn:221}
\int_{\tau} \gamma := \int_Z \tau^*(\gamma) \in \R . 
\end{equation}







\cleardoublepage
