---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-014-two-exact-sequences
section_title: "Two exact sequences"
section_number: null
pages: 16-17
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.99
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#2es label="2es"} This subsection is not necessary to understand the rest of the article.

::: Definition
Let $M$ be a smooth manifold. Let $* \in M$. The group $\pi_2^2(M,*)$ is given by all 2-paths $\G \in S_2(M)$ such that $\G(\d([0,1]^2))=\{*\}$, up to the equivalence relation given by $\G \cong \G'$ if there exists a rank-2 homotopy ${J\colon [0,1]^2\times [0,1] \to M}$, connecting $\G$ and $\G'$, such that, in addition, $J\left ((\d ([0,1]^2) \times I\right)=\{*\}$. The group law is taken to be the horizontal composition.
:::

For more details see [@MP].

::: Theorem
Let $M$ be a smooth manifold with a base point $*$. The crossed module $\Pi_2^{2,1}(M,*)$ can be embedded into the exact sequence: $$\{0\} \to \pi_2^2(M,*) \ra{i} \pi_2^{2,1}(M,*) \ra{\d} \pi_1^1(M,*) \ra{p} \pi_1(M,*)\to \{1\}.$$
:::

::: Proof
The only non-trivial part is the proof that the natural map $i\colon \pi_2^2(M,*)  \to \pi_2^{2,1}(M,*)$ is injective. This follows from Lemma [\[MAIN\]](#MAIN){reference-type="ref" reference="MAIN"}.
:::

::: Definition
The thin $k$-invariant of $M$ is defined as being the cohomology class $k_t(M,*) \in H^3\left (\pi_1(M,*),\pi_2^2(M,*)\right)$ determined by the exact sequence above. See [@EML; @Br] for the construction of these group cohomology classes.
:::

We can define a 2-category $\Qc_2(M)$, with objects given by the points of $M$ and morphisms given by the arrows of the groupoid $\S_1(M)$. The set of 2-morphisms $\Q_2(M)$ of $\Qc_2(M)$ is given by the set of $2$-paths of $M$ up to homotopy. Here the notion of homotopic 2-paths is defined in the same way as the notion of rank-2 homotopic 2-paths (Definition [\[thin2\]](#thin2){reference-type="ref" reference="thin2"}), but omitting the final condition on the rank of the derivative of the map defining the homotopy; see the remarks after definition [\[K\]](#K){reference-type="ref" reference="K"}. If $\G$ and $\G'$ are 2-paths, we write $\G \cong_\infty \G'$ to denote that they are homotopic. Applying the construction that defined the crossed module $\Pi_2^{2,1}(M,*)$ to $\Qc_2(M,*)$ yields a crossed module $$\Pi_2^{\infty,1}(M,*)=\left ( \pi_2^{\infty,1}(M,*) \ra {\d} \pi_1^1(M,*), \tr \right).$$ Here the group $\pi_2^{\infty,1}(M,*)$ is given by $$\pi_2^{\infty,1}(M,*)=\left \{[\G] \in \Qc_2(M,*) \colon \d_d({[\G]})=[*]\right \}$$ with the product law being the horizontal composition. Therefore the map $\d \doteq \d_u \colon {\pi_2^{\infty,1}(M,*)}\to \pi_1^1(M,*)$ is a group morphism.

As before we have:

::: Theorem
The crossed module $\Pi_2^{\infty,1}(M,*)$ can be embedded into the exact sequence: $$\{0\} \to \pi_2(M,*) \ra{i} \pi_2^{\infty,1}(M,*) \ra{\d} \pi_1^1(M,*) \ra{p} \pi_1(M,*)\to \{1\}.$$
:::

It is easy to show that the cohomology class $k(M,*) \in  H^3\left (\pi_1(M,*),\pi_2(M,*)\right)$ given by this exact sequence coincides with the $k$-invariant of $M$. This follows from the explicit construction of it in [@EML], and also from the no-free-lunch principle.
