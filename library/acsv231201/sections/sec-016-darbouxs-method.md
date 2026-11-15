---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-016-darbouxs-method
section_title: "Darboux's method"
section_number: null
pages: 85-88
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
67
3.3 Darboux’s method
The fact that the asymptotic contribution of a pole singularity ω is easy to
compute using the theory of residues is partially a reﬂection of the fact that
f(z) is analytic in a punctured disk around ω, which is a disk centered at ω
with the center removed. Unfortunately, this property no longer holds near
singularities where f(z) locally behaves like a complex logarithm or a non-
integral power, due to the branch cuts required to deﬁne such functions. A
singularity where branch cuts are required to discuss local behavior of f(z)
is called a branch point, and in this section we illustrate a classical method
for computing asymptotics in the presence of a branch point coming from a
non-integral power.
Our ﬁrst general asymptotic result (3.5), which bounded the exponential
growth of an, was achieved by pushing the domain of integration in the Cauchy
integral to the boundary of the domain of convergence of f(z). Crucially, even
if f(z) admits a branch point on the boundary of its domain of convergence,
such a deformation can be performed without needing to cross a branch cut.
Integrating a slight modiﬁcation of f(z) on the boundary of the domain of con-
vergence leads to Darboux’s method and Darboux’s Theorem. Before describ-
ing Darboux’s method we require two preliminary results, the ﬁrst of which
asymptotically bounds integrals of smooth functions.
Lemma 3.9. Suppose a complex-valued function f is k times continuously
diﬀerentiable on the circle γ of radius R for some integer k ≥0. Then
Z
γ
z−n−1 f(z) dz = O

n−kR−n
as n →∞.
Proof
Replacing f(z) by f(z/R) we may assume without loss of generality
that R = 1. Integrating by parts shows
Z
γ
z−n−1 f(z) dz =
Z
γ
1
nz−n f ′(z) dz ,
where the term involving z−n
−n f(z) vanishes because γ has no boundary, and
induction on k implies
Z
γ
z−n−1 f(z) dz =
1
k!
n
k

Z
γ
zk−n−1 f (k)(z) dz .
Since f (k) is continuous, it is bounded on the unit circle. Thus, the last integral
above is bounded independently of n and our result follows from the behavior
k!
n
k

∼nk when k is ﬁxed and n →∞.
□
68
Univariate asymptotics
Our second preliminary result concerns expansions of power functions.
Lemma 3.10. For any α ∈C the series (1−z)α has the power series expansion
(1 −z)α =
X
n≥0
(−1)n
 α
n
!
zn,
which converges for |z| < 1, where
 α
n
!
=
Qn
j=1(α −j + 1)
n!
.
Furthermore, if α < N then there is a series expansion
 α
n
!
= n−α−1
Γ(−α)
1 +
∞
X
k=1
ek
nk

as n →∞, where each ek is a polynomial in α of degree 2k that can be com-
puted explicitly.
Proof
The series expansion of (1 −z)α is Newton’s generalized binomial the-
orem. The series expansion for
α
n

follows from an asymptotic analysis of the
Euler Gamma function, and can be found in [FS09, Theorem VI.1].
□
Darboux’s method consists of decomposing a generating function of interest
into the sum of an error term that can be bounded by Lemma 3.9 and a ﬁnite
number of terms that can be asymptotically approximated with Lemma 3.10.
The method dates back to nineteenth-century work of Darboux on complex
functions with algebraic singularities.
Example 3.11. The techniques of Section 2.5 often give non-rational (or even
non-algebraic) generating functions to which Darboux’s method can be ap-
plied. For instance, if C denotes the class of even length cycles of length at
least four, with exponential generating function
C(z) =
X
n≥2
z2n
(2n)! = 1
2 log
1
1 −z2 −z2
2 ,
then the class P of permutations with disjoint cycles of even length at least
four has exponential generating function
P(z) = eC(z) =
e−z2/2
√
1 −z2 .
Since P is a function of z2, we make the substitution t = z2 and analyze f(t) =
3.3 Darboux’s method
69
P( √t) = e−t/2/
√
1 −t. The Taylor series expansion e−t/2 = e−1/2 + e−1/2
2 (1−t)+
O((1 −t)2) at t = 1 proves that we can write
f(t) = e−1/2(1 −t)−1/2 + e−1/2
2
√
1 −t + ψ(t)
for some C1 function ψ(t). Lemma 3.9 then implies
[tn] f(t) = e−1/2[tn](1 −t)−1/2 + e−1/2
2
[tn](1 −t)1/2 + o

n−1
,
so Lemma 3.10 shows that the counting sequence pn of P satisﬁes
p2n
(2n)! = [tn] f(t) ∼e−1/2
Γ(−α)n−1/2 = e−1/2
√πn .
◁
Exercise 3.3. Find real constants C , 0 and β such that the generating function
f(t) in Example 3.11 satisﬁes
tn f(t) = e−1/2
√πn + (C + o(1))nβ .
As seen in Example 3.11, it is common that a generating function is an
analytic function multiplied by a pure power. Applying Darboux’s method in
this context gives the following result.
Theorem 3.12 (Darboux’s Theorem). Suppose that f(z) = (1 −z/R)αψ(z) for
some R > 0, where α < N and ψ is analytic on the closed disk |z| ≤R and
satisﬁes ψ(R) , 0. If the expansion of ψ about R is ψ(z) = P∞
n=0 bn(R −z)n then
the power series coeﬃcients {an} of f have an asymptotic expansion
an ≈R−n
∞
X
k=0
ckn−α−1−k,
where the coeﬃcient ck is an explicit linear combination of b0, . . . , bk. In par-
ticular,
an ∼ψ(R)
Γ(−α)n−α−1R−n .
Proof
Again, by rescaling our variable we assume without loss of gener-
ality that R = 1. Lemma 3.10 implies that we can expand
α
n

into a series
in decreasing powers n−α−1−k with explicit coeﬃcients, making it possible to
convert an asymptotic series of the form an ≈P∞
k=0 c′
k(−1)nα+k
n

into a series
an ≈P∞
k=0 ckn−α−1−k with c0 = c′
0/Γ(−α). Thus, to prove our claimed result it
is suﬃcient to show that an can be expressed as a series in bk(−1)nα+k
n

.
70
Univariate asymptotics
Let m be a positive integer greater than Re{−α} and let ψm be the Taylor
series remainder such that
ψ(z) −
m
X
k=0
bk(1 −z)k = (1 −z)m+1ψm(z) .
Multiplying by (1 −z)α yields
f(z) −
m
X
k=0
bk(1 −z)α+k = (1 −z)α+m+1ψm(z)
on the open unit disk, and taking the coeﬃcient of zn on both sides implies
an −
m−1
X
k=0
bk(−1)n
 α + k
n
!
+ O(n−α−m−1) = [zn](1 −z)α+m+1ψm(z) .
(3.9)
By assumption α + m + 1 ≥0, so the function (1 −z)α+m+1ψm is ⌊α + m + 1⌋
times continuously diﬀerentiable on the unit circle and Lemma 3.9 implies
the right-hand side of (3.9) is O(n−α−m). Since this argument works for any m
suﬃciently large, this proves the desired series for an exists.
□
Example 3.13 (2-regular graphs: an algebraic singularity). Let
f(z) = e−z/2−z2/4/
√
1 −z
be the exponential generating function for the number an of 2-regular graphs
that was derived in Example 2.52 of Chapter 2. Applying Darboux’s Theorem
with R = 1, α = −1/2, and ψ = exp(−z/2 −z2/4) gives
an
n! ∼ψ(1)
Γ(−α)n−1/2 = e−3/4
√πn .
◁
Exercise 3.4. Use Darboux’s Theorem to compute an asymptotic estimate for
the coeﬃcients of the generating function f(z) =
1
1 −4z + z2 .
