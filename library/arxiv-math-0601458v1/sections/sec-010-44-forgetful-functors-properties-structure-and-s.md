---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-010-44-forgetful-functors-properties-structure-and-s
section_title: "Forgetful Functors: Properties, Structure, and Stuff"
section_number: 4.4
pages: 27-30
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.972
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
Here we take a detour through some ideas from category theory which apply directly to stuff types. The first is a classification of functors by degrees of forgetfulness, which is the source of the term "stuff" in "stuff type". In fact, we want to explain the terms "structure" and "stuff" which appear before the word "type" in our terminology. We began by trying to categorify a certain rigs, replacing it by a 2-rig of functors - and now we look at a classification of functors to see how we generalized this process. In particular, we are interested in functors which are, respectively: faithful; full and faithful; or full and faithful and essentially surjective:

::: definition
A functor $F : \mathcal{C} \rightarrow \mathcal{D}$ is ***essentially surjective*** if the images of objects in $\mathcal{C}$ cover all objects of $\mathcal{D}$ in the sense that for any $d \in \operatorname{Ob} ( \mathcal{D} )$, there is some $c \in
  \mathcal{C}$ with $F(c) \cong d$. It is ***full*** if for any $c, c' \in \mathcal{C}$, the map between the sets of morphisms, $F : \operatorname{Hom}_{\mathcal{C}} ( c, c' ) \rightarrow
  \operatorname{Hom}_{\mathcal{D}} (F(c), F(c'))$, is surjective (in the set-theoretic sense). The functor $F$ is ***faithful*** if for morphisms in its image, $F(f), F(f') \in
  \operatorname{Hom}_{\mathcal{D}} (F(c), F(c'))$, we have $F(f) = F(f')
  \Rightarrow f = f' \operatorname{in} \operatorname{Hom}_{\mathcal{C}} (c,c')$.
:::

Each of these can be seen as a form of surjectivity. The notion of essential surjectivity is a version of *onto* for categories at the level of objects. Fullness means that a functor is "*onto* for morphisms"; faithfulness is "*onto* for equations between morphisms" in the sense that any equation between morphisms in $\operatorname{Hom}_{\mathcal{D}} ( F ( c ), F
( c' ) )$ comes from some equation between the preimage morphisms in $\operatorname{Hom}_{\mathcal{C}} ( c, c' )$.

We have a classification of functors, then, by which of these it satisfies (which we will attempt to explain next):

::: center
                **Functor**                 **Forgets**
  ---------------------------------------- --------------
   essentially surjective, full, faithful    "nothing"
               full, faithful               "properties"
                  faithful                  "structure"
                    all                       "stuff"
:::

When we move to the setting of $n$-categories, we have not only objects and morphisms, and the possibility that morphisms may be equal, but also 2-morphisms between morphisms (so that they may be 2-isomorphic, rather than merely equal, or indeed might have non-iso 2-morphisms between them), and 3-morphisms between 2-morphisms, and so on. Important to notice is that essential surjectivity involves a weakening (a functor is essentially surjective if it is surjective onto isomorphism classes, but not necessarily objects). This is because we should not distinguish between equivalent categories, and since every category is equivalent to a skeletal category with only one object in each equivalence class. We will, in fact, want similarly weakened versions of *full*, *faithful*, and their higher-dimensional counterparts, when we use $n$-categories.

For now, though, we will explain the second column of this table, and see how it applies to structure types. The intuition begins with the commonplace fact that a map between sets is an isomorphism if it is both injective and surjective. For functors between categories, essential surjectivity is the natural analog of surjectivity, but *full* functors are the natural analogs of injective maps. A map is injective if no two distinct objects have the same image - that is, any equation of objects in the image comes from an equation in the domain. A functor is full if every morphism between objects in the image comes from a morphism in the domain, so injectivity of set maps is a special case, considering a set as a category with only identity morphisms. In this trivial sort of category, every functor is faithful.

So a bijection between sets is a full, faithful, essentially surjective functor, and if such a functor exists, we should treat the sets as "the same" - the functor has lost no important information (of which there is very little, for a set), which is reflected in the fact that it is invertible. If we have more general categories, with nontrivial morphisms, then in much the same way, we have that a functor $F : \mathcal{C \rightarrow \text{D}}$, is an equivalence of $\mathcal{C}$ and $\mathcal{D}$ (i.e. there is a functor $F^{-
1}$ which is an inverse to $F$ up to natural isomorphism) if $F$ is full, faithful, and essentially surjective. Similar results are true for higher-dimensional categories ($n$-categories, for any $n$), while functors which fail to have these properties are in various senses "forgetful" - not being equivalences, they must forget information about the source category. This gives a "periodic table" of grades of "stuff" forgotten by functors which fail to be onto for objects, morphisms, 2-morphisms (between morphisms), 3-morphisms (between 2-morphisms), and so on. We restrict our attention to the case $n = 1$, but note that the pattern we will develop continues for higher $n$.

We see that these classes of functor can be used to talk about classes of "type": structure types and stuff types are functors from groupoids into the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$ - in fact, they are functors which forget "structure" and "stuff" respectively.

### Examples of Forgetful Functors

Some examples illustrate the classes of functors we have described. So for instance, if a functor $F : \mathcal{C} \rightarrow \mathcal{D}$ is not essentially surjective, but is full and faithful, we have a subcategory of $\mathcal{C}$ in $\mathcal{D}$, namely the image of $F$, which is equivalent to $\mathcal{C}$, but which does not exhaust the isomorphism classes of $\mathcal{D}$:

::: example
The functor $$I : \boldsymbol{\operatorname{{AbGrp}}} \rightarrow \boldsymbol{\operatorname{{Grp}}}$$ embeds the category of abelian groups and their homomorphisms into the category of all groups and homomorphisms. This functor has "forgotten a property", namely the property of being Abelian. The category $\boldsymbol{\operatorname{{Grp}}}$ does not discriminate between objects with and without this property, whereas $\boldsymbol{\operatorname{{AbGrp}}}$ is distinguished by the fact that it does.
:::

If a functor fails to be essentially surjective *and* fails to be full, we can have not only the sort of situation above, but the target category can have morphisms which do not correspond to those in the source:

::: example
The functor $$I : \boldsymbol{\operatorname{{OrdFinSet_0}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$$ takes any element in the groupoid $\boldsymbol{\operatorname{{OrdFinSet_0}}}$ of totally ordered finite sets (whose morphisms are order-preserving bijections) into $\boldsymbol{\operatorname{{FinSet_0}}}$ - taking ordered sets and order-preserving maps to the underlying sets and set-maps. This fails to be full since there can be bijections between the underlying sets of two ordered sets which fail to preserve order. This functor "forgets structure" - namely, that structure which must be preserved by morphisms in $\boldsymbol{\operatorname{{OrdFinSet_0}}}$, the total ordering on its objects.
:::

Both of these examples are faithful functors, in the sense that each morphism in the source category is sent to a distinct morphism in the target. There are functors which lack this property as well:

::: example
Consider the functor: $$P_1 : \boldsymbol{\operatorname{{Vect^2}}} \rightarrow
  \boldsymbol{\operatorname{{Vect}}}$$ The objects and morphisms in $\boldsymbol{\operatorname{{Vect^2}}}$ are ordered pairs of those in $\boldsymbol{\operatorname{{Vect}}}$, namely vector spaces and linear transformations between them, while the functor $P_1$ is just projection onto the first component of these pairs. Clearly, this is not faithful, since there are many pairs morphisms in $\boldsymbol{\operatorname{{Vect^2}}}$ with the same first component. What this functor has "forgotten" is, for each object, an entire vector space, and all the information about morphisms associated to these. More than simply forgetting about properties shared by all objects, or structure which must be preserved by morphisms, we say this functor forgets "stuff" - parts of objects, in this case.
:::

::: example
[]{#st-ex:tuple label="st-ex:tuple"}Our previous example of a completely forgetful functor involved the category of vector spaces, but similarly, there is an obvious class of stuff types associated to the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}^n$, whose objects and morphisms are $n$-tuples of finite sets and bijections: $$P_j : \boldsymbol{\operatorname{{FinSet_0}}}^n \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$$ where $P_j$ is the projection onto the $j^{\operatorname{th}}$ coordinate. The set in this entry is the "underlying set", and the "stuff" being forgotten consists of all the other sets in the tuple. This stuff type is a completely forgetful functor.
:::
