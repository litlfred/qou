---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-013
section_title: "Page 13"
section_number: null
pages: 13-13
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Proposition 2.7. The functions ep2(λ), ep3(λ), . . . belong to the algebra A and are
related to the functions p1(λ), p2(λ) by the relations
epk =
[ k−1
2
]
X
j=0

k
2j + 1

2−2j pk−1−2j ,
k = 2, 3, . . . .
(2.13)
Proof. Formula (2.6) implies that
ln Φ(z −1
2; λ) −ln Φ(z + 1
2; λ) = ln
m
Y
j=1

1 −yj
z

−ln
m+1
Y
i=1

1 −xi
z

.
(2.14)
By Proposition 1.4, the left–hand side equals
∞
X
l=1
pl(λ)
l

1
(z −1
2)l −
1
(z + 1
2)l

=
∞
X
l=1
pl(λ)
l
z−l
 
1 −1
2z
−l
−

1 + 1
2z
−l!
=
∞
X
l=1
∞
X
j=0
l(l + 1) . . .(l + 2j)
(2j + 1)!
pl(λ)
l
z−(l+2j+1)
22j
=
∞
X
l=1
∞
X
j=0
(l + 1) . . .(l + 2j + 1)
(2j + 1)!
pl(λ)
l + 2j + 1
z−(l+2j+1)
22j
.
Setting l + 2j + 1 = k we rewrite this as
∞
X
k=2
[ k−1
2
]
X
j=0

k
2j + 1
 pk−2j−1(λ)
22j
z−k
k
.
(2.15)
By Proposition 2.5, the right–hand side of (2.14) equals
∞
X
k=1
epk(λ) z−k
k
.
(2.16)
Comparing the coeﬃcients of z−k/k in (2.15) and (2.16) we get ep1(λ) ≡0 (which
we already know) and then (2.13).
□
Note that
inv(epk) = (−1)kepk ,
k = 2, 3, . . .,
(2.17)
where ‘inv’ is the involution introduced in Deﬁnition 1.7.
Indeed, (2.17) easily
follows from the deﬁnition of epk and the symmetry property λ′(x) = λ(−x). The
fact that in the right–hand side of (2.13), the subscript varies with step 2 agrees
with the symmetry properties of pk’s and epk’s, see (1.7) and (2.17).
13
