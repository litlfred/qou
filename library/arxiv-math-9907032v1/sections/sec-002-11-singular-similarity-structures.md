---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-002-11-singular-similarity-structures
section_title: "Singular similarity structures."
section_number: 1.1
pages: 3-5
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.995
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
Consider an oriented surface $S$, possibly with boundary, and with a number of distinguished points $\{p_1, \ldots, p_n\}$. A *similarity structure* on $S$ is given by an atlas for $S
\backslash \{p_1, \ldots, p_n\}$, such that the transition maps are Euclidean similarities. A similarity structure induces a holonomy representation $H_s$ of $\Gamma = \pi_1(S \backslash \{p_1, \ldots,
p_n\})$ into the similarity $\mathrm{Sim\:}(\mathbf{E}^2)\simeq
\widetilde{\mathbf{C}^*}$, where the tilde indicates the universal cover. We define the *dilatational holonomy* as the induced representation $H_d:
\Gamma \rightarrow \mathbf{R}$, where $H_d(\gamma) = \log \mbox{dilatation} H_s(\gamma) = \log |H_s(\gamma)|$. The *rotational holonomy* can almost be defined as $H_r(\gamma) = \arg
H_s(\gamma)$, but for the slight complication that we need to take the argument in $\widetilde{\mathbf{C}^*}$, since we want to distinguish, eg, the angle of $4\pi$ from one of $2\pi.$ This notion of argument is what is used in the sequel. In particular, if $\gamma$ is a loop surrounding one of the distinguished points $p_i$, then $H_r(\gamma)$ is the *cone angle* at $p_i$. In the case where $H_d(\Gamma) = \{0\}$, the similarity structure is a *singular Euclidean structure*, with cone angles defined by $H_r$ as above. In the sequel, references to the *holonomy* of a similarity structure will actually mean the dilatational holonomy $H_d$. A more concrete way to think of both similarity and Euclidean structure is by assembling our surface out of Euclidean triangles, in the pattern given by some complex $T$. In the case where the lengths of the edges of the triangles being glued together agree, then we have a singular Euclidean structure. If not, then we have a similarity structure. In either case, the vertices of $T$ are potentially cone points, with cone angles given by the sums of the appropriate angles of the incident triangles.

Consider an oriented surface $S$, possibly with boundary, and assume that $S$ has a Euclidean metric (or, more generally, a similarity structure -- with the exception of the results of Section [\[ideal\]](#ideal){reference-type="ref" reference="ideal"} , some of which depend on the metric Theorem [\[infty\]](#infty){reference-type="ref" reference="infty"}, the metric structure or lack thereof plays no role in the arguments). with cone singularities. We will be dealing with *semi-simplicial* triangulations of $S$, that is, triangulations where two and where distinct closed cells might intersect in a collection of lower-dimensional cells. All triangulations will be assumed semi-simplicial, unless specified otherwise. A subcomplex $\mathcal{F}$ of $T$ will be called *closed* if whenever an open face $F$ is in $\mathcal{F}$, so are all of the faces of $\partial
F$.

Assume now that the surface $S$ is equipped with a finite geodesic semi-simplicial triangulation $T$, such that the $0$-skeleton of $T$, which is denoted by $V(t)$, contains all of the cone points of $S$. Each face of $T$ is then a Euclidean triangle. There are two kinds of edges of $T$ -- the interior edges, incident to two faces of $T$, and the boundary edges, incident to only one face of $T$.

::: definition
[]{#dihdef label="dihdef"} Let $e$ be an edge of $T$. First, suppose that $e$ is a boundary edge, and let $t=ABC$ be a face of $T$ incident to $e$, so that $e=AB$. Then the *dihedral angle* $\delta(e)$ at $e$ is the angle of $t$ at the vertex $C$. Now, assume that $e$ is an internal edge of $T,$ so that $e$ is incident to $t_1 = ABC$ and $t_2 = ABD$, so that $e = AB.$ Then the dihedral angle at $e$ is the sum of the angle of $t_1$ at $C$, and the angle of $t_2$ at $D.$ The *exterior* dihedral angle $\delta^\prime(e)$ at $e$ is defined to be $\delta^\prime(e) = \pi - \delta(e)$.

The *cone angle* at an interior vertex $v$ of $T$ is the sum of all the angles of the faces of $T$ incident to $v$ at $v$; the *boundary angle* at a boundary angle is defined in the same way.
:::

The following is a slight extension of [@rvol Lemma 4.2].

::: lemma
[]{#cona label="cona"} The cone angle at an interior vertex $v\in V(T)$ is equal to the sum of the exterior dihedral angles at the edges of $T$ incident to $v.$ At a boundary vertex, the boundary angle is equal to the sum of the exterior dihedral angles as above, less $\pi$.
:::

::: proof
*Proof.* First, let $v$ be an interior vertex. Suppose that there are $n$ triangles $t_1, \dots, t_n$ incident to $v$. The sum of all of their angles is $n \pi.$ The cone angle at $v$ is the sum of the angles of the triangles $t_i$ at $v.$ On the other hand, the sum of the dihedral angles of the edges $e_1, \dots, e_n$ incident to $v$ is the sum of all of the angles of $t_i$ *not* incident to $v$. Thus, $$\label{anglesum1}
n \pi = \mbox{Cone angle at $v$} + \sum_{i=1}^n \delta(e_i).$$ The result follows by rearranging the terms.

If $v$ is a boundary vertex, and there are $n$ faces incident to $v$, then there are $n+1$ edges, and equation [\[anglesum1\]](#anglesum1){reference-type="ref" reference="anglesum1"} becomes: $$\label{anglesum2}
n \pi = \mbox{boundary angle at $v$} + \sum_{i=1}^{n+1} \delta(e_i),$$ and the result follows by rearranging terms, as above. ◻
:::

::: observation
[]{#gaussbonnet label="gaussbonnet"} The sum of all of the dihedral angles of all of the edges of $T$ is equal to the $\pi |V(T)|$ -- in combination with the Lemma above this gives the Gauss-Bonnet theorem in this polyhedral context, since the curvature at an interior vertex $v$ of $T$ is defined to be $2\pi - \mbox{Cone angle at $v$}$, while the curvature at a boundary vertex is defined to be $\pi -
\mbox{boundary angle at $v$}$.
:::

::: proof
*Proof.* Every angle of every face of $T$ is opposite to exactly one edge of $T$. ◻
:::

The next theorem is [@rvol Theorem 6.16].

::: theorem
[]{#uniqueness label="uniqueness"} Let $\Delta: E(T) \rightarrow (0, 2\pi)$ be an assignment of dihedral angles to the edges of $T$, and $H_d$ a holonomy representation. There exists at most one singular similarity structure on $S$ with holonomy $H_d$ (and in particular, at most one singular Euclidean structure, up to scaling), such that so that $\delta(e) = \Delta(e),$ for every edge $e\in E(T)$.
:::

::: definition
A triangulation $T$ with $\delta(e) \leq \pi$ for every interior $e\in E(T)$ is called a *Delaunay triangulation*.
:::

Let $\Delta$ be a map -- $\Delta: E(T) \rightarrow (0, 2\pi).$ When does there exist a singular Euclidean metric on $S$ with the dihedral angles prescribed by $\Delta$? It is clear that there are certain linear constraints which must be satisfied -- to wit, for every face $t=ABC$ of $T$, we must be able to find angles $\alpha$, $\beta$, and $\gamma$, such that:

Positivity

:   All angles are strictly positive.

Euclidean Faces

:   For every face $t$, $\alpha_t + \beta_t +
      \gamma_t = \pi.$

Boundary edge dihedral angles

:   For every boundary edge $e = AB,$ incident to the triangle $ABC$, $\gamma = \Delta(e).$

Interior edge conditions

:   For every interior edge $e = AB,$ incident to triangles $ABC$ and $ABD$, $\alpha+\delta = \Delta(e).$

The system of equations and inequalities above specify a *linear program* $L$. The feasible region (set of solutions) of $L$ must be non-empty in order for us to have any hope of having a singular Euclidean metric on $S$ with prescribed dihedral angles. One of the principal results (Theorem 6.1) of [@rvol] is that if all of the dihedral angles are no greater than $\pi$ (that is, the triangulation is Delaunay), then Conditions 1-4 are also sufficient, thus:

::: theorem
[]{#exist label="exist"} If the feasible region of $L$ is non-empty and every dihedral angle is at most $\pi$, then there exists a similarity structure with any prescribed holonomy $H_d$ and, in particular, a singular Euclidean metric on $S$ with the prescribed dihedral angles -- this structure is unique by Theorem [\[uniqueness\]](#uniqueness){reference-type="ref" reference="uniqueness"} (and the metric is unique up to scaling).
:::
