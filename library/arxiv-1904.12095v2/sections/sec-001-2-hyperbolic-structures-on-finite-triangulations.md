---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-001-2-hyperbolic-structures-on-finite-triangulations
section_title: "Hyperbolic structures on finite triangulations"
section_number: 2
pages: 4-6
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
text_source: latex
latex_prose_ratio: 0.851
latex_coverage_ratio: 0.976
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
[]{#sec:hypStru label="sec:hypStru"}

Consider the isometry class of a positively oriented, finite geodesic simplex $\Delta$ with vertices labeled $0, \dots, 3$ in $\mathbb H^3$. We briefly review the relationship of the edge lengths and the angles of $\Delta$ following [@heardThesis] with one difference though: we use a slightly simpler definition for the vertex Gram matrix $G$ where all diagonal entries are $-1$ since we are not interested in generalized simplices here. To be consistent with the vertex labels, we $0$-index the rows and columns of a matrix (so $m_{00}$ denotes the top left-most entry).

<figure id="fig:Prism">
<div class="center">
<div class="center">

</div>
<div class="center">

</div>
<div class="center">

</div>
<p><br />
</p>
</div>
<figcaption>A prism.</figcaption>
</figure>

Let $l_{ij}$ denote the length of the edge between vertex $i$ and $j$. The vertex Gram matrix $G$ associated to the simplex is the symmetric $4\times 4$-matrix with entries $$v_{ij}=-\cosh(l_{ij}).$$ The edge lengths as well as the vertex Gram matrix uniquely determine the isometry class of the simplex. Let $c_{ij}$ denote the respective cofactor of $G$ which is given by $$c_{ij}=(-1)^{i+j} \det(G_{ij}),$$ where $G_{ij}$ is obtained by deleting the $i$-th row and $j$-th column. The dihedral angle between face $i$ and $j$ and the angle at vertex $i$ of the triangle $ijk$ (derived from the law of cosines) are then given by (also see Figure [\[fig:anglesInTet\]](#fig:anglesInTet){reference-type="ref" reference="fig:anglesInTet"}): $$\theta_{ij}=\arccos\left(\frac{c_{ij}}{\sqrt{c_{ii}c_{jj}}}\right) \quad\mbox{and}\quad \eta_{i,jk}=\arccos\left(\frac{v_{ij}v_{ik}+v_{jk}}{\sqrt{v_{ij}^2-1}\sqrt{v_{ik}^2-1}}\right). \label{eqn:dihedral}$$

::: definition
Let $G$ be a real symmetric $4\times 4$-matrix with $-1$ on the diagonal. We say that $G$ is realized if $G$ is the vertex Gram matrix of some finite, non-flat simplex.
:::

The following theorem is a special case of [@heardThesis Theorem 1.5] (also compare to [@ratcliffe:hyp Theorem 7.2.2]):

::: lemma
$G$ is realized if and only if

1.  $G$ has one negative and three positive eigenvalues (which is equivalent to the characteristic polynomial $p_G(x)=\det(x I - G)=x^4+4x^3+a_2x^2+a_1x+a_0$ having coefficients $a_2 < 0$, $a_1>0$, $a_0<0$ by the Budan-Fourier theorem [@algRealGeom]),

2.  $c_{ii}<0$ for all $i$, and[]{#item:condNegAdj label="item:condNegAdj"}

3.  $c^2_{ij} < c_{ii} c_{jj}$ for all $i$ and $j$,[]{#item:wellDefinedCos label="item:wellDefinedCos"}

where $c_{ij}$ denotes the respective cofactor of $G$. []{#lemma:singleGeomSimp label="lemma:singleGeomSimp"}
:::

Let $\mathcal{T}$ be an oriented, finite 3-dimensional triangulation (i.e., all vertex links are $2$-spheres) and let $E(\mathcal{T})$ denote the set of edges of $\mathcal{T}$. Assume we have an assignment of a length $l_e>0$, or equivalently, a parameter $\nu_e < -1$ to each $e\in E(\mathcal{T})$ where the two are related by the formula $\nu_e=-\cosh(l_e)$. This induces a symmetric $4\times 4$-matrix $G_\Delta$ for each simplex $\Delta$ of $\mathcal{T}$ where $v_{ii}=-1$ and $v_{ij}=\nu_e$ if $i\not=j$ and the edge of $\Delta$ from vertex $i$ to $j$ is incident to $e$. Let $\Theta_e$ denote the sum of all dihedral angles $\theta_{ij}$ incident to the edge $e$ of $\mathcal{T}$. We can now use [@heardThesis Lemma 2.4] to check whether this assignment yields a hyperbolic structure on $\mathcal{T}$:

::: theorem
An assignment of a parameter $\nu_e<-1$ to each edge $e$ of an oriented, finite triangulation $\mathcal{T}$ induces a hyperbolic structure on $\mathcal{T}$ if

1.  []{#main:condA label="main:condA"} each matrix $G_\Delta$ is realized (i.e., fulfills the conditions of Lemma [\[lemma:singleGeomSimp\]](#lemma:singleGeomSimp){reference-type="ref" reference="lemma:singleGeomSimp"}) and

2.  []{#main:condB label="main:condB"} $\Theta_e=2\pi$ for every $e\in E(\mathcal{T})$.

[]{#thm:hypStruct label="thm:hypStruct"}
:::
