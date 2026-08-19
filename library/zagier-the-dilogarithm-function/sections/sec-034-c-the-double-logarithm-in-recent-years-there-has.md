---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-034-c-the-double-logarithm-in-recent-years-there-has
section_title: "The double logarithm. In recent years there has been a resurgence of"
section_number: C
pages: 24-26
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
interest in the “multiple zeta values”
ζ(k1,...,k m)=
∑
n1,...,nm∈Z
0<n1<···<nm
1
nk1
1 ··· nkm
m
originally deﬁned (for m = 2) by Euler; these numbers turn up in particular
in connection with quantum invariants of knots and with the calculation of
certain Feynman diagram integrals. The multiple zeta values are simply the
specializations to x1 =··· =xm = 1 of the multiple polylogarithm functions
Lik1,...,km (x1,...,x m)=
∑
n1,...,nm ∈Z
0<n1<···<nm
xn1
1 ··· xnm
m
nk1
1 ··· nkm
m
which form = 1 is the ordinary polylogarithm function.
In the hierarchy of multiple polylogarithm functions, the key invariant is
the total weight k1 +··· +km. The only multiple polylogarithm of weight 1
is the ordinary logarithm Li 1(x)= −log(1−x), but there are two multiple
polylogarithms of weight 2, the dilogarithm function Li 2(x) and the double
logarithm function [21]
The Dilogarithm Function 27
Li1,1(x,y )=
∑
0<m<n
xmyn
mn (x, y∈ C, |y|< 1, |xy|< 1).
The remarkable fact here is that the function Li1,1, which has two arguments
and hence is a priori a more complicated type of object than the one-argument
function Li2, can in fact be expressed in terms only of the latter:
Proposition 1. For x, y∈ C with |xy|< 1,|y|< 1 we have
Li1,1(x,y )=L i 2
(xy−y
1−y
)
− Li2
( −y
1−y
)
− Li2(xy). (2)
Before proving this identity, we mention some equivalent formulas and con-
sequences. First of all, the double logarithm function satisﬁes the identity—the
simplest case of the “shuﬄe relations” satisﬁed by all multiple zeta values and
multiple polylogarithms—
Li
1,1(x,y )+L i1,1(y,x )+L i2(xy)=L i 1(x)L i1(y), (3)
which is an immediate consequence of the fact that any pair of positive integers
(m,n) must satisfy exactly one of the three conditions 0<m<n ,0 <n<m ,
or 0 <m =n. Combining this with (2) and interchanging the roles of x and
y, we can rewrite (2) in the equivalent form
Li
1,1(x,y )=L i 1(x)L i1(y)+L i 2
( −x
1−x
)
− Li2
(xy−x
1−x
)
, (4)
which is slightly less pretty than (2) in that it involves products of logarithms
as well as dilogarithms, but has the advantage of containing only two rather
than three dilogarithms. And if we use (4) to express both Li
1,1(x,y )a n d
Li1,1(y,x ) in (3) in terms of dilogarithms, we obtain what is perhaps the most
natural proof of the ﬁve-term relation.
We now give the proof of Proposition 1 (in the form (4) or (2)). In fact,
just for fun we give three proofs.
(i) We have
∂
∂y Li1,1(x,y )=
∑
0<m<n
xm
m yn−1 =
∞∑
m=1
xm
m
ym
1−y
= 1
1−y log 1
1−xy .
The derivative with respect to y of the right-hand side of (4) (or of (2)) has
the same value and both sides of (4) (or of (2)) vanish aty =0 .
(ii) We have
∂
∂x Li1,1(x,y )=
∑
0<m<n
xm−1 yn
n =
∞∑
n=1
1−xn−1
1−x
yn
n
= 1
1−x log 1
1−y − 1
x(1−x) log 1
1−xy .
