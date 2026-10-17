---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-004-23-geometric-aspects
section_title: "Geometric aspects"
section_number: 2.3
pages: 8-9
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.981
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangulated cusped hyperbolic 3-manifold (together with some further choices)"
---
\label{sub.geometric}

In this section, we discuss some geometric aspects of Theorem~\ref{thm.1} related
to the choice of the shapes $z$ in a Neumann--Zagier datum. Let us fix an ideal
triangulation $\calT$. A solution $z \in (\BC\setminus\{0,1\})^N$ to the
Neumann--Zagier equations gives rise, via a developing map, to a representation
$\rho_z: \pi_1(M) \to \PSL_2(\BC)$. For a detailed discussion, see the appendix
of~\cite{BoydII}. However, not every representation $\rho: \pi_1(M) \to \PSL_2(\BC)$ is
``seen'' by $\calT$, that is, is in the image of the map $z \to \rho_z$.
What's more, if $\rho$ is in the image of the above map and we do a 2--3 Pachner
move on the triangulation, it may no longer be in the image of the map corresponding
to the new triangulation. The reason is that the shapes of the two triangulations
are related by a rational map, which may send a complex number different from $0$
and $1$ to $0$, $1$ or $\infty$. To phrase the problem differently, every two ideal
triangulations (each with at least two tetrahedra, as we will always assume) of
a 3-manifold with non-empty boundary are related by a sequence of 2--3 Pachner
moves~\cite{Matveev,Piergallini}. However, it is not known that the set of
ideal triangulations that see the discrete faithful representation
$\rho^\geom : \pi_1(M) \to \PSL_2(\BC)$ is connected under 2--3 Pachner moves,
nor is it known whether the set of nondegenerate NZ data is connected under
2--3 Pachner moves. 

A solution to these issues was found in~\cite{DG}, and this was used to
prove the topological invariance of the 1-loop function, and was also used
in~\cite{GHRS} to prove the topological invariance of the 3D-index. Let us recall
the geometric details here. Every cusped hyperbolic 3-manifold $M$ (complete,
finite volume) has a canonical ideal cell decomposition whose cells are
3-dimensional convex ideal polytopes given by Epstein--Penner~\cite{EP}. It is easy to
see that every convex ideal polyhedron can be triangulated into ideal
tetrahedra by connecting an ideal vertex to all other ideal vertices (thus
reducing the problem to the ideal cone of an ideal polygon), and then triangulating
further the ideal polygon into ideal triangles. Doing so, the triangulation of
the common faces of the 3-dimensional convex ideal polytopes may not match, in
which case one can pass from one triangulation of a polygonal face to another by
adding flat tetrahedra. 

The question is whether every two such triangulations are related by a sequence of
2--3 moves. This is a combinatorial problem of convex geometry, which we summarize
below. For a detailed discussion, the reader may consult the book~\cite{LRS}
and references therein.

Fix a convex polytope $P$ in $\BR^d$. One can consider the set of
triangulations of $P$. When $d=2$, $P$ is a polygon and it is known that 
every two triangulations are related by a sequence of flips. For general
$d$, flips are replaced by {\em geometric bistellar moves}. When $d \geq 5$,
it is known that the graph of triangulations (with edges given
by geometric bistellar flips) is not connected, and has isolated vertices.
For $d=3$, it is not known whether the graph is connected.

The situation is much better when one considers {\em regular triangulations}
of $P$. In that case, the corresponding graph of regular triangulations
is connected and, in fact, it is the edge set of the {\em secondary polytope} of
$P$. When $d=3$ and $P$ is convex and in general position, then the only
geometric bistellar move is the 2--3 move where the added edge that appears in
the move is an edge that connects two vertices of $P$. When $d=3$ and $P$ is
not in general position, the same conclusion holds as long as one allows for
tetrahedra that are flat, i.e., lie on a 2-dimensional plane.

Returning to the Epstein-Penner ideal cell decomposition, let $\calT^{\mathrm{EP}}$
denote a regular ideal triangulations of the canonical ideal cell decomposition
of $M$. (For a detailed discussion of this set, see also~\cite[Sec.6]{GHRS}).
The set $\{\calT^{\mathrm{EP}}\}$ of regular ideal triangulations
is connected by 2--3 Pachner moves. Moreover, such triangulations see $\rho^\geom$
since by the geometric construction, the shapes are always nondegenerate, i.e.,
not equal to $0$ or $1$ and in fact always have nonnegative
(though sometimes zero) imaginary part.

Finally, we need to show that $\det(\Lambda)$ is nonzero. This follows from the
fact that\\ $\det(B)\det(\Lambda)=\det(-A+B\diag(1/(1-z_j))$ equals (up to
multiplication by a monomial in $z$ and $z''$) to the 1-loop invariant
of~\cite[Sec.1.3]{DG}. The nonvanishing of the latter follows from
Thurston's hyperbolic Dehn surgery theorem~\cite{Th}, which implies that
$\rho^\geom \in X_M^\geom \cup P_M$ is an isolated smooth point of the geometric
component $X^\geom_M$ of the $\PSL_2(\BC)$-character variety of $M$, intersected
with the locus $P_M$ of boundary-parabolic $\PSL_2(\BC)$-representations, i.e.,
representations $\rho$ satisfying $\mathrm{tr}(\rho(\gamma))^2=4$ for all peripheral
elements $\gamma \in \pi_1(M)$. 
Since the 1-loop invariant is the determinant of the Hessian of the defining
NZ equations of $\rho^\geom$, it follows that the 1-loop invariant is nonzero.
