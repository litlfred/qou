---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-008-7-conclusions
section_title: "Conclusions"
section_number: 7
pages: 56-58
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
---
Here we summarize what we have shown, and suggest directions in wh ich this
work could be carried further.
7.1. Categoriﬁed Quantum Mechanics. We began by describing the quantum
harmonic oscillator and the Weyl algebra, the algebra of linear opera tors on its
space of states which correspond to observables and interaction s of the oscillator
system. We saw how this could be related - by the Fock representat ion of the Weyl
algebra - to formal power series with complex coeﬃcients with expon ents counting
quanta of energy.
Our aim at the outset was to categorify this aspect of quantum mec hanics.
Categoriﬁcation of concepts such as “group”, “vector-space” , and indeed “category”
itself have proved interesting within mathematics, and the resulting 2-groups, 2-
vector-spaces, and 2-categories arise naturally in surprising way s. The idea here
was that categoriﬁcation could be applied in a physically relevant sett ing, and
could reveal something useful about the mathematical structur es involved. Here,
we began with the Hilbert space of states of a quantum mechanical s ystem, and
the relevant algebra of operators acting on it. We have produced c ategory-theoretic
equivalents of these: the 2-categories of stuﬀ types and of stuﬀ operators can be
seen as a categoriﬁed Hilbert space and a categoriﬁed algebra.
These are connected to the original setting by concepts of decat egoriﬁcation
which go by the name “cardinality”. We have shown that when we take the cardi-
nalities of all our entities involving “stuﬀ”, we recover much of the st ructure of the
Weyl algebra. By introducing the idea of M -sets, and attendant ideas of entities
labelled with “phases” from some monoid, we have improved this resem blance to
quantum mechanics.
Stuﬀ types - groupoids over FinSet0 - have creation and annihilation operators
which give a purely combinatorial construction which categoriﬁed ma ny features of
the Weyl algebra. They also have a natural inner product which, in c onjunction
with these creation and annihilation operators, allows us to interpre t transition
amplitudes as sums over Feynman diagrams.
However, what these categorify is not Fock space, since it only has scalar mul-
tiplication over /CA
+, rather than /BV , and cardinalities in /CA
+[ [z] ], rather than /BV [ [z] ].
Our U (1)-stuﬀ types are a better categoriﬁcation of Fock space, and these have
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 57
cardinalities in ( /CA
+⊗U (1))[ [z] ], which we can map to /BV [ [z] ]. This map h is not
one-to-one, and this fact is responsible for the phenomenon of int erference of states
with diﬀerent phases.
The problem of categorifying quantum mechanics is much more gener al than
the simple case of a harmonic oscillator we have discussed. Another a pproach to
bringing category theory to quantum mechanics is [5]. That paper pr ovides good
description of a simple “picture calculus” for quite general quantum mechanics
which uses a background of category theory. This is not a categor iﬁcation in our
sense, but together with some of the structure described in appe ndix B may suggest
a broader framework for dealing with the question.
Although we have conﬁned ourselves to the harmonic oscillator in this paper, we
can suggest various directions in which these ideas could be taken fu rther. One is
to look at the inner product through a more category-theoretic le ns.
7.1.1. Conjugate-Linearity and the Inner Product. Recall that the inner product
for M -stuﬀ types had to be modiﬁed somewhat in order to agree with the u sual
inner product on the Hilbert space /BV [ [z] ] in the case whenM =U (1). The nontrivial
isomorphism of U (1) with itself provides a notion of complex conjugation. But how
should we interpret the inner product for U (1)-stuﬀ types?
In fact, it makes more sense when we adopt the interpretation of t he inner
product⟨φ|ψ⟩ as pairing a state vector with a costate covector. So the (conjugate-
linear) inner product ⟨ψ|Tφ⟩ gives the amplitude to ﬁnd a system set up in state φ
and evolving according to the operator T to be measured in state ψ. This suggests
we should think of observing a system in a certain state as a time-rev ersed version
of setting the system up in that state.
But if time evolution by T is given by an operator ET , time-evolution by −T is
described by an operator E−T . This has groupoid and projections to FinSet0 the
same as those for ET , but the groupoid has objects labels by inverses of the labels
on the objects of ET . In U (1), this inverse is the same as the complex conjugate,
so that E−T = ET . This suggests an interpretation of the complex conjugate Φ
as a time-reversal of the original stuﬀ type, consistent with our in terpretation of a
measurement process.
7.1.2. Categorifying M . The operation hom takes two objects in a category and
yields the set of morphisms between them. In an enriched category , this can be
replaced by some other kind of collection of morphisms - a vector spa ce, for instance.
In the case that this collection is always an object of the same categ ory as the
original objects, we have a “hom-object”. In any case hom(−,−) becomes a functor
into the category in which hom-objects are found.
Moreover, the functor hom(−,B ) is a covariant functor, while hom(A,−) is
contravariant - that is, a (covariant) functor to Bop. This seems closely analogous
to the conjugate-linearity in the complex inner product on a Hilbert s pace. We
may ask whether the inner product on a Hilbert space comes from so me hom? In
particular, in order to make a category where morphisms are spans (see appendix
B), we need to look at the opposite category of a U (1)-groupoid. A groupoid is
indistinguishable from its opposite category after taking cardinality - but what
about an M -groupoid?
To make sense of this idea, we could replace a monoid M with a monoidal
category,M. A groupoid with objects labelled in the monoid - that is, with a
58 JEFFREY MORTON
function from its set of objects to M , would be replaced by a groupoid X with a
functor into the monoidal categoryM - so in particular, we would have labellings of
morphisms of X with morphisms of M. This combination of groupoid and functor
can be interpreted as an object in the category of “groupoids ove rM”.
Given a categoriﬁcation of U (1), we could ask whether this new setting more
naturally produces the inner product we want for quantum mechan ics. So far,
though, we have not considered how to categorify the group of ph ases in order to
accomplish this most naturally.
7.1.3. Non-Counting Measures and M -Groupoid Cardinality. We saw in equation
(73) and what followed that the transition amplitudes for the pertu rbed harmonic
oscillator are given in terms of a sum and integral over all Feynman dia grams
with edges weighted by phases. To do this, we had to accept the equ ation at
the equational level and then give it an interpretation in terms of U (1)-stuﬀ types,
since we have, to date, not given any categoriﬁed meaning for the in tegrals. We can
observe, however, that our notion of cardinality for M -groupoids, and by extension
M -stuﬀ types, used only the groupoid cardinality derived from count ing measure
on sets, weights from the monoid M .
To give a categoriﬁed interpretation of the integral directly, we mig ht wish to
use the fact that when M =U (1), there is a measure other than counting measure
on M itself. In this case, the natural choice is the Haar measure on the L ie group
U (1) - though for other choices of M there may be other natural choices. Then
a cardinality operator for an M -groupoid would involve an integral involving both
M and the groupoid structure. In the case where the measure on M is just set
cardinality, this should reduce to the more combinatorial deﬁnition g iven here. We
could hope that such a notion of cardinality would let us give a direct ca tegoriﬁed
interpretation of equations such as (73).
