---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
LetK be a knot and JN(K;q) be the usual Nth colored Jones polynomial, normalized to be
1 for the unknot. It is often useful to determine a q-hypergeometric expression for JN(K;q),
and such expressions have been computed for a variety of knots (e.g., [13, 14, 15, 21, 24, 30]).
These have applications to the AJ conjecture [14], the generalized Volume conjecture [11, 16],
the computation of WRT invariants [3, 17] and quantum modular and mock modular forms
[6, 9, 18, 19, 32].
Consider the family of double twist knots K(m,p), where 2 m and 2p are nonzero integers
denoting the number of half-twists in each respective region of Figure 1. Positive integers
correspond to right-handed half-twists and negative integers correspond to left-handed half-
twists.
Using ideas of Habiro [13] and Masbaum [24], Lauridsen [20, Section 6] gave the cyclotomic
expansion ofJN(K(m,p);q) for all nonzero m andp (cf. [7, 30]). For example, when m andp are
positive integers we have
JN(K(m,p);q) =
∑
n≥0
n=nm≥nm−1≥···≥n1≥0
n=sp≥sp−1≥···≥s1≥0
(q1+N)n(q1−N)nqn
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
(1.1)
Date: April 13, 2021.
2010 Mathematics Subject Classiﬁcation. 57M27.
Key words and phrases. double twist knots, colored Jones polynomial, duality.
1
2 JEREMY LOVEJOY AND ROBERT OSBURN
2m 
2p 
Figure 1. Double twist knots
and
JN(K(m,−p);q)
=
∑
n≥0
n=nm≥nm−1≥···≥n1≥0
n=sp≥sp−1≥···≥s1≥0
(q1+N)n(q1−N)n(−1)nq−(n+1
2 )
m−1∏
i=1
qn2
i +ni
[
ni+1
ni
]p−1∏
j=1
q−sj−sj+1sj
[
sj+1
sj
]
.
(1.2)
Here we have used the usual q-binomial coeﬃcient
[
n
k
]
=
[
n
k
]
q
:= (q)n
(q)n−k(q)k
(1.3)
with the standard q-hypergeometric notation
(a)n = (a;q)n :=
n−1∏
k=0
(1−aqk).
Recall that
JN(K;q−1) =JN(K∗;q), (1.4)
where K∗ denotes the mirror image of the knot K. Thus, since K(m,p) =K(p,m) and K(−m,−p)
is the mirror image of K(m,p), equations (1.1) and (1.2) cover all of the double twist knots, up
to a substitution of q byq−1.
In this paper, we use a result of Takata [28] to proveq-hypergeometric formulas for the colored
Jones polynomial of the double twist knots K(−m,−p) andK(−m,p) which are diﬀerent from those
corresponding to (1.1) and (1.2). To state the ﬁrst case, deﬁne the functions ϵi,j,m and γi,m by
ϵi,j,m =



1, if j≡−i or−i− 1 (mod 2 m),
−1, if j≡i or i− 1 (mod 2 m),
0, otherwise
(1.5)
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 3
where 1≤i<j ≤ 2mp− 1 with m ∤i and
γi,m =
{
1, if i≡ 1,...,m − 1 (mod 2 m),
−1 otherwise (1.6)
where 1≤i≤ 2mp− 2. Our ﬁrst main result is the following.
Theorem 1.1. For positive integers m and p, we have
JN(K(−m,−p);q)
=q1−N ∑
N−1≥n2mp−1≥···≥n1≥0
(q1−N)n2mp−1(−1)n2mp−1q−(
n2mp−1+1
2 ) ∏
1≤i<j≤2mp−1
m∤i
qϵi,j,mninj
×
2p−1∏
i=1
(−1)nmiq(−1)iNn mi+(nmi+1
2 )
2mp−2∏
i=1
q−nini+1+γi,mni
[
ni+1
ni
]
.
(1.7)
The case m = 1 of Theorem 1.1 was proved by Takata [28] 1. Here K(1,p) =Kp>0, the usual
pth twist knot. As K(−1,−p) is the mirror image of K(1,p), one recovers JN(K∗
p>0;q) by taking
m = 1 in (1.7) and simplifying. Namely, we have (cf. equation (15) in [28])
JN(K∗
p>0;q)
=q1−N ∑
N−1≥n2p−1≥···≥n1≥0
(q1−N)n2p−1q−Nn 2p−1
2p−2∏
i=1
(−1)niq(−1)iNn i+(ni
2 )−nini+1
[
ni+1
ni
]
.
(1.8)
For an example with m> 1, take m =p = 2. Then we have
JN(K(−2,−2);q)
=q1−N ∑
N−1≥n7≥n6≥n5≥n4≥n3≥n2≥n1≥0
(q1−N)n7(−1)n2+n4+n6+n7qN(−n2+n4−n6)
×q−(n7+1
2 )+(n6+1
2 )+(n4+1
2 )+(n2+1
2 )+n1(n3−n4−n5+n6+n7)+n3(n5−n6−n7)+n5n7
×q−n2n3−n4n5−n6n7+n1−n2−n3−n4+n5−n6
[
n7
n6
][
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
(1.9)
For the case of K(−m,p), deﬁne the functions ∆i,j,m and βi,m by
∆i,j,m =



1, if j≡−i or−i + 1 (mod 2 m),
−1, if j≡i or i + 1 (mod 2 m),
0, otherwise
(1.10)
1Note that Takata’s q-hypergeometric notation diﬀers slightly from the standard one we use here
