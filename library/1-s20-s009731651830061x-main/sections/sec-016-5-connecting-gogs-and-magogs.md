---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Journal of Combinatorial Theory, Series A 158 (2018) 560–604 Contents lists available at ScienceDirect Journal of Combinatorial Theory, Series A www.elsevier.com/locate/jcta Consta"
section_id: sec-016-5-connecting-gogs-and-magogs
section_title: "Connecting Gogs and Magogs"
section_number: 5
pages: 31-34
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
In summary, we have seen that the constant term expressions for the number of 
Gog-type objects are all of the following form
s ·
n∏
i=1
fi(xi)
∏
1≤i<j≤n
(xi − xj)(1 + xj + xixj),
where fi(x)a r e certain (simple) rational function—often of the form
fi(x)=x ai (1 + x)bi ,
ai, bi integers—and s is a sign. These functions usually have (somewhat) homogeneous 
deﬁnitions for certain ranges of i: for instance, when considering (m, n, k)-Gog trapezoids, 
the deﬁnition is homogeneous for 1 ≤ i ≤ k and also for k +1 ≤ i ≤ n, see Theorem 7. In 
this case, a factor 1 +x in fi(x)i s replaced by 1 +Qxi for k +1 ≤ i ≤ n when considering 
the number of maxima, and f1(x)h a s an exceptional deﬁnition when considering the 
number of minima. When considering the generating function w.r.t. the two inversion 
numbers, the term 1 +xj +xixj is replaced by 1 +(1 −v)xi +u(xj +xixj)a n d some fi(x)
have an additional factor 1
(1+(1−v)x)ci , while others have an additional factor 1
(1+ux)di , 
ci, di non-negative integers.
Concerning constant term expressions for the number of Magog-type objects we need 
to distinguish between the two versions. In the ﬁrst case (Theorem 13), we have a sum 
of two expressions of the form
s ·
n∏
i=1
fi(xi)
∏
1≤i<j≤n
(xi − xj)(xi + xj + xixj)
∏
n−k+1≤i<j≤n
1
1 − xixj
,
while in the second case (Theorem 14), we have an expression of the form
s ·
n∏
i=1
fi(xi)
∏
1≤i<j≤m+n−1
xj − xi
1 − xixj
if q = n − k +1a n d a slightly more complicated expression otherwise.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 591
In [17]i t was shown that the number of n ×n ASMs (which is the same as the number 
of (n, n, n)-Gog trapezoids) is the constant term of the following expression
n−1∏
i=1
(1 + xi)2x−2i+1
i
∏
1≤i<j≤n−1
(xj − xi)(1 + xj + xixj). (5.1)
This is a Gog-type constant term expression as described above. Interestingly, this 
formula was derived using the six-vertex model approach, which is diﬀerent from the 
approach that was used here. On the other hand, it was shown that the number of TSS-
CPPs in an 2n × 2n × 2n box (which is the same as the number of (n, n, n)-Magogs) is 
the constant term of
n∏
i=1
(1 + xi)ix−2i+2
i (1 − x2
i )−1 ∏
1≤i<j≤n
xj − xi
1 − xixj
, (5.2)
and this is a Magog-type constant term expression. In [17], Fonseca and Zinn-Justin 
succeeded in showing that the constant terms of the two expressions are equal. It can es-
sentially be deduced from the following theorem, which was conjectured by Di Francesco 
and Zinn-Justin [34]a n d ﬁrst proven by Zeilberger [33].
Theorem 15. Let S(x1, ...,  xn) be a power series in x1, ...,  xn that is symmetric in 
x1, ...,  xn. Then
CTx1,...,xn S(x1,...,x n)
n∏
i=1
x−2i+1
i
∏
1≤i<j≤n
(xj − xi)(1 + txj + xixj)
=C Tx1,...,xn S(x1,...,x n)
n∏
i=1
(1 + txi)i−1x−2i+1
i
1 − x2
i
∏
1≤i<j≤n
xj − xi
1 − xixj
.
Fonseca and Zinn-Justin [17]g a v e another proof of the fact that the constant term 
of (5.1)i s equal to the constant term of (5.2), which is discussed next.
The general strategy (which also appeared in [32]) is to compute the symmetrizers
of ( 5.1)a n d of (5.2). (The symmetrizer is deﬁned as the antisymmetrizer except for 
the sign sgn σ which is omitted, see (2.7).) Clearly, in order to show that the constant 
terms of the original expressions are equal, it suﬃces to show this for the symmetrized 
expressions.
The computation of the symmetrizer is usually much easier for the Magog-type con-
stant term expressions, as ∏
1≤i<j≤n
xj −xi
1−xixj
is antisymmetric and therefore it suﬃces to 
compute the antisymmetrizer of 
n∏
i=1
fi(xi)( w i t h fi(x) =( 1 +xi)ix−2i+2
i (1 −x2
i
)−1 in this 
case), which can often be accomplished using the Vandermonde determinant evaluation.
As for the Gog-type constant term expressions, the following result of Fonseca and 
Zinn-Justin [17]c a n be used to compute the symmetrizer of (5.1)( a n d also to prove 
592 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
Theorem 15). The symmetrization of the Gog-type expression (5.1)c a u s e s the “core” ∏
1≤i<j≤n−1(xj − xi)(1 + xj + xixj)t o be transformed into ∏
1≤i<j≤n
xj −xi
1−xixj
(which is 
the “core” of the Magog-type expression (5.1)), and so the expressions are very similar 
(but not equal) after symmetrization.3
Theorem 16. Let hq(w, y) =( qw − q−1y)(qwy − q−1). Then the antisymmetrizer of
∏
1≤i<j≤n(qwi − q−1wj)∏
1≤i≤j≤n h1(wj,y i)∏
1≤j≤i≤n hq(wj,y i) (5.3)
w.r.t. w1, ...,  wn is
q
(n
2
)
det1≤i,j≤n
(
1
h1(wi,yj )hq (wi,yj )
)
∏
1≤i<j≤n h1(yi,y j)(1 − q2wiwj) .
Now in order to compute the constant term of (5.1)u s i n g Theorem 16, one sets 
wi =( xiq−1 − 1)/(xiq − 1) in (5.3)a n d obtains
(q − q−1)
(n
2
) ∏
1≤i<j≤n
(1 − (q + q−1)xj + xixj)
n∏
i=1
(qxi − 1)n+3
×
⎛
⎝
i∏
j=1
(−1+ yj + xi(q − q−1yj))(1 − yj + xi(−q−1 + qyj))
×
n∏
j=i
(−q−1 + qyj + xi(1 − yj))(q − q−1yj + xi(−1+ yj))
⎞
⎠
−1
. (5.4)
We need to compute the antisymmetrizer of
n∏
i=1
x−2i+1
i
∏
1≤i<j≤n
(1 + xj + xixj) (5.5)
3 The following identity is often helpful for further manipulations (the proof is left to the reader as we 
will not use it here): Suppose P (x1, ...,  xn ), S(x1, ...,  xn )a r e two formal power series and S(x1, ...,  xn)
is symmetric. Then the constant term of
S(x1,...,x n)P (x1,...,x n )
(x1 ··· xn )n−1
∏
1≤i<j≤n
(xj − xi)
agrees with the constant term of
S(0,..., 0)P (x1,...,x n)
(x1 ··· xn)n−1
∏
1≤i<j≤n
(xj − xi).
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 593
After setting yj =1a n d q = e2iπ/3, (5.4)i s up to a factor that is symmetric in x1, ...,  xn
equal to (5.5). Using Theorem 16, the antisymmetrizer can be written in terms of an 
expression involving a determinant, which can in turn be related to (5.2).
