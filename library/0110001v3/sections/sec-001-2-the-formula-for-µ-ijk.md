---
doc_id: 0110001v3
doc_title: "A geometric interpretation of Milnor's triple linking numbers"
section_id: sec-001-2-the-formula-for-µ-ijk
section_title: "The formula for ¯µ ijk"
section_number: 2
pages: 3-6
source_pdf: 0110001v3.pdf
source_sha256: f30f603ac1c555e0
doc_brief: "A geometric interpretation of Milnor's triple linking numbers — Milnor’s triple linking numbers of a link in the 3-sphere are interpreted geometrically in terms of the pattern of intersections of the"
---
Fix three components Li, Lj, Lk of L, with δ the greatest common divisor
of their pairwise linking numbers, and choose any associate d oriented Seifert
surfaces Fi, Fj , Fk in general position. Set F = Fi ∪ Fj ∪ Fk . It will be shown
below that ¯µijk is the diﬀerence of two geometric invariants, tijk(F ) ∈ Z and
mijk (F ) ∈ Z/δZ, deﬁned as follows.
The intersection Fi ∩ Fj ∩ Fk consists of isolated triple points, each of which is
given a sign according to the orientations and ordering of th e surfaces: the sign
is positive if and only if the ordered basis of normal vectors to Fi, Fj , Fk at the
triple point agrees with the standard orientation on S3 . Let
tijk(F ) = # Fi ∩ Fj ∩ Fk,
the total number of triple points, counted with sign . This integer is clearly
invariant under isotopies of the individual Seifert surfac es which maintain their
mutual general position, and is antisymmetric in the indice s.
Similarly any pairwise intersection of the Seifert surface s is a union of circles,
clasps and ribbons (see Figure 1).
Algebraic & Geometric Topology, Volume 3 (2003)
560 Blake Mellor and Paul Melvin
/X2B
/X2B
/X2B
Fi
Fj
Fi
Fj
Fi Fj Fi Fj
(a) clasp (b) ribbon
Figure 1: Intersections of Seifert surfaces
The endpoints of the clasps and ribbons are oriented in a natu ral way since
they are intersection points of one oriented surface with th e oriented boundary
of another. Observe that the two endpoints of any clasp alway s have the same
orientation, while the endpoints of a ribbon are oppositely oriented, and so these
orientations can be speciﬁed by a single sign for each clasp a nd an orientation
on each ribbon arc (from negative to positive) as shown in the ﬁgure.
Now choose a basepoint on each link component (this is equiva lent to choosing
the meridians in the deﬁnition of Milnor’s invariant). Star ting at the basepoint
of Li , read oﬀ a word wi in j and k by proceeding around Li : each double point
in Li ∩ Fj of sign ε contributes jε , and similarly for k . (Here and below we
simply use the indices i, j, k to denote the corresponding meridians mi, mj, mk .)
Similarly deﬁne words wj and wk . Let epqr (F ) denote the coeﬃcient of hphq
in the Magnus expansion of wr , i.e. epqr (F ) = εpq(wr), and set
mijk (F ) = eijk (F ) + ejki (F ) + ekij (F ),
the sum of the eijk ’s over cyclic permutation of the indices.
Example The Borromean rings are shown in Figure 2, bounding three dis ks
with two clasps and one ribbon. If the basepoints are chosen n ear the labels,
we compute wi = 1, wj = kk− 1 = 1, and wk = iji− 1j− 1 . Thus eijk = 1 and
ejki = ekij = 0, so mijk = 1. Note that the clasps can be eliminated, at the
expense of introducing a triple point, by sliding the disk Fj to the left so that
its boundary encircles Fi and pierces Fk (cf. the theorem below).
Algebraic & Geometric Topology, Volume 3 (2003)
A geometric interpretation of Milnor’s triple linking numb ers 561
/X2B
/X5F
/X5F
/X5F
/X2B
/X2B
Fi Fj
Fi Fj
Fk
Fk
k
k− 1
i− 1 i
j− 1
j
Figure 2: Computation of mijk
Remarks (1) Choosing a diﬀerent basepoint changes eijk , and hence mijk ,
by some multiple of the linking numbers, so mijk (like ¯µijk ) is well deﬁned mod-
ulo δ . To see this, note that a basepoint change induces a cyclic pe rmutation of
wk , which reduces the value of eijk by εij(uv) − εij(vu) for some factorization
wk = uv . But (using Remarks 1 and 2 at the end of the previous section)
εij(uv) − εij(vu) = εi(u)εj (v) − εi(v)εj (u)
= (εi(u) + εi(v))εj (v) − εi(v)(εj (u) + εj(v))
= εi(uv)εj (v) − εi(v)εj (uv) = µikεj(v) + εi(v)µjk .
where µpq = lk(Lp, Lq), so this diﬀerence is trivial mod δ .
(2) The invariants eijk are antisymmetric in i and j . Indeed eijk + ejik =
εij(wk) + εji(wk) = εi(wk)εj(wk) = µikµjk ≡ 0 (mod δ), by Remark 3 in §1. It
follows that mijk is totally antisymmetric.
Our goal is to prove the following result, where as usual δ denotes the greatest
common divisor of the pairwise linking numbers of Li , Lj and Lk .
Theorem (1) For any choice of Seifert surfaces F ,
¯µijk ≡ mijk (F ) − tijk (F ) (mod δ).
(2) There is a choice of F such that tijk (F ) = 0 , so ¯µijk ≡ mijk (F ) (mod δ).
(3) There is a choice of F such that mijk(F ) ≡ 0, so ¯µijk ≡ −tijk (F ) (mod δ).
Algebraic & Geometric Topology, Volume 3 (2003)
562 Blake Mellor and Paul Melvin
The familiar fact that the Milnor invariants ¯ µijk are antisymmetric in the in-
dices follows immediately from the theorem and the precedin g remark. We also
recover Cochran’s result that ¯µijk = −tijk (F ) if the boundary of F is disjoint
from the double point set (which is only possible if the pairw ise linking numbers
vanish).
The idea of the proof is as follows. We will deﬁne two special t ypes of of Seifert
surfaces F and show that mijk(F ) ≡ ¯µijk and tijk (F ) = 0 for those of type 1,
while mijk (F ) ≡ 0 for those of type 2. We will then describe a set of ﬁnger
moves that can transform an arbitrary F into either reduced type, and that
preserve mijk − tijk (mod δ). The theorem follows.
