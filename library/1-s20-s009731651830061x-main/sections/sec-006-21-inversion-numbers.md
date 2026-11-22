---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-006-21-inversion-numbers
section_title: "Inversion numbers"
section_number: 2.1
pages: 5-10
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
toc_source: outline
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
The inversion number of an ASM A = (ai,j)1≤i,j≤n, as deﬁned in [29, Eq. (18)], is 
given by
inv(A) =

1≤i′<i≤n,1≤j′≤j≤n
ai′,jai,j′.
It generalizes the inversion number of permutations, that is, for a permutation matrix A, 
inv(A) is the number of inversions of the permutation π = (π1, . . . , πn), where πi is the 
column of the unique 1 in row i. Deﬁne the complementary inversion number inv′(A) as 
follows.
inv′(A) =

1≤i′<i≤n,1≤j≤j′≤n
ai′,jai,j′
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
565
If A is the permutation matrix of π = (π1, . . . , πn), then inv′(A) is clearly the number of 
inversions of (πn, πn−1, . . . , π1), and so we have inv(A) + inv′(A) =
n
2

for permutation 
matrices.
It is a well-known fact [5] that n ×n alternating sign matrices correspond to Gelfand–
Tsetlin patterns with strictly increasing rows and bottom row 1, . . . , n. Recall that a 
Gelfand–Tsetlin pattern is a triangular array (mi,j)1≤j≤i≤n of integers, where the ele-
ments are usually arranged as follows
m1,1
m2,1
m2,2
. . .
. . .
. . .
mn−2,1
. . .
. . .
mn−2,n−2
mn−1,1
mn−1,2
. . .
. . .
mn−1,n−1
mn,1
mn,2
mn,3
. . .
. . .
mn,n
(2.1)
such that there is a weak increase in northeast and southeast direction, i.e., mi+1,j ≤
mi,j ≤mi+1,j+1 for all i, j with 1 ≤j ≤i < n. Throughout this paper, we use the 
indexing of the entries of triangular arrays and partial triangular arrays as given here. 
A Gelfand–Tsetlin pattern in which each row is strictly increasing except for possibly the 
bottom row is said to be a monotone triangle. (This deﬁnition deviates from the standard 
deﬁnition where also the bottom row needs to be strictly increasing.) Monotone triangles 
of order n where also the bottom row is increasing and the entries are positive integers 
no greater than m + n are just (m, n, n)-Gog trapezoids.
Suppose M = (mi,j)1≤j≤i≤n is the monotone triangle corresponding to the ASM 
A = (ai,j)1≤i,j≤n, then it is not hard to see that
inv(A) = #{(i, j) : mi,j = mi+1,j+1}
and
inv′(A) = #{(i, j) : mi,j = mi+1,j}.
Since the −1’s of an n × n ASM A correspond to the entries mi,j of the associated 
monotone triangle with i < n and mi+1,j < mi,j < mi+1,j+1, it follows that
inv(A) + inv′(A) =
n
2

−(# of −1’s in A).
(2.2)
We use this to extend the deﬁnition of the inversion number and the complementary 
inversion number to all monotone triangles, that is,
inv(M) = #{(i, j) : mi,j = mi+1,j+1}
and
inv′(M) = #{(i, j) : mi,j = mi+1,j}.
In [15, Corollary 3.1], it was shown that the number of monotone triangles with bottom 
row b1, . . . , bn is the constant term of
n

i=1
(1 + xi)bix−n+1
i

1≤i<j≤n
(xi −xj)(1 + xj + xixj).
(2.3)
566
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
(This derivation was based on [11].) In this section, we aim at generalizing this in order 
to obtain a constant term expression for the generating function of monotone triangles 
with respect to the two inversion numbers. For an increasing sequence b = (b1, . . . , bn), 
we deﬁne the generating function
MTb(u, v) =

M
uinv(M)vinv′(M),
where the sum is over all monotone triangles with bottom row b.
We say that the two non-decreasing sequences b = (b1, . . . , bn) and a = (a1, . . . , an−1)
are interlacing (in symbols: a ≺b), if
b1 ≤a1 ≤b2 ≤a2 ≤. . . ≤an−1 ≤bn.
Consecutive rows of monotone triangles are obviously interlacing sequences, and we can 
write down the following recursion for MTb(u, v):
MTb(u, v) =

a≺b
a strictly increasing
MTa(u, v)u#{i : ai=bi+1}v#{i : ai=bi}
We ﬁx some notation that is needed in the following: We use the shift operator Ex, 
the forward diﬀerence Δx and the backward diﬀerence Δx, which are deﬁned as follows.
Ex p(x) := p(x + 1)
Δx := Ex −Id
Δx := Id −E−1
x
We also need the following operator.
Strictx,y = E−1
x Ey +u Δx Ey −v E−1
x Δy = u Ey +v E−1
x +(1 −u −v) E−1
x Ey
Moreover, we need to work with the following extended deﬁnition of the summation
b

i=a
f(i) =
⎧
⎪
⎪
⎨
⎪
⎪
⎩
f(a) + f(a + 1) + . . . + f(b),
a ≤b,
0,
b = a −1,
−f(b + 1) −f(b + 2) −. . . −f(a −1),
b + 1 ≤a −1
.
The crucial property of the operator is the following: (Here we use the Iversion bracket, 
i.e., [statement] = 1 if the statement is true and [statement] = 0 otherwise.)

(ai−1,ai)≺(bi−1,bi,bi+1)
ai−1<ai
f(ai−1, ai)u[ai−1=bi]v[ai=bi]
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
567
=
⎡
⎢⎣Strictb(1)
i
,b(2)
i
b(1)
i
ai−1=bi−1
bi+1

ai=b(2)
i
f(ai−1, ai)
⎤
⎥⎦

b(1)
i
=b(2)
i
=bi
,
which is true provided that bi−1 < bi < bi+1. In case u = v = 1, it is also true if 
bi−1 ≤bi ≤bi+1. However, note that also
bi+1

ai=bi
f(ai)v[ai=bi] =
⎡
⎢⎣Strictb(1)
i
,b(2)
i
bi+1

ai=b(2)
i
f(ai)
⎤
⎥⎦

b(1)
i
=b(2)
i
=bi
(2.4)
and
bi+1

ai=bi
f(ai)u[ai=bi+1] =
⎡
⎢⎣Strictb(1)
i+1,b(2)
i+1
b(1)
i+1

ai=bi
f(ai)
⎤
⎥⎦

b(1)
i+1=b(2)
i+1=bi+1
(2.5)
whenever bi ≤bi+1. This implies

a≺b
a strictly increasing
f(a)u#{i : ai=bi+1}v#{i : ai=bi}
=
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
whenever b1 < b2 < . . . < bn, and, under the assumption that u = v = 1, it is suﬃcient 
to require b1 ≤b2 ≤. . . ≤bn. For x = (x1, . . . , xn), we deﬁne
GTn(x) =

1≤i<j≤n
xj −xi + j −i
j −i
and
Mn(u, v, x) =

1≤p<q≤n
Strictxq,xp GTn(x).
Theorem 2.1 in [15] can be generalized as follows.
Theorem 2. Suppose b = (b1, . . . , bn) is a strictly increasing sequence of integers, then 
the generating function of monotone triangles with bottom row b1, . . . , bn w.r.t. the two 
inversion numbers is the evaluation of the polynomial Mn(u, v, x) at (x1, . . . , xn) =
(b1, . . . , bn). When considering the special case u = v = 1, it suﬃces to require that 
(b1, . . . , bn) is weakly increasing.
The proof is analogous to the proof of Theorem 2.1 in [15]. Moreover, using the fact 
that
568
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
Strictx,y = E−1
x (Id +u Δx + (1 −v) Δy + u ΔxΔy),
the following generalization of Corollary 3.1 in [15] can be proved.
Corollary 3. Suppose b = (b1, . . . , bn) is a strictly increasing sequence of integers, then 
the generating function of monotone triangles with bottom row b1, . . . , bn w.r.t. the two 
inversion numbers is the constant term in x1, . . . , xn of the following Laurent polynomial.
n

i=1
(1 + xi)bix−n+1
i

1≤i<j≤n
(xi −xj)(1 + (1 −v)xi + u(xj + xixj))
When considering the special case u = v = 1, it suﬃces to require that (b1, . . . , bn) is 
weakly increasing.
In Appendix A, we elaborate on the case v = 1 −u, which is an interesting case since 
there exist certain combinatorial tools to handle it. Also note that we can recover the 
generating function with respect to number of −1 in the ASM proved in [13] by setting 
u = v = 1/Q and multiplying with Q
n
2

. This follows from (2.2).
Remark 2.1. There exist two alternative constant term expressions for the number of 
monotone triangles with bottom row b = (b1, . . . , bn) that could replace (2.3) in all what 
follows in the special case u = v = 1. Both of them are also based on [11]. First, it was 
shown in [12, Theorem 3] that the constant term of
n

i=1
x−n+1−bi
i
(1 −xi)−n

1≤i<j≤n
(xj −xi)(1 −xj + xixj)
(2.6)
is the number of monotone triangles with bottom row b = (b1, . . . , bn) if bi ≥0 for all i. 
Note that this is not a Laurent polynomial but a rational function, and so we need to 
clarify how we expand it into a Laurent series. Here and throughout the remainder of 
the paper, unless stated otherwise, we expand in powers with non-negative exponents, 
in particular, we have
(1 −xi)−n =
∞

j=0
−n
j

(−1)jxj
i
in (2.6). In order to present the second alternative formula, we deﬁne ASx1,...,xn to be 
the antisymmetrizer w.r.t. x1, . . . , xn, that is
ASx1,...,xnp(x1, . . . , xn) :=

σ∈Sn
sgn σ p(xσ(1), . . . , xσ(n)).
(2.7)
In [16] it was shown that the number of monotone triangles with bottom row b =
(b1, . . . , bn) is given by the constant term of the following expression.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
569
ASx1,...,xn
⎡
⎣
n

i=1
(1 + xi)bi

1≤i<j≤n
(1 + xj + xixj)
⎤
⎦

1≤i<j≤n
(xj −xi)−1
(2.8)
It can be seen directly that this constant term is equal to the constant term of (2.3) as, 
for any polynomial f(x1, . . . , xn), the constant term of f(x1, . . . , xn) 

1≤i<j≤n
(x−1
i
−x−1
j )
is equal to the constant term of ASx1,...,xn [f(x1, . . . , xn)] / 

1≤i<j≤n
(xi −xj). Note that 
the expression in (2.8) is a polynomial in x1, . . . , xn (and not only a Laurent polynomial).
It should be noted that (2.6) and (2.8) could actually be generalized to arbitrary u
and v.
