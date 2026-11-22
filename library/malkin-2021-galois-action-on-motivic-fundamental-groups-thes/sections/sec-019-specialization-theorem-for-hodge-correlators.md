---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-019-specialization-theorem-for-hodge-correlators
section_title: "Specialization theorem for Hodge correlators"
section_number: null
pages: 71-76
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
toc_source: outline
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
Specialization theorem for Hodge correlators
We now study how the Hodge correlators over a base 퐵behave when the sections collide. This will require
extending the theory of Hodge correlators to nodal curves.
The correlator Lie coalgebra for nodal curves
Recall the moduli space M′
0,푛of 푛distinct points and a distinguished tangent vector on P1. Its Deligne-
Mumford compactiﬁcation M
′
0,푛consists of the nodal curves of genus 0, i.e., those whose dual graph is a
tree and in which every component is a punctured projective line. with 푛marked points and a distinguished
tangent vector 푣∞.
Let 푋= Ð
푖푋푖be a genus 0 nodal curve with a set of punctures 푆. Let 푇be the dual tree of 푋, with vertices
indexed by 푖corresponding to 푋푖, rooted at the component 0 with the base point 푠0 ∈푋0, oriented away from
the root (write 푖→푗if (푖, 푗) is an edge). Choose a coordinate 푧푖on each 푋푖such that the point joining the
component to its parent 푋푗is (푧푖= ∞, 푧푗= 푣푗푖), and the base point on 푋0 is at 푧0 = ∞with tangent vector
푣∞. Let 푆푖be the set of punctures on 푋푖. Let 푁푖=

푣푖푗: 푖→푗
	
.
We deﬁne the correlator Lie coalgebra for the nodal curve 푋by
CL∨
푋,푆,푣∞=
Ê
푖
CL∨
푋푖,푆푖∪푁푖,푣푖,
(2.108)
where 푣푖is the tangent vector −1
푧2
푖
휕
휕푧푖at 푧푖= ∞.
It coincides with the usual deﬁnition if 푋is smooth, justifying the notation. If 푋is not smooth, it is
diﬀerent from g
CL
∨
푋,푆,푠0, the coalgebra naively deﬁned as the tensor algebra of 푆modulo cyclic symmetry
and shuﬄe relations with a 퐻2(푋) coeﬃcient. They are related in the following way. For each 푖, there is a
surjective coalgebra morphism to the component of the direct sum corresponding to 푋푖:
g
CL
∨
푋,푆,푠0
휋푖
−−→CL∨
푋푖,푆푖∪푁푖,푣푖.
To deﬁne it on a generator (푥1 ⊗· · · ⊗푥푛) ⊗[푋푖], let 푝be the common parent of the components containing
the 푥푗. If 푝≠푖, the 푖-th component of the map is 0. Otherwise, set
휋푖(푥) =


푥,
푥∈푋푖
푧푖= 푣푖푗∈푁푖,
푥∈푋푘, where ∃path 푖→푗→· · · →푘
,
extended to preserve the tensor product. That is, points in 푋푖remain, while points in components below 푋푖
collapse to the nearest node on 푋푖. Evidently this map preserves the coproduct and deﬁning relations. Taking
the direct sum of the maps 휋푖, we have produced a coalgebra morphism:
휋: g
CL
∨
푋,푆,푣∞→CL∨
푋,푆,푣∞.
It preserves the decomposition of the domain by 퐻2(푋) = É
푖퐻2(푋푖).
In particular, if (푋, 푆, 푣0) vary over a base 퐵→M′
0,푛, and the variation extends to 퐵→M
′
0,푛, with
퐷= 퐵\ 퐵, then we have a degeneration map
휋퐷: CL∨
푋/퐵,푆,푣∞→g
CL
∨
푋/퐷,푆,푣∞→CL∨
푋/퐷,푆,푣∞,
(2.109)
where the ﬁrst map simply applies the induced map on 퐻2 and the second map is the quotient deﬁned above.
The composition forgets the way in which the sections in 푆collided at boundary of 퐵.
Specialization theorem
Recall that an element of CL∨
푋/퐵,푆,푣∞over a base 퐵→M′
0,푛determines, by the map CorHod, a variation of
Hodge structures over 퐵, and, by the period map 푝, a smooth function on 퐵. The maps CorHod and 푝also
exist for 푋a nodal curve, extended by linearity from the deﬁnition (2.108).
Theorem 2.23. Suppose 퐵→M′
0,푛is a family of curves (푋, 푆, 푣∞) extending to 퐵→M
′
0,푛, with 퐷= 퐵\ 퐵
a normal crossings divisor, and suppose 푥∈CL∨
푋/퐵,푆,푠0 of weight 푛> 1.
(a) The Deligne’s canonical extension to 퐷of the variation of framed mixed Hodge structures determined
by CorHod(푥) is independent of the normal vector to 퐷. Thus there is a specialized map Spec퐷CorHod :

CL푋/퐵,푆,푣∞→Lie∨
HT/퐷

푤>1.
(b) This specialized map coincides with the Hodge correlator of the degeneration map:

CL∨
푋/퐵,푆,푣∞

푤>1
휋퐷/
CorHod


CL∨
푋/퐷,푆,푣∞

푤>1
CorHod

(Lie∨
HT/퐵)
Spec퐷
/ (Lie∨
HT/퐷).
.
(c) Let 푡= 0 be a local equation for 퐷. Then
lim
푡→0 푝(CorHod(푥푡)) = 푝(퐶표푟Hod(푥푡=0)).
Proof. Let 푥∈CL∨
푋/퐵,푆,푣∞be a generator of weight 푤> 1. For any 푣a normal vector to 퐷, we get the
specialized framed mixed Hodge-Tate structure Spec푣
퐷CorHod(푥).
We must show that:
(1) The periods of CorHod(푥) extend continuously to 퐷.
(2) The coproduct of Spec푣
퐷CorHod(푥) does not depend on the direction of specialization 푣at any smooth
point of 퐷.
(3) The periods of the specializations (i.e., the limits of the periods at 퐷) coincide with the periods of the
degeneration to 퐷.
We will prove (1)-(3) by induction on the weight. First, let us see how they imply the result.
Assuming (2), the coproduct of Spec푣
퐷CorHod(푥) is independent of 푣. Because the coproduct commutes
with Spec푣
퐷, this element is independent of 푣up to Ext1(R(0), R(푛)), which is 1-dimensional and controlled
by the period. By (1), the period is independent of the direction of specialization, which gives (a). By (3), it
coincides with the period of the degeneration, which gives (b). Then (c) follows by the deﬁnitions from (b).
To show (1), we let {휀푖= 0} be a set of smooth local equations for 퐷and prove that 푝(CorHod(푥)) can
be represented locally as a polynomial in the log 휀푖such that the terms with log 휀푖appearing in positive
degree have coeﬃcients vanishing along {휀푖= 0} (tame logarithmic singularities). This will follow from the
diﬀerential equations on the periods. Note that in weight 1, the period of 퐶(푥, 푦) has a (not tame) logarithmic
singularity along 푥= 푦. In weight > 1, we proceed by induction.
Consider a simple element 푥= 푥0 ⊗· · · ⊗푥푛∈CL∨
푋/퐵,푆,푣∞(푛> 1). Suppose that not all 푥푖collide on 퐷,
so we must only consider the summand of the nodal CL∨
푋/퐷,푆,푠0 corresponding to the component containing
the base point. The terms of 훿(푥) can be grouped into those of two forms:
(i) 푥′ ∧푥′′, where not all sections in 푥′ and in 푥′′ collide to the same section on 퐷;
(ii) 푥′ ∧(푥′′
1 −푥′′
2 ), where not all sections in 푥′ collapse on 퐷, but 푥′′
1 and 푥′′
2 coincide on 퐷.
By the inductive hypothesis, the specialization of 훿(푥) does not depend on the direction of specialization:
for terms (i), 푥′ and 푥′′ satisfy (2), while in terms (ii) the 푥′′
1 −푥′′
2 vanish under specialization to 퐷. This gives
(2).
For (1), from the diﬀerential equations on the periods (1.14), we see that 푑퐵푝(CorHod(푥)) is a sum of
terms that are smooth over 퐵with logarithmic singularities along 퐷(from type (i)) and terms that vanish along
퐷by the inductive hypothesis (from type (ii)). We conclude that 푝푣∞(푥) has tame logarithmic singularities
along 퐷.
If all 푥푖collide on 퐷, we simply pass to their common parent component and apply the same argument.
We conclude with (3). We have shown that the specializations of Cor푣0
Hod and its coproduct to 퐷exist at
every point and their periods are independent of 푣, and thus the specialized period map 푝◦CorHod is equal to
the period of the degeneration up to adding a constant for each smooth component of the smooth locus of 퐷.
We must show the constant 0.
It is enough to show this for 퐷a lowest-codimension boundary stratum in M
′
푔,푛. We are done by the next
lemma.
□
Lemma 2.24. Let 퐼be a proper subset of {0, 1, . . . , 푛} (푛> 1) and 푥0, . . . , 푥푛∈C∗with 푥푖≠푥푗if 푖≠푗and
either 푖, 푗∈퐼or 푖, 푗∉퐼. Let
푥푖(푡) =


푡푥푖
푖∈퐼,
푥푖
푖∉퐼
.
Then
CorH(푥0(푡), 푥1(푡), . . . , 푥푛(푡))
is continuous at 푡= 0.
Proof. For 푛= 2, this amounts to continuity of L2 at 1.
In the proof of Theorem 2.23 it was established that
lim
푡→0 CorH(푥0(푡), 푥1(푡), . . . , 푥푛(푡)) −CorH(푥0(0), 푥1(0), . . . , 푥푛(0))
is independent of the 푥푖, for generic 푥푖. Let us integrate this diﬀerence over (푥0, . . . , 푥푛) ∈(푆1)푛+1, with
respect to the standard measures 휇(푥푖) of volume 1 on 푆1 = {|푧| = 1} ⊂C.
The limit is uniform in the directions 푥푖(푖∈퐼), and so
∫
lim
푡→0 CorH(푥0(푡), 푥1(푡), . . . , 푥푛(푡))
Ö
푑휇(푥푖) = lim
푡→0
∫
CorH(푥0(푡), 푥1(푡), . . . , 푥푛(푡))
Ö
푑휇(푥푖).
To conclude, it suﬃces to show that
∫
CorH(푥0(푡), 푥1(푡), . . . , 푥푛(푡))
Ö
푑휇(푥푖) = 0.
(2.110)
for all 푡.
For any tree푇entering into the Feynman integral expression for (2.110), choose a pair of boundary vertices
(without loss of generality, labeled 푥0 and 푥1) incident to a common internal vertex 푣with corresponding
variable 푥푣, and let 푥푤be variable corresponding to the third vertex incident to 푣. Then the integral over the
푥푖contains the term
∫
푥0,푥1
∫
L2
푥푤−푥0(푡)
푥푤−푥1(푡)

∧(terms independent of 푥0(푡), 푥1(푡))

푑휇(푥0) 푑휇(푥1).
Exchanging the two integrals and noting that L2( 푧−푎
푧−푏) changes sign under the involution
푎↦→푎푧2
|푧|2 ,
푏↦→푏푧2
|푧|2 ,
we conclude that this expression is 0.
□
The specialization theorem states that when the punctures labeling an element of CL∨collide, only the
component nearest to the base point of the resulting nodal curve determines the limit Hodge correlator. We
obtain as a corollary Theorem 1.6:
Theorem. The Hodge correlators CorH(푧0, . . . , 푧푛) are continuous on C푛+1 \ {푧0 = · · · = 푧푛}.
For example, L2 is continuous with a tame logarithmic singularity at 1, but L2
  푎−푐
푏−푐
 has no limit as
푎, 푏, 푐→0.
