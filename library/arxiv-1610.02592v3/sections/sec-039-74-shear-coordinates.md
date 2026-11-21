---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-039-74-shear-coordinates
section_title: "Shear coordinates"
section_number: 7.4
pages: 219-227
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.874
latex_coverage_ratio: 0.993
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
The Teichm\"uller space of a punctured surface may also be parametrized using ideal triangles instead of pairs-of-pants: this viewpoint is maybe a bit simpler, and generalises successfully to dimension three (via ideal tetrahedra). The coordinates that it produces are called \emph{shear coordinates}.\index{shear coordinates}


\subsection{Ideal triangulations}
In dimension two and three it is customary to relax the definition of \emph{triangulation}, originally restricted to simplicial complexes, see Section \ref{triangulations:subsection}. We prefer to define a triangulation in a looser sense, as a finite set of triangles glued together by pairing their edges. 

Let $\Delta_1,\ldots, \Delta_{2k}$ be an even number of identical copies of the standard oriented 2-simplex. A \emph{triangulation} $\calT$ is a partition of the $6k$ edges of the triangles into $3k$ pairs, and for each pair a simplicial isometry between the two edges. The triangulation is \emph{oriented} if the simplicial isometries are orientation-reversing. If we glue the triangles along the isometries we get a compact surface $S$: we always suppose that $S$ is connected and $\calT$ is oriented, hence $S = S_g$ for some $g\geqslant 0$.

The surface $S$ is triangulated with $2k$ triangles, $3k$ edges, and some $p$ vertices. Vertices, edges, and triangles form a cellularisation of $S$, but not necessarily a simplicial complex: for instance two or three vertices of the same triangle $\Delta_i$ can be identified to a single one along the process, as the following exercise shows.

\begin{ex}
Construct a triangulation of the torus with one vertex, three edges, and two triangles.
\end{ex}

Let $\Sigma$ be the non-compact surface obtained by removing the $p$ vertices of the triangulation $\calT$ from $S$: we say that $\calT$ is an \emph{ideal triangulation} for $\Sigma$. The surface $\Sigma$ is a \emph{punctured surface}, \emph{i.e.}~$\Sigma = S_{g,0,p}$ with $p\geqslant 1$.\index{ideal triangulation}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{triangulated_surface-BW}{triangulated_surface}}
\nota{The standard representation of $S_g$ by identifying the edges of a $4g$-gon has only one vertex; if we triangulate the $4g$-gon we get an ideal triangulation for $S_{g,0,1}$ (left). A move that modifies a triangulation by adding a new vertex (right).}
\label{triangulated_surface:fig}
\end{center}
\end{figure}

\begin{prop} We have $\chi(\Sigma) = -k <0$. Every punctured surface of negative Euler characteristic has an ideal triangulation.
\end{prop}
\begin{proof}
We have $\chi(\Sigma) = \chi(S) -p = p-3k+2k-p = -k$. An ideal triangulation for $S_{0,0,3}$ is constructed by attaching $\Delta_1$ and $\Delta_2$ via the obvious maps. An ideal triangulation for $S_{g,0,1}$ is constructed in Figure \ref{triangulated_surface:fig}-(left) for all $g\geqslant 1$. An ideal triangulation for $S_{g,0,p}$ with $\chi(S_{g,0,p})<0$ and $p\geqslant 2$ is obtained from one of these by increasing $p$ as in Figure \ref{triangulated_surface:fig}-(right).
\end{proof}


\subsection{Hyperbolic ideal triangulations}
Let $\calT$ be an oriented triangulation with triangles
$\Delta_1,\ldots, \Delta_{2k}$. We substitute every $\Delta_i$ with an ideal hyperbolic triangle (recall that it is unique up to isometry) and pair the edges with some orientation-reversing isometries. The resulting oriented punctured surface $\Sigma$ now inherits a hyperbolic structure of area $k\pi$, since an ideal triangle has area $\pi$. We call $\calT$ a \emph{hyperbolic ideal triangulation} for $\Sigma$.


\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{triangoli_ideali-BW}{triangoli_ideali}}
\nota{On an ideal triangle every edge has a unique perpendicular which ends at the opposite vertex. The base of this perpendicular is the \emph{midpoint} of the edge and the three perpendiculars intersect in a point called \emph{barycenter} (left). There is a unique configuration of three pairwise tangent horocycles centred at the ideal vertices, and their tangency points are the midpoints of the edges (right).}
\label{triangoli_ideali:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{shear-BW}{shear}}
\nota{The \emph{shear} is the signed distance $d$ between two midpoints after the gluing. By convention the sign is positive $d>0$ if the points are as shown here, that is an observer that arrives at the midpoint of an edge sees the other midpoint on its left: we need the orientation of $\calT$ here (left). We develop a triangulation around a puncture $v$: here $h=3$ (right).}
\label{shear:fig}
\end{center}
\end{figure}

The edges are infinite lines and the gluing isometry is not unique: indeed there is a 1-parameter family of isometries to choose from at every pair of edges, and the hyperbolic structure depends on that -- although the topology of $\Sigma$ does not. To encode this dependence, we note that every edge of an ideal triangle has a preferred \emph{midpoint} defined in Figure \ref{triangoli_ideali:fig}. The orientation-reversing isometry between two edges of two triangles is determined by the signed distance $d$ (called \emph{shear}) of their two midpoints as shown in Figure \ref{shear:fig}-(left). The hyperbolic structure on $\Sigma$ is determined by the \emph{shear coordinates} $d=(d_1, \ldots, d_{3k})$ of the $3k$ edges of the triangulation.


\subsection{Complete solutions}
The hyperbolic structure on $\Sigma$ may be incomplete! Recall that a hyperbolic surface is complete if and only if its universal cover is $\matH^2$, so we now look at the universal cover of $\Sigma$. 

\begin{figure}
\begin{center}
\includegraphics[width = 4cm] {\iftoggle{BW}{universale-BW}{universale}}
\nota{The universal covering of $\Sigma$ is isometric to the interior of a convex set delimited by some lines in $\matH^2$, which is the intersection of (possibly infinitely many) half-planes bounded by disjoint lines.}
\label{universal:fig}
\end{center}
\end{figure}

\begin{prop}
The universal cover $\tilde \Sigma$ of $\Sigma$ is isometric to
the interior of the intersection of some half-planes in $\matH^2$ with disjoint boundary lines (see Figure \ref{universal:fig}). The surface $\Sigma$ is complete if and only if $\tilde \Sigma \isom\matH^2$.
\end{prop}

\begin{proof}
Recall from Section \ref{non-complete:subsection} that there is a developing map $D\colon \tilde {\Sigma} \to \matH^2$. We prove that $D$ is injective. 

We can construct $D$ as follows: the hyperbolic ideal triangulation $\calT$ of $\Sigma$ lifts to a hyperbolic ideal triangulation $\tilde \calT$ of $\tilde{\Sigma}$ with infinitely many triangles. Send a triangle of $\tilde \calT$ to an arbitrary ideal triangle of $\matH^2$ and then develop the map $D$ by attaching subsequently all the triangles of $\tilde \calT$.  At each step the image of $D$ is an ideal polygon and we attach a new triangle to the exterior of some side of the polygon. Therefore at each step $D$ is injective and hence $D$ is globally injective.

Since $D$ is injective we identify $\tilde{\Sigma}$ with its open image in $\matH^2$. Pick a point $x\in\partial\tilde{\Sigma}$. Every neighbourhood of $x$ must intersect infinitely many triangles of $\tilde \calT$, hence there is a sequence of edges $e_i$ of $\tilde \calT$ such that $d(e_i,x)$ is monotone decreasing and tends to zero. Since the $e_i$ are disjoint, their endpoints in $\partial \matH^2$ are monotone and tend to two points, which determine a line $l$. We must have $d(l,x)=0$ and hence $x\in l$ and $l\subset \partial \tilde \Sigma$. 

We have discovered that $\partial \tilde \Sigma$ consists of disjoint lines. This proves that the closure of $\tilde\Sigma$ is the intersection of half-planes. A surface $\Sigma$ is complete if and only if $\tilde \Sigma$ is complete, and hence isometric to $\matH^2$.
\end{proof}

The hyperbolic structure on $\Sigma$ depends on the shearing coordinates $d\in \matR^{3k}$, and we now want to understand which values of $d$ produce a complete metric. An ideal vertex $v$ of the triangulation $\calT$ is adjacent to some $h$ triangles, which we denote by $\Delta_{1},\ldots, \Delta_{h}$ for simplicity although there might be repetitions, and to $h$ edges with some shearing coordinates that we also indicate by $d_1,\ldots, d_h$ for simplicity. The vertex $v$ is a puncture of $\Sigma$ and we let $N(v)$ be a small topological punctured closed disc around $v$.

\begin{prop}
The punctured disc $N(v)$ is complete if and only if $d_1 + \ldots + d_h = 0$.
\end{prop}
\begin{proof}
We construct a portion of the developing map $D\colon \tilde \Sigma \to \matH^2$ as follows: we use the half-plane model and send $\Delta_1$ to $\matH^2$ with $v=\infty$ as in Figure \ref{shear:fig}-(right), then we develop the triangulation horizontally. In the picture we have $h=3$ so we reproduce $\Delta_1, \Delta_2, \Delta_3$ and then another copy $\Delta_1'$ of $\Delta_1$. Let $\varphi\in\PSLR$ be the holonomy isometry that sends $\Delta_1$ to $\Delta_1'$.

If $d_1+\ldots + d_h=0$ the midpoints of $\Delta_1$ and $\Delta_1'$ are at the same height as in Figure \ref{shear:fig}-(right) and therefore $\varphi$ is a parabolic map $\varphi\colon z \mapsto z+b$ for some $b\in \matR$. Therefore $N(v)$ is a truncation of the cusp $\matH^2/_{\langle \varphi\rangle }$, which is complete.

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{shear2-BW}{shear2}}
\nota{When $d_1+\ldots + d_h \neq 0$, the isometry $\varphi$ sending $\Delta_1$ to $\Delta_1'$ is hyperbolic, with some axis $l$ which (up to translations) has endpoints $0$ and $\infty$. Hence $\varphi(z)=e^d z$ and the triangulation develops towards $l$ as shown here.}
\label{shear2:fig}
\end{center}
\end{figure}

If $d_1+\ldots + d_h \neq 0$ the midpoints of $\Delta_1$ and $\Delta_1'$ are at different heights and therefore $\varphi$ is not parabolic. Since $\infty \in \Fix(\varphi)$, the isometry $\varphi$ is a hyperbolic transformation having some other fixed point in $\matR$. Up to translating everything we may suppose that $\Fix(\varphi)=\{0,\infty\}$, hence the axis $l$ of $\varphi$ is the vertical coordinate axis, and $\varphi(z) =  e^d z$ with $d = d_1+\ldots + d_h$. The map $D$ develops towards $l$ as shown in Figure \ref{shear2:fig}: we get $l\subset \partial \tilde\Sigma$, so $\tilde\Sigma \neq\matH^2$ is not complete. 
\end{proof}
 
Summing up, we have a \emph{completeness equation} of type $d_{i_1}+\ldots + d_{i_h}=0$ for each of the $p$ ideal vertices of the triangulation.

\begin{cor}
The hyperbolic structure on $\Sigma$ is complete if and only if $d$ satisfies the $p$ completeness equations.
\end{cor}
\begin{proof}
Let $N(v)$ be a small punctured closed disc at $v$ for every ideal vertex $v$. The closure of $\Sigma \setminus \cup_v N(v)$ is compact. Therefore $\Sigma$ is complete if and only if each $N(v)$ is.
\end{proof} 


\subsection{Shear coordinates for Teichm\"uller space}
The solution space of the completeness equations is some linear subspace $V \subset \matR^{3k}$ of dimension at least $3k-p = -3\chi(\Sigma)-p$. Note that this is precisely the dimension of $\Teich(\Sigma)$, see Section \ref{Teich:finite:type:subsection}. We have constructed a map
$${\rm sh}\colon V \longrightarrow \Teich(\Sigma).$$
We will prove below that $\sh$ is a homeomorphism and hence $\dim V = 3k-p$. We will use the following.

\begin{prop} \label{straightens:prop}
Let $\Sigma$ be a complete hyperbolic punctured surface.
Every ideal triangulation is isotopic to a unique hyperbolic ideal triangulation. 
\end{prop}
\begin{proof}
We describe a procedure that \emph{straightens} every ideal triangulation $\calT$ of $\Sigma = \matH^2/_\Gamma$ to a hyperbolic one. 

Truncate the cusps of $\Sigma$ to get a compact sub-surface. The ideal triangulation $\calT$ is now truncated to a decomposition into hexagons, each with three boundary and three interior edges. We lift the truncated cusps and the hexagons to $\matH^2$. Truncated cusps lift to horoballs, bounded by horocycles, and hexagons lift to hexagons (the hexagons are not geodesic, only smooth). 

An interior edge of a hexagon in $\matH^2$ cannot have both its endpoints in the same horocycle, since it would form a bigon with it, and a bigon does not decompose into hexagons (by a Euler characteristic argument). Therefore every interior edge connects two distinct horocycles, centred at two distinct points of $\partial \matH^2$. Replace this edge with the geodesic line connecting these two ideal points.

If we do this at every interior edge we get a $\Gamma$-invariant hyperbolic ideal triangulation of $\matH^2$, which projects to a hyperbolic ideal triangulation for $\Sigma$ isotopic to $\calT$.  
\end{proof}

We can now parametrize $\Teich(\Sigma)$.
 
\begin{cor} The map $\sh$ is a bijection.
\end{cor}
\begin{proof}
Proposition \ref{straightens:prop} shows that in every metric the initial triangulation $\calT$ straightens to an ideal hyperbolic one and is hence realised by some $d$, so $\sh$ is surjective. Moreover the straightened triangulation is unique and the parameters $d_i$ are obtained intrinsically from it, so $\sh$ is also injective.
\end{proof}


\subsection{Incomplete metrics} \label{incomplete:metrics:subsection}
The shear coordinates $d$ may define an incomplete metric on $\Sigma$, and we now determine its metric completion $\overline \Sigma$.

Recall that every ideal vertex $v$ has a \emph{total shear} $d_v = d_{i_1}+\ldots +d_{i_h}$ which is zero precisely when $\Sigma$ is complete near $v$. 

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{shear3-BW}{shear3}}
\nota{Let $s$ be a Euclidean line at hyperbolic distance $R$ from $l$. If $R$ is sufficiently small, the line $s$ does not intersect the lower edges of $\Delta_1, \Delta_2, \Delta_3$. Let $S$ be the region lying above $s$.}
\label{shear3:fig}
\end{center}
\end{figure}


\begin{prop}  \label{completion:surface:prop}
The metric completion $\overline\Sigma$ is a hyperbolic surface with geodesic boundary, whose boundary lengths are the absolute values of the total shears of the vertices. 
\end{prop}
\begin{proof}
Let $N(v)$ be a small closed punctured disc around $v$.
If $d_v=0$ we already know that $N(v)$ is a truncated cusp. If $d_v\neq 0$ we develop $N(v)$ in $\matH^2$ as in Figure \ref{shear3:fig}. The hyperbolic transformation is $\varphi(z) = e^{d_v} z$ and the points at distance $R$ from $l$ form a Euclidean line $s$ starting from $0$. Pick $R$ small so that $s$ does not intersect the lower edges of $\Delta_1,\ldots,\Delta_h$. Since $s$ is $\varphi$-invariant, it is contained in the union of all the developed triangles of Figure \ref{shear3:fig} and hence in $\tilde\Sigma$.

The line $s$ projects to a (non-geodesic) circle in $\Sigma$ around $v$, and we can suppose that $\partial N(v)$ is that circle. We have $N(v) = S/_\gamma$ where $S\subset H^2$ is the region lying above $s$. The completion $\overline S $ equals $S\cup l$ and therefore $\overline{N(v)} = \overline S/_\gamma$ is an annulus with two boundary components: the original non-geodesic $\partial N(v)$ and a new geodesic $l/_\gamma$, a curve of length $|d_v|$.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{shear_completion2-BW}{shear_completion}}
\nota{Near an ideal vertex $v$, horocycles (in \iftoggle{BW}{black}{blue}) and edges of the triangulation (in \iftoggle{BW}{grey}{red}) are mutually orthogonal. They behave much differently in presence of a cusp (left) or of a geodesic boundary (right): in a cusp, horocycles form parallel circles and edges point toward the cusp; near a geodesic boundary, the horocycle point orthogonally toward the boundary and the edges spin and wind around it indefinitely.}
\label{shear_completion:fig}
\end{center}
\end{figure}

If $d_v\neq 0$, the edges of the triangulation pointing towards $v$ spin around the geodesic boundary as shown in Figure \ref{shear_completion:fig}-(right). The spinning direction induces an orientation on each component of $\partial \overline \Sigma$, which depends on the sign of $d_v$. 

Summing up, every shear coordinate $d = (d_1,\ldots, d_{3k})\in \matR^{3k}$ determines a hyperbolic surface $\overline{\Sigma}$ with some $p'$ cusps and $b$ oriented geodesic boundary, where $b+p'=p$ is the number of vertices of the ideal triangulation. The surface $\overline \Sigma$ is diffeomorphic to $S_{g,b,p'}$. Let $\Teich^{\rm or}(S_{g,b,p'})$ denote the Teichm\"uller space of the surface $S_{g,b,p'}$ equipped with an orientation of the $b$ boundary components: of course this is just $2^b$ copies of $\Teich(S_{g,b,p'})$.

\begin{prop} \label{straighten:incomplete:prop}
The shear coordinates induce a bijection
$$\matR^{3k} \longleftrightarrow \bigsqcup_{b+p' = p} \Teich^{\rm or}(S_{g,b,p'}).$$
\end{prop}
\begin{proof}
The map sends $d\in\matR^{3k}$ to the complete hyperbolic $\overline \Sigma$, and we now exhibit an inverse. Let $\overline\Sigma$ be a surface of finite type with a hyperbolic structure with $p'$ cusps and $b$ oriented geodesic boundary components, and $\Sigma = \interior{\overline\Sigma}$. We may straighten any ideal triangulation $\calT$ of $\Sigma$ similarly as we did in Proposition \ref{straightens:prop}, with the only difference that horocycles are replaced by \emph{oriented} geodesic lines as lifts of oriented geodesic boundary components; in the construction, we use the final endpoint of the oriented line instead of the ideal point of the horocycle. We get an ideal triangulation of $\Sigma$ whose completion is $\overline \Sigma$.
\end{proof}

For instance, $\matR^3$ parametrizes altogether all the hyperbolic metrics on the pair of pants, where each boundary component becomes either an oriented geodesic or ``degenerates'' to a cusp.


\subsection{References}
Most of the material presented here is standard and can be found in many books, starting from Thurston's notes \cite{Th}. The main reference is Farb -- Margalit \cite{FM}, which also contains the proof of Proposition \ref{strettamente:convessa:prop}, that appeared originally in a paper of Bestvina, Bromberg, Fujiwara, and Souto \cite{BBFS}. The proof of the Collar Lemma is taken from Hubbard \cite{Hu}.



\chapter{Surface diffeomorphisms} \label{automorfismi:chapter} \label{automorphisms:chapter}

We describe in this chapter an analogy between the hyperbolic space $\matH^n$ and the Teichm\"uller space $\Teich(S_g)$ of a closed orientable surface $S_g$ of genus $g\geqslant 1$. The theory, originated from Thurston in the late 1970s, provides a beautiful and powerful framework for the analysis of the geometric and dynamical properties of the surfaces $S_g$ and of their mapping class group $\MCG(S_g)$. 

Here is a quick sketch of this analogy. We have already seen that $\matH^n$ compactifies to a closed disc $\overline{\matH^n}$, that $\Iso(\matH^n)$ acts on it, that by Brouwer's theorem every non-trivial isometry $\varphi$ has a fixed point in $\overline{\matH^n}$, and we have called $\varphi$ \emph{elliptic}, \emph{parabolic}, or \emph{hyperbolic} according to the position of its fixed points.

We construct in this chapter a similar compactification of the open ball $\Teich(S_g)$ to a closed disc. The action of the mapping class group $\MCG(S_g)$ extends to this closed disc, and by Brouwer's theorem every non-trivial element $\varphi$ of $\MCG(S_g)$ has a fixed point there. According to the position of the fixed points of $\varphi$, we say that $\varphi$ is \emph{finite order}, \emph{reducible}, or \emph{pseudo-Anosov}. 

If $\varphi$ is an isometry for some hyperbolic structure of $S_g$, it belongs to the first type. Dehn twists belong to the second. The pseudo-Anosov maps are both the most mysterious and the most important, and for their study we need to introduce a wealth of beautiful new technology: \emph{geodesic currents}, \emph{laminations}, and \emph{train tracks}.
