---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-030-61-topological-classification
section_title: "Topological classification"
section_number: 6.1
pages: 161-165
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.784
latex_coverage_ratio: 0.927
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
A surface can be topologically quite complicated: think for instance of $\matR^2$ with a Cantor set removed. We decide to restrict our investigation to the surfaces \emph{of finite type}, i.e.~obtained from a closed one by removing points and/or open discs: these include all the compact surfaces with or without boundary.
We introduce here these surfaces and classify them up to diffeomorphism.

We manipulate surfaces using various cut-and-paste tools: boundary gluings, removal of discs or points, handle decompositions, connected sums. See Section \ref{differential:topology:section} to refresh these notions.


\subsection{Gluing surfaces}
A simple way to construct a surface is by gluing simpler surfaces along their boundaries. We show here that the glued surface depends only on the orientation classes of the gluing maps.

Two self-diffeomorphisms of $S^1$ are \emph{co-oriented} if they both preserve or both invert the orientation of $S^1$.
\begin{lemma} \label{diffeo:isotopi:lemma}
Two co-oriented self-diffeomorphisms of $S^1$ are isotopic.
\end{lemma}
\begin{proof}
Let $f_0, f_1\colon S^1 \to S^1$ be two co-oriented self-diffeomorphisms. Their lifts $\tilde f_0, \tilde f_1\colon \matR\to\matR$ are periodic and monotone, hence $\tilde f_t = (1-t)\tilde f_0 + t\tilde f_1$ also is and descends to an isotopy $f_t$ connecting $f_0$ and $f_1$.
\end{proof}

\begin{cor} \label{not:depend:cor}
If we glue two oriented surfaces along their boundaries via orientation-reversing diffeomorphisms, the resulting oriented surface does not depend on the diffeomorphisms chosen.
\end{cor}
\begin{proof}
All the orientation-reversing gluing maps are isotopic by Lemma \ref{diffeo:isotopi:lemma}, and isotopic gluing maps produce diffeomorphic manifolds, as stated in Proposition \ref{depend:diffeo:prop}.
\end{proof}

In a non-oriented context, we have two possible maps for every glued boundary component.

\begin{cor} \label{sphere:cor}
If we glue two discs we get a sphere.
\end{cor}
\begin{proof}
The two discs are copies of $D^2\subset \matC$ and are glued along a diffeomorphism $\varphi\colon S^1\to S^1$. Up to mirroring one disc we may suppose that $\varphi$ is orientation-reversing, and by Corollary \ref{not:depend:cor} we may suppose that $\varphi(z) = \bar z$. The resulting surface is diffeomorphic to a sphere (exercise).
\end{proof}

\begin{warning}
In dimension $n\geqslant 7$, by gluing two discs we may get a manifold homeomorphic but \emph{not} diffeomorphic to a sphere! See Section \ref{self:disc:subsection}.
\end{warning}



\subsection{Classification of surfaces}
In Section \ref{sum:subsection} we introduced the connected sum, a two-steps operation which consists of first removing balls and then gluing the new sphere boundaries. Let $S_g$ be the connected sum 

\begin{figure}
\begin{center}
\includegraphics[width = 3 cm] {\iftoggle{BW}{Sphere_with_three_handles-BW}{500px-Sphere_with_three_handles}}
\quad \includegraphics[width = 3 cm] {\iftoggle{BW}{Triple_torus_array-BW}{500px-Triple_torus_array}}
\quad \includegraphics[width = 3 cm] {\iftoggle{BW}{Triple_torus_illustration-BW}{500px-Triple_torus_illustration}}
\nota{A surface of genus $3$ may be represented in various ways.}
\label{handles_surface:fig}
\end{center}
\end{figure}

$$S_g = \underbrace{T \# \ldots \# T}_g$$ 
of $g$ tori $T=S^1\times S^1$. By convention $S_0 = S^2$ is the sphere and $S_1=T$ is the torus. The number $g$ is the \emph{genus} of the closed surface $S_g$. The surface $S_g$ may be represented in $\matR^3$ in various ways, see Figure \ref{handles_surface:fig}.\index{surface!genus of a surface}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{classification-BW}{classification}}
\nota{The 0-handle and $k$ 1-handles form a subsurface $S'\subset S$ with connected boundary, to which the 2-handle is attached (left). A 0-handle and two linked 1-handles (centre). If we attach a 2-handle to the centre figure we get a handle decomposition of the torus (right).}
\label{classification:fig}
\end{center}
\end{figure}

\begin{prop}
We have $\chi(S_g) = 2-2g$.
\end{prop}
\begin{proof}
Let $S,S'$ be surfaces and $D\subset \interior S, D'\subset \interior{S'}$ be discs. Then
$$\chi(S\# S') = \chi(S\setminus D) + \chi(S' \setminus D') - \chi(S^1) = \chi (S) + \chi(S') - 2.$$
Therefore $\chi(S_g) =2-2g$ by induction on $g$.
\end{proof}

\begin{teo}[Classification of surfaces] Every closed, connected, orientable surface is diffeomorphic to $S_g$ for some $g\geqslant 0$.\index{surface!classification of surfaces}
\end{teo}
\begin{proof}
Being a closed manifold, every closed orientable surface $S$ has a handle decomposition. By Proposition \ref{0:handle:prop} it has one with one 0-handle, a certain number $k$ of 1-handles, and one 2-handle. We get $\chi(S) = 2-k$. We prove by induction on $k$ that $k=2g$ is even and $S$ is diffeomorphic to $S_g$.

If $k=0$ then $S$ is obtained by gluing two discs (the 0- and 2-handle) and is hence a sphere by Corollary \ref{sphere:cor}.

Suppose $k>0$. The 0-handle is a disc and the 1-handles are rectangles attached to its boundary as in Figure \ref{classification:fig}-(left). Note that since $S$ is orientable every rectangle is attached without a twist, otherwise it would create a M\"obius strip. The 0- and 1-handles altogether form a compact surface $S'\subset S$ with only one boundary component, to which the 2-handle is attached.

Since $\partial S'$ is connected, every rectangle is linked to some other rectangle as in Figure \ref{classification:fig}-(centre). A pair of linked rectangles form a sub-subsurface $S''\subset S'\subset S$ as in Figure \ref{classification:fig}-(centre) with connected boundary. If we cut $S$ along the curve $\partial S''$ and then cap off with two discs we perform the inverse of a connected sum. 

Therefore $S = S_1\# S_2$, where $S_1$ is $S''$ with a disc attached, \emph{i.e.}~a torus  as Figure \ref{classification:fig}-(right) shows. The surface $S_2$ decomposes into a 0-handle, $k-2$ 1-handles, and one 2-handle. We conclude by induction on $k$.
\end{proof}


\subsection{Homology} \label{homolgy:surface:subsection}
The homology of $S_g$ is easily calculated.
\begin{prop}
We have
$$H_0(S_g,\matZ) = \matZ, \quad H_1(S_g,\matZ) = \matZ^{2g}, \quad H_2(S_g,\matZ) = \matZ.$$
\end{prop}
\begin{proof}
Since $S_g$ is closed, connected, and orientable, we have $H_0(S_g) = H_2(S_g) = \matZ$. Since $\chi(S_g) = 2-2g$, the group $H_1(S_g)$ has rank $2g$. By Poincar\'e duality $H_1(S_g) = H^1(S_g) = \Hom(\pi_1(S_g),\matZ)$ has no torsion.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 10cm] {\iftoggle{BW}{surface_homology-BW}{surface_homology}}
\nota{These 6 oriented curves represent a symplectic basis for $H_1(S_3,\matZ) = \matZ^6$.}
\label{surface_homology:fig}
\end{center}
\end{figure}

Recall from Section \ref{intersection:subsection} that by fixing an orientation for $S_g$ we get a symplectic intersection form $\omega$ on $H_1(S_g,\matZ)$. 
A basis for $H_1(S_g, \matZ)$ is \emph{symplectic} if $\omega = \matr 0 {I_g} {-I_g} 0$ with respect to this basis: an example is in Figure \ref{surface_homology:fig}.\index{symplectic basis} 

The \emph{algebraic intersection} of two closed curves is the intersection form of their classes in $H_1(S_g, \matZ)$; if the curves are transverse, this is just the algebraic sum of their intersections, where each intersection counts as $\pm 1$ according to the local orientations.\index{algebraic intersection!algebraic intersection of curves}


\subsection{Surfaces of finite type}
We extend our investigation to a larger interesting class of surfaces.\index{surface!surface of finite type} 

\begin{figure}
\begin{center}
\includegraphics[width = 6cm] {tipo_finito.pdf}
\nota{The finite type surface $S_{g,b,p}$.}
\label{tipo_finito:fig}
\end{center}
\end{figure}

\begin{defn}
Let $g,b,p\geqslant 0$ be three natural numbers. The \emph{surface of finite type} $S_{g,b,p}$ is the surface obtained from $S_g$ by removing the interior of $b$ disjoint discs and $p$ points. 
\end{defn}
See Figure \ref{tipo_finito:fig}. We say that $S_{g,b,p}$ has genus $g$, has $b$ boundary components, and $p$ punctures. Its Euler characteristic is
$$\chi(S_{g,b,p}) = 2-2g-b-p.$$

We also use the notation $S_{g,b}$ to indicate $S_{g,b,0}$.

\begin{prop}
Every compact connected orientable surface with boundary is diffeomorphic to $S_{g,b}$ for some $g,b\geqslant 0$.
\end{prop}
\begin{proof}
Let $S$ be a compact orientable surface with some $b$ boundary components.
If we glue $b$ discs to $\partial S$ we get a closed orientable surface, hence diffeomorphic to $S_g$ for some $g\geqslant 0$. The original $S$ is obtained from $S_g$ by removing the interiors of $b$ disjoint open discs.
\end{proof}

The compact connected orientable surfaces with $\chi>0$ are $S^2=S_0$ and $D^2=S_{0,1}$, those with $\chi=0$ are the annulus $A=S_{0,2}$ and the torus $T=S_1$.

\begin{cor}[Smooth Jordan curve Theorem] \label{Jordan:cor}
Every smooth simple closed curve $\gamma \subset \matR^2$ bounds a disc.\index{smooth Jordan curve theorem}
\end{cor}
\begin{proof}
Consider the curve $\gamma$ inside $S^2 = \matR^2\cup\{\infty\}$. By cutting $S^2$ along $\gamma$ we get one or two compact orientable surfaces with non-empty boundary and with $\chi=2$ in total. The only possibility is that we get two discs.
\end{proof}


\subsection{Triangulations} \label{surface:triangulations:subsection}
Like every honest smooth compact manifold, compact surfaces admit smooth triangulations, see Section \ref{triangulations:subsection}. Conversely, we may use simplicial complexes to construct smooth surfaces combinatorially.

Let $X$ be a two-dimensional pure simplicial complex where every edge is incident to two faces, and the link of every vertex is a circle.

\begin{prop}
The complex $X$ is the smooth triangulation of a closed surface $S$, unique up to diffeomorphism.
\end{prop}
\begin{proof}
By dualising $X$ we get a handle decomposition: triangles, edges, and vertices transform into 0-, 1-, and 2-handles, and we get a smooth surface $S$ triangulated by $X$. The way the handles are attached is determined up to isotopy, therefore $S$ is determined up to diffeomorphism.
\end{proof}

\begin{warning}
It is worth noting that this procedure (getting a unique smooth structure from a simplicial complex) does not work in all dimensions (here we used implicitly Lemma \ref{diffeo:isotopi:lemma}).
\end{warning}
