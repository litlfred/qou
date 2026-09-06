---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-027-associating-2-holonomies-to-embedded-spheres
section_title: "Associating 2-holonomies to embedded spheres"
section_number: null
pages: 41-43
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
Let G = (∂ : E →G,⊲ ) be a Lie crossed module. Let M be a smooth mani-
fold. Consider a principal G-bundle P overM with a G-categorical connection
(ω,m ). Consider an embedded oriented 2-sphere Σ ⊂ M . We want to deﬁne
the categorical holonomy of Σ, which we call a Wilson Sphere, by analogy with
Wilson loops, familiar in gauge theory.
Deﬁnition 48 Choose an orientation preserving parametrisation
S2 = D2/∂D2 φ
− →Σ ⊂M
of Σ . Let ∗ = φ(∂D2) ∈ Σ ⊂ M . Choose u ∈ P∗, the ﬁbre of P at ∗. The
categorical holonomy of Σ is deﬁned as:
W(ω,m)(Σ,φ,u ) = F 2
(ω,m,u)(φ) ∈ ker(∂) ⊂E.
The fact that the categorical holonomy W(ω,m)(Σ,φ,u ) lives in ker( ∂) ⊂ E
follows from the fact that ∂d(φ) = ∂u(φ) = ∗, and lemma 40.
Theorem 49 The categorical holonomy W(ω,m)(Σ,φ,u ) does not depend on φ
and u, up to acting by an element of G. Therefore, we can deﬁne a categorical
holonomy W(ω,m)(Σ) of embedded 2-spheres Σ in M (the Wilson Sphere), tak-
ing values in E/G. If Σ ∗ is obtained from Σ by reversing its orientation then
W(ω,m)(Σ ∗) =
(
W(ω,m)(Σ)
) −1
.
41
Example 50 Consider the U (1)-bundle Pn over S2 with Chern class n, where
n ∈ Z. Deﬁne a crossed module G given by the exponential map exp :iR →U (1),
considering the trivial action of U (1) on iR. Consider some connection 1-form
ω on Pn, thus (ω, Ω) is a categorical G-connection on Pn. We will then have
that W(ω,Ω) (S2) = n.
Proof. (Theorem 49) The independence of W(ω,m)(Σ,φ,u ) on the choice
of u ∈P∗, up to acting by an element of G, follows from theorem 46.
Choose a diﬀerent orientation preserving parametrisation D 2/∂D2 φ′
− →Σ
of Σ. Since both φ and φ′ are orientation preserving, there exists a smooth 1-
parameter family of embeddings x ∈ [0, 1] ↦→φx connectingφ andφ′. Here φx is
an orientation preserving parametrisation φx : D 2/∂D2 → Σ, for each x ∈ [0, 1].
Let q : [0, 1] → M be the map such that q(x) = φx(∂([0, 1]2)), ∀x ∈ [0, 1];
therefore ∗ = q(0). Put Γ x(t,s ) .= φx(t,s ), where t,s,x ∈ [0, 1]. Therefore
∂l(Γx) = ∂r(Γx) = q(x), for each x ∈ [0, 1]. Let also J(t,s,x ) .= Γx(t,s ), where
t,s,x ∈ [0, 1].
The map J : [0, 1]3 → Σ ⊂ M satisﬁes the conditions of theorem 42. In
particular
W(ω,m)(Σ,φ 0,u ) = eΓ 0 =eΓ 1 = W(ω,m)(Σ,φ 1, Hω(q, 1,u )),
since certainly Rank( DzJ) ≤ 2, ∀z ∈ [0, 1]3.
Finally, let φ−1(x,y ) = φ(1 −x,y ); ∀x,y ∈ [0, 1]. It does not follow that
φ−1 ◦hφ is rank-2 homotopic to ∗ in a strict sense, since a homotopy connecting
φ−1 ◦hφ with ∗ will have some singular points, as φ and φ−1 are not 2-paths,
because they fail the sitting instant conditions.
Let γs(t) = φ(t,s ) and γ′
s(t) = φ−1(t,s ), where t,s ∈ [0, 1]. Let us analyse
eφ−1(s) directly. We have:
d
dseφ−1(s) = eφ−1(s)
∫ 1
0
m
(
~∂
∂tγ′s(t),
~∂
∂sγ′s(t)
)
Hω (γ′
s,t,u)
dt
= −eφ−1(s)
∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,ugγ ′s )
dt
Therefore:
d
dseφ−1(s) = −eφ−1(s)
(
g−1
γ′s
⊲
∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt
)
= −eφ−1(s)
(
∂
(
e−1
φ−1(s)
)
⊲
∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt
)
= −
(∫ 1
0
m
( ~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt
)
eφ−1(s).
42
The result follows from the fact that if A(t) is a smooth function [0, 1] →E and if
w(s) is a solution of d
dsw(s) = w(s)A(s) then the smooth function v(s) .=w(s)−1
is a solution of d
dsv(s) = −A(s)v(s). In particular eφ−1(1) = e−1
φ (1).
Note that the previous proof uses, in an essential way, the fact t hat the
mapping class group of S2 is {±1}. Therefore, it is likely that the previous
theorem does not extend to an embedded surface of genus great er than zero.
However, it is probable that this can be ﬁxed if any embedded surfac e Σ ⊂M
is assigned an equivalence class of embedding S → Σ, where two embeddings
φ,φ ′ : S → Σ are equivalent if φ−1 ◦φ′ is isotopic to the identity diﬀeomorphism.
We will analyse this issue in a subsequent publication.
