---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-015-42-second-version
section_title: "Second version"
section_number: 4.2
pages: 27-31
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
There are other options to encode (m, n, k)-Magog trapezoids as families of non-
intersecting lattice paths, see for instance [21]. We derive the constant term expression 
for a second possibility in this subsection, following an encoding that was used for in-
stance in [17]. Instead of interpreting NE-diagonals as lattice paths, we now consider 
the lattice paths that separate the entries that are less than or equal to i in the Magog 
trapezoid from the entries that are greater than or equal to i +1 , 1 ≤ i ≤ m + n − 1, 
see Fig. 3. By rotating the picture and shifting the paths appropriately, these paths can 
be transformed into a family of non-intersecting lattice paths, see Fig. 4 (the leftmost 
separating path in Fig. 3, i.e. the one separating the 1’s from 2’s, corresponds to the 
bottom path in Fig. 4).
It can be worked out that (m, n, k)-Magog trapezoids correspond to families of non-
intersecting lattice paths with starting points (−i +1 , i − 1), i =1 , ...,  m − 1, and 
(−i +1 , 2i − m − 1), m ≤ i ≤ m + n − 1, and end points (k − bj +1 , n − k + bj − 1), 
1 ≤ j ≤ m + n − 1, for some 1 ≤ b1 <b 2 < ... < b m+n−1 ≤ m + n + k − 1, with north 
steps and east steps. The maximums correspond to the lattice paths with starting points 
(−i +1 , 2i − m − 1), m ≤ i ≤ m + n − 1, such that the ﬁrst step is horizontal, while 
the number of minima is just the height of the last horizontal step of the path ending at 
(k −b1 +1, n −k +b1 −1) if b1 =1 , otherwise it is n −k +1. It follows that the number of 
(m, n, k)-Magog trapezoids with q minima is equal to the number of the following family 
of lattice paths depending on whether or not q = n − k +1 .
Case q ≤ n −k: In this case, we need to count families of non-intersecting lattice paths 
starting at (−i +1 , i − 1), i =1 , ...,  m − 1, and (−i +1 , 2i − m − 1), m ≤ i ≤ m + n − 1, 
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 587
Fig. 4. Non-intersecting lattice paths for the second version.
and with ending points (k − 1, q)a n d (k − bj +1 , n − k + bj − 1), 2 ≤ j ≤ m + n − 1, for 
some 2 ≤ b2 <...<b m+m−1 ≤ m + n + k − 1.
Case q = n − k +1 : Here, we need to count families of non-intersecting lattice paths 
starting at (−i +1 , i − 1), i =1 , ...,  m − 1, and (−i +1 , 2i − m − 1), m ≤ i ≤ m + n − 1, 
and with ending points (k − bj +1 , n − k + bj − 1), 1 ≤ j ≤ m + n − 1, for some 
2 ≤ b1 <...<b m+m−1 ≤ m + n + k − 1.
First we assume q ≤ n − k.
The generating function of lattice paths starting at (a, b)a n d ending at (c, d)w i t h 
respect to the weight
P [ﬁrst step is horizontal]
allowing steps in north direction and east direction is
P ·N ((a +1 ,b ) → (c, d)) + N ((a, b+1 ) → (c, d))
= P
( c + d − a − b − 1
c − a − 1
)
+
( c + d − a − b − 1
c − a
)
.
The formula is true whenever c + d − a − b > 0. It is also true when c + d − a − b =0
and c − a =0 . If c + d − a − b =0a n d c − a ⁄=0o r  c + d − a − b < 0, then the generating 
function vanishes. It follows that the generating function of (m, n, k)-Magog trapezoids 
with q minima and w.r.t. the number of maxima is
det
1≤i,j≤m+n−1
⎛
⎝
(k+q−1
k+i−2
) ( n
i+k−bj
)
⎧
⎨
⎩
P
(k+m+q−i−2
k+i−3
)
+
(k+m+q−i−2
k+i−2
)
,i ≤ k + m + q − 2
0,i ≥ k + m + q − 1
P
(m+n−i−1
i+k−bj −1
)
+
(m+n−i−1
i+k−bj
)
⎞
⎠ ,
588 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
where we need to distinguish between 1 ≤ i ≤ m − 1a n d m ≤ i ≤ m + n − 1 concerning 
the row, and between j =1a n d 2 ≤ j ≤ m + n − 1 concerning the columns, and we have 
to exclude the case when k =1a n d m + q =1 . This is equal to the constant term of
det
1≤i,j≤m+n−1
⎛
⎜⎜⎜⎝
(1+xi )k+q−1
xi+k−3
i
(1+xi )n
x
i+k−bj
i⎧
⎪⎪
⎪
⎪
⎪
⎪
⎨
⎪⎪
⎪
⎪
⎪
⎪
⎩
P (1+xi )k+m+q−i−2
xi+k−3
i
+ (1+xi )k+m+q−i−2
xi+k−2
i
,
i ≤ k + m + q − 2
0,i ≥ k + m + q − 1
P (1+xi )m+n−i−1
x
i+k−bj −1
i
+ (1+xi )m+n−i−1
x
i+k−bj
i
⎞
⎟⎟⎟⎠ .
We pull out the factor
P [m=0]
m+n−1∏
i=1
(1 + xi)nx−i−k
i
m+n−1∏
i=max(1,m)
(1 + xi)m−i−1 (Pxi +1 ),
and we obtain the following determinant
det
1≤i,j≤m+n−1
({
(1 + xi)k+q−n−1x2
i ,i ≤ k + m + q − 2
0,i ≥ k + m + q − 1
xbj
i
)
,
where we now only have to distinguish between j =1a n d 2 ≤ j ≤ m + n − 1 concerning 
the columns, while we have a homogeneous deﬁnition in the rows. We expand w.r.t. the 
ﬁrst column and obtain
k+m+q−2∑
l=1
(−1)l+1(1 + xl)k+q−n−1x2
l det
2≤j≤m+n−1
1≤i≤m+n−1,i⁄=l
(
xbj
i
)
. (4.4)
Now we aim to sum over all 2 ≤ b2 < ... < b m+n−1 ≤ m + n + k − 1. However, 
since the constant term is zero if bm+n−1 ≥ m + n + k, we can simply sum over all 
2 ≤ b2 <...<b m+n−1. Observe that by Lemma 12 we get
∑
b≤b1<b2<...<br
det
1≤i,j≤r
(
xbj
i
)
=
∑
b≤b1<b2<...<br
∑
σ∈Sr
sgn σ · σ
[
xb1
1 ··· xbr
r
]
=
l∏
i=1
xb
i
∑
σ∈Sr
sgn σ · σ
⎡
⎣ ∑
0≥b1<b2<...<br
xb1
1 ··· xbr
r
⎤
⎦
=
r∏
i=1
xb
i
∑
σ∈Sr
sgn σ · σ
⎡
⎣
r∏
i=1
xi−1
i(
1 −∏r
j=i xj
)
⎤
⎦
=
r∏
i=1
xb
i (1 − xi)−1 ∏
1≤i<j≤r
xj − xi
1 − xixj
. (4.5)
We sum (4.4)o v e r all b2, ...,  bm+n−1 with 2 ≤ b2 ...<b m+n−1 and obtain
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 589
k+m+q−2∑
l=1
(−1)l+1(1 + xl)k+q−n−1x2
l
∏
1≤i≤m+n−1
i⁄=l
x2
i
(1 − xi)−1 ∏
1≤i<j≤m+n−1
i,j⁄=l
xj − xi
1 − xixj
It follows that the generating function of (m, n, k)-Magog trapezoids with q Minima 
w.r.t. the weight P #o fm a x i m ais the constant term of
P [m=0]
m+n−1∏
i=1
(1 + xi)nx−i−k
i
m+n−1∏
i=max(m,1)
(1 + xi)m−i−1 (Pxi +1 )
×
k+m+q−2∑
l=1
(−1)l+1(1 + xl)k+q−n−1x2
l
m+n−1∏
1≤i≤m+n−1
i⁄=l
x2
i
(1 − xi)−1 ∏
1≤i<j≤m+n−1
i,j⁄=l
xj − xi
1 − xixj
if we assume q ≤ n − k.
In case q = n − k +1 , the number of Magog trapezoids is the constant term of
det
1≤i,j≤m+n−1
⎛
⎝
⎧
⎨
⎩
(1+xi)n
x
i+k−bj
i
,i =1 ,...,m − 1
P (1+xi)m+n−i−1
x
i+k−bj −1
i
+ (1+xi)m+n−i−1
x
i+k−bj
i
,i = m ,...,m + n − 1
⎞
⎠ .
Again we pull out the factor
P [m=0]
m+n−1∏
i=1
(1 + xi)nx−i−k
i
m+n−1∏
i=max(m,1)
(1 + xi)m−i−1 (Pxi +1 ),
and, in this case, we obtain the following simple determinant.
det
1≤i,j≤m+n−1
(
xbj
i
)
.
Finally, we sum over all 2 ≤ b1 <b 2 <...<b m+n−1, and, by (4.5), we obtain
P [m=0]
m+n−1∏
i=1
(1 + xi)nx−i−k+2
i (1 − xi)−1
m+n−1∏
i=max(m,1)
(1 + xi)m−i−1 (Pxi +1 )
×
∏
1≤i<j≤m+n−1
xj − xi
1 − xixj
.
We summarize our results in the following theorem.
Theorem 14. Suppose k ⁄=1 or m + q ⁄=1. The generating function of (m, n, k)-Magog 
trapezoids w.r.t. the weight P # of maxima and with q minima is equal to the constant 
term of
590 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
P [m=0]
m+n−1∏
i=1
(1 + xi)nx−i−k+2
i (1 − xi)−1
m+n−1∏
i=max(m,1)
(1 + xi)m−i−1 (Pxi +1 )
×
∏
1≤i<j≤m+n−1
xj − xi
1 − xixj
×
⎧
⎪⎪⎨
⎪⎪⎩
k+m+q−2∑
i=1
(1 + xi)k+q−n−1(1 − xi) ∏
1≤j≤m+n−1
j⁄=i
1−xixj
xj −xi
, if q ≤ n − k
1, if q = n − k +1 .
