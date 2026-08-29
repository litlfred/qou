---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-008-24-descent
section_title: "Descent"
section_number: 2.4
pages: 9-12
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
first step is to define a canonicalΓLE{F -action on the ringRE{F .
Note thatLE{Lis a totally ramified extension and that the sequence:
1ÑΓ LE{LÑW LE{F ÑW L{F Ñ1,
is split by any lift of the Frobenius element inW L{F . Fix such a splitting and hence a lift which we denote
fF . Restriction gives an injectionΓ LE{L ãÑΓE{F . We denote the image of this injection byΩE.
We now define aΓ LE{F -semilinear action ofW LE{F onR E{F which we denote rΦRE{F . We define the
action ofΓ LE{L such thatγpℓ pbσqσq“γpℓq pbγ´1σqσ, whereγis the projection ofγtoΓ E{F . We define the
action offF such that
fFpℓpbσqσq“pf Fpℓq
ź
σ1PΩE
σ1pϖEq
bfF
´1σ1
qpbfF
´1σqσ.
In particular, this implies that
f´1
F pℓpbσqσq“pf ´1
F pℓq
ź
σ1PΩE
f´1
F σ1pϖEq´bσ1qpbfFσqσ,
which can be verified easily by checking thatf´1
F ˝fF “id.
We need to check that this indeed induces an action ofW LE{F . To do so, we need to check that for
γPΓ LE{L, the action off F ˝γ˝f ´1
F PΓ LE{L agrees with the action induced by the composition. Since
both actions are semilinear in the correct way, we need only understand the action on1pbσqσ. We have
pfF˝γ˝f ´1
F qp1pbσqσq“pf F˝γqp
ź
σ1PΩE
f´1
F σ1pϖEq´bσ1qpbfFσqσq
“f Fp
ź
σ1PΩE
γf´1
F σ1pϖEq´bσ1qpbfFγ´1σqσq
“p
ź
σ1PΩE
fFγf´1
F σ1pϖEq´bσ1
ź
σ2PΩE
σ2pϖEq
b
fFγ´1f´1
F σ2
qqpb
fFγ´1f´1
F σ
qσ
“1pb
fFγ´1f´1
F σ
qσ,
as desired.
9
The action does not depend on the choice off F . Indeed, any other lift is of the formγf F forγPΓ LE{L
and we have
γfFpℓpbσqσq“γf Fpℓq
ź
σ1PΩE
γσ1pϖEq
b
f´1
F σ1
pb
f´1
F γ´1σ
qσ
“γf Fpℓq
ź
σ1PΩE
σ1pϖEq
b
f´1
F γ´1σ1
pb
f´1
F γ´1σ
qσ
,
which is the same actionγf F would have if we had chosen it as our lift of Frobenius.
Finally, we need to compute the action of the canonical generatorfE ofWLE{EĂW LE{F . We can write
fE“γf fpE{Fq
F for someγPΓ LE{L. Then
γffpE{Fq
F p1pbσqσq“γ
¨
˝
fpE{Fqź
k“1
ź
σ1PΩE
ffpE{Fq´k
F σ1pϖEq
b
f´k
F σ
pb
f´fpE{Fq
F σ
qσ
˛
‚
“γ
¨
˝
fpE{Fqź
k“1
ź
σ1Pf´k
F pΩEq
ffpE{Fq
F σ1pϖEqbσ1
pb
f´fpE{Fq
F σ1
qσ
˛
‚
“γ
¨
˝ ź
σ1PΓE{F
ffpE{Fq
F σ1pϖEqbσ1
pb
f´fpE{Fq
F σ
qσ
˛
‚“
ź
σ1PΓE{F
σ1pϖEqbσ1
pbσqσ
.
With this action in hand, we are ready to define a descent datum for our categoryRP E{F,s. Fix a sec-
tions E : ΓE{F ÑW LE{F , which determines a 2-cocycle ofΓ E{F valued inZ, denoted byc E. For a
fixedγPΓ E{F , we define the functorβ γ :RP E{F,s ÑRP E{F,s to send the triplepV,Φ,Dqto the triple
pβγpVq,β γpΦq,βγpDqqsuch that
‚the underlying vector spaceβ γpVqis defined to beVb RE{F RE{F where the mapR E{F ÑR E{F
is given by the action ofsEpγq,
‚the endomorphismβ γpΦqis defined byΦbps Epγq˝Φ Rq,
‚the gradingβ γpDqonβ γpVqis such thatv paγσ{sqσqbrpbσqσ is in theppaσ`sbσq{sqσ graded piece.
A morphismf:pV,Φ,DqÑpV 1,Φ1,D1qis mapped byβ γ toβ γpfq:“fbid. This construction gives
aγ-semilinear tensor equivalence fromRP E{F,s to itself. For instance, forePE, we observe that
βγpeqpvbrq“evbr“vbγpeqr“γpeqpvbrq.
To finish giving our descent datum, we need to provide an isomorphism of functorsµγ1,γ :β γ1γÑβ γ1˝βγ
for all pairspγ 1,γqwhich satisfies a cocycle condition (explained in more detail later). The morphism
µγ1,γpXqwill be defined for any objectpV,Φ,Dq“XPRP E{F,s by the map
µγ1,γpXq:vbrÞÑΦ ´cEpγ1,γqpvqbs Epγ1γ1qprq.
We check that this is a well-defined morphism inRP E{F,s. First we note that forvPVandrPR E{F ,
we haveµγ1,γpXqpvbrq“µ γ1,γprvb1q. Indeed,
µγ1,γpXqpvbrq“Φ ´cEpγ1,γqpvqbs Epγ1γqprq“Φ ´cEpγ1,γqpvqbs Epγ1qsEpγqΦ´cEpγ1,γqprq
“Φ´cEpγ1,γqprvqb1“µ γ1γpXqprvb1q.
Now, evidentlyµγ1,γpXqisΦ-equivariant and preserves gradings, so it remains to showR E{F -linearity.
For anyvPVandrPR E{F , we compute that
µγ1,γpXqpvbrq“Φ ´cEpγ1,γqpvqbs Epγ1,γqprq“r¨µ γ1γpvb1q.
10
We claim that the family of isomorphisms of functorsµ γ1,γ satisfies the “cocycle condition.” Explicitly,
forγ 2,γ1,γPΓ E{F , we need to check that the following diagram commutes:
βγ2γ1γpVq βγ2pβγ1γpVqq
βγ2γ1pβγpVqq βγ2pβγ1pβγpVqqq.
pµγ2,γ1γqV
pµγ2γ1,γqV βγ2ppµγ1,γqVq
pµγ2,γ1qβγpVq
We can write any element in the above spaces in the formvb1. Then we note that on elements of this
form, the top arrow is given byΦ´cEpγ2,γ1γq, the right arrow byΦ´cEpγ1,γq, the left byΦ´cEpγ2γ1,γq, and the
bottom byΦ´cEpγ2,γ1q. The desired commutativity then follows from the fact thatcE is a2-cocycle (keeping
in mind that the action ofΓE{F onZ“W LE{E is trivial).
With this setup in hand, we get a Tannakian category overF, denoted byRWE{F,s. Explicitly, the objects
ofRW E{F,s are tuplespX,f γ :XÑβ γpXqqwhereXis an object ofRP E{F,s andf γ is a morphism such
that
µγ1,γpXq˝f γ1γ“β γ1pfγq˝f γ1.
Morphisms inRW E{F,s are morphisms inRP E{F,s that commute with thef γ maps. The band ofRW E{F,s
is anF-group scheme whose base-change toEis ś
ΓE{F
µs. In fact, we have the following claim.
Claim 2.9.The band of the gerbe associated toRW E{F,s isResE{Fpµsq.
To make the verification of this claim easier, we note that we can define an analogous descent datum
on the categoryP E{F,s defined in the identical way, except forgetting about anyR E{F -module structure
(so for instance,β γpVq “Vb LE LE where the mapL E ÑL E is the Galois action bys Epγq). This
gives a Tannakian categoryW E{F,s overF. Moreover, the quotient functorqextends to a morphism˜qof
Tannakian categories with descent data; that is, for an objectpX,f γqinW E{F,s, the objectpqpXq,˜qpfγqq
lies inRW E{F,s. The map˜qpfγq:VbR E{F ÑVbR E{F bRE{F RE{F “β γpVbR E{Fqis defined by
vbrÞÑf γpvqbs Epγq´1prqb1. This map isR E{F -linear since forrPR E{F andvPV, we have
vbrÞÑf γpvqbs Epγq´1prqb1“f γpvqb1br“r¨qpf γqpvb1q.
This extension ofqis again a quotient functor, and the same argument as in §2.3 shows that the band of
RWE{F,s is given by thes-torsion subgroup-scheme of theF-group scheme giving the band ofW E{F,s. It
thus suffices to show that the latter band is theF-group scheme Res E{FpGmq.
Since we have identified the band ofP E{F,s with theF-group scheme ś
ΓE{F
Gm via the isomorphism
of Tannakian categories overEwith the category Rep EspEpcσqσqconstructed in §2.1, we will work with
this latter category. Conjugating the functorsβγ with this (E-linear) identification gives a descent datum on
RepEspEpcσqσq. ForγPΓ E{F , this is given by taking the representationpV,ρqto the representationpV 1,ρ1q
whereV 1 “Vb Es Es such that the mapE s ÑE s is given by the action ofs Epγqrestricted toE s and
V1
phσqσ “Vphγσqσ. We defineρ1 such that the elementpp1q,f Eqacts byΦbf E where the action on the right
is the Galois action, and an elementpa σqσ of the torus acts onV phσq by the scalar ś
σPΓE{F
a
hγ´1σ
σ . With
the descent functorsβ1
γ on RepEspEpcσqσqin hand, we are ready to compute theΓ E{F -action giving the band
the structure of anF-group scheme.
We know that the automorphisms of the canonical fiber functorωare parametrized by ś
ΓE{F
GmpEsq,
where the tuplepc τqacts onVvia scalingV phσq by ś
τPΓE{F
chτ
τ . Starting with such an automorphism
φand objectpV,ρq, we first applyβ γ´1, obtainingpV 1,ρ1q, and obtain an automorphism ofV 1 denoted
φpβγ´1pV1,ρ1qq. We then twist theLE-action byspγq´1, obtaining an automorphismspγq´1rφpβγ´1pV1,ρ1qqs
11
of the vector spacepV spγ´1q´1
qspγq´1
, and then applyωpµ γ,γ´1qto get an automorphism ofV“ωppV,ρqq,
which we want to explicitly describe. The automorphismφpβγ´1pV1,ρ1qqscalesV phσq“V 1
phγσq byś
τchγτ
τ
(using the twistedL E-action), which means thatspγq ´1pφpβγ´1pV1,ρ1qqqscalesV phσq byspγq¨p ś
τchγτ
τ q
(using the usualL E-action), so that the new automorphism of our fiber functor is given by the tuple
pspγqΦcEpγ,γ´1qcγ´1τqτ . It follows that whenpc τqτ P ś
ΓE{F
GmpEq, this action agrees with the usual
ΓE{F -action on ResE{FpGmqpEq. This implies that theF-group scheme structure of our band is given by
ResE{FpGmq, as desired.
Finally, note that this identification of the bands ofWE{F,s andRW E{F,s with theseF-group schemes is
compatible with our transition maps, in the sense that, at the level of bands, the functorιs,s1 induces thes1{s-
power map from ResE{FpGmqto itself (and thus, thes 1{s-power map from ResE{Fpµs1qto Res E{Fpµsq).
This fact follows from base-changing toE, where the analogous statement holds for the categoryP E{F,s
(and thus forRP E{F,s), as discussed in §2.1). IfpX,f γqis an object ofW E{F,s, thenpιpXq,ιpf γqqis an
object ofWE{F,s1, similarly forRWE{F,s, and we defineWE{F andRWE{F to be their direct limits, whose
bands have an explicit description via the above observation.
