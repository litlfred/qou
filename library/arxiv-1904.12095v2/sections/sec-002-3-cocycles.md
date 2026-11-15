---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-002-3-cocycles
section_title: "Cocycles"
section_number: 3
pages: 6-9
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 1.0
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
[]{#sec:cocycles label="sec:cocycles"}

We will describe how to compute a representation[^1] $\pi_1(\mathcal{T})\to\mathrm{PGL}_{2}(\mathbb C)$ from an assignment of parameters $\nu_e$ as in Theorem [\[thm:hypStruct\]](#thm:hypStruct){reference-type="ref" reference="thm:hypStruct"} using cocycles inspired by [@higherGluingEqns Section 9] as follows:

::: definition
Let $\mathcal{G}$ be a group and $X$ be a space with a polyhedral decomposition. A $\mathcal{G}$-cocycle on $X$ is an assignment of elements in $\mathcal{G}$ to the oriented edges of $X$ such that the product around each face is the identity and such that reversing the orientation of an edge replaces the labeling by its inverse.
:::

All cocycles in this section are $\mathrm{PGL}_{2}(\mathbb C)$-cocycles.

Given a matrix $G$ fulfilling the conditions in Lemma [\[lemma:singleGeomSimp\]](#lemma:singleGeomSimp){reference-type="ref" reference="lemma:singleGeomSimp"}, we will construct a cocycle on the doubly truncated simplex $\overline{\Delta}$ coming from a simplex $\Delta$, see Figure [\[fig:DoublyTruncated\]](#fig:DoublyTruncated){reference-type="ref" reference="fig:DoublyTruncated"}. We index a vertex $v$ of $\overline{\Delta}$ by the permutation $\sigma\in \mathbf{S}_4$ such that the vertex of $\Delta$ closest to $v$ is $\sigma(0)$, the edge of $\Delta$ closest to $v$ is $\sigma(0)\sigma(1)$, and the face of $\Delta$ closest to $v$ is $\sigma(0)\sigma(1)\sigma(2)$. We label an oriented long, middle, or short edge of $\overline{\Delta}$ by $\alpha^{\sigma(0)\sigma(1)\sigma(2)}, \beta^{\sigma(0)\sigma(1)\sigma(2)},$ respectively $\gamma^{\sigma(0)\sigma(1)\sigma(2)}$ if it starts at the vertex indexed by $\sigma$. Let us introduce the notion of standard position to define the $\mathrm{PGL}_{2}(\mathbb C)$-matrices assigned to these edges.

<figure id="fig:standardPos">
<div class="center">

</div>
<figcaption>A simplex in different standard positions.</figcaption>
</figure>

We think of the upper half space model of hyperbolic 3-space as a subset $\mathbb H^3=\{w = z+t\jmath: t>0\}$ of the quaternions. Recall that $\mathrm{Isom}^+(\mathbb H^3)\cong\mathrm{PGL}_{2}(\mathbb C) \cong\mathrm{PSL}_{2}(\mathbb C)$ where the action of a $\mathrm{SL}_{2}(\mathbb C)$-matrix on $\mathbb H^3$ is given by $$\left(\begin{array}{cc}a &b\\ c&d\end{array}\right)\mapsto \left( w \mapsto (aw+b)\cdot(cw+d)^{-1} \right).$$

::: definition
[]{#def:standardPosSimplex label="def:standardPosSimplex"} We say that a positively oriented, finite simplex $\Delta$ is in $\sigma$-standard position where $\sigma\in \mathbf{S}_4$ if vertex

-   $\sigma(0)$ is at $\jmath$,

-   $\sigma(1)$ at $t\jmath$ with $t>1$,

-   $\sigma(2)$ at $a+t\jmath$ with $a>0$ and

-   $\sigma(3)$ at $z+t\jmath$ with $\mathrm{Im}(z)>0$ if $\sigma$ is even and $\mathrm{Im}(z)<0$ otherwise.
:::

An example of this is shown in Figure [1](#fig:standardPos){reference-type="ref" reference="fig:standardPos"}. Geometrically, the motivation for this definition is that two faces of two (not necessarily distinct) simplices line up in $\mathbb H^3$ if the respective edge lengths match and the two simplices are in the respective standard positions. More precisely, let $f_1\in\{0,1,2,3\}$ be a face of the simplex $\Delta_1$ and $f_2\in\{0,1,2,3\}$ of $\Delta_2$. Let $\sigma\in \mathbf{S}_4\setminus \mathbf{A}_4$ with $\sigma(f_1)=f_2$ be a pairing of the two faces. If the edge lengths match under this pairing, then the faces match if each $\Delta_k$ is in $\sigma_k$-standard position where $\sigma_1$ is any permutation with $\sigma_1(3)=f_1$ and $\sigma_2=\sigma\circ \sigma_1$.

This definition also gives us a cocycle as follows (also see Figure [1](#fig:standardPos){reference-type="ref" reference="fig:standardPos"}):

::: definition
Consider the isometry class of a finite simplex $\Delta$. Given an oriented edge $e$ of $\overline{\Delta}$, let $\sigma$ and $\sigma'$ be the permutations that index the vertex where $e$ starts and, respectively, ends. The natural cocycle on $\overline{\Delta}$ is the cocycle assigning to each edge $e$ the $\mathrm{PGL}_{2}(\mathbb C)$-matrix taking $\Delta$ from $\sigma$-standard position to $\sigma'$-standard position.
:::

Note that we can identify Euclidean 3-vector space isometrically with the tangent space of a point in $\mathbb H^3$ such that the tangents corresponding to the $x$-, $y$-, and $z$-axis are parallel to the real line, the imaginary line, respectively, the line $t\jmath$ (see Figure [1](#fig:standardPos){reference-type="ref" reference="fig:standardPos"}). Thus, we can associate a $\mathrm{SO}_{3}$-matrix to an element in $\mathrm{Isom}^+(\mathbb H^3)$ fixing a (finite) point of $\mathbb H^3$. Let $$R_\omega = \left(\begin{array}{ccc} \cos\omega & -\sin\omega & 0 \\ \sin\omega & \phantom{-}\cos\omega &  0\\0 &0 & 1\end{array}\right)$$ be the rotation about the $z$-axis by the angle $\omega$.

::: lemma
The natural cocycle on $\overline{\Delta}$ can be computed from the vertex Gram matrix $G$ as follows (apply even permutations $\sigma\in \mathbf{A}_4$ to obtain labels for all edges): $$\alpha^{120}=\alpha^{210}=\alpha^{123}=\alpha^{213}=\left(\begin{array}{cc}0  & \sqrt{v_{12}^2-1} - v_{12}\\1 & 0 \end{array}\right),$$ $$\beta^{123}=\beta^{132}=\left(\begin{array}{cc}-\cos(\eta_{1,32}/2) & \sin(\eta_{1,32}/2)\\ \phantom{-}\sin(\eta_{1,32}/2) & \cos(\eta_{1,32}/2)\end{array}\right),$$ $$\gamma^{123}=\left(\gamma^{120}\right)^{-1}=\gamma^{210}=(\gamma^{213})^{-1}=\left(\begin{array}{cc}\exp(\imath\theta_{03}) & 0 \\ 0 & 1\end{array}\right).$$ Note that $\beta^{123}$ and $\gamma^{123}$ fix the point $\jmath\in\mathbb H^3$ and the associated $\mathrm{SO}_{3}$-matrices are: $$\left(\begin{array}{ccc}
-\cos\eta_{1,32} & \phantom{-}0 & \sin \eta_{1,32} \\
 0 & -1 & 0 \\
  \phantom{-}\sin\eta_{1,32} & \phantom{-}0 & \cos\eta_{1,32} \end{array}\right)\quad\mbox{and}\quad R_{\theta_{03}}.$$ []{#lemma:coycleAssignment label="lemma:coycleAssignment"}
:::

::: proof
*Proof.* $\alpha^{120}$ is an involution exchanging the points $\jmath$ and $\exp(l_{12})\jmath$. The associated $\mathbb CP^1$-automorphism is of the form $z\mapsto x/z$ and exchanges $1$ and $\exp(l_{12})$. An elementary calculation gives the value for $x$.\
Consider the hyperbolic plane $\mathbb H^2=\{x+t\jmath: x\in \mathbb R, t>0\}\subset \mathbb H^3$. $\beta^{123}$ is the composition of the rotation of $\mathbb H^2$ about $\jmath$ by $\eta_{1,32}$ with the involution fixing the line $t\jmath$ pointwise. We obtain the $\mathrm{PSL}_{2}(\mathbb R)$-matrix for the rotation of $\mathbb H^2$ by conjugating the rotation of the unit disk by $\eta_{1,32}$ with the matrix taking the upper half plane model to the Poincare disk model of hyperbolic 2-space: $$\left(\begin{array}{cc}\imath& 1\\ 1 & \imath\end{array}\right)^{-1} \cdot \left(\begin{array}{cc} \exp(\imath\eta_{1,32}/2) & 0 \\ 0 & \exp(-\imath\eta_{1,32}/2)\end{array}\right)\cdot \left(\begin{array}{cc}\imath& 1\\ 1 & \imath\end{array}\right)$$ ◻
:::

Given an oriented triangulation $\mathcal{T}$, let $\overline{\mathcal{T}}$ be the complex obtained by replacing each simplex $\Delta$ by the double truncated simplex $\overline{\Delta}$. The long and short edges of $\overline{\mathcal{T}}$ about an edge $e$ of $\mathcal{T}$ form a prism, see Figure [\[fig:Prism\]](#fig:Prism){reference-type="ref" reference="fig:Prism"}. Given an assignment of edge parameters $\nu_e$ for $\mathcal{T}$, this prism about an edge $e\in E(\mathcal{T})$ is a cocycle if and only if the short edges compose to the identity, which is equivalent to $\Theta_e$ being a multiple of $2\pi$. Let $\hat\mathcal{T}$ denote the complex $\overline{\mathcal{T}}\cup\mbox{Prisms}$.

::: theorem
[]{#thm:cocycleExtendingToTrig label="thm:cocycleExtendingToTrig"} Consider an assignment of a parameter $\nu_e<-1$ to each edge of an oriented, finite triangulation $\mathcal{T}$.

1.  []{#cocycCondA label="cocycCondA"} If each matrix $G_\Delta$ is realized, we obtain a natural cocycle on $\overline{\mathcal{T}}$ and, thus, a representation $\pi_1(\overline{\mathcal{T}})\to\mathrm{PGL}_{2}(\mathbb C)$ (up to conjugation, unless we pick a vertex of $\overline{\mathcal{T}}$ as basepoint).

2.  []{#cocycCondB label="cocycCondB"} If, furthermore, $\Theta_e$ is a multiple of $2 \pi$ for every $e\in E(\mathcal{T})$, the cocycle extends to $\hat{\mathcal{T}}$ and, thus, yields a representation of $\pi_1(\mathcal{T})\to\mathrm{PGL}_{2}(\mathbb C)$.

3.  []{#cocycCondC label="cocycCondC"} If, furthermore, $\Theta_e = 2\pi$ for every $e\in E(\mathcal{T})$, the representation is giving a hyperbolic structure on $\mathcal{T}$. []{#thm:cocycle label="thm:cocycle"}
:::

::: proof
*Proof.* Note that $\alpha$ and $\beta$ in Lemma [\[lemma:coycleAssignment\]](#lemma:coycleAssignment){reference-type="ref" reference="lemma:coycleAssignment"} are involutions and only involve the parameters $v_{ij}$ on the edges of the triangle containing the respective $\alpha$ and $\beta$. Hence, the matrices on two big hexagons on two doubly-truncated simplices are compatible and the hexagons can be identified if the edge parameters on the respective triangles of the corresponding tetrahedra match. This proves [\[cocycCondA\]](#cocycCondA){reference-type="eqref" reference="cocycCondA"}.\
[\[cocycCondB\]](#cocycCondB){reference-type="eqref" reference="cocycCondB"} follows from the above comment about the prisms being cocycles and the fact that $\hat{\mathcal{T}}$ differs from $\mathcal{T}$ only by a set of 3-balls which do not change $\pi_1$.\
[\[cocycCondC\]](#cocycCondC){reference-type="eqref" reference="cocycCondC"} is just restating Theorem [\[thm:hypStruct\]](#thm:hypStruct){reference-type="ref" reference="thm:hypStruct"}. ◻
:::

[^1]: For consistency on how arrows in a category compose, the loop traversing the loop $a$ first and the loop $b$ second is denoted by $ba$ in $\pi_1(\mathcal{T})$.
