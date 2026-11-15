---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-012-9-some-applications-to-combinatorial-geometry
section_title: "Some applications to combinatorial geometry"
section_number: 9
pages: 22-23
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 1.0
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#someapps label="someapps"}

A well-known theorem of Steinitz says that every three-connected planar graph can be realized as the $1$-skeleton of a convex polyhedron in $R^{3}$, while a famous theorem of Aleksandrov states that every Euclidean metric on $S^{2}$ with positively curved cone-points can be realized as the induced metric on the surface of a convex polyhedron in $R^{3}$. Below, we show a negative result, which should be compared with the final example of [@rit]:

::: theorem
[]{#badtri label="badtri"} There exist infinitely many triangulations of $S^{2}$ which can not be realized as a Delaunay triangulation with respect to the cone-points of any Euclidean metric on $S^{2}$ with positively curved cone-points.
:::

First a definition:

::: definition
Let $T$ be a triangulation. The *stellation* $s(T)$ of $T$ is the complex obtained by replacing each face $ABC$ of $T$ by three faces $AOB$, $AOC$, and $BOC$.
:::

Theorem [\[badtri\]](#badtri){reference-type="ref" reference="badtri"} follows immediately from the following claim.

::: claim
Let $T$ be any triangulation of $S^{2}$ with at least eight faces. Then the stellation $s(T)$ of $T$ is not combinatorially equivalent to the Delaunay triangulation of any Euclidean metric on $S^{2}$ with positively curved cone-points, where the cone-points correspond to vertices of $s(T)$.
:::

::: proof
*Proof.* Let an *old* vertex of $s(T)$ be one that was already a vertex of $T$, while a *new* vertex be one that was added at stellation. The set $\mathcal{N}$ of new vertices of $s(T)$ corresponds to the set of faces of $T$. For any vertex $v$, recall that $C(v)$ denotes the cone angle at $v$. The Gauss-Bonnet theorem tells us that $$\sum_{v\in V(s(T))}(2\pi - C(v)) = 4\pi.$$ Or, recombining the terms: $$\label{gaussb}
\sum_{v\in V(s(T))}C(v) = 2\pi (|V(s(T))| - 2).$$ Note that every edge of $s(T)$ is incident to an old vertex, and to at most one new vertex. Combining this observation with Lemma [\[cona\]](#cona){reference-type="ref" reference="cona"}, we see that for any *Delaunay* triangulation combinatorially equivalent to $s(T)$, it must be true that $$\label{badineq}
\sum_{v \in \{\mbox{old vertices of $s(T)$}\}} C(v) \geq 
\sum_{v \in \{\mbox{new vertices of $s(T)$}\}} C(v).$$ Combining Eq. [\[badineq\]](#badineq){reference-type="ref" reference="badineq"} with Eq. [\[gaussb\]](#gaussb){reference-type="ref" reference="gaussb"}, it follows that $$\label{badderineq}
\sum_{v \in \{\mbox{old vertices of $s(T)$}\}} C(v) \geq \pi (|V(s(T)) - 
2).$$ Note now that $|V(s(T))| = |V(T)| + |F(T)|$. By a standard computation using Euler's formula for triangulations of the sphere, we know that $|V(T)| = \frac12 |F(T)| + 2,$ thus $|F(T)| = 2 |V(T)| - 4.$ Thus, $$\label{neww}
|V(s(T))-2| = 3 |V(T)| - 6.$$ Equations [\[neww\]](#neww){reference-type="ref" reference="neww"} and [\[badderineq\]](#badderineq){reference-type="ref" reference="badderineq"} together imply that the *average* cone angle at an old vertex of $s(T)$ is at least $\pi(3 |V(T)| - 6)/|V(T)| = 3 \pi - 6/|V(T)|.$ If $|V(T)| > 6$ it follows that the average cone angle at an old vertex is greater than $2\pi$, which contradicts the assumption that the cone angles were positively curved. ◻
:::
