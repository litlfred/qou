---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-020-5-a-q-difference-equation-of-the-41-knot
section_title: "A q-difference equation of the 41 knot"
section_number: 5
pages: 37-40
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
This section is devoted to the proof of Theorem 1.7, Theorem 1.8 and Theorem 1.9.
5.1. Solutions. The q-diﬀerence equation ( 28) has Newton polygon shown in Figure 4.
g(0,0) g(0,1)
f (−1) f (1)
Figure 4. The Newton polygon of Equation ( 28).
The boundary of the lower Newton polygon has edges of slope −1 and 1. The edge with
slope −1 must be divided by a θ-function to get a power series solution. The eﬀect on the
Newton polygon is as follows.
38 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
f (−1) θ(t; q)−1
ˆf (−1)
Therefore, the bottom edge of the Newton polygon with slope −1 has a solution of the form
f (−1)(t, q) = θ(t; q)−1 ˆf (−1)(t, q) = θ(t; q)−1
∞∑
k=0
α(−1)
k (q)tk θ(ρ−1t; q)
θ(t; q) (192)
where
(1 − q−k−1ρ−1)α(−1)
k (q) − 2α(−1)
k−1 (q) − qkρα(−1)
k−2 (q) = 0 . (193)
Therefore, this edge has indicial polynomial
(1 − q−1ρ−1)α(−1)
0 (q) (194)
and so ρ = q−1. Now notice that if we take the ( −1)-q-Borel transform we see the eﬀect on
the Newton polygon is as follows.
ˆf (−1)
B−1
B−1 ˆf (−1)
This means that this Borel transform will satisfy the q-diﬀerence equation
(1 − q−1t)2B−1 ˆf (−1)(q−1t; q) = B−1 ˆf (−1)(t, q). (195)
Therefore, normalising so that α0(q) = −(q; q)2
∞ we have
B−1 ˆf (−1)(t, q) =
∞∑
k=0
(−1)kq−k(k+1)/2α(−1)
k (q)tk = −(q; q)2
∞
(t; q)2
∞
. (196)
Therefore, we see that
α(−1)
k (q) = ( q; q)2
∞(−1)k+1qk(k+1)/2
k∑
ℓ=0
1
(q; q)ℓ(q; q)k−ℓ
. (197)
In particular, we have
f (−1)(t, q) = ( q; q)2
∞θ(q−1t; q)−1
∞∑
k=0
k∑
ℓ=0
(−1)k qk(k+1)/2
(q; q)ℓ(q; q)k−ℓ
tk . (198)
Now the bottom edge of slope 1 must be multiplied by a θ-function to get a power series
solution. However, this will then be divergent so we must take (1 /2)-q-Borel resummation.
The eﬀect on the Newton polygon is as follows.
MODULAR q-HOLONOMIC MODULES 39
f (1) θ(t; q)
ˆf (1)
B1/2
B1/ 2 ˆf (1)
By symmetry of the q-diﬀerence equation, one can easily use the previous solution to che ck
that the formal solution to this edge is given by q ↦→q−1 which gives
f (1)(t, q) = θ(t; q)
(q; q)2
∞
ˆf (1)(t, q) = θ(t; q)
(q; q)2
∞
∞∑
k=0
k∑
ℓ=0
qℓ2−ℓk
(q; q)ℓ(q; q)k−ℓ
tk. (199)
One then sees that
B1/2 ˆf (1)(ξ, q) =
∞∑
k=0
k∑
ℓ=0
(−1)k qk(k+1)/4+ℓ2−ℓk
(q; q)ℓ(q; q)k−ℓ
ξk =
∞∑
k,ℓ=0
(−1)k+ℓ qk(k+1)/4−kℓ/2+ℓ(ℓ+1)/4
(q; q)k(q; q)ℓ
ξk+ℓ
(200)
is holomorphic for |ξ| < |q−1/4|. Then, using the functional equation
(1 − q1/2ξ2)B1/2 ˆf (1)(ξ, q) + 2ξB1/2 ˆf (1)(q1/2ξ, q) − B1/2 ˆf (1)(qξ, q ) = 0 , (201)
we can analytically extend away from ξ ∈ ± q−1/4+ 1
2
/CI
≤0 and we see that there are poles at
ξ ∈ ±q−1/4+ 1
2
/CI
≤0. Therefore, we ﬁnally deﬁne
f (1)(t, λ, q) = θ(t; q)
(q; q)2
∞
L1/2B1/2 ˆf (1)(t, λ, q)
= θ(t; q)
(q; q)2
∞
∑
n∈
/CI
B1/2 ˆf (1)(q
n
2 λt, q)
θ(q
n
2 λ; q
1
2 )
= θ(t; q)
(q; q)2
∞θ(λ; q1/2)
∑
n∈
/CI
(−1)nqn(n+1)/4λnB1/2 ˆf (1)(q
n
2 λt, q).
(202)
Now the top of the Newton polygon has one edge of slope 0. We ﬁnd th e solution satisﬁes
g(0)(t, q) =
∞∑
k=0
βk(q)t−k θ(ρ−1t; q)
θ(t; q) where βk(q) − q−kρ−1(1 − qkρ−1)2βk+1(q) = 0 . (203)
Therefore, as the indicial polynomial is
(1 − q−1ρ−1)2β0(q) = 0 (204)
40 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
we take ρ = q−1eε and expand to order ε2 to ﬁnd solutions
g(0)(t, ε, q) =
∞∑
k=0
(−1)k qk(k+1)/2
(q; q)2
k
t−1−k
+
( ∞∑
k=0
(
1
2 E1(q) − 1
2 − θ′(t−1; q)
θ(t−1; q) +
k∑
j=1
1 + qj
1 − qj
)
(−1)k qk(k+1)/2
(q; q)2
k
t−1−k
)
ε + O(ε2) ,
(205)
where E1(q) = 1 − 4∑ ∞
j=1
qj
1−qj . Therefore, we have solutions
g(0,0)(t, q) =
∞∑
k=0
(−1)k qk(k+1)/2
(q; q)2
k
t−1−k
g(0,1)(t, q) =
∞∑
k=0
(
1
2 E1(q) − 1
2 − θ′(t−1; q)
θ(t−1; q) +
k∑
j=1
1 + qj
1 − qj
)
(−1)k qk(k+1)/2
(q; q)2
k
t−1−k.
(206)
