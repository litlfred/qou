---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-006-magnus-expansion-generator
section_title: "Magnus expansion generator"
section_number: null
pages: 12-12
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
The above procedure can, indeed, provide a recursive procedure to generate all the terms in the Magnus series (40). Thus,
by substituting Ω(t) = P∞
n=1 Ωn into Eq. (39) and equating terms of the same order, one gets in general
Ω′
1 = A
Ω′
n =
n−1
X
j=1
Bj
j!
S(j)
n ,
n ≥2,
(47)
where
S(k)
n
=
X
[Ωi1, [. . . [Ωik, A] . . .]]
(i1 + · · · + ik = n −1).
(48)
Notice that, in the last equation, the order in A has been explicitly reckoned, whereas k represents the number of Ω’s. The
newly defined operators S(k)
n
can again be calculated recursively. The recurrence relations are now given by
S(j)
n =
n−j
X
m=1
h
Ωm, S(j−1)
n−m
i
,
2 ≤j ≤n −1
(49)
S(1)
n
= [Ωn−1, A] ,
S(n−1)
n
= adn−1
Ω1 (A).
After integration we reach the final result in the form
Ω1 =
Z t
0
A(τ)dτ
Ωn =
n−1
X
j=1
Bj
j!
Z t
0
S(j)
n (τ)dτ,
n ≥2.
(50)
Alternatively, the expression of S(k)
n
given by (48) can be inserted into (50), thus arriving at
Ωn(t) =
n−1
X
j=1
Bj
j!
X
k1+···+kj=n−1
k1≥1,...,kj≥1
Z t
0
adΩk1(s) adΩk2(s) · · · adΩkj(s)A(s)ds
n ≥2.
(51)
Notice that each term Ωn(t) in the Magnus series is a multiple integral of combinations of n −1 nested commutators
containing n operators A(t). If, in particular, A(t) belongs to some Lie algebra g, then it is clear that Ω(t) (and in fact
any truncation of the Magnus series) also stays in g and therefore exp(Ω) ∈G, where G denotes the Lie group whose
corresponding Lie algebra (the tangent space at the identity of G) is g.
