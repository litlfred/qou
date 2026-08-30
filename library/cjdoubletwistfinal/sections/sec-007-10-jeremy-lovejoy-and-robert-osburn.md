---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-007-10-jeremy-lovejoy-and-robert-osburn
section_title: "JEREMY LOVEJOY AND ROBERT OSBURN"
section_number: 10
pages: 10-12
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
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
