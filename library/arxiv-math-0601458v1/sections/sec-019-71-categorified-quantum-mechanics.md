---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-019-71-categorified-quantum-mechanics
section_title: "Categorified Quantum Mechanics"
section_number: 7.1
pages: 56-58
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.857
latex_coverage_ratio: 0.989
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
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
