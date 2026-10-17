---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-001-11-results
section_title: "Results"
section_number: 1.1
pages: 1-2
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
diﬀerent ﬁelds.
A major development in the study of categoriﬁed link invariants was an alternative categoriﬁcation
of the Jones polynomial called odd Khovanov homology introduced by Ozsv´ath, Rasmussen and Szab´o
[27]. Odd Khovanov homology coincides with Khovanov homology when taken with
Z2-coeﬃcients,
but is distinct from Khovanov homology in general [31]. In order to obtain a representation theoretic
undestanding of this odd Khovanov homology, Ellis, Khovanov, and Lauda started a program studying
odd analogues of structures related to Uq(sl2) and its categoriﬁcation [13, 12, 14].
These investigations into odd categoriﬁcation turned out to be closely connected with independent
parallel investigations into Kac-Moody superalgebra categoriﬁcations [18, 16, 17], with the odd cat-
egoriﬁcation of sl2 lifting the rank one Kac-Moody superalgebra. These odd categoriﬁcations give
categoriﬁcations of the theory of covering Kac-Moody algebras [15, 9, 7, 8]. Covering algebras Uq,π(g)
generalize quantum enveloping algebras, depending on an additional parameter π with π2 = 1. When
π = 1, it reduces to the usual quantum enveloping algebra Uq(g), while the π = −1 specialization
recovers the quantum group of a super Kac-Moody algebra. The quantum algebra and quantum super-
algebra can be identiﬁed by an automorphism of (an extension of) the covering quantum group called
a twistor, which sends π →−π and q →t−1q where t2 = −1 [11].
In the rank one case, the π = 1 specialization is Uq(sl2), while for π = −1 it gives the quantum
supergroup Uq(osp(1|2)) associated with the lie superalgebra osp(1|2). Ellis and Lauda deﬁned a 2-
supercategory U that categoriﬁes the rank one covering algebra Uq,π(sl2) [14]. This categoriﬁcation was
later greatly simpliﬁed and generalized by Brundan and Ellis [6], where the 2-supercategory formalism
1
2
MARK EBERT
was better developed, building oﬀof their work [5].
However, a understanding of odd Khovanov
homology in terms of higher representation theory of U still eludes us.
There is heurisitic evidence for the existence of odd link homology theories associated to so2n+1 from
Mikhaylov and Witten [26]. If we are somehow able to develop an odd version of Webster’s results in
the future, then we can get odd link homology theories categorifying invariants obtained through the
RT process on quantum supergroups.
The Uq(osp(1|2n)) link invariant has been deﬁned using Markov traces on the Birman-Wenzl-
Murakami algebra[4]. Clark [10] produced the colored Uq(osp(1|2n)) invariant from the representation
theory of the quantum covering group Uq,π(osp(1|2n)) a la Turaev [33]. A notable result from Clark’s
paper is that the osp(1|2n) invariant and the so(2n + 1) invariant are basically the same using the
theory of twistors. If we represent a tangle as a composition S of Uq,π-module homomorphisms, then
Clark showed that twistors commute with S up to an integral power of τ.
Theorem 1.1. [10, Theorem 4.24] Let K be any oriented knot, and let ospJλ
K(q), soJλ
K(q) ∈Q(q, t)τ
be the λ-colored osp and so knot invariants. Then
ospJλ
K(q) = t⋆(K,λ)soJλ
K(t−1q)
for some ⋆(K, λ) ∈
Z.
In particular, the Uq(osp(1|2))-invariant in the variable q is just the Jones polynomial in the variable
τ −1q.
If T+, T−, T0 are unframed oriented links that diﬀer as shown below
T+
T−
T0
,
then
(τ −1q)−2J1
T+ −(τ −1q)2J1
T−= (τq−1 −τ−1q)J1
T0.
(1.1)
However, a categoriﬁcation of this invariant has not been discovered as of yet.
1.1. Results. In this paper, we also construct an invariant bJ of oriented links using the representation
theory of osp(1|2). We ﬁrst deﬁne a new Kauﬀman bracket-type Skein relation satisfying

=
τ

−q

Then bJ is given by a renormalization of the bracket, and satisﬁes 1.1. Therefore bJ agrees with Clark’s
osp(1|2) invariant J1
L on any oriented link L. We then show that the osp(1|2) link invariant formulated
this way can be easily categoriﬁed with a slightly modiﬁed version of Khovanov homology with an
additional
Z4-grading. We also construct a slight modiﬁcation of Putyra’s covering Khovanov homology
[28] that has an additional
Z4 grading. The idea of adding an additional grading to Khovanov homology
has been done[24], but the connection to osp(1|2) is new.
