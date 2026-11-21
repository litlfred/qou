---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
As in [Ma], we assign to a partition a Young diagram, which is denoted by the
same symbol. We identify partitions and Young diagrams, and we denote by Y the
set of all Young diagrams. The conjugation involution of Y (transposition of rows
and columns of a diagram) is denoted as λ 7→λ′.
There is another presentation of Young diagrams, the Frobenius notation. We
shall use its modiﬁcation due to Vershik and Kerov [VeK2]:
λ = (a1, . . ., ad | b1, . . ., bd).
Here d = d(λ) is the length of the main diagonal in λ,
d(λ) = {i | λi ≥i} = {j | λ′
j ≥j},
and
ai = λi −i + 1
2,
bi = λ′
i −i + 1
2,
i = 1, . . ., d(λ).
(1.1)
The numbers ai, bi are called the modiﬁed Frobenius coordinates of λ.
Both
a1, . . ., ad and b1, . . ., bd are strictly decreasing positive proper half–integers, i.e.,
numbers from { 1
2, 3
2, 5
2, . . .}, such that P(ai + bi) = |λ|. Note that the Vershik–
Kerov deﬁnition (1.1) diﬀers from the classical deﬁnition of the Frobenius coordi-
nates, which does not involve one–halves (see [Ma, p. 3]). However, these one–
halves play an important role in what follows.
Note that the conjugation involution λ 7→λ′ has a very simple description in
terms of the Frobenius coordinates:
(a1, . . ., ad | b1, . . ., bd)′ = (b1, . . ., bd | a1, . . ., ad).
(1.2)
One more useful presentation of Young diagrams, due to Kerov, will be given in
§2.
Set
Z′ = Z + 1
2 = {. . . , −3
2, −1
2, 1
2, 3
2, . . .},
Z′
+ = { 1
2, 3
2, . . .},
Z′
−= {. . . , −3
2, −1
2}.
Given λ ∈Y, set
li = λi −i + 1
2 ∈Z′,
i = 1, 2, . . .,
and note that l1 > l2 > . . . . We assign to λ the inﬁnite subset L(λ) = {l1, l2, . . . } ⊂
Z′.
The following claim is a version of the classical Frobenius lemma, see [Ma, ch.
I, (1.7) and Example 1.15 (a)].
Proposition 1.1. Let λ ∈Y be arbitrary.
(i) We have Z′ = L(λ) ⊔(−L(λ′)).
I.e., L(λ) ∩(−L(λ′)) = ∅and L(λ) ∪
(−L(λ′)) = Z′.
(ii) In the notation (1.1),
L(λ) ∩Z′
+ = {a1, . . ., ad},
Z′
−\ L(λ) = −(L(λ′) ∩Z′
+) = {−b1, . . ., −bd}).
Proof. (i) We represent λ as a plane shape in the quarter plane R2
+. Let (r, s) be
the coordinates in R2
+. Here the rows of λ are counted along the ﬁrst coordinate r,
6
