---
doc_id: arxiv-2601.07042v1
doc_title: "A Tannakian description of the local Kaletha gerbe"
section_id: sec-011-27-the-category-rigisocf
section_title: "The category RigIsocF"
section_number: 2.7
pages: 16-17
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
toc_source: outline
doc_brief: "A Tannakian description of the local Kaletha gerbe — We construct, for a p-adic field F, an explicit semisimple Tannakian category RigIsocF whose category of fiber functors recovers Kaletha’s Galois"
---
rigid inner forms. We define the category RigIsocF to be the direct limit of the categories RIE{F,s over the
inductive system of tuples pE, sq, where E{F is a finite Galois extension and s P N, which is ordered by
the relation that pK, s1q ą pE, sq if and only if K contains E and s | s1, with respect to the transition
maps pK{E,s,s1 defined in the previous subsection. It will frequently be convenient to fix a cofinal system
of objects in the indexing category indexed by N, denoted by pEk, nkq. Note that lim
ÝÑk RIk “ RigIsocF ,
where RIk :“ RIEk{F,nk.
By construction, RigIsocF is a Tannakian category over F, with fiber functor over L, and the correspond-
ing gerbe is banded by the F-group scheme u “ lim
ÐÝk ResEk{F pµnkq. Note that each category RIE{F,s has a
fiber functor over the finite extension Es{F, given explicitly by sending pV, D, Φq to the (finite-dimensional)
Es-vector space
(1)
à
0ďpaσ{sqă1
pr
à
pbσqPś
ΓE{F Z
V fs
E¨pś σpϖEq´raσ`sbσsqs bRE{F RE{F {Iq,
where V fs
E¨pś σpϖEq´raσ`sbσsq denotes the subgroup of V of all elements on which fs
E acts by the scalar
ś
σPΓE{F σpϖEq´raσ`sbσs. Note that the above expression is well-defined, since the internal direct sum
is RE{F -stable. We may extend this to a fiber functor over F by simply post-composing the above fiber
functor over Es with ´ bEs F. By considering the automorphisms of this fiber functor over F, we get
a canonical cohomology class in the group H2pΓF{F , ResE{F pµsqpFqq, which we now compute. Since
RIE{F,s is a quotient of IE{F,s, the above cohomology class maps to the class corresponding to the group
of automorphisms of the fiber functor IE{F,s Ñ VectF given explicitly by tensoring the Es-fiber functor
pV, D, ˜Φq ÞÑ
à
paσ{sqPś
ΓE{F
1
s Z
V fs
E¨pś σpϖEq´aσ q
with F over Es, under the canonical map H2pΓF{F , ResE{F pµsqpFqq Ñ H2pΓF{F , ResE{F pGmqpFqq,
noting that the above fiber functors are compatible with the quotient functor from IE{F,s to RIE{F,s, and
using [Mil07, §2.10].
Because of the above observation, it will be useful to first describe the corresponding cohomology class
in H2pΓF{F , ResE{F pGmqpFqq corresponding to IE{F,s.
Since the Tannakian category IE{F,s over F
has base-change to E which is isomorphic as Tannakian categories over E to PE{F,s, it follows that the
image of this class in H2pE, ResE{F pGmqpFqq is the ΓE{F -fold product of the classes ´1{s P Q{Z in
ś
ΓE{F H2pE, GmpFqq. In particular, the image of this class under the Shapiro isomorphism
H2pΓF{F , ResE{F pGmqpFqq „
ÝÑ H2pΓF{E, GmpFqq
is the class mapping to ´1{s P Q{Z under the local invariant map.
Recall that H2pΓF{F , upFqq “ lim
ÐÝk H2pΓF{F , ukpFqq, where uk :“ ResEk{F pµnkq. Using Hilbert 90
and Shapiro’s Lemma, we see that the latter groups fit into the exact sequence
0 Ñ H2pΓF{F , ukpFqq Ñ H2pΓF{F , ResEk{F pGmqpFqq
xÞÑnkx
ÝÝÝÝÑ H2pΓF{F , ResEk{F pGmqpFqq,
and so we get, via Shapiro’s Lemma and the local invariant map, a canonical identification of the cohomol-
ogy group H2pΓF{F , ukpFqq with ´ 1
nk Z{Z. Moreover, it follows from our above discussion that the gerbe
corresponding to the Tannakian category RIk has cohomology class equal to the element ´ 1
nk . For l ą k,
the projection map H2pΓF{F , ulpFqq Ñ H2pΓF{F , ukpFqq corresponds (via the F-fiber functor given by
16
direct limit of the F-fiber functors for each RIk, which are evidently compatible) to the multiplication-by-
nl{nk map from 1
nl Z{Z to
1
nk Z{Z. We thus conclude that the category RigIsocF corresponds to the class
´1 P pZ “ lim
ÐÝk
1
nk Z{Z “ H2pΓF{F , upFqq, which is exactly what we want. All in all, we have proved:
Theorem 2.11. The Galois gerbe given associated to the gerbe of fiber functors of RigIsocF represents the
class ´1 P pZ – H2pΓF{F , upFqq. In particular, we may identify RigIsocF with ReppEKalq.
Remark 2.12. As noted in the introduction, we use an alternative presentation of the group scheme u to
the presentation u1 (a priori a different group) used in [Kal16a]. Nevertheless, the map u Ñ u1 is an
isomorphism. It suffices to show this at the level of character modules, where the map is the inclusion
lim
ÝÑ
E{F
pQ{ZqrΓE{F s0 Ñ lim
ÝÑ
E{F
pQ{ZqrΓE{F s,
where the direct limit is over all finite Galois extensions. Surjectivity comes from the fact that for a fixed
x P Q{ZrΓE{F s which is m-torsion, if we take K{E{F finite Galois with m | rK : Es then the image of x
in Q{ZrΓK{F s lies in Q{ZrΓK{F s0. We warn that this result is false when F “ R.
