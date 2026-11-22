---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-018-33-tessellations
section_title: "Tessellations"
section_number: 3.3
pages: 90-97
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.825
latex_coverage_ratio: 1.0
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
A tessellation is a nice paving of $\matH^n$ made of polyhedra. Not only tessellations are beautiful objects, but they are also tightly connected with discrete groups of $\Iso(\matH^n)$ and hence with hyperbolic manifolds.


\index{tessellation}

\begin{defn}
A \emph{tessellation} of $\matH^n$ (or $\matR^n$, $S^n$) is a locally finite set of polyhedra that cover the space and may intersect only in common faces.
\end{defn}

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{Uniform_tiling_532-t012-BW}{Uniform_tiling_532-t012}} \quad
\includegraphics[width = 5 cm] {\iftoggle{BW}{Truncated_octahedra-BW}{Truncated_octahedra}}
\nota{A tessellation of $S^2$ into squares, hexagons, and decagons, and a tessellation of $\matR^3$ into truncated octahedra.}
\label{tiling:fig}
\end{center}
\end{figure}

Some examples in spherical and Euclidean space are shown in Figure \ref{tiling:fig}. We now construct some families explicitly.


\subsection{Triangles} \label{triangular:subsection}
We want to define some nice tessellations of $\matH^2, \matR^2$, and $S^2$ into triangles. The following exercise says that every triple of acute angles is realised by some triangle in the appropriate geometry.

\begin{ex}
Given three real numbers $0<\alpha, \beta, \gamma \leqslant \frac \pi 2$ there is a triangle $\Delta$ with inner angles $\alpha, \beta, \gamma$ inside $\matH^2, \matR^2$, or $S^2$ depending on whether the sum $\alpha + \beta + \gamma$ is smaller, equal, or bigger than $\pi$. 
\end{ex}

Let $a,b,c \geqslant 2$ be three natural numbers and $\Delta$ be a triangle with inner angles $\frac \pi a, \frac \pi b, \frac \pi c$. The triangle $\Delta$ lies in $\matH^2$, $\matR^2$, or $S^2$ depending on whether $\frac 1a+\frac 1b + \frac 1c$ is smaller, equal, or bigger than 1. In all cases, by mirroring iteratively $\Delta$ along its edges we construct a tessellation of the space. 


\begin{figure}
\begin{center}
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{233_BW}{233}} \quad
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{234_BW}{234}} \quad 
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{235_BW}{235}} 
\nota{The tessellations $(2,3,3)$, $(2,3,4)$ and $(2,3,5)$ of the sphere.}
\label{triangular:fig}
\end{center}
\end{figure}

The triples realisable in $S^2$ are $(2,2,c)$, $(2,3,3)$, $(2,3,4)$, and $(2,3,5)$: the last three tessellations are shown in Figure \ref{triangular:fig} and are connected to the platonic solids. They consist of $24$, $48$, and $120$ triangles. 

\begin{figure}
\begin{center}
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{Tile_V46b_BW}{200px-Tile_V46b}} \quad
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{Tile_V488_bicolor_BW}{200px-Tile_V488_bicolor}} \quad 
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{1024px-Tile_36_BW}{200px-Tile_36}} 
\nota{The tessellations $(2,3,6)$, $(2,4,4)$, and $(3,3,3)$ of the Euclidean plane.}
\label{triangular2:fig}
\end{center}
\end{figure}

The triples realisable in $\matR^2$ are $(2,3,6)$, $(2,4,4)$, and $(3,3,3)$: the tessellations are shown in Figure \ref{triangular2:fig}. There are infinitely many triples realisable in $\matH^2$, and some are shown in Figure \ref{triangular3:fig}. 

\begin{figure}
\begin{center}
\includegraphics[width = 3.7 cm] {\iftoggle{BW}{Order-3_heptakis_heptagonal_tiling-BW}{240px-Order-3_heptakis_heptagonal_tiling}} \quad
\includegraphics[width = 3.7 cm] {\iftoggle{BW}{Order-4_bisected_pentagonal_tiling-BW}{240px-Order-4_bisected_pentagonal_tiling}} \quad 
\includegraphics[width = 3.7 cm] {\iftoggle{BW}{Uniform_dual_tiling_433-t012-BW}{240px-Uniform_dual_tiling_433-t012}} 
\nota{The tessellations $(2,3,7)$, $(2,4,5)$, and $(3,3,4)$ of the hyperbolic plane.}
\label{triangular3:fig}
\end{center}
\end{figure}

In the hyperbolic plane we can also use triangles with vertices at infinity, which have inner angle zero by definition.
\begin{ex}
Given three real numbers $0\leqslant \alpha, \beta, \gamma \leqslant \frac \pi 2$ with sum smaller than $\pi$ there is a triangle $\Delta\subset \matH^2$ with inner angles $\alpha, \beta, \gamma$.
\end{ex}

For any triple $(a,b,c)$ of numbers in $\matN \cup \{\infty \}$ with $\frac 1a + \frac 1b + \frac 1c < 1$ we may take the triangle $\Delta \subset \matH^2$ with inner angles $\frac \pi a$, $\frac \pi b$, $\frac \pi c$ and reflect it iteratively to get a tessellation of $\matH^2$. 

The triple $(\infty, \infty, \infty)$ gives a nice tessellation into ideal triangles called the \emph{Farey tessellation} and shown in Figure \ref{tiling_Farey:fig}. 
\index{tessellation!Farey tessellation}
 
\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {H2checkers_iii.png}
\nota{The Farey tessellation $(\infty, \infty, \infty)$ of the hyperbolic plane.}
\label{tiling_Farey:fig}
\end{center}
\end{figure}


\subsection{Platonic solids}
We now turn to tessellations of 3-dimensional spaces. Table \ref{platonic:table} displays a finite list of platonic solids $P$ with dihedral angles $\frac{2\pi}k$ contained in $\matH^3$, $\matR^3$, or $S^3$. For each solid in the list, by reflecting iteratively $P$ along its faces we get a tessellation of the space. 

The Figures \ref{honeycomb_dodecahedron_534:fig}, \ref{honeycomb_dodecahedron_536:fig}, and \ref{honeycomb_dodecahedron_533:fig} show the tessellations of $\matH^3, \matH^3,$ and $S^3$ by regular dodecahedra with dihedral angles $\frac \pi 2$, $\frac \pi 3$, and $\frac{2\pi}3$. The first two tessellations contain infinitely many polyhedra and appear in the figures as seen by an observer floating inside $\matH^3$. The reader is invited to observe the differences between the first two tessellations of the hyperbolic space. The third tessellation contains finitely many polyhedra and the figure shows its stereographic projection in $\matR^3$.

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{H3_534_CC_center-BW}{H3_534_CC_center}}
\nota{The tessellation of $\matH^3$ into right-angled regular dodecahedra, seen from inside $\matH^3$.}
\label{honeycomb_dodecahedron_534:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{H3_536_CC_center-BW}{H3_536_CC_center}}
\nota{The tessellation of $\matH^3$ into ideal regular dodecahedra with dihedral angle $\frac \pi 3$, seen from inside $\matH^3$. Note that all vertices lie at infinity.}
\label{honeycomb_dodecahedron_536:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{Stereographic_polytope_120cell_faces-BW}{600px-Stereographic_polytope_120cell_faces}}
\nota{The tessellation of $S^3$ into 120 regular dodecahedra with dihedral angle $\frac {2\pi} 3$, transposed into $\matR^3$ via the stereographic projection, that transforms straight faces into round ones but preserves the angles.}
\label{honeycomb_dodecahedron_533:fig}
\end{center}
\end{figure}


\subsection{Regular tessellations} \label{regular:subsection}
Platonic solids are \emph{regular}, that is they have many symmetries. A notion of regularity may be defined in all dimensions for polyhedra and tessellations as follows.
\index{tessellation!regular tessellation} \index{polyhedron!regular polyhedron}

Every tessellation in $\matH^n$, $\matR^n$, or $S^n$ has a symmetry group, consisting of all the isometries of the ambient space that preserve it. A \emph{flag} is a sequence of faces $f_0 \subset \ldots \subset f_n$ of the tessellation with $\dim f_i = i$. A tessellation is \emph{regular} if the symmetry group acts transitively on flags. 

These definitions apply also to polyhedra. We note that a regular polyhedron in $\matR^n$, considered up to similarities, may be interpreted as a regular tessellation in $S^{n-1}$, and vice versa.\index{Schl\"afli notation}

The \emph{Schl\"afli notation} beautifully encodes various regular tessellations, in all dimensions and in all geometries. The symbol $\{n\}$ with $n\geqslant 3$ denotes the regular $n$-gon, that is a regular tessellation of $S^1$ by $n$ congruent arcs, and by extension $\{\infty \}$ denotes the regular tessellation of $\matR$ by infinitely many congruent segments.

The symbol $\{p,q\}$ denotes a regular tessellation in $\matH^2, \matR^2,$ or $S^2$ by $p$-gons where $q$ of them meet at every vertex. The five platonic solids are
$$\{3,3\}, \{3,4\}, \{3,5\}, \{4,3\}, \{5,3\},$$
the symbols $\{3,6\}$, $\{4,4\}$, and $\{6,3\}$ denote the two regular tessellations of $\matR^2$ into equilateral triangles, squares, and regular hexagons, and every other pair $\{p,q\}$ denotes a tessellation of regular $p$-gons in $\matH^2$ with angles $\frac {2\pi}q$, that meet at $q$ at every vertex. We can also interpret $\{p, \infty\}$ as a regular tessellation of $\matH^2$ into ideal regular $p$-gons (the Farey tessellation is $\{3,\infty\}$) and $\{\infty, q\}$ as a regular tessellation of $\infty$-gons that meet at $q$ at every vertex, whose edges form a $q$-regular tree (a tree where $q$ edges meet at every vertex). Finally $\{\infty, \infty\}$ is a regular tessellation of ideal $\infty$-gons. See Figure \ref{infty:tessellations:fig}

\begin{figure}
\begin{center}
\includegraphics[width = 3.8 cm] {\iftoggle{BW}{600px-H2chess_iiif}{600px-H2chess_iiif}} \quad
\includegraphics[width = 3.8 cm] {\iftoggle{BW}{600px-H2chess_24ic}{600px-H2chess_24ic}} \quad 
\includegraphics[width = 3.8 cm] {\iftoggle{BW}{600px-H2chess_2iib}{600px-H2chess_2iib}} 
\nota{The tessellations of $\matH^2$ with Schl\"afli symbols $\{4,\infty\}$, $\{\infty, 4\}$, and $\{\infty, \infty\}$.}
\label{infty:tessellations:fig}
\end{center}
\end{figure}

The symbol $\{p,q,r\}$ denotes a regular tessellation in $\matH^3, \matR^3,$ or $S^3$ by polyhedra $\{p,q\}$ where $r$ of them meet at every edge. We deduce from Table \ref{platonic:table} that the regular tessellations of $S^3$ are
$$\{3,3,3\}, \{3,3,4\}, \{3,3,5\}, \{3,4,3\}, \{4,3,3\}, \{5,3,3\}.$$
These are the six regular polyhedra (usually called \emph{polytopes}) in dimension four: we will encounter them again in Chapter \ref{regular:polytopes:subsection}. The symbol $\{4,3,4\}$ indicates the tessellation of $\matR^3$ into cubes, and
$$\{3,3,6\}, \{3,4,4\}, \{3,5,3\}, \{4,3,5\}, \{4,3,6\}, \{5,3,4\}, \{5,3,5\}, \{5,3,6\}$$
denote the tessellations of $\matH^3$ into platonic solids. It is also possible to interpret more triples $\{p,q,r\}$ in an appropriate way, sometimes by representing the vertices of the polyhedra as space-like vectors in the hyperboloid model.

Every regular tessellation has a \emph{dual} regular tessellation obtained by taking the barycenters of all the cells involved. The dual of $\{a,b, \ldots, z\}$ is $\{z, \ldots, b,a\}$. 
Duals of ideal tessellations involve infinite polyhedra: for instance $\{6,3,3\}$ is shown in Figure \ref{honeycomb_dodecahedron_633:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{H3_633_FC_boundary-BW}{H3_633_FC_boundary}}
\nota{In the tessellation $\{6,3,3\}$ of $\matH^3$ every polyhedron has infinitely many hexagonal faces, whose vertices all lie in a single horosphere.}
\label{honeycomb_dodecahedron_633:fig}
\end{center}
\end{figure}

The story continues in four dimensions: we denote by $\{p,q,r,s\}$ a regular tessellation made of polytopes of type $\{p,q,r\}$ that meet in $s$ at every codimension-two face. With the same techniques of Section \ref{platonici:subsection} we can identify the regular polytopes in $\matH^4, \matR^4$ and $S^4$ with dihedral angles that divide $2\pi$, and the corresponding tessellations of the ambient space -- that we are unfortunately unable to see.


\subsection{Voronoi tessellations} \label{Voronoi:subsection}
In the previous section we have constructed some tessellations by exploiting the symmetries of regular polyhedra: we can probably extend these methods to less symmetric polyhedra, but how far can we go? How can we construct highly non-regular tessellations?

There is a strikingly simple procedure that transforms every discrete set $S$ of points in $\matH^n$ into a tessellation, called the \emph{Voronoi tessellation} of $S$. The construction goes as follows. \index{tessellation!Voronoi tessellation}

For every point $p \in S$ we define
$$D(p) = \big\{ q\in \matH^n\ \big|\ d(q,p)\leqslant d(q,p') \quad \forall p'\in S \big\}.$$

\begin{prop}
The set $D(p)$ is a polyhedron and the polyhedra $D(p)$ as $p\in S$ varies form a tessellation of $\matH^n$.
\end{prop}
\begin{proof}
It is an easy exercise to show that the points in $\matH^n$ having the same distance from two distinct fixed points form a hyperplane. For every $p'\in S$ different from $p$ we define the half-space
$$H_{p'} = \big\{q \in \matH^n\ \big| \ d(q,p) \leqslant d(q,p') \big\}.$$
The set $D(p)$ is the intersection of the half-paces $H_{p'}$ as $p'$ varies in $S\setminus \{p\}$.

Since $S$ is discrete, these half-spaces are locally finite (there are finitely many points in $S$ at bounded distance from $p$, hence finitely many hyperplanes). Therefore $D(p)$ is a polyhedron. Since $S$ is discrete, every point $q\in \matH^n$ has at least one nearest point $p\in S$: therefore the polyhedra $D(p)$ cover $\matH^n$ as $p\in S$ varies. 

It remains to prove that the polyhedra $D(p)$ intersect along common faces. We have $D(p) \cap D(p') = D(p) \cap \partial H_{p'}$ and hence $D(p) \cap D(p')$ is either empty or a face of $D(p)$. The case of multiple intersections follows from Exercise \ref{intersection:faces:ex}.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{Coloured_Voronoi_2D-BW}{Coloured_Voronoi_2D}} 
\nota{A Voronoi tessellation of the Euclidean plane.}
\label{Voronoi:fig}
\end{center}
\end{figure}

Voronoi tessellations of course make sense also in $\matR^n$ and $S^n$, see Figure \ref{Voronoi:fig}. We have just proved that tessellations are not exoteric, but quite ordinary objects, and we now show that they are useful to study hyperbolic manifolds.
