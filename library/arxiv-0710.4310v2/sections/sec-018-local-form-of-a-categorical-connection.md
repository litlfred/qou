---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-018-local-form-of-a-categorical-connection
section_title: "Local form of a categorical connection"
section_number: null
pages: 20-22
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
Let G = (∂ : E →G,⊲ ) be some Lie crossed module, and let G = (∂ : e → g,⊲ )
be the associated diﬀerential crossed module. Fix a smooth manifold M and
a smooth principal G-bundle P → M , with a categorical G-connection (ω,m ),
where, as usual, ω ∈ A1(P, g) and m ∈ A2(P, e).
The local form of the categorical G-connection (ω,m ) is similar to the local
form of a connection. Let {Uα} be an open covering of the manifold M . We can
suppose that each Uα is contractible and that, for each α andβ, the intersection
Uα ∩Uβ is contractible; see [BT]. Therefore, for each α, the restriction Pα of
P to Uα is trivial, and, in particular, it admits a section fα : Uα → Pα. The
local form of a categorical G-connection is therefore given by the family of forms
ωa =f ∗
α(ω) and mα =f ∗
α(m).
For eachα, by the structure equation, the local curvature form Ω α =f ∗
α(Ω)
takes the form
Ωα =dωα + 1
2ωα ∧adωα.
20
Locally, the Bianchi identity reads:
dΩα +ωα ∧ad Ωα = 0.
Analogously, from the 2-structure equation, locally in each Uα, the 2-curvature
3-form Mα =f ∗
α(M) takes the form:
Mα =dmα +ωα ∧⊲mα,
and the 2-Bianchi identity reads:
dMα +ωα ∧⊲ Mα = 0.
These local expressions correspond to the formulae in [B] when the fake curva-
ture vanishes.
Let φα,β : Ua ∩Uβ → G be deﬁned as fα(x)φα,β (x) = fβ(x), for each x ∈
Uα ∩Uβ. We have:
ωβ(X) = φ−1
α,βω(X)φα,β +φ−1
α,βdφα,β, (11)
Ωβ(X,Y ) = φ−1
α,βΩ(X,Y )φα,β, (12)
for each X,Y ∈ X(M ). Since both m and M are G-equivariant and horizontal,
it follows that for each α,β :
mβ(X,Y ) = φ−1
α,β⊲mα(X,Y ), (13)
Mβ(X,Y,Z ) = φ−1
α,β⊲ Mα(X,Y,Z ), (14)
for each X,Y,Z ∈ X(M ).
Lemma 32 LetM be a smooth manifold. Let also G = (∂ : E →G,⊲ ) be a Lie
crossed module, and let G = (∂ : e → g,⊲ ) be the associated diﬀerential crossed
module. Suppose π : P →M is the trivial bundle M ×G. Given m0 ∈ A2(M, e)
and ω0 ∈ A1(M, g), such that ∂(m0) = Ω 0 = dω0 + 1
2ω0 ∧adω0, there exists a
categorical G-connection (ω,m ) on P such that its local form is (ω0,m 0).
Proof. Let θ be the canonical g-valued left-invariant 1-form on G; see 2.4.2.
Thenω =g−1π∗(ω0)g +θ is a connection 1-form on M ×G, and its local form,
considering the section f : M → P such that, for each x ∈ M , f (x) = (x, 1G),
is ω0. The 2-form π∗(m0) ∈ A2(P, e) is horizontal. However, it is not G-
equivariant. Therefore we deﬁne m ∈ A2(M ×G, e) as being such that, given
X,Y ∈T(x,g)P , we have:
m(X,Y ) = g−1⊲π ∗(m0)(X,Y ),
whereg ∈G,x ∈M andX,Y ∈T(x,g)M ×G. This 2-form is obviously smooth
and horizontal. Moreover, given X,Y ∈T(x,g)P it follows that:
(R∗
hm)(X,Y ) = m(Xh,Yh )
= (gh)−1⊲π ∗(m0)(Xh,Yh )
=h−1g−1⊲π ∗(m0)(X,Y )
=h−1⊲m (X,Y ).
21
Therefore m is G-equivariant. Let Ω be the curvature of ω. Then Ω( X,Y ) =
g−1π∗(Ω 0)(X,Y )g, where as before X,Y ∈T(x,g)P . In particular it follows that
Ω = ∂(m).
The following follows from the previous discussion.
Corollary 33 Let M be a smooth manifold. Let also G = (∂ : E →G,⊲ ) be
a Lie crossed module, and let G = (∂ : e → g,⊲ ) be the associated diﬀerential
crossed module. Let {Uα} be an open cover of M , such that the restriction Pα
of P to Uα is the trivial bundle. Let also fα : Uα → Pα be local sections of
P . Deﬁne φα,β : Uα ∩Uβ → G as fα(x)φα,β (x) = fβ(x). Suppose that for
each α we are given forms ωα ∈ A1(Uα, g) and mα ∈ A2(Uα, e), satisfying
∂(mα) = Ω α = dωα + 1
2ωα ∧adωα. Moreover, suppose that for each α,β with
Uα ∩Uβ ⁄= ∅ equations (11) and (13) are satisﬁed. There exists a unique c at-
egorical connection (ω,m ) on P such that the forms ωα and mα are its local
form.
The trivial bundle M ×G → M always admits the trivial categorical con-
nection, whose local form is given by the forms ω0 = 0 and m0 = 0. However,
there exist several other examples for the trivial bundle. Let A =∂(E), and let
a be its Lie algebra. There exists a linear map r : a → e such that ∂ ◦r = id a.
Letω0 be any a-valued 1-form on M . Let Ω 0 be the curvature of ω0 and deﬁne
m0 = r(Ω 0). Then ( ω0,m 0) is the local form of a categorical G-connection on
M ×G. In fact, let B = ker∂ ⊂E. Therefore B is closed under the action of G
on E, by the ﬁrst condition of the deﬁnition of crossed modules; see deﬁ nition
3. Let b be the Lie algebra of B. Given any b-valued 2-form ρ0 on M then
ρ0 +m0 is the local form of a categorical G-connection on M ×G.
It is not a trivial problem whether there always exists a categorical G-
connection on any principal G-bundle. This issue is very likely to depend on the
topology of the manifold. The strategy of combining locally deﬁned co nnection
1-forms ω using a partition of unity cannot be carried through for the 2-form s
m, since ∂(m) = Ω, which is not C ∞-linear in ω.
