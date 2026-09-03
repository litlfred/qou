---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-041-65-construction-of-the-double-leaves-basis
section_title: "Construction of the double leaves basis"
section_number: 6.5
pages: 43-44
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
In this section we consider two arbitrary sequences (not necessarily reduced)
of simple reﬂections s =s1··· sn and r =r1··· rp. We are interested in calcu-
lating the space Hom(Bs,B r).
Philosophy: The natural basis between Bott-Samelson bimodules is the treeTs ”pasted”
with the treeTr inverted.
For any light leafl :Br→Bt inTr we can ﬁnd its adjoint light leaf la :Bt→Br
by replacing each morphism in the set{ms,j s,f sr} by its adjoint. So we obtain
a treeTa
r where the arrows go from children to parents.
LetLs be the set of light leaves ofTs (recall that each leaf of the tree is seen as
a morphism between Bott-Samelson bimodules).
Let h∈Ls and g∈La
r , with h∈ Hom(Bs,B x) and g∈ Hom(By,B r), where
x and y are reduced expressions of the elements x,y ∈ W respectively. We
deﬁne
g·h =
{
g◦F◦h if x =y
∅ if x⁄=y
where F is any path morphism in Hom(Bx,B y). We call the set La
r·Ls the
double leaves basis of Hom(Bs,B r). The following theorem is proved in [Li4].
5The reason for this is that if the “weight” of a leaf is the length of the corresponding
Bott-Samelson bimodule, then the leaves colored byR are the “lightest” ones.
43
Theorem 6.4 (Nicolas Libedinsky ) The Double Leaves Basis is a basis as a
right (or left)R-module of the space Hom(Bs,B r).
The proof of Theorem 6.4 is quite close to the proof of [Li2, Th´eor`eme 5.1].
Remark 8 Twice in this construction we said “where F is any path mor-
phism”. Of course, for this basis to be well deﬁned, these choices must be
done once and for all. But what is quite striking about this theorem is that
with any of these choices, Theorem 6.4 holds. There is a way to solve this
ambiguity problem that we explore in the paper in preparation [LW].
Question 6.5 Give an algorithm to express a composition of double leaves as
a linear combination of double leaves.
