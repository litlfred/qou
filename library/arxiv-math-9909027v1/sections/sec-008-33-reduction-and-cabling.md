---
doc_id: arxiv-math-9909027v1
doc_title: "arXiv:math/9909027v1 [math.QA] 4 Sep 1999"
section_id: sec-008-33-reduction-and-cabling
section_title: "Reduction and cabling"
section_number: 3.3
pages: 77-79
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
---
We give two ways to produce new planar algebras from a given one.
The ﬁrst is a reduction process which makes “irreducible” planar algebras
— those with dim P1 = 1 — the focus of study. A planar algebra is not
reconstructible in any simple way from its irreducible reductions, though, as
can be seen from example 2 where the irreducible reductions would be trivial.
Given a general planar algebra P presented on itself by Φ, and an idem-
potent p ∈P1, we deﬁne the reduced general planar algebra pPp (by p) as
77
follows: for each k we let pk be the element
p
p
p
p
· · ·
of Pk (illustrated when k is odd) and we set (pPp)k = pk(Pk)pk with identity
pk, and unital inclusion Pk֒ →Pk+1 given by pkxpk֒ →pk+1xpk+1 (note
pk+1pk = pkpk+1 = pk+1).
We make pPp into a planar algebra on P as
follows. Given a tangle T ∈P(P), deﬁne the tangle pTp ∈P(P) by inserting
p
in every string of TG. Then pΦp : P(L) →pPp is pΦp(T) = Φ(pTp).
Since p is idempotent, pΦp is a ﬁltered algebra homomorphism with annular
invariance, obviously surjective, so pPp is a general planar algebra. Planarity
is inherited from P and pPp has parameters Z( p
) and Z(
p
),
provided these are nonzero. If P is a C∗-planar algebra and p is a projection
(p = p2 = p∗), pPp is clearly also a C∗-planar algebra, spherical if P is.
Note. We have used the canonical labelling set for P to deﬁne pPp.
If were given another speciﬁc other labelling set L, it is not clear that the
homomorphism obtained in the same way from P(L) to pPp is surjective.
We do not have any example of this phenomenon.
To use the reduction process we require dim P1 > 1. But even “irre-
ducible” planar algebras can yield this situation by cabling, i.e. grouping
several strings together. The term is borrowed from knot theory. Given a
general planar algebra P we deﬁne the nth cabled (general) planar algebra
C\(P) by Cn(P)k = Pnk which we endow with a planar algebra structure as
follows. If Φ presents P on itself, we deﬁne Cn(Φ) : P(Cn(P)) →Cn(P) by
taking a labelled k-tangle T in P(Cn(P)) and constructing an nk-tangle ˜T
in P(P) with the same labels on boxes, but where every boundary point in
TG (both on internal and external boxes) is replaced by n boundary points,
and of course orientations alternate. Every string in T is then replaced by
n parallel strings. The procedure is illustrated in Figure 3.4.1, where k = 3
78
and n = 2.
The 3-tangle ˜T
The 3-tangle T
R
Q
B
Q
R
B
Figure 3.4.1
Then we deﬁne Cn(Φ)(T) to be Φ( ˜T). It is clear that Cn(Φ) is a general planar
algebra, connected and multiplicative if P is, with parameters (δ1δ2)[ n
2]δ
n−[ n
2]
1
,
(δ1δ2)[ n
2]δ
n−[ n
2]
2
, (where δ1 and δ2 are the parameters of the planar algebra P
and [n
2] is the integer part of [n
2]). Also Cn(P) is a C∗-planar algebra if P is,
spherical if P is.
