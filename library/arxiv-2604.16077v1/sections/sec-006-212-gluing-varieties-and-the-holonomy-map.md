---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-006-212-gluing-varieties-and-the-holonomy-map
section_title: "Gluing varieties and the holonomy map"
section_number: 2.1.2
pages: 10-12
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.967
---
\label{sec:tri_GV} In this section we explain how the structures carried by quantum $3$-simplices can be globalized on ideal triangulations.
\smallskip

Let $M$ be a cusped manifold, i.e. an oriented non-compact $3$-manifold admitting a complete hyperbolic metric of finite volume. We denote by $\bar{M}$ the compact manifold with interior $M$; $\partial \bar{M}$ is a union of $p$ tori. 

Let  $T$ be an ideal triangulation of $M$, i.e. a gluing by simplicial face pairings of tetrahedra with truncated (``ideal'') vertices, homeomorphic to $M$. 

Denote by $\Delta^1,\ldots,\Delta^n$ the tetrahedra of $T$, with the orientation induced from $M$. We call {\it abstract tetrahedra} and {\it abstract edges} of $T$ the tetrahedra $\Delta^i$ and their edges before their gluings in $T$. Give each tetrahedron $\Delta^i$ a branching $b^i$, as defined in Section \ref{sec:q3Delta}. Denote by $b$ the collection of these local branchings $b^i$. We do not ask that they match along common edges (so we can choose each $b^i$ so that $*_{b^i}(\Delta^i)=1$). We note however that for such global branchings $b$, when they exist (like for $(T,b)$ in Figure 1), the QHI state sums have the simplest form (\cite{AGT}).
\smallskip

\begin{defi} {\rm The {\it quantum gluing variety} $G_N(T,b)$ is the set of tuples $\bw:=(\bw^1,\ldots,\bw^n)\in \mc^{3n}$, where $\bw^i=(\bw_0^i,\bw_1^i,\bw_2^i)$ is a triple of quantum shape parameters on $(\Delta^i,b^i)$, $i=1,\ldots,n$, as in Section \ref{sec:q3Delta}, satisfying the following {\it edge relation} at each edge $e$ of $T$:}
\begin{equation}\label{edgerel}
\prod_{E\ra e} \bw(E)^{*_E(\Delta)} =  e^{-\frac{2\pi i}{N}}.
\end{equation}
{\rm Here the product is over all the abstract edges $E$ identified to $e$ in $T$ (which is denoted $E\ra e$), $\bw(E)$ is the quantum shape parameter of $E$ in the corresponding  tetrahedron $\Delta^i$, and $*_E(\Delta)$ is its branching sign.}
\end{defi}
Note that the branching $b$ enters the definition of $G_N(T,b)$ only in that it specifies a concrete model of the space in $\mc^{3n}$. Different branchings yield isomorphic spaces. In \cite[Section 3B and 4C]{AGT} the space $G_N(T,b)$ was denoted $G_0(T,b,c)_N$. 
\smallskip

For $N=1$, $G(T,b):=G_1(T,b)$ is Thurston's gluing variety associated to $T$, since in this case $\bw^i = w^i$ is a triple of shape parameters $(w_0^i,w_1^i,w_2^i)$ for the tetrahedron $\Delta^i$, satisfying the edge relations $\textstyle \prod_{E\ra e} w(E)^{*_E(\Delta)} =  1$ (with the notations of \eqref{edgerel}). 
\smallskip

It is a well-known fact that $G(T,b)\ne \emptyset$ if all the edges $e$ of $T$ are {\it essential}, {\it i.e.}, $e\cap \bar{M}$ is not homotopic to an arc in $\partial \bar{M}$ by a homotopy fixing the endpoints. In that case we have $G_N(T,b)\ne \emptyset$ (see Theorem \ref{teocoverGN}). Moreover, denote by $\tilde M$ the universal cover of $M$. By ``straightening'' the tetrahedra of $T$ by means of an isometry $\tilde M\ra \mh^3$, one can see that if $G(T,b)\ne \emptyset$, then the character $\rho_{hyp}$ of the discrete faithful representations of $\pi_1(M)$ into $PSL(2,\mc)$ is encoded by a point of $G(T,b)$. 

More generally, when $G(T,b)$ is non-empty it is related to the variety $X(M)$ of {\it $PSL(2,\mc)$-characters of $M$} as follows (see {\it e.g.} \cite{NZ,BP,Martelli}). Recall that $X(M)$ is the affine algebraic set consisting of representations $\pi_1(M)\ra PSL(2,\mc)$ up to the equivalence relation of having the same trace on each element of $\pi_1(M)$. Denote by $\tilde M$ the universal cover of $M$. Any point $w\in G(T,b)$  determines a {\it pseudo-developing map} $D_w\colon \tilde{M} \ra \mh^3$, unique up to post-composition with an isometry, which sends a lift $\tilde{\Delta}^i$ of the tetrahedron $\Delta^i$ to a hyperbolic ideal tetrahedron with shape parameters $(w_0^i,w_1^i,w_2^i)$. A pseudo-developing map $D_w$ defines a representation $\rho_w\colon \pi_1(M) \to PSL(2,\mc)$ by $D_w(\gamma.x) = \rho_w(\gamma)D_w(x)$ for all $\gamma\in \pi_1(M)$, $x\in \tilde{M}$. Different choices of developing maps $D_w$ yield conjugate representations $\rho_w$. The resulting holonomy map (denoting again by $\rho_w$ the character of a representation $\rho_w$)
\begin{equation}\label{defholmapSept24}\fonc{hol}{G(T,b)}{X(M)}{w}{\rho_w}
\end{equation} is regular, and generically $2:1$. More will be said about it in Section \ref{GhypN}. For the moment, let us note that in general $hol$ is not surjective (for instance, by the construction of pseudo-developing maps it is not hard to see that the image of $hol$ cannot contain any character of reducible representations). 
\smallskip

The Thurston gluing variety $G(T,b)$ and the map $hol$ have good properties when $T$ is a geometric triangulation, in the following sense.
\begin{defi}\label{defgeomtri}{\rm We say that $T$ is a {\it geometric triangulation} of $M$ when:
\begin{itemize}
\item either the edges of $T$ are isotopic to geodesics in the complete hyperbolic structure of $M$, and these geodesics triangulate $M$ into tetrahedra with non zero volume and disjoint interiors; 
\item or $T$ is obtained by subdividing the Epstein-Penner canonical polyhedral decomposition of $M$ (then some tetrahedra may be flat, {\it i.e.}, of zero volume).
\end{itemize}}
\end{defi}
In the former case we say that $T$ is a {\it positive} triangulation, as it can be isotoped to a gluing of positively oriented hyperbolic ideal tetrahedra corresponding to the $\Delta^i$, with classical shape parameters satisfying $\mathfrak{I}(w_{hyp}(E)^{*_E(\Delta)})> 0$ for every abstract edge $E$ of $T$. Such triangulations are produced, e.g., by the software program SnapPy \cite{CDGW}. In general, when $T$ is geometric there exists a point $w_{hyp}\in G(T,b)$ such that $$hol(w_{hyp}) = \rho_{hyp}, \ {\rm and\ } \mathfrak{I}(w_{hyp}(E)^{*_E(\Delta)})\geq 0 \ {\rm for\ every\ abstract\ edge\ }E \ {\rm of\ } T.$$ 

For a geometric triangulation $T$ the following facts hold true  (see \cite{NZ},  \cite[Chapter E.6 and Proposition 7.7]{BP}, \cite{PW} and \cite[Proposition 3.5-3.6]{PP},  \cite{Choi} and \cite[Proposition 15.3.4]{Martelli}):
\begin{itemize}
\item[(i)] ${\rm dim}_\mc(G(T,b))=p$, the number of cusps of $M$ (this is also the dimension of the geometric component $X_{hyp}(M)$ of $X(M)$, see Section \ref{GhypN});
\item[(ii)] there is a unique point $w_{hyp}$ as above, it is a smooth point of $G(T,b)$, and a neighborhood of $w_{hyp}$ parametrizes a space of (non complete) hyperbolic structures on $M$.
 \end{itemize} 

Now let $w:=(w^1,\ldots,w^n)\in  G(T,b)$, where $w^i:=(w_0^i,w_1^i,w_2^i)$ as usual. 
\begin{defi} {\rm We say that a tuple $d:=(d^1,\ldots,d^n)\in \mz^{3n}$ is a {\it system of (edge) colors} for $w$ if: 
\begin{itemize}
\item for every tetrahedron $\Delta^i$ of $T$, $i=1,\ldots,n$, we have 
\begin{equation}\label{tetcol2}
\sum_{k=0,1,2} (\Log(w_k^i) +\pi i d_k^i) = -*_b\! (\Delta)\pi i 
\end{equation}
\item for every edge $e$ of $T$ we have (with notations similar to \eqref{edgerel}):
\begin{equation}\label{edgecol}
\sum_{E\ra e} *_E(\Delta)(\Log(w(E)) +\pi i d(E)) =  -2\pi i.
\end{equation}
\end{itemize}
In such a situation we say that $d$ and $w$ are {\it compatible}. }
\end{defi}
The existence and the structure of the set of compatible pairs $(w,d)$ is discussed in Section \ref{LOGW}. By means of the formula \eqref{coldef} relating $d_k^i$, $w_k^i$ and $\bw_k^i$ for every $i$ and $k$, to any compatible pair $(w,d)$ we can associate a point $\bw:=(\bw^1,\ldots,\bw^n)\in G_N(T,b)$, where $\bw^i:=(\bw_0^i,\bw_1^i,\bw_2^i)$. We say that $(w,d)$ and $\bw$ are compatible.

We can also consider {\it systems of (edge) $N$-colors}, {\it i.e.}, tuples $e:=(e^1,\ldots,e^n)\in (\mz/N)^{3n}$, where $e^i=(e_0^i,e_1^i,e_2^i)$, satisfying the relations obtained from \eqref{tetcol2}-\eqref{edgecol} by replacing $d_k^i$ and $d(E)$ with $2e_k^i$ and $2e(E)$ and working {\rm mod}$(2\pi i N)$; clearly the pairs $(w,e)$ are in one-to-one correspondence with the points of $G_N(T,b)$. 

\begin{remark}\label{defflatcharge}{\rm The log-parameters in \eqref{tetcol} are intrinsic to Neumann's simplicial formulas (\cite{N}) of the Chern-Simons invariant of $PSL(2,\mc)$-characters. Indeed, these simplicial formulas are given by functions of the shape parameters $w=(w_k^i)$ and so-called {\it combinatorial flattenings} $f=(f_k^i)\in \mz^{3n}$, which are defined by the following relations, for every tetrahedron $\Delta^i$ and every edge $e$ of $T$ respectively:
\begin{equation}\label{rellogparoct25}
\sum_{k=0,1,2} (\Log(w_k^i) +\pi i f_k^i) = 0\ ,\ \sum_{E\ra e} *_E(\Delta)(\Log(w(E)) +\pi i f(E)) = 0.
\end{equation}
The colors in \eqref{tetcol} can be written
\begin{equation}\label{expdfc}
d_k^i=f_k^i- *_b (\Delta) c_k^i,
\end{equation}
where $c=(c_k^i)\in \mz^{3n}$ is a topological version of combinatorial flattenings, introduced in \cite{N0} and that we call a charge; by definition, it satisfies for every tetrahedron $\Delta^i$ and every edge $e$ of $T$ the equations} 
$$\sum_{k=0,1,2} c_k^i = 1\ ,\ \sum_{E\ra e} c(E) = 2.$$
\end{remark}
