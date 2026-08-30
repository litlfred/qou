---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-001-2-results-on-squared-norms-global-dimensions-wea
section_title: "Results on squared norms, global dimensions, weak Hopf algebras, and Ocneanu rigidity"
section_number: 2
pages: 3-4
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
algebras, and Ocneanu rigidity
Letk be an algebraically closed ﬁeld. By a multi-fusion category overk we mean
a rigid semisimple k-linear tensor category C with ﬁnitely many simple objects and
ﬁnite dimensional spaces of morphisms. If the unit object 1 of C is simple, then
the category C is said to be a fusion category. Otherwise (if 1 is not simple), it is
easy to see that we have 1 = ⊕i∈J 1i, where 1i are pairwise nonisomorphic simple
objects.
Let us list a few examples to keep in mind when thinking about fusion and
multi-fusion categories.
Examples of fusion categories.
1. The category Vec G of ﬁnite dimensional vector spaces graded by a ﬁnite group
G (or, equivalently, ﬁnite dimensional modules over the function algeb ra Fun(G,k ).)
Simple objects in this category are evaluation modules Vg, g ∈ G, and the tensor
product is given by Vg ⊗Vh = Vgh, with the associativity morphism being the
identity.
More generally, pick a 3-cocycle ω ∈Z 3(G,k ×). To this cocycle we can attach a
twisted version VecG,ω of VecG: the simple objects and the tensor product functor
are the same, but the associativity isomorphism is given by Φ Vg,Vh,Vk =ω(g,h,k )id.
The pentagon axiom then follows from the cocycle condition
ω(h,k,l )ω(g,hk,l )ω(g,h,k ) =ω(gh,k,l )ω(g,h,kl ).
Note that cohomologous cocycles deﬁne equivalent fusion categor ies.
2. The category of ﬁnite dimensional k-representations of a ﬁnite group G, whose
order is relatively prime to the characteristic of k.
3. The category of integrable modules (from category O) over the aﬃne algebra
ˆsl2 at levell (see [BaKi]). The tensor product in this category is the fusion prod uct,
deﬁned at the level of objects by the Verlinde fusion rule
Vi ⊗Vj =
l−|i+j−l|∑
k=|i−j|
k≡i+j mod 2
Vk
Examples of multi-fusion categories.
4 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
1. The category of ﬁnite dimensional bimodules over a ﬁnite dimension al semi-
simple k-algebra, with bimodule tensor product. It has simple objects Mij with
“matrix” tensor product Mij ⊗Mjk =Mik; thus the identity object is 1 = ⊕iMii.
2. The category of ﬁnite dimensional modules over the function alge bra on a
ﬁnite groupoid.
