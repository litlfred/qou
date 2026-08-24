---
doc_id: 0110001v3
doc_title: "A geometric interpretation of Milnor's triple linking numbers"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0110001v3.pdf
source_sha256: f30f603ac1c555e0
doc_brief: "A geometric interpretation of Milnor's triple linking numbers — Milnor’s triple linking numbers of a link in the 3-sphere are interpreted geometrically in terms of the pattern of intersections of the"
---
Milnor’s higher order linking numbers (or mu-bar invariants) ¯µi of an oriented
link L = L1 ∪ · · · ∪Lℓ in the 3-sphere are a measure of how deep the longitudes
li of the components Li lie in the lower central series of the link group π =
π1(S3 − L). They are deﬁned as follows [4]:
Any diagram of L gives rise to a Wirtinger presentation of π whose generators
are meridians of the link, one for each arc in the diagram. If o ne works modulo
any term πn in the lower central series of π (where π1 = π and πn = [π, πn− 1])
then only one meridian mi is needed from each component Li . In particular the
longitude li can be written mod πn as a word ln
i in these preferred meridians,
i.e. as an element of the free group F = F (m1, . . . , mℓ). Now each element in
F can be viewed as a unit in the ring A of power series in the noncommuting
variables h1, . . . , hℓ by substituting 1 + hi for mi and 1 − hi + h2
i − + · · ·
for m− 1
i ; this is its Magnus expansion [3] (which embeds F in A). For any
sequence i = i1 · · · ir of integers between 1 and ℓ, let µi denote the coeﬃcient
of hi1 · · ·hir− 1 in the Magnus expansion of ln
ir for large n. It is easily shown
that µi is independent of n for n ≥ r, but unfortunately it does depend on
the original choice of meridians. If however one reduces mod ulo the greatest
c© G eometry & Topology Publications
558 Blake Mellor and Paul Melvin
common divisor δi of the lower order coeﬃcients µj (for all proper subsequences
j of i) then one obtains Milnor’s linking numbers
¯µi = µi (mod δi) ∈ Z/δiZ.
They are invariants of L (with a given ordering of its components) up to link
concordance, and in fact up to link homotopy if the indices i1, . . . , ir are distinct.
Note that in general ¯µi depends on the ordering of the indices in i, although it
is symmetric in these indices for r = 2 (indeed µij = ¯µij is the usual pairwise
linking number) and antisymmetric for r = 3.
The computation of ¯µi from this point of view is tedious and unenlightening,
especially for large r. As a warm-up consider the pairwise linking number ¯ µij ,
which is the coeﬃcient of hi in the Magnus expansion of l2
j . To compute ¯ µij ,
write the word for the longitude lj as a product of generators in the Wirtinger
presentation, each of which is a conjugate wmpw− 1 of its associated (preferred)
meridian mp . Working mod the commutator subgroup π2 , this conjugate can
be replaced by just mp , giving a word uj in m1, . . . , mℓ . Then
¯µij = εi(uj)
where εi(uj) is the sum of the exponents of mi in uj (cf. [2, p 8]).
Now consider the triple linking number ¯ µijk for distinct i, j, k, which is the
coeﬃcient of hihj in the Magnus expansion of l3
k , reduced modulo the greatest
common divisor δ = δijk of the pairwise linking numbers of Li , Lj and Lk .
As before, write the word for the longitude lk as a product of generators in
the Wirtinger presentation, and then express each generato r as a conjugate
wmpw− 1 of its associated meridian. Working mod π3 , each generator in the
conjugating word w can be replaced by its associated meridian, giving the word
l3
k in m1, . . . , mℓ . Since we are only interested in the coeﬃcient of hihj in the
Magnus expansion of this word, any occurrence of meridians o ther than mi and
mj can be ignored. Thus we are left with a word uk in mi and mj . Now
¯µijk = εij(uk) (mod δ)
where εij(uk) denotes the sum of the signed occurences of mimj in the word
uk : each · · ·mr
i · · ·ms
j · · · in uk , where r, s = ±1, contributes rs to εij(uk)
(see [2, pp 38,142]). (In fact ¯ µijk can be computed as εij(u) for any word u
representing lk mod π3 .)
Algebraic & Geometric Topology, Volume 3 (2003)
A geometric interpretation of Milnor’s triple linking numb ers 559
The purpose of this note is to reinterpret this process for co mputing the triple
linking numbers in terms of Seifert surfaces of the link comp onents and their
intersections. This generalizes work of Cochran [1] for lin ks with trivial pairwise
linking numbers (also see Turaev [5]).
Remarks It is worth noting a few properties of εi and εij . Let u and v be
words in the meridians m1, . . . , mℓ . Then
(1) εi(uv) = εi(u) + εi(v)
(2) εij(uv) = εij(u) + εij(v) + εi(u)εj (v)
(3) εij(u) + εji(u) = εi(u)εj(u)
(cf. [2, Lemma 4.2.7]). The third equation identiﬁes two way s of counting (with
sign) all pairs of an occurrence of mi and an occurrence of mj (in either order).
The authors gratefully acknowledge the hospitality of the M athematics Institute
at the University of Warwick during the Geometry/Topology W orkshop in July
2000, where this work was initiated.
