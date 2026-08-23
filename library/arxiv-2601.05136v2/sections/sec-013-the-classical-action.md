---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL₂(ℂ) Chern–Simons invariant"
section_id: sec-013-the-classical-action
section_title: "The classical action"
section_number: null
pages: 13-15
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
doc_brief: "State integrals for the quantized SL₂(ℂ) Chern–Simons invariant — Previous work of the author and N."
---
Herewedeﬁneanaction S(D)correspondingtothe N→∞ limitofSN(D). Set
(4.2)
Ω+(t1,t 2,t 3,t 4) := L(t4−t1) + L(t2−t3)
− L(t2−t1 + 1)− L(t4−t3)
− 2πi(t2−t1)
Ω−(t1,t 2,t 3,t 4) :=− L(t1−t4 + 1)− L(t3−t2 + 1)
+ L(t1−t2) + L(t3−t4 + 1)
+ 2πi(t2−t1)
Assigncomplexvariables ti tothesegmentsasbeforeandconstructafunction S(D|t)bytakinga
sumovercrossingfunctions
t2
t4t1
t3
→ Ω+(t1,t 2,t 3,t 4)(4.3)
t1
t3t2
t4
→ Ω−(t1,t 2,t 3,t 4)(4.4)
andassigningcriticalpointsshiftsinthevariables(whichwecouldalsothinkofas δ functions)
t
t
t
t
t− 1
t
t + 1
t
(4.5)
Deﬁnition4.2.Theconstructionabovedeﬁnesthe classical actionasaholomorphicfunction
S(D) : ΩD→ C
where
ΩD =

t∈ CE

ti−tj̸∈X wheneveri,j meetatacornerof D
	
TheclassicalactionisavariantofYokota’s potential functionintroducedin[Yok00]andused
throughouttheVolumeConjectureliterature. Weprefertocallitan actiontomatchthelanguage
usedinphysics,sinceitisessentiallytheChern-Simonsactionifweview ΩD asparametrizingﬂat
sl2 connectionsontheknotcomplement. Ouractionincludesparametershiftsthatappeartobe
relatedtothenormalizationterms Ω1, Ω2 studiedbyOhtsukiandTakata[OT15].
Deﬁnition4.3.Ageneralized critical pointγ∈ CE oftheclassicalactionisonewhere
exp ∂S(D)
∂ti

γ
= 1forall i∈E.
orequivalently,apointforwhichthereisa ﬂattening vectork∈ ZE with
∂S(D)
∂ti

γ
= 2πiki forall i∈E.
4. Formalasymptotics 13
[CKK14]J.Cho,H.Kim,andS.Kim,“Optimistic
limitsofKashaevinvariantsandcomplexvol-
umesofhyperboliclinks”. arXiv doi
8 For example, whenℓ = 1 the orientation
conditionsaysthat Γshouldgofromoneside
ofthemountainpasstotheother,notdouble
back.
Proposition4.4.LetD be a diagram of a knotK. Generalized critical points ofS(D) are in
bijectionwithnormalizednon-pinchedshadowcolorings (ρ,u )ofD withmeridianeigenvalue 1.
Ifγ isthecriticalpointcorrespondingto (ρ,u ),thenitscriticalvalueisthe SL2(C)Chern-Simons
invariantof ρ(whichisindependentof u). Inthenotationof[McP25a],
expS(D|γ) =Iψ(K,ρ,u ). ⌟
Proof. Lemma4.1showsthatgeneralizedcriticalpointsareequivalenttothesegmentequationsfor
m = 1,sowecanapplyProposition2.12. ThesecondclaimwasworkedoutindetailbyCho,Kim,
andKim[CKK14]. Weexplaintheideainournotation. In[McP25a]theChern-Simonsinvariant
logIψ isdeﬁnedbytakingasumofcontributionsovercrossings. However,insteadofusingthe
crossingfunctions(4.2)deﬁnedintermsof L[McP25a]useslifteddilogarithms
λ(ζ) = L(ζ) +ζ log(1−e2πiζ)
Ingeneraltheextraterms ζ log(1−e2πiζ)arenontrivial: theycorrespondtothegluingequations.
Atacriticalpoint γ thesearesatisﬁedandtheextratermsvanishmodulo Z.
Remark4.5.Neumann[Neu04]gaveanalgebraicmethodtocomputethe SL2(C)Chern-Simons
invariantofatriangulatedmanifold. Thehyperbolicstructureon M isencodedusingasolutionof
Thurston’sgluingequationsasusual,buthismethodrequiresanadditionalchoiceofcombinatorial
datacalleda ﬂattening. Thisisacoherentchoiceoflogarithmsoftheshapeparameterssatisfyinga
logarithmic form of the gluing equations. For an octahedral decomposition the only nontrivial
ﬂatteningequationscomefromthesegmentequationsandareoftheform
±µ + log(1−zj)− log(1−zj′) =±µ + log(1−zl)− log(1−zl′) +ki
foraninteger ki ateachsegment. Thesearepreciselytheintegersappearingintheﬂatteningvector
above.
4.3. Asymptotics
It isimmediate fromLemma4.1 thatSN(D)converges pointwiseon ΩD toS(D)asN→∞ ,
whichsuggestswecanapproximatethestateintegrals JN(D,µ,β|k)of (3.9)byusingasaddle-
pointapproximation. Ohtsukigivesadetailedexplanationofthesaddlepointapproximationin
thecontextoftheVolumeConjecturein[Oht16,Section3],whichwesummarizehere.
Letf beholomorphiconsomedomainin Cℓ containinganisolatedcriticalpoint γ. Acontour
Γ: [−1, 1]ℓ→ Cℓwith Γ(0) =γpassesthrough γinsaddlepointposition if Ref(Γ(t))< Ref(γ)
except for whent = 0 and it satisﬁes an additional orientation condition.8 The saddle point
approximationsaysthat
Z
Γ
eNf (t) dt =N−ℓ/2eNf (γ)[τ + O(N−1)]
foraconstant τ relatedtothedeterminantoftheHessianof f atγ. Itcanbereﬁnedtoinclude
higher-ordertermsintheexponentwhosecoeﬃcientsarerelatedtoderivativesof f. Theideais
thatnearthecriticalpointwecanapproximate eNf byaGaussian.
Wecanapplythisapproximationtostudytheasymptoticsof Zψ
N(K,ρ,u )forK ahyperbolic
knot. Supposethereissomediagram D whereρisnotpinched;asdiscussedinSection2.2wecan
thinkofthisasanondegeneracyconditionon ρ. IfwecouldshowthatStep2holdsthenwecould
replacethestateintegralsofequation(3.9)withmodiﬁedintegrals
eJN(D|k) :=
Z
Γ
expN (S(D|t)− 2πik·t) dt
4. Formalasymptotics 14
[GM08]S.GukovandH.Murakami,“ SL(2, C)
Chern-Simons theory and the asymptotic be-
haviorofthecoloredJonespolynomial”. arXiv
doi
9 Iftheintegrandwereperiodictheboundary
terms would cancel but this only holds on a
latticein CE asinLemma3.4(a).
for some other contourΓ. The dependence on the initial representationρ drops out because
β/N→ 0;thisisoneexplanationforwhythegrowthratein(1.1)isindependentof ρ. Changing
thecontour Γisplausiblebecause S(D)isaholomorphicfunctionandwecanuseStokes’Theorem
(i.e.ahigher-dimensionalCauchytheorem)butthereareotherissuesdiscussedinSection4.4.
Fornow,supposethatitisvalidtowrite
(4.6) Zψ
N(K,ρ,µ ) =N|E|/2−1/2 X
k∈ZE
eJN(D|k) + O(eN(ReςK−δ))
forsome δ >0. Sinceweassumed ρwasnotpinchedthecompletehyperbolicstructure ρhyp is
alsonotpinched. ByProposition4.4thereisageneralizedcriticalpoint γ ofS(D)withﬂattening
vectork0 correspondingtosomenormalizedshadowcoloringof ρhyp avoidingtheunitcircle.
We know thatS(D|γ) = ςK is theSL2(C)Chern-Simons invariant ofρhyp normalized as
inequation(1.1)andthat ReςK ismaximalamongallgeneralizedcriticalpoints. Supposethat Γ
passes throughγ in saddle point position (which is not quite right: see below). Then the saddle
pointapproximationgives
N|E|/2−1/2eJN(D|k0) =τN−1/2eNςK+O(N−1)
because Γisan|E|-dimensionalcontour. Thetermsofthesumwith k̸=k0 donotcontribute
at highest order to the asymptotics because the saddle point approximation also requires the
imaginarypartofthederivativeof S(D)tovanish: ifitdoesnotthegrowthissuppressedbyrapid
oscillations in the phase of the integrand. The sum overk in(3.10)naturally captures the extra
choiceofﬂatteningusedinthecomputationof ςK.
As noted above this analysis is incorrect. The problem is thatγ is never an isolated critical
pointbecauseofgaugesymmetry: thegaugetransformationsofDeﬁnition2.7showthatagiven
representationρ corresponds to a manifold of complex dimension3 lying in the spaceCE of
segmentparameters. Ifwerestricttonormalizedshadowcoloringsweﬁxonedegreeoffreedom,
soS(D)isconstantintwocomplex,hencefourrealcoordinatedirectionsnear γ. Thisrecoversan
overallpowerof N2,giving
Conjecture1.LetK beahyperbolicknot. Supposethat ρisadecoratedrepresentationof D that
isgeometricallynondegenerateinthesensethat ρisnon-pinchedforsomeopendiagram D ofK.
Thenforsomechoicesoflog-meridian µ(seeSection4.4)thereisaconstant τ sothat
Zψ
N(K,ρ,µ ) =N3/2eNςK[τ + O(N−1)] ⌟
SimilarconjecturesweremadebyGukovandMurakami[GM08].
