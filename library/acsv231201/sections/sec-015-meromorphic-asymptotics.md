---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-015-meromorphic-asymptotics
section_title: "Meromorphic asymptotics"
section_number: null
pages: 80-88
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
---
Partial fraction decomposition gives a simple algebraic method to determine
asymptotics for rational generating functions. In this section we introduce an-
alytic techniques, allowing for a vast generalization from rational functions
to functions that behave locally like rational functions. Our arguments make
use of standard results about meromorphic functions and, although we make
our presentation as self-contained as possible, the reader not familiar with this
aspect of complex analysis can consult [Con78b] for further background.
Analytic methods require that the series f(z) represents an analytic function
3.2 Meromorphic asymptotics
63
at the origin. To that end, we now assume that the sequence {an} behaves ex-
ponentially, meaning there exist C1,C2 > 0 such that Cn
1 < |an| < Cn
2 for all
suﬃciently large n. Under this assumption, the open domain of convergence of
f(z) is a ﬁnite open disk around the origin, and the Cauchy Integral Formula
implies
an = 1
2πi
Z
C
f(z) dz
zn+1
(3.4)
whenever C is a simple closed contour enclosing the origin in this disk. The
domain of integration in a complex integral can be deformed without changing
the value of the integral, as long as the deformation stays where the integrand
is analytic. It is therefore crucial to understand where f(z) is not analytic.
Deﬁnition 3.3 (singularities). If D1 and D2 are domains (connected open sub-
sets) of C and g1(z) and g2(z) are analytic functions that agree on D1 ∩D2 , ∅
then we say g2 is a direct analytic continuation of g1 to D2. More generally,
we say that g2(z) is an analytic continuation of g1(z) if there exists a sequence
of direct analytic continuations on consecutively overlapping domains that be-
gins with g1 and end with g2. If f(z) can be analytically continued to the interior
of a simple closed curve γ but cannot be analytically continued to a neighbor-
hood of a point ω ∈γ then we call ω a singularity of f.
Example 3.4. If f(z) is a rational function with coprime numerator and de-
nominator then f has singularities at the roots of its denominator. Aside from
division by zero, the most common types of singularities encountered in com-
binatorial applications include substitution of zero into an algebraic root or
logarithm (see Section 3.4 below).
◁
One implication of the Cauchy Integral Formula is that the radius of conver-
gence 0 < R < ∞of f equals the minimum modulus of a singularity of f, and
this correspondence allows us to obtain a rough estimate of the growth of an.
Since
|an| =

1
2πi
Z
|z|=R−ε
z−n−1 f(z) dz

 ≤(R −ε)−n sup
|z|=R−ε
|f(z)| ,
we see that lim supn→∞|an|1/n ≤(R −ε)−1 for all 0 < ε < R. Conversely,
because there is a singularity of modulus R the power series for f does not
converge for |z| > R, so for any 0 < ε < R we have |an|1/n ≥(R −ε)−1 inﬁnitely
often. Thus, the exponential growth rate lim supn→∞|an|1/n of an satisﬁes
lim sup
n→∞
|an|1/n = 1
R = 1
|ρ| ,
(3.5)
64
Univariate asymptotics
where ρ is a singularity of f(z) with minimal modulus. The exponential growth
rate of an can be viewed as the coarsest measure of its asymptotic behavior.
Just as for rational functions, the singularities of f(z) give contributions to
the asymptotic behavior of an. For the rest of this section, we restrict to the
case where f locally behaves like a rational function near the singularities that
determine dominant asymptotics of an. The asymptotic contributions of more
general types of singularities are discussed in Section 3.4 below.
Deﬁnition 3.5 (poles and meromorphic functions). We say that f has a pole
(or polar singularity) of order κ ∈Z>0 at the point z = ω if f(z) cannot be ana-
lytically continued to z = ω but (z −ω)κ f(z) can, and κ is the smallest positive
integer with this property. A pole of order one is usually called a simple pole.
If f is either analytic or has a pole at every point of a set D ⊂C then we say
f(z) is a meromorphic function on D.
Suppose now that f(z) is analytic on a closed disk D = {z ∈C : |z| ≤S }
for some S > 0, except at a nonempty collection {ρ1, . . . , ρt} of poles of orders
κ1, . . . , κt which lie in the interior of D (by our running assumption that an
grows exponentially, the ρj must be non-zero). If C−is any positively oriented
circle around the origin with radius less than R = min j |ρj|, and C+ is the
positively oriented circle around the origin with radius S , then the Cauchy
residue theorem implies
1
2πi
Z
C+
f(z) dz
zn+1 −1
2πi
Z
C−
f(z) dz
zn+1 =
tX
j=1
Res
z=ρ j
h
z−n−1 f(z)
i
.
(3.6)
For readers unfamiliar with complex residues, the residue of a function g(z) at
a pole z = ω of order k can be deﬁned by the explicit formula
Res
z=ω g(z) =
1
(k −1)! lim
z→ω
" dk−1
dzk−1

(z −ω)kg(z)
#
,
(3.7)
which for a simple pole reduces to
Res
z=ω g(z) = lim
z→ω
h
(z −ω)g(z)
i
.
(3.8)
It is a classic result in complex analysis that if z = ω is a pole of f(z) of order
k then for z in a neighborhood of ω we can write f as a ratio f(z) = p(z)/q(z)
of analytic functions with p(ω), q(k)(ω) , 0 and q(ω) = · · · = q(k−1)(ω) = 0
(taking a series expansion of q at z = ω shows the converse is also true). We
can use such a representation to compute the residue of f at z = ω.
Lemma 3.6. Under the assumptions of the previous paragraph,
Res
z=ω f(z)z−n−1 = ω−nP(n),
3.2 Meromorphic asymptotics
65
where P(n) is a polynomial in n of degree k −1 with leading term expansion
P(n) = nk−1 (−1)k−1
k p(ω)
ωk q(k)(ω) + O(nk−2).
Proof
The vanishing of the repeated derivatives of q implies q(z) = q(k)(ω)
k! (z −
ω)k + h(z)(z −ω)k+1 for some function h(z) analytic at z = ω, so (3.7) yields
Res
z=ω f(z)z−n−1 =
1
(k −1)! lim
z→ω

dk−1
dzk−1

p(z)
q(k)(ω)
k!
+ (z −ω)h(z)
z−n−1

.
The product rule gives a ﬁnite sum expression for the repeated derivative in
this limit, each term of which is a multiple of ω−n times a polynomial in n. The
leading term of this polynomial in n is contained only in the summand
lim
z→ω

p(z)
q(k)(ω)
k!
+ (z −ω)h(z)
· dk−1
dzk−1

z−n−1= k! p(ω)
q(k)(ω) ω−n−k (−n)k−1
+ O(ω−n−knk−2),
and algebraic simpliﬁcation gives the stated result.
□
Exercise 3.2. Compute P(n) in Lemma 3.6 when f(z) = p(z)/q(z) = (2z −
1)/(2 −z −e1−z).
Combining Lemma 3.6 with (3.7) gives a generalization of Proposition 3.1
from rational functions to functions whose closest singularities to the origin
are poles.
Proposition 3.7 (meromorphic coeﬃcients). Suppose that f(z) is analytic on
a closed disk D = {z ∈C : |z| ≤S } for some S > 0, except at a nonempty
collection {ρ1, . . . , ρt} of non-zero poles of orders κ1, . . . , κt lying in the interior
of D. Then there exist polynomials P1(n), . . . , Pt(n) in n such that
[zn] f(z) = −
tX
j=1
Pj(n) ρ−n
j + O(S −n) ,
where P j(n) has degree κ j −1. If f(z) = p(z)/q(z) represents f as a ratio of
analytic functions at z = ρj with p(ρj) , 0 then the polynomial Pj(n) is the
polynomial P(n) in Lemma 3.6 with ω = ρj and k = κj. The terms of Pj(n) can
be computed explicitly from the evaluations of the ﬁrst κ j −1 derivatives of p
and the ﬁrst 2κ j derivatives of q at z = ρj.
Proof
Because f is analytic inside and on C−, the Cauchy integral formula
66
Univariate asymptotics
implies 1
2π
R
C−f(z) dz
zn+1 = an, and (3.6) can be rearranged to give
an = −
tX
j=1
Res
z=ρ j
h
z−n−1 f(z)
i
+ 1
2πi
Z
C+
f(z) dz
zn+1 .
Since f(z) is analytic on the circle C+, which is a compact set, the function
| f(z)| is bounded on C+, and

1
2πi
Z
C+
f(z) dz
zn+1

 ≤max
z∈C+ | f(z)| · S −n = O(S −n).
The stated forms for the residues follow from Lemma 3.6.
□
As was observed above for rational functions, if f(z) satisﬁes the conditions
of Proposition 3.7 and has a unique singularity closest to the origin then the
contribution of this point determines dominant asymptotics of an, up to an
exponentially smaller error. If f(z) has multiple poles of minimal modulus,
and several of them have maximum order, then we must consider cancellation
between their asymptotic contributions.
Example 3.8 (surjection asymptotics). As seen in Example 2.53, the number
an of surjections from a set of size n has exponential generating function
f(z) =
1
2 −ez .
This function is meromorphic in the entire complex plane, with poles at the
solutions Ξ = {log 2 + k2πi : k ∈Z} to the equation 2 −ez = 0 in the com-
plex plane. Writing p(z) = 1 and q(z) = 2 −ez, we see that ω ∈Ξ implies
p(ω), q′(ω) , 0, so every element of Ξ is a simple pole. Because log 2 is the
unique element of Ξ with minimal modulus, Proposition 3.7 implies
an
n! ∼
−p(log 2)
(log 2)q′(log 2)
 
1
log 2
!n
= 1
2
 
1
log 2
!n+1
.
In fact, because all singularities of f(z) are poles, Proposition 3.7 allows us
to obtain an asymptotic expansion of an to arbitrary accuracy. If S > 0 is not
equal to the modulus of any element in Ξ, and ΞS denotes the elements of Ξ
with modulus at most S , then
an
n! =
X
ω∈ΞS
−p(ω)
ωq′(ω)ω−n + O  S −n = 1
2
X
ω∈ΞS
ω−n−1 + O  S −n .
◁
3.3 Darboux’s method
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
