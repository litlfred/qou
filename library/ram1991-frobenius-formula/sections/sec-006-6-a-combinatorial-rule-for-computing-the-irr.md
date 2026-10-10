---
doc_id: ram1991-frobenius-formula
doc_title: "A Frobenius formula for the characters of the Hecke algebras"
section_id: sec-006-6-a-combinatorial-rule-for-computing-the-irr
section_title: "A combinatorial rule for computing the irreducible characters of the Hecke algebras"
section_number: "6"
pages: 19-23
source_pdf: ram1991-frobenius-formula.pdf
source_sha256: 26b2fc85338d9150
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
---
6 A combinatorial rule for computing the irreducible characters
of the Hecke algebras
In this section we rewrite the formula
Z (- 1)5-mgm-1(q-1)Zcav(1-mm)Kvμ (6.1)
m= 1
from Theorem 5.5 to derive a combinatorial rule for computing the irreducible
characters of the Hecke algebra. For the remainder of this section we will assume
that all symmetric functions are in the variables xi, X2, : : :, Xn, so that we may
Write Sa for Sa(xi, . . ., Xn).
For any two partitions a, μ f define
CauvSv :
where, as in (4.7), Cauv denotes the Kronecker coefficient. Extend this definition
linearly to all symmetric functions.
(6.2) Lemma.
Z CvapKvu = (hu @ S,)lsi
Proof.
ZcvapKvu = E(s, @ sp)ls, Kvμ
?sp
= (hu@ Sp)Is, : 
Evaluation of the product hu @s, is facilitated by the following theorem of
Garsia and Remmel [G-R].
(6.3) Theorem.
huβs=Z II Sp(i/p(--1)
(p) i=1
where the sum is over all sequences of partitions (p) = ( = p(0) 三 p(1) . . . 
n = l(t-)d - (od1 ao yons (d = (no
Applying Theorem 6.3 when p = (1 f -mm) gives
hy @ S(1-mm) =ZS(14t-mm1) II hm.eut-m= 
(u) i=2
480 A. Ram
where the sum is over all sequences of nonnegative integers (m) -- (m1, m2, : . : , mk)
such that mi > O, Zi mi = m and mi ≤ μi. Then
 (- 1)5-mqm=1(q - 1)(hu ? S(1-mm)
m= 1
Z Z(- 1)-mqm-1(q - 1)s(1μ-mm1) II hmeμ:- m 
m=1 (m) i2
Since lμul = f we can write this in the form
≥ Z(- 1)u1-m1qm1-1(q - 1)(1-mm) II(- 1)=-miqm* hm:eμ=-m:
m= 1 (m) i=2
Eui-mi '
(m) i=2
where the last sum is over all  sequences of nonnegative integers
(m) =- (mi, m2, . . : , m) such that m1 > O and mi ≤ μi. Summarizing, we may write
(6.1) in the form
(m)
(6.4)
i=2
In the standard fashion (see [Mac]), to each partition  -(21, 22,...) we
associate a diagram of t(a) rows of boxes such that each row i contains a; boxes. If
2, μ are partitions, μ  a, then the skew diagram ^/μ, also denoted  -- μ, is the set
theoretic difference of the diagrams  and μ. A horizontal (resp. vertical) strip is
a skew diagram with at most one box in each column (row). A strip is a skew
diagram that does not contain any 2 x 2 block of boxes. Two boxes are connected if
they have an edge in common. A connected strip is called a hook. Any strip is
a union of connected components, each of which is a hook. As an example, in the
diagram (6.5), the diagonally hatched boxes form a horizontal strip, the cross
hatched boxes form a vertical strip, and together the diagonally hatched boxes and
the vertically hatched boxes form a strip.
Pieri's rule states that
Schm: =Esβ ,
where the sum is over all partitions β such that β/α is a horizontal strip of length mi.
Pictorially the shape of β is produced by adding a horizontal strip of m; boxes to
the shape of α. Similarly,
Saeui-m: = Zsp ,
where this time the sum is over all partitions β such that β/α is a vertical strip of
length μi -- mi.
Thus one can view the product sahm:eui-m as the sum of Schur functions of
shapes obtained by an application of m; boxes in a horizontal strip followed by an
A Frobenius formula for the characters of the Hecke algebras 481
application of μ; -- m; boxes in a vertical strip. In the same fashion the product
each horizontal box contributes a weight of q and each vertical box contributes
a weight of -- 1 to the resulting Schur function. Observe that the result of an
application of m; boxes in a horizontal strip and μi -- m; boxes in a vertical strip to
a shape α produces a shape β such that β/α is a strip of length μi.
(6.5)
Now, consider a strip of length μ; and assume that it arose from an application
of a horizontal strip followed by an application of a vertical strip. The strip is
a union of components each of which is a hook. Any box with a box to its right
must have come from the horizontal application. Any box with a box under it must
have come from the vertical application. In any component only the rightmost
bottommost (end of the hook) box could have been placed by either the horizontal
or the vertical application of boxes.
Not including the ? box, the number of boxes resulting from a vertical application is
equal to the number of rows in the hook minus 1. Similarly, the number of boxes
resulting from a horizontal application is the number of columns in the hook minus
1. If we weight horizontal boxes by q and vertical boxes by -- 1 then the weight of
the hook over all applications (first horizontal boxes and then vertical boxes) which
produce this hook is
g # cols - 1(- 1)# rows - 1(q - 1) .
a horizontal box and the -- 1 in the (q -- 1) factor from the application in which the
? box is a vertical box. The weight of the whole strip is the product of the above
weight over all components in the strip.
In a similar fashion we can view the factor
(- 1)1-m1qm1-1(q - 1)S(1u-mm1)
in (6.4) as having arisen from an application of a strip of length μi to the empty
partition Q.
482 A. Ram
In this case the strip has exactly one component receiving a weight of
In this way we rewrite the sum in (6.1) in the form
(q - 1)(m) wt(T)salsa 
where the sum is over all tableaux T of shape a arising from applications of strips of
lengths μ; and wt(T) is given by
wt(T) = (6.6)
hook
components of T
Define a diagonally strict tableau of shape a and weight μ to be a filling of the
shape a with μi 1's, μ2 2's, etc., such that
(1) the rows of T are weakly increasing from left to right,
(2) the columns of T are weakly increasing from bottom to top,
(3) the diagonals are strictly increasing in the northeast direction.
For each 1 ≤i≤t(u) the i's in T form a strip. A hook component of T is
a component of one of these strips. We have proved the following theorem.
(6.7) Theorem. For any two partitions a, μu  f the value of the irreducible character
x" at the element T, e H, is given by
wt(T) ,
where the sum is over all diagonally strict tableaux T of shape  and weight μu and
wt(T) is given by (6.6).
As an example to illustrate Theorem 6.7 we calculate x^(T,.) for the partitions
 = (42) and μ =- (33). The following gives the diagonally strict tableaux of shape
 and weight μ. x^(T,.) is given by summing the weights (6.6)) of these tableau and
dividing by (q -~ 1)r(2)
12 22
x(42)(T(33)  q)q(q - 1)3 + q²q(q - 1)3) = q4  2q3 + q² 
1)t(μ)
A Frobenius formula for the characters of the Hecke algebras 483
