---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-001-11-motivation-and-overview
section_title: "Motivation and overview"
section_number: 1.1
pages: 1-3
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
injection from irreducible smooth representations ofGpFq, forGreductive and quasi-split, to enhanced
L-parameterspϕ,ρqwhereϕ: WD F Ñ LG(hereWD F “W F ˆSL 2pCqis theSL 2 form of the Weil–
Deligne group) andρis an algebraic irreducible representation of the centralizer groupS ϕ of the image
ofϕ. The image of the refined correspondence map should be contained in the set of pairspϕ,ρqsuch that
ρPIrrpπ 0pSϕ{Zp pGqΓFqq. V ogan ([V og93]) proposed that in order to upgrade the correspondence to contain
Irrpπ0pSϕqqĂIrrpS ϕqin its image, one should enlarge the domain by adding in irreducible representations
of inner forms ofG. In [BMO25], Oi and the first named author showed that if a refined local Langlands
correspondence exists forGand its Levi subgroups, one can upgrade it to a bijection with the entire target
IrrpSϕqif one further allows irreducible representations of Levi subgroups ofGon the automorphic side.
The question of exactly how to parametrize inner forms ofG(and possibly its Levi subgroups) in this
context is a subtle one because the cohomology groupH 1pF,G adqis not sufficiently rigid, in the sense that
translating byG ad-coboundaries identifies non-isomorphic representations ofGpFq. However, there are
many options for sufficiently rigid cohomology sets including the ‘pure inner forms’ given byH 1pF,Gq,
the ‘extended pure inner forms’ classified by the Kottwitz setBpGq bas, and finally ‘rigid inner forms’
defined by Kaletha in [Kal16a] and corresponding to basic classesH 1
baspEKal,Gqof the rigid gerbe denoted
EKal in this paper. This last set has the advantage that it surjects ontoH 1pF,G adq, whereas the others do
not in general. For a nice discussion of this topic, we recommend the survey article [Kal16b].
One advantage that the Kottwitz setBpGq bas (or more generallyBpGq) has is that there is an explicit
Tannakian category, namely that ofF-isocrystals,Isoc F , whose objects are in bijection with š
nBpGLnq
fornPN. The category ofF-isocrystals appears naturally in Dieudonné theory and hence has connections
to local Shimura varieties. By the Tannakian formalism, we can thus view the isocrystal gerbeE iso (cf.
[LR87] where this is called the Dieudonné gerbe), whose algebraic cohomology isBpGq, as the Galois
gerbe obtained from the gerbe of fiber functors ofIsoc F and, in the other direction, identify the tensor
categoryReppE isoqwithIsoc F (see [Tai25, §7.1] for a summary of this formalism).
The goal of the present work is to construct a Tannakian category of “Rigid Isocrystals”RigIsocF which
can be canonically identified withReppE Kalqand whose objects are classified by š
nH1pEKal,GLnqfor
nPN. Considered as a Galois gerbe,E Kal is an extension ofΓF{F byupFq, whereuis the pro-multiplicative
grouplimÐ ÝE{F,n ResE{Fpµnq, where the limit is takes over all finite Galois extensionsE{Fand all natural
numbersn. We alert the reader that this group was originally defined in [Kal16a] withu 1 in place ofu,
where
u1“limÐ Ý
E{F,n
ResE{Fpµnq
µn
,
Date: January 2026.
1
arXiv:2601.07042v1  [math.NT]  11 Jan 2026
but one can useuas well because the natural mapuÑu 1 is an isomorphism (see Remark 2.12). Kaletha
works with theu 1-presentation of this group because it gives the correct object overRas well. Since we
only considerp-adic fields, it suffices to consider theu-presentation.
The point of our article is to explain that since the gerbeE Kal can be constructed from the isocrystal
gerbe with bandGm by a relatively simple sequence of operations, the same is true at the level of Tannakian
categories. Let us describe the operations we need to consider. Beginning with the isocrystal gerbe with
bandGm, we pass to the subgroupµn. At the level of Tannakian categories, this is a quotient operation and
is realized by passing to a certain module category. After this, we take products to get a gerbe with bandś
ΓE{F
µn,E and then descend this gerbe to produce one with bandRes E{Fpµnq. Finally, we take limits over
E,n. By understanding just these four operations, products, modules, limits, and descent, we can produce a
Tannakian category for the gerbeE Kal.
Theorem 1.1.There is a Tannakian categoryRigIsoc F whose associated gerbe of fiber functors represents
rEKals 1 and is described as follows. Its objects consists of tuplespV, ˜Φ,n,EqwherenPN, andE{Fis a
finite Galois extension. The other components of this tuple are given as follows:
‚ pV,Dqis a vector space overLE ,the completion of the maximal unramified extension ofE, equipped
a ś
ΓE{F
1
n Z-gradingDand an action of the ringR E{F :“L Er ś
ΓE{F
Zswhich is additive on the grad-
ings and makesVa finitely-generatedR E{F -module;
‚ ˜Φis a semilinear action ofW LE{F onVthat acts in the natural way on the gradingDand is
compatible with the action ofWLE{F onRE{F (cf. §2.4 for the description of this action) ;
‚There is anL E-basis of thepa σqσ-graded piece ofVsuch that annth powerf n
E of a choicef E of
the Frobenius ofEinW LE{F acts by ś
σPΓE{F
σpϖEqaσ, forϖE a fixed choice of anti-uniformizer.
Morphisms betweem two such objects inRigIsoc F areW LE{F -equivariant graded morphisms ofR E{F -
modules.
In the final section, we discuss the structure of the Tannakian categoryRigIsoc F , which is semisimple,
and give a number of examples of its simple objects. We point out that the situation differs fairly dramatically
from that ofIsoc F concerning the role of basic objects—inIsoc F (resp.RigIsoc F ) these are the objects
whose graded pieces are concentrated in oneQ- (resp. ś
ΓE{F
Q{Z-) degree and are important because they
give inner forms ofGL n. ForIsoc F , the simple objects are all basic and are classified according to the
Dieudonné–Manin classification by a rational sloper{sPQwritten in reduced form. A basic isocrystal is
simple ifsequals the dimension of the underlyingL-vector space.
In our situation, the simple objects ofReppE Kalqneed not be basic, but instead come from certain basic
classes ofH 1pEKal,MqforMan elliptic twisted Levi subgroup ofGL n. Recall that twisted Levi subgroups
areF-rational subgroups that become Levi subgroups upon base-change and are precisely the centralizers
ofF-rational tori. A twisted Levi subgroup isellipticif the split rank of its center equals that ofG, and the
elliptic twisted Levi subgroups ofGL n are all isomorphic toRes E{F GLs withsrE:Fs “n. The set of
basic classes of such a twisted Levi are in bijection with tuplespa iq P pQ{ZqHomFpE,Fq such that ř
i
ai P
1
s Z{Z. In this paper we explain how to explicitly construct the simple object inRigIsoc F corresponding to
each suchEandpa iq. More precisely, we prove:
Theorem 1.2.Every isomorphism class of simple objects inRigIsocF may be represented by a pairpE,paiqq
whereE{Fis a finite separable field extension and the tuplepa iqis an element ofpQ{Zq HomFpE,Fq which is
not inflated from a tuple inpQ{Zq HomFpK,Fq for any proper subextensionF{K{E. For a fixed collection of
1Of course, one can always take the Tannakian categoryReppE Kalqand recoverE Kal as the associated gerbe, but the point of
this result is to give a more explicit Tannakian category.
2
finite extensionstEuwhich have the same Galois closure rEand are an orbit underΓ rE{F , the groupΓ rE{F
acts on all such pairs involvingE 1PtEu, and two arbitrary pairs give the same isomorphism class if and
only if the extensionsE 1,E 2 are related in this manner and the pairs lie in the sameΓ rE{F -orbit.
In the case ofE iso, the explicit linear-algebraic description ofReppE isoqhas many uses, such as in the
definition of crystalline cohomology, Dieudonné theory forp-divisible groups, and in the definition of the
stackIsocG in Zhu’s ([Zhu25]) geometrization of the local Langlands correspondence. It is reasonable to ask
analogous questions ofRigIsoc F ; namely if there is a natural cohomology theory valued in this Tannakian
category and if this category leads to a more refined geometrization of the local Langlands correspondence.
We do not take up these questions here, but we do relateRigIsoc F to Fargues’ categoryIsoc e
F of extended
isocrystals [Far22] and remark that steps towards a refined geomerization are taken in that paper.
