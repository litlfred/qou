---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-004-13-the-next-theorem-gives-bases-for-morphism-spa
section_title: "The next theorem gives bases for morphism spaces. Again, this is du e to Turaev"
section_number: 1.3
pages: 3-4
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
---
[T2, Theorems 5.1 and 5.2.3]; Turaev notes that it was also proved inde pendently by
Morton and Traczyk. To formulate it, given a = am··· a1, b = bn··· b1∈⟨↑,↓⟩, an
(a, b)-matching means a bijection
{( m+1−i
m+1 , 0, 0
) ⏐⏐⏐ai =↑
}
∪
{( n+1−j
n+1 , 1, 0
) ⏐⏐⏐bj =↓
}
∼
−→
{( m+1−i
m+1 , 0, 0
) ⏐⏐⏐ai =↓
}
∪
{( n+1−j
n+1 , 1, 0
) ⏐⏐⏐bj =↑
}
.
There are no such bijections unless the domain and codomain have th e same size d, in
which case there ared! possibilities. An ( a, b)-ribbon is a lift of a given (a, b)-matching if
the boundary of each strand in the ribbon consists of a pair of point s which correspond
under the matching; in particular, it contains no “ﬂoating bubbles.” A n ( a, b)-ribbon
is reduced if no strand crosses itself and no two strands cross more than onc e.
Theorem 1.2. The morphism space HomOS(z,t)(a, b) is free as a k -module with basis
given by any set consisting of a reduced lift for each of the (a, b)-matchings. The
same is true in ˆOS (z,t ) with one exception: if a = b = ∅ then the morphism space
HomˆOS(q,t)(∅, ∅ ) is free of rank two with basis
{
1∅,
}
.
The algebra Hom ˆOS(z,t)(∅, ∅ ) appearing in Theorem 1.2 is known in the literature
as the Conway skein module [T1] or the framed HOMFLY-PT skein module [MS, Def-
inition 2.1] of the manifold R3. The basis
{
1∅,
}
for it described in the theorem is
implicit already in [HOMFLY, PT], indeed, the existence of the HOMFLY-P T polyno-
mial for oriented links constructed in those papers follows easily fro m this result. To
explain this brieﬂy, let L be an oriented link diagram, and deﬁne writhe( L) as usual to
be the number of positive crossings minus the number of negative cr ossings. Viewing
L as a ( ∅, ∅ )-ribbon, there is a unique scalar H(L)∈ k such that
t− writhe(L)L =H(L)
in End ˆOS(q,t)(∅ ). The scalar H(L) is invariant under the Reidemeister moves (RI),
(RII) and (RIII); for all but (RI), this is automatic from the deﬁn ing relations inFOT ,
while (RI) follows from (T) and (FRI). The relation (S) implies that
tH(L+)−t−1H(L−) = zH (L0)
for oriented link diagrams L+,L− and L0 which agree except in one place, which is
a positive crossing in L+, a negative crossing in L−, and the crossing is resolved in
L0. This is exactly the skein relation deﬁning the HOMFLY-PT polynomial. F inally,
observe that H(L) = 1 in case L is the unknot. Hence, taking k := Z[z,z−1,t,t−1],
the scalar H(L) is exactly the HOMFLY-PT polynomial of L.
