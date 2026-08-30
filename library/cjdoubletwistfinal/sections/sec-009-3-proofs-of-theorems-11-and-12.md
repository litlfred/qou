---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-009-3-proofs-of-theorems-11-and-12
section_title: "Proofs of Theorems 1.1 and 1.2"
section_number: 3
pages: 12-14
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
Proof of Theorem 1.1. As (1.7) reduces to (1.8) when m = 1 and this case was proven in [28],
we assume m ≥ 2. Using Lemmas 2.2 and 2.3, one can check that for l = 4mp− 1 and
t = 4mp− 2p− 1
a(n) =
2p−1∑
j=1
(−1)jnmj− 1 (3.1)
and b1(n) +b2(n) equals
1 +n2mp−1 +
p∑
j=1
(m−1∑
i=1
n2mj−2m+i−
2m−1∑
i=m
n2mj−2m+i
)
+
p∑
j=1
j∑
j′=1
m−1∑
k=1
k∑
k′=1
(n2mj−k−n2mj−k−1)(n2mj′−2m+k−k′+1−n2mj′−2m+k−k′)
−
p∑
j=1
j∑
j′=1
m∑
k=1
m−k+1∑
k′=1
(n2mj−m−k+1−n2mj−m−k)(n2mj′−2m−k′+1−n2mj′−2m−k′)
+
m−1∑
s=1
p∑
j=1
(j−1∑
j′=1
(n2mj′−s−n2mj′−2m+s) +
p∑
j′=j
(n2mj′−s−n2mj′−2m+s−1)
)
n2mj−2m+s−1
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 13
+
p∑
j=1
( p∑
j′=j
(n2mj′−m−n2mj′−m−1)
)
n2mj−m−1
−
p−1∑
j=1
( p∑
j′=j+1
(n2mj′−1−n2mj′−2m) +n2mj
)
n2mj−1
−
m−1∑
s=1
p∑
j=1
( j∑
j′=1
(n2mj′−m+s−n2mj′−m−s) +
p∑
j′=j+1
(n2mj′−m+s−1−n2mj′−m−s)
)
n2mj−m+s−1.
(3.2)
Also, by (2.1) and (2.2)
X(n) = (−1)n2mp−1q−Nn 2mp−1 (q)N−1(q)n2mp−1
(q)N−n2mp−1−1
×
p∏
j=1
(−1)n2mj−1−n2mj−mq
1
2
m∑
s=1
(n2mj−2m+s−n2mj−2m+s−1)(n2mj−2m+s−n2mj−2m+s−1+1)
2m−1∏
s=1
(q)n2mj−2m+s−n2mj−2m+s−1
×
p−1∏
j=1
(−1)n2mj−n2mj−1
(q)n2mj−n2mj−1
.
(3.3)
Upon comparing (2.3) and (3.1)–(3.3) with (1.7) and then simplifying, it suﬃces to prove that
for m≥ 2
p∑
j=1
j∑
j′=1
m−1∑
k=1
k∑
k′=1
(n2mj−k−n2mj−k−1)(n2mj′−2m+k−k′+1−n2mj′−2m+k−k′)
−
p∑
j=1
j∑
j′=1
m∑
k=1
m−k+1∑
k′=1
(n2mj−m−k+1−n2mj−m−k)(n2mj′−2m−k′+1−n2mj′−2m−k′)
+
m−1∑
s=1
p∑
j=1
(j−1∑
j′=1
(n2mj′−s−n2mj′−2m+s) +
p∑
j′=j
(n2mj′−s−n2mj′−2m+s−1)
)
n2mj−2m+s−1
+
p∑
j=1
( p∑
j′=j
(n2mj′−m−n2mj′−m−1)
)
n2mj−m−1
−
p−1∑
j=1
( p∑
j′=j+1
(n2mj′−1−n2mj′−2m) +n2mj
)
n2mj−1
