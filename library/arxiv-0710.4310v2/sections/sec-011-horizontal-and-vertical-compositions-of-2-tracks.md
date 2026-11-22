---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-011-horizontal-and-vertical-compositions-of-2-tracks
section_title: "Horizontal and vertical compositions of 2-tracks"
section_number: null
pages: 14-15
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#HVC label="HVC"}

Note that the horizontal composition of 2-paths descends immediately to a horizontal composition in $\S_2(M)$. Suppose that $\G$ and $\G'$ are 2-paths with $\d_u(\G)\cong_1 \d_d(\G')$. Choose a rank-1 homotopy ${J}$ connecting $\d_u(\G)$ and $\d_d(\G')$. Then $[\G]\circ_v[\G']$ is defined as $[(\G \circ_v J) \circ_v \G'].$ The fact that this composition is well defined in $\S_2(M)$ follows immediately from lemma [\[MAIN\]](#MAIN){reference-type="ref" reference="MAIN"} in the appendix.

Therefore both the vertical and horizontal compositions of 2-paths descend to $\S_2(M)$. These compositions are obviously associative, and admit units and inverses. Since the interchange law is trivially verified the following theorem holds:

::: Theorem
Let $M$ be a smooth manifold. The horizontal and vertical compositions in $\S_2(M)$ together with the boundary maps $\d_u,\d_d,\d_l,\d_r\colon \S_2(M) \to \S_1(M)$ define a 2-groupoid $\Sc_2(M)$, whose set of objects is given by all points of $M$, the set of 1-morphisms by the set $\S_1(M)$ of 1-tracks on $M$, and given two 1-tracks $[\g]$ and $[\g']$, the set of 2-morphisms $[\g] \to [\g']$ is given by all 2-tracks $[\G]$ with $\d_d([\G])=[\g]$ and $\d_u([\G])=[\g']$.
:::

The definition of a 2-groupoid can be found in [@HKK]. This construction should be compared with [@HKK; @BHKP], where the thin strict 2-groupoid of a Hausdorff space was defined, using a different notion of thin equivalence (factoring through a graph) - see also [@BH] for the construction of the fundamental double groupoid of a triple of spaces. For analogous non-strict constructions see [@M; @BS; @MP].
