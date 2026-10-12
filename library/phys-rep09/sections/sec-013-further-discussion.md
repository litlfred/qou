---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-013-further-discussion
section_title: "Further discussion"
section_number: null
pages: 19-21
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Theorem 9 provides sufficient conditions for the convergence of the Magnus series based on an estimate by the norm
of the operator A. In particular, it guarantees that the operator Ω(t) in Y(t) = exp Ω(t) can safely be obtained with the
convergent series P
k≥1 Ωk(t) for 0 ≤t < T when the terms Ωk(t) are computed with (51). A natural question at this stage
is — what is the optimal convergence domain? In other words, is the bound estimate rc = π given by Theorem 9 sharp or
is there still room for improvement? In order to clarify this issue, we next analyze two simple examples involving 2 × 2
matrices.
Example 1. Moan and Niesen [71] consider the coefficient matrix
A(t) =

2
t
0
−1

.
(74)
170
S. Blanes et al. / Physics Reports 470 (2009) 151–238
If we introduce, as before, the complex parameter ε in the problem, the corresponding exact solution Y(t; ε) of (70) is given
by
Y(t; ε) =

e2εt
1
9ε
e2εt −

1
9ε +
1
3
t

e−εt
0
e−εt


(75)
and therefore
log Y(t; ε) =

2t
g(t; ε)
0
−t

,
with g(t; ε) =
t(1 −e3εt + 3εt)
3(1 −e3εt)
.
The Magnus series can be obtained by computing the Taylor expansion of log Y(t; ε) around ε = 0. Notice that the function
g has a singularity when εt =
2π
3 i, and thus, by taking ε = 1, the Magnus series only converges up to t =
2
3π. On the
other hand, condition
R T
0 ∥A(s)∥ds < π leads to T ≈1.43205 < 2
3π. In consequence, the actual convergence domain of the
Magnus series is larger than the estimate provided by Theorem 9.
□
Example 2. Let us introduce the matrices
X1 =

1
0
0
−1

= σ3,
X2 =

0
1
0
0

(76)
and define
A(t) =

β X2
0 ≤t ≤1
α X1
t > 1
with α, β complex constants. Then, the solution of Eq. (30) at t = 2 is
Y(2) = eαX1eβX2 =

eα
βeα
0
e−α

,
so that
log Y(2) = log(eαX1eβX2) = αX1 +
2αβ
1 −e−2α X2,
(77)
an analytic function if |α| < π with first singularities at α = ±iπ. Therefore, the Magnus series cannot converge at t = 2 if
|α| ≥π, independently of β̸ = 0, even when it is possible in this case to get a closed-form expression for the general term.
Specifically, a straightforward computation with the recurrence (49)–(50) shows that
∞
X
n=1
Ωn(2) = αX1 + βX2 +
∞
X
n=2
(−1)n−1 2n−1Bn−1
(n −1)! αn−1β X2.
(78)
If we take the spectral norm, then ∥X1∥= ∥X2∥= 1 and
Z t=2
0
∥A(s)∥ds = |α| + |β|,
so that the convergence domain provided by Theorem 9 is |α| + |β| < π for this example. Notice that in the limit |β| →0
this domain is optimal.
□
From the analysis of Examples 1 and 2 we can conclude the following. First, the convergence domain of the Magnus series
provided by Theorem 9 is the best result one can get for a generic bounded operator A(t) in a Hilbert space, in the sense that
one may consider specific matrices A(t), as in Example 2, where the series diverges for any time t such that
R t
0 ∥A(s)∥ds > π.
Second, there are also situations (as in Example 1) where the bound estimate r = π is still rather conservative: indeed, the
Magnus series converges for a larger time interval than that given by Theorem 9. This is particularly evident if one takes A(t)
as a diagonal matrix: then, the exact solution Y(t; ε) of (70) is a diagonal matrix whose elements are non-vanishing entire
functions of ε, and obviously log Y(t; ε) is also an entire function of ε. In such circumstances, the convergence domain
|ε|
R t
0 ∥A(s)∥ds < π for the Magnus series does not make much sense. Thus, a natural question arises: is it possible to
obtain a more precise criterion of convergence? In trying to answer this question, in [31] an alternative characterization
of the convergence has been developed which is valid for n × n complex matrices. More precisely, a connection has been
established between the convergence of the Magnus series and the existence of multiple eigenvalues of the fundamental
matrix Y(t; ε) for a fixed t, which we denote by Yt(ε). By using the theory of analytic matrix functions, and in particular, of
the logarithm of an analytic matrix function (such as is done, e.g. in [76]), the following result has been proved in [31]: if the
analytic matrix function Yt(ε) has an eigenvalue ρ0(ε0) of multiplicity l > 1 for a certain ε0 such that: (a) there is a curve in
S. Blanes et al. / Physics Reports 470 (2009) 151–238
171
the ε-plane joining ε = 0 with ε = ε0, and (b) the number of equal terms in log ρ1(ε0), log ρ2(ε0), . . . , log ρl(ε0) such that
ρk(ε0) = ρ0, k = 1, . . . , l is less than the maximum dimension of the elementary Jordan block corresponding to ρ0, then
the radius of convergence of the series Ωt(ε) = P
k≥1 εkΩt,k verifying exp Ωt(ε) = Yt(ε) is precisely r = |ε0|. An analysis
along the same line has been carried out in [77].
When this criterion is applied to Example 1, it gives, as the radius of convergence of the Magnus series corresponding to
Eq. (70) for a fixed t,
Ωt(ε) =
∞
X
k=1
εk Ωt,k,
(79)
the value
r = |ε| =
2π
3t .
(80)
To get the actual convergence domain of the usual Magnus expansion we have to take ε = 1, and so, from (80), we get
2π/(3t) = 1, or equivalently t = 2π/3, i.e., the result achieved from the analysis of the exact solution.
With respect to Example 2, one gets [31]
|ε| =
π
|α|(t −1).
If we now fix ε = 1, the actual t-domain of convergence of the Magnus series is
t = 1 + π
|α|.
Observe that, when t = 2, we get |α| = π and thus the previous result is recovered: the Magnus series converges only for
|α| < π.
It should also be mentioned that the case of a diagonal matrix A(t) is compatible with this alternative
characterization [31].
