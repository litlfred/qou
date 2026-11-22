---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.964
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
In this paper we study an application of left-invariant total ordering of braid group $B_{n}$ to knot theory. An left-invariant total ordering, called Dehornoy ordering is an interesting structure of braid groups found in 1990's by Dehornoy ([@d]). Today the ordering is interpreted in both algebraic and geometric way and these interpretation shows the Dehornoy ordering is a quite natural structure of braid groups.

Braid groups are very important tool for studying links. Many link invariants such as Jones polynomial are first constructed via closed braid representative of links, so it is natural to study an application of this interesting structure of braid groups to knot theory. In [@mn],[@ma] it is found that braid ordering can be seen as some kinds of restriction for admissibility of braid moves. Braid moves are moves of closed braids which do not change their representing link types. Most typical (and important) example of braid moves are *exchange move* or *destabilization, stabilization*, which is shown in figure [1](#braidmove){reference-type="ref" reference="braidmove"}. These works suggest that there would be some relationships between Birman-Menasco's braid foliation theory and ordering of braid groups because braid moves appears naturally in braid foliation theory ([@bf]). For example, exchange move is used to make braid foliation simple and it is one of the most fundamental operation in Birman-Menasco's braid foliation theory. Indeed, we investigate relationship between braid foliation and left invariant total ordering of braid groups, and obtain following result:

<figure id="braidmove">
<div class="center">
<embed src="braidmove.eps" style="width:120mm" />
</div>
<figcaption>exchange move, stabilization and destabilization</figcaption>
</figure>

::: thm
[]{#thm:main1 label="thm:main1"} Let $\beta \in B_{n}$ be a braid and $F$ be an essential, genus $g$ closed surface in the complement of closed braid $\widehat{\beta}$.

1.  If $F$ is tiled, then $[\beta]_{D} < g+2$.

2.  If $F$ is mixed-foliated, $[\beta]_{D} < 2g+1$.

3.  If $[\beta]_{D} \geq 2g+1$, then $F$ is circular foliated.
:::

In above statements, $[\;]_{D}$ represents *Dehornoy floor* of $\beta$, which is a non-negative integer defined in section 2. This integer is determined by the Dehornoy ordering of braid groups, and efficiently computable. The notion of tiled, mixed foliated or circular foliated are derived from Birman-Menasco's braid foliation theory, which will be explained in section 3. Proof of Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} will be given in section 4.

Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} means braid ordering gives some information about the geometry of closed braid complements, and especially if Dehornoy floor is relatively large with respect to its genus, then the surface can be positioned to special position, which is simple .

We remark that Dehornoy floor might vary under even conjugation, stabilization or destabilization, so it is far from knot invariant. Indeed, Dehornoy floor of braids obtained by performing stabilization always vanish. Nevertheless theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} seems to suggests that braid ordering provide some important information about its closure which can not be obtained from known invariants of links.

As an application of theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} we obtain a sufficient condition for Nielsen-Thurston classification determines the geometry of its closure's complement. Nielsen-Thurston theorem states braids are classified into three types by their dynamics; *periodic, reducible* and *pseudo-Anosov*. On the other hand, a famous Thurston's hyperbolization theorem shows knots are classified into following three types by the geometry of their complements; *Torus knots, Satellite knots,* and *Hyperbolic knots*. Although there are many similarities between these two classifications, in general there are no one-to-one correspondence of them. In figure [2](#fig:example){reference-type="ref" reference="fig:example"}, we give an example of periodic, reducible and pseudo-Anosov braids whose closure represents $(2,3)$-Torus knot. Therefore the following question naturally arises:

*When the Nielsen-Thurston classification of braids completely determine the geometrical types of its closure?*

Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} partially answers the question.

<figure id="fig:example">
<div class="center">
<embed src="example.eps" style="width:60mm" />
</div>
<figcaption>Examples of periodic (a), pseudo-Anosov (b), reducible (c) braids all of whose closure are <span class="math inline">(2,3)</span>-Torus knots</figcaption>
</figure>

::: thm
[]{#thm:main2 label="thm:main2"} Let $\beta \in B_{n}$ be a braid whose closure is a knot. If $[\beta]_{D} \geq 3$, following holds:

1.  $\beta$ is periodic if and only if $\widehat{\beta}$ is a torus knot.

2.  $\beta$ is reducible if and only if $\widehat{\beta}$ is a satellite knot.

3.  $\beta$ is pseudo-Anosov if and only if $\widehat{\beta}$ is a hyperbolic knot.

Especially, under this assumption, Satellite knots are all braided-satellite.
:::

We recall that satellite knot $K$ is called braided satellite if $K$ admit closed braid representatives whose axis does not intersect some essential tori in the complement of $K$. This theorem implies, under the condition $[\beta]_{D} \geq 3$, the Nielsen-Thurston classification of braid groups and the geometric classification of their closures are in one-to-one correspondence. In [@l], Los studied the relationship between these two classifications in the case knots are represented by closed braid with minimum braid index. Main result of [@l] shows under the condition of braid index, two classifications are related each other by performing exchange move. However, in general to determine braid index of given knots or links are very difficult question and to see whether or not given braids admit exchange move is also difficult, so the relationships between two classifications cannot be seen directly. In this regard, theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} gives more general and direct condition for the question. We will give a proof of theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} in section 5, and in this section we also give concrete method to create hyperbolic knots via Nielsen-Thurston theory.

::: ack
The author would like to thank his adviser Toshitake Kohno for many helpful suggestions and advices for preparing this manuscript. He also would like to thank Eiko Kin for useful conversations.
:::
