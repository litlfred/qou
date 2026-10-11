---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
text_source: latex
latex_prose_ratio: 0.801
latex_coverage_ratio: 0.988
---
Up to isometry, a finite hyperbolic 3-simplex is determined by its $6$ edge parameters, by which we mean either the edge lengths $l_{ij}$ or the respective entries of its vertex Gram matrix $v_{ij}=-\cosh(l_{ij})$. Thus, an assignment of a parameter to each edge of a finite triangulation $\mathcal{T}$ of a closed 3-manifold determines a hyperbolic structure for each $3$-simplex of $\mathcal{T}\!{}$. If certain conditions are fulfilled, the hyperbolic structures on the individual simplices are compatible and form a hyperbolic structure on the manifold (see [@heardThesis] and Section [2](#sec:hypStru){reference-type="ref" reference="sec:hypStru"}).

Existing software (such as Casson's Geo [@casson:geo] and Heard's Orb [@orb]) finds a numerical approximation for the edge parameters using Newton's method and reports whether the necessary equations are fulfilled within an error smaller than a certain $\varepsilon$. This suggests but does not prove hyperbolicity. The aim of this paper is to describe how to take such a numerical approximation and rigorously prove hyperbolicity by giving real intervals that are verified to contain a solution to all the necessary equations and inequalities. An algorithm either returning such intervals or (conservatively) reporting failure is described in Section [\[sec:algo\]](#sec:algo){reference-type="ref" reference="sec:algo"}. The algorithm is a hyperbolicity verification procedure but not a hyperbolicity decision procedure since its failure just means that the given candidate approximation was not close enough to a hyperbolic structure or needs to be perturbed to avoid "gimbal lock" (explained below). An implementation of this algorithm is available at [@veriClosedRepo]. Therefore, this paper is achieving for finite triangulations what Hoffman, Ichihara, Kashiwagi, Masai, Oishi, and Takayasu [@hikmot] did for ideal triangulations (HIKMOT's functionality has been integrated into SnapPy [@SnapPy] by the author since version 2.3).

This is motivated by applications that benefit from using geometric finite triangulations in place of geometric spun triangulation. In particular, such applications no longer need to overcome the incompleteness locus. An example is the generation of cohomology fractals for a closed hyperbolic 3-manifold. As shown in [@cohomologyFractals Figure 8.7], the incompleteness locus produces artifacts in the raytraced image of a cohomology fractal which simply disappear when using finite triangulations instead. Another example is the algorithm proposed in [@HHGT] to rigorously compute the length spectrum for a hyperbolic 3-manifold. This algorithm requires tiling $\mathbb H^3$ with translates of a fundamental domain to cover a ball of specified radius and thus would not work if there is incompleteness locus.

An even more basic motivation is proving hyperbolicity of a closed 3-manifold by finding a triangulation admitting a geometric structure. Restricting ourselves to just spun triangulations introduces a bottleneck. For example, the obvious spun triangulation of a closed census manifold such as `m135(1,3)` can fail to be geometric. Thus finding a geometric spun triangulation requires drilling and filling (or, in other words, finding a different closed geodesic $\gamma$ such that there is a geometric triangulation spun about $\gamma$). Even worse, some hyperbolic 3-manifolds such as `m007(3,1)` seem to lack any geometric spun triangulation unless we pass to a cover[^1]. Note that a geometric spun triangulation is known for every orientable closed manifold in the SnapPy census (except for `m007(3,1)` where a 3-fold cover is needed), see [@hikmot]. However, the process of finding such (covers admitting) geometric spun triangulations can be tedious and is not known to be possible in general. Furthermore, passing to a cover can complicate applications such as computing the length spectrum.

Potential future work might generalize the techniques of this paper to Heard's work [@heardThesis] on 3-orbifolds and Frigerio and Petronio's work [@frigPet] on 3-manifolds with geodesic boundary. To find hyperbolic structures on these, Heard's program Orb [@orb] uses triangulations with finite as well as ideal and "hyperinfinite" vertices. Note that some of the theory in this paper also carries over to spherical and Euclidean geometry and might generalize to yield methods for verifying spherical or Euclidean structures on finite triangulations.

Like [@hikmot], we use interval arithmetic methods such as the interval Newton method or the Krawczyk test. These methods can only show the existence of a solution to a system of equations if the Jacobian matrix is invertible near that solution. If the Jacobian fails to be invertible, these methods can only show the existence of a solution to a subset of the equations. This applies to the edge equations whether we are solving for shapes in the cusped case or for edge lengths in the closed case. Hence, in both cases, we need an additional result showing that there is a redundancy among the edge equations such that solving a suitable subset of them is sufficient. For ideal triangulations, this result is due to Neumann-Zagier [@NeumannZagier; @NeumannComb] and Moser [@moser] (see Appendix). For finite triangulations, we derive such a result in this paper.

Note that while we actually have exactly as many variables as equations in the case of finite triangulations (namely, one per edge), the Jacobian of this system of equations has a kernel at a solution corresponding to a hyperbolic structure. This is because we can move each individual finite vertex of a triangulation in the hyperbolic manifold and obtain a whole family of solutions (see Theorem [\[thm:hypStructAreSubmanifold\]](#thm:hypStructAreSubmanifold){reference-type="ref" reference="thm:hypStructAreSubmanifold"}). Thus, we need to use a two-step strategy to verify a hyperbolic structure: First, we drop some edge equations and fix an equal number of edge parameters such that we can apply interval arithmetic methods to find intervals verified to contain a solution to the subsystem of equations we kept. Next, we show that this solution is also a solution to the equations we dropped earlier and thus that the intervals for the edge parameters contain a point giving a hyperbolic structure. Interval arithmetic can verify that the error of the dropped equations is small and we will show that if the dropped equations are fulfilled approximately, then they are fulfilled exactly provided that a certain condition we call "gimbal lock" is avoided.

To define gimbal lock, we will look at the complex of doubly-truncated simplices associated to the triangulation and an assignment of $\mathrm{PGL}_{2}(\mathbb C)$-matrices to the edges of the complex computed from the edge parameters (see Section [\[sec:cocycles\]](#sec:cocycles){reference-type="ref" reference="sec:cocycles"}). The cocycle condition says that the matrices on the edges of a polygon must multiply to the identity. Since a subset of the edge equations is known to be fulfilled, the cocycle condition is known to hold for some polygons but not necessarily for others. The goal is to show that it holds for all polygons so that we get a $\mathrm{PGL}_{2}(\mathbb C)$-representation of the fundamental group (see Section [\[sec:vertexCocycles\]](#sec:vertexCocycles){reference-type="ref" reference="sec:vertexCocycles"} and [\[sec:extendCocycles\]](#sec:extendCocycles){reference-type="ref" reference="sec:extendCocycles"} and examples in Section [\[section:examples\]](#section:examples){reference-type="ref" reference="section:examples"}). Roughly speaking, the idea is that if the product of three small rotations about three axes in generic position is the identity, then each rotation must be the identity. Inspired by the mechanical device called gimbal (see Figure [\[fig:gimbal\]](#fig:gimbal){reference-type="ref" reference="fig:gimbal"}), we say that we avoid "gimbal lock": if a gimbal is not in its locked position, then we can apply any small rotation to the inner-most ring, or equivalently, if we fix the inner-most ring, none of the other rings can be turned.

We describe the resulting algorithm to obtain real intervals in Section [\[sec:algo\]](#sec:algo){reference-type="ref" reference="sec:algo"}. The algorithm is effective and able to verify a hyperbolic structure on all 36093 closed orientable manifolds in the Hodgson-Weeks census [@hwcensus] and in the census bundle by Bell [@bellBundleCensus], see Section [\[sec:results\]](#sec:results){reference-type="ref" reference="sec:results"}. Branched double covers of knots or links (or more precisely: double covers of $S^3$ branched over a knot or link) provide a good class of test cases since finding a geometric spun-triangulation of some of them can be challenging. Using finite triangulations instead, we are able to prove the following new result:

::: theorem
[]{#thm:hyperbolicBranchedDoubleCovers label="thm:hyperbolicBranchedDoubleCovers"} Out of the 313230 knots with up to 15 crossings (not including the unknot), exactly 193839 have a hyperbolic branched double cover.\
Out of the 120573 links with up to 14 crossings (with at least two components), exactly 37709 have a hyperbolic branched double cover.
:::

Section [\[sec:discussion\]](#sec:discussion){reference-type="ref" reference="sec:discussion"} concludes with a conjecture that implies that a hyperbolic structure on a finite triangulation can always be perturbed so that the algorithm can verify it.

The appendix in Section [\[sec:hikmotGap\]](#sec:hikmotGap){reference-type="ref" reference="sec:hikmotGap"} points out a gap in the argument (but not the algorithm) of the HIKMOT paper.

# Acknowledgements

The author wishes to thank Marc Culler, Nathan Dunfield, Damian Heard, Neil Hoffman, and Christian Zickert for helpful discussions. Special thanks goes to Nathan Dunfield for finding some mistakes and providing some of the examples and some Python scripts for Regina.

# Hyperbolic structures on finite triangulations {#sec:hypStru}

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

[^1]: In not yet published work, Maria Trnkova has proven that there is no geometric spun triangulation of `m007(3,1)` with a small number of tetrahedra.
