---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-010
section_title: "Page 10"
section_number: null
pages: 10-10
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
10
JEREMY LOVEJOY AND ROBERT OSBURN
−
4p−1
X
k=p+1
nik−1 = −
 
2p
X
k=p+1
nik−1 +
3p
X
k=2p+1
nik−1 +
4p−1
X
k=3p+1
nik−1
!
= −
 p
X
j=1
(n4j−2 + n4j−4) +
p−1
X
j−1
n4j−1
!
,
(2.10)
4p−1
X
k=p+1
1 + σik
2
nik =
3p
X
k=2p+1
nik =
p
X
j=1
n4j−3,
(2.11)
1
2
4p−2
X
j=1
(σj+1 −σj)nj =
2p−1
X
j=1
(−1)jn2j
(2.12)
and
b2(n) =
3p−1
X
k=p+1
1 + σik
2
nik−1 =
3p−1
X
k=2p+1
nik−1 =
p
X
j=2
n4j−4.
(2.13)
By (2.9)–(2.13), the sum of b2(n) and the ﬁrst six terms in b1(n) equals
1 + n4p−1 +
p
X
j=1
(n4j−3 −n4j−2 −n4j−1).
(2.14)
To compute the seventh term in b1(n), we use (2.5) and (2.6) to observe that k < k′ and σik̸ = σik′
if and only if either 1 ≤k ≤p and p + 1 ≤k′ ≤2p or 1 ≤k ≤p and 3p + 1 ≤k′ ≤4p −1
or p + 1 ≤k ≤2p and 2p + 1 ≤k′ ≤3p or 2p + 1 ≤k ≤3p and 3p + 1 ≤k′ ≤4p −1.
Also, sgn(ik −ik′) = 1 if and only if ik > ik′ and either ik = 4p −4k + 2 for 1 ≤k ≤p and
ik′ = 4k′ −4p −1 for p + 1 ≤k′ ≤2p or ik = 4p −4k + 2 for 1 ≤k ≤p and ik′ = 4k′ −12p
for 3p + 1 ≤k′ ≤4p −1 or ik = 4k −4p −1 for p + 1 ≤k ≤2p and ik′ = 12p −4k′ + 1
for 2p + 1 ≤k′ ≤3p or ik = 12p −4k + 1 for 2p + 1 ≤k ≤3p and ik′ = 4k′ −12p for
3p + 1 ≤k′ ≤4p −1. Taking these cases into account and reindexing, we have
−1
2
4p−2
X
k=1
4p−1
X
k′=k+1
1 + sgn(ik −ik′)
2
(σik −σik′)(nik −nik−1)(nik′ −nik′−1)
= −
p
X
k=1
2p−k
X
k′=p+1
(nik −nik−1)(nik′ −nik′−1) −
p
X
k=1
4p−k
X
k′=3p+1
(nik −nik−1)(nik′ −nik′−1)
+
2p
X
k=p+1
3p
X
k′=4p−k+1
(nik −nik−1)(nik′ −nik′−1) −
3p
X
k=2p+1
6p−k
X
k′=3p+1
(nik −nik−1)(nik′ −nik′−1)
= −
p
X
j=1
j
X
j′=2
(n4j−2 −n4j−3)(n4j′−5 −n4j′−6) −
p
X
j=1
j
X
j′=2
(n4j−2 −n4j−3)(n4j′−4 −n4j′−5)
