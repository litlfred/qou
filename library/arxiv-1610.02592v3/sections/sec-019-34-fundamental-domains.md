---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-019-34-fundamental-domains
section_title: "Fundamental domains"
section_number: 3.4
pages: 97-105
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.96
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We turn back to our discrete subgroups $\Gamma < \Iso(\matH^n)$. The geometry of a discrete $\Gamma$ is nicely controlled by some polyhedra, called \emph{fundamental domains}.
We introduce these objects and make some important examples.


\subsection{Fundamental and Dirichlet domains}
Let $\Gamma$ be a discrete group of isometries of $\matH^n$. The group $\Gamma$ may or may not act freely on $\matH^n$.  \index{fundamental domain}
\begin{defn}
A \emph{fundamental domain} for $\Gamma$ is a polyhedron $D \subset\matH^n$ whose translates $g(D)$ as $g\in \Gamma$ varies are distinct and form a tessellation of the space $\matH^n$. 
\end{defn}
If $D$ is a fundamental domain, the group $\Gamma$ acts freely and transitively on the tessellation $\big\{g(D)\big\}_{g \in \Gamma}$, so in particular the polyhedra $g(D)$ are all isometric. 

We describe a procedure that builds a fundamental domain for any discrete subgroup $\Gamma < \Iso(\matH^n)$. Pick  a point $p\in \matH^n$ 
with trivial stabiliser $\Gamma_p$, which exists by Proposition \ref{dense:prop}. The group $\Gamma$ acts freely and transitively on the orbit $\Gamma(p)$, which is discrete by Proposition \ref{discrete:prop}.

The discrete orbit $\Gamma(p)$ defines a $\Gamma$-invariant Voronoi tessellation of $\matH^n$, and every polyhedron of the tessellation is a fundamental domain. The polyhedron $D(p)$ of the tessellation containing $p$ is called the \emph{Dirichlet domain} for $\Gamma$ centred at $p$. By construction we have \index{Dirichlet domain}
$$D(g(p)) = g(D(p))$$
for all $g\in \Gamma$. We have proved in particular the following.

\begin{prop}
Every discrete group $\Gamma < \Iso(\matH^n)$ has a fundamental domain.
\end{prop}

Fundamental domains are far from being unique. The Dirichlet domain $D(p)$ depends on $p$ in a continuous fashion, and many fundamental domains are not Dirichlet domains.

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{ModularGroup-FundamentalDomain-01-BW}{ModularGroup-FundamentalDomain-01}}
\nota{The shadowed triangle (with one ideal vertex) is a fundamental domain for $\Gamma = \PSLZ$ acting on the half-space $H^2$. The translates of the fundamental domain form the tessellation shown.}
\label{modular_group:fig}
\end{center}
\end{figure}

\begin{ex}
Prove that the shadowed triangle in Figure \ref{modular_group:fig} is a fundamental domain for the modular group $\PSLZ$. 
\end{ex}

Everything we say also holds for $\matR^n$ and $S^n$.


\subsection{Fundamental domain of manifolds}
Let $\Gamma< \Iso(\matH^n)$ be a discrete subgroup that acts freely on $\matH^n$ and $D$ be a fundamental domain for $\Gamma$. We can get some information on the hyperbolic manifold $M=\matH^n/_\Gamma$ by looking at $D$. 

\begin{prop}
Let $M=\matH^n/_\Gamma$ be a hyperbolic manifold and $D$ a fundamental domain for $\Gamma$. The projection $\pi\colon \matH^n \to M$ restricts to a surjective map $D \to M$ that sends $\interior D$ isometrically onto an open dense subset of $M$. In particular we have
$$\Vol(D) = \Vol (M).$$
If $D$ is a Dirichlet domain, it is compact if and only if $M$ is.
\end{prop}
\begin{proof}
The translates $g(D)$ cover $\matH^n$, hence the projection $D \to M$ is surjective.
The translates $g(\interior D)$ are disjoint, hence $\interior D$ is sent isometrically inside $M$. The boundary $\partial D$ has measure zero, hence $\Vol(D) = \Vol(\interior D) = \Vol(M)$. 

If $D$ is compact then $M$ clearly is. If $D = D(p)$ is a Dirichlet domain and $M$ is compact, $M$ has finite diameter $\delta$ and hence every point in $\matH^n$ is at distance $\leqslant \delta$ of some point in the orbit of $p$. Hence $D(p)$ is contained in the closure of $B(p,\delta)$.
\end{proof}

A fundamental domain $D$ alone however does not determine $M$: we will soon see in Section \ref{piatte:subsection} that a square in $\matR^2$ is the fundamental domain of two non homeomorphic compact flat surfaces.


\subsection{Asteroids}
The facets of a fundamental domain $D$ are naturally partitioned into isometric pairs, as follows. Ever facet $f$ of $D$ is incident to $D$ and to another fundamental domain $g(D)$ of the tessellation. The isometry $g^{-1}$ sends $g(D)$ to $D$ and hence sends $f$ to another facet $f'$ of $D$. One checks immediately that $(f')' = f$, so $f$ and $f'$ are paired isometrically. 

One should think of $M$ as obtained from $D$ by identifying these facets in pairs: we can picture an observer -- say, a spaceship -- floating and traveling inside $M$ by visualising it in $D$, and jumping from $f$ to $f'$ every time it crosses the interior of a facet $f$, like in the 1979 video game \emph{Asteroids}.


\subsection{Spine and cut locus}
Another picture that may help to understand $M$ geometrically is the \emph{spine}\index{spine} $S \subset M$ defined as $S=\pi(\partial D)$. This is a $(n-1)$-dimensional object in $M$ whose complement is an open ball. When $D = D(p)$ is the Dirichlet domain of a point $p$, the spine $S$ is called the \emph{cut locus} of the point $q=\pi(p) \in M$. \index{cut locus}

\begin{ex}
The cut locus of $q \in M$ consists of all points $q'$ such that there are at least two geodesics of minimal length connecting $q$ to $q'$.
\end{ex}

We now exhibit some important examples of discrete groups of isometries in the three geometries $\matH^n$, $\matR^n$, and $S^n$, and study their fundamental domains. 


\subsection{Triangle groups} \label{triangle:groups:subsection}
Let $a,b,c \geqslant 2$ be natural numbers and $\Delta$ be the triangle in $\matH^2, S^2$, or $\matR^2$ with inner angles $\frac \pi a$, $\frac \pi b$, $\frac \pi c$. By reflecting iteratively $\Delta$ along its sides we get a tessellation $T$, see Section \ref{triangular:subsection}. \index{group!triangle group}

The \emph{triangle group} $\Gamma = \Gamma (a,b,c)$ is the group of isometries of $S^2$, $\matR^2$, or $\matH^2$ generated by the reflections $x,y,z$ along the three sides of $\Delta$ opposite to the vertices with inner angles $a,b,c$, respectively.

\begin{prop} \label{triangle:gamma:prop}
The triangle group $\Gamma (a,b,c)$ acts freely and transitively on the triangles of the tessellation $T$. Hence it is discrete and $\Delta$ is a fundamental domain for $\Gamma$. A presentation for the group is
$$\langle x, y,z\ |\ x^2, y^2, z^2, (xy)^c, (yz)^a, (zx)^b \rangle.$$
\end{prop}
\begin{proof}
We restrict for simplicity to the hyperbolic case, the others being analogous. It is convenient to construct the tessellation $T$ abstractly (this also furnishes a rigorous proof that by mirroring $\Delta$ along its sides we get a tessellation of $\matH^2$). 

We denote by $x,y,z$ both the sides of $\Delta$ and the reflections along them. For every $g\in \Gamma$ we define an abstract copy $\Delta_g$ of $\Delta$, and then we glue all these abstract copies altogether by pairing their sides  as follows: for every side of $\Delta$, say $x$, and every $g\in \Gamma$, we identify the two copies of the side $x$ in $\Delta_g$ and $\Delta_{gx}$ with the obvious identity map.

Via these identifications we get an abstract space $T$ tessellated into the triangles $\Delta_g$. The group $\Gamma$ acts freely and transitively on the tessellation (the element $g'\in \Gamma$ sends $\Delta_g$ to $\Delta_{g'g}$). We now prove that $T$ has a natural structure of a hyperbolic surface: since $\Gamma$ acts transitively, it suffices to check this for the points $p$ lying in $\Delta_e$. If $p$ lies in the interior of $\Delta_e$ or of a side, this is clear by construction. If $p$ is a vertex, say with inner angle $a$, by construction a cycle of $2a$ triangles $\Delta_e, \Delta_y, \Delta_{yz}, \Delta_{yzy}, \Delta_{yzyz}, \ldots $ is attached around $p$ because $(yz)^a = e$, and hence $T$ is naturally a hyperbolic surface also near $p$.

The hyperbolic surface $T$ is easily seen to be connected and complete. There is a natural developing map $\varphi\colon T\to \matH^2$ that sends $\Delta_g$ to $g(\Delta)$. The map $\varphi$ is a local isometry, hence a covering by Proposition \ref{local:isometry:prop}, hence an isometry since $\matH^2$ is simply connected. We identify $T$ with $\matH^2$ through $\varphi$.

It remains to prove that $\Gamma$ may be presented as stated. Let $G$ be the group presented as
$$\langle x, y,z\ |\ x^2, y^2, z^2, (xy)^c, (yz)^a, (zx)^b \rangle.$$
There is a natural surjection $G\to \Gamma$. We may repeat all the arguments above using $G$ instead of $\Gamma$ and get another $T'$ isometric to $\matH^2$ that covers $T$. We deduce that $T'=T$ and $G=\Gamma$.
\end{proof}

The triangle group $\Gamma(2,2,c) \isom \matZ/_{2\matZ}\times D_{2c}$ has order $4c$ and is the symmetry group of a prism. The triangle groups $\Gamma(2,3,3)$, $\Gamma(2,3,4)$, and $\Gamma(2,3,5)$ have order $24$, $48$, and $120$ and are the symmetry groups of the regular tetrahedron, octahedron, and icosahedron: the reader is invited to check all these facts visually by looking at Figure \ref{triangular:fig}.

The triangle groups $\Gamma(2,3,6)$, $\Gamma(2,4,4)$, and $\Gamma(3,3,3)$ are discrete groups of isometries of $\matR^2$ with compact quotient $\matR^2/_\Gamma$. 
If $\frac 1a + \frac 1b + \frac 1c <1$ the group $\Gamma(a,b,c)$ is a discrete subgroup of $\Iso(\matH^2)$. It contains infinitely many elliptic elements, such as reflections along lines and finite-order rotations around the vertices of the triangles. By Selberg's Lemma, there is a torsion-free subgroup $\Gamma' < \Gamma$ of some finite index $h$. The quotient $\matH^2/_{\Gamma'}$ is a closed hyperbolic surface and is tessellated into $h$ triangles isometric to $\Delta$.


\subsection{Coxeter polyhedra}
Triangle groups may be generalised to all dimensions as follows. A polyhedron $P$ in $\matH^n$ (or $\matR^n$, $S^n$) is a \emph{Coxeter polyhedron} if the dihedral angle of every codimension-two face divides $\pi$.\index{polyhedron!Coxeter polyhedron} For instance, the regular ideal tetrahedron and octahedron are Coxeter polyhedra.

The following theorem generalises Proposition \ref{triangle:gamma:prop}. Let $P$ be a finite Coxeter polyhedron: it is the convex hull of finitely many vertices in $\overline{\matH^n}$ (or $\matR^n$, $S^n$) and has $k$ facets, that we number as $1, \ldots, k$; we denote by $r_i$ the reflection along the $i$-th facet, and by $\frac {\pi}{a_{ij}}$ the dihedral angle formed by the $i$-th and $j$-th facets, if they are incident. Let $\Gamma$ be the isometry group generated by the reflections along the facets of $P$.

\begin{teo}
By mirroring iteratively a finite Coxeter polyhedron $P$ along its facets we get a tessellation of $\matH^n$ (or $\matR^n, S^n$).
The group $\Gamma$ acts freely and transitively on the tessellation: hence it is discrete and $P$ is a fundamental domain for $\Gamma$. A presentation for $\Gamma$ is
$$\langle r_1, \ldots, r_k \ |\  r_i^2, (r_ir_j)^{a_{ij}} \rangle$$
where $i$ varies in $1,\ldots, k$ and the pair $i,j$ varies among the incident facets.
\end{teo}
\begin{proof}
Same proof as Proposition \ref{triangle:gamma:prop}, with in addition an induction on the dimension $n$. Here are the details. We consider for simplicity only the hyperbolic case.

For every $g\in \Gamma$ we define an abstract copy $P_g$ of $P$, and we identify the $i$-th facet of $P_g$ and $P_{gr_i}$ for all $g\in \Gamma$ and all $i$. To prove that the resulting space $T$ is naturally a hyperbolic manifold, we use the induction hypothesis as follows. Every $p\in P_e$ lies in the interior of some $h$-dimensional face $f$, and let $\Gamma_f<\Gamma$ be the subgroup generated by the reflections along all the facets of $P$ containing $f$. The point $p$ is adjacent in $T$ to the polyhedra $P_g$ such that $g\in \Gamma_f$. By intersecting each such $P_g$ with a small codimension $h+1$ sphere centred in $p$ and contained in the codimension $h$ subspace orthogonal to $f$, we get some spherical polytope $Q_g$ of dimension $n-h-1<n$. (The spherical polytope $Q_t$ is usually called the \emph{spherical link} of $f$.)

By construction $Q_e \subset S^{n-h-1}$ is a Coxeter polytope and the subgroup $\Gamma_f < \Iso(S^{n-h-1})$ is generated by the reflections along its facets. By applying the induction hypothesis on $Q_e$ we deduce that the polytopes $Q_g$ with $g\in \Gamma_f$ form a tessellation of $S^{n-h-1}$, hence the polyhedra $P_g$ incident to $p$ form naturally a hyperbolic ball locally near $p$. Therefore $T$ is a hyperbolic manifold.

Proving that $T$ is complete requires a bit of care if $P_e$ has some ideal vertex $v$. In that case $v$ has a Euclidean link (obtained by intersecting $P_e$ with a small horosphere) and we conclude by induction as above that the Euclidean links of the $P_g$ incident to $v$ in $T$ glue to form a Euclidean $\matR^{n-1}$, that is a horosphere, so by intersecting each $P_g$ with small horoballs we get a horoball near $v$, which is complete.

The hyperbolic space $T$ is complete and connected, and we conclude as in the proof of Proposition \ref{triangle:gamma:prop}. 
\end{proof}

A group generated by some reflections along hyperplanes is called a \emph{reflection group}.\index{group!reflection group}
The following proposition shows that Coxeter polyhedra generate all the interesting reflection groups.

\begin{prop}
Every discrete reflection group $\Gamma$ is generated by the reflections along the facets of some Coxeter polyhedron.
\end{prop}
\begin{proof}
Consider the mirror hyperplanes of all the reflections in $\Gamma$. Since $\Gamma$ is discrete, these form a locally finite set and hence define a tessellation of $\matH^n$ onto which $\Gamma$ acts transitively. Pick one polyhedron $P$ of the tessellation. The reflections along the facets of $P$ generate $\Gamma$ (exercise).
\end{proof}

Coxeter polyhedra are beautiful objects that can be used to construct hyperbolic manifolds: every finite Coxeter polyhedron $P$ generates a reflection group $\Gamma$ which contains, by Selberg's Lemma, a torsion-free subgroup $\Gamma'$ of some finite index $h$. The quotient $M=\matH^n/_{\Gamma'}$ is a hyperbolic manifold and is tessellated into $h$ copies of $P$, so that $\Vol(M) = h\Vol(P)$. By residual finiteness, there are plenty of such manifolds.


\subsection{Coxeter graphs}
If a Coxeter polyhedron $P$ has a reasonable number of facets (for instance, if $P$ is a simplex), then one can study many of its properties by looking at its \emph{Coxeter graph},\index{Coxeter graph} which is constructed as follows: draw one node for each facet of $P$, and for every pair of facets intersecting with dihedral angle $\frac \pi a$ connect the corresponding nodes with an edge labeled with $a$. One also uses thickened or dashed edges to denote non-incident faces that do or do not intersect at some ideal vertex, respectively (these cases cannot occur on simplexes). Given the abundance of right angles, one usually omit the edges with label 2. 

\begin{ex}
Let $P$ be a regular polytope or tessellation with Schl\"afli symbol $\{a,b, \ldots, z\}$. By quotienting $P$ via all its isometries we get a Coxeter simplex, called its \emph{characteristic simplex}, whose Coxeter graph is\index{simplex!characteristic simplex}
\begin{center}
\includegraphics[width = 3 cm]{Coxeter_line}
\end{center}
\end{ex}


\subsection{Flat tori} \label{piatte:subsection}
The isometry group $\Iso(\matR^n)$ of $\matR^n$ contains the translations subgroup that we identify with $\matR^n$. The integer translations $\Gamma = \matZ^n$ form a discrete subgroup that acts freely on $\matR^n$, therefore the quotient $\matR^n /_\Gamma$ is a flat manifold. It is naturally diffeomorphic to the $n$-dimensional torus: 
$$\matR^n/_{\matZ^n} = \left(\matR/_{\matZ}\right)^n \isom \underbrace{S^1  \times \ldots \times S^1}_n.$$

\begin{ex} For every $p\in \matR^n$ the Dirichlet domain $D(p)$ is a $n$-dimensional unit cube centred at $p$.
\end{ex}

The flat $n$-torus may be seen as the unit $n$-cube with its opposite facets identified by translations. The two-dimensional case is shown in Figure \ref{domini:fig}-(left): by identifying the opposite sides of a square we get a torus. \index{flat torus}

\begin{figure}
\begin{center}
\includegraphics[width = 11.5 cm] {\iftoggle{BW}{domini-BW}{domini}}
\nota{A fundamental domain in $\matR^2$ for the torus (left) and the Klein bottle (centre): opposite sides should be identified as indicated by the arrows. A fundamental domain in $S^2$ for $\matRP^2$ (right).}
\label{domini:fig}
\end{center}
\end{figure}

The $n$-torus possesses a continuous family of non-isometric flat metrics. A \emph{lattice} $\Gamma<\matR^n$ is a discrete subgroup isomorphic to $\matZ^n$ which spans $\matR^n$ as a vector space. We see $\Gamma$ as a group of translations. \index{lattice}

\begin{ex} For every lattice $\Gamma$, the flat manifold $\matR^n/_\Gamma$ is diffeomorphic to the $n$-torus. A fundamental domain is the parallelotope spanned by $n$ generators of $\Gamma$.
\end{ex}

A Dirichlet domain for $\Gamma$ is almost never a parallelotope! In the \emph{hexagonal torus} $\matR^2/_\Gamma$ the group $\Gamma$ is the equilateral lattice generated by the translations\index{torus!hexagonal torus}
$$(1,0), \quad \big(\tfrac 12, \tfrac{\sqrt 3}2\big)$$ 
and the Dirichlet domain of any point is a regular hexagon. Orientable flat manifolds are easily classified (up to diffeomorphism) in dimension two. \index{hexagonal torus}

\begin{prop} \label{flat:is:torus:prop}
Every closed flat orientable surface is a torus.
\end{prop}
\begin{proof}
A closed flat surface $S$ is isometric to $\matR^2/_\Gamma$ for some discrete group $\Gamma$ of orientation-preserving isometries acting freely. Every fixed-point-free orientation-preserving isometry of $\matR^2$ is a translation (exercise), hence $\Gamma < \matR^2$. If $\Gamma$ has rank one then $S$ is not compact, hence $\Gamma$ is a lattice and $S$ is a torus.
\end{proof}

Flat manifolds more complicated than tori can be constructed by considering also non-translational isometries of $\matR^n$, which exist for $n\geqslant 3$ and also for $n=2$ in the non-orientable setting. For instance, in dimension two we find the \emph{Klein bottle} by taking $\Gamma$ as the group generated by the isometries:
$$\tau\colon(x,y) \mapsto (x+1, y), \qquad \eta\colon(x,y) \mapsto (1-x, y+1).$$
A fundamental domain for the Klein bottle is shown in Figure \ref{domini:fig}-(centre).
\index{Klein bottle}

Every subgroup $\Gamma' < \Gamma$ furnishes another flat manifold $\matR^2/_{\Gamma'}$ that covers the Klein bottle. For instance, the subgroups $\langle \tau \rangle$ and $\langle \eta \rangle$ generated respectively by $\tau$ and $\eta$ are both isomorphic to $\matZ$ but provide two different coverings: the manifold $\matR^2/_{\langle\tau\rangle}$ is an infinite cylinder while $\matR^2/_{\langle\eta\rangle}$ is an infinite M\"obius strip. 

The subgroup $\Gamma'$ generated by the translations $\tau$ and $\eta^2$ is isomorphic to $\matZ^2$ and has index 2 in $\Gamma$. The Klein bottle is doubly covered by the flat torus $\matH^2/_{\Gamma'}$. A fundamental domain for $\Gamma'$ is a rectangle with vertices $(0,0)$, $(1,0)$, $(0,2)$, $(1,2)$.

We have seen that the Klein bottle is covered by a torus. In fact, we will see in Section \ref{Bieberbach:section} that \emph{every} closed flat $n$-manifold is covered by a flat $n$-torus.

\begin{ex}
A square $Q\subset \matR^2$ is a Coxeter polygon and determines a reflection group $\Gamma$. What is the minimum index of a torsion-free subgroup $\Gamma' < \Gamma$? Which topological surfaces $\matR^2/_{\Gamma'}$ do we get?
\end{ex}


\subsection{Real projective spaces} 
We now exhibit some elliptic manifolds. Every elliptic manifold is covered by $S^n$ and is hence compact and has finite fundamental group (because coverings between compact manifolds have finite degree). \index{$\matRP^n$}

An important example is the real projective space $\matRP^n = S^n/_\Gamma$ where $\Gamma$ is the order-two group generated by the antipodal map $\iota (x) = -x$. 

\begin{ex}
For every $p\in S^n$, the Dirichlet domain $D(p)$ of $\Gamma$ is the hemisphere centred at $p$.
\end{ex}
The two-dimensional case is shown in Figure \ref{domini:fig}-(right). The only elliptic surfaces are $S^2$ and $\matRP^2$ in virtue of the following.
\begin{prop}
In even dimension $n$ the only elliptic manifolds are $S^n$ and $\matRP^n$.
\end{prop}
\begin{proof}
Let $M=S^n/_\Gamma$ be an elliptic manifold. Every matrix in $\SO(n+1)$ has an eigenvalue $+1$ because $n$ is even (exercise) and hence acts in $S^n$ with a fixed point. Therefore $\Gamma$ contains no non-trivial orientation-preserving isometries, and since these form a group of index at most two, either $\Gamma$ is trivial or is generated by an orientation-reversing fixed-point free involution in $O(n+1)$, and $-I$ is the only such element (exercise).
\end{proof}
