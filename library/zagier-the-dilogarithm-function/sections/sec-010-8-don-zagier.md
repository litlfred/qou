---
doc_id: zagier-the-dilogarithm-function
doc_title: "The dilogarithm function"
section_id: sec-010-8-don-zagier
section_title: "Don Zagier"
section_number: 8
pages: 6-6
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
The quantitative interpretation turned out as follows [9] : The diﬀerence
between the left and right sides of Ramanujan’s equation isO
(
exp
(π2/5
log q
))
for
x =1 ,q→ 1. (The proof of this used the identities
1
1+ q
1+ q2
1+ q3
1+ ···
=
∞∏
n=1
(
1−qn)( n
5 )
=
∑(−1)rq
5r2+3r
2
∑(−1)rq
5r2+r
2
,
which are consequences of the Rogers-Ramanujan identities and are surely
among the most beautiful formulas in mathematics.) For x→ 0a n dq → 1
the diﬀerence in question is O
(
exp
(π2/4
log q
))
,a n df o r0<x< 1a n dq→ 1i t
isO
(
exp
(c(x)
logq
))
wherec′(x)= −1
x arg sinhx
2 =−1
x log
(√
1+x 2/4+x/ 2
)
.
For these three formulas to be compatible, one needs
∫1
0
1
x log(
√
1+ x2/4+ x/2)dx =c(0)−c(1) = π2
4 − π2
5 = π2
20 .
Using integration by parts and formula A.3.1 (6) of [4] one ﬁnds
∫1
x log
(√
1+ x2/4+ x/2
)
dx =−1
2 Li2
((√
1+ x2/4− x/2
)2)
−1
2 log2(
√
1+ x2/4+ x/2) + (logx) log(
√
1+x 2/4+ x/2) +C,
so
∫1
0
1
x log(
√
1+x 2/4+ x/2)dx = 1
