---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Journal of Combinatorial Theory, Series A 158 (2018) 560–604 Contents lists available at ScienceDirect Journal of Combinatorial Theory, Series A www.elsevier.com/locate/jcta Consta"
section_id: sec-018-52-the-application-of-theorem-17-to-28-when-bii
section_title: "The application of Theorem 17 to (2.8) when bi=i"
section_number: 5.2
pages: 38-41
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
The expression in (2.8)i s more complicated at ﬁrst glance as it already involves the 
antisymmetrizer operator. However, as our approach involves the computation of the 
antisymmetrizer anyway, this is no disadvantage.
598 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
By (5.11), (2.8)i s equal to
(−1)
(n+1
2
)
qn(q − q−1)(n+3)n/2
n∏
i=1
(1 + xi)n+1(1 + q + xi)−2
× lim
(y1,...,yn )→1
det
1≤i,j≤n
⎛
⎝ 1(
yj − xi+1+q−1
xi+1+q
)(
yj − q2 xi+1+q−1
xi+1+q
)
⎞
⎠
×
∏
1≤i<j≤n
(xj − xi)−1(yj − yi)−1, (5.14)
where q = e2πi/3. The same procedure as above can be used to show that this is equal 
to
n∏
i=1
(1 + xi)n+1(xi +1+ q−1)−1
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
(1 + xixj)(si − sj)+x i(1 − si − 2sj +3 sisj)+ xj(−1+ sj +2 si − 3sisj)
xj − xi
=
n∏
i=1
(1 + xi)n+1(xi +1+q −1)−1 det
1≤i,j≤n
(
xj−1
i − (−1 − xi)−jq−1
) ∏
1≤i<j≤n
(xj − xi)−1.
(5.15)
On the other hand, the advantage of (2.8)i s  that it is actually a polynomial and 
therefore we can compute the constant term using (5.9). Now, by (5.14), it follows that 
the number of n × n ASMs is
lim
(x1,...,xn )→0
(y1,...,yn )→0
(−1)n(q−1−q)
(n+1
2
) n∏
i=1
(1+xi)n+1(1+q−1+xi)−1 ∏
1≤i<j≤n
(xj−xi)−1(yj−yi)−1
× det
1≤i,j≤n
( 1
(yj +1 ) (xi +1+ q) − xi − 1 − q−1
− 1
(yj +1 ) (xi +1+q ) − q2(xi +1+ q−1)
)
. (5.16)
The coeﬃcient of xiyj in
1
(y +1 ) (x +1+ q) − x − 1 − q−1 − 1
(y +1 ) (x +1+ q) − q2(x +1+q −1)
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 599
when considering this expression as a power series in x, y is
( j
i
)
(1 + q)−i−1(q − 1)−j−1(−1)jqj+1 −
i+j∑
k=i
( k
j
)( j
i − k + j
)(1 + q)k−i−j−1
(1 − q)j+1 (−1)k.
It follows that the number of n × n ASMs is given by
(1 + q)−n(−q)−
(n
2
)
det
0≤i,j≤n−1
(( j
i
)
(−1)jqj+1 +
n−1∑
k=0
( k + i
j
)(j
k
)
(−1 − q)k+i−j
)
.
Using basic properties of the binomial coeﬃcient and the Chu–Vandermonde summation, 
it can be shown that
( j
i
)
(−1)jqj+1 +
n−1∑
k=0
( k + i
j
)(j
k
)
(−1 − q)k+i−j
=
n−1∑
k=0
(−1)i
( i
k
)(−k − 1
j
)(
qj+1(−1)k + qk(−1)j)
,
and it follows that the number of n × n ASMs is given by
det
[(( i
j
)
(−1)i+j
)
0≤i,j≤n−1
·
(( i + j
j
)1 − (−q)j+1−i
1+ q
)
0≤i,j≤n−1
]
=d e t
0≤i,j≤n−1
(( i + j
j
)1 − (−q)j+1−i
1+ q
)
,
provided that q = e2iπ/3. This seems to be a new determinant for the ASM numbers.
In a forthcoming paper by F. Aigner, the more general determinant
det
0≤i,j≤n−1
(( x + i + j
j
)1 − (−q)j+1−i
1+ q
)
(5.17)
will be computed for all sixth roots of unity q not equal to 1, and consequences of this 
for the enumeration of Gogs. In these cases, the determinants have only integer zeros as 
a polynomial in x. Moreover, the determinant is related to the following determinant
det
0≤i,j≤n−1
(( x + i + j
j
)
+ qδ i,j
)
(5.18)
that was considered by Ciucu, Eisenkölbl, Krattenthaler and Zare [9], and computed 
for all sixth roots of unity q. To be more precise, the quotient of the ﬁrst and the 
second determinant is (−q)n if q = − 1
2 +
√
3
2 i, and it is (−q)−n if q = − 1
2 −
√
3
2 i. Other 
curious observations such as the following will be studied: For general q, there seems 
600 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
to be a sequence of functions pn(x, q)t h a t are polynomials in x of degree no greater 
than 
(⌈(n+1)/2⌉
2
)
and Laurent polynomials in q with highest exponent 
(⌊(n+1)/2⌋
2
)
and 
lowest exponent −
(⌊(n+1)/2⌋
2
)
over Q such that the determinant in (5.17)i s  equal to 
pn−1(x, q)pn(x, q).
Let us ﬁnally remark that one could of course apply (5.10)t o (5.15)a n d obtain
det
0≤i,j≤n−1
(
−q
( i + j
i
)
− q2δi,j
)
,
which is up to a trivial factor a specialization of (5.18)a n d has thus already been 
computed.
