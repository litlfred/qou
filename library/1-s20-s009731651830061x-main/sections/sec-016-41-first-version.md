---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-016-41-first-version
section_title: "First version"
section_number: 4.1
pages: 21-27
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
toc_source: outline
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
Using a standard technique, we can transform (m, n, k)-Magog trapezoids with pre-
scribed bottom row (bn−k+1, bn−k+2, . . . , bn) into families of non-intersecting lattice 
paths as follows: We start by adding a new leftmost SE-diagonal consisting entirely of 
1’s and a new rightmost SE-diagonal consisting of (m +1, m +2, . . . , m +n) as indicated 
in green in our running Example 1.1:
3
3
4
2
3
5
2
3
4
6
1
3
4
5
7
1
2
3
5
7
8
1
1
3
4
6
7
9
1
2
3
4
7
9
.
Next, we add i −1 to the i-th NE-diagonal, counted from the left, for all 1 ≤i ≤n. 
Then we associate with each NE-diagonal a lattice path with north steps and east steps 
where the entries of the NE-diagonals are the heights of the paths, and, as long as 
1 ≤i ≤n −k −1, the x-coordinate of the starting point is shifted by one unit to 
the left when passing from the i-th NE-diagonal to the (i + 1)-st NE-diagonal, while 
these x-coordinates are the same for the k + 1 rightmost NE-diagonals. The family of 
non-intersecting lattice paths in Fig. 2 corresponds to the Magog in (1.1). Note that each 
of the paths starts and ends with a horizontal step and thus we cut oﬀ these horizontal 
steps in the following.
Now it can be deduced that (m, n, k)-Magogs with bottom row (bn−k+1, bn−k+1, . . . , bn)
correspond to the families of non-intersecting lattice paths starting at (−i + 1, i), 
1 ≤i ≤n −k, and (−n + k + 1, bi + i −1), n −k + 1 ≤i ≤n, and ending at 
(k −j + 1, m + 2j −1), 1 ≤j ≤n, allowing steps in north direction and east direction. 
The last entry of a NE-diagonal is a maximum if the last step of the respective lattice 
path is horizontal, while the ﬁrst entry of the n −k leftmost NE-diagonals is a minimum 
if the ﬁrst step of the respective path is horizontal. The following generating function of 
lattice paths starting at (a, b) and ending at (c, d)

lattice path (a, b) →(c, d)
Q[ﬁrst step is horizontal]P [last step is horizontal]
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
581
Fig. 2. Non-intersecting lattice paths.
allowing steps in north direction and east direction is
N((a, b + 1) →(c, d −1)) + Q N((a + 1, b) →(c, d −1))+
P N((a, b + 1) →(c −1, d)) + PQ N((a + 1, b) →(c −1, d)),
where N((a, b) →(c, d)) denotes the number of lattice paths starting at (a, b) and ending 
at (c, d) (which is equal to 
c+d−a−b
d−b

). Thus, this generating function is
c + d −a −b −2
d −b −2

+ (P + Q)
c + d −a −b −2
d −b −1

+ PQ
c + d −a −b −2
d −b

,
which evaluates to
c + d −a −b −1
d −b −1

+ P
c + d −a −b −1
d −b

if Q = 1. If we use
582
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
n
k

=
 n(n−1)···(n−k+1)
k!
k ≥0
0
k < 0
,
then the formulas for the generating functions are true for any choice of integers a, b, c, d
(in particular also when there is no path from (a, b) to (c, d)) if whenever the upper 
parameter of each binomial coeﬃcient is negative, then also the lower parameter is neg-
ative. The Lindström–Gessel–Viennot theorem [24,19] now implies that the generating 
function of (m, n, k)-Magog trapezoids that have bottom row (bn−k+1, . . . , bn) is
det
1≤i,j≤n

 j+k+m−3
2j+m−i−3

+ (P + Q)
 j+k+m−3
2j+m−i−2

+ PQ
 j+k+m−3
2j+m−i−1

,
i = 1, . . . , n −k
j+m+n−bi−i−1
2j+m−bi−i−1

+ P
j+m+n−bi−i−1
2j+m−bi−i

,
i = n −k + 1, . . . , n

,
where the weight is
P # of maxima · Q# of minima not contained in the bottom row.
In case 1 ≤i ≤n −k, the upper parameter of a binomial coeﬃcient in the matrix is 
negative only if j = 1, k = 1, m = 0; then all lower parameters are also negative, except 
the one after PQ if i = 1 which is 0 and it can be checked that also in this case we 
have the correct generating function. In case n −k + 1 ≤i ≤n, the upper parameters 
are either no less than the lower parameters or non-negative or the lower parameters are 
negative, except for the binomial coeﬃcient after P when j + m + n −bi −i −1 = −1
and 2j +m −bi −i = 0, and it can be checked that also in this case we obtain the correct 
result.
Using 
n
k

= (−1)kk−n−1
k

, this is equal to
(−1)
(m−1)n+
n+1
2

+
n

i=n−k+1
bi
×
det
1≤i,j≤n

 j−i−k−1
2j+m−i−3

−(P + Q)

j−i−k
2j+m−i−2

+ PQ
 j−i−k+1
2j+m−i−1

,
i = 1, . . . , n −k

j−n−1
2j+m−bi−i−1

−P

j−n
2j+m−bi−i

,
i = n −k + 1, . . . , n

.
Now, as CTx
(1+x)n
xk
=
n
k

, where CTx denotes the constant term in x, this is equal to
CTx1,...,xn(−1)
(m−1)n+
n+1
2

+
n

i=n−k+1
bi
×
det
1≤i,j≤n
⎛
⎝
⎧
⎨
⎩
(1+xi)j−i−k−1
x2j+m−i−3
i
−(P + Q) (1+xi)j−i−k
x2j+m−i−2
i
+ PQ (1+xi)j−i−k+1
x2j+m−i−1
i
,
i = 1, . . . , n −k
(1+xi)j−n−1
x2j+m−bi−i−1
i
−P
(1+xi)j−n
x2j+m−bi−i
i
,
i = n −k + 1, . . . , n
⎞
⎠.
After pulling out the factor
n−k

i=1
(1 + xi)−i−k
xm−i+1
i
(xi −P(1 + xi)) (xi −Q(1 + xi))
n

i=n−k+1
(1 + xi)−n
xm−bi−i+2
i
(xi −P(1 + xi))
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
583
of the determinant, it remains
det
1≤i,j≤n

(x−1
i
+ x−2
i )j−1
=

1≤i<j≤n

x−1
j
+ x−2
j
−x−1
i
−x−2
i

=

1≤i<j≤n
(xi −xj)(xi + xj + xixj)
x2
i x2
j
,
which can be computed using the Vandermonde determinant evaluation.
We obtain the following theorem.
Theorem 11. The generating function of (m, n, k)-Magog trapezoids with bottom row 
bn−k+1, . . . , bn and w.r.t. the weight
P #of maximaQ#of minima not including bn−k+1
is the constant term of the following expression in x1, . . . , xn.
(−1)
(m−1)n+
n+1
2

+
n

i=n−k+1
bi n−k

i=1
(1+xi)−i−kx−m−2n+i+1
i
(xi −P(1 + xi)) (xi −Q(1+xi))
×
n

i=n−k+1
(1 + xi)−nx−m−2n+bi+i
i
(xi −P(1 + xi))

1≤i<j≤n
(xi −xj)(xi + xj + xixj).
(4.1)
We set
Mm,n,k(x1, . . . , xn)
= (−1)(m−1)n+
n−k+1
2
 n−k

i=1
(1 + xi)−i−kx−m−2n+i+1
i
(xi −P(1 + xi)) (xi −Q(1 + xi))
×
n

i=n−k+1
(1 + xi)−nx−m−2n
i
(xi −P(1 + xi))

1≤i<j≤n
(xi −xj)(xi + xj + xixj),
so that the generating function is
n

i=n−k+1
(−xi)bi+iMm,n,k(x1, . . . , xn).
It will be crucial that Mm,n,k(x1, . . . , xn) is an antisymmetric function in xn−k+1, . . . , xn. 
It follows that the generating function of (m, n, k)-Magogs w.r.t. the weight
P # of maxima · Q# of minima
584
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
is the constant term of
⎛
⎝Q
⎛
⎝

1≤bn−k+2≤bn−k+3≤...≤bn
yn−k+2
n−k+1
n

i=n−k+2
ybi+i
i
⎞
⎠
+
⎛
⎝

2≤bn−k+1≤bn−k+2≤...≤bn
n

i=n−k+1
ybi+i
i
⎞
⎠
⎞
⎠Mm,n,k(x1, . . . , xn)
=

Q +
n
i=n−k+1 yi
1 −n
i=n−k+1 yi

n
i=n−k+1 yi+1
i
n
i=n−k+2

1 −n
j=i yj
Mm,n,k(x1, . . . , xn),
(4.2)
where we set yi = −xi. We use the following notation: Suppose F(xr+1, . . . , xr+s) is a 
function in xr+1, . . . , xr+s and σ ∈Ss, then
σ[F(xr+1, . . . , xr+s)] := F(xσ(r+1), . . . , xσ(r+s)).
Now the constant term of the expression in (4.2) is the constant term of
1
(k −1)!

σ∈Sk−1
Q yn−k+2
n−k+1Mm,n,k(x1, . . . , xn) sgn σ · σ
#
n

i=n−k+2
yi+1
i
1 −n
j=i yj
$
+ 1
k!

σ∈Sk
Mm,n,k(x1, . . . , xn) sgn σ · σ
#
n

i=n−k+1
yi+2
i
1 −n
j=i yj
$
.
(4.3)
We need the following lemma, which can be found in [25, Example 4, Chapter III.5]. 
It appeared in a similar context in [32, Subsublemma 1.1.3].
Lemma 12. Let r ≥1 be an integer. Then

σ∈Sr
sgn σ · σ
# r

i=1
yi−1
i
1 −r
j=i yj
$
=
r

i=1
(1 −yi)−1

1≤i<j≤r
yj −yi
1 −yiyj
.
From the lemma it now follows that the expression in (4.3) is equal to
Q · yn−k+2
n−k+1Mm,n,k(x1, . . . , xn) n
i=n−k+2 yn−k+3
i
(1 −yi)−1
(k −1)!

n−k+2≤i<j≤n
yj −yi
1 −yiyj
+ Mm,n,k(x1, . . . , xn) n
i=n−k+1 yn−k+3
i
(1 −yi)−1
k!

n−k+1≤i<j≤n
yj −yi
1 −yiyj
.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
585
This can also be written as
Q · yn−k+2
n−k+1Mm,n,k(x1, . . . , xn) n
i=n−k+2(1 −yi)−1
(k −1)!
×

n−k+2≤i<j≤n
1
1 −yiyj

σ∈Sk−1
sgn σ σ
#
n

i=n−k+2
yi+1
i
$
+ Mm,n,k(x1, . . . , xn) n
i=n−k+1(1 −yi)−1
k!
×

n−k+1≤i<j≤n
1
1 −yiyj

σ∈Sk
sgn σ σ
#
n

i=n−k+1
yi+2
i
$
.
We again employ the antisymmetry of Mm,n,k(x1, . . . , xn) to see that the constant term 
of the previous expression this is equal to the constant term of
Q · yn−k+2
n−k+1Mm,n,k(x1, . . . , xn)
n

i=n−k+2
yi+1
i
(1 −yi)−1

n−k+2≤i<j≤n
1
1 −yiyj
+ Mm,n,k(x1, . . . , xn)
n

i=n−k+1
yi+2
i
(1 −yi)−1

n−k+1≤i<j≤n
1
1 −yiyj
= (−1)
n+3
2

+
n−k+3
2

Mm,n,k(x1, . . . , xn)
n

i=n−k+1
xi+2
i
1 + xi

n−k+1≤i<j≤n
1
1 −xixj
×
⎛
⎝(−1)kQ(1 + x−1
n−k+1)
n

j=n−k+2
(x−1
j
−xn−k+1) + 1
⎞
⎠.
We summarize our result in the following theorem.
Theorem 13. The generating function of (m, n, k)-Magog trapezoids w.r.t. the weight
P #of maxima Q#of minima
is the constant term in x1, . . . , xn of the following expression.
(−1)(m−1)n+
n+1
2

⎛
⎝(−1)kQ(1 + x−1
n−k+1)
n

j=n−k+2
(x−1
j
−xn−k+1) + 1
⎞
⎠
×
n−k

i=1
(1 + xi)−i−kx−m−2n+i+1
i
(xi −P(1 + xi)) (xi −Q(1 + xi))
586
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
Fig. 3. An (2, 7, 5)-Magog trapezoids and its separating lattice paths.
×
n

i=n−k+1
(1 + xi)−n−1x−m−2n+i+2
i
(xi −P(1 + xi))
×

1≤i<j≤n
(xi −xj)(xi + xj + xixj)

n−k+1≤i<j≤n
1
1 −xixj
