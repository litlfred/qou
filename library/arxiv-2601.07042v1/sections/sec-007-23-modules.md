---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-007-23-modules
section_title: "Modules"
section_number: 2.3
pages: 7-9
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
ΓE{F
Z-gradedLE-algebra
à
pbτqτPś
ΓE{F
Z
pLEqpbτqτ,
with addition defined component-wise and multiplication determined byℓpbτqτ¨ℓ1
pcτqτ “pℓ¨ℓ 1qpbτ`cτqτ for
allℓ,ℓ 1PL E. This ring will also be equipped with anf E-semilinear action, denoted byΦ RE{F , determined
by the semilinearity condition and the identityΦRE{Fp1pbσqq“ ś
γPΓE{F
γpϖEqbγ1pbσq.
Definition 2.6.For a positive integers, we define the categoryRP E{F,s to have objects given by tuples
pV,Φ,Dq, consisting of
‚a (not necessarily finite-dimensional)L E-vector spaceVequipped with anR E{F -action such that it
is finitely generated as anRE{F -module,
‚anf E-semilinear isomorphismΦ,
‚and a ś
ΓE{F
1
s Z-gradingDsuch thatV paσ{sq has anL E-basis on whichΦ s acts by the scalarś
σPΓE{F
σpϖEqaσ.
In addition, we require that theR E{F -action is compatible with theΦ-action, in the sense that, for all
vPVandrPR, we haveΦpr¨vq“Φ RE{Fprq¨Φpvq. Note that this last condition implies that
1pbσq¨Vpaσ{sqĎVpaσ`sbσ
s q.
Morphisms inRP E{F,s will beΦ-equivariant morphisms ofR E{F -modules that preserve the gradings.
Note thatRP E{F,s is a rigid abelian tensor category overEwith identity objectR E{F (with the canonical
RE{F -module structure, andΦ“Φ RE{F ).
We now define a fiber functor for this category. First, note that there is a canonical surjective augmentation
mapR E{F ÑL E defined by sending each1pbσq to1, whose kernel we will denote byI. Note for an object
pV,Φ,DqofRP E{F,s, thatVis a finitely generated and free, hence flat,R E{F -module. Hence, we have an
equality ofL E-vector spacesVb RRE{F{I“V{IV. We define a functorω RPE{F,s :RP E{F,s ÑVectLE
by
pV,Φ,DqÞÑV{IV.
Note thatIVis exactly the kernel of the naturalL E-linear surjectionVÑ À
p0qďpaσ{sqăp1qVpaσ{sq
defined on eachVpraσ`sbσs{sq by multiplication by1p´bσq. This defines anL E-linear tensor functor.
Lemma 2.7.The above functor is a fiber functor; that is, it is faithful and exact.
7
Proof.We first prove faithfulness. Letfandgbe two morphisms fromVtoW(we omit the other structure
from our notation for brevity), and suppose that their image under this functor coincides, and letV pbσ{sq be
a fixed graded component ofV. Since these categories are additive, we may assume thatgequals zero. For
anyvPV pbσ{sq, we know thatfpvq PW pbσ{sq, but also thatfpvq PIW, and thus conclude by observing
thatIWXW pbσ{sq“0for all tuplespb σ{sq.
We now prove exactness. By construction, this functor is evidently right-exact, so we only need to prove
that it preserves injections. To this end, suppose thatvPVis such thatfpvqPIWfor injectivef. Writing
v“
ÿ
paσ{sq
vpaσ{sq
in terms of graded components, we note that, sincefisR E{F -linear, for allpbσq, we have
fpvpraσ`sbσs{sqq“1 pbσq¨fp1 p´bσq¨vpraσ`sbσs{sqq.
It follows that
fpvq“
ÿ
p0qďpaσ{sqăp1q
ÿ
pbσq
1pbσq¨fp1 p´bσq¨vpraσ`sbσs{sqq.
For this expression to lie inIW, it is necessary that, for a fixedp0qďpa σ{sqăp1q, we have
ÿ
pbσq‰p0q
fp1p´bσq¨vpraσ`sbσs{sqq“´fpv paσ{sqq
inside the spaceWpaσ{sq. Sincefis injective, this means that
ÿ
pbσq‰p0q
1p´bσq¨vpraσ`sbσs{sq“´vpaσ{sq
inVpaσ{sq, which implies thatvPIV.□
It follows from the above Lemma 2.7 thatRP E{F,s is a Tannakian category overE. Fors|s 1, note that
the embedding functorι s,s1 extends naturally to a functor, also denoted byι s,s1, fromRP E{F,s toRP E{F,s1,
defined identically (with theRE{F -module structure ofιs,s1pXqbeing the same as the one associated toX).
As before, the direct limit of these categories will be denoted byRPE{F.
We now want to investigate the band ofRP E{F,s (and thusRP E{F ). There is an “extension of scalars"
functorq:P E{F,s ÑRP E{F,s given byVÞÑR E{F bLE Von objects, and byfÞÑid RE{F bfon
morphisms, which is anL E-linear tensor functor. Recall that an exact tensor functor between Tannakian
categoriesPandQis called aquotient functorif every object ofQis a subquotient of an object in the image
of the functor.
Proposition 2.8.The functorq:P E{F,sÑRP E{F,s is a quotient functor.
Proof.SinceR E{F is a flatL E-module, the functorqis evidently exact. To show the other condition for
quotient functors, letpV,Φ,Dqbe an object ofRP E{F,s, and lette iun
i“1 be a set of generators forVas an
RE{F -module, which we may assume without loss of generality is such thate i PV paσqσ (depending oni)
on whichΦ s acts in the appropriate way. We then get an object ofP E{F,s by taking theL E-span ofte iu,
with the obvious inherited grading andΦ-action; denote this object byp ˜V, ˜Φ, ˜Dq. ThenR E{F bLE
˜Vis a
freeR E{F -module, with basist1be iu, and there is a quotient mapR E{F bLE
˜VÑVsending1be i to
ei, which is a morphism inRP E{F,s, giving the result.□
In the notation of [Mil07, §2], recall thatP q
E{F,s denotes all objects ofP E{F,s whose image underqis
isomorphic to a direct sum of copies of the identity object inRPE{F,s, which is a full Tannakian subcategory
overE. Observe that an objectpV,Φ,DqinP E{F,s lies inP q
E{F,s if and only if the only nonzero graded
componentsVpaσ{sq are such that eacha σ{sis an integer. According to [Mil07, §2], the band of the gerbe
corresponding toRP E{F,s is canonically isomorphic to all automorphisms of the fiber functor ofP E{F,s
8
which restrict trivially toP q
E{F,s. In order to investigate how the band acts on the restriction of the fiber
functor to these objects, it is easiest to use our identification ofPE{F,s with RepLEpEpcσqσqfrom the previous
subsection. We will work not withP E{F,s, but instead withP E{F,s,L, which is the same category asP E{F,s
except replacingL E-vector spaces with L-vector spaces and the semilinearf E-action with a semilinear
WF{E -action that acts on anL-basis of the graded pieces in the same way (after restricting toΓLE{E).
Letpx σqP ś
ΓE{F
GmpFq, which acts on the canonical F-fiber functor of RepFpEpcσq,Fqby, for a fixed
representationV, mapping the ś
ΓE{F
Z-graded pieceVphσq to itself via sendingvtop śxhσ
σ qv. The image
of the subcategoryP q
E{F,s,F under the above equivalence is all representations whose only nonzero graded
pieces have eachhσ divisible bys. These two observations make show that the subgroup of ś
ΓE{F
GmpFq
fixing the image ofP q
E{F,s,F is exactly ś
ΓE{F
µspFq, which implies (since we know that the band is an
E-subgroup scheme of the band ofE pcσqσ, which is ś
ΓE{F
Gmq) that the band of the gerbe overEcorre-
sponding to the Tannakian categoryRPE{F,s may be identified with theE-group scheme ś
ΓE{F
µs.
