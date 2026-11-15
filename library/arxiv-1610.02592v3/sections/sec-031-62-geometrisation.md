---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-031-62-geometrisation
section_title: "Geometrisation"
section_number: 6.2
pages: 165-176
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.931
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{surface:geometrisation:section}
We now prove that every surface $S_{g,b,p}$ of finite type can be \emph{geometrised}, that is it may be equipped with a hyperbolic, flat, or elliptic metric. The metric type is prescribed by the sign of the Euler characteristic of the surface.


\subsection{Hyperbolic pair-of-pants} \label{pantaloni:subsection}
The sphere has of course an elliptic structure, and the torus has many flat structures, see Section \ref{piatte:subsection}. We now construct hyperbolic structures on all the surfaces $S_g$ of genus $g\geqslant 2$, and more generally on all the surfaces $S_{g,b,p}$ of negative Euler characteristic.
We start with a simple block, the \emph{pair-of-pants} $S_{0,3}$, with Euler characteristic $-1$.\index{pair-of-pants}

\begin{prop} \label{pantaloni:prop}
Given three real numbers $a,b,c\geqslant 0$ there is (up to isometries) a unique complete finite-volume hyperbolic pair-of-pants with geodesic boundary, with boundary curves of length $a$, $b$, and $c$.
\end{prop}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{pantalone_degenere-BW}{pantalone_degenere}}
\nota{A pair-of-pants, an annulus with one puncture, a disc with two punctures, and a thrice-punctured sphere. The last three surfaces may be considered as some degenerated hyperbolic pairs-of-pants where one or more boundary lengths $a,b$, or $c$ are zero, and we get cusps instead of geodesic boundary components there.}
\label{pantalone_degenere:fig}
\end{center}
\end{figure}

When some length in $a,b,c$ is zero, we mean that the geodesic boundary is actually a cusp (recall Section \ref{finite-volume:subsection}) and hence the surface is topologically a punctured annulus $S_{0,2,1}$, a twice punctured disc $S_{0,1,2}$, or a thrice-punctured sphere $S_{0,0,3}$: see Figure \ref{pantalone_degenere:fig}. 

To prove this proposition we construct some right-angled hexagons in $\matH^2$ as in Figure \ref{esagono:fig}-(left). Three \emph{alternate sides} on a hexagon are three pairwise non-incident sides, like the $a,b,c$ shown in the figure. A \emph{degenerate} hexagon is one where the length of some alternate sides is zero as in Figure \ref{esagoni_generalizzati:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 11cm] {\iftoggle{BW}{esagono-BW}{esagono}}
\nota{A right-angled hexagon with alternate sides of length $a$, $b$ and $c$ (left) and its construction (right), which goes as follows: take a line $l$ with two arbitrary points $A$ and $B$ in it  (bottom black). Draw the perpendiculars from $A$ and $B$ (\iftoggle{BW}{grey}{red}). At distances $a$ and $b$ we find two points $A'$ and $B'$ and we draw again two perpendiculars (black) $r$ and $s$, with some points at infinity $P$ and $Q$. 
Draw the (unique) perpendiculars to $l$ pointing to $P$ and $Q$ (\iftoggle{BW}{dark grey}{blue}): they intersect $l$ in two points $T$ and $U$. Note that $AT$ and $UB$ have some fixed length depending only on $a$ and $b$. We can vary the parameter $x=TU$: if $x>0$ the lines $r$ and $s$ are ultra-parallel and there is a unique segment orthogonal to both of some length $f(x)$.} 
\label{esagono:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{esagoni_generalizzati-BW}{esagoni_generalizzati}}
\nota{A right-angled hexagon with parameters $a,b,c\geqslant 0$ degenerates to a pentagon, quadrilateral, or triangle with ideal vertices if one, two, or three parameters are zero.}
\label{esagoni_generalizzati:fig}
\end{center}
\end{figure}

\begin{lemma} \label{esagono:lemma}
Given three real numbers $a,b,c\geqslant0$ there exists (up to isometries) a unique (possibly degenerate) hyperbolic right-angled hexagon with three alternate sides of length $a$, $b$, and $c$.
\end{lemma}
\begin{proof}
We first suppose $a,b>0$. The construction of the hexagon is depicted in Figure \ref{esagono:fig}-(right). If $x=0$ the \iftoggle{BW}{dark grey}{blue} lines coincide, hence $P=Q$ and $f(0)=0$. The function $f\colon [0,+\infty) \to [0,+\infty)$ is continuous, strictly monotonic, and with $\lim_{x\to \infty} f(x) = \infty$: therefore there is precisely one $x$ such that $f(x)=c$. 

If exactly two parameters are zero, say $a=b=0$, a simpler construction works: take a segment of length $c$ as in Figure \ref{esagoni_generalizzati:fig}-(centre), draw the perpendiculars at their endpoints, and a line connecting the endpoints of these. 

If $a=b=c=0$, pick any ideal triangle. Ideal triangles are indeed unique up to isometry: use the half-space model and recall that $\PSLR$ acts transitively on the ordered triples of points in $\partial \matH^2$.
\end{proof}
The most degenerate case is so important that we single it out.
\begin{cor}
All the ideal triangles in $\matH^2$ are isometric.
\end{cor}


\begin{figure}
\begin{center}
\includegraphics[width = 10cm] {\iftoggle{BW}{pantalone-BW}{pantalone}}
\nota{By gluing two identical right-angled hexagons along their black sides we get a hyperbolic pair-of-pants with geodesic boundary.}
\label{pantalone:fig}
\end{center}
\end{figure}

By gluing two identical (possibly degenerate) hexagons along alternate sides as in Figure \ref{pantalone:fig} we construct a (possibly degenerate) hyperbolic pair-of-pants whose geodesic boundary consists of three simple closed geodesics of length $2a$, $2b$, and $2c$. 

\begin{proof}[Proof of Proposition \ref{pantaloni:prop}]
We have proved the existence of a geodesic pairs-of-pants with any parameters $a,b,c\geqslant 0$, and we now turn to its uniqueness. Let $P$ be a pair-of-pants with geodesic boundary curves $C_1, C_2, C_3$ of length $a, b, c>0$.

Since $P, C_1$, and $C_2$ are compact, there are points $x_1\in C_1$ and $x_2 \in C_2$ at minimum distance $d=d(x_1,x_2)$, connected by some curve $\gamma_3$ of length $d$. The curve is a simple geodesic orthogonal to both $C_1$ and $C_2$: if not, some other curve connecting $x_1$ and $x_2$ would be shorter. We construct analogously two orthogeodesics $\gamma_1$ and $\gamma_2$ connecting $C_2$ to $C_3$ and $C_3$ to $C_1$ having minimal length.

The fact that $\gamma_1,\gamma_2,\gamma_3$ have minimal length easily implies that they are disjoint (if they intersect, we find shorter curves). The three orthogeodesics subdivide $P$ into two hexagons, with alternate sides of length $L(\gamma_1)$, $L(\gamma_2)$, and $L(\gamma_3)$: by Lemma \ref{esagono:lemma} the two hexagons are isometric, and hence the three other alternating sides also have the same length $\frac a2, \frac b2$, and $\frac c2$. Hexagons are unique up to isometry and hence the original pair-of-pants also are.

We can extend the argument to the more general case $2a, 2b, 2c \geqslant 0$ as follows. If $a=0$, a neighbourhood of the puncture is a cusp, and we truncate it at some small horocycle $C_1$ (we do the same if $b=0$ or $c=0$). After these truncations we get a compact pair-of-pants (whose boundary is \emph{not} geodesic at the horocycles) and decompose it into two hexagons as above. The resulting curve $\gamma_3$ is orthogonal to the horocycle $C_1$, hence it extends to a half-line pointing towards the puncture. The curves $\gamma_1, \gamma_2, \gamma_3$ decompose the surface into degenerate hexagons.
\end{proof}


\subsection{Hyperbolic surfaces} \label{hyperbolic:surfaces:subsection}
The pairs-of-pants can be used as building blocks to construct topologically all finite type surfaces with $\chi<0$.

\begin{figure}
\begin{center}
\includegraphics[width = 8cm] {\iftoggle{BW}{surface-BW}{surface}}
\nota{Every surface of finite type with $\chi<0$ decomposes into pair-of-pants. We show here a decomposition of $S_3$.}
\label{surface:fig}
\end{center}
\end{figure}

\begin{prop} \label{decompone:pantaloni:prop}
If $\chi (S_{g,b,p}) <0$ then $S_{g,b,p}$ decomposes topologically into $-\chi(S_{g,b,p})$ (possibly degenerate) pairs-of-pants.
\end{prop}
\begin{proof}
If $b+p=0$ then $g\geqslant 2$ and the surface decomposes easily in many ways, see for instance Figure \ref{surface:fig}. If $b+p>0$ and $\chi < -1$, a decomposition for $S_{g,b,p}$ may be obtained from one of $S_{g,b-1,p}$ or $S_{g,b,p-1}$ by inserting one more (possibly degenerate) pair-of-pants. If $\chi=-1$ the surface is either a pair-of-pants, or a torus with a puncture or boundary component, which is in turn obtained by glueing two boundary components of a pair-of-pants.
\end{proof}

We can use this building block to construct hyperbolic structures.

\begin{cor} \label{ammette:cor}
If $\chi(S_{g,b,p})<0$ then $S_{g,b,p}$ admits a complete hyperbolic metric with $b$ geodesic boundary components of arbitrary length.
\end{cor}
\begin{proof}
Decompose $S_{g,b,p}$ in pair-of-pants, assign an arbitrary length to all the closed curves of the decomposition (the 6 \iftoggle{BW}{grey}{red} curves shown in Figure \ref{surface:fig}) and give each pair-of-pants the hyperbolic metric determined by the three assigned boundary lengths. Everything glues to a complete hyperbolic metric for $S_{g,b,p}$ thanks to Proposition \ref{geodesic:glue:prop}.
\end{proof}

Can we geometrise the few orientable surfaces with $\chi \geqslant 0$? Yes, but since there are no cusps in the elliptic and flat geometries we do not consider surfaces with punctures. The compact orientable surfaces with $\chi >0$ are the sphere and the disc, and they all have an elliptic metric with geodesic boundary (represent the disc as a hemisphere). Those with $\chi = 0$ are the torus and the annulus, and they admit flat metrics with geodesic boundary.


\subsection{Non-orientable surfaces}
The classification of all the finite-type non-orientable surfaces is also simple. Let $S^{\rm no}_g$ be the connected sum
$$S_g^{\rm no} = \underbrace{\matRP^2 \# \ldots \# \matRP^2}_g$$ 
of $g\geqslant 1$ copies of the projective plane $\matRP^2$.

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{Klein_bottle-BW}{Klein_bottle}}
\nota{The Klein bottle immersed in $\matR^3$.}
\label{Klein_bottle:fig}
\end{center}
\end{figure}

\begin{prop}
We have $\chi(S_g^{\rm no}) = 2-g$. The surface $S_2^{\rm no}$ is diffeomorphic to the Klein bottle $K$ shown in Figure \ref{Klein_bottle:fig}. We have
$$S_g \#\matRP^2 \isom S^{\rm no}_{2g+1}.$$
\end{prop}
\begin{proof}
The formula for $\chi$ follows from $\chi(\matRP^2)=1$. The Klein bottle $K$ may be cut along a closed curve into two M\"obius strips, and $\matRP^2$ minus an open disc is a M\"obius strip too, hence $\matRP^2\#\matRP^2 = K$. The latter equality is a consequence of $T\#\matRP^2 \isom K \# \matRP^2$ which is left as an exercise.
\end{proof}

\begin{prop}
Every closed, connected, non-orientable surface is diffeomorphic to $S_g^{\rm no}$ for some $g\geqslant 1$.
\end{prop}
\begin{proof}
Pick a handle decomposition of the surface $S$. Since it is non-orientable, at least one 1-handle is twisted and forms a M\"bius strip. We have proved that $S$ contains a M\"obius strip, and we now remove it and substitute it with a disc to get a new surface $S'$. We have $S=S'\#\matRP^2$ and we conclude by induction on $-\chi(S')$.
\end{proof}

We may also denote by $S^{\rm no}_{g,b,p}$ the surface obtained from $S^{\rm no}_g$ by removing the interiors of $b$ discs and $p$ points.

\begin{ex}
If $\chi(S^{\rm no}_{g,b,p})<0$ then $S^{\rm no}_{g,b,p}$ decomposes into pairs-of-pants and hence admits a complete hyperbolic metric with geodesic boundaries of arbitrary length.
\end{ex}

As in the orientable case, compact surfaces with $\chi \geqslant 0$ can be geometrised: these are $\matRP^2$, the M\"obius strip, and the Klein bottle. The first has an elliptic structure while the other two have flat structures with geodesic boundary.


\subsection{Orbifolds} \label{orbifold:surface:subsection}
We can push the classification and geometrisation further to compact two-dimensional orbifolds. 

The finite subgroups of $\On(2)$ are: the cyclic $\matZ_2$ generated by a reflection, the cyclic $\matZ_n$ generated by a rotation, and the dihedral $D_{2n}$ containing reflections and rotations. Therefore every singular point $x$ on a two-dimensional orbifold $O$ is locally of one of these types:
$$V/_{\matZ_2}, \quad V/_{\matZ_n}, \quad V/_{D_{2n}}$$
with $V$ the unit ball in $\matR^2$. The point $x$ is called respectively a \emph{mirror}, a \emph{cone}, and a \emph{corner reflector} point of $O$, see Figure \ref{orbifold_types:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 8 cm] {\iftoggle{BW}{orbifold_types-BW}{orbifold_types}}
\nota{A mirror, a cone point, and a corner reflector on a two-dimensional orbifold.}
\label{orbifold_types:fig}
\end{center}
\end{figure}

We consider for simplicity only \emph{locally orientable} orbifolds, \emph{i.e.}~orbifolds with isotropy groups in $\SO(2)$. In other words, we exclude mirrors and corner reflectors. One such orbifold $O$ is easily encoded as
$$(S, p_1, \ldots, p_k)$$
where $S$ is a surface, and the orbifold $O$ is $S$ with $k$ cone points with rotational isotropy groups of order $p_1, \ldots, p_k >1$. We do not require $O$ to be globally orientable, so $S$ can be a non-orientable surface like $\matRP^2$. We define the \emph{Euler characteristic} of that orbifold as\index{Euler characteristic!of an orbifold} 
$$\chi(O) = \chi(S) - \sum \left( 1 - \frac 1{p_i} \right).$$
This definition is designed to behave well under coverings. The \emph{degree} of an orbifold covering $O\to O'$ is the cardinality of the fibre of any non-singular point in $O'$.
\begin{prop}
If $O \to O'$ is a degree-$d$ orbifold covering then 
$$\chi(O) = d \cdot \chi(O').$$
\end{prop}
\begin{proof}
Pick a cellularisation of $O'$ whose vertices contain the cone points: it lifts to a similar cellularisation of $O$. We consider all the vertices of these cellularisations as cone points, possibly with order 1, and we get
$$\chi(O') = V - E + F - \sum \left(1-\frac 1{p_i'}\right) = - E + F + \sum \frac 1 {p_i'}$$
where $V, E, F$ is the number of vertices, edges, and faces in the cellularisation of $O'$. The same formula holds for $O$: 
$$\chi(O) = - dE + dF + \sum \frac 1 {p_j}.$$
A cone point of order $p_i'$ in $O'$ lifts to some cone points with orders $p_{j_1}, \ldots, p_{j_l}$ of $O$, such that
$$d = \sum_{a=1}^l \frac {p_i'}{p_{j_a}} \quad \Longrightarrow \quad 
d \cdot \frac 1 {p_i'} = \sum_{a=1}^l \frac 1{p_{j_a}}.$$
This implies that $\chi(O) = d\cdot \chi(O')$.
\end{proof}


\subsection{Geometrisation of orbifolds}
Recall that an orbifold is good if it is covered by a manifold.
With a couple of exceptions, all the closed two-orbifolds are good and geometric.\index{orbifold!geometrisation of orbifolds}

\begin{table}
\begin{center}
\begin{tabular}{c||c}
\phantom{\Big|} \!\! orbifold & $\Gamma$ \\
\hline \hline
\phantom{\Big|} \!\! $S^2$ & \{e\} \\
\phantom{\big|} \!\! $(S^2, n, n)$ & $\matZ_n$ \\ 
\phantom{\Big|} \!\! $\matRP^2$ & $\matZ_2$ \\ 
\phantom{\big|} \!\! $(\matRP^2, n)$ & $D_{2n}$
\end{tabular}
\quad
\begin{tabular}{c||c}
\phantom{\Big|} \!\! orbifold & $\Gamma$ \\
\hline \hline
\phantom{\Big|} \!\! $(S^2, 2, 2, n)$ & $D_{2n}$ \\
\phantom{\big|} \!\! $(S^2, 2, 3, 3)$ & $T_{12}$ \\
\phantom{\Big|} \!\! $(S^2, 2, 3, 4)$ & $O_{24}$ \\
\phantom{\big|} \!\! $(S^2, 2, 3, 5)$ & $I_{60}$ 
\end{tabular}
\vspace{.2 cm}
\nota{Except the two bad cases, every locally orientable closed orbifold $O$ with $\chi(O)>0$ can be geometrised as $O=S^2/_{\Gamma}$ for some discrete $\Gamma <\On(3)$. In all cases $\Gamma < \SO(3)$ and hence $O$ is orientable, except $\matRP^2$ and $(\matRP^2,n)$ whose $\Gamma$ contains the antipodal map. 
The groups on the right table are the spherical Von Dyck groups, see Section \ref{more:examples:subsection}. 
The groups $T_{12}, O_{24}, I_{60}$ are the orientation-preserving isometry groups of the tetrahedron, octahedron, and icosahedron, and are isomorphic to $A_4$, $S_4$, $A_5$ respectively.}
\label{orbifold:elliptic:table}
\end{center}
\end{table}

\begin{teo} \label{O:geometrisation:teo}
Every closed locally orientable 2-orbifold $O$ is good except
$$(S^2, p), \quad (S^2,p_1,p_2)$$
with $p_1 \neq p_2$. A good orbifold $O$ has an elliptic, flat, hyperbolic structure $\Longleftrightarrow$ $\chi(O)$ is positive, zero, negative. The elliptic orbifolds are listed in Table \ref{orbifold:elliptic:table}.
\end{teo}
\begin{proof}
The orbifolds $(S^2, p)$ and $(S^2,p_1,p_2)$ are bad: subdivide $S^2$ into two discs, each containing at most one cone point; each disc has a unique surface (disc) covering, but the two coverings do not match if $p\neq 1$ or $p_1\neq p_2$.
The remaining orbifolds with $\chi(O)>0$ are 
$$S^2,\ (S^2, n, n),\ \matRP^2,\ (\matRP^2, n),$$ 
$$(S^2, 2, 2, n),\ (S^2, 2, 3, 3),\ (S^2, 2, 3, 4),\ (S^2, 2, 3, 5)$$
and they can all be realised as $S^2/_\Gamma$ for an appropriate finite $\Gamma < \On(3)$, see Table \ref{orbifold:elliptic:table}. The orbifolds with $\chi(O)=0$ are
$$(S^2, 2,3,6), \ (S^2,2,4,4),\ (S^2, 3,3,3),\ (S^2, 2,2,2,2),$$
$$(\matRP^2, 2,2),\ K,\ T$$
where $K$ and $T$ are the Klein bottle and the torus. The first four orbifolds were obtained as $\matR^2/_\Gamma$ in Section \ref{more:examples:subsection}. The orbifold $(\matRP^2, 2,2)$ is $\matR^2/_\Gamma$ where $\Gamma$ is generated by two glide reflections with orthogonal axis:
$$(x,y) \mapsto (x+1, -y), \quad (x,y) \mapsto (-x, y+1).$$
To prove this, consider the fundamental domain $[-\frac 12, \frac 12]\times [-\frac 12, \frac 12]$.

If $\chi(O)<0$ we construct a hyperbolic metric as we did in the surface case. If $O = (S^2, p_1, p_2, p_3)$ we get $O = \matH^2/_{\Gamma^{\rm or}(p_1,p_2,p_3)}$ using Von Dyck groups, see Section \ref{more:examples:subsection}. Otherwise, the orbifold $O$ easily decomposes along disjoint simple closed curves (that avoid the cone points) into some basic pieces with $\chi<0$, which are of the following kind: 
$$P,\ (A, p),\ (D, p_1, p_2)$$
where $P,A,D$ are the pair-of-pants, the annulus, and the disc, and $(p_1,p_2)\neq (2,2)$. We can give a hyperbolic structure to $P$ with any fixed length at the boundaries. 

Analogously, we can give a cone manifold structure with geodesic boundary to $(A,p)$ (respectively, $(D,p_1,p_2)$) with one (two) cone point of angle $\frac{2\pi}p$ ($\frac{2\pi}{p_1}$ and $\frac{2\pi}{p_2}$), for any fixed lengths at the boundaries. We already know this for $P$, and the proof for $(A,p)$ and $(D,p_1,p_2)$ is similar: instead of constructing right-angled hexagons, we construct pentagons with angles $\frac \pi 2, \frac \pi 2, \frac \pi 2, \frac \pi 2, \frac \pi p$ and quadrilaterals with angles $\frac \pi 2, \frac \pi 2, \frac \pi {p_1}, \frac \pi {p_2}$, and we double them, see Figure \ref{orbifold_pieces:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {orbifold_pieces.pdf}
\nota{For every angle $\alpha\leqslant \frac \pi 2$ and lengths $b,c>0$ there is a pentagon as shown (left); by doubling it along the unmarked edges we get a hyperbolic annulus with a cone point of angle $2\alpha$. For every angles $\alpha, \beta\leqslant \frac \pi 2$ and every length $c>0$ there is a quadrilateral as shown (right). By doubling it along the unmarked edges we get a hyperbolic disc with cone points of angle $2\alpha$ and $2\beta$.}
\label{orbifold_pieces:fig}
\end{center}
\end{figure}

By gluing all the pieces we obtain a hyperbolic cone structure on $O$ with cone angles $\frac{2\pi}{p_i}$ and we apply Proposition \ref{from:cone:to:orbifold:prop} to translate it to a hyperbolic orbifold structure.
\end{proof}

Recall that an orbifold is very good if it is finitely covered by a manifold. In the following corollary we use the geometrisation to prove shortly a non-trivial topological fact.

\begin{cor} \label{very:good:surface:cor}
Every good closed locally orientable 2-orbifold is very good.
\end{cor}
\begin{proof}
Every such orbifold is geometric, so Corollary \ref{very:good:cor} applies.
\end{proof}

The punctured case is also interesting when $\chi(O)<0$. We define a \emph{punctured orbifold} to be one of type
$$O = (S_{g,0,b}, p_1, \ldots, p_k).$$
\begin{teo}
Every punctured orbifold $O$ with $\chi(O)<0$ has a hyperbolic structure.
\end{teo}
\begin{proof}
Same proof as above, where we use triangular groups with possibly ideal vertices and we allow the pieces $P$, $(A, p)$, $(D, p_1, p_2)$ to have boundary components and/or cone points that degenerate to cusps. To construct them we build hexagons, pentagons, quadrilaterals with some lengths or angles that may be zero.
\end{proof}

These punctured orbifolds are also very good for the same reason above. It is also possible to consider orbifolds based on surfaces $S_{g,b,p}$ with boundary: every boundary component can be considered in two natural but distinct ways, either as a mirror (hence the orbifold is locally non-orientable), or as a boundary component: to do this we need to define an appropriate notion of orbifold with boundary.


\subsection{Gauss--Bonnet formula}
How can we compute the area of a hyperbolic surface? We can easily answer this question in the closed case.\index{Gauss--Bonnet formula} 

\begin{prop}[Gauss--Bonnet] \label{GB:prop}
Let $S$ be a closed hyperbolic surface. We have
$$\Area (S) = -2\pi \chi(S).$$
\end{prop}
\begin{proof}
Pick a Dirichlet domain $D$ for $S$. It is a $(2n)$-gon with inner angles $\alpha_1, \ldots, \alpha_{2n}$. By Proposition \ref{polygon:area:prop} we have
$$\Area(S) = \Area(D) = (2n-2)\pi - \sum_{i=1}^{2n} \alpha_i.$$
The surface $S$ is obtained from $D$ by gluing isometrically some pairs of edges. We get a cellularisation of $S$ with some $v$ vertices, $n$ edges, and one face $D$. Therefore 
$$\chi(S) = v - n + 1.$$
Each of the $v$ vertices is obtained by identifying some of the vertices of $D$, whose inner angles must sum to $2 \pi$. Therefore we get
$$\sum_{i=1}^{2n} \alpha_i = 2\pi v$$
and hence 
$$\Area(S) = (2n-2)\pi - 2\pi v = -2\pi(v-n+1) = -2\pi \chi(S).$$
The proof is complete.
\end{proof}
We can extend the formula to orbifolds and to the other geometries. 
\begin{cor}
Let $O$ be a closed hyperbolic, flat, or elliptic locally orientable 2-orbifold. We have
$$K\cdot\Area(O) = 2\pi \chi(O)$$
where $K=-1$, $0$, or $+1$ respectively.
\end{cor}
\begin{proof}
If $O$ is an orientable surface, then the equality holds: in the hyperbolic case this is Proposition \ref{GB:prop}, in the flat case we get $0=0$, and in the elliptic case $S=S^2$ and $\Area(S^2) = 4\pi = 2\pi \chi(S^2)$.

In general there is a degree-$d$ covering $S\to O$ of an orientable geometric surface $S$ by Corollary \ref{very:good:surface:cor}. The equality holds for $S$ and hence also for $O$ since 
$$\chi(S) = d \cdot \chi(O), \qquad \Area (S) = d \cdot \Area (O).$$
The proof is complete.
\end{proof}


\subsection{Lie subgroups of $\SO(3)$}
The following proposition is of general interest and is used in many different contexts.
It shows, among other things, that orientable elliptic orbifolds are \emph{rigid}: their geometry is fully determined by their fundamental group. (Flat and hyperbolic surfaces are not rigid, as we will soon see.)\index{$\SO(3)$}

\begin{prop} \label{subgroups:SO3:prop}
Every non-trivial proper Lie subgroup of $\SO(3)$ is conjugate to one of the following:
$$C_n, \ D_{2n},\ T_{12},\ O_{24},\ I_{60},\ \SO(2),\ \SO(2) \rtimes C_2.$$
These are the orientation-preserving isometry groups of: a regular $n$-pyramid, $n$-prism, tetrahedron, octahedron, icosahedron, cone, and cylinder.
\end{prop}
\begin{proof}
The Lie algebra $\frakg = \frakso(3,\matR)$ is generated by the matrices
$$A_x = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}, \quad
A_y = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ -1 & 0 & 0 \end{pmatrix}, \quad
A_z = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} $$
with the relations
$$[A_x, A_y] = A_z, \quad [A_y, A_z] = A_x, \quad [A_z, A_x] = A_y.$$
Therefore $\frakg$ is isomorphic to $\matR^3$ equipped with the standard vector product $\times$. We deduce that the only non-trivial proper sub-algebras of $\frakg$ have dimension 1, and hence every non-trivial proper Lie subgroup $G<\SO(3)$ has dimension $0$ or $1$.

If a Lie subgroup $G<\SO(3)$ has dimension zero, it is finite. Every non-trivial element in $G$ is a rotation along some axis, and hence it acts on $S^2$ with two (antipodal) fixed points.
Let $P\subset S^2$ be the set of the fixed points of all the non-trivial elements of $G$. 

The group $G$ clearly acts on $P$, and a double-counting argument gives
$$2\big(|G| - 1\big) = \sum_{p \in P}\big(|G_p| - 1\big)$$
where $G_p < G$ is the stabiliser of $p$. The fundamental theorem on group actions says that 
$$|G_p| = \frac{|G|}{|O(p)|}$$
where $O(p)$ is the orbit of $p$. Therefore
$$2\big(|G| - 1\big) = \sum_{p \in P}\left(\frac{|G|}{|O(p)|} - 1\right) = 
\sum_{O}\big({|G|} - |O|\big)
$$
where in the latter we sum on orbits $O$. We divide by $|G|$ to get
\begin{equation} \label{G:orbit:eqn}
2-\frac 2{|G|}  = \sum_{i=1}^r \left(1- \frac 1{a_i}\right)
\end{equation}
where $a_1,\ldots, a_r$ are the orders of the stabilisers of the $r$ orbits.

If $r=1$ we get $a_1 = |G| = 1$ and hence $G$ is trivial, a contradiction. If $r=2$ we get $a_1 = a_2 = |G|$ and hence every orbit is a single point, with stabiliser $G$. Therefore the points are antipodal and $G=C_n$.

If $r=3$ then $(a_1,a_2, a_3)$ is a triple with $\frac 1{a_1} + \frac 1{a_2} + \frac 1{a_3} > 1$, that is one of
$$(2,2,n), \quad (2,3,3), \quad (2,3,4), \quad (2,3,5).$$
In each case one calculates $|G|$ using (\ref{G:orbit:eqn}) and deduces the cardinalities of the three orbits. For instance in the $(2,2,n)$ case we have $|G|=2n$ and the orbits have cardinality $(n,n,2)$. One deduces that $G$ contains an index-two cyclic group $C_n$ and is the symmetry group $D_{2n}$ of the prism.

In the $(2,3,3)$ case we get $|G|=12$ and hence the orbits have order $(6,4,4)$. The stabiliser of a point in the order-4 orbit $O$ is a $\frac{2\pi}3$-rotation that rotates the other three points: one deduces that the points in $O$ are the vertices of a regular tetrahedron and $G$ is its symmetry group. The other cases are treated analogously.

If $G$ has dimension one, it contains the group $\SO(2)$ of all rotations along some axis $r$. Either $G=\SO(2)$, or there is a $g \in G \setminus \SO(2)$. If $g(r)\neq r$, then $G$ contains another $\SO(2)$ of rotations along $g(r)$, and these two copies of $\SO(2)$ generate a Lie subgroup of dimension $\geqslant 2$ in $G$, a contradiction. Therefore every element in $G\setminus \SO(2)$ preserves $r$ and is hence a $\pi$-rotation along an axis perpendicular to $r$. Therefore $G=\SO(2) \rtimes C_2$.
\end{proof}
