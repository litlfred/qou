---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS
3
where 1 ≤i < j ≤2mp −1 with m ∤i and
γi,m =
(
1,
if i ≡1, . . . , m −1
(mod 2m),
−1
otherwise
(1.6)
where 1 ≤i ≤2mp −2. Our ﬁrst main result is the following.
Theorem 1.1. For positive integers m and p, we have
JN(K(−m,−p); q)
= q1−N
X
N−1≥n2mp−1≥···≥n1≥0
(q1−N)n2mp−1(−1)n2mp−1q−(
n2mp−1+1
2
)
Y
1≤i<j≤2mp−1
m∤i
qϵi,j,mninj
×
2p−1
Y
i=1
(−1)nmiq(−1)iNnmi+(nmi+1
2
)
2mp−2
Y
i=1
q−nini+1+γi,mni

ni+1
ni

.
(1.7)
The case m = 1 of Theorem 1.1 was proved by Takata [28]1. Here K(1,p) = Kp>0, the usual
pth twist knot. As K(−1,−p) is the mirror image of K(1,p), one recovers JN(K∗
p>0; q) by taking
m = 1 in (1.7) and simplifying. Namely, we have (cf. equation (15) in [28])
JN(K∗
p>0; q)
= q1−N
X
N−1≥n2p−1≥···≥n1≥0
(q1−N)n2p−1q−Nn2p−1
2p−2
Y
i=1
(−1)niq(−1)iNni+(ni
2 )−nini+1

ni+1
ni

.
(1.8)
For an example with m > 1, take m = p = 2. Then we have
JN(K(−2,−2); q)
= q1−N
X
N−1≥n7≥n6≥n5≥n4≥n3≥n2≥n1≥0
(q1−N)n7(−1)n2+n4+n6+n7qN(−n2+n4−n6)
× q−(n7+1
2 )+(n6+1
2 )+(n4+1
2 )+(n2+1
2 )+n1(n3−n4−n5+n6+n7)+n3(n5−n6−n7)+n5n7
× q−n2n3−n4n5−n6n7+n1−n2−n3−n4+n5−n6

n7
n6
 
n6
n5
 
n5
n4
 
n4
n3
 
n3
n2
 
n2
n1

.
(1.9)
For the case of K(−m,p), deﬁne the functions ∆i,j,m and βi,m by
∆i,j,m =





1,
if j ≡−i or −i + 1
(mod 2m),
−1,
if j ≡i or i + 1
(mod 2m),
0,
otherwise
(1.10)
1Note that Takata’s q-hypergeometric notation diﬀers slightly from the standard one we use here
