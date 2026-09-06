---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-021-a-well-known-lemma
section_title: "A well-known lemma"
section_number: null
pages: 27-27
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
Let G be a Lie group. Consider a g-valued smooth function V (s,x ) deﬁned on
[0, 1]2. Consider the following diﬀerential equation in G:
∂
∂sa(s,x ) = a(s,x )V (s,x ),
with initial condition a(0,x ) = 1G, ∀x ∈ [0, 1]. We want to know ∂
∂xa(s,x ).
Let θ be the canonical g-valued 1-form on G. Thus θ is left invariant and
satisﬁes θ(A) = A, ∀A ∈ g, being deﬁned uniquely by these properties. Also
dθ(A,B ) = −θ([A,B ]), (21)
where A,B ∈ g. We have:
∂
∂xθ
(∂
∂sa(s,x )
)
= ∂
∂xθ
(
a(s,x )V (s,x )
)
= ∂
∂xV (s,x ).
On the other hand:
∂
∂xθ
(∂
∂sa(s,x )
)
=da∗(θ)
( ∂
∂x, ∂
∂s
)
+ ∂
∂sa∗(θ)
( ∂
∂x
)
+a∗(θ)
([ ∂
∂x, ∂
∂s
])
=dθ
( ∂
∂xa(s,x ), ∂
∂sa(s,x )
)
+ ∂
∂sθ
( ∂
∂xa(s,x )
)
.
Therefore:
θ
( ∂
∂xa(s,x )
)
=
∫ s
0
(
−dθ
( ∂
∂xa(s′,x ), ∂
∂s′a(s′,x )
)
+ ∂
∂xV (s′,x )
)
ds′ +θ
( ∂
∂xa(0,x )
)
.
Since ∂
∂xa(0,x ) = 0 (due to the initial conditions) we have the following:
Lemma 41
∂
∂xa(s,x ) = a(s,x )
∫ s
0
(
−dθ
( ∂
∂xa(s′,x ), ∂
∂s′a(s′,x )
)
+ ∂
∂xV (s′,x )
)
ds′,
for each x,s ∈ [0, 1].
