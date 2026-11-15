---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
Introduction
In this paper we ﬁx our ground ﬁeld to be C.
A fusion category is a rigid
semisimple linear monoidal category with ﬁnitely many isomorphism classes of
simple objects and whose unit object is simple. A basic example of a fusion
category is the category of representations of a ﬁnite group; in this way the
study of fusion categories can be regarded as a common generalization of group
theory and representation theory.
For an overview on fusion categories, see
[21, 5].
Many of the basic results on fusion categories were obtained by Etingof,
Nikshych and Ostrik in [9]. These results include the fact that the quadruple
dual functor is canonically isomorphic to the the identity functor, positivity of
the paired dimensions, and Ocneanu rigidity.
These results were proved in [9] using the theory of weak Hopf algebras. The
idea is that since every fusion category can be expressed as the category of ﬁnite-
dimensional representations of some semisimple weak Hopf algebra [9], one may
prove results about fusion categories by translating them into the language of
weak Hopf algebras. One motivation for this paper, building on [10, 16, 19, 4],
was to give a uniﬁed account of how these results can be proved directly in the
fusion category itself, using the graphical calculus of string diagrams [14, 13, 26].
Another motivation has been the string-net description for the vector spaces
in the Turaev-Viro model of 3-dimensional topological quantum ﬁeld theory
[15], where the graphical calculus plays a prominent role.
However, the main motivation has been to investigate the conjecture of
Etingof, Nikshych and Ostrik, that every fusion category admits a pivotal struc-
ture [9], as we now explain.
1
arXiv:1502.02882v2  [math.QA]  20 Jul 2015
The pairing convention
In the string diagram calculus, the objects V of the fusion category C are used
as labels for strands in the plane. The main feature is rigidity — the notion
that the strands are oriented, and that there are left and right dual structure
maps, drawn as
 
,
!
and
 
,
!
respectively, satisfying ‘snake equations’ such as
=
.
One can also form closed loops, which involves pairing left and right dual struc-
ture maps together:
∈Hom(1, 1) .
(1)
In order to make this well-deﬁned, it is usually imagined that one needs a
pivotal structure on the fusion category, that is, a monoidal natural isomorphism
γ : id ⇒∗∗from the identity functor on the fusion category to the double dual
functor (see Section 5.1). Etingof, Nikshych and Ostrik have conjectured that
such a structure always exists:
Conjecture ([9]). Every fusion category admits a pivotal structure.
The main idea we use in this article is that, in fact, there is a well-deﬁned
way to make sense of diagrams which employ both left and right dual structure
maps together, such as (1), even without a pivotal structure. The rule (at least
for simple objects V ) is that if left and right dual structure maps appear in a
diagram, then they cannot be chosen independently but must be correlated in
the following way: when paired together, they must give the fusion dimension of
V . The fusion dimension of V is a certain positive number canonically associated
to V in a fusion category which we deﬁne in Section 3.1; it does not make use
of a pivotal structure. We call this the pairing convention, and it allows us to
unambiguously evaluate diagrams such as
in a ‘bare’ fusion category, which would otherwise not be well-deﬁned.
2
Pivotal operators
Using the pairing convention, we can give a simple diagrammatic deﬁnition of
the pivotal operators of a fusion category, which are certain canonically deﬁned
linear maps
T A
BC : Hom(A, B ⊗C) →Hom(A, B ⊗C)
associated to every triple of objects A,B and C in a fusion category.
One
advantage of our framework is that these maps are canonical, not depending
on any choices of duals for their deﬁnition. The pivotal operators play the role
of the double dual functor, and the string diagram calculus then gives a simple
proof that T A
BC squares to the identity, see Theorem 3.10.
The idea of this
graphical proof is originally due to Hagge and Hong [10].
Main results
Our main results are as follows. Firstly, we show that every fusion category
C over C comes equipped with a canonical monoidal endofunctor T , whose
underlying functor is the identity, whose action on the hom-sets Hom(Xi, Xj ⊗
Xk) between tensor products of simple objects is given graphically by the pivotal
operators, and which squares to the identity (Theorem 3.28).
Secondly, we use this viewpoint to give graphical proofs of the following
results from [9]:
• the quadruple dual is monoidally naturally isomorphic to the identity
(Corollary (3.30))
• positivity of the paired dimensions (Theorem 3.19),
• a pseudo-unitary fusion category is spherical (Corollary 5.5)
• the sphericalization of a fusion category is spherical (Corollary 5.15)
• Ocneanu rigidity, i.e. the vanishing of the Davydov-Yetter cohomology
(Theorem 6.6)
Thirdly, in Theorem 4.17 we explicitly compute the pivotal operators in terms
of the associators of the fusion category as a product of the pivotal indicators,
which we introduce in Section 4.2, with the apex associator monodromy, which
we introduce in Section 4.3.
Finally, we characterize pivotal structures as solutions of an explicit set of
equations over the complex numbers (Theorem 5.4), reﬁning a formula of Wang
[27, Prop 4.17].
Outline of paper
In Section 2 we give our conventions on string diagrams. In Section 3 we deﬁne
the pairing convention and the pivotal operators, show that the paired dimen-
sions are positive, and show how to interpret the pivotal operators as a monoidal
functor. In Section 4 we compute the pivotal operators explicitly in terms of
the associators. In Section 5 we express pivotal structures as solutions of cer-
tain explicit algebraic equations, and formulate the sphericalization of a fusion
category from our approach. Finally in Section 6 we give a graphical proof of
Ocneanu rigidity.
3
