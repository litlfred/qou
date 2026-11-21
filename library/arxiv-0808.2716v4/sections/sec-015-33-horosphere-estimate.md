---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-015-33-horosphere-estimate
section_title: "Horosphere estimate"
section_number: 3.3
pages: 17-20
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.979
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
[]{#subsec:large-horosphere label="subsec:large-horosphere"}

We can now show that each zigzag contains a large horosphere.

::: prop
[]{#prop:horosize label="prop:horosize"} Let $M$ be a Farey manifold. If $M$ is a $4$--punctured sphere bundle or two--bridge link complement, denote its meridian length by $\mu$; if $M$ is a punctured torus bundle, denote its meridian length by $2\mu$. (See Definition [\[def:fibered-meridian\]](#def:fibered-meridian){reference-type="ref" reference="def:fibered-meridian"}.) Then every zigzag in $M$ contains a horosphere of diameter at least $\mu^2/7$.
:::

::: proof
*Proof.* Let $S$ be a zigzag in $M$. As at the beginning of §[\[subsec:param\]](#subsec:param){reference-type="ref" reference="subsec:param"}, let $a$ denote the radius of the largest face of the Ford domain of $S$. Call this face $F_a$. Rescale such that the distance between the center of $F_a$ and the center of the face directly to its right is $1$. Call the face to its right $F_b$, and let $b$ denote the radius of the face $F_b$. The third face, which we will call $F_{ab}$, will then have radius $ab$, and have center distance $b^2$ from $F_b$, and distance $a^2$ from $F_a$, by Lemma [\[lemma:ford-circles\]](#lemma:ford-circles){reference-type="ref" reference="lemma:ford-circles"}. Then the length $\mu$ is equal to $d/h$, where $d$ is the minimal distance between centers of faces $F_a$ and $h$ is the height of the maximal cusp in $M$.

By Lemma [\[lemma:triangle-ineq\]](#lemma:triangle-ineq){reference-type="ref" reference="lemma:triangle-ineq"}, $a$, $b$, and $1$ satisfy the triangle inequality. Additionally, because $F_a$ was chosen to have radius larger than that of $F_b$ and $F_{ab}$, we have the following inequalities.

1.  $a\geq b$, and $a\geq ab$, hence $1\geq b$.

2.  $b>-a+1$ and $b>a-1$.

This forces values of $a$ and $b$ to lie within the region shown in Figure [1](#fig:abregion){reference-type="ref" reference="fig:abregion"}.

![The region of allowable values for $a$ and $b$ in Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"}.](figures/abregion2.eps){#fig:abregion}

Label the angles of the zigzag as follows. Let $\theta$ denote the acute angle between the edges of the zigzag of length $a^2$ and $b^2$. Let $\eta$ denote the acute angle between edges of the zigzag of length $1$ and $b^2$. Note this means that the angle between edges of length $1$ and $a^2$ is $\pi-\theta+\eta$.

By considering orthogonal projections to the edge of length $b^2$, we find that $$d^2 = 1+a^4 + b^4 - 2a^2b^2\cos\theta - 2b^2\cos\eta
-2a^2\cos(\pi-\theta+\eta).
\label{eqn:d}$$ See Figure [2](#fig:zigzag){reference-type="ref" reference="fig:zigzag"} for an example. Note in Figure [2](#fig:zigzag){reference-type="ref" reference="fig:zigzag"}, the angles $\theta$ and $\eta$ correspond to angles of tetrahedra in the canonical decomposition. Because we chose $F_a$ to be the largest face, this will not necessarily be the case, but two of the three angles $\theta$, $\eta$, $\pi-\theta+\eta$ will be canonical (or, if $2\pi-(\pi-\theta+\eta)$ happens to be acute rather than $\pi-\theta+\eta$, then exactly two of the three angles $\theta$, $\eta$, and $2\pi-(\pi-\theta+\eta)$ will be canonical).

<figure id="fig:zigzag">

<figcaption>A zigzag. Here the dotted circles correspond to faces of the Ford domain. Recall the corners of the zigzag are geometric duals of these faces. Reading left to right following the zigzag, the faces of the Ford domain have radius <span class="math inline"><em>a</em></span>, <span class="math inline"><em>b</em></span>, <span class="math inline"><em>a</em><em>b</em></span>, <span class="math inline"><em>a</em></span>, <span class="math inline"><em>b</em></span>, <span class="math inline"><em>a</em><em>b</em></span>, and <span class="math inline"><em>a</em></span>. Here <span class="math inline"><em>η</em></span> and <span class="math inline"><em>θ</em></span> are angles of canonical tetrahedra. The angle <span class="math inline"><em>π</em> − <em>θ</em> + <em>η</em></span> is not an angle of a canonical tetrahedron.</figcaption>
</figure>

By Lemma [\[lemma:horo-sizes\]](#lemma:horo-sizes){reference-type="ref" reference="lemma:horo-sizes"}, and because we chose the face $F_a$ to be largest, the largest horosphere in the zigzag $S$ has diameter $a^2/h^2$.

Write: $$\frac{a^2}{h^2} = \frac{a^2\mu^2}{d^2} =
    \mu^2 \, \frac{a^2}{d^2}.$$

We minimize the quantity $a^2/d^2$.

Note that if $\theta$ is an angle of a tetrahedron in the canonical polyhedral decomposition of $M$, then by Lemma [\[lemma:cos-bound\]](#lemma:cos-bound){reference-type="ref" reference="lemma:cos-bound"}, $\cos\theta$ satisfies: $$\cos\theta > \frac{1+a^4+b^4 - 2a^2-2b^2}{2a^2b^2}.$$

Similarly, Lemma [\[lemma:cos-bound\]](#lemma:cos-bound){reference-type="ref" reference="lemma:cos-bound"} implies that if $\eta$ is an angle of a tetrahedron in the canonical polyhedral decomposition of $M$, then $\cos\eta$ satisfies: $$\cos\eta > \frac{1+a^4+b^4 - 2a^2b^2-2a^2}{2b^2},$$

and if $\pi-\theta+\eta$ (or $2\pi-(\pi-\theta+\eta)$) is an angle of a tetrahedron in the canonical polyhedral decomposition, then $\cos(\pi-\theta+\eta)$ satisfies: $$\cos(\pi-\theta+\eta) > \frac{1+a^4+b^4 -2a^2b^2-2b^2}{2a^2}.$$

Two of the three will be canonical. The third will not, since all three angles cannot be canonical at the same time. However, we know the cosine in that case will be at least $-1$. Hence combining the cosine inequalities above with the formula for $d^2$ of ([\[eqn:d\]](#eqn:d){reference-type="ref" reference="eqn:d"}), we will have one of the three inequalities:

1.  If $\theta$ and $\eta$ are canonical: $$\frac{a^2}{d^2} >
            \frac{a^2}{6a^2+2a^2b^2+2b^2-1-a^4-b^4} =: f_1(a,b).$$

2.  If $\theta$ and $\pi-\theta+\eta$ are canonical: $$\frac{a^2}{d^2} >
            \frac{a^2}{6b^2 + 2a^2b^2 + 2a^2 -1-a^4-b^4}=:f_2(a,b).$$

3.  If $\eta$ and $\pi-\theta+\eta$ are canonical: $$\frac{a^2}{d^2} >
            \frac{a^2}{6a^2b^2+2b^2+2a^2 -1-a^4-b^4} =:f_3(a,b).$$

To complete the proof, we minimize all three of these functions in the region of Figure [1](#fig:abregion){reference-type="ref" reference="fig:abregion"}. This is a calculus problem.

For each $f_j(a,b)$, $j=1, 2, 3$, we find the only critical point of $f_j$ in the region of Figure [1](#fig:abregion){reference-type="ref" reference="fig:abregion"} is the point $a=1,
b=0$. For all positive $a$, the function $f_j$ is decreasing on the line $b=a$, increasing on the line $b=1$, increasing or constant on $b=-a+1$, and decreasing or constant on $b=a-1$. This implies that $f_j$ takes its minimum value in the region at the point $a=1, b=1$.

At this value, $f_j(1,1) = 1/7$. Hence $a^2/h^2 \geq \mu^2/7$. ◻
:::

::: remark
The proof of Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"} does not require the zigzag $S$ to be embedded. In other words, the proposition applies even to the terminal pleated surfaces $S_1$ and $S_c$ that are folded in the construction of a 2--bridge link. When $S$ is a folded surface $S_1$ or $S_c$, one of the angles $\theta$, $\eta$, or $(\pi - \theta
+ \eta)$ is actually $0$, hence its cosine is even larger than claimed, which only improves the estimate.
:::

Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"} should be compared to previous work of Jørgensen [@jorgensen Lemma 4.3], which was carefully written down by Akiyoshi, Sakuma, Wada, and Yamashita [@aswy-book Lemma 8.1.1]. After adjusting for slightly different choices of normalization, Jørgensen's Lemma 4.3 can be summarized as saying that, whenever a zizag of a quasifuchsian punctured torus group is dual to six faces of the Ford domain, one of those faces has radius at least $$\mu/(4+2\sqrt{5}).$$

It follows from Minksy's classification of punctured torus groups [@minsky], that given a punctured torus bundle $M$, the Kleinian subgroup of $\pi_1(M)$ that corresponds to the fiber can be obtained as a geometric limit of quasifuchsian groups. As a result, Jørgensen's estimate extends to punctured torus bundles. Because a Ford domain face of radius $r$ corresponds to a horosphere of diameter $r^2$, Jørgensen's Lemma 4.3 implies that every zigzag in a punctured torus bundle contains a horosphere of diameter at least $$\frac{\mu^2}{(4+2\sqrt{5})^2} \: \approx \: \frac{\mu^2}{71.777}.$$ Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"}, which is proved by a direct geometric argument without reference to quasifuchsian groups, improves this estimate by a factor of about $10.25$.

This improvement becomes highly significant in Section [\[sec:cusp-area\]](#sec:cusp-area){reference-type="ref" reference="sec:cusp-area"}. In Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"}, we estimate the area of a maximal cusp by packing the horospherical torus with disjoint disks that are shadows of large horospheres. As a result, a 10--fold increase in the estimate for the diameter of a horosphere turns into a 100--fold increase in the estimate for the area of its shadow. Since our applications in Sections [\[sec:volume3braids\]](#sec:volume3braids){reference-type="ref" reference="sec:volume3braids"} and [\[sec:jones3braids\]](#sec:jones3braids){reference-type="ref" reference="sec:jones3braids"} rely on these explicit estimates for cusp area, the 100--fold improvement becomes particularly important for applications.
