---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-007-53-lebowitz-penrose
section_title: "Lebowitz-Penrose"
section_number: 5.3
pages: 8-10
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
follow the method outlined in [Leb64] and starting with (5.10), we arrange our expression
r(s) into the form:
r(s) = C(β)−1
1 +u
s
u2
(
(1 +u)2e−s− (1 +u)
)
(5.17)
We use the identity: 1+u
u2 = (1+u)2
u2 − 1+u
u , to rewrite it as:
r(s) = C(β)−1
1 +u
(
s1 +u
u −s2 (1 +u)2
u2
(1−e−s
s
))
(5.18)
We make the change of variables v =s 1+u
u and deﬁne g(w) := 1−e−w
w and obtain:
ˆr(s) = C(β)−1
1 +u (v−v2g
( uv
1 +u
)
) (5.19)
We note that g′(w) = we−w−(1−e−w)
w2 = (w+1)e−w−1
w2
If we use the inequality ew≥ 1 +w, then 1 ≥ (1 +w)e−w and so 0 ≥ (1 +w)e−w− 1
and hence g is decreasing. We note that u ∈ (1,∞) and so u
u+1 ∈ ( 1
2, 1). Since g is
decreasing, we get maximum value at g(v
2), which would give a minimum value for the
VIRIAL EXPANSION BOUNDS 9
expression in brackets, which gives a bound uniform in u. This is an extra approximation in
the derivation of the virial coeﬃcient bounds, which is not made in the general derivation.
This is equivalent to realising that the g-function is dominated by its contribution at u = 1,
that is, when β = 0, so at high temperatures.
We then seek to maximise: f(v) =v−v2g( 1
2v). Upon diﬀerentiation we get:
f′(v) = 1− 2vg(1
2v)− 1
2v2g′(1
2v)
= 1− 2v
(
1−e− 1
2v
1
2v
)
− 1
2v2
(
( 1
2v + 1)e− 1
2v− 1
1
4v2
)
= 1− 4(1−e− 1
2v)− 2(1
2v + 1)e− 1
2v + 2
=−1 + 2e− 1
2v−ve− 1
2v (5.20)
When we set this to zero we get:
1 = (2−v)e− 1
2v (5.21)
changing parameters to δ = 1− 1
2v, we have:
e
2 =δeδ (5.22)
and so using the Lambert W-function again we get:
δ =W
(e
2
)
(5.23)
In our original expression:
˜f(δ) = 2− 2δ− (2− 2δ)2g(1−δ)
= 2(1−δ)− 4(1−δ)2
(1−eδ−1
1−δ
)
= (1−δ)(2− 4(1−eδe−1))
= 2(−1 +δ + 1
δ− 1)
= 2(W (e
2)− 1)2
W (e
2) (5.24)
This therefore gives us the bound
|ρ|≥ 2C(β)−1
1 +u
W (e
2)− 1)2
W (e
2) (5.25)
Leading to the coeﬃcient bound of:
|cn|≤ β−1
n C(β)n−1(1 +e2βB)n−1
( W (e
2)
2(W (e
2)− 1)2
)n−1
(5.26)
and the lower bound on the radius of convergence as:
C(β)−1 1
1 +e2βB 2(W (e
2)− 1)2
W (e
2) (5.27)
10 S. J. TATE
