---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-014-an-explicit-formula-for-rational-functions
section_title: "An explicit formula for rational functions"
section_number: null
pages: 78-80
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
---
For rational functions in one variable, it is possible to determine an exact for-
mula for an when n is suﬃciently large. For instance, when ρ , 0 the equality
[zn]
1
(1 −z/ρ)k =
 n + k −1
k −1
!
ρ−n
(3.1)
holds for k = 1 as the left-hand side is a geometric series, and repeated dif-
ferentiation proves inductively that it holds for all k ∈N. More generally,
suppose f(z) = p(z)/q(z) is any rational function that is analytic at z = 0.
We assume, without loss of generality, that p and q are relatively prime poly-
nomials with q having the distinct roots ρ1, . . . , ρt ∈C, and that q(0) = 1.
For each j ∈{1, . . . , t}, let mj denote the multiplicity of the root ρj and let
qj(z) = q(z)/(1 −z/ρ j)mj.
Because the qj have no common root, there exist polynomials p1, . . . , pt ∈
C[z] such that the numerator p of f can be written as a linear combination
p(z) = Pt
j=1 pj(z)q j(z). This yields a partial fraction decomposition
f(z) = p(z)
q(z) =
tX
j=1
p j(z)q j(z)
q(z)
= h0(z) +
tX
j=1
hj(z)
(1 −z/ρ j)mj ,
where h0, . . . , ht ∈C[z] and for every j ∈{1, . . . , t} the polynomial hj(z) has
60
3.1 An explicit formula for rational functions
61
degree at most mj −1 and does not vanish at ρj. Further decomposing each
term hj(z)/(1 −z/ρj)mj as a sum Pmj
i=0 ci j/(1 −z/ρj)i for constants ci j ∈C and
applying (3.1) then implies
an =
tX
j=1
m j
X
i=0
cij
 n + i −1
i −1
!
ρ−n
j
when n > deg(p0).
(3.2)
In this way, a partial fraction decomposition of f results in an explicit expres-
sion for the coeﬃcients in its power series expansion.
Proposition 3.1 (univariate rational coeﬃcients). Suppose f(z) = p(z)/q(z)
is the ratio of coprime polynomials p and q, where q has the distinct roots
ρ1, . . . , ρt ∈C and q(0) , 0. Then there exist N ∈N and polynomials
P1(n, x), . . . , Pt(n, x) ∈Q[n, x]
such that
[zn] f(z) =
tX
k=1
Pk(n, ρk) ρ−n
k
for all n ≥N. If the zero ρk of q(z) has multiplicity mk then as a function of n
the polynomial Pk(n, x) has degree mk −1 and leading term expansion
Pk(n, x) = nmk−1 (−1)mk
mk p(x)
xmk q(mk)(x) + O(nmk−2).
(3.3)
If q(z) has degree d then the polynomials P1, . . . , Pt have degree at most d in
x, and they can all be computed explicitly in polynomial time with respect to d.
Proof
The stated decomposition and the degree of Pk(n, x) as a polynomial in
n follow from (3.2) after noting that the binomial coeﬃcient
n+i−1
i−1

is a poly-
nomial of degree i −1 in n. The fact that each Pk(n, x) has rational coeﬃcients,
and a method to compute them, follows most easily from an analytic argument
given in Lemma 3.6 below. Each ρj is an algebraic number of degree at most
d, so the degree of Pk(n, x) in x can be taken to be at most d.
□
Proposition 3.1 has strong consequences for asymptotics. Most importantly,
the roots of q each give a contribution to the asymptotics of an, with the roots
of minimal modulus having the exponentially largest asymptotic contributions.
Remark 3.2. When q(x) has a unique root ρ1 of minimal modulus then
an = P1(n, ρ1) ρ−n
1 + O(ρ−n
† ),
62
Univariate asymptotics
where ρ† is any root of q(z) with second smallest modulus. When ρ1 has mul-
tiplicity one then P1(n, ρ1) is constant, and the expression
an = −
p(ρ1)
ρ1 q′(ρ1) ρ−n
1 + O(ρ−n
† )
gives an asymptotic expansion of an with exponentially small error term. When
q(x) has a unique root ρ1 of minimal modulus with multiplicity larger than one
then, because the coeﬃcients of P1(n, x) get rather unwieldy to compute, it is
common to give only the leading term (or the ﬁrst few terms) in P1(n, x) and
leave an error of polynomially smaller size. Algorithms to separate the roots
of a univariate polynomial by modulus are discussed in [GS96] and [MS21].
If there are several roots of q with minimal modulus then only those with
maximum multiplicity contribute to dominant asymptotic behavior. The exis-
tence of several roots of minimal modulus and maximum multiplicity means
one must compute the terms in Proposition 3.1 coming from each, and po-
tentially deal with cancellation in the powers of these roots. Because it can
be very diﬃcult to track algebraic relations between terms involving powers
of algebraic numbers with the same modulus, there are (perhaps surprisingly)
still open problems related to when such cancellation can occur. Thankfully,
the very pathological cases where it is diﬃcult to detect dominant asymptotic
behavior do not arise for combinatorial examples; see [Mel21, Section 2.2] for
further discussion of these issues.
Exercise 3.1. Let a0 and a1 be any real numbers and suppose an+1 = 10an −
25an−1 for all integers n ≥1. Explicitly determine the generating function
f(z) = P∞
n=0 anzn and use this to determine the asymptotic behavior of an as
n →∞. Split the parameter space determined by a0 and a1 into regions de-
pending on the diﬀerent asymptotic behaviors of an.
