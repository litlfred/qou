---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-036
section_title: "Page 36"
section_number: null
pages: 36-36
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
We have
wt((p#
1 )ν1(p#
2 )ν2 . . .) = ∥ν∥,
deg1((p#
1 )ν1(p#
2 )ν2 . . .) ≤∥ν∥′.
By Proposition 3.7, we know all coeﬃcients aν with the maximal value of ∥ν∥(it
equals k), while we need all coeﬃcients with ∥ν∥′ ≥k −1. By (7.10), ∥ν∥′ does not
exceed k, and there are 3 possible cases:
• ∥ν∥′ = ∥ν∥= k. Then ν2 = ν3 = · · · = 0, k = 2ν1, so that k is even; write it
as 2m. The corresponding monomial is (p#
1 )k/2.
• ∥ν∥′ = k −1, ∥ν∥= k. Then ν2 + ν3 + · · · = 1, i.e., exactly one of the numbers
ν2,ν3, . . . equals 1. The corresponding monomial is of the form
p#
k−1−2j(p#
1 )j ,
j = ν1 = 0, 1, . . ., [ k−3
2 ].
(7.11)
• ∥ν∥′ = ∥ν∥= k −1. Then ν2 = ν3 = · · · = 0, k is odd, and the corresponding
monomial is (p#
1 )(k−1)/2.
In the ﬁrst and second cases, ∥ν∥takes the maximal value k, and then the
coeﬃcients aν are known from Proposition 3.7. In the third case, ∥ν∥is no longer
maximal, so that Proposition 3.7 does not tell us what is the coeﬃcient. However,
an additional argument will imply that it is actually 0.
Indeed, in the third case k must be odd, which implies that epk is antisymmetric
with respect to “inv”, see (2.17).
On the other hand, by virtue of (4.10), any
monomial in p#
1 , p#
2 , . . . is either symmetric or antisymmetric. Therefore, in the
expansion of epk only antisymmetric monomials can occur. Since p#
1 is symmetric,
the monomial (p#
1 )(k−1)/2 is also symmetric, so that it does not appear.
Thus, we have proved that the top degree component of epk is obtained from the
top weight terms as given in Proposition 3.7; we simply keep all terms proportional
either to (p#
1 )k/2 or to a monomial of the form (7.11), and remove all the remaining
terms. This procedure leads to (7.9).
□
In the next proposition we invert (7.8).
Proposition 7.4. For any k ≥2,
p#
k
(p#
1 )k/2 =
[ k−2
2
]
X
j=0
(−1)j
k
k −j
k −j
j

qk−2j + . . . ,
(7.12)
where dots mean a remainder term with deg1( · ) < 0.
Proof. We employ the following combinatorial inversion formula, see [Ri, §2.4, (10)]:
Let a0, a1, a2, . . ., b0, b1, b2, . . . be formal variables. Then


ak =
[k/2]
X
j=0
k
j

bk−2j



k=0,1,...
⇐⇒


bk =
[k/2]
X
j=0
(−1)j
k
k −j
k −j
j

ak−2j



k=0,1,...
(7.13)
36
