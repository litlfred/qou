---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-020-72-other-generalizations
section_title: "Other Generalizations"
section_number: 7.2
pages: 58-60
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.822
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
### Higher-Valence Stuff Operators

We have described stuff types and operators in terms of quantum mechanics, but it should be clear that they also have an independent interest as algebraic objects in their own right. Stuff types form a categorified Hilbert space, but also a categorified algebra, since they have a concept of multiplication in the space.

The key fact behind our approach has been that stuff types and stuff operators form 2-categories of groupoids over either one or two copies of $\boldsymbol{\operatorname{{FinSet_0}}}$. Stuff operators have an action which are the equivalent of linear operators on this 2-Hilbert space. This action arises because of the fact that taking a pullback over one copy of $\boldsymbol{\operatorname{{FinSet_0}}}$ under both a stuff type and an operator removes two of the maps to this underlying $\boldsymbol{\operatorname{{FinSet_0}}}$, and gives an object with one such map.

In fact, there is no reason why we must restrict ourselves to groupoids with either one or two maps to $\boldsymbol{\operatorname{{FinSet_0}}}$ - the categorified versions of vectors or matrices. We have done so because these are the most directly relevant to quantum mechanics, but for categorified algebra, it makes sense to generalize to look at the equivalent of "$p$-forms", or "$p$-index tensors" (the natural inner product obscures the difference between vectors and covectors in this setting). These would be groupoids with projections into $p$ copies of $\boldsymbol{\operatorname{{FinSet_0}}}$. Contraction of two tensors over some pair of indices would amount to identifying the corresponding copies of $\boldsymbol{\operatorname{{FinSet_0}}}$ and taking a pullback of the two projections into this copy.

The categorified $p$-forms could be seen as $p$-sort types: types of structure (or stuff) which could be put on $p$ underlying sets of different "sorts" of objects.

The notion of a *club* described by Max Kelly in [@kelly] can be seen as a significant generalization of this setup, where the categories involved need not be groupoids. There is a body of results about these which may bear on the ideas above, and turn out to be relevant to other physical situations.

### Multisort Species and QFT

In appendix [\[generalspecies\]](#generalspecies){reference-type="ref" reference="generalspecies"} we refer to a description of generalized species as functor categories between $! \mathbbm{G}$ and $\widehat{\mathbbm{H}}$ for groupoids $\mathbbm{G}$ and $\mathbbm{H}$. These "species" are the "structure types" of our terminology, which correspond to the case where both groupoids are $\boldsymbol{1}$, the one-element groupoid, in which case $!\boldsymbol{1}= \boldsymbol{\operatorname{{FinSet_0}}}$ and $\hat{\boldsymbol{1}} = \boldsymbol{\operatorname{{Set}}}$. These correspond to functors from finite sets to sets of structures which can be put on them. We also mentioned the 2-rig $\widehat{!\boldsymbol{n}}$, a.k.a $\boldsymbol{\operatorname{{Set [
Z_1, \ldots, Z_n ]}}}$, the 2-rig of $n$-sort structure types: these correspond to functors from collections finite sets of $n$ "sorts" (i.e. $n$ copies of $\boldsymbol{\operatorname{{FinSet_0}}}$) to sets of structures which can be put on these.

We could reverse this point of view in the case of structure types, to view them as faithful functors from groupoids of structures into the groupoid of finite sets (giving the "underlying" set of a structure) and then weaken the requirement that the functor be faithful to get the more general "stuff types", so too we can reverse our point of view of multisort structure types, to view them as faithful functors from a groupoid of "$n$-sort structures" down to $\boldsymbol{\operatorname{{FinSet_0}}}^n$, giving the $n$ underlying sets of each sort. These functors will be faithful for the same reason as in the case $n = 1$. Weakening this requirement would give us a notion of stuff type corresponding to functions of more than one variable. Defining creation and annihilation operators on each sort of element would let us define a Weyl algebra for $n$ sorts of particles - that is, the algebra of operators for $n$ quantum harmonic oscillators. This is interesting, since a quantum field theory may be represented as a collection of harmonic oscillators.

Replacing the various sorts of finite sets with finite sets over monoids - in particular, over $U(1)$, as in our discussion of $U(1)$-stuff types - we may find an elementary categorical description of a simple QFT. Further research in this direction may prove fruitful.

### Beyond $\boldsymbol{\operatorname{{FinSet_0}}}$

We have described the 2-Hilbert space of categorified states (stuff types) and 2-algebra of operators (stuff operators) for the categorified quantum harmonic oscillator in terms of some over categories. The 2-category $\boldsymbol{\operatorname{{StuffTypes}}}$ is the slice category of $\boldsymbol{\operatorname{{Gpd}}}$ over the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$, while the 2-category $\boldsymbol{\operatorname{{StuffOps}}}$ is the slice category of $\boldsymbol{\operatorname{{Gpd}}}$ over $\boldsymbol{\operatorname{{FinSet_0}}}^2$.

The groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$ appears in both of these cases, in the fact that it does allows stuff operators to act on stuff types by means of pullbacks. But the 2-Hilbert space structure of $\boldsymbol{\operatorname{{StuffTypes}}}$ does not depend on the fact that the groupoid it lies over is $\boldsymbol{\operatorname{{FinSet_0}}}$: the linear structure is inherited entirely from the direct sums of groupoids, and the inner product depends only on the fact that any two stuff types $\Psi$ and $\Phi$ are groupoids over the *same* groupoid $\boldsymbol{\operatorname{{G}}}$, and thus that we can find a groupoid $\left\langle{\Psi,\Phi}\right\rangle$ by taking a weak pullback over $\boldsymbol{\operatorname{{G}}}$.

Similarly, the algebraic properties of $\boldsymbol{\operatorname{{StuffOps}}}$ - its linear structure, composition, and action on $\boldsymbol{\operatorname{{StuffTypes}}}$ - derive from $\boldsymbol{\operatorname{{Gpd}}}$ and the possibility of forming pullbacks. We could derive the same structures for the 2-category of groupoids over $\boldsymbol{\operatorname{{G}}}^2$ for any groupoid $\boldsymbol{\operatorname{{G}}}$. What's more, just as not all matrices need to be square, and linear transformations needn't be endofunctions on some single vectorspace, we could take two different groupoids $\boldsymbol{\operatorname{{G}}}$ and $\boldsymbol{\operatorname{{G'}}}$, and take the 2-category of groupoids over $\boldsymbol{\operatorname{{G}}} \times \boldsymbol{\operatorname{{G'}}}$. We could compose these in the obvious way, treating them as "spans" between $\boldsymbol{\operatorname{{G}}}$ and $\boldsymbol{\operatorname{{G'}}}$ - and also as functors between categories of groupoids over $\boldsymbol{\operatorname{{G}}}$ and $\boldsymbol{\operatorname{{G'}}}$ just as stuff operators are endofunctors of groupoids over $\boldsymbol{\operatorname{{FinSet_0}}}$.

Why did we choose the specific groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$ (or its $M$-coloured counterpart) for the constructions we actually studied? Because its decategorification is $\mathbbm{N}$, which is the spectrum of the number operator for the quantum harmonic oscillator. This may suggest how to find other groupoids $\boldsymbol{\operatorname{{G}}}$ for which these constructions have some particular physical interest. Indeed, as remarked before, Kelly's theory of "clubs" ([@kelly]) generalizes our framework by, among other things, allowing categories which are not groupoids. Perhaps phenomena related to groupoids can be found which can be given a treatment like the one we have given for the oscillator.
