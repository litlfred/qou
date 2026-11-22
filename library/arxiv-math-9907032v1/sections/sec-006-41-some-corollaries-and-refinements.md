---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-006-41-some-corollaries-and-refinements
section_title: "Some corollaries and refinements"
section_number: 4.1
pages: 11-13
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 1.0
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#corref label="corref"}

Here are some easy consequences of Theorem [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"}:

Special case 1

:   $\mathcal{F} = T$. Then, since $E^\prime(\mathcal{F}) =
    \emptyset$, we just get the Gauss-Bonnet theorem (with curvature defined in terms of the dihedral angles).

Special case 2

:   The complement of $\mathcal{F}$ is an annulus containing no vertices of $T$ -- this corresponds to a simple cycle in the Poincaré dual $T^*$. For every edge in $E^\prime(\mathcal{F})$, $n_e = 2$. Theorem [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"} just says that $\sum_{e \in
    E^\prime} \delta^\prime(e) > 0.$

Special case 3

:   For every edge in $E^\prime(\mathcal{F})$, $n_e = 1$. This will hold in the case where $\mathcal{F}$ is a subset of $T$ with a collar, and removing the edges in $E^\prime$ separates the $1$-skeleton of $T$ into (at least) two connected components. In this case, Theorem [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"} tells us that $$\sum_{e\in E^\prime(\mathcal{F})} \delta^\prime(e)\geq 
    2\pi \chi (\mathcal{F})- K(\mathcal{F}).$$

A drawback of both conditions [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} and Theorem [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"} is that they require their respective inequalities to be checked for *every* subcomplex of $T$ in order to verify whether a given assignment of dihedral angles is admissible. It is not hard to see that this requirement can be weakened somewhat.

Let $\mathcal{F}$ be the subcomplex in question.

::: observation
[]{#obs1 label="obs1"} It can assumed that every edge in $E(\mathcal{F})$ is an edge of at least one face.
:::

::: observation
[]{#obs2 label="obs2"} The $1$-skeleton of the Poincaré dual $\mathcal{F}^*$ of $\mathcal{F}$ can be assumed connected -- this is somewhat stronger than saying that $\mathcal{F}$ is connected.
:::

::: observation
[]{#obs3 label="obs3"} It can be assumed that the $1$-skeleton of $\overline{\mathcal{F}}^*$ -- the Poincaré dual of the complement of $\mathcal{F}$ -- has no isolated vertices.
:::

It is straightforward to check all of the above observations.

In the special situation where $\delta(e)\leq \pi$ for all $e\in E(T)$ -- that is, $\delta$ is Delaunay, one can further assume that every face $f$ of $\overline{\mathcal{F}}$ is adjacent to at most one face of $\mathcal{F}$. Otherwise, adjoin $f$ to $\mathcal{F}$, to create a new complex $\mathcal{F}^\prime$. This complex has one more face than $\mathcal{F}$, but its sum of dihedral angles is at most $\pi$ greater than that of $\mathcal{F}$. Hence, it is enough to check that $\mathcal{F}^\prime$ satisfies the hypotheses of Theorem [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"}, or the conditions [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"}.

::: definition
A *simple* subcomplex of $T$ is a subcomplex $\mathcal{F}$ such that both $\mathcal{F}$ and $T \backslash \mathcal{F}$ are connected.
:::

::: theorem
[]{#versimple label="versimple"} To verify that Conditions 2.1 and 2.2 (or equivalently, conditions of Theorem [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"}\[(b)\]) hold for *all* subcomplexes of $T$, it is necessary and sufficient to check them for simple subcomplexes.
:::

::: proof
*Proof.* By Observation [\[obs2\]](#obs2){reference-type="ref" reference="obs2"}, it is enough to check the connected subcomplexes of $T$. If such a subcomplex $\mathcal{F}$ is simple, then we are done. Otherwise, its complement is not connected. Let $\mathcal{C}$ be a connected component of the complement of $\mathcal{F}$.

::: lemma
The complex $\mathcal{C}$ is simple.
:::

::: proof
*Proof.* By construction, $\mathcal{C}$ is connected. Also, every point of $T \backslash \mathcal{C}$ can be connected by a path to a point of $\mathcal{F}$. Since $\mathcal{F}$ is assumed connected, the lemma follows. ◻
:::

Consider $\mathcal{F}^\prime = \mathcal{F} \cup \mathcal{C}$. By assumption, $\mathcal{F}^\prime \neq T.$ Now

$$\begin{aligned}
 & & \left(\sum_{e\in E(\mathcal{F})} \Delta(e) -  \pi
  |F(\mathcal{F})|\right) +
\left(\sum_{e\in E(\mathcal{C})} \Delta(e) -  \pi
  |F(\mathcal{C})|\right) - \sum_\partial \mathcal{C} \\
 & = &
\left(\sum_{e\in E(\mathcal{F}^\prime)} \Delta(e) -  \pi
  |F(\mathcal{F})^\prime|\right).
\end{aligned}$$

By lemma [\[boundaryineq\]](#boundaryineq){reference-type="ref" reference="boundaryineq"} (more precisely, a version for simple complexes), $$\left(\sum_{e\in E(\mathcal{C})} \Delta(e) -  \pi
  |F(\mathcal{C})|\right) - \sum_\partial \mathcal{C} < 0,$$ thus, $$\left(\sum_{e\in E(\mathcal{F})} \Delta(e) -  \pi
  |F(\mathcal{F})|\right) > 
\left(\sum_{e\in E(\mathcal{F}^\prime)} \Delta(e) -  \pi
  |F(\mathcal{F})^prime|\right).$$

Thus, in order to check that condition [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} holds for $\mathcal{F}$, it is enough to check that it holds for $\mathcal{F}^\prime$. The proof of Theorem [\[versimple\]](#versimple){reference-type="ref" reference="versimple"} is finished by the obvious induction argument on the number of connected components of the complement of $\mathcal{F}$. ◻
:::

In the case where $T$ is a genuine simplicial complex (that is, two cells intersect in a lower-dimensional cell), simple subcomplexes corresponds to *non-coterminous minimal cutsets* of edges of $T$:

::: definition
A collection $\mathcal{C}$ of edges of $T$ is a *cutset* if removing the edges in $\mathcal{C}$ disconnects the $1$-skeleton of $T$. A cutset $\mathcal{C}$ is $\emph{minimal}$ if no proper subset of $\mathcal{C}$ is a cutset. A cutset $\mathcal{C}$ is *coterminous* if all of the edges in $\mathcal{C}$ are incident to the same vertex.
:::

In other words, a minimal cutset corresponds to a separating simple curve in the Poincaré dual $T^*$ of $T$ (the curve need not be closed if $T$ has boundary). A coterminous cutset corresponds to a boundary of a face in the dual. The non-coterminous simple cutset corresponding to the subcomplex $\mathcal{F}$ is nothing other than the set of edges $E^\prime(\mathcal{F})$ define just before the statement of theorem [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"}.

In the case where the surface $S$ is a flat disk, theorems [\[maindual\]](#maindual){reference-type="ref" reference="maindual"}, [\[exist\]](#exist){reference-type="ref" reference="exist"}, [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"}, and [\[versimple\]](#versimple){reference-type="ref" reference="versimple"} immediately imply:

::: theorem
[]{#andreevthm label="andreevthm"} Let $T$ be a triangulation of the disk, let $\Delta: E(T) \rightarrow
(0, \pi]$ be an assignment of dihedral angles to the edges of $T$, let $V_\partial(T)$ be the set of boundary vertices of $T$ and let $\Lambda: V_\partial(T) \rightarrow (0, \pi]$ be the assignment of boundary angles. Then, there exists a collection of points $p_1,
\ldots, p_{V(T)}$ in the plane $\mathbf{E}^2$ whose Delaunay triangulation is combinatorially equivalent to $T$, has dihedral angles given by $\Delta$, and whose convex hull is a polygon with angles given by $\Lambda$, if and only if:

-   []{#sumvv label="sumvv"} If $v$ is an interior vertex of $T$, then $$\sum_{\mbox{$e \in E(T)$ incident to $v$}} (\pi - \Delta(e)) = 2\pi.$$

-   []{#sumvb label="sumvb"} If $v$ is a boundary vertex of $T$, then $$\sum_{\mbox{$e \in E(T)$ incident to $v$}} (\pi - \Delta(e)) + (\pi -
    \Lambda(v)) = 2\pi.$$

-   []{#sumintcyc label="sumintcyc"} If $\mathcal{E}$ is a non-coterminous minimal cutset corresponding to a simple closed curve in the Poincaré dual $T^*$ of $T$, then $$\sum_{e \in \mathcal{E}} (\pi - \Delta(e)) > 2\pi.$$

-   []{#sumextcyc label="sumextcyc"} If $\mathcal{E}$ is a non-coterminous minimal cutset not corresponding to a simple closed curve in $T^*$, and $\mathcal{E}$ separates the boundary vertices of $T$ into two groups $v_1, \ldots, v_k$ and $v_{k+1}, \ldots, v_{|V_\partial(T)|}$, then $$\sum_{e \in \mathcal{E}} (\pi - \Delta(e)) + \sum_{i=1}^k (\Pi-\Lambda(v_i))> 2\pi.$$
:::

*Remark.* Theorem [\[andreevthm\]](#andreevthm){reference-type="ref" reference="andreevthm"} is nothing but one of the main results (Theorem 0.1) of [@steiner], stated in a different language (without mentioning convex ideal polyhedra), so we have succeeded in deducing that theorem in a purely combinatorial way from the results of [@rvol]. In addition, Theorem [\[versimple\]](#versimple){reference-type="ref" reference="versimple"} is seen to be a direct generalization of [@steiner]\[Theorem 0.1\] to a characterization of dihedral angles of Delaunay triangulations of arbitrary, possibly singular, Euclidean surfaces.
