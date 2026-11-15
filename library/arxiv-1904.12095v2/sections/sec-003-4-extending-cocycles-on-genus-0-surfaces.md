---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-003-4-extending-cocycles-on-genus-0-surfaces
section_title: "Extending cocycles on genus 0 surfaces"
section_number: 4
pages: 9-12
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 1.0
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
[]{#sec:vertexCocycles label="sec:vertexCocycles"}

Let us define a punctured topological polyhedron which we will use as model for a "vertex link" of $\hat\mathcal{T}$ when removing some prisms.

::: definition
[]{#def:puncTopPolyhed label="def:puncTopPolyhed"} Let $L$ be a topological polyhedron, i.e., a decomposition of an oriented $2$-sphere into polygons. Let $P_1, \dots, P_p$ be selected two-cells of $L$ such that $\partial P_i \cap \partial P_j \not =\emptyset$ for all $i\not=j$. We call $(L,L\setminus \bigcup P_l)$ a punctured topological polyhedron.
:::

The complex $L\setminus \bigcup P_l$ will often be equipped with the following kind of cocycle.

::: definition
Let $X$ be a surface with boundary and with a decomposition into polygons. A $(\mathrm{SO}_{3}, \mathrm{SO}_{2})$-cocycle on $X$ is a $\mathrm{SO}_{3}$-cocycle where edges in the boundary $\partial X$ are labeled by rotations $R_\omega\in\mathrm{Im}(\mathrm{SO}_{2}\hookrightarrow\mathrm{SO}_{3})$ about the $z$-axis.
:::

The goal of this section is to give a criterion when such a cocycle on $L\setminus \bigcup P_l$ extends to a $\mathrm{SO}_{3}$-cocycle on $L$.

::: definition
Let $X$ be a $2$-complex. An edge-loop $\Gamma$ is a word in the oriented edges of $X$ such that the end of one edge coincides with start of the next edge (when reading the word from right to left and cyclically).
:::

Note that by parametrizing the oriented edges of $X$ and concatenating them in the order given by $\Gamma$, we obtain a geometric realization of $\Gamma$ that is a (based) topological loop in $X$. Also note that a $\mathcal{G}$-cocycle on $X$ assigns a value in $\mathcal{G}$ to an edge-loop $\Gamma$ obtained by multiplying the labels of the oriented edges in the respective order. The value assigned to $\Gamma$ depends only on the homotopy type of (the geometric realization of) $\Gamma$ and, in particular, is trivial if the loop is contractible in $X$.

::: definition
[]{#def:gimbalLoop label="def:gimbalLoop"} Let $(L,L\setminus \bigcup P_l)$ be a punctured topological polyhedron. A gimbal loop $\Gamma$ is a word in the oriented edges of $L$ and the selected two cells $P_1, \dots, P_p$ such that

-   each $P_1, \dots, P_p$ is contained in $\Gamma$ exactly once,

-   each $P_l$ in $\Gamma$ is preceeded (when reading the word from right to left and cyclically) by an edge $e_j$ such that the endpoint of $e_j$ is a vertex of $\partial P_l$, and

-   dropping all $P_1, \dots, P_p$ from $\Gamma$ results in an edge loop. This edge loop bounds a disk in $L\setminus\bigcup P_l$. The interior of the disk embeds into $L\setminus\bigcup P_l$ matching the orientation of $L$.
:::

::: example
[]{#example:GimbalLoop label="example:GimbalLoop"} Figure [\[fig:gimbalLoop\]](#fig:gimbalLoop){reference-type="ref" reference="fig:gimbalLoop"} shows an example of a gimbal loop $\Gamma$ for $p=3$. The corresponding word is $e_6 P_2 e_5 e_4 P_1 e_3 e_2 P_3 e_1.$
:::

<figure id="fig:splicedGimbalLoop">
<div class="center">
<div class="center">

</div>
<div class="center">

</div>
<p><br />
</p>
</div>
<figcaption>The edge loop obtained when replacing <span class="math inline"><em>P</em><sub><em>l</em></sub></span> by <span class="math inline">∂<em>P</em><sub><em>l</em></sub></span> in a gimbal loop <span class="math inline"><em>Γ</em></span>.</figcaption>
</figure>

::: definition
[]{#def:defGimbalFunction label="def:defGimbalFunction"} Let $(L,L\setminus \bigcup P_l)$ be a punctured topological polyhedron and $\Gamma$ be a gimbal loop. Fix a $(\mathrm{SO}_{3},\mathrm{SO}_{2})$-cocycle on $L\setminus \bigcup P_l$. Assume we are given numbers $(d_1,\dots,d_p)$. Recall that the cocycle assigns a $\mathrm{SO}_{3}$-matrix to every edge in $\Gamma$. Assign to each $P_l$ in $\Gamma$ the rotation $R_{d_l}\in\mathrm{Im}(\mathrm{SO}_{2}\hookrightarrow\mathrm{SO}_{3})$. We call the product of the matrices assigned to the letters in $\Gamma$ the gimbal matrix $m_\Gamma(d_1,\dots,d_p)$. Furthermore, we call the function $$g_\Gamma:\mathbb R^p\to\mathbb R^3,\quad (d_1,\dots, d_p)\mapsto\left(m_\Gamma(d_1,\dots,d_p)_{01},m_\Gamma(d_1,\dots,d_p)_{02},m_\Gamma(d_1,\dots,d_p)_{12}\right)$$ assigning the upper triangular entries of the gimbal matrix the gimbal function.
:::

Recall that a $(\mathrm{SO}_{3},\mathrm{SO}_{2})$-cocycle on $L\setminus \bigcup P_l$ assigns a rotation $R_\omega\in\mathrm{Im}(\mathrm{SO}_{2}\hookrightarrow\mathrm{SO}_{3})$ to each edge in $\partial P_l$ (with orientation induced from the orientation of $P_l\subset L$) where we pick $\omega\in(-\pi,\pi]$. Let $\delta_l$ denote the sum of all the angles $\omega$ over the edges of $\partial P_l$. For example, $\delta_2$ in Figure [\[fig:gimbalLoop\]](#fig:gimbalLoop){reference-type="ref" reference="fig:gimbalLoop"} is the sum of the angles $\omega$ associated to the edges $e^{-1}_{6}, e_{19}, e_{18}, e_{17}, e_{16},$ and $e_{15}.$

::: lemma
Using the same setup as in Definition [\[def:defGimbalFunction\]](#def:defGimbalFunction){reference-type="ref" reference="def:defGimbalFunction"}, we have $g_\Gamma(2\pi,\dots,2\pi)=g_\Gamma(\delta_1,\dots,\delta_p)=(0,0,0)$. []{#lemma:gimbalMatrixId label="lemma:gimbalMatrixId"}
:::

::: proof
*Proof.* Assume each $d_l=2\pi$. Then each $R_{d_l}$ is the identity and thus can be dropped from the gimbal matrix $m_\Gamma(2\pi,\dots,2\pi)$. Thus the gimbal matrix is equal to the matrix the cocycle assigns to the edge loop obtained when dropping the $P_i$. This edge loop is contractible. Thus the gimbal matrix is the identity and $g_\Gamma(2\pi,\dots,2\pi)=(0,0,0)$.\
The gimbal loop $\Gamma$ can also be turned into an edge loop by replacing each $P_l$ in $\Gamma$ by a word in the oriented edges in $\partial P_l$. Here we use the orientation of $\partial P_l$ induced from the $P_l\subset L$ and start traversing $\partial P_l$ at the endpoint of the preceding edge. Figure [1](#fig:splicedGimbalLoop){reference-type="ref" reference="fig:splicedGimbalLoop"} shows this edge loop for Example [\[example:GimbalLoop\]](#example:GimbalLoop){reference-type="ref" reference="example:GimbalLoop"}. The corresponding word is: $$e_6(e_6^{-1}e_{19}e_{18}e_{17}e_{16}e_{15})e_5e_4(e_4^{-1}e_{14}e_{13}e_{12}e_{11})e_3e_2(e_2^{-1}e_{10}e_9e_8e_7)e_1.$$ Note that by definition of $\delta_l$, the matrix assigned to this edge loop by the cocycle is equal to the gimbal matrix $m_\Gamma(\delta_1,\dots,\delta_p)$. This edge loop is again contractible and thus $g_\Gamma(\delta_1,\dots,\delta_p)=(0,0,0)$. To see that the edge loop is contractible, note that a genus 0 surface with $p$ boundary components can be obtained by attaching a 2-cell to a 1-complex consisting of $p$ loops and $p$ arcs connecting the loops to common base point. The edge looped can be homotoped into this form since it bounds a disk with interior embedding into $L\setminus \cup P_l$, see Figure [\[fig:gimbalLoopSkeleton\]](#fig:gimbalLoopSkeleton){reference-type="ref" reference="fig:gimbalLoopSkeleton"}.

<figure id="fig:gimbal">
<div class="center">
<div class="center">

</div>
<div class="center">

</div>
<p><br />
</p>
</div>
<figcaption>A gimbal.</figcaption>
</figure>

 ◻
:::

Let $Dg_\Gamma:\mathbb R^p\to M(3\times p, \mathbb R)$ denote the Jacobian of $g_\Gamma$ and $[Dg_\Gamma(K)]$ be the interval closure of $Dg_\Gamma(K)$, i.e., the smallest (axis-aligned) closed box containing $Dg_\Gamma(K)$ when thinking of the matrix space $M(3\times p, \mathbb R)$ as $\mathbb R^{3p}$. We say that $[Dg_\Gamma(K)]$ is invertible if every matrix in $[Dg_\Gamma(K)]$ is invertible.

::: definition
[]{#def:gimbalLockAvoided label="def:gimbalLockAvoided"} Using the same setup as in Definition [\[def:defGimbalFunction\]](#def:defGimbalFunction){reference-type="ref" reference="def:defGimbalFunction"}, let $K\subset \mathbb R^p$ be a box. We say that $K$ avoids gimbal lock with respect to $\Gamma$ if $[Dg_\Gamma(K)]$ is invertible.
:::

::: remark
The term gimbal lock is inspired by the mechanical device called gimbal or Cardan suspension used to achieve an arbitrary rotation in $\mathrm{SO}_{3}$, see Figure [2](#fig:gimbal){reference-type="ref" reference="fig:gimbal"}. Letting $d_1, d_2$ and $d_3$ denote the Euler angles at the joints from the grounding boxes to the inner-most ring, the rotation achieved by the gimbal is given by the matrix $$(d_1,d_2,d_3)\mapsto R_{d_1} \left(\begin{smallmatrix} &  & -1\\ & 1 & \\ 1 & & \end{smallmatrix}\right) R_{d_2} \left(\begin{smallmatrix} &  & 1\\ & 1 & \\ -1 & & \end{smallmatrix}\right) R_{d_3}$$ and a configuration of $(d_1, d_2, d_3)$ where this map does not have full rank is known as gimbal lock. Note the formal similarity of this product to the gimbal matrix $m_\Gamma(d_1,\dots, d_p)$.
:::

The following lemma is not useful in the general setting, but illustrates the principle we will use later (also see Example [\[example:singleEdgeViolation\]](#example:singleEdgeViolation){reference-type="ref" reference="example:singleEdgeViolation"}):

::: lemma
Using the same setup as in Definition [\[def:defGimbalFunction\]](#def:defGimbalFunction){reference-type="ref" reference="def:defGimbalFunction"}, let $K\subset \mathbb R^p$ be a box avoiding gimbal lock with respect to $\Gamma$ such that $(2\pi, \dots, 2\pi) \in K$. If $(\delta_1,\dots,\delta_p)\in K$, then all $\delta_l=2\pi$ and the cocycle extends to $L$. []{#lemma:noGimbalImpliesAllEqnsVertexLink label="lemma:noGimbalImpliesAllEqnsVertexLink"}
:::

::: proof
*Proof.* A standard result about the interval Newton method says that $g_\Gamma$ is injective on $K$ since $[Dg_\Gamma(K)]$ is invertible. Thus, Lemma [\[lemma:gimbalMatrixId\]](#lemma:gimbalMatrixId){reference-type="ref" reference="lemma:gimbalMatrixId"} implies that $\delta_l=2\pi$. ◻
:::
