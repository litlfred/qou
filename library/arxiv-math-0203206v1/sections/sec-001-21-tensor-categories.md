---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-001-21-tensor-categories
section_title: "Tensor Categories"
section_number: 2.1
pages: 2-3
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
---
will become clear in our treatment. (Yamagami has recently proved a result [44, Theorem 3.6] implying that,
passing if necessary to an equivalent tensor ∗-category, there is an essentially unique ε-structure.) On the other
hand, the von Neumann algebraic formulation of discrete quantum groups used in [43] is considerably more
involved than current deﬁnitions, in that it unnecessarily mixes analytic and algebraic structures.
In neither of [40, 43] does one ﬁnd a complete proof of equivalence between the given category and the
representation category of the derived quantum group. Also questions of uniqueness and braidings have not
been addressed.
It is well known that the self-duality of the category of ﬁnite dimensional Hopf algebras breaks down in the
inﬁnite dimensional case. Motivated by the desire to ﬁnd a purely algebraic framework for quantum groups
admitting a version of Pontryagin duality, A. Van Daele developed the theory of algebraic quantum groups
(aqg) [37]. This is achieved by admitting non-unital algebras and requiring the existence of a positive and left-
invariant functional, the Haar functional. All compact and all discrete quantum groups are aqg, and every aqg
has a unique analytic extension to a locally compact quantum group [20], having an equivalent von Neumann
algebraic version [22]. A discrete multiplier Hopf ∗-algebra [35] can be shown to have a Haar functional rendering
it a discrete aqg.
The purpose of the present paper is to give a coherent and reasonably complete survey of the Tannaka-
Krein theory of quantum groups. The only other review we are aware of is [15], which appeared ten years ago.
At the time, no appropriate self-dual category of quantum groups existed. (In the same year, P. Podl´es and
Woronowicz, in deﬁning a discrete quantum group, took the ﬁrst step in this direction [28].) The approach to
Tannakian categories motivated by algebraic geometry is well reviewed in [6], where, however, only symmetric
tensor categories are considered.
Our approach to generalized Tannaka-Krein theory adopts the philosophy on quantum groups in [41, 43],
meaning a self-dual category with emphasis on ∗-categories. In contradistinction to these authors we wish to
distinguish categorical from quantum group aspects as well as algebraic from analytic aspects as far as possible.
Following [31, 7, 34, 45], we emphasize natural transformations of the embedding functor. Yet, our use of natural
transformations is more direct and we work with representations rather than corepresentations. The algebra
product is just the composition of natural transformations and the coproduct is deﬁned directly in terms of the
tensor structure, the tensor unit giving rise to the counit. This yields a quantum semigroup, whose discreteness
is an immediate consequence of the semisimplicity of the category. (The semisimplicity of ∗-categories avoids
appealing to the theorem of Barr-Beck in [31, 7] and to proceed in a pedestrian way, using only the deﬁnition
of natural transformations.) The coinverse now arises from the conjugation in the category. The result is a
discrete multiplier Hopf ∗-algebra. Thus our reconstruction of the discrete aqg is purely algebraic, the existence
of the Haar functional following by quantum group theory.
The selfduality of the category of aqg and the existence of analytic extensions allow us to to relate our
reconstruction result to those of Woronowicz and Yamagami on one hand and the purely algebraic ones on the
other [34, 45]. In particular, making use of the universal unitary corepresentation of an aqg introduced by J.
Kustermans [18], we prove that the tensor ∗-category of ∗-representations (or modules) of a discrete aqg (A, ∆) is
equivalent to the tensor ∗-category of unitary corepresentations (or comodules) of the dual compact aqg ( ˆA, ˆ∆).
We provide these categories with conjugates (for representations of discrete aqg this has not been worked out
before). We also show that the tensor ∗-category of pointwise continuous ﬁnite dimensional ∗-representations
of a sub Hopf ∗-algebra of the maximal dual (or Sweedler dual) Hopf ∗-algebra of a compact quantum group is
equivalent to any of the tensor ∗-categories mentioned above, whenever the Hopf ∗-algebra separates the regular
functions associated with the compact quantum group. This is a useful result since it applies to the deformed
universal enveloping Lie algebras Uq(g) of M. Jimbo and V.G. Drinfeld.
It therefore links these axiomatic
quantum group results to the more familiar context of quantum groups given by deformations of semisimple Lie
algebras g. Indeed, this is how the latter can be shown to produce compact (or discrete) quantum groups and
how Woronowicz [41] constructed the compact matrix pseudogroup SUq(N).
2
The correspondence between inﬁnite dimensional representations and corepresentations was already estab-
lished in [28] and [18], but only for the objects of the respective categories, morphisms and the tensor structure
were not considered. In [39] tensor structure and braiding were taken into account in a purely algebraic context
and, while studying the amenability of quantum groups, the correspondence between tensor C*-categories of
inﬁnite dimensional representations and corepresentations was established in [3, 4], for the various analytic
versions of aqg and lcqg. The latter results rely on the theory of inﬁnite dimensional representations and corep-
resentations and of the construction of the universal corepresentation for lcqg developed in [19]. But none of
this work touched on Tannaka-Krein reconstruction, since conjugates do not exist in the inﬁnite dimensional
case. Another type of reconstruction result for tensor C*-categories involving inﬁnite dimensional objects was
undertaken in [10] from the point of view of multiplicative unitaries and the regular corepresentation.
For a discrete aqg (A, ∆) we establish a bijection between braidings of the category Repf(A, ∆) and R-
matrices in the multiplier algebra M(A⊗A). To the best of our knowledge this is the ﬁrst such result rigorously
proven in an axiomatic framework for quantum groups.
If the category is symmetric and the embedding
functor maps the braiding into the canonical braiding of the category of Hilbert spaces, the discrete aqg is
cocommutative.
For any discrete aqg there is a compact group G, the intrinsic group, and for cocommutative (A, ∆) we
prove an equivalence Repf(A, ∆) ≃Repf G of tensor ∗-categories. This is the only point in our approach were
analysis plays a role, in that we use the theorems of Gelfand, Krein-Milman, Stone-Weierstrass, etc. In the
theory of locally compact quantum groups it is well known that commutative and cocommutative quantum
groups are Kac algebras. Furthermore, commutative (resp. cocommutative) lcqg are of the form (C(G), ∆)
(resp. (C∗
r (G), ∆)) for a locally compact group G. Finally, a commutative compact aqg is the algebra of regular
functions on a compact group G, but cocommutative discrete aqg are inconvenient to characterize. This is why,
alternatively, we give the more instructive and direct proof of the above equivalence of categories. In passing
we give a description of a cocommutative aqg in terms of the intrinsic group G.
It cannot be emphasized strongly enough that all Tannaka-Krein type results discussed so far depend on the
tensor ∗-category being concrete, i.e. coming with a faithful tensor functor into the category of Hilbert spaces.
There are applications in pure mathematics and in quantum ﬁeld theory, where such a functor is not given a
priori. For symmetric categories, it was ﬁrst shown by S. Doplicher and J. E. Roberts [9] that such a functor
always exists. An alternative approach in a more algebraic setting was given by P. Deligne [8]. The questions
of existence and uniqueness of an embedding functor will be addressed anew in a sequel to this paper.
The above discussion did not follow the order of presentation. Let us therefore give a brief overview of the
