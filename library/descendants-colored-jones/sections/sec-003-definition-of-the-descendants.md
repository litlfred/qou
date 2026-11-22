---
doc_id: descendants-colored-jones
doc_title: "The descendant colored Jones polynomials"
section_id: sec-003-definition-of-the-descendants
section_title: "Definition of the descendants"
section_number: null
pages: 4-5
source_pdf: descendants_colored_jones.pdf
source_sha256: f00693a5926c074f
toc_source: outline
doc_brief: "The descendant colored Jones polynomials — We discuss two realizations of the colored Jones polyno- mials of a knot, one appearing in an unnoticed work of the second author in 1994 on quantum"
---
In this section we extend the 2-parameter colored Jones function Jn(q) of a
knot in 3-space into a 3-parameter descendant colored Jones function DJ(m)
n
(q)
for n ≥0, m ∈Z, which
• specializes to the colored Jones polynomials Jn(q) when m = 0 and
n ≥1;
• specializes to a sequence of elements of the Habiro ring DJ(m)(q) when
n = 0;
• is determined by either of the above specializations;
• is determined by a 3-parameter function DJ(m)(x, q) by DJ(m)
n
(q) =
DJ(m)(qn, q) for all n ≥1.
In other words, we have a commutative diagram
(1)
DJ(m)
n
(q)
Jn(q)
DJ(m)(q)
DJ(m)(x, q)




+
m=0
QQQQ
s
n=0
6
x=qn
Q
Q
Q
Q
k

3
To deﬁne the functions appearing in this diagram, we start with the colored
Jones polynomials JK
n (q) ∈Z[q±] of a knot K (mostly omitted from the
notation), colored by the n-dimensional irreducible representation of sl2 for
n ≥1 and normalized to be 1 at the unknot [Tur94]. In [Hab08] Habiro proved
that the colored Jones polynomials can be written in the form
(2)
Jn(q) =
∞

k=0
cn,k(q)Hk(q),
cn,k(q) = q−kn(qn+1; q)k(qn−1; q−1)k
The descendant colored Jones polynomials
2311
where Hk(q) ∈Z[q±] for all k ≥0 and cn,k(q) is the cyclotomic kernel which
is independent of the knot and vanishes when k ≥n ≥1. Equation (2) can
be inverted [Hab08, Lem. 6.1]
Hk(q) =
k+1

n=1
γk,n(q)Jn(q),
γk,n(q) = (−1)k−n−1 q
k(k+3)+n(n−3)
2
+1(1 −qn)(1 −q2n)
(q; q)k+n+1(q; q)k−n+1
(3)
where γk,n(q) = 0 for n ≥k+2 and k ≥0. There are three important features
in Habiro’s expansion (2) of the colored Jones polynomials.
(i) The Habiro polynomials Hk(q) which a priori lie in Q(q) (as follows
from (3)), actually lie in Z[q±].
(ii) Setting n = 0 in the right hand side of (2) gives a well-deﬁned element
of the Habiro ring 
Z[q] = lim
←−n Z[q]/((q; q)n).
(ii) The dependence on the color comes only through the cyclotomic kernel
cn,k(q). Thus, one can replace qn by a variable x and deﬁne an element
J(x, q) of the colored Habiro ring Λ = lim
←−n Z[q±][x+x−1−2]/(cn(x, q)),
so that J(qn, q) = Jn(q) for n ≥1, where
J(x, q) =
∞

k=0
ck(x, q)Hk(q),
ck(x, q) = x−k(qx; q)k(q−1x; q−1)k.
(4)
We now have all the ingredients to deﬁne the descendant colored Jones
function.
Deﬁnition 2.1. For an integer m and for n ≥0, we deﬁne
DJ(m)
n
(q) =
∞

k=0
cn,k(q)Hk(q) qkm, DJ(m)(x, q) =
∞

k=0
ck(x, q)Hk(q)qkm
(5)
and
(6)
DJ(m)(q) =
∞

k=0
(q; q)k(q−1; q−1)kHk(q) qkm.
