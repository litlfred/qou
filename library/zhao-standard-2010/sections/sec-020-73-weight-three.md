---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-020-73-weight-three
section_title: "Weight three"
section_number: 7.3
pages: 19-20
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Apparently there are N 2(N + 1) MPVs of weight three and level N : for each
choice (i, j, k) with 1 ≤ i ≤ N − 1, 0 ≤ j, k ≤ N − 1 we have four MPVs of level
N :
LN (13|i, j, k) := LN (1, 1, 1|i, j, k), L N (1, 2|i, j), L N (2, 1|j, k), L N (3|k).
For 1 ≤ i, j, k < N the FDS Z ∗(
y1,i ∗ (y1,jy1,k)
)
= Zx(
y1,ix(y1,jy1,k)
)
yields
LN (13|i, j − i, k) + LN (13|j, i − j, k + j − i) + LN (13|j, k, i − k − j)
= LN (2, 1|i + j, k) + LN (1, 2|j, i + k)
+ LN (13|i, j, k) + LN (13|j, i, k) + LN (13|j, k, i). (28)
For 1 ≤ i, j < N the FDS Z ∗(y1,i ∗ y2,j) = Zx(y1,ixy2,j) yields
LN (3|i + j) + LN (1, 2|i, j) + LN (2, 1|j, i)
= LN (1, 2|i, j − i) + LN (2, 1|i, j − i) + LN (2, 1|j, i − j). (29)
Moreover, there are three ways to produce RDS. Since ρ(T ) = T the ﬁrst
family of RDS come from Z ∗(
y1,0 ∗ (y1,iy1,i+j)
)
= Zx(
y1,0x(y1,iy1,i+j)
)
for
1 ≤ i ≤ N − 1, 0 ≤ j ≤ N − 1:
y1,0 ∗ (y1,iy1,i+j) = y1,0y1,iy1,i+j + y1,iτi(y1,0 ∗ y1,j) + y2,iy1,i+j
=y1,0y1,iy1,i+j + y1,iy1,iy1,i+j + y1,iy1,i+jy1,i+j + y1,iy2,i+j + y2,iy1,i+j
On the other hand,
y1,0xy1,iy1,i+j = y1,0y1,iy1,i+j + y1,iy1,0y1,i+j + y1,iy1,i+jy1,0.
Hence
LN (13|i, 0, j) + LN (13|i, j, 0) + LN (1, 2|i, j) + LN (2, 1|i, j)
= LN (13|i, −i, i + j) + LN (13|i, j, −i − j). (30)
The second family of RDS follow from ρ(Z ∗(y1,0 ∗ y2,i)) = Zx(y1,0xy2,i):
y1,0y2,i + y2,iy1,i + y3,i = y1,0y2,i + y2,0y1,i + y2,iy1,0
Documenta Mathematica 15 (2010) 1–34
