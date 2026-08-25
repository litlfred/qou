---
doc_id: 04procbryden
doc_title: "Some computations of Ohtsuki series"
section_id: sec-011-43-slopes
section_title: "Slopes"
section_number: 4.3
pages: 13-16
source_pdf: 04procbryden.pdf
source_sha256: 8baffbc6542c34a5
doc_brief: "Some computations of Ohtsuki series — We present some computational data on Ohtsuki series for a two pa- rameter family of integer homology spheres obtained by surgery around what we call ‘2–strand"
---
For ﬁxedS and T, the dependence onm of λ±
m(S, T) is more interesting.
See Figure 5 for graphs of the ratios λ+
n
(S,T)
λ+
n−1(S,T) for S = −2 and several
odd values of T. From this ﬁgure there is an obvious conjecture.
Conjecture If M is a rational homology sphere, then the ratio
λn(M)
λn−1(M) is asymptotically linear in n, for large n.
When this conjecture holds, set
σ(M) = limn−→ ∞
λn(M)
nλn−1(M) ;
this will be called the slope of M (not to be confused with slopes in
hyperbolic geometry).
It is known from (LR) that the slope exists for Seifert ﬁbred mani-
folds and is
σ
(
Σ
( Q1
P1
,..., QN
PN
))
= ±
∏ Pi
π2 = ±
(
π2
N∑
i=1
Qi
Pi
) −1
.
As a corollary π2σ(M) ∈ Q for such manifolds, while if in addition the
manifold is an integer homology sphere then π2σ(M) ∈ Z. Since the
WRT invariant (and therefore also the Ohtsuki series) is multiplicative
under connect sum,
|σ(M#N)| = max(|σ(M)|, |σ(N)|)
when |σ(M)| ⁄=|σ(N)|, while under mirror image, the sign of the slope
is reversed (σ(M)=−σ (M)).
65
N. Jacoby & R. Lawrence
Figure 5. λ+
n (S, T)/λ+
n−1(S, T) for S = −2 against n
Assuming that slopes exist for our family of manifolds, from the
polynomiality of the termsλ±
m(S, T), one can make a further conjecture.
Conjecture The slope for the manifolds M ±
(( S
T )) is polynomial in
S and T of degree at most 2.
Observe that this conjecture does not follow from the previous
conjecture and the theorem giving λ±
m(S, T) as a polynomial of degree
2m in S and T, since we have no control on the growth rate of the
coeﬃcients in such polynomials withm (it is conceivable that the lower
order coeﬃcients may grow more rapidly that the leading one). This
conjecture is backed by numerical data. See for example Figure 6 which
gives the slopes forS = −3 plotted againstT (even); and Figure 7 which
g i v e ss l o p e sf o rS and T even, plotted against T for various values of
S.
Again assuming this conjecture, we can theoretically determine what
its form should be. For the case ofS odd and T even, we know that the
knot for S = ±1 is the (2,T ∓1) torus knot, surgery around which gives
for M
δ
(( S
T )) the Seifert ﬁbred manifold on three ﬁbers Σ(2,T − S, 2T −
2S − δ), and hence its slope is 2
π2 (T − S)((2T − 2S)δ − 1). Hence for
general (odd) S and even T, the quadratic giving the slope must still
have coeﬃcient 4
π2 for T2.
66
Some computations of Ohtsuki series
Figure 6. Graph of slopes for S = −3a n dT even
Figure 7. Graph of slopes for S and T even, against T
67
N. Jacoby & R. Lawrence
For the case of S and T both even, we have no similar data from
special cases, since although we know that for S = 0, the manifold
obtained is S3 and Z∞ = 1, there is no well-deﬁned slope!
Finally we remark that the numerical data and precision is suﬃcient
to demonstrate (assuming the conjectures) the existence of integer
homology spheres for which π2σ(M) ⁄∈Z, for example M+
((3
2 )).
