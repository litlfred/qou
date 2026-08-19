---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-006-2-a-brugui-eres-and-a-virelizier
section_title: "A. BRUGUI `ERES AND A. VIRELIZIER"
section_number: 2
pages: 2-3
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨ uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
The dimension dim C of C (which is the sum of squares of dimensions of simple
objects) is moreover assumed to be invertible in k. The algorithm for computing
TVC(M ) consists in presenting the 3-manifold M by a triangulation, coloring the
edges of the triangulation with simple objects of C, and then evaluating the colored
tetrahedra by means of the 6 j-symbols of C.
If B is a modular category, then it is also a spherical category, and the R eshetikhin-
Turaev and Turaev-Viro invariants are related [Tur94, Ro95] by:
TVB(M ) = RT B(M )RTB(−M )
for any 3- manifold M , where −M is the 3-manifold M with opposite orientation.
But in general a spherical category need not to be braided and so c annot be
used as input to deﬁne the Reshetikhin-Turaev invariant. However , spherical and
modular categories are related by a theorem of M¨ uger [M¨ u03]: if C is a spherical
fusion category over an algebraically closed ﬁeld k and has invertible dimension,
then its center Z(C) is a modular fusion category of dimension dim Z(C) = (dim C)2.
In this setting, Turaev conjectured that, for any 3-manifold M ,
TVC(M ) = RT Z(C)(M ).
This conjecture was shown to be true for some spherical categor ies C arising from
subfactors, see [KSW05]. The general case is still open.
In this context, a natural question is: how can we compute RT Z(C)(M )? Using
the algorithm given by Reshetikhin and Turaev is not a practicable app roach here,
as that would require a description of the simple objects of Z(C) in terms of those
of C, and no such description is available in general. What we need is a diﬀere nt
algorithm for computing RT Z(C)(M ), which one should be able to perform inside C,
without reference to the simple objects of Z(C). This is the primary objective of
this paper.
In order to fulﬁll this objective, it will be convenient to adopt an alte rna-
tive approach for constructing RT-like quantum invariants of 3-ma nifolds, due to
Lyubashenko [Lyu95] and later developed in [KL01, Vir06], where the input data
is a (non-necessarily linear neither semisimple) ribbon category B which admits a
coend C = ∫ X∈B ∨X ⊗X. This coend C is naturally endowed with a very rich
algebraic structure. In particular, it is a Hopf algebra in the braided category B
and comes equipped with a Hopf pairing ω : C ⊗C → /BD . Such a category B is
modular if the pairing ω is non-degenerate (this is the natural way of formulating
the invertibility of the S-matrix in this setting).
The construction of the Lyubashenko invariant consists in presen ting the 3-man-
ifold by surgery along a ribbon link L, using the universal property of the coend C
to associate a form φL to the link, and then evaluating this form on an integral Λ
of the Hopf algebra C. Note that, more generally, one can evaluate the form φL
by a ‘Kirby element’α of B to get other invariants τB(M ;α) of 3-manifold invari-
ants, see [Vir06]. In particular, up to normalization, τB(M ; Λ) is the Lyubashenko
invariant and, in the special case where B is a modular fusion category, τB(M ; Λ)
is the Reshetikhin-Turaev invariant.
In order to make this construction eﬀective, we need an algorithm f or computing
the forms φL which are deﬁned by universal property. Such an algorithm, based
on an encoding of certain tangles by means of Hopf diagrams , is given in [BV05].
Thus the invariants τB(M ;α) can be expressed in terms of certain structural mor-
phisms of the coend C. Section 2 is devoted to these quantum invariants and their
computation.
Hence, when C is a spherical fusion category, we may compute τZ(C)(M ; Λ) pro-
vided we can describe explicitly the structural morphisms of the coe nd of Z(C). In
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INV ARIANTS 3
other words, we need an algebraic interpretation of the center co nstruction. If C
is braided and has a coend A (which is a Hopf algebra), then the category Z(C)
coincides with the category of (right) A-modules in C. However the diﬃculty here
is that we don’t want to assume C is braided. To bypass this diﬃculty, we use the
notion of Hopf monad introduced in [BV07].
Hopf monads generalize Hopf algebras in a non-braided setting. In p articu-
lar, ﬁnite-dimensional Hopf algebras and their diﬀerent generalizat ions (Hopf al-
gebras in braided autonomous categories, quantum bialgebroids, e tc...) provide
examples of Hopf monads. If fact, any monoidal adjunction betwe en autonomous
categories gives rise to a Hopf monad. It turns out that much of th e theory of
ﬁnite-dimensional Hopf algebras extends to Hopf monads, see [BV0 7]. In Section 3,
we recall a few results on Hopf monads.
The whole point of introducing Hopf monads here is that they provide an al-
gebraic interpretation of the center construction [BV08]. If C is a centralizable
autonomous category, meaning that the coend Z(X) =
∫ Y ∈C ∨Y ⊗X ⊗Y exists
for any object X of C, then Z is a quasitriangular Hopf monad on C and the cen-
ter Z(C) coincides, as a braided category, with the category of Z-modules in C. In
addition, Drinfeld’s double construction extends naturally to Hopf m onads. This
theory provides a description of the coend of Z(C). In Section 4, we recall a few
facts on the double of Hopf monads.
In Section 5, we apply the above results to spherical fusion catego ries. Firstly,
we obtain a generalization of M¨ uger’s theorem on the modularity of t he center of
a spherical fusion category C to the case where dim C is not necessarily invertible
and k is any commutative ring. Denoting by {Vi}i∈I a (ﬁnite) representative family
of scalar objects of C, we get:
Z(X) =
⨁
i∈I
∨Vi ⊗X ⊗Vi,
Moreover Z(C) is centralizable and dim Z(C) = (dim C)2. The underlying object of
the coend of Z(C) is:
C =
⨁
i,j ∈I
∨Vi ⊗ ∨Vj ⊗ ∨∨Vi ⊗Vj,
and all structural morphisms of C (including its integral Λ : /BD →C) can be written
down explicitly in C. Furthermore, Z(C) is always modular. When k is an alge-
braically closed ﬁeld and dim C is invertible, then Z(C) is a fusion category and
so we recover M¨ uger’s theorem. However, when dim C is not invertible, Z(C) is a
non-semisimple ribbon category. Nevertheless, in this case, the ve rsionτZ(C)(M ; Λ)
of the Lyubashenko invariant is still deﬁned and computable in terms of C.
