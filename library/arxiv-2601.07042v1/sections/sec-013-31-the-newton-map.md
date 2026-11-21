---
doc_id: arxiv-2601.07042v1
doc_title: "A Tannakian description of the local Kaletha gerbe"
section_id: sec-013-31-the-newton-map
section_title: "The Newton map"
section_number: 3.1
pages: 17-18
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.834
doc_brief: "A Tannakian description of the local Kaletha gerbe — We construct, for a p-adic field F, an explicit semisimple Tannakian category RigIsocF whose category of fiber functors recovers Kaletha’s Galois"
---
Given an object $X = (V,\tilde{\Phi},\mathcal{D})$ in $R\mathcal{I}_{k}$, one can attach a homomorphism $f_{X} \in \text{Hom}_{\overline{F}}(u_{\overline{F}}, \mathrm{GL}(\omega_{k}(X))$ as follows: The group $\mathrm{Res}_{E_{k}/F}(\mu_{n_{k}})(\overline{F})$ is canonically identified with the group of automorphisms of the $\overline{F}$-fiber functor described in the previous subsection, which we will denote by $\omega_{k}$, and then $f_{X}$ is defined by sending $x \in \mathrm{Res}_{E_{k}/F}(\mu_{n_{k}})$ to the $\overline{F}$-linear automorphism of $\omega_{k}(X)$ corresponding to $x$.

::: lem
The dimension of $\omega_{k}(X)$ is $\sum_{(a_{\sigma}/n_{k}) \in \prod_{\Gamma_{E_{k}/F}}[0,1)} \textnormal{dim}_{L_{E_{k}}}(V_{(a_{\sigma}/n_{k})})$.
:::

::: proof
*Proof.* This follows immediately from the explicit description in [\[keyfiberfunctor\]](#keyfiberfunctor){reference-type="eqref" reference="keyfiberfunctor"} of the functor $\omega_{R\mathcal{I}_{k}}$, noting that all the internal summands in [\[keyfiberfunctor\]](#keyfiberfunctor){reference-type="eqref" reference="keyfiberfunctor"} are identified upon taking the quotient by $IR_{E_{k}/F}$. ◻
:::

It is straightforward to verify that the homomorphisms $f_{X}$ are compatible with the transition maps $R\mathcal{I}_{k} \to R\mathcal{I}_{l}$, and we thus can associate to an object $X$ in $\mathrm{RigIsoc}_{F}$ in the image of $R\mathcal{I}_{k}$ a morphism $f_{X} \in \text{Hom}_{\overline{F}}(u_{\overline{F}}, \mathrm{GL}(\omega_{k}(X)))$.

We say that an object $X$ of $\mathrm{RigIsoc}_{F}$ is *basic* if the homomorphism $f_{X}$ is valued in $Z(\mathrm{GL}(\omega_{k}(X)))$. One can classify the basic objects as follows:

::: prop
[]{#prop:Newton label="prop:Newton"} An object $X$ of $\mathrm{RigIsoc}_{F}$ is basic if and only if all of the indices in $\mathbb{Q}[\Gamma_{\overline{F}/F}]$ of all its nonzero graded pieces have the same image in $\mathbb{Q}/\mathbb{Z}[\Gamma_{\overline{F}/F}]$.
:::

::: proof
*Proof.* It suffices to prove this for the finite-level Tannakian category $R\mathcal{I}_{k}$.

An element $x = (x_{\sigma}) \in  \prod_{\Gamma_{E_{k}/F}} \mu_{n_{k}}(\overline{F}) = \mathrm{Res}_{E_{k}/F}(\mu_{n_{k}})(\overline{F})$ acts on the fiber functor by sending $V_{(a_{\sigma}/n_{k})}$ to itself via multiplication by $\prod_{\sigma}x_{\sigma}^{a_{\sigma}}$. This gives for each graded piece $V_{(a_{\sigma}/n_{k})}$ a morphism from $u_{\overline{F}}$ to $Z(\mathrm{GL}_{V_{(a_{\sigma}/n_{k})}}) = \overline{F}^{\times}$, and the resulting map lies in $Z(\mathrm{GL}(\omega_{k}(X)))$ if and only if these maps agree for all $(a_{\sigma}/n_{k})_{\sigma}$. This last condition holds precisely when all tuples $(a_{\sigma}/n_{k})_{\sigma}$ with $V_{(a_{\sigma}/n_{k})} \neq 0$ are the same modulo $\prod_{\Gamma_{E_{k}/F}}\mathbb{Z}$. ◻
:::

Denote by $\mathrm{RigIsoc}_{F,n}$ the full subcategory of objects whose image under the canonical fiber functor, temporarily denoted by $\omega$, given above (and thus any fiber functor) is $n$-dimensional; we can also consider the full subcategory $\mathrm{RigIsoc}_{F,n,\text{basic}}$ of basic objects. Recall that if $\mathcal{E}_{\text{Kal}}$ is the gerbe of fiber functors for $\mathrm{RigIsoc}_{F}$, then we have an equivalence of categories $$\label{gerbeequiv}
  \mathrm{RigIsoc}_{F,n} \ \xrightarrow{\sim} Z_{\text{alg}}^{1}(\mathcal{E}_{\text{Kal}}, \mathrm{GL}_{n}),$$ and we observe that this functor is compatible with the maps from both objects to $\text{Hom}_{\overline{F}}(u_{\overline{F}},\mathrm{GL}_{n,\overline{F}})$. More explicitly, recall from [@Taibi25 Proposition 7.1] that there is an equivalence of categories from the category of pairs $(R,t)$, where $R \colon \mathcal{E}_{\mathop{\mathrm{Kal}}} \to B\mathrm{GL}_{n}$ is a morphism of fibered categories over $F$ and $t$ is a trivialization of $R(\omega)$, to the category $Z_{\text{alg}}^{1}(\mathcal{E}_{\text{Kal}}, \mathrm{GL}_{n})$. The claimed equivalence [\[gerbeequiv\]](#gerbeequiv){reference-type="eqref" reference="gerbeequiv"} is given by composing this equivalence with the functor sending $X \in \mathop{\mathrm{obj}}(\mathrm{RigIsoc}_{F,n})$ to the pair consisting of the functor $F \mapsto \underline{\text{Isom}}(F(X), \omega(X))$ and the trivialization of $\underline{\text{Isom}}(\omega(X), \omega(X))$ induced by our distinguished basis for the underlying vector space of $X = (V,\mathcal{D}, \Phi)$.

Note that [\[gerbeequiv\]](#gerbeequiv){reference-type="eqref" reference="gerbeequiv"} induces an equivalence of categories $$\mathrm{RigIsoc}_{F,n,\text{basic}} \xrightarrow{\sim} Z_{\mathop{\mathrm{bas}}}^{1}(\mathcal{E}_{\text{Kal}}, \mathrm{GL}_{n}).$$

::: cor
When $X \in \mathop{\mathrm{obj}}(\mathrm{RigIsoc}_{F})$ is basic, the morphism $f_{X} \in \textnormal{Hom}_{\overline{F}}(u_{\overline{F}}, \mathrm{GL}(\omega_{k}(X)))$ descends to a morphism in $\textnormal{Hom}_{F}(u, \mathrm{GL}(\omega_{k}(X))).$
:::

This result can also be verified directly using the explicit description of $f_{X}$ given above.
