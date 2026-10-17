---
doc_id: arxiv-math-9907032v1
doc_title: "arXiv:math/9907032v1 [math.GT] 6 Jul 1999"
section_id: sec-012-9-some-applications-to-combinatorial-geometry
section_title: "Some applications to combinatorial geometry"
section_number: 9
pages: 22-27
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.707
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

# Linear hyperbolic structures on $3$-manifolds {#lhyp}

As explained in [@rvol], the study of Euclidean triangulations on surfaces is essentially equivalent to the study of hyperbolic ideally triangulated complexes, which are combinatorially just cones over the triangulated surface. Hence, the contents of this section are closely related to the subject-matter of much of the rest of the paper, in more than just the linear programming approach.

Consider a $3$-manifold $M^3$ with boundary a collection of tori, and consider a topological ideal triangulation $T$ of $M^3$. We would like to know when there is a complete hyperbolic structure on $M^3$, such that $T$ is a geometric ideal triangulation. In general, this is a very difficult question, at least as hard as Thurston's hyperbolization conjecture (since even if $M^3$ admits a hyperbolic structure of finite volume, there might not be an ideal triangulation combinatorially equivalent to $T$). However, below we will consider a "linear" version of the question above.

Recall that an ideal simplex $S$ in $\mathbf{H}^3$ has the properties that

Euclidean links

:   The link of each vertex is a Euclidean triangle.

Equal opposite dihedral angle

:   If $S = ABCD$, then the dihedral angles at the edges $AB$ and $CD$ are equal (this is actually a consequence of the condition on the links).

An ideal simplex is thus determined by the angles of the link of any one of its vertices (all links are easily seen to be the same).

Now, if $T$ comes from a genuine hyperbolic structure, it must be true that the sum of the dihedral angles incident to the edges of $T$ must equal $2\pi$, and so for $T$ to correspond to such a structure, the following linear program must have a strictly positive solution:

The variables

:   These are the dihedral angles of the simplices. For each simplex $S$ we use three angles $\alpha, \beta, \gamma$ corresponding to the angles of the link of one vertices of $S$.

Simplex conditions

:   For each simplex $S$, the sum of the dihedral angles is equal to $\pi$: $$f_S: \alpha + \beta + \gamma = \pi.$$

Edge conditions

:   For each edge $e$ of $T$ the sum of the dihedral angles of all simplices incident to $e$ equals $2\pi:$ $$f_e: \sum \lambda_i = 2\pi.$$

::: definition
We say that if the above linear program has a non-negative solution, then the pair $(M^3, T)$ admits a *weak linear hyperbolic structure*. If the linear program has a strictly positive solution, then we say that the pair $(M^3, T)$ admits a *linear hyperbolic structure.*
:::

It is clear that the existence of a linear hyperbolic structure is, in general, no guarantee of the existence of a genuine hyperbolic structure, since the linear conditions do not preclude "Dehn surgery" singularities, as well as translational singularities along edges of $T$ (see [@thgt3m; @nz] for discussion). Conversely, as remarked above, the existence of a complete hyperbolic structure on $M^3$ is no guarantee that there is a positively oriented ideal triangulation combinatorially equivalent to $T$ (or, indeed, any positively oriented triangulation). However, linear hyperbolic structures have the advantage of being considerably more tractble.

::: theorem
[]{#hext label="hext"} In order for there to exist a weak linear hyperbolic structure for $(M^3, T)$, every normal surface with respect to $T$ must have non-negative Euler characteristic. In order for there to exist a linear hyperbolic structure for $(M^3, T)$, every non-boundary-parallel normal surface with respect to $T$ must have strictly negative Euler characteristic.
:::

::: proof
*Proof.* We will use the method of Section [\[suff\]](#suff){reference-type="ref" reference="suff"}. First, let us write the dual program of the linear program (referred to as $L_h$ in the sequel) for weak hyperbolic structure: Our variables are $\{v_S\}$, where $S$ ranges over all the simplices of $T$, and $\{v_e\}$ where $S$ ranges over all the edges of $T$.

The dual program $L_h^*$ is:

::: description
Maximize $\sum_{S\in S(T)} v_S + 2 \sum_{e \in E(T)} v_e$.

Subject to $v_S + v_{e_1} + v_{e_2}\leq 0$ for all faces $S$ and pairs of opposite edges $e_1, e_2$.
:::

In order for the primal program to have a non-empty feasible region, the objective of the dual must be non-positive.

Consider now a normal surface $\mathcal{S}$ (see, eg, [@hack; @jaco; @hemion] for rudiments of normal surface theory). The surface $\mathcal{S}$ intersects each simplex $S$ in a collection of disks, which are combinatorially either triangles (cutting off one vertex of $S$ from the other three), or quadrilaterals (separating one pair of vertices from another). For each simplex $S$, define $t_S(\mathcal{S})$ to be the number of triangular components of $\mathcal{S} \cap S$, and $q_S(\mathcal{S})$ to be the number of quadrilateral components. For each edge $e$ of $T$, define $i_e(\mathcal{S})$ to be the number of intersections of $\mathcal{S}$ with $e$. The intersections of $\mathcal{S}$ with the simplices of $T$ induces a triangulation $\mathcal{T}$ of $S$, where each triangular disk contributes one triangle, and each quadrangle contributes two. Define $u_S(\mathcal{S})$ to be the number of triangles of $\mathcal{T}$ sitting inside a simplex $S$. Evidently, $u_S = t_S + 2
q_S$.

Note that, by Euler's formula, $\chi(\mathcal{S}) = \sum_{e \in E(T)}
i_e -\frac 12 \sum_{S \in S(T)} u_S$. This is seen to be very similar in form to the objective function of $L_h^*$, so let us set $v_S = - u_S$, and $v_e = i_e$.

::: lemma
[]{#normvar label="normvar"} The assignment of the variables as above satisfies the inequality constraints of $L_h^*$.
:::

::: proof
*of lemma.* We need to check that for $S$ a simplex and $e_1, e_2$ a pair of disjoint edges of $S$. We need to check that $$\label{normineq}
i_{e_1} + i_{e_2} \leq u_S.$$ By linearity, we need just check the inequality [\[normineq\]](#normineq){reference-type="ref" reference="normineq"} for connected components of $\mathcal{S} \cap S$. If that component is a triangle $t$, then $t$ contributes $1$ to $i_{e_1} + i_{e_2}$ (since a "normal triangle" intersects exactly one of each pair of opposite edge). Also, $t$ contributes $1$ to $u_S$, so for a triangular face, the right and left hand sides of ([\[normineq\]](#normineq){reference-type="ref" reference="normineq"}) are equal.

Suppose now we have a quadrilateral component $q$. It contributes $2$ to the right hand side of ([\[normineq\]](#normineq){reference-type="ref" reference="normineq"}). As for the left hand sides, $q$ hits two pairs of opposite sides of $S$, so if $e_1$ and $e_2$ is one of those pairs, then we have a contribution of $2$ to the left hand side, and otherwise we have a contribution of $0$. ◻
:::

::: remark
[]{#rmkkk label="rmkkk"} Notice that if $\mathcal{S}$ is such that all of the components of $\mathcal{S} \cap S$, for all $S\in S(T)$ are triangles, then all of the constraints of $L_h^*$ are equalities with the assignment of variables as above. Any such $\mathcal{S}$ is easily seen to be a union of boundary tori.
:::

Lemma [\[normvar\]](#normvar){reference-type="ref" reference="normvar"} concludes the proof of the "weak" part of Theorem [\[hext\]](#hext){reference-type="ref" reference="hext"}, since if any $\mathcal{S}$ had positive Euler characteristic, the program $L_h^*$ would have a positive objective, and thus the program $L_h$ would have no solution.

For the proof of the "strong part" we use the same trick as in Section [\[suff\]](#suff){reference-type="ref" reference="suff"}. Define new variables $\alpha^\prime = \alpha +
\epsilon$, *etc.* Our primal linear hyperbolicity program $L_s$ is now:

::: description
Minimize: $-\epsilon$

subject to face constraints $\alpha^\prime + \beta^\prime +
  \gamma^\prime + 3\epsilon = \pi.$

and to edge constraints $\sum_{\alpha^prime} + v(e) \epsilon =
  2\pi$, where $v(e)$ is the valence of $e$.
:::

The dual program $L_s^*$ is then

::: description
Maximize $\sum_{S\in S(T)} v_S + 2 \sum_{e \in E(T)} v_e$.

Subject to the old constraints $v_S + v_{e_1} + v_{e_2}\leq 0$ for all faces $S$ and pairs of opposite edges $e_1, e_2$.

and the new constraint $3\sum_{S \in S(T)} v_S + \sum_{e\in
    E(T)} v(e) v_E \leq -1.$
:::

In order for $(M^3, T)$ to be linearly hyperbolic, the objective must be strictly negative.

Observe that the sum of the left hand sides of the old constraints is *equal* to the left hand side of the new constraint. Indeed, each $v_S$ occurs three times (once for each pair of opposite edges), and each $v_e$ occurs the number of times equal to the valence of $e$. Hence, the new constraints simply says that in at least one of the old constraints the inequality must be *strict*. Keeping in mind Remark [\[rmkkk\]](#rmkkk){reference-type="ref" reference="rmkkk"}, this implies that every non-boundary-parallel normal surface must have strictly negative Euler characteristic, thus proving the second part of Theorem [\[hext\]](#hext){reference-type="ref" reference="hext"} ◻
:::

Some remarks may be in order: It is easy to see (and not surprising) that an identical theorem can be proved if the cone angles around the edges of $T$ are required to not be smaller than $2\pi$, while if the angles are smaller than $2\pi$, one can show an analogous "orbifold" version of the theorem. A more interesting question is whether theconverse of Theorem [\[hext\]](#hext){reference-type="ref" reference="hext"} holds. This is equivalent to asking whether every assignment of variables satisfying the constraints of programs $L_h^*$ and $L_s^*$ comes from a normal surface.

::: acks
The author would like to thank the École Normale Superieure de Lyon and the Institut Henri Poincaré for their hospitality. The special case of Theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"} for Euclidean structures (that is, trivial holonomy) has been independently shown for closed surfaces by W. Veech ([@veech]) and B. H. Bowditch ([@bhb]) using completely different methods. Theorem [\[hext\]](#hext){reference-type="ref" reference="hext"} is due to A. Casson.
:::
