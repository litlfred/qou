---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-006-7-associated-circle-packings-and-cusp-moduli
section_title: "Associated circle packings and cusp moduli"
section_number: 7
pages: 18-21
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.968
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
[]{#pack label="pack"} In this section we study the circle packing corresponding to the hyperbolic graph $W_n$ shown in Figure [1](#fig.graphW){reference-type="ref" reference="fig.graphW"}.

![Graph $W_n$ with $2n+2$ vertices](graphW2.eps){#fig.graphW}

The two isometric polyhedra in the decomposition of the complement of $W_n$ described in section [\[sec.Vol\]](#sec.Vol){reference-type="ref" reference="sec.Vol"} are obtained by gluing together $n$ regular ideal octahedra (see Figure [2](#fig.graphW2){reference-type="ref" reference="fig.graphW2"} (right)). Therefore the volume of its complement is $2nV_8$ where $V_8= 3.663862 \ldots$ is the volume of the regular ideal octahedron. A circle packing corresponding to the graph is depicted in Figure [2](#fig.graphW2){reference-type="ref" reference="fig.graphW2"} (left). Each tangency point of the circle packing corresponds to an annulus cusp of the complement of $W_n$.

![A circle packing obtained from the graph $W_n$ (left) and a (topological) polyhedral decomposition (right)](graphW3.eps){#fig.graphW2}

Recall from Remark [\[cusp_param\]](#cusp_param){reference-type="ref" reference="cusp_param"} that each torus cusp of a hyperbolic $3$-manifold has a Euclidean structure $\mathbb{C}/\Gamma$ where $\Gamma \cong \mathbb{Z}^2 \subset \mathbb{C}$ is a lattice, and its shape parameter is determined by giving two independent translations corresponding to a choice of basis for $\Gamma$. Since there are infinitely many ways to choose such a basis, this shape parameter is not unique. The *modulus* of a torus cusp is defined as the complex ratio $$\label{eq_mod}
z = (\text{second shortest translation})/(\text{shortest translation}).$$ It is a complex number lying in the region $|$Re$(z)| \leq 1/2$ and $|z|\geq 1$. If $z$ lies on the boundary of this region, we choose it so that Re$(z) \geq 0$.

For the complement of $W_n$, there are three different types of annulus cusps, see Figures [3](#fig.pack1){reference-type="ref" reference="fig.pack1"}, [4](#fig.pack2){reference-type="ref" reference="fig.pack2"} and [5](#fig.pack3){reference-type="ref" reference="fig.pack3"}. The circle packing diagrams giving the cusp shapes are obtained by Möbius transformations which map one of the marked cusps to infinity. Since the graph complement is reconstructed by gluing the two isometric polyhedra along their corresponding white faces, we get the boundary of a horoball neighbourhood of the annulus cusp by gluing two copies of rectangles together along corresponding edges depicted by solid lines. Later, we glue these annuli cusps together along their boundaries (depicted as dotted lines) to get a torus cusp, and compute its modulus.

By using Lemma [\[Vol\]](#Vol){reference-type="ref" reference="Vol"}, we obtain hyperbolic links from $W_n$. The modulus of each cusp can be computed by knowing how to glue the rectangles according to the gluing pattern of thrice punctured spheres.

![Cusp modulus for ideal vertices of type 1](Wpack1.eps){#fig.pack1}

![Cusp modulus for ideal vertices of type 2](Wpack2.eps){#fig.pack2}

![Cusp modulus for ideal vertices of type 3](Wpack3.eps){#fig.pack3}

::: ex
[]{#example label="example"}

*The graph $G_{n,k}$ in Figure [6](#fig.example){reference-type="ref" reference="fig.example"} (top) is obtained from the graph in Figure [1](#fig.graphW){reference-type="ref" reference="fig.graphW"} by $k+2$ applications of Lemma [\[Vol\]](#Vol){reference-type="ref" reference="Vol"}, where $k+2 \le n$. The torus cusp corresponding to the knot component (with $k$ crossings) comes from the $2(k+1)$ marked vertices in Figure [6](#fig.example){reference-type="ref" reference="fig.example"} (bottom). Note that in Figure [6](#fig.example){reference-type="ref" reference="fig.example"} (also in Figure [\[fig.source\]](#fig.source){reference-type="ref" reference="fig.source"}), the choice of crossings below the crossing circles is not important, because changing an over crossing to an under crossing does not change the graph complement.*

![A graph $G_{n,k}$ obtained from $W_n$ (top) and vertices corresponding to the knot component cusp (bottom) ](example.eps){#fig.example}

In Figure [7](#fig.cuspshapes){reference-type="ref" reference="fig.cuspshapes"}, we depict the shapes of the torus cusps. The left diagram shows the shape of a crossing circle cusp without a half twist below, the middle shows the shape of a crossing circle cusp with a half twist, and the right shows the shape of the cusp which comes from the knot component.

![Shapes of the torus cusps for the graph $G_{n,k}$ in Figure [6](#fig.example){reference-type="ref" reference="fig.example"}](cuspshapes.eps){#fig.cuspshapes}

The shape of the torus cusp of the knot component in Figure [6](#fig.example){reference-type="ref" reference="fig.example"} is obtained by arranging $2 \times 2(k+1)$ copies of the $1 \times 2$ rectangle in Figure [4](#fig.pack2){reference-type="ref" reference="fig.pack2"} to form a $2 \times 4(k+1)$ rectangle with opposite edges identified by translations. Therefore, its cusp modulus is $2(k+1)\sqrt{-1}$. The modulus of each crossing circle cusp depends on the existence of a half twist; if it has a half twist below, the modulus is $\sqrt{-1}$ and if not, it is $2\sqrt{-1}$. (Note that these moduli do not depend on the total number of vertices in the graph $G_{n,k}$.)
:::
