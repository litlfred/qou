---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-012
section_title: "Page 12"
section_number: null
pages: 12-12
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Next, consider a horizontal piece below the main diagonal. Such a piece sits
between the diagonal lines s −r = xk and s −r = yk, where 1 ≤k ≤l −1. In this
piece, the column Frobenius coordinates make up the sequence
−(xk + 1
2),
−(xk + 3
2),
. . . ,
−(yk −3
2),
−(yk −1
2),
whose contribution to the product Qd
i=1(z + bi) equals
Γ(z −xk + 1
2)
Γ(z −yk + 1
2) .
Therefore, the contribution of all horizontal pieces below the main diagonal equals
l−1
Y
k=1
Γ(z −xk + 1
2)
Γ(z −yk + 1
2) .
(2.10)
Finally, consider the only piece that intersects the main diagonal. By our as-
sumption, this piece is horizontal, and it sits between the lines s −r = xl and
s −r = yl. We have to examine the row Frobenius coordinates inside it. They
make up the sequence
−(xl + 1
2),
−(xl + 3
2),
. . . ,
1
2
(recall that xl < 0 < yl). The corresponding contribution equals
Γ(z −xl + 1
2)
Γ(z + 1
2)
.
(2.11)
Multiplying up (2.10) and (2.11) we get
d
Y
i=1
(z + bi) =
l−1
Y
k=1
Γ(z −xk + 1
2)
Γ(z −yk + 1
2) · Γ(z −xl + 1
2)
Γ(z + 1
2)
=
Ql
k=1 Γ(z −xk + 1
2)
Γ(z + 1
2) Ql−1
k=1 Γ(z −yk + 1
2)
.
(2.12)
Now (2.8) follows from (2.9) and (2.12).
We have veriﬁed (2.6) under the assumption xl < 0 < yl, i.e., in the case when
the main diagonal s −r = 0 meets the boundary line ∂λ at an interior point of a
horizontal piece. The same argument works if the intersection of s −r = 0 with ∂λ
is inside a vertical piece (i.e., yl < 0 < xl+1 for a certain l) or if the intersection
point coincides with a brake of ∂λ (i.e., some xl or yl is 0).
□
Set
epk(λ) = epk[λ( · )],
k = 1, 2, . . .,
λ ∈Y,
where the right–hand side is given by (2.2) or, equivalently, by (2.3). Note that
ep1(λ) ≡0.
12
