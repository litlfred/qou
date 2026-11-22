---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-019-6-almost-exchangeable-measures
section_title: "Almost exchangeable measures"
section_number: 6
pages: 33-41
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
By Pemantle’s result (Theorem 3.7 in §3.5), for symmetric measures in Pn all
ﬁve conditions NLC, h-NLC, Rayleigh/h-NLC+, CNA, and CNA+ are equivalent
to the ULC condition for the rank sequence. Therefore, the relations between all
these negative dependence properties are completely understood in the exchange-
able case. In this section we study the almost exchangeable case, that is, measures
whose generating polynomials are symmetric in all but possibly one variable (Def-
inition 2.1). We prove that for such measures one has both h-NLC ⇔CNA and
554
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
Rayleigh/h-NLC+ ⇔CNA+, which conﬁrms Pemantle’s Conjecture 2.6 in this
case. In the next section we will use this result to show that the counterexamples
in 20 or more variables that we construct there satisfy all negative dependence
properties other than strongly Rayleigh.
Let C be an m × n matrix (where m, n are allowed to be inﬁnite), and let i and
j be ﬁnite equi-numerous subsets of [m] and [n], respectively. Denote by C(i, j) the
minor of C with rows indexed by i and columns indexed by j. The Cauchy-Binet
theorem, see, e.g., [49], asserts that
(AB)(i, j) =

k, |k|=|i|=|j|
A(i, k)B(k, j)
for any m × n matrix A and n × q matrix B, where 1 ≤m, n, q ≤∞, provided that
the sum in the right-hand side converges absolutely.
Recall the notion of (non-negative) LC sequence from Deﬁnition 2.8. For conve-
nience, we ﬁrst prove a technical result that will be frequently used later on.
Lemma 6.1. Let {aj}n
j=0 and {bj}n
j=0 be two LC sequences that satisfy
(i) {aj + bj}n
j=0 is LC, and
(ii) ajbj+1 ≥aj+1bj for all 0 ≤j ≤n −1.
If ℓ< k and bℓak > 0, then brar > 0 for all ℓ≤r ≤k.
Proof. Suppose that ar = 0 for some ℓ≤r < k and let s be the largest such index.
Assumption (ii) for j = s gives bs = 0, hence as + bs = 0. This contradicts the “no
internal zeros” part of assumption (i) (cf. Deﬁnition 2.8). Therefore ar > 0, and a
similar argument shows that br > 0 as well.
□
The following proposition shows that for almost exchangeable measures the
Rayleigh property is the same as the negative lattice condition (NLC) closed under
conditioning and external ﬁelds on the last variable. Indeed, condition (ii) follows
directly from NLC while (i) follows from NLC after having imposed an external
ﬁeld on the last coordinate and then projected onto the ﬁrst n coordinates.
Proposition 6.2. Let µ ∈Pn+1 be such that its generating polynomial g = gµ is
symmetric in its ﬁrst n variables, so that
g(z1, . . . , zn+1) = zn+1
n

k=0
akek(z1, . . . , zn) +
n

k=0
bkek(z1, . . . , zn).
Then µ is Rayleigh if and only if
(i) {θak + (1 −θ)bk}n
k=0 is LC for all 0 ≤θ ≤1, and
(ii) akbk+1 ≥ak+1bk for all 0 ≤k ≤n −1.
Proof. Suppose ﬁrst that µ is Rayleigh. By Proposition 2.1 we get that if 0 ≤θ < 1,
then g(z1, . . . , zn, θ/(1 −θ)) is a Rayleigh polynomial that is symmetric in all its
n variables. Condition (i) now follows from the exchangeable case (Theorem 3.7).
Let S ⊆[n −1] be of cardinality i. The NLC condition gives
aibi+1 = µ(S ∪{n + 1})µ(S ∪{n}) ≥µ(S ∪{n, n + 1})µ(S) = ai+1bi,
which veriﬁes (ii).
Assume now that {ak}n
k=0 and {bk}n
k=0 satisfy (i) and (ii). The inequality
∂g
∂zi
(x) ∂g
∂zj
(x) ≥
∂2g
∂zi∂zj
(x)g(x),
x ∈Rn+1
+
, i, j ∈[n],
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
555
follows from the exchangeable case and (i). What is left to prove is the inequality
∂g
∂zi
(x)
∂g
∂zn+1
(x) ≥
∂2g
∂zi∂zn+1
(x)g(x),
x ∈Rn+1
+
, i ∈[n],
and by symmetry (in the ﬁrst n variables) we only need to check it for, e.g. i = n.
We may write g as
g(z1, . . . , zn+1) =
n

k=0
bkek(z1, . . . , zn−1) + zn
n

k=0
bk+1ek(z1, . . . , zn−1)
+ zn+1
n

k=0
akek(z1, . . . , zn−1) + znzn+1
n

k=0
ak+1ek(z1, . . . , zn−1),
so the desired inequality is equivalent to
(20)
⎛
⎝
j
ajej
⎞
⎠
⎛
⎝
j
bj+1ej
⎞
⎠−
⎛
⎝
j
aj+1ej
⎞
⎠
⎛
⎝
j
bjej
⎞
⎠≥0
for all x ∈Rn−1
+
, where ej = ej(x1, . . . , xn−1). Now let
C =

a0
a1
a2
. . .
an
b0
b1
b2
. . .
bn

and recall the deﬁnition of a TPp matrix from §3.5. We claim that C is TP2. Let
1 ≤i < j ≤n. We need to prove that aibj ≥biaj. Clearly, we may assume that
biaj̸ = 0 and that j −i ≥2. By Lemma 6.1 we have brar > 0 for i ≤r ≤j and
thus
ai
bi
≥ai+1
bi+1
≥· · · ≥aj
bj
by (ii), which shows that C is indeed TP2. Let E = (ei−j)n
i,j=0. By Theorem 3.8
we have that E is TP2, and by the Cauchy-Binet formula so is CE. Now
CE =
  ajej
 aj+1ej
. . .
 bjej
 bj+1ej
. . .

,
from which (20) follows.
□
The next result is the analog of Proposition 6.2 for the h-NLC property.
Proposition 6.3. Let µ ∈Pn+1 be such that its generating polynomial g = gµ is
symmetric in its ﬁrst n variables, so that
g(z1, . . . , zn+1) = zn+1
n

k=0
akek(z1, . . . , zn) +
n

k=0
bkek(z1, . . . , zn).
Then µ is h-NLC if and only if
(i) {ak}n
k=0, {bk}n
k=0, and {ak + bk}n
k=0 are LC, and
(ii) akbk+1 ≥ak+1bk for all 0 ≤k ≤n −1.
Proof. Let S, T ⊂[n]. The NLC condition applied to each of the three pairs (S, T),
(S, T ∪{n + 1}), and (S ∪{n + 1}, T ∪{n + 1}) gives, respectively,
b|S|b|T | ≥b|S∪T |b|S∩T |,
b|S|a|T | ≥a|S∪T |b|S∩T |,
a|S|a|T | ≥a|S∪T |a|S∩T |.
Therefore, setting ℓ= |S|, k = |T|, m = |S ∩T|, we see that NLC is equivalent to
556
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
(21)
bℓbk ≥bk+ℓ−mbm,
bℓak ≥ak+ℓ−mbm,
aℓak ≥ak+ℓ−mam
for m ≤k, ℓ≤n and k + ℓ≤n + m.
If S ⊆[n] has cardinality n −j, the measure obtained by projecting µ onto
2S∪{n+1} is of the same form as µ with coeﬃcients
ak(j) =
j

i=0
j
i

ak+i
and
bk(j) =
j

i=0
j
i

bk+i,
0 ≤k ≤n −j,
while the one obtained by projecting µ onto 2S is exchangeable with coeﬃcients
ak(j) + bk(j), 0 ≤k ≤n −j. Therefore, h-NLC is equivalent to the statement that
for each 0 ≤j ≤n one has
bℓ(j)bk(j) ≥bk+ℓ−m(j)bm(j),
bℓ(j)ak(j) ≥ak+ℓ−m(j)bm(j), aℓ(j)ak(j) ≥ak+ℓ−m(j)am(j),
(aℓ(j) + bℓ(j))(ak(j) + bk(j)) ≥(ak+ℓ−m(j) + bk+ℓ−m(j))(am(j) + bm(j))
(22)
for m ≤k, ℓ≤n −j and k + ℓ≤n −j + m.
It follows from this that the h-NLC property implies that the sequences in (i)
have no internal zeros. For example, if k ≤ℓ, bk−1 > 0, bk = · · · = bℓ= 0, bℓ+1 > 0
contradicts bkbℓ≥bk−1bℓ+1. Given this, the fact that the three sequences are LC
and satisfy (ii) is a consequence of the ﬁrst and last inequalities in (21) with ℓ= k,
m = k −1, the middle inequality in (21) with ℓ= k + 1, m = k, and the last
inequality in (22) with j = 0, ℓ= k, m = k −1.
For the converse, assume that (i) and (ii) hold. Note that for each j, {ak(j)}n−j
k=0
is a convolution of two LC sequences, and hence is LC by [49, Theorem 1.2 on
p. 394], and the same holds for the sequences bk(j) and ak(j) + bk(j). This gives
three of the four inequalities in (22). For the other one, note that since evaluating
the elementary symmetric polynomials at the “all ones vector” produces binomial
coeﬃcients, it follows from (20) that
(23)
ak(j)bk+1(j) ≥ak+1(j)bk(j).
We need to check that
ak(j)bℓ(j) ≥ak+ℓ−m(j)bm(j)
for m ≤k, ℓ, and in doing so, can assume that the right-hand side is not zero. By
Lemma 6.1, it follows that ai(j)bi(j) > 0 for m ≤i ≤k + ℓ−m. To conclude the
proof, write
ak(j)
ak+ℓ−m(j) ≥am(j)
aℓ(j) ≥bm(j)
bℓ(j) .
The ﬁrst inequality comes from the already proved part of (22), while the second
is obtained by repeated application of (23).
□
Theorem 6.4. Let µ ∈Pn+1 be such that its generating polynomial g = gµ is
symmetric in its ﬁrst n variables, so that
g(z1, . . . , zn) = zn+1
n

k=0
akek(z1, . . . , zn) +
n

k=0
bkek(z1, . . . , zn).
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 557

Suppose that {ay}R_9 and {bp }p-9 are LC sequences that satisfy
(i) {ap + de }peo is LC, and
(ii) Aber > angibe for allO<k<n-1.

Then pu is CNA.

Proof. Asin we denote by X;, i € [n+1], the i-th coordinate function/random
(binary) variable on 2in+1]_ First, observe that it is enough to prove that pis NA.
To see this, note that if 4 is conditioned on X; = 1 for k values of i < n, on X; = 0
for | values of i < n, and possibly on the value of X,4+1, the resulting measure is
of the same form with a new value n’ of n and new a,’s and b;’s that again satisfy
the assumptions of the theorem. Using primes to denote the new values, we have
n’ =n—k-—l, and if the value of X,41 is not conditioned on, then, except for
a constant factor, a, = ajz, and bi = bi+,. If the value of X;,41 is conditioned
on, then a} = b! = a+ if the conditioning is on X,41 = 1 and a} = bi = die, if
the conditioning is on X,41; = 0. Now take two increasing functions F and G on
alr+1] that depend on disjoint sets of coordinates (cf. Definition 2.2). Without loss
of generality, we may assume that there is an m satisfying 1 < m <n such that
F depends on the coordinates {X1...,Xm}, and G depends on the coordinates
{Xingi,---;Xn4i}. We need to prove

(24) [ Poa < [Pe fea.

Since jz is symmetric in the first n coordinates, these three integrals are not changed
if F and G are replaced by the functions obtained by symmetrizing them with
respect to the coordinates {X1,...,Xm} and {Xm41,-.-,Xn}, respectively. These
symmetrized functions are also increasing. Therefore, we may assume that F’ and
G are of the following form:

m

F(X1,...,Xm) = fe if SO Xi =k,
i=l

n
G(Xmpis-.s Xn Xnp1 =0) = ge if SS Xi =k, and

i=m+1

n
G(Xmgas Xn Xng1 = VY =heif SO Xi =k,
i=m41

where fx, gx and hy, are increasing, and g;, < hy, for each k. Using the fact that the
covariance of F and G with respect to the measure jz can be written as

1

5 LPS) — FIDYIG(S) — G(T) a(S) a7),

S.Te2ln+)

becomes

SVM an ft-ro

+ (gk — ge)be+ibdery + (he — ge)an+ibers + (ge — he)acyjbeti] = 0.
558
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
Note that we are using the usual convention that
 n
m
	
= 0 unless 0 ≤m ≤n. Since
the summand above is not changed if the roles of i and j are interchanged and the
roles of k and ℓare interchanged, this can be written as
(25)

i<j

k,ℓ
m
i
m
j
n −m
k
n −m
ℓ

(fj −fi)
*
(hk −hℓ)ak+iaℓ+j
+ (gk −gℓ)bk+ibℓ+j + (hk −gℓ)ak+ibℓ+j + (gk −hℓ)aℓ+jbk+i
+
≥0.
So, it is enough to show that for ﬁxed i < j and ﬁxed p,

k+ℓ=p
n −m
k
n −m
ℓ
*
(hk −hℓ)ak+iaℓ+j
+ (gk −gℓ)bk+ibℓ+j + (hk −gℓ)ak+ibℓ+j + (gk −hℓ)aℓ+jbk+i
+
≥0.
Furthermore, it is enough to prove this in the case when the gk’s and hk’s take
only the values 0 and 1, since any increasing function on a partially ordered set
(in this case, {0, . . . , n} × {0, 1}) can be written as a positive linear combination of
increasing functions that take only the values 0 and 1.
We will in fact prove that for such gk’s and hk’s,
Sq =

k+ℓ=p, |k−ℓ|≤2q
n −m
k
n −m
ℓ
*
(hk −hℓ)ak+iaℓ+j
+ (gk −gℓ)bk+ibℓ+j + (hk −gℓ)ak+ibℓ+j + (gk −hℓ)aℓ+jbk+i
+
≥0
by induction on q. For the basis step, note that S0 = 0 if p is odd, while if p = 2r
is even, then
S0 =
n −m
r
2
(hr −gr)(ar+ibr+j −ar+jbr+i),
which is non-negative by (ii), since i < j.
We will now prove that Sq ≥0, assuming that Sq−1 ≥0. The diﬀerence Sq−Sq−1
consists of two summands, which when combined, become
(26)n −m
k
n −m
ℓ
*
(hk−hℓ)(ak+iaℓ+j−aℓ+iak+j)+(gk−gℓ)(bk+ibℓ+j−bℓ+ibk+j)
+ (hk −gℓ)(ak+ibℓ+j −ak+jbℓ+i) + (gk −hℓ)(aℓ+jbk+i −aℓ+ibk+j)
+
,
where k +ℓ= p, while k −ℓ= 2q if p is even and k −ℓ= 2q −1 if p is odd. Now we
consider the possible values of gℓ, hk for this pair k, ℓ. Recall that gℓ≤hℓ, gk ≤hk.
If gℓ= hk, then gt = ht = this common value for all ℓ≤t ≤k, so that (26) is zero.
So, we may assume that gℓ= 0, hk = 1. Now there are four possible values for the
pair (hℓ, gk) (note that the use of the fractions that appear below is justiﬁed by
Lemma 6.1):
(a)
hℓ= gk = 1. In this case, (26) becomes
n −m
k
n −m
ℓ
*
(bk+ibℓ+j −bℓ+ibk+j) + (ak+ibℓ+j −ak+jbℓ+i)
+
.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
559
This is non-negative by the log-concavity of the b’s and (ii):
ak+i
ak+j
≥bk+i
bk+j
≥bℓ+i
bℓ+j
.
(b)
hℓ= 0, gk = 1. Now (26) is
n −m
k
n −m
ℓ
*
(ak+i + bk+i)(aℓ+j + bℓ+j) −(aℓ+i + bℓ+i)(ak+j + bk+j)
+
,
which is non-negative by (i).
(c)
hℓ= gk = 0. This time (26) is
n −m
k
n −m
ℓ
*
(ak+iaℓ+j −aℓ+iak+j) + (ak+ibℓ+j −ak+jbℓ+i)
+
,
which is non-negative by the log-concavity of the a’s and (ii).
In these three cases, (26) is non-negative, and therefore Sq ≥0 by the induction
hypothesis. The fourth case is diﬀerent, since (26) need not be non-negative:
(d)
hℓ= 1, gk = 0. In this case, gt ≡0 and ht ≡1 for ℓ≤t ≤k, so
Sq =

r+s=p, |r−s|≤2q
n −m
r
n −m
s

(ar+ibs+j −as+jbr+i).
Now use summation by parts, together with the fact that
u(r) =
n −m
r
n −m
p −r

is decreasing in r for r ≥p/2, to argue that it suﬃces to show that
(27)
Tq =

r+s=p, r,s≥0, |r−s|≤2q
(ar+ibs+j −as+jbr+i) ≥0
for each q. Here is the argument: noting that
Sq −Sq−1 = (Tq −Tq−1)u

q + [p/2]
	
and summing, we have
Sq =

r≤q
(Sr −Sr−1) =

r≤q
(Tr −Tr−1)u

r + [p/2]
	
= Tqu

q + [p/2]
	
+

r<q
Tr
&
u

r + [p/2]
	
−u

r + 1 + [p/2]
	'
.
Now to check (27), we rearrange the sum as follows, noting that there may be some
cancellation of terms, leading to the truncation of the upper limit of the sum:
(k+i)∧(ℓ+j−1)

r=ℓ+i
(arbp−r+i+j −ap−r+i+jbr).
Here again k + ℓ= p, and k −ℓ= 2q if p is even and k −ℓ= 2q −1 if p is odd. The
summands in this sum are non-negative by (ii) since for all r appearing in the sum,
r ≤p −r + i + j. To check this, write 2r = r + r ≤(k + i) + (ℓ+ j) = p + i + j.
□
Corollary 6.5. Suppose {ak}n
k=0 and {bk}n
k=0 are LC sequences that satisfy
(i) {λak + bk}n
k=0 is LC for all λ > 0, and
(ii) akbk+1 ≥ak+1bk for 0 ≤k < n.
Then µ is CNA+.
560
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
Proof. Let {wi > 0}n+1
i=1 be the external ﬁeld that is applied to µ, and µ′ be the
resulting measure:
µ′(S) = constant ×
n+1

i=1
wXi(S)
i
µ(S),
S ⊆[n + 1].
We need to show that (24) holds with µ replaced by µ′. First, note that the eﬀect
of wn+1 is to replace ak by a constant multiple of ak, so since we have introduced
a general positive λ in assumption (i), we may assume that wn+1 = 1. The analog
of (25) that we must check is
(28)

i<j

k,ℓ
(fj −fi)cicjdkdℓ
*
(hk −hℓ)ak+iaℓ+j
+ (gk −gℓ)bk+ibℓ+j + (hk −gℓ)ak+ibℓ+j + (gk −hℓ)aℓ+jbk+i
+
≥0,
where now the fk’s, gk’s and hk’s are obtained by symmetrizing F and G with
respect to the ﬁeld on the set of coordinates {X1, . . . , Xm} in the case of F and
{Xm+1, . . . , Xn} in the case of G. For example,
fk = c−1
k
·

F(S)
m

i=1
wXi(S)
i
,
where
ck =
 m

i=1
wXi(S)
i
,
and the above sums are taken over all S ⊆[m] such that m
i=1 Xi(S) = k. The
formulas for gk and hk are exactly analogous, and the corresponding normalization
factor (instead of ck) is
dk =

n

i=m+1
wXi(S)
i
,
the sum being taken over all S ⊆{m + 1, . . . , n} such that n
i=m+1 Xi(S) = k.
Note that if wi ≡1, then ck =
m
k
	
and dk =
n−m
k
	
, so that fk reduces to the
symmetrization used in the proof of Theorem 6.4, and (28) reduces to (25).
In order to deduce (28) from the arguments used to prove (25), we then need to
check the following statements:
(a)
fk ≤fk+1, gk ≤gk+1, hk ≤hk+1 and gk ≤hk for all k, and
(b)
{dk}n−m
k=0 is an LC sequence.
The latter is needed to check that drdp−r is decreasing in r for r ≥p/2, which is
then used in the analog of the treatment of case (d) in the proof of Theorem 6.4.
Note that statement (b) follows from e.g. Theorem 3.8, since dk is just the k-th
elementary symmetric function on {wm+1, . . . , wn}.
Now the fact that gk ≤hk is immediate from the monotonicity of G in its last
argument. The veriﬁcation of the ﬁrst three statements in (a) is the same for all of
them, so we check (a) only for fk. Letting as usual |S| denote the cardinality of a
set S, write
ckck+1(fk+1 −fk) =

|S|=k, |T |=k+1
[F(T) −F(S)]
m

i=1
wXi(S)+Xi(T )
i
.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
561
Consider the sum of the terms corresponding to S’s and T’s that satisfy Xi(S) +
Xi(T) = zi for all i and an arbitrarily ﬁxed z ∈{0, 1, 2}m. If A, B, C are the index
sets corresponding to those coordinates Xi for which zi = 0, 1, 2, respectively, we
see that we need to check
(29)

|T |=k+1, Xi(T )=0, i∈A,
Xi(T )=1, i∈C
F(T) ≥

|S|=k, Xi(S)=0,i∈A,
Xi(S)=1,i∈C
F(S).
Noting that the sums above have the same number of summands, namely
2k −2|C| + 1
k −|C| + 1

and
2k −2|C| + 1
k −|C|

,
respectively, we see that (29) is a consequence of the monotonicity of F.
□
Recall from Remark 2.4 that CNA+ ⇒Rayleigh/h-NLC+ and CNA ⇒h-NLC.
By combining Proposition 6.2 and Corollary 6.5 on the one hand, and Proposi-
tion 6.3 and Theorem 6.4 on the other hand, we deduce the following result.
Corollary 6.6. If µ is an almost symmetric measure (i.e., its generating polyno-
mial is symmetric in all but possibly one variable; cf. Deﬁnition 2.1), then
(1) µ is Rayleigh/h-NLC+ ⇐⇒µ is CNA+;
(2) µ is h-NLC ⇐⇒µ is CNA.
This shows that Pemantle’s Conjecture 2.6 is true for almost symmetric measures
(recall that by the results in §4.2, Conjecture 2.6 also holds for strongly Rayleigh
measures and PHR measures).
