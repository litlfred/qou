---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL₂(ℂ) Chern–Simons invariant"
section_id: sec-001-background-and-motivation
section_title: "Background and motivation"
section_number: null
pages: 2-3
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
doc_brief: "State integrals for the quantized SL₂(ℂ) Chern–Simons invariant — Previous work of the author and N."
---
Kashaev’s Volume Conjecture[Kas97] proposes a striking connection between the geometry of
hyperbolicknotsandtheirquantuminvariants. Thisconjectureappearstoberelatedtoquantum
SL2(C)Chern-Simonstheory,aTQFTarisingasacomplexiﬁcation[Guk05]oranalyticcontinu-
ation[Wit10]ofthemorefamiliarquantum SU(2)Chern-Simonstheory[Wit89]. Anumberof
authors[BB04;BWY21;KR05;McP25a]haveconstructedgeometricquantuminvariantsthatcan
beinterpretedascandidatesforamathematicalrealizationof SL2(C)Chern-Simonstheory.
Wediscusssometypicalfeaturesofacandidatemathematicalrealization. 1 Forconcreteness
letK beahyperbolicknotin S3,althoughsomeversionsareadditionallyorinsteaddeﬁnedfor
closed 3-manifoldsorrelatedobjects. Arealizationisafamilyoffunctions
ZN : X(K)→ C
forN apositiveintegerrelatedtotheleveland X(K)aspaceparametrizinghyperbolicstructures
onS3\K;itisusuallyaversionofthe SL2(C)charactervarietyof S3\K. LetςK∈ C/2πiZbe
the SL2(C)Chern-Simonsinvariantofthecanonicalstructure ρhypofK,normalizedso 2π ReςK
isthehyperbolicvolumeof K. Avolumeconjectureisthestatementthat(uptonormalizationand
someotherdetails)
(1.1) lim
N→∞
logZN(K,ρ )
N =ςK
forsome ρ∈ X(K)thatisnotnecessarily ρhyp. Wethinkof N→∞ asthesemiclassicallimit.
Thesurprisingobservationisthatthisholdsfor ρotherthan ρhyp;Kashaev’soriginalconjecture
[Kas97] is that it happens for the trivial hyperbolic structure1. In this caseZN(K, 1) can be
identiﬁed with a value of theNth colored Jones polynomial ofK [MM01]. There is a standard
ansatz(successfulinsomespecialcases)forprovingtheseconjecturesthatusestwosteps.
Step1(Establishintegrals) .Showthattheinvariantisequivalent(perhapsasymptotically)toa state
integral,acontourintegral
ZN(K,ρ )∼
Z
Γ
eNS(t) dt
whereS is a holomorphic function that can be identiﬁed with the Chern-Simons functional.
Sometimesinsteadonemustconsiderasumofsuchintegrals. ⌟
Inmoredetail,givenacombinatorialdescription T ofS3\K thedomainof S isaspace ΩT
parametrizinghyperbolicstructuresontheindividualpiecesof T . CriticalpointsofS arechoices
thatcombinetogethertogiveacoherentstructureonallof S3\K andthecriticalvalueisthe
SL2(C)Chern-Simonsinvariant. Forexample,if T isanidealtriangulationthen ΩT parametrizes
shapesofthetetrahedraandcriticalpointsof S aresolutionsofThurston’sgluingequations.
Step2(Movethecontour) .Showthat
Z
Γ
eNS(t) dt∼
Z
Γ′
eNS(t) dt
where Γ′ isacontourinsaddlepointpositionforacriticalpointcorrespondingto ρhyp. ⌟
Themaximumcriticalvalueof ReS is ReςK. Itoccursatasaddlepointof ReS becauseS
isaholomorphicfunction. If Γ′ isacontourpassingthroughthissaddlepointintherightwaya
standardsaddle-point approximationbyaGaussianintegralgivesthedesiredasymptotics(1.1).
1. Introduction 2
[Oht16]T.Ohtsuki,“Ontheasymptoticexpan-
sionoftheKashaevinvariantofthe 52 knot”.
doi
[McP25a]C.McPhail-Snyder, A quantization of
the SL2(C) Chern-Simons invariant of tangle
exteriors. arXiv
[MR25]C.McPhail-SnyderandN.Reshetikhin,
CyclicUξ(sl2)-modules and invariants of knots
withﬂat sl2connectionsinthecomplement . arXiv
2 In[McP25a]wewrote Zψ
N asdependingona
log-decoration s,whichalsoincludesachoiceof
log-longitudeλ. Thenormalization Zψ
N used
hereisindependentof λsowedropitfromthe
notation.
[Kas95]R.M.Kashaev,“Alinkinvariantfrom
quantumdilogarithm”. arXiv doi
[ADO92]Y.Akutsu,T.Deguchi,andT.Ohtsuki,
“Invariantsofcoloredlinks”. doi
3 As discussed in Remark 4.5 the choice ofk
(along withβ) determines a ﬂattening of the
octahedraldecompositionassociatedto D.
Ingeneralbothstepsrequirehardcomputations;adetaileddiscussionoftheanalyticissuesis
givenbyOhtsuki[Oht16]. Step1requiresre-writingadiscretesumasa(sumof)integrals,typically
byusingthePoissonsummationformula. Ensuringthatthisisvalidrequirescarefulestimateson
thesizeof S andrelatedfunctions.
Previousworkoftheauthor[McP25a]usestheholonomy R-matricesdeﬁnedinjointwork
withN.Reshetikhin[MR25]todeﬁneacandidatemathematicalrealization Zψ
N ofcomplexChern-
Simonstheoryasdescribedabove. Inthispaperweshowthat Zψ
N isequaltoasumofstateintegrals.
Ourmethoddoesnotrequirecheckinganyinequalitiesandworksforanyrepresentationsatisfying
anatural,algebraicnondegeneracycondition. Tomyknowledgethisistheﬁrstexampleofanexact
(notasymptotic)stateintegralpresentationofacyclictypeinvariant. Suchintegralpresentations
automaticallyoccurforprincipaltypeinvariants,aninequivalentbutrelatedmathematicalreal-
izationofcomplexChern-Simonstheory(Section1.3). Ourresultsmayclarifytherelationship
betweenthesetwobranches.
