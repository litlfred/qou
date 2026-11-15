---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mos"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
toc_source: outline
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
Khovanov polynomials for satellites and asymptotic adjoint polynomials
A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡
ITEP/TH-09/21
IITP/TH-06/21
MIPT/TH-05/21
a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia
b Institute for Information Transmission Problems, Moscow 127994, Russia
c Moscow Institute of Physics and Technology, Dolgoprudny 141701, Russia
∗anokhina@itep.ru † morozov.itep@mail.ru ‡ popolit@gmail.com
Abstract
We compute explicitly the Khovanov polynomials (using the computer program from katlas.org) for
the two simplest families of the satellite knots, which are the twisted Whitehead doubles and the two-
strand cables. We ﬁnd that a quantum group decomposition for the HOMFLY polynomial of a satellite
knot can be extended to the Khovanov polynomial, whose quantum group properties are not manifest.
Namely, the Khovanov polynomial of a twisted Whitehead double or two-strand cable (the two simplest
satellite families) can be presented as a naively deformed linear combination of the pattern and companion
invariants. For a given companion, the satellite polynomial “smoothly” depends on the pattern but for
the “jump” at one critical point deﬁned by the s-invariant of the companion knot. A similar phenomenon
is known for the knot Floer homology and τ-invariant for the same kind of satellites
Contents
Introduction
2
2
The knots we study and the questions we ask
3
2.1
Coloured decompositions for the simplest satellites . . . . . . . . . . . . . . . . . . . . . . . .
4
2.2
The pattern decomposition
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.3
How to get the satellite class from a knot diagram
. . . . . . . . . . . . . . . . . . . . . . . .
5
2.4
Summary of Jones formulae . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
3
Khovanov-evolution formulae for satellite families
6
3.1
Preliminaries
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
3.2
Positive pattern-companion decompositions . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.3
False adjoint Khovanov polynomials
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
4
Explicit form of the pattern and companion invariants
8
4.1
The pattern-deﬁning polynomial
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
4.2
AAK for the simplest prime knots
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
4.3
AAK for the two-strand torus knots
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
4.3.1
General formulae . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
4.3.2
Reduced vs unreduced polynomials . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
4.3.3
Mirror symmetry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
4.4
AAK for the twist knots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
4.4.1
General formulae . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
4.4.2
Why there is no mirror symmetry? . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
4.5
Double-evolution phase diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
5
Eigenvalue expressions, polynomiality and positivity
11
1
arXiv:2104.14491v1  [hep-th]  29 Apr 2021
6
Possible applications and further development
12
A Cabling and an invariant deﬁnition of the m-strand satellite
16
B First symmetric polynomials for the simplest knot families
17
B.1
Two-strand torus knots
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
B.2
Twist knots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
C Technical guidance to the experimental data
19
C.1
Simplest knots
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
C.2
Simplest knot families . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
C.3
Precaution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
