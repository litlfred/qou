---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-003-the-dependence-of-the-parallel-transport-on-a-sm
section_title: "The dependence of the parallel transport on a smooth family of curves - the Ambrose-Singer theorem"
section_number: null
pages: 6-9
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
of curves - the Ambrose-Singer theorem
Let M be a smooth manifold. Let D n .= [0, 1]n be the n-cube, where n ∈ N. A
mapf : Dn →M is said to be smooth if its partial derivatives of any order exist
and are continuous as maps D n →M . Let G be a Lie group with Lie algebra
g. Consider a smooth principal G-bundle π : P →M with a connection 1-form
ω ∈ A1(P, g).
Now let s ∈ [0, 1] ↦→γs be a smooth 1-parameter family of smooth curves
[0, 1] → M . Here smooth means that the map Γ : ( t,s ) ∈ [0, 1]2 ↦→γs(t) ∈ M
is smooth. Deﬁne the initial point map q : [0, 1] →M by q(s) = γs(0) for each
s ∈ [0, 1]. Choose u ∈ Pq(0) and set us = Hω(q,s,u ) ∈ Pq(s), where s ∈ [0, 1].
Our purpose is to analyse the s-dependence of Hω(γs,t,u s), where s,t ∈ [0, 1],
by calculating:
∂
∂s Hω(γs,t,u s).
6
This analysis is of course classical.
For convenience of notation, deﬁne
f (s,t ) = Hω(γs,t,u s);s,t ∈ [0, 1].
Let the coordinate vector ﬁelds of [0 , 1]2 be ∂
∂t and ∂
∂s . We have:
∂
∂tω
(∂
∂sf (s,t )
)
= ∂
∂tf ∗(ω)
(∂
∂s
)
=f ∗(dω)
(∂
∂t, ∂
∂s
)
+ ∂
∂sf ∗(ω)
(∂
∂t
)
=dω
(∂
∂tf (s,t ), ∂
∂sf (s,t )
)
.
Note that the second equation follows from the well-known formula
dφ(X,Y ) = Xφ(Y ) −Yφ (X) −φ([X,Y ]), (3)
valid for any 2-form φ on a manifold M and any X,Y ∈ X(M ). The last
equation follows from the fact that ∂
∂tf (s,t ) is horizontal, by deﬁnition of parallel
transport.
Therefore by Cartan’s structure equation (1) and the fact that ∂
∂tf (s,t ) is
horizontal it follows that:
∂
∂tω
(∂
∂sf (s,t )
)
= Ω
(∂
∂tf (s,t ), ∂
∂sf (s,t )
)
. (4)
Since Ω( X,Y ) = 0 if either of the vectors X or Y is vertical we can conclude:
∂
∂tω
(∂
∂sf (s,t )
)
= Ω
((∂
∂tf (s,t )
) H
,
(∂
∂sf (s,t )
) H)
.
Note that, by deﬁnition of parallel transport, we have
(∂
∂tf (s,t )
) H
= ∂
∂tf (s,t ) =
( ~∂
∂tγs(t)
)
Hω (γs,t,us)
.
Given that
(∂
∂sf (s,t )
) H
is horizontal and the fact that:
π∗
((∂
∂sf (s,t )
) H)
=π∗
(∂
∂sf (s,t )
)
= ∂
∂sπ
(
f (s,t )
)
= ∂
∂sγs(t),
it follows (∂
∂sf (s,t )
) H
=
(
~∂
∂sγs(t)
)
Hω (γs,t,us)
.
Going back to equation (4), we have that, for each s ∈ [0, 1], ω
(∂
∂sf (s, 0)
)
=
0, since f (s, 0) = us = Hω(q,s,u ), hence ∂
∂sf (s, 0) is horizontal for each s ∈
[0, 1]. We thus arrive at the following well known result:
7
Lemma 1 LetG be a Lie group with Lie algebra g. Let P be a smooth principal
G-bundle over the manifold M . Let s ∈ [0, 1] ↦→γs be a smooth 1-parameter
family of curves [0, 1] →M . Here smooth means that the map (s,t ) ∈ [0, 1]2 ↦→
γs(t) ∈ M is smooth. Consider a connection ω ∈ A1(P, g). Let q : [0, 1] → M
be the curve such that q(s) = γs(0), ∀s ∈ [0, 1]. Choose u ∈Pq(0), and let us =
Hω(q,s,u ) ∈Pq(s), where s ∈ [0, 1]. The following holds for each s,t ′ ∈ [0, 1]:
ω
(∂
∂s Hω(γs,t ′,us)
)
=
∫ t′
0
Ω
( ~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,us)
dt. (5)
Consider the case when all curves γs : [0, 1] →M , where s ∈ [0, 1], are closed,
though possibly with varying initial points. (This ﬂexibility will be importa nt
to deﬁne Wilson spheres in 2.5.3). Then we can deﬁne a family of holonom ies
gγs ∈G, where s ∈ [0, 1], by:
usgγs = Hω(γs, 1,us), ∀s ∈ [0, 1].
We will use the preceding lemma to obtain a diﬀerential equation satisﬁ ed by
gγs.
Because d
dsus is horizontal it follows that:
ω
(d
ds (usgγs)
)
=ω
(
us
d
dsgγs
)
=
∫ 1
0
Ω
( ~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,us)
dt.
Since, for each s ∈ [0, 1], the vector us d
dsgγs is vertical, this means, by the second
condition of the deﬁnition of a connection 1-form ω (see 1.1.1):
us
d
dsgγs =


∫ 1
0
Ω
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,us)
dt


#
Hω (γs,1,us)
, (6)
or[ d
dt′usgγ(s+t′)
]
t′=0
= d
dt′ Hω(γs, 1,us) exp

t′
∫ 1
0
Ω
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,us)
dt


t′=0
= d
dt′usgγs exp

t′
∫ 1
0
Ω
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,us)
dt


t′=0
,
which, given the fact that the right action of G on P is free, is equivalent to:
Lemma 2
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
Hω (γs,t,us)
dt. (7)
This fact will be of major importance later.
8
