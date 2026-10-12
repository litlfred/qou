---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-008-4-haccessibility-of-3-manifold-groups
section_title: "H–accessibility of 3-manifold groups"
section_number: 4
pages: 10-12
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a grou p G on diﬀerent hyperbolic metric spaces carries a natural partial order."
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.988
---
[]{#sec:NPC label="sec:NPC"}

The goal of this section is to prove Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"}, which gives conditions under which the fundamental group of a non-geometric 3--manifold is $\mathcal H$--inaccessible.

We begin by recalling some definitions and facts about 3-manifolds. Let $M$ be a compact, connected, orientable, irreducible 3-manifold with empty or toroidal boundary. By the geometrization theorem for 3-manifolds of Perelman ([@Perel1], [@Perel2], [@Perel3]) and Thurston, either

1.  the manifold $M$ is *geometric*, in the sense that its interior admits one of the following geometries: $S^3$, $\mathbb{E}^3$, $\mathbb{H}^3$, $S^{2} \times \mathbb{R}$, $\mathbb{H}^{2} \times \mathbb{R}$, $\widetilde{SL(2, \mathbb{R})}$, Nil, and Sol; or

2.  the manifold $M$ is *non-geometric*. In this case, the torus decomposition of 3-manifolds yields a nonempty minimal union $\mathcal{T} \subset M$ of disjoint essential tori, unique up to isotopy, such that each component of $M \backslash \mathcal{T}$ is either a Seifert fibered piece or a hyperbolic piece.

We refer the reader to [@Scott] for background on geometric structures on 3-manifolds. A Seifert fibered piece is called *non-elementary* if its base orbifold is orientable and hyperbolic, and it is called *isolated* if it is not glued to any other Seifert fibered piece.

The manifold $M$ is called a *graph manifold* if all the pieces of $M \backslash \mathcal{T}$ are Seifert fibered. A graph manifold is *non-elementary* if it contains at least two pieces and all pieces are non-elementary. In other words, a non-elementary graph manifold is obtained by gluing at least two and at most finitely many non-elementary Seifert fibered manifolds, where the gluing maps between the Seifert components do not identify (unoriented) Seifert fibers up to homotopy.

We will call a non-geometric manifold $M$ a *mixed manifold* if it is not a graph manifold. If there is a subcollection $\mathcal T'$ of $\mathcal T$ and a connected component of $M \backslash \mathcal T'$ that is a graph manifold, then this connected component is called a *graph manifold component* of the mixed manifold $M$. A graph manifold component is *maximal* if it is not properly contained in another graph manifold component. A mixed manifold is *non-elementary* if all maximal graph manifold components and Seifert fibered pieces are non-elementary.

::: rem
Every graph (respectively, mixed) manifold is finitely covered by a non-elementary graph (respectively, mixed) manifold (see, for example, [@PW14 Lemma 3.1], [@KL98 Lemma 2.1]).
:::

Our starting point for proving Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"} is the following lemma, which describes when $\pi_1(M)$ is relatively hyperbolic.

::: lem
[]{#lem:RHmfld label="lem:RHmfld"} Let $M_1, \dots, M_k$ be the maximal graph manifold components and Seifert fibered pieces of the torus decomposition of $M$. Let $S_1, \dots, S_{\ell}$ be the tori in the boundary of $M$ that bound a hyperbolic piece, and let $T_1, \dots,T_m$ be the tori in the torus decomposition of $M$ that separate two hyperbolic components. Then $\pi_1(M)$ is hyperbolic relative to $$\mathbb{P} = \{\pi_1(M_p)\}_{p=1}^k \cup \{\pi_1(S_q)\}_{q=1}^\ell \cup \{\pi_1(T_r)\}_{r=1}^m.$$
:::

This relatively hyperbolic structure on $\pi_1(M)$ is useful because of the following result, which gives a criterion for relatively hyperbolic groups to be $\mathcal H$--inaccessible.

::: lem
[]{#lem:RHG label="lem:RHG"} Let $(G, \mathbb{P})$ be a relatively hyperbolic group. If there is a peripheral subgroup $P \in \mathbb{P}$ that satisfies the hypotheses of Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}, then $G$ is $\mathcal{H}$--inaccessible.
:::

Before proving the lemma, we state an immediate corollary, which gives a different proof of [@AR19 Theorem 6.2].

::: cor
[]{#cor:hyp label="cor:hyp"} The fundamental group of a finite-volume cusped hyperbolic 3-manifold is $\mathcal{H}$--inaccessible.
:::

We now turn to the proof of Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"}.

::: proof
*Proof of Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"}.* To see that $\mathcal{H}(G)$ does not contain a largest element, we will construct two actions of $G$ on hyperbolic spaces with commuting elements $a, b \in G$ that satisfy the hypotheses of Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}. To do this, we will apply the machinery of *induced actions* from [@AHO].

Since $P$ satisfies the hypotheses of Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"} by assumption, there are commuting elements $a,b\in P$ and isometric actions $P \curvearrowright X$ and $P \curvearrowright Y$ on hyperbolic spaces such that $a$ and $b$ act loxodromically and elliptically, respectively, in the action $P \curvearrowright X$, and $b$ acts loxodromically in the action $P \curvearrowright Y$. For all $Q\in \mathbb P\setminus \{P\}$, fix the trivial action of $Q$ on a point. By [@AHO Corollary 4.11(a)], there exist hyperbolic spaces $Z_X,Z_Y$ on which $G$ acts by isometries, associated to the collection of actions $\{Q\curvearrowright * \mid Q\in \mathbb P\setminus \{P\}\}\cup \{P\curvearrowright X\}$ and the collection of actions $\{Q\curvearrowright * \mid Q\in \mathbb P\setminus \{P\}\}\cup \{P\curvearrowright Y\}$, respectively. Moreover, there are coarsely $P$--equivariant quasi-isometric embeddings $X\to Z_X$ and $Y\to Z_Y$. Therefore, $a$ acts loxodromically and $b$ acts elliptically in the action $G\curvearrowright Z_X$, while $b$ acts loxodromically in the action $G\curvearrowright Z_Y$. This completes the proof. ◻
:::

In light of Lemmas [\[lem:RHmfld\]](#lem:RHmfld){reference-type="ref" reference="lem:RHmfld"} and [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"}, to prove the $\mathcal H$--inaccessibility of $\pi_1(M)$, it suffices to understand its peripheral subgroups. In Section [0.1](#subsec:SF){reference-type="ref" reference="subsec:SF"}, we analyze the fundamental groups of the Seifert fibered pieces. The more difficult subgroups to understand are the fundamental groups of the maximal graph manifold components. We consider these in Section [\[sec:NPCgraph\]](#sec:NPCgraph){reference-type="ref" reference="sec:NPCgraph"} and give conditions under which they satisfy Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}; see Proposition [\[prop:NPCgraph\]](#prop:NPCgraph){reference-type="ref" reference="prop:NPCgraph"}. In Section [\[sec:mixedmanifolds\]](#sec:mixedmanifolds){reference-type="ref" reference="sec:mixedmanifolds"}, we put these results together and prove Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"}. Up to this point, we have been assuming that $M$ has empty or toroidal boundary. Finally, in Section [\[sec:Boundary\]](#sec:Boundary){reference-type="ref" reference="sec:Boundary"}, we consider $3$-manifolds with higher genus boundary components.

## Seifert fibered manifolds {#subsec:SF}

In this section, we analyze Seifert fibered pieces.

::: lem
[]{#lem:centralextension label="lem:centralextension"} Let $1 \to \mathbb{Z} \xrightarrow{i} G \xrightarrow{\pi} H \to 1$ be a short exact sequence where $\mathbb{Z}$ is central in $G$ and $H$ is a non-elementary hyperbolic group. Then $G$ is $\mathcal{H}$--inaccessible.
:::

::: proof
*Proof.* Choose a finite generating set $J$ of $H$ and consider the hyperbolic action $G \curvearrowright \mathop{\mathrm{Cay}}(H, J)$. Let $a$ be a generator of the group $\mathbb{Z}$, and let $b$ be an element of $G$ such that $\pi(b)$ is loxodromic in $H \curvearrowright \mathop{\mathrm{Cay}}(H, J)$. The element $b$ is thus loxodromic in the action $G \curvearrowright \mathop{\mathrm{Cay}}(H, J)$, as well, while the element $a$ is elliptic (in fact, trivial) in this action.

Since every integral cohomology class of a hyperbolic group is bounded (see [@Min01]), the central extension $\mathbb{Z}\to G \to H$ corresponds to a bounded element of $H^{2}(H, \mathbb{Z})$. Hence [@HRSS22 Lemma 4.1] provides a quasi-morphism $\phi \colon G \to \mathbb{Z}$ which is unbounded on $i(\mathbb{Z})$. By [@ABO19 Lemma 4.15], there exists a generating set $S$ for $G$ such that $L\vcentcolon = \mathop{\mathrm{Cay}}(G, S)$ is a quasi-line and the inclusion $\mathbb{Z}\to L$ induced by $i$ is a $\mathbb{Z}$--equivariant quasi-isometry. We thus obtain a hyperbolic action $G \curvearrowright L$ for which $a$ is loxodromic. Since $a \in Z(G)$, the elements $a$ and $b$ commute. By Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}, $G$ is $\mathcal{H}$--inaccessible. ◻
:::

::: cor
[]{#cor:SF label="cor:SF"} Let $M$ be a non-elementary Seifert fibered manifold. Then $\pi_1(M)$ is $\mathcal{H}$--inaccessible.
:::

::: proof
*Proof.* Let $\varphi \colon M \to \Sigma$ be a Seifert fibration. Since $S^1 \to M \to \Sigma$ is a circle bundle over $\Sigma$, there is a short exact sequence $$1 \to \mathbb{Z}\to \pi_1(M) \to \pi_1(\Sigma) \to 1,$$ where $\mathbb{Z}$ is the normal cyclic subgroup of $\pi_1(M)$ generated by a fiber. The group $\mathbb{Z}$ is central in $\pi_1(M)$ since $\Sigma$ is orientable (see, e.g., [@Mar Proposition 10.4.4]). By Lemma [\[lem:centralextension\]](#lem:centralextension){reference-type="ref" reference="lem:centralextension"}, the group $\pi_1(M)$ is $\mathcal{H}$--inaccessible. ◻
:::
