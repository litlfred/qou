---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-002-4-jeremy-lovejoy-and-robert-osburn
section_title: "JEREMY LOVEJOY AND ROBERT OSBURN"
section_number: 4
pages: 4-6
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
where 1≤i<j ≤ 2mp with m ∤i and
βi,m =



1, if i≡ 1,...,m − 1 (mod 2 m),
−1 if i≡m + 1,..., 2m− 1 (mod 2 m),
0, otherwise
(1.11)
where 1≤i≤ 2mp− 1. Our second main result is the following.
Theorem 1.2. For positive integers m and p, we have
JN(K(−m,p);q)
=
∑
N−1≥n2mp≥···≥n1≥0
(q1−N)n2mp(−1)n2mpq−(
n2mp+1
2 ) ∏
1≤i<j≤2mp
m∤i
q∆i,j,mninj
×
2p−1∏
i=1
(−1)nmiq(−1)i+1Nn mi+(nmi+1
2 )
2mp−1∏
i=1
qβi,mni
[
ni+1
ni
]
.
(1.12)
Again, the case m = 1 was established by Takata [28]. As K(1,−p) =Kp<0 and K(−1,p) is the
mirror image of K(1,−p), one recovers JN(K∗
p<0;q) by taking m = 1 in (1.12) and simplifying.
Namely, we have (cf. equation (14) in [28])
JN(K∗
p<0;q)
=
∑
N−1≥n2p≥···≥n1≥0
(q1−N)n2p(−1)n2pq−(
n2p+1
2 )
2p−1∏
i=1
(−1)niq(−1)i+1Nn i+(ni+1
2 )
[
ni+1
ni
]
. (1.13)
For an example with m> 1, take m = 3 and p = 1. Then we have
JN(K(−3,1);q)
=
∑
N−1≥n6≥n5≥n4≥n3≥n2≥n1≥0
(q1−N)n6(−1)n3+n6qNn 3−(n6+1
2 )+(n3+1
2 )
×qn1(−n2+n5+n6)+n2(−n3+n4+n5)−n4n5−n5n6
×qn1+n2−n4−n5
[
n6
n5
][
n5
n4
][
n4
n3
][
n3
n2
][
n2
n1
]
.
(1.14)
Motivated by the expressions in (1.7) and (1.1), we deﬁne the q-seriesFm,p(q) and Um,p(x;q)
by
Fm,p(q) =q
∑
n2mp−1≥···≥n1≥0
(q)n2mp−1(−1)n2mp−1q−(
n2mp−1+1
2 ) ∏
1≤i<j≤2mp−1
m∤i
qϵi,j,mninj
×
2p−1∏
i=1
(−1)nmiq(nmi+1
2 )
2mp−2∏
i=1
q−nini+1+γi,mni
[
ni+1
ni
] (1.15)
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 5
and
Um,p(x;q) =
∑
n≥0
n=nm≥nm−1≥···≥n1≥0
n=sp≥sp−1≥···≥s1≥0
(−xq)n(−x−1q)nqn
m−1∏
i=1
qn2
i +ni
[
ni+1
ni
]p−1∏
j=1
qs2
j+sj
[
sj+1
sj
]
.
(1.16)
Note that if ζN is any Nth root of unity, we have
Fm,p(ζN) =JN(K(−m,−p);ζN) (1.17)
and
Um,p(−1;ζN) =JN(K(m,p);ζN). (1.18)
The base case F1,1(q) is q times the Kontsevich-Zagier series,
F (q) :=
∑
n≥0
(q)n, (1.19)
one of the foundational examples of Zagier’s quantum modular forms [31, 32], while
U1,1(x;q) =q−1U(x;q), (1.20)
where U(x;q) is the generating function for strongly unimodal sequences [4],
U(x;q) :=
∞∑
n=0
(−xq)n(−x−1q)nqn+1. (1.21)
For this reason, we call the seriesFm,p(q) the generalized Kontsevich-Zagier functions for double
twist knots and the Um,p(x;q) the generalized U-functions for double twist knots . Note that
whileUm,p(x;q) is well-deﬁned for|q|< 1 and forq a root of unity whenx =−1, the generalized
Kontsevich-Zagier functions Fm,p(q) are only deﬁned at roots of unity.
The original Kontsevich-Zagier seriesF (q) and the generating function for strongly unimodal
sequences U(x;q) when x =−1 are dual at roots of unity via
F (ζ−1
N ) =U(−1;ζN). (1.22)
This was ﬁrst shown by Bryson, Ono, Pitman and Rhoades [4]. It also follows at once from
(1.4) and the case m =p = 1 of (1.17) and (1.18), which was ﬁrst observed in [18]. Using (1.4)
and the general case of (1.17) and (1.18), we immediately have the following generalization of
(1.22).
Corollary 1.3. If ζN is any Nth root of unity, then we have
Fm,p(ζN) =Um,p(−1;ζ−1
N ). (1.23)
Next we turn our attention to (1.12) and (1.2). Motivated by these expressions, we deﬁne
Fm,p(q) andUm,p(x;q) by
Fm,p(q) =
∑
n2mp≥···≥n1≥0
(q)n2mp(−1)n2mpq−(
n2mp+1
2 ) ∏
1≤i<j≤2mp
m∤i
q∆i,j,mninj
×
2p−1∏
i=1
(−1)nmiq(nmi+1
2 )
2mp−1∏
i=1
qβi,mni
[
ni+1
ni
] (1.24)
