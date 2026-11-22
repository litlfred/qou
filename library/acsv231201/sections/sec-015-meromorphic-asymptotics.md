---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-015-meromorphic-asymptotics
section_title: "Meromorphic asymptotics"
section_number: null
pages: 80-85
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
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
64 Univariate asymptotics

where p is a singularity of f(z) with minimal modulus. The exponential growth
rate of a, can be viewed as the coarsest measure of its asymptotic behavior.

Just as for rational functions, the singularities of f(z) give contributions to
the asymptotic behavior of a,,. For the rest of this section, we restrict to the
case where f locally behaves like a rational function near the singularities that
determine dominant asymptotics of a,. The asymptotic contributions of more
general types of singularities are discussed in Section 3.4 below.

Definition 3.5 (poles and meromorphic functions). We say that f has a pole
(or polar singularity) of order x € Z,o at the point z = w if f(z) cannot be ana-
lytically continued to z = w but (z — w)* f(z) can, and k is the smallest positive
integer with this property. A pole of order one is usually called a simple pole.
If f is either analytic or has a pole at every point of a set D c C then we say
f(2) is a meromorphic function on D.

Suppose now that f(z) is analytic on a closed disk D = {z € C: |z| < S}
for some S > 0, except at a nonempty collection {p1,...,;} of poles of orders
K1,...,k; Which lie in the interior of D (by our running assumption that a,
grows exponentially, the p; must be non-zero). If C_ is any positively oriented
circle around the origin with radius less than R = minj|p,|, and C, is the
positively oriented circle around the origin with radius S, then the Cauchy
residue theorem implies

1 do ad _< el
ami [, (set ~ an J, FOr = DRS fo]. 6)

For readers unfamiliar with complex residues, the residue of a function g(z) at
a pole z = w of order k can be defined by the explicit formula

1 — fae A
Res @(2) = Gy lim |= (c- 0) x) . (3.7)

which for a simple pole reduces to
Res g(z) = lim [tc - w)g(2)| . (3.8)

It is a classic result in complex analysis that if z = w is a pole of f(z) of order
k then for z in a neighborhood of w we can write f as a ratio f(z) = p(z)/q(z)
of analytic functions with p(w), q¢(w) # 0 and gw) = ++» = q—Yw) = 0
(taking a series expansion of g at z = w shows the converse is also true). We
can use such a representation to compute the residue of f at z = w.

Lemma 3.6. Under the assumptions of the previous paragraph,

Res f(z"! = w" Pn),
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
