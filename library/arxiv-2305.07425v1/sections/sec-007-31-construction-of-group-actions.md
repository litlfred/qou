---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-007-31-construction-of-group-actions
section_title: "Construction of group actions"
section_number: 3.1
pages: 8-10
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.985
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a group G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
For notational simplicity, we replace $G$ by its index $\leq 2$ subgroup $G'$. For each vertex $v$ in the Bass-Serre tree $T$, let $L_v$ be the quasi-line from Definition [\[defn:quasilineL_v\]](#defn:quasilineL_v){reference-type="ref" reference="defn:quasilineL_v"}. Recall that $gL_v = L_{gv}$ for any group element $g$ in $G$.

Let $\mathbb{L}_1$ be the collection of quasi-lines $\{ L_v \}_{v \in \mathcal{V}_1}$ and $\mathbb{L}_2$ be the collection of quasi-lines $\{ L_v \}_{v \in \mathcal{V}_2}$. We define a projection of $L_v$ to $L_{v'}$ in $\mathbb L_i$ as follows.

::: defn
[]{#defn:projectionmap label="defn:projectionmap"} For any two distinct vertices $v,v'\in \mathcal V_i$, let $e'=[w, u]$ and $e=[u,v]$ denote the last two (oriented) edges in $[v',v]$. The *projection* from $L_{v'}$ into $L_v$ is $$\Pi_{L_v} (L_{v'}) \vcentcolon = \psi_{e}(\mathop{\mathrm{\operatorname{proj}}}_{\ell_{\bar{e}}}(\ell_{e'})),$$ where $\psi_e \colon \ell_{\bar{e}} \to L_v$ and $\mathop{\mathrm{\operatorname{proj}}}_{\ell_{\bar{e}}} \colon \mathcal{H}_u \to \ell_{\bar{e}}$ are the maps introduced in Section [\[sec:pre\]](#sec:pre){reference-type="ref" reference="sec:pre"}.
:::

The fact that $d(v, v')$ is even is not necessary for Definition [\[defn:projectionmap\]](#defn:projectionmap){reference-type="ref" reference="defn:projectionmap"}, only that $d(v, v') \ge 2$.

We will verify that the $\mathbb{L}_i$ with these projection maps satisfy the projection axioms (see Definition [\[defn:Projectionaxioms\]](#defn:Projectionaxioms){reference-type="ref" reference="defn:Projectionaxioms"}) for $i=1,2$. Let $d_{L_a}(L_b,L_c)$ be the projection distance $\mathop{\mathrm{diam}}\bigl (\Pi_{L_{a}} (L_{b}) \cup \Pi_{L_{a}} (L_{b}) \bigr )$.

::: lem
[]{#lem:easy1 label="lem:easy1"} There exists a constant $\lambda >0$ such that $\mathop{\mathrm{diam}}(\Pi_{L_v}(L_{v'}))\leq \lambda$ for any distinct $v,v'\in \mathcal V_i$ for $i=1,2$. Moreover, if ${a},  {b}, {c} \in \mathcal V_i$ are distinct vertices with $d_{T}( a, [b, c]) \ge 2$, then $\Pi_{L_a}(L_c) = \Pi_{L_a}(L_b)$.
:::

::: proof
*Proof.* By Remark [\[rem:boundeddiameter\]](#rem:boundeddiameter){reference-type="ref" reference="rem:boundeddiameter"}, there is a uniform bound on the diameter of $\mathop{\mathrm{\operatorname{proj}}}_{\ell_{\bar{e}}}(\ell_{e'})$. Combined with the fact that $\psi_e$ is uniformly coarsely Lipschitz, this gives the constant $\lambda$. Considering the convex hull of $\{a\}\cup [b,c]$, we see that, orienting $[c,a]$ and $[b,a]$ towards $a$, the last two edges of $[c,a]$ are the same as the last two edges of $[b,a]$. Hence by definition, $\Pi_{L_a}(L_c) =  \Pi_{L_a}(L_b)$. ◻
:::

Let $v$ be a vertex of the Bass-Serre tree $T$. By Remark [\[rem:boundeddiameter\]](#rem:boundeddiameter){reference-type="ref" reference="rem:boundeddiameter"}, the collection $\{ \ell_{f} = i_{v} (\tau_{f}(X_f)) \, |\, f \in E(T)\,\,\text{such that}\, f^{+} = v \}$ satisfies the projection axioms with a constant $\xi_0$. Let $d_\ell$ denote the projection distances with respect to $\mathop{\mathrm{\operatorname{proj}}}_\ell$. The following lemma follows immediately from Lemma [\[lem:psiquasi\]](#lem:psiquasi){reference-type="ref" reference="lem:psiquasi"} and the definitions of $d_{\ell_e}$ and $d_{L_{v}}$.

::: lem
[]{#lem:easy3 label="lem:easy3"} There exists a constant $\lambda >0$ such that the following holds. Let $u, v, w$ be distinct vertices in $\mathcal{V}_1$ contained in $\mathop{\mathrm{Lk}}(o)$ for some vertex $o$ in $\mathcal{V}_2$. Let $e=[w,o]$, $e_1=[u,o],$ and $e_2=[v,o]$. Then $$\frac{1}{\lambda} d_{\ell_{e}}(\ell_{e_1}, \ell_{e_2}) -\lambda \le d_{L_{w}} (L_{u}, L_{v})     \le \lambda d_{\ell_{e}}(\ell_{e_1}, \ell_{e_2}) + \lambda.$$
:::

We are now ready to verify the projection axioms.

::: prop
[]{#prop:Fi label="prop:Fi"} There exists $\xi >0$ such that for each $i \in \{1,2\}$, $\mathbb{L}_i$ together with the projection maps $\mathop{\mathrm{\operatorname{proj}}}_\ell$ satisfies the projection axioms.
:::

::: proof
*Proof.* We verify the projection axioms for $\mathbb L_1$. The case for $\mathbb L_2$ is identical. The constant $\xi$ will be defined explicitly during the proof.

**Axiom 1:** This follows from Lemma [\[lem:easy1\]](#lem:easy1){reference-type="ref" reference="lem:easy1"}.

**Axiom 2:** Let ${u},  {v}, {w}$ be distinct vertices in $\mathcal V_1$. In the course of the proof, we will compute a constant $\xi > 0$ such that if $d_{L_w}(L_u, L_v ) > \xi$, then $d_{L_u}(L_w, L_v )  \le \xi$.

Since $d_{L_w}(L_u, L_v ) > 0$, it follows from Lemma [\[lem:easy1\]](#lem:easy1){reference-type="ref" reference="lem:easy1"} that either $w$ lies on $[u,v]$ or $d_T(w, [u,v]) =1$. If $w$ lies on $[u,v]$, then since $u,w,v\in \mathcal V_1$, we have $d_{T}(u, [w,v])\ge 2$ and $d_{T}(v, [u,w])\ge 2$. Axiom 2 thus follows from Lemma [\[lem:easy1\]](#lem:easy1){reference-type="ref" reference="lem:easy1"}.

On the other hand, suppose that $d(w,[u,v])=1$. Let $o\in [u,v]$ be adjacent to $w$ and consider the vertices $u',v'\in \mathop{\mathrm{Lk}}(o)\cap [u,v]$ which lie in $[u,o]$ and $[o,v]$, respectively. If $u\neq u'$, then $d_{L_u}(L_w,L_v)=0$, and so we may assume without loss of generality that $u=u'$. Furthermore, $\pi_{L_u}(L_v)=\pi_{L_u}(L_{v'})$ by definition. Thus to prove the upper bound on $d_{L_u}(L_w,L_v)$, it suffices to assume that $v=v'$, in which case $u,v,w$ all lie in $\mathop{\mathrm{Lk}}(o)$, where $o\in \mathcal V_2$.

Let $e=[w,o]$, $e_1=[u,o],$ and $e_2=[v,o]$. It follows from Lemma [\[lem:easy3\]](#lem:easy3){reference-type="ref" reference="lem:easy3"} that $$\frac{1}{\lambda} d_{\ell_{e}}(\ell_{e_1}, \ell_{e_2}) -\lambda \le d_{L_{w}} (L_{u}, L_{v})     \le \lambda d_{\ell_{e}}(\ell_{e_1}, \ell_{e_2}) + \lambda.$$ Again applying Lemma [\[lem:easy3\]](#lem:easy3){reference-type="ref" reference="lem:easy3"} with the roles of $u, v, w$ exchanged, we have that $$\frac{1}{\lambda} d_{\ell_{e_1}}(\ell_{e}, \ell_{e_2}) - \lambda \le d_{L_{u}} (L_{w}, L_{v} ) \le \lambda d_{\ell_{e_1}}(\ell_{e}, \ell_{e_2}) + \lambda.$$ Since $\{ \ell_{f}   \, |\, f \in E(T) \textrm{ and } f^{+} = o \}$ satisfies the projection axioms with constant $\xi_0$, it follows that $d_{\ell_e}(\ell_{e_1}, \ell_{e_2})>\xi_0$ implies that $d_{\ell_{e_1}}(\ell_{e}, \ell_{e_2})\le \xi_0$. Since there are finitely many choices for $o$ up to the action $G'$, the constant $\xi_0$ may be chosen independently of $o$. Thus, setting $\xi = \lambda \xi_{0} + \lambda$, the above inequalities show that $d_{L_W}(L_u,L_v)>\xi$ implies that $d_{L_u}(L_w,L_v)\leq \xi$. This verifies Axiom 2.

**Axiom 3:** For distinct $u, v \in \mathcal V_1$, we will prove the set $$\{w\in \mathcal V_1 \mid d_{L_w}(L_u, L_v )>\xi\}$$ is finite. By Lemma [\[lem:easy1\]](#lem:easy1){reference-type="ref" reference="lem:easy1"}, any such vertex $w$ is either contained in the interior of $[u,v]$ or satisfies $d(w, [u,v])=1$. The first case yields at most $d(u, v)-1$ choices for $w$.

Suppose $d(w, [u,v])=1$. As in the proof of Axiom 2, we can assume that $u,v,w$ lie in $\mathop{\mathrm{Lk}}(o)$ for some vertex $o$ in $\mathcal{V}_{2}$. Let $e_1=[u,o], e_2=[v,o]$, and $e = [w,o]$. By Lemma [\[lem:easy3\]](#lem:easy3){reference-type="ref" reference="lem:easy3"}, we have $d_{L_{w}} (L_{u}, L_{v}) \le \lambda d_{\ell_{e}}(\ell_{e_1}, \ell_{e_2}) + \lambda$. Since $\xi =  \lambda \xi_{0} + \lambda$, it follows that $$\{w \in \mathop{\mathrm{Lk}}(o) \, \bigl | \,d_{L_w}(L_u, L_v ) > \xi \} \subset \{w \in \mathop{\mathrm{Lk}}(o) \, \bigl |\, d_{\ell_e}(\ell_{e_1}, \ell_{e_2}) > \xi_0 \}.$$

The projection axioms for $\{ \ell_{f} \, |\, f \in E(T) \textrm{ and } f^{+} = v \}$ imply that the latter set is finite, and so the former set must also be finite. Since there are finitely many possibilities for $o$, this verifies Axiom 3. ◻
:::

::: lem
For each $i =1,2$, the action of $G = \pi_1(\mathcal{G})$ on the collection $\mathbb L_i= \{ L_v \mid v\in\mathcal V_i\}$ satisfies $$\Pi_{g L_v}(g L_u) = g \Pi_{L_v}( L_u)$$ for any $v\in \mathcal V_i$ and any $g\in G$.
:::

::: proof
*Proof.* This follows immediately from the definition of $\Pi$ and the fact that the maps $\mathop{\mathrm{\operatorname{proj}}}$ and $\psi$ are $G$--equivariant in the sense that $\mathop{\mathrm{\operatorname{proj}}}_{\overline{ge}}(\ell_{gf})=g\cdot \mathop{\mathrm{\operatorname{proj}}}_{\bar e}(\ell_f)$ and $\psi_{ge}(gx)=g\psi_e(x)$. ◻
:::

We are now ready to prove Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"}.

::: proof
*Proof of Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"}.* Let $G'$ be the finite index subgroup of $G$ given by Lemma [\[lem:index2subgroup\]](#lem:index2subgroup){reference-type="ref" reference="lem:index2subgroup"}, which is also a Croke-Kleiner admissible group. Without loss of generality, we replace $G$ by $G'$ for the rest of the proof.

By Proposition [\[prop:Fi\]](#prop:Fi){reference-type="ref" reference="prop:Fi"}, the collection of quasi-lines $\mathbb L_i= \{ L_v \mid v\in\mathcal V_i\}$ satisfies the projection axioms with a constant $\xi$ for $i=1,2$. Fix $K>4\xi$. The unbounded quasi-trees of metric spaces $\mathcal C_{K} (\mathbb L_1)$ and $\mathcal C_{K} (\mathbb L_2)$ are themselves quasi-trees, and they admit unbounded isometric actions $G \curvearrowright \mathcal C_{K} (\mathbb L_1)$ and $G \curvearrowright \mathcal C_{K}(\mathbb L_2)$.

Since the underlying graph of $G$ is bipartite, we can choose an edge $\check{e}$ in $\Gamma$ which is not a loop. Choosing the orientation of $\check{e}$ correctly, $\mu = \check{e}^{-}$ and $\omega = \check{e}^{+}$ have lifts in $T$ belonging to $\mathcal{V}_1$ and $\mathcal{V}_2$ respectively. By construction, elements of $Z_{\mu}$ and $Z_{\omega}$ are loxodromic and elliptic in the action on $\mathcal{C}_{K}(\mathbb{L}_1)$, respectively, and elliptic and loxodromic in the action on $\mathcal{C}_{K}(\mathbb{L}_2)$, respectively. By Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}, we conclude that the group $G$ is $\mathcal{H}$--inaccessible. ◻
:::

Every graph manifold has a finite cover that is a graph manifold $N$ containing at least two Seifert fibered spaces such that each Seifert fibered piece has orientable, hyperbolic base orbifold. We call such a graph manifold *non-elementary* in Section [\[sec:NPC\]](#sec:NPC){reference-type="ref" reference="sec:NPC"}. Since $\pi_1(N)$ is a Croke-Kleiner admissible group, the following corollary is immediate from Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"}.

::: cor
[]{#cor:graphmanifoldfi label="cor:graphmanifoldfi"} Every graph manifold has a finite cover whose fundamental group is $\mathcal{H}$--inaccessible.
:::

It is still unknown whether $\mathcal{H}$--inaccessibility of a finite index normal subgroup of $G$ passes to $\mathcal{H}$--inaccessibility of the ambient group $G$. Thus it is natural to ask whether the "finite cover" condition in Corollary [\[cor:graphmanifoldfi\]](#cor:graphmanifoldfi){reference-type="ref" reference="cor:graphmanifoldfi"} can be removed. We will address this question in the following section.
