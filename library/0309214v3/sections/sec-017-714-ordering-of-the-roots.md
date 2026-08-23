---
doc_id: 0309214v3
doc_title: "The colored Jones function is q-holonomic"
section_id: sec-017-714-ordering-of-the-roots
section_title: "Ordering of the roots"
section_number: 7.1.4
pages: 26-27
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
doc_brief: "The colored Jones function is q-holonomic — A function of several variables is called holonomic if, roug hly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many l inear"
---
Suppose w = si1si2 . . . sit is a reduced word representing the longest element
ω0 of the Weyl group. For r between 1 and t let
γr(w) := si1si2 . . . sir−1(αir ).
Then the set {γi, i = 1 , ..., t} is exactly the set of positive roots. We totally
order the set of positive roots by γ1 < γ 2 < · · · < γ t . This order depends on
the reduced word w, and has the following convexity property: If β1, β2 are
two positive roots such that β1 + β2 is also a root, then β1 + β2 is between β1
and β2 . In particular, the ﬁrst and the last, γ1 and γt , are always fundamental
roots. Conversely, any convex total ordering of the set of po sitive roots comes
from a reduced word representing the longest element of W .
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1279
7.1.5 PBW basis for U −, U + , and U
Suppose w = si1 . . . sit is a reduced word representing the longest element of
W . Let us deﬁne
er(w) = Tαi1 Tαi2 . . . Tαir−1 (Eαir ),
fr(w) = Tαi1 Tαi2 . . . Tαir−1 (Fαir ).
Then |er| = γr = −|fr|. (We drop w if there is no confusion.)
If γr is one of the fundamental roots, γr = α ∈ {α1, . . . , αℓ}, then er(w) = Eα ,
fr(w) = Fα (and do not depend on w).
For t ≥ j ≥ i ≥ 1 let U −[j, i] be the vector space spanned by f nj
j f nj−1
j−1 . . . fni
i ,
for all nj, nj−1, . . . , ni ∈ N and let U +[i, j] the vector space spanned by
eni
i eni+1
i+1 . . . enj
j , for all nj, nj−1, . . . , ni ∈ N. It is known that U − = U −[t, 1]
and U + = U +[1, t].
For n = ( n1, . . . , nt) ∈ Nt , j = (j1, . . . jℓ) ∈ Zℓ and m = (m1, . . . , mt) ∈ Nt let
us deﬁne f n , Kj and em by
f n(w) := f nt
t . . . fn1
1 , Kj := Kj1α1 . . . Kjℓαℓ en(w) := en1
1 . . . ent
t .
Then as vector spaces over Q(v) U − , U + and U have Poincare-Birkhoﬀ-Witt
(in short, PBW) basis
{f n | n ∈ Nt}, {em | m ∈ Nt}, {f nKjem | n, m ∈ Nt, j ∈ Zℓ}
respectively, associated with the reduced word w.
In order to simplify notation, we deﬁne S := Nt × Zℓ × Nt , and xσ := f n K j em .
Thus,
{xσ | σ ∈ S} (4)
is a PBW basis of U with respect to the reduced word w.
