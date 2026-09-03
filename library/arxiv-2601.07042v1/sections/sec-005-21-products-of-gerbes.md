---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-005-21-products-of-gerbes
section_title: "Products of gerbes"
section_number: 2.1
pages: 3-6
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
2.2. Limits of gerbes 6
2.3. Modules 7
2.4. Descent 9
2.5. Concrete Tannakian categories 12
2.6. Transition maps 14
2.7. The categoryRigIsoc F 16
3. The structure ofRigIsoc F 17
3.1. The Newton map 17
3.2. Comparison with isocrystals 18
3.3. Comparison with Fargues’ extended isocrystals 18
3.4. Reduction to Newton centralizers 20
3.5. Classification of simple objects 22
References 25
3
2. CONSTRUCTION OFTANNAKIANCATEGORIES
All Tannakian categories constructed in this section are built from the category of isocrystals, whose
objects are pairspV,Φq, whereVis a finite-dimensionalL-vector space andΦis af F -semilinear automor-
phism and whose morphisms areΦ-equivariant linear maps. For a fixedsPN, one can also consider the full
subcategory of allpV,Φqwhich have a basis on whichf s
F acts on each basis element by a (possibly different)
power ofϖF .
2.1.Products of gerbes.
Definition 2.1.FixsPN. Then we define the categoryP E{F,s as follows.
‚Objects are triplespV,Φ,Dq, whereVis a finite-dimensionalL E-vector space,Φ:VÑVis an
fE-semilinear automorphism, andDis a ś
ΓE{F
1
s Z-grading onVsuch that the subspaceV pbσ{sqσ has
anLE-basis on whichΦs acts by the scalar ś
γPΓE{F
γpϖEqbγ .
‚Morphisms inP E{F,s will beΦ-equivariant morphisms ofL E-spaces which preserve the gradings.
Lemma 2.2.The categoryP E{F,s can be equipped with the structure of a Tannakian category overEin a
natural way. The forgetful functorωPE{F,s :P E{F,sÑVectLE is a fiber functor defined overLE.
Proof.There is a natural functorb:P E{F,sˆPE{F,sÑP E{F,s which sendspV,Φ,DqˆpV 1,Φ1,D1qto the
triplepVb LE V1,ΦbΦ 1,DbD 1q, where the first two terms are clear and the gradingDbD 1 is given by
pVbV 1qpbσ{sqσ “
à
pcσ{sqσP ś
ΓE{F
1
s Z
Vpcσ{sqσbLE V1
pbσ´cσ
s qσ
.
The above construction gives a well-defined tensor functor onPE{F,s. Denote by1 PE{F,s the object given
by the vector spaceL E with the usualf E-action concentrated in thep0q σ-graded piece. ThenP E{F,s is a
rigid abelian tensor category with identity object1 PE{F,s . Moreover, the endomorphism algebra of1 PE{F,s
is identified withE. Finally, we note that the functorω PE{F,s :P E{F,sÑVectLE is anE-linear exact tensor
functor, makingPE{F,s a Tannakian category overEwhich is neutralized by the extensionL E.□
IfΓis a profinite group acting continuously on an abelian groupAand we fixcPZ 2pΓ,Aq, there is a
standard way to construct a group extension ofΓbyAwhich we use throughout this paper. Namely, one
definesEas a set byAˆΓ, with group multiplication given bypa,gq¨pb,hq“pa¨ gb¨cpg,hq,ghq. Observe
that there is a natural set-theoretic sectionΓÑEsendinggtop1,gq.
We now identify the gerbe corresponding to the categoryPE{F,s. For eachσPΓ E{F , the elementσpϖEq
determines a cocycle ofΓ Es{E representing the anti-canonical class inH 2pΓEs{E,Eˆ
sq, given explicitly by
cσpfi
E,fj
Eq“1ifi`jăs, andσpϖ Eqotherwise. We will consider a group extension corresponding to the
2-cocyclepcσqσ ofΓEs{E valued inś
ΓE{F
GmpEsq, given by
1Ñ
ź
ΓE{F
GmpEsqÑ Ăź
ΓE{F
Ecσ ÑΓ Es{EÑ1,
where by “Ăś” we mean that the product is fibered with respect to the projection of eachE cσ toΓ Es{E.
Denote this Galois gerbe byEpcσqσ.
We now make the following claim:
Claim 2.3.The categoryP E{F,s is isomorphic as Tannakian categories overEto Rep EspEpcσqσq.
Before proving the claim, we first investigate the latter Tannakian category. Letρ:E pcσqσ ÑAutpVqbe
a representation ofE pcσqσ, for a finite-dimensionalE s-vector spaceV. The Galois gerbeE pcσqσ comes, by
4
construction, equipped with a sectionΓ Es{F ÑE pcσqσ, which allows us to identify it with pairsppa σq,xq
foraσPE ˆ
s for eachσPΓ E{F andxPΓ Es{E, where the group operation is
ppaσqσ,xqppbσqσ,yq“ppa σxpbσqcσpx,yqqσ,xyq.
Our fixed representationρgives anf E-semilinear automorphismΦ :“ρpp1 σq,fEqofV, which is such
thatΦ s acts byρppσpϖ Eqq,1q; note also thatρ: ś
ΓE{F
GmpEsqÑGL V must be an algebraic homomor-
phism. Via simultaneous diagonalization, we may decomposeVinto a direct sumV“ À
ś
ΓE{F
Z
Vphσqσ,
wherepG mqτ acts onV phσqσ viax¨v“x hτvfor eachxP pG mqτpEsq. Note that each subspaceV phσq
isΦ-stable, and also thatΦ s must act onV phσq by the scalar ś
ΓE{F
σpϖEqhσ. A morphism ofE pcσq-
representations fromVtoWsendsV phσq toWphσq for all tuplesphσqand isΦ-equivariant.
We now prove the claim.
Proof.We first define a functor from Rep EspEpcσqqtoP E{F,s; for a representationpV,ρq, we send it to
pVb EsLE,Φbid LE,Dq, whereDis the grading induced by tensoring the ś
ΓE{F
1
s Z-gradingVphσ{sq :“
Vphσq withL E overEs. A morphism frompV,ρqtopW,ρ 1qwill go to the morphism given by applying the
functor´bid LE; this construction evidently defines a morphism of Tannakian categories overE. There is
also an inverse functor, given by sending the tuplepV,Φ,Dqto the representation given as a vector spaceV 1
by theE s-span of any choice ofL E-bases ofVphσ{sq (for all tuples) such thatΦ s acts by ś
ΓE{F
σpϖEqhσ.
Note that this vector space does not depend on the choice of basis: Indeed, given anyvon whichΦ s acts
byλ:“ śσpϖEqhσ and choice of basispe iqfor the corresponding graded piece, writingv“ řaiei for
aiPL E gives that ÿ
paiλqei“
ÿ
pfs
Epaiqλqei,
which means thatfs
Epaiq“a i for alli, so thata iPE s.
The mapρis defined by sendingpp1 σq,ρqtoΦandpG mqτ to the linear operator onV 1 determined by
x¨v“x hσvfor anyvin theE s-span of a basis of the graded componentV phσ{sq. This is a well-defined
representation, since for anypaσqP ś
ΓE{F
GmpEsq, we have that the mapsΦ˝pa σq˝Φ ´1 andfEpaσqf´1
E
areLE-linear and act on a vector elementvinV 1
phσ{sq as follows:
fEpaσqf´1
E v“ppf Epaσqq,1q¨v“p
ź
ΓE{F
fEpaσqhσqv,
and we also have (using theΦ-stability ofV 1
phσq) that
pΦ˝pa σq˝Φ ´1qv“Φppa σq¨pΦ ´1pvqqq“Φp
ź
ahσ
σ Φ´1pvqq“p
ź
fEpaσqhσqv,
as desired. These define mutually-inverse functors, giving the desired equivalence.□
Corollary 2.4.The gerbe over SpecpEq fpqc corresponding to the Tannakian categoryPE{F,s is isomorphic
to the product of the gerbes (as fibered categories over SpecpEqfpqc)ś
σPΓE{F
Ecσ. In particular, it is banded
by theE-group scheme ś
ΓE{F
Gm and corresponds to the anti-canonical class inH 2pΓLE{E,ś
ΓE{F
Lˆ
Eq
corresponding to the elementp´1{sqσP ś
ΓE{F
Q{Z.
What the above construction does is give an isomorphism of ś
ΓE{F
Gm-gerbes fromE PE{F,s toEpcσqσ;
note that sinceH 1pΓLE{E,ś
ΓE{F
Lˆ
Eqvanishes, this isomorphism is unique up to conjugation by an ele-
ment ofś
ΓE{F
Lˆ
E, which we will see later does not affect cohomology.
5
