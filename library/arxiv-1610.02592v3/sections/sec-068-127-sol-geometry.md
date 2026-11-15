---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-068-127-sol-geometry
section_title: "Sol geometry"
section_number: 12.7
pages: 404-408
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.803
latex_coverage_ratio: 0.996
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
The $\Sol$ geometry is the least symmetric one among the eight. It has a bundle structure, but with a one-dimensional basis: it is a $\matR^2$-bundle over $\matR$. Again, the geometry is fully governed by a Lie group $\Sol$.\index{$\Sol$ geometry}


\subsection{The Lie group Sol}
The Lie group $\Sol$ is the space $\matR^3$ equipped with the following operation
$$(x,y,z)\cdot(x',y',z') = (x+ e^{-z}x', y+e^zy', z+z').$$
\begin{ex} \label{Sol:conti:ex}
We have
\begin{align*}
(x,y,z)^{-1} & = (-xe^z, -ye^{-z}, -z), \\
[(x,y,z),(x',y',z')] & = \big(x(1\!-\!e^{-z'}) - x'(1\!-\!e^{-z}), y(1\!-\!e^{z'}) - y'(1\!-\!e^z), 0\big), \\
[(x,y,z), (x',y',0)] & = \big(- x'(1-e^{-z}), - y'(1 - e^z), 0\big). \
\end{align*}
\end{ex}
The subgroup $\matR^2$ consisting of all elements $(x,y,0)$ is the centre of $\Sol$ and by setting $p(x,y,z)=z$ we get an exact sequence
$$0 \longrightarrow \matR^2 \longrightarrow \Sol \stackrel p \longrightarrow \matR \longrightarrow 0.$$
Therefore $\Sol$ is a plane bundle over $\matR$. Exercise \ref{Sol:conti:ex} implies the following.
\begin{ex} We have $[\Sol, \Sol] = \matR^2$ and hence $\Sol$ is solvable. However $[\Sol, \matR^2] = \matR^2$ and hence $\Sol$ is not nilpotent.
\end{ex}

We define a Riemannian metric on $\Sol$ by assigning the scalar product
$$\begin{pmatrix}
e^{2z} & 0 & 0 \\
0 & e^{-2z} & 0 \\
0 & 0 & 1
\end{pmatrix}
$$
to the point $(x,y,z)$. The metric is left-invariant and every plane $z=k$ is isometric to the Euclidean $\matR^2$. This is the geometry with the smallest amount of symmetries.

We remark that the metric tensor has unit determinant at every point: therefore the volume form on $\Sol$ is the standard one on $\matR^3$.

The non-zero Christoffel symbols at $(x,y,z)$ are
$$\Gamma^1_{13} = \Gamma^1_{31} = 1,$$
$$\Gamma^2_{23} = \Gamma^2_{32} = -1,$$
$$\Gamma^3_{11} = -e^{2z}, \quad \Gamma^3_{22} = e^{-2z}.$$
The Ricci tensor is
$$\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -2
\end{pmatrix}.
$$
The average value of the sectional curvatures of the planes containing $v\in T_{(x,y,z)} \Sol$ ranges from $-1$ to $0$, and is minimal when $v=(0,0,\pm 1)$.


\subsection{Sol geometry}
We start with a simple exercise.
\begin{ex} \label{D8:ex}
The eight maps 
$$(x,y,z) \mapsto (\pm x, \pm y,z), \qquad (x,y,z) \mapsto (\pm y, \pm x, -z)$$
are isometries and form the dihedral group $D_8$. The orientation-preserving ones form the subgroup $D_4 = \matZ_2 \times \matZ_2$.
\end{ex}
Let $\Iso_*(\matR^2) < \Iso(\matR^2)$ be the subgroup consisting of all maps $v\mapsto \pm v +b$. It has two components, one being the translations $\matR^2$.
\begin{prop}
Every isometry of $\Sol$ preserves the plane bundle and induces an isometry of $\matR$. We have
$$0 \longrightarrow \Iso_*(\matR^2) \longrightarrow \Iso^+(\Sol) \stackrel p \longrightarrow \Iso(\matR) \longrightarrow 0.$$
The group $\Iso^+(\Sol)$ has four components, one of which is $\Sol$ acting by left-multiplication. 
\end{prop}
\begin{proof}
The group $\Sol$ acts transitively and freely on $\Sol$ itself, and to conclude it suffices to check that the stabiliser of the origin $0$ is the dihedral $D_4$ described in Exercise \ref{D8:ex}. 

The Ricci tensor tells us that an isometry fixing a point also fixes the vertical axis and the horizontal plane. Therefore the vertical unitary constant vector field $X=(0,0,1)$ is preserved up to sign by any isometry of $\Sol$. The covariant differentiation $v \mapsto \nabla_v X$ defines an endomorphism of $T_p \Sol$ for all $p \in \Sol$. We have $\nabla_{e_i} X = \Gamma_{i3}^ke_k$ and therefore the endomorphism is
$$\begin{pmatrix}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 0 
\end{pmatrix}.
$$
The three coordinate axis are precisely the eigenvectors of the endomorphism, and being intrinsically defined they are preserved by every isometry. Therefore the orientation-preserving stabiliser of a point is $D_4$.
\end{proof}


\begin{prop}
A discrete group $\Gamma < \Iso^+(\Sol)$ is cofinite if and only if both $p(\Gamma)$ and $\Gamma \cap \ker p$ are discrete and cofinite.
\end{prop}
\begin{proof}
If $p(\Gamma)$ is discrete we get
$$\Vol \big(\Sol/_\Gamma \big) = {\rm Length}(\matR/_{p(\Gamma)}) \times \Area\big(\matR^2/ _{\Gamma \cap \ker p}\big). $$
This formula is proved as above by taking a fundamental domain for $p(\Gamma)$. We now prove that $p(\Gamma)$ is in fact discrete (since $\Gamma$ is).

Up to taking an index-four subgroup we suppose that $\Gamma < \Sol$. 
If $\gamma \in \Sol$ does not lie in $\matR^2$, then it fixes a vertical line. To prove that, note that $\gamma = (x,y,z)$ acts on $\matR^3$ as an affine transformation, which permutes the vertical lines and acts on $\matR^2$ as $(x',y') \mapsto (x+e^{-z}x', y+e^zy')$. If $z \neq 0$ this map has a fixed point (because $1$ is not an eigenvalue of its linearisation).

If $\Gamma$ is abelian, either it is contained in $\matR^2$ or it fixes a vertical line: in both cases we get a discrete $p(\Gamma)$. If $\Gamma$ is non-abelian, then $[\Gamma, \Gamma]<\matR^2$ is non-trivial so $\Gamma$ contains a non-trivial element $\gamma \in \matR^2$ and another $\eta \not \in \matR^2$. The elements $\gamma$ and $\eta\gamma\eta^{-1}$ are both in $\matR^2$ and independent, hence $\matR^2 /_{\Gamma \cap \ker p}$ is compact. This implies easily that $p(\Gamma)$ is discrete (since $\Gamma$ is).
\end{proof}

We now classify the manifolds modelled on $\Sol$. Recall that every semi-bundle is doubly covered by a canonical bundle. A torus bundle is \emph{of Anosov type} if its monodromy is Anosov. A torus semi-bundle is of Anosov type if its double-covering is.

\begin{prop} \label{Sol:bundle:prop}
The interior of a compact orientable manifold $M$ admits a finite-volume complete $\Sol$ geometry if and only if it is a torus (semi-)bundle of Anosov type.
\end{prop}
\begin{proof}
If $\interior M= \Sol/_\Gamma$ has finite volume, then both $\Gamma \cap \ker p$ and $p(\Gamma)$ are discrete and cofinite. The horizontal foliation of $\Sol$ into Euclidean planes $z=k$ is preserved by $\Gamma$ and projected to a surface bundle over the 1-orbifold $\matR /_{p(\Gamma)}$, which is either $S^1$ or an interval. The fibres are flat and have finite area, hence they are tori or Klein bottles. 

If $p(\Gamma)$ acts by translations, then $M$ is a torus bundle with an Anosov monodromy $\pm\matr {e^{-z}} 0 0 {e^z}$ for some $z>0$. If $M$ is a semi-bundle, this holds on its double-covering.

Conversely, let $M_A$ be a torus bundle with Anosov monodromy $A\in \SLZ$. We have $M_A = \matR^3/_\Gamma$ where $\Gamma$ is generated by the affine maps
$$(x,y,z) \mapsto (x+1,y,z), \quad (x,y,z) \mapsto (x,y+1,z), \quad (\bar x,z) \mapsto 
(A\bar x, z+h)$$
where $\bar x = (x,y)$ and $h>0$ is any positive number. A linear isomorphism $\psi$ of $\matR^2$ conjugates $A$ into a diagonal matrix $\pm\matr {e^{-a}} 0 0 {e^a}$ for some $a>0$ and transforms the generators into
$$(\bar x,z) \mapsto (\bar x +\bar v ,z), \ (\bar x,z) \mapsto (\bar x + \bar w, z), \ (x,y,z) \mapsto (\pm e^{-a}x, \pm e^{a}y, z+h)$$
where $\bar v = \psi(1,0)$ and $\bar w = \psi(0,1)$. If $\tr A>0$ and $h=a$ these maps are left-multiplications by the following elements of $\Sol$:
$$(\bar v,0), \quad (\bar w,0), \quad (\bar 0,a)$$
where $\bar 0 = (0,0)$, and we are done. If $\tr A <0$ we compose the third generator with the isometry $(x,y,z)\mapsto (-x,-y,z)$. 

If $M$ is a semi-bundle double-covered by $M_A$, we represent it as $\matR^3/_{\Gamma'}$ where $\Gamma'$ is generated by the group $\Gamma$ representing $M_A$ plus the element
$$(x,y,z) \mapsto \left(x+\frac 12, -y, -z\right)$$
which will be transformed via $\psi$ into an isometry of $\Sol$.
\end{proof}

\begin{cor} \label{Sol:not:Nil:cor}
If a closed three-manifold $M$ has a $\Sol$ geometry, then $\pi_1(M)$ is virtually solvable but not virtually nilpotent.
\end{cor}
\begin{proof}
It is virtually solvable because $\Sol$ has finite index in $\Iso^+(\Sol)$. The proof of Proposition \ref{Sol:bundle:prop} shows that
up to finite index $M=\Sol/_\Gamma$ and $\Gamma$ is generated by
$$(\bar v,0), \quad (\bar w,0), \quad (\bar 0,a).$$
Exercise \ref{Sol:conti:ex} implies that $[(\bar 0,a), (\bar v,0)] = (\bar v',0)$ for some $\bar v' \neq 0$ and hence $\Gamma$ is not nilpotent. This holds for any $\Gamma$ of this kind, and therefore $\Gamma$ is not virtually nilpotent, either.
\end{proof}


\section{Summary}
We have proudly completed the proof of Theorem \ref{Seifert:geometrisation:teo}. We state that theorem again here:

\begin{teo} 
A closed orentable 3-manifold has a geometric structure modelled on one of the following six geometries:
$$S^3,\ \matR^3,\ S^2\times \matR,\ \matH^2\times \matR,\ \Nil,\ \widetilde{\SL_2}$$
if and only if it is a Seifert manifold of the appropriate commensurability class, as prescribed by Table \ref{Seifert:geometry:table}. It has a $\Sol$ geometric structure if and only if it is a torus (semi-)bundle of Anosov type.
\end{teo}

We can deduce that the eight geometries are mutually exclusive:

\begin{prop}
Two closed 3-manifolds admitting different geometries are not diffeomorphic, and not even commensurable.
\end{prop}
\begin{proof}
We already know that the six Seifert geometries form six distinct commensurability classes. A manifold of type $\Sol$ is not Seifert by Proposition \ref{torus:bundle:prop}. A closed hyperbolic manifold is neither Seifert nor Sol because its fundamental group is infinite and does not contain an infinite normal abelian subgroup by Corollary \ref{normal:abelian:cor} (as opposite to the other geometries, see Proposition \ref{infinite:K:prop}).

Two manifolds having different geometries cannot be commensurable, since a common finite cover would inherit both geometries. 
\end{proof}

In fact one can tell the geometry of the manifold directly from its fundamental group. 

\begin{prop}
Let $M$ be a closed manifold modelled on one $\matX$ of the eight geometries; this flowchart shows how to determine $\matX$ from $\pi_1(M)$:
\begin{itemize}
\item if $\pi_1(M)$ is finite, then $\matX = S^3$; otherwise
\item if $\pi_1(M)$ is virtually cyclic, then $\matX = S^2\times \matR$; otherwise
\item if $\pi_1(M)$ is virtually abelian, then $\matX = \matR^3$; otherwise
\item if $\pi_1(M)$ is virtually nilpotent, then $\matX = \Nil$; otherwise
\item if $\pi_1(M)$ is virtually solvable, then $\matX = \Sol$; otherwise
\item if $\pi_1(M)$ contains a normal cyclic group $K$, then:
\begin{itemize}
\item if a finite-index subgroup of the quotient lifts, then $\matX = \matH^2 \times \matR$, 
\item otherwise $\matX = \widetilde{\SL_2}$; 
\end{itemize}
\item otherwise $\matX = \matH^3$.
\end{itemize}
\end{prop}
\begin{proof}
The virtually abelian cases were settled in Section \ref{virtually:abelian:subsection}. The $\Nil$ and $\Sol$ geometries were considered by Corollaries \ref{Nil:is:Nil:cor} and \ref{Sol:not:Nil:cor}. 

If $\matX = \matH^2\times \matR$ or $\widetilde{\SL_2}$ then 
$\pi_1(M)$ surjects onto $\pi_1(S)$ for some closed hyperbolic surface $S$. 
This implies that $\pi_1(M)$ is not solvable, for otherwise
(by Propositions \ref{subgroup:prop} and \ref{solvable:normal:prop})
the group $\pi_1(S)$ would also be, and hence it would contain a normal cyclic subgroup, contradicting Corollary \ref{normal:abelian:cor}.

If $\matX = \widetilde{\SL_2}$ then $\pi_1(S) = \pi_1(M)/_K$ and no finite-index subgroup of $\pi_1(S)$ can lift to $\pi_1(M)$ by Proposition \ref{SL2:no:lift:prop}.

Finally, if $\matX=\matH^3$ then $\pi_1(M)$ contains no normal cyclic group $K$ by Corollary \ref{normal:abelian:cor} again.
\end{proof}

The boundary case is slightly different. Of the eight geometries, only three produce non-compact finite-volume complete orientable manifolds:
$$\matH^3,\ \matH^2 \times \matR,\ \widetilde{\SL_2}.$$
These non-compact finite-volume manifolds are diffeomorphic to the interior of a compact manifold $M$ with boundary consisting of tori.

\begin{teo}
Let $M$ be a compact orientable 3-manifold with boundary consisting of tori. The following are equivalent:
\begin{itemize}
\item $M$ has a finite-volume complete $\matH^2 \times \matR$ structure,
\item $M$ has a finite-volume complete $\widetilde{\SL_2}$ structure,
\item $M$ is Seifert with $\chi<0$.
\end{itemize}
\end{teo}

In contrast with the closed case, a non-closed $M$ may admit two different geometric structures of Seifert type. On the other hand, a manifold $M$ cannot admit both a hyperbolic and a Seifert structure.
