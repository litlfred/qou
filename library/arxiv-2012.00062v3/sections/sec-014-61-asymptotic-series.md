---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-014-61-asymptotic-series
section_title: "Asymptotic series"
section_number: 6.1
pages: 45-47
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
the 52 knot. The state-integral for the52 knot [AK14, Eqn.(39)] (after removing a prefactor
that depends onu alone)
Z52(u;τ) =
∫
R +i0
Φb(v) Φb(v +u) Φb(v−u) e−2πiv2
dv. (230)
After a change of variablesu↦→u/(2πb) (see Equation (2)) andv↦→v/(2πb), it follows that
the integrand ofZ52(ub;τ) has a leading term given byeV (u,v)/(2πiτ) where
V (u,v ) = Li2(−ev) + Li2(−eu+v) + Li2(−e−u+v) + (v)2. (231)
Taking derivative with respect tov gives the equation for the critical point
2v− log(1 + ev)− log(1 + eu+v)− log(1 + e−u+v) = 0 (232)
which implies thatx = e2πbu and y =−e2πbv are points of the aﬃne curveS given by
S :y2 = (1−y)(1−xy)(1−x−1y) (233)
46 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
and (u,v ) are points of the exponentiated curveS∗ given by the above equation with(x,y ) =
(eu,−ev). Moreover,
V (u,v ) = Li2(y) + Li2(xy) + Li2(x−1y) + (log(−y))2 (234)
is a holomorphic C /2π2Z -valued function on the exponentiated curveS∗. Note that when
u = 0, Equation (233) becomes (73).
The constant term of the asymptotic expansion is given by the Hessian ofV (u,v ) at a
critical point (u,v ), and it is a rational function ofx and y is given by
δ(x,y ) =y− (1 +x +x−1)y−1 + 2y−2. (235)
Note thatδ(x,y ) = 0 on S if and only ifx is a root of the discriminant ofS with respect to
y, i.e.,
1− 6x + 11x2− 12x3− 11x4− 12x5 + 11x6− 6x7 +x8 = 0. (236)
This happens at two points in the real line given approximately by x ≈ 0.235344 and
x≈ 4.24909. Moreover, whenx is a root of (236), exactly two out of the three branches of
y =y(x) collide, and the corresponding branch point is simple.
Beyond the leading asymptotic expansion and its constant term, the asymptotic series has
the form Φ(x,y ;τ) where
Φ(x,y ;τ) = exp
(V (u,v )
2πiτ
)
ϕ(x,y ;τ), ϕ (x,y ;τ)∈ 1√
iδ
Q [x±,y±,δ−1][[2πiτ]] (237)
whereδ is given in (235) and
√
iδϕ (x,y ; 0) = 1. In other words, the coeﬃcient of every power
of 2πiτ in
√
δϕ (x,y ;τ) is a rational function onS. There is a natural projectionS→ C ∗
given by (x,y ) ↦→ x and we denote byyσ(x) the choice of a local section (an algebraic
function ofx), forσ∈P ={σ1,σ 2,σ 3}. We denote the corresponding seriesϕ(x,yσ(x);τ)
simply byϕσ(x;τ). When x is close to 1, we orderP so thatσ1,σ 2,σ 3 correspond to small
deformations away from geometric, conjugate, and real connections atx = 1. Note forσ3,
we only keep the real part ofV. The power series
√
iδϕσ(x;τ) can be computed by applying
Gaussian expansion on the state-integral (230), and one can compute up to 15 terms in a
few minutes. Let us write down the ﬁrst few terms ofϕσ(x;τ)
ϕσ(x; τ
2πi) = 1 + τ
24δ3
σ
(
81 + 112s− 78s2− 70s3 + 94s4− 38s5 + 5s6
+
(
138− 254s + 127s2 + 44s3− 89s4 + 38s5− 5s6)
yσ
+
(
135− 101s− 11s2 + 61s3− 33s4 + 5s5)
y2
σ
)
+O(τ 2), (238)
where
s =s(x) =x−1 + 1 +x. (239)
On the other hand, if one setsx to numerical values, the power series can be computed to
200 terms.
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 47
