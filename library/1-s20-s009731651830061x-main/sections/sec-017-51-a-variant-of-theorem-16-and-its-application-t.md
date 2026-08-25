---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-017-51-a-variant-of-theorem-16-and-its-application-t
section_title: "A variant of Theorem 16 and its application to (2.3) and to (2.6) when bi=i"
section_number: 5.1
pages: 34-38
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
Next we state a theorem that is similar to Theorem 16 and that can be proven 
analogously.
Theorem 17. Let hq(w, y) = qw − q−1y. Then the antisymmetrizer of
∏
1≤i<j≤n hq(wi,w j)∏
1≤i≤j≤n h1(wj,y i)∏
1≤j≤i≤n hq(wj,y i) (5.6)
w.r.t. w1, ...,  wn is
det1≤i,j≤n
(
1
h1 (wi,yj )hq (wi,yj )
)
∏
1≤i<j≤n h1(yj,y i) .
Proof. The proof is by induction w.r.t. n. The case n =1i s  easy to check.
Let A(w1, ...,  wn; y1, ...,  yn)d e n o t e the antisymmetrizer of (5.6). We have the fol-
lowing recursion for A(w1, ...,  wn; y1, ...,  yn).
A(w1,...,w n; y1,...,y n)
=
n∑
k=1
(−1)k+n
∏
1≤i≤n,i⁄=k
hq(wi,w k)
n∏
i=1
h1(wk,y i)hq(wi,y n)
A(w1,..., ˆwk,...,w n; y1,...,y n−1)
By the induction hypothesis, the right-hand side is equal to
n∑
k=1
(−1)k+n det
1≤i≤n,i⁄=k
1≤j≤n−1
( 1
h1(wi,y j)hq(wi,y j)
)
∏
1≤i≤n,i⁄=k
hq(wi,w k) ∏
1≤i≤n−1
h1(yn,y i)
n∏
i=1
h1(wk,y i)hq(wi,y n) ∏
1≤i<j≤n
h1(yj,y n)
.
(5.7)
We deﬁne
gl(w1,...,w n; y1,...,y n)=
∏
1≤i≤n−1,i⁄=l
h1(yi,y n)
h1(yl,y i)
n∏
i=1
hq(wi,y l)
hq(wi,y n)
and claim that
594 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
n∑
l=1
gl(w1,...,w n; y1,...,y n) 1
h1(wk,y l)hq(wk,y l)
=
∏
1≤i≤n,i⁄=k
hq(wi,w k) ∏
1≤i≤n−1
h1(yi,y n)
∏
1≤i≤n
h1(wk,y i)hq(wi,y n) . (5.8)
Assuming (5.8)i s  true, we can replace in (5.7)t h e expression on the right-hand side 
of (5.8)b y the left-hand side of (5.8). We change the order of summation and obtain
(−1)n−1 ∏
1≤i<j≤n
h1(yj,y i)−1
n∑
l=1
gl det
1≤i,j≤n
( 1
h1(wi,y j)hq(wi,y j)
)⏐⏐⏐
⏐
yn =yl
and the last expression is equal to the expression in the theorem. In order to prove (5.8), 
we rearrange the identity and obtain
n∑
l=1
∏
1≤i≤n−1
i⁄=l
h1(yi,y n)
h1(yl,y i)
∏
1≤i≤n
i⁄=k
hq(wi,y l)
∏
1≤i≤n
i⁄=l
h1(wk,y i)
=
∏
1≤i≤n,i⁄=k
hq(wi,w k)
∏
1≤i≤n−1
h1(yi,y n).
We consider both sides as polynomials in wk. The degree is in both cases not greater than 
n − 1a n d so it suﬃces to show that they agree at the evaluations wk = yp, 1 ≤ p ≤ n. 
In this case, each summand on the left-hand side vanishes except for the summand 
corresponding to l = p. 2
Note that the statement of this theorems diﬀers from the statement of Theorem 16 only 
in so far that we set hq(w, y) = qw −q−1y instead of hq(w, y) =( qw −q−1y)(qwy −q−1).
Before we apply this theorem, we mention another formula that will be useful in the 
following. The formula appeared in [1, Eqs. (43)–(47)]. Suppose f(x, y)i s a power series 
in x and y, then
lim
(x1,...,xn)→(x,...,x)
(y1,...,yn)→(y,...,y)
det
1≤i,j≤n
(f(xi,y j))
∏
1≤i<j≤n
(xj − xi)(yj − yi) =d e t
0≤i,j≤n−1
(
[uivj]f(x + u, y + v)
)
, (5.9)
where [uivj]f(x +u, y+v) denotes the coeﬃcient of uivj in f(x +u, y+v). A close relative 
of this formula is the following: Suppose fj(x)i s a power series in x for 1 ≤ j ≤ n, then
lim
(x1,...,xn)→(x,...,x)
det
1≤i,j≤n
(fj(xi))
∏
1≤i<j≤n
(xj − xi) =d e t
0≤i≤n−1
1≤j≤n
(
[ui]fj(x + u)
)
. (5.10)
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 595
We compute the symmetrizer of (2.3): We set wi =( xi +1  + q−1)/(xi +1  + q)i n (5.6)
and obtain
(
q − q−1)(n
2
) ∏
1≤i<j≤n
(q−1 +2+q +( q−1 +1+ q)xi + xj + xixj)
×
n∏
i=1
(1 + q + xi)2
⎛
⎝
n∏
i=1
i∏
j=1
(
xi(1 − yj)+( 1+q −1)(1 − qyj)
)
×
n∏
j=i
(
xi(q − q−1yj)+( 1+q )(1 − yjq−1)
)
⎞
⎠
−1
.
By setting yi =1 , q = e2iπ/3 and applying Theorem 17, we obtain
ASx1,...,xn
⎡
⎣ ∏
1≤i<j≤n
(1 + xj + xixj)
n∏
i=1
(1 + xi)ix−n+1
i
⎤
⎦
=( −1)
(n+1
2
)
qn(q − q−1)(n+3)n/2
n∏
i=1
(1 + xi)n+1x−n+1
i (1 + q + xi)−2
× lim
(y1,...,yn )→1
det
1≤i,j≤n
⎛
⎝ 1
(
yj − xi+1+q−1
xi+1+q
)(
yj − q2 xi+1+q−1
xi+1+q
)
⎞
⎠ ∏
1≤i<j≤n
(yj − yi)−1.
(5.11)
We use the following partial fraction decomposition
1
(y − a)(y − b) = 1
a − b
( 1
y − a − 1
y − b
)
to rewrite the matrix entry of the determinant. We obtain
(−1)
(n
2
)
(q − q−1)
(n+1
2
) n∏
i=1
(1 + xi)n+1x−n+1
i (xi +1+q )−1(xi +1+ q−1)−1
× lim
(y1,...,yn )→1
det
1≤i,j≤n
⎛
⎝ 1
(
yj − xi+1+q−1
xi+1+q
)− 1(
yj − q2 xi+1+q−1
xi+1+q
)
⎞
⎠ ∏
1≤i<j≤n
(yj − yi)−1
(5.12)
for the right-hand side. Now we can apply (5.10)t o obtain the following.
n∏
i=1
(1 + xi)n+1x−n+1
i (xi +1+q −1)−1 det
1≤i,j≤n
(
(xi +1+ q)j−1(
1 − (−1 − xi)−jq−j))
596 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
Alternatively, we can also use the Cauchy determinant.
det
1≤i,j≤n
( 1
xi + yj
)
=
∏
1≤i<j≤n(xj − xi)(yj − yi)∏n
i,j=1(xi + yj)
The determinant in (5.12)c a n be written as a sum of 2n Cauchy determinants.
det
1≤i,j≤n
⎛
⎝ 1(
yj − xi+1+q−1
xi+1+q
)− 1(
yj − q2 xi+1+q−1
xi+1+q
)
⎞
⎠
=
∑
(s1,...,sn)∈{0,1}n
det
1≤i,j≤n
⎛
⎝(−1)
si 1(
yj − q2si xi+1+q−1
xi+1+q
)
⎞
⎠
In a similar situation, namely the proof of the equality of the constant terms of (5.1)
and (5.2), only one of these Cauchy determinants contributes to the constant term. This 
is not true here, which is mainly due to the factor 
n∏
i=1
x−n+1
i in (2.3). However, it is 
still possible to get rid of the extra set of variables y1, ...,  yn and it follows that the 
right-hand side is equal to
n∏
i=1
(1 + xi)n+1x−n+1
i (xi +1+ q−1)−1
×
∑
(s1,...,sn)∈{0,1}n
(−1)(n−1)(s1+...+sn)+
(n
2
)
q−s1−...−sn
n∏
i=1
(1 + xi)−nsi
×
∏
1≤i<j≤n
((1 + xixj)(si − sj)+ xi(1 − si − 2sj +3 sisj)+ xj(−1+ sj +2 si − 3sisj)) ,
and this can also be written as follows.
n∏
i=1
(1 + xi)n+1x−n+1
i (xi +1+ q−1)−1 det
1≤i,j≤n
(
xj−1
i − (−1 − xi)−jq−1
)
As for computing the symmetrizer of (2.6)w h e n bi = i, we set wi =( xiq−1 − 1)/
(xiq − 1) in (5.6)a n d obtain
(q − q−1)
(n
2
) ∏
1≤i<j≤n
(1 − (q + q−1)xj + xixj)
n∏
i=1
(qxi − 1)2
×
⎛
⎝
i∏
j=1
(−1+ yj + xi(q−1 − qyj))
n∏
j=i
(−q + yjq−1 + xi(1 − yj))
⎞
⎠
−1
(5.13)
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 597
Furthermore, we set yi =1a n d q = eiπ/3, and Theorem 17 now implies in a similar way 
as above
ASx1,...,xn
⎡
⎣ ∏
1≤i<j≤n
(1 − xj + xixj)
n∏
i=1
(1 − xi)−nx−n+1−i
i
⎤
⎦ =
(−1)
n(q − q−1)(n+1)n/2
n∏
i=1
(1 − xi)−nx−n+1
i (qxi − 1)−1(q−1xi − 1)−1
× lim
(y1,...,yn )→1
det
1≤i,j≤n
⎛
⎝ 1
(
yj − xiq−1−1
xiq−1
)− 1(
yj − q2 xiq−1−1
xiq−1
)
⎞
⎠ ∏
1≤i<j≤n
(yj − yi)−1.
Using (5.10), we obtain
n∏
i=1
(1 − xi)−nx−n+1
i (q−1xi − 1)−1 det
1≤i,j≤n
(
(1 − xiq)j−1
(
q−j − x−j
i
))
.
Alternatively, we can also use the approach from above involving the Cauchy determinant 
and obtain
n∏
i=1
(1 − xi)−nx−n+1
i (q−1xi − 1)−1
×
∑
(s1,...,sn)∈{0,1}n
(−q)−s1−...−sn (−1)
(s1+...+sn
2
)
+
(n−s1−...−sn
2
)
+n
n∏
i=1
xn(si−1)
i
×
∏
1≤i<j≤n
((1 + xixj)(si − sj)+ xi(−1+ si +2 sj − 3sisj)
+ xj(1 − sj − 2si +3 sisj)) .
This can also be written as
n∏
i=1
(1 − xi)−nx−n+1
i (q−1xi − 1)−1 det
1≤i,j≤n
(
−x−j
i +( 1 − xi)j−1q−1
)
.
