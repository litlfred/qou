---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-004-4-kv-2-vector-spaces-and-finite-groupoids
section_title: "KV 2-Vector Spaces and Finite Groupoids"
section_number: 4
pages: 15-16
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.977
---
[]{#sec:kv2vsgrpd label="sec:kv2vsgrpd"}

We have now seen that we can get a 2-vector space as a category of functions from some finite set $S$ into $\boldsymbol{\operatorname{{Vect}}}$, and this may have extra structure if $S$ does. However, this is somewhat unnatural, since $\boldsymbol{\operatorname{{Vect}}}$ is a category and $S$ a mere set. It seems more natural to consider functor categories into $\boldsymbol{\operatorname{{Vect}}}$ from some category $\boldsymbol{\operatorname{{C}}}$. These are examples of the generalized 2-vector spaces described by Elgueta [@elgueta]. Then the above way of looking at a KV 2-vector space can be reduced to the situation when $\boldsymbol{\operatorname{{C}}}$ is a discrete category with a finite set of objects. However, there are interesting cases where $\boldsymbol{\operatorname{{C}}}$ is not of this form, and the result is still a KV vector space. A relevant class of examples, as we shall show, come from special kinds of groupoids.

## Free 2-Vector Space on a Finite Groupoid

Since we want our 2-vector spaces to have finitely many generators, we need a condition on the sorts of groupoids we are talking about here. Of course, since often one works with topological groupoids which may be uncountable, the kind of finiteness condition we will have to apply seems restrictive. A full treatment of, for example, Lie groupoids, would require much more consideration of infinite dimensional 2-vector spaces (and indeed 2-Hilbert spaces). In the meantime, we can only consider groupoids which are essentially finite.

We first show that essentially finite groupoids are among the special categories $\boldsymbol{\operatorname{{C}}}$ we want to consider:

::: lemma
[]{#lemma:fgkv label="lemma:fgkv"} If $X$ is an essentially finite groupoid, $\boldsymbol{\operatorname{{Rep(X)}}} = [\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$ is a 2-vector space
:::

::: proof
*Proof.* The groupoid $\boldsymbol{\operatorname{{X}}}$ is equivalent its skeleton, $\underline{\boldsymbol{\operatorname{{X}}}}$, which contains a single object in each isomorphism class. Since $\boldsymbol{\operatorname{{X}}}$ is essentially finite, this is a finite set of objects, and each object has a finite group of endomorphisms. So $$X \simeq \coprod_{x \in \underline{\boldsymbol{\operatorname{{X}}}}} Aut(x)$$ where the groups $Aut(x)$ are seen as one-object groupoids.

Then $$\begin{aligned}
& \simeq \prod_{x \in \underline{\boldsymbol{\operatorname{{X}}}}} [Aut(x),\boldsymbol{\operatorname{{Vect}}}] \\
 & = \prod_{x \in \underline{X}} Rep(Aut(x))
\end{aligned}$$

This inherits the biproducts from the categories $Rep(Aut(x))$. An irreducible representation of an essentially finite groupoid amounts to a choice of isomorphism class of objects $[x]$, and an irreducible representation of the group $Aut(x)$. By Schur's Lemma, these are indeed simple objects, since irreducible representations of a group are simple. ◻
:::

We notice that we are speaking here of groupoids, and any groupoid $\boldsymbol{\operatorname{{X}}}$ is equivalent to its opposite category $\boldsymbol{\operatorname{{X}}}^{op}$, by an equivalence that leaves objects intact and replaces each morphism by its inverse. So there is no real difference between $[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$, the category of $\boldsymbol{\operatorname{{Vect}}}$-valued functors from $\boldsymbol{\operatorname{{X}}}$, and $[\boldsymbol{\operatorname{{X}}}^{op},\boldsymbol{\operatorname{{Vect}}}]$, the category of *$\boldsymbol{\operatorname{{Vect}}}$-valued presheaves* (or just "$\boldsymbol{\operatorname{{Vect}}}$-presheaves") on $\boldsymbol{\operatorname{{X}}}$. (We also should note that, since our groupoids are discrete, there is no distinction here between sheaves and presheaves).

Figure [1](#fig:vectpresheaf){reference-type="ref" reference="fig:vectpresheaf"} is an illustration of an object in $[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$.

<figure id="fig:vectpresheaf">
<div class="center">
<embed src="vectpresheaf.eps" />
</div>
<figcaption><span id="fig:vectpresheaf" label="fig:vectpresheaf"></span>A <span class="math inline"><strong>Vect</strong> </span>-valued Presheaf on <span class="math inline"><em>X</em></span></figcaption>
</figure>

We will use the terminology of "presheaves" for objects of $[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$ for the sake of highlighting the connection between these results and the usual facts about presheaves of sets in topos theory - which again raises questions about topologically interesting groupoids. This will be addressed in later work, but for now we consider the algebraic aspect of the 2-linearization construction by itself.
