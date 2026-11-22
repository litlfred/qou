---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-019-45-number-of-distinct-prime-divisors-of-a-random
section_title: "Number of distinct prime divisors of a random integer"
section_number: 4.5
pages: 56-58
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
As pointed out in the introduction, number theory provides another area
where the phenomenon of mod-Poisson convergence is prominent; see in
particular the discussion of [26, Section 7.2]. Consider as in Example 1.7
the number ω(Nn) of distinct prime divisors of a random integer chosen
TOME 70 (2020), FASCICULE 3
1170
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
uniformly in [[1, n]]. This quantity satisﬁes the celebrated Erdős–Kac central
limit theorem:
ω(Nn) −log log n
√log log n
⇀NR(0, 1),
where NR(0, 1) denotes a standard one-dimensional Gaussian distribution
of mean 0 and variance 1 (cf. [25]). This Gaussian approximation actually
comes from a more precise Poissonian approximation, which can be stated
in the framework of mod-Poisson convergence:
Theorem 4.8 (Rényi–Turán). — Locally uniformly in z ∈C,
E[ezω(Nn)] = e(log log n+γ)(ez−1)
×

Y
n∈N

1 + ez −1
n

e−ez−1
n
Y
p∈P

1 + ez −1
p

e−ez−1
p
+ O

1
log n

.
This formula ﬁrst appeared in [50], and it can be obtained by an appli-
cation of the Selberg–Delange method, see [57, Chapter II.5]. It is actually
stronger than the prime number theorem, as it requires a larger zero-free re-
gion of the Riemann zeta function than the line Re(s) = 1. The problem of
the rate of convergence in the Erdős–Kac central limit theorem was already
studied by Harper in [31] for the Kolmogorov distance to the Gaussian ap-
proximation; and by Barbour, Kowalski and Nikeghbali in [7] for the three
distances to the Poissonian (or signed measure) approximation.
Note that the residue
ψ(ξ) =
Y
n∈N∗

1 + eiξ −1
n

e−eiξ−1
n
Y
p∈P

1 + eiξ −1
p

e−eiξ−1
p
can be rewritten as
exp

X
k⩾2
(−1)k−1 pk(N∗−1 + P−1)
k
(eiξ −1)k

,
where pk(N∗−1 + P−1) = P∞
n=1
1
nk + P
p∈P
1
pk . Therefore:
Theorem 4.9. — For any r ⩾1, we introduce the scheme of approxi-
mation (σ(r)
n )n∈N, deﬁned by the Fourier transforms
d
σ(r)
n (ξ) = e(log log n+γ)(eiξ−1)
 r
X
k=0
ek(N∗−1 + P−1) (eiξ −1)k
!
,
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1171
where the parameters ek(N∗−1 + P−1) correspond to the specialisation of
Sym:
p1(N∗−1 + P−1) = 0 ;
pk⩾2(N∗−1 + P−1) = ζ(k) +
X
p∈P
1
pk .
With log2 n := log log n, one has the asymptotic formulas:
dL(ω(Nn), σ(r)
n ) = |er+1(N∗−1 + P−1) Gr+1(zr+2)|
√
2π (log2 n)
r
2 +1
+ o

1
(log2 n)
r
2 +1

;
dK(ω(Nn), σ(r)
n ) = |er+1(N∗−1 + P−1) Gr(zr+1)|
√
2π (log2 n)
r+1
2
+ o
 
1
(log2 n)
r+1
2
!
;
dTV(ω(Nn), σ(r)
n ) =
R
R |er+1(N∗−1+P−1) Gr+1(α)| dα
√
2π (log2 n)
r+1
2
+ o
 
1
(log2 n)
r+1
2
!
.
This theorem allows one to quantify how much better the Poisson ap-
proximation is in comparison to the Gaussian approximation (Erdős–Kac
theorem). Indeed, since the case r = 1 of Theorem 4.9 is the basic scheme
of approximation of ω(Nn) by a Poisson random variable Yn of parameter
λn = log2 n + γ, one has:
dK
 
ω(Nn) −log2 n −γ
p
log2 n + γ
, P(log2 n+γ) −log2 n −γ
p
log2 n + γ
!
= dK(ω(Nn), P(log2 n+γ)) = O

1
log2 n

.
On the other hand, the classical Berry–Esseen estimate for sums of identi-
cally distributed random variables ensures that
dK
 
P(log2 n+γ) −log2 n −γ
p
log2 n + γ
, NR(0, 1)
!
= O
 
1
p
log2 n
!
.
Thus, in terms of Kolmogorov distance, the Poisson approximation of the
sequence (ω(Nn))n∈N is at distance O(
1
log2 n), whereas the Gaussian ap-
proximation is at distance O(
1
√
log2 n). Similar remarks can be made for
the statistics of random combinatorial objects previously studied.
