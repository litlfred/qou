---
doc_id: arxiv-1905.06064v1
doc_title: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS"
section_id: sec-005-appendix-b-computations
section_title: "Appendix B. Computations"
section_number: null
pages: 26-26
source_pdf: 1905.06064v1.pdf
source_sha256: 3ffe25c8ee62779d
toc_source: outline
doc_brief: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS — We develop a regularity theory for extremal knots of scale invariant knot ener- gies deﬁned by J. O’hara in 1991."
---
Lemma B.1. For ϕ ∈C∞
c (Bρ), L ∈N, k ∈N, we have the estimate

Z
B2Lρ
Z
B2L+kρ\B2L+k−1
1
ρ(x, y)2
ρ(x, y)−2
y
Z
x
y
Z
x
|u(s) −u(t)||ϕ(s)v(s) −ϕ(t)v(t)| ds dt

p
2
dx dy

2
p
≾2−s(L+k) ∥v∥∞[u]W
1p ,p(B2L+kρ) ∥|∇|
1
p ϕ∥Lp
.
Proof. W.l.o.g. Bρ is centered around 0.
Note that the support of ϕ tells us that whenever x, y > ρ or x, y < −ρ,
1
ρ(x, y)2
ρ(x, y)−2
y
Z
x
y
Z
x
|u(s) −u(t)||ϕ(s)v(s) −ϕ(t)v(t)| ds dt

p
2
≡0.
Thus, it suﬃces to estimate
ρ
Z
−2Lρ
2L+kρ
Z
2L+k−1ρ
1
ρ(x, y)1+ 1
p
ρ(x, y)−2
y
Z
x
y
Z
x
|u(s) −u(t)||ϕ(s)v(s) −ϕ(t)v(t)| ds dt

p
2
dx dy
≾(2L+kρ)−2−p(2Lρ)(2L+kρ)

Z
B2L+kρ
Z
B2L+kρ
|u(s) −u(t)||ϕ(s)v(s) −ϕ(t)v(t)| ds dt

p
2
≾(2L+kρ)−1−p(2Lρ) ∥v∥
p
2∞(2L+kρ)p−2
Z
B2L+kρ
Z
B2L+kρ
|u(s) −u(t)|
p
2 |ϕ(s) −ϕ(t)|
p
2 ds dt
+ (2L+kρ)−1−p(2Lρ)(2L+kρ)p−2
Z
B2L+kρ
Z
B2L+kρ
|u(s) −u(t)|
p
2 |ϕ(t)|
p
2 |v(t) −v(s)|
p
2 ds dt
=(2L+kρ)−3(2Lρ) ∥v∥
p
2∞
Z
B2L+kρ
Z
B2L+kρ
|u(s) −u(t)|
p
2 |ϕ(s) −ϕ(t)|
p
2 ds dt
+ (2L+kρ)−3(2Lρ)
Z
B2L+kρ
Z
B2L+kρ
|u(s) −u(t)|
p
2 |ϕ(t)|
p
2 |v(t) −v(s)|
p
2 ds dt
≾(2L+kρ)−3(2Lρ) ∥v∥
p
2∞

Z
B2L+kρ
Z
B2L+kρ
|u(s) −u(t)|p ds dt

1
2

2L+kρ ∥ϕ∥p
Lp
 1
2
≾(2L+kρ)−5
2 (2Lρ) ∥v∥
p
2∞
(2L+kρ)1+1[u]p
W
1p ,p(B2L+kρ)

1
2 
ρ1∥|∇|
1
p ϕ∥p
Lp
 1
2
=(2L+k)−3
2 (2L) ∥v∥
p
2∞
[u]p
W
1p ,p(B2L+kρ)

1
2 
∥|∇|
1
p ϕ∥p
Lp
 1
2
□
