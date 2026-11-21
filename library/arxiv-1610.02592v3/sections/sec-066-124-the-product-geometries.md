---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-066-124-the-product-geometries
section_title: "The product geometries"
section_number: 12.4
pages: 391-394
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.851
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
The eight three-dimensional geometries include the three isotropic ones, plus five more. Among the five non-isotropic geometries, two are products of lower-dimensional geometries. We analyse them here.


\subsection{$S^2 \times \matR$ geometry.}
We equip $S^2\times \matR$ with the product metric. The product $S^2\times \matR$ is the poorest of the eight geometries, in the sense that there are very few manifolds modelled on $S^2\times \matR$. 

Recall that the sectional curvature is a number assigned to every plane in the tangent space of every point $p\in S^2 \times \matR$. One such plane is \emph{horizontal} if it is tangent to the $S^2$ factor and \emph{vertical} if it contains the line tangent to the $\matR$ factor.

\begin{prop}
The sectional curvatures of horizontal and vertical planes are $1$ and $0$, respectively.
\end{prop}
\begin{proof}
Let $\gamma \subset S^2$ be a closed geodesic. The surfaces $S^2 \times y$ and $\gamma\times \matR$ are totally geodesic, because they are fixed by some isometric reflections of $S^2\times \matR$. Therefore the sectional curvatures of horizontal and vertical planes equal the gaussian curvatures of these surfaces, which are $1$ and $0$.
\end{proof}

\begin{prop}
We have
$$\Iso(S^2\times \matR) = \Iso(S^2) \times \Iso(\matR).$$
\end{prop}
\begin{proof}
We certainly have the inclusion $\supset$, which gives to every point $x\in S^2\times \matR$ a stabiliser in $\Iso^+(S^2\times \matR)$ isomorphic to $\SO(2) \rtimes C_2$, a proper maximal subgroup of $\SO(3)$ by Proposition \ref{subgroups:SO3:prop}. 

If there were more isometries that that, there would be more fixing $p$ since they act transitively on $S^2\times \matR$ and the stabiliser would be the whole of $\SO(3)$, a contradiction because the sectional curvature of $S^2\times \matR$ is not constant.
\end{proof}
Since the isometry groups of $S^2$ and $\matR$ have two connected components each, the group $\Iso(S^2\times \matR)$ has four connected components, two of which are orientation-preserving.

\begin{prop}
An orientable manifold $M$ admits a finite-volume $S^2\times \matR$ geometry $\Longleftrightarrow$ $M$ is a closed Seifert manifold with $e= 0$ and $\chi>0$. 
\end{prop}
\begin{proof}
The closed Seifert manifolds with $e=0$ and $\chi>0$ are
just $S^2\times S^1$ and $\matRP^2 \timtil S^1$, and they are diffeomorphic to $(S^2\times \matR)/_{\Gamma}$ where $\Gamma$ is generated respectively by 
$$\big\{(\id, \tau)\big\}, \qquad \big\{(\iota, r), (\iota, r')\big\}$$
where $\tau$ is any translation, $\iota$ is the antipodal map and $r,r'$ are reflections with respect to distinct points in $\matR$.

Conversely, pick an orientable $M = (S^2\times S^1)/_\Gamma$. The discrete subgroup $\Gamma < \Iso(S^2) \times \Iso(\matR)$ preserves the foliation into spheres $S^2\times \{x\}$ which descends into a foliation into spheres and/or projective planes for $M$. Therefore $M$ decomposes into orientable interval bundles $S^2\times I$ and $\matRP^2\timtil I$, and is hence either $S^2\times S^1$ or $\matRP^2 \timtil S^1$.
\end{proof}


\subsection{$\matH^2 \times \matR$ geometry}
We give $\matH^2 \times \matR$ the product metric. The discussion of the previous section applies as is to this case, showing that horizontal and vertical planes in the tangent spaces have sectional curvature $-1$ and $0$. This in turn implies that
$$\Iso(\matH^2\times \matR) = \Iso(\matH^2) \times \Iso(\matR)$$
has four connected components, two being orientation-preserving. It is convenient to write the exact sequence
$$0 \longrightarrow \Iso(\matR) \longrightarrow \Iso(\matH^2\times \matR) \stackrel p \longrightarrow \Iso(\matH^2) \longrightarrow 0.$$
A discrete group $\Gamma<\Iso(X)$ is \emph{cofinite} if $X/_\Gamma$ has finite volume.

\begin{prop} \label{H2R:prop}
A discrete group $\Gamma < \Iso(\matH^2 \times \matR)$ is cofinite if and only if both $p(\Gamma)$ and $\Gamma \cap \ker p$ are discrete and cofinite.
\end{prop}
\begin{proof} 
If $p(\Gamma)$ is discrete we get
\begin{equation} \label{volume:product:eqn}
\Vol \big((\matH^2\times \matR)/_\Gamma \big) = \Area(\matH^2/_{p(\Gamma)}) \times {\rm Length}\big(\matR/ _{\Gamma \cap \ker p}\big). 
\end{equation}
This surprisingly simple formula is proved by picking a fundamental domain $D\subset \matH^2$ for $p(\Gamma)$ and noticing that 
$$\Vol \big((\matH^2\times \matR)/_\Gamma \big) = \Vol\big(p^{-1}(D)/_{\Gamma \cap \ker p}\big).$$ 
We deduce that $\Gamma$ is cofinite if and only if both $p(\Gamma)$ and $\Gamma \cap \ker p$ are. 

If $p(\Gamma)$ is not discrete, we prove that $\Gamma$ cannot be cofinite. Up to replacing $\Gamma$ with an index-four subgroup we may suppose 
$$\Gamma < \Iso^+(\matH^2) \times \Iso^+(\matR) = \Iso^+(\matH^2) \times \matR.$$
Pick a neighbourhood $U\subset \Iso^+(\matH^2) \times \matR$ of $e$ such that $[U,U] \subset U$ and $U\cap\Gamma = \{e\}$. Let $f,g \in \Gamma$ be two elements. 
We now prove that if $p(f), p(g) \in p(U)$ then $f$ and $g$ commute.
We note that the commutator $[f,g]$ depends only on the images $p(f)$ and $p(g)$, and since they lie in $p(U)$ we may suppose that $f,g\in U$ and get $[f,g]\in U\cap \Gamma$, which must be trivial.

The elements in $p(\Gamma)\cap p(U)$ commute. Two non-trivial elements in $\Iso^+(\matH^2)$ commute if and only if they are both hyperbolic, parabolic, or elliptic fixing the same line, point in $\partial \matH^2$, or point in $\matH^2$. Therefore all the isometries in $p(\Gamma)\cap p(U)$ are of the same type and fix the same line or point.

Analogously, for every $f \in \Gamma$ we pick a neighbourhood $U_f$ of $e$ such that $[f, U_f] \subset U$ and conclude that $f$ commutes with all the elements in $\Gamma $ projecting to $p(U_f)$. (There are non-trivial such elements since $p(\Gamma)$ is not discrete.) Therefore $p(f)$ also fixes the same line or point as above.

We have proved that $p(\Gamma)$ fixes a line, a horocycle, or a point in $\matH^2$ and hence fixes its inverse image in $\matH^2 \times \matR$ which is a line or a Euclidean plane. Moreover $\Gamma$ acts freely and proper discontinuously on it: hence $\Gamma =\matZ$ or $\matZ^2$ up to finite index and it is easy to deduce that $\Gamma$ is not cofinite.
\end{proof}

\begin{cor} \label{H2R:cor}
If the interior of a compact orientable manifold $M$ admits a finite-volume complete $\matH^2\times \matR$ geometry then $M$ is a Seifert manifold with $\chi<0$. If $M$ is closed then also $e = 0$.
\end{cor}
\begin{proof}
We have $\interior M = (\matH^2\times \matR)/_\Gamma$ with $\Gamma$ cofinite: by Proposition \ref{H2R:prop} the group $\Gamma \cap \ker p$ quotients every line $\{x\}\times \matR$ to a circle in $M$, giving a Seifert fibration $M\to S$ onto the finite-area orbifold $S=\matH^2/_{p(\Gamma)}$. We have $\chi(S)<0$, and either $e(M)=0$ or $\partial M \neq \emptyset$ because $\matH^2 \times y$ projects to a section for $M\to S$.
\end{proof}

We now prove the converse of Corollary \ref{H2R:cor}.
\begin{prop}
If $M$ is a Seifert manifold with  $\chi<0$ and either $\partial M \neq \emptyset$ or $e = 0$, the interior of $M$ admits a finite-volume complete $\matH^2\times S^1$ geometry.
\end{prop}
\begin{proof}
By hypothesis there is a section $\Sigma$ of $M\to S$, which is the fibre of a bundle $M\to O$ over a 1-orbifold $O$, see Section \ref{Seifert:fibers:subsection}. The two structures give two exact sequences
\begin{align*}
0 \longrightarrow K \longrightarrow \pi_1(M) & \stackrel f\longrightarrow \pi_1(S) \longrightarrow 0, \\
0 \longrightarrow \pi_1(\Sigma) \longrightarrow \pi_1(M) & \stackrel g\longrightarrow \pi_1(O) \longrightarrow 0.
\end{align*}
Since $\chi(S)<0$ we may write $S= \matH^2/_\Gamma$ and identify $\pi_1(S)$ with $\Gamma < \Iso(\matH^2)$. Analogously we consider $\pi_1(O)$ inside $\Iso(\matR)$.
The map 
$$(f,g) \colon \pi_1(M) \longrightarrow \Iso(\matH^2) \times \Iso(\matR)$$
is injective and its image is discrete and acts freely on $\matH^2\times \matR$, inducing a finite-volume $\matH^2 \times \matR$ structure on $M$.
\end{proof}
