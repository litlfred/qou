---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-038-from-magnus-to-fer-and-cayley-methods
section_title: "From Magnus to Fer and Cayley methods"
section_number: null
pages: 56-56
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
For arbitrary matrix Lie groups, it is feasible to design numerical methods based also on the Fer and Wilcox expansions,
whereas for the J-orthogonal group (Eq. (21)) the Cayley transform also maps the Lie algebra onto the Lie group [41] and
thus it allows us to build a new class of Lie-group methods. Here we briefly show how these integration methods can be
easily constructed from the previous schemes, based on Magnus. In other words, if the solution of (223) in a neighborhood
of t0 is written as
Y(t0 + h) = eΩ(h) Y0
(Magnus)
(259)
= eF1(h)eF2(h) · · · Y0
(Fer)
(260)
= eS1(h)eS2(h) · · · eS2(h)eS1(h)Y0
(Symmetric Fer)
(261)
=

I −
1
2
C(h)
−1 
I +
1
2
C(h)

Y0
(Cayley)
(262)
one may express the functions Fi(h), Si(h) and C(h) in terms of the successive approximations to Ωand, by using the same
techniques as in the previous section, obtain the new methods. As the schemes based on the Wilcox factorization are quite
similar as the Fer methods, they will not be considered here.
