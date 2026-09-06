---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-023-re-scaling
section_title: "Re-scaling"
section_number: null
pages: 33-37
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
Let Γ be a 2-path in M such that ∂l(Γ) = ∂r(Γ) = ∗. As usual put Γ( t,s ) =
γs(t);s,t ∈ [0, 1]. Consider a smooth map f : [a,b ] → [0, 1], where −∞ < a <
b< +∞. We suppose that f (a) = 0 and f (b) = 1. Let Γ ′(s,t ) = γ′
s(t) be such
that γ′
s(t) = γf (s)(t), where s ∈ [a,b ] and t ∈ [0, 1]. Even though Γ ′ is not a
2-path, for its domain is [0 , 1] × [a,b ], the elements gγ′
s ∈ E and eΓ ′(s) ∈ E,
where s ∈ [a,b ], deﬁned in 2.4.1, still make sense.
Lemma 44 We have
gγ′s =gγf (s) and eΓ ′(s) = eΓ (f (s)),
for each s ∈ [a,b ].
Proof. The ﬁrst equation follows since γ′
s = γf (s), as curves [0 , 1] → M , for
eachs ∈ [a,b ]. As for the second one we have:
d
dseΓ ′(s) = eΓ ′(s)
∫ 1
0
m
(
~∂
∂t Γ ′(t,s ),
~∂
∂s Γ ′(t,s )
)
Hω (γ′s,t,u)
dt
=eΓ ′ (s) d
dsf (s)
∫ 1
0
m
(
~∂Γ
∂t (t,f (s)),
~∂Γ
∂s (t,f (s))
)
Hω (γf (s),t,u)
dt.
Whereas:
d
dseΓ (f (s)) = eΓ (f (s)) d
dsf (s)
∫ 1
0
m
(
~∂Γ
∂t (t,f (s)),
~∂Γ
∂s (t,f (s))
)
Hω (γf (s),t,u)
dt.
Therefores ↦→eΓ ′(s) ands ↦→eΓ (f (s)) are both solutions of the same diﬀerential
equation and they have the same initial conditions.
33
2.4.5 V eriﬁcation of the axioms for a categorical holonomy
Let G = (∂ : E →G,⊲ ) be a Lie crossed module and let G = (∂ : e → g,⊲ ) be the
associated diﬀerential crossed module. Fix a smooth manifold M with a base
point ∗, a principal G-bundle P overM and an element u ∈P∗, the ﬁbre of P
over ∗. Consider a categorical connection ( ω,m ) on P . Let us prove that the
assignments
[γ] ∈π1
1(M, ∗) ↦→F 1
(ω,u)([γ]) ∈G
and
[Γ] ∈ P2(M, ∗) ↦→F 2
(ω,m,u)([Γ]) ∈G ⋉E,
deﬁned in 2.4.1, yield a categorical holonomy F(ω,m,u) : P(M, ∗) → C (G). To
begin with, let us see that F(ω,m,u) deﬁnes a monoidal functor P2(M, ∗) → C (G).
Here C(G) is the categorical group constructed from G; see 1.2.1.
Claim: F(ω,m,u) is a functor.
Proof. Recall that the source and target maps in a category are denoted
by σ and τ , respectively. Let Γ be a 2-path in M such that ∂l(Γ),∂r(Γ) = ∗.
As usual put Γ( t,s ) = γs(t);t,s ∈ [0, 1]. We have:
σ
(
F 2
(ω,m,u)([Γ])
)
=σ
(
g−1
γ0 ,e [Γ]
)
=g−1
γ0 =F1 (σ([Γ])).
On the other hand by lemma 40:
τ
(
F 2
(ω,m,u)([Γ])
)
=τ
(
g−1
γ0 ,e [Γ]
)
=∂(e−1
Γ )g−1
γ0 =g−1
γ1 =F1 (τ ([Γ])).
Therefore we can represent F(ω,m,u) as:
∂u([Γ])
↑[Γ]
∂d([Γ])
∈ P 2(M, ∗) ↦− →
g−1
γ1 =∂(eΓ )−1g−1
γ0
↑eΓ
g−1
γ0
∈ C (G),
where, as usual, Γ( t,s ) = γs(t);s,t ∈ [0, 1].
Let Γ 1 and Γ 2 be 2-paths in M with∂l(Γ 1),∂r(Γ 1) = ∗ and∂l(Γ 2),∂r(Γ 2) =
∗. Suppose also that ∂u(Γ 1) = ∂d(Γ 2). For each s,t ∈ [0, 1], put Γ 1(t,s ) = γ1
s (t)
and Γ 2(t,s ) = γ2
s (t). Let Γ = Γ 1 ◦v Γ 2. Put Γ( t,s ) = γs(t);s,t ∈ [0, 1]. Suppose
s ∈ [0, 1/2]. We have:
d
dseΓ (s) = eΓ (s)
∫ 1
0
m
( ~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt.
By lemma 44, eΓ (1/2) = eΓ 1. Let e′
Γ (s) = eΓ (1/2)−1eΓ (s), where s ∈ [1/2, 1].
Then:
d
dse′
Γ (s) = e′
Γ (s)
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
dt.
34
Sincee′
Γ (1/2) = 1E, it follows, by lemma 44, that e′
Γ =eΓ 2. Putting everything
together yields eΓ =eΓ 1eΓ 2. Therefore we have:
F 2
(ω,m,u)


∂u([Γ 2])
↑[Γ 2]
∂d([Γ 2])
↑[Γ 1]
∂d([Γ 1])


=
F 1
(ω,m,u)
(
∂u([Γ 2])
)
↑F 2
(ω,m,u )
(
[Γ 2]
)
F 1
(ω,m,u)
(
∂u([Γ 1])
)
↑F 2
(ω,m,u )
(
[Γ 1]
)
F 1
(ω,m,u)
(
∂d([Γ 1])
)
given any two elements [Γ 1] and [Γ 2] of P2(M, ∗), with ∂d(Γ 2) = ∂u(Γ 1).
If we are given elements [Γ 1] and [Γ 2] of P2(M, ∗), such that ∂d([Γ 2]) =
∂u([Γ 1]), then, for some representatives Γ 1
1 ∈ [Γ 1] and Γ 2
1 ∈ [Γ 2]) we have
∂d(Γ 2
1) = ∂u(Γ 1
1). For example, take a rank-1 homotopy H connecting ∂u(Γ 1)
with ∂d(Γ 2), and put Γ 1
1 = Γ 1 ◦vH and Γ 2
1 = Γ 2. Hence F(ω,m,u) : P2(M, ∗) →
C(G) is a functor.
Claim: F(ω,m,u) is a monoidal functor.
Proof. Let Γ 1 and Γ 2 be 2-paths in P2(M, ∗). Let also Γ = Γ 1 ◦h Γ 2. Put
Γ 1(s,t ) = γ1
s (t), Γ 2(s,t ) = γ2
s (t) and Γ( s,t ) = γs(t). Here s,t ∈ [0, 1]. We want
to prove that eΓ (s) =
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1(s) for any s ∈ [0, 1]; see 1.2.1. Note
that this equation holds for s = 0. Furthermore we have:
d
ds
((
g−1
γ1
0
⊲e Γ 2 (s)
)
eΓ 1(s)
)
=
(
g−1
γ1
0
⊲ d
dseΓ 2(s)
)
eΓ 1(s) +
(
g−1
γ1
0
⊲e Γ 2(s)
) d
dseΓ 1 (s)
=
(
g−1
γ1
0
⊲
(
eΓ 2(s)
∫ 1
0
m
(
~∂
∂tγ2s (t),
~∂
∂sγ2s (t)
)
Hω (γ2
s,t,u)
dt
))
eΓ 1(s)
+
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1(s)
∫ 1
0
m
(
~∂
∂tγ1s (t),
~∂
∂sγ1s (t)
)
Hω (γ1s,t,u)
dt
=Cs +Ds.
35
Let us analyse each of the terms above separately:
Cs =
(
g−1
γ1
0
⊲e Γ 2(s)
)(
g−1
γ1
0
⊲
∫ 1
0
m
( ~∂
∂tγ2s (t),
~∂
∂sγ2s (t)
)
Hω (γ2s,t,u)
dt
)
eΓ 1 (s)
=
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1(s)
((
∂(eΓ 1(s))−1g−1
γ1
0
)
⊲
∫ 1
0
m
(
~∂
∂tγ2s (t),
~∂
∂sγ2s (t)
)
Hω (γ2
s,t,u)
dt
)
=
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1(s)
(
g−1
γ1
s
⊲
∫ 1
0
m
(
~∂
∂tγ2s (t),
~∂
∂sγ2s (t)
)
Hω (γ2s,t,u)
dt
)
.
Given that m is G-equivariant, given X,Y ∈ X(M ) we have:
g−1⊲m (~X,~Y )v =m(~Xg, ~Yg )vg =m(~X,~Y )vg. (30)
Here v ∈P and g ∈G. Therefore (recall γs =γ1
sγ2
s ):
Cs =
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1 (s)
∫ 1
0
m
(
~∂
∂tγ2s (t),
~∂
∂sγ2s (t)
)
Hω (γ2s,t,u)gγ 1s
dt
=
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1 (s)
∫ 1
0
m
( ~∂
∂tγ2s (t),
~∂
∂sγ2s (t)
)
Hω (γ2s,t,ugγ 1s
)
dt
=
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1 (s)
∫ 1
1/2
m
( ~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt.
On the other hand
Ds =
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1(s)
∫ 1/2
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt.
Putting everything together it follows that:
d
ds
((
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1(s)
)
=
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1(s)
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
dt.
Therefore s ∈ [0, 1] ↦→
(
g−1
γ1
0
⊲e Γ 2(s)
)
eΓ 1(s) ∈E and s ∈ [0, 1] ↦→eΓ (s) ∈E are
both solutions of the same diﬀerential equation in E and have the same initial
condition.
36
In particular
(
g−1
γ1
0
⊲e Γ 2
)
eΓ 1 =eΓ . Therefore:
F


∂u([Γ 1])
↑[Γ 1]
∂d([Γ 1])
⊗
∂u([Γ 2])
↑[Γ 2]
∂d([Γ 2])

 =
g−1
γ1
1
g−1
γ2
1↑
„
g−1
γ 1
0
⊲eΓ 2
«
eΓ 1
g−1
γ1
0
g−1
γ2
0
=
F1
(
∂u([Γ 1])
)
↑F2([Γ 1])
F1
(
∂d([Γ 1])
)
⊗
F1
(
∂u([Γ 2])
)
↑F2
(
[Γ 2]
)
F1
(
∂d([Γ 2])
)
.
We have therefore proven that F(ω,m,u) : P2(M, ∗) → C (G) is a monoidal
functor, and therefore a categorical group map.
Claim: The functor F(ω,m,u) : P2(M, ∗) → C (G) is smooth both on the sets
π1
1(M, ∗) and P2(M, ∗) of objects and morphisms of P2(M, ∗).
Proof. This follows directly from the deﬁnition of F(ω,m,u), and from the
lemma on page 74 of [KN].
The proof of theorem 39 is complete.
