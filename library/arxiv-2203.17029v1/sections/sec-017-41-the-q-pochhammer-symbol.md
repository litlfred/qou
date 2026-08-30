---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-017-41-the-q-pochhammer-symbol
section_title: "The q-Pochhammer symbol"
section_number: 4.1
pages: 30-32
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
The q-diﬀerence equation ( 19) can be written in operator form as ((1 − qt)σ − 1)f = 0, with
the Newton polygon shown in Figure 2.
The lower Newton polygon has one edge of slope zero. Applying the Fr obenius method, we
seek a formal power series solution of the form
f (0)(t, q) =
∞∑
k=0
αk(q)tk θ(ρ−1t; q)
θ(t; q) where qkραk(q) − qkραk−1(q) − αk(q) = 0 . (150)
MODULAR q-HOLONOMIC MODULES 31
g(1)
f (0)
Figure 2. The Newton polygon of Equation ( 19).
Since αk(q) = 0 for k < 0, setting k = 0 in the above equation implies the vanishing of the
indicial polynomial
(ρ − 1)α0(q) = 0 , (151)
giving ρ = 1. Then we have
αk(q)
αk−1(q) = − qk
1 − qk . (152)
Therefore, normalising so that α0(q) = 1,
f (0)(t, q) =
∞∑
k=0
(−1)k qk(k+1)/2
(q; q)k
tk = (qt; q)∞ . (153)
This solution is convergent at t = 0, in fact it is an entire function of t.
The upper Newton polygon has one edge of slope of one. Therefore , we must multiply by
a θ-function to get a slope zero, i.e. a power series solution. The new Newton polygon is as
follows.
g(1)
θ(t; q) ˆg(1)
Therefore, the top edge has solution of the form
g(1)(t, q) = θ(t; q)ˆg(1)(t, q), ˆg(1)(t, q) = θ(t; q)
∞∑
k=0
βk(q)t−k θ(ρ−1t; q)
θ(t; q) (154)
where
− q−kρβk−1(q) + q−kρβk(q) − βk(q) = 0 . (155)
32 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
As βk(q) = 0 for k < 0, we get indicial polynomial
(ρ − 1)β0(q) = 0 (156)
and so ρ = 1. Then we have
βk
βk−1
= 1
1 − qk . (157)
Therefore, normalising so that β0(q) = 1
(q;q)∞
, we obtain that
g(1)(t, q) = θ(t; q)
(q; q)∞
∞∑
k=0
t−k
(q; q)k
= θ(t; q)
(t−1; q)∞(q; q)∞
. (158)
It follows that the monodromy is given by
− →
M(t, q) = V (t, q)−1U(t, q) = (qt; q)∞(t−1; q)∞(q; q)∞
θ(t; q) = 1 (159)
and the cocycles are equal and given by
Ω U (z, τ ) = ( U|0S)(z, τ )U(z, τ )−1 = Ω U (z, τ ) = ( V |0S)(z, τ )V (z, τ )−1 = (~q~t;~q)∞
(qt; q)∞
. (160)
Notice that
(~q~t;~q)∞
(qt; q)∞
= Φ b
( iz
b + ib
2 + 1
2ib
) −1
(161)
where Φ is the Faddeev quantum dilogarithm function [ 19, 20]. This function extends to
a meromorphic function of ( z, τ ) ∈ /BV × /BV
′, with poles at z ∈ /CI
≥0 + /CI
≥0τ . Noting that
Ω T = 1, it then follows from Theorem 1.2 that Ω U,γ also extends. This is discussed in detail
in upcoming work [ 27]. This proves that this is a modular q-holonomic module.
