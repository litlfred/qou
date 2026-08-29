---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-012-32-comparison-with-isocrystals
section_title: "Comparison with isocrystals"
section_number: 3.2
pages: 18-20
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
IsocF toRigIsoc F . The categoryIsoc F,s of isocrystals whose slopes are a multiple of 1
s is equivalent to
the categoryI F{F,s . Indeed, we can define the equivalence by mapping the isocrystalpV,Φqto the space
pV, ˜Φ,Dqwhere the gradingDis defined such thatV aσ{s is the´a σ{sslope isotypic piece ofVand the
WL{F -action is given byΦ.
Then for any isocrystalpV,Φq, we choose some sufficiently largekPNsuch thatpV,ΦqPIsoc F,nk and
pV, ˜Φ,Dqis the corresponding object ofI F{F,nk. We then apply the quotient functor to obtain an object
RIF{F,nk and finally the transition mapRI F{F,nkÑRI Ek{F,nk.
If we restrict ourselves to isocrystals with slopes of denominator dividingn k for some fixedk, then we
see that, on bands, the above functor is the composition
(3) Res Ek{Fpµnkq
´NEk{F
ÝÝÝÝÝÑµnk ãÑGm,
which, after taking inverse limits, implies that the above morphism of Tannakian categories overFcorre-
sponds to the composition
uÑµÑD,
where the first map is given by the inverse limit of the negative norm maps.
Recall that [Kal18, §3.3] constructs a homomorphismE 1
Kal ÑE iso for any choice of gerbeE 1
Kal repre-
senting the canonical class´1PH 2pF,uqwhich is compatible with the projections toΓ F{F and agrees
with the map (3) on bands. Since the choice ofE 1
Kal is only canonical up to conjugation byu, any such map
is only unique up to post-composing by the automorphisms ofE iso induced byIntpxqforxPDp Fq. In fact,
all maps satisfying these two properties differ in this manner, sinceH 1pF,Dqis trivial. In particular, the
morphism of gerbesE KalÑE iso induced by our functorIsoc F ÑRigIsoc F is such a morphism.
3.3.Comparison with Fargues’ extended isocrystals.We first briefly recall the Tannakian category Isoce
F
constructed by Fargues in [Far22, §6] corresponding to the gerbeE KalˆE iso:
First, one picks a splitting of the short exact sequence
0ÑlimÝ Ñ
ź
ΓK{F
ZÑlimÝ Ñ
ź
ΓK{F
QÑlimÝ Ñ
ź
ΓK{F
,Q{ZÑ0,
where the direct limits are over all finite Galois extensionsK{F, with corresponding2-cocyclec. We will
take the splitting to be the unique one valued inr0,1q, such thatctakes values inlimÝ Ñ
ś
ΓK{F
t0,1u.
18
As in [Far22, §6.2], one constructs, for a fixed finite GaloisE{F, a canonical rank one, slope oneE-
isocrystalLE. We will not need the precise definition of this isocrystal (it is built using the Fargues–Fontaine
curve)—the only property needed for the construction ofIsoce
F is that for eachK{Ea finite Galois extension
one has thatN K{EpLKq:“ Â
τPΓK{E
LKbLK,˜τLK, where˜τis some lift ofτtoΓ LK{E, equalsL E. Our
norm-compatible system of (anti-)uniformizers evidently furnishes us with such a system by settingL E to
the vector spaceLE with the Frobenius ofEacting on1byϖ ´1
E .
For a fixed functionΓE{F
αÝ ÑZ, we define theE-isocrystal
Lα
8 :“
â
τPΓE{F
Lbαpτq
E bLE,˜τLE,
where˜τis some lift ofτtoΓ LE{F . By construction, this is a finite dimensional discrete, semilinearW E-
module overL.
The Tannakian category Isoce has objects given bylimÝ Ñ
ś
ΓK{F
,Q{Z-graded finite-dimensional L-vector
spaces
D“
à
αPlimÝ Ñ
ś
ΓK{F
,Q{Z
Dα
equipped with a discrete, semilinearW F -action such that acting byτPW F is an isomorphism fromD α to
Dτα, with tensor product given by
pDbD 1qα“
à
β`γ“α
DβbF D1
γbL Lcpβ,γq
8 ,
whereWF acts onLcpβ,γq
8 by mapping it topLcpβ,γq
8 qτ »L
τcpβ,γq
8 via the mapLα
8ÑL α
8bLE,σL,xÞÑxb1.
We will denote all of the above data byD“pV D,ΦD,DD,q(the underlying vector space, theW F -action,
and the grading, respectively). The morphisms in Isoce are morphisms of gradedWF -modules.
The goal is to define a morphism of Tannakian categories
RigIsocF ÑIsoc e
F
corresponding (possibly up to twisting by a coboundary) to the projection mapE KalˆE isoÑE Kal.
At the level of objects, this functor is the exact functor given by sendingpV,˜Φ,DqtopV r0,1q, ˜Φ, Dq, where
Vr0,1q denotes the direct sum of the graded pieces ofVall of whose entries lie inlimÝ Ñ
ś
ΓK{F
r0,1q, which is
preserved by theWF -action ˜Φ, and Dis thelimÝ Ñ
ś
ΓK{F
,Q{Zgrading induced by thelimÝ Ñ
ś
ΓK{F
Q-grading.
On morphisms the functor sendsfto f(this makes sense becausefisR F{F -equivariant).
It remains to justify that this functor preserves the tensor structure. To check tensor compatibility we
first compute that (for fixedE{Ffinite Galois) andpa σqσ,pb σqσ in ś
ΓE{F
r0,1q, denoting by ˜bthe tensor
product in Isoce:
Vpaσq ˜bWpbσq“pVpaσqbWpbσqqbL cppaσq,pbσqq
8 ĎpVbWq paσ`bσq
whereL cppaσq,pbσqq
8 is the tensor product of eachL EbLE,˜σLE such thata σ`bσ ě1. On the other hand,
first note that for any graded componentUpcσq that
UpcτqbpLEbLE,˜σLEq“1 δσp´1q¨Upcτq,
whereδ σp´1qdenotes the element of ś
ΓE{F
Zwith´1in theσ-coordinate and zeros elsewhere such that
1δσp´1q PR E{F . Using the above two computations, we find (using that the tensor productVbWin
RigIsocF is a tensor product ofRE{F -modules) that
pr1p´cppaσq,pbσqqqσ
¨VpaσqsbW pbσqq“pV paσqbr1p´cppaσq,pbσqqqσ
¨WpbσqsqĎpVbWq r0,1q
and equalsVpaσq ˜bWpbσq. From here, the desired tensor compatibility follows easily.
19
We conclude this subsection by studying the map on gerbesE KalˆE iso ÑE Kal corresponding to this
morphism of Tannakian categoriesRigIsocF ÑIsoc e
F .
A fiber functor ofIsoc e
F is given, at a fixed finiteK{F-level, by the following composition 2
Isoce
F,K ÑVectF ÑR K{F -modÑVect F,
whereIsoce
F,K denotes the full subcategory ofIsoce
F where the grading factors throughś
ΓK{F
Q{Z, the first
functor forgets thelimÝ Ñ
ś
ΓK{F
Q{Z-grading andW F -action, the second functor sendsYtoYb LK RK{F ,
and the third functor is the fiber functor on finitely-generatedR K{F -modules from §2.3. We deduce that
the automorphism group this fiber functor, identified withu FˆDF , acts on the image of the ś
ΓK{F
Q{Z-
graded pieceV pcσ{sqσ of an objectXofIsoc e
F according to the ś
ΓK{F
Q{Z-grading via theu F -factor,
showing that, at the level of bands, the morphism of gerbesE KalˆE iso ÑE Kal is the projection map.
This lets us deduce that this morphism of gerbes agrees with the projection mapE KalˆE isoÑE Kal up to
possibly composing withIntpaqforaPup FqˆDp Fq—we suspect that this in fact equals the projection
map, but have not verified this. Note that the equality up toIntpaqalready implies that the pullback map
H1
étpEKal,GqÑH 1
étpEKalˆE iso,Gqagrees with pullback by the projection map.
