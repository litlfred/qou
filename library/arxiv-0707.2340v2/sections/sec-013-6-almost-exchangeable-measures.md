---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-013-6-almost-exchangeable-measures
section_title: "Almost Exchangeable Measures"
section_number: 6
pages: 33-41
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
---
By Pemantle’s result (Theorem 3.7 in §3.5), for symmetric measures in Pn all
ﬁve conditions NLC, h-NLC, Rayleigh/h-NLC+, CNA, CNA+ are equiva lent to the
ULC condition for the rank sequence. Therefore, the relations be tween all these
negative dependence properties are completely understood in the exchangeable case.
In this section we study the almost exchangeable case, that is, mea sures whose gen-
erating polynomials are symmetric in all but possibly one variable (Deﬁn ition 2.1).
34 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
We prove that for such measures one has both h-NLC ⇔ CNA and Rayleigh/h-
NLC+ ⇔ CNA+, which conﬁrms Pemantle’s Conjecture 2.6 in this case. In the
next section we will use this result to show that the counterexample s in 20 or more
variables that we construct there satisfy all negative dependenc e properties other
than strongly Rayleigh.
Let C be an m × n matrix (where m, n are allowed to be inﬁnite), and let i and
j be ﬁnite equi-numerous subsets of [ m] and [ n], respectively. Denote by C(i, j) the
minor of C with rows indexed by i and columns indexed by j. The Cauchy-Binet
theorem, see, e.g., [49], asserts that
(AB)(i, j) =
∑
k, |k|=|i|=|j|
A(i, k)B(k, j)
for any m × n matrix A and n × q matrix B, where 1 ≤ m, n, q ≤ ∞, provided that
the sum in the right-hand side converges absolutely.
Recall the notion of (non-negative) LC sequence from Deﬁnition 2.8 . For conve-
nience, we ﬁrst prove a technical result that will be frequently use d later on.
Lemma 6.1. Let {aj}n
j=0 and {bj}n
j=0 be two LC sequences that satisfy
(i) {aj + bj}n
j=0 is LC, and
(ii) ajbj+1 ≥ aj+1bj for all 0 ≤ j ≤ n − 1.
If ℓ < k and bℓak > 0, then brar > 0 for all ℓ ≤ r ≤ k.
Proof. Suppose that ar = 0 for some ℓ ≤ r < k and let s the largest such index.
Assumption (ii) for j = s gives bs = 0, hence as + bs = 0. This contradicts the “no
internal zeros” part of assumption (i) (cf. Deﬁnition 2.8). Theref ore ar > 0, and a
similar argument shows that br > 0 as well. □
The following proposition shows that for almost exchangeable measu res the
Rayleigh property is the same as the negative lattice condition (NLC) closed under
conditioning and external ﬁelds on the last variable. Indeed, condit ion (ii) follows
directly from NLC while (i) follows from NLC after having imposed an ext ernal
ﬁeld on the last coordinate and then projected onto the ﬁrst n coordinates.
Proposition 6.2. Let µ ∈ Pn+1 be such that its generating polynomial g = gµ is
symmetric in its ﬁrst n variables, so that
g(z1, . . . , zn+1) = zn+1
n∑
k=0
akek(z1, . . . , zn) +
n∑
k=0
bkek(z1, . . . , zn).
Then µ is Rayleigh if and only if
(i) {θak + (1 − θ)bk}n
k=0 is LC for all 0 ≤ θ ≤ 1, and
(ii) akbk+1 ≥ ak+1bk for all 0 ≤ k ≤ n − 1.
Proof. Suppose ﬁrst that µ is Rayleigh. By Proposition 2.1 we get that if 0 ≤ θ < 1
then g(z1, . . . , zn, θ/(1 − θ)) is a Rayleigh polynomial that is symmetric in all its
n variables. Condition (i) now follows from the exchangeable case (The orem 3.7).
Let S ⊆ [n − 1] be of cardinality i. The NLC condition gives
aibi+1 = µ(S ∪ {n + 1})µ(S ∪ {n}) ≥ µ(S ∪ {n, n + 1})µ(S) = ai+1bi,
which veriﬁes (ii).
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 35
Assume now that {ak}n
k=0 and {bk}n
k=0 satisfy (i) and (ii). The inequality
∂g
∂zi
(x) ∂g
∂zj
(x) ≥ ∂2g
∂zi∂zj
(x)g(x), x ∈ Rn+1
+ , i, j ∈ [n],
follows from the exchangeable case and (i). What is left to prove is th e inequality
∂g
∂zi
(x) ∂g
∂zn+1
(x) ≥ ∂2g
∂zi∂zn+1
(x)g(x), x ∈ Rn+1
+ , i ∈ [n],
and by symmetry (in the ﬁrst n variables) we only need to check it for e.g. i = n.
We may write g as
g(z1, . . . , zn+1) =
n∑
k=0
bkek(z1, . . . , zn−1) + zn
n∑
k=0
bk+1ek(z1, . . . , zn−1)
+ zn+1
n∑
k=0
akek(z1, . . . , zn−1) + znzn+1
n∑
k=0
ak+1ek(z1, . . . , zn−1),
so the desired inequality is equivalent to

∑
j
ajej



∑
j
bj+1ej

 −

∑
j
aj+1ej



∑
j
bjej

 ≥ 0 (20)
for all x ∈ Rn−1
+ , where ej = ej(x1, . . . , xn−1). Let now
C =
( a0 a1 a2 . . . a n
b0 b1 b2 . . . b n
)
and recall the deﬁnition of a TP p matrix from §3.5. We claim that C is TP 2. Let
1 ≤ i < j ≤ n. We need to prove that aibj ≥ biaj. Clearly, we may assume that
biaj ⁄= 0 and that j − i ≥ 2. By Lemma 6.1 we have brar > 0 for i ≤ r ≤ j and
thus ai
bi
≥ ai+1
bi+1
≥ · · · ≥ aj
bj
by (ii), which shows that C is indeed TP 2. Let E = ( ei−j)n
i,j=0. By Theorem 3.8
we have that E is TP 2 and by the Cauchy-Binet formula so is CE . Now
CE =
( ∑ ajej
∑ aj+1ej . . .∑ bjej
∑ bj+1ej . . .
)
,
from which (20) follows. □
The next result is the analog of Proposition 6.2 for the h-NLC proper ty.
Proposition 6.3. Let µ ∈ Pn+1 be such that its generating polynomial g = gµ is
symmetric in its ﬁrst n variables, so that
g(z1, . . . , zn+1) = zn+1
n∑
k=0
akek(z1, . . . , zn) +
n∑
k=0
bkek(z1, . . . , zn).
Then µ is h-NLC if and only if
(i) {ak}n
k=0, {bk}n
k=0, and {ak + bk}n
k=0 are LC, and
(ii) akbk+1 ≥ ak+1bk for all 0 ≤ k ≤ n − 1.
36 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
Proof. Let S, T ⊂ [n]. The NLC condition applied to each of the three pairs ( S, T ),
(S, T ∪ {n + 1}), and ( S ∪ {n + 1}, T ∪ {n + 1}) gives respectively
b|S|b|T | ≥ b|S∪T |b|S∩T |, b |S|a|T | ≥ a|S∪T |b|S∩T |, a |S|a|T | ≥ a|S∪T |a|S∩T |.
Therefore, setting ℓ = |S|, k = |T |, m = |S ∩ T |, we see that NLC is equivalent to
bℓbk ≥ bk+ℓ−mbm, b ℓak ≥ ak+ℓ−mbm, a ℓak ≥ ak+ℓ−mam (21)
for m ≤ k, ℓ ≤ n and k + ℓ ≤ n + m.
If S ⊆ [n] has cardinality n − j, the measure obtained by projecting µ onto
2S∪{n+1} is of the same form as µ with coeﬃcients
ak(j) =
j∑
i=0
(j
i
)
ak+i and bk(j) =
j∑
i=0
(j
i
)
bk+i, 0 ≤ k ≤ n − j,
while the one obtained by projecting µ onto 2 S is exchangeable with coeﬃcients
ak(j) + bk(j), 0 ≤ k ≤ n − j. Therefore, h-NLC is equivalent to the statement that
for each 0 ≤ j ≤ n one has
bℓ(j)bk(j) ≥ bk+ℓ−m(j)bm(j),
bℓ(j)ak(j) ≥ ak+ℓ−m(j)bm(j), a ℓ(j)ak(j) ≥ ak+ℓ−m(j)am(j),
(aℓ(j) + bℓ(j))(ak(j) + bk(j)) ≥ (ak+ℓ−m(j) + bk+ℓ−m(j))(am(j) + bm(j))
(22)
for m ≤ k, ℓ ≤ n − j and k + ℓ ≤ n − j + m.
It follows from this that the h-NLC property implies that the sequen ces in (i)
have no internal zeros. For example, if k ≤ ℓ, bk−1 > 0, bk = · · · = bℓ = 0, bℓ+1 > 0
contradicts bkbℓ ≥ bk−1bℓ+1. Given this, the fact that the three sequences are LC
and satisfy (ii) is a consequence of the ﬁrst and last inequalities in (21 ) with ℓ = k,
m = k − 1, the middle inequality in (21) with ℓ = k + 1, m = k, and the last
inequality in (22) with j = 0, ℓ = k, m = k − 1.
For the converse, assume that (i) and (ii) hold. Note that for each j, {ak(j)}n−j
k=0
is a convolution of two LC sequences, and hence is LC by [49, Theore m 1.2 on
p. 394], and the same holds for the sequences bk(j) and ak(j) + bk(j). This gives
three of the four inequalities in (22). For the other one, note that since evaluating
the elementary symmetric polynomials at the “all ones vector” prod uces binomial
coeﬃcients, it follows from (20) that
ak(j)bk+1(j) ≥ ak+1(j)bk(j). (23)
We need to check that
ak(j)bℓ(j) ≥ ak+ℓ−m(j)bm(j)
for m ≤ k, ℓ, and in doing so, can assume that the right-hand side is not zero. By
Lemma 6.1, it follows that ai(j)bi(j) > 0 for m ≤ i ≤ k + ℓ − m. To conclude the
proof, write
ak(j)
ak+ℓ−m(j) ≥ am(j)
aℓ(j) ≥ bm(j)
bℓ(j) .
The ﬁrst inequality comes from the already proved part of (22), wh ile the second
is obtained by repeated application of (23). □
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 37
Theorem 6.4. Let µ ∈ Pn+1 be such that its generating polynomial g = gµ is
symmetric in its ﬁrst n variables, so that
g(z1, . . . , zn) = zn+1
n∑
k=0
akek(z1, . . . , zn) +
n∑
k=0
bkek(z1, . . . , zn).
Suppose that {ak}n
k=0 and {bk}n
k=0 are LC sequences that satisfy
(i) {ak + bk}n
k=0 is LC, and
(ii) akbk+1 ≥ ak+1bk for all 0 ≤ k ≤ n − 1.
Then µ is CNA.
Proof. As in §2.1, we denote by Xi, i ∈ [n+1], the i-th coordinate function/random
(binary) variable on 2 [n+1]. First, observe that it is enough to prove that µ is NA.
To see this, note that if µ is conditioned on Xi = 1 for k values of i ≤ n, on Xi = 0
for l values of i ≤ n, and possibly on the value of Xn+1, the resulting measure is
of the same form with a new value n′ of n and new ai’s and bi’s that again satisfy
the assumptions of the theorem. Using primes to denote the new va lues, we have
n′ = n − k − l and if the value of Xn+1 is not conditioned on, then, except for
a constant factor, a′
i = ai+k and b′
i = bi+k. If the value of Xn+1 is conditioned
on, then a′
i = b′
i = ai+k if the conditioning is on Xn+1 = 1 and a′
i = b′
i = bi+k if
the conditioning is on Xn+1 = 0. Now take two increasing functions F and G on
2[n+1] that depend on disjoint sets of coordinates (cf. Deﬁnition 2.2). Wit hout loss
of generality, we may assume that there is an m satisfying 1 ≤ m ≤ n such that
F depends on the coordinates {X1 . . . , Xm}, and G depends on the coordinates
{Xm+1, . . . , Xn+1}. We need to prove
∫
F Gdµ ≤
∫
F dµ
∫
Gdµ. (24)
Since µ is symmetric in the ﬁrst n coordinates, these three integrals are not changed
if F and G are replaced by the functions obtained by symmetrizing them with
respect to the coordinates {X1, . . . , Xm} and {Xm+1, ..., Xn}, respectively. These
symmetrized functions are also increasing. Therefore, we may ass ume that F and
G are of the following form:
F (X1, . . . , Xm) = fk if
m∑
i=1
Xi = k,
G(Xm+1, . . . , Xn, Xn+1 = 0) = gk if
n∑
i=m+1
Xi = k, and
G(Xm+1, . . . , Xn, Xn+1 = 1) = hk if
n∑
i=m+1
Xi = k,
where fk, gk and hk are increasing, and gk ≤ hk for each k. Using the fact that the
covariance of F and G with respect to the measure µ can be written as
1
2
∑
S,T ∈2[n+1]
[F (S) − F (T )][G(S) − G(T )]µ(S)µ(T ),
38 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
(24) becomes
∑
i,j,k,ℓ
(m
i
)(m
j
)(n − m
k
)(n − m
ℓ
)
(fj − fi)
[
(hk − hℓ)ak+iaℓ+j
+ (gk − gℓ)bk+ibℓ+j + (hk − gℓ)ak+ibℓ+j + (gk − hℓ)aℓ+jbk+i
]
≥ 0.
Note that we are using the usual convention that
(n
m
)
= 0 unless 0 ≤ m ≤ n. Since
the summand above is not changed if the roles of i and j are interchanged and the
roles of k and ℓ are interchanged, this can be written as
∑
i<j
∑
k,ℓ
(m
i
)(m
j
)(n − m
k
)(n − m
ℓ
)
(fj − fi)
[
(hk − hℓ)ak+iaℓ+j
+ (gk − gℓ)bk+ibℓ+j + (hk − gℓ)ak+ibℓ+j + (gk − hℓ)aℓ+jbk+i
]
≥ 0. (25)
So, it is enough to show that for ﬁxed i < j , and ﬁxed p,
∑
k+ℓ=p
(n − m
k
)(n − m
ℓ
)[
(hk − hℓ)ak+iaℓ+j
+ (gk − gℓ)bk+ibℓ+j + (hk − gℓ)ak+ibℓ+j + (gk − hℓ)aℓ+jbk+i
]
≥ 0.
Furthermore, it is enough to prove this in case when the gk’s and hk’s take only the
values 0 and 1, since any increasing function on a partially ordered se t (in this case,
{0, . . . , n} × { 0, 1}) can be written as a positive linear combination of increasing
functions that take only the values 0 and 1.
We will in fact prove that for such gk’s and hk’s,
Sq =
∑
k+ℓ=p, |k−ℓ|≤2q
(n − m
k
)(n − m
ℓ
)[
(hk − hℓ)ak+iaℓ+j
+ (gk − gℓ)bk+ibℓ+j + (hk − gℓ)ak+ibℓ+j + (gk − hℓ)aℓ+jbk+i
]
≥ 0
by induction on q. For the basis step, note that S0 = 0 if p is odd, while if p = 2 r
is even, then
S0 =
(n − m
r
)2
(hr − gr)(ar+ibr+j − ar+jbr+i),
which is non-negative by (ii), since i < j .
We will prove now that Sq ≥ 0, assuming that Sq−1 ≥ 0. The diﬀerence Sq −Sq−1
consists of two summands, which when combined, become
(n − m
k
)(n − m
ℓ
)[
(hk −hℓ)(ak+iaℓ+j −aℓ+iak+j )+(gk −gℓ)(bk+ibℓ+j −bℓ+ibk+j)
+ (hk − gℓ)(ak+ibℓ+j − ak+j bℓ+i) + (gk − hℓ)(aℓ+j bk+i − aℓ+ibk+j )
]
, (26)
where k + ℓ = p while k − ℓ = 2q if p is even and k − ℓ = 2q − 1 if p is odd. Now we
consider the possible values of gℓ, hk for this pair k, ℓ. Recall that gℓ ≤ hℓ, gk ≤ hk.
If gℓ = hk, then gt = ht = this common value for all ℓ ≤ t ≤ k, so that (26) is zero.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 39
So, we may assume that gℓ = 0, hk = 1. Now there are four possible values for the
pair ( hℓ, gk) (note that the use of the fractions that appear below is justiﬁed by
Lemma 6.1):
(a) hℓ = gk = 1. In this case, (26) becomes
(n − m
k
)(n − m
ℓ
)[
(bk+ibℓ+j − bℓ+ibk+j ) + (ak+ibℓ+j − ak+jbℓ+i)
]
.
This is non-negative by the log-concavity of the b’s and (ii):
ak+i
ak+j
≥ bk+i
bk+j
≥ bℓ+i
bℓ+j
.
(b) hℓ = 0, gk = 1. Now (26) is
(n − m
k
)(n − m
ℓ
)[
(ak+i + bk+i)(aℓ+j + bℓ+j) − (aℓ+i + bℓ+i)(ak+j + bk+j )
]
,
which is non-negative by (i).
(c) hℓ = gk = 0. This time (26) is
(n − m
k
)(n − m
ℓ
)[
(ak+iaℓ+j − aℓ+iak+j) + (ak+ibℓ+j − ak+j bℓ+i)
]
,
which is non-negative by the log-concavity of the a’s and (ii).
In these three cases, (26) is non-negative, and therefore Sq ≥ 0 by the induction
hypothesis. The fourth case is diﬀerent, since (26) need not be no n-negative:
(d) hℓ = 1, gk = 0. In this case, gt ≡ 0 and ht ≡ 1 for ℓ ≤ t ≤ k, so
Sq =
∑
r+s=p, |r−s|≤2q
(n − m
r
)(n − m
s
)
(ar+ibs+j − as+jbr+i).
Now use summation by parts, together with the fact that
u(r) =
(n − m
r
)(n − m
p − r
)
is decreasing in r for r ≥ p/2, to argue that it suﬃces to show that
Tq =
∑
r+s=p, r,s≥0, |r−s|≤2q
(ar+ibs+j − as+jbr+i) ≥ 0 (27)
for each q. Here is the argument: noting that
Sq − Sq−1 = (Tq − Tq−1)u
(
q + [p/2]
)
and summing, we have
Sq =
∑
r≤q
(Sr − Sr−1) =
∑
r≤q
(Tr − Tr−1)u
(
r + [p/2]
)
= Tqu
(
q + [p/2]
)
+
∑
r<q
Tr
[
u
(
r + [p/2]
)
−
[
u
(
r + 1 + [p/2]
)]
.
Now to check (27), we rearrange the sum as follows, noting that th ere may be some
cancellation of terms, leading to the truncation of the upper limit of t he sum:
(k+i)∧(ℓ+j−1)∑
r=ℓ+i
(arbp−r+i+j − ap−r+i+jbr).
40 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
Here again k + ℓ = p, and k − ℓ = 2q if p is even and k − ℓ = 2q − 1 if p is odd. The
summands in this sum are non-negative by (ii) since for all r appearing in the sum,
r ≤ p − r + i + j. To check this, write 2 r = r + r ≤ (k + i) + (ℓ + j) = p + i + j. □
Corollary 6.5. Suppose {ak}n
k=0 and {bk}n
k=0 are LC sequences that satisfy
(i) {λak + bk}n
k=0 is LC for all λ > 0, and
(ii) akbk+1 ≥ ak+1bk for 0 ≤ k < n.
Then µ is CNA+.
Proof. Let {wi > 0}n+1
i=1 be the external ﬁeld that is applied to µ, and µ′ be the
resulting measure:
µ′(S) = constant ×
n+1∏
i=1
wXi (S)
i µ(S), S ⊆ [n + 1].
We need to show that (24) holds with µ replaced by µ′. First, note that the eﬀect
of wn+1 is to replace ak by a constant multiple of ak, so since we have introduced
a general positive λ in assumption (i), we may assume that wn+1 = 1. The analog
of (25) that we must check is
∑
i<j
∑
k,ℓ
(fj − fi)cicjdkdℓ
[
(hk − hℓ)ak+iaℓ+j
+ (gk − gℓ)bk+ibℓ+j + (hk − gℓ)ak+ibℓ+j + (gk − hℓ)aℓ+jbk+i
]
≥ 0, (28)
where now the fk’s, gk’s and hk’s are obtained by symmetrizing F and G with
respect to the ﬁeld on the set of coordinates {X1, . . . , Xm} in the case of F and
{Xm+1, . . . , Xn} in the case of G. For example,
fk = c−1
k ·
∑
F (S)
m∏
i=1
wXi(S)
i ,
where
ck =
∑ m∏
i=1
wXi (S)
i
and the above sums are taken over all S ⊆ [m] such that ∑ m
i=1 Xi(S) = k. The
formulas for gk and hk are exactly analogous and the corresponding normalization
factor (instead of ck) is
dk =
∑ n∏
i=m+1
wXi (S)
i ,
the sum being taken over all S ⊆ { m + 1, . . . , n} such that ∑ n
i=m+1 Xi(S) = k.
Note that if wi ≡ 1, then ck =
(m
k
)
and dk =
(n−m
k
)
, so that fk reduces to the
symmetrization used in the proof of Theorem 6.4, and (28) reduces to (25).
In order to deduce (28) from the arguments used to prove (25), we then need to
check the following statements:
(a) fk ≤ fk+1, gk ≤ gk+1, hk ≤ hk+1 and gk ≤ hk for all k, and
(b) {dk}n−m
k=0 is an LC sequence.
The latter is needed to check that drdp−r is decreasing in r for r ≥ p/2, which is
then used in the analog of the treatment of case (d) in the proof of Theorem 6.4.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 41
Note that statement (b) follows from e.g. Theorem 3.8, since dk is just the k-th
elementary symmetric function on {wm+1, . . . , wn}.
Now the fact that gk ≤ hk is immediate from the monotonicity of G in its last
argument. The veriﬁcation of the ﬁrst three statements in (a) is t he same for all of
them, so we check (a) only for fk. Letting as usual |S| denote the cardinality of a
set S, write
ckck+1(fk+1 − fk) =
∑
|S|=k, |T |=k+1
[F (T ) − F (S)]
m∏
i=1
wXi(S)+Xi(T )
i .
Consider the sum of the terms corresponding to S’s and T ’s that satisfy Xi(S) +
Xi(T ) = zi for all i and an arbitrarily ﬁxed z ∈ {0, 1, 2}m. If A, B, C are the index
sets corresponding to those coordinates Xi for which zi = 0 , 1, 2, respectively, we
see that we need to check
∑
|T |=k+1, Xi(T )=0, i∈A,
Xi (T )=1, i∈C
F (T ) ≥
∑
|S|=k, Xi (S)=0,i∈A,
Xi (S)=1,i∈C
F (S). (29)
Noting that the sums above have the same number of summands, na mely
(2k − 2|C| + 1
k − |C| + 1
)
and
(2k − 2|C| + 1
k − |C|
)
,
respectively, we see that (29) is a consequence of the monotonicit y of F . □
Recall from Remark 2.4 that CNA+ ⇒ Rayleigh/h-NLC+ and CNA ⇒ h-NLC.
By combining Proposition 6.2 and Corollary 6.5 on the one hand, and Pro posi-
tion 6.3 and Theorem 6.4 on the other hand, we deduce the following re sult.
Corollary 6.6. If µ is an almost symmetric measure (i.e., its generating polyno -
mial is symmetric in all but possibly one variable, cf. Deﬁni tion 2.1), then
(1) µ is Rayleigh/h-NLC+ ⇐ ⇒µ is CNA+;
(2) µ is h-NLC ⇐ ⇒µ is CNA.
This shows that Pemantle’s Conjecture 2.6 is true for almost symmet ric measures
(recall that by the results in §4.2, Conjecture 2.6 also holds for strongly Rayleigh
measures and PHR measures).
