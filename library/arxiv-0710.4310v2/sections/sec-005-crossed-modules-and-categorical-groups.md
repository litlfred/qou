---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-005-crossed-modules-and-categorical-groups
section_title: "Crossed modules and categorical groups"
section_number: null
pages: 11-12
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
Deﬁnition 13 (Categorical groups and Lie categorical group s) A cate-
gorical group C is a groupoid provided with a strict monoidal structure C×C
⊗
− → C,
as well as a “group inversion” functor −1 :C →C such that both the set of ob-
jects C0 of C and the set of morphisms C1 of C are groups under the tensor
product, and both the source and target maps σ,τ : C1 → C0 are group mor-
phisms. A Lie categorical group is deﬁned analogously by rep lacing groups by
Lie groups and group morphisms by Lie group morphisms.
See [BM, BL] for more details.
Deﬁnition 14 (Morphism of categorical groups) A morphism of categor-
ical groups is given by a strict monoidal functor; see [ML].
It is well-known that the category of crossed modules and the cate gory of
categorical groups are equivalent; see for example [BL, BM, BHS]. L et us ex-
plain how to deﬁne a categorical group C(G) from a crossed module G. This
construction is an old one.
Let G = (∂ : E →G,⊲ ) be a crossed module. The set of objects C0 of C(G)
is given by all elements of G. The set of morphisms C1 of C(G) is given by the
set of all pairs ( X,e ) where X ∈ G and e ∈ E. The source and the target of
(X,e ) ∈ C1 are given by σ(X,e ) = X and τ (X,e ) = ∂(e)−1X, respectively.
In other words, a morphism in C(G) “looks like” X
(X,e)
− − − →∂(e)−1X, which we
will sometimes abbreviate as X
e
− →∂(e)−1X. Given X ∈ G and e,f ∈ E the
composition
X
e
− →∂(e)−1X
f
− →∂(f )−1∂(e)−1X
is
X
ef
− →∂(ef )−1X.
The tensor product has the form:
∂(e)−1X
↑e
X
⊗
∂(f )−1Y
↑f
Y
=
∂(e)−1X∂ (f )−1Y
↑(X⊲f )e
XY
, (8)
where X,Y ∈ G and e,f ∈ E. Therefore, the set of morphisms of C(G) is a
group under the tensor product. This group is isomorphic to the se midirect
product G ⋉E of G and E.
11
From the deﬁnition of a crossed module, it is easy to see that we have indeed
deﬁned a strict monoidal category which, furthermore, is a categ orical group.
We will recall in 1.3.4 how to deﬁne a crossed module from a categorical
group.
