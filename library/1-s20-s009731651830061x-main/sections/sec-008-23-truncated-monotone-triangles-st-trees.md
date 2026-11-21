---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-008-23-truncated-monotone-triangles-st-trees
section_title: "Truncated monotone triangles: (s,t)-trees"
section_number: 2.3
pages: 11-14
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
toc_source: outline
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
Next we turn to certain partial monotone triangles. Let l, r, n be non-negative integers 
with l + r ≤n. Suppose s = (s1, s2, . . . , sl), t = (tn−r+1, tn−r+2, . . . , tn) are sequences 
of non-negative integers, where s is weakly decreasing, while t is weakly increasing. 
An (s, t)-tree of order n is an integer array whose shape is obtained from the shape 
of a monotone triangle with n rows when deleting the bottom si entries from the i-th 
NE-diagonal for 1 ≤i ≤l (NE-diagonals are counted from the left) and the bottom ti
entries from the i-th SE-diagonal for n −r + 1 ≤i ≤n (SE-diagonals are also counted 
from the left), see Fig. 1. We assume in the following that there is no interference between 
the deletion of the entries in the l leftmost NE-diagonals (as prescribed by s) with the 
deletion of the entries from the r rightmost SE-diagonals (as prescribed by t).
In an (s, t)-tree, an entry mi,j is said to be regular if it has a SW neighbor mi+1,j
and a SE neighbor mi+1,j+1. We require the following monotonicity properties in an 
(s, t)-tree:
(1) Each regular entry mi,j has to fulﬁll mi+1,j ≤mi,j ≤mi+1,j+1.
(2) Two adjacent regular entries mi,j, mi,j+1 in the same row have to be distinct.
This extends the notion of monotone triangles, as a monotone triangle of order n is 
just an (s, t)-tree, where l, r are any two numbers with l + r ≤n, s = (0, . . . , 0
  
l
) and 
t = (0, . . . , 0
  
r
).
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
571
We extend the deﬁnition of the two inversion numbers as follows. Suppose M = (mi,j)
(using the indexing indicated in (2.1)) is an (s, t)-tree of order n and deﬁne
inv(M) = #{mi,j regular : mi,j = mi+1,j+1},
inv′(M) = #{mi,j regular : mi,j = mi+1,j}.
We deﬁne further generalizations of the inversion numbers that are useful for our pur-
poses: The generalization of inv depends on a subset J ⊆{j|tj < tj+1} ∪{n} of 
exceptional SE-diagonals and is deﬁned as
invJ(M) = #{mi,j regular : mi,j = mi+1,j+1
and mi+1,j+1 is not the bottom entry of an exceptional SE-diagonal}.
The generalization of the complementary inversion number inv′ depends on a subset 
I ⊆{1} ∪{i|si−1 > si} of exceptional NE-diagonals and is deﬁned as
inv′
I(M) = #{mi,j regular : mi,j = mi+1,j
and mi+1,j is not the bottom entry of an exceptional NE-diagonal}.
Next we deﬁne generalizations of the forward diﬀerence operator and of the backward 
diﬀerence operator, namely the v-forward diﬀerence operator Δ[v]x (w.r.t. the variable x) 
and the u-backward diﬀerence operator Δ[u]x.
Δ[v]x = (1 + (1 −v)Δx)−1Δx
and
Δ[u]x = (1 + (u −1)Δx)−1Δx
These operators are well-deﬁned in our context, since
(1 + (1 −v)Δx)−1 =
∞

i=0
(v −1)iΔ
i
x
and
(1 + (u −1)Δx)−1 =
∞

i=0
(1 −u)iΔi
x
and the sums are ﬁnite if applied to polynomials, because for each polynomial p(x) of 
degree d we have Δ
i
xp(x) = Δi
xp(x) = 0 for all i > d. The following property of Δ[v]x is 
crucial:
−Δ[v]b1
⎡
⎢⎣Strictb(1)
1
,b(2)
1
. . . Strictb(1)
n ,b(2)
n
b(1)
2
a1=b(2)
1
b(1)
3
a2=b(2)
2
· · ·
b(1)
n

an−1=b(2)
n−1
f(a)
⎤
⎥⎦

b(1)
i
=b(2)
i
=bi
= −Δb1
⎡
⎢⎣Strictb(1)
2
,b(2)
2
. . . Strictb(1)
n ,b(2)
n
b(1)
2
a1=b1
b(1)
3
a2=b(2)
2
· · ·
b(1)
n

an−1=b(2)
n−1
f(a)
⎤
⎥⎦

b(1)
i
=b(2)
i
=bi
572
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
=
⎡
⎢⎣Strictb(1)
2
,b(2)
2
. . . Strictb(1)
n ,b(2)
n
b(1)
3
a2=b(2)
2
· · ·
b(1)
n

an−1=b(2)
n−1
f(b1, a2, . . . , an−1)
⎤
⎥⎦

b(1)
i
=b(2)
i
=bi
A similar identity is true for Δ[u]x. These observations imply almost immediately the 
following result. The case u = v = 1 appeared ﬁrst in [14], however the proof given there 
can be generalized easily, see also [15].
Theorem 5. Let n, l, r be non-negative integers with l + r ≤n. Suppose b1, . . . , bn is 
a strictly increasing sequence of integers, and s = (s1, s2, . . . , sl), t = (tn−r+1, tn−r+2,
. . . , tn) are a weakly decreasing and a weakly increasing sequence of non-negative integers, 
respectively. Then the evaluation of the following polynomial
(−Δ[v]x1)s1 · · · (−Δ[v]xl)slΔ[u]tn−r+1
xn−r+1 · · · Δ[u]tn
xnMn(u, v, x)
(2.9)
at (x1, . . . , xn) = (b1, . . . , bn) is the generating function with respect to inv and inv′ of 
(s, t)-trees of order n with the following properties:
• For 1 ≤i ≤n −r, the bottom entry of the i-th NE-diagonal is bi.
• For n −r + 1 ≤i ≤n, the bottom entry of the i-th SE-diagonal is bi.
Furthermore, suppose I ⊆{1} ∪{i|si−1 > si} and J ⊆{j|tj < tj+1} ∪{n}, then 
the generating function with respect to invJ and inv′
I of these (s, t)-trees is obtained 
from (2.9) by applying

i∈I

1 + (1 −v)Δxi
−1 
j∈J

1 + (u −1)Δxj
−1
,
and then evaluating at (x1, . . . , xn) = (b1, . . . , bn). Finally, suppose min ≤a ≤max
are integers with min ≤b1 and bn ≤max, then we obtain the generating function of 
the above mentioned (s, t)-trees that have a in the top row if Mn(u, v, x) is replaced by 
Mn,a,min,max(u, v, x).
When considering the special case u = v = 1, all results are true also if we only require 
that b1, . . . , bn is weakly increasing.
In order to prove the modiﬁcation concerning the generalized inversion numbers invJ
and inv′
I, it has to be noted that
Strictx,y = 1 + (1 −v)Δy
when applied to functions that are independent of x, while
Strictx,y = 1 + (u −1)Δx
when applied to functions that are independent of y. Compare also to (2.4) and (2.5).
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
573
We translate the formula in the theorem into a constant term expression generaliz-
ing the constant term expression of Corollary 3: To this end, we ﬁrst observe that the 
application of Δbi to the constant term expression in Corollary 3 corresponds to the 
multiplication with (1 + xi) −1 = xi, while the application of Δbi corresponds to the 
multiplication with 1 −1/(1 + xi) = xi/(1 + xi). This implies the following relations:
Δ[u]bi ∼
xi
1 + (1 −v)xi
and
Δ[u]bi ∼
xi
1 + uxi
.
Corollary 6. The generating function of (s, t)-trees as described in the theorem is given 
by the constant term in x1, . . . , xn of the following expression:
l
i=1

xi
(v −1)xi −1
si
n

i=n−r+1

xi
uxi + 1
ti
n

i=1
(1 + xi)bix−n+1
i
×

1≤i<j≤n
(xi −xj)(1 + (1 −v)xi + u(xj + xixj))
If I, J are two sets as described in the theorem, then the generating function with re-
spect to invJ, inv′
I is the constant term in x1, . . . , xn of the expression one obtains by 
multiplying the rational function above with

i∈I
1
1 + (1 −v)xi

j∈J
1 + xj
1 + uxj
.
If min ≤a ≤max are integers with min ≤b1 and bn ≤max, then the generating function 
of the above mentioned (s, t)-trees whose top row is a is the constant term of the rational 
function which is obtained by multiplying the respective expression by Pn,a,min,max(x).
