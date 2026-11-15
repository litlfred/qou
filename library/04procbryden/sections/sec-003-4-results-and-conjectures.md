---
doc_id: 04procbryden
doc_title: "Some computations of Ohtsuki series"
section_id: sec-003-4-results-and-conjectures
section_title: "Results and conjectures"
section_number: 4
pages: 11-16
source_pdf: 04procbryden.pdf
source_sha256: 8baffbc6542c34a5
toc_source: inferred
doc_brief: "Some computations of Ohtsuki series — We present some computational data on Ohtsuki series for a two pa- rameter family of integer homology spheres obtained by surgery around what we call ‘2–strand"
---
Results and conjectures
4.1. Individual Ohtsuki series
For small K (up to 100), it turns out that the number of states is
≈K2.9 (rather than K3) while the running time is ≈K4.2 (rather
than K4) due to the increase in computational time of each summand
and initialization procedures, for the larger values of K. For M+
(( 3
2 ))
discussed above ((S, T, U) = (−2, −3, 6)), K < 137 was suﬃcient to
63
N. Jacoby & R. Lawrence
compute the ﬁrst 21 coeﬃcients of Z∞,
Z∞(M+
(( 3
2 )))
= 1 + 12h + 258h2 + 7756h3 + 300055h4 + 14192892h5
+793556722h6 + 51201783488h7 + 3744412949224h8
+306062634843942h9 + 27651533457983745h10
+2736207255879667844h11 + 294306807889008940143h12
+34188707473104409330168h13
+4265845139103716469762268h14
+568978507509845435699024672h15
+80787229265313530505892175542h16
+12165972894589961487357113418955h17
+1936811327962748352514940775515283h18
+325007156713501796302801741846095206h19
+57334985329655520887251821186176103843h20
+10607981215487793536113323249915379712259h21
+2053956644731187123340443541756436810603354h22 + · · ·
where h = q −1.
4.2. Polynomiality of coefficients
We already know that for ﬁxed m, the dependence on S and T (of
ﬁxed parity) of λ±
m(S, T) is polynomial of degree 2m. Since for S = 0
(or T = 0), K(( S
T )) is the unknot for which Z∞= 1, thus λ±
m(S, T) is
divisible by S (for S even) and by T (for T even) and by ST (for S, T
both even).
Since the WRT invariants of the mirror image manifold
¯
M of M
are given by ZK( ¯
M)(q) = ZK(M)(q−1) at all roots of unity, thus
Z∞( ¯
M) can be obtained from Z∞(M) by replacing q by q−1, that is by
substituting
1
1+h −1 = −
h
1+h for h. This gives (complicated) relations
between λ±
m(S, T) and λ∓
m(T, S), while λ±
m(−T, −S) = λ±
m(S, T). Hence
it is only necessary to compute the polynomials λ+
m(S, T) for the two
parity combinations, (even, even), (even, odd). Knowing the degrees of
the polynomials, numerical results for a large enough number of pairs
(S, T) are suﬃcient to determine these polynomials. The results for the
ﬁrst few coeﬃcients are, for S and T both even,
λ+
0
= 1
λ+
1
= −3
2ST
λ+
2
=
3
4ST(5ST + T −S + 3)
64
Some computations of Ohtsuki series
and for S even, T odd,
λ+
0
= 1
λ+
1
=
3
4S(S + 2T)
λ+
2
=
25
32S4+ 25
8 S3T + 15
4 S2T 2−1
2S3−3
2S2T −3
4ST 2−1
2S2+ 1
4ST −1
4S
Observe, for example, that λ1 is divisible by 6, and indeed the Casson
invariant is
λ(M+
(( S
T ))) = 1
6λ+
1 (S, T) =

−1
4ST
for S and T both even
1
8S(S + 2T)
for S even and T odd
4.3. Slopes
For ﬁxed S and T, the dependence on m of λ±
m(S, T) is more interesting.
See Figure 5 for graphs of the ratios
λ+
n (S,T)
λ+
n−1(S,T) for S = −2 and several
odd values of T. From this ﬁgure there is an obvious conjecture.
Conjecture
If M is a rational homology sphere, then the ratio
λn(M)
λn−1(M) is asymptotically linear in n, for large n.
When this conjecture holds, set
σ(M) =
lim
n−→∞
λn(M)
nλn−1(M) ;
this will be called the slope of M (not to be confused with slopes in
hyperbolic geometry).
It is known from (LR) that the slope exists for Seifert ﬁbred mani-
folds and is
σ

Σ
Q1
P1
, . . . , QN
PN

= ±
 Pi
π2
= ±

π2
N

i=1
Qi
Pi
−1
.
As a corollary π2σ(M) ∈Q for such manifolds, while if in addition the
manifold is an integer homology sphere then π2σ(M) ∈Z. Since the
WRT invariant (and therefore also the Ohtsuki series) is multiplicative
under connect sum,
|σ(M#N)| = max(|σ(M)|, |σ(N)|)
when |σ(M)|̸ = |σ(N)|, while under mirror image, the sign of the slope
is reversed (σ(M) = −σ(M)).
65
N. Jacoby & R. Lawrence
Figure 5. λ+
n (S, T)/λ+
n−1(S, T) for S = −2 against n
Assuming that slopes exist for our family of manifolds, from the
polynomiality of the terms λ±
m(S, T), one can make a further conjecture.
Conjecture
The slope for the manifolds M±
(( S
T )) is polynomial in
S and T of degree at most 2.
Observe that this conjecture does not follow from the previous
conjecture and the theorem giving λ±
m(S, T) as a polynomial of degree
2m in S and T, since we have no control on the growth rate of the
coeﬃcients in such polynomials with m (it is conceivable that the lower
order coeﬃcients may grow more rapidly that the leading one). This
conjecture is backed by numerical data. See for example Figure 6 which
gives the slopes for S = −3 plotted against T (even); and Figure 7 which
gives slopes for S and T even, plotted against T for various values of
S.
Again assuming this conjecture, we can theoretically determine what
its form should be. For the case of S odd and T even, we know that the
knot for S = ±1 is the (2, T ∓1) torus knot, surgery around which gives
for Mδ
(( S
T )) the Seifert ﬁbred manifold on three ﬁbers Σ(2, T −S, 2T −
2S −δ), and hence its slope is
2
π2 (T −S)((2T −2S)δ −1). Hence for
general (odd) S and even T, the quadratic giving the slope must still
have coeﬃcient
4
π2 for T 2.
66
Some computations of Ohtsuki series
Figure 6. Graph of slopes for S = −3 and T even
Figure 7. Graph of slopes for S and T even, against T
67
N. Jacoby & R. Lawrence
For the case of S and T both even, we have no similar data from
special cases, since although we know that for S = 0, the manifold
obtained is S3 and Z∞= 1, there is no well-deﬁned slope!
Finally we remark that the numerical data and precision is suﬃcient
to demonstrate (assuming the conjectures) the existence of integer
homology spheres for which π2σ(M)̸ ∈Z, for example M+
(( 3
2 )).
