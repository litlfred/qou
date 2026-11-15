---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-002-12-functional-analysis-of-d-module-categories
section_title: "Functional analysis of D-module categories"
section_number: 1.2
pages: 7-9
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
formalism of D-module on stacks, as developed in [DrG1, GR], see Section 4. Our main interest is
in results relating functors between D-module categories with integral transforms: given varieties
X, Y and a D-module K on the product X × Y , one deﬁnes a functor on derived categories of
D-modules
D(X)
/ D(Y )
F ✤
/ πY ∗(π!
XF ⊗K).
by pulling back from X to the product X × Y , tensoring with the integral kernel K, and then
pushing forward to Y via the natural diagram
X
X × Y
πX
o
πY
/ Y.
1.2.1. Integral transforms for quasicoherent sheaves. In the context of quasicoherent sheaves, there
is a very tight connection between categorical operations and geometric operations on the underlying
stacks. In our paper [BFN] with John Francis, we studied the homotopical algebra of categories
of quasicoherent sheaves, and in particular proved a result identifying functors on quasicoherent
sheaves with integral transforms, generalizing results of Orlov [O], Bondal, Larsen and Lunts [BLL]
and To¨en [To]. Namely, we introduced the class of perfect stacks X, which as mentioned above
are characterized (among quasi-compact stacks with aﬃne diagonal) by the property that Q(X) is
compactly generated and rigid. This class includes all (quasi-compact and separated) schemes as
well as most common stacks in characteristic zero, and is closed under natural operations such as
ﬁber products. For perfect stacks X1, X2 over a perfect stack Y we showed that the natural maps
are equivalences
Q(X1) ⊗Q(Y ) Q(X2)
∼
/ Q(X1 ×Y X2)
∼
/ FunL
Q(Y )(Q(X1), Q(X2)).
In other words, Q(Y )-linear integral transforms between Q(X1) and Q(X2) are identiﬁed both with
all Q(Y )-linear functors and with the relative tensor product of the respective categories.
When X = X1 = X2, we also studied the algebra structure of convolution on such “ma-
trix” algebras of quasicoherent sheaves. The dg category of integral transforms Q(X ×Y X) ≃
FunQ(Y )(Q(X), Q(X)) has a natural multiplication, given by convolution, or equivalently by com-
position of functors, making it into a monoidal dg category. In the case Y is a point, this is a
categoriﬁed version of the algebra of matrices with entries labelled by X, while in general it is a
version of Y -block diagonal matrices. Thus one expects the monoidal center and trace of such an
algebra to be a categoriﬁed version of functions on Y . Indeed, we showed that they are identiﬁed
7
with the category Q(LY ) of sheaves on the derived loop space of Y . (In fact Q(X ×Y X) is Morita
equivalent to Q(Y ) under mild hypotheses, see [BFN2].)
Example 1.13. If we take X = pt/B to be the classifying stack of the Borel and Y = pt/G, the
center and trace of the quasicoherent Hecke category Q(B\G/B) are identiﬁed with all quasicoherent
sheaves Q(G/ad G).
1.2.2. Integral transforms for equivariant D-modules. A modiﬁcation of the techniques of [BFN]
provides an analogous description of integral transforms in the D-module setting when the base Y
is a scheme and the projection X1 →Y is a relative Deligne-Mumford stack, or more generally, a
safe morphism in the sense of [DrG1].
Theorem 1.14 (Corollary 5.3). Let X1 →Y denote a Deligne-Mumford stack over a scheme, and
X2 →Y an arbitrary stack. Then the natural maps are equivalences
D(X1) ⊗D(Y ) D(X2)
∼
/ D(X1 ×Y X2)
∼
/ FunL
D(Y )(D(X1), D(X2))
The identiﬁcation of tensors, integral transforms and functors as above fails badly when the base
is a stack, as in our motivating case Y = BG. The fundamental obstruction is the inherently topo-
logical nature of D-modules. Pushing forward along an aﬃne map almost always loses information
(that is, it fails to be conservative): for example, unlike quasicoherent sheaves, many nontrivial
D-modules have no global ﬂat sections at all. Thus even for stacks with aﬃne diagonal, one can
not reconstruct D-modules on a ﬁber product from algebraic operations on D-modules on the fac-
tors (for stacks with ﬁnite diagonal, for example for schemes, this problem disappears). In short,
the Tannakian theory of D-modules is not rich enough to capture the geometric theory. As a re-
sult, tensor and functor categories are not identiﬁed with all integral kernels: there are adjunctions
exhibiting the former as pale shadows of the latter. For example, the category D(G) cannot be
reconstructed from D(pt) = ModC as a module category for D(BG) = C∗(G) -mod where C∗(G) is
the algebra of singular chains on G.
In Section 5.2, we prove the following partial result. We make the very strong assumption that
the stack Y is a classifying stack of an aﬃne group, thus ensuring that the technical conditions
that Y is smooth with aﬃne diagonal. This setup suﬃces for D(Y ) to be semi-rigid under tensor
product, a condition which typically fails for schemes: compact objects in D(Y ) for a scheme are
coherent D-modules, but only ﬂat vector bundles are dualizable. In this restricted setting, we then
ﬁnd that tensor products and linear functors with source a relative Deligne-Mumford stack, or more
generally safe stack, are identiﬁed with each other via the natural map factoring through a full
inclusion into integral transforms.
Theorem 1.15 (Corollary 5.6, Proposition 5.7). Let X1 →Y = BG be a relative Deligne-Mumford
stack over the classifying stack of an aﬃne group, and X2 →Y an arbitrary stack.
Then the
natural map from tensors to functors is an equivalence, and factors through the integral transform
construction
D(X1 ×Y X2)
Φ
)❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
D(X1) ⊗D(Y ) D(X2)
∼
/
Ψ
5❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
FunL
D(Y )(D(X1), D(X2))
Moreover, Φ has a fully faithful left adjoint.
Example 1.16. If X1 = X2 = pt →Y = BG, so that X ×Y X = G, we ﬁnd that the tensor product
and functor categories are identiﬁed with the full subcategory
EndD(BG)(D(pt)) ≃⟨OG⟩⊂D(G)
generated by the structure sheaf.
8
Using this more subtle understanding of the relation between integral transforms and functors,
we calculate the center and trace of Hecke categories. Unlike the quasicoherent case, we do not see
all sheaves on L(BG) = G/ad G as the center and trace, but precisely the full subcategory of sheaves
that can be accessed through the horocycle correspondence, or in other words, unipotent character
sheaves.
