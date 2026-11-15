---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-035
section_title: "Page 35"
section_number: null
pages: 35-35
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
By Propositions 2.2 and 5.3, for any k = 0, 1, . . .,
√n
Z
R
xk Ω(x) −|x|
2
dx =
√n epk+2[Ω]
(k + 1)(k + 2)
=
√n
(k + 1)(k + 2) ·



(2m)!
m!m! ,
if k is even, k = 2m −2, where m = 1, 2, . . .,
0,
if k is odd.
Combining this with the deﬁnition of q1, q2, . . ., we get (7.7).
□
In order to apply Theorem 6.1 we need the expression of p#
k in terms of q2, q3, . . .
within lower degree terms. We obtain this in two steps. First, using a trick, we
deduce from Proposition 3.7 a formula expressing any qk through p#
2 , p#
3 , . . . , up
to lower degree terms.
See Proposition 7.3.
Next, we invert this formula, see
Proposition 7.4. One could derive the result directly from Proposition 3.3 but this
way turns out to be more diﬃcult.
Proposition 7.3. For any k = 2, 3, . . .,
qk =
[ k−2
2
]
X
j=0
k
j

p#
k−2j
(p#
1 )(k−2j)/2 + . . . ,
(7.8)
where dots mean a remainder term with deg1( · ) < 0.
Note that the elements occurring in the numerator of the right–hand side are
p#
2 , p#
3 , . . . but not p#
1 .
Proof. The claim of the proposition is equivalent to the following: for any k =
3, 4, . . .,
epk =
[ k−3
2
]
X
j=0
k↓j+1
j!
p#
k−1−2j (p#
1 )j +



(2m)!
m!m! (p#
1 )m,
if k is even, k = 2m,
0,
if k is odd.
+terms with deg1( · ) < k −1.
(7.9)
We shall deduce this from Proposition 3.7, which expresses epk as a polynomial in
p#
1 , p#
2 , . . . , up to terms of lower weight. A nontrivial point is how to switch from
the weight ﬁltration to the Kerov ﬁltration.
Write the exact expansion of epk through p#
1 , p#
2 , . . .,
epk =
X
ν
aν (p#
1 )ν1(p#
2 )ν2 . . . ,
where aν are certain coeﬃcients. Let us set
∥ν∥= 2ν1 + 3ν2 + 4ν3 + . . . ,
∥ν∥′ = 2ν1 + 2ν2 + 3ν3 + . . . ,
so that
∥ν∥′ = ∥ν∥−(ν2 + ν3 + . . . ).
(7.10)
35
