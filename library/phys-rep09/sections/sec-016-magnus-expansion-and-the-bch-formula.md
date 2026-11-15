---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-016-magnus-expansion-and-the-bch-formula
section_title: "Magnus expansion and the BCH formula"
section_number: null
pages: 21-22
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The Magnus expansion can also be used to explicitly obtain the terms of the series Z in
Z = log(e™! e%2),
X, and X2 being two non commuting indeterminate variables. As it is well known [41],

00

Z =X, +X + D> GAG, X2), (81)

n=2
where G,,(X1, X2) is a homogeneous Lie polynomial in X; and X2 of grade n; in other words, G, can be expressed in terms
of X; and X2 by addition, multiplication by rational numbers and nested commutators. This result is often known as the
Baker-Campbell-Hausdorff (BCH) theorem and proves to be very useful in various fields of mathematics (theory of linear
differential equations [4], Lie group theory [78], numerical analysis [79]) and theoretical physics (perturbation theory,
transformation theory, Quantum Mechanics and Statistical Mechanics [19,80,81]). In particular, in the theory of Lie groups,
with this theorem one can explicitly write the operation of multiplication in a Lie group in canonical coordinates in terms
of the Lie bracket operation in its algebra and also prove the existence of a local Lie group with a given Lie algebra [78].
If X; and X2 are matrices and one considers the piecewise constant matrix-valued function

_ fx. O<t<1
AO = tk 1<t<2 (82)
then the exact solution of (30) at t = 2 is Y(2) = e*! e*2. By computing Y(2) = e®) with recursion (51) one gets for the
first terms
2\(2) =X +X

1

22(2) = 7X1. Xa] (83)
1 1

23(2) = prince [X1, X2]] — pranch [X1, X2]]

1
24(2) = Pyne [X2, [Xo, Xi]]]-

In general, each G,(X1, X2) is a linear combination of the commutators of the form [Vj, [V2,...,[Vn—1, Va]..-J] with
Vi © {X1,X2} for 1 < i < n, the coefficients being universal rational constants. This is perhaps one of the reasons why
the Magnus expansion is often referred to in the literature as the continuous analogue of the BCH formula. As a matter of
fact, Magnus proposed a different method for obtaining the first terms in the series (40) based on (81) [4].
172 S. Blanes et al. / Physics Reports 470 (2009) 151-238

Now we can apply Theorem 9 and obtain the following sharp bound.

Theorem 10. The Baker-Campbell-Hausdorff series in the form (81) converges absolutely when ||X;|| + ||X2|| <2.
This result can be generalized, of course, to any number of non commuting operators Xj, X2, . . . , Xq. Specifically, the series
Z = log(e*! e&® ... eXa),

converges absolutely if ||X1|| + [|X|] + «+» + [|Xqll < 2.
