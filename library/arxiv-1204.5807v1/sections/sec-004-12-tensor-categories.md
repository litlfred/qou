---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-004-12-tensor-categories
section_title: "Tensor categories"
section_number: 1.2
pages: 3-4
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
---
3
objects in an abelian category C is denoted Irr C; we use the abbreviation
Irr A instead of Irr A- mod.
1.2. Tensor categories. We refer to [BaK, McL, EGNO, ENO, EO] for
basic results and terminology on tensor and monoidal categories. A monoidal
category is one with tensor product and unit, denoted 1; thus End(1) is a
monoid. A monoidal category is rigid when it has right and left dualities.
In this article, we understand by tensor category a monoidal rigid abelian
k-linear category, with End(1) ≃k. A particular important class of tensor
categories is that of fusion categories, that is semisimple tensor categories
with ﬁnite set of isomorphism classes of simple objects, that includes the
unit object, and ﬁnite-dimensional spaces of morphisms. Another important
class of tensor categories is that of braided tensor categories, i. e. those with
a commutativity constraint cV,W : V ⊗W →W⊗V for every objects V and
W. A braided vector space is a pair (V, c) where V is a vector space and
c ∈GL(V ⊗V ) satisﬁes (c⊗id)(id ⊗c)(c⊗id) = (id ⊗c)(c⊗id)(id ⊗c); this
notion is closely related to that of braided tensor category.
1.3. Hopf algebras. We use standard notation for Hopf algebras (always
assumed with bijective antipode); ∆, ε, S, denote respectively the comulti-
plication, the counit, and the antipode. For the ﬁrst, we use the Heyneman-
Sweedler notation ∆(x) = x(1) ⊗x(2). The tensor category of ﬁnite-dimen-
sional representations of a Hopf algebra H is denoted Rep H instead of
H- mod, to stress the tensor structure. There are two duality endo-functors
of Rep H composing the transpose of the action with either the antipode or
its inverse: if M ∈Rep H, then M∗= Hom(M, k) = ∗M, with actions
⟨h · f, m⟩= ⟨f, S(h) · m⟩,
⟨h · g, m⟩= ⟨g, S−1(h) · m⟩,
for h ∈H, f ∈M∗, g ∈∗M, m ∈M.
The tensor category of ﬁnite-dimensional corepresentations of a Hopf al-
gebra H, i. e. right comodules, is denoted Corep H. The coaction map of
V ∈Corep H is denoted ρ = ρV : V →V ⊗H; in Heyneman-Sweedler nota-
tion, ρ(v) = v(0) ⊗v(1), v ∈V . Also, the coaction map of a left comodule W
is denoted δ = δW : W →W ⊗H; that is, δ(w) = w(−1) ⊗w(0), w ∈W.
A Yetter-Drinfeld module V over a Hopf algebra H is simultaneously a
left H-module and a left H-comodule, subject to the compatibility condition
δ(h·v) = h(1)v(−1)S(h(3))⊗h(2)·v(0) for v ∈V , h ∈H. The category H
HYD of
Yetter-Drinfeld modules over H is a braided tensor category with braiding
c(v⊗w) = v(−1) · w⊗v(0), see e. g.
[AS2, Mo]; when dim H < ∞, H
HYD
coincides with the category of representations of the Drinfeld double D(H).
Let H be a Hopf algebra. A basic list of H-invariants is
• The group G(H) of group-like elements of H,
• the coradical H0 = largest cosemisimple subcoalgebra of H,
• the coradical ﬁltration of H.
4
ANDRUSKIEWITSCH, ANGIONO, GARCÍA IGLESIAS, TORRECILLAS, VAY
Assume that H0 is a Hopf subalgebra of H. In this case, another funda-
mental invariant of H is the inﬁnitesimal braiding, a Yetter-Drinfeld module
V over H0, see [AS2]. We shall consider two particular cases:
• The Hopf algebra H is pointed if H0 = kG(H).
• The Hopf algebra H is copointed if H0 = kG for a ﬁnite group G.
Recall that x ∈H is (g, 1) skew-primitive when ∆(x) = x⊗1 + g⊗x;
necessarily, g ∈G(H). If H is generated as an algebra by group-like and
skew-primitive elements, then it is pointed.
We shall need the description of Yetter-Drinfeld modules over kG, G a
ﬁnite group; these are G-graded vector spaces M = ⊕g∈GMg provided with a
G-module structure such that g·Mt = Mgtg−1 for any g, t ∈G. The category
kG
kGYD of Yetter-Drinfeld modules over G is semisimple and its irreducible
objects are parameterized by pairs (O, ρ), where O is a conjugacy class of G
and ρ ∈Irr CG(g), g ∈O ﬁxed. We describe the corresponding irreducible
Yetter-Drinfeld module M(O, ρ). Let g1 = g, . . . , gm be a numeration of O
and let xi ∈G such that xi g x−1
i
= gi for all 1 ≤i ≤m. Then
M(O, ρ) = IndG
CG(g) V = ⊕1≤i≤mxi ⊗V.
Let xiv := xi ⊗v ∈M(O, ρ), 1 ≤i ≤m, v ∈V . The Yetter-Drinfeld module
M(O, ρ) is a braided vector space with braiding given by
(1.1)
c(xiv ⊗xjw) = gi · (xjw) ⊗xiv = xh ρ(γ)(w) ⊗xiv
for any 1 ≤i, j ≤m, v, w ∈V , where gixj = xhγ for unique h, 1 ≤h ≤m,
and γ ∈CG(g). Now the categories kG
kGYD and kG
kGYD are tensor equivalent,
so that a similar description of the objects of the latter holds, see e. g. [AV1].
The following notion is appropriate to describe all braided vector spaces
arising as Yetter-Drinfeld modules over some ﬁnite abelian group. A braided
vector space (V, c) is of diagonal type if there exist qij ∈k× and a basis
{xi}i∈I of V such that c(xi⊗xj) = qijxj⊗xi, for each pair i, j ∈I. In such
case, we say that i, j ∈I are connected if there exist ik ∈I, k = 0, 1, . . . , n,
such that i0 = i, in = j, and qik−1,ikqik,ik−1̸ = 1, 1 ≤k ≤n. It establishes
an equivalence relation on I. The equivalence classes are called connected
components, and V is connected if it has a unique component.
When H = kΓ, where Γ is a ﬁnite abelian group, each V ∈H
HYD is a
braided vector space of diagonal type.
Indeed, V = ⊕g∈Γ,χ∈bΓV χ
g , where
Vg = {v ∈V | δ(v) = g ⊗v}, V χ = {v ∈V | g · v = χ(g)v for all g ∈Γ},
V χ
g = V χ ∩Vg. Note that c(x ⊗y) = χ(g)y ⊗x, for each x ∈Vg, g ∈Γ,
y ∈V χ, χ ∈bΓ. On the other hand, we can realize every braided vector space
of diagonal type as a Yetter-Drinfeld module over the group algebra of an
appropriate abelian group.
