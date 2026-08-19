---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-010-25-duality
section_title: "Duality"
section_number: 2.5
pages: 20-23
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
modules. Recall that we can write the linear q-diﬀerence equation
ar(t, q)f (qrt, q) + ar−1(t, q)f (qr−1t, q) + · · · + a0(t, q)f (t, q) = 0 (84)
for a function f (t, q) in matrix form σX = AX where X = Xf = ( f, σf, . . . , σr−1f )t is a
column vector and A = comp(−a0/ar, . . . ,−ar−1/ar) is the companion matrix where
comp(c0, c 1, . . . , c r−1) =






0 1 0 . . . 0
0 0 1 . . . 0
: : : . . . :
0 0 0 . . . 1
c0 c1 c2 . . . c r−1






. (85)
We will also write (
84) in operator form Lf = 0 where L =∑ r
j=0 ajσr−j ∈ W and denote
by Mf = Wf the corresponding module over the q-Weyl algebra W. The module Mf has
two duals. The ﬁrst one is deﬁned by
M ∧
f = Mf ∧, f ∧(t, q) = f (t, q−1) (86)
which in matrix form is given by
σXf ∧ = A∧Xf ∧, A ∧(t, q) = A(qt, q−1)−1 . (87)
Indeed, we have
ar(t, q−1)f ∧(q−rt, q) + ar−1(t, q−1)f ∧(q−r+1t, q) + · · · + a0(t, q−1)f ∧(t, q) = 0
and inverting ar, we obtain that
f ∧(qt, q) = − ar(qt, q−1)
a0(qt, q−1) f ∧(q1−rt, q) − ar−1(qt, q−1)
a0(qt, q−1) f ∧(t, q) − · · · − a1(qt, q−1)
a0(qt, q−1) f ∧(t, q)
which implies ( 87). The second dual module is deﬁned by
M ∨
f = Hom
/C9 (q)[t±1](Mf , /C9 (q)[t±1]) (88)
with a basis f ∨
i for i = 0, . . . r − 1 such that for j = 0, . . . , r− 1 we have f ∨
i (σjf ) = δi,j. We
claim that in matrix form, this dual module is given by
σXf ∨ = A∨Xf ∨, A ∨(t, q) = ( A(t, q)−1)t . (89)
MODULAR q-HOLONOMIC MODULES 21
Indeed, using the basis f ∨, we can deﬁne an action of W on M ∨
f via conjugation with σ. By
deﬁnition, the action satisﬁes σ(λ(v)) = ( σ · λ)(σv) for λ ∈ M ∨
f and v ∈ Mf . In particular
we have σ · f ∨
i = σf ∨
i σ−1. Notice that for i, j = 0, . . . , r− 1
(σ · f ∨
i )(σjf ) = ( σf ∨
i )(σj−1f ) = ( σf ∨
i )
( r−1∑
k=0
(A(q−1t, q)−1)jkσkf
)
= σ
( r−1∑
k=0
(A(q−1t, q)−1)jkδik
)
= (A(t, q)−1)ji =
( r−1∑
k=0
(A(t, q)−t)ikf ∨
k
)
(σjf )
which implies ( 89).
Recall that if two modules with companion matrices A and B are isomorphic, there exists
a change of basis P such that
B = (σP )AP −1 . (90)
Then taking
P ∨(t, q) =






1 0 0 . . . 0
a1/a0 1 0 . . . 0
a2/a0 σ(a1/a0) 1 . . . 0
: : : . . . :
ar−1/a0 σ(ar−2/a0) σ(ar−3/a0) . . . 1






, P ∧(t, q) =






0 0 . . . 0 1
0 0 . . . 1 0
: : . . . : :
0 1 . . . 0 0
1 0 . . . 0 0






(91)
we ﬁnd that
(σP ∨)−1A∨P ∨ = comp(−ar/a0, σ(ar−1/a0), . . . , σr(a1/a0))
(σP ∨)−1A∨P ∨ = comp
(
− ar(qt, q−1)
a0(qt, q−1) , ar−1(qt, q−1)
a0(qt, q−1) , . . . , a1(qt, q−1)
a0(qt, q−1)
)
.
(92)
We now remark an elementary relation between fundamental solutio ns of inhomogeneous
linear q-diﬀerence equations and their corresponding homogeneous ones . Consider the inho-
mogeneous equation
a0(t, q)f (t, q) + · · · + ar−1(t, q)f (qr−1t, q) + f (qrt, q) = c0(q). (93)
We can write it either in the form σXf (in) = A(in)Xf (in) with
Xf (in) =




1
f
:
σr−1f



 , A (in) =








1 0 0 0 . . . 0
0 0 1 0 . . . 0
0 0 0 1 . . . 0
: : : : . . . :
0 0 0 0 . . . 1
c0 −a0 −a1 −a2 . . . −ar−1








or in the form σX = AX with
Xf = (f, σf, . . . σ rf )t, A = comp(−a0, σa 0 − a1, σa 1 − a2, . . . , σa r−2 − ar−1, σa r−1 − 1) .
The two equations are related by Xf = P Xf (in), A = σP A(in)P −1 where
P = comp(c0, −a0, −a1, −a2, . . . ,−ar−1) .
We end this subsection by discussing the duality
M ∨ ∼= M ∧ (94)
22 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
which follows from (but is not equivalent to) the existence of matrice s P ∨, P ∧ ∈ GLr(
/C9 (t, q))
such that
σP ∧A∧(P ∧)−1 = σP ∨A∨(P ∨)−1 (95)
is a companion matrix. For the q-holonomic modules that come from Chern-Simons theory,
the duality M ↦→M ∧ corresponds to orientation-reversal of the ambient 3-manifold. On the
other hand, the factorisation of the Andersen–Kashaev state in tegrals into elements of M
and M ∧ suggests that in those examples, we have M ∧ ∼= M ∨. The following proposition
conﬁrms this for the case of the 4 1 knot.
Proposition 2.5. The q-diﬀerence module M associated to Equation ( 28) satisﬁes
M ∼= M ∧ ∼= M ∨ . (96)
The fundamental matrices satisfy
U(t, λ, q) = P ∧(t, q)U ∧(t, λ, q) = P ∨(t, q)U ∨(t, λ, q)
(
0 −1
1 0
)
,
V (t, q) = P ∧(t, q)V ∧(t, q) = P ∨(t, q)V ∨(t, q)
(
0 −1
1 0
) (97)
with
P ∧(t, q) =
(
1 0
2q−1 − t−1q−1 −q−2
)
, P ∨(t, q) =
(
0 −q−1t−2
q−1t−2 0
)
(98)
and cocycle Ω of M satisﬁes
Ω = ( P ∧|κγ)Ω ∧(P ∧)−1 = (P ∨|κγ)Ω ∨(P ∨)−1 . (99)
Equation ( 99) was called “quadratic relations” in Section 3.3 and equations (68)-( 70)
of [ 33]. An example of a self-dual module is the generalised q-hypergeometric equation (see
Equation ( 116) below).
Proof. With A, given in Equation ( 235), and the gauge transformations ( 98), we have
A(t, q) = P ∧(qt, q)A∧(t, q)P ∧(t, q)−1 = P ∨(qt, q)A∨(t, q)P ∨(t, q)−1. (100)
□
The extra symmetry with M ∼= M ∧ comes from the fact the 4 1 knot is amphichiral.
However, this symmetry does not persist to the module associated to the inhomogeneous
equation. This can again be seen from the state integrals introduce d in [ 24] whose integrand
lacks the symmetry the Andersen-Kashaev state integrals have.
Proposition 2.6. The q-diﬀerence module M ∨ associated to Equation (
35) is not isomorphic
to M ∧.
Proof. The companion matrices of M and M ∧ are given by
A∧(t, q) =


1 0 0
q−1t−1 2q−1 − t−1q−1 −q−2
0 1 0

 , A ∨(t, q) =


1 t−1 0
0 2 q − t−1 1
0 −q2 0

 . (101)
MODULAR q-HOLONOMIC MODULES 23
If there was an isomorphism there would exist P (t, q) ∈ GL3( /C9 (t, q)) such that
P (qt, q)A∨(t, q) = A∧(t, q)P (t, q) . (102)
It follows that
P1,1(qt, q) = P1,1(t, q), P 1,2(qt, q) = P1,3(t, q), (103)
which then implies
tP1,2(t, q) + (1 − 2tq)P1,2(qt, q) + q2tP1,2(q2t, q) = P1,1(qt, q). (104)
Since P1,1 ∈ /C9 (t, q) satisﬁes ( 103), it is independent of t, i.e., P1,1(t, q) = P1,1(q). Therefore,
P1,2 would be a P1,1(q) multiple of a /C9 (t, q)-valued solution to Equation ( 35). The only such
solution is zero, thus P1,1 = P1,2 = 0 which, together with ( 103) gives also P1,3 = 0, which
violates the fact that P is invertible. □
