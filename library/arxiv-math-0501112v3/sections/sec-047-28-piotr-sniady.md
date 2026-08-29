---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-047-28-piotr-sniady
section_title: "PIOTR ´SNIADY"
section_number: 28
pages: 28-29
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
Proof. Equations (5.4) and (5.5) follow immediately from the deﬁni tion
(5.3).
We shall treat (5.6) as a deﬁnition of the left-hand side and we shall verify
that so deﬁned cumulants fulﬁll the deﬁning relation of cumu lants (5.2).
Before we do this we need to compute the corresponding partition-indexed
cumulants. Let µ be a partition of {1, . . . , n }; we denote by ˜µ a partition of
the set {i1 + 1, i 1 + 2, . . . , i n+1}such that a ∈ ρs and b ∈ ρt belong to the
same block of ˜µ if and only if s and t belong to the same block of µ. Then
(5.6) implies
(5.7) kid
µ (Σ π 1 , . . . , Σ π n ) =
∑
σ 
Σ σ ,
where the sum on the right-hand side runs over all partitions σ of the set
{i1 + 1, i 1 + 2, . . . , i n+1}such that
(1) for any a, b ∈ ρs, 1 ≤ s ≤ n we have that a and b are connected
by σ if and only if they are connected by π s,
(2) elements i2, i 3, . . . , i n+1 belong to the same block of σ; we will
denote this block by σ 1,
(3) (σ \ σ 1) ∨ { ρ1, . . . , ρ n}= ˜µ.
Equation (5.7) implies immediately (5.2). □
For example, for
(5.8) ρ1 = {1, 2, 3, 4 }, ρ 2 = {5, 6, 7, 8 },
π 1 =
{
{1, 3 }, {2, 4 }
}
, π 2 =
{
{5, 7 }, {6}, {8}
}
,
the above theorem states that
Σ π 1 Σ π 2 = Σ {
{1,3 }, {2,4,8 }, {5,7 }, {6}
} + Σ {
{1,3,6 }, {2,4,8 }, {5,7 }
} + Σ {
{1,3,5,7 }, {2,4,8 }, {6}
}
and
kid(Σ π 1 , Σ π 2) = Σ {
{1,3,6 }, {2,4,8 }, {5,7 }
} + Σ {
{1,3,5,7 }, {2,4,8 }, {6}
} ;
the readers acquainted with the results of Section 5.7 may ch eck that it is
equivalent to
Σ 1Σ 1,1 = Σ 1,1,1 + Σ 1,1 + Σ 1,1
and
kid(Σ 1, Σ 1,1 ) = Σ 1,1 + Σ 1,1 .
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS 29
FIGURE 5.1. Graphical representation of a partition{
{1, 3 }, {2, 5, 7 }, {4}, {6}
}
.
FIGURE 5.2. The ﬁrst collection of discs for partition π
from Figure 5.1.
