---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-033-92-the-birkhoff-guenther-normal-form
section_title: "The Birkhoff-Guenther normal form"
section_number: 9.2
pages: 45-47
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.947
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:BGNF label="subsection:BGNF"}

Going from two slopes to general case rests on the following remark. The functor $M \leadsto M' := M_{\leq \mu_{k-1}}$ induces an onto mapping ${\mathcal{F}}(P_{1},\ldots,P_{k}) \rightarrow {\mathcal{F}}(P_{1},\ldots,P_{k-1})$. The inverse image in ${\mathcal{F}}(P_{1},\ldots,P_{k})$ of the class of $M'$ in ${\mathcal{F}}(P_{1},\ldots,P_{k-1})$ is in natural one-to-one correspondance with the space $\text{Ext}^{1}(P_{k},M')$. The latter is a ${\mathbf C}$-vector space of dimension $\sum\limits_{1 \leq j < k} r_{j} r_{k} (\mu_{k} - \mu_{j})$. This follows from the slope filtration $0 = M_{0} \subset \cdots \subset M_{k-1} = M'$ and the resulting exact sequences, for $1 \leq j < k$: $$0 \rightarrow M_{j-1} \rightarrow M_{j} \rightarrow P_{j} \rightarrow 0
\Longrightarrow$$ $$0 \rightarrow \text{Ext}^{1}(P_{k},M_{j-1}) \rightarrow \text{Ext}^{1}(P_{k},M_{j}) 
\rightarrow \text{Ext}^{1}(P_{k},P_{j}) \rightarrow 0.$$ (Recall that $\text{Hom}(P_{k},P_{j}) = 0$.) Actually, there is a non canonical ${\mathbf C}$-linear isomorphism $\text{Ext}^{1}(P_{k},M') \simeq \bigoplus_{1 \leq j < k} \text{Ext}^{1}(P_{k},P_{j})$. One can go further using the matricial description of paragraph [\[subsection:matricialdescriptionofF(P1,\...,Pk)\]](#subsection:matricialdescriptionofF(P1,...,Pk)){reference-type="ref" reference="subsection:matricialdescriptionofF(P1,...,Pk)"}. We keep the notations recalled at the beginning of subsection [\[subsection:twointegralslopes\]](#subsection:twointegralslopes){reference-type="ref" reference="subsection:twointegralslopes"} and moreover denote []{#not40 label="not40"} $\overline{M_{U}}$ the class in ${\mathcal{F}}(P_{1},\ldots,P_{k})$ of the module $M_{U} := (K^{n},\Phi_{A_{U}})$ for $U := (U_{i,j})_{1 \leq i < j \leq k} \in 
\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$.

::: prop
[]{#prop:kintegralslopesspace label="prop:kintegralslopesspace"} The map $U \mapsto \overline{M_{U}}$ from $\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j} })$ to ${\mathcal{F}}(P_{1},\ldots,P_{k})$ is one-to-one.
:::

::: proof
*Proof.* We already now that the map is onto and the conclusion will follow from the following fact: for all $U \in \prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$, there exists a unique pair $(F,V) \in {\mathfrak{G}}({{\mathbf C}(\{z\})}) \times 
\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j}})$ such that $F[A_{V}] = A_{U}$. Writing $F$ as in equation ([\[eqn:isoplat\]](#eqn:isoplat){reference-type="ref" reference="eqn:isoplat"}) and $V = (V_{i,j})$, this is equivalent to the following system: $$\forall (i,j), 1 \leq i < j \leq k ~,~
V_{i,j} + \sum_{\ell = i+1}^{j-1} (\sigma_qF_{i,\ell}) V_{\ell,j} + 
(\sigma_qF_{i,j}) (z^{\mu_{j}} A_{j}) =
(z^{\mu_{i}} A_{i}) F_{i,j} + \sum_{\ell = i+1}^{j-1} U_{i,\ell} F_{\ell,j} + U_{i,j}.$$ It is understood that an empty sum vanishes: if $(t_{\ell})$ is any sequence, $\sum\limits_{\ell = i+1}^{j-1} t_{\ell} = 0$ when $j = i+1$. Then, $U$ being given, the system is (uniquely) solved by induction on $j - i$ by the following formulas: $$(F_{i,j},V_{i,j}) := Red\left(\mu_{i},A_{i},\mu_{j},A_{j},U_{i,j} +
\sum_{\ell = i+1}^{j-1} U_{i,\ell} F_{\ell,j} - 
\sum_{\ell = i+1}^{j-1} (\sigma_qF_{i,\ell}) V_{\ell,j}\right).$$ ◻
:::

The following is a particular case of theorem [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"}, page (itself a particular case of corollary [\[coro:themodulispaceabstract\]](#coro:themodulispaceabstract){reference-type="ref" reference="coro:themodulispaceabstract"}, page ): the only novelty being that, in the case of integral slopes, we obtain an explicit coordinate system.

::: theo
[]{#theo:kintegralslopesspace label="theo:kintegralslopesspace"} The set ${\mathcal{F}}(P_{1},\ldots,P_{k})$ is an affine space of dimension $\sum\limits_{1 \leq i < j \leq k} r_{i} r_{j} (\mu_{j} - \mu_{i})$.
:::

::: proof
*Proof.* This is an immediate consequence of the proposition. ◻
:::

Note that this is the area contained in the lower finite part of the Newton polygon. This result is the natural continuation of a normalisation process found by Birkhoff and Guenther in [@Birkhoff3].

::: defi
[]{#defi:BirkhoffGuenthernormalform label="defi:BirkhoffGuenthernormalform"} A matrix $A_{U}$ such that $U := (U_{i,j})_{1 \leq i < j \leq k} \in 
\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j} })$ will be said to be in *Birkhoff-Guenther normal form*.
:::

Now, using the argument that follows theorem [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"}, we draw from corollary [\[coro:themodulispaceabstract\]](#coro:themodulispaceabstract){reference-type="ref" reference="coro:themodulispaceabstract"}:

::: coro
[]{#coro:schemadesmodules label="coro:schemadesmodules"} The components of the matrices $(U_{i,j})_{1 \leq i < j \leq k}$ make up a complete system of coordinates on the space ${\mathcal{F}}(P_{1},\ldots,P_{k})$.
:::

A generalisation of Birkhoff-Guenther normal form to the case of arbitrary slopes has recently been obtained by Virginie Bugeaud [@VB].
