---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-008-7-conclusions
section_title: "Conclusions"
section_number: 7
pages: 56-58
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
text_source: latex
latex_prose_ratio: 0.71
latex_coverage_ratio: 0.986
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
---
Here we summarize what we have shown, and suggest directions in which this work could be carried further.

## Categorified Quantum Mechanics

We began by describing the quantum harmonic oscillator and the Weyl algebra, the algebra of linear operators on its space of states which correspond to observables and interactions of the oscillator system. We saw how this could be related - by the Fock representation of the Weyl algebra - to formal power series with complex coefficients with exponents counting quanta of energy.

Our aim at the outset was to categorify this aspect of quantum mechanics. Categorification of concepts such as "group", "vector-space", and indeed "category" itself have proved interesting within mathematics, and the resulting 2-groups, 2-vector-spaces, and 2-categories arise naturally in surprising ways. The idea here was that categorification could be applied in a physically relevant setting, and could reveal something useful about the mathematical structures involved. Here, we began with the Hilbert space of states of a quantum mechanical system, and the relevant algebra of operators acting on it. We have produced category-theoretic equivalents of these: the 2-categories of stuff types and of stuff operators can be seen as a categorified Hilbert space and a categorified algebra.

These are connected to the original setting by concepts of decategorification which go by the name "cardinality". We have shown that when we take the cardinalities of all our entities involving "stuff", we recover much of the structure of the Weyl algebra. By introducing the idea of $M$-sets, and attendant ideas of entities labelled with "phases" from some monoid, we have improved this resemblance to quantum mechanics.

Stuff types - groupoids over $\boldsymbol{\operatorname{{FinSet_0}}}$ - have creation and annihilation operators which give a purely combinatorial construction which categorified many features of the Weyl algebra. They also have a natural inner product which, in conjunction with these creation and annihilation operators, allows us to interpret transition amplitudes as sums over Feynman diagrams.

However, what these categorify is not Fock space, since it only has scalar multiplication over $\mathbbm{R}^+$, rather than $\mathbbm{C}$, and cardinalities in $\mathbbm{R}^+[\![z]\!]$, rather than $\mathbbm{C}[\![z]\!]$. Our $U(1)$-stuff types are a better categorification of Fock space, and these have cardinalities in $(\mathbbm{R}^+ \otimes U(1))[\![z]\!]$, which we can map to $\mathbbm{C}[\![z]\!]$. This map $h$ is not one-to-one, and this fact is responsible for the phenomenon of interference of states with different phases.

The problem of categorifying quantum mechanics is much more general than the simple case of a harmonic oscillator we have discussed. Another approach to bringing category theory to quantum mechanics is [@coecke]. That paper provides good description of a simple "picture calculus" for quite general quantum mechanics which uses a background of category theory. This is not a categorification in our sense, but together with some of the structure described in appendix [\[sec:slicecategory\]](#sec:slicecategory){reference-type="ref" reference="sec:slicecategory"} may suggest a broader framework for dealing with the question.

Although we have confined ourselves to the harmonic oscillator in this paper, we can suggest various directions in which these ideas could be taken further. One is to look at the inner product through a more category-theoretic lens.

### Conjugate-Linearity and the Inner Product {#sec:conjtimereversal}

Recall that the inner product for $M$-stuff types had to be modified somewhat in order to agree with the usual inner product on the Hilbert space $\mathbbm{C}[\![z]\!]$ in the case when $M=U(1)$. The nontrivial isomorphism of $U(1)$ with itself provides a notion of complex conjugation. But how should we interpret the inner product for $U(1)$-stuff types?

In fact, it makes more sense when we adopt the interpretation of the inner product $\left\langle{\phi|\psi}\right\rangle$ as pairing a *state vector* with a *costate covector*. So the (conjugate-linear) inner product $\left\langle{\psi|T\phi}\right\rangle$ gives the amplitude to find a system *set up* in state $\phi$ and evolving according to the operator $T$ to be *measured* in state $\psi$. This suggests we should think of observing a system in a certain state as a time-reversed version of setting the system up in that state.

But if time evolution by $T$ is given by an operator $E_T$, time-evolution by $-T$ is described by an operator $E_{-T}$. This has groupoid and projections to $\boldsymbol{\operatorname{{FinSet_0}}}$ the same as those for $E_T$, but the groupoid has objects labels by inverses of the labels on the objects of $E_T$. In $U(1)$, this inverse is the same as the complex conjugate, so that $E_{-T}=\overline{E_T}$. This suggests an interpretation of the complex conjugate $\overline{\Phi}$ as a time-reversal of the original stuff type, consistent with our interpretation of a measurement process.

### Categorifying $M$ {#sec:categorifyingM}

The operation $hom$ takes two objects in a category and yields the set of morphisms between them. In an enriched category, this can be replaced by some other kind of collection of morphisms - a vector space, for instance. In the case that this collection is always an object of the same category as the original objects, we have a "$hom$-object". In any case $hom(-,-)$ becomes a functor into the category in which $hom$-objects are found.

Moreover, the functor $hom(-,B)$ is a covariant functor, while $hom(A,-)$ is contravariant - that is, a (covariant) functor to $B^{op}$. This seems closely analogous to the conjugate-linearity in the complex inner product on a Hilbert space. We may ask whether the inner product on a Hilbert space comes from some $hom$? In particular, in order to make a category where morphisms are spans (see appendix [\[sec:slicecategory\]](#sec:slicecategory){reference-type="ref" reference="sec:slicecategory"}), we need to look at the opposite category of a $U(1)$-groupoid. A groupoid is indistinguishable from its opposite category after taking cardinality - but what about an $M$-groupoid?

To make sense of this idea, we could replace a *monoid* $M$ with a *monoidal category*, $\mathcal{M}$. A groupoid with objects labelled in the monoid - that is, with a function from its set of objects to $M$, would be replaced by a groupoid $\boldsymbol{\operatorname{{X}}}$ with a functor into the monoidal category $\mathcal{M}$ - so in particular, we would have labellings of morphisms of $\boldsymbol{\operatorname{{X}}}$ with morphisms of $\mathcal{M}$. This combination of groupoid and functor can be interpreted as an object in the category of "groupoids over $\mathcal{M}$".

Given a categorification of $U(1)$, we could ask whether this new setting more naturally produces the inner product we want for quantum mechanics. So far, though, we have not considered how to categorify the group of phases in order to accomplish this most naturally.

### Non-Counting Measures and $M$-Groupoid Cardinality

We saw in equation ([\[eq:perturbfeynman\]](#eq:perturbfeynman){reference-type="ref" reference="eq:perturbfeynman"}) and what followed that the transition amplitudes for the perturbed harmonic oscillator are given in terms of a sum and integral over all Feynman diagrams with edges weighted by phases. To do this, we had to accept the equation at the equational level and then give it an interpretation in terms of $U(1)$-stuff types, since we have, to date, not given any categorified meaning for the integrals. We can observe, however, that our notion of cardinality for $M$-groupoids, and by extension $M$-stuff types, used only the groupoid cardinality derived from counting measure on sets, weights from the monoid $M$.

To give a categorified interpretation of the integral directly, we might wish to use the fact that when $M=U(1)$, there is a measure other than counting measure on $M$ itself. In this case, the natural choice is the Haar measure on the Lie group $U(1)$ - though for other choices of $M$ there may be other natural choices. Then a cardinality operator for an $M$-groupoid would involve an integral involving both $M$ and the groupoid structure. In the case where the measure on $M$ is just set cardinality, this should reduce to the more combinatorial definition given here. We could hope that such a notion of cardinality would let us give a direct categorified interpretation of equations such as ([\[eq:perturbfeynman\]](#eq:perturbfeynman){reference-type="ref" reference="eq:perturbfeynman"}).

## Other Generalizations

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
