---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-019-62-regular-triangulations
section_title: "Regular triangulations"
section_number: 6.2
pages: 34-39
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.961
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
The concept of a regular triangulation comes from the study of triangulations of convex polytopes in $\mathbb{R}^n$. Here we are not dealing with topological triangulations, where tetrahedra may have self-identifications or two vertices may have multiple edges connecting them. Rather, the vertices are concrete points in $\mathbb{R}^n$, the edges are straight line segments in $\mathbb{R}^n$ and so on. In this context, a triangulation of a convex polytope is a subdivision of the polytope into concrete Euclidean simplices. Roughly speaking, a triangulation of a polytope in $\mathbb{R}^n$ is *regular* if it is isomorphic to the lower faces of a convex polytope in $\mathbb{R}^{n+1}$. The following series of definitions make this idea precise.

::: defn
An *affine combination* of a set of points $(\bp_j)_{j\in C}$ in $\mathbb{R}^n$ is a sum $\sum_{j\in C} \lambda_j \bp_j$ where $\sum_{j\in C} \lambda_j =1.$ A set of points is *affinely independent* if none of them is an affine combination of the others. A *$k$--simplex* is the convex hull of an affinely independent set of $k+1$ points.
:::

::: defn
A *point configuration* is a finite set of labelled points in $\mathbb{R}^n$. Let $\bA = (\bp_j)_{j\in J}$ be a point configuration with label set $J$. For $C\subset J$, the *affine span of $C$ in $\bA$* is the set of affine combinations of the set of points labelled by $C$. The *dimension of $C$* is the dimension of the affine span of $C$. The *convex hull of $C$ in $\bA$* is the convex hull in $\mathbb{R}^n$ of the set of points labelled by $C$. $$\text{conv}_\bA(C):=\left\{ \sum_{j\in C} \lambda_j \bp_j \mid \lambda_j\geq0 \text{ for all } j \in C, \text{ and } \sum_{j\in C} \lambda_j =1\right\}$$ The *relative interior of $C$ in $\bA$* is the interior of the convex hull in its affine span. $$\text{relint}_\bA(C):=\left\{ \sum_{j\in C} \lambda_j \bp_j \mid \lambda_j >0 \text{ for all } j \in C, \text{ and } \sum_{j\in C} \lambda_j =1\right\}$$
:::

::: defn
With the above notation, if $\psi\in(\mathbb{R}^n)^*$ is a linear functional, then the *face of $C$ in direction $\psi$* is the subset of $C$ given by $$\text{face}_\bA(C, \psi):=\left\{ j\in C \mid \psi(\bp_j)=\max_{b\in C}(\psi(\bp_b)) \right\}$$ If $F$ is a face of $C$, we write $F\leq_\bA C$ and if in addition $F\neq C$ we write $F<_\bA C$.
:::

::: defn
With the above notation, a collection $\mathcal{S}$ of subsets of $J$ is a *polyhedral subdivision of $\bA$* if it satisfies the following conditions. (The elements of $\mathcal{S}$ are called *cells*.)

1.  If $C\in\mathcal{S}$ and $F\leq C$ then $F\in \mathcal{S}$.

2.  $\cup_{C\in\mathcal{S}} \text{conv}_\bA(C) \supset \text{conv}_\bA(J)$.

3.  If $C\neq C'$ are two cells in $\mathcal{S}$ then $\text{relint}_\bA(C)\cap\text{relint}_\bA(C')=\emptyset$.
:::

::: rmk
The first condition says that if some cell is in our subdivision then all faces of it are also. The second condition says that it is a subdivision of the whole convex hull of the points in $\bA$. The third condition says that the cells can only overlap with each other on their faces, not their interiors.
:::

::: defn
[]{#point config triangulation label="point config triangulation"} With the above notation, a *triangulation of $\bA$* is a polyhedral subdivision of $\bA$ such that every cell is a simplex.
:::

::: defn
Let $\bA = (\bp_j)_{j\in J}$ be a point configuration with label set $J$. Suppose that $\omega\colon\thinspace\bA\to\mathbb{R}$ is any map. The *lifted point configuration* in $\mathbb{R}^{n+1}$ is the point configuration $$\bA^\omega = (\bp^\omega_j)_{j\in J} := (\bp_j, \omega(\bp_j))_{j\in J}$$ (again with label set $J$) given by adjoining to each vector an $n+1$th coordinate given by the value of $\omega$ at that point. Consider the set of faces of $\text{conv}_{\bA^\omega}(J)$. A *lower face* of this convex hull is a face that is "visible from below". That is, $\text{face}_{\bA^\omega}(J, \psi)$ is a lower face if $\psi$ is negative on the last coordinate.
:::

::: defn
The *regular polyhedral subdivision of $\bA$ produced by $\omega$*, denoted $\mathcal{S}(\bA,\omega)$, is the set of lower faces of the point configuration $\bA^\omega$.
:::

Note that a face in these definitions is a set of labels for the point configuration. So the set of faces making up the polyhedral subdivision of $\bA$ is defined in terms of $\bA^\omega$, but this works because the same set of labels is used for the two point configurations. Lemma 2.3.11 of [@DeLoera:book] shows that $\mathcal{S}(\bA,\omega)$ is indeed a polyhedral subdivision of $\bA$, for every $\omega$.

::: defn
A *regular triangulation of $\bA$* is a regular polyhedral subdivision of $\bA$ that is a triangulation of $\bA$.
:::

Proposition 2.2.4 of [@DeLoera:book] shows that every point configuration has a regular triangulation. The connection between regular triangulations of point configurations and our situation can be made via the Klein model of $\mathbb{H}^3$. In this model, geodesics are represented as straight lines in Euclidean space, $\mathbb{E}^3$. A convex ideal hyperbolic polyhedron is represented as a convex Euclidean polyhedron whose vertices lie on a sphere. Such a Euclidean polyhedron can be seen as a point configuration, with the points consisting of the vertices of the polyhedron. Note that this is a more restrictive situation than the full generality discussed in [@DeLoera:book] -- since all the vertices lie on a sphere, there can be no internal points, and no three points can lie on a line. These observations imply that the set of subdivisions of a convex ideal hyperbolic polyhedron into (strictly positive) volume ideal hyperbolic tetrahedra is in one-to-one correspondence with the set of triangulations of the convex Euclidean polyhedron, in the sense of Definition [\[point config triangulation\]](#point config triangulation){reference-type="ref" reference="point config triangulation"}. The bijective map between the two sets preserves the combinatorial structure of the triangulations.

::: defn
Given the above discussion, we define a *regular ideal triangulation* of a convex ideal hyperbolic polyhedron to be an ideal triangulation of the polyhedron whose corresponding Euclidean triangulation of the corresponding convex Euclidean polyhedron is regular.[^1]
:::

We are now in a position to be able to define our class of triangulations $\mathcal X_M^{\mathrm{EP}}$.

::: defn
Let $M$ be a cusped hyperbolic 3--manifold. Let $\mathcal{P}$ be the PPP--cellulation of $M$ derived from the Epstein--Penner decomposition of $M$ (choosing equal volumes for the cusps if there is more than one) by inserting polygonal pillows between any two non-triangular faces of the decomposition. The class of triangulations $\mathcal X_M^{\mathrm{EP}}$ consists of all triangulations constructed via the following method:

1.  Insert a regular ideal triangulation of each polyhedron $P$ of $\mathcal{P}$ into $P$.

2.  Each polygonal pillow $Q$ has two (not necessarily distinct) polyhedra $P_-$ and $P_+$ glued to it. The regular ideal triangulations of $P_-$ and $P_+$ induce triangulations $t_-$ and $t_+$ of the two polygonal faces of $Q$. Insert into $Q$ a layered triangulation of $Q$, bridging between $t_-$ and $t_+$.
:::

Note that although there are only finitely many regular ideal triangulations of a given convex ideal polyhedron, there may be infinitely many triangulations in $\mathcal X_M^{\mathrm{EP}}$, since the layered triangulations can be arbitrarily long.

::: rmk
[]{#Xbar^EP 1-efficient label="Xbar^EP 1-efficient"} From the geometric construction, every triangulation of $\mathcal X_M^{\mathrm{EP}}$ has a natural semi-angle structure, as in Remark [\[rem:natural semi-angle structure\]](#rem:natural semi-angle structure){reference-type="ref" reference="rem:natural semi-angle structure"}, so they are all 1-efficient by Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"}.
:::

::: defn
The *corank* of a $d$--dimensional point configuration with $n$ points is the number $n-d-1$.
:::

A point configuration has corank *zero* if and only if it is affinely independent. A point configuration has corank *one* if and only if it has a unique affine dependence relation. This means that there is a unique solution to $$\sum_{j\in J} \lambda_j \bp_j =0 \text{ with } \sum_{j\in J} \lambda_j =0, \text{ where at least one } \lambda_j\neq0.$$ Uniqueness is up to scaling all $\lambda$'s by the same factor. The affine dependence divides $J$ into three subsets: $$J_+ := \{j\in J \mid \lambda_j>0\}, \quad J_0 := \{j\in J \mid \lambda_j=0\}, \quad J_- := \{j\in J \mid \lambda_j<0\}.$$ (Which is which of $J_+$ and $J_-$ is not well defined since we can multiply all of the coefficients by $-1$ to swap them.) Then $\text{relint}_\bA(J_+)\cap\text{relint}_\bA(J_-)$ is a single point, given by $$\sum_{j\in J_+} \lambda_j \bp_j = \sum_{j\in J_-} -\lambda_j \bp_j,$$ where we have normalised the $\lambda$'s so that $$\sum_{j\in J_+} \lambda_j = \sum_{j\in J_-} -\lambda_j  = 1.$$

::: defn
Let $\bA = (\bp_j)_{j\in J}$ be a point configuration with label set $J$. A subset of $J$ is called a *circuit*, $Z$, if it is a minimal affinely dependent set (i.e. it is dependent, but every proper subset is independent).
:::

In the above discussion, $Z=J_+\cup J_-$, and $Z$ is partitioned into the two sets, $Z_+=J_+$ and $Z_-=J_-$ since if $\lambda_j=0$ in the affine dependence then it could be removed from $Z$, contradicting minimality.\
In $\mathbb{R}^3$, five points in general position are a circuit, but there may be circuits with fewer points. Four points are a circuit if they lie in a plane, three if they lie on a line, and two if they are coincident. However, for our purposes the points are the vertices of a convex Euclidean polyhedron, so we may assume that there are no repeated points. Moreover, the points lie on a sphere, so no three lie on a line. Therefore, the only two possibilities are five points in general position, or four points that lie on a plane, as shown in Figure [1](#circuits){reference-type="ref" reference="circuits"}.

<figure id="circuits">
<p><span class="math inline">−</span> at 0 106 <span class="math inline">+</span> at 8 19 <span class="math inline">−</span> at 136 38 <span class="math inline">+</span> at 109 119</p>
<p><span class="math inline">+</span> at 195 77 <span class="math inline">+</span> at 319 94 <span class="math inline">+</span> at 309 22 <span class="math inline">−</span> at 260 4 <span class="math inline">−</span> at 260 137</p>
<img src="draws_eps/circuits" style="width:60.0%" />
<figcaption>Circuits with 4 and 5 elements.</figcaption>
</figure>

::: rmk
[]{#our corank one configs label="our corank one configs"} For us then, the only possible corank one configurations are

1.  five points in general position, or []{#corank 1 5 label="corank 1 5"}

2.  four points in a plane, or []{#corank 1 4 label="corank 1 4"}

3.  four points in a plane plus one point not in that plane. []{#corank 1 4+1 label="corank 1 4+1"}
:::

::: defn
[]{#def:almost-triangulation label="def:almost-triangulation"} Let $\mathcal{S}$ be a polyhedral subdivision that is not a triangulation. Then $\mathcal{S}$ is an *almost--triangulation* if

1.  all of the cells of $\mathcal{S}$ have corank at most one, and

2.  all of the cells of $\mathcal{S}$ of corank one contain the same circuit.
:::

::: lemma
[]{#lem:almost-triangulations label="lem:almost-triangulations"} In our case, the 3--cells of an almost--triangulation are all simplices apart from one or two 3--cells. These 3--cells can have the following forms:

1.  The convex hull of five points on a sphere, in general position, as in the upper diagram of Figure [2](#flip_2-3){reference-type="ref" reference="flip_2-3"}. []{#a-t_flip_2-3 label="a-t_flip_2-3"}

2.  A 4--sided pyramid, with the base of the pyramid on a boundary face of the polyhedron, as in the upper diagram of Figure [\[flip_2-2_external\]](#flip_2-2_external){reference-type="ref" reference="flip_2-2_external"}. []{#a-t_flip_2-2_external label="a-t_flip_2-2_external"}

3.  Two 4--sided pyramids whose bases are coincident, as in the upper diagram of Figure [\[flip_2-2_internal\]](#flip_2-2_internal){reference-type="ref" reference="flip_2-2_internal"}. []{#a-t_flip_2-2_internal label="a-t_flip_2-2_internal"}
:::

::: proof
*Proof.* This follows immediately from Definition [\[def:almost-triangulation\]](#def:almost-triangulation){reference-type="ref" reference="def:almost-triangulation"} and Remark [\[our corank one configs\]](#our corank one configs){reference-type="ref" reference="our corank one configs"}. ◻
:::

<figure id="flip_2-3">
<p>refinement at 60 156 refinement at 225 156 flip at 139 86</p>
<img src="draws_eps/flip_2-3" style="width:44.0%" />
<figcaption>The almost–triangulation in case (<a href="#a-t_flip_2-3" data-reference-type="ref" data-reference="a-t_flip_2-3">[a-t_flip_2-3]</a>) of Lemma <a href="#lem:almost-triangulations" data-reference-type="ref" data-reference="lem:almost-triangulations">[lem:almost-triangulations]</a>, and its two refinements to triangulations. Note that although the top and lower left pictures are identical, the top is to be interpreted as a single 3–cell, while the lower left shows two tetrahedra meeting in a triangle. The associated flip between the two triangulations is a 2–3 flip.</figcaption>
</figure>

<figure id="2-2_flips">

<figcaption>Almost–triangulations in cases (<a href="#a-t_flip_2-2_external" data-reference-type="ref" data-reference="a-t_flip_2-2_external">[a-t_flip_2-2_external]</a>) and (<a href="#a-t_flip_2-2_internal" data-reference-type="ref" data-reference="a-t_flip_2-2_internal">[a-t_flip_2-2_internal]</a>) of Lemma <a href="#lem:almost-triangulations" data-reference-type="ref" data-reference="lem:almost-triangulations">[lem:almost-triangulations]</a>, and the associated 2–2 flips. In all diagrams, vertices <span class="math inline"><em>v</em><sub>1</sub></span> through <span class="math inline"><em>v</em><sub>4</sub></span> are coplanar.</figcaption>
</figure>

::: defn
Let $\mathcal{S}$ and $\mathcal{S}'$ be two polyhedral subdivisions of a point configuration $\bA$. Then *$\mathcal{S}$ is a refinement of $\mathcal{S}'$* if for each $C\in \mathcal{S}$, there is a $C'\in\mathcal{S}'$ with $C\subset C'$.
:::

::: lemma
Every almost--triangulation has exactly two proper refinements, which are both triangulations.
:::

::: defn
Two triangulations of the same point configuration are *connected by a flip supported on the almost--triangulation $\mathcal{S}$* if they are the only two triangulations refining $\mathcal{S}$.
:::

::: defn
We call the flips associated to the three possible almost--triangulation types listed in Lemma [\[lem:almost-triangulations\]](#lem:almost-triangulations){reference-type="ref" reference="lem:almost-triangulations"} the *2-3 flip*, *external 2--2 flip*, and *internal 2--2 flip* respectively. See Figures [2](#flip_2-3){reference-type="ref" reference="flip_2-3"} and [3](#2-2_flips){reference-type="ref" reference="2-2_flips"}.
:::

::: defn
The *flip graph* of the point configuration $\bA$ is the graph whose vertices are the triangulations of $\bA$ and whose edges are triangulations connected by flips.
:::

We use the following result, due to Gelfand, Kapranov and Zelevinsky, and given as Corollary 5.3.14 in [@DeLoera:book].

::: thm
[]{#GKZ label="GKZ"} Let $\bA$ be a point configuration. The subgraph of the flip graph induced by all regular triangulations of $\bA$ that use the same vertices is connected.
:::

In our case, since the vertices lie on a sphere, all vertices are used in every triangulation, so this says that we can get from any regular triangulation of the polyhedron to any other by performing flips.\

::: rmk
[]{#retriangulate strategy label="retriangulate strategy"} Our strategy for connecting two triangulations $\mathcal{T}_1, \mathcal{T}_2\in\mathcal X_M^{\mathrm{EP}}$ is as follows. Both triangulations consist of regular triangulations of the polyhedra of the PPP--cellulation, together with layered triangulations in the polygonal pillows between them.

1.  Use Theorem [\[GKZ\]](#GKZ){reference-type="ref" reference="GKZ"} on each polyhedron, to change the triangulation of each polyhedron in $\mathcal{T}_1$ into the corresponding triangulation of the polyhedron in $\mathcal{T}_2$. This step may alter the triangulations of the polygonal pillows as well. []{#retriangulate step 1 label="retriangulate step 1"}

2.  Change the triangulation in each polygonal pillow of the resulting triangulation so that it matches with the corresponding triangulation in $\mathcal{T}_2$. This step does not alter the triangulations of the polyhedra. []{#retriangulate step 2 label="retriangulate step 2"}
:::

[^1]: Note that this definition has no relation to the definition of a regular ideal hyperbolic tetrahedron, in the sense of a tetrahedron with all dihedral angles being $\pi/3$.
