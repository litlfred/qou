---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-005-formulae-for-the-first-terms-in-magnus-expansion
section_title: "Formulae for the first terms in Magnus expansion"
section_number: null
pages: 11-12
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Suppose now that A is of first order in some parameter ε and try a solution in the form of a series
Ω(t) =
∞
X
n=1
Ωn(t),
(40)
where Ωn is supposed to be of order εn. Equivalently, we replace A by εA in (30) and determine the successive terms of
Ω(t) =
∞
X
n=1
εnΩn(t).
(41)
This can be done explicitly, at least for the first terms, by substituting the series (41) in (39) and equating powers of ε.
Obviously, the Magnus series (40) is recovered by taking ε = 1. Thus, using the notation A(ti) ≡Ai, the first four orders
read
(1) Ω′
1 = A, so that
Ω1(t) =
Z t
0
dt1A1.
(42)
(2) Ω′
2 = −1
2[Ω1, A]. Thus
Ω2(t) =
1
2
Z t
0
dt1
Z t1
0
dt2[A1, A2].
(43)
(3) Ω′
3 = −1
2[Ω2, A] +
1
12[Ω1, [Ω1, A]]. After some work, and using the formula
Z α
0
dx
Z x
0
f (x, y)dy =
Z α
0
dy
Z α
y
f (x, y)dx
(44)
162
S. Blanes et al. / Physics Reports 470 (2009) 151–238
we obtain
Ω3(t) =
1
6
Z t
0
dt1
Z t1
0
dt2
Z t2
0
dt3{[A1, [A2, A3]] + [[A1, A2], A3]}.
(45)
(4) Ω′
4 = −1
2[Ω3, A] +
1
12[Ω2, [Ω1, A]] +
1
12[Ω1, [Ω2, A]], which yields
Ω4(t) =
1
12
Z t
0
dt1
Z t1
0
dt2
Z t2
0
dt3
Z t3
0
dt4{[[[A1, A2], A3]A4]
+ [A1, [[A2, A3], A4]] + [A1, [A2, [A3, A4]]] + [A2, [A3, [A4, A1]]]}.
(46)
The apparent symmetry in the formulae above is deceptive. High orders require repeated use of (44) and become unwieldy.
Prato and Lamberti [49] give explicitly the fifth order using an algorithmic point of view. One can also find in the literature,
quite involved explicit expressions for an arbitrary order [50–54]. In the next subsection we describe a recursive procedure
to generate the terms in the expansion.
