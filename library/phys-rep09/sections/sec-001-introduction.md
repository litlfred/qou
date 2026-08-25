---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 48-79
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
doc_brief: "The Magnus expansion and some of its applications — 8 sections: Introduction; Introduction; Stochastic differential equations"
---
TheMagnusexpansion,asformulatedinSection 2,hasfoundextensiveuseinmathematicalphysics,quantumchemistry,
controltheoryetc,essentiallyasaperturbativetoolinthetreatmentofthelinearequation
Y′=A(t)Y, Y(t0)=Y0. (223)
Whentherecurrence (49)–(50)isapplied,oneisabletoexplicitlygetthesuccessiveterms Ωkintheseries,defining Ωas
linearcombinationsofmultivariateintegralscontainingcommutatorsactingiterativelyonthecoefficientmatrix A,asin
S.Blanesetal./PhysicsReports470(2009)151–238 199
(42)–(46).Asaresult,withthisscheme,analyticalapproximationstotheexactsolutionareconstructedexplicitly.These
approximatesolutionsarefairlyaccurateinsidetheconvergencedomain,especiallywhenhighordertermsintheMagnus
seriesaretakenintoaccount,asillustratedbytheexamplesconsideredinSection 4.
Thereareseveraldrawbacks,however,involvedintheproceduredevelopedsofar,especiallywhenonetriestofind
accurateapproximationstothesolutionforverylongtimes.Thefirstoneisimplicitlycontainedintheanalysisdonein
Section2:thesizeoftheconvergencedomainoftheMagnusseriesmayberelativelysmall.Thelogarithmoftheexact
solutionY(t)mayhavecomplexsingularitiesandthisimpliesthatnoseriesexpansioncanconvergebeyondthefirst
singularity.Thisdisadvantagemaybe,uptosomepoint,avoidedbyusingdifferentpictures(e.g.thetransformationsshown
inSection 2.9)inordertoincreasetheconvergencedomainoftheMagnusexpansion,afactalsoillustratedbyseveral
examplesinSection 4.Unfortunately,thesepreliminarytransformationssometimeseitherdonotguaranteeconvergence,
ortherateofconvergenceoftheseriesisveryslow.Inthatcase,accurateresultscanonlybeobtainedprovidedalarge
numberoftermsintheseriesaretakenintoaccount.
Theseconddrawbackistheincreasinglycomplexstructureoftheterms ΩkintheMagnusseries:each Ωkisa k-
multivariateintegralinvolvingalinearcombinationof (k−1)-nestedcommutatorsof Aevaluatedatdifferenttimes ti,
i= 1,..., k.Althoughinsomecasestheseexpressionscanbecomputedexplicitly(forinstance,whentheelementsof
Aanditscommutatorsarepolynomialortrigonometricfunctions),ingeneralaspecialprocedurehastobedesignedto
approximatemultivariateintegralsandreducethenumberofcommutatorsinvolved.
Whentheentriesofthecoefficientmatrix A(t)arecomplicatedfunctionsoftimeortheyareonlyknownforcertain
valuesof t,numericalapproximationschemesareunavoidable.Inmanycases,itisthusdesirabletoobtainnumerical
approximationstotheexactsolutionatmanydifferenttimes.ThissectionisdevotedpreciselytotheMagnusseries
expansionasatoolforbuildingnumericalintegratorsforEq. (223).
Beforeembarkingonexposingthetechnicaldetailscontainedinthisconstruction,letusfirstintroduceseveralconcepts
whicharecommonplaceinthecontextofthenumericalintegrationofdifferentialequations.
Giventhegeneral(nonlinear)ordinarydifferentialequation(ODE)
x′=f(t,x), x(t0)=x0∈ Cd, (224)
standardnumericalintegrators,suchasRunge–Kuttaandmultistepmethods,proceedasfollows.Firstthewholetime
interval[t0,tf],issplitinto Nsubintervals,[tn−1,tn], n= 1,..., N,with tN = tf,andsubsequentlythevalueof x(tn)
isapproximatedwithatime-steppingadvanceprocedureoftheform
xn+1=Φ(hn,xn,..., h0,x0) (225)
startingfrom x0.Herethemap Φdependsonthespecificnumericalmethodand hn= tn+1−tnarethetimesteps.For
simplicityinthepresentation,weconsideraconstanttimestep h,sothat tn=t0+nh.Inthisway,onegets xn+1asan
approximationto x(tn+1).Inotherwords,theexactevolutionofthesystem (224)isreplacedbythediscreteornumerical
flow(225).Thesimplestofallnumericalmethodsfor (224)istheexplicitEulerscheme
xn+1=xn+hf(tn,xn). (226)
Itcomputesapproximations xntothevalues x(tn)ofthesolutionusingoneexplicitevaluationof fatthealreadycomputed
valuexn−1.Ingeneral,thenumericalmethod (225)issaidtobeoforder pif,assuming xn=x(tn),then xn+1=x(tn+1)+
O(hp+1).Thus,inparticular,Eulermethodisoforderone.
Ofcourse,moreelaborateandefficientgeneralpurposealgorithms,usingseveral fevaluationsperstep,havebeen
proposedalongtheyearsforthenumericaltreatmentofEq. (224).Infact,anystandardsoftwarepackageandprogram
librarycontainsdozensofroutinesaimedatprovidingnumericalapproximationswithseveraldegreesofaccuracy,including
(explicitandimplicit)Runge–Kuttamethods,linearmultistepmethods,extrapolationschemesetc,withfixedoradaptive
stepsize.Theyaredesignedinsuchawaythattheuserhastoprovideonlytheinitialconditionandthefunction ftoobtain
approximationsatanygiventime.
Thisbeingthecase,onecouldaskthefollowingquestion:ifgeneralpurposeintegratorsarewidelyavailableforthe
integrationofthelinearequation (223)(whichisaparticularcaseof (224)),whatisthepointofdesigningnewandsomehow
sophisticatedalgorithmsforthisspecificproblem?
Itturnsoutthat,inthesamewayasforclassicaltime-dependentperturbationtheory,thequalitativepropertiesofthe
exactsolutionarenotpreservedbythenumericalapproximationsobtainedbystandardintegrators.Thismotivatesthestudy
oftheMagnusexpansion,withtheultimategoalofconstructingnumericalintegrationmethods.Wewillshowthathighly
accurateschemescan,indeed,bedesigned,whichinadditionpreservequalitativepropertiesofthesystem.Theprocedure
canalsoincorporatethetoolsdevelopedfortheanalyticaltreatment,suchaspreliminarylineartransformations,toendup
withimprovednumericalalgorithms.
WefirstsummarizethemainfeaturesofthewellknowclassofRunge–Kuttamethodsasrepresentativeofintegrators
oftheform (225).TheyareintroducedforthegeneralnonlinearODE (224)andaresubsequentlyadaptedtothelinear
case(223).
200 S.Blanesetal./PhysicsReports470(2009)151–238
5.2. Runge–Kuttamethods
TheRunge–Kutta(RK)classofmethodsarepossiblythemostfrequentlyusedalgorithmsfornumericallysolvingODEs.
Amongthem,perhapsthemostsuccessfulduringmorethanhalfacenturyhasbeenthe4th-ordermethod,which,applied
toEq.(224),providesthefollowingnumericalapproximationfortheintegrationstep tn↦→tn+1=tn+h:
Y1=xn
Y2=xn+
h
2
f(tn,Y1)
Y3=xn+
h
2
f
(
tn+
h
2
,Y2
)
(227)
Y4=xn+hf
(
tn+
h
2
,Y3
)
xn+1=xn+
h
6
(
f(tn,Y1)+2f
(
tn+
h
2
,Y2
)
+2f
(
tn+
h
2
,Y3
)
+f(tn+h,Y4)
)
.
Noticethatthefunction fcanalwaysbecomputedexplicitlybecauseeach Yidependsonlyonthe Yj,j<i,previously
evaluated.Tomeasurethecomputationalcostofthemethod,itisusualtoconsiderthattheevaluationofthefunction f(t,x)
isthemostconsumingpart.Inthissense,scheme (227)requiresfourevaluations,whichispreciselythenumberof stages
(orinnersteps)inthealgorithm.
Thegeneralclassof s-stageRunge–Kuttamethodsarecharacterizedbytherealnumbers aij,bi(i,j= 1,..., s)and
ci=∑s
j=1aij,as
Yi=xn+h
s∑
j=1
aijf(tn+cjh,Yj), i=1,..., s
xn+1=xn+h
s∑
i=1
bif(tn+cih,Yi), (228)
whereYi,i=1,..., saretheintermediatestages.Forsimplicity,theassociatedcoefficientsareusuallydisplayedwiththe
so-calledButchertableau[125,126]asfollows:
c1 a11 ... a1s
...
...
...
cs as1 ... ass
b1 ... bs
(229)
Ifaij=0,j≥i,thentheintermediatestages Yicanbeevaluatedrecursivelyandthemethodisexplicit.Inthatcase,the
zeroaijcoefficients(intheuppertriangularpartofthetableau)areomittedforclarity.Withthisnotation,‘the’4th-order
Runge–Kuttamethod(227)canbeexpressedas
0
1
2
1
2
1
2 0 1
2
1 0 0 1
1
6
2
6
2
6
1
6
(230)
Otherwise,theschemeisimplicitandrequiresonetonumericallysolveasystemof sdnonlinearequationsoftheform
y=Xn+hG(h,y), (231)
wherey=(Y1,..., Ys)T,Xn=(xn,..., xn)T∈ Rsd,andGisafunctionwhichdependsonthemethod.Astandardprocedure
togetxn+1from(231)isapplyingsimpleiteration:
y[j]=Xn+hG(h,y[j−1]), j=1,2,.... (232)
Whenhissufficientlysmall,theiterationstartswith y[0]= Xnandstopsonce ‖y[j]−y[j−1]‖issmallerthanaprefixed
tolerance.Ofcourse,moresophisticatedtechniquescanbeused[ 126].
Afterthesegeneralconsiderations,letusnowturnourattentiontothelinearequation (223).Whendealingwith
numericalmethodsappliedtothisequation,itisimportanttokeepinmindthattherelevantsmallparameterhereisno
longerthenormofthematrix A(t)asintheanalyticaltreatment,butthetimestep h.Forthisreason,theconceptoforderof
S.Blanesetal./PhysicsReports470(2009)151–238 201
accuracyofamethodisdifferentinthiscontext.Now f(t,x)=A(t)xandthegeneralclassof s-stageRunge–Kuttamethods
adoptthemorecompactform
Yi=xn+h
s∑
j=1
aijAjYj, i=1,..., s
xn+1=xn+h
s∑
i=1
biAiYi, (233)
withAi=A(tn+cih).Intermsofmatrices,thisisequivalentto



Y1
...
Ys



=



xn
...
xn



+h~A



Y1
...
Ys



, with~A=


a11A1 ··· a1sAs
...
...
as1A1 ··· assAs


xn+1=xn+h
(
b1A1 ··· bsAs
)



Y1
...
Ys



, (234)
sothattheapplicationofthemethodfortheintegrationstep tn↦→tn+1=tn+hcanalsobewrittenas
xn+1=
(
Id+h
(
b1A1 ··· bsAs
)(
Isd−h~A
)−1
Isd×d
)
xn, (235)
where Isd×d= (Id,Id,..., Id)TandIdisthe d×didentitymatrix.Forinstance,taking s=2andusingMatlabthiscanbe
easilyimplementedasfollows
A=[a11∗A1 a12∗A2;a21∗A1 a22∗A2];
x=(Id+h∗[b1∗A1 b2∗A2]∗ ((I2d−h∗A)\[Id Id]′))∗x;
whereb1,b2,a11,..., a22arethecoefficientsofthemethod, A1,A2correspondto A1,A2andId,I2daretheidentity
matricesofdimension dand2d,respectively.
ThereisextensiveliteratureregardingRKmethodsbuiltformanydifferentpurposes[ 125,126].Itisthereforereasonable
tolookforthemostappropriateschemetobeusedforeachproblem.Inpractice,explicitRKmethodsarepreferred,because
itsimplementationisusuallysimpler.Theytypicallyrequiremorestagesthanimplicitmethodsand,ingeneral,ahigher
numberofevaluationsofthematrix A(t),althoughthisisnotalwaysthecase.Forinstance,the4-stagefourthordermethod
(227)onlyrequirestwonewevaluationsof A(t)perstep( A(tn+h/2)andA(tn+h)),whichispreciselytheminimum
numberofevaluationsneededbyanyfourthordermethod.Inournumericalexamples,wewillalsousethe7-stagesixth
ordermethodwithcoefficients[ 125,p.203-205]
0
5−
√
5
10
5−
√
5
10
5+
√
5
10
−
√
5
10
5+2
√
5
10
5−
√
5
10
−15+7
√
5
20
−1+
√
5
4
15−7
√
5
10
5+
√
5
10
5−
√
5
60 0 1
6
15+7
√
5
60
5−
√
5
10
5+
√
5
60 0 9−5
√
5
12
1
6
−5+3
√
5
10
1 1
6 0 −55+25
√
5
12
−25−7
√
5
12 5−2
√
5 5+
√
5
2
1
12 0 0 0 5
12
5
12
1
12
(236)
Observethatthismethodonlyrequiresthreenewevaluationsofthematrix A(t)perstep.Thisis,infact,theminimum
numberforasixth-ordermethod.OtherimplicitRKschemeswidelyusedintheliteratureinvolvingtheminimumnumber
ofstagesateachorderarebasedonGauss–Legendrecollocationpoints[ 126].Forinstance,thecorrespondingmethodsof
orderfourandsix(withtwoandthreestages,respectively)havethefollowingcoefficients:
3−
√
3
6
1
4
3−2
√
3
12
3+
√
3
6
3+2
√
3
12
1
4
1
2
1
2
5−
√
15
10
5
36
2
9−
√
15
15
5
36−
√
15
30
1
2
5
36+
√
15
24
2
9
5
36+
√
15
24
5+
√
15
10
5
36+
√
15
30
2
9+
√
15
15
5
36
5
18
4
9
5
18
(237)
202 S.Blanesetal./PhysicsReports470(2009)151–238
5.3. Preservationofqualitativeproperties
NoticethatthenumericalsolutionprovidedbytheclassofRunge–Kuttaschemes,andingeneralbyanintegratorofthe
form(225),isconstructedasasumofvectorsin Rd.Letuspointoutsome(undesirable)consequencesofthisfact.Suppose,
forinstance,that xisavectorknowntoevolveonasphere.Onedoesnotexpectthat xnbuiltasasumoftwovectorsasin
(225),preservesthisfeatureoftheexactsolution,whereasapproximationsoftheform xn+1=Qnxn,withQnanorthogonal
matrix,clearlylieonthesphere.
InSection3.3wehaveintroducedisospectralflows (143),whichinclude,asaparticularcase,thesystem
Y′=[A(t),Y], Y(t0)=Y0, (238)
withAaskew-symmetricmatrix.Aswehaveshownthere,if Y0isasymmetricmatrix,theexactsolutioncanbefactorized
asY(t)=Q(t)Y0QT(t),with Q(t)anorthogonalmatrixsatisfyingtheequation
Q′=A(t)Q, Q(0)=I (239)
and,inaddition, Y(t)andY(0)havethesameeigenvalues.Thisisalsotruewhen YisHermitian, Aisskew-Hermitianand
Qisunitary,inwhichcase (238)and(239)canbeinterpretedasparticularexamplesoftheHeisenbergandSchrödinger
equationsinQuantumMechanics,respectively.
Whenanumericalschemeoftheform (225)isappliedto (239),ingeneral,theapproximations Qnwillnolongerbe
unitarymatricesandtherefore YnandY0willnotbeunitarilysimilar.Asaresult,theisospectralcharacterofthesystem
(238)islostinthenumericaldescription.ObservethatexplicitRunge–Kuttamethodsemploytheansatz,thatlocallythe
solutionofthedifferentialequationbehaveslikeapolynomialin t,sothatonecannotexpecttheapproximatesolutionto
beaunitarymatrix.Inthissense,explicitRunge–Kuttamethodspresentthesamedrawbacksinthenumericalanalysisof
differentialequationsasthestandardtime-dependentperturbationtheory,whenlookingforanalyticalapproximations.
ImplicitRunge–Kuttamethods,ontheotherhand,canbeconsideredasrationalapproximations,andinsomecasesthe
outcometheyprovideisaunitarymatrix.Forthisclassofmethods,however,matricesofrelativelylargesizeshavetobe
inverted,makingthealgorithmscomputationallyexpensive.Furthermore,theevolutionofmanysystems(includinghighly
oscillatoryproblems)cannotbeefficientlyapproximated,eitherbypolynomialorbyrationalapproximations.
Withalltheseconsiderationsinmind,apairofquestionsariseinaquitenaturalway:
(Q1)Is it possible to design numerical integration methods for Eq.(224) such that the corresponding numerical
approximationsstillpreservethemainqualitativefeaturesoftheexactsolution?
(Q2)Since the Magnus expansion constitutes an extremely useful procedure for obtaining analytical (as opposed to
numerical)approximatesolutionstothelinearevolutionequation (223),isitfeasibletoconstructefficientnumerical
integrationschemesfromthegeneralformulationexposedinSection 2?
Itturnsoutthatbothquestionscanbeansweredintheaffirmative.Asamatteroffact,ithasbeenintryingtoaddress
(Q1),thatthefieldof geometricnumericalintegration hasdevelopedduringthelastfewyears.Here,theaimistoreproduce
thequalitativefeaturesofthesolutionofthedifferentialequationwhichisbeingdiscretized,inparticularitsgeometric
properties.Themotivationfordevelopingsuchstructure-preservingalgorithmsarisesindependentlyinareasofresearch
asdiverseascelestialmechanics,moleculardynamics,controltheory,particleacceleratorsphysics,andnumericalanalysis
[59,79,127–129].
Althoughdiverse,thesystemsappearingintheseareashaveoneimportantcommonfeature.Theyallpreservesome
underlyinggeometricstructurewhichinfluencesthequalitativenatureofthephenomenatheyproduce.Inthefieldof
geometricnumericalintegration,thesepropertiesarebuiltintothenumericalmethod,whichgivesthemethodanimproved
qualitativebehavior,butalsoallowsforasignificantlymoreaccuratelong-timeintegrationthanwithgeneral-purpose
methods.
Inadditiontotheconstructionofnewnumericalalgorithms,animportantaspectofgeometricintegrationisthe
explanationoftherelationshipbetweenpreservationofthegeometricpropertiesofanumericalmethodandtheobserved
favorableerrorpropagationinlong-timeintegration.
Geometricnumericalintegrationhasbeenanactiveandinterdisciplinaryresearchareaduringthelastdecade,and
nowadays is the subject of intensive development. Perhaps the most familiar examples ofgeometric integratorsare
symplecticintegrationalgorithmsinclassicalHamiltoniandynamics,symmetricintegratorsforreversiblesystemsand
methodspreservingfirstintegralsandnumericalmethodsonmanifolds[ 79].
Aparticularclassofgeometricnumericalintegratorsaretheso-called Lie-groupmethods.Ifthematrix A(t)in(223)
belongstoaLiealgebra g,theaimofLie-groupmethodsistoconstructnumericalsolutionsstayinginthecorrespondingLie
group G[59].
Withrespecttoquestion(Q2)above,itwillbethesubjectofthenextsubsection,wherethemainissuesinvolved
intheconstructionofnumericalintegratorsbasedontheMagnusexpansionareanalyzed.Themethodsthusobtained,
preservethequalitativepropertiesofthesystemand,inaddition,arehighlycompetitivewithothermoreconventional
numericalschemes,withrespecttoaccuracyandcomputationaleffort.Theyconstitute,therefore,clearexamplesofLie-
groupmethods.
S.Blanesetal./PhysicsReports470(2009)151–238 203
5.4. Magnusintegratorsforlinearsystems
SincetheMagnusseriesonlyconvergeslocally,aswehavepointedoutbefore,whenthelengthofthetime-integration
intervalexceedstheboundprovidedby Theorem9,andinthespiritofanynumericalintegrationmethod,theusual
procedureconsistsofdividingthetimeinterval [t0,tf]intoNstepssuchthattheMagnusseriesconvergesineachsubinterval
[tn−1,tn],n=1,..., N,with tN=tf.Inthisway,thesolutionof (223)atthefinaltime tfisrepresentedby
Y(tN)=
N∏
n=1
exp(Ω(tn,tn−1))Y0, (240)
andtheseries Ω(tn,tn−1)hastobeappropriatelytruncated.
Earlystepsinthisapproachweretakenin[ 21,130],wheresecondandfourthordernumericalschemeswereusedfor
calculationsofcollisionalinelasticityandpotentialscattering,respectively.Thoseauthorswerewellawarethattheresulting
integrationmethod‘‘wouldbecomepracticalonlywhentheadvantageofbeingabletousebiggerstepsizesoutweighsthe
disadvantageinhavingtoevaluatetheintegralsinvolvedintheMagnusseries,andthendoingtheexponentiation’’[ 130].
Lateron,byfollowingasimilarapproach,Devries[ 131]designedanumericalprocedurefordeterminingafourthorder
approximationtothepropagatoremployedintheintegrationofthesinglechannelSchrödingerequation,butitwasinthe
pioneeringwork[ 37]whereIserlesandNørsettcarriedoutthefirstsystematicstudyoftheMagnusexpansionwiththe
aimofconstructingnumericalintegrationalgorithmsforlinearproblems.Todesignthenewintegrators,theexplicittime
dependencyofeachterm Ωkhadtobeanalyzed,inparticularitsorderofapproximationintimetotheexactsolution.
Generallyspeaking,theprocessofrenderingtheMagnusexpansion,apracticalnumericalintegrationalgorithm,involves
threesteps.First,the Ωseriesistruncatedatanappropriateorder.Second,themultivariateintegralsinthetruncatedseries
Ω[p]= ∑p
i=1Ωiarereplacedbyconvenientlychosenapproximations.Third,theexponentialofthematrix Ω[p]hastobe
computed.Wenowbrieflyconsiderthefirsttwoissues,whereasthegeneralproblemofevaluatingthematrixexponential
willbetreatedinSection 5.6.
WehaveshowninSection 2.6thattheMagnusexpansionistimesymmetric.AsaconsequenceofEq. (66),if A(t)is
analyticandoneevaluatesitsTaylorseriescenteredaroundthemidpointofaparticularsubinterval [tn,tn+h],theneach
termin Ωkisanoddfunctionof h,andthus Ω2s+1 = O(h2s+3)fors≥ 1.Equivalently, Ω[2s−2] = Ω+ O(h2s+1)and
Ω[2s−1]=Ω+ O(h2s+1).Inotherwords,forachievinganintegrationmethodoforder2 s(s>1)onlytermsupto Ω2s−2in
theΩseriesarerequired[ 37,39].Forthisreason,ingeneral,onlyevenordermethodsareconsidered.
Oncetheseriesexpansionistruncateduptoanappropriateorder,themultidimensionalintegralsinvolvedhavetobe
computedoratleastconvenientlyapproximated.Although,atfirstglance,thisseemstobeaquitedifficultenterprise,it
turnsoutthattheirverystructureallowsonetoapproximateallthemultivariateintegralsappearingin Ωjustbyevaluating
A(t)atthenodesofaunivariatequadrature[ 37].
Toillustratehowthistaskcanbeaccomplished,letusexpandthematrix A(t)aroundthemidpoint, t1/2≡tn+h/2,of
thesubinterval[tn,tn+1],
A(t)=
∞∑
j=0
aj
(
t−t1/2
)j
, whereaj=
1
j!
djA(t)
dtj
⏐⏐⏐⏐
t=t1/2
, (241)
andinserttheseries (241)intotherecurrencedefiningtheMagnusexpansion (49)–(50).Inthiswayonegets,explicitly,the
expressionof Ωkuptoorder h6as
Ω1=ha0+h31
12
a2+h51
80
a4+ O(h7)
Ω2=h3−1
12
[a0,a1]+ h5
(−1
80
[a0,a3]+
1
240
[a1,a2]
)
+ O(h7)
Ω3=h5
(
1
360
[a0,a0,a2]−
1
240
[a1,a0,a1]
)
+ O(h7) (242)
Ω4=h5 1
720
[a0,a0,a0,a1]+ O(h7),
whereas Ω5 = O(h7), Ω6 = O(h7) and Ω7 = O(h9). Here we write for clarity[ai1,ai2,..., ail−1,ail] ≡
[ai1,[ai2,[..., [ail−1,ail]...]]].Noticethat,asanticipated,onlyoddpowersof happearin Ωkand,inparticular, Ω2i+1=
O(h2i+3)fori>1.
Letusdenote αi≡hiai−1.Then[αi1,αi2,...,α il−1,αil]isanelementoforder hi1+···+il.Infact,thematrices {αi}i≥1canbe
consideredasthegenerators(withgrade i)ofagradedfreeLiealgebra L(α1,α2,...) [62].Itturnsoutthatitispossibleto
buildmethodsoforder p≡2sbyconsideringonlytermsinvolving α1,...,α sinΩ.Then,thesetermscanbeapproximated
204 S.Blanesetal./PhysicsReports470(2009)151–238
byappropriatelinearcombinationsofthematrix A(t)evaluatedatdifferentpoints.Inparticular,uptoorderfour,wehave
toapproximate
Ω=α1−
1
12
[α1,α2]+ O(h5), (243)
whereas,uptoordersix,therelevantexpressionis
Ω= α1+
1
12
α3−
1
12
[α1,α2]+
1
240
[α2,α3]+
1
360
[α1,α1,α3]
−
1
240
[α2,α1,α2]+
1
720
[α1,α1,α1,α2]+ O(h7). (244)
Inordertopresentmethodswhichcanbeeasilyadaptedfordifferentquadraturerules,weintroducetheaveraged(or
generalizedmomentum)matrices
A(i)(h)≡
1
hi
∫ tn+h
tn
(
t−t1/2
)i
A(t)dt=
1
hi
∫ h/2
−h/2
tiA(t+t1/2)dt (245)
fori=0,..., s−1.Iftheirexactevaluationisnotpossible,oriscomputationallyexpensive,anumericalquadraturemay
beusedinstead.Supposethat bi,ci,(i=1,..., k),aretheweightsandnodesofaparticularquadraturerule,say X(wewill
useX=GforGauss–Legendrequadraturesand X=NCforNewton–Cotesquadratures)oforder p,respectively[45],
A(0)=
∫ tn+h
tn
A(t)dt=h
k∑
i=1
biAi+ O(hp+1),
withAi≡A(tn+cih).Thenitispossibletoapproximatealltheintegrals A(i)(uptotherequiredorder)byusingonlythe
evaluationsAiatthenodes ciofthequadraturerulerequiredtocompute A(0).Specifically,
A(i)=h
k∑
j=1
bj
(
cj−
1
2
)i
Aj, i=0,..., s−1, (246)
orequivalently,A(i)=h
∑k
j=1
(
Q(s,k)
X
)
ij
Ajwith
(
Q(s,k)
X
)
ij
=bj
(
cj− 1
2
)i
.
Inparticular,iffourthandsixthorderGauss–Legendrequadraturerulesareconsidered,thenfor s=k=2wehave[ 45]
b1=b2=
1
2
, c1=
1
2
−
√
3
6
, c2=
1
2
+
√
3
6
,
toorderfour,whereasfor s=k=3,
b1=b3=
5
18
, b2=
4
9
, c1=
1
2
−
√
15
10
, c2=
1
2
, c3=
1
2
+
√
15
10
,
toordersix,sothat
Q(2,2)
G =


1
2
1
2
−
√
3
12
√
3
12

, Q(3,3)
G =


5
18
4
9
5
18
−
√
15
36
0
√
15
36
1
24
0
1
24


. (247)
Furthermore,substituting(241)into(245)wefind(neglectinghigherorderterms)
A(i)=
s∑
j=1
(
T(s))
ijαj≡
s∑
j=1
1−(−1)i+j
(i+j)2i+j αj, 0≤i≤s−1. (248)
Ifthisrelationisinverted(toorderfour, s=2,andsix, s=3)onehas
R(2)≡(T(2))−1=
(
1 0
0 12
)
, R(3)=


9
4
0 −15
0 12 0
−15 0 180

 (249)
S.Blanesetal./PhysicsReports470(2009)151–238 205
respectively,sothatthecorrespondingexpressionof αiintermsof A(i)orAjisgivenby
αi=
s∑
j=1
(
R(s))
ijA(j−1)=h
k∑
j=1
(
R(s)Q(s,k)
X
)
ij
Aj. (250)
Thus,byvirtueof (250)wecanwrite Ω(h)intermsoftheunivariateintegrals (245)orintermsofanydesiredquadrature
rule.Inthisway,onegetsthefinalnumericalapproximationsto Ω.Fourthandsixth-ordermethodscanbeobtained
bysubstitutingin (243)and(244),respectively.Thealgorithmthenprovidesanapproximationfor Y(tn+1)startingfrom
Yn≈Y(tn),with tn+1=tn+h.
Theobservantreadersurelyhasnoticedthat,uptoorder h6,therearemoretermsinvolvedin (242)thanthoseconsidered
in(243)or(244):specifically, 1
12α3in(243)and 1
80α5and−1
80[α1,α4]in(244).Thereasonisthat Ω[6]canbeapproximated
byA(0),A(1),A(2)uptoorder h6andthen,theseomittedtermsareautomaticallyreproducedwheneither A(0),A(1),A(2)are
evaluatedanalyticallyorareapproximatedbyanysymmetricquadratureruleofordersixorhigher.
AnotherimportantissueinvolvedinanyapproximationbasedontheMagnusexpansionisthenumberofcommutators
appearingin Ω.Asisalreadyevidentfrom (242),thisnumberrapidlyincreaseswiththeorder,andsoitmightconstitute
amajorfactorintheoverallcomputationalcostoftheresultingnumericalmethods.Itispossible,however,todesignan
optimizationprocedureaimedatreducingthisnumbertoaminimum[ 40].Forinstance,astraightforwardcountingof
thenumberofcommutatorsin (244)suggeststhatitseemsnecessarytocomputesevencommutatorsuptoordersixin h,
whereasthegeneralanalysiscarriedoutin[ 40]showsthatthiscanbedonewithonlythreecommutators.Morespecifically,
thescheme
C1=[α1,α2],
C2=−
1
60
[α1,2α3+C1] (251)
Ω[6]≡α1+
1
12
α3+
1
240
[−20α1−α3+C1,α2+C2],
verifiesthat Ω[6] = Ω+ O(h7).Threeis,infact,theminimumnumberofcommutatorsrequiredtogetasixth-order
approximationto Ω.
Thistechniquetoreducethenumberofcommutatorsis,indeed,validforanyelementinagradedfreeLiealgebra.Ithas
beenused,inparticular,toobtainapproximationstotheBaker–Campbell–Hausdorffformulauptoagivenorder,withthe
minimumnumberofcommutators[ 132].
Asanillustration,nextweprovidetherelevantexpressionsforintegrationschemesoforder4and6,whichreadilyfollow
fromthepreviousanalysis.
Order4.ChoosingtheGauss–Legendrequadraturerule,onehastoevaluate
A1=A
(
tn+
(
1
2
−
√
3
6
)
h
)
, A2=A
(
tn+
(
1
2
+
√
3
6
)
h
)
(252)
andthus,taking Q(2,2)
G in(247),R(2)in(249)andsubstitutingin (250)wefind
α1=
h
2
(A1+A2), α 2=
h
√
3
12
(A2−A1). (253)
Then,byreplacingin (243)weobtain
Ω[4](h)=
h
2
(A1+A2)−h2
√
3
12
[A1,A2]
Yn+1=exp(Ω[4](h))Yn.
(254)
Alternatively,evaluating Aatequispacedpoints,with k=3and c1=0,c2=1/2,c3=1; b1=b3=1/6,b2=2/3
(i.e.,usingtheSimpsonruletoapproximate
∫tn+h
tn
A(s)ds),
A1=A(tn), A2=A
(
tn+
h
2
)
, A3=A(tn+h)
wehaveinstead α1= h
6(A1+4A2+A3),α2=h(A3−A1),andthen
Ω[4](h)=
h
6
(A1+4A2+A3)−
h2
72
[A1+4A2+A3,A3−A1]. (255)
206 S.Blanesetal./PhysicsReports470(2009)151–238
Itshouldbenoticedthatotherpossibilitiesnotdirectlyobtainablefromthepreviousanalysisareequallyvalid.Forinstance,
onecouldconsider
Ω[4](h)=
h
6
(A1+4A2+A3)−
h2
12
[A1,A3]. (256)
Althoughapparentlymore Aevaluationsarenecessaryin (255)and(256),thisisnotactuallythecase,since A3canbereused
atthenextintegrationstep.
Order6.IntermsofGauss–Legendrecollocationpoints,onehas
A1=A
(
tn+
(
1
2
−
√
15
10
)
h
)
, A2=A
(
tn+
1
2
h
)
, A3=A
(
tn+
(
1
2
+
√
15
10
)
h
)
andsimilarlyweobtain
α1=hA2, α 2=
√
15h
3
(A3−A1), α 3=
10h
3
(A3−2A2+A1), (257)
whicharetheninsertedin (251)togettheapproximation Yn+1=exp(Ω[6])Yn.
Ifthematrix A(t)isonlyknownatequispacedpoints,wecanusetheNewton–Cotes(NC)quadraturevalueswith s=3
andk=5,b1=b5=7/90,b2=b4=32/90,b3=12/90andcj=(j−1)/4,j=1,..., 5.Then,usingthecorresponding
matrixQ(3,5)
NC from(246)weget
α1=
1
60
(−7(A1+A5)+28(A2+A4)+18A3)
α2=
1
15
(7(A5−A1)+16(A4−A2)) (258)
α3=
1
3
(7(A1+A5)−4(A2+A4)−6A3).
Bothschemesinvolvetheminimumnumberofcommutators(three)andrequirethreeorfourevaluationsofthematrix A(t)
perintegrationstep(observethat A5canbereusedinthenextstepintheNewton–Cotesimplementationbecause c1=0
andc5=1).
Higherorderscanbetreatedinasimilarway.Forinstance,an8th-orderMagnusmethodcanbeobtainedwithonlysix
commutators[40].Alsovariablestepsizetechniquescanbeeasilyimplemented[ 39,133].
5.4.1. FromMagnustoFerandCayleymethods
ForarbitrarymatrixLiegroups,itisfeasibletodesignnumericalmethodsbasedalsoontheFerandWilcoxexpansions,
whereasforthe J-orthogonalgroup(Eq. (21))theCayleytransformalsomapstheLiealgebraontotheLiegroup[ 41]and
thusitallowsustobuildanewclassofLie-groupmethods.Herewebrieflyshowhowtheseintegrationmethodscanbe
easilyconstructedfromthepreviousschemes,basedonMagnus.Inotherwords,ifthesolutionof (223)inaneighborhood
oft0iswrittenas
Y(t0+h)=eΩ(h)Y0 (Magnus) (259)
=eF1(h)eF2(h)··· Y0 (Fer) (260)
=eS1(h)eS2(h)··· eS2(h)eS1(h)Y0 (SymmetricFer) (261)
=
(
I−
1
2
C(h)
)−1(
I+
1
2
C(h)
)
Y0 (Cayley) (262)
onemayexpressthefunctions Fi(h),Si(h)andC(h)intermsofthesuccessiveapproximationsto Ωand,byusingthesame
techniquesasintheprevioussection,obtainthenewmethods.AstheschemesbasedontheWilcoxfactorizationarequite
similarastheFermethods,theywillnotbeconsideredhere.
5.4.2. Ferbasedmethods
ToobtainintegrationmethodsbasedontheFerfactorization (260)oneappliestheBaker–Campbell–Hausdorff(BCH)
formulaafterequatingtotheMagnusexpansion (259).Morespecifically,inthedomainofconvergenceofexpansions (259)
and(260)wecanwrite
eΩ(h)=eF1(h)eF2(h)··· ,
S.Blanesetal./PhysicsReports470(2009)151–238 207
whereF1 = Ω1isthefirsttermintheMagnusseries, F2 = O(h3)andF3 = O(h7).Then,a p-thorderalgorithmwith
3≤p≤6,basedontheFerexpansionrequiresonetocompute F[p]
2 suchthat
Y(tn+h)=eF1(h)eF[p]
2 (h)Y(tn)+ O(hp+1). (263)
Takingintoaccountthat
eΩ[p](h)=eF1(h)eF[p]
2 (h)+ O(hp+1),
wehave(F1=Ω1)
eF[p]
2 (h)=e−Ω1(h)eΩ[p](h)+ O(hp+1).
Then,byusingtheBCHformulaandsimplealgebratoremovehigherordertermsweobtaintoorderfour
F[4]
2 =−
1
12
(
[α1,α2]−
1
2
[α1,α1,α2]
)
, (264)
so that two commutators are needed in this case. A sixth-order method can be similarly obtained with four
commutators[40].ThesemethodsareslightlymoreexpensivethantheirMagnuscounterpart,andtheydonotpreserve
thetime-symmetryoftheexactsolution.Thiscanbefixedbytheself-adjointversionoftheFerfactorizationintheform
(261)proposedin[134]andpresentedinamoreefficientwayin[ 40].Theschemesbasedon (261)uptoordersixaregiven
by
Y(tn+h)=eS1(h)eS[p]
2 (h)eS1(h)Yn (265)
withS1=Ω1/2.Afourth-ordermethodisgivenby
S[4]
2 (h)=−
1
12
[α1,α2] (266)
andasixth-orderoneby
s1=[α1,α2]
r1=
1
120
[α1,−4α3+3s1]
S[6]
2 (h)=
1
240
[−20α1−α3+s1, α2+r1]. (267)
Tocompletetheformulationofthescheme,the αihavetobeexpressedintermsofthematrices Aievaluatedatthe
quadraturepoints(e.g.,Eqs. (257)or(258)).
5.4.3. Cayley-transformmethods
WehaveseeninSection 1.2that,forthe J-orthogonalgroupO J(n),theCayleytransform (23)providesausefulalternative
totheexponentialmapping,relatingtheLiealgebratotheLiegroup.Thisfactisparticularlyimportantfornumerical
methodswheretheevaluationoftheexponentialmatrixisthemostcomputation-intensivepartofthealgorithm.
IfthesolutionofEq. (223)iswrittenas
Y(t)=
(
I−
1
2
C(t)
)−1(
I+
1
2
C(t)
)
Y0 (268)
thenC(t)∈oJ(n)satisfiestheequation[ 135]
C′=A−
1
2
[C,A]−
1
4
CAC, t≥t0, C(t0)=0. (269)
Time-symmetricmethodsoforder4and6havebeenobtained,basedontheCayleytransform (268),byexpandingthe
solutionof (269)inarecursivemannerandconstructingquadratureformulaeforthemultivariateintegralsthatappear
intheprocedure[ 135–137].ItturnsoutthatefficientCayleybasedmethodscanbebuiltdirectlyfromMagnusbased
integrators[40].Inparticular,weget:
Order4:
C[4]=Ω[4]
(
I−
1
12
(Ω[4])2
)
=α1−
1
12
[α1,α2]−
1
12
α3
1+O(h5), (270)
whereC[4]=C(h)+O(h5).
208 S.Blanesetal./PhysicsReports470(2009)151–238
Order6:
C[6]=Ω[6]
(
I−
1
12
(Ω[6])2
(
I−
1
10
(Ω[6])2
))
=C(h)+O(h7). (271)
Threematrix–matrixproductsarerequiredinadditiontothethreecommutatorsinvolvedinthecomputationof Ω[6],fora
totalofninematrix–matrixproductsperstep.
5.5. Numericalillustration:TheRosen–Zenermodelrevisited
Nextweapplythepreviousnumericalschemestotheintegrationofthedifferentialequationgoverningtheevolutionof
aparticularquantumtwo-levelsystem.Ourpurposehereistoillustratethemainissuesinvolved,andcomparethedifferent
approximationsobtainedwithboththeanalyticaltreatmentdoneinSection 4andtheexactresult.Specifically,weconsider
theRosen–ZenermodelintheInteractionPicturealreadyanalyzedinSection 4.1.2.Inthiscase,theequationtobesolvedis
U′
I=˜HI(t)UI,orequivalently,Eq. (223)withY(t)=UI(t)andcoefficientmatrix( ¯h=1)
A(t)=˜HI(t)=−iV(s)(σ1cos(ξs)−σ2sin(ξs))≡−ib(s)·σ. (272)
HereV(s)=V0/cosh(s),ξ=ωTands=t/T.Giventheinitialcondition |+⟩≡ (1,0)Tatt=−∞,ourpurposeistoget
anapproximatevalueforthetransitionprobabilitytothestate |−⟩≡ (0,1)Tatt=+∞.Itsexactexpressioniscollected
inthefirstlineofEq. (204),whichwereproducehereforthereader’sconvenience:
Pex=|(UI)12(+∞,−∞)|2=
sin2γ
cosh2(πξ/2), (273)
withγ=πV0T.
Toobtain,inpractice,anumericalapproximationto Pex,wehavetointegratetheequationinasufficientlylargetime
interval.Wetaketheinitialconditionat s0=− 25andthenumericalintegrationiscarriedoutuntil sf = 25.Then,we
determine(UI)12(sf,s0).
Asafirstnumericaltest,wetakeafixed(andrelativelylarge)timestep hsuchthatthewholenumericalintegrationinthe
timeintervals∈[s0,sf]iscarriedoutwith50evaluationsofthevector b(s)forallmethods.Inthisway,theircomputational
costissimilar.
ToillustratethequalitativebehaviorofMagnusintegratorsincomparisonwithstandardRunge–Kuttaschemes,the
followingmethodsareconsidered:
•Explicitfirst-orderEuler (E1):Yn+1=Yn+hA(tn)Ynwithtn+1=tn+handh=1(solidlineswithsquaresinthe
figures).
•Explicitfourth-orderRunge–Kutta (RK4),i.e.,scheme (227)withh=2,sinceonlytwoevaluationsof b(s)perstepare
requiredinthelinearcase(solidlineswithtriangles).
•Second-orderMagnus (M2):weconsiderthemidpointrule(oneevaluationperstep)toapproximate Ω1takingh=1
(dashedlines),i.e.,
Yn+1=exp(−ihbn·σ)Yn=
(
cos(hbn)I−i
sin(hbn)
hbn
bn·σ
)
Yn (274)
withbn≡b(tn+h/2)andbn=‖bn‖.Thetrapezoidalruleisequallyvalidbyconsidering bn≡(b(tn)+b(tn+h))/2.
•Fourth-orderMagnus(M4).Usingthefourth-orderGauss–Legendreruletoapproximatetheintegralsandtaking h=2,
onehasthescheme (254)which,forthisproblem,reads
b1=b(tn+c1h), b2=b(tn+c2h),
d=
h
2
(b1+b2)−h2
√
3
6
i(b1×b2) (275)
Yn+1=exp(−ihd·σ)Yn
withc1= 1
2−
√
3
6 ,c2= 1
2+
√
3
6 (dottedlines).
Wechoose ξ = 0.3and ξ = 1,andeachnumericalintegrationiscarriedoutfordifferentvaluesof γ intherange
γ ∈[0,2π].Weplotthecorrespondingapproximationstothetransitionprobabilityinasimilarwayasin Fig.7 forthe
analyticaltreatment.Thusweobtaintheplotsof Fig.14.Asexpected,theperformanceofthemethodsdeterioratesas γ
increases.Notice,also,thatthequalitativebehaviorofthedifferentnumericalschemesisquitesimilarasthatexhibited
bytheanalyticalapproximations.EulerandRunge–Kuttamethodsdonotpreserveunitarityandmayleadtotransition
probabilitiesgreaterthan1(justlikethestandardperturbationtheory).Ontheotherhand,forsufficientlysmallvaluesof
γ(insidetheconvergencedomainoftheMagnusseries)thefourth-orderMagnusmethodimprovestheresultachievedby
thesecond-order,whereasforlargevaluesof γ,ahigherordermethoddoesnotnecessarilyleadtoabetterapproximation.
S.Blanesetal./PhysicsReports470(2009)151–238 209
Fig.14. Rosen–Zenermodel:Transitionprobabilitiesasafunctionof γ,with ξ=0.3and ξ=1.Thecurvesarecodedasfollows.Solidlinerepresentsthe
exactresult;E1:solidlineswithsquares;RK4:solidlineswithtriangles;M2:dashedlines;M4:dashed-brokenlines(indistinguishablefromexactresult
inleftpanel).
Fig.15. Rosen–Zenermodel:Transitionprobabilitiesasafunctionof ξ,with γ=2and γ=5.Linesarecodedasin Fig.14.
InFig.15werepeattheexperiment,nowtaking γ=1and γ=2,andfordifferentvaluesof ξ.Inthefirstcase,onlythe
Eulermethoddiffersconsiderablyfromtheexactsolution,andinthesecondcasethishappensforbothRKmethods.
Toincreasetheaccuracy,onecanalwaystakesmallertimesteps,butthenthenumberofevaluationsof A(t)increases,
andthismaybecomputationallyveryexpensiveforsomeproblemsduetothecomplexityofthetimedependenceand/or
thesizeofthematrix.Inthosecases,itisimportanttohavereliablenumericalmethods,providingthedesiredaccuracyas
fastaspossibleor,alternatively,leadingtothebestpossibleaccuracyatagivencomputationalcost.
Agoodperspectiveoftheoverallperformanceofagivennumericalintegratorisprovidedbytheso-calledefficiency
diagram.Thisefficiencyplotisobtainedbycarryingoutthenumericalintegrationwithdifferenttimesteps,corresponding
todifferentnumbersofevaluationsof A(t).Foreachrun,onecomparesthecorrespondingapproximationwiththeexact
solution,andplotstheerrorasafunctionofthetotalnumberofmatrixevaluations.Theresultsarebetterillustratedina
doublelogarithmicscale.Inthatcase,theslopeofthecurvesshouldcorrespond,inthelimitofverysmalltimesteps,to
(minus)theorderofaccuracyofthemethod.
Toillustratethisissue,in Fig.16 wecollecttheefficiencyplotsofthepreviousschemeswhen ξ= 0.3with γ = 10
(left)and γ = 100(right).Wehavealsoincludedtheresultsobtainedbyseveralhigherorderintegrators,namelythe
sixth-orderRKmethod(RK6)whosecoefficientsarecollectedin (229)andthesixth-orderMagnusintegrator(M6)given
210 S.Blanesetal./PhysicsReports470(2009)151–238
Fig.16. Rosen–Zenermodel:ErrorinthetransitionprobabilitiesversusthenumberofevaluationsoftheHamiltonian HI(s)forξ=0.3and γ=10(left
panel)and γ=100(rightpanel).
by(251)and(257).WeclearlyobservethattheEulermethodis,byfar,theworstchoiceifaccurateresultsaredesired.
Noticethe(double)logarithmicscaleoftheplots:thus,forinstance,when γ = 10therangegoesapproximatelyfrom
300to3000evaluationsof A(t).Magnusintegrators,inadditiontoprovidingresultsinSU (2)byconstruction(astheexact
solution),showabetterefficiencythanRunge–Kuttaschemesfortheseexamples,andthisefficiencyincreaseswiththevalue
ofγconsidered.TheimplicitRunge–Kutta–Gauss–Legendremethods (237)showslightlybetterresultsthantheexplicitRK
methods,butstillconsiderablyworsethanMagnusintegrators.
IfwecompareMagnusintegratorsofdifferentordersofaccuracy,weobservethatthemostefficientschemeisthesecond
ordermethodM2whenrelativelylowaccuraciesaredesired.Forhigheraccuracy,however,itisnecessarytocarryouta
thoroughanalysisofthecomputationalcostofthemethodsforagivenproblembeforeassertingtheconvenienceofM4
orM6withrespecttohigherorderschemes.Forafixedtimestep h,thecomputationalcostofacertainfamilyofmethods
(suchasthosebasedonMagnus)usuallyincreaseswiththeorder.However,ifonefixesthenumberof A(t)evaluations,this
isnotnecessarilythecase(sometimeshigherordermethodsrequiremorecommutatorsbutlessexponentials).
LetusnowcomparetheperformanceoftheMagnusmethodswithrespecttootherLie-groupsolvers,namelyFerand
Cayleymethods.Werepeatthesameexperimentsasin Fig.16but,forclarity,onlytheresultsforthe6th-ordermethodsare
shown.Weconsiderthesymmetric-Fermethodgivenby (265)and(267)andtheCayleymethod (268)with(271),usingin
bothcasestheGauss–Legendrequadrature.Theresultsobtainedarecollectedin Fig.17.Weclearlyobservethattherelative
performanceoftheCayleymethoddeterioratesbyincreasingthevalueof γsimilarlytotheRK6.Inspiteofpreservingthe
qualitativeproperties,thisexampleshowsthatforsomeproblems,polynomialorrationalapproximationsdonotperform
efficiently.Here,inparticular,theMagnusschemeisslightlymoreefficientthanthesymmetricFermethod,althoughfor
otherproblemstheirperformanceisquitesimilar.
5.6. Computingtheexponentialofamatrix
WehaveseenthatthenumericalschemesbasedontheMagnusexpansionprovideexcellentresultswhenappliedtoEq.
(223)withcoefficientmatrix (272).Infact,theyareevenmoreefficientthanseveralRunge–Kuttaalgorithms.Ofcourse,
forthisparticularexample,thenumberof A(t)evaluationsisagoodindicationofthecomputationalcostrequiredbythe
numericalschemes,sincetheevaluationofexp (Ω)canbedoneanalyticallybymeansofformula (18).Ingeneral,however,
thematrixexponentialalsohastobeapproximatednumerically,andthustheperformanceofthenumericalintegration
algorithmsbasedontheMagnusexpansionstronglydependsonthisfact.Itmaybethattheevaluationofexp (C),where C
isa(realorcomplex) N×Nmatrix,representsthemajorfactorintheoverallcomputationalcostrequiredbythisclassof
algorithmsandisprobablyoneofthemostproblematicaspects.
Asamatteroffact,theapproximationofthematrixexponentialisamongtheoldestandmostextensivelyresearched
topicsinnumericalmathematics.Althoughmanyefficientalgorithmshavebeendeveloped,theproblemisstillfarfrom
beingsolvedingeneral.Itseems,then,reasonabletobrieflysummarizehere,someofthemostwidelyusedproceduresin
thiscontext.
Letusbeginwithtwoobviousbutimportantremarks.(i)First,onehastodistinguishwhetheritisnecessaryto
evaluatethefullmatrixexp (C)oronlytheproductexp (C)vforsomegivenvector v.Inthelattercase,specialalgorithms
canbedesigned,requiringamuchreducedcomputationaleffort.Thisisespeciallytruewhen C islargeandsparse
S.Blanesetal./PhysicsReports470(2009)151–238 211
Fig.17. Rosen–Zenermodel:Sameas Fig.16wherewecomparetheperformanceofthe6th-orderMagnus,symmetric-Fer,CayleyandRK6.
(asoftenhappenswithmatricesarisingfromthespatialdiscretizationofpartialdifferentialequations).(ii)Second,for
thenumericalintegrationmethodsbasedonME,onehastocomputeexp (C(h)),whereC(h)= O(hp),hisa(nottoolarge)
stepsizeand p≥1.Inotherwords,thematricestobeexponentiatedtypicallyhaveasmallnorm(usuallyrestrictedbythe
convergenceboundsoftheexpansion).
Inanycase,priortothecomputationofexp (C),itisimportanttohaveasmuchinformationabouttheexponent Cas
possible.Thus,forinstance,ifthematrix CresidesinaLiealgebra,thenexp (C)belongstothecorrespondingLiegroup
andonehastodecidewhetherthisqualitativepropertyhastobeexactlypreserved,orifconstructingasufficientlyaccurate
approximation(e.g.,atahigherorderthantheorderoftheintegratoritself)isenough.Also,when Ccanbesplitintodifferent
parts,onemayconsiderafactorizationoftheformexp (C)≈exp(C1)exp(C2)··· exp(Cm)ifeachindividualexponentialis
easytoevaluateexactly.
An important reference in this context is [138] and its updated version [139], where up to nineteen (or twenty
in[139])differentnumericalalgorithmsforcomputingtheexponentialofamatrixarecarefullyreviewed.Anextensive
softwarepackageforcomputingthematrixexponentialisExpokit,developedbyR.Sidje,withFortranandMatlabversions
available[140,141].Inadditiontocomputingthematrix-valuedfunctionexp (C)forsmall,densematrices C,Expokithas
functionsforcomputingthevector-valuedfunctionexp (C)vforbothsmall,densematricesandlarge,sparsematrices.
5.6.1. ScalingandsquaringwithPadéapproximation
Amongoneoftheleastdubiouswaysofcomputingexp (C)isbyscalingandsquaringincombinationwithadiagonal
Padéapproximation[139].Theprocedureisbasedonafundamentalpropertyoftheexponentialfunction,namely
eC=(eC/j)j
foranyinteger j.Theidea,then,istochoose jtobeapoweroftwoforwhichexp (C/j)canbereliablyandefficientlycomputed,
andthentoformthematrix (exp(C/j))jbyrepeatedsquaring.Iftheinteger jischosenasthesmallestpoweroftwoforwhich
‖C‖/j<1,thenexp (C/j)canbesatisfactorilycomputedbydiagonalPadéapproximantsoforder,say, m.Thisisroughlythe
methodusedbythebuilt-infunction expminMatlab.
FortheintegratorsbasedontheMagnusexpansion,as C= O(hp)withp≥1,oneusuallygetsgoodapproximations
withrelativelysmallvaluesof jandm.
Asiswellknown,diagonalPadéapproximantsmaptheLiealgebrao J(n)tothe J-orthogonalLiegroupO J(n)andthus
alsoconstituteavalidalternativetotheevaluationoftheexponentialmatrixinMagnus-basedmethodsforthisparticular
Liegroup.Morespecifically,if B∈oJ(n),then ψ2m(tB)∈OJ(n)forsufficientlysmall t∈ R,with
ψ2m(λ)=
Pm(λ)
Pm(−λ), (276)
providedthepolynomials Pmaregeneratedaccordingtotherecurrence
P0(λ)=1, P1(λ)=2+λ
Pm(λ)=2(2m−1)Pm−1(λ)+λ2Pm−2(λ).
212 S.Blanesetal./PhysicsReports470(2009)151–238
Moreover,ψ2m(λ)=exp(λ)+ O(λ2m+1)andψ2correspondstotheCayleytransform (262),whereasfor m=2,3wehave
ψ4(λ)=
(
1+
1
2
λ+
1
12
λ2
)/(
1−
1
2
λ+
1
12
λ2
)
ψ6(λ)=
(
1+
1
2
λ+
1
10
λ2+
1
120
λ3
)/(
1−
1
2
λ+
1
10
λ2−
1
120
λ3
)
.
Thus,wecancombinetheoptimizedapproximationsto ΩobtainedinSection 5.4forMagnusbasedmethodswithdiagonal
Padéapproximants,uptothecorrespondingorder,toobtaintime-symmetricintegrationschemespreservingthealgebraic
structureoftheproblemwithoutcomputingthematrixexponential.Forinstance,the‘‘Magnus–Padé’’methodsthus
obtainedinvolve,inadditiontoonematrixinversion,3and8matrix–matrixproductsfororder4and6,respectively.
Observethatsince Ω[2n]= O(h)then
ψ2m(Ω[2n])=exp(Ω[2n])+ O(h2k+1),
wherek=min{m,n}.Withm=nwehaveamethodoforder2 n.However,forsomeproblems,thisrationalapproximation
totheexponentialmaybenotveryaccuratedependingontheeigenvaluesof Ω[2n].Inthiscase,onemaytake m>n,thus
givingabetterapproximationtotheexponentialandamoreaccurateresultbyslightlyincreasingthecomputationalcost
ofthemethod.Ofcourse,whenthenormofthematrix Ω[2n]isnotsosmall,thistechniquecanbecombinedwithscaling
andsquaring[142].
InsteadofusingPadéapproximantsfortheexponentialofthescaledmatrix B≡C/2k,NajfeldandHavel[ 143]propose
arationalapproximationforthematrixfunction
H(B)=Bcoth(B)=B
e2B+I
e2B−I
, (277)
fromwhichtheexponentialcanbeobtainedas
e2B=
H(B)+B
H(B)−B
andtheniterativelysquaretheresult ktimestorecovertheexponentialoftheoriginalmatrix C.Fromthecontinuedfraction
expansionofH(B),itispossibletocomputethefirstrationalapproximationsas
H2(B)=
I+ 2
5B2
I+ 1
15B2
, H4(B)=
I+ 4
9B2+ 1
63B4
I+ 1
9B2+ 1
945B4
andsoon.Observethattherepresentation (277)canberegardedasageneralizedCayleytransformof Bandthusitalso
providesapproximationsinthegroupO J(n).In[ 143]theauthorsreportasavingofabout30%inthenumberofmatrix
multiplicationswithrespecttodiagonalPadéapproximantswhenanoptimal kandarationalapproximationfor H(B)is
used.
5.6.2. Chebyshevapproximation
Anothervalidalternativeistousepolynomialapproximationstotheexponentialof Casawhole.Suppose,inparticular,
thatCisamatrixoftheform C = −iτH,with HHermitianand τ > 0,asisthecaseinQuantumMechanics.Inthe
Chebyshevapproach,theevolutionoperatorexp (−iτH)isexpandedinatruncatedseriesofChebyshevpolynomials,in
analogywiththeapproximationofascalarfunction[ 144].Asiswellknown,givenafunction F(x)intheinterval[−1,1],the
Chebyshevpolynomialapproximationsareoptimal,inthesensethatthemaximumerrorintheapproximationisminimal
comparedtoalmostallpossiblepolynomialapproximations[ 145].Toapplythisprocedure,onehastopreviouslyboundthe
extremeeigenvalues EminandEmaxofH.ThenatruncatedChebyshevexpansionofexp (−ix)ontheinterval [τEmin,τEmax]
isconsidered:
exp(−ix)≈
m∑
n=0
cnPn(x),
where
Pn(x)=Tn
(
2x−τEmax−τEmin
τEmax−τEmin
)
withappropriatelychosencoefficients cn.HereTn(x)aretheChebyshevpolynomialsontheinterval [−1,1][45],whichcan
bedeterminedviatherecurrencerelation
Tn+1(x)=2xTn(x)−Tn−1(x); T1(x)=x; T0(x)=1.
Finally,oneusestheapproximation
exp(−iτH)≈
m∑
n=0
cnPn(τH). (278)
S.Blanesetal./PhysicsReports470(2009)151–238 213
Thistechniqueisfrequentlyusedinnumericalquantumdynamicstocomputeexp (−iτH)ψ0oververylongtimes.Thiscan
bedonewith mmatrix-vectorproductsiftheapproximation (278)isconsideredwithasufficientlylargetruncationindex m.
Infact,thedegree mnecessaryforachievingaspecificaccuracydependslinearlyonthestepsize τandthespectralradiusof
H[146],andthusanincreaseofthestepsizereducesthecomputationalworkperunitstep.Inapracticalimplementation,
mcanbechosensuchthattheaccuracyisdominatedbytheround-offerror[ 147].Thisapproachhastwomaindrawbacks:
(i)itisnotunitary,andthereforethenormisnotconserved(althoughthedeviationfromunitarityisreallysmallduetoits
extremeaccuracy),and(ii)intermediateresultsarenotobtained,since,typically, τisverylarge.
5.6.3. Krylovspacemethods
Aswehavealreadypointedout,veryoftenwhatisreallyrequired,ratherthantheexponentialofthematrix Citself,
isthecomputationofexp (C)appliedtoavector.Inthissituation,evaluatinge Cissomehowanalogoustocomputing C−1
togetthesolutionofthelinearsystemofequations Cx=bformanydifferent b’s:otherproceduresareclearlyfarmore
desirable.Thecomputationofe CvcanbeefficientlydonewithKrylovsubspacemethods,inwhichapproximationstothe
solutionareobtainedfromtheKrylovspacesspannedbythevectors {v,Cv,C2v,..., Cjv}forsomejthatistypicallysmall
comparedtothedimensionof C[148,149].TheLanczosmethodforsolvingiterativelysymmetriceigenvalueproblemsisof
thisform[ 150].If,asbefore,welet C=−iτH,thesymmetricLanczosprocessrecursivelygeneratesanorthonormalbasis
Vm=[v1··· vm]ofthemthKrylovsubspace Km(H,u)=span(u,Hu,..., Hm−1u)suchthat
HVm=VmLm+[0··· 0βmvm+1],
wherethesymmetrictridiagonal m×mmatrixLm=VT
mHVmistheorthogonalprojectionof HontoKm(H,u).Finally,
exp(−iτH)u≈Vmexp(−iτLm)VT
mu
andthematrixexponentialexp (−iτLm)canbecomputedbydiagonalizing Lm,Lm=QmDmQT
m,as
exp(−iτLm)=Qmexp(−iτDm)QT
m,
withDmadiagonalmatrix.Thisiterativeprocessisstoppedwhen
βm
‖‖(exp(−iτLm))m,m
‖‖<tol
forafixedtolerance.Verygoodapproximationsareoftenobtainedwithrelativelysmallvaluesof m,andcomputable
errorboundsexistfortheapproximation.Thisclassofschemesgenerallyrequire O(N2)floatingpointoperationsinthe
computationofe Cv.Moredetailsarecontainedinthereferences[ 151–153].
5.6.4. Splittingmethods
Frequently,onehastoexponentiateamatrixwhichcanbesplitintoseveralpartswhichareeithersolvableoreasyto
dealwith.Letusassumeforsimplicitythat C=A+B,wherethecomputatione Cisveryexpensive,bute AandeBarecheap
andeasytoevaluate.Insuchcircumstances,itmakessensetoapproximatee εCwithε,asmallparameter,bythefollowing
scheme:
ψ[p]
h ≡eεbmBeεamA··· eεb1Beεa1A=eε(A+B)+ O(εp+1) (279)
withappropriateparameters ai,bi.Thiscanbeseenastheapproximationstothesolutionat t = εoftheequation
Y′ = (A+B)Ybyacompositionoftheexactsolutionsoftheequations Y′ = AYandY′ = BYattimes t = aiεand
t=biε,respectively.TwoinstancesofthiskindofapproximationaregivenbythewellknownLie–Trotterformula
ψ[1]
h =eεAeεB (280)
andthesecondordersymmetriccomposition
ψ[2]
h =eεA/2eεBeεA/2, (281)
referredtoasStrangsplitting,Störmer,Verletandleap-frog,dependingontheparticularareawhereitisused.
Splittingmethodshavebeenconsideredindifferentcontexts:indesigningsymplecticintegrators,forconstructing
volume-preservingalgorithms,inthenumericalintegrationofpartialdifferentialequationsetc.Anextensivesurveyofthe
theoryandpracticeofsplittingmethodscanbefoundin[ 154,79,127–129]andreferencestherein.
Splittingmethodsareparticularlyusefulingeometricnumericalintegration.Supposethatthematrix C=A+Bresides
inaLiealgebra g.Then,obviously,exp (C)belongstothecorrespondingLiegroup Gandoneisnaturallyinterestedinalso
gettingapproximationsin G.Inthisrespect,noticethatif A,B∈ g,thenthescheme (279)alsoprovidesanapproximation
in G.Itisworthnoticingthatothermethodsfortheapproximationofthematrixexponential(e.g.,Padéapproximantsand
Krylovsubspacetechniques)arenotguaranteedtomapelementsfrom gto G.AlthoughdiagonalPadéapproximantsmap
theLiealgebrao Jtotheunderlyinggroup,itispossibletoshowthattheonlyanalyticfunctionthatmaps sl(n)intothe
speciallineargroupSL (n)approximatingtheexponentialfunctionuptoagivenorder,istheexponentialitself[ 155].In
consequence,diagonalPadéapproximantsonlyprovideresultsinSL (n)ifthecomputationisaccuratetomachineprecision.
214 S.Blanesetal./PhysicsReports470(2009)151–238
In[156],CelledoniandIserlesdevisedasplittingtechniqueforobtaininganapproximationtoexp (C)intheLiegroup G
basedonadecompositionof C∈ gintolow-rankmatrices Ci∈ g.Basically,givena n×nmatrixC∈ g,theyproposedto
splititintheform
C=
k∑
i=1
Ci,
suchthat
(1)Ci∈ g,for i=1,..., k.
(2)Eachexp(Ci)iseasytoevaluateexactly.
(3)Productsofsuchexponentialsarecomputationallycheap.
Forinstance,fortheLiealgebra so(n),thechoice
Ci=
1
2
cieT
i−
1
2
eibT
i, i=1,..., n,
wherec1,..., cnarethecolumnsof Candeiisthei-thvectorofthecanonicalbasisof Rn,satisfiestheaboverequirements
(withk=n),whereasinthecaseof g= sl(n)other(moreinvolved)alternativesarepossible[ 156].
Proceedingasin (280),with
ψ[1]=exp(εC1)exp(εC2)··· exp(εCk)
wegetanorderoneapproximationin εtoexp(εC),whereasthesymmetriccomposition
ψ[2]=e
1
2εCke
1
2εCk−1··· e
1
2εC2eεC1e
1
2εC2··· e
1
2εCk−1e
1
2εCk (282)
providesanapproximationofordertwoin ε,andthiscanbesubsequentlycombinedwithdifferenttechniquesforincreasing
theorder.
Withrespecttothecomputationalcost,theresultsreportedin[ 156]showthat,uptoorderfourin ε,thisclassof
splittingschemesiscompetitivewiththeMatlabbuilt-infunction expmwhenmachineaccuracyisnotrequiredinthefinal
approximation.Running expmonrandomlygeneratedmatrices,itispossibletoverifythatcomputingexp (C)tomachine
accuracyrequiresabout(20–30) n3floatingpointoperations,dependingontheeigenvaluesof C,whereasthe4th-order
methodconstructedfrom (282)involves(12–15)n3operationswhen C∈ so(100)[156].Inthecaseoftheapproximation
ofexp(C)vandv∈ Rn,thecostoflow-ranksplittingmethodsdropdownto Kn2,where Kisaconstant,andthustheyare
comparabletothoseachievedbypolynomialapproximants[ 153].
Splittingmethodsoftheabovetypearebynomeanstheonlywaytoexpressexp (C)asaproductofexponentialsof
elementsin g.Forinstance,theWei–Normanapproach (111)canalsobeimplementedinthissetting.Supposethatdim g=s
andlet{X1,X2,..., Xs}beabasisof g.Inthatcase,aswehaveseen(Section 2.10.3),itispossibletorepresentexp (tC)for
C∈ gandsufficientlysmall |t|incanonicalcoordinatesofthesecondkind,
etC=eg1(t)X1eg2(t)X2··· egs(t)Xs,
wherethescalarfunctions gkareanalyticat t=0.Althoughthe gksareimplicitlydefined,theycanbeapproximatedby
Taylorseries.ThecostoftheprocedurecanbegreatlyreducedbyadequatelychoosingthebasisandexploitingtheLie-
algebraicstructure[157].
Yetanotherproceduretogetapproximationsofexp (C)inaLie-algebraicsetting,whichhasreceivedconsiderable
attentionduringthelastyears,isbasedongeneralizedpolardecompositions(GPD),anapproachintroducedin[ 158]and
furtherelaboratedin[ 159,160].Inparticular,in[ 159],bybringingtogetherGPDwithtechniquesfromnumericallinear
algebra,newalgorithmsarepresentedwithcomplexity O(n3),bothwhentheexponentialisappliedtoavectorandto
amatrix.ThisiscertainlynotcompetitivewithKrylovsubspacemethodsinthefirstcase,butrepresentsatleasta50%
improvementontheexecutiontime,dependingontheLiealgebraconsidered,inthelatter.Anotherdifferencewithrespect
toKrylovmethodsisthatthealgorithmsbasedongeneralizedpolardecompositionsapproximatetheexponentialtoagiven
orderofaccuracyand,thus,theyarewellsuitedtoexponentialapproximationswithinnumericalintegratorsforODEs,
sincetheerrorissubsumedinthatoftheintegrationmethod.Foracompletedescriptionoftheprocedureanditspractical
implementation,wereferthereaderto[ 159].
5.7. Additionalnumericalexamples
ThepurposeofSection 5.5wastoillustratethemainfeaturesofthenumericalschemesbasedontheMagnusexpansion
incomparisonwithotherstandardintegrators(suchasRunge–Kuttaschemes)andotherLie-groupmethods(e.g.,Ferand
Cayley)onasolvablesystem.Forlargersystemstheefficiencyanalysisismorechallengingsincethe(exactorapproximate)
computationofexponentialmatricesplayanimportantroleontheperformanceofthemethods.Itmakessense,then,to
analyzefromthispointofview,morerealisticproblems,whereonenecessarilyhastoapproximatetheexponentialina
consistentway.
S.Blanesetal./PhysicsReports470(2009)151–238 215
Fig.18. Efficiencydiagramcorrespondingtotheoptimized4-th(circles)and6-th(squares)orderLie-groupsolversbasedonMagnus(solidlines)and
Cayley(brokenlines),andthestandardRunge–Kuttamethods(dashedlines).
Asanillustrationofthissituation,wenextconsidertwoskew-symmetricmatrices, A(t)andY(0)=I,sothatthesolution
Y(t)ofY′=A(t)Yisorthogonalforall t.Inparticular,theuppertriangularelementsofthematrices A(t)areasfollows:
(a) Aij=sin
(
t(j2−i2)
)
1≤i<j≤N (283)
(b) Aij=log
(
1+t
j−i
j+i
)
(284)
withN=10.Inbothcases Y(t)oscillateswithtime,mainlyduetothetime-dependenceof A(t)(in(283))orthenormof
theeigenvalues(in (284)).
Theintegrationiscarriedoutintheinterval t∈[ 0,10]andtheapproximatesolutionsarecomparedwiththeexact
oneatthefinaltime tf=10(obtainedwithveryhighaccuracybyusingasufficientlysmalltimestep).Thecorresponding
errorat tfiscomputedfordifferentvaluesofthetimestep h.TheLie-groupsolversareimplementedwithGauss–Legendre
quadraturesandconstantstepsize.
First,weplottheaccuracyofthedifferent4-thand6-thordermethodsasafunctionofthenumberof A(t)evaluations.
Incontrasttothepreviousexamples,nowthereisnoclosedformulaforthematrixexponentialsappearingintheMagnus
basedintegrators,sothatsomealternativeproceduremustbeapplied.Inparticular,thecomputationofe Ctomachine
accuracyisdonebyscaling–(diagonalPadé)–squaring,sothattheresultiscorrectuptoround-off. Fig.18showstheresults
obtainedfortheproblems (283)and(284)withfourth-andsixth-ordernumericalschemesbasedonMagnusandCayley,
andalsoexplicitRunge–Kuttamethods.Inthefirstproblem,MagnusandCayleyshowaverysimilarperformance,which
happenstobeonlyslightlybetterthanthatofRKmethods.
Thesituationchangesdrastically,however,forthesecondproblem.HerethebehaviorofCayleyandRKmethodsis
essentiallysimilar,whereasschemesbasedonMagnusareclearlymoreefficient.ThereasonseemstobethatCayleyandRK
methodsgivepoorapproximationstotheexponential,which,ontheotherhand,hastobeaccuratelyapproximated,since
theeigenvaluesof A(t)maytakelargevalues.
WithrespecttosymmetricFermethods,theirefficiencyisquitesimilartothatofMagnusifthematrixexponentialsare
evaluatedaccuratelyuptomachineprecision.Thisissoforthematrix (283)evenifPadéapproximantsofrelativelylow
orderareusedtoreplacetheexponentials.
Ontheotherhand,theefficiencyof‘‘Magnus–Padé’’methods(wedenotebyMP nmaMagnusmethodoforder nwhere
theexponentialisapproximatedbyadiagonalPadéoforder m,andMP nifn=m)ishighlydeterioratedfortheproblem
(284),althoughitisalwaysbetterthanthatcorrespondingtoCayleyschemes.
Tobetterillustrateallthesecomments,in Fig.19 wedisplaytheerrorinthesolutioncorrespondingto (283)and(284)
asafunctionoftimeintheinterval t∈[0,100]forh=1/20,asisobtainedbythepreviousmethods.Weshouldstressthat
allschemesrequirethesamenumberof Aevaluations.
Intherightpicture,theexponentialsappearingintheMagnusmethodarecomputedusingaPadéapproximantoforder
six(MP6),ofordereight(MP68)andtomachineaccuracy(M6).Observethegreatimportanceofevaluatingtheexponential
asaccuratelyaspossibleforthematrix (284):byslightlyincreasingthecomputationalcostperstepinthecomputationof
thematrixexponential,itispossibletodramaticallyimprovetheaccuracyofthemethods.Onthecontrary,forproblem
(283)themeaningfulfactseemstobethattheintegrationschemeprovidesasolutioninthecorrespondingLiegroup.
216 S.Blanesetal./PhysicsReports470(2009)151–238
Fig.19. Errorasafunctionoftime(inlogarithmicscale)obtainedwithdifferent6-thorderintegratorsfor h=1/20:(a)problem (283);(b)problem (284).
5.8. ModifiedMagnusintegrators
5.8.1. Variationsonthebasicalgorithm
TheexamplescollectedinSections 5.5and5.7showthatthenumericalmethodsconstructedfromtheMagnusexpansion
canbe,computationally,veryefficientindeed.Itisfairtosay,however,thatthisefficiencycanbeseriouslyaffectedwhen
dealingwithcertaintypesofproblems.
Suppose,forinstance,thatonehastonumericallyintegrateaproblemdefinedinSU (n).AlthoughMagnusintegrators
areunconditionallystableinthissetting(sincetheypreserveunitarityuptoround-off,independentlyofthestepsize h),in
practiceonlysmallvaluesof hareusedforachievingaccurateresults.Otherwisetheconvergenceoftheseriesisnotassured.
Ofcourse,theuseofsmalltimestepsmayrenderthealgorithmexceedinglycostly.
Inotherapplications,theproblemdependsonseveralparameters,sothattheintegrationhastobecarriedoutfor
differentvaluesoftheparameters.Inthatcase,theoverallintegrationprocedurecanbecomputationallyveryexpensive.
Inviewofallthesedifficulties,itishardlysurprisingthatseveralmodificationsofthestandardalgorithmofMagnus
integratorshadbeendevelopedtotrytominimizetheseundesirableeffectsandgetspeciallyadaptedintegratorsfor
particularproblems.
Onebasictool,usedtimeandagaininthiscontext,isperformingapreliminarylineartransformation,similarlytothose
introducedinSection 2.9.Thesetransformationscanbecarriedouteitherforthewholeintegrationintervalorateachstep
intheprocess.Givenanappropriatelychosentransformation, ˜Y0(t),onefactorizes Y(t)=˜Y0(t)˜Y1(t),wheretheunknown
˜Y1(t)satisfiestheequation
˜Y′
1=B(t)˜Y1 (285)
andB(t)dependson A(t)and˜Y0(t).Thistransformationmakessense,ofcourse,if ‖B(t)‖<‖A(t)‖andthustypically ˜Y0is
choseninsuchawaythatthenormof Bverifiestheaboveinequality.Asaconsequence,Magnusintegratorscanbeapplied
on(285)withlargertimestepsalsoprovidingmoreaccurateresults.
Alternatively,forproblemswhere,inadditiontothetimestep hthereisanotherparameter( E,say),onemayanalyzethe
Magnusexpansionintermsof handE.Thisallowsustoidentifywhichtermsateachorderintheseriesexpansiongivethe
maincontributiontotheerror,andtodesignmethodswhichincludethesetermsintheirformulation.Theresultingschemes
shouldthenprovidemoreaccurateresultsatamoderatecomputationalcostwithoutalteringtheconvergencedomain.As
ageneralrule,itisalwaysdesirabletohave,inadvance,asmuchinformationabouttheequationandthepropertiesofits
solutionaspossible,andthentotrytoincorporateallthisinformationintothealgorithm.
Letusreviewsomeusefulpossibilitiesinthiscontext.From (241)onehas
A(t)=a0+τa1+τ2a2+··· , (286)
whereτ = t−t1/2.Thefirsttermisexactlysolvable( a0= A(t1/2))and,formanyproblems,itjustprovidesthemain
contributiontotheevolutionofthesystem.Inthatcase,itmakessensetotake
˜Y0(t)=e(t−tn)a0=e(t−tn)A(t1/2)
S.Blanesetal./PhysicsReports470(2009)151–238 217
andsubsequentlyintegrateEq. (285)with
B(t)=e−(t−tn)A(t1/2)(
A(t)−A(t1/2)
)
e(t−tn)A(t1/2).
Thisapproachhasbeenconsideredin[ 161,162],andshowsanextraordinaryimprovementwhenthesystemishighly
oscillatoryandthemainoscillatorypartisintegratedwith ˜Y0.Inthosecases,thenormof B(t)isconsiderablysmallerthan
‖A(t)‖,butB(t)isstillhighlyoscillatory,sothatspeciallyadaptedquadratureruleshavetobeusedinconjunctionwiththe
Magnusexpansion[163,164].
Insomeotherproblems,thecontributionsfromthederivativescanalsobesignificant,sothatamoreappropriate
transformationisdefinedby
˜Y0(t)=exp
(∫ t
tn
A(τ)dτ
)
. (287)
Theresultingmethodscanbeconsidered,then,asacombinationoftheFerorWilcoxexpansionsandtheMagnusexpansion.
Thisapproachhasbeenpursuedin[ 165].
Ontheotherhand,itisknownthatseveralphysicallyrelevantsystemsevolveadiabaticallyoralmost-adiabatically.In
thatcase,itseemsappropriatetoconsidertheadiabaticpicturewhichinstantaneouslydiagonalizes A(t)(Section2.9).This
analysisiscarriedoutin[ 166–168].In[ 167]theadiabaticpictureisusedperturbatively,whereasin[ 166]itisshownthat
Magnusinthenewpictureleadstosignificantimprovements.
Alternatively,onecananalyzethestructureoftheleadingerrortermsinordertoidentifythemaincontributionto
theerrorateach ΩiintheMagnusseriesexpansion.Inmostcases,theycorrespondtotermsinvolvingonly α1andits
nestedcommutatorswith α2.Thus,inparticular,thestandardfourth-ordermethodgivenby (243)canbeeasilyimproved
byincludingthedominanterrortermathigherorders,i.e.,
Ω[4]=α1−
1
12
[α1,α2]+
1
720
[α1,α1,α1,α2]−
1
30240
[α1,α1,α1,α1,α1,α2]+··· .
Werecallthatusingthefourth-orderGauss–Legendrequadraturerulewecantake α1= h
2(A1+A2), α2= h
√
3
12 (A2−A1)
withA1,A2givenin(252).Thenewmethodrequiresadditionalcommutatorsbuttheaccuracycanbeimprovedagooddeal.
Thisprocedureisanalyzedin[ 70],whereitisshownhowtosumupalltermsoftheform [α1,α1,...,α 1,α2].Anerror
analysisinthelimitofverylargevaluesof ‖α1‖isdonein[ 169,170].
5.8.2. Commutator-freeMagnusintegrators
AllnumericalmethodsbasedontheMagnusexpansionappearingintheprecedingsectionsrequiretheevaluation
ofamatrixexponentialwhichcontainsseveralnestedcommutators.Aswehaverepeatedlypointedout,computingthe
exponentialisfrequentlythemostconsumingpartofthealgorithm.Thereareproblemswherethematrix A(t)hasa
sufficientlysimplestructurewhichallowsonetoefficientlyapproximatetheexponentialexp (A(ti)),ortheexponential
ofalinearcombinationofthematrix A(t)evaluatedatdifferentpoints.Insomesense,thisisequivalenttohavingefficient
methodstocomputeortoapproximate ˜Y0in(287).Itmaybe,however,thatthecomputationofthematrixexponentialis
amuchmoreinvolvedtaskduetothepresenceofcommutatorsintheMagnusexpansion.Forthisreason,itmakessense
tolookforapproximationstotheMagnusexpansionwhichdonotinvolvecommutators,whilststillpreservingthesame
qualitativeproperties.Inotherwords,onemaybeinterestedincompositionsoftheform
Ψ[n]
m ≡exp
(∫ tn+h
tn
pm(s)A(s)ds
)
··· exp
(∫ tn+h
tn
p1(s)A(s)ds
)
(288)
wherepi(s)arescalarfunctionschoseninsuchawaythat Ψ[n]
m =eΩ(tn+h)+ O(hn+1).Alternatively,insteadofthefunctions
pi(s),itispossibletofindcoefficients ϱi,j,i=1,..., m,j=1,..., ksuchthat
Ψ[n]
m ≡e˜Am··· e˜A1, with˜Ai=h
k∑
j=1
ϱi,jAj (289)
isanapproximationofthesameorder.Thisprocedurerequiresonefirsttocompute Aj= A(tn+cjh), j= 1,..., kfor
somequadraturenodes, cj,oforder norhigherand,obviously,thecoefficients ϱi,jwilldependonthischoice.Theprocess
simplifiesifoneworksintheassociatedgradedfreeLiealgebrageneratedby {αi},asinthesequelofEq. (242).Thus,achieving
fourth-orderintegratorsreducesjusttosolvetheequationsforthenewcoefficients ai,1,ai,2in
Ψ[4]
m ≡exp
(
am,1α1+am,2α2
)
··· exp
(
a1,1α1+a1,1α2
)
(290)
withtherequirementthat Ψ[4]
m =exp
(
Ω[4])
+O(h5),where Ω[4]isgivenby (243).Here,thedependenceof ai,1,ai,2on
thecoefficients ϱi,jisdeterminedthroughtheexistingrelationshipbetweenthe αiandthe Ajgivenin (250).Theorder
conditionsforthecoefficients ai,1,ai,2canbeeasilyobtainedfromtheBaker–Campbell–Hausdorffformula.Aswehave
218 S.Blanesetal./PhysicsReports470(2009)151–238
alreadymentioned,time-symmetryisanimportantpropertytobepreservedbytheintegrators,whereas,atthesametime,
italsosimplifiestheanalysis.Scheme (290)istime-symmetricif
am+1−i,1=ai,1, am+1−i,2=−ai,2, i=1,2,..., m (291)
inwhichcasetheorderconditionsatevenordertermsareautomaticallysatisfied.Asanillustration,thesimplecompositions
Ψ[4]
2 ≡exp
(
1
2
α1+
1
6
α2
)
exp
(
1
2
α1−
1
6
α2
)
(292)
Ψ[4]
3 ≡exp
(
1
12
α2
)
exp(α1)exp
(
−
1
12
α2
)
(293)
areinfactfourth-order(commutator-free)methodsrequiringtwoandthreeexponentials,respectively[ 171].Inparticular,
scheme(292),when α1,α2areapproximatedusingthefourth-orderGauss–Legendrequadratureasshownin (252)and
(253)leadstothescheme
Ψ[4]
2 ≡exp
(
h(ϱ2,1A1+ϱ2,2A2)
)
exp
(
h(ϱ1,1A1+ϱ1,2A2)
)
(294)
withϱ1,1=ϱ2,2= 1
2+
√
3
72,ϱ1,2=ϱ2,1= 1
2−
√
3
72.Methodscloselyrelatedtothescheme (293)arepresentedin[ 171–173],
wheretheyareappliedtotheSchrödingerequationwithatime-dependentpotential.Amethodquitesimilarto (292)is
analyzedin[ 174]throughitsapplicationtoparabolicinitialboundaryvalueproblems.Adetailedstudyoffourthandsixth
ordercommutator-freemethodsispresentedin[ 175].
Ontheotherhand,veryoftenthedifferentialequation (223)canbesplitintotwoparts,sothatonehas,instead,
Y′=(A(t)+B(t))Y, (295)
whereeachpartcanbetriviallyorveryefficientlysolved.Forinstance,theSchrödingerequationwithatime-dependent
potentialand,possibly,atime-dependentkineticenergybelongstothisclass.Inprinciple,thefollowingfamiliesof
geometricintegratorsarespeciallytailoredforthisproblem:
I-Thecommutator-freeMagnusintegrators (289),whichinthiscaseread
Ψ[n]
m ≡e˜Am+˜Bm··· e˜A1+˜B1, with˜Ai=h
k∑
j=1
ϱi,jAj,˜Bi=h
k∑
j=1
ϱi,jBj. (296)
Assumingthate ˜Aiande˜Biareeasilycomputed,theneachexponentialcanbeapproximatedbyaconvenientlychosen
splittingmethod(279)[128]
e˜Ai+˜Bi≃ebs˜Bieas˜Ai··· eb1˜Biea1˜Ai. (297)
II-Ifonetakesthetimevariablein A(t),B(t)astwonewcoordinates,onemayuseanysplittingmethodasfollows[ 176]:
Ψ[n]
l,h ≡eblhB(wl)ealhA(vl)··· eb1hB(w1)ea1hA(v1), (298)
with
vi=
i−1∑
j=1
bj, w i=
i∑
j=1
aj.
andb0=0,A(vi)≡A(tn+vih),B(wi)≡B(tn+wih).
Bothapproacheshaveprosandcons.ByapplyingprocedureIwemaygetmethodsoforder2 nwithonlynevaluationsof
A(t),B(t)using,forexample,Gauss–Legendrequadratures,butif min(296)islarge,thenumberofmatrixexponentialstobe
computedleadstoexceedinglycostlymethods.TheapproachII,ontheotherhand,hastheadvantageofasmallernumber
ofstages,butalsopresentstwodrawbacks:(i)manyevaluationsof A(t),B(t)arerequiredingeneral;(ii)formatrices Aand
Bwithaparticularstructure,therearespeciallydesignedsplittingmethodswhicharefarmoreefficient,buttheseschemes
arenoteasilyadaptedtothissituation.
Next,weshowhowtocombinesplittingmethodswithtechniquesleadingtocommutatorfreeMagnusschemes,to
designefficientnumericalalgorithmspossessingtheadvantagesofapproachesIandII,andatthesametimegeneralizing
thesplittingidea (279)tothissetting[ 177,178].
Thestartingpointissimilarasinpreviousschemes,i.e.weconsideracompositionoftheform
ψ[n]
l,h=e˜Ble˜Al··· e˜B1e˜A1, (299)
S.Blanesetal./PhysicsReports470(2009)151–238 219
Table1
Splittingmethodsoforder4forseparablenon-autonomoussystems.GS 6-4isintendedforgeneralseparableproblems,whereasMN 6-4canbeapplied
when[B(ti),[B(tj),[B(tk),A(tl)]]]= 0.Allthecoefficientsaregivenintermsof b11,a11,b21,a21,b31foreachmethod.
GS6-4 MN6-4
b11=0.0792036964311957 b11=0.0829844064174052
a11=0.209515106613362 a11=0.245298957184271
b21=0.353172906049774 b21=0.396309801498368
a21=−0.143851773179818 a21=0.604872665711080
b31=−0.0420650803577195 b31=−0.0390563049223486
a31=1/2−(a11+a21) b41=1−2(b11+b21+b31)
a41=a31 b51=b31
a51=a21 b61=b21
a61=a11 b71=b11
a12=(2a11+2a21+a31−2b11−2b21)/c b12=(2a11+2a21−2b11−b21)/d
a22=0 b22=(−2a11+b11)/d
a32=−a11/c b32=b42=0
a42=−a32 b52=−b32
a52=−a22 b62=−b22
a62=−a12 b72=−b12
c=12(a11+2a21+a31−2b11+2a11b11−2b21+2a11b21)
d=12(2a21−b11+2a11b11−2a21b11−b21+2a11b21)
wherethematrices ˜Aiand˜Biare
˜Ai=h
k∑
j=1
ρijAj, ˜Bi=h
k∑
j=1
σijBj, (300)
withappropriatelychosenrealparameters ρij,σijdependingonthecoefficientsofthechosenquadraturerule.Noticethat
e˜Aicanbeseenasthesolutionoftheinitialvalueproblem Y′=ˆAiY,Y(tn)=Iattn+1,where˜Ai=hˆAi.Ofcourse,thesame
considerationsapplytoe ˜Bi.
Inmanycasesitisconvenienttowritethecoefficients ρij,σijexplicitlyintermsofthecoefficients ci.Following[ 177]
theycanbewrittenas
ρij=
s∑
l=1
ai,l
(
R(s)Q(s,k)
X
)
lj
, σ ij=
s∑
l=1
bi,l
(
R(s)Q(s,k)
X
)
ij
. (301)
wherethecoefficientsforthematrices R(s), s= 2,3aregivenin (249)andfor Q(s,k)
X (whoseelementsdependonthe
coefficientsbi,ciforthequadraturerule)asshownin (246).
Inthisway,thecoefficients aijandbijareindependentofthequadraturechoiceandcanbeobtainedbysolvingsome
orderconditions(see[ 177]formoredetails).
Thisprocedureallowsustoseparatelyanalyzeparticularcasesforthematrices A,Binordertobuildefficientmethods.
Forinstance,in[ 177]thefollowingparticularcasesareconsidered:(i)whenthematrices A(t),B(t)haveageneralstructure;
(ii)whentheysatisfytheadditionalconstraint [B(ti),[B(tj),[B(tk),A(tl)]]]= 0asithappens,forinstance,if Acorresponds
tothekineticenergyand Btothepotentialenergy(bothinclassicalorquantummechanics).
Asanillustration,weconsiderthefollowing4th-order6-stageBABcomposition
ψ[4]
6,h=e˜B7e˜A6e˜B6··· e˜A1e˜B1. (302)
InTable1wecollectthecoefficients aij,bijtobeusedin (301)toobtainthecoefficients ρij,σijtobeusedinthescheme (302)
fortwomethods,denotedbyGS 6-4inthegeneralcase(whosecoefficients ai1,bi1correspondtoS6in[154])andMN 6-4when
[B(ti),[B(tj),[B(tk),A(tl)]]]= 0(thecoefficients ai1,bi1correspondtoSRKN b
6in[154]).
Finally,onehastowritetheschemeintermsofthematrices Ai,Bi.Forinstance,thecomposition (302)withthe4th-order
Gauss–Legendrequadrature(i.e.taking Q(2,2)in(247)andR(2)in(249)toobtainthecoefficients ρij,σijin(301))gives
˜Ai=
(
1
2
ai1−
√
3ai2
)
hA1+
(
1
2
ai1+
√
3ai2
)
hA2
˜Bi=
(
1
2
bi1−
√
3bi2
)
hB1+
(
1
2
bi1+
√
3bi2
)
hB2. (303)
220 S.Blanesetal./PhysicsReports470(2009)151–238
5.9. Magnusintegratorsfornonlineardifferentialequations
ThesuccessofMagnusmethodsappliedtothenumericalintegrationoflinearsystemshasmotivatedseveralattemptsto
adapttheschemesforsolvingtimedependentnonlineardifferentialequations.Forcompletenesswepresentsomerecently
proposedgeneralizationsofMagnusintegrators.Weconsidertwodifferentproblems:(i)anonlinearmatrixequation
definedinaLiegroup,and(ii)ageneralnonlinearequationtowhichthetechniquesofSection 3.4canbeapplied.
5.9.1. NonlinearmatrixequationsinLiegroups
Aswehavealreadymentioned,thestrategyadoptedbymostLie-groupmethodsforsolvingthenonlinearmatrix
differentialequation(139),
Y′=A(t,Y)Y, Y(0)=Y0∈ G
definedinaLiegroup G,whilstpreservingitsLiegroupstructure,istolift Y(t)from GtotheunderlyingLiealgebra g
(usuallywiththeexponentialmap),thenformulateandnumericallysolvethereanassociateddifferentialequation,and
finallymapthesolutionbackto G.Inthisway,thediscretizationprocedureworksinalinearspaceratherthanintheLie
group.Inparticular,theideaoftheso-calledRunge–Kutta–Munthe-Kaasclassofschemesistoapproximatethesolutionof
theassociateddifferentialequationintheLiealgebra gbymeansofaclassicalRunge–Kuttamethod[ 59,179,180].
TogeneralizeMagnusintegratorswhen A=A(t,Y),animportantdifferencewithrespecttothelinearcaseisthat,now,
multivariateintegralsdependalsoonthevalueofthe(unknown)variable Yatquadraturepoints.Thisleadstoimplicit
methodsandnonlinearalgebraicequationsineverystepoftheintegration[ 181],whichingeneralcannotcompetein
efficiencywithotherclassesofgeometricintegratorssuchassplittingandcompositionmethods.
AnobviousalternativeisjusttoreplacetheintegralsappearinginthenonlinearMagnusexpansiondevelopedin
Section3.3byaffordablequadratures,dependingontheparticularproblem.If,forinstance,weuseEuler’smethodto
approximatethefirsttermin (142),Ω[1](h)=hA(0,Y0)+ O(h2)andΩ[2]isdiscretizedwiththemidpointrule,weget
thesecondorderscheme
v2≡hA
(
h
2
,e
h
2A(0,Y0)Y0
)
=Ω[2](h)+ O(h3)
Y1=ev2Y0. (304)
Thesameprocedurecanbecarriedoutathigherorders,consistentlydiscretizingtheintegralsappearingin Ω[m](h)for
m>2[99].
5.9.2. Thegeneralnonlinearproblem
Inprinciple,itispossibletoadaptallmethodsbuiltforlinearproblemstothegeneralnonlinearnon-autonomous
equation(159)
x′=f(t,x),
orequivalently,theoperatordifferentialequation (160),
d
dt
Φt=ΦtLf(t,y), y=x0.
AswepointedoutinSection 3.4,therearetwoproblematicaspectswhendesigningpracticalnumericalschemesbasedon
Magnusexpansioninthenonlinearcase.ThefirstoneishowtocomputeorapproximatethetruncatedMagnusexpansion
(oritsactionontheinitialconditions).ThesecondoneishowtoevaluatetherequiredLietransforms.Forexample,to
computetheLietransformexp (tLf(y))actingonyisequivalenttosolvingtheautonomousdifferentialequation x′=f(x)at
t=hwithx(0)=y,orx(t)=exp(tLf(x0))x0wherex0=ycanbeconsideredasasetofcoordinates.
Veryoften,thepresenceofLiebracketsintheexponentleadstofundamentaldifficulties,sincetheresultingvector
fieldsusuallyhaveverycomplicatedstructures.Sometimes,however,thisproblemcanbecircumventedbyusingthesame
techniques,leadingtocommutator-freeMagnusintegratorsinthelinearcase.Inanycase,oneshouldbearinmindthatthe
actionoftheexponentialsinthemethodsdesignedforthelinearcasehastobereplacedbytheircorrespondingmaps.
Alternatively,ifthemethodisformulatedintermsofLietransforms,theorderoftheexponentialshastobereversed,
accordingtoEq. (155).
Nextweillustratehowtonumericallysolvetheproblem
x′=f1(t,x)+f2(t,x) (305)
usingthescheme (299)with(303)andthecoefficients aij,bijtakenfromMN 6-4inTable1.
LetusconsidertheDuffingequation
q′′+ϵq′+q3−q=δcos(ωt) (306)
S.Blanesetal./PhysicsReports470(2009)151–238 221
Table2
Algorithmsforthenumericalintegrationof (307)or(308):(Algorithm1)withscheme (298),and(Algorithm2)withscheme (302).
Algorithm1:Standardsplit Algorithm1:Magnussplit
q0=q(tn); p0=p(tn);
ta=tn; tb=tn
do i=1,m
pi=pi−1−haiV′(ta,qi−1)
ta=ta+hai
qi=qi−1+hbiT′(tb,pi)
tb=tb+hbi
enddo
q0=q(tn); p0=p(tn);
do i=1,k
T′
i(p)=T′(tn+cih,p); V′
i(q)=V′(tn+cih,q)
enddo
do i=1,m
˜Vi(q)=σi1V′
1(q)+···+ σikV′
k(q)
˜Ti(p)=ρi1T′
1(p)+···+ ρikT′
k(p)
pi=pi−1−h˜Vi(qi−1)
qi=qi−1+h˜Ti(pi)
enddo
whichcanbeobtainedfromthetime-dependentHamiltonian
H(q,p,t)=T(p,t)+V(q,t)=e−ϵt1
2
p2+eϵt
(
1
4
q4−
1
2
q2−δcos(ωt)q
)
(307)
orequivalentlyfrom
d
dt
{
q
p
}
=
{
T′(t,p)
−V′(t,q)
}
=
{
e−ϵtp
0
}
+
{
0
eϵt(
q−q3+δcos(ωt)
)
}
. (308)
Noticethatthissystemalreadyhastheform (305),eachpartbeingexactlysolvable.Inconsequence,thesplittingmethod
shownin(298)canbeusedhere.TheprocedureisdescribedasAlgorithm1in Table2.
Observethattheleap-frogcomposition (281)correspondstom=2and
a1=a2=
1
2
, b1=1, b2=0. (309)
Sinceb2=0onestagecanbesaved(withatrivialmodificationofthealgorithm)andtheschemeisconsideredasaone
stagemethod.Anefficientsymmetric5-stagefourthorderintegratorisgivenbythecoefficients( m=6)
ai= γi+γi−1
2
, bi=γi. (310)
i=0,1,..., 6with γ0=γ6=0and γ1=γ2=γ4=γ5=1/(4−41/3), γ3=1−4γ1.
Alternatively,wecanusetheMagnusintegrator (302).Sincethekineticenergyisquadraticinmomenta,wecanapply
thefourth-ordermethodMN 6-4.Ifwetakethefourth-orderGauss-Legendrequadraturerulefortheevaluationofthetime-
dependentfunctionthenwecanconsider (303),wherethecoefficients aij,bijaregivenin Table1.Here,A(t)playstheroleof
T′(t,p)andB(t)playstheroleof V′(t,q)(theyarenotinterchangeable,otherwisetheperformanceseriouslydeteriorates).
ThecomputationofonetimestepisshownasAlgorithm2in Table2.
Wetake ϵ=1/20,δ=1/4,ω=1andinitialconditions q(0)=1.75,p(0)=0.Weintegrateupto t=10πand
measuretheaverageerrorinphasespace,intermsofthenumberofforceevaluationsfordifferenttimesteps(inlogarithmic
scale).Theresultsareshownin Fig.20.TheschemeMN 6-4has6stagesperstep,butonlytwotime-evaluations.Forthis
reason,inthefigure,wehaveconsidered,asthenumberofevaluationsperstep,bothtwoandsix(leftandrightcurves
connectedbyanarrow).ThesuperiorityofthenewsplittingMagnusintegratorsforthisproblemisevident.Ifthetime-
dependentfunctionsdominatethecostofthealgorithm,thesuperiorityisevenhigher.Surprisingly,themethodshows
betterstabilitythantheleap-frogmethod,whichattainsthehigheststabilitypossibleamongthesplittingmethodsfor
autonomousproblems.
6. SomeapplicationsofthenumericalintegratorsbasedonME
InthissectionwecollectseveralexampleswherethenumericalintegrationmethodsbasedontheMagnusexpansion
havebeenappliedintherecentliterature.SpecialattentionisdedicatedtothenumericalintegrationoftheSchrödinger
equation,sincetheMagnusseriesexpansionhasbeenextensivelyusedinthissettingalmostsinceitsveryformulation.
Thetime-independentSchrödingerequationcanbeconsideredasaparticularexampleofaSturm–Liouvilleproblem,sowe
alsoreviewtheapplicabilityofMagnusbasedtechniquesinthiscontext.Thenweconsideraparticularnonlinearsystem
(thedifferentialRiccatiequation)whichcanbe,insomesense,linearized,sothatattheendonemayworkwithfinite-
dimensionalmatrices.Finally,wesummarizearecentbutnoteworthyapplication:thedesignofnewclassesofnumerical
schemesfortheintegrationofstochasticdifferentialequations.
222 S.Blanesetal./PhysicsReports470(2009)151–238
Fig.20. Averageerrorversusnumberofforceevaluationsinthenumericalintegrationof (308)usingsecondandfourthordersymplecticintegrators
forgeneralseparablesystems(S2correspondstothesecondorderleapfrogmethodwithcoefficients (309)andSU54tothefourthordermethodwith
coefficients(310))andthefourthordersymplecticRunge–Kutta–NyströmmethodMN 6-4withinitialconditions q(0)=1.75,p(0)=0and ϵ=1/20,
δ=1/4,ω=1.
6.1. Casestudy:NumericaltreatmentoftheSchrödingerequation
BeforeembarkingontheuseofnumericalmethodsbasedontheMagnusexpansionintheintegrationoftheSchrödinger
equation,letusestablishfirstthetheoreticalframeworkwhichallowsonetousenumericalintegratorsinthissettingfor
obtainingapproximatesolutionsintimeandspace.
6.1.1. Time-dependentSchrödingerequation
Tokeepthetreatmentassimpleaspossible,wecommencebyconsideringtheone-dimensionaltime-dependent
Schrödingerequation(¯h=1)
i
∂
∂t
ψ(t,x)=Hψ(t,x)≡−
1
2
∂2
∂x2ψ(t,x)+V(x)ψ(t,x), (311)
withinitialcondition ψ(0,x)=ψ0(x).Ifwelookforasolutionoftheform ψ(t,x)=φ(t)ϕ(x),itisclearthat,bysubstituting
into(311),onegets φ(t)=e−itE,where Eisaconstantand ϕ(x)isthesolutionofthesecondorderdifferentialequation
−
d2ϕ
dx2+V(x)ϕ=Eϕ. (312)
IfE >Vthesolutionisoscillatory,whereasif E <Vthesolutionisalinearcombinationofexponentiallyincreasingand
decreasingfunctions.Forboundedproblems,thislastconditionalwaystakesplaceattheboundaries.Since
∫
|ψ(x,t)|2dx=
∫
|ϕ(x)|2dx<∞, (313)
itisclearthattheexponentiallyincreasingsolutionshavetobecanceled,andthiscanonlyoccurforcertainvaluesofthe
constantE,whicharepreciselytheeigenvaluesoftheproblem.
Letusassumethatthesystemhasonlyadiscretespectrum,anddenoteby {En,ϕn}∞
n=0,withEi<Ej,i<j,thecomplete
setofeigenvaluesandassociatedeigenvectors.Itiswellknownthatwecantake {ϕn}∞
n=0asanorthonormalbasisand,since
(311)islinear,anysolutioncanbewrittenas
ψ(t,x)=
∞∑
n=0
cne−itEnϕn(x). (314)
Usingthestandardnotationfortheinnerproduct,onehas
⟨ϕn(x)|ψ(t,x)⟩=
∫
ϕ∗
n(x)ψ(t,x)dx=cne−itEn (315)
and
|⟨ϕn(x)|ψ(t,x)⟩|2=|cn|2
S.Blanesetal./PhysicsReports470(2009)151–238 223
istheprobabilityoffindingthesystemintheeigenstate ϕn,sothat
∑
n|cn|2=1.Theenergyisgivenby
E=⟨ψ|H|ψ⟩=
∫
ψ∗(t,x)Hψ(t,x)dx=
∞∑
n=1
∞∑
m=1
c∗
ncmHn,m, (316)
where
Hn,m≡⟨m|H|n⟩=⟨ ϕm|H|ϕn⟩.
Ingeneral,thecoefficients cndecreaseveryfastwith nand,insomecases,thesystemallowsonlyafinitenumberofstates.
Inthatsituation,onemayconsidertheSchrödingerequationasafinitedimensionallinearsystemwheretheHamiltonian
isamatrixwithelements Hn,m.ThisispreciselythecasefortheexamplesexaminedinSection 4.
WhentheHamiltonianisexplicitlytime-dependent,thisprocedureisnolongervalid.Instead,onemayusesome
alternativetechniqueswhichwenowbrieflyreview.
(i)Spectraldecomposition.Letusassumethatthesystemisperturbedwithatime-dependentpotential,i.e.,Eq. (311)
takestheform
i
∂
∂t
ψ(t,x)=ˆH(t)ψ(t,x)≡(ˆT+ˆV(t))ψ(t,x), (317)
where
ˆTψ≡−
1
2
∂2ψ
∂x2 , ˆV(t)ψ≡(V(x)+˜V(t,x))ψ.
Inthiscase,wecannotuseseparationofvariables.However,since {ϕn}isacompletebasiswecanstillwritethesolutionas
ψ(t,x)≃
d−1∑
n=0
cn(t)e−itEnϕn(x), (318)
whereEnandϕnaretheexacteigenvaluesandeigenfunctionswhen ˜V = 0,andthecomplexcoefficients cngivethe
probabilityamplitudetofindthesysteminthestate ϕn(
∑
n|cn(t)|2 = 1forall t).Then,substituting (318)into(317)
weobtainthematrixequation
i
d
dt
c(t)=H(t)c(t), c(0)=c0, (319)
wherec=(c0,..., cd−1)T∈ Cd andH∈ Cd×d isaHermitianmatrixassociatedtotheHamiltonian
(H(t))ij=⟨ϕi|ˆH(t)−ˆH0|ϕj⟩ei(Ei−Ej)t, i,j=1,..., d
andˆH0=ˆH(t=0).Giventheinitialwavefunction ψ(0,x),thecomponentsof c0aredeterminedby c0,i=⟨ϕi|ψ(0,x)⟩.
Obviously,anycompletebasiscanbeusedinthiscase,althoughthenormofthematrix H(t)maydependonthechoice.
Inaddition,thenumberofbasiselements(i.e.theminimumdimension dnecessarytoobtainasufficientlyaccurateresult)
alsodependsonthechosenbasis.
(ii)Spacediscretization.ThisprocedureintendstotakeadvantageofthestructureoftheHamiltonian ˆHin(317):ˆVis
diagonalinthecoordinatespaceand ˆT isdiagonalinthemomentumspace.Letusassumethatthesystemisdefinedinthe
intervalx∈[x0,xf]withperiodicboundaryconditions.Wecanthensplitthisintervalin dpartsoflength 1x=(xf−x0)/d
andconsider cn= ψ(t,xn)wherexn=x0+n1x,n=0,1,..., d−1.Thenafinitedimensionallinearequationsimilar
(butwithadifferentcoefficientmatrix H)toEq. (319)results.Since ˆVisdiagonalinthecoordinatespaceand ˆT isdiagonal
inmomentumspace,itispossibletousecomplexFastFourierTransforms(FFTs)forevaluatingtheproducts Hc,where
ˆTψ(t,xn)= F−1DT Fψ(t,xn),andDT isadiagonaloperator.
Wethusseethatwhatevertheprocedureused(spectraldecompositionorspacediscretization),oneendsupwithalinear
equationoftheform
i
dψ
dt
(t)=H(t)ψ(t), ψ( 0)=ψ0 (320)
whereψ(t)nowrepresentsacomplexvectorwith dcomponentswhichapproximatesthe(continuous)wavefunction.
ThecomputationalHamiltonian H(t)appearingin (320)isthusaspacediscretization(orotherfinite-dimensionalmodel)
ofˆH(t)= ˆT+ˆV(t).NumericaldifficultiescomemainlyfromtheunboundednatureoftheHamiltonianandthehighly
oscillatorybehaviorofthewavefunction.
ItisatthispointwhennumericalalgorithmsbasedontheMagnusexpansion,suchastheyhavebeenformulatedin
previoussections,comeintoplayforintegratingintimethelinearsystem (320).Toputtheminperspective,letusfirst
introducesomeothernumericalmethodsalsousedinthiscontext.Ourexpositionislargelybasedonthereference[ 182].
224 S.Blanesetal./PhysicsReports470(2009)151–238
6.1.1.1. Theimplicitmidpointrule. Theapproximationtothesolutionof (320)providedbythisschemeisimplicitlydefined
by
i
ψn+1−ψn
1t
=H(tn+1/2)
1
2
(ψn+1+ψn), (321)
wheretn+1/2= 1
2(tn+1+tn).Here,andinthesequel,forclarity,wehavedenotedby 1tthetimestepsizeand tn=n1t.
Alternatively,
ψn+1=r(−i1tH(tn+1/2))ψn, withr(z)=
1+ 1
2z
1− 1
2z
. (322)
Observethat,as risnothingbuttheCayleytransform,thenumericalpropagatorisunitaryandconsequentlytheEuclidean
normofthediscretewavefunctionispreservedalongtheevolution: ‖ψn+1‖=‖ ψn‖.Thisisacrucialqualitativefeature
themethodshareswiththeexactsolution,contrarilytootherstandardnumericalintegrators,suchasexplicitRunge–Kutta
methods.Fromapurelynumericalpointofview,thealgorithmisstableforanystepsize 1t.
Anotherusefulpropertyofthisnumericalschemeistime-symmetry:exchangingin (322)nbyn+1and 1tby−1twe
getthesamenumericalmethodagain.Equivalently, r(−z)=r(z)−1,exactlyastheexponentiale z.
Withrespecttoaccuracy,itisnotdifficulttoshowthat,if H(t)isboundedandsufficientlysmooth,theerrorverifies
‖ψn−ψ(tn)‖= O(1t2) (323)
uniformlyforn1tinatimeinterval [0,tf].Inotherwords,theimplicitmidpointruleisasecond-ordermethod.Ithappens,
however,thattheconstantintheterm O(1t2)dependsonboundsof H′andH′′andonthenormofthethirdderivativeof
thesolution ψ.Since,ingeneral,thewavefunctionishighlyoscillatoryintime,thistimederivativecanbecomelarge,and
sotheuseofverysmalltimestepsismandatory.
6.1.1.2. Theexponentialmidpointrule. Anotherpossibilitytogetapproximatesolutionsof (320)consistsofreplacing r(z)
byexp(z)in(322):
ψn+1=exp(−i1tH(tn+1/2))ψn. (324)
Now,insteadofsolvingsystemsoflinearequationsaspreviously,onehastocomputetheexponentialofalargematrixtimes
avectorateachintegrationstep.Inthisrespect,thetechniquesreviewedinSection 5.6canbeefficientlyimplemented.The
exponentialmidpointrule (324)alsoprovidesaunitarypropagatoranditistime-symmetric.Inaddition,theerrorsatisfies
thesamecondition (323),butnowtheconstantinthe O(1t2)termisindependentofthetimederivativesof ψundercertain
assumptionsonthecommutator [H(t),H(s)][183].Asaconsequence,muchlargertimestepscanbetakentoachievethe
sameaccuracyaswiththeimplicitmidpointrule.
6.1.1.3. IntegratorsbasedontheMagnusexpansion. Themethod (324)isaparticularinstanceofasecondorderMagnus
methodwhentheintegral
∫1t
0 H(s)dsisreplacedbythemidpointquadraturerule.Infact,wehavealreadyuseditin (274).
Obviously,ifhigherorderapproximationsareconsidered,theaccuracycanbeenhancedagreatdeal.Thisclaimhasto
beconvenientlyjustified,however,sincetheorderofthenumericalmethodsbasedonMagnushasbeendeducedwhen
‖1tH(t)‖→ 0andisobtainedbystudyingtheremainderofthetruncatedMagnusseries.IntheSchrödingerequation,on
theotherhand,onehastocopewithdiscretizationsofunboundedoperators,soinprincipleitisnotevidenthowtheprevious
resultsontheorderofaccuracyapplyinthiscontext.In[ 183],HochbruckandLubichanalyze,indetail,theapplicationof
thefourth-orderMagnusintegrator (254)toEq.(320),showingthatitworksextremelywellevenwithstepsizesforwhich
thecorresponding‖1tH(t)‖islarge.Inparticular,theschemeretainsfourthorderofaccuracyin 1tindependentlyofthe
normofH(t)whenH(t)=T+V(t),Tisadiscretizationof −1
2
∂2
∂x2(withmaximumeigenvalue Emax∼(1x)−2)andV(t)is
sufficientlysmoothunderthetimesteprestriction 1t
√
Emax≤Const.Thisissoevenwhenthereisnoguaranteethatthe
Magnusseriesconvergesatall.
6.1.1.4. Symplecticperspective.Theevolutionoperatorcorrespondingto (317)isnotonlyunitary,butalsosymplecticwith
canonicalcoordinatesandmomentaRe (ψ)andIm(ψ),respectively.Ifwecarryoutadiscretizationinspace,thissymplectic
structureisinheritedbythecorrespondingEq. (319).Itmakessense,then,towrite c=q+ipandconsidertheequations
satisfiedbyq,p∈ Rd,namely
q′=H(t)p, p′=−H(t)q, (325)
whichcanbeinterpretedasthecanonicalequationscorrespondingtotheHamiltonian[ 184]
H(t,q,p)=pTH(t)p+qTH(t)q. (326)
Denotingz =(q,p)T,itisclearthat
z′=(A(t)+B(t))z
S.Blanesetal./PhysicsReports470(2009)151–238 225
where
A(t)=
(
0 H(t)
0 0
)
, B(t)=
(
0 0
−H(t) 0
)
. (327)
Forthissystemitispossible,therefore,toapplythecommutator-freeMagnusintegratorsconstructedinSection 5.8.2.In
addition,onehas
[B,[B,[B,A]]]=[ A,[A,[A,B]]]= 0,
andthispropertyallowsustousespeciallydesignedandhighlyefficientintegrationmethods[ 178].
6.1.2. Time-independentSchrödingerequation
Restrictingourselvestothetime-independentSchrödingerequation (312),wenextillustratehowMagnusintegrators
can,infact,beusedtocomputethediscreteeigenvaluesdefinedbytheproblem.AlthoughonlytheSchrödingerequation
inafinitedomainisconsidered,
−
d2ϕ
dx2+V(x)ϕ=λϕ, x∈(a,b) (328)
theprocedurecanbeeasilyadaptedtoothertypesofeigenvalueproblems,inwhichonehastofindboth λ≡Eandϕ.Here
itisassumedthatthepotentialissmooth, V∈Cm(a,b)and,forsimplicity, ϕ(a)=ϕ(b)=0.
Undertheseassumptions,itiswellknownthattheeigenvaluesarereal,distinctandboundedfrombelow.Theproblem
(328)canbeformulatedinthespeciallineargroupSL (2),
dy
dx
=
(
0 1
V(x)−λ 0
)
y, x∈(a,b), wherey=(ϕ,dϕ/dx)T, (329)
sothattheMagnusexpansioncanbeappliedinanaturalway.Asusual,ratherthanapproximatingthefundamentalsolution
of(329)intheentireinterval (a,b)byexp(Ω),theideaistopartitiontheintervalinto Nsmallsubintervals,andthenapply
aconvenientlydiscretizedversionoftheMagnusexpansion.Inthisway,theconvergenceproblemnolongerrestrictsthe
size(b−a)[70].
Forthesakeofsimplicity,letusconsiderthefourth-ordermethod (254).Writing
Vn,1=V
(
xn+
(
1
2
−
√
3
6
)
h
)
, Vn,2=V
(
xn+
(
1
2
+
√
3
6
)
h
)
,
whereh=(b−a)/Nandxn=a+hn,weform
σn(λ)=


−
√
3
12
h2(Vn,1−Vn,2) h
1
2
h(Vn,1+Vn,2)−hλ
√
3
12
h2(Vn,1−Vn,2)

,
forn=0,1,..., N−1.Then,thefourth-orderapproximationtothesolutionof (329)atx=bis
y(b)=eσN−1(λ)··· eσ1(λ)eσ0(λ)y(a) (330)
andthevaluesof λareobtainedfrom (330)byrepeatedlyusingtheexpressionoftheexponentialofatracelessmatrix,
Eq.(24),andrequiringthat ϕ(a) = ϕ(b) = 0.Theresultingnonlinearequationin λcanbesolved,forinstance,by
Newton–Raphsoniteration,whichprovidesquadraticconvergenceforstartingvaluessufficientlynearthesolution[ 70].
Although,byconstructionthisprocedureleadstoaglobalorderofapproximation O(hp)ifa pth-orderMagnusmethod
isapplied,itturnsoutthattheerroralsodependsonthemagnitudeoftheeigenvalue.Specifically,theerrorina pth-order
methodgrowsas O(hp+1λp/2−1)[70],andthusoneexpectspoorapproximationsforlargeeigenvalues.Thisdifficultycan
beovercome,uptoapoint,byanalyzingthedependenceon λofeachtermintheMagnusseriesandconsideringpartial
sumsofthetermscarryingthemostsignificantdependenceon λ.Forinstance,itispossibletodesignasixth-orderMagnus
integratorforthisproblemwitherror O(h7λ),whichthereforebehaveslikeafourth-ordermethodwhen h2λ≈1,whereas
thestandardsixth-orderMagnusscheme,carryinganerrorof O(h7λ2),reducestoanorder-twomethod[ 70].Inanycase,
gettingaccurateapproximationswhen |λ|→∞ ismoreproblematic[ 185].
6.2. Sturm–Liouvilleproblems
Thesystemdefinedby (328)withboundaryconditions ϕ(a)=ϕ(b)=0isjustoneparticularexampleofasecondorder
Sturm–Liouvilleproblem[ 186,187].ItisthusquitenaturaltotrytoapplyMagnusintegratorstomoregeneralproblems
withinthisclass.
226 S.Blanesetal./PhysicsReports470(2009)151–238
AsecondorderSturm–Liouvilleeigenvalueproblemhastheform
d
dx
(
p(x)
dy
dx
(x)
)
+q(x)y(x)=λr(x)y(x) on(a,b) (331)
withseparatedboundaryconditionswhichcommonlyhavetheform
A1y(a)+A2p(a)y′(a)=0 B1y(b)+B2p(b)y′(b)=0 (332)
forgivenconstants Ai,Biandfunctions p(x),q(x)andr(x).Solvingthisproblemmeans,ofcourse,determiningthevalues
λnofλforwhichEq. (331)hasanontrivial(continuouslydifferentiablesquareintegrable)solution yn(x)satisfyingEq.
(332)[187,188].
TheseandotherhigherorderSturm–Liouvilleproblemscanberecastasalinearmatrixsystemoftheform
Y′=(λB+C(x))Y (333)
bytransformingtotheso-called compoundmatrixormodifiedRiccativariables[ 189,185].HereBisaconstantmatrix.When
generalizingtheabovetreatmentbasedontheMagnusexpansiontothisproblem,thereisoneelementarybutimportant
remarkworthstatingexplicitly: unlessthedifferentialequation (333)hasthesamelarge λ-asymptoticsassomedifferential
equationwithx -independentcoefficients,thenitwillbeimpossibletodevelopaMagnusmethodwhichaccuratelyapproximates
itssolutionsforlarge λ[185].ThereasonisthataMagnusmethodapproximatesthesolutionbyadiscretesolution,calculated
usingaformulaoftheform Y(xn+1)=exp(σn(λ))Y(xn);inparticular,onthefirststep (x0,x1),thedifferentialequationis
approximatedbyoneinwhichthecoefficientmatrixisreplacedbythe x-independentmatrix σ0(λ)/(x1−x0).
Inconsequence,theattentionshouldberestrictedtosystemsforwhichitisknownthatasuitableconstant-coefficient
systemprovidesthecorrectasymptotics.Thisisthecase,inparticular,forEq. (328),andmoregenerallyforlinearequations
oforder2ninwhichthe (2n−1)stderivativeiszero,suchas
(−1)ny(2n)+
2n−2∑
j=0
qj(x)y(j)=λy.
Heretheasymptoticsaredeterminedbytheequation (−1)ny(2n)=λy[190].Eventhen,themethodsdevelopedin[ 70]for
Eq.(328)andimplementedforsystemswithmatricesofgeneralsizein[ 185]requirea λ-dependentstepsizerestrictionof
theform h≤ O(|λ|−1/4)inordertobedefined.Nevertheless,theanalysiscarriedoutin[ 185]showsthatthefourthorder
Magnusintegratorbasedonatwo-pointGaussianquadratureappearstooffersignificantadvantagesoverconventional
methodsbasedonpowerseriesandlibraryroutines.
MagnusintegratorshavealsobeensuccessfullyappliedinthesomewhatrelatedproblemofcomputingtheEvans
functionforspectralproblemsarisingintheanalysisofthelinearstabilityoftravelingwavesolutionstoreaction–diffusion
PDEs [169]. In this setting, Magnus integrators possess some appealing features in comparison, for instance, with
Runge–Kuttaschemes:(1)theyareunconditionallystable;(2)theirperformanceissuperiorinhighlyoscillatoryregimes
and(3)theirstepsizecanbecontrolledinadvance.Items(2)and(3)areduetothefactthaterrorboundsforMagnus
methodsdependonlyonloworderderivativesofthecoefficientmatrix,not(asforRunge–Kuttaschemes)onderivativesof
thesolution.Therefore,performanceand,correspondingly,thechoiceofoptimalstepsizeremainuniformoveranybounded
regionofparameterspace[ 169].
6.3. ThedifferentialRiccatiequation
Letusnowconsiderthetwo-pointboundaryvalueprobleminthe tvariabledefinedbythelineardifferentialequation
y′≡
(
y′
1
y′
2
)
=
(
A(t) B(t)
C(t) D(t)
)(
y1
y2
)
, 0<t<T (334)
withseparatedboundaryconditions
(K11 K12)
(
y1
y2
)
t=0
=γ1, ( K21 K22)
(
y1
y2
)
t=T
=γ2. (335)
HereA∈ Cq×q,B∈ Cq×p,C∈ Cp×q,D∈ Cp×p,whereas y1,γ2∈ Cp,y2,γ1∈ Cqandthematrices Kijhaveappropriate
dimensions.Wenextintroducethetime-dependentchangeofvariables(orpicture) y=Y0(t)w,with
Y0(t)=
(
Ip 0
X(t) Iq
)
(336)
andchoosethematrix X∈ Cp×qsoastoensurethatinthenewvariables w= Y−1
0 (t)ythesystemassumesthepartly
decoupledstructure[191]
w′≡
(
w′
1
w′
2
)
=
(
A+BX B
O D −XB
) (
w1
w2
)
, (337)
S.Blanesetal./PhysicsReports470(2009)151–238 227
togetherwiththecorrespondingboundaryconditionsfor w.Itturnsoutthatthisispossibleif,andonlyif, X(t)satisfiesthe
so-calleddifferentialRiccatiequation[ 192]
X′=C(t)+D(t)X−XA(t)−XB(t)X, X(0)=X0 (338)
forsomeX0.Byrequiring
X0=−K−1
12K11, (339)
thentheboundaryconditions (335)alsodecoupleas
(O K12)w(0)=γ1, (K21+K22X(T) K22)w(T)=γ2. (340)
Hereweassume,withoutlossofgenerality,that K12isinvertible.Inthisway,theoriginalboundaryvalueproblemcanbe
solvedasfollows[ 191,192]:(i)solveEq. (338)withinitialcondition (339)fromt=0to t=T;(ii)solvethe w2-equation
in(337)and(340),alsofromzeroto T;(iii)solvethe w1-equationin (337)fromt=Ttot=0andrecover y=Y0(t)w.In
otherwords,thesolutionoftheoriginaltwo-pointboundaryvalueproblemcanbeobtainedbysolvingasequenceofthree
differentinitialvalueproblems,oneofwhichinvolvesthenonlinearequation (338).Obviously,steps(i)and(iii)canbesolved
usingnumericalintegratorsbasedontheMagnusexpansion.Itcouldbeperhapsmoresurprisingthatthesealgorithmscan,
indeed,beusedtointegratetheRiccatiequationinstep(ii).
Althoughtheboundaryvalueproblem (334)isaconvenientwaytointroducethedifferentialRiccatiequation (338),
thisequationarisesinmanyfieldsofscienceandengineering,suchaslinearquadraticoptimalcontrol,stabilitytheory,
stochasticcontrol,differentialgamesetc.Accordingly,ithasreceivedconsiderableattentionintheliterature,bothfocused
onitstheoreticalaspects[ 193,194]anditsnumericaltreatment[ 191,195,196].
InordertoapplyMagnusmethodstonumericallysolvetheRiccatiequation,wefirstapplythetransformation
X(t)=V(t)W−1(t), (341)
withV∈ Cp×q,W∈ Cq×qandV(0)=X0,W(0)=Iq,intheregionwhere W(t)isinvertible.ThenEq. (338)isequivalent
tothelinearsystem
Y′=S(t)Y(t), Y(0)=
(
Iq
X0
)
(342)
with
Y(t)=
(
W(t)
V(t)
)
, S(t)=
(
A(t) B(t)
C(t) D(t)
)
(343)
sothatthepreviousMagnusintegratorsforlinearproblemscanbeappliedhere.Apparently,thissystemissimilarto (334),
butnowwearedealingwithaninitialvalueproblemand Yisamatrixinsteadofavector.
WhendealingingeneralwiththedifferentialRiccatiequation (338),itismeaningfultodistinguishthefollowingthree
cases:
(i)Theso-calledsymmetricRiccatiequation,whichcorrespondsto q = p,D(t) = −A(t)Treal,and B(t),C(t)real
andsymmetricmatrices.Inthiscase,thesolutionsatisfies XT= X.Itisstraightforwardtoshowthatthisproblem
isequivalenttothetreatmentofthegeneralizedtime-dependentharmonicoscillator,describedbytheHamiltonian
function
H=
1
2
pTB(t)p+pTA(t)q−
1
2
qTC(t)q.
TheapproximatesolutionattainedbyMagnusintegrators,whenappliedto (342)–(343),canbeseenastheexact
solutioncorrespondingtoaperturbedsymplecticmatrix ˜S(t) ≃ S(t).Inotherwords,wearesolving,exactly,a
perturbedHamiltoniansystemsothattheapproximatesolution, ˜X,willshareseveralpropertiesoftheexactsolution,
inparticular ˜XT=˜X.
(ii)Thelinearnon-homogeneousproblem
X′=D(t)X+C(t) (344)
correspondstotheparticularcase A=0and B=0in(338).
(iii)Theproblem
X′=D(t)X+XA(t) (345)
isrecoveredfrom (338)bytaking C=0and B=0.Ithasbeentreatedin[ 36]bydevelopingan adhoc Magnus-type
expansion.Noticethatthecase p=q,D=−Acorrespondstothelinearisospectralsystem (238).
228 S.Blanesetal./PhysicsReports470(2009)151–238
6.4. Stochasticdifferentialequations
Inrecentyears,theuseofstochasticdifferentialequations(SDEs)hasbecomewidespreadinthesimulationofrandom
phenomenaappearinginphysics,engineering,economicsetc,suchasturbulentdiffusion,polymerdynamicsandinvestment
finance[197].AlthoughmodelsbasedonSDEscanofferamorerealisticrepresentationofthesystemthanordinary
differentialequations,thedesignofeffectivenumericalschemesforsolvingSDEsis,incomparisonwithODEs,aless
developedfieldofresearch.Thisfactnotwithstanding,itistruethat,recently,newclassesofintegrationmethodshave
beenconstructedwhichautomaticallyincorporateconservationpropertiestheSDEpossesses.Sincesomeofthemethods
arebasedpreciselyontheMagnusexpansion,webrieflyreviewtheirmainfeatureshere,andreferthereadertothemore
advancedliteratureonthesubject[ 197–199].
ASDEinitsgeneralformisusuallywrittenas
dy(t)=g0(t,y(t))dt+
d∑
j=1
gj(t,y(t))dWj(t), y(0)=y0, y∈ Rm, (346)
wheregj,(j≥ 0),are m-vector-valuedfunctions.Thefunction g0isthedeterministiccontinuouscomponent(calledthe
driftcoefficient),the gj,(j≥ 1),representthestochasticcontinuouscomponents(the diffusioncoefficients)and Wjared
independentWienerprocesses.AWienerprocess W(alsocalledBrownianmotion)isastochasticprocess[ 197]satisfying
W(0)=0, E[W(t)]= 0, Var[W(t)−W(s)]= t−s, t>s
whichhasindependentincrementsonnon-overlappingintervals.Inotherwords,aWienerprocessisnormallydistributed
withmeanorexpectationvalue Eequaltozeroandvariance t.
Eq.(346)canbewritteninintegralformas
y(t)=y0+
∫ t
0
g0(s,y(s))ds+
d∑
j=1
∫ t
0
gj(s,y(s))dWj(s). (347)
Thedintegralsin (347)cannotbeconsideredasRiemann–Stieltjesintegrals,sincethesamplepathsofaWienerprocess
arenotofboundedvariation.Infact,ifdifferentchoicesaremadeforthepoint τi(inthesubintervals [ti−1,ti]ofagiven
partition)wherethefunctionisevaluated,thentheapproximatingsumsforeach gj,
N∑
i=1
gj(τi,y(τi))(Wj(ti)−Wj(ti−1)), τ i=θti+(1−θ)ti−1, (348)
converge(inthemean-squaresense)todifferentvaluesoftheintegral,dependingonthevalueof θ[35].Thus,forinstance,
∫ b
a
W(t)dW(t)=
1
2
(W2(b)−W2(a))+
(
θ−
1
2
)
(b−a).
Ifθ=0,then τi=ti−1(theleft-handpointofeachsubinterval)andtheresultingintegraliscalledanItôintegral;if θ=1/2
(sothatthemidpointisusedinstead),onehasaStratonovichintegral.Thesearethetwomainchoicesand,althoughthey
arerelated,theparticularelectiondependsultimatelyonthenatureoftheprocesstobemodeled[ 35].Itcanbeshownthat
theStratonovichcalculussatisfiestheRiemann–Stieltjesrulesofcalculus,andthusitisthenaturalchoicehere.
Whendealingwithnumericalmethodsforsolving (346),therearetwowaysofmeasuringaccuracy[ 197].Thefirstis
strongconvergence,essentialwhentheaimistogetnumericalapproximationstothetrajectorieswhichareclosetotheexact
solution.Thesecondis weakconvergence,whenonlycertainmomentsofthesolutionareofinterest.Thus,if ˆyndenotesthe
numericalapproximationto y(tn)afternstepswithconstantstepsize h= (tn−t0)/n,thenthenumericalsolution ˆy
convergesstronglytotheexactsolution ywithstrongglobalorder pifthereexist C >0(independentof h)and δ> 0such
that
E[‖ˆyn−y(tn)‖]≤ Chp, h∈(0,δ).
Itisworthnoticingthat pcanbefractional,sincetherootmean-squareorderoftheWienerprocessis h1/2.Oneofthe
simplestproceduresforsolving (346)numericallyistheso-calledEuler–Maruyamamethod[ 200],
yn+1=yn+
d∑
j=0
Jjgj(tn,yn), (349)
where
h=tn+1−tn, J0=h, Jj=Wj(tn+1)−Wj(tn), j=1,..., d.
Thisschemeturnsouttobeofstrongorder1 /2.Herethe Jjcanbecomputedas
√
hNj,wherethe NjareN(0,1)normally
distributedindependentrandomvariables[ 35].
S.Blanesetal./PhysicsReports470(2009)151–238 229
Forthegeneralnon-autonomouslinearStratonovichproblemdefinedby
dy=G0(t)ydt+
d∑
j=1
Gj(t)ydWj, y(0)=y0∈ Rm (350)
theMagnusexpansionforthedeterministiccasecanbeextendedinquiteastraightforwardway.Itiswellworthnotingthat
inEq. (350),evenwhenthefunctions Gjareconstant,thereisnoexplicitsolution[ 198],unlessallthe Gj,j≥0,commute
withoneanother,inwhichcaseitholdsthat
y(t)=exp
(
G0t+
d∑
j=1
GjWj(t)
)
y0. (351)
Inmanymodelingsituations,however,thereisnoreasontoexpectthatthefunctions GjassociatedwiththeWiener
processescommute.If,forsimplicity,weonlyconsidertheautonomouscaseandwrite
G(t)≡G0dt+
d∑
j=1
GjdWj(t),
then(350)canbeexpressedas
dy=G(t)ydt, y(0)=y0
andthusonecanformallyapplytheMagnusexpansiontothisequationtoget y(t)=exp(Ω(t))y0.Thefirstterminthe
seriesreads,inthiscase,
∫ t
0
G(s)ds≡
∫ t
0
G0ds+
d∑
j=1
∫ t
0
GjdWj(s)=G0t+
d∑
j=1
GjJj,
wherenow
Jj=
∫ t
0
dW(s)=Wj(t)−Wj(0).
ByinsertingtheseexpressionsintotherecurrenceassociatedwiththeMagnusseries,BurrageandBurrage[ 35]showthat
Ω(t)=
d∑
j=0
GjJj+
1
2
d∑
i=0
d∑
j=i+1
[Gi,Gj](Jji−Jij)
+
d∑
i=0
d∑
k=0
d∑
j=k+1
[Gi,[Gj,Gk]]
(
1
3
(Jkji−Jjki)+
1
12
Ji(Jjk−Jkj)
)
+··· , (352)
wherethemultipleStratonovichintegralsaredefinedby
Jj1j2···jl(t)=
∫ t
0
∫ sl
0
···
∫ s2
0
dWj1(s1)··· dWjl(sl), ji∈{0,1,..., d}. (353)
SincenotalltheStratonovichintegralsareindependent,onehastocomputeonly d(d+1)(d+5)/6stochasticintegral
evaluationstoachievestrongorder1.5withtheexpression (352)[35].If,ontheotherhand, Ω(t)istruncatedafterthefirst
setofterms,thentheresultingnumericalapproximation
y(t)=exp
(
d∑
j=0
GjJj
)
y0
hasstrongorder1 /2,butleadstosmallererrorcoefficientsthantheEuler–Maruyamamethod (349)[35].Furthermore,the
errorbecomessmallerasthe GiGjtermsgetclosertocommutingandtheschemepreservestheunderlyingstructureofthe
problem.
Oneshouldnotice,atthispoint,thatEq. (346)(or,inthelinearcase,Eq. (350)),hasformallythesamestructureasthe
nonlinearODE(171)appearingincontroltheory.Therefore,theformalismdevelopedtheretogettheChen–Fliessseriescan
beappliedherewiththealphabet I={0,1,..., d}andtheintegrals
(∫
0
µ
)
(t)=
∫ t
0
µ(s)ds,
(∫
i
µ
)
(t)=
∫ t
0
µ(s)dWi(s), i≥1,
sincetheStratonovichintegralssatisfytheintegrationbypartsrule.Inotherwords,onecanobtainthecorresponding
