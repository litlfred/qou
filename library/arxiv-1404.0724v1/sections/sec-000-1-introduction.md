---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to Representations of Braid Groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
---
Camilo Arias Abad∗
April 4, 2014
Abstract
These are lecture notes prepared for a minicourse given at the Cimpa Research School
Algebraic and geometric aspects of representation theory, held in Curitiba, Brazil in March
2013. The purpose of the course is to provide an introduction to the study of representations
of braid groups. Three general classes of representations of braid groups are considered:
homological representations via mapping class groups, monodromy representations via the
Knizhnik-Zamolodchikov connection, and solutions of the Yang-Baxter equation via braided
bialgebras. Some of the remarkable relations between these three diﬀerent constructions are
described.
Contents
1
Introduction
2
2
Braid groups
2
2.1
Artin’s presentation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.2
Conﬁguration spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.3
Mapping class groups
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.4
Pure braids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
3
Homological representations
7
3.1
The Burau representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.2
Homological interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3.3
Braids, knots and the Alexander Conway polynomial . . . . . . . . . . . . . . . .
10
3.4
The Lawrence-Krammer-Bigelow representation . . . . . . . . . . . . . . . . . . .
13
4
The Knizhnik-Zamolodchikov connection
15
4.1
Cohomology of conﬁguration spaces and the KZ connection . . . . . . . . . . . .
16
4.2
Representations of sl2(C) and Lawrence-Krammer-Bigelow
. . . . . . . . . . . .
20
5
The Yang-Baxter equation and the Drinfeld-Kohno theorem
22
5.1
The Yang-Baxter equation and quasi-triangular bialgebras
. . . . . . . . . . . .
22
5.2
The Drinfeld-Kohno theorem
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
∗Max Planck Institut f¨ur Mathematik, Vivatgasse 7, Bonn, camiloariasabad@gmail.com. Supported by SNF
Grant 200020-131813/1 and a Humboldt fellowship.
1
arXiv:1404.0724v1  [math.AT]  2 Apr 2014
Acknowledgements. I would like to thank Florian Sch¨atz and David Martinez Torres for their
comments on an earlier version, and Bernardo Uribe, for his help with some of the references.
I would also like to thank the organizers of the Cimpa School for the invitation to teach this
course, which gave me the opportunity to learn about braid groups. I am very grateful to the
anonymous referee for carefully reading a previous version and correcting several mistakes.
1
Introduction
Braid groups were introduced by Emil Artin in 1925, and by now play a role in various parts
of mathematics including knot theory, low dimensional topology, public key cryptography and
deformation quantization.
The braid group Bn admits diﬀerent equivalent deﬁnitions: the
fundamental group of the conﬁguration space Cn(C) of n unordered points in the complex
plane, the mapping class group of a disk with n marked points, and Artin’s presentation. Each
of these descriptions provides a method for constructing representations of Bn: fundamental
groups act via monodromy, mapping class groups act on the homology groups of spaces, and
solutions to the Yang-Baxter equations produce solutions to Artin’s relations. The aim of these
notes is to introduce these methods, and describe some of the relations between these seemingly
unrelated constructions. The notes are organized as follows:
In section §2 we present three diﬀerent ways in which the braid group Bn can be deﬁned,
explain how these deﬁnitions are equivalent, and introduce some general facts regarding the
braid groups. Section §3 regards the group Bn as the mapping class group of a disk with n
marked points. This description produces representations of Bn via the action on the homol-
ogy of spaces which are functorially associated to the punctured disk. The Burau represen-
tation is discussed and the relationship with the Alexander-Conway polynomial is explained.
The Lawrence-Krammer-Bigelow representation is also constructed. Section §4 begins with the
introduction of the Knizhnik-Zamolodchikov connection and explains how representations of
complex semisimple Lie algebras produce, via the Knizhnik-Zamolodchivok connection, mon-
odromy representations of the braid group. A theorem of Kohno is explained, which describes
the relationship between monodromy representations associated to the Lie algebra sl2(C) and
the Lawrence-Krammer-Bigelow representation. In section §5 we introduce the Yang-Baxter
equation, and explain the way in which solutions of this equation produce representations of
Bn. We deﬁne the notion of a quasi-triangular bialgebra, and show that modules over quasi-
triangular bialgebras come equipped with solutions to the Yang-Baxter equation. Finally, the
Drinfeld-Kohno theorem is discussed. This remarkable theorem explains the precise relationship
between the monodromy representations constructed via the Knizhnik-Zamolodchikov connec-
tion, and the representations constructed as solutions of the Yang-Baxter equation provided by
quantum enveloping algebras. We have included some proofs of the results we discussed, when
they are enlightening and suﬃciently simple. However, no attempt has been made to present
all proofs of the theorems we mentioned, as this would go far beyond the scope of these notes.
When proofs are missing, we have tried to provide references to the many excellent sources that
were used in preparing this course.
2
Braid groups
Artin’s braid groups admit several equivalent descriptions, which we will review in this section.
2
2.1
Artin’s presentation
We denote by D2 the unit disk in the complex plane and ﬁx n marked points
−1 < p1 < p2 · · · < pn < 1 ∈D2 ∩R.
Deﬁnition 2.1. A braid is a collection of n paths fi : I = [0, 1] 7→D2, called strands, such that:
1. fi(0) = pi.
2. fi(1) = pτ(i), for some permutation τ in the symmetric group Σn.
3. For each t ∈I, fi(t)̸ = fj(t) provided that i̸ = j.
Braids are pictured geometrically as a collection of n strands in three dimensional space. One
is usually interested in braids only up to isotopies ﬁxing the endpoints of each strand. We will
abuse the notation and take the word braid to mean an isotopy class. Some examples of braids
are the following:
Figure 1: Examples of braids
Deﬁnition 2.2. The braid group in n strands, denoted Bn, consists of the set of all braids with
n strands with multiplication given by glueing.
It is a good exercise to become convinced that this operation indeed gives Bn the structure of
a group. The following result, due to Emil Artin, gives a presentation for the group Bn.
Theorem 2.3 (Artin [3]). Denote by Bn the group generated by the symbols σ1, . . . , σn−1 modulo
the relations:
1. σiσi+1σi = σi+1σiσi+1 for i = 1, ..., n −2.
2. σiσj = σjσi for |i −j| ≥2.
There is an isomorphism of groups φ : Bn →Bn determined by:
σi
7→
.
3
=
=
Proof. The fact that the ﬁrst relation is satisﬁed follows from the equality:
The fact that the second relation is satisﬁed follows from:
We conclude that φ deﬁnes a homomorphism. Next, one needs to prove that φ is actually an
isomorphism. Surjectivity is easy since the elements φ(σi) clearly generate Bn. For a proof of
injectivity see [18] Theorem 1.12.
□
From now on we will identify the groups Bn and Bn using the isomorphism above.
