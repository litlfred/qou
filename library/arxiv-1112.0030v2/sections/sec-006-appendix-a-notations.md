---
doc_id: arxiv-1112.0030v2
doc_title: "Homological algebra of knots and BPS states Sergei Gukov and Marko Stoˇsi´c"
section_id: sec-006-appendix-a-notations
section_title: "Appendix A. Notations"
section_number: null
pages: 36-37
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
toc_source: outline
doc_brief: "Homological algebra of knots and BPS states Sergei Gukov and Marko Stoˇsi´c — It is known that knot homologies admit a physical description as spaces of open BPS states."
---
K denotes a knot.
denotes the unknot.
For every positive integer r we have:
• P
Sr
N (K)(q) or P
r
z }| {
· · ·
N
(K)(q) denotes the unreduced one-variable polynomial
quantum invariant of K, labelled with the r-th symmetric representation of sl(N).
• P Sr
N (K)(q) or P
r
z }| {
· · ·
N
(K)(q) denotes the reduced (a.k.a. normalized) one-
variable polynomial quantum invariant of K, labeled by the r-th symmetric rep-
resentation of sl(N). It is obtained from the unnormalized polynomial P
Sr
N (K)(q)
by
P Sr
N (K) = P
Sr
N (K)
P
Sr
N (
)
,
so that P Sr
N (
) = 1.
• P Sr(K)(a, q) or P
r
z }| {
· · ·
(K)(a, q) denotes the reduced two-variable colored
HOMFLY polynomial of K. The normalization is P Sr(
) = 1. In particular
P Sr(K)(a = qN, q) = P Sr
N (K)(q)
• HSr(K) or H
r
z }| {
· · ·
(K) denotes a reduced triply-graded homology theory
HSr
i,j,k(K) that categoriﬁes the two-variable colored HOMFLY polynomial P Sr(K):
χ(HSr(K)) = P Sr(K).
The homological grading of HSr
i,j,k(K) is its third grading, and its (doubly-
graded) Euler characteristic is given by:
χ(HSr(K)) =
X
i,j,k
(−1)kqitj(dim HSr
i,j,k(K)).
• PSr(K) or P
r
z }| {
· · ·
(K) denotes the Poincar´e polynomial of HSr(K), i.e.
PSr(K)(a, q, t) =
X
i,j,k
aiqjtk(dim HSr
i,j,k(K)).
Specialization to t = −1 gives P Sr(K):
PSr(K)(a, q, t = −1) = P Sr(K)(a, q) .
We also call PSr(K) the Sr-colored superpolynomial.
• Hsl(N),Sr(K) denotes the reduced doubly-graded homology theory categori-
fying P Sr
N (K).
• PSr
N (K) denotes the Poincar´e polynomial of Hsl(N),Sr(K). In particular
PSr
N (K)(q, t) =
X
j,k
qjtk(dim Hsl(N),Sr
j,k
(K)) .
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES
37
PSr
N (K)(q, t = −1) = P Sr
N (K)(q) .
• The corresponding polynomials and homologies for the anti-symmetric rep-
resentations are denoted in the same way with Sr replaced by Λr.
• Unreduced versions of the homology and polynomials are denoted by putting
a bar.
All (tri-)degrees are (a, q, t)-degrees.
Remark A.1. Conventions for the superpolynomial in the vector rep-
resentation:
The case r = 1 corresponds to the (ordinary) HOMFLY polynomial
and the Khovanov-Rozansky homology. The corresponding superpolynomial, to-
gether with the structure of the triply-graded homology was studied in [3].
Here we shall use slightly diﬀerent conventions: in the superpolynomial, we
replace a and q from [3] with a1/2 and q1/2, respectively. For example, the super-
polynomial of the trefoil knot becomes:
(A.1)
P (31) = aq−1 + aqt2 + a2t3.
Also, by S(K), or just S, we mean half of the value of S(K) from [3].
This way, the degrees of canceling diﬀerentials d1 and d−1 from [3] become
(−1, 1, −1) and (−1, −1, −3), respectively. Also, from now on we denote these two
diﬀerentials by d1 and d−1, respectively.
