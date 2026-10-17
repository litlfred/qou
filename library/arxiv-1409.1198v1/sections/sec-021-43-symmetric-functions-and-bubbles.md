---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-021-43-symmetric-functions-and-bubbles
section_title: "Symmetric functions and bubbles"
section_number: 4.3
pages: 27-29
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
is remarkably rich. A prominent role is played by the non-nested dotted bubbles of a ﬁxed orientation
since any closed diagram in the graphical calculus for UQ(sln) can be reduced to composites of such
diagrams.
There is a beautiful analogy between dotted bubbles in the graphical calculus and various bases for
the ring of symmetric functions. In [37] it is shown that there is an isomorphism
ψλ :
Sym
−→
Z(λ) = UQ(sl2)(1λ, 1λ)
(4.35)
hr
7→
i

M
•
♠+r
λ
28
ANNA BELIAKOVA, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. LAUDA
(−1)ses
7→
i
Q

•
♠+s
λ
where Sym denotes the ring of symmetric functions, hr denotes the complete symmetric function of
degree r, and es denotes the elementary symmetric function of degree s. In fact, under this isomor-
phisms the well known relationship between complete and elementary symmetric functions becomes
the inﬁnite Grassmannian equation (4.24).
It is well known that for a partition λ = (λ1, . . . , λn) with λ1 ≥λ2 ≥· · · ≥λn, products of
elementary symmetric functions eλ = eλ1 . . . eλn form a basis for Sym, see for example [46]. Likewise,
products of complete symmetric functions also provide a basis for Sym. This mirrors the fact that any
closed diagram in the graphical calculus for UQ(sl2) can be reduced to a product on non-nested bubbles
of a given orientation.
In the sln calculus of the 2-category U(sln), we have the isomorphism
ψλ :
Y
i∈I
Sym
−→
Z(λ) = UQ(sln)(1λ, 1λ)
since any closed diagram can still be reduced to products of non-nested closed bubbles labelled by
i ∈I.
In what follows, it will be interesting to consider which products of closed diagrams correspond to
the basis of Sym given by the power sum pr symmetric functions. Using a formula that expresses power
sum symmetric functions in terms of products of complete and elementary symmetric functions, we
can denote by pi,r(λ) for r > 0, the image of the power symmetric polynomial on i-labelled strands in
Z(λ):
(4.36)
pi,r(λ) :=
X
a+b=r
(a + 1)
i

M
•
♠+a
i
Q

•
♠+b
λ
= −
X
a+b=r
(b + 1)
i

M
•
♠+a
i
Q

•
♠+b
λ
= −
X
a+b=r
a
i

M
•
♠+b
i
Q

•
♠+a
λ
For later convenience we set pi,0(λ) = λi.
Exercise 18. Using the bubble slide formulas from exercise 17, show that
pi,r(λ) =















































−
λ
P

i
•
♠+r

O
i
•
♠+0
if λi ≥0
λ

M
i
•
♠+r
O

i
•
♠+0
if λi ≤0,
so that the formulas deﬁning pr(λ) can be obtained by simplifying a degree r bubble with one orientation
nested inside of a degree zero bubble with the opposite orientation.
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR
29
Note that other interesting basis for symmetric functions also have natural graphical analogs. In
[34] diagrams corresponding to the basis of Schur functions are given.
Exercise 19. Using the bubble sliding equations from exercise 17, prove the following power sum slide
rules
λ −αj
O
j
pi,r(λ −αj)
=









































λ
O
j
pi,r(λ)
−2
λ
O
j
• r
if i = j,
λ
O
j
pi,r(λ)
if i · j = 0,
λ
O
j
pi,r(λ)
−(−t−1
ij tji)r
λ
O
j
• r
if i · j = −1
(4.37)
λ
O
j
pi,r(λ + αj)
=





























λ
O
j
pi,r(λ) + 2
λ
O
j
• r
if i = j,
λ
O
j
pi,r(λ) + (−t−1
ij tji)r
λ
O
j
• r
if i · j = −1
(4.38)
