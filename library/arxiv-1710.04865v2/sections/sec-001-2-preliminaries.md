---
doc_id: arxiv-1710.04865v2
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 6-12
source_pdf: 1710.04865v2.pdf
source_sha256: ac8f436173d550e8
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
duplicate_of: "cjdoubletwistfinal"
---
a discussion of the generalized Kontsevich-Zagier functions and the generalized U-functions for
the torus knots T(2,2t+1), along with some related questions.
2. Preliminaries
We begin by recalling the setup from [28]. Let l andt be coprime odd integers with l>t ≥ 1
and p′ := l−1
2 . For 1 ≤ j≤ p′, deﬁne integers r(j) such that r(j)≡ (2j− 1)t (mod 2l) and
−l < r(j) < l. We put σj := (−1)⌊ (2j−1)t
l ⌋, r′(j) := |r(j)|+1
2 and ir′(j) = j (and thus ik = j if
and only if r′(j) = k). For an integer i, sgn(i) denotes the sign of i. Let n = (n1,...,n p′) and
ns = 0 for s≤ 0. Finally, deﬁne
κ(p′) =
{
−Nnp′ if σp′ =−1,
0 if σp′ = 1 (2.1)
and
τ(j) =
{
(−1)nj−nj−1 if σj =−1,
q(
nj−nj−1+1
2 ) if σj = 1. (2.2)
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 7
Consider the family of 2-bridge knots b(l,t ) [5]. The main result in [28] is an explicit formula
for the colored Jones polynomial of b(l,t )∗.
Theorem 2.1. We have
JN(b(l,t )∗;q) =
∑
N−1≥np′≥...≥n1≥0
qa(n)N+b1(n)+b2(n)X(n) (2.3)
where2
a(n) =−1
2
p′
∑
j=1
( p′
∑
k=r′(j)
(σik +σip′+1−k)
)
(nj−nj−1)− 1
2
p′−1∑
j=1
(σj+1 +σp′+1−j)nj
− 1
2(σp′ + 1)np′−
p′
∑
j=1
σj,
b1(n) =−a(n) +
l−t
2∑
k=1
1−σik
2 nik−1−
p′
∑
k= l−t
2 +1
nik−1 +
p′
∑
k= l−t
2 +1
1 +σik
2 nik− (1 +σp′)np′
+ 1
2
p′−1∑
j=1
(σj+1−σj)nj
− 1
2
p′−1∑
k=1
p′
∑
k′=k+1
1 + sgn(ik−ik′)
2 (σik−σik′)(nik−nik−1)(nik′−nik′−1)
+
p′
∑
j=1
σj
(r′(j)∑
k=1
(nik−nik−1)
)
nj−1,
b2(n) =



t−1
2∑
k= l−t
2 +1
1 +σik
2 nik−1 if l< 2t
−
l−t
2∑
k= t+1
2 +1
1 +σik
2 nik−1 if l> 2t,
X(n) = (−1)np′qκ(p′) (q)N−1(q)np′
(q)N−np′−1
p′
∏
j=1
τ(j)
(q)nj−nj−1
.
As the mirror image of the torus knots T(2,2t+1) is b(2t + 1, 1) (cf. [5, 26, 29]), one can
check that Theorem 2.1 recovers the q-hypergeometric expression for JN(T(2,2t+1);q) given in
[14, 15]. Our interest will be to apply Theorem 2.1 to the case of the double twist knots
K(m,p) = b(4mp− 1, 4mp− 2p− 1) and K(m,−p) = b(4mp + 1, 4mp− 2p + 1) (cf. [29]). In order
to facilitate these computations, we need the following results concerning σj, ik and σik. We
omit the proofs as they are straightforward generalizations of Lemmas 6–9 in [28].
2Note that there is a misprint in the deﬁnition of X(n) in [28]. Each q in the prefactor should be q.
8 JEREMY LOVEJOY AND ROBERT OSBURN
Lemma 2.2. Forl = 4mp− 1 and t = 4mp− 2p− 1, we have
(i) σj =
{
1 if j≡ 1, 2,...,m (mod 2m)
−1 if j≡ 0,m + 1,..., 2m− 1 (mod 2m).
(ii) To compute ik, apply the following algorithm. Divide the integers from 1 to p′ into
2m− 1 intervals, each of length p, and a ﬁnal interval of length p− 1. The value of ik
is 2m(p−k) +m in the ﬁrst interval and 1− (2m(p−k) +m) in the second. If j >1
is odd, then to obtain the value of ik in the jth interval, add 4mp− 1 to the formula for
ik in the (j− 2)th interval. If j > 2 is even, then to obtain the value of ik in the jth
interval, subtract 4mp− 1 from the formula for ik in the (j− 2)th interval.
(iii) To compute σik, apply the following algorithm. Divide the integers from 1 to p′ into
2m− 1 intervals, each of length p, and a ﬁnal interval of length p− 1. The value of σik
alternates between 1 and−1 starting with 1 in the ﬁrst interval.
Lemma 2.3. Letl = 4mp− 1 and t = 4mp− 2p− 1. Then for 1≤k≤p′ and 1≤j≤p′− 1
we have
(i) σik +σip′+1−k =



2 if k =p, 3p,..., (2m− 1)p
−2 if k = 2p,..., (2m− 2)p
0 otherwise.
(ii) σj+1 +σp′+1−j = 0.
Lemma 2.4. Forl = 4mp + 1 and t = 4mp− 2p + 1, we have
(i) σj =
{
1 if j≡ 1, 2,...,m (mod 2m)
−1 if j≡ 0,m + 1,..., 2m− 1 (mod 2m).
(ii) To compute ik, apply the following algorithm. Divide the integers from 1 to p′ into 2m
intervals of length p. The value of ik is 2m(p−k) +m + 1 in the ﬁrst interval and
1− (2m(p−k) +m + 1) in the second. If j >1 is odd, then to obtain the value of ik in
the jth interval, add 4mp + 1 to the formula for ik in the (j− 2)th interval. If j >2 is
even, then to obtain the value of ik in the jth interval, subtract 4mp+1 from the formula
for ik in the (j− 2)th interval.
(iii) To computeσik, apply the following algorithm. Divide the integers from 1 to p′ into 2m
intervals of length p. The value of σik alternates between−1 and 1 starting with−1 in
the ﬁrst interval.
Lemma 2.5. Letl = 4mp + 1 and t = 4mp− 2p + 1. Then for 1≤k≤p′ and 1≤j≤p′− 1
we have
(i) σik +σip′+1−k = 0
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 9
(ii) σj+1 +σp′+1−j =



2 if j≡ 0 (mod 2m)
−2 if j≡m (mod 2m)
0 otherwise.
We now illustrate the computation of a(n) and b1(n) +b2(n) for l = 8p− 1 and t = 6p− 1.
The routine evaluation of X(n) is left to the reader. First, we take m = 2 in Lemmas 2.2 and
2.3 to obtain
σj =
{
1 if j≡ 1, 2 (mod 4)
−1 if j≡ 0, 3 (mod 4) , (2.4)
ik =



4(p−k) + 2 if 1 ≤k≤p,
4(k−p)− 1 if p + 1≤k≤ 2p,
12p− 4k + 1 if 2 p + 1≤k≤ 3p,
4k− 12p if 3p + 1≤k≤ 4p− 1,
(2.5)
σik =



1 if 1 ≤k≤p,
−1 if p + 1≤k≤ 2p,
1 if 2 p + 1≤k≤ 3p,
−1 if 3 p + 1≤k≤ 4p− 1,
(2.6)
σik +σi4p−k =



2 if k =p, 3p
−2 if k = 2p
0 otherwise
(2.7)
and
σj+1 +σ4p−j = 0. (2.8)
Applying (2.4), (2.5), (2.7), (2.8) and reindexing yields
a(n) =−1
2
4p−1∑
j=1
( 4p−1∑
k=r′(j)
(σik +σi4p−k)
)
(nj−nj−1)− 1
=−1
2
[ p∑
j=1
( 4p−1∑
k=3p−j+1
(σik +σi4p−k)
)
(n4j−3−n4j−4)
+
p∑
j=1
( 4p−1∑
k=p−j+1
(σik +σi4p−k)
)
(n4j−2−n4j−3) +
p−1∑
j=1
( 4p−1∑
k=3p+j
(σik +σi4p−k)
)
(n4j−n4j−1)
+
p∑
j=1
( 4p−1∑
k=p+j
(σik +σi4p−k)
)
(n4j−1−n4j−2)
]
− 1
=
2p−1∑
j=1
(−1)jn2j− 1.
(2.9)
By (2.4) and (2.6), the second and ﬁfth sums in b1(n) are zero. We then use (2.4)–(2.6) and
reindex to obtain
10 JEREMY LOVEJOY AND ROBERT OSBURN
−
4p−1∑
k=p+1
nik−1 =−
( 2p∑
k=p+1
nik−1 +
3p∑
k=2p+1
nik−1 +
4p−1∑
k=3p+1
nik−1
)
=−
( p∑
j=1
(n4j−2 +n4j−4) +
p−1∑
j−1
n4j−1
)
,
(2.10)
4p−1∑
k=p+1
1 +σik
2 nik =
3p∑
k=2p+1
nik =
p∑
j=1
n4j−3, (2.11)
1
2
4p−2∑
j=1
(σj+1−σj)nj =
2p−1∑
j=1
(−1)jn2j (2.12)
and
b2(n) =
3p−1∑
k=p+1
1 +σik
2 nik−1 =
3p−1∑
k=2p+1
nik−1 =
p∑
j=2
n4j−4. (2.13)
By (2.9)–(2.13), the sum of b2(n) and the ﬁrst six terms in b1(n) equals
1 +n4p−1 +
p∑
j=1
(n4j−3−n4j−2−n4j−1). (2.14)
To compute the seventh term inb1(n), we use (2.5) and (2.6) to observe thatk<k ′ andσik⁄=σik′
if and only if either 1 ≤ k≤ p and p + 1≤ k′≤ 2p or 1≤ k≤ p and 3p + 1≤ k′≤ 4p− 1
or p + 1≤ k≤ 2p and 2p + 1≤ k′ ≤ 3p or 2p + 1≤ k≤ 3p and 3p + 1≤ k′ ≤ 4p− 1.
Also, sgn(ik−ik′) = 1 if and only if ik > ik′ and either ik = 4p− 4k + 2 for 1 ≤ k≤ p and
ik′ = 4k′− 4p− 1 for p + 1≤ k′≤ 2p or ik = 4p− 4k + 2 for 1 ≤ k≤ p and ik′ = 4k′− 12p
for 3p + 1≤ k′≤ 4p− 1 or ik = 4k− 4p− 1 for p + 1≤ k≤ 2p and ik′ = 12p− 4k′ + 1
for 2p + 1 ≤ k′ ≤ 3p or ik = 12p− 4k + 1 for 2 p + 1 ≤ k ≤ 3p and ik′ = 4k′− 12p for
3p + 1≤k′≤ 4p− 1. Taking these cases into account and reindexing, we have
− 1
2
4p−2∑
k=1
4p−1∑
k′=k+1
1 + sgn(ik−ik′)
2 (σik−σik′)(nik−nik−1)(nik′−nik′−1)
=−
p∑
k=1
2p−k∑
k′=p+1
(nik−nik−1)(nik′−nik′−1)−
p∑
k=1
4p−k∑
k′=3p+1
(nik−nik−1)(nik′−nik′−1)
+
2p∑
k=p+1
3p∑
k′=4p−k+1
(nik−nik−1)(nik′−nik′−1)−
3p∑
k=2p+1
6p−k∑
k′=3p+1
(nik−nik−1)(nik′−nik′−1)
=−
p∑
j=1
j∑
j′=2
(n4j−2−n4j−3)(n4j′−5−n4j′−6)−
p∑
j=1
j∑
j′=2
(n4j−2−n4j−3)(n4j′−4−n4j′−5)
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 11
+
p∑
j=1
j∑
j′=1
(n4j−1−n4j−2)(n4j′−3−n4j′−4)−
p∑
j=1
j∑
j′=2
(n4j−3−n4j−4)(n4j′−4−n4j′−5).
(2.15)
Finally, using (2.4) and (2.5), then reindexing and simplifying gives the eighth term in b1(n),
4p−1∑
j=1
σj
(r′(j)∑
k=1
(nik−nik−1)
)
nj−1
=
p∑
j=1
σ4j−3
(3p−j+1∑
k=1
(nik−nik−1)
)
n4j−4 +
p∑
j=1
σ4j−2
(p−j+1∑
k=1
(nik−nik−1)
)
n4j−3
+
p−1∑
j=1
σ4j
(3p+j∑
k=1
(nik−nik−1)
)
n4j−1 +
p∑
j=1
σ4j−1
(p+j∑
k=1
(nik−nik−1)
)
n4j−2
=
p∑
j=1
( p∑
k=1
(n4p−4k+2−n4p−4k+1) +
2p∑
k=p+1
(n4k−4p−1−n4k−4p−2)
+
3p−j+1∑
k=2p+1
(n12p−4k+1−n12p−4k)
)
n4j−4 +
p∑
j=1
(p−j+1∑
k=1
(n4p−4k+2−n4p−4k+1)
)
n4j−3
−
p−1∑
j=1
( p∑
k=1
(n4p−4k+2−n4p−4k+1) +
2p∑
k=p+1
(n4k−4p−1−n4k−4p−2)
+
3p∑
k=2p+1
(n12p−4k+1−n12p−4k) +
3p+j∑
k=3p+1
(n4k−12p−n4k−12p−1)
)
n4j−1
−
p∑
j=1
( p∑
k=1
(n4p−4k+2−n4p−4k+1) +
p+j∑
k=p+1
(n4k−4p−1−n4k−4p−2)
)
n4j−2
=
p∑
j=1
(j−1∑
j′=1
(n4j′−1−n4j′−3) +
p∑
j=j′
(n4j′−1−n4j′−4)
)
n4j−4 +
p∑
j=1
( p∑
j′=j
(n4j′−2−n4j′−3)
)
n4j−3
−
p−1∑
j=1
( p∑
j′=j+1
(n4j′−1−n4j′−4) +n4j
)
n4j−1
−
p∑
j=1
( j∑
j′=1
(n4j′−1−n4j′−3) +
p∑
j′=j+1
(n4j′−2−n4j′−3)
)
n4j−2.
(2.16)
Thus, combining (2.9)–(2.16) implies that b1(n) +b2(n) equals
12 JEREMY LOVEJOY AND ROBERT OSBURN
1 +n4p−1 +
p∑
j=1
(n4j−3−n4j−2−n4j−1)
−
p∑
j=1
j∑
j′=2
(n4j−2−n4j−3)(n4j′−5−n4j′−6)−
p∑
j=1
j∑
j′=2
(n4j−2−n4j−3)(n4j′−4−n4j′−5)
+
p∑
j=1
j∑
j′=1
(n4j−1−n4j−2)(n4j′−3−n4j′−4)−
p∑
j=1
j∑
j′=2
(n4j−3−n4j−4)(n4j′−4−n4j′−5)
+
p∑
j=1
(j−1∑
j′=1
(n4j′−1−n4j′−3) +
p∑
j=j′
(n4j′−1−n4j′−4)
)
n4j−4 +
p∑
j=1
( p∑
j′=j
(n4j′−2−n4j′−3)
)
n4j−3
−
p−1∑
j=1
( p∑
j′=j+1
(n4j′−1−n4j′−4) +n4j
)
n4j−1
−
p∑
j=1
( j∑
j′=1
(n4j′−1−n4j′−3) +
p∑
j′=j+1
(n4j′−2−n4j′−3)
)
n4j−2.
