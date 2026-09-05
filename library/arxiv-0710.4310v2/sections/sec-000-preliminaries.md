---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-000-preliminaries
section_title: "Preliminaries"
section_number: null
pages: 4-5
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
1.1 Resum´ e of results and notation from the theory of
principal ﬁbre bundles
1.1.1 Connections on principal ﬁbre bundles
For full details on connections on principal ﬁbre bundles see [KN, P].
Let M be a paracompact smooth manifold. Let G be a Lie group with Lie
algebra g. Consider a principal G-bundle P overM , with canonical projection
π : P →M . For each x ∈M , let Px =π−1(x) be the ﬁbre at x. Let also X(P )
denote the Lie algebra of smooth vector ﬁelds on P . Recall that there exists a Lie
algebra morphism A ∈ g ↦→A# ∈ X(P ), such that A#
u = d
dtu exp(tA)t=0, ∀u ∈
P, ∀A ∈ g. Here if X ∈ X(P ) is a vector ﬁeld then Xu ∈TuP (the tangent space
of P at u ∈P ) denotes the value of X at the point u.
Denote the right action of G on P as g ∈G ↦→Rg ∈ diﬀ(P ), where diﬀ( P )
denotes the diﬀeomorphism group of P . Recall the following very useful formula:
(Rg)∗(A#) =
(
g−1Ag
) #
,
4
whereg ∈G andA ∈ g. Given an element u ∈P , recall that a vector Xu ∈TuP
is said to be vertical if π∗(Xu) = 0. Let TV
u P denote the subspace of vertical
vectors in TuP . Notice that any Xu ∈TV
u P is of the form A#
u for some A ∈ g,
and this correspondence is one-to-one.
Letω ∈ A1(P, g) be a connection on P . In other words ω is a smooth 1-form
on P with values in g such that:
1. R∗
g(ω) = g−1ωg, ∀g ∈G,
2. ω(A#) = A, ∀A ∈ g.
Given an element u ∈ P , let TH
u P = {Xu ∈ TuP : ω(Xu) = 0 }, the horizontal
subspace at u ∈P . Then TH
u is a complementary subspace of TV
u P in TuP for
eachu ∈P . Moreover, the following identity holds for each g ∈G and u ∈P :
(
TH
u P
)
g =TH
ugP.
The natural projection maps X ∈ TP ↦→XH and X ∈ TP ↦→XV are
smooth. Here TP denotes the tangent bundle of P . There exists also a unique
map X ∈ X(M ) ↦→~X ∈ X(P ), called the horizontal lift of X ∈ X(M ), such
that ~Xu ∈ TH
u P, ∀u ∈ P and π∗(~X) = X, for any X ∈ X(M ), the Lie algebra
of smooth vector ﬁelds on M . Note that this horizontal lift gives rise to linear
mapsTxM →TuP , if π(u) = x, where x ∈M andu ∈P . The horizontal lift of
a vector ﬁeld X ∈ X(M ) is always G-invariant. In other words:
~Xg = ~X, ∀g ∈G.
