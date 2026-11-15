---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-018-the-saddle-point-method
section_title: "The saddle point method"
section_number: null
pages: 95-107
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
77
3.5 The saddle point method
One of the crowning achievements of complex analysis is the development of
techniques to evaluate integrals through clever deformations of their contours
of integration. Much of this work can be grouped together under the umbrella
of the saddle point method, aimed at discovering the best deformation for an
asymptotic analysis. Unlike the techniques discussed above, saddle point meth-
ods do not require an integrand to have singularities, and it is common to use
a saddle point analysis in situations where transfer theorems cannot be utilized
(in fact, the presence of singularities can complicate the saddle point method).
In this section we give a short overview of univariate saddle point techniques,
with further development of the univariate case covered in Chapter 4 and mul-
tivariate generalizations discussed in Chapter 5.
The heart of the saddle point method is the following statement: when the
modulus of an integrand falls steeply on either side of its maximum, most of the
contribution to the integral comes from a small interval about the maximum.
If the descent is steep enough, multiplying the integrand by the length of the
interval where the modulus is suﬃciently near its maximum (or doing some-
thing slightly more fancy) gives an accurate estimate. Most contours, however,
cannot be used for this purpose: such an estimate cannot hold if the contour
can be deformed so as to decrease the maximum modulus of the integrand,
since then the integral would be less than the claimed estimate.
Let γ be a contour and let I = log f(z) −(n + 1) log z be the logarithm of the
Cauchy integrand in (3.4). Fixing z0 ∈γ, we write Re{I′} and Im{I′} for the real
and imaginary parts of the derivative at z0 of I restricted to the curve γ. If z0
maximizes the modulus of the Cauchy integrand on γ then Re{I′} = 0, however
it is not usually true that Im{I′} = 0. In fact, the Cauchy–Riemann equations
imply that Im{I′} equals the real part of the derivative at z0 of I along any
curve perpendicular to γ at z0. Thus, when Im{I′} , 0 the curve γ may be
locally perturbed, ﬁxing the endpoints but pushing the center in the direction
of increasing Re{I}, thereby decreasing the maximum modulus of the Cauchy
integrand on the contour. In other words, if the modulus of the integrand is
maximized on γ at z0, and this maximum cannot be reduced by perturbing γ,
then I′ must vanish at z0. The univariate saddle point method thus consists of
the following steps:
(i) locate the zeros of I′, which form a discrete set of points,
(ii) see whether the contour of integration can be deformed so as to minimize
Re{I} at such a point,
(iii) estimate the integral via a Taylor series expansion of the integrand.
78
Univariate asymptotics
In Chapter 4 we will see that for integrals of the form
Z
A(z) exp(−λφ(z))
with parameter λ going to inﬁnity, including the Cauchy integral, one can get
away with approximating the critical point z0(λ) by the critical point z0 for φ,
ignoring A and removing the dependence of z0 on λ. This approximation is
often good enough to provide an asymptotic expansion of the integral, but here
we consider cases where we can deal with z0(λ) directly. For the second step
above not to fail, either f must be entire or the saddle point where I′ vanishes
must have smaller modulus than the singularities of f. In practice this is often
satisﬁed, and this classic method is widely applicable. For instance, the seminal
paper [Hay56] deﬁnes a broad class of functions, called admissible functions,
for which the saddle point method works and can be automated.
Examples of saddle point integrals
Because we go into great detail on saddle point integrals in Chapter 4, here
we simply present two examples illustrating the theory. At their heart, these
examples rely on the estimate
Z
γ
A(z) exp(−λφ(z)) dz ∼A(z0)
s
2π
φ′′(z0)λ exp(−λφ(z0)),
(3.13)
where A and φ are smooth functions with Re{φ} minimized in the interior of γ
at a point z0 where φ′′ does not vanish. The approximation (3.13) follows from
Theorem 4.1, however we compute it directly in our ﬁrst example to illustrate
why it is true.
Example 3.18 (ordered-set partitions: an isolated essential singularity). Ex-
ample 2.51 implies that the exponential generating function for the number an
of ordered-set partitions of [n] is
f(z) = exp

z
1 −z

.
Our goal here is to prove the estimate
an ∼n!
r
1
4πen−3/4 exp

2 √n

,
starting with the Cauchy integral expression
an
n! = 1
2πi
Z
|z|=ε
exp

z
1 −z

z−n−1 dz
3.5 The saddle point method
79
Figure 3.3 The circle |z| = 1 −βn can be deformed to a rectangle with right edge
(bold) on the line x = 1 −βn and other edges arbitrarily far from the origin.
that holds for any 0 < ε < 1 (in fact, we will select ε to vary with n, with ε →0
as n →∞).
Following the outline of the saddle point method above, we let
I(z) = In(z) = −(n + 1) log z +
z
1 −z
be the logarithm of the integrand and begin by computing the points where the
derivative
I′(z) = −n −1
z
+
1
(1 −z)2
vanishes. The closest solution of I′(z) = 0 to the origin is 1 −βn where
βn = n−1/2 −1
2n−1 + O

n−3/2
,
(3.14)
and we thus take the Cauchy contour of integration to be the circle of radius
ε = 1 −βn (which is less than one for all n suﬃciently large). Because the
only singularities of the Cauchy integrand lie at the origin and the point z = 1,
without changing the value of the Cauchy integral we can deform this circle to
a rectangle with right edge on the line x = 1−βn and all other points arbitrarily
far from the origin (see Figure 3.3). When |z| ≥2 the modulus of the Cauchy
integrand is upper bounded by exp
 |z|
|z|−1

|z|−n−1 ≤e2|z|−n−1, meaning we can
take the left, top, and bottom edges of the rectangle in Figure 3.3 to inﬁnity
and use the change of variables z = 1 −βn + it to obtain
an
n! = 1
2πi
Z ∞
−∞
exp(I(1 −βn + it)) (i dt)
(3.15)
for n suﬃciently large, fulﬁlling the second step of the saddle point method.
80
Univariate asymptotics
The ﬁnal step is to prove an approximation of the form
1
2π
Z ∞
−∞
exp(I(1 −βn + it)) dt ∼1
2π
Z ∞
−∞
exp
"
I(1 −βn) + 1
2I′′(1 −βn)(it)2
#
dt,
(3.16)
where I(1−βn+it) is replaced by its second-degree Taylor approximation. This
is very useful because, as a Gaussian integral, the right-hand side of (3.16) can
be computed exactly,
1
2π
Z ∞
−∞
exp
"
I(1 −βn) + 1
2I′′(1 −βn)(it)2
#
dt =
s
1
2πI′′(1 −βn) exp(I(1−βn)) .
(3.17)
The estimate (3.16) – comparable to (3.13) with λ = n + 1 and φ(t) = −I(1 −
βn + it) – is veriﬁed through several integral bounds. The approximation (3.14)
for βn implies
I′′(1 −βn) =
n + 1
(1 −βn)2 + 2
β3n
= (2 + o(1))n3/2,
(3.18)
so that the right-hand side of (3.17) is
s
1
2πI′′(1 −βn) exp(I(1 −βn))
∼
r
1
4πn3/2 exp
 
−(n + 1) log(1 −βn) −1 + 1
βn
!
∼
r
1
4πn3/2 exp
 
−(n + 1)

−n−1/2 + O

n−3/2
−1 + n1/2 + 1
2 + O

n−1/2!
∼
r
1
4πen−3/4 exp

2 √n

.
Our claimed asymptotic result for an thus holds as long as we can show the
left and right sides of (3.16) are equal up to an error that is o

n−3/4 exp

2 √n

.
The approximation (3.18) suggests that the main contributions to the integrals
in (3.16) come from the region where t2n3/2 is not too small, meaning |t| is
roughly n−3/4 or smaller. Accordingly, we pick a cutoﬀL = 2n−3/4 log n a little
greater than that and break our integrals into the two parts |t| ≤L and |t| > L.
Up to the cutoﬀthe two integrals are close, and past the cutoﬀthey are both
3.5 The saddle point method
81
small. More precisely, deﬁne
M1 =
Z
|t|≥L

exp
"
I(1 −βn) + 1
2I′′(1 −βn)(it)2
# 

 dt
M2 =
Z
|t|≥n−1/2

exp[I(1 −βn + it)]

 dt
M3 =
Z
n−1/2>|t|≥L

exp[I(1 −βn + it)]

 dt
M4 =
Z
|t|<L

exp
"
I(1 −βn) + 1
2I′′(1 −βn)(it)2
#
−exp I(1 −βn + it)

 dt
so that
• M1 is the integral on the right-hand side of (3.16) beyond L,
• the sum of M2 and M3 bounds the integral on the left-hand side of (3.16)
beyond L,
• M4 bounds the diﬀerence between the left- and right-hand sides of (3.16) on
[−L, L],
• and the modulus of the diﬀerence between the left and right sides of (3.16)
is bounded by the sum M1 + M2 + M3 + M4.
Letting M = exp[I(1 −βn)], we prove M1, M2, and M3 have upper bounds of
the form M · exp(−c(log n)2) for some c > 0, and that M4 = o(Mn−3/4). These
bounds all lie in o

n−3/4 exp

2 √n

, completing our derivation of asymptotics
for this example.
Bound on M1 We bound M1 with a standard Gaussian tail estimate. For any
a,C > 0
Z
|t|≥C
e−at2dt = 2
Z
t≥C
e−at2dt = 2e−aC2 Z
t≥0
e−at2−2aCtdt
≤2e−aC2 Z
t≥0
e−at2dt
=
p
π/ae−aC2,
so the growth rates of I′′(1 −βn) and L give the asserted upper bound on M1
for any c < 8.
Bound on M2 To bound M2, observe ﬁrst that if |t| ≥n−1/2 then the exponent
−t2/(β3
n + βnt2) decreases to −β−1
n ∼−√n. This is small, but integrating it over
82
Univariate asymptotics
the unbounded region [n−1/2, ∞] requires us to be careful. In particular, we use
the upper bound
| exp(I(1 −βn + it))|
exp(I(1 −βn))
≤
|1 −βn|n
|1 −βn + it|n exp
 
Re
(1 −βn + it
βn −it
−1 −βn
βn
)!
≤(1 + t2)−n/2 exp

−(1 + o(1))n1/2
,
where we can bound the power of n in the ﬁrst line by (1+t2)−n/2 since 1−βn <
1 and |x/(x + it)| is increasing in x ≥0. Integrating the factor (1 + t2)−n/2 as t
ranges from n−1/2 to inﬁnity gives a term of size o(1), so
M2
M
≤exp

−(1 + o(1))n1/2
= o

exp
h
−c(log n)2i
for any c > 0.
Bound on M3 To bound M3 we pull out the factor of M, obtaining
M3 ≤M
Z
L<|t|<n−1/2 exp
h
Re {I(1 −βn + it) −I(1 −βn)}
i
dt .
The real part of −(n + 1) log(1 −βn + it) is maximized at t = 0, whence
Re {I(1 −βn + it) −I(1 −βn)} ≤Re
(1 −βn + it
βn −it
−1 −βn
βn
)
,
and
M3 ≤M
Z
L<|t|<n−1/2 exp
 
Re
(1 −βn + it
βn −it
−1 −βn
βn
)!
dt
= M
Z
L<|t|<n−1/2 exp
 
−t2
β3n + βnt2
!
≤M
Z
L<|t|<n−1/2 exp
 
−t2
2β3n
!
dt
because the β3
n term is the greatest term in the denominator when t < n−1/2.
The behavior βn ∼n−1/2 and L = 2n−3/4 log n proves the desired upper bound
on M3 for any constant c < 2.
Bound on M4 Finally, for M4 we use the Taylor approximation

I(1 −βn + it) −I(1 −βn) + 1
2t2I′′(1 −βn)

 ≤t3
6 sup
|s|≤L
|I′′′(1 −βn + s)|.
Diﬀerentiating I′(z) = −(n+1)/z+1/(1−z)2 twice we ﬁnd that I′′′(z) ∼6/(1−
z)4 near z = 1, and hence that the right-hand side is bounded by (k+o(1))t3n2 =
3.5 The saddle point method
83
(k + o(1))n−1/4 log3 n for some k > 0. Because the integrand on the right-hand
side of (3.16) is everywhere positive, this implies the existence of c > 0 such
that M4 ≤cn−1/4 log3 n times the value of M, as desired.
◁
Remark. The approach of Example 3.18 yields a full asymptotic development
of an with minor modiﬁcations.
Our second example simply assumes the approximation (3.13), greatly re-
ducing the amount of work.
Example 3.19 (involutions: an entire function). Let f(z) = exp(z+z2/2) be the
exponential generating function for the number an of involutions in the permu-
tations group S n, as discussed in Example 2.49. This is an entire function, and
we apply a saddle point analysis. Let
I(z) = log(f(z)z−n−1) = z + z2
2 −(n + 1) log z .
Setting the derivative of I equal to zero gives the quadratic z2 + z −(n + 1) = 0
with roots −1
2 ±
q
n + 5
4. The series coeﬃcients an of f are positive, whereas
exp(I(z)) alternates in sign near the negative root, meaning an cannot be ap-
proximated by the integrand near the negative root.
We thus let γ be the positively oriented circle around the origin through z0 =
q
n + 5
4 −1
2. The real part of I on γ is maximized at z0, so the estimate (3.13)
implies
[zn] f(z) = 1
2πi
Z
γ
exp(I(zn)) dz ∼exp(I(z0))
s
1
2π I′′(z0) .
From the approximations
z0 = n1/2 −1
2 + 5
8n−1/2 + O(n−3/2)
z2
0
2 = 1
2n −1
2n1/2 + 3
4 + O(n−1/2)
log(z0) = 1
2 log n −1
2n−1/2 + 1
2n−1 + O(n−3/2)
it follows that
I(z0) = −1
2n log n + 1
2n + n1/2 −1
2 log n −1
4 + O(n−1/2)
84
Univariate asymptotics
and I′′(z0) = 2 + o(1). Thus,
an ∼n! exp(I(z0))
s
1
2π I′′(z0)
= n! exp
 
−1
2n log n + 1
2n + n1/2 −1
2 log n −1
4 + O(n−1/2)
!
2−1/2
∼nn/2e
√n−n/2
1
q
2 √e
,
where the ﬁnal line follows from Stirling’s approximation for n!.
◁
Notes
One of the earliest and most well-known uses of a modern generating func-
tion analysis to obtain asymptotics was Hardy and Ramanujan’s derivation of
asymptotics for the number of partitions of an integer [HR00a]. Their original
argument used a Tauberian theorem and the behavior of the generating func-
tion f(s) as s ↑1 through real values, though later work such as [HR00b] used
a circle method obtained by integrating over a circle near the boundary of the
domain of convergence. Saddle point methods are even more classical, dating
back centuries. As mentioned in the chapter, [Hay56] was an inﬂuential work
in developing the modern general theory.
The exposition in this chapter does not follow any one source, though it
owes a debt to Chapter 11 of [Hen91] and to the beautiful paper [FO90]. A
nice reference book for univariate asymptotics is the exemplary text [FS09].
Additional exercises
Exercise 3.6. The explicit leading term formulae in Lemmas 3.6 and Propo-
sition 3.7 are only useful when the numerator of the meromorphic generating
function is non-zero at the pole in question. Extend these two results to cap-
ture vanishing numerators and ﬁnd the leading asymptotic term for the series
coeﬃcients of f(z) = (1 −z)/(2 −z −e1−z) as n →∞.
Exercise 3.7. (set partition asymptotics) Use the exponential generating func-
tion f(z) = exp(ez −1) for the number an of set partitions of [n] from Exam-
ple 2.51 to derive the estimate
an = (log n + O(1))n .
3.5 The saddle point method
85
Exercise 3.8. (Exercise 2.18 continued) Using the fact that the series coef-
ﬁcients an of the generating function f in Exercise 2.18 are positive, prove
that its smallest positive singularity has the least modulus of any singularity of
f. Approximate this singularity and then estimate the logarithmic exponential
growth rate lim sup
n→∞
n−1 log an. Prove that this limsup is equal to the liminf, so
the limit exists.
Exercise 3.9. Sometimes, even when f is given explicitly, it can be tricky to
compute the minimal modulus of the singularities of f in order to obtain the
exponential coeﬃcient behavior using (3.5). The power series coeﬃcients of
the function
f(z) = arctan
√
2e−z −1
√
2e−z −1
were shown by H. Wilf to yield rational approximations to π. An asymptotic
analysis was provided by [War10]; do the ﬁrst step by ﬁnding the radius of
convergence of the power series for f at zero.
Exercise 3.10. Suppose P(x) is a polynomial of degree k with leading coeﬃ-
cient ak , 0. What does the saddle point method tell you about the asymptotics
of the Maclaurin coeﬃcients an of eP(x)? Speciﬁcally, can you identify an ex-
ponent β such that lim
n→∞n−β log |an| is ﬁnite?
Exercise 3.11. (Open Problem) Is the generating function φ from Example 3.17
analytic in a ∆-domain?
PART II
MATHEMATICAL BACKGROUND
