---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-020-categorical-connections-and-categorical-connecti
section_title: "Categorical connections and categorical connection holonomies"
section_number: null
pages: 25-27
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
The aim of this subsection is to prove the following main theorem.
Theorem 39 LetG be a Lie group. Let M be a smooth manifold. Let also P →
M be a smooth principal ﬁbre bundle with structure group G. Let G = (∂ : E →G,⊲ )
be a Lie crossed module. A G-categorical connection (ω,m ) on P together with
an element u ∈P∗, the ﬁbre of P over ∗ ∈ M , determines a categorical holonomy
F(ω,m,u) : P2(M, ∗) → C (G), which we call a categorical connection holonomy,
since it arises from a categorical connection.
For the rest of this subsection, ﬁx a Lie crossed module G = (∂ : E →G,⊲ ),
and let G = (∂ : e → g,⊲ ) be the associated diﬀerential crossed module. Consider
also a smooth manifold M and a principal G-bundle P overM , as well as a G-
categorical connection (ω,m ) on P .
2.4.1 Deﬁning a categorical holonomy from a categorical con nection
Consider a base point ∗ ∈ M . Choose also u ∈ P∗, the ﬁbre of P at ∗. To
describeF(ω,m,u) on the set π1
1(M, ∗) of objects of P2(M, ∗), we use theorem 35.
Therefore we deﬁne:
F 1
(ω,m,u)([γ]) = F 1
(ω,u)([γ]), where [γ] ∈π1
1(M, ∗). (18)
Let now Γ be a 2-path in M with∂l(Γ) = ∂r(Γ) = ∗. Let γs(t) = Γ(t,s );s,t ∈
[0, 1]. To deﬁne F 2
(ω,m,u), consider the smooth function s ∈ [0, 1] ↦→eΓ (s) ∈E,
which solves the following diﬀerential equation in E:
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
dt, (19)
with initial condition eΓ (0) = 1E. SeteΓ =eΓ (1) to be the element of E assigned
to the 2-path Γ. Then we deﬁne:
F 2
(ω,m,u)(Γ) =
(
F 1
(ω,u)
(
[∂d(Γ)]
)
,e Γ
)
. (20)
Recall the elements gγs ∈ G, where s ∈ [0, 1], which are given by the
condition: ugγs = Hω(γs, 1,u ); see 1.1.4. Thus F 1
(ω,m,u)([γs]) = g−1
γs , where
g−1
γs
.=
(
gγs
) −1
. In local coordinates, our deﬁnition of a categorical holonomy
coming from a categorical connection coincides with deﬁnition 2.32 of [BS].
We will prove that F(ω,m,u) =
(
F 1
(ω,m,u),F 2
(ω,m,u)
)
deﬁnes a categorical
holonomy P2(M, ∗) → C (G). Explicitly, we need to prove that the assignment:
∂u(Γ)
↑Γ
∂d(Γ)
↦→
g−1
γ1
↑eΓ
g−1
γ0
,
25
where Γ is a 2-path in M such that∂l(Γ) = ∂r(Γ) = ∗, and Γ(t,s ) = γs(t); ∀s,t ∈
[0, 1], depends only on the rank-2 homotopy class to which Γ belongs, an d deﬁnes
a monoidal functor P2(M, ∗) → C (G), such that the induced maps on the set of
objects and morphisms of P2(M, ∗) are smooth.
First of all:
Lemma 40 Let Γ be a 2-path in M with ∂l(Γ) = ∂r(Γ) = ∗. Then for each
s ∈ [0, 1] we have: gγ0∂(eΓ (s)) = gγs. Here Γ(t,s ) = γs(t); ∀s,t ∈ [0, 1].
Proof. The previous equation holds for s = 0, by deﬁnition of eΓ (s). We have:
d
ds
(
gγ0∂(eΓ (s))
)
=gγ0
d
ds∂ (eΓ (s)) = gγ0∂
(d
dseΓ (s)
)
,
therefore:
d
ds
(
gγ0∂(eΓ (s))
)
=gγ0∂
(
eΓ (s)
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
=gγ0∂(eΓ (s))
∫ 1
0
Ω
( ~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt,
since ∂(m) = Ω. By equation (7) we also have:
d
dsgγs =gγs
∫ 1
0
Ω
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
.
Thus both sides of the equation are solutions of the same diﬀerentia l equation
in G, and have the same initial condition.
We remark that, using the terminology of [BS], this result correspon ds to
the condition that a local pre-2-holonomy gives rise to a local true 2 -holonomy,
which there also follows from the vanishing of the fake curvature.
Let Γ : [0 , 1]2 → M be a 2-path in M with ∂l(Γ) = ∂r(Γ) = ∗. We need
to prove that F 2
(ω,m,u)(Γ) depends only on the 2-track deﬁned by Γ, in other
words on the rank-2 homotopy class of 2-paths to which Γ belongs. This will
be shown shortly in Corollary 43 of Theorem 42. For now, consider a 3 -pathJ,
where J(t,s,x ) = Γ x(t,s ); ∀t,s,x ∈ [0, 1], deﬁning a homotopy (not necessarily
rank-2) connecting the 2-paths Γ 0 and Γ 1. Suppose that ∂l(Γ 0),∂r(Γ 0) = ∗,
thus∂l(Γ 1),∂r(Γ 1) = ∗. We want to calculate ∂
∂xeΓ x(s), where s,x ∈ [0, 1].
In fact, for later applications, we will consider the more general ca se when,
for each x ∈ [0, 1], we have that ∂l(Γx) = q(x) and ∂r(Γx) = q(x), where
q : [0, 1] → M is a smooth map. This generality will be important to deﬁne
Wilson spheres in 2.5.3. The lemma in the following subsection will be usefu l
for our purpose.
26
