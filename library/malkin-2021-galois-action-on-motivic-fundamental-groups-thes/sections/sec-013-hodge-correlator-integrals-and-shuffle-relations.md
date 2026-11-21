---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-013-hodge-correlator-integrals-and-shuffle-relations
section_title: "Hodge correlator integrals and shuffle relations"
section_number: null
pages: 36-41
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
toc_source: outline
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
Hodge correlator integrals and shuﬄe relations
The main result of this chapter is a set of functional equations on the Hodge correlator integrals and the
Hodge-theoretic and motivic upgrades of these relations. Let us ﬁrst state the results for the Hodge correlator
integrals.
Second shuﬄe relation
Recall the ﬁrst shuﬄe relation for the Hodge correlator integrals (1.5):
Õ
휎∈Σ푖, 푗
CorH(푥0, 푥휎−1(1), 푥휎−1(2), . . . , 푥휎−1(푖+ 푗)) = 0.
The shuﬄe relations may be considered “easy” because they hold on the level of the sum over trees of the
integrands in (1.3).
We found another relation on the Hodge correlators. Together, the two relations form the double shuﬄe
relations. To state the new relations, we must introduce some notation.
Because of the multiplicative invariance (in weight > 1) of Hodge correlators, it is possible and convenient
to introduce an inhomogeneous notation for them, where the arguments are represented by the quotients
between successive nonzero values and the number of 0s between them. That is, given 푤0, . . . , 푤푘∈C∗such
that 푤0푤1 . . . 푤푘= 1, deﬁne
Cor∗
H(푤0|푛0, 푤1|푛1, . . . , 푤푘|푛푘) :=
= CorH(0, . . . , 0
|   {z   }
푛0
, 1, 0, . . . , 0
|   {z   }
푛1
, 푤1, 0, . . . , 0
|   {z   }
푛2
, 푤1푤2, . . . , 0, . . . , 0
|   {z   }
푛푘
, 푤1 . . . 푤푘).
(2.3)
This deﬁnition is illustrated in Figure 2.1.
The depth of an expression CorH(푧0, . . . , 푧푛) is one less than the number of arguments in the multiplicative
notation, that is, 푘in the formula above.
Our new shuﬄe relation states:
Õ
휎∈Σ푟,푠
Cor∗
H(푤휎−1(1)|푛휎−1(1), . . . , 푤휎−1(푟+푠)|푛휎−1(푟+푠), 푤0|푛0) + lower-depth terms = 0.
(2.4)
푧0
푧1
푧2
0
0
0
0
0
0
푛0
푛1
푛2
· · ·
|   {z   }
· · ·
|   {z   }
· · ·
|   {z   }
푛1
푛2
푛0
푤1
푤2
푤0
푤푖=
푧푖
푧푖−1
Figure 2.1. Deﬁnition of Cor∗
H: CorH(푧0, 0, . . . , 0
|   {z   }
푛1
, 푧1, 0, . . . , 0
|   {z   }
푛2
, 푧2, 0, . . . , 0
|   {z   }
푛0
) ≡Cor∗
H(푤1|푛1, 푤2|푛2, 푤0|푛0).
That is, we shuﬄe two ordered sets of expressions (푤푖| 푛푖), while leaving the segment (푤0 | 푛0) ﬁxed. For
example the (1, 1)-shuﬄe relation begins:
푛1
푛2
푛0
푤1
푤2
푤0
푛2
푛1
푛0
푤2
푤1
푤0
Cor∗
H(푤1|푛1, 푤2|푛2, 푤0|푛0)
+ Cor∗
H(푤2|푛2, 푤1|푛1, 푤0|푛0)
We explicitly describe the lower-depth terms in (2.4). They come in two kinds:
(1) Terms coming from the (푟, 푠)-quasishuﬄes that are not proper shuﬄes (see §1.2.3).
Whenever the
segments (푤푖| 푛푗) and (푤푗| 푛푗) collide, we get a new segment (푤푖푤푗| 푛푖+ 푛푗+ 1) in their place – a 0
is inserted – and the term picks up a negative sign.
For the (1, 1)-shuﬄe relation, there is only one quasishuﬄe that is not a shuﬄe. In this quasishuﬄe, the
two segments (푤1 | 푛1) and (푤2 | 푛2) collide:
푛1 + 푛2 + 1
푛0
푤1푤2
푤0
−Cor∗
H(푤1푤2|푛1 + 푛2 + 1, 푤0|푛0)
(2) Two additional terms: one where the segments 푤1, . . . , 푤푟appear in order and the remaining seg-
ments 푤푟+1, . . . , 푤푟+푠, 푤0 collapse; another where the segments 푤푟+1, . . . , 푤푟+푠appear in order and
푤1, . . . , 푤푟, 푤0 collapse. These terms come with a negative sign.
For the (1, 1)-shuﬄe relation:
푛2 + 푛0 + 1
푛1
푤2푤0
푤1
푛1 + 푛0 + 1
푛2
푤1푤0
푤2
−Cor∗
H(푤1|푛1, 푤2푤0|푛2 + 푛0 + 1)
−Cor∗
H(푤2|푛2, 푤1푤0|푛1 + 푛0 + 1)
In summary, the (1, 1)-shuﬄe relation states, for 푤0, 푤1, 푤2 ∈C∗and 푤0푤1푤2 = 1,
Cor∗
H(푤1|푛1, 푤2|푛2, 푤0|푛0) + Cor∗
H(푤2|푛2, 푤1|푛1, 푤0|푛0)
−Cor∗
H(푤1푤2|푛1 + 푛2 + 1, 푤0|푛0)
−Cor∗
H(푤1|푛1, 푤2푤0|푛2 + 푛0 + 1)
−Cor∗
H(푤2|푛2, 푤1푤0|푛1 + 푛0 + 1)
= 0.
It is already a nontrivial relation which is not easy to prove from the deﬁnition (1.3) even for 푛0 = 푛1 = 푛2 = 0.
By formula (1.10), Hodge correlators in weight 2 are expressed in a simple way in terms of the Bloch-
Wigner function L2.
The (1, 1)-shuﬄe relation with 푛0 = 푛1 = 푛2 = 0 is equivalent to the ﬁve-term
relation,
L2
 1 −푤1
1 −푤1푤2

+ L2
 1 −푤2
1 −푤1푤2

+ L2(1 −푤1푤2) + L2(푤1) + L2(푤2) = 0.
According to [B5], this is essentially the only functional equation for L2. It follows that the dihedral symmetry
and shuﬄe relations are the only relations between the Hodge correlators in weight 2.
For further illustration, let us write out the (2, 1)-shuﬄe relation for the Hodge correlator
Cor∗
H(푤1|0, 푤2|1|푤3|1, 푤4|0),
where 푤1 and 푤2 will be shuﬄed with 푤3:
(0) There are three terms from the shuﬄes:
푤1 푤2 푤3
푤1 푤3 푤2
푤3 푤1 푤2
1
푤1
0
푤1푤2
0
푤1푤2푤3
1
푤1
0
푤1푤3
0
푤1푤2푤3
1
0
푤3
푤1푤3
0
푤1푤2푤3
(1) There are two terms from the quasishuﬄes that are not shuﬄes:

푤1
푤3

푤2
푤1

푤2
푤3

1
0
0
푤1푤3
0
푤1푤2푤3
1
푤1
0
0
0
푤1푤2푤3
(2) There are two additional terms:
1
푤1
0
푤1푤2
0
0
1
0
푤3
0
0
0
The full relation is then
Cor∗
H(푤1|0, 푤2|1, 푤3|1, 푤4|0) + Cor∗
H(푤1|0, 푤3|1, 푤2|1, 푤4|0) + Cor∗
H(푤3|1, 푤1|0, 푤2|1, 푤4|0)
−Cor∗
H(푤1푤3|2, 푤2|1, 푤4|0) −Cor∗
H(푤1|0, 푤2푤3|3, 푤4|0)
−Cor∗
H(푤1|0, 푤2|1, (푤1푤2)−1|2) −Cor∗
H(푤3|1, 푤−1
3 |3)
= 0,
where the 3 + 2 + 2 terms in the three rows match the 3 + 2 + 2 pictures above.
We now write out the general relation:
Theorem 2.1. (a) Suppose that 푟, 푠> 1 and that not all 푛푖= 0 or not all 푤푖= 1. Then the Hodge correlators
satisfy the relation:
Õ
휎∈Σ푟,푠
(−1)푟+푠−푀휎Cor∗
H(푤휎−1(1)|푛휎−1(1), . . . , 푤휎−1(푀휎)|푛휎−1(푀휎), 푤0|푛0)
−Cor∗
H(푤1|푛1, . . . , 푤푟|푛푟, 푤{푟+1,...,푟+푠,0}|푛{푟+1,...,푟+푠,0})
−Cor∗
H(푤푟+1|푛푟+1, . . . , 푤푟+푠|푛푟+푠, 푤{1,...,푟,0}|푛{1,...,푟,0})
= 0,
where
푛퐼=
Õ
푖∈퐼
(푛푖+ 1) −1,
푤퐼=
Ö
푖∈퐼
푤푖.
(b) The Hodge correlators satisfy all specializations of this relation as any subset of the 푤푖(1 ≤푖≤푛)
approaches 0.
Applications
Theorem 2.1 gives simple proofs of certain results of [GR].
Corollary 2.2 ([GR], Proposition 2.8). For 푛> 2, every Hodge correlator of weight 푛is a linear combination
of Hodge correlators of weight 푛and depth at most 푛−2. Explicitly, for 푧1, . . . , 푧푛∈C∗, we have
CorH(푧1, . . . , 푧푛, 0) =
푛
Õ
푖=1
CorH

푧1, . . . , 푧푖−1, 푧푖, 푧푖
푧1
푧푛
, . . . , 푧푛−1
푧1
푧푛
, 푧푛
푧1
푧푛

−
푛
Õ
푖=2
CorH

푧1, . . . , 푧푖−1, 0, 푧푖
푧1
푧푛
, . . . , 푧푛−1
푧1
푧푛
, 푧푛
푧1
푧푛

−CorH

푧1, 푧1
푧1
푧푛
, 0, . . . , 0

.
(2.5)
In weight 3, we deduce the Hodge correlator version of relations (27) and (29) from [GR].
Corollary 2.3. The Hodge correlators in weight 3 satisfy the relations:
CorH(1, 0, 0, 푥) + CorH(1, 0, 0, 1 −푥) + CorH(1, 0, 0, 1 −푥−1) = CorH(1, 0, 0, 1),
(2.6)
CorH(0, 푥, 1, 푦) = −CorH(1, 0, 0, 1 −푥−1) −CorH(1, 0, 0, 1 −푦−1) −CorH

1, 0, 0, 푦
푥

−CorH

1, 0, 0, 1 −푦
1 −푥

+ CorH

1, 0, 0, 1 −푦−1
1 −푥−1

+ CorH(1, 0, 0, 1).
(2.7)
We have noted that the double shuﬄe and dihedral symmetry relations give all relations between Hodge
correlators in weight 2. In weight 3, the Hodge correlators of depth 1 are expressed in terms of the single-
valued trilogarithm L3 (see the end of §1.2.3). By the results of [GR], the relations (2.7) imply the general
functional equation for L3 ([G1]). We conclude that the double shuﬄe relations for Hodge correlators imply
all functional equations for L2 and L3.
푥0
푥1
푥푛
푥푖푥푖+1
훿↦→
푥0
푥푛
푥푖+1
∧
푥0
푥1
푥푖
Figure 2.2. The typical term of the coproduct in the cyclic Lie coalgebra.
