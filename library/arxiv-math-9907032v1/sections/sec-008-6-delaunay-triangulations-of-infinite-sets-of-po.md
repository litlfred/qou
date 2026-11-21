---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-008-6-delaunay-triangulations-of-infinite-sets-of-po
section_title: "Delaunay triangulations of infinite sets of points"
section_number: 6
pages: 16-19
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#ideal label="ideal"} In this section we will show that theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"} for singular Euclidean structures can be extended without change to infinite locally finite complexes:

::: theorem
[]{#infmain label="infmain"} Let $T$ be an infinite but locally finite complex, and let $\Delta:
E(T) \rightarrow (0, \pi]$. Then there exists a singular euclidean structure on $T$, with cone points at vertices of $T$, whose Delaunay triangulation is combinatorially equivalent to $T$, and whose dihedral angles are given by $\Delta$ if and only if each finite subcomplex $\mathcal{F} \subset T$ with $E(\mathcal{F}) \neq
\emptyset$ has positive excess.
:::

There are two ingredients in the argument. The first (Lemma [\[linref\]](#linref){reference-type="ref" reference="linref"}) is an extension of section [\[suff\]](#suff){reference-type="ref" reference="suff"}, the second ([\[infty\]](#infty){reference-type="ref" reference="infty"}) is a geometric estimate which will enable us to extract the necessary subsequences.

::: lemma
[]{#linref label="linref"} Let $T$ be a complex, and let $\Delta: E(T) \rightarrow (0, \pi]$. Then there exists a Euclidean structure with cone angles at vertices of $T$, and dihedral angles given by $\Delta$, except at the boundary edges of $T$, where they are smaller than prescribed by $\Delta$ if the excess of any subcomplex $\mathcal{F}$ of $T$, such that $E(\mathcal{F}) \neq \emptyset$ is positive.
:::

*Remark.* Lemma [\[linref\]](#linref){reference-type="ref" reference="linref"} can be viewed as a relative version of theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"}.

::: proof
*Proof.* The argument parallels very closely that of section [\[suff\]](#suff){reference-type="ref" reference="suff"}. The existence of the desired structure is, as before, equivalent to a negative objective of a linear program, and as before, we set up a slightly simpler linear program first. To wit, the program $L^\prime$ is:

> Positivity
>
> :   All angles are strictly positive.
>
> Euclidean Faces
>
> :   For every face $t$, $\alpha_t + \beta_t +
>       \gamma_t = \pi.$
>
> Boundary edge dihedral angles
>
> :   For every boundary edge $e = AB,$ incident to the triangle $ABC$, $\gamma + x_e = \Delta(e),$ where the slack variables (see the comments following the statement of Theorem [\[duality\]](#duality){reference-type="ref" reference="duality"}) $x_e$ are also non-negative.
>
> Interior edge conditions
>
> :   For every interior edge $e = AB,$ incident to triangles $ABC$ and $ABD$, $\alpha+\delta = \Delta(e).$

We relax the program $L^\prime$ to a program $L_1^\prime$ by dropping the requirement that the angles be strictly positive, make the objective 0, as before, and we see that the dual to the new weakened linear program $L_1^\prime$ is the following:

The dual program

:   Maximize $F({\bf u}, {\bf v}):\pi \sum_{t \in F(T)} u_t + \sum_{e\in E(T)} \Delta(e)v_e$, subject to the conditions

    the inequalities of $L_1^*$

    :   $u_t+v_e\leq 0$ whenever $e$ is an edge of $t$.

    new inequalities

    :   Whenever $e$ is a boundary edge of $T$, $v_e \leq 0$

Since the constraints of the above program $L_1^{\prime *}$ are a superset of the constraints of $L_1^*$, Theorem [\[maindual\]](#maindual){reference-type="ref" reference="maindual"} still tells us that the objective function is maximized if there exists a $u$, such that $u_t = - v_e = u$, for all $t\in F(T)$, $e\in
E(T)$. Now, this is not enough to guarantee that the objective is zero, since the equality case of condition [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} (when $\mathcal{F} = T$) no longer exists. Since the new inequalities require $u$ to be non-negative, it follows that for the objective function to equal $0$, $u$ must be $0$.

Now, we follow Section [\[suff\]](#suff){reference-type="ref" reference="suff"} again, to define a program $L_2^\prime$ in the same way as before (that is, since we want the angles to be strictly positive, we set $\alpha_i = \beta_i+\epsilon$, etc, and to also define its dual $L_2^{\prime *}$. By the same reasoning as before, it follows that the objective of $L_2^{\prime *}$, and hence of $L_2^\prime$, is negative. In fact, we can do more: we can also require all of the slack variables $x_e$ to be strictly positive. The (yet another) new dual program $L_3^{\prime *}$ will have the form:

*Third dual.* Maximize $F({\bf u}, {\bf v}):\pi \sum_{t \in F(T)} u_t + \sum_{e\in E(T)} \Delta(e)v_e$, subject to the conditions

> $u_t+v_e\leq 0$ whenever $e$ is an edge of $t$.
>
> $v_e \leq 0$, when $e$ is a boundary edge of $T$.
>
> $3  \sum_{t \in F(t)} u_t + 
> 2 \sum_{e\in E(T), e\notin \partial T} v_e + 
> 2 \sum_{e\in E(T), e \in \partial T} v_e \leq -1$.

If we omit the last constraint, we remain with the dual program $L_1^{\prime *}$, and as the discussion above showed, the objective of that can only be $0$ if $u_t \equiv v_e \equiv 0$, which is at odds with the last constraint of $L_3^{\prime *}$ ◻
:::

::: theorem
[]{#infty label="infty"} Let $p_1, \ldots, p_n$ be a set of points in the plane, and $D$ their Delaunay triangulation. Assume that the shortest edge of $D$ has length $1$, and the excess of every non-trivial subcomplex of $D$ is no smaller than $d_0$. Then $$\mathrm{diameter\:}D \leq \left(\frac{4 n}{d_0}\right)^n.$$
:::

The proof of Theorem [\[infty\]](#infty){reference-type="ref" reference="infty"} will depend on a couple of easy auxillary results:

::: lemma
[]{#thmcos label="thmcos"} Let $ABC$ be a triangle with $a/c, a/b < \epsilon$, $0<\epsilon
<1/10$. Then, $\alpha < 2\epsilon$.
:::

::: proof
*Proof.* This is an immediate consequence of the theorem of Cosines, or the theorem of Sines. ◻
:::

::: lemma
[]{#howcom label="howcom"} Let $\mathcal{F}$ be a subcomplex of $D$. Then the excess of $\mathcal{F}$ is $$\sum_{\mbox{triangles $ABC$ such that $AB \in \mathcal{F}$}}\gamma(ABC),$$ where $\gamma(ABC)$ is the angle at $C$.
:::

::: proof
*Proof.* This is immediate from the definition of excess. ◻
:::

::: proof
*of theorem [\[infty\]](#infty){reference-type="ref" reference="infty"}.* Suppose that the conclusion of the theorem does not hold. Assume, without loss of generality, that the edge between the vertices $p_0$ and $p_1$ is the shortest one (and thus of length $1$).

We construct a family of disks $D_1, D_2,\ldots, D_{n}$, all centered on $p_0$, and such that the radius of $D_i$ is equal to $\left(\frac{4 n} d_0\right)^n.$ Let $A_i = D_{i+1} \backslash D_i$, and let $\mathcal{F}_i$ to be the maximal closed subcomplex of $D$ contained in $D_i$. The hypothesis of the theorem ensures that at least one of the annuli $A_i$ contains no vertices of $D$, let this annulus be $A_j$. Then we claim that the excess of $\mathcal{F}_j$ is smaller than $d_0$. Indeed, consider a triangle $ABC$ of $D$ adjacent to $\mathcal{F}_j$ along an edge $AB$. The vertex $C$ of $ABC$ lies outside $D_{j+1}$, and thus the lengths of $AC$ and $BC$ are at least $\left(\frac{4n}{d_0}\right)^{j+1} - \left(\frac{4n}{d_0}\right)^j$, while the length of $AB$ is at most $\left(\frac{4n}{d_0}\right)^j$. Thus, $$\gamma(ABC) < \frac{2}{\frac{4n}{d_0} - 1} < \frac{d_0}{n},$$ by lemma [\[thmcos\]](#thmcos){reference-type="ref" reference="thmcos"}. Thus, by lemma [\[howcom\]](#howcom){reference-type="ref" reference="howcom"}, it follows that $$\mathrm{excess\:}\mathcal{F}_j < d_0,$$ contradicting the hypothesis of the theorem. ◻
:::

::: proof
*of Theorem [\[infmain\]](#infmain){reference-type="ref" reference="infmain"}.* We only need to show that the positive excess conditions are sufficient, since they are obviously necessary. In addition, we may assume that the $1$-skeleton of the Poincaré dual $T^*$ is connected (if not, we prove the theorem for each connected component separately).

Now, we pick a pair of adjacent base vertices $v_1, v_2 \in V(T),$ and fix $d(v_1, v_2) = 1$. Now, for $v, w \in V(T)$ we define $d_c(v, w)$ to be equal to the combinatorial distance between $v$ and $w$ in the $1$-skeleton of $T$. Now, define $\mathcal{F}_i$ to be the span of all vertices $u$, such that $d_c(v_1, u) \leq i$. The complex $\mathcal{F}_i$ is finite by local finiteness of $T$. In addition, $\bigcup_i
\mathcal{F}_i = T$, so every finite subcomplex of $T$ belongs to some $\mathcal{F}_i$. For each $\mathcal{F}_i$ we consider a geometric realization $S(\mathcal{F}_i)$, whose existence is guaranteed by lemma [\[linref\]](#linref){reference-type="ref" reference="linref"} (there are many such realizations, we pick any one of them).

Now, enumerate the faces of $T$, in such a way that $t_1$ contains the edge $v_1 v_2$, and, for any $j$, the faces $t_j$ and $t_{j+1}$ are adjacent (that is, share an edge) in $T$. For each triangle, we have the space of shapes (similarity classes), given (for example) by the complex parameter $z$, obtained by placing the first two vertices of the triangle at the points $0$ and $1$ in the complex plane, and reading off the position of the third point (in the upper half-plane, assuming the triangle is positively oriented). Theorem [\[infty\]](#infty){reference-type="ref" reference="infty"} tells us that for any face $t$ of $T$, the set of shape parameters of realizations of $t$ is contained in a compact set $C_t$ (since the ratio of lengths of any two sides is bounded by some constant, depending on the function $\Delta$). We can think of each $S(\mathcal{F}_i)$ as being an element of $C = \prod_j C_{t_j}$, which is a compact set by Tykhonov's theorem, and hence we can extract a convergent subsequence from $S(\mathcal{F}_1), \ldots,
S_(\mathcal{F}_k), \ldots$. Call the limit of that subsequence $\mathcal{S}$. Since the dihedral angles are obviously continuous functions of the triangle parameters, the dihedral angles of $\mathcal{S}$ will be given by $\Delta$, and so $\mathcal{S}$ is the sought-after realization. ◻
:::

*Note.* For the comfort of more analytically inclined readers, it should be pointed out that the last argument is just an Arzela-Ascoli -- uniform convergence on compact sets argument.
