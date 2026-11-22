---
doc_id: 0110001v3
doc_title: "A geometric interpretation of Milnor's triple linking numbers"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 0110001v3.pdf
source_sha256: f30f603ac1c555e0
toc_source: inferred
doc_brief: "A geometric interpretation of Milnor's triple linking numbers — Milnor’s triple linking numbers of a link in the 3-sphere are interpreted geometrically in terms of the pattern of intersections of the"
---
Introduction
Milnor’s higher order linking numbers (or mu-bar invariants) ¯µi of an oriented
link L = L1 ∪· · · ∪Lℓin the 3-sphere are a measure of how deep the longitudes
li of the components Li lie in the lower central series of the link group π =
π1(S3 −L). They are deﬁned as follows [4]:
Any diagram of L gives rise to a Wirtinger presentation of π whose generators
are meridians of the link, one for each arc in the diagram. If one works modulo
any term πn in the lower central series of π (where π1 = π and πn = [π, πn−1])
then only one meridian mi is needed from each component Li. In particular the
longitude li can be written mod πn as a word ln
i in these preferred meridians,
i.e. as an element of the free group F = F(m1, . . . , mℓ). Now each element in
F can be viewed as a unit in the ring A of power series in the noncommuting
variables h1, . . . , hℓby substituting 1 + hi for mi and 1 −hi + h2
i −+ · · ·
for m−1
i
; this is its Magnus expansion [3] (which embeds F in A). For any
sequence i = i1 · · · ir of integers between 1 and ℓ, let µi denote the coeﬃcient
of hi1 · · · hir−1 in the Magnus expansion of ln
ir for large n. It is easily shown
that µi is independent of n for n ≥r, but unfortunately it does depend on
the original choice of meridians. If however one reduces modulo the greatest
c⃝Geometry & Topology Publications
558
Blake Mellor and Paul Melvin
common divisor δi of the lower order coeﬃcients µj (for all proper subsequences
j of i) then one obtains Milnor’s linking numbers
¯µi = µi (mod δi) ∈Z/δiZ.
They are invariants of L (with a given ordering of its components) up to link
concordance, and in fact up to link homotopy if the indices i1, . . . , ir are distinct.
Note that in general ¯µi depends on the ordering of the indices in i, although it
is symmetric in these indices for r = 2 (indeed µij = ¯µij is the usual pairwise
linking number) and antisymmetric for r = 3.
The computation of ¯µi from this point of view is tedious and unenlightening,
especially for large r. As a warm-up consider the pairwise linking number ¯µij ,
which is the coeﬃcient of hi in the Magnus expansion of l2
j . To compute ¯µij ,
write the word for the longitude lj as a product of generators in the Wirtinger
presentation, each of which is a conjugate wmpw−1 of its associated (preferred)
meridian mp. Working mod the commutator subgroup π2, this conjugate can
be replaced by just mp, giving a word uj in m1, . . . , mℓ. Then
¯µij = εi(uj)
where εi(uj) is the sum of the exponents of mi in uj (cf. [2, p 8]).
Now consider the triple linking number ¯µijk for distinct i, j, k, which is the
coeﬃcient of hihj in the Magnus expansion of l3
k, reduced modulo the greatest
common divisor δ = δijk of the pairwise linking numbers of Li, Lj and Lk.
As before, write the word for the longitude lk as a product of generators in
the Wirtinger presentation, and then express each generator as a conjugate
wmpw−1 of its associated meridian. Working mod π3, each generator in the
conjugating word w can be replaced by its associated meridian, giving the word
l3
k in m1, . . . , mℓ. Since we are only interested in the coeﬃcient of hihj in the
Magnus expansion of this word, any occurrence of meridians other than mi and
mj can be ignored. Thus we are left with a word uk in mi and mj . Now
¯µijk = εij(uk) (mod δ)
where εij(uk) denotes the sum of the signed occurences of mimj in the word
uk: each · · · mr
i · · · ms
j · · · in uk, where r, s = ±1, contributes rs to εij(uk)
(see [2, pp 38,142]). (In fact ¯µijk can be computed as εij(u) for any word u
representing lk mod π3.)
Algebraic & Geometric Topology, Volume 3 (2003)
A geometric interpretation of Milnor’s triple linking numbers
559
The purpose of this note is to reinterpret this process for computing the triple
linking numbers in terms of Seifert surfaces of the link components and their
intersections. This generalizes work of Cochran [1] for links with trivial pairwise
linking numbers (also see Turaev [5]).
Remarks It is worth noting a few properties of εi and εij . Let u and v be
words in the meridians m1, . . . , mℓ. Then
(1)
εi(uv) = εi(u) + εi(v)
(2)
εij(uv) = εij(u) + εij(v) + εi(u)εj(v)
(3)
εij(u) + εji(u) = εi(u)εj(u)
(cf. [2, Lemma 4.2.7]). The third equation identiﬁes two ways of counting (with
sign) all pairs of an occurrence of mi and an occurrence of mj (in either order).
The authors gratefully acknowledge the hospitality of the Mathematics Institute
at the University of Warwick during the Geometry/Topology Workshop in July
2000, where this work was initiated.
2
The formula for ¯µijk
Fix three components Li, Lj, Lk of L, with δ the greatest common divisor
of their pairwise linking numbers, and choose any associated oriented Seifert
surfaces Fi, Fj, Fk in general position. Set F = Fi ∪Fj ∪Fk. It will be shown
below that ¯µijk is the diﬀerence of two geometric invariants, tijk(F) ∈Z and
mijk(F) ∈Z/δZ, deﬁned as follows.
The intersection Fi ∩Fj ∩Fk consists of isolated triple points, each of which is
given a sign according to the orientations and ordering of the surfaces: the sign
is positive if and only if the ordered basis of normal vectors to Fi, Fj, Fk at the
triple point agrees with the standard orientation on S3. Let
tijk(F) = #Fi ∩Fj ∩Fk,
the total number of triple points, counted with sign. This integer is clearly
invariant under isotopies of the individual Seifert surfaces which maintain their
mutual general position, and is antisymmetric in the indices.
Similarly any pairwise intersection of the Seifert surfaces is a union of circles,
clasps and ribbons (see Figure 1).
Algebraic & Geometric Topology, Volume 3 (2003)
560
Blake Mellor and Paul Melvin
+
+
+
Fi
Fj
Fi
Fj
Fi
Fj
Fi
Fj
(a) clasp
(b) ribbon
Figure 1: Intersections of Seifert surfaces
The endpoints of the clasps and ribbons are oriented in a natural way since
they are intersection points of one oriented surface with the oriented boundary
of another. Observe that the two endpoints of any clasp always have the same
orientation, while the endpoints of a ribbon are oppositely oriented, and so these
orientations can be speciﬁed by a single sign for each clasp and an orientation
on each ribbon arc (from negative to positive) as shown in the ﬁgure.
Now choose a basepoint on each link component (this is equivalent to choosing
the meridians in the deﬁnition of Milnor’s invariant). Starting at the basepoint
of Li, read oﬀa word wi in j and k by proceeding around Li: each double point
in Li ∩Fj of sign ε contributes jε, and similarly for k. (Here and below we
simply use the indices i, j, k to denote the corresponding meridians mi, mj, mk.)
Similarly deﬁne words wj and wk. Let epqr(F) denote the coeﬃcient of hphq
in the Magnus expansion of wr, i.e. epqr(F) = εpq(wr), and set
mijk(F) = eijk(F) + ejki(F) + ekij(F),
the sum of the eijk’s over cyclic permutation of the indices.
Example The Borromean rings are shown in Figure 2, bounding three disks
with two clasps and one ribbon. If the basepoints are chosen near the labels,
we compute wi = 1, wj = kk−1 = 1, and wk = iji−1j−1. Thus eijk = 1 and
ejki = ekij = 0, so mijk = 1. Note that the clasps can be eliminated, at the
expense of introducing a triple point, by sliding the disk Fj to the left so that
its boundary encircles Fi and pierces Fk (cf. the theorem below).
Algebraic & Geometric Topology, Volume 3 (2003)
A geometric interpretation of Milnor’s triple linking numbers
561
+
_
_
_
+
+
Fi
Fj
Fi
Fj
Fk
Fk
k
k−1
i−1
i
j−1
j
Figure 2: Computation of mijk
Remarks (1) Choosing a diﬀerent basepoint changes eijk, and hence mijk,
by some multiple of the linking numbers, so mijk (like ¯µijk) is well deﬁned mod-
ulo δ. To see this, note that a basepoint change induces a cyclic permutation of
wk, which reduces the value of eijk by εij(uv) −εij(vu) for some factorization
wk = uv. But (using Remarks 1 and 2 at the end of the previous section)
εij(uv) −εij(vu) = εi(u)εj(v) −εi(v)εj(u)
= (εi(u) + εi(v))εj(v) −εi(v)(εj(u) + εj(v))
= εi(uv)εj(v) −εi(v)εj(uv) = µikεj(v) + εi(v)µjk.
where µpq = lk(Lp, Lq), so this diﬀerence is trivial mod δ.
(2)
The invariants eijk are antisymmetric in i and j. Indeed eijk + ejik =
εij(wk) + εji(wk) = εi(wk)εj(wk) = µikµjk ≡0 (mod δ), by Remark 3 in §1. It
follows that mijk is totally antisymmetric.
Our goal is to prove the following result, where as usual δ denotes the greatest
common divisor of the pairwise linking numbers of Li, Lj and Lk.
Theorem
(1)
For any choice of Seifert surfaces F ,
¯µijk ≡mijk(F) −tijk(F)
(mod δ).
(2)
There is a choice of F such that tijk(F) = 0, so ¯µijk ≡mijk(F) (mod δ).
(3)
There is a choice of F such that mijk(F) ≡0, so ¯µijk ≡−tijk(F) (mod δ).
Algebraic & Geometric Topology, Volume 3 (2003)
562
Blake Mellor and Paul Melvin
The familiar fact that the Milnor invariants ¯µijk are antisymmetric in the in-
dices follows immediately from the theorem and the preceding remark. We also
recover Cochran’s result that ¯µijk = −tijk(F) if the boundary of F is disjoint
from the double point set (which is only possible if the pairwise linking numbers
vanish).
The idea of the proof is as follows. We will deﬁne two special types of of Seifert
surfaces F and show that mijk(F) ≡¯µijk and tijk(F) = 0 for those of type 1,
while mijk(F) ≡0 for those of type 2. We will then describe a set of ﬁnger
moves that can transform an arbitrary F into either reduced type, and that
preserve mijk −tijk (mod δ). The theorem follows.
