---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-015-53-relation-with-the-blob-complex
section_title: "Relation with the Blob complex"
section_number: 5.3
pages: 47-49
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.962
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
[]{#S:blob label="S:blob"}

It is asserted in [@MW Example 6.2.10] that the **Blob complex** of Morrison-Walker is equivalent to *an unoriented variant of* topological chiral homology. We briefly explain here how to deduce this equivalence from the proof of Theorem [\[T:TCH=CH\]](#T:TCH=CH){reference-type="ref" reference="T:TCH=CH"} and several statements from [@MW]. The main difference with § [\[S:ReviewTCH\]](#S:ReviewTCH){reference-type="ref" reference="S:ReviewTCH"} and § [\[S:locality\]](#S:locality){reference-type="ref" reference="S:locality"} to keep in mind is that we no longer assume our manifold to be *framed*. Indeed, we are using the variant of topological chiral homology for (non-necessarily framed nor oriented) manifolds of dimension $n$. However this forces us to restrict our attention to *unoriented $E_n$-algebras*:

::: definition
[]{#D:unorientedEn label="D:unorientedEn"} The category of *unoriented $E_n$-algebras*, denoted $\mathbb{E}_n^{O(n)}\textit{-}Alg_\infty$ is defined as the ($(\infty,1)$-)category of symmetric monoidal functors $$\mathbb{E}_n^{O(n)}\textit{-}Alg_\infty := \text{\emph{Fun}}^\otimes(\text{\emph{Disk}}_n,\,k\textit{-}Mod_\infty)$$ where $\text{\emph{Disk}}_n$ is the category with objects the integers and morphism the spaces $\text{\emph{Disk}}_n(k,\ell):= \text{\emph{Emb}}(\coprod_{k} \mathbb R^n, \coprod_{\ell} \mathbb R^n)$ of smooth embeddings of $k$ disjoint copies of a disk $\mathbb R^n$ into $\ell$ such copies; the monoidal structure is induced by disjoint union of copies of disks.
:::

Note that $\mathbb{E}_n^{O(n)}$-algebras are denoted $\mathcal{EB}_n$-algebras in [@MW].

::: remark
The definition above is extracted from [@L-VI; @Francis]. There is an natural action of the orthogonal group $O(n)$ on $E_n\textit{-}Alg_\infty$, see [@L-TFT]; the category $(E_n\textit{-}Alg_\infty)^{hO(n)}$ of $O(n)$-homotopy fixed points is equivalent to the $(\infty,1)$-category $\mathbb{E}_n^{O(n)}\textit{-}Alg_\infty$ of Definition [\[D:unorientedEn\]](#D:unorientedEn){reference-type="ref" reference="D:unorientedEn"} In particular, *any CDGA is an unoriented $E_n$-algebra*.

If one replaces the action of $O(n)$ by $SO(n)$,one recovers the notion of *oriented* $E_n$-algebras which are commonly known as *framed $E_n$-algebras* in the literature.
:::

Let $M$ be a dimension $n$ manifold. By [@MW Example 6.2.10], an $\mathbb{E}_n^{O(n)}$-algebra $A$ defines an $A_\infty$-$n$-category[^1] $\mathcal{C}^A$ and thus yields the **Blob complex** $\mathcal{B}_*(M,\mathcal{C}^A)$, see [@MW Definition 7.0.1]. Similarly we can form the topological chiral homology $\int_M A$, see [@Francis Definition 3.15] (or [@L-VI; @L-TFT]).

::: proposition
[]{#P:blob label="P:blob"} Let $M$ be a closed $n$-dimensional manifold (non necessarily framed nor oriented) and $A$ an $\mathbb{E}_n^{O(n)}$-algebra. There is an natural equivalence $$\int_{M} A\; \cong\; \mathcal{B}_*(M,\mathcal{C}^A)$$ in $k\textit{-}Mod_\infty$. Further, if $A$ is a CDGA, there is an natural equivalence $CH_M^{\scriptstyle\bullet}(A) \cong \int_{M} A$ in $k\textit{-}Mod_\infty$.
:::

::: proof
*Proof.* According to [@MW Theorem 7.2.1], the Blob complex $\mathcal{B}_*(M,\mathcal{C}^A)$ satisfies the excision property for closed manifolds and can be computed using a colimit construction ([@MW § 6.3]) similar to Definition [\[Def:TCHasColimit\]](#Def:TCHasColimit){reference-type="ref" reference="Def:TCHasColimit"}. It also converts disjoint union of manifolds to tensor products [@MW Property 1.3.2] and $\mathcal{B}_*(D^n,\mathcal{C}^A)\cong A$ by [@MW Property 1.3.4] (and [@MW Example 6.2.10]). The same properties hold for topological chiral homology as in Proposition [\[P:TCHpushout\]](#P:TCHpushout){reference-type="ref" reference="P:TCHpushout"} (or Lemma [\[L:TCHpushout2\]](#L:TCHpushout2){reference-type="ref" reference="L:TCHpushout2"}), the proofs and references to [@Francis; @L-VI; @L-TFT] in the unoriented case being essentially the same as in the framed one (using $O(n)$-homotopy fixed $E_n$-algebras). It follows that one can apply *mutatis mutandis* the proof of Theorem [\[T:TCH=CH\]](#T:TCH=CH){reference-type="ref" reference="T:TCH=CH"} to get the equivalences stated in the proposition. ◻
:::

::: remark
Let $A=C_{\scriptstyle\bullet}(\Omega^{n} Y)$ be the $E_n$-algebra associated to the $n$-fold loop space of an $n$-connective pointed space $Y$. The Blob complex $\mathcal{B}_*(M,\mathcal{C}^{C_{\scriptstyle\bullet}(\Omega^{n} Y)})$ for non-necessarily closed manifolds shall not be mistaken with the Blob complex associated to the $A_\infty$-$n$-category associated to the fundamental groupoid of the space $Y$ in [@MW § 6] (though the construction share some similarities). Indeed, it is claimed [@MW Theorem 7.3.1] that the latter construction compute the chains on the space of all maps $\textrm{Map}(M,Y)$, while the first one, by non-abelian Poincaré duality [@L-VI], $\int_{M} \Omega^{n} Y$ is the chains on the space of maps with compact support $\textrm{Map}_{c}(M,Y)$.
:::

Theorem [\[T:HF=TCH\]](#T:HF=TCH){reference-type="ref" reference="T:HF=TCH"} below and Proposition [\[P:blob\]](#P:blob){reference-type="ref" reference="P:blob"} suggest that the blob complex should be closely related to Factorization algebras as well. It would be interesting to relate system of fields, n-category and the blob complex in the sense of [@MW] to factorization algebras (with extra properties) in the sense of [@CG]. We plan to investigate these relationship in a future work.

[^1]: this is, for $n=1$, an instance of the linear category with a single object associated to an associative algebra and, for general $n$, a slight variant of the construction of an $(\infty, n)$-category $\mathcal{B}^n(A)$ associated to an $E_n$-algebra $A$ as in [@Francis]
