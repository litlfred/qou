---
doc_id: characteristic
doc_title: "ON THE CHARACTERISTIC AND DEFORMATION VARIETIES OF A KNOT"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: characteristic.pdf
source_sha256: 42bd31da2754488f
toc_source: inferred
doc_brief: "ON THE CHARACTERISTIC AND DEFORMATION VARIETIES OF A KNOT — The colored Jones function of a knot is a sequence of Laurent polynomials in one variable, whose nth term is the Jones polynomial of the"
---
Introduction
1
1.1.
The colored Jones function of a knot
1
1.2.
The characteristic variety of a knot
2
1.3.
The deformation variety of a knot
2
1.4.
The conjecture
3
1.5.
Acknowledgement
3
2.
A polynomial version of Conjecture 1
4
2.1.
The A-polynomial of a knot
4
2.2.
A noncommutative version of the A-polynomial
4
2.3.
Computing the Aq polynomial of a knot
5
3.
Proof of the conjecture for the Trefoil and Figure 8 knots
6
3.1.
The colored Jones function and the A-polynomial of the 31 and 41 knots
6
3.2.
Computer calculations
6
4.
Higher rank groups
11
References
12
1. Introduction
1.1. The colored Jones function of a knot. The colored Jones function
JK :

−→
 [q±]
Date: December 15, 2003
First edition: May 1, 2003.
The author was supported in part by NSF and BSF.
1991 Mathematics Classiﬁcation. Primary 57N10. Secondary 57M25.
Key words and phrases: q-holonomic functions, D-modules, characteristic variety, deformation variety, colored Jones function,
multisums, hypergeometric functions, WZ algorithm.
1
of a knot K in 3-space is a sequence of Laurent polynomials, whose nth term JK(n) is the Jones polynomial
of a knot colored with the n-dimensional irreducible representation of sl2; see [Tu]. We will normalize it by
Junknot(n) = 1 for all n, and (for those who worry about framings), we will assume that K is zero-framed.
The ﬁrst two terms of the colored Jones function of a knot K are better known. Indeed, JK(1) = 1, and
JK(2) coincides with the Jones polynomial of a knot K, deﬁned by Jones in [J]. Although we will not use
it, note that the colored Jones function of a knot essentially encodes the Jones polynomial of a knot and its
connected parallels.
The starting point for our paper is the key property that the colored Jones function is q-holonomic, as
was shown in joint work with TTQ Le; see [GL]. Informally, a q-holonomic function is one that satisﬁes
a nontrivial linear recursion relation, with appropriate coeﬃcients. A convenient way to describe recursion
relations is the operator point of view which we now describe.
