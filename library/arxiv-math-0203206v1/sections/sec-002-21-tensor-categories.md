---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-002-21-tensor-categories
section_title: "Tensor Categories"
section_number: 2.1
pages: 2-3
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
will become clear in our treatment. (Yamagami has recently proved a result [44, Theorem 3.6] implying that,
passing if necessary to an equivalent tensor ∗-category, there is an essentially unique ε-structure.) On the other
hand, the von Neumann algebraic formulation of discrete quantum g roups used in [43] is considerably more
involved than current deﬁnitions, in that it unnecessarily mixes analy tic and algebraic structures.
In neither of [40, 43] does one ﬁnd a complete proof of equivalence b etween the given category and the
representation category of the derived quantum group. Also que stions of uniqueness and braidings have not
been addressed.
It is well known that the self-duality of the category of ﬁnite dimens ional Hopf algebras breaks down in the
inﬁnite dimensional case. Motivated by the desire to ﬁnd a purely alge braic framework for quantum groups
admitting a version of Pontryagin duality, A. Van Daele developed the theory of algebraic quantum groups
(aqg) [37]. This is achieved by admitting non-unital algebras and requ iring the existence of a positive and left-
invariant functional, the Haar functional. All compact and all discre te quantum groups are aqg, and every aqg
has a unique analytic extension to a locally compact quantum group [20 ], having an equivalent von Neumann
algebraic version [22]. A discrete multiplier Hopf ∗-algebra [35] can be shown to have a Haar functional rendering
it a discrete aqg.
The purpose of the present paper is to give a coherent and reason ably complete survey of the Tannaka-
Krein theory of quantum groups. The only other review we are awar e of is [15], which appeared ten years ago.
At the time, no appropriate self-dual category of quantum group s existed. (In the same year, P. Podl´ es and
Woronowicz, in deﬁning a discrete quantum group, took the ﬁrst st ep in this direction [28].) The approach to
Tannakian categories motivated by algebraic geometry is well review ed in [6], where, however, only symmetric
tensor categories are considered.
Our approach to generalized Tannaka-Krein theory adopts the ph ilosophy on quantum groups in [41, 43],
meaning a self-dual category with emphasis on ∗-categories. In contradistinction to these authors we wish to
distinguish categorical from quantum group aspects as well as alge braic from analytic aspects as far as possible.
Following [31, 7, 34, 45], we emphasize natural transformations of t he embedding functor. Yet, our use of natural
transformations is more direct and we work with representations r ather than corepresentations. The algebra
product is just the composition of natural transformations and t he coproduct is deﬁned directly in terms of the
tensor structure, the tensor unit giving rise to the counit. This yie lds a quantum semigroup, whose discreteness
is an immediate consequence of the semisimplicity of the category. (T he semisimplicity of ∗-categories avoids
appealing to the theorem of Barr-Beck in [31, 7] and to proceed in a p edestrian way, using only the deﬁnition
of natural transformations.) The coinverse now arises from the c onjugation in the category. The result is a
discrete multiplier Hopf ∗-algebra. Thus our reconstruction of the discrete aqg is purely alg ebraic, the existence
of the Haar functional following by quantum group theory.
The selfduality of the category of aqg and the existence of analytic extensions allow us to to relate our
reconstruction result to those of Woronowicz and Yamagami on on e hand and the purely algebraic ones on the
other [34, 45]. In particular, making use of the universal unitary co representation of an aqg introduced by J.
Kustermans [18], we prove that the tensor ∗-category of ∗-representations (or modules) of a discrete aqg ( A, ∆) is
equivalent to the tensor ∗-category of unitary corepresentations (or comodules) of the d ual compact aqg ( ˆA, ˆ∆).
We provide these categories with conjugates (for representatio ns of discrete aqg this has not been worked out
before). We also show that the tensor ∗-category of pointwise continuous ﬁnite dimensional ∗-representations
of a sub Hopf ∗-algebra of the maximal dual (or Sweedler dual) Hopf ∗-algebra of a compact quantum group is
equivalent to any of the tensor ∗-categories mentioned above, whenever the Hopf ∗-algebra separates the regular
functions associated with the compact quantum group. This is a use ful result since it applies to the deformed
universal enveloping Lie algebras Uq(g) of M. Jimbo and V.G. Drinfeld. It therefore links these axiomatic
quantum group results to the more familiar context of quantum gro ups given by deformations of semisimple Lie
algebras g. Indeed, this is how the latter can be shown to produce compact (o r discrete) quantum groups and
how Woronowicz [41] constructed the compact matrix pseudogrou pSUq(N ).
2
The correspondence between inﬁnite dimensional representation s and corepresentations was already estab-
lished in [28] and [18], but only for the objects of the respective cate gories, morphisms and the tensor structure
were not considered. In [39] tensor structure and braiding were t aken into account in a purely algebraic context
and, while studying the amenability of quantum groups, the corresp ondence between tensor C*-categories of
inﬁnite dimensional representations and corepresentations was e stablished in [3, 4], for the various analytic
versions of aqg and lcqg. The latter results rely on the theory of inﬁ nite dimensional representations and corep-
resentations and of the construction of the universal corepres entation for lcqg developed in [19]. But none of
this work touched on Tannaka-Krein reconstruction, since conju gates do not exist in the inﬁnite dimensional
case. Another type of reconstruction result for tensor C*-cat egories involving inﬁnite dimensional objects was
undertaken in [10] from the point of view of multiplicative unitaries and the regular corepresentation.
For a discrete aqg ( A, ∆) we establish a bijection between braidings of the category Rep f (A, ∆) and R-
matrices in the multiplier algebra M (A ⊗A). To the best of our knowledge this is the ﬁrst such result rigorous ly
proven in an axiomatic framework for quantum groups. If the cate gory is symmetric and the embedding
functor maps the braiding into the canonical braiding of the catego ry of Hilbert spaces, the discrete aqg is
cocommutative.
For any discrete aqg there is a compact group G, the intrinsic group, and for cocommutative ( A, ∆) we
prove an equivalence Rep f (A, ∆) ≃ RepfG of tensor ∗-categories. This is the only point in our approach were
analysis plays a role, in that we use the theorems of Gelfand, Krein-M ilman, Stone-Weierstrass, etc. In the
theory of locally compact quantum groups it is well known that commu tative and cocommutative quantum
groups are Kac algebras. Furthermore, commutative (resp. coc ommutative) lcqg are of the form ( C(G), ∆)
(resp. (C∗
r (G), ∆)) for a locally compact group G. Finally, a commutative compact aqg is the algebra of regular
functions on a compact group G, but cocommutative discrete aqg are inconvenient to characteriz e. This is why,
alternatively, we give the more instructive and direct proof of the a bove equivalence of categories. In passing
we give a description of a cocommutative aqg in terms of the intrinsic g roup G.
It cannot be emphasized strongly enough that all Tannaka-Krein t ype results discussed so far depend on the
tensor ∗-category being concrete, i.e. coming with a faithful tensor funct or into the category of Hilbert spaces.
There are applications in pure mathematics and in quantum ﬁeld theor y, where such a functor is not given a
priori. For symmetric categories, it was ﬁrst shown by S. Doplicher a nd J. E. Roberts [9] that such a functor
always exists. An alternative approach in a more algebraic setting wa s given by P. Deligne [8]. The questions
of existence and uniqueness of an embedding functor will be addres sed anew in a sequel to this paper.
The above discussion did not follow the order of presentation. Let u s therefore give a brief overview of the
organization of this paper. In the next section we provide some pre liminaries on tensor ∗-categories and aqg.
Concerning the former we are quite brief, since much of this materia l is almost universally known. Concerning
the latter we focus in particular on the discrete and compact cases and discuss the examples related to groups.
In Section 3 we treat the representation and corepresentation t heory of discrete and compact aqg, respectively,
from a tensor ∗-category point of view. To this end, we recall the universal corep resentation due to Kustermans,
and we discuss conjugates in these categories. The special case o f cocommutative discrete aqg is considered in
Section 4. Section 5 is the heart of this paper. There we construct a discrete quantum semigroup from a tensor
∗-category, deriving the coinverse from the conjugation and leadin g to a discrete aqg. The precise statement of
the generalized Tannaka-Krein theorem for quantum groups is the n made in Theorem 5.25. In the ﬁnal Section
6 we establish the bijection between braidings and R-matrices. In the case of a symmetric tensor ∗-category
with symmetric embedding functor we recover the classical Tannak a-Krein theorem for compact groups.
