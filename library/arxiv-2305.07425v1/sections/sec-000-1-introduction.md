---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.986
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a group G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
A fixed group $G$ will admit many different cobounded actions on different hyperbolic metric spaces. Abbott, Balasubramanya, and Osin in [@ABO19] show that the set of equivalence classes of cobounded hyperbolic actions of a group $G$ carries a natural partial order; see Section [\[sec:prelim\]](#sec:prelim){reference-type="ref" reference="sec:prelim"}. The resulting poset is called the *poset of hyperbolic structures* on $G$, denoted $\mathcal{H}(G)$. Roughly speaking, one action is larger than another if the smaller space can be formed by equivariantly collapsing some subspaces of the larger. The motivation is that the larger an action is in this partial order, the more information about the geometry of the group it should provide.

The posets $\mathcal H(G)$ remain mysterious, especially for groups with features of non-positive curvature, which tend to have uncountable posets of hyperbolic structures [@ABO19]. First steps towards understanding these posets were made in [@Bal20], [@AR19], and [@AR19b]. While [@Bal20] and [@AR19b] give complete descriptions of $\mathcal H(G)$ for the groups in question, it appears essentially impossible to do this, given current technology, for groups with strong features of non-positive curvature. Nonetheless, one aspect of the poset that can be understood in many instances is the (non-)existence of a *largest* element of $\mathcal H(G)$, that is, an element that is greater than or equal to every other element of the poset. When a largest element exists, we say that the group $G$ is *$\mathcal H$--accessible*; otherwise, the group is *$\mathcal H$--inaccessible*. The first and third authors show that many groups with features of non-positive curvature are $\mathcal H$--inaccessible [@AR19b]. In this paper, we follow this direction by extending these results to a large class of 3-manifold groups.

We first consider fundamental groups of non-geometric 3--manifolds with empty or toroidal boundary. If $M$ is a compact, orientable, irreducible non-geometric 3-manifold, then there exists a non-empty minimal union $\mathcal T$ of disjoint essential tori in $M$ such that each connected component of $M\setminus\mathcal T$ is Seifert fibered or hyperbolic. This is called the *torus decomposition of $M$*, and the connected components of $M\setminus\mathcal T$ are called *pieces*. Our first result shows that if $M$ contains certain types of pieces, then $\pi_1(M)$ is $\mathcal H$--inaccessible. To describe these pieces, we introduce the class of *non-elementary* Seifert fibered manifolds, which are those whose base orbifolds are orientable and hyperbolic. Non-elementary graph manifolds are those whose Seifert pieces are non-elementary, and a mixed manifold is non-elementary if all of its Seifert fibered pieces and maximal graph manifold components are non-elementary. Any graph manifold or Seifert fibered manifold is finitely covered by a non-elementary one. See Section [\[sec:NPC\]](#sec:NPC){reference-type="ref" reference="sec:NPC"} for a more in-depth discussion.

::: restatable
thmNPCmfld []{#thm:NPCmld label="thm:NPCmld"} Let $M$ be a non-geometric 3-manifold with empty or toroidal boundary. If the torus decomposition of $M$ contains any of the following, then $\pi_1(M)$ is $\mathcal H$--inaccessible:

(1) a hyperbolic piece which contains a boundary torus of $M$;

(2) two hyperbolic pieces glued along a torus;

(3) an isolated non-elementary Seifert fibered piece; or

(4) a non-elementary maximal graph manifold component.
:::

We note a straightforward corollary of Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"}.

::: cor
If $M$ is one of the following types of 3-manifolds, then $\pi_1(M)$ is $\mathcal H$--inaccessible:

(a) a finite non-trivial connected sum of finite volume cusped hyperbolic 3-manifolds;

(b) a non-elementary mixed manifold.
:::

::: proof
*Proof.* Part (a) follows from Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"}(1). For part (b), observe that a mixed manifold must contain either: two hyperbolic pieces glued along a torus, an isolated non-elementary Seifert fibered piece, or a non-elementary graph manifold component with boundary. In these cases, we apply Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"} (2), (3), or (4), respectively. ◻
:::

The first and third author give a straightforward criterion to show that a group is $\mathcal H$--inaccessible [@AR19 Lemma 1.4]; see Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}. In this paper, we show in Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"} that if a peripheral subgroup of a relatively hyperbolic group satisfies this criterion, then the group itself also satisfies the criterion. There is a natural relatively hyperbolic structure on $\pi_1(M)$ in which the peripheral subgroups are fundamental groups of certain tori, Seifert fibered pieces, and graph manifolds. The proof Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"} proceeds by showing that, in each case, there is a peripheral subgroup that is $\mathcal H$--inaccessible because it satisfies Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}, and then applying Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"}. The key step is the following theorem.

::: thm
[]{#thm:graphandSFmflds label="thm:graphandSFmflds"} If $M$ is a non-elementary graph manifold or a non-elementary Seifert fibered manifold, then $\pi_1(M)$ is $\mathcal H$--inaccessible.
:::

Theorem [\[thm:graphandSFmflds\]](#thm:graphandSFmflds){reference-type="ref" reference="thm:graphandSFmflds"} generalizes [@AR19 Theorem 1.1], in which the first and third authors show that flip graph manifold groups, a special class of graph manifold groups, are $\mathcal{H}$--inaccessible.

The class of non-elementary graph manifold groups belongs to a larger class of graphs of groups called *Croke-Kleiner admissible groups* that were introduced by Croke and Kleiner in [@CK02]. Roughly speaking, Croke-Kleiner admissible groups are modeled on the JSJ structure of graph manifolds where the (fundamental groups of the) Seifert fibered pieces are replaced by central extensions $G$ of general hyperbolic groups $H$: $$\label{centralExtEQ}
1\to Z(G)=\mathbb Z\to G\to H\to 1.$$ In some sense, Croke-Kleiner admissible groups are the simplest interesting groups constructed algebraically from a finite number of hyperbolic groups. The $\mathcal{H}$--inaccessibility of non-elementary graph manifold groups follows from the following result for Croke-Kleiner admissible groups.

::: thm
[]{#thm1 label="thm1"} Every Croke-Kleiner admissible group has a subgroup of index at most $2$ which is $\mathcal{H}$--inaccessible.
:::

A non-geometric 3-manifold $M$ always has a double cover in which all Seifert fibered pieces are non-elementary, and hence passing to a further finite cover if necessary, we obtain a finite cover $M' \to M$ such that $M'$ is either a non-elementary graph manifold or a non-elementary mixed manifold. Combining Theorems [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"} and [\[thm:graphandSFmflds\]](#thm:graphandSFmflds){reference-type="ref" reference="thm:graphandSFmflds"} yields the following corollary.

::: cor
If $M$ is a non-geometric 3-manifold then $\pi_1(M)$ has a finite index subgroup $H$ such that every finite index subgroup $K \le H$ is $\mathcal{H}$--inaccessible.
:::

So far, we have only discussed non-geometric $3$--manifolds. In some cases, we can also understand the $\mathcal H$--accessibility of (finite-index subgroups) of geometric $3$--manifold groups.

::: prop
Every $3$--manifold with Nil or Sol geometry has a finite cover whose fundamental group is $\mathcal H$--inaccessible. The fundamental group of a closed hyperbolic $3$--manifold is $\mathcal H$--accessible, while the fundamental group of a finite-volume cusped hyperbolic $3$--manifold is $\mathcal H$--inaccessible.
:::

::: proof
*Proof.* If a 3--manifold $M$ has the geometry of Sol, then $M$ is a torus bundle over a $1$--dimensional orbifold (an interval with reflection boundary points or a circle) and thus $M$ has a double cover that is a torus bundle with Anosov monodromy. The $\mathcal H$--inaccessibility of the fundamental group of this bundle then follows from work of the first and third authors [@AR19].

If the geometry of $M$ is Nil, $M$ is a Seifert fibered 3-manifold, and $M$ is finitely covered by a torus bundle $M'$ with unipotent monodromy, and the only possible hyperbolic actions are lineal and elliptic. On the other hand, the abelianization of $\pi_1(M')$ is virtually $\mathbb{Z}^2$, so this yields infinitely many homomorphisms $\mathbb{Z}^2 \to \mathbb{R}$ modulo scaling, and infinitely many inequivalent actions on $\mathbb{R}$ by translations. Since such lineal actions are incomparable by [@ABO19 Theorem 2.3], $\pi_1(M')$ is $\mathcal H$-inaccessible.

The fundamental group of a closed hyperbolic $3$--manifold is a hyperbolic group, and so is $\mathcal H$--accessible. The result for a finite-volume cusped hyperbolic $3$--manifold is Corollary [\[cor:hyp\]](#cor:hyp){reference-type="ref" reference="cor:hyp"}. ◻
:::

In Section [\[sec:Boundary\]](#sec:Boundary){reference-type="ref" reference="sec:Boundary"}, we consider general finitely generated 3-manifold groups. This includes fundamental groups of reducible 3-manifolds, certain geometric 3-manifolds, and 3-manifolds with non-toroidal boundary. In Proposition [\[prop:highergenus\]](#prop:highergenus){reference-type="ref" reference="prop:highergenus"}, we characterize the $H$--accessibility of many such 3-manifold groups. In particular, any finitely generated fundamental group of a hyperbolic 3-manifold without rank-1 cusps is $\mathcal H$--accessible.

Many basic questions about posets of hyperbolic structures are still open. Surprisingly, it is still unknown whether $\mathcal{H}$--inaccessibility of a finite index normal subgroup of $G$ passes to $\mathcal{H}$--inaccessibility of the ambient group $G$. In the setting of non-geometric 3-manifolds, the only cases in which we are unable to determine the $\mathcal H$--(in)accessibility of the fundamental group are a manifold all of whose Seifert fibered pieces are elementary and a graph manifold whose underlying graph contains a single vertex. We suspect that these manifolds are also $\mathcal{H}$--inaccessible, but the techniques in this paper do not apply. We thus ask the following question.

::: ques
Let $M$ be a graph manifold with underlying graph containing only one vertex. Is $\pi_1(M)$ $\mathcal{H}$--inaccessible?
:::
