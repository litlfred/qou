---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-008-42-mixed-foliated-surface
section_title: "Mixed foliated surface"
section_number: 4.2
pages: 12-16
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.988
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
Next we proceed to $F$ is mixed foliated case. The strategy is almost the same as tiled case, but we need to do some additional arguments to evaluate valance of vertices because the decomposition by regions do not determine cellular decomposition. First we see the same conclusion of lemma [\[lem:estimate-tiled\]](#lem:estimate-tiled){reference-type="ref" reference="lem:estimate-tiled"} holds.

::: lem
[]{#lem:estimate-mixed label="lem:estimate-mixed"} Let $F$ be a mixed foliated essential genus $g(\neq0)$ closed surface in the complement of closed braid $\widehat{\beta}$. If $\beta$ contains a valance $v$ vertex, then $[\beta]_{D} < \frac{v}{2}+1$.
:::

::: proof
*Proof.* Let $p$ be a valance $v$ vertex. We can use the same arguments appeared in proof of lemma [\[lem:estimate-tiled\]](#lem:estimate-tiled){reference-type="ref" reference="lem:estimate-tiled"}. The main difference is a presence of c-circles and bc-singularity around $p$. First we modify closed braid as in the proof of lemma [\[lem:estimate-tiled\]](#lem:estimate-tiled){reference-type="ref" reference="lem:estimate-tiled"} so that we can consider sub-braiding in each interval $[\theta_{i}-\varepsilon, \theta_{i}+\varepsilon]$, $[\theta_{i}+\varepsilon, \theta_{i+1}-\varepsilon]$. Assume that singular point in the fiber $H_{\theta_{2}}$ is bc-singularity. Then by taking appropriate conjugation of sub-braiding $[\theta_{1}+\varepsilon, \theta_{3}-\varepsilon]$, bc-singularity is now modeled as in the figure [1](#fig:model2){reference-type="ref" reference="fig:model2"}. Then braiding in the interval $[\theta_{1}+\varepsilon, \theta_{3}-\varepsilon]$ can be written as shown in figure [2](#fig:braiding2){reference-type="ref" reference="fig:braiding2"}, which contains only one $\sigma_{1}^{\pm 1}$. Thus, the same argument of the proof of lemma [\[lem:estimate-tiled\]](#lem:estimate-tiled){reference-type="ref" reference="lem:estimate-tiled"} gives desired estimation.

<figure id="fig:model2">
<div class="center">
<embed src="model2.eps" style="width:80mm" />
</div>
<figcaption>Model of bc-singularity</figcaption>
</figure>

<figure id="fig:braiding2">
<div class="center">
<embed src="subbraiding2.eps" style="width:80mm" />
</div>
<figcaption>Braiding in <span class="math inline">[<em>θ</em><sub>1</sub>+<em>ε</em>,<em>θ</em><sub>3</sub>−<em>ε</em>]</span>: bc-singularity case</figcaption>
</figure>

 ◻
:::

Then, we want to estimate the minimal valance of vertices. Since there might be all types of singularity in the foliation of $F$, in general decomposition into regions dose not define usual sense of cellular decomposition: bc-region is annulus, and cc-region is pair of pants. However, in special case of normal mixed foliation, defined below, one can constructs canonical cellular decomposition via decomposition into regions as shown in [@bm2]. First we describe this.

We say mixed foliation is *normal* if there exists no cc-singularity. In normal mixed foliation case, we can construct canonical cellular decomposition as follows. First we see that in normal mixed foliation, bc-annuli always occur in pairs. This is because the c-circle boundary of bc-annuli must be attached to c-circle boundary of another bc-annuli, since there is no cc-regions and boundary of bb-tile are all b-arcs. Now, take annulus $W$ obtained by attaching two bc-annuli along their c-circle boundaries. Each component of $\partial W$ has two vertices. By cutting $W$ along the arc which connects two vertices which lies different components of $\partial W$, as shown in figure [3](#fig:be-tile){reference-type="ref" reference="fig:be-tile"}, we obtain two 2-cells, called *be-tile*. These cutting arcs are called *e-edge*. Now decomposition into be-tile and bb-tile determines cellular decomposition of $F$.

<figure id="fig:be-tile">
<div class="center">
<embed src="betile.eps" style="width:120mm" />
</div>
<figcaption>Construction of be-tile</figcaption>
</figure>

Note that there might exist be-tile which has no singular point or two singular points, but from construction of be-tile, be-tile with zero singularity and be-tile with two singularity must occur in pairs in each neighbor of vertex, so the notion of vertex and valance defined in section 3 coincide with the usual meaning of vertex and valance in this cellular decomposition. Then we see the same Euler characteristic formula holds:

::: lem
[]{#lem:eulerform-nmixed label="lem:eulerform-nmixed"} Let $F$ be a normal mixed foliated surface with genus $g \neq 0$ and $V(v)$ be a number of vertex whose valance is $v$ in cellular decomposition described above. Then,

$$\sum_{v=1}^{3}(4-v)V(v)+8g-8 = \sum_{v=4}^{\infty}(v-4)V(v)$$ holds.
:::

::: proof
*Proof.* A be-tile has exactly four 1-cells in its boundary and each 1-cell is boundary of two 2-cells, so the same argument in proof of lemma [\[lem:eulerform-tiled\]](#lem:eulerform-tiled){reference-type="ref" reference="lem:eulerform-tiled"} gives desired result. ◻
:::

So we can estimate minimal valance of vertices in case of normal mixed foliation by using lemma [\[lem:eulerform-nmixed\]](#lem:eulerform-nmixed){reference-type="ref" reference="lem:eulerform-nmixed"} as in the tiled case. To estimate general mixed foliated case, we perform \"preimage surgery\" to delete cc-singularities. Let $F$ be a mixed foliated surface and we denote $\mathcal{F}$ by the preimage of $F$; that is, $\mathcal{F}$ is a foliated surface forgetting information of embedding.

Let $c$ be an one of the c-circle boundary of cc-pants $P$. $c$ is also a boundary of some other cc-pants or bc-annulus $Q$. We modify foliations of $P$ and $Q$ as shown in figure [4](#fig:preimagesurgery){reference-type="ref" reference="fig:preimagesurgery"} by filling $c$ by discs and changes foliation in $P$ and $Q$, according to type of regions. Since modified regions are trivially foliated, these regions are amalgamated to some other regions and they disappears. Moreover, this operation can be done so that obtained surface is connected by choosing c-circle boundary $c$ appropriately and reduces genus of $\mathcal{F}$ because all c-circle in the foliation is non-null homotopic in $\mathcal{F}$. Thus, this modification deletes two regions $P$ and $Q$, hence two singular points. We call this operation *preimage surgery* because we can regard this modification as surgery of $\mathcal{F}$ along c-circle $c$. We remark that preimage surgery is not realizable as a surgery of embedded surface $F$, because we cannot choose take a disc bounded by $c$ without intersecting original surface $F$ in $S^{3}$.

Since each preimage surgery reduces a genus of $\mathcal{F}$, after $k \leq g$ preimage surgery we obtain normal mixed foliated surface $\mathcal{F}'$. As we remarked before, $\mathcal{F}'$ cannot be realized as an embedded surface, but we can use the arguments of proof of lemma [\[lem:eulerform-nmixed\]](#lem:eulerform-nmixed){reference-type="ref" reference="lem:eulerform-nmixed"}, because the proof uses only information from cellular decomposition of $\mathcal{F}'$. Therefore we can use lemma [\[lem:eulerform-nmixed\]](#lem:eulerform-nmixed){reference-type="ref" reference="lem:eulerform-nmixed"} for $\mathcal{F}'$ to estimate valance of vertices of preimage-surgered surface $\mathcal{F}'$.

<figure id="fig:preimagesurgery">
<div class="center">
<embed src="preimagesurgery.eps" style="width:120mm" />
</div>
<figcaption>Preimage surgery</figcaption>
</figure>

::: proof
*Proof of Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"}(2)(3).* Assume $F$ is mixed foliated and after performing preimage surgery $k$-times described above, we create abstract foliated surface $\mathcal{F}'$ with no cc-singularity, that is, normal mixed foliated. Let $m$ be a minimal valance of vertices of $\mathcal{F}'$. Then, we trace preimage surgery procedure backwards. Each surgery deletes at most one bc-singularity, so original surface $F$ has at most more than $k$ bc-singular points than that of $\mathcal{F}'$. Since singular leaf containing bc-singularity has two vertices as its endpoints and there exist at least two vertices in $F$, we conclude minimal valance of vertices in $F$ is smaller than $m+k$. Thus, we only need to estimate $m$ to estimate minimal valance of vertices in original surface $F$.

Let $V(v)$ be the number of valance $v$ vertices of $\mathcal{F}'$. If $V(i)$ is non-zero for some $1 \leq i \leq 3$, then form the argument above, we conclude the minimal valance of vertices of $F$ is smaller than $3+g$, so $[\beta]_{D} < \frac{3+g}{2} \leq 2g+1$, so we can assume $V(i)$ is zero for all $1 \leq i \leq 3$. In this case, the Euler characteristic formula for $\mathcal{F}'$ become $$8(g-k)-8 > \sum_{i=4}^{\infty}(v-4)V(v).$$ Mixed foliated means there exist at least one b-arc in the foliation, so there exist at least two vertices in $\mathcal{F}'$. Therefore the minimal value of valance of vertices in $\mathcal{F}'$ is less than $4(g-k)$. Therefore, from our earlier argument, minimal valance of vertices in $F$ is smaller than $4(g-k)+k = 4g-3k+1$. Now, lemma [\[lem:estimate-mixed\]](#lem:estimate-mixed){reference-type="ref" reference="lem:estimate-mixed"} establishes an inequality $[\beta]_{D}< 2g-\frac{3k}{2}< 2g+1$.

From statement (1) and (2), we conclude if $[\beta]_{D} \geq 2g+1$, then $F$ is neither tiled nor mixed-foliated, hence circular-foliated. This completes proof of theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} ◻
:::
