---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-040-744-t-is-q--holonomic
section_title: "T is q--holonomic"
section_number: 7.4.4
pages: 35-36
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
Proposition 7.12 For a ﬁxed fundamental root α ∈{α1, . . . , αℓ}, the braid
operator Tα : U →U and its inverse T −1
α
are q–holonomic.
Proof By Proposition 7.3 we can use any PBW basis.
Choose a reduced word w′ = si1 . . . sit representing the longest element ω0
that begins with α: αi1 = α. Then w = si2 . . . sits¯α is another reduced word
representing ω0, where ¯α is the dual of α: ¯α = −ω0(α).
Geometry & Topology, Volume 9 (2005)
1288
Stavros Garoufalidis and Thang T Q Lˆe
We use fr to denote fr(w), and f ′
r to denote fr(w′). The relation between the
two PBW basis of w and w is as follows: For 1 ≤r ≤t −1,
Tα(fr) = f ′
r+1,
Tα(er) = e′
r+1.
Besides, ft = Fα = f ′
1, et = Eα = e′
1.
We will consider the matrix entry of Tα : U →U where the source space is
equipped with the PBW corresponding to w, while the target space with the
PBW basis corresponding to w′.
From [17, Chapter 8], recall that:
Tα(Fα) = −K−1
α Eα,
Tα(Eα) = −FαKα.
Hence
Tα(F n
α ) = (−1)nvn(n−1)
α
K−n
α En
α,
Tα(Em
α ) = (−1)mv−m(m−1)
α
F m
α Km
α .
For a basis element xσ = f nt
t
. . . f n1
1 Kβem1
1
. . . emt
t
, we have
Tα(xσ) = dα(nt, mt) K−nt
α
Ent
α × (f ′
t)mt−1
. . . (f ′
1)n2Ksαβ(e′
1)m2 . . . (e′
t)mt−1 × F mt
α Kmt
α ,
where
dα(nt, mt) := (−1)nt+mtvnt(nt−1)−mt(m1−1)
α
.
The left or right multiplication by Kn
α is q–holonomic with respect to n and
all the coordinates. The left multiplication by Ent , as well as the right mul-
tiplication my F mt
α
is q–holonomic with respect to nt and all coordinates, by
Proposition 7.11. One then can conclude that Tα is q–holonomic.
The proof for T −1
α : U →U is similar. One should use the PBW basis of w′ for
the source, and that of w for the target.
7.4.5
