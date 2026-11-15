---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-005-3-index-structures-and-1efficiency
section_title: "Index structures and 1–efficiency"
section_number: 3
pages: 9-16
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.891
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sec: index structures and 1-efficiency label="sec: index structures and 1-efficiency"}

We first give a sketch proof of Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"}, showing that a semi--angle structure implies 1--efficiency. We follow [@KR2] and indicate the required small modification. Suppose that $M$ is oriented with cusps and has an ideal triangulation $\mathcal{T}$ with a semi-angle structure. Assume that there is an embedded normal torus or Klein bottle or sphere or projective plane, where the normal torus is not a peripheral torus. Firstly, exactly as in [@Lackenby] the latter two cases are excluded by a simple Euler characteristic argument. Similarly, if there is a cube with knotted hole bounded by an embedded normal torus, then a barrier argument as in [@JR] establishes that there is a normal 2-sphere bounding a ball containing this normal torus, which is a contradiction. Embedded Klein bottles are excluded, so we are reduced to the cases of an embedded essential non peripheral normal torus or a normal torus bounding a solid torus.

In both cases, there is a sweepout between the normal torus and a peripheral normal torus (for essential tori) or to a core circle of the solid torus. By a minimax argument (see [@Rub], [@Sto]), there is an almost normal torus associated with this sweepout. This is either obtained by attaching a tube parallel to an edge to a normal 2-sphere or has a single properly embedded octagonal disc in a tetrahedron and a collection of normal triangular and quadrilateral discs. The first case is excluded, since we have ruled out such normal 2-spheres.

The semi-angle structure now implies that a standard combinatorial Gauss-Bonnet argument can be applied. Each polygonal disc in our torus has curvature given by $\Sigma_i \alpha_i  - (n-2)\pi$, where $n$ is the number of edges of the disc and $\alpha_i$ are the interior angles at the vertices of the disc. Gauss-Bonnet then says that the sum of the curvatures of all the discs is zero, since the Euler characteristic of the torus is zero. Every normal triangular disc contributes zero and each normal quadrilateral is non-positive in the curvature sum. On the other hand, any embedding of an octagon into an ideal tetrahedron with a semi-angle structure gives a strictly negative contribution. See Figure [1](#normal_octagon){reference-type="ref" reference="normal_octagon"}. Hence the Euler characteristic of such a surface cannot be zero and there could not have been an embedded normal torus to begin with. This completes the sketch proof. 0◻

<figure id="normal_octagon" data-latex-placement="htbp">
<p><span class="math inline"><em>α</em></span> at 174 335 <span class="math inline"><em>α</em></span> at 249 326 <span class="math inline"><em>α</em></span> at 141 76 <span class="math inline"><em>α</em></span> at 280 89 <span class="math inline"><em>γ</em></span> at 84 200 <span class="math inline"><em>γ</em></span> at 350 184 <span class="math inline"><em>β</em></span> at 241 212 <span class="math inline"><em>β</em></span> at 170 152</p>
<img src="draws_eps/normal_octagon" style="width:50.0%" />
<figcaption>A normal octagon in a tetrahedron with a semi-angle structure with angles <span class="math inline"><em>α</em>, <em>β</em>, <em>γ</em> ∈ [0, <em>π</em>]</span>. The curvature of this octagon is <span class="math inline">4<em>α</em> + 2<em>β</em> + 2<em>γ</em> − (8 − 2)<em>π</em> = 2<em>α</em> + 2<em>π</em> − 6<em>π</em> = 2<em>α</em> − 4<em>π</em> &lt; 0.</span></figcaption>
</figure>

A useful observation (see [@KR2]) following from Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"} is the following;

::: cor
[]{#strongly label="strongly"}

Suppose that $\mathcal{T}$ is an ideal triangulation of an oriented $3$-manifold $M$ with cusps. If $M$ is an-annular and $\mathcal{T}$ admits a semi-angle structure then $M$ is strongly 1-efficient.
:::

::: proof
*Proof.* The key observation is that the semi-angle structure on $\mathcal{T}$ lifts to a semi-angle structure on the lifted triangulation $\widetilde\mathcal{T}$, for any covering space $\widetilde M$ of $M$. Assume that there is an immersed normal torus $T$ in $M$ which is not a covering of the peripheral torus. If $\widetilde M$ is chosen as the covering space whose fundamental group corresponds to the image of $\pi_1(T)$, then $T$ lifts to a normal torus $\widetilde T$ so that the inclusion map induces an onto map $\pi_1(\widetilde T) \rightarrow \pi_1(\widetilde M)$.

We can now use $\widetilde T$ as a barrier (see [@JR]) to produce an embedded normal non-peripheral torus $T^*$, which is either essential and isotopic into a boundary cusp, or bounds a solid torus or cube with knotted hole. (Here the an-annular assumption is used to show that the covering space $\widetilde M$ is atoroidal). The rest of the argument is exactly the same as in Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"}. ◻
:::

:::: proof
*Proof of Theorem [\[index_structure_iff_1-efficient\]](#index_structure_iff_1-efficient){reference-type="ref" reference="index_structure_iff_1-efficient"}.* We closely follow Luo--Tillmann [@LT]. We use the following version of Farkas' lemma, which is given as Lemma 10 (3) in [@LT]:

::: lemma
Let $A$ be a real $K \times L$ matrix, $b\in\mathbb{R}^K$, and $\cdot$ denote the usual Euclidean inner product on $\mathbb{R}^K$. Then $\{x\in\mathbb{R}^L \mid Ax=b, x>0\} \neq \emptyset$ if and only if for all $y\in\mathbb{R}^K$ such that $A^Ty\neq 0$ and $A^Ty\leq 0,$ one has $y\cdot b<0.$
:::

For our purposes, $Ax=b$ is the matrix form [\[full_matrix_eqn\]](#full_matrix_eqn){reference-type="eqref" reference="full_matrix_eqn"} of the generalised angle structure equations, so $b=(2\pi, \ldots, 2\pi, \pi, \ldots, \pi)^T$. Consider a particular quad-choice $Q$, as in Definition [\[choice_of_quads\]](#choice_of_quads){reference-type="ref" reference="choice_of_quads"}. If there is to be an index structure, then we must be able to find the appropriate generalised angle structure $x$. That is, $x_l>0$ if $l$ corresponds to one of the $Q_n$, and $x_l$ can have any real value if not. We refer to the former as *restricted* variables, and the latter as *unrestricted* variables.

The problem with applying Farkas' lemma directly is that it applies to the set of solutions $\{Ax=b \mid x>0\}$. That is, *all* variables are strictly positive. However, we use a standard trick: for each unrestricted variable $x_l$, introduce a new variable $x_l'$. The new variable acts precisely like $-x_l,$ so the old $x_l$ can be written in the new coordinates as $x_l - x_l'$. This allows both new variables $x_l, x_l' > 0$, making them restricted variables, so that Farkas' lemma can be applied.

The effect that this has on the matrix $A$ is as follows: We get a new column after each unrestricted $x_l$ for $x_l'$, and the values in the new column are the negatives of the values in the column for $x_l$.

Now we apply Farkas' lemma. We get a solution to our system if and only if for all $y\in\mathbb{R}^K$ such that $A^Ty\neq 0$ and $A^Ty\leq 0,$ we have $y\cdot b<0.$ The transposed matrix $A^T$ has dual variables $(z_1, ..., z_n, w_1, ..., w_t)$, where the $w_i$ correspond to the tetrahedra and the $z_j$ correspond to the edges. The dual system $A^T(z,w)^T \leq 0$ is given by inequalities: $$w_i + z_j + z_k \leq 0$$ whenever the $i$th tetrahedron contains a quad that faces the edges $j$ and $k$ (which may not be distinct). This holds for all the rows corresponding to the $x_l$, and we get the following for the $x_l'$: $$-(w_i + z_j + z_k) \leq 0$$ The two of these together imply that $w_i + z_j + z_k = 0$ for the quads corresponding to unrestricted angles, while $w_i + z_j + z_k \leq 0$ for restricted angles. The rest of the argument is the same as in [@LT], as follows.

Kang and Rubinstein [@KR1] give a basis of the normal surface solution space $C(M; \mathcal{T})$ which consists of one element for each edge and one element for each tetrahedron of $\mathcal{T}$. For the edge $e$, the corresponding basis element has each of the quad types in the normal quadrilateral type sequence for $e$ with coefficient $-1$ (or $-2$ if that quad appears twice), and each of the triangle disc types that intersect $e$ with coefficient $+1$. For each tetrahedron $\sigma$, the corresponding basis element has each of the quad types in $\sigma$ with coefficient $-1$, and each of the triangle disc types in $\sigma$ with coefficient $+1$.

If we have a solution to the dual system, then we can form a normal surface solution class $W_{w,z}$ as a sum of tetrahedral and edge basis elements with coefficients given by the $w_i$ and $z_j$ corresponding to their tetrahedra and edges respectively. There is a linear functional $\chi^*$ on $\mathbb{R}^{7n}$ called the *generalised Euler characteristic*, which agrees with the Euler characteristic in the case of an embedded normal surface represented by an element of $C(M; \mathcal{T})$. It is shown in [@LT] that the generalised Euler characteristic $\chi^*(W_{w,z})$ is equal to $y\cdot b$, and that the normal quad coordinates of $W_{w,z}$ are given by $-(w_i + z_j + z_k)$. From the above inequalities, we find that the obstruction classes are solutions to the normal surface matching equations with zero quad coordinates for unrestricted angles, non-negative quad coordinates for restricted angles (i.e. the quads specified by the quad-choice $Q$), at least one quad coordinate strictly positive, and generalised Euler characteristic $\chi^*(W_{w,z}) \geq 0$.

If there are any negative triangle coordinates, we can add vertex linking copies of the boundary tori to the solution until all normal disc coordinates are non-negative. Now, since at most one quad coordinate in each tetrahedron is non-zero, we can in fact realise the normal surface solution class as an embedded normal surface, and so the generalised Euler characteristic is equal to the Euler characteristic. Therefore, an obstruction class to this quad-choice having an associated generalised angle structure is an embedded normal sphere, projective plane, Klein bottle or torus, with the only quads appearing being of the quad types given by the quad-choice. Thus, if the triangulation is 1-efficient, then there can be no such obstruction.

The above argument shows that a 1-efficient triangulation admits an index structure. For the converse, note that if a triangulation is not 1-efficient, then there is an embedded normal sphere, projective plane, Klein bottle or non-vertex linking torus. This must then have at least one non-zero quad coordinate, and since it is embedded, there can be only one non-zero quad coordinate in each tetrahedron. Choosing these quad types in the tetrahedra containing the surface, and arbitrarily choosing quad types in any other tetrahedra, we construct a quad-choice that by the above argument cannot have a suitable generalised angle structure, and so there is no index structure. This completes the proof of Theorem [\[index_structure_iff_1-efficient\]](#index_structure_iff_1-efficient){reference-type="ref" reference="index_structure_iff_1-efficient"}. ◻
::::

::: cor
[]{#atoroidal=>1-efficient label="atoroidal=>1-efficient"} Suppose that $M$ is a compact oriented irreducible 3-manifold with incompressible tori boundary components and no immersed incompressible tori or Klein bottles, except those which are homotopic into the boundary tori. Then $M$ admits an ideal triangulation $\mathcal{T}$ having an index structure. Moreover if $M$ has no essential annuli (i.e $M$ is an-annular) then for any finite sheeted covering space $\widetilde M$, the lifted triangulation also admits an index structure.
:::

::: proof
*Proof.* To construct 1-efficient triangulations, we can use a construction of Lackenby [@Lackenby2]. He proves that if $M$ is a compact oriented irreducible 3-manifold with incompressible tori boundary components and $M$ has no immersed essential annuli, except those homotopic into the boundary tori, then $M$ admits a taut ideal triangulation $\mathcal{T}$. Then by Corollary [\[strongly\]](#strongly){reference-type="ref" reference="strongly"} such triangulations are strongly 1-efficient. Note that the lift of such a triangulation to any finite sheeted covering space is also 1-efficient.\
There is a remaining case of small Seifert fibred spaces. For these are precisely the oriented $3$-manifolds with tori boundary components which admit essential annuli, but no embedded incompressible tori which are not homotopic into the boundary components.

Such examples have base orbifold either a disc with two cone points or an annulus with one cone point or Möbius band with no cone points. The cone points are the images of the exceptional fibres in the Seifert structure. These manifolds have immersed incompressible tori, but do not have embedded incompressible tori or Klein bottles, except in the case where the base orbifold has orbifold Euler characteristic zero: a disc with two cone points corresponding to exceptional fibres of multiplicity two or orbit surface a Möbius band with no cone points. This represents two different Seifert fibrations of the same manifold. We exclude this latter case.

Now to construct a suitable ideal triangulation, note that these Seifert fibred spaces $M$ are bundles over a circle with a punctured surface of negative Euler characteristic as the fibre. To see this, note that $M$ is Seifert fibred over an orientable base orbifold $B$ with $\chi^{orb}(B)<0$. Then $M$ admits a connected horizontal surface $F$ which is orientable with $\chi(F)<0$ since $F$ is an orbifold covering of $B$. (A surface is *horizontal* if it is everywhere transverse to the Seifert fibration.) Since $M$ is orientable it follows that $F$ non-separating, so $M$ fibres over the circle with $F$ as fibre (see, for example, [@Hat sections 1.2 and 2.1].)

After Lemma 6 in [@Lackenby2], it is shown that, starting with any ideal triangulation of the punctured surface $F$, a bundle can be formed as a layered triangulation. This is done by realising a sequence of diagonal flips on the surface triangulation needed to achieve any given monodromy map. Such a triangulation then gives an ideal triangulation with a taut structure. So by Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"} these are 1-efficient triangulations and hence admit index structures. ◻
:::

::: rmk
[]{#small SFS lifted may not have index structure label="small SFS lifted may not have index structure"} The small Seifert fibred spaces from the proof of Corollary [\[atoroidal=\>1-efficient\]](#atoroidal=>1-efficient){reference-type="ref" reference="atoroidal=>1-efficient"} have finite sheeted coverings with embedded incompressible tori so that the lifted triangulations do not all admit index structures, in contrast with the hyperbolic case.
:::

<figure id="trefoil_example" data-latex-placement="htbp">
<p><span class="math inline"><em>L</em><sup>−1</sup></span> at 120 140 <span class="math inline"><em>R</em></span> at 117 268 <span class="math inline">(0, 0)</span> at 44 19 <span class="math inline">(1, 0)</span> at 161 19 <span class="math inline">(1, 1)</span> at 124 88 <span class="math inline">(0, 1)</span> at 9 88 <span class="math inline">(0, 1)</span> at 9 274 <span class="math inline">(0, 0)</span> at 44 208 <span class="math inline">(1, 0)</span> at 161 208 <span class="math inline">(1, 1)</span> at 178 134 <span class="math inline">(0, −1)</span> at 103 325 <span class="math inline">(1, 1)</span> at 103 475 <span class="math inline">(0, 0)</span> at 44 398 <span class="math inline">(1, 0)</span> at 161 398</p>
<img src="draws_eps/trefoil_example" style="width:80.0%" />
<figcaption>A layered triangulation of the complement of the trefoil knot, seen as a punctured torus bundle. On the left, the monodromy is decomposed into generators which act on the punctured torus. The diagrams are shown sheared to highlight the fact that the monodromy has the effect of rotation by <span class="math inline">−<em>π</em>/3</span>. The arrows show where edges of a triangulation of the punctured torus map to under the generators. In the middle, we realise each change in the triangulation by layering on a flat tetrahedron. The arrows are shown on the bottom and top of the stack of two tetrahedra to show the gluing. On the right, we see the edges after the identifications induced by gluing the top to the bottom. There are two tetrahedra and two edges in the triangulation, one of degree two (shown with a dashed line) and the other of degree ten.</figcaption>
</figure>

::: ex
The trefoil knot complement has an ideal layered triangulation with two tetrahedra and two edges, one of degree $2$ and one of degree $10$. See Figure [2](#trefoil_example){reference-type="ref" reference="trefoil_example"}. The complement of the trefoil knot can be seen as a punctured torus bundle with monodromy given by $RL^{-1}$, where $$L=\begin{pmatrix}1&0\\1&1\end{pmatrix} \qquad R=\begin{pmatrix}1&1\\0&1\end{pmatrix}\negthinspace .$$ Following the caption of Figure [2](#trefoil_example){reference-type="ref" reference="trefoil_example"}, we obtain a triangulation of the complement of the trefoil consisting of two tetrahedra. The matrix form of the generalised angle structure equations for this triangulation is $$\begin{pmatrix} 
1&1&0&0&0&0\\
1&1&2&2&2&2\\
1&0&1&0&1&0\\
0&1&0&1&0&1
\end{pmatrix} 
\begin{pmatrix}
Z_1 \\ Z_2 \\ Z'_1 \\ Z'_2\\ Z''_1 \\ Z''_2
\end{pmatrix}
=
\begin{pmatrix}
2\pi \\ 2\pi \\ \pi \\ \pi
\end{pmatrix}  \negthinspace.$$

There is a taut structure given by choosing angles $(\pi, \pi,0,0,0,0)^T$. This assigns the angle $\pi$ to the quad types facing the degree $2$ edge and $0$ to all other angles. This taut structure is compatible with the layering construction. By Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"}, this triangulation is 1--efficient.

It is easy to see that there are no other semi-angle structures for this particular triangulation, because of the degree 2 edge. However, consistent with Theorem [\[index_structure_iff_1-efficient\]](#index_structure_iff_1-efficient){reference-type="ref" reference="index_structure_iff_1-efficient"}, it admits an index structure. To see this, we have to produce a generalised angle structure for each of the $3^2=9$ possible quad-choices. However, by symmetry of the matrix we can reduce this number to three, represented by the following three pairs of conditions that must be satisfied by three generalised angle structures. $$(Z_1 > 0, Z_2>0), \qquad (Z_1 > 0, Z'_2>0),  \qquad (Z'_1 > 0, Z'_2>0)$$ These three representatives are all satisfied by, for example, $(\pi,\pi,x,x,-x,-x)^T$ for any $x>0$.\
Note that there is a well-known 6-fold cyclic covering by the bundle which is a product of a once punctured torus and a circle. This covering is toroidal so we see that there is an index structure on the trefoil knot space but not on this covering space.
:::

<figure id="deg1_deg2_example" data-latex-placement="htb">
<p><span class="math inline"><em>e</em><sub>1</sub></span> at 39 150 <span class="math inline"><em>e</em><sub>2</sub></span> at 255 115 <span class="math inline"><em>a</em></span> at 278 55 <span class="math inline"><em>b</em></span> at 322 160 <span class="math inline"><em>q</em></span> at 240 71</p>
<img src="draws_eps/deg1_deg2_example" style="width:45.0%" />
<figcaption>Part of a triangulation that does not admit an index structure, and part of the corresponding surface. The edge <span class="math inline"><em>e</em><sub>1</sub></span> is degree 1, so the two faces incident to it are identified (indicated by the arrows).</figcaption>
</figure>

::: ex
We give an example of a subset of a triangulation consisting of two tetrahedra identified in a particular way. Namely, we have a tetrahedron $\sigma_1$ with opposite edges $e_1$ of degree 1 and $e_2$ of degree 2, and another tetrahedron $\sigma_2$ which is the second tetrahedron incident to $e_2$. See Figure [3](#deg1_deg2_example){reference-type="ref" reference="deg1_deg2_example"}. If these tetrahedra are part of any ideal triangulation with torus boundary components then that triangulation will not have an index structure, and will have a normal torus that is not vertex-linking, so it is not 1--efficient.

First we show that there is no index structure. Since $e_1$ is degree 1, for any generalised angle structure the angle of $\sigma_1$ at the quad type facing $e_1$ must be $2\pi$. This quad type also faces $e_2$. The angle of the quad type in $\sigma_2$ facing $e_2$ must add to $2\pi$ to give $2\pi$, and so it must be zero. Therefore this angle can never be strictly positive, and so there is no index structure.

Next, we find the corresponding embedded normal torus. It has a single quadrilateral in $\sigma_2$, labelled $q$ in Figure [3](#deg1_deg2_example){reference-type="ref" reference="deg1_deg2_example"}. Two of its triangles are in $\sigma_1$, also shown. When the two identified faces of $\sigma_1$ are glued to each other, the boundary of the shown surface consists of the two arcs labelled $a$ and $b$, on two of the boundary faces of $\sigma_2$. Now consider the vertex--linking normal torus $T$, given by the link of the vertex at which the endpoints of $e_2$ meet. We complete our surface into an embedded normal torus by deleting from $T$ the normal triangles in $\sigma_1$ and $\sigma_2$ at the endpoints of $e_2$, and gluing the resulting boundary arcs to $a$ and $b$. The resulting surface is boundary parallel and so is a torus, but is obviously not vertex--linking since it contains a quadrilateral.
:::
