---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-004-5-extending-cocycles-on-triangulations
section_title: "Extending cocycles on triangulations"
section_number: 5
pages: 12-14
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
text_source: latex
latex_prose_ratio: 0.878
latex_coverage_ratio: 1.0
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
[]{#sec:extendCocycles label="sec:extendCocycles"}

Let $\mathcal{T}$ be a triangulation with an assignment of edge parameters $\nu_e<-1$ such that each $G_\Delta$ is realized (i.e., fulfills the conditions of Lemma [\[lemma:singleGeomSimp\]](#lemma:singleGeomSimp){reference-type="ref" reference="lemma:singleGeomSimp"}). Let $E^\sim \cup E^==E(\mathcal{T})$ be a partition of the edges into two disjoint sets where $|E^\sim| = 3o$ with $o=|V(\mathcal{T})|$ being the number of vertices of $\mathcal{T}$. Assume that we know that $\Theta_e=2\pi$ for every edge $e\in E^=$, but we only know that $\Theta_e$ is close to $2\pi$ for $e\in E^\sim$. Thus, the $\mathrm{PGL}_{2}(\mathbb C)$-cocycle in Theorem [\[thm:cocycleExtendingToTrig\]](#thm:cocycleExtendingToTrig){reference-type="ref" reference="thm:cocycleExtendingToTrig"} might only extend to $\hat\mathcal{T}^==\hat\mathcal{T}\setminus \mathrm{Prisms}(E^\sim)$, the complex where the prisms (including the top and bottom face) about the edges in $E^\sim$ have been removed. The goal of this section is to give a criterion that forces $\Theta_e=2\pi$ for all $e\in E(\mathcal{T})$, so that the conclusions of Theorem [\[thm:cocycleExtendingToTrig\]](#thm:cocycleExtendingToTrig){reference-type="ref" reference="thm:cocycleExtendingToTrig"} apply and the edge parameters $\nu_e$ yield a hyperbolic structure for $\mathcal{T}$.

Let $V(\mathcal{T})=\{v_1,\dots,v_o\}$ be the vertices of $\mathcal{T}$. If we drop all all $\alpha$-edges and all $2$- and $3$-cells adjacent to any $\alpha$-edge from $\hat\mathcal{T}$, the remaining complex has a connected component for each vertex $v_k$. We call such a connected component the "vertex link" of $v_k$ and denote it by $L_k$. Starting with $\hat\mathcal{T}^=$ instead of $\hat\mathcal{T}$, we similarly obtain a subcomplex $L^=_k\subset L_k$ for each $v_k$. Note that $(L_k,L^=_k)$ is a punctured topological polyhedron as in Definition [\[def:puncTopPolyhed\]](#def:puncTopPolyhed){reference-type="ref" reference="def:puncTopPolyhed"} and the $\mathrm{SO}_{3}$-cocycle on $\hat\mathcal{T}^=$ descends to a $(\mathrm{SO}_{3},\mathrm{SO}_{2})$-cocycle on each $L^=_k$ formed by the $\beta$- and $\gamma$-edges. Let us fix a gimbal loop $\Gamma_k$ for each $(L_k,L^=_k)$, giving us gimbal functions $g_1,\dots, g_o$ as in Definition [\[def:defGimbalFunction\]](#def:defGimbalFunction){reference-type="ref" reference="def:defGimbalFunction"}.

<figure id="fig:gimbalLoopsInTriangulation">
<div class="center">

</div>
<figcaption>Gimbal loops for two “vertex links” (only some part of each is shown). The thick line is the edge in the triangulation.</figcaption>
</figure>

Let us label the edges in $E^\sim = \{e^\sim_1,\dots,e^\sim_{3o}\}$ and $E^==\{e^=_1,\dots, e^=_{m-3o}\}$. We again want to construct a gimbal function, but this time in one variable $T_j$ per edge $e^\sim_j\in E^\sim$ instead of a variable $d_{k,l}$ per removed polygon as in Section [\[sec:vertexCocycles\]](#sec:vertexCocycles){reference-type="ref" reference="sec:vertexCocycles"}. Note that each edge $e^\sim_j\in E^\sim$ corresponds to two polygons $P_{k,l}$ and $P_{k',l'}$ that have been removed (from the "vertex links" $L_k$ and $L_{k'}$ in $\hat\mathcal{T}$) to obtain $L^=_k$ and $L^=_{k'}$ (with $k$ and $k'$ not necessarily distinct), see Figure [1](#fig:gimbalLoopsInTriangulation){reference-type="ref" reference="fig:gimbalLoopsInTriangulation"}. We obtain a gimbal function in $(T_1,\dots, T_{3o})$ for each vertex by setting $d_{k,l}=d_{k',l'}=T_j$ in Definition [\[def:defGimbalFunction\]](#def:defGimbalFunction){reference-type="ref" reference="def:defGimbalFunction"}. We combine these gimbal functions into a single one:

::: definition
[]{#def:trigGimbalFunction label="def:trigGimbalFunction"} Let $\mathcal{T}$ be a triangulation with an assignment of edge parameters $\nu_e<-1$ such that each $G_\Delta$ fulfills the conditions of Lemma [\[lemma:singleGeomSimp\]](#lemma:singleGeomSimp){reference-type="ref" reference="lemma:singleGeomSimp"}. Let $E^\sim = \{e^\sim_1,\dots,e^\sim_{3o}\}$ and $E^==\{e^=_{1},\dots, e^=_{m-3o}\}$ be a partition of $E(\mathcal{T})$ and fix gimbal loops $\Gamma_1,\dots,\Gamma_o$. The gimbal function is given by $$g: \mathbb R^{3o} \to \mathbb R^{3 o}, \quad (T_1,\dots, T_{3o}) \mapsto \left(g_1(d_{1,1}, \dots, d_{1, p_1}), \dots, g_o(d_{o,1}, \dots, d_{o,p_o})\right).$$ A box $K\subset \mathbb R^q$ avoids gimbal lock if $[Dg(K)]$ is invertible.
:::

Note that the orientation on $(L_k,L^=_k)$ in the above definitions must be chosen such that the boundary of a small hexagon in $(L_k,L^=_k)$ contains a $\gamma^{\sigma(0)\sigma(1)\sigma(2)}$ for $\sigma\in \mathbf{A}_4$.

::: example
Figure [1](#fig:gimbalLoopsInTriangulation){reference-type="ref" reference="fig:gimbalLoopsInTriangulation"} shows examples of gimbal loops for two "vertex links" of $\hat{\mathcal{T}}^=$. The corresponding gimbal matrices would be given by $$\cdots \gamma^{031}_{\Delta_i} \cdot
 \beta^{013}_{\Delta_i} \cdot 
 R_{T_j} \cdot
  \gamma^{012}_{\Delta_i} \cdot
   \beta^{021}_{\Delta_i}
     \cdots
      \quad\mbox{and}\quad
       \cdots
          \gamma^{103}_{\Delta_i}
          \cdot
           \gamma^{310}_{\Delta_{i'}}
           \cdot
            R_{T_j} \cdot \beta^{301}_{\Delta_{i'}}
            \cdot
             \gamma^{302}_{\Delta_{i'}}\cdots .$$ The gimbal function $g$ for the triangulation is obtained by taking the upper triangular entries of the gimbal matrix for each vertex.
:::

::: theorem
[]{#thm:mainThm label="thm:mainThm"} Let $\mathcal{T}\!{}$, $\nu_e$, $E^\sim$ and $E^=$, $\Gamma_1, \dots, \Gamma_o$ and $g$ be as in Definition [\[def:trigGimbalFunction\]](#def:trigGimbalFunction){reference-type="ref" reference="def:trigGimbalFunction"}. Let $K\subset \mathbb R^{3o}$ be a box avoiding gimbal lock such that $(2\pi, \dots, 2\pi)\in K$. If

1.  $(\Theta_{e^\sim_1},\dots,\Theta_{e^\sim_{3o}})\in K$ and

2.  $\Theta_{e^=_1}=\dots=\Theta_{e^=_{m-3o}}=2\pi$

then $\Theta_e=2\pi$ for all $e\in E(\mathcal{T})$, so the edge parameters $\nu_e$ yield a hyperbolic structure on $\mathcal{T}$.
:::

::: proof
*Proof.* By applying Lemma [\[lemma:gimbalMatrixId\]](#lemma:gimbalMatrixId){reference-type="ref" reference="lemma:gimbalMatrixId"} to each vertex $v_1,\dots, v_o$, we see that $$g(2\pi,\dots,2\pi)=g(0,\dots,0)=(0,\dots,0).$$ Hence, the proof from Lemma [\[lemma:noGimbalImpliesAllEqnsVertexLink\]](#lemma:noGimbalImpliesAllEqnsVertexLink){reference-type="ref" reference="lemma:noGimbalImpliesAllEqnsVertexLink"} applies here as well and we have $\Theta_{e^\sim_1}=\dots=\Theta_{e^\sim_{3o}}=2\pi$. Therefore, all conditions of Theorem [\[thm:cocycleExtendingToTrig\]](#thm:cocycleExtendingToTrig){reference-type="ref" reference="thm:cocycleExtendingToTrig"} are fulfilled. ◻
:::
