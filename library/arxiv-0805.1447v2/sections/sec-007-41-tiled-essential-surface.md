---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-007-41-tiled-essential-surface
section_title: "Tiled essential surface"
section_number: 4.1
pages: 10-12
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.981
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
First we prove statement (1), tiled case. Assume $F$ is tiled. Since $F$ is tiled, every singular point is bb-singularity, and $F$ can be decomposed into bb-tiles. A decomposition into bb-tiles determines cellular-decomposition of $F$, and we call this *tiling*. The notion of vertex and valance we defined in section 3 coincides to usual definition of vertex and valance in this cellular decomposition.

First we estimate a valance of each vertex, using Euler characteristic argument which is standard in braid foliation theory.

::: lem
[]{#lem:eulerform-tiled label="lem:eulerform-tiled"} Let $\beta$ be a braid and $F$ be a tiled essential genus $g$ closed surface in the complement of closed braid $\widehat{\beta}$, and $V(i)$ be a number of vertex whose valance is $i$. then, $$\sum_{v=1}^{3}(4-v)V(v)+8g-8= \sum_{v=4}^{\infty}(v-4)V(v)$$ holds.
:::

::: proof
*Proof.* Let $E,R$ be a number of 1-cell and 2-cell of tiling. Since $F$ has an Euler characteristic $-2g+2$, $(\sum_{i=1}^{\infty}V_{i}) - E + R = -2g+2$. On the other hand, each 1-cell is the boundary of exactly two 2-cells and each 1-cell has two vertices as their boundary ,so $2R=E$ and $(\sum_{i=1}^{\infty}iV_{i}) = 2E$. By combining these equation, we establish the claim. ◻
:::

Since each term of equation in lemma [\[lem:eulerform-tiled\]](#lem:eulerform-tiled){reference-type="ref" reference="lem:eulerform-tiled"} is positive, lemma [\[lem:eulerform-tiled\]](#lem:eulerform-tiled){reference-type="ref" reference="lem:eulerform-tiled"} implies $V(i)$ are bounded except $V(4)$. Next we see that Dehornor floor can be estimated from above by a valance of vertex.

::: lem
[]{#lem:estimate-tiled label="lem:estimate-tiled"} Let $F$ be a tiled essential genus $g$ closed surface in the complement of closed braid $L=\widehat{\beta}$. If $F$ contains a valance $v$ vertex, then $[\beta]_{D} < \frac{v}{2}+1$.
:::

::: proof
*Proof.* Let $p$ be a valance $v$ vertex and $\{H_{\theta_{1}},H_{\theta_{2}},\cdots ,H_{\theta_{v}} |\; \theta_{i}<\theta_{i+1} \}$ be a sequence of singular fibers such that each $H_{\theta_{i}}$ contains singular leaves which pass the vertex $p$. Let $b_{\theta}$ be a b-arc in the fiber $H_{\theta}$ which passes $v$. By taking isotopy near each singular fiber $H_{\theta_{i}}$, we can always assume that for sufficiently small $\varepsilon > 0$, braiding of strands does not occur in the interval $[\theta_{i}-\varepsilon, \theta_{i}+\varepsilon]$ and each fiber $H_{\theta_{i} \pm \varepsilon}$ is pierced by $L$ exactly the same points $\{p_{1},p_{2},\cdots,p_{n}\}$. Notice that this modification can be done without changing $H_{0}\cap \widehat{\beta}$ so this modification does not change braid $\beta$ as a element of braid groups. After this modification, we can always consider sub-braiding in each interval $[\theta_{i} - \varepsilon,\theta_{i}+\varepsilon]$, $[\theta_{i}+\varepsilon, \theta_{i+1}-\varepsilon]$. Since $\varepsilon$ is chosen to sufficiently small, we can assume there exist no other singular points in each interval $[\theta_{i}-\varepsilon, \theta_{i}+\varepsilon]$.

Now we see a sequence of $b_{\theta}$ as a move of b-arc in $D^{2}$. Then we can also assume by taking isotopy of surface and braids, in the interval $[\theta_{i}+\varepsilon, \theta_{i+1}-\varepsilon]$, $b_{\theta}$ do not move when we see $b_{\theta}$ as a move of the arcs.

First we investigate a sub-braiding $\beta_{1}$ in $[\theta_{1}+\varepsilon, \theta_{3}-\varepsilon]$. By taking appropriate conjugacy of $\beta_{1}$, we can assume $F \cap H_{\theta_{1} + \varepsilon}$ consists of several number of vertical arcs as depicted in left of figure [1](#fig:model){reference-type="ref" reference="fig:model"} and bb-singularity in $\theta_{2}$ is modeled as shown in the right of figure [1](#fig:model){reference-type="ref" reference="fig:model"}. We denote this braid by $\beta'_{1}$

Then, by seeing braids as a move of puncture point of disc, we can write this modified braiding $\beta_{1}'$ in $[\theta_{1}+\varepsilon, \theta_{3}-\varepsilon]$ as shown in figure [2](#fig:braiding){reference-type="ref" reference="fig:braiding"}, which contains only one $\sigma_{1},\sigma_{1}^{-1}$. The original braiding $\beta_{1}$ in $[\theta_{1}+\varepsilon, \theta_{3}-\varepsilon]$ is conjugate to the braid $\beta_{1}'$ so proposition [\[prop:newestimation\]](#prop:newestimation){reference-type="ref" reference="prop:newestimation"} shows $[\beta_{1}]_{D} =0$.

<figure id="fig:model">
<div class="center">
<embed src="model.eps" style="width:110mm" />
</div>
<figcaption>Model of intersection and bb-singularity</figcaption>
</figure>

<figure id="fig:braiding">
<div class="center">
<embed src="subbraiding.eps" style="width:80mm" />
</div>
<figcaption>Braiding in <span class="math inline">[<em>θ</em><sub>1</sub>+<em>ε</em>,<em>θ</em><sub>3</sub>−<em>ε</em>]</span>: bb-singularity case</figcaption>
</figure>

Iterating this argument, we conclude that sub-braid $\beta_{i}$ in the interval $[\theta_{2i-1}+\varepsilon, \theta_{2i+1}-\varepsilon]$ for $i=1,\cdots ,\frac{v}{2}$ has zero Dehornoy floor. Since original braid $\beta$ is conjugate to the braid $\beta_{1}\beta_{2}\cdots\beta_{v \slash 2}$, by proposition [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"}, $[\beta]_{D}< \frac{v}{2}$. ◻
:::

Combining above two lemmas, now it is easy to estimate Dehornor floor via information of tiling.

::: proof
*Proof of Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"}(1).* Assume $F$ is tiled. Let $V(i)$ be the number of valance $i$ vertices. If some of $V(i)$ is non-zero for $i \leq 3$, then lemma [\[lem:estimate-tiled\]](#lem:estimate-tiled){reference-type="ref" reference="lem:estimate-tiled"} means $[\beta]_{D}< 2 < g+1$, so conclusion holds. Therefore we can assume $V(i)=0$ for $i \leq 3$, and Euler characteristic formula in lemma [\[lem:eulerform-tiled\]](#lem:eulerform-tiled){reference-type="ref" reference="lem:eulerform-tiled"} become $$8g-8= \sum_{v=4}^{\infty}(v-4)V(v)$$

Since $g$ is not zero, there exist at least two b-arcs in each regular fiber, so at least four vertices in the tiling of $F$. Therefore the minimal valance of vertices is smaller than $max\{ 2g+2,4 \}$, that is, $2g+2$. Then lemma [\[lem:estimate-tiled\]](#lem:estimate-tiled){reference-type="ref" reference="lem:estimate-tiled"} establishes $[\beta]_{D}< g+2$. ◻
:::
