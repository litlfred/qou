---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-014-magnus-expansion-and-the-bch-formula
section_title: "Magnus expansion and the BCH formula"
section_number: null
pages: 21-22
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
The Magnus expansion can also be used to explicitly obtain the terms of the series Z in
Z = log(eX1 eX2),
X1 and X2 being two non commuting indeterminate variables. As it is well known [41],
Z = X1 + X2 +
∞
X
n=2
Gn(X1, X2),
(81)
where Gn(X1, X2) is a homogeneous Lie polynomial in X1 and X2 of grade n; in other words, Gn can be expressed in terms
of X1 and X2 by addition, multiplication by rational numbers and nested commutators. This result is often known as the
Baker–Campbell–Hausdorff (BCH) theorem and proves to be very useful in various fields of mathematics (theory of linear
differential equations [4], Lie group theory [78], numerical analysis [79]) and theoretical physics (perturbation theory,
transformation theory, Quantum Mechanics and Statistical Mechanics [19,80,81]). In particular, in the theory of Lie groups,
with this theorem one can explicitly write the operation of multiplication in a Lie group in canonical coordinates in terms
of the Lie bracket operation in its algebra and also prove the existence of a local Lie group with a given Lie algebra [78].
If X1 and X2 are matrices and one considers the piecewise constant matrix-valued function
A(t) =

X2
0 ≤t ≤1
X1
1 < t ≤2
(82)
then the exact solution of (30) at t = 2 is Y(2) = eX1 eX2. By computing Y(2) = eΩ(2) with recursion (51) one gets for the
first terms
Ω1(2) = X1 + X2
Ω2(2) =
1
2[X1, X2]
(83)
Ω3(2) =
1
12[X1, [X1, X2]] −
1
12[X2, [X1, X2]]
Ω4(2) =
1
24[X1, [X2, [X2, X1]]].
In general, each Gn(X1, X2) is a linear combination of the commutators of the form [V1, [V2, . . . , [Vn−1, Vn] . . .]] with
Vi ∈{X1, X2} for 1 ≤i ≤n, the coefficients being universal rational constants. This is perhaps one of the reasons why
the Magnus expansion is often referred to in the literature as the continuous analogue of the BCH formula. As a matter of
fact, Magnus proposed a different method for obtaining the first terms in the series (40) based on (81) [4].
172
S. Blanes et al. / Physics Reports 470 (2009) 151–238
Now we can apply Theorem 9 and obtain the following sharp bound.
Theorem 10. The Baker–Campbell–Hausdorff series in the form (81) converges absolutely when ∥X1∥+ ∥X2∥< π.
This result can be generalized, of course, to any number of non commuting operators X1, X2, . . . , Xq. Specifically, the series
Z = log(eX1 eX2 · · · eXq),
converges absolutely if ∥X1∥+ ∥X2∥+ · · · + ∥Xq∥< π.
