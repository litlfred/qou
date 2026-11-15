---
doc_id: characteristic
doc_title: "ON THE CHARACTERISTIC AND DEFORMATION VARIETIES OF A KNOT"
section_id: sec-010-31-the-colored-jones-function-and-the-a-polynomi
section_title: "The colored Jones function and the A-polynomial of the 31 and 41 knots"
section_number: 3.1
pages: 6-6
source_pdf: characteristic.pdf
source_sha256: 42bd31da2754488f
toc_source: inferred
doc_brief: "ON THE CHARACTERISTIC AND DEFORMATION VARIETIES OF A KNOT — The colored Jones function of a knot is a sequence of Laurent polynomials in one variable, whose nth term is the Jones polynomial of the"
---
give the following formula for the colored Jones function of the left handed trefoil (31) and Figure 8 (41)
knots:
J31(n)
=
∞
X
k=0
(−1)kqk(k+3)/2qnk(q−n−1; q−1)k(q−n+1; q)k
(4)
J41(n)
=
∞
X
k=0
qnk(q−n−1; q−1)k(q−n+1; q)k.
(5)
where we deﬁne the rising and falling factorials for k > 0 by:
(a; q)k = (1 −a)(1 −aq) . . . (1 −aqk−1)
(a; q−1)k = (1 −a)(1 −aq−1) . . . (1 −aq−k+1)
and (a; q)0 = (a; q)0 = 1. Notice that the sums in in Equations (4) and (5) have compact support, namely
for each positive n, only the terms with k ≤n contribute.
These formulas are discussed in detail in Masbaum [Ma, Thm.5.1], in relation to the cyclotomic expansion
of the colored Jones function of twist knots. To compare Masbaum’s formula with the one given above, keep
in mind that:
S(n, k)
:=
qnk(q−n−1; q−1)k(q−n+1; q)k
=
{n −k}{n −k + 1} . . . {n + k}
{n}
=
k
Y
j=1
((qn/2 −q−n/2)2 −(qj/2 −q−j/2)2)
where {m} = qm/2 −q−m/2.
On the other hand, [CCGLS] compute the A-polynomial of the 31 and 41 knots, as follows:
A(31)
=
(L −1)(L + M 6)
(6)
A(41)
=
(L −1)(−L + LM 2 + M 4 + 2LM 4 + L2M 4 + LM 6 −LM 8)
(7)
where we include the factor L −1 in the A-polynomial which corresponds to the abelian representations of
the knot complement.
