---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-004-5-tilting-modules-in-the-modular-case
section_title: "Tilting modules in the modular case"
section_number: 5
pages: 13-16
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.896
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick ideals."
---
[]{#tilting-modular label="tilting-modular"}

We recall some statements about tilting modules over a field $\Bbbk$ and a complete discrete valuation ring $R$.

## Weights

Let $\Bbbk$ be a field of characteristic $p > 0$ and $G$ a semisimple, simply connected algebraic group over $\Bbbk$. We denote by $Rep(G)$ the category of finite dimensional representations. We fix a maximal torus $T$ and a Borel subgroup $B$. We denote by $R$ the set of roots and by $R^+$ the set of positive roots. The dominant integral weights are $$X(T)^+ = \{ \lambda \in X(T) \ | \ <\lambda, \alpha^{\vee}> \geq 0\quad \forall \alpha \in R^+ \}.$$

## Induced modules and Weyl modules

The induction functor from $B$ to $G$ is not exact. For any $B$-module $M$ we put $$H^i(M) = R^i Ind_B^G M, \ i \in \mathbb{N}$$ and also abbreviate $$H^i(\lambda) = H^i (k_{\lambda})$$ where $\Bbbk_{\lambda}$ stands for $\Bbbk$ regarded as a $B$-module via $\lambda \in X(T)$. All these $H^i(\lambda)$ are finite dimensional over $\Bbbk$ [@Jantzen I.5.12.c]. The following properties are well-known:

1.  For $\lambda \in X(T)^+$ we have $H^0(\lambda) \neq 0$.

2.  If $\lambda \in X(T)^+$, then $soc(H^0(\lambda)) =: L(\lambda)$ is simple, and any finite dimensional simple $G$-module is isomorphic to exactly one $L(\lambda)$.

3.  $L(\lambda)^* \cong L(-w_0 \lambda)$ where $w_0$ is the longest element of the Weyl group $W$.

4.  $End_G(H^0(\lambda)) \cong \Bbbk \cong End_G L(\lambda)$.

5.  $H^i(\lambda) = 0$ for $i > 0$ and $\lambda \in X(T)^+$ (Kempf vanishing).

We define $V(\lambda) := H^0(-w_0 \lambda)^*$. We call $H^0(\lambda)$ the induced module and $V(\lambda)$ the Weyl module. A $G$-module $V$ has a good filtration if there is an ascending chain $$0 = V_0 \subset V_1 \subset \ldots$$ such that $V = \bigcup_i V_i$ and $V_i/V_{i-1} \cong H^0(\lambda_i)$ for some $\lambda_i \in X(T)^+$. Likewise we say it has a Weyl filtration if $V_i/V_{i-1} \cong V(\lambda_i)$ for some $\lambda_i \in X(T)^+$. Then

1.  $V$ admits a good filtration iff $Ext^1_G(V(\lambda),V) = 0 \ \forall \lambda \in X(T)^+$.

2.  $V$ admits a Weyl filtration iff $Ext^1_G(V,H^0(\lambda)) = 0 \ \forall \lambda \in X(T)^+$.

3.  $V$ has a Weyl filtration iff $V^*$ has a good filtration.

4.  The tensor product of two modules with a good filtration has again a good filtration.

## Tilting modules over $\Bbbk$

A finite dimensional $G$-module is called a tilting module if it has a Weyl filtration and a good filtration. We denote by $Tilt(G,k)$ the full subcategory of tilting modules where $\Bbbk$ is a field of characteristic $p > 0$. The direct sum and the tensor product of two tilting modules is tilting. If $V_1,V_2$ are tilting modules, then $Ext^1_G(V_1,V_2) = 0 \ \forall i> 0$.

::: proposition
[@Jantzen Lemma E.6] []{#prop:tilting-ind label="prop:tilting-ind"} For each $\lambda \in X^+$ there exists a unique indecomposable tilting module $T(\lambda)$ such that the weight space $T(\lambda)_{\lambda}$ is free of rank 1 over $\Bbbk$ and such that $T(\lambda)_{\mu} \neq 0$ implies $\mu \leq \lambda$. Every tilting module can be written in a unique way as a direct sum of these $T(\lambda)$.
:::

## Tilting modules over discrete valuation rings

The entire theory of tilting modules can be developed over more general rings. We assume now that $R$ is a complete discrete valuation ring.

For a split reductive group $G$ over ${\mathbb Z}$ we denote by $G_R$ the group over $R$ obtained by extension of scalars to $R$ (but we may omit the subscript if there is no risk of confusion). As for $R = k$, one defines $$H^i_R(M) = R^i Ind_{B_R}^{G_R} (M), \ H^i_R(\lambda) = H^i_R(R_{\lambda}).$$ We denote by $V(\lambda)_{{\mathbb Z}}$ the ${\mathbb Z}$-form of the irreducible $G_{{\mathbb Q}}$-module $V(\lambda)$, $\lambda \in X(T)^+$ as in [@Jantzen II.8.3] and put $$V(\lambda)_R = V(\lambda)_{{\mathbb Z}} \otimes_{{\mathbb Z}} R.$$ By [@Jantzen II.8.8, II.8.9] $H^0_R(\lambda) \cong H^0_{{\mathbb Z}}(\lambda) \otimes_{{\mathbb Z}} R$, $H^i(\lambda) = 0$ for all $i>0$ and $V(\lambda)_R \cong H^0_R (-w_0\lambda)^{\vee}$. The analogue of Kempf's vanishing theorem permits to develop the theory of good filtrations and Weyl filtrations also over $R$.

::: lemma
[]{#lem:tilting label="lem:tilting"} [@Jantzen Lemma B.9, B.10] Suppose $R$ is a complete discrete valuation ring. Let $M$ be a $G$-module that is free of finite rank over $R$. Then [\[GF-1\]](#GF-1){reference-type="ref" reference="GF-1"} - [\[GF-3\]](#GF-3){reference-type="ref" reference="GF-3"} are equivalent and [\[GF-4\]](#GF-4){reference-type="ref" reference="GF-4"} - [\[GF-6\]](#GF-6){reference-type="ref" reference="GF-6"} are equivalent.

1.  []{#GF-1 label="GF-1"} $M$ has a good filtration.

2.  []{#GF-2 label="GF-2"} $Ext^1_G(V(\lambda)_R,M) = 0 \ \forall \lambda \in X(T)^+$.

3.  []{#GF-3 label="GF-3"} For each maximal $\mathfrak{m}$ in $R$ the $G_{R/\mathfrak{m}}$-module $M \otimes R/\mathfrak{m}$ has a good filtration.

4.  []{#GF-4 label="GF-4"} $M$ has a Weyl filtration.

5.  []{#GF-5 label="GF-5"} $Ext^1_G(M,H^0_R(\lambda)) = 0 \ \forall \lambda \in X(T)^+$.

6.  []{#GF-6 label="GF-6"} For each maximal $\mathfrak{m}$ in $R$ the $G_{R/\mathfrak{m}}$-module $M \otimes R/\mathfrak{m}$ has a Weyl filtration.
:::

Note that if a $G$-module $M$ has a good filtration, then $M$ is free over $R$ (since all $H^0(\mu)$ are so) and for each $R$-algebra $R'$ the $G_{R'}$-module $M \otimes R'$ has a good filtration since $H^0(\mu) \otimes R' \cong H_{R'}^0(\mu)$ [@Jantzen 8.8(1)]. Furthermore $V(\lambda) \otimes R/\mathfrak{m} \cong V(\lambda)_{R/\mathfrak{m}}$ [@Jantzen 8.3].

In particular we can define tilting modules for $G_R$. Any tilting module for $G_R$ is free of finite rank over $R$.

::: lemma
[@Jantzen Lemma E.19, Proposition E.22] Suppose that $R$ is a complete discrete valuation ring. For each $\lambda \in X^+$ there exists a unique indecomposable tilting module $T_R(\lambda)$ such that the weight space $T_R(\lambda)_{\lambda}$ is free of rank 1 over $R$ and such that $T_R(\mu)_{(\mu)} \neq 0$ implies $\mu \leq \lambda$. Every tilting module can be written in a unique way as a direct sum of these $T_R(\lambda)$.
:::

::: remark
The existence of the $T(\lambda)$ with the correct properties works in greater generality (for instance if $R$ is a Dedekind ring which is a principal ideal domain, see [@Jantzen Section E]). While any tilting module for such $R$ can be decomposed into a direct sum of indecomposable tilting modules, their decomposition will in general not be unique.
:::

## Extension of scalars for tilting modules

By [@Jantzen E.20] $M$ is an indecomposable $G_R$-module if and only if $End_{G_R}(M)$ is a local ring. We have $$End_{G_R}(T(\lambda)) = R id_{T_R(\lambda)} + rad \ End_{T_R(\lambda)} (T_R(\lambda)),$$ where $$rad \ End_{G_R} (T_R(\lambda)) = \{ \varphi \in End_{G_R} (T_R(\lambda)) \ | \ \varphi((T_R(\lambda)_{\lambda}) \subset \mathfrak{m} (T_R(\lambda))_{\lambda}  \}.$$ Furthermore $$End_{G_{R/\mathfrak{m}}} (T_R(\lambda)) \otimes_R R/\mathfrak{m}) \cong End_{G_R} (T_R(\lambda)) \otimes_R R/\mathfrak{m}.$$ From this one concludes that $End_{G_{R/\mathfrak{m}}}(T_R(\lambda)) \otimes_R R/\mathfrak{m})$ is a local ring and that therefore $T_R(\lambda) \otimes R/\mathfrak{m}$ is indecomposable.

::: corollary
[@Jantzen E.20] We have $$T_R(\lambda) \otimes R/\mathfrak{m}  \cong T_{R/\mathfrak{m}} (\lambda).$$
:::
