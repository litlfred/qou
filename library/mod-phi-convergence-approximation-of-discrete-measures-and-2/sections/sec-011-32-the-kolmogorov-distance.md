---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-011-32-the-kolmogorov-distance
section_title: "The Kolmogorov distance"
section_number: 3.2
pages: 27-29
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
To evaluate the Kolmogorov distance between µn and νn, we use the
classical integral formula
µn([[k, +∞]]) −νn([[k, +∞]]) =
Z
T
(ψn(ξ) −χn(ξ)) eλnφ(ξ)
e−ikξ
1 −e−iξ
dξ
2π .
Indeed, for any l ⩾k, one has
µn([[k, l]]) −νn([[k, l]]) =
l
X
j=k
Z
T
(ψn(ξ) −χn(ξ)) eλnφ(ξ) e−ijξ dξ
2π
=
Z
T
(ψn(ξ) −χn(ξ)) eλnφ(ξ) e−ikξ −e−i(l+1)ξ
1 −e−iξ
dξ
2π .
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1141
Since ψn(ξ) −χn(ξ) = βn (iξ)r+1 (1 + o(1)), the quotient
ψn(ξ)−χn(ξ)
1−eiξ
is
actually a continuous function on the torus, hence bounded. The same
holds for eλnφ(ξ) = E[eiξYn], where Yn is an inﬁnitely divisible random
variable with exponent λnφ. Thus,
f(ξ) = ψn(ξ) −χn(ξ)
1 −eiξ
eλnφ(ξ)
is a bounded continuous function, hence in L 1(T), and by the Riemann–
Lebesgue lemma, one concludes that
lim
l→+∞
Z
T
f(ξ) e−i(l+1)ξ dξ
2π = 0.
Since liml→+∞µn([[k, l]]) −νn([[k, l]]) = µn([[k, +∞]]) −νn([[k, +∞]]), the
integral formula is indeed shown. It leads to the analogue of Proposition 3.2
for probabilities of half-lines of integers [[k, +∞]]:
Proposition 3.5. — The error term being uniform in k ∈Z, one has
µn([[k, +∞]]) −νn([[k, +∞]])
=
(−1)r β
√
2π (σ2λn)
r+1
2
∂r
∂αr

e−α2
2


α= k−λnm
σ√
λn
+ o
 
1
(λn)
r+1
2
!
.
Proof. — One has the Taylor expansion
ψn(ξ) −χn(ξ)
1 −e−iξ
= βn(iξ)r+1
iξ
(1 + oξ(1)) = βn(iξ)r (1 + oξ(1)).
Combined with the aforementioned integral formula and with the same
Laplace method as in Proposition 3.2, it yields
µn([[k, +∞]]) −νn([[k, +∞]]) = β (1 + o(1))
(σ2λn)
r+1
2
Z ∞
−∞
(it)r e−t2
2 e
−it k−λnm
σ√
λn dt.
Therefore, one has the same asymptotics as in Proposition 3.2, but with r
replacing r + 1.
□
The same argument as in Section 3.1 gives:
Theorem 3.6. — Under the assumptions stated at the beginning of this
section (general scheme of approximation with condition (H1)), one has
dK(µn, νn) = |β| |Gr(zr+1)|
√
2π (σ2λn)
r+1
2
+ o
 
1
(λn)
r+1
2
!
.
Example 3.7. — Consider the basic scheme of approximation of a mod-φ
convergent sequence of random variables (Xn)n∈N:
c
νn(ξ) = eλnφ(ξ).
TOME 70 (2020), FASCICULE 3
1142
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Hence, νn is the law of an inﬁnitely divisible random variable Yn with Lévy–
Khintchine exponent λnφ. Then, if c
µn(ξ) = eλnφ(ξ) ψn(ξ) and ψn(ξ) →ψ(ξ)
in C 1(T), the hypothesis (H1) is satisﬁed with r = 0 and βn →β = ψ′(0).
Therefore, in this setting,
dL(Xn, Yn) = |ψ′(0)| e−1
2
√
2π σ2λn
+ o
 1
λn

;
dK(Xn, Yn) =
|ψ′(0)|
√2π σ2λn
+ o

1
√λn

.
The second result should be compared with a computation in [26, Chap-
ter 4], which ensures that
dK(Xn, Yn) = |ψ′(0)|
√2π λn
+ o

1
√λn

if (Xn)n∈N is a sequence of random real numbers that converges mod-
Gaussian with parameters λn, and if (Yn)n∈N is a sequence of random
Gaussian variables with means 0 and variances λn.
