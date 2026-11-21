---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-019-41-the-q-pochhammer-symbol
section_title: "The q-Pochhammer symbol"
section_number: 4.1
pages: 31-33
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
toc_source: outline
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
The q-diﬀerence equation (19) can be written in operator form as ((1 −qt)σ −1)f = 0, with
the Newton polygon shown in Figure 2.
g(1)
f (0)
Figure 2. The Newton polygon of Equation (19).
The lower Newton polygon has one edge of slope zero. Applying the Frobenius method, we
seek a formal power series solution of the form
f (0)(t, q) =
∞
X
k=0
αk(q)tk θ(ρ−1t; q)
θ(t; q)
where
qkραk(q) −qkραk−1(q) −αk(q) = 0.
(153)
Since αk(q) = 0 for k < 0, setting k = 0 in the above equation implies the vanishing of the
indicial polynomial
(ρ −1)α0(q) = 0,
(154)
giving ρ = 1. Then we have
αk(q)
αk−1(q) = −
qk
1 −qk .
(155)
Therefore, normalising so that α0(q) = 1,
f (0)(t, q) =
∞
X
k=0
(−1)k qk(k+1)/2
(q; q)k
tk = (qt; q)∞.
(156)
This solution is convergent at t = 0, in fact it is an entire function of t.
The upper Newton polygon has one edge of slope of one. Therefore, we must multiply by
a θ-function to get a slope zero, i.e. a power series solution. The new Newton polygon is as
follows.
32
STAVROS GAROUFALIDIS AND CAMPBELL WHEELER
g(1)
θ(t; q)
ˆg(1)
Therefore, the top edge has solution of the form
g(1)(t, q) = θ(t; q)ˆg(1)(t, q),
ˆg(1)(t, q) = θ(t; q)
∞
X
k=0
βk(q)t−k θ(ρ−1t; q)
θ(t; q)
(157)
where
−q−kρβk−1(q) + q−kρβk(q) −βk(q) = 0.
(158)
As βk(q) = 0 for k < 0, we get indicial polynomial
(ρ −1)β0(q) = 0
(159)
and so ρ = 1. Then we have
βk
βk−1
=
1
1 −qk .
(160)
Therefore, normalising so that β0(q) =
1
(q;q)∞, we obtain that
g(1)(t, q) = θ(t; q)
(q; q)∞
∞
X
k=0
t−k
(q; q)k
=
θ(t; q)
(t−1; q)∞(q; q)∞
.
(161)
It follows that the monodromy is given by
−→
M(t, q) = V (t, q)−1U(t, q) = (qt; q)∞(t−1; q)∞(q; q)∞
θ(t; q)
= 1
(162)
and the cocycles are equal and given by
ΩU(z, τ) = (U|0S)(z, τ)U(z, τ)−1 = ΩU(z, τ) = (V |0S)(z, τ)V (z, τ)−1 = (eqet; eq)∞
(qt; q)∞
.
(163)
Notice that
(eqet; eq)∞
(qt; q)∞
= Φb
iz
b + ib
2 + 1
2ib
−1
(164)
where Φ is the Faddeev quantum dilogarithm function [23, 24]. This function extends to
a meromorphic function of (z, τ) ∈C × C′, with poles at z ∈Z≥0 + Z≥0τ. Noting that
ΩT = 1, it then follows from Theorem 1.2 that ΩU,γ also extends. This is discussed in detail
in upcoming work [31]. This proves that this is a modular q-holonomic module.
MODULAR q-HOLONOMIC MODULES
