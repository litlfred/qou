---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-022-the-dependence-of-the-surface-holonomy-on-a-smoo
section_title: "The dependence of the surface holonomy on a smooth family of surfaces"
section_number: null
pages: 27-33
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
of surfaces
The discussion in this subsection will be very similar to that of 1.1.4. We w ant
to prove an analogue of lemma 2 for the surface holonomy of a family o f 2-paths
Γx.
Consider a smooth map J : [0, 1]3 →M , where J(t,s,x ) = Γ x(t,s ); ∀t,s,x ∈
[0, 1]. Given x,s ∈ [0, 1], a smooth curve γx
s : [0, 1] → M is deﬁned as γx
s (t) =
27
J(t,s,x ), where t,s,x ∈ [0, 1]. Suppose that, for each x ∈ [0, 1], there exists
q(x) ∈ M such that J(0,s,x ) = J(1,s,x ) = q(x) for each s ∈ [0, 1]. In other
words ∂l(Γx) = ∂r(Γx) = q(x). Note that the map x ∈ [0, 1] ↦→q(x) ∈ M is
necessarily smooth. Let q(0) = ∗ ∈ M . Choose u ∈P∗, the ﬁbre of P at ∗. Let
also ux = Hω(q,x,u ), where x ∈ [0, 1]. In particular u0 =u.
Note that the conditions above imply that:
Rank(D(s,x)J)(t,s,x) ≤ 1 if t = 0 or t = 1, for each s,x ∈ [0, 1]. (22)
Suppose that we also have:
Rank(D(t,x)J)(t,s,x) ≤ 1 if s = 0 or s = 1, for each t,x ∈ [0, 1]. (23)
For each x ∈ [0, 1], let s ∈ [0, 1] ↦→eΓ x(s) ∈ E be the solution of the
diﬀerential equation in E:
d
dseΓ x(s) = eΓ x(s)
∫ 1
0
m
(
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)
dt, (24)
with initial condition:
eΓ x(0) = 1E, ∀x ∈ [0, 1]. (25)
See equation (19). Our purpose is to calculate the x-dependence of eΓ x =
eΓ x(1), the element of E assigned to Γ x, by calculating d
dxeΓ x. The result of this
calculation, Theorem 42, is entirely analogous to Lemma 2, with the 2- curvature
3-form M replacing the curvature 2-form Ω.
Lemma (41) leads to:
d
dxeΓ x =eΓ x
∫ 1
0
∫ 1
0
∂
∂x

m
(
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)

dtds
−eΓ x
∫ 1
0
dθ
( ∂
∂xeΓ x(s), ∂
∂seΓ x(s)
)
ds. (26)
Let
Ax =
∫ 1
0
∫ 1
0
∂
∂x

m
(
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)

dtds ∈ e
Bx =
∫ 1
0
dθ
( ∂
∂xeΓ x(s), ∂
∂seΓ x(s)
)
ds ∈ e.
Thus d
dxeΓ x =eΓ x(Ax −Bx). (27)
Let us analyse Ax andBx separately. Consider the map f : [0, 1]3 →P such
that f (x,s,t ) = Hω(γx
s,t,u x), for each x,s,t ∈ [0, 1]. This map is smooth; see
28
[KN, page 74]. By deﬁnition we have ∂
∂tf (x,s,t ) = ~∂
∂tγxs (t)Hω (γxs,t,ux). Also,
we trivially get:
(∂
∂sf (x,s,t )
) H
= ~∂
∂sγxs (t)Hω (γxs,t,ux) and
(∂
∂xf (x,s,t )
) H
=
~∂
∂xγxs (t)Hω (γxs,t,ux); see 1.1.4. Therefore, since m(X,Y ) vanishes if either X or
Y is vertical, it follows that:
Ax =
∫ 1
0
∫ 1
0
∂
∂xm
(∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dtds
=
∫ 1
0
∫ 1
0
dm
( ∂
∂xf (x,s,t ), ∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dtds
−
∫ 1
0
∫ 1
0
∂
∂tm
(∂
∂sf (x,s,t ), ∂
∂xf (x,s,t )
)
dtds
−
∫ 1
0
∫ 1
0
∂
∂sm
( ∂
∂xf (x,s,t ), ∂
∂tf (x,s,t )
)
dtds.
We have used the well known equation:
dα(X,Y,Z ) = Xα(Y,Z ) +Yα (Z,X ) +Zα(X,Y )
+α(X, [Y,Z ]) +α(Y, [Z,X ]) +α(Z, [X,Y ]),
valid for any smooth 2-form α in a manifold. Therefore:
Ax =
∫ 1
0
∫ 1
0
dm
( ∂
∂xf (x,s,t ), ∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dtds
−
∫ 1
0
[
m
(∂
∂sf (x,s, 1), ∂
∂xf (x,s, 1)
)
−m
(∂
∂sf (x,s, 0), ∂
∂xf (x,s, 0)
)]
ds
−
∫ 1
0
[
m
( ∂
∂xf (x, 1,t ), ∂
∂tf (x, 1,t )
)
−m
( ∂
∂xf (x, 0,t ), ∂
∂tf (x, 0,t )
)]
dt.
We analyse each term separately. Since m(X,Y ) = 0 if either X orY is vertical
we have:
m
( ∂
∂xf (x, 1,t ), ∂
∂tf (x, 1,t )
)
=m
( ~∂
∂xγx
1 (t),
~∂
∂tγx
1 (t)
)
Hω (γx
1,t,ux)
= 0,
by equation (23). Analogously from equation (22) or equation (23) it follows
that: m
(∂
∂xf (x, 0,t ), ∂
∂tf (x, 0,t )
)
= 0, m
(∂
∂sf (x,s, 0), ∂
∂xf (x,s, 0)
)
= 0, and
m
(∂
∂sf (x,s, 1), ∂
∂xf (x,s, 1)
)
= 0. Therefore we have:
Ax =
∫ 1
0
∫ 1
0
dm
( ∂
∂xf (x,s,t ), ∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dtds, (28)
for each x ∈ [0, 1].
29
We now analyse Bx, for each x ∈ [0, 1]. We have:
dθ
(∂
∂xeΓ x(s), ∂
∂seΓ x(s)
)
=
∫ 1
0
dθ
(∂
∂xeΓ x(s),e Γ x(s)m
(
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)
)
dt,
=
∫ 1
0
dθ
(
eΓ x(s)−1 ∂
∂xeΓ x(s),m
(
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γx
s,t,ux)
)
dt
= −
∫ 1
0
[
eΓ x(s)−1 ∂
∂xeΓ x(s),m
(
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)
]
dt
= −
∫ 1
0
∂
(
eΓ x(s)−1 ∂
∂xeΓ x(s)
)
⊲m
( ~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)
dt.
The ﬁrst equation follows by deﬁnition of eΓ x(s), the second since the e-valued
2-form dθ on E is left invariant (since θ is left invariant) and the third by the
well-known formula (21). Finally, the last equation follows since ( ∂ : e → g,⊲ )
is a diﬀerential crossed module.
By lemma 40, we also have that gγx
0∂(eΓ x(s)) = gγxs , for each s,x ∈ [0, 1].
Therefore:
∂
(
e−1
Γ x (s) ∂
∂xeΓ x(s)
)
=∂
(
e−1
Γ x (s)
)
∂
(∂
∂xeΓ x(s)
)
=g−1
γxs
gγx
0
∂
∂x
(
g−1
γx
0
gγxs
)
=
∫ 1
0
Ω
(
~∂
∂tγxs (t),
~∂
∂xγxs (t)
)
Hω (γxs,t,ux)
dt,
where the last equation follows by lemma 2. We also use the fact that ∂
∂xgγx
0 = 0.
This follows from lemma 2 and equation 23. Putting everything togeth er, we
obtain:
dθ
( ∂
∂xeΓ x(s), ∂
∂seΓ x(s)
)
= −
∫ 1
0
Ω
( ~∂
∂tγxs (t),
~∂
∂xγxs (t)
)
Hω (γxs,t,ux)
dt⊲
∫ 1
0
m
( ~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)
dt.
Due to the fact that ( ∂ : e → g,⊲ ) is a diﬀerential crossed module, given e,f ∈ e
we have: ∂(e)⊲f = [e,f ] = −[f,e ] = −∂(f )⊲e. If we use this together with the
fact that Ω( X,Y ) and m(X,Y ) vanish if either of the vectors X orY is vertical
30
it thus follows that (since ∂(m) = Ω):
Bx =
∫ 1
0
(∫ 1
0
Ω
(∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )dt
)
⊲
∫ 1
0
m
(∂
∂tf (x,s,t ), ∂
∂xf (x,s,t )
)
dt
)
ds. (29)
The following is a 2-dimensional version of Lemma 2.
Theorem 42 Let M be a smooth manifold. Let G = (∂ : E →G,⊲ ) be a Lie
crossed module. Let P → M be a principal G-bundle over M . Consider a G-
categorical connection (ω,m ) on P . Let J : [0, 1]3 → M be a smooth map. Let
J(t,s,x ) = Γ x(t,s ) = γx
s (t); ∀t,s,x ∈ [0, 1]. Suppose that ∂l(Γx) = ∂r(Γx) =
q(x), ∀x ∈ [0, 1], where q : [0, 1] →M is a smooth curve. Choose u ∈Pq(0), the
ﬁbre of P at q(0). Let also ux = Hω(q,x,u ), where x ∈ [0, 1]. In particular
u0 =u.
Consider the map (s,x ) ∈ [0, 1]2 ↦→eΓ x(s) ∈ E deﬁned by equations (24)
and (25). Let eΓ x =eΓ x(1). For each x ∈ [0, 1], we have:
d
dxeΓ x =eΓ x
∫ 1
0
∫ 1
0
dm
(
~∂
∂xγxs (t),
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)
dtds
=eΓ x
∫ 1
0
∫ 1
0
M
( ~∂
∂xγxs (t),
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)
dtds.
Proof. By the 2-structure equation, see 2.2.2, and equation (10) it follows that:
∫ 1
0
∫ 1
0
dm
(
~∂
∂xγxs (t),
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γx
s,t,u)
dtds
=
∫ 1
0
∫ 1
0
M
( ∂
∂xf (x,s,t ), ∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dtds
=
∫ 1
0
∫ 1
0
dm
( ∂
∂xf (x,s,t ), ∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dtds
+
∫ 1
0
∫ 1
0
ω
( ∂
∂xf (x,s,t )
)
⊲m
(∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dtds
−
∫ 1
0
∫ 1
0
ω
(∂
∂sf (x,s,t )
)
⊲m
(∂
∂tf (x,s,t ), ∂
∂xf (x,s,t )
)
dtds.
Note that ω
(∂
∂tf (x,t,s
)
=ω
(∂
∂t Hω(γx
s,t,u x)
)
= 0.
31
Also by lemma 1 and the fact that Ω is horizontal:
∫ 1
0
ω
(∂
∂sf (x,s,t )
)
⊲m
(∂
∂tf (x,s,t ), ∂
∂xf (x,s,t )
)
dt
=
∫ 1
0
∫ t
0
Ω
( ∂
∂t′f (x,s,t ′), ∂
∂sf (x,s,t ′)
)
dt′⊲m
(∂
∂tf (x,s,t ), ∂
∂xf (x,s,t )
)
dt
=
∫ 1
0
Ω
( ∂
∂t′f (x,s,t ′), ∂
∂sf (x,s,t ′)
)
dt′⊲
∫ 1
0
m
( ∂
∂t′f (x,s,t ′), ∂
∂xf (x,s,t ′)
)
dt′
−
∫ 1
0
Ω
(∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
⊲
(∫ t
0
m
( ∂
∂t′f (x,s,t ′), ∂
∂xf (x,s,t ′)
)
dt′
)
dt.
The last equation follows from integrating by parts. Indeed, given a smooth
g-valued function V (t) and a smooth e-valued function W (t), each deﬁned on
[0, 1], we have:
∫ 1
0
∫ t
0
V (t′)dt′⊲W (t)dt
=
[( ∫ t
0
V (t′)dt′
)
⊲
(∫ t
0
W (t′)dt′
)]
t=1
−
∫ 1
0
V (t)⊲
(∫ t
0
W (t′)dt′
)
dt.
Let us analyse the very last term. Applying the fact that ( ∂ : e → g,⊲ ) is a
diﬀerential crossed module together with ∂(m) = Ω, part of the deﬁnition of a
categorical connection (ω,m ), we have, since ∂(e)⊲f = −∂(f )⊲e ; ∀e,f ∈ e:
∫ 1
0
Ω
(∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
⊲
(∫ t
0
m
( ∂
∂t′f (x,s,t ′), ∂
∂xf (x,s,t ′)
)
dt′
)
dt
= −
∫ 1
0
∫ t
0
Ω
( ∂
∂t′f (x,s,t ′), ∂
∂xf (x,s,t ′)
)
dt′⊲m
(∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dt
= −
∫ 1
0
ω
( ∂
∂xf (x,s,t )
)
dt′⊲m
(∂
∂tf (x,s,t ), ∂
∂sf (x,s,t )
)
dt.
Therefore:
∫ 1
0
∫ 1
0
M
(
~∂
∂xγxs (t),
~∂
∂tγxs (t),
~∂
∂sγxs (t)
)
Hω (γxs,t,ux)
dtds =Ax −Bx,
by equations (28) and (29). Comparing with equation (27), yields th eorem 42.
From this theorem and the fact that the horizontal lift X ↦→~X of vector
ﬁelds on M deﬁnes a linear map X(M ) → X(P ) we obtain the following:
Corollary 43 Let M be a smooth manifold with a base point ∗. Let also
G = (∂ : E →G,⊲ ) be a Lie crossed module. Let P → M be a principal G-
bundle over M , and let u ∈ P∗, the ﬁbre at ∗ ∈ M . Consider a G-categorical
32
connection (ω,m ) on P . Let Γ be a 2-path in M with ∂l(Γ) = ∂r(Γ) = ∗. Let
Γ(t,s ) = γs(t), for each t,s ∈ [0, 1]. Then F 2
(ω,m,u)(Γ) = (g−1
γ0 ,e Γ ) depends only
on the rank-2 homotopy class of 2-tracks [Γ] to which Γ belongs.
Consider a crossed module G = (∂ : E →G,⊲ ). Let the categorical group it
deﬁnes be C(G); see 1.2.1. Let also be given a smooth manifold M with a base
point ∗, a principal G-bundleP overM and G-categorical connection (ω,m ) on
P . We deﬁned maps F 1
(ω,m,u) :π1
1(M, ∗) →G (the sets of objects of P(M, ∗) and
of C(G), respectively) and F 2
(ω,m,u) : P2(M, ∗) →G ⋉E (the sets of morphisms
of P(M, ∗) and C(G), respectively). We now prove that this assignment, deﬁned
in 2.4.1, is a categorical holonomy. This will complete the proof of theo rem 39.
