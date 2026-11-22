---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
4
JEREMY LOVEJOY AND ROBERT OSBURN
where 1 ≤i < j ≤2mp with m ∤i and
βi,m =





1,
if i ≡1, . . . , m −1
(mod 2m),
−1
if i ≡m + 1, . . . , 2m −1
(mod 2m),
0,
otherwise
(1.11)
where 1 ≤i ≤2mp −1. Our second main result is the following.
Theorem 1.2. For positive integers m and p, we have
JN(K(−m,p); q)
=
X
N−1≥n2mp≥···≥n1≥0
(q1−N)n2mp(−1)n2mpq−(
n2mp+1
2
)
Y
1≤i<j≤2mp
m∤i
q∆i,j,mninj
×
2p−1
Y
i=1
(−1)nmiq(−1)i+1Nnmi+(nmi+1
2
)
2mp−1
Y
i=1
qβi,mni

ni+1
ni

.
(1.12)
Again, the case m = 1 was established by Takata [28]. As K(1,−p) = Kp<0 and K(−1,p) is the
mirror image of K(1,−p), one recovers JN(K∗
p<0; q) by taking m = 1 in (1.12) and simplifying.
Namely, we have (cf. equation (14) in [28])
JN(K∗
p<0; q)
=
X
N−1≥n2p≥···≥n1≥0
(q1−N)n2p(−1)n2pq−(
n2p+1
2
)
2p−1
Y
i=1
(−1)niq(−1)i+1Nni+(ni+1
2 )

ni+1
ni

. (1.13)
For an example with m > 1, take m = 3 and p = 1. Then we have
JN(K(−3,1); q)
=
X
N−1≥n6≥n5≥n4≥n3≥n2≥n1≥0
(q1−N)n6(−1)n3+n6qNn3−(n6+1
2 )+(n3+1
2 )
× qn1(−n2+n5+n6)+n2(−n3+n4+n5)−n4n5−n5n6
× qn1+n2−n4−n5

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
(1.14)
Motivated by the expressions in (1.7) and (1.1), we deﬁne the q-series Fm,p(q) and Um,p(x; q)
by
Fm,p(q) = q
X
n2mp−1≥···≥n1≥0
(q)n2mp−1(−1)n2mp−1q−(
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
(−1)nmiq(nmi+1
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
(1.15)
