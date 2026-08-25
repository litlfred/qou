---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-003-22-quantum-vc
section_title: "Quantum VC"
section_number: 2.2
pages: 9-11
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
The second option for generalizing the volume conjecture (1.14) is to ask for higher-
order terms in the asymptotic expansion of the colored Jones polynomial. Let us deﬁne
a new “quantum” parameter ℏ as
ℏ = iπ
k , (2.13)
so that
q =e2ℏ. (2.14)
The two parameters N andk of the colored Jones polynomial can be traded for ℏ and
u, and the limit (2.1) is simply ℏ→ 0. At u = iπ, higher-order asymptotics are then
predicted [10, 11] to have the form
VN(K;q =e
2πi
N )
N→∞
∼ exp
(
1
2ℏ(Vol +iCS)− 3
2 log ℏ + 1
2 log−iπTK
4 +
∞∑
n=2
˜Snℏn−1
)
.
(2.15)
Here, for example, TK is the Ray-Singer torsion of the knot complement S3\K. It can
be deﬁned after putting any background metric on S3\K [25] as
T (M) = exp
(
−1
2
3∑
n=0
n(−1)n log det′∆n
)
= (det′ ∆0)
3
2
(det′ ∆1)
1
2
, (2.16)
where ∆n is the Laplacian acting on n-forms.
7We thank E. Witten for useful observations on this subject.
8
It is fairly straightforward to combine the present quantum deformation with the
parametrization of the volume conjecture in u. The expectation is that
JN(K;q)
N,k→∞
∼ exp
(
− 1
4ℏICS(A(u))− 3
2 log ℏ + 1
2 logiTK(u)
4π +
∞∑
n=2
Sn(u)ℏn−1
)
.
(2.17)
Here, TK(u) is a u-deformed torsion, and is related to the Alexander polynomial of K
[26]. The higher-order coeﬃcients in (2.15) are related to those in (2.17) as
∑
n≥2
˜Snℏn−1 =
∑
n≥2
Sn(iπ)ℏn−1− log sinh ℏ
ℏ . (2.18)
For the ﬁgure-eight knot, the quantum volume conjecture (2.17) was tested to ﬁrst
subleading order in [27], using the Ray-Singer torsion
T41(u) = 4π2
√
−m−4 + 2m−2 + 1 + 2m2−m4. (2.19)
Higher-order coeﬃcients Sn(u) can also be computed [11]. For example,
S2(u) = −i(T41)3
12(4π2)3m6
(
1−m2− 2m4 + 15m6− 2m8−m10 +m12)
, (2.20)
S3(u) =−2(T41)6
(4π2)6m6
(
1−m2− 2m4 + 5m6− 2m8−m10 +m12)
− 1
6. (2.21)
These expressions appear to be new, unexplored knot invariants with distinctive number-
theoretic properties. Needless to say, it would be interesting to test the quantum volume
conjecture (2.17) for other hyperbolic knots and/or to higher order in the ℏ-expansion.
Just as the generalization of the volume conjecture to u⁄= 0 was interpreted in
terms of the SL(2, C) Chern-Simons functional, there is also a Chern-Simons inter-
pretation of the quantum volume conjecture. One must consider how the functional
ICS(A) behaves when the connection A undergoes “quantum ﬂuctuations” away from
the ﬂat connection A(u). This is accomplished in physics via perturbative quantum
ﬁeld theory. Symbolically, we can write A =A(u) +A′, whereA′ contains the ﬂuctu-
ations away from ﬂatness, and deﬁne a perturbative “partition function” via the path
integral
Z(S3\K;u; ℏ)pert =
∫
DA′e− 1
4ℏICS (A(u)+A′). (2.22)
The exponent in the integrand has a critical point at A′ = 0, and a saddle point
expansion around this point yields the right-hand-side of (2.17). (To be very precise,
JN(K;q)∼ Z(S3\K; ℏ;u)/Z(S3; ℏ), where Z(S3; ℏ) =
√
2/k sin(π/k) is the partition
function of the three-sphere S3.)
9
