---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-012-44-haccessibility-of-finitely-generated-3-manifo
section_title: "H–accessibility of finitely generated 3-manifold groups"
section_number: 4.4
pages: 17-18
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.994
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a group G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
[]{#sec:Boundary label="sec:Boundary"} In this section, we explain how one might reduce the study of $\mathcal{H}$--accessibility of all finitely generated 3--manifold groups to the case of compact, orientable, irreducible, $\partial$--irreducible 3--manifold groups. In particular, we show that for any hyperbolic 3-manifold $M$ without rank-1 cusps, if $\pi_1(M)$ is finitely generated then it is $\mathcal H$-accessible.

Let $M$ be an orientable 3-manifold with finitely generated fundamental group. It follows from Scott's Core Theorem that $M$ contains a compact codimension zero submanifold whose inclusion map is a homotopy equivalence [@ScottCore], and thus also an isomorphism on fundamental groups. We thus can assume our 3-manifolds are compact.

The sphere-disk decomposition provides a decomposition of a compact, orientable 3-manifold $M$ into irreducible, $\partial$--irreducible pieces $M_1, \ldots, M_k$. In particular, $\pi_1(M)$ is a free product $\pi_1(M_1) * \pi_1(M_2) * \cdots *\pi_1(M_k)$. Let $G_i\vcentcolon =  \pi_1(M_i)$. Note that $\pi_1(M)$ is hyperbolic relative to the collection $\mathbb{P}= \{ G_1, \ldots, G_k \}$. In light of Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"}, the $\mathcal{H}$--inaccessibility of $\pi_1(M)$ follows whenever some $G_i$ satisfies the conditions of Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}. Hence, it suffices to investigate the $\mathcal{H}$--accessibility of the groups $G_i$.

If $M$ has empty or toroidal boundary, then $\mathcal{H}$--accessibility of $\pi_1(M)$ is understood, except for a few sporadic cases, by Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"}. The following proposition addresses certain manifolds with higher genus boundary.

::: prop
[]{#prop:highergenus label="prop:highergenus"} Let $M$ be a compact, orientable, irreducible, $\partial$--irreducible 3-manifold which has at least one boundary component of genus at least $2$. Then $\pi_1(M)$ is $\mathcal H$--inaccessible under either of the following hypotheses:

1.  []{#item:higherboundary1 label="item:higherboundary1"} $M$ has trivial torus decomposition and at least one torus boundary component; or

2.  []{#item:higherboundary2 label="item:higherboundary2"} $M$ has non-trivial torus decomposition.

On the other hand, if $M$ has trivial torus decomposition and all boundary components have genus at least $2$, then $\pi_1(M)$ is $\mathcal H$--accessible.
:::

::: proof
*Proof.* As in [@Sun20 Section 6.3], we can paste compact hyperbolic 3-manifolds with totally geodesic boundaries to the higher genus boundary components of $M$ to obtain a finite volume hyperbolic manifold $N$ (in case $M$ has trivial torus decomposition) or a mixed 3-manifold (in case $M$ has non-trivial torus decomposition).

If ([\[item:higherboundary1\]](#item:higherboundary1){reference-type="ref" reference="item:higherboundary1"}) holds, then the manifold $N$ has toroidal boundary, and, by assumption, there is a boundary torus $T$ for $N$ which is also a boundary torus of $M$.

The subgroup $P\vcentcolon= \pi_1(T)\simeq \mathbb Z^2$ satisfies Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"} and is a peripheral subgroup in the relatively hyperbolic structure on $\pi_1(N)$. The proof of Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"} shows that there are commuting elements $a,b\in P$ and hyperbolic actions $\pi_1(N) \curvearrowright Z_X$ and $\pi_1(N) \curvearrowright Z_Y$ such that $a$ and $b$ act loxodromically and elliptically, respectively, in the action $\pi_1(N) \curvearrowright Z_X$, and $b$ acts loxodromically in the action $G \curvearrowright Z_Y$. As $\pi_1(M)$ is a subgroup of $\pi_1(N)$, we obtain induced actions $\pi_1(M) \curvearrowright Z_X$ and $\pi_1(M) \curvearrowright Z_Y$. Since $a, b \in \pi_1(M)$, we see that $\pi_1(M)$ is $\mathcal{H}$--inaccessible by Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}.

If ([\[item:higherboundary2\]](#item:higherboundary2){reference-type="ref" reference="item:higherboundary2"}) holds, then $N$ has either empty or toroidal boundary and has the following properties:

(i) $M$ is a submanifold of $N$ with incompressible toroidal boundary;

(ii) cutting $N$ along the tori in the torus decomposition of $M$ yields the torus decomposition of $N$; and

(iii) each piece of $M$ with a boundary component of genus at least $2$ is contained in a hyperbolic piece of $N$.

In particular, it follows from (ii) and (iii) that $N$ is a mixed 3-manifold, and hence $\pi_1(N)$ is $\mathcal{H}$--inaccessible by Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"}.

In the proof of Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"}, we prove the $\mathcal H$--inaccessibility of $\pi_1(N)$ by showing there are two commuting elements $a,b\in \pi_1(T)$ for some torus $T$ in the torus decomposition of $N$ and isometric actions $\pi_1(N) \curvearrowright Z_X$ and $\pi_1(N) \curvearrowright Z_Y$ on hyperbolic spaces, and then applying Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}.

By (ii), $T$ is also a torus in the torus decomposition of $M$. Thus the induced actions $\pi_1(M) \curvearrowright Z_X$ and $\pi_1(M) \curvearrowright Z_Y$ satisfy the hypotheses of Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}, and so $\pi_1(M)$ is $\mathcal{H}$--inaccessible.

We now turn our attention to the final statement of the theorem. In this case, the manifold $N$ is closed. A finitely generated subgroup $H$ of $N$ is a *virtual surface fiber subgroup* if $N$ admits a finite cover $N' \to N$ such that $H$ is a subgroup of $\pi_1(N')$ and $H$ is a surface fiber subgroup of $\pi_1(N')$. Any finitely generated subgroup $H$ of $\pi_1(N)$ is either a geometrically finite Kleinian group or a virtual surface fiber subgroup in $\pi_1(N)$ by the Covering Theorem (see [@Can96]) and the Subgroup Tameness Theorem (see [@Agol04; @CG06] or [@AFW15 Theorem 4.1.2] for a statement). In particular, $\pi_1(M)$ is either a virtual surface fiber subgroup, in which case it is hyperbolic, or it is geometrically finite in $\pi_1(N)$. In the latter case, $\pi_1(M)$ is undistorted in $\pi_1(N)$ [@Hru10 Corollary 1.6], and we again conclude that $\pi_1(M)$ is hyperbolic, since undistorted subgroups of hyperbolic groups are hyperbolic. As a result, in either case, $\pi_1(M)$ is $\mathcal{H}$--accessible. ◻
:::
