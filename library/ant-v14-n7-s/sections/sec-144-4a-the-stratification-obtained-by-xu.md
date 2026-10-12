---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-144-4a-the-stratification-obtained-by-xu
section_title: "4A. The stratification obtained by Xu"
section_number: null
pages: 259-261
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
Corollary 1.8] in our setting of dimension 2r. For each ﬁxed n,r ≥1, we deﬁne a set of parameters θ j
for 1 ≤j ≤n, as follows:
θ j =



0
if j = 0,
j⌊(r −1)/(n −1)⌋
if j = 1, . . . , n −2,
r −1
if j = n −1,
nr
if j = n.
(4-1)
Note that this differs superﬁcially from the deﬁnition of θ j in [Xu 2018, p. 2]: we are working with
dimension 2r in place of r and the ﬂoor function results in slightly different formulas. (Precisely, from
Xu’s work we may take
θ1 = ⌊(2r −1)/(2n −2)⌋= ⌊(r −1)/(n −1)⌋
(4-2)
and then we set θ j = jθ1 for 1 ≤j ≤n −1. In particular for j = n −1,
θn−1 = ⌊(2r −1)/2⌋= r −1.
In fact, Xu’s original theorem allows a slightly larger value of θ j ≥jθ1; it is later apparent in (7-13) that
this slightly larger choice, leading to a slightly stronger version of Theorem A, would not signiﬁcantly
improve our current application.)
Theorem A [Xu 2018, Theorem 1.1]. Let integers n,r, 1, D ≥1 be ﬁxed. There exist integers C =
C(n,r, D) ≥1 and C′ = C′(n,r, 1, D) ≥1 and a ﬁnite set S = S(n,r, 1, D) of primes such that the
following holds.
Let κ denote a ﬁnite ﬁeld with algebraic closure denoted by κ. For each 1 ≤i ≤2r, let χi : κ× →C×
be a multiplicative character (extended to κ by setting χi(0) = 0) and assume that di := ord(χi)|1 > 0.
Let Fi ∈κ(x1, . . . , xn) be a di-th power-free rational function of degree at most D and assume that
TFi := {m ∈κn : Fi(x) ≡Fi(x + m)}
(4-3)
is ﬁnite for each 1 ≤i ≤2r. Then upon deﬁning
S(x(1), . . . , x(2r)) :=
X
m∈κn
2r
Y
i=1
χi(Fi(m + x(i))),
(4-4)
1926
Lillian B. Pierce and Junyan Xu
we have that whenever char κ̸ ∈S, there exist subschemes
A2nr
κ
= X0 ⊃X1 ⊃X2 ⊃· · · ⊃Xn
such that for each 1 ≤j ≤n,
(1) the sum of the degrees of irreducible components of X j is at most C′;
(2) dim X j ≤2nr −θ j with θ j deﬁned as in (4-1);
(3) for all (x(1), . . . , x(2r)) ∈A2nr(κ) \ X j(κ),
|S(x(1), . . . , x(2r))| ≤C(#κ)(n+ j−1)/2.
Remark. The hypothesis that for each 1 ≤i ≤2r, χi has order di > 0 could allow that χi is the principal
character. However, if χi is principal then di = 1 and hence to be di-th power-free Fi ∈κ(x1, . . . , xn)
must be a constant function. This implies that TFi is inﬁnite, thus excluding this possibility from the
theorem. This remark applies to Corollary B, below, and the resulting Theorem 4.1 and Corollary 4.2.
Remark. Note that while the subschemes X j may depend on the Fi, the parameters C, C′, θ j depend
only on the maximum degree D of the Fi. The constant C = C(n,r, D) noted above is bounded above
by (4r(D +1)+1)n as computed in [Katz 2001, Theorem 11] (see the remarks following Theorem 1.1 in
[Xu 2018], again recalling that we have 2r in place of r). The constant C′ (and later C′′ in Corollary 4.3)
only depends on n,r, D, 1 but is not explicitly determined. For further details on the dependence of C′
and C′′ see [Xu 2018, Section 2.1, and the remark following Theorem 1.1] and Corollary 4.3.
Next, we must convert Theorem A into a count for the number of points (x(1), . . . , x(2r)) ∈A2nr(κ)
(later denoted as collections {x(1), . . . , x(2r)}) such that a given upper bound for |S(x(1), . . . , x(2r))| holds.
It is convenient to deﬁne for each 0 ≤j ≤n and any sequence 1 ≤k1 ≤k2 ≤· · · ≤kn < ∞the function
Bn,r( j; k) = Bn,r( j; k1, . . . , kn) =



1
if j = 0,
k
θ j
1 = k j⌊(r−1)/(n−1)⌋
1
if j = 1, . . . , n −2,
kθn−1
1
= kr−1
1
if j = n −1,
(k1 · · · kn/2)2r
if j = n, n even,
(k1 · · · k(n−1)/2)2rkr
(n+1)/2
if j = n, n odd.
(4-5)
(To aid comparison to Xu’s original notation [2018] involving parameters denoted by n0, η, we make the
simple observation that for j = n and θ j = nr, if n is even we write nr = (n/2)2r (with n0 = n/2 and
η = 0) and when n is odd we write nr = ((n −1)/2) · 2r + r (with n0 = (n −1)/2 and η = r), so that
Xu’s original notation results in the expression stated above for Bn,r( j, k) in the case j = n, and with
ambient dimension 2r.)
Corollary B [Xu 2018, Corollary 1.8]. Let integers n,r, 1, D ≥1 be ﬁxed. There exist integers
C = C(n,r, D) ≥1 and C′ = C′(n,r, 1, D) ≥1 and a ﬁnite set S = S(n,r, 1, D) of primes such
that the following holds.
Burgess bounds for short character sums evaluated at forms
1927
Let κ denote a ﬁnite ﬁeld with algebraic closure denoted by κ. For each 1 ≤i ≤2r, let χi : κ× →C×
be a multiplicative character (extended to κ by setting χi(0) = 0) and assume that di := ord(χi)|1 > 0.
Let Fi ∈κ(x1, . . . , xn) be a di-th power-free rational function of degree at most D and assume that TFi as
deﬁned in (4-3) is ﬁnite for each 1 ≤i ≤2r.
Let {Mi}n
i=1 be subsets of κ such that 1≤|M1|≤|M2|≤· · ·≤|Mn|<∞, and deﬁne M :=Qn
i=1 Mi ⊂κn
and ∥M∥:= Qn
i=1 |Mi|. Then whenever char κ /∈S, for each 1 ≤j ≤n,
#

(x(1), . . . , x(2r)) ∈M2r : |S(x(1), . . . , x(2r))| > C(#κ)(n+ j−1)/2	
≤C′∥M∥2r Bn,r( j; |M1|, . . . , |Mn|)−1.
(4-6)
