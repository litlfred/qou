---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-010-42-haccessibility-of-non-elementary-graph-manifo
section_title: "H–accessibility of non-elementary graph manifolds"
section_number: 4.2
pages: 12-16
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.993
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a group G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
[]{#sec:NPCgraph label="sec:NPCgraph"} Let $M$ be a 3-dimensional non-elementary graph manifold with Seifert fibered pieces $M_1,\ldots,M_k$ in its torus decomposition. There is an induced graph-of-groups structure $\mathcal{G}$ on $\pi_1(M)$ with underlying graph $\Gamma$ as follows. There is a vertex of $\Gamma$ for each $M_i$, with vertex group $\pi_1(M_{i})$. Each edge group is $\mathbb{Z}^2$, the fundamental group of a torus in the decomposition. The edge monomorphisms come from the two different gluings of the torus into the two adjacent Seifert fibered components. With this graph of groups structure, $\pi_1(M)$ is a Croke-Kleiner admissible group.

The universal cover $\widetilde{M}$ of $M$ is tiled by a countable collection of copies of the universal covers $\widetilde{M}_1, \dots, \widetilde{M}_k$. We call these subsets *vertex spaces*. We refer to boundary components of vertex spaces as *edge spaces*. Two vertex spaces are either disjoint or intersect along an edge space. Let $T$ be the Bass-Serre tree of $\mathcal G$.

Applying Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"} to the Croke-Kleiner admissible group $\pi_1(M)$, we obtain a cover $M' \to M$ of degree $2$ such that $\pi_1(M')$ is not $\mathcal{H}$--accessible. However, this is not enough to conclude $\mathcal{H}$--inaccessibility of $\pi_1(M)$, as it is unknown whether $\mathcal{H}$--inaccessibility of a finite index subgroup passes to the ambient group. In this section, we will show that $\pi_1(M)$ itself is $\mathcal{H}$--inaccessible; see Proposition [\[prop:NPCgraph\]](#prop:NPCgraph){reference-type="ref" reference="prop:NPCgraph"}.

We begin with a lemma. Let $\pi_{\alpha}(
\beta)$ be the closest point projection of a line $\beta$ to a line $\alpha$ in a hyperbolic space. Let $d_\alpha(\cdot, \cdot)$ be in the resulting projection distances.

::: lem
[]{#lem:important label="lem:important"} Let $F$ be a 2-dimensional hyperbolic orbifold with nonempty boundary and universal cover $\widetilde{F}$, and let $\mathbb L$ be the collection of boundary lines of $\widetilde{F}$. For any $\alpha\in \mathbb L$ and any loxodromic $\gamma\in \pi_1(F)$ whose axis in $\widetilde{F}$ is also a line in $\mathbb L$, the following holds. There exists a constant $\lambda >0$ such that for any $n \in  \mathbb{Z}$ and any line $\beta \in \mathbb{L}\setminus \{\alpha, \gamma^{n}(\alpha) \}$, we have $$d_{\beta}(\alpha, \gamma^{n}(\alpha)) \le \lambda.$$
:::

The proof of this lemma is very similar to that of [@AR19 Lemma 5.6]. We refer the reader to that paper for some figures that may be helpful; see in particular [@AR19 Figure 8].

::: proof
*Proof of Lemma [\[lem:important\]](#lem:important){reference-type="ref" reference="lem:important"}.* Since $\mathbb L$ is a $\pi_1(F)$--invariant collection of axes in the hyperbolic plane $\mathbb H^2$, it follows from Example [\[ex:linesinhypplane\]](#ex:linesinhypplane){reference-type="ref" reference="ex:linesinhypplane"} that $(\mathbb L,\pi_\ell)$ satisfies the projection axioms for some constant $\xi$. In particular, there exists a constant $\xi > 1$ such that $\operatorname{diam}(\pi_\ell(\ell')) \le \xi$ for distinct elements $\ell$ and $\ell'$ in $\mathbb{L}$. Let $$\lambda = \max \{ \xi, d(\alpha, \gamma(\alpha)) + 2\xi, d(\alpha,\gamma^{2}(\alpha)) + 2\xi \}.$$

Let $\ell\in \mathbb L$ denote the axis of $\gamma$ in $\widetilde{F}$. If $\ell=\alpha$, then $$d_\beta(\alpha,\gamma^n(\alpha))=d_\beta(\alpha,\alpha)\leq \xi\leq \lambda,$$ and the result holds. For the remainder of the proof, we assume $\ell\neq\alpha$ and consider two cases.

*Case 1*: $\beta \notin \{\gamma^{k}(\alpha)  \,| k \in \mathbb Z \}$

In this case, there exists a unique $k_0 \in \mathbb Z$ such that $\beta$ lies between $\gamma^{k_{0}}(\alpha)$ and $\gamma^{k_{0}+1}(\alpha)$. That is, $\partial \mathbb H^2$ minus the endpoints of $\gamma^{k_0}(\alpha)$ and $\gamma^{{k_0}+1}(\alpha)$ consists of four intervals, one containing the endpoints of $\beta$, one containing the endpoints of all $\gamma^i(\alpha)$ for $i\notin \{k_0,k_0+1\}$, and the other two disjoint from all endpoints of lines in $\mathbb L$. Fixing an appropriate orientation on $\beta$, we partially order sub-intervals $I=[x,y]$ and $J=[z,w]$ of $\beta$ (with $x\leq y$ and $z\leq w$ in the orientation) by $I \leq J$ if $x\leq z$ and $y\leq w$. Then the projections of the lines $\gamma^{k}(\alpha)$ onto $\beta$ occur in the following order $$\pi_{\beta}(\gamma^{k_{0}}(\alpha)) < \pi_{\beta}(\gamma^{k_{0}-1}(\alpha))  < \pi_{\beta}(\gamma^{k_{0} -2}(\alpha))  < \ldots < \pi_{\beta}(\ell)$$ and $$\pi_{\beta}(\ell) < \ldots < \pi_{\beta}(\gamma^{k_{0} +3}(\alpha)) < \pi_{\beta}(\gamma^{k_{0} + 2}(\alpha)) < \pi_{\beta}(\gamma^{k_{0} +1}(\alpha)).$$ Thus $$d_{\beta}(\alpha, \gamma^{n}(\alpha)) \le d_{\beta} (\gamma^{k_{0}}(\alpha), \gamma^{k_{0} +1}(\alpha)) \le  d(\gamma^{k_{0}}(\alpha), \gamma^{k_{0} +1}(\alpha)) + 2\xi,$$ where $d(\gamma^{k_{0}}(\alpha), \gamma^{k_{0} +1}(\alpha))$ denotes the distance between $\gamma^{k_{0}}(\alpha)$ and $\gamma^{k_{0} +1}(\alpha)$ in the hyperbolic plane. The final inequality follows from the fact that the nearest point projection is a $1$--Lipschitz map and that $\pi_\ell(\ell')$ has diameter at most $\xi$ for any distinct lines $\ell,\ell'\in \mathbb L$. Since $d(\gamma^{k_{0}}(\alpha), \gamma^{k_{0} +1}(\alpha))) = d(\alpha, \gamma(\alpha))$, it follows that $$d_{\beta}(\alpha, \gamma^{n}(\alpha)) \le  d(\alpha, \gamma(\alpha)) + 2\xi \le \lambda.$$

*Case 2*: $\beta = \gamma^{k}(\alpha)$ for some integer $k \neq 0, n$. Using an analogous argument to Case 1, we see that $d_{\beta}(\alpha, \gamma^{n}(\alpha))$ is bounded above by $$d_{\beta}(\gamma^{k-1}(\alpha), \gamma^{k+1}(\alpha)) \le d(\alpha, \gamma^{2}(\alpha)) + 2\xi \le \lambda. \qedhere$$ ◻
:::

::: prop
[]{#prop:NPCgraph label="prop:NPCgraph"} The fundamental group of a non-elementary graph manifold is $\mathcal{H}$--inaccessible.
:::

::: proof
*Proof.* Let $\mathcal{G}$ be the graph-of-groups structure on $\pi_1(M)$ with underlying graph $\Gamma$ described at the beginning of this section. The assumption that the graph manifold $M$ is non-elementary ensures that there are at least two vertices in the graph $\Gamma$. We divide the proof into two cases, depending on the location of loops in $\Gamma$.

Fix an edge $\alpha$ in $\Gamma$ that is not a loop, and label the vertex $\alpha^-$ by $\mu$ and the vertex $\alpha^+$ by $\omega$. Let $T_{\alpha}$ be the torus in $M$ associated to the edge $\alpha$. Let $v$ and $w$ be two adjacent vertices in the tree $T$ such that $\widetilde{M}_v$ and $\widetilde{M}_w$ are the universal covers of the Seifert pieces $M_{\mu}$ and $M_{\omega}$, respectively. Let $z_\mu$ and $z_\omega$ be the generators of $Z_\mu$ and $Z_\omega$, respectively.

Suppose there is no loop in $\Gamma$ based at the vertex $\mu$. Let $$\mathbb{W}_{\mu} \vcentcolon= \bigl \{ L_v \, \bigl |\, \text{$\widetilde{M}_v$ is a lift of the Seifert fibered piece $M_\mu$} \bigr \}$$

If $L_v$ and $L_{v'}$ are two distinct elements in $\mathbb{W}_\mu$, then $d(v, v') \ge 2$ (though they are not necessarily an even distance apart). In this case, the techniques in Section [\[CKA:finiteindex\]](#CKA:finiteindex){reference-type="ref" reference="CKA:finiteindex"} apply to show that there is a cobounded action $\pi_1(M) \curvearrowright \mathcal{C}_{K}(\mathbb{W}_\mu)$ such that $z_\mu$ is loxodromic and $z_\omega$ is elliptic.

Suppose there is a loop in $\Gamma$ based at the vertex $\mu$.

As in Section [\[CKA:finiteindex\]](#CKA:finiteindex){reference-type="ref" reference="CKA:finiteindex"}, we partition the vertex set $T^0$ into two disjoint collections of vertices $\mathcal{V}_1$ and $\mathcal{V}_2$ such that if $z$ and $z'$ both lie in $\mathcal{V}_i$ then $d(z, z')$ is even. Applying Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"} to the Croke-Kleiner admissible group $\pi_1(M)$, we obtain a degree 2 cover $M' \to M$ such that $\pi_1(M')$ is $\mathcal{H}$--inaccessible and $\pi_1(M')$ preserves $\mathcal V_1$ and $\mathcal V_2$.

Assume without loss of generality that $v$ is in $\mathcal{V}_1$ and $w$ is in $\mathcal{V}_2$. Let $$\mathbb{Q}_{\mu} \vcentcolon= \bigl \{ L_u \, \bigl | \, \text{$u \in \mathcal{V}_1$ and $\widetilde{M}_{u}$ is a lift of $M_{\mu}$} \bigr. \}$$ The results in Section [\[CKA:finiteindex\]](#CKA:finiteindex){reference-type="ref" reference="CKA:finiteindex"} still hold for $\mathbb{Q}_\mu$, and thus we obtain quasi-trees of spaces $\mathcal{C}_{K} (\mathbb{Q}_\mu)$ for sufficiently large $K$. Since $\pi_1(M')$ preserves $\mathbb{Q}_\mu$, we obtain an action $\pi_1(M') \curvearrowright \mathcal{C}_{K} (\mathbb{Q}_\mu)$ as in Section [\[CKA:finiteindex\]](#CKA:finiteindex){reference-type="ref" reference="CKA:finiteindex"}.

Passing to a power of two if necessary, we may assume that $z_{\mu}, z_\omega \in \pi_1(M')$. As shown in the proof of Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"}, the element $z_{\mu}$ acts loxodromically on $\mathcal{C}_{K}(\mathbb{Q}_\mu)$, while $z_{\omega}$ acts elliptically on $\mathcal{C}_{K}(\mathbb{Q}_\mu)$. By the construction of $\mathcal C_K(\mathbb Q_\mu)$, and since vertex groups are central extensions of $\mathbb{Z}$, the element $z_{\mu}$ is a WWPD${}^+$ element in the action $\pi_1(M')\curvearrowright \mathcal C_K(\mathbb Q_\mu)$. Hence Proposition [\[prop1\]](#prop1){reference-type="ref" reference="prop1"} provides a homogeneous quasimorphism $q_K \colon \pi_1(M') \to \mathbb R$ satisfying $q_K(z_{\omega}) =0$ and $q_K(z_{\mu}) \neq 0$.

Our goal is to extend $q_K$ to a homogeneous quasimorphism $\pi_1(M)\to\mathbb R$ while ensuring that $z_{\omega}$ and $z_{\mu}$ still have trivial and non-trivial image, respectively. Let $h \in \pi_1(M)$ be a representative of the non-trivial coset of $\pi_1(M')$ in $\pi_1(M)$. Define a function $q'_{K} \colon \pi_1(M') \to \mathbb{R}$ by $$q'_{K}(x) \vcentcolon= q_{K}(x) + q_{K}(hxh^{-1}).$$

Note that $q'_{K}$ is constant on conjugacy classes of $\pi_1(M)$, i.e., $q'_{K}(yxy^{-1}) = q'_{K}(x)$ for any $y \in \pi_1(M)$ and $x \in \pi_1(M')$). Hence it follows from the proof of [@BF09 Lemma 7.2] that $q'_{K}$ extends to a homogeneous quasimorphism $\rho_K \colon \pi_1(M) \to \mathbb{R}$ defined by $\rho_K(x) \vcentcolon= q'_{K}(x^2) \bigl / 2$ for each $x \in \pi_1(M)$.

::: lem
[]{#lem:inproof label="lem:inproof"} Suppose there is a loop in $\Gamma$ based at $\mu$. For $K$ large enough, we have $\rho_K(z_{\omega}) =0$ and $\rho_K(z_{\mu}) \neq 0$.
:::

We defer the proof of the lemma for the moment and assume this result to complete the proof Proposition [\[prop:NPCgraph\]](#prop:NPCgraph){reference-type="ref" reference="prop:NPCgraph"}. Since $\rho_K \colon \pi_1(M) \to \mathbb{R}$ is a nonzero homogeneuous quasimorphism, we obtain from Proposition [\[prop2\]](#prop2){reference-type="ref" reference="prop2"} an action $\pi_1(M) \curvearrowright \mathcal{L}$ on a quasi-line. Moreover, since $\rho_{K}(z_{\mu}) \neq 0$ and $\rho_K(z_{\omega})=0$, the element $z_{\mu}$ is loxodromic while $z_{\omega}$ is elliptic in this action.

Now, consider the other endpoint $\omega$ of $\alpha$. Suppose first there is not a loop in $\Gamma$ based at $\omega$. Interchanging the roles of $\mu$ and $\omega$ in Case 1 above produces an action $\pi_1(M)\curvearrowright \mathcal C_K(\mathbb W_\omega)$ such that $z_\mu$ is elliptic and $z_\omega$ is loxodromic. On the other hand, if there is a loop in $\Gamma$ based at $\omega$, then interchanging the roles of $\mu$ and $\omega$ in Case 2 above produces an action $\pi_1(M)\curvearrowright \mathcal L'$ on a quasi-line in which (after possibly passing to a power of 2) $z_\mu$ is elliptic and $z_\omega$ is loxodromic.

Regardless of which combination of cases holds for the vertices $\mu$ and $\omega$, we have produced two actions on hyperbolic spaces and two commuting elements $z_\mu$ and $z_\omega$ which satisfy the conditions of Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}, which concludes the proof. ◻
:::

We now prove Lemma [\[lem:inproof\]](#lem:inproof){reference-type="ref" reference="lem:inproof"}.

::: proof
*Proof of Lemma [\[lem:inproof\]](#lem:inproof){reference-type="ref" reference="lem:inproof"}.* Recall that $v\in \mathcal V_1$. As $h \in \pi_1(M)$ is a representative of the non-trivial coset of $\pi_1(M')$ in $\pi_1(M)$, we have $hv \in \mathcal{V}_2$. Note that $\widetilde{M}_{hv}$ is also a lift of $M_{\mu}$, even though $hv$ is not in $\mathcal{V}_1$. Fix a vertex $v_0$ adjacent to $hv$ such that $\widetilde{M}_{v_0}$ is a lift of $M_{\mu}$ in $\widetilde{M}$. This ensures that $L_{v_0}$ is in $\mathbb{Q}_1$. Let $l \in 
\mathbb{L}_{hv}$ be the boundary line of $\widetilde{F}_{hv}$ corresponding to the edge $[v_0, hv].$

We will first show that $\rho_K(z_{\omega}) = 0$. Since $q_K$ is a homogeneous quasimorphism and $z_\omega\in \pi_1(M')$, we have that $$\rho_{K}(z_{\omega}) = q'_{K}(z_{\omega}) = q_{K}(z_{\omega}) + q_{K}(hz_{\omega}h^{-1}) = 0 + q_{K}(hz_{\omega}h^{-1}).$$ By Proposition [\[prop1\]](#prop1){reference-type="ref" reference="prop1"}, to show $\rho_K(z_{\omega}) = q_{K}(hz_{\omega}h^{-1}) =  0$, it suffices to show that $hz_{\omega}h^{-1}$ is elliptic in the action $\pi_1(M') \curvearrowright \mathcal{C}_{K}(\mathbb{Q}_1)$. Let $\xi >0$ be the projection constant of the projection complexes $\mathbb{Q}_1$ and $\mathbb Q_2$. Since $M_{hv}$ is a Seifert fibered piece, we have $\widetilde{M}_{hv}= \widetilde{F}_{hv} \times \mathbb{R}$, where $F_{hv}$ is the base orbifold of $M_{hv}$. Applying Lemma [\[lem:important\]](#lem:important){reference-type="ref" reference="lem:important"} to the space ${F}_{hv}$, the collection of boundary lines of $\widetilde{F}_{hv}$, the fixed boundary line $l$, and the chosen element $\gamma=h z_\omega h^{-1}$, we obtain a constant $\lambda >0$. We further enlarge $\lambda$ so that it satisfies Lemma [\[lem:easy3\]](#lem:easy3){reference-type="ref" reference="lem:easy3"}.

Choose $K > 4\xi + 4 +  2\lambda  +  \lambda^2$ large enough to apply Proposition [\[prop:BBFDistanceProp\]](#prop:BBFDistanceProp){reference-type="ref" reference="prop:BBFDistanceProp"}, and let $y_0$ be a point in the projection of $L_{hz_\omega h^{-1} v_0}$ to $L_{v_0}$. We will show that $d_{\mathcal C_K(\mathbb Q_1)}(y_0, \gamma^{n} (y_0)) \le 6K$ for all $n \in \mathbb{Z}$, which will imply that $\gamma$ is elliptic in the action $\pi_1(M') \curvearrowright \mathcal{C}_{K}(\mathbb{Q}_1)$, as desired.

Fix $n\in \mathbb Z$. By Proposition [\[prop:BBFDistanceProp\]](#prop:BBFDistanceProp){reference-type="ref" reference="prop:BBFDistanceProp"}, we have $$\label{equ:4}
    d_{\mathcal C_K(\mathbb Q_1)}(y_0, \gamma^{n}( y_0)) \le 4 \sum_{\substack{u \in \mathcal{V}_1 \\ \text{$L_u \in \mathbb{Q}_1$}}} [d_{L_u}(y_0,  \gamma^{n}(y_0))]_K + 6K.$$ Thus it suffices to show that $d_{L_u}(y_0,  \gamma^{n}(y_0))< K$ for all $u\in \mathcal V_1$ such that $L_u\in \mathbb Q_1$. Since $L_u\in \mathbb Q_1$, $\widetilde M_u$ is a lift of $M_\mu$.

We divide the proof into several cases, depending on the location of the vertex $u$.

*Case 1: $u\in\{v_0,\gamma^n(v_0)\}$.* We assume that $u = v_0$ as the case $u=  \gamma^{n}(v_0)$ is proved similarly.

By assumption, $y_0\in L_{v_0}$, and so $\gamma^{n}(y_0) \in L_{\gamma^{n}(y_0)}$. By definition, $$d_{L_{v_0}}(y_0, \gamma^{n}(y_0)) = \mathop{\mathrm{diam}}(\{y_{0}\} \cup \Pi_{L_{v_0}}(L_{\gamma^{n}(v_0)}))$$ and $$d_{L_{v_0}} (L_{\gamma(v_0)}, L_{\gamma^{n}(v_0)}) = \mathop{\mathrm{diam}}\bigl (\Pi_{L_{v_0}}(L_{\gamma(v_0)}) \cup \Pi_{L_{v_0}}(L_{\gamma^{n}(v_0)}) \bigr ).$$ As $y_0 \in \Pi_{L_{v_0}}(L_{\gamma(v_0)})$ and the diameter of $\Pi_{L_{v_0}}(L_{\gamma(v_0)})$ is no more than $\xi$, it follows that $$\label{equ:1}
    \bigl | d_{L_{v_0}}(y_0, \gamma^{n}(y_0)) - d_{L_{v_0}} (L_{\gamma(v_0)}, L_{\gamma^{n}(v_0)}) \bigr | \le 2 \xi.$$

The line $l$ is the boundary line of $\widetilde{F}_{hv}$ associated to the edge $[v_0, hv]$. Recall that $z_\omega$ is an element of the edge group $G_{[v,w]}$, and so it fixes the vertex $v$. Thus $\gamma(hv)=hz_\omega h^{-1}(hv)=h z_\omega(v)=hv$,

and so the lines $\gamma(l)$ and $\gamma^{n}(l)$ are the boundary lines in $\widetilde{F}_{hv}$ associated to the edges $[hv, \gamma(v_0)]$ and $[hv, \gamma^{n}(v_0)]$, respectively.

Combining ([\[equ:1\]](#equ:1){reference-type="ref" reference="equ:1"}) with Lemmas [\[lem:easy3\]](#lem:easy3){reference-type="ref" reference="lem:easy3"} and [\[lem:important\]](#lem:important){reference-type="ref" reference="lem:important"} implies that $$\begin{aligned}
d_{L_{v_0}}(y_0,  \gamma^{n}(y_0)) & \le 
  d_{L_{v_0}}(L_{\gamma (v_0)},  L_{\gamma^{n}(v_0)}) + 2 \xi \\ 
    & \le \lambda  d_{l}(\gamma(l), \gamma^{n}(l)) + \lambda + 2\xi \\
    &= \lambda \, d_{\gamma^{-1}(l)} (l, \gamma^{n-1}(l)) + \lambda + 2\xi \le \lambda^2 + \lambda + 2\xi < K.
\end{aligned}$$

*Case 2: $u\in \mathop{\mathrm{Lk}}(hv)$ but $u\not\in\{v_0,\gamma^n(v_0)\}$.* Let $b$ be the boundary line of $\widetilde{F}_{hv}$ corresponding to the edge $[u, hv]$, so that $b \notin \{ l, \gamma^{n}(l) \}$. By Lemma [\[lem:important\]](#lem:important){reference-type="ref" reference="lem:important"}, we have that $d_{b}(l , \gamma^{n}(l)) \le \lambda$. It follows from Lemma [\[lem:easy3\]](#lem:easy3){reference-type="ref" reference="lem:easy3"} that $$\begin{aligned}
     d_{L_u}(y_0,  \gamma^{n}(y_0)) &= d_{L_u}(L_{v_0}, L_{\gamma^{n}(v_0)}) \\
     &\le \lambda \,d_{b}(l , \gamma^{n}(l)) + \lambda \\
     &\le \lambda^2 + \lambda < K.
 
\end{aligned}$$

*Case 3: $u\not\in \mathop{\mathrm{Lk}}(hv)$.* In this case, $d(u, [v_0,\gamma^{n}(v_0)])\ge 2$, and so $$d_{L_u}(y_0,  \gamma^{n}y_0)= d_{L_u}(L_{v_0}, L_{\gamma^{n}(v_0)}) \le \lambda < K.$$

We have shown that $d_{L_u}(y_0,  \gamma^{n}(y_0))< K$ for all $u\in \mathcal V_1$ such that $L_u\in \mathbb Q_1$. Therefore [\[equ:4\]](#equ:4){reference-type="eqref" reference="equ:4"} shows that $d_{\mathcal C_K(\mathbb Q_1)}(y_0, \gamma^{n} (y_0)) \leq 6K$ for all $n$. It follows that $\gamma$ is elliptic in the action $\pi_1(M')\curvearrowright \mathcal C_K(\mathbb Q_1)$, and so $q(z_\omega)=0$.

To complete the proof, we need to verify that $$\rho_{K}(z_{\mu}) = q_{K}'(z_{\mu}) = q_{K}(z_{\mu}) + q_{K}(hz_{\mu}h^{-1}) \neq 0.$$ Since $hz_\mu h^{-1}$ is a central element in $G_{hv} = \mathop{\mathrm{Stab}}_{G}(hv)$, it follows from Remark [\[rem:loxellipaction\]](#rem:loxellipaction){reference-type="ref" reference="rem:loxellipaction"} that $hz_\mu h^{-1}$ acts elliptically on $L_{v_0}$, and thus also on $\mathcal{C}_{K}(\mathbb{Q}_1)$. By Proposition [\[prop1\]](#prop1){reference-type="ref" reference="prop1"}, we have $q_K(hz_\mu h^{-1})=0$. Since $q_{K}(z_{\mu}) \neq 0$, it follows that $\rho_K(z_\mu)\neq 0$. ◻
:::

Theorem [\[thm:graphandSFmflds\]](#thm:graphandSFmflds){reference-type="ref" reference="thm:graphandSFmflds"} now follows immediately from Corollary [\[cor:SF\]](#cor:SF){reference-type="ref" reference="cor:SF"} and Proposition [\[prop:NPCgraph\]](#prop:NPCgraph){reference-type="ref" reference="prop:NPCgraph"}.

## Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"} {#sec:mixedmanifolds}

In this section, we put together the above results and prove Theorem [\[thm:NPCmld\]](#thm:NPCmld){reference-type="ref" reference="thm:NPCmld"}, whose statement we recall for the convenience of the reader.

::: proof
*Proof.* Let $M_1, \dots, M_k$ be the maximal graph manifold components and isolated Seifert fibered pieces of the torus decomposition of $M$. Let $S_1, \dots, S_{\ell}$ be the tori in the boundary of $M$ that bound a hyperbolic piece, and let $T_1, \dots,T_m$ be the tori in the torus decomposition of $M$ that separate two hyperbolic components of the torus decomposition. By Lemma [\[lem:RHmfld\]](#lem:RHmfld){reference-type="ref" reference="lem:RHmfld"}, $\pi_1(M)$ is hyperbolic relative to $$\mathbb{P} = \{\pi_1(M_p)\}_{p=1}^k \cup \{\pi_1(S_q)\}_{q=1}^\ell \cup \{\pi_1(T_r)\}_{r=1}^m.$$ In all of the cases (1)--(4), the collection $\mathbb P$ is non-empty.

In case (1), the collection $\{S_1,\dots, S_\ell\}\neq \emptyset$, while in case (2), $\{T_1,\dots, T_m\}\neq \emptyset$. Both of these collections consist of tori. Note that $\mathbb Z^2$ is $\mathcal H$--inaccessible: the projections of $\mathbb{Z}^2$ onto each factor yield two actions on lines to which Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"} applies. Thus, if $\{\pi_1(S_q)\} \cup \{\pi_1(T_r)\}$ is nonempty, then $\pi_1(M)$ is $\mathcal{H}$--inaccessible by Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"}, proving the theorem in cases (1) and (2).

Next suppose that (3) holds, so that there is an isolated non-elementary Seifert fibered piece $M_p$. By the proof of Corollary [\[cor:SF\]](#cor:SF){reference-type="ref" reference="cor:SF"} we see that $\pi_1(M_p)$ has two actions to which Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"} applies. By Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"}, $\pi_1(M)$ is $\mathcal{H}$--inaccessible.

Finally, suppose that (4) holds, so that there is a non-elementary maximal graph manifold component $M_p$. By the proof of Proposition [\[prop:NPCgraph\]](#prop:NPCgraph){reference-type="ref" reference="prop:NPCgraph"}, there are two commuting elements $a,b\in\pi_1(M_p)$ and two actions on hyperbolic spaces (in fact, quasi-trees) $\pi_1(M_p) \curvearrowright X$ and $\pi_1(M_p) \curvearrowright Y$ such that $a$ and $b$ are elliptic and loxodromic, respectively, in $\pi_1(M_p) \curvearrowright X$ and $a$ is loxodromic in $\pi_1(M_p) \curvearrowright Y$. Applying Lemma [\[lem:RHG\]](#lem:RHG){reference-type="ref" reference="lem:RHG"} to $P = \pi_1(M_p)$, we conclude that $\mathcal{H}(\pi_1(M))$ contains no largest element. ◻
:::
