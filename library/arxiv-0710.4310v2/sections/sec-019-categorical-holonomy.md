---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-019-categorical-holonomy
section_title: "Categorical holonomy"
section_number: null
pages: 22-25
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
2.3.1 Deﬁnition of a holonomy .
The following deﬁnition appears in [CP].
Deﬁnition 34 (Holonomy) LetM andN be smooth manifolds. Suppose that
M has a chosen base point ∗. A map F : π1
1(M, ∗) →N is said to be smooth if,
for any 2-path Γ : [0, 1]2 →M, with ∂l(Γ) = ∂r(Γ) = ∗, the map
s ∈ [0, 1] ↦→F ([γs]) ∈N
is smooth. Here Γ(t,s ) = γs(t), where s,t ∈ [0, 1].
LetG be a Lie group. A holonomy is, by deﬁnition, a smooth group mor phism
π1
1(M, ∗) →G.
The following result appears in [CP].
22
Theorem 35 Let M be a smooth manifold with a base point ∗. Let also G
be a Lie group. Let P → M be a smooth principal G-bundle over M with a
connectionω. Let u ∈P∗, the ﬁbre of P at ∗. Then the parallel transport of ω
determines a holonomy F 1
(ω,u) : π1
1(M, ∗) →G.
Proof. Recall the notation of 1.1.3. Given a 1-path γ : [0, 1] → M , with
γ(0),γ (1) = ∗, deﬁne F 1
(ω,u)(γ) to be the unique element of G such that u =
Hω(γ, 1,u )F 1
(ω,u)(γ). Then, if Γ is a 2-path, with ∂l(Γ) = ∂r(Γ) = ∗, it follows
that the map
s ∈ [0, 1] ↦→F 1
(ω,u)(γs) ∈G,
where Γ(t,s ) = γs(t);s,t ∈ [0, 1], is smooth. This follows from the fact that the
map t ∈ [0, 1] ↦→ Hω(γs,t,u ) is a solution of a diﬀerential equation in t. This
diﬀerential equation depends smoothly on s if Γ is smooth. For details see [KN,
page 74].
The fact that F 1
(ω,u) descends to a map π1
1(M, ∗) →G follows from lemma 2
and the fact that the horizontal lift of vectors deﬁnes a linear map . Finally the
fact that F 1
(ω,u) is a group morphism follows from the fact that Hω
(
γ2γ1, 1,u
)
=
Hω
(
γ1, 1, Hω(γ2, 1,u )
)
, for any smooth curves γ1 and γ2 in M starting and
ending at ∗.
It is proved in [CP] that any holonomy π1
1(M, ∗) →G arises from a bundle
with connection in this way.
2.3.2 Deﬁnition of a categorical holonomy
Deﬁnition 36 (3-path) LetM be a manifold. A smooth map J : [0, 1]3 →M ,
say J(t,s,x ) = Γ x(t,s ) = γx
s (t), wheret,s,x ∈ [0, 1], is said to be a 3-path if:
1. J is constant over {0} × [0, 1]2 and over {1} × [0, 1]2.
2. J restricts to a rank-1 homotopy (connecting γ0
0 withγ1
0) over [0, 1]×{0}×
[0, 1] and over [0, 1] × {1} × [0, 1] (connectingγ0
1 with γ1
1 ).
3. J has a product structure close to the boundary of [0, 1]3; see deﬁnition
19.
In particular J deﬁnes a homotopy connecting the 2-paths Γ 0 and Γ 1; see 1.3.6.
Note that it is not necessarily a rank-2 homotopy.
Deﬁnition 37 Let M and N be smooth manifolds. Consider the projection
map S2(M ) → S2(M ). A map F : S2(M ) →N is said to be smooth if, for any
3-pathJ, the map
x ∈ [0, 1] ↦→F ([Γx]) ∈N
is smooth. Here J(t,s,x ) = Γ x(t,s ), for each (t,s,x ) ∈ [0, 1]3.
Let G = (∂ : E →G,⊲ ) be a Lie crossed module. Consider the categorical
group C(G) constructed from G, see 1.2.1. Its set of objects is G and its set
of morphisms is the semidirect product G ⋉E of G and E; all of these are
23
smooth manifolds. The following deﬁnition extends the deﬁnition of ho lonomy
for principal G-bundles of [CP] and should be compared with analogous non-
strict constructions in [BS, MP, M].
Deﬁnition 38 (Categorical holonomy) LetM be a smooth manifold. Choose
an element ∗ ∈ M . A categorical holonomy is, by deﬁnition, a strict monoidal
functor (in other words a categorical group morphism) F : P2(M, ∗) → C (G),
such that the associated maps F1 : π1
1(M ) →G and F2 : P2(M, ∗) →G ⋉E on
the sets of objects and morphisms of P2(M, ∗) are smooth. Here P2(M, ∗) is the
thin fundamental categorical group of M ; see 1.3.4.
If we use the notation
[Γ] =
∂u([Γ])
↑[Γ]
∂d([Γ])
and ( X,e ) =
∂(e)−1X
↑e
X
,
to denote the morphisms of P2(M, ∗) and of C(G), then the tensor product of
two elements [Γ] and [Γ ′] of P2(M, ∗) can be presented in the suggestive form:
∂u([Γ])
↑[Γ]
∂d([Γ])
⊗
∂u([Γ ′])
↑[Γ ′]
∂d([Γ ′])
=
∂u([Γ])∂u([Γ ′])
↑[Γ] ◦h[Γ ′]
∂d([Γ])∂d([Γ ′])
(15)
In this notation, the condition that a functor F = (F1,F 2) : P2(M, ∗) → C (G)
be a strict monoidal functor means that:
F


∂u([Γ])
↑[Γ]
∂d([Γ])
⊗
∂u([Γ ′])
↑[Γ ′]
∂d([Γ ′])

 =
F1(∂u([Γ]))
↑F2([Γ])
F1(∂d([Γ]))
⊗
F1(∂u([Γ ′]))
↑F2([Γ ′])
F1(∂d([Γ ′]))
(16)
for each [Γ] , [Γ ′] ∈ P2(M, ∗). In other words:
F1
(
∂u([Γ])∂u([Γ ′])
)
↑F2([Γ] ◦h[Γ ′])
F1
(
∂d([Γ])∂d([Γ ′])
)
=
F1
(
∂u([Γ]))F1 (∂u([Γ ′]))
↑
(
F1(∂d[Γ])⊲F2([Γ ′])
)
F2([Γ])
F1 (∂d([Γ]))F1 (∂d([Γ ′]))
(17)
for each [Γ] , [Γ ′] ∈ P2(M, ∗); see 1.2.1. Recall that an arrow g
(g,e)
− − − →∂(e−1)g in
C(G) is sometimes simply denoted by g
e
− →∂(e−1)g, where g ∈G and e ∈E.
Since the category of crossed modules and the category of categ orical groups
are equivalent, we can give an alternative deﬁnition of a categorical holonomy,
and deﬁne it as being a smooth crossed module map
Π 2,1
2 (M, ∗) → G,
where the notion of a smooth crossed module map is the obvious one. Here
Π 2,1
2 (M, ∗) is the thin fundamental crossed module of the smooth manifold M ;
see 1.3.5.
24
