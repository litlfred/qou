---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-006-4-stuff-types
section_title: "Stuff Types"
section_number: 4
pages: 14-14
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.99
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
[]{#stuff-types-sec label="stuff-types-sec"}

We have described a structure type as a functor $F \in \boldsymbol{\operatorname{{Set [ Z ]}}}$, where the image of each finite set $S$ is the set of structures "of type $F$" which can be put on $S$, but it should be obvious that the category $\boldsymbol{\operatorname{{Set}}}$ is rather larger than we need, since for most sorts of structures we can think of, almost all sets will not appear in the image at all - most are not sets of $F$ structures on an $n$-element set for any $F$ or $n$. If we think of a category $\boldsymbol{\operatorname{{X}}}$ whose objects are precisely the structures of type $F$, and whose morphisms are those maps which arise from bijections of the underlying sets, we have a category better suited to $F$. This category is, in fact, a groupoid (i.e. a category in which all morphisms are iso), since $\boldsymbol{\operatorname{{FinSet_0}}}$ is.

If we do this, however, we now have not sets of $F$ structures as objects, but $F$-structures themselves, and there are many such structures corresponding to each $n$. So now it is more natural to think of $F$ as a functor: $$F : \boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$$ where each object of $\boldsymbol{\operatorname{{X}}}$ is taken to its underlying set, and each morphism to the underlying bijection of sets. So every morphism in the image, $\text{$\boldsymbol{\operatorname{{FinSet_0}}}$}$, then comes from morphisms in $\boldsymbol{\operatorname{{X}}}$ under this $F$. A functor with this property is called **faithful**.

Why should we make this changed to the definition of a structure type? There are at least two good reasons to take this approach. One is that, while the previous definition fit well with the view of formal power series in which we are interested in finding the coefficient of the $n^{\operatorname{th}}$ power of $z$, this definition allows us to think of $F$ as corresponding to a power series which we evaluate at various (positive) real numbers to get other (positive) real numbers. To see how this works, we first remark that it will make sense to think of a structure type $F$ being evaluated at a *groupoid*, and so we need some useful facts about these.
