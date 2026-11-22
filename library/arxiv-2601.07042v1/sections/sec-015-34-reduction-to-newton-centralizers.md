---
doc_id: arxiv-2601.07042v1
doc_title: "A Tannakian description of the local Kaletha gerbe"
section_id: sec-015-34-reduction-to-newton-centralizers
section_title: "Reduction to Newton centralizers"
section_number: 3.4
pages: 20-22
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.871
doc_brief: "A Tannakian description of the local Kaletha gerbe — We construct, for a p-adic field F, an explicit semisimple Tannakian category RigIsocF whose category of fiber functors recovers Kaletha’s Galois"
---
We start with a basic structural result about $\mathrm{RigIsoc}_{F}$:

::: lem
The category $\mathrm{RigIsoc}_{F}$ is semisimple.
:::

::: proof
*Proof.* We work with the category $\text{Rep}(\mathcal{E}_{\text{Kal}})$ instead, which we showed in §[\[sec:RigIsocdef\]](#sec:RigIsocdef){reference-type="ref" reference="sec:RigIsocdef"} can be identified with $\mathrm{RigIsoc}_{F}$. By [@DM82 Proposition 2.23], it suffices to show that $\mathcal{E}_{\text{Kal}}$ is pro-reductive (in this proof by "reductive" we mean that the connected component of the identity is reductive). This follows from the fact that it can be written as a projective limit of groups of the form $$1 \to [\frac{\mathrm{Res}_{E/F}(\mu_{n})}{\mu_{n}}](\overline{F}) \to \mathcal{E}_{E/F,n} \to \Gamma_{K_{E}/F} \to 1,$$ where $K_{E}/E/F$ are finite Galois extensions, cf. [@Kalannals §3.1], which are all finite. ◻
:::

The previous lemma implies that, in order to construct all objects in $\mathrm{RigIsoc}_{F}$, the important task is to construct its simple objects. To facilitate this, we recall some standard facts about twisted Levi subgroups of $\mathrm{GL}_n$.

Recall that for a reductive group $G$ defined over $F$, a subgroup $M \subset G$ is a twisted Levi subgroup if it is defined over $F$ and $M_{\overline{F}} \subset G_{\overline{F}}$ is a Levi subgroup. We say that a twisted Levi $M \subset G$ subgroup is *elliptic* if the $F$-split rank of $Z(M)$ equals that of $Z(G)$. We denote the maximal split sub-torus of $Z(M)$ by $A_M$. Suppose that $M \subset G$ is a non-elliptic twisted Levi subgroup. Then $L=Z_{G}(A_M)$ is a proper Levi subgroup of $G$ containing $M$. In particular, the elliptic twisted Levi subgroups of $G$ are precisely those that are not contained in a proper Levi subgroup.

::: lem
[]{#lem: GLntwistedlevis label="lem: GLntwistedlevis"} The twisted Levi subgroups of $\mathrm{GL}_n$ over $F$ are isomorphic to $$\prod\limits_{i=1}^k \mathrm{Res}_{E_i/F} \mathrm{GL}_{n_i},$$ where $E_i/F$ is a field extension of degree $m_i$ and $\sum\limits_{i=1}^k m_in_i=n$.
:::

::: proof
*Proof.* This statement is well-known. See the proof given in [@FintzenSchwein Lemma 4.3.4] ◻
:::

Suppose that $X \in \mathop{\mathrm{obj}}(\mathrm{RigIsoc}_{F})$, which maps via [\[gerbeequiv\]](#gerbeequiv){reference-type="eqref" reference="gerbeequiv"} to an algebraic $1$-cocycle $z_X: \mathcal{E}_{\mathop{\mathrm{Kal}}} \rightarrow \mathrm{GL}_n$ with $\nu_X$ the associated algebraic homomorphism of the band.

::: lem
[]{#lemma:reg label="lemma:reg"} We continue with $G=\mathrm{GL}_n$. One can conjugate $z_X$ by $G(\overline{F})$ such that $\nu_X$ has trivial Galois action (i.e., it gives an $F$-rational homomorphism $u \to \mathrm{GL}_{n}$).
:::

::: proof
*Proof.* We first argue that for all twisted Levis subgroups $M$, the map $$H^1(F, N_G(M)) \rightarrow H^1(F, N_G(M)/M)$$ is surjective. Note that for $M$ a maximal torus, this surjectivity is a corollary of Raghunathan's theorem. For $G=\mathrm{GL}_n$ we can prove the result for a general twisted Levi. First, we assume $M$ is a Levi subgroup, and then $N_G(M) \rightarrow N_G(M)/M$ has a natural $\Gamma_{\overline{F}/F}$-equivariant splitting coming from the permutation matrices. This implies the surjectivity for $M$, and then we prove the general case by twisting.

Let $M= Z_{G}(\nu_X)$. Since $G=\mathrm{GL}_n$, we have that $M$ is a twisted Levi of $G_E$, where $E$ is the field of definition of $\nu_X$. Notice that the action on $z_X$ by coboundaries induces a conjugation action on $\nu_X$ and hence $M$. The group $M$ might not be $\Gamma_{\overline{F}/F}$-invariant, but since $G = \mathrm{GL}_{n}$ is split, every Levi subgroup over $\overline{F}$ is conjugate to the base-change of an $F$-rational Levi subgroup and we can thus conjugate $\nu_X$ (and twist $z_{X}$ by the corresponding coboundary) such that $M$ is the base-change to $\overline{F}$ of such a subgroup $L$ of $G$.

Thus we may as well assume $M = L_{\overline{F}}$ is $\Gamma_{\overline{F}/F}$-stable. Now, $z_X$ gives a cocycle in $Z^1(F, N_G(L)/L)$ via the function $$\sigma \mapsto \bar{\sigma} \mapsto z_{X}(\bar{\sigma}) \hspace{1mm} \text{mod} \hspace{1mm} L(\overline{F}),$$ where $\bar{\sigma}$ is any lift of $\sigma \in \Gamma_{\overline{F}/F}$ to $\mathcal{E}_{\mathop{\mathrm{Kal}}}$ (the cocycle is independent of the lift). By our above argument, we may modify $z_X$ by a coboundary such that this cocycle comes via projection from some $z \in Z^1(F, N_G(L))$. Now, suppose there exists some $h \in G(\overline{F})$ such that $h\nu_Xh^{-1}$ is $\Gamma_{\overline{F}/F}$-fixed. Then we compute this is equivalent to $h^{-1}\gamma(h)z^{-1}_{\gamma} \in L(\overline{F})$ for each $\gamma \in \Gamma_{\overline{F}/F}$. This would certainly follow if we knew that $z_{\gamma}$ came from a class in $H^1(F, N_G(L))$ that is trivial in $H^1(F,G)$. But this latter group is trivial again because $G = \mathrm{GL}_{n}$. ◻
:::

From now on, we assume $\nu_X$ is fixed by $\Gamma_{\overline{F}/F}$.

::: rem
The cohomology set $H_{\text{alg}}^{1}(\mathcal{E}_{\mathop{\mathrm{Kal}}}, G)$ for a connected reductive group $G$ is studied in detail in [@DS24], which excusively works with so-called "regular" classes, which are those arising as the image of $H^{1}_{\text{alg}}(\mathcal{E}_{\mathop{\mathrm{Kal}}}, T)$ for a maximal torus $T$ of $G$. Lemma [\[lemma:reg\]](#lemma:reg){reference-type="ref" reference="lemma:reg"} implies that every class in $[z] \in H_{\text{alg}}^{1}(\mathcal{E}_{\mathop{\mathrm{Kal}}}, \mathrm{GL}_{n})$ is regular, as follows: One combines [@DS24 Lemma 2.8] which says, when $z|_{u}$ is defined over $F$, we have that $z \in Z_{\mathop{\mathrm{bas}}}^{1}(\mathcal{E}_{\mathop{\mathrm{Kal}}}, Z_{G}(z|_{u}))$ with the fact ([@Kalannals Corollary 3.7]) that $H_{\text{alg}}^{1}(\mathcal{E}_{\mathop{\mathrm{Kal}}}, T) \to H_{\mathop{\mathrm{bas}}}^{1}(\mathcal{E}_{\mathop{\mathrm{Kal}}}, M)$ is surjective for any connected reductive group $M$ with elliptic maximal torus $T$.
:::

::: lem
[]{#lem:simple label="lem:simple"} Under the assumption above, suppose $M \subset \mathrm{GL}_n$ is a minimal twisted Levi subgroup through which $z_X$ factors. If $X$ is simple, then $z_X$ is basic in $M$ (in other words, $\nu_X$ factors through $Z(M)$) and $M$ is elliptic. On the other hand, $X$ is simple if and only if $z_X$ factors through only elliptic twisted Levi subgroups of $\mathrm{GL}_{n}$.
:::

::: proof
*Proof.* Suppose $z_X$ is not basic in $M$. Then let $M' \subset M$ be the centralizer of $\nu_X$ in $M$. Since $G=\mathrm{GL}_n$, we claim that $M'$ is a twisted Levi subgroup of $M$ and hence $G$. Indeed, $M'$ is the intersection of centralizers of commuting semisimple elements of $\mathrm{GL}_n$, each of which is a twisted Levi subgroup. Moreover, $M' \subset M$ is proper since $\nu_X$ is not basic. The cocycle $z_X$ factors through $M'$ since $x \in \mathcal{E}_{\mathop{\mathrm{Kal}}}$ lifting $\sigma \in \Gamma_{\overline{F}/F}$ satisfies $\mathop{\mathrm{Int}}(x)(\nu_X) = \mathop{\mathrm{Int}}(x)(\sigma(\nu_X))=\nu_X$, hence $M$ is not minimal.

If $X$ is simple, then $z_X$ cannot factor through any non-elliptic twisted Levi subgroup, since by the above discussion this would imply $z_X$ factors through a Levi subgroup of $G$ and hence is not simple.

For the second part, observe that $X$ is simple if and only if $z_X$ does not factor through a proper Levi subgroup of $G$ and by the discussion before Lemma [\[lem: GLntwistedlevis\]](#lem: GLntwistedlevis){reference-type="ref" reference="lem: GLntwistedlevis"}, this is equivalent to $z_X$ not factoring through any non-elliptic twisted twisted Levi subgroup. ◻
:::
