---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-010-26-transition-maps
section_title: "Transition maps"
section_number: 2.6
pages: 14-17
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
cation ofW E{F andRW E{F with the direct limit of the systems categories, denoted byI E{F andRI E{F ,
respectively. However, when constructing our final Tannakian category, we will use slightly more interesting
transition maps than these (in particular, we will also change the extensionE{F).
2.6.Transition maps.Consider a tower of finite Galois extensionsK{E{F. Fix an anti-uniformizerϖ E
ofE. LetK 1 ĂKbe the maximal unramified extension ofE. ThenK{K 1 is totally ramified and we
have our fixed anti-uniformizerϖ K such thatN K{K1pϖKq “ϖE. We define a transition functorp K{E :
RIE{F,s ÑRI K{F,s defined according to our choices of uniformizers. We pick a lift of the Frobenius of
Fin the absolute Weil groupW F{F , whose restriction we use in our definitions of the actions ofW LK{F
andW LE{F onR K{F andR E{F , respectively. To begin, we consider the ś
τPΓK{F
Z-graded ringR 1
E{F,K
whosepc τqτ -graded piece is0if the grading is not fixed under theΓ K{E -action and is thepc τqσ-graded
piece ofR E{F otherwise. We then defineR E{F,K :“R 1
E{F,K bLE LK. We giveR E{F,K the diagonal
WLK{F -action wherebyWLK{F acts on the first factor by projection toWLE{F and on the second factor by
the natural Galois action. Note that we have an inclusion of graded rings
RE{F,K ãÑRK{F.
Moreover, we claim this inclusion respects theWLK{F -actions. We need only check that the actions offF,K
(our chosen lift of Frobenius) agree on1pcτqτ since the actions ofΓLK{L both act by the natural Galois action
and shift the gradings in the same way. We have
fF,Kp1pcτqτq“
ź
τ1PΩK
τ1pϖKq
cf´1
F,Kτ1
pcf´1
F,Kτqτ
“
ź
σ1PΓK1{pKXLq
ź
τ2PΓK{K1
σ1τ2pϖKq
cf´1
K,Fτ1
pcf´1
K,Fτqτ
“
ź
σ1PΓK1{pKXLq
σ1pϖEq
cf´1
F,Eσ1
pcf´1
F,Eσqσ
“
ź
σ1PΓE{pEXLq
σ1pϖEq
cf´1
F,Eσ1
pcf´1
F,Eσqσ
“rf F,E1pcσqσsb1“f F,Kp1pcσqσb1q,
To obtain the fourth equality, we have used the fact that the restriction-to-Emap induces a surjection
ΓK1{pKXLq ↠Γ E{pEXLq , with kernel equal toΓK1{rE¨pKXLqs , where nowE¨pKXLq“K 1, since the max-
imal unramified subextension ofK{Eis the compositum ofEand the maximal unramified subextension of
K{F, by elementary algebraic number theory. The last equality follows from the fact that, by construction,
the image offF,K inWLE{F isfF,E.
We are now ready to define the functorp K{E . For an objectMofRI E{F,s, we defineM K to be theś
τPΓK{F
1
s Z-gradedRE{F,K -module whosepcτqτ -graded piece is0if the grading is not fixed under theΓ K{E -
action and is thepc τqτ graded piece ofMb LE LK otherwise. We then definep K{EpMq:“M KbRE{F,K
RK{F (with the induced grading) and define theWLK{F -action diagonally, noting this is well-defined by the
WLK{F -equivariance ofRE{F,K ãÑRK{F .
Note also that there is a similar transition functorp 1
K{E :I K{F,s ÑI E{F,s, defined simply by sending
theW LE{F -moduleMto theW LK{F -moduleMb LE LK with diagonalW LK{F -action induced on the
first factor by projection toW LE{F and grading given the same way as with the functorp K{E . Note that,
trivially, the transition functorsp 1
K{E andp K{E are compatible with the quotient mapsI ?{F,s ÑRI ?{F,s,
where?“EorK. By abuse of notation, we will also usep 1
K{E to denote the functor fromPK{F,s toPE{F,s
given in the same way asp 1
K{E , except now with diagonalΓ LK{K-action onMbL K induced on the first
factor via projecting intoΓLE{E.
14
As usual, to describe whatp K{E does on bands, we will first describe whatp1
K{E does, which in turn we
will do via our identifications ofPE{F,s andPK{F,s with the categoriesEpcσqσ andEpdσqσ, respectively. Here,
as in §2.1, the tuplespc σqσ andpd σqσ are the representatives of the anti-canonical class inH 2pΓEs{E,Eˆ
sq
andH 2pΓKs{K,Kˆ
sq, respectively corresponding toϖE andϖK. Conjugatingp1
K{E by these equivalences
gives a functor from RepEspEpcσqσqto RepKspEpdσqσq, which we will explicitly compute.
Recall that, given anL E-representationpV,ρqof the groupE pcσqσ, determined by the homomorphism
hρ : ś
ΓE{F
GmpLEq ÑGLpVqand thef E-semilinear automorphism induced bypp1q,f Eq, we obtain an
objectpV 1,Φ,DqofP E{F,s as in §2.1, withV 1“Vb EsLE,Φgiven by the actionpp1q,f Eq, andV 1
phσ{sq“
VphσqbEs LE. Then, by definition,p 1
K{E sends this to the objectpV 1bLE LK,Φ1,D1q, whereΦ 1 acts
diagonally onV 1bLE LK byΦ fpK{Eq bf K andV 2
phτ{sq “0ifph τ{sqis notΓ K{E -fixed, and equals
V1
ph¯τ{sqbLE LK otherwise. To compute the image of this object under the equivalence, we note that the
subspace
V2
phτ{sq“V 1
ph¯τ{sqbLE LK“Vph¯τqbEsLK“pVph¯τqbEsKsqbKsLK
has anLK-basis given byteib1b1u, whereei is anEs-basis ofVph¯τq on whichΦs acts byś
σPΓE{F
σpϖEqhσ.
Thus,
pΦ1qspeib1b1q“r
ź
σPΓE{F
σpϖEqfpK{Eqhσspeib1b1q,
which, by construction, equals
r
ź
σPΓE{F
σp
ź
γPΓK{K1
γpϖKqqfpK{Eqhσspeib1b1q.
Finally, the above expression may be rewritten as
r
ź
τPΓK{F
τpϖKqh¯τspeib1b1q,
showing that the corresponding representation ofE pdσq, denoted bypW,ρ 1q, hasW phτq “0ifph τqis not
ΓK{E -stable, and isVph¯τqbEsKs otherwise. Thus, if the automorphism of the fiber functorωK acts onWph1τq
via scaling byś
τPΓK{F
ah1
τ
τ , (wherepaτqP ś
ΓK{F
GmpKsq), then the above calculation shows that we get
an induced automorphism ofpωEqK, which acts onVphσqbEsKs byś
σPΓE{F
pś
τPΓK{F,τÞÑσaτqhσ, which
shows that the induced map, onKs-points, is given by the “norm" mapś
ΓK{F
GmpKsqÑ ś
ΓE{F
GmpKsq.
By construction, theF-group morphism on bands from Res K{FpGmqto Res E{FpGmqinduced byp 1
K{E
is given onK s-points via the map described explicitly at the bottom of the previous paragraph; the same is
true of the canonical “norm map" Res K{FpGmq ÑResE{FpGmq. Since both schemes are tori andK s is
infinite, by unirationality this implies that the two maps coincide. The following diagram of transition maps
commutes
IE{F,s IK{F,s
RIE{F,s RIK{F,s,
where the vertical arrows are the quotient maps discussed above, which means that the morphism ofF-
group schemes ResK{FpµsqÑRes E{Fpµsqassociated top K{E is induced by the inclusion ResK{FpµsqãÑ
ResK{FpGmqfollowed by the map induced byp 1
K{E , which implies that it is also given by the norm map.
Finally, fors|s 1, we define the transition mappK{E,s1,s :I E{F,sÑI K{F,s1 to be the composition
IE{F,s
pK{E
ÝÝÝÑIK{F,s
ιs,s1
ÝÝÑIK{F,s1,
15
which on bands gives the map ResK{Fpµs1qÑRes E{FpµsqofF-group schemes given byN K{F composed
with thes1{s-power map.
2.7.The categoryRigIsoc F .We are now ready to define the Tannakian category overFwhich parametrizes
rigid inner forms. We define the categoryRigIsocF to be the direct limit of the categoriesRIE{F,s over the
inductive system of tuplespE,sq, whereE{Fis a finite Galois extension andsPN, which is ordered by
the relation thatpK,s 1q ą pE,sqif and only ifKcontainsEands|s 1, with respect to the transition
mapsp K{E,s,s1 defined in the previous subsection. It will frequently be convenient to fix a cofinal system
of objects in the indexing category indexed byN, denoted bypE k,nkq. Note thatlimÝ ÑkRIk “RigIsoc F ,
whereRI k :“RI Ek{F,nk.
By construction,RigIsocF is a Tannakian category overF, with fiber functor overL, and the correspond-
ing gerbe is banded by theF-group schemeu“limÐ Ýk ResEk{Fpµnkq. Note that each categoryRIE{F,s has a
fiber functor over the finite extensionEs{F, given explicitly by sendingpV,D,Φqto the (finite-dimensional)
Es-vector space
(1)
à
0ďpaσ{sqă1
pr
à
pbσqPś
ΓE{F
Z
V fs
E¨pśσpϖEq´raσ`sbσsqsbRE{F RE{F{Iq,
whereV fs
E¨pśσpϖEq´raσ`sbσsq denotes the subgroup ofVof all elements on whichf s
E acts by the scalarś
σPΓE{F
σpϖEq´raσ`sbσs. Note that the above expression is well-defined, since the internal direct sum
isR E{F -stable. We may extend this to a fiber functor over Fby simply post-composing the above fiber
functor overE s with´b Es F. By considering the automorphisms of this fiber functor over F, we get
a canonical cohomology class in the groupH 2pΓF{F,ResE{FpµsqpFqq, which we now compute. Since
RIE{F,s is a quotient ofI E{F,s, the above cohomology class maps to the class corresponding to the group
of automorphisms of the fiber functorIE{F,sÑVectF given explicitly by tensoring theEs-fiber functor
pV,D, ˜ΦqÞÑ
à
paσ{sqPś
ΓE{F
1
s Z
V fs
E¨pśσpϖEq´aσq
with FoverE s, under the canonical mapH 2pΓF{F,ResE{FpµsqpFqq ÑH 2pΓF{F,ResE{FpGmqpFqq,
noting that the above fiber functors are compatible with the quotient functor fromI E{F,s toRI E{F,s, and
using [Mil07, §2.10].
Because of the above observation, it will be useful to first describe the corresponding cohomology class
inH 2pΓF{F,ResE{FpGmqpFqqcorresponding toI E{F,s. Since the Tannakian categoryI E{F,s overF
has base-change toEwhich is isomorphic as Tannakian categories overEtoP E{F,s, it follows that the
image of this class inH 2pE,ResE{FpGmqpFqqis theΓ E{F -fold product of the classes´1{sPQ{Zinś
ΓE{F
H2pE,GmpFqq. In particular, the image of this class under the Shapiro isomorphism
H2pΓF{F,ResE{FpGmqpFqq „Ý ÑH2pΓF{E,GmpFqq
is the class mapping to´1{sPQ{Zunder the local invariant map.
Recall thatH 2pΓF{F,upFqq“limÐ ÝkH2pΓF{F,ukpFqq, whereu k :“Res Ek{Fpµnkq. Using Hilbert 90
and Shapiro’s Lemma, we see that the latter groups fit into the exact sequence
0ÑH 2pΓF{F,ukpFqqÑH 2pΓF{F,ResEk{FpGmqpFqq
xÞÑnkx
ÝÝÝÝÑH2pΓF{F,ResEk{FpGmqpFqq,
and so we get, via Shapiro’s Lemma and the local invariant map, a canonical identification of the cohomol-
ogy groupH 2pΓF{F,ukpFqqwith´ 1
nk
Z{Z. Moreover, it follows from our above discussion that the gerbe
corresponding to the Tannakian categoryRI k has cohomology class equal to the element´ 1
nk
. Forląk,
the projection mapH 2pΓF{F,ulpFqq ÑH 2pΓF{F,ukpFqqcorresponds (via the F-fiber functor given by
16
direct limit of theF-fiber functors for eachRI k, which are evidently compatible) to the multiplication-by-
nl{nk map from 1
nl
Z{Zto 1
nk
Z{Z. We thus conclude that the categoryRigIsoc F corresponds to the class
´1P pZ“limÐ Ýk
1
nk
Z{Z“H 2pΓF{F,upFqq, which is exactly what we want. All in all, we have proved:
Theorem 2.11.The Galois gerbe given associated to the gerbe of fiber functors ofRigIsoc F represents the
class´1P pZ–H 2pΓF{F,upFqq. In particular, we may identifyRigIsoc F withReppE Kalq.
Remark 2.12.As noted in the introduction, we use an alternative presentation of the group schemeuto
the presentationu 1 (a priori a different group) used in [Kal16a]. Nevertheless, the mapuÑu 1 is an
isomorphism. It suffices to show this at the level of character modules, where the map is the inclusion
limÝ Ñ
E{F
pQ{ZqrΓE{Fs0ÑlimÝ Ñ
E{F
pQ{ZqrΓE{Fs,
where the direct limit is over all finite Galois extensions. Surjectivity comes from the fact that for a fixed
xPQ{ZrΓ E{Fswhich ism-torsion, if we takeK{E{Ffinite Galois withm|rK:Esthen the image ofx
inQ{ZrΓK{Fslies inQ{ZrΓ K{Fs0. We warn that this result is false whenF“R.
3. THE STRUCTURE OFRigIsoc F
In this section we study the structure ofRigIsoc F as an abelian tensor category and construct examples
of its objects.
