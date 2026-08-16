---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-018-42-the-appell-lerch-sums
section_title: "The Appell-Lerch sums"
section_number: 4.2
pages: 32-37
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
q-diﬀerence equation ( 22) has Newton polygon shown in Figure 3.
f (0)
f (−1)
g(0)
g(−1)
Figure 3. The Newton polygon of Equation ( 22).
MODULAR q-HOLONOMIC MODULES 33
To begin with, the boundary of the lower Newton polygon consists of one edge of slope zero
and one edge of slope 1. The edge of slope zero has a solution of the f orm
f (0)(t, q) =
∞∑
k=0
αk(q)tk θ(ρ−1t; q)
θ(t; q) where αk(q)q2kρ2 + qkραk−1(q) − qkραk(q) − αk−1(q) = 0 .
(162)
Therefore, as αk(q) = 0 for k < 0, we get the indicial polynomial
α0(q)(ρ2 − ρ) = 0 (163)
and so ρ = 1. Then we have
(q2k − qk)αk(q) − (1 − qk)αk−1(q) = 0 so − qkak = ak−1. (164)
Therefore, normalising so that α0(q) = 1,
ˆf (0)(t, q) =
∞∑
k=0
(−1)kq−k(k+1)/2tk. (165)
This is of course divergent for |q| < 1 so we must q-Borel resum. The aﬀect on the Newton
polygon is as follows
f (0)
B1
B1f (0)
Now notice that
B1 ˆf (0)(ξ, q) =
∞∑
k=0
ξk = 1
1 − ξ (166)
and so we ﬁnd
f (0)(t, λ, q) = L1B1( ˆf (0))(t, λ, q) = 1
θ(λ; q)
∑
ℓ
(−1)ℓ qℓ(ℓ+1)/2λℓ
1 − λtqℓ . (167)
This is the Appell-Lerch sum whose modular properties were studied in Zwegers thesis [ 67].
Now the bottom edge of slope −1 must be divided by a θ-function to get a zero slope. The
eﬀect on the Newton polygon is as follows.
f (−1) θ(q−1t; q)−1
ˆf (−1)
34 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
Therefore, the bottom edge of slope minus one has a solution of the form
f (−1)(t, q) = θ(q−1t; q)−1 ˆf (−1)(t, q) = θ(q−1t; q)−1
∞∑
k=0
αk(q)tk θ(ρ−1t; q)
θ(t; q) (168)
where
(1 − qkρ)αk(q) + qkρ(1 − qk−1ρ)αk−1(q) = 0 . (169)
Therefore, the indicial polynomial is given by
(1 − ρ)α0(q) = 0 (170)
and so ρ = 1. Then we see that
(1 − q)α1(q) = 0 (171)
and so αk = 0 for k ⁄= 0. Therefore,
f (−1)(t, q) = θ(q−1t; q)−1 . (172)
Now following similar calculations we ﬁnd that
B1ˆg(0)(ξ, q) = −
−1∑
k=−∞
ξk = − ξ−1
1 − ξ−1 = 1
1 − ξ (173)
and so
g(0)(t, µ, q) = 1
θ(µ; q)
∑
ℓ
(−1)ℓ qℓ(ℓ+1)/2µℓ
1 − µtqℓ . (174)
Then ﬁnally, we have
g(−1)(t, q) = θ(q−1t; q)−1 . (175)
Consider the inhomogeneous gauge transformation (see Section 2.6)
U(t, λ, q) =
(
0 1
1 −t
)( 1 0
f (0)(t, λ, q) f (−1)(t, q)
)
(176)
and the similar one for V . With the deﬁnition of the fundamental matrices given in Equa-
tions (
23) and associated monodromy, we then have that
− →
M(t, λ, q) =
( 1 0
g(0)(t, µ, q) g(−1)(t, q)
) −1( 1 0
f (0)(t, λ, q) f (−1)(t, q)
)
= θ(q−1t, q)
( θ(q−1t, q)−1 0
−g(0)(t, µ, q) 1
)( 1 0
f (0)(t, λ, q) θ(q−1t, q)−1
)
=
( 1 0
− →
M2,1(t, λ, µ, q) 1
)
(177)
where
− →
M2,1(t, λ, µ, q) = θ(q−1t; q)f (0)(t, λ, q) − θ(q−1t; q)g(0)(t, µ, q)
= θ(q−1t; q)
θ(λ; q)
∑
ℓ
(−1)ℓ qℓ(ℓ+1)/2λℓ
1 − λtqℓ − θ(q−1t; q)
θ(µ; q)
∑
ℓ
(−1)ℓ qℓ(ℓ+1)/2µℓ
1 − µtqℓ . (178)
MODULAR q-HOLONOMIC MODULES 35
Using Equation (7) of Proposition 1.4 of [ 67], we can deduce that
− →
M2,1(t, λ, µ, q) = −(q; q)3
∞θ(q−1t; q)θ(λ−1µ; q)θ(λ−1µ−1t−1; q)
θ(λ−1; q)θ(µ; q)θ(λ−1t−1; q)θ(µ−1t−1; q) . (179)
We now give a second proof of the above equation using elliptic functio ns and residues, which
is more general and applicable to our third example. Let m2,1 denote the function deﬁned
by the right-hand side of ( 179). We need to prove that the function E1, deﬁned by
E1(t, λ, µ, q) := f (0)(t, λ, q) − g(0)(t, µ, q) − m2,1(t, λ, µ, q)
θ(q−1t; q) (180)
is identically zero. This will follow from the facts, that E1 is holomorphic at /BV
× (see
Lemma 4.2 below), and a solution of a ﬁrst order equation ( 181) (see Lemma 4.1).
Lemma 4.1. If h(t, q) is a solution to the equation
h(qt, q) + th(t, q) = 0 (181)
that is holomorphic for t ∈ /BV
× then h(t, q) = 0.
Proof. Every solution is of the form C(t, q)/θ(q−1t; q) for some elliptic function C(t, q).
Therefore, C(t, q) = h(t, q)θ(q−1t; q) is a holomorphic elliptic function and therefore con-
stant. However, this implies that h has simple poles unless C = 0. □
Lemma 4.2. (a) The function f (0)(t, λ, q) has simple poles at t ∈ λ−1q
/CI
with residue
Rest=q−mλ−1f (0)(t, λ, q) dt
2πit = −1
θ(qmλ; q)
Rest=q−mµ−1g(0)(t, µ, q) dt
2πit = −1
θ(qmµ; q) .
(182)
(b) The function θ(q−1t; q)−1m2,1(t, λ, µ, q) has simple poles at t ∈ q
/CI
λ−1, q
/CI
µ−1 with residues
Rest=q−mλ−1θ(q−1t; q)−1m2,1(t, λ, µ, q) dt
2πit = −1
θ(qmλ; q)
Rest=q−mµ−1θ(q−1t; q)−1m2,1(t, λ, µ, q) dt
2πit = 1
θ(qmµ; q) .
(183)
Proof. Part (a) follows from a calculation of the residue of the only term in th e sum that
contributes to the residue in Equations ( 167) ( 174) and Equation ( 48). Now for part (b) we
note that
Rest=1
1
θ(t; q)
dt
2πit = 1
(q; q)3
∞
(184)
36 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
which follows easily from the Jacobi triple product (
46) for example. Therefore, we see
Rest=q−mλ−1
m2,1(t, λ, µ, q)
θ(q−1t; q)
dt
2πit
= (−1)mqm(m+1)/2Rest=1 − (q; q)3
∞θ(λ−1µ; q)θ(µ−1t−1; q)
θ(λ−1; q)θ(µ; q)θ(t−1; q)θ(λµ−1t−1; q)
dt
2πit
= (−1)mqm(m+1)/2 θ(λ−1µ; q)θ(µ−1; q)
θ(λ−1; q)θ(µ; q)θ(λµ−1; q)
= −1
θ(qmλ; q)
(185)
where we have repeatedly used Equations ( 47) and ( 48). A similar computation calculates
the other residues or using Equation ( 47) we can show that
m2,1(t, λ, µ, q) = −m2,1(t, µ, λ, q) . (186)
□
Noting that E1(t, λ, µ, q) satisﬁes Equation ( 181) these lemmata show that the potential
simple poles of E1(t, λ, µ, q) cancel and therefore it is holomorphic on t ∈ /BV
× and therefore
vanishes.
For completeness, we give a third proof of ( 179) using Lemma 2.1.
− →
M2,1(t, λ, µ, q) = θ(q−1t; q)L1
( 1
1 − ξ
)
(t, λ; q) − θ(q−1t; q)L1
( 1
1 − ξ
)
(t, µ; q)
= θ(q−1t; q)θ(λ−1µ; q)(q; q)3
∞
θ(λ−1; q)θ(µ; q) Resξ=1
θ(λ−1µ−1t−1ξ; q)
θ(ξλ−1t−1; q)θ(ξµ−1t−1; q)(1 − ξ)
= −(q; q)3
∞θ(q−1t; q)θ(λ−1µ; q)θ(λ−1µ−1t−1; q)
θ(λ−1; q)θ(µ; q)θ(λ−1t−1; q)θ(µ−1t−1; q)
(187)
concluding the proof of Equation ( 24). From the explicit expression for
− →
M2,1 from Equa-
tion (25) and the modularity of the Dedekind η-function and the Jacobi θ-function it follows
that M satisﬁes Equation ( 6) with weight κ = (0 , 1). It follows that the two cocycles of
Equation (23) agree. This implies that neither cocycle depends on λ or µ. This is equivalent
to observations in [ 67] that the slash operator acting on the Appell-Lerch sums depends only
on the diﬀerence of two Jacobi variables. Then using [ 67, Proposition 1.5] we can give an ex-
plicit formula for the cocycle in terms of the Mordell integral ( 27) and elementary functions.
In particular, we have
f (0)(qt, λ, q) + tf (0)(t, λ, q) = 1
f (−1)(qt, q) + tf (−1)(t, q) = 0
~f (0)(t, λ, q) e
( (z + 1/2 − τ /2)2
2τ − 1
8
) √τ = τ f(0)(t, λ, q) − τ t− 1
2 q
1
8 h(t, q)
f (−1)(~t,~q) e
( (z + 1/2 − τ /2)2
2τ − 1
8
) √τ = f (−1)(t, q) .
(188)
MODULAR q-HOLONOMIC MODULES 37
This means that
det U(t, λ, q) = f (−1)(qt, q)f (0)(t, q) − f (−1)(t, q)f (0)(qt, q)
= f (−1)(t, q)
(
−tf (0)(t, q) − f (0)(qt, q)
)
= −f (−1)(t, q).
(189)
Therefore, we see that
Ω S(z, τ ) =
( 0 1
1 −˜t
) ( τ −1 0
e( 1
8 )√τ
˜t− 1
2 ˜q
1
8 e
(
z2
2τ
)
h(z, τ )
e( 1
8 )√τ e
(
− (z+1/2−τ /2)2
2τ
)
) (
0 1
1 −t
) −1
.
(190)
We can vary the contour in Equation (
27) to get the integral
∫
ζ /CA
eπi(τ x2+2izx)
2 cosh(πx) dx (191)
for |ζ| = 1 and ζ ⁄= ±i. This is a convergent integral to a holomorphic function in ( z, τ )
