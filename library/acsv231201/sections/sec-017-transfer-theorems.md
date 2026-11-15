---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-017-transfer-theorems
section_title: "Transfer theorems"
section_number: null
pages: 88-95
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Our proof of Darboux’s Theorem uses analyticity of ψ(z) = f(z)/(R −z)α be-
yond the disk of radius R only to provide a series development of f at z = R. By
making stronger use of analytic properties, and using a sharper estimate than
Lemma 3.9 to bound error terms, it is possible to do better. There are various
results along these lines, our favorite being the transfer theorems of Flajolet
3.4 Transfer theorems
71
and Odlyzko [FO90]. The idea of this approach is to establish an estimate of
the form an = O(n−α−1) for the coeﬃcients of any power series f(z) that is
analytic in neighborhood of the unit disk in a slit plane, except at z = 1 where
f(z) = O((1 −z)α).
Remark. To simplify our notation in this section we state our results for func-
tions with singularities at z = 1. As noted above, this loses no generality since
[zn]f(z/R) = R−n[zn] f(z) for any non-zero constant R and analytic function f.
The transfer theorem method is also ﬂexible enough to extend beyond pow-
ers to other branch singularities. Let alg-log be the class of functions that are
a product of a power of 1 −z, a power of z−1 log(1/(1 −z)), and a power
of log
h
z−1 log(1/(1 −z))
i
. We begin with a description of asymptotics for all
functions in the class alg-log, then discuss asymptotics of functions which lo-
cally behave as if they are in alg-log near their singularities.
Proposition 3.14. Let α, γ, δ ∈C \ N and let
f(z) = (1 −z)α
 1
z log
1
1 −z
!γ 1
z log
 1
z log
1
1 −z
!!δ
.
Then the power series coeﬃcients {an} of f satisfy
an ∼n−α−1
Γ(−α)(log n)γ(log log n)δ .
Proof
See [FO90, Theorem 3B].
□
Remark. When at least one of α, γ, or δ is a nonnegative integer, diﬀerent
formulae can hold. For example, when γ < N but δ = 0 and α ∈N the coinci-
dence of α with a nonnegative integer decreases the exponent of the logarithm
by one, giving the estimate
an ∼Cn−α−1(log n)γ−1 .
(3.10)
For any R > 0 and ε ∈(0, π/2), the ∆-domain (or Camembert-shaped
region) deﬁned by R and ε is
∆(R, ε) = {z ∈C : |z| < R + ε, z , R, | arg(z −R)| ≥π/2 −ε} ,
pictured in Figure 3.1.
Theorem 3.15 (Transfer Theorem). Let f(z) = P∞
n=0 anzn be analytic in a ∆-
domain ∆(1, ε). If g(z) = P∞
n=0 bnzn is in alg-log then the following statements
hold.
(i) If f(z) = O(g(z)) as z →1 then an = O(bn) as n →∞.
72
Univariate asymptotics
ε
ε
R
Figure 3.1 A ∆-domain.
(ii) If f(z) = o(g(z)) as z →1 then an = o(bn) as n →∞.
(iii) If f(z) ∼g(z) as z →1 then an ∼bn as n →∞.
Theorem 3.15 with g(z) = C(1 −z)α strengthens Theorem 3.12. So as not
to devote too much space to computation, we only prove Theorem 3.15 for the
subset of alg-log given by powers (1 −z)α.
Proof for g(z) = (1 −z)α.
We need only prove the ﬁrst two statements in the
theorem, as the third follows as an immediate consequence. Cauchy’s integral
formula implies an can be expressed as a sum of integrals
an = 1
2πi
Z
γ1
f(z)z−n−1dz + 1
2πi
Z
γ2
f(z)z−n−1dz
+ 1
2πi
Z
γ3
f(z)z−n−1dz + 1
2πi
Z
γ4
f(z)z−n−1dz
deﬁned by two parameters ξ and η, where
• γ1 is the circular arc parametrized by 1 + n−1e−it for ξ ≤t ≤2π −ξ,
• γ2 is the line segment between 1 + n−1eiξ and the number β of modulus 1 + η
and arg(β −1) = ξ,
• γ3 is the arc on the circle of radius 1 + η running between β and β the long
way, and
• γ4 is the conjugate of γ2, oriented oppositely.
Our argument works with any 0 < η < ε and any 0 < ξ < π/2 large enough
so that the curves are contained in ∆(1, ε); see Figure 3.2 for an illustration.
3.4 Transfer theorems
73
Suppose ﬁrst that f(z) = O((1 −z)α) near z = 1, so that for some K > 0 the
inequality |f(z)| ≤K|1 −z|α holds everywhere on the curves.
Figure 3.2 The contour γ.
On γ1 the modulus of f is at most Kn−α and the modulus of z−n−1 is at most
(1 −n−1)−n−1 ≤2e ≤6 so, since the length of the curve is less than 2πn−1, the
Cauchy integral over γ1 has size at most 6Kn−α−1.
On γ3 the z−n−1 factor reduces the modulus of the integrand to at most
C(η)(1+η)−n, where C(η) grows at most polynomially with η. Thus, the Cauchy
integral over γ3 is O(n−N) for any N ∈N.
By symmetry, it remains only to bound the integral over γ2. Set ω = eiξ and
parametrize the integral as z = 1+(ω/n)t for t from 1 to En, where E = |β−1|.
We have | f(z)| ≤K|z −1|α = K(t/n)α and |z|−n−1 =

1 + ωt
n

−n−1, so

Z
γ2
f(z)z−n−1dz

 ≤
Z
γ2
| f(z)||z−n−1|dz ≤
Z En
1
K
 t
n
α 

1 + ωt
n

−n−1 dt
n
≤Kn−α−1
Z ∞
1
tα

1 + ωt
n

−n−1
dt.
(3.11)
The inequality |1 + ωt/n| ≥1 + Re{ωt/n} = 1 + (t/n) cos(ξ) implies an upper
bound of
Z ∞
1
tα
 
1 + t cos(ξ)
n
!−n−1
dt
74
Univariate asymptotics
for the integral in (3.11), which can be relaxed to
Jn =
Z ∞
1
tα
 
1 + t cos(ξ)
n
!−n
dt
because cos(ξ) > 0. The integrand of Jn monotonically decreases as n in-
creases, and is ﬁnite for any positive n larger than the real part of α, so the
decreasing limit is
J = lim
n→∞Jn =
Z ∞
1
tαe−t cos(ξ) dt ,
which is ﬁnite as 0 < ξ < π/2. We have now bounded all four integrals by
multiples of n−α−1, so the proof of statement (i) in the theorem is complete.
The proof of statement (ii) is contained in this argument too. When | f(z)| ≤
Kg(z) then the integral over γ1 is bounded above by 6Kn−α−1, the integral over
γ3 is o(n−α−1), and the integrals over γ2 and γ4 are bounded by JKn−α−1. Fur-
thermore, the contributions to each of these four integrals from parts of γ at
distance greater than any ﬁxed δ > 0 from 1 are o(n−α−1). If f(z) = o(g(z)) at
z = 1 then for any ε > 0 there is a δ such that | f(z)| ≤ε|g(z)| when |1 −z| ≤δ.
It follows that an ≤(2J + 6 + o(1))εn−α−1. This is true for every ε > 0, whence
an = o(n−α−1).
□
Example 3.16 (Catalan asymptotics). Let an =
1
n+1
2n
n

be the nth Catalan
number, whose generating function
f(z) =
∞
X
n=0
anzn = 1 −
√
1 −4z
2z
=
1 −2
q
1
4 −z
2z
was described in Example 2.14 of Chapter 2. The function f(z) has an algebraic
singularity at z = 1/4, near which the asymptotic expansion for f begins
f(z) = 2 −4
r
1
4 −z + 8
 1
4 −z
!
−16
 1
4 −z
!3/2
+ O

 1
4 −z
!2.
Note that f(z)/ √1/4 −z is not analytic in any disk of radius 1/4+ε, since both
integral and half-integral powers appear in f, but f is analytic in a ∆-domain.
Since the integral powers of (1−z) do not contribute to asymptotic behavior as
3.4 Transfer theorems
75
they are polynomials, Theorem 3.15 thus gives an expansion
an = −4 · 4n
−
1
4n
3
2 √π
−
3
32n
5
2 √π
+ O

n−7
2 
|                                          {z                                          }
[zn](1/4−z)1/2
−16 · 4n
 −3
32n
5
2 + O

n−7
2 !
|                    {z                    }
[zn](1/4−z)3/2
+ O

4nn−7
2 
|     {z     }
[zn]O((1/4−z)2)
= 4n
 
n−3
2 1√π −n−5
2
9
8 √π + O

n−7
2 !
.
◁
Exercise 3.5 (common subexpression problem). Flajolet and Odlyzko [FO90]
quote the generating function
f(z) = 1
2z
X
p≥0
1
p + 1
 2p
p
!  p
1 −4z + 4zp+1 −
√
1 −4z

involved in the representation of trees by directed acyclic graphs.
(a) Show that the minimal modulus singularity occurs at z = 1/4, around
which
f(z) ∼
c
p
(1 −4z) log(1 −4z)−1 .
(b) Compute the asymptotic behavior of the coeﬃcients of f (you can check
your answer against [FO90, (6.7b)]).
Example 3.17 (branching random walk: logarithmic singularity). For an ex-
ample including a logarithmic term, recall from Example 2.13 the implicit
equation
φ(z) = [(1 −p)z + pφ(φ(z))]2 .
This characterizes the probability generating function for the number X of par-
ticles to reach the origin in a binary branching nearest-neighbor random walk
with absorption at the origin. Aldous (see [AB05, Theorem 29] and [Ald98,
Theorem 6]) showed that there is a critical value p = p∗satisfying 16p∗(1 −
p∗) = 1, such that if p > p∗then X is sometimes inﬁnite, while if p < p∗then
X is never inﬁnite. At the critical value X is always ﬁnite, and it is of interest
to know the likelihood of large values of X.
Below, we show that
φ(z) = 1 −1 −z
4p −(c + o(1))
1 −z
log(1/(1 −z)),
(3.12)
76
Univariate asymptotics
where c = log(1/(4p))/(4p) and the statement holds for z ∈[0, 1] (the interest-
ing situation is when z →1). If we knew this for all z in a ∆-domain, we could
use (3.10) to conclude an ∼cn−2(log n)−2, so that X has a ﬁrst moment but not
a “1 + log” moment. Here we establish (3.12) on the unit interval, although
it is probably true in a ∆-domain and this is left to the interested reader. Just
knowing (3.12), we can deduce information on the partial sums Pn
k=0 ak via a
Tauberian theorem of Hardy and Littlewood, and perhaps asymptotic informa-
tion on an itself (see [FS09, Sec. VI.11]).
To show (3.12), ﬁx 0 < z0 < 1 and consider the iterates zn = φ(−n)(z0) of
the inverse of φ. The function φ is convex on [0, 1] with φ(0) > 0, φ(1) = 1,
and one other ﬁxed point k with p∗< k < 1. Because φ(x) < x on (k, 1), if
we iterate φ on any point in (c, 1) it converges downward to c. Likewise, if we
iterate the inverse function φ−1 starting with any point in (c, 1), it converges
upwards to 1, so zn ↑1. The recursion for φ gives
zn = ((1 −p)zn+1 + pzn−1)2,
and changing variables to yn = 1 −zn implies
yn = 1 −((1 −p)(1 −yn+1) + p(1 −yn−1))2
= 1 −(1 −((1 −p)yn+1 −pyn−1))2.
Solving for yn+1 gives
yn+1 = 1 −
p
1 −yn −pyn−1
1 −p
.
Setting xn = yn/(4p)n and using 16p(1 −p) = 1 results in
xn+1 = 2xn −xn−1 + O(yn)2.
Verifying ﬁrst that yn is small, we then approximately solve the linear re-
currence for xn to obtain xn ∼An + B, for some constants A, B, whence
yn ∼(4p)n(An + B). We may write this as
yn+1 = 4pyn + (1 + o(1)) yn+1
n + 1 = 4pyn + (1 + o(1))
yn+1
log yn+1/ log(4p).
Let z = 1 −yn+1 so φ(z) = 1 −yn. We then have
1 −φ(z) = 1 −z
4p −(1 + o(1))1 −z
4p
log(4p)
log(1 −z)
for all real z ↑1, proving (3.12).
◁
