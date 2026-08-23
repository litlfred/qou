---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-010-32-minima-and-maxima
section_title: "Minima and maxima"
section_number: 3.2
pages: 16-18
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
In order to involve the number of minima and the number of maxima in the Gog-
trapezoids, we have to apply the version of Corollary 6 where the requirement on b1, b2,
...,  bn is only that it is weakly increasing, and thus we cannot involve the inversion 
numbers at the same time.
An (m, n, k)-Gog trapezoids with p minima can be identiﬁed with (s, t)-trees of or-
der n, where s =( p − 1), t =( 0, 1, ...,  n − k − 1) and where the bottommost entry of 
the ﬁrst NE-diagonal is set to 2. In order to see this, delete in the (m, n, k)-Gog trape-
zoids with p minima the occurrences of 1 except for the topmost which is replaced by 2. 
In order to obtain a formula for the number we have to multiply (3.1)b y (−x1)p−1 and 
set b1 =2 . We obtain
(−1)p−1(1 + x1)2xp−n
1
k∏
i=2
(1 + xi)bi x−n+1
i
n∏
i=k+1
(1 + xi)m+k+1x−n+i−k
i
×
∏
1≤i<j≤n
(xi − xj)(1 + xj + xixj). (3.2)
The case p =0i s  not covered by this formula. In that case, we use (3.1)w i t h the 
appropriate b1 > 1.
Now let M ⊆{ k +1 , ...,  n} and suppose we require to have a maximum in the i-th 
SE-diagonal precisely if i ∈ M (and possibly in the k-th SE-diagonal, in which case we 
have bk = m + k). Then we need to multiply (3.2)b y
∏
i∈M
xi
1+ xi
∏
i∈{k+1,k+2,...,n}\M
1
1+ xi
.
If we sum over all subsets M with cardinality q, we obtain
n∏
i=k+1
1
1+ xi
eq (xk+1,...,x n) ,
where eq denotes the q-th elementary symmetric function. As eq(xk+1, ...,  xn)i s  the 
coeﬃcient of Qq in 
n∏
i=k+1
(1 + Qxi), we obtain the following theorem.
Theorem 9. The generating function of (m, n, k)-Gog trapezoids with bottom row 
1, b2, ...,  bk w.r.t. the weight
P #of minima Q#of maxima not including bk
is the constant term of
576 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
P(1 + Px 1)−1(1 + x1)2x−n+1
1
k∏
i=2
(1 + xi)bi x−n+1
i
n∏
i=k+1
(1 + Qxi)( 1+ xi)m+kx−n+i−k
i
×
∏
1≤i<j≤n
(xi − xj)(1 + xj + xixj) (3.3)
in x1, ...,  xn, while the generating function of (m, n, k)-Gog trapezoids with bottom row 
b1, b2, ...,  bk w.r.t. the weight
Q#of maxima not including bk
is the constant term of
k∏
i=1
(1 + xi)bi x−n+1
i
n∏
i=k+1
(1 + Qxi)( 1+ xi)m+kx−n+i−k
i
×
∏
1≤i<j≤n
(xi − xj)(1 + xj + xixj) (3.4)
in x1, ...,  xn.
The generating functions in Theorems 8 and 9 can be restricted further to Gog trape-
zoids with ﬁxed top entry by multiplying with the Laurent series provided in Theorem 4.
In case m =0 , there is always a minimum and the bottom row is forced. Also note 
that the last entry of the bottom row is a maximum in this case.
Corollary 10. The generating function of (0, n, k)-Gog trapezoids w.r.t. the number of 
minima and maxima is the constant term of
PQ(1 + Px 1)−1(1 + x1)2x−n+1
1
k∏
i=2
(1 + xi)ix−n+1
i
n∏
i=k+1
(1 + Qxi)( 1+ xi)m+kx−n+i−k
i
×
∏
1≤i<j≤n
(xi − xj)(1 + xj + xixj).
In order to obtain the number of all (m, n, k)-Gog trapezoids with p minima and q
maxima also if m ⁄=0 ,  one has to sum over all possible bottom rows and take into 
account whether the rightmost entry in the bottom row is a maximum. In the expres-
sions in Theorem 9, the bottom row appears only through the factors 
k∏
i=2
(1 + xi)bi and 
k∏
i=1
(1 + xi)bi , respectively.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 577
