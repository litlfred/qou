---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-006-8-jeremy-lovejoy-and-robert-osburn
section_title: "JEREMY LOVEJOY AND ROBERT OSBURN"
section_number: 8
pages: 8-10
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
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
