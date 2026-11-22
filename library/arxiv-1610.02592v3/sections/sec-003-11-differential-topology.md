---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-003-11-differential-topology
section_title: "Differential topology"
section_number: 1.1
pages: 15-23
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.932
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{differential:topology:section}
We introduce manifolds, bundles, embeddings, tubular neighbourhoods, isotopies, and connected sums. Throughout this book, we will always work in the smooth category. 
The material contained in this section is carefully explained in \emph{Differentiable manifolds} of Kosinksi \cite{K}.


\subsection{Differentiable manifolds}
A \emph{topological manifold} of dimension $n$ is a paracompact Hausdorff topological space $M$ locally homeomorphic to $\matR^n$. In other words, there is a covering $\{U_i\}$ of $M$ consisting of open sets $U_i$ homeomorphic to open sets $V_i$ in $\matR^n$.
\index{manifold}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{test-BW}{test}}
\nota{The \emph{Alexander horned sphere} is a subset of $\matR^3$ homeomorphic to the 2-sphere $S^2$. It divides $\matR^3$ into two connected components, none of which is homeomorphic to an open ball. It was constructed by Alexander as a counterexample to a natural three-dimensional generalisation of Jordan's curve theorem. The natural generalisation would be the following: does every 2-sphere in $\matR^3$ bound a ball? If the 2-sphere is only topological, the answer is negative
as this counterexample shows. If the sphere is a differentiable submanifold, the answer is however positive as proved by Alexander himself.}
\label{Alexander:fig}
\end{center}
\end{figure}

Topological manifolds are difficult to investigate, their definition is too general and allows to directly define and prove only few things. Even the notion of dimension is non-trivial: to prove that an open set of $\matR^k$ is not homeomorphic to an open set of $\matR^h$ for different $k$ and $h$ we need to use non-trivial constructions like homology. It is also difficult to treat topological subspaces: for instance, the \emph{Alexander horned sphere} shown in Figure \ref{Alexander:fig} is a subspace of $\matR^3$ topologically homeomorphic to a 2-sphere. It is a complicated object that has many points that are not ``smooth'' and that cannot be ``smoothened'' in any reasonable way.

We need to define some ``smoother'' objects, and for that purpose we can luckily invoke the powerful multivariable infinitesimal calculus. Let $U\subset \matR^n$ be an open set: a map $f\colon U\to \matR^k$ is  \emph{smooth} if it is $C^\infty$, \emph{i.e.}~it has partial derivatives of any order.

\begin{defn} Let $M$ be a topological manifold.
A \emph{chart} is a fixed homeomorphism $\varphi_i\colon U_i \to V_i$ between an open set $U_i$ of $M$ and an open set $V_i$ of $\matR^n$. An \emph{atlas} is a set of charts $\big\{(U_i, \varphi_i)\big\}$ where the open sets $U_i$ cover $M$. 

If $U_i\cap U_j\neq\varnothing$ there is a \emph{transition map} $\varphi_{ji} = \varphi_j\circ \varphi_i^{-1}$ that sends homeomorphically the open set $\varphi_i({U_i\cap U_j})$ onto the open set $\varphi_j({U_i\cap U_j})$. Since these two open sets are in $\matR^n$, it makes sense to require $\varphi_{ij}$ to be smooth. The atlas is \emph{differentiable} if all transition maps are smooth. 
\end{defn}

\index{manifold!differentiable manifold}
\begin{defn}
A \emph{differentiable manifold} is a topological manifold that is equipped with a differentiable atlas.
\end{defn}

We will often use the word \emph{manifold} to indicate a differentiable manifold.
The integer $n$ is the \emph{dimension} of the manifold. We have defined the objects, so we now turn to their morphisms. 

\begin{defn}
A map $f\colon M \to M'$ between differentiable manifolds is \emph{smooth} if it is smooth when read locally through charts. This means that for every $p \in M$ there are two charts $(U_i, \varphi_i)$ of $M$ and $(U_j', \varphi_j')$ of $N$ with $p\in U_i$ and $f(p)\in U_j'$ such that the composition
$\varphi_j'\circ f \circ \varphi_i^{-1}$ is smooth wherever it is defined. 
\end{defn}

A \emph{diffeomorphism} is a smooth map $f\colon M \to M'$ that admits a smooth inverse $g\colon M'\to M$. A \emph{curve} in $M$ is a smooth map $\gamma \colon I \to M$ defined on some open interval $I$ of the real line, which may be bounded or unbounded. 
\index{diffeomorphism}

\begin{defn} A differentiable manifold is \emph{oriented} if it is equipped with an atlas where all transition functions are orientation-preserving (that is, the determinant of their differential at any point is positive).
\end{defn}

A manifold which can be oriented is called \emph{orientable}.
\index{manifold!oriented manifold}


\subsection{Tangent space} \label{tangente:subsection}
Let $M$ be a differentiable manifold of dimension $n$. We may define for every point $p\in M$ a $n$-dimensional vector space $T_pM$ called the \emph{tangent space}. 

The space $T_pM$ may be defined briefly as the set of all curves $\gamma\colon (-a,a) \to M$ such that $\gamma(0) = p$ and $a>0$ is arbitrary, considered up to some equivalence relation. The relation is the following: we identify two curves that, read on some chart $(U_i,\varphi_i)$, have the same tangent vector at $\varphi_i(p)$. The definition does not depend on the chart chosen.
\index{tangent space}

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{Tangentialvektor_new-BW}{Tangentialvektor_new}}
\nota{The tangent space in $x$ may be defined as the set of all curves $\gamma$ with $\gamma(0)=x$ seen up to an equivalent relation that identifies two curves having (in some chart) the same tangent vector at $x$. This condition is chart-independent.}
\label{Tangentialvektor:fig}
\end{center}
\end{figure}

A chart identifies $T_pM$ with the usual tangent space $\matR^n$ at $\varphi_i(p)$ in the open set $V_i = \varphi_i(U_i)$. Two distinct charts $\varphi_i$ and $\varphi_j$ provide different identifications with $\matR^n$, which differ by a linear isomorphism: the differential $d\varphi_{ji}$ of the transition map $\varphi_{ij}$. The structure of $T_pM$ as a vector space is then well-defined, while its identification with $\matR^n$ is not.

Every smooth map $f\colon M \to N$ between differentiable manifolds induces at each point $p\in M$ a linear map $df_p\colon T_pM \to T_{f(p)} N$ between tangent spaces in the following simple way: the curve $\gamma$ is sent to the curve $f\circ\gamma$.

\begin{defn} A smooth map $f\colon M \to N$ is a \emph{local diffeomorphism} at a point $p \in M$ if there are two open sets $U\subset M$ and $V\subset N$ containing respectively $p$ and $f(p)$ such that $f|_U\colon U \to V$ is a diffeomorphism.\index{diffeomorphism!local diffeomorphism}
\end{defn}

The inverse function theorem in $\matR^n$ implies easily the following fact, that demonstrates the importance of tangent spaces.

\begin{teo}
Let $f\colon M \to N$ be a smooth map between manifolds of the same dimension. The map is a local diffeomorphism at $p\in M$ if and only if the differential $df_p\colon T_pM \to T_{f(p)}N$ is invertible.
\end{teo}

In this theorem a condition satisfied at a single point (differential invertible at $p$) implies a local property (local diffeomorphism). Later on, we will see that in Riemannian geometry a condition satisfied at a single point may also imply a global property.

If $\gamma\colon I \to M$ is a curve, its \emph{velocity} $\gamma'(t)$ in $t\in I$ is the tangent vector $\gamma'(t) = d\gamma_t(1)$. Here ``1'' means the vector 1 in the tangent space $T_tI = \matR$. We note that the velocity is a vector and not a number: the modulus of a tangent vector is not defined in a differentiable manifold (because the tangent space is just a real vector space, without a norm).


\subsection{Differentiable submanifolds}
Let $N$ be a differentiable manifold of dimension $n$. 
\begin{defn}
A subset $M\subset N$ is a \emph{differentiable submanifold} of dimension $m\leqslant n$ if every $p\in M$ has an open neighbourhood $U\subset N$ diffeomorphic to an open set $V\subset \matR^n$ via a map $\varphi\colon U \to V$ that sends $U\cap M$ onto $V\cap L$, where $L$ is a linear subspace of dimension $m$.
\end{defn}
\index{submanifold!differentiable submanifold}

The pairs $\{(U\cap M, \varphi|_{U\cap M})\}$ form an atlas for $M$, which inherits a structure of $m$-dimensional differentiable manifold. At every point $p\in M$ the tangent space $T_p M$ is a linear subspace of $T_p N$. 


\subsection{Fibre bundles}
We introduce an important type of smooth maps. 
\begin{defn}
A \emph{smooth fibre bundle} is a smooth map
$$\pi\colon E \longrightarrow B$$
such that every fibre $\pi^{-1}(p)$ is diffeomorphic to a fixed manifold $F$ and $\pi$ looks locally like a projection. This means that $B$ is covered by open sets $U_i$ equipped with diffeomorphisms $\psi_i \colon U_i\times F \to \pi^{-1}(U_i) $ such that $\pi\circ\psi_i$ is the projection on the first factor.
\end{defn}
\index{fibre bundle}

The manifolds $E$ and $B$ are called the \emph{total} and \emph{base manifold}, respectively. The manifold $F$ is the \emph{fibre} of the bundle. A \emph{section} of the bundle is a smooth map $s\colon B\to E$ such that $\pi\circ s = \id_B$. Two fibre bundles $\pi\colon E \to B$ and $\pi'\colon E' \to B$ are \emph{isomorphic} if there is a diffeomorphism $\psi\colon E \to E'$ such that $\pi = \pi'\circ\psi$.


\subsection{Vector bundles}
A \emph{smooth vector bundle} is a smooth fibre bundle where every fibre $\pi^{-1}(p)$ has the structure of a $n$-dimensional real vector space which varies smoothly with $p$. Formally, we require that $F=\matR^n$ and $\psi_i (p,\cdot)\colon F \to \pi^{-1}(p) $ be an isomorphism of vector spaces for every $\psi_i$ as above.
\index{vector bundle}

The \emph{zero-section} of a smooth vector bundle is the section $s\colon B \to E$ that sends $p$ to $s(p)=0$, the zero in the vector space $\pi^{-1}(p)$. The image $s(B)$ of the zero-section is typically identified with $B$ via $s$.

Two vector bundles are \emph{isomorphic} if there is a diffeomorphism $\psi$ as above, which restricts to an isomorphism of vector spaces on each fibre.
As every manifold here is differentiable, likewise every bundle will be smooth and we will hence often omit this word.


\subsection{Tangent and normal bundle}
Let $M$ be a differentiable manifold of dimension $n$. The union of all tangent spaces 
$$TM = \bigcup_{p\in M} T_pM$$ 
is naturally a differentiable manifold of double dimension $2n$, called the \emph{tangent bundle}. The tangent bundle $TM$ is naturally a vector bundle over $M$, the fibre over $p\in M$ being the tangent space $T_pM$. 

\index{normal space}
Let $M\subset N$ be a smooth submanifold of $N$. The \emph{normal space} at a point $p\in M$ is the quotient vector space $\nu_pM = T_pN/_{T_pM}$. The \emph{normal bundle} $\nu M$ is the union
$$\nu M = \bigcup_{p\in M} \nu_p M$$ 
and is also naturally a smooth vector bundle over $M$. The normal bundle is not  canonically contained in $TN$ like the tangent bundle, but (even more usefully) it may be embedded directly in $N$, as we will soon see.


\subsection{Vector fields}
A \emph{vector field} $X$ on a smooth manifold $M$ is a section of its tangent bundle. A point $p$ and a vector $v\in T_pM$ determine an \emph{integral curve} $\alpha\colon I\to M$ starting from $v$, that is a smooth curve with $\alpha(0) = p, \alpha'(0) = v$, and $\alpha'(t) = X(\alpha(t))$ for all $t\in I$. The curve $\alpha$ is unique if we require the interval $I$ to be maximal. It depends smoothly on $p$ and $v$.
\index{vector field}


\subsection{Immersions and embeddings}
A smooth map $f\colon M \to N$ between manifolds is an \emph{immersion} if its differential is everywhere injective: note that this does not imply that $f$ is injective. 
The map is an \emph{embedding} if it is a diffeomorphism onto its image: this means that $f$ is injective, its image is a submanifold, and $f\colon M \to f(M)$ is a diffeomorphism. 
\index{immersion}
\index{embedding}

\begin{teo} If $M$ is compact, every injective immersion $f\colon M \to N$ is an embedding.
\end{teo}


\subsection{Isotopy and ambient isotopy} \label{isotopy:subsection}
Let $X$ and $Y$ be topological spaces. We recall that a \emph{homotopy} between two continuous maps $\varphi, \psi\colon X \to Y$ is a continuous map $F\colon X\times [0,1]\to Y$  such that $F_0 = \varphi$ and $F_1 = \psi$, where $F_t = F(\cdot, t)$. 

\index{isotopy}
Let $M$ and $N$ be differentiable manifolds. A \emph{smooth isotopy} between two embeddings $\varphi, \psi\colon M \to N$ is a smooth homotopy $F$ between them, such that every map $F_t$ is an embedding. Again, we will shortly use the word \emph{isotopy} to mean a smooth isotopy. We note that many authors do not require an isotopy to be smooth, but we do.

Being isotopic is an equivalence relation for smooth maps $M\to N$: two isotopies $F_t$ and $G_u$ can be glued if $F_1 = G_0$, and since we want a smooth map we priorly modify $F$ and $G$ so that they are constant near $t=1$ and $u=0$. This can be done easily by reparametrising $t$ and $u$.

An \emph{ambient isotopy} on $N$ is an isotopy between $\id_N$ and some other diffeomorphism $\varphi\colon N \to N$, such that every level is a diffeomorphism. Two embeddings $\varphi, \psi\colon M \to N$
are \emph{ambiently isotopic} if there is an ambient isotopy $F$ of $N$ such that $\psi = F_1\circ \varphi$. 

\begin{teo} 
If $M$ is compact, two embeddings $\varphi, \psi\colon M \to N$ are isotopic if and only if they are ambiently isotopic.
\end{teo}


\subsection{Tubular neighbourhood}
Let $M\subset N$ be a differentiable submanifold. A \emph{tubular neighbourhood} of $M$ is an open subset $U\subset N$ with a diffeomorphism $\nu M \to U$ sending identically the zero-section onto $M$. 
\index{tubular neighbourhood}

\begin{teo} Let $M\subset N$ be a closed differentiable submanifold. A tubular neighbourhood for $M$ exists and is unique up to an isotopy fixing $M$ and up to pre-composing with a bundle isomorphism of $\nu M$.
\end{teo}

If we are only interested in the open set $U$ and not its parametrisation, we can of course disregard the bundle isomorphisms of $\nu M$.

Vector bundles are hence useful (among other things) to understand neighbourhoods of submanifolds. Since we will be interested essentially in manifolds of dimension at most 3, two simple cases will be important.

\begin{prop} \label{unique:line:bundle:prop}
A connected compact manifold $M$ has a unique line bundle $E\to M$ up to isomorphism with orientable total space $E$.
\end{prop}

The orientable line bundle on $M$ is a product $M\times \matR$ precisely when $M$ is also orientable. If $M$ is not orientable, the unique orientable line bundle is indicated by $M \timtil \matR$.

\begin{prop} \label{S1:bundle:prop}
For every $n$, there are exactly two vector bundles of dimension $n$ over $S^1$ up to isomorphism, one of which is orientable.
\end{prop}

Again, the orientable vector bundle is $S^1 \times \matR^n $ and the non-orientable one is denoted by $S^1 \timtil \matR^n$. These simple facts allow us to fully understand the possible neighbourhoods of curves in surfaces, and of curves and surfaces inside orientable 3-manifolds. 


\subsection{Manifolds with boundary}
Let a \emph{differentiable manifold $M$ with boundary} be a topological space with charts on a fixed half-space of $\matR^n$ instead of $\matR^n$, forming a smooth atlas. (By definition, maps from subsets of $\matR^n$ are smooth if they locally admit extensions to smooth functions defined on open domains.) 
\index{manifold!manifold with boundary}

The points corresponding to the boundary of the half-space form a subset of $M$ denoted by $\partial M$ and called \emph{boundary}. The boundary of a $n$-manifold is naturally a $(n-1)$-dimensional manifold without boundary. The \emph{interior} of $M$ is $M\setminus \partial M$.

We can define the tangent space $T_pM$ at a point $p\in \partial M$ as the set of all curves in $M$ starting from or arriving to $p$, with the same equivalence relation as above. The space $T_pM$ is a vector space that contains the hyperplane $T_p \partial M$. Most of the notions introduced for manifolds extend in an appropriate way to manifolds with boundary. A \emph{submanifold} of a manifold with boundary $M$ is the image of an embedding $N \hookrightarrow M$, where $N$ is another manifold with boundary.

\index{disc}
The most important manifold with boundary is certainly the \emph{disc} 
$$D^n = \big\{x\ \big|\ \|x\|\leqslant 1\big\}\subset \matR^n.$$ 
More generally, a \emph{disc} in a $n$-manifold $N$ is a submanifold $D\subset N$ with boundary diffeomorphic to $D^n$. Since a disc is in fact a (closed) tubular neighbourhood of any point in its interior, the uniqueness of tubular neighbourhoods implies the following.

\begin{teo}[Cerf -- Palais] \label{dischi:teo}
Let $N$ be connected and oriented. Two orientation-preserving embeddings $f,g\colon D^n \to \interior {N}$ are ambiently isotopic.
\end{teo}

A \emph{boundary component} $N$ of $M$ is a connected component of $\partial M$. A \emph{collar} for $N$ is an open neighbourhood diffeomorphic to $N\times [0,1)$. As for tubular neighbourhoods, every compact boundary component has a collar, unique up to isotopy.
\index{collar}

A \emph{closed manifold} is a compact manifold without boundary.
\index{manifold!closed manifold}


\subsection{Cut and paste} \label{cut:subsection}
If $M\subset N$ is a closed and orientable $(n-1)$-submanifold in the interior of an orientable $n$-manifold $N$, it has a tubular neighbourhood diffeomorphic to $M \times \matR$. The operation of \emph{cutting} $N$ along $M$ consists of the removal of the portion $M\times (-1,1)$. The resulting manifold $N'$ has two new boundary components $M\times \{-1\}$ and $M\times \{1\}$, both diffeomorphic to $M$. By the uniqueness of the tubular neighbourhood, the manifold $N'$ depends (up to diffeomorphisms) only on the isotopy class of $M\subset N$.

\index{cut and paste}
Let $M$ and $N$ be connected. The submanifold $M$ is \emph{separating} if its complement consists of two connected components. The cut manifold has two or one components depending on whether $M$ is separating or not.

Conversely, let $M$ and $N$ be $n$-manifolds with boundary, and let $\varphi \colon \partial M \to \partial N$ be a diffeomorphism. It is possible to \emph{glue} $M$ and $N$ along $\varphi$ and obtain a new $n$-manifold as follows.

A na\"\i ve approach would consist in taking the topological space $M\sqcup N$ and identify $p$ with $\varphi (p)$ for all $p\in \partial M$. The resulting quotient space is indeed a topological manifold, but the construction of a smooth atlas is not immediate. A quicker method consists of taking two collars $\partial M\times [0,1)$ and $\partial N\times [0,1)$ of the boundaries and then consider the topological space
$$(M\setminus \partial M) \sqcup (N\setminus \partial N).$$
Now we identify the points $(p,t)$ and $(\varphi (p), 1-t)$ of the open collars, for all $p\in \partial M$ and all $t\in (0,1)$. Having now identified two \emph{open} subsets of $M\setminus \partial M$ and $N\setminus \partial N$, a differentiable atlas for the new manifold is immediately derived from the atlases of $M$ and $N$.

\begin{prop} \label{depend:diffeo:prop}
The resulting smooth manifold depends (up to diffeomorphism) only on the isotopy class of $\varphi$.
\end{prop}


\subsection{Connected sum} \label{sum:subsection}
We introduce an important cut-and-paste operation. The \emph{connected sum} of two connected oriented $n$-manifolds $M$ and $M'$ is a new $n$-manifold obtained by choosing two $n$-discs $D\subset \interior{M}$ and $D'\subset \interior{M'}$ and an orientation-reversing diffeomorphism $\varphi\colon D \to D'$. The new manifold is constructed in two steps: we first remove the interiors of $D$ and $D'$ from $M\sqcup M'$, thus creating two new boundary components $\partial D$ and $\partial D'$, and then glue these boundary components along $\varphi|_{\partial D}$. See Figure \ref{Connected_sum:fig}.\index{connected sum}

We denote the resulting manifold by $M\# M'$. Since $\varphi$ is orientation-reversing, the manifold $M\# M'$ is oriented coherently with $M$ and $M'$. Theorem \ref{dischi:teo} implies the following.

\begin{figure}






\centering
\includegraphics[width = 7 cm] {Connected_sum}
\nota{A connected sum of closed surfaces.}
\label{Connected_sum:fig}
\end{figure}

\begin{prop}
The oriented smooth manifold $M\# M'$ depends (up to diffeomorphism) only on $M$ and $M'$. The connected sum operation $\#$ is commutative, associative, and $S^n$ serves as the identity element.
\end{prop}

We can invert a connected sum as follows. Suppose a $n$-manifold $M$ contains a separating $(n-1)$-sphere $N\subset \interior{M}$. We fix a diffeomorphism $\varphi\colon N \to \partial D^n$. By cutting $M$ along $N$ we get two new boundary components diffeomorphic to $N$ and we glue two discs to them via the map $\varphi$. We get two manifolds $N_1, N_2$ such that $M=N_1\# N_2$.


\subsection{Transversality}
Let $f\colon M \to N$ be a smooth map between manifolds and $X\subset N$ be a submanifold. We say that $f$ is \emph{transverse} to $X$ if for any $p\in f^{-1}X$ the following condition holds:
$$\img (d f_p) + T_{f(p)}X = T_{f(p)}N.$$
The maps transverse to a fixed $X$ are generic, that is they form an open dense subset in the space of all smooth maps from $X$ to $Y$, with respect to an appropriate topology. In particular the following holds.
\begin{teo}
Let $f\colon M \to N$ be a continuous map and $d$ a distance on $N$ compatible with the topology of $N$. For every $\varepsilon >0$ there is a smooth map $g$ transverse to $X$, homotopic to $f$, with $d(f(p), g(p))<\varepsilon$ for all $p\in M$.
\end{teo}
\index{transverse map}
