---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-006-52-morais-procacci-bound
section_title: "Morais-Procacci Bound"
section_number: 5.2
pages: 7-8
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
bounds using the method outlined in Section 4.
In the recent paper [Mor13], Morais and Procacci obtain a bound for the virial coeﬃcients
via the Canonical Ensemble, using polymer expansion methods and the bounds for cluster
coeﬃcients, in the form:
|nbn|≤ nn−1
n! e2βB(n−2)C(β)−1 (5.8)
The values a = C(β)−1e−4βB; b = e2βBCβ; and thus ab = e−2βB are substituted into
(4.9), so that we get:
r(s) =s(e−s(1 +e−2βB)C(β)−1e−2βB−C(β)−1e−4βB) (5.9)
If we let u =e2βB, then our equation becomes:
r(s) =C(β)−1 1
us(e−s(1 + 1
u)− 1
u) (5.10)
We reiterate the remark that s∈ (0, ln(1 +u)) so that we change variables (monotonically)
to s = ln(1 +u(1−e−α)), so that:
8 S. J. TATE
˜r(α) = 1
C(β)u
(
ln(1 +u(1−e−α))
( u + 1
u(1 +u(1−e−α))− 1
u
))
(5.11)
= 1
C(β)u
ln(1 +u(1−e−α))
eα(1 +u(1−e−α)) (5.12)
This then gives us the bound for |ρ| as:
|ρ|≥ C(β)−1 max
α∈(0,∞)
ln(1 +u(1−e−α))
ueα(1 +u(1−e−α)) (5.13)
If we then follow the same argument before, we get the bound for the virial coeﬃcient as:
|cn|≤ β−1
n C(β)n−1(F(u))−(n−1) (5.14)
whereF(u) = maxa∈(0,∞)
ln(1+u(1−e−α))
ueα(1+u(1−e−α)).
The main improvement in the paper comes from better techniques of approximating virial
coeﬃcients. Using techniques involving Canonical Ensemble calculations for free energy and
its relationship as the Legendre transform of pressure, they obtain slightly better bounds on
the virial coeﬃcients, although still under the proviso that |ρ|≤ ρ∗, where ρ∗ is the radius
of convergence in (5.7). The improved estimates for the coeﬃcients seem to imply that there
may be a way of extending the radius of convergence, at least for temperatures for which
the bound on the coeﬃcient is an improvement. They obtain bounds on the coeﬃcient of
ρk+1 in the free energy as:
( 1
k + 1 + (eα∗
β− 1)eα∗
βk
)
e2βB(k−1) (k + 1)k
k! C(β)k (5.15)
whereα∗
β is the optimal α from (5.13). This leads to the (better) asymptotic bound for the
virial coeﬃcients as:
K
(e2βBC(β)
0.24026
)k
(5.16)
where K is a constant.
