---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-023-22-anatol-n-kirillov
section_title: "Anatol N. Kirillov"
section_number: 22
pages: 22-24
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
L
(1
2
)
+L
(1−x
1 +x
)
=L
( 1−x
2(1 +x)
)
+L(x(1−x))−L(x(1 +x)) +L(1),
L
(1
2
)
+L
( 1
1 +x
)
=L
( 1
2(1 +x)
)
+L
( 1
1 + 2x
)
+L
( x
1 + 2x
)
,
L(x(1−x)) +L
((1−x
2x
)2)
+L
(1
4
)
=L(1), (1.25)
L
( 1
1 +x
)
+L
( 1 +x
1 + 2x
)
=L
( 1
1 + 2x
)
+L
( 1
2(1 +x)
)
+L
(1
2
)
,
L
((1−x
2x
)2)
= 2L
(1−x
2x
)
− 2L
(1−x
1 +x
)
. (1.26)
Using these identities one can ﬁnd
L(x6) = 2L(x3) + 2L(x2) + 2L(x(1−x))− 2L
( x
1 +x
)
− 2L
(1
4
)
,
L(x3) = 2L(x2) + 3L(x) +L
( x
1 +x
)
+L(x(1−x))−L
(1−x
1 +x
)
−L
( 1
2(1 +x)
)
− 3
2L(1).
Consequently,
LHS(1.23) =−2L(x(1−x))− 2L
(1
4
)
+ 4L
(1−x
1 +x
)
+ 4L
( 1
2(1 +x)
)
+ 6L(1).
Using the relations (1.25) and (1.26) one can rewrite the las t expression as
LHS(1.23) = 4L(1) + 4
{
L
(1−x
2x
)
+L
( 1
2(1 +x)
)}
.
But it follows from the equation 3 x2 +x = 1, that
1−x
2x + 1
2(1 +x) = 1.
The proof of the Browkin ﬁrst dilogarithm relation is over.
Now let us prove the second Browkin’s identity. Having in min d an observation that
z = x
1−x , one can rewrite the LHS of (1.24) in the following form (hint : 1 +z +z2 = 4x2)
−6L
( x
1−x
)
+ 14L(x) +L
(1
4
)
+L
( 1
4x
)
− 2L
( x3
1− 3x + 3x2
)
. (1.27)
Dilogarithm identities 23
In order to prove that the expression (1.27) is equal to 2 L(1), we are going to use the
relations
x3
1− 3x + 3x2 = x(1 +x)
2 , 3x− 1 = x
1 +x, (2− 3x)x = 3x− 1,
1− 2x = (3x− 1)x, (2 +x)x2 = (1−x)(1−x2), 1
1 + 2x = x
1−x2,
which are a direct consequence of the quadratic equation for x, namely, 3x2 +x− 1 = 0,
and, additionally, the following identities which can be ob tained immediately from the
functional equation (1.4)
2L
(x(1 +x)
2
)
+ 2L
(1 +x
2 +x
)
+ 2L
( x
2 +x
)
− 2L(x)− 2L
(1 +x
2
)
= 0,
2L
(1
2
)
+ 2L(1−x)− 2L
(1−x
1 +x
)
− 2L
( x
1 +x
)
− 2L
(1−x
2
)
= 0,
4L
( x
1−x
)
− 4L(x)− 2L
(1 +x
2 +x
)
= 0, (hint : 1 +x
2 +x =
( x
1−x
)2
),
L
(4x− 1
4x
)
− 2L
(1−x
2x
)
+ 2L
(1−x
1 +x
)
= 0, (hint : 4x− 1
4x =
(x− 1
2x
)2
),
2L
( x
1−x
)
+ 2L
(1−x
2x
)
− 2L
(1
2
)
− 2L
( x
1 +x
)
− 2L
(3x− 1
1−x
)
= 0,
2L(1−x2) + 2L
( x
1−x2
)
− 2L(x)− 2L
( x
2 +x
)
− 2L
(2
3
)
= 0.
Taking the sum of these, simplifying and using the relation x
1−x2 = 3x− 1
1−x , one can ﬁnd
4L(x)− 4L
( x
1 +x
)
+ 2L(1−x2) +L
(1
4
)
− 2L
(2
3
)
+L(1).
The last expression can be simpliﬁed by using the duplicatio n formula (1.7). The result is
2L
(1
2
)
+L(1) = 2L(1), as it was claimed.
1.3. Dilogarithm identities and conformal weights.
Let us consider the following dilogarithm sum
n−1∑
k=1
r∑
m=1
L
( sinkϕ· sin(n−k)ϕ
sin(m +k)ϕ· sin(m +n−k)ϕ
)
:= π2
6 s(j,n,r ),
where ϕ = (j + 1)π
n +r , 0≤ 2j≤n +r− 2 and g.c.d. ( j + 1, n+r) = 1.
