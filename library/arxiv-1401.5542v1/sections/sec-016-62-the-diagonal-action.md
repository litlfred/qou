---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-016-62-the-diagonal-action
section_title: "The diagonal action"
section_number: 6.2
pages: 15-16
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
---
follows from results in [7]: A decoration is an equivariant map
(5.16) D :ˆ~M
(0)
→ PSL(2, C)
/
P,
and is thus determined by its image of lifts ~e1,..., ~ev of the cusps of M. The freedom in
the choice of D(~ei) is the choice of a coset gP satisfying that gρ(Stab(~ei))g−1⊂ P , where
16 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
Stab(~ei)⊂π1(M) is the stabilizer of ~ei, i.e. a peripheral subgroup corresponding to cusp i.
Hence, if ρ(Stab(~ei)) is non-trivial, the freedom is right multiplication by a diagonal matrix
(if it is trivial, any coset works). Hence, if ρ is boundary-non-trivial, the only freedom in
choosing a decoration is the diagonal action.
6. Ptolemy varieties for n> 2
Many of our results generalize in a straightforward way to the higher rank Ptolemy varieties
Pn(T ). We recall the deﬁnition of these below, and refer to [7, 5] for details.
We identify all simplices ofT with a standard simplex
(6.1) ∆ 3
n =
{
(x0,x 1,x 2,x 3)∈ R4⏐⏐ 0≤xi≤n, x0 +x1 +x2 +x3 =n
}
and regard ˆM as a quotient of a disjoint union ∐s
k=1 ∆3
n,k, with a copy ∆ 3
n,k of ∆ 3
n for each
simplexk ofT . Deﬁne ∆ 3
n(Z) = ∆3
n∩ Z4 and ˙∆3
n(Z) to be ∆3
n(Z) with the four vertex points
removed. A point in M in the image of ∐s
k=1
˙∆3
n,k(Z) is called an integral point of M.
6.1. Deﬁnition of the Ptolemy variety. Assign to each (t,k )∈ ∆3
n,k(Z) a Ptolemy coor-
dinate ct,k. For each simplex k, we have|∆n−2(Z)| =
(n+1
3
)
Ptolemy relations
(6.2) cα+1001,kcα+0110,k +cα+1100,kcα+0011,k =cα+1010,kcα+0101,k, α ∈ ∆n−2(Z)
as well as identiﬁcation relations,
(6.3) ct,k =±ct′,k′, when ( t,k )∼ (t′,k′).
Remark 6.1. The signs in 6.3 depend in a non-trivial way on the face pairings (see [5]).
For ordered triangulations the signs are always positive. As in Remark 3.3 we can eliminate
the identiﬁcation relations by selecting a representative of each integral point of M.
Deﬁnition 6.2. The Ptolemy variety Pn(T ) is the subset of the aﬃne algebraic set deﬁned
by the Ptolemy- and identiﬁcation relations, consisting of the points where all Ptolemy
coordinates are non-zero.
For general n, we denote the group of upper triangular matrices with 1 on the diagonal
byN (instead of P ). As in 1.2 we have
(6.4){
Points in
Pn(T )
}
oo 1−1 //
{
Natural (SL(n, C),N )-
cocycles on M
}
oo 1−1 //
{
Generically decorated
