---
doc_id: descendants-colored-jones
doc_title: "Pure and Applied Mathematics Quarterly"
section_id: sec-001-the-descendant-colored-jones-polynomials-of-a-kn
section_title: "The descendant colored Jones polynomials of a knot"
section_number: null
pages: 3-5
source_pdf: descendants_colored_jones.pdf
source_sha256: f00693a5926c074f
doc_brief: "Pure and Applied Mathematics Quarterly The descendant colored Jones polynomials — We discuss two realizations of the colored Jones polyno- mials of a knot, one appearing in an unnoticed work of the"
---
2.1. A conjectured matrix-valued invariant from [ GZ, GZ23]
We begin by explaining the most recent reappearance of the colored Jones
polynomials. An extension of the Volume Conjecture is the Quantum Mod-
ularity Conjecture of Zagier [ Zag10] which, roughly speaking, discusses the
asymptotics of the Kashaev invariant at roots of unity. More recently, a Re-
ﬁned Quantum Modularity Conjecture was proposed in [ GZ] which suggests
the existence of a matrix-valued invariant deﬁned at (and near) roots of unity.
These conjectured matrix-valued invariants (denoted by J(x)f o r x ∈
Q/Z)
were studied in [ GZ, Sec. 5] with explicit examples given for the 4 1 and the
52 knots in Sections 7.1 and 7.2 of [ GZ], respectively.
The conjectured matrix-valued knot invariant J (deﬁned as a 1-periodic
function at the rationals, or alternatively as a function at the complex roots
of unity), has many interesting analytic, arithmetic properties and geometric
properties which are listed in detail in the introduction (Part 0) of [ GZ]. The
rows and columns of the matrix J are parametrized by the set of bound-
ary parabolic SL
2(C)-representations of the knot (assuming the latter set
is ﬁnite), and this set always contains two distinguished elements, the triv-
ial representation σ
0, and the geometric representation σ1 of a hyperbolic
knot. The σ0-column of J is (1, 0,..., 0)t but the σ0-row is very interesting.
Its (σ0,σ 1)-entry is the Kashaev invariant of a knot, whereas the remaining
entries are expected to be elements of the Habiro ring (whose deﬁnition is
recalled below), tensored with the rational numbers. Moreover, the entries
of each row of the matrix are expected to extend to sequences that satisfy
a homogeneous recursion relation (if not the σ
0-row), or an inhomogeneous
recursion (if the σ0-row). In other words, the matrix J is expected to be a
fundamental matrix solution of a q-holonomic module.
2310 Stavros Garoufalidis and Rinat Kashaev
In [Zag10, Sec. 7.3,7.4] a method was proposed for deﬁning all but the
ﬁrst row of this matrix, given a suitable ideal triangulation of the knot. But
the ﬁrst row of the above matrix remained elusive. The goal of this paper is
to propose a deﬁnition for this ﬁrst row and verify some of its conjectured
properties. After a linear change of variables, the ﬁrst row of the matrix J is
conjecturally equal to one of the best-known quantum knot invariants, namely
the colored Jones polynomials; see Conjecture 2.4 below.
2.2. Deﬁnition of the descendants
In this section we extend the 2-parameter colored Jones function J
n(q)o fa
knot in 3-space into a 3-parameterdescendant colored Jonesfunction DJ(m)
n (q)
for n ≥ 0, m ∈ Z,w h i c h
• specializes to the colored Jones polynomials J n(q)w h e nm =0a n d
n ≥ 1;
• specializes to a sequence of elements of the Habiro ring DJ (m)(q)w h e n
n =0 ;
• is determined by either of the above specializations;
• is determined by a 3-parameter function DJ (m)(x, q)b yD J (m)
n (q)=
DJ(m)(qn,q ) for all n ≥ 1.
In other words, we have a commutative diagram
(1)
DJ(m)
n (q)
Jn(q) DJ(m)(q)
DJ(m)(x, q)
+
m=0 QQQQs
n=06
x=qn
QQQQk
3
To deﬁne the functions appearing in this diagram, we start with the colored
Jones polynomials J K
n (q) ∈ Z[q±]o fak n o t K (mostly omitted from the
notation), colored by the n-dimensional irreducible representation of sl2 for
n ≥ 1 and normalized to be 1 at the unknot [Tur94]. In [Hab08]H a b i r op r o v e d
that the colored Jones polynomials can be written in the form
(2) J n(q)=
∞∑
k=0
cn,k(q)Hk(q),c n,k(q)= q−kn(qn+1; q)k(qn−1; q−1)k
The descendant colored Jones polynomials 2311
where Hk(q) ∈ Z[q±] for all k ≥ 0a n dcn,k(q) is the cyclotomic kernel which
is independent of the knot and vanishes when k ≥ n ≥ 1. Equation ( 2)c a n
be inverted [Hab08,L e m .6 . 1 ]
Hk(q)=
k+1∑
n=1
γk,n(q)Jn(q),
γk,n(q)=( −1)k−n−1 q
k(k+3)+n(n−3)
2 +1(1 − qn)(1 − q2n)
(q; q)k+n+1(q; q)k−n+1
(3)
where γk,n(q)=0f o r n ≥ k+2 and k ≥ 0. There are three important features
in Habiro’s expansion ( 2) of the colored Jones polynomials.
(i) The Habiro polynomials H k(q) which a priori lie in Q(q) (as follows
from (3)), actually lie in Z[q±].
(ii) Setting n = 0 in the right hand side of ( 2) gives a well-deﬁned element
of the Habiro ring ˆZ[q] = lim←−n Z[q]/((q; q)n).
(ii) The dependence on the color comes only through the cyclotomic kernel
cn,k(q). Thus, one can replace qn by a variable x and deﬁne an element
J(x, q) of the colored Habiro ring Λ = lim←−n Z[q±][x+x−1 −2]/(cn(x, q)),
so that J(qn,q )=J n(q)f o rn ≥ 1, where
J(x, q)=
∞∑
k=0
ck(x, q)Hk(q),c k(x, q)= x−k(qx; q)k(q−1x; q−1)k.(4)
We now have all the ingredients to deﬁne the descendant colored Jones
function.
Deﬁnition 2.1. For an integer m and for n ≥ 0, we deﬁne
DJ(m)
n (q)=
∞∑
k=0
cn,k(q)Hk(q) qkm, DJ(m)(x, q)=
∞∑
k=0
ck(x, q)Hk(q)qkm(5)
and
(6) DJ (m)(q)=
∞∑
k=0
(q; q)k(q−1; q−1)kHk(q) qkm.
