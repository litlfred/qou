---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-009-horizontal-and-vertical-compositions-of-2-tracks
section_title: "Horizontal and vertical compositions of 2-tracks"
section_number: null
pages: 14-15
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 1.0
---
[]{#HVC label="HVC"}

Note that the horizontal composition of 2-paths descends immediately to a horizontal composition in $\S_2(M)$. Suppose that $\G$ and $\G'$ are 2-paths with $\d_u(\G)\cong_1 \d_d(\G')$. Choose a rank-1 homotopy ${J}$ connecting $\d_u(\G)$ and $\d_d(\G')$. Then $[\G]\circ_v[\G']$ is defined as $[(\G \circ_v J) \circ_v \G'].$ The fact that this composition is well defined in $\S_2(M)$ follows immediately from lemma [\[MAIN\]](#MAIN){reference-type="ref" reference="MAIN"} in the appendix.

Therefore both the vertical and horizontal compositions of 2-paths descend to $\S_2(M)$. These compositions are obviously associative, and admit units and inverses. Since the interchange law is trivially verified the following theorem holds:

::: Theorem
Let $M$ be a smooth manifold. The horizontal and vertical compositions in $\S_2(M)$ together with the boundary maps $\d_u,\d_d,\d_l,\d_r\colon \S_2(M) \to \S_1(M)$ define a 2-groupoid $\Sc_2(M)$, whose set of objects is given by all points of $M$, the set of 1-morphisms by the set $\S_1(M)$ of 1-tracks on $M$, and given two 1-tracks $[\g]$ and $[\g']$, the set of 2-morphisms $[\g] \to [\g']$ is given by all 2-tracks $[\G]$ with $\d_d([\G])=[\g]$ and $\d_u([\G])=[\g']$.
:::

The definition of a 2-groupoid can be found in [@HKK]. This construction should be compared with [@HKK; @BHKP], where the thin strict 2-groupoid of a Hausdorff space was defined, using a different notion of thin equivalence (factoring through a graph) - see also [@BH] for the construction of the fundamental double groupoid of a triple of spaces. For analogous non-strict constructions see [@M; @BS; @MP].

### Definition of the thin fundamental categorical group of a smooth manifold {#TCM}

Since $\Sc_2(M)$ is a 2-category, given a base point $*$ of $M$ (in other words an object of $\Sc_2(M)$) we can define a monoidal category $\Pc_2(M,*)$. The objects of $\Pc_2(M,*)$ are given by all 1-tracks of $M$ starting and ending at $*$, and therefore by all elements of $\pi_1^1(M,*)$. On the other hand, the set $\P_2(M,*)$ of morphisms of $\Pc_2(M,*)$ is given by the set of all 2-tracks $[\G] \in \S_2(M)$ such that $\d_l([\G])=\d_r([\G])=*$. Therefore, given $[\g],[\g'] \in \pi_1^1(M,*)$, the set of morphisms $[\g] \to [\g']$ is given by all 2-tracks $[\G]$ connecting $[\g]$ and $[\g']$, in other words with $\d_{{d}}([\G])=[\g]$ and $\d_{{u}}([\G])=[\g']$. The composition in $\P_2(M,*)$ is given by the vertical composition in $\S_2(M)$. On the other hand the horizontal composition of 2-tracks will give the tensor product in $\Pc_2(M,*)$.

Given that $\Sc_2(M)$ is a 2-groupoid, the monoidal category $\Pc_2(M,*)$ is a categorical group. We therefore call $\Pc_2(M,*)$ the *thin fundamental categorical group of $M$.*
