---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-067-higher-order-asymptotics
section_title: "Higher order asymptotics"
section_number: null
pages: 417-420
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
399
let W be the set of four preimages of r in V1 for the S (p) walk with 0 < p < 1
and ﬁxed states i and j. Then, as r →∞with ˆr in a compact subset of the
feasible velocity region R, the amplitude p(r) satisﬁes
p(r) = (−1)δ
1
2π|r|
X
z∈W
z−r
P(z)
∥∇log Q(z)∥2
2
1
p
| K (z)|
e−iπτ(z)/4 + O

|r|−3/2
,
(12.15)
where δ = 1 if ∇log Q is a negative multiple of ˆr (to account for the absolute
value in Corollary 9.46) and zero otherwise.
◁
12.5 Higher order asymptotics
Our results give eﬀective methods for computing asymptotic expansions of
multivariate generating functions. Although the ﬁrst term in such an expansion
generically dictates behavior of the sequence under consideration, there are
several reasons for wanting to compute higher order terms. Most obviously,
computing more terms in such expansions gives better approximations.
Example 12.15. Consider the (4, 3)-diagonal of the Delannoy numbers with
generating function F(x, y) = 1/(1 −x −y −xy). The critical points in this
direction are (−2, −3) and (1/2, 1/3), both of which are smooth, and the point
w = (1/2, 1/3) is strictly minimal. Corollary 5.17 implies
[x4ny3n]F(x, y) = 432n 
a1n−1/2 + a2n−3/2 + O(n−5/2)

as n →∞, where
a1 =
√
30
10 √π ≈0.3090193616
a2 = −
√
30
288 √π ≈−0.01072983895 .
Comparing this approximation with the actual Delannoy numbers for small
n gives (after scaling out the exponential growth) the results in Table 12.5. The
error in the 1-term approximation clearly decays as 1/n while the 2-term error
decays as 1/n2 – note the extreme accuracy even for n = 1. The question of the
optimal order to which to truncate an asymptotic series in a given application
goes beyond our scope here.
400
Combinatorial applications
n
1
2
4
8
16
Exact
0.2986
0.2148
0.1532
0.1088
0.07709
1-term
0.3090
0.2185
0.1545
0.1093
0.07726
Rel. error
-0.03486
-0.01742
-0.008698
-0.004345
-0.002171
2-term
0.2983
0.2147
0.1532
0.1088
0.07709
Rel. error
0.001077
0.0002450
0.00005820
0.00001417
0.000003496
Table 12.5 Approximations to scaled Delannoy numbers 432nF4n,3n.
Higher order terms in an asymptotic expansion for any direction ˆr with pos-
itive coordinates can be computed symbolically with the coordinates of ˆr as
parameters.
◁
Although the ﬁrst terms in our asymptotic expansions are typically non-
zero, and thus determine dominant asymptotic behavior, they can vanish. In
this case, higher order terms need to be computed in order to determine how
the sequence behaves.
Example 12.16. The rational functions
F1(x, y) =
1
1 −x −y,
F2(x, y) = y(1 −2y)
1 −x −y, and F3(x, y) =
x −y
1 −x −y
all admit (x, y) = (1/2, 1/2) as a minimal contributing point in the main di-
agonal direction. Applying the results of smooth ACSV gives an asymptotic
expansion (9.4) of the coeﬃcients of F1 whose leading term is non-zero. The
leading term in the asymptotic expansion of the coeﬃcients of F2 vanishes, as
the numerator of F2 vanishes at the contributing point, but the second order
term in this expansion is non-zero (in fact, the main diagonal of F2 is the gen-
erating function of the Catalan numbers – see Example 12.18 below). On the
other hand, it can be shown that the main diagonal of F3 is identically zero, so
all coeﬃcients in the asymptotic expansion must vanish. It is not obvious how
to detect automatically the vanishing of all terms in the asymptotic expansion
for a general rational function.
◁
Another reason why we may need higher order terms is because of cancel-
lation of terms when we combine asymptotic expansions of related functions.
Example 12.17. Consider the (d + 1)-variate function
W(x1, . . . , xd, y) =
A(x)
1 −yB(x),
12.5 Higher order asymptotics
401
where
A(x) =
1
1 −Pd
j=1
x j
1+x j
B(x) = 1 −(1 −e1(x))A(x)
for the elementary symmetric function e1(x) = Pd
i=1 xj. The combinatorial
constructions discussed in Chapter 2 imply that W enumerates words over the
alphabet {1, . . . , d}, where xj marks occurrences of the letter j and y marks oc-
currences of snaps, which are nonoverlapping pairs of duplicate letters. The
factor A(x) counts snapless words over X, which are the Smirnov words de-
scribed in Example 2.11. If ψ denotes the random variable counting snaps
among words with n occurrences of each letter then the expected value and
variance of ψ satisfy
E(ψ) = [xn1]Wy(x, 1)
[xn1]W(x, 1) = [xn1]A(x)−1B(x)(1 −e1(x))−2
[xn1](1 −e1(x))−1
and V(ψ) = E(ψ2) −E(ψ)2 with
E(ψ2) =
[xn1]

Wyy(x, 1) + Wy(x, 1)

[xn1]W(x, 1)
= [xn1]A(x)−2B(x)(B(x) + 1)(1 −e1(x))−3
[xn1](1 −e1(x))−1
.
Each of the above coeﬃcient extractions applies to a rational function whose
denominator is a power of Q(x) = 1 −e1(x). By Lemma 6.41, asymptotics
can be determined by applying the smooth ACSV results of Chapter 9 to the
strictly minimal critical point (1/d, . . . , 1/d) of each function, giving
E(ψ) =
3
√
3
8π −61
√
3
192π n−1 + O(n−2)
√
3
2π n−1 −
√
3
9π n−2 + O(n−3)
= (3/4)n −15/32 + O(n−1)
and
E(ψ2) =
9
√
3
32π n −35
√
3
128π + O(n−1)
√
3
2π n−1 −
√
3
9π n−2 + O(n−3)
= (9/16)n2 −(27/64)n + O(1)
so that V(ψ) = (9/32)n + O(1). Note that determining the leading term of
V(ψ) requires the second-order terms in the expansions of E(ψ) and E(ψ2).
402
Combinatorial applications
Comparing these approximations when d = 3 with the actual values for small
n, we obtain the following table.
n
1
2
4
8
E(ψ)
0
1.00000
2.50909
5.52056
(3/4)n
0.75
1.5
3
6
(3/4)n −15/32
0.28125
1.03125
2.53125
5.53125
One-term relative error
Undeﬁned
0.50000
0.19565
0.086846
Two-term relative error
Undeﬁned
0.031250
0.0088315
0.0019363
V(ψ)
0
0.8
1.20057
2.31961
(9/32)n
0.28125
0.5625
1.125
2.25
Relative error
Undeﬁned
0.29688
0.062942
0.030013
◁
