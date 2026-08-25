---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 3-48
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
doc_brief: "The Magnus expansion and some of its applications — 8 sections: Introduction; Introduction; Stochastic differential equations"
---
1.1. Motivation,overviewandhistory
TheoutstandingmathematicianWilhelmMagnus(1907–1990)madeimportantcontributionstoawidevarietyoffields
inmathematicsandmathematicalphysics[ 1].Amongthem,onecanmentioncombinatorialgrouptheory[ 2]andhis
collaborationintheBatemanprojectonhighertranscendentalfunctionsandintegraltransforms[ 3].Inthisreportwereview
anotherofhislong-lastingconstructions:theso-calledMagnusexpansion(hereafterreferredtoasME).MEwasintroduced
asatooltosolvenon-autonomouslineardifferentialequationsforlinearoperators.Itisinterestingtoobservethat,inhis
seminalpaperof1954,[ 4],althoughitisessentiallymathematicalinnature,Magnusrecognizesthathisworkwasstimulated
byresultsofK.O.FriedrichsonthetheoryoflinearoperatorsinQuantumMechanics[ 5].Furthermore,asthefirstantecedent
ofhisproposal,hequotesapaperbyR.P.FeynmaninthePhysicalReview[ 6].Westressthesefactstoshowthatalready,at
itsverybeginning,MEwasstronglyrelatedtoPhysics,andhasbeeneversince,andthereisnoreasontodoubtthatitwill
continuetobe.Thisisthefirstmotivationtoofferhereareviewasthepresentone.
Magnus’proposalhastheveryattractivepropertyofleadingtoapproximatesolutionswhichexhibit,atanyorderof
approximation,somequalitativeorphysicalcharacteristics,whichthefirstprinciplesguaranteefortheexact(butunknown)
solutionoftheproblem.Importantphysicalexamplesarethesymplecticorunitarycharacteroftheevolutionoperatorwhen
dealingwithclassicalorquantummechanicalproblems,respectively.Thisisatvariancewithmoststandardperturbation
theories,andisapparentwhenformulatedinacorrectalgebraicsetting:LiealgebrasandLiegroups.Butthisgreatadvantage
hassometimesbeentaintedinthepast,bythedifficultiesbothinconstructingexplicitlyhigherorderterms,andinassuring
existenceandconvergenceoftheexpansion.
Inouropinion,recentyearshavewitnessedgreatimprovementinthissituation.Concerninggeneralquestionsof
existenceandconvergence,newresultshaveappeared.Fromthepointofviewofapplications,somenewapproachesin
oldfieldshavebeenpublished,whilecompletelynewandpromisingavenueshavebeenopenedbytheuseoftheMagnus
expansioninNumericalAnalysis.Itseemsreasonabletoexpectfruitfulcrossfertilizationbetweenthesenewdevelopments
andthemostconventionalperturbativeapproachtoMEand,fromit,furtherapplicationsandnewcalculations.
ThisnewscenariomakesitdesirableforthePhysicscommunityindifferentareas(andscientistsandengineersingeneral)
tohaveaccess,inasunifiedawayaspossible,toalltheinformationconcerningMEwhich,sofar,hasbeentreatedinvery
differentsettings,andhasappearedscatteredthroughverydifferentbibliographicsources.
Asimpliedbytheprecedingparagraphs,thisreportismainlyaddressedtoaPhysicsaudience,orcloseneighbors,and
consequentlyweshallkeepthetreatmentofitsmathematicalaspectswithinreasonablelimitsandreferthereadertomore
detailedliteraturewherenecessary.Bythesametoken,theapplicationspresentedwillbelimitedtoexamplesfromPhysics,
orfromthecloselyrelatedfieldofPhysicalChemistry.Weshallalsoemphasizeitsinstrumentalcharacterfornumerically
solvingphysicalproblems.
Inthepresentsection,asanintroduction,wepresentabriefoverviewandsketchahistoryofmorethan50yearsofME.
Tostartwith,letusconsidertheinitialvalueproblemassociatedwiththelinearordinarydifferentialequation
Y′(t)=A(t)Y(t), Y(t0)=Y0, (1)
where,asusual,theprimedenotesthederivativewithrespecttotherealindependentvariablewhichwetakeastime t,
althoughmuchofwhatwillbesaidalsoappliestoacomplexindependentvariable.Inorderofincreasingcomplexity,we
mayconsidertheequationaboveindifferentcontexts:
(a)Y: R−→ C,A: R−→ C.Thismeansthattheunknown Yandthegiven Aarecomplexscalarvaluedfunctionsofone
realvariable.Inthiscase,thereisnoproblematall:thesolutionreducestoaquadratureandanordinaryexponential
evaluation:
Y(t)=exp
(∫ t
t0
A(s)ds
)
Y0. (2)
(b)Y: R−→ Cn,A: R−→ Mn(C),where Mn(C)isthesetof n×ncomplexmatrices.Now Yisacomplexvectorvalued
function,andAacomplexn×nmatrixvaluedfunction.Atvariancewiththepreviouscase,onlyinveryspecialcasesis
thesolutioneasytostate:whenforanypairofvaluesof t,t1andt2,onehas A(t1)A(t2)=A(t2)A(t1),whichiscertainly
thecaseif Aisconstant.Thenthesolutionreducestoaquadrature(trivialornot)andamatrixexponential.Withthe
obviouschangesinthemeaningofthesymbols,Eq. (2)stillapplies.Inthegeneralcase,however,thereisnocompact
expressionforthesolutionand (2)isnolongerthesolution.
154 S.Blanesetal./PhysicsReports470(2009)151–238
(c)Y: R−→ Mn(C),A: R−→ Mn(C).Nowboth YandAarecomplexmatrixvaluedfunctions.Aparticularcase,butstill
generalenoughtoencompassthemostinterestingphysicalandmathematicalapplications,correspondsto Y(t)∈ G,
A(t)∈ g,where Gand gare,respectively,amatrixLiegroupanditscorrespondingLiealgebra.Whythisisofinterest,
iseasytograsp:thekeyreasonforthefailureof (2)isthenon-commutativityofmatricesingeneral.Soonecanexpect
thatthe(ingeneralnon-vanishing)commutatorsplayanimportantrole.Butwhencommutatorsentertheplay,one
immediatelythinksinLiestructures.Furthermore,plainlyspeaking,thewayfromaLiealgebratoitsLiegroupiscovered
bytheexponentialoperation—afactthatwillbeofnosurpriseinthiscontext.Thesamecommentsofthepreviouscase
arevalidhere.Inthisreport,weshallmostlydealwiththismatrixcase.
(d)Themostgeneralsituationonecanthinkofcorrespondsto Y(t)andA(t)beingoperatorsinsomespace,e.g.,Hilbertspace
inQuantumMechanics.Perhapsthemostparadigmaticexampleof (1)inthissettingisthetime-dependentSchrödinger
equation.
Observethatcase(b)abovecanbereducedtocase(c).Thisiseasilyseenifoneintroduceswhat,inmathematical
literature,iscalledthematrizant,aconceptdatingbackatleasttothebeginningofthe20thcenturyintheworkofBaker
[7].Itisthe n×nmatrixU(t,t0)definedthrough
Y(t)=U(t,t0)Y0. (3)
Withoutlossofgenerality,wewilltake t0 = 0unlessotherwiseexplicitlystated,forthesakeofsimplicity.Whenno
confusionmayarise,wewriteonlyoneargumentin Uanddenote U(t,0)≡ U(t),whichthensatisfiesthedifferential
equationandinitialcondition
U′(t)=A(t)U(t), U(0)=I, (4)
whereIstandsforthe n-dimensionalidentitymatrix.Thereaderwillhaverecognized U(t)aswhat,inphysicalterms,is
knownasthetimeevolutionoperator.
WearenowreadytostateMagnus’proposal:asolutionto (4)whichisatruematrixexponential
U(t)=expΩ(t), Ω(0)=O, (5)
andaseriesexpansionforthematrixintheexponent
Ω(t)=
∞∑
k=1
Ωk(t), (6)
whichiswhatwecallthe Magnusexpansion.Themathematicalelaborationsexplainedinthenextsectiondetermine Ωk(t).
Herewejustwritedownthethreefirsttermsofthatseries:
Ω1(t)=
∫ t
0
A(t1)dt1,
Ω2(t)=
1
2
∫ t
0
dt1
∫ t1
0
dt2[A(t1),A(t2)] (7)
Ω3(t)=
1
6
∫ t
0
dt1
∫ t1
0
dt2
∫ t2
0
dt3([A(t1),[A(t2),A(t3)]]+[A(t3),[A(t2),A(t1)]])
where[A,B]≡AB−BAisthematrixcommutatorof AandB.
Theinterpretationoftheseequationsseemsclear: Ω1(t)coincidesexactlywiththeexponentin (2).Butthisequation
cannotgivethewholesolution,ashasalreadybeensaid.So,ifoneinsistsonhavinganexponentialsolution,theexponent
hastobecorrected.TherestoftheMEin (6)givesthatcorrection,necessarytokeeptheexponentialformofthesolution.
Thetermsappearingin (7)alreadysuggestthemostappealingcharacteristicofME.RememberthatamatrixLiealgebra
isalinearspaceinwhichonehasdefinedthecommutatorasthesecondinternalcompositionlaw.If,aswesuppose, A(t)
belongstoaLiealgebra gforallt,sodoesanysumofmultipleintegralsofnestedcommutators.Then,ifalltermsinMEhave
astructuresimilartothatoftheonesshownbefore,thewhole Ω(t)andanyapproximationtoitobtainedbytruncationof
ME,willalsobelongtothesameLiealgebra.Inthenextsection,itwillbeshownthatthisturnsouttobethecaseand, a
fortiori,itsexponentialwillbeinthecorrespondingLiegroup.
Whyisthissoimportantforphysicalapplications?Justbecausemanyofthepropertiesofevolutionoperatorsderived
fromfirstprinciplesarelinkedtothefactthattheybelongtoacertainLiegroup:e.g.unitarygroupinQuantumMechanics,
symplecticgroupinClassicalMechanics.Inthatway,useof(truncated)MEleadstoapproximationswhichshare,withthe
exactsolutionofEq. (4),importantqualitative(veryoften,geometric)properties.Forinstance,inQuantumMechanicsevery
approximantpreservesprobabilityconservation.
Fromthepresentpointofview,wecouldsaythatthelastparagraphssummarize,inanutshell,themaincontentsofthe
famouspaperofMagnusof1954.Withnoexaggeration,itsappearancecanbeconsideredaturningpointinthetreatment
oftheinitialvalueproblemdefinedby (4).
S.Blanesetal./PhysicsReports470(2009)151–238 155
Butimportantasitcertainlywas,Magnus’paperleftsomeproblems,atleastpartially,open:
•First,forwhatvaluesof tandforwhatoperators AdoesEq. (4)admitatrueexponentialsolution?This,wecallthe
existenceproblem.
•Second,forwhatvaluesof tandforwhatlinearoperators AdoestheseriesinEq. (6)converge?Thiswedescribeasthe
convergenceproblem.Wewanttoemphasizethat,althoughrelated,thesearetwodifferentproblems.Toseewhy,think
ofthescalarequation y′=y2withy(0)=1.Itssolution y(t)=(1−t)−1existsfor t⁄=1,butitsforminpowerseries
y(t)=∑∞
0 tnconvergesonlyfor |t|<1.
•Third,howdoesoneconstructhigherorderterms Ωk(t),k≥3,intheseries?Moreover,isthereaclosed-formexpression
forΩk(t)?
•Fourth,howdoesonecalculateinanefficientwayexp Ω[N],where Ω[N]≡∑N
k=1Ωk(t)isatruncationoftheME?
Allthesequestions,andmanyothers,willbedealtwithintherestofthepaper.Butbeforeenteringthatanalysis,we
thinkitisinterestingtopresentaview,howeverbrief,fromthehistoricalperspectiveofthehalf-centuryofdevelopments
ontheMagnusseries.Needlesstosay,webynomeanstrytopresentadetailedandexhaustivechronologicalaccountof
themanyapproachesfollowedbyauthorsfromverydifferentdisciplines.Tominimizeduplicationwithlatersections,we
simplymentionsomerepresentativesamples,sothatthereadercanunderstandtheevolutionofthefield.
Includingsomeprecedents,andwitha(asundeniableasunavoidable)doseofarbitrariness,wemaydistinguishfour
periodsinthehistoryofourtopic:
(1)Before1953.TheproblemwhichMEsolveshasacentennialhistorydatingbackatleasttotheworkofPeano,bythe
endof19thcentury,andBaker,atthebeginningofthe20th(forreferencestotheoriginalpapersseee.g.[ 8]).They
combinethetheoryofdifferentialequationswithanalgebraicformulation.Intimatelyrelatedtothesetreatmentsfrom
theverybeginning,isthestudyofthesocalledBaker–Campbell–Hausdorff(orBCHformulaforshort)[ 9–11]which
givesCintermsof A,Bandtheirmultiplenestedcommutatorswhenexpressingexp (A)exp(B)asexp(C).Thistopic
hasalonghistoryinitsownright,andwillalsobediscussedinSection 2.Asoneofitsearlyhallmarks,wequote[ 12].
InPhysicsliterature,theinterestintheproblemposedbyEq. (4)wasverymuchrevivedwiththeadventofQuantum
Electrodynamics(QED).TheworksofDyson[ 13]and,inparticular,Feynman[ 6]inthelatefortiesandearlyfifties,are
worthmentioninghere.
(2)1953–1970.Wehavequotedasthe‘birthcertificate’ofME,thepaper[ 4]byMagnusin1954.Thisisnotstrictlytrue:
thereisaResearchReport[ 14]datedJune1953whichdiffersfromthepublishedpaperinthetitleandinafewminor
details,andwhichshouldinfactbetakenasapreliminarydraftofit.Inbothpublications,theresultsummarizedabove
onMEappears,inalmostidenticalwords.TheworkofPechukasandLight[ 15]gave,forthefirsttime,amorespecific
analysisoftheproblemofconvergencethantherathervagueconsiderationsinMagnus’paper.WeiandNorman[ 16,
17]didthesamefortheexistenceproblem.Robinson,tothebestofourknowledge,seemstohavebeenthefirsttoapply
MEtoaphysicalproblem[ 18].SpecialmentioninthisperiodshouldbegiventoapaperbyWilcox[ 19],inwhichuseful
mathematicaltoolsaregiven,andMEispresentedtogetherwithotheralgebraictreatmentsofEq. (4),inparticular
Fer’sinfiniteproductexpansion[ 20].Alsoworthmentioninghere,isthefirstapplicationofMEasanumericaltoolfor
integratingthetime-independentSchrödingerequationforpotentialscattering,byChangandLight[ 21].
(3)1971–1990.Duringtheseyears,MEwasconsolidatedondifferentfronts.Itwassuccessfullyappliedtoawidespectrum
offieldsinPhysicsandChemistry:fromatomic[ 22]andmolecular[ 23]PhysicstoNuclearMagneticResonance
(NMR)[24,25]toQuantumElectrodynamics[ 26]andelementaryparticlePhysics[ 27].Anumberofcasestudiesalso
helpedtoclarifyitsmathematicalstructure,seeforexample[ 28].Theconstructionofhigherordertermswasapproached
fromdifferentangles.TheintrinsicandgrowingcomplexityofMEallowsfordifferentschemes.Onewhichhasshown
itselfveryusefulintacklingotherquestionsliketheconvergenceproblem,wastherecurrentschemebyKlarsfeldand
Oteo[29].
(4)Since1991.Thelastdecadeofthe20thcenturywitnessedarenewedinterestinME,whichstillcontinuesnow.Ithas
followeddifferentlines.ConcerningthebasicproblemsofexistenceandconvergenceofME,therehasbeendefinite
progress[30–33].MEhasalsobeenadaptedforspecifictypesofequations:Floquettheorywhen A(t)isaperiodic
function[34],stochasticdifferentialequations[ 35]orequationsoftheform Z′=AZ−ZB[36].Specialmentionshould
bemadeofthenewfield,openinthismostrecentperiod,thatusesMagnus’schemetobuildnovelalgorithms[ 37]
forthenumericalintegrationofdifferentialequationswithinthewidestfieldofgeometricintegration[ 38].After
optimization[39,40],theseintegratorshaveprovedtobehighlycompetitive.
Asproofofthepersistentimpactthe1954paperbyMagnushashadinscientificliterature,wepresentin Figs.1and2,the
numberofcitationsperyearandthecumulativenumberofcitations,respectively,asDecember2007withdatatakenfrom
ISIWebofScience.Theoriginalpaperappearsabout750timesofwhich,roughly,50,320and380correspond,respectively,
toeachofthelastthreeperiodswehaveconsidered.Theenduringinterestinthatseminalpaperisclearfromthefigures.
Thepresentationofthisreportisorganizedasfollows.Intheremainderofthissection,weincludesomemathematical
toolsandnotationsthatwillbeusedtimeandagaininourtreatment.InSection 2weformallyintroducetheMagnus
expansion,studyitsmainfeaturesandthoroughlyanalyzetheconvergenceissue.Next,inSection 3severalgeneralizations
oftheMagnusexpansionarereviewed,withspecialemphasisinitsapplicationtogeneralnonlineardifferentialequations.
InordertoillustratethemainpropertiesofME,inSection 4weconsidersimpleexamplesforwhichthecomputations
156 S.Blanesetal./PhysicsReports470(2009)151–238
Fig.1. PersistencyofMagnus’originalpaper:numberofcitationsperyear.
Fig.2. PersistencyofMagnus’originalpaper:cumulativenumberofcitations.
requiredarerelativelystraightforward.Section 5isdevotedtoanaspectthathasbeenmostrecentlystudiedinthissetting:
thedesignofnewalgorithmsforthenumericalintegrationofdifferentialequationsbasedontheMagnusexpansion.There,
afterabriefcharacterizationofnumericalintegrators,wepresentseveralmethodsthatareparticularlyefficient,asshown
bytheexamplesconsidered.Giventherelevanceofthenewnumericalschemes,webrieflyreviewinSection 6someofits
applicationsindifferentcontexts,rangingfromboundary-valueproblemstostochasticdifferentialequations.InSection 7,
ontheotherhand,applicationsoftheMEtosignificantphysicalproblemsareconsidered.Finally,thepaperendswithsome
concludingremarks.
1.2. Mathematicalpreliminariesandnotations
Herewecollect,forthereader’sconvenience,somemathematicalexpressions,terminologyandnotationswhichappear
mostfrequentlyinthetext.Needlesstosay,wehavemadenoattemptatbeingcompletelyrigorous.Wejusttrytofacilitate
thecasualreadingofisolatedsections.
Asalreadymentioned,thenaturalmathematicalhabitatformostoftheobjectswewilldealwithinthisreportisaLie
group,oritsassociatedLiealgebra.Althoughmostoftheresultsdiscussedinthesepagesarevalidinamoregeneralsetting,
wewillessentiallyconsideronlymatrixLiegroupsandalgebras.
ByaLiegroup Gweunderstandasetwhichcombinesanalgebraicstructurewithatopologicalone.Atthealgebraiclevel,
everytwoelementsof Gcanbecombinedbyaninternalcompositionlawtoproduceathirdelement,alsoin G.Thelawis
requiredtobeassociative,tohaveanidentityelement,andeveryelementmusthaveaninverse.Theordinaryproductand
theinverseoftheinvertiblematrix,playthatroleinthecaseswearemoreinterestedin.Thetopologicalexigenceforcesthe
compositionlawandtheassociationofaninversetobesufficientlysmoothfunctions.
S.Blanesetal./PhysicsReports470(2009)151–238 157
ALiealgebra gisavectorspacewhoseelementscanbecombinedbyasecondlaw,theLiebracket,whichwerepresent
by[A,B]= C,withA,B,Celementsof g,insuchawaythatthelawisbilinear,skew-symmetricandsatisfiesthewellknown
Jacobiidentity,
[A,[B,C]]+[ B,[C,A]]+[ C,[A,B]]= 0. (8)
Whendealingwithmatriceswetake,asLiebracket,thefamiliarcommutator:
[A,B]= AB−BA, A∈ g,B∈ g, (9)
whereABstandsfortheusualmatrixproduct.Ifweconsiderafinite-dimensionalLiealgebrawithdimension danddenote
byAi,i=1,..., d,thevectorsofoneofitsbases,thenthefundamentalbracketsonehastoknoware
[Ai,Aj]= ck
ijAk, (10)
wheresumoverrepeatedindexesisunderstood.Thecoefficients ck
ijaretheso-calledstructureconstantsofthealgebra.
Associatedwithany A∈ gwecandefinealinearoperatorad A: g→ gwhichactsaccordingto
adAB=[A,B], ad
j
AB=[A,ad
j−1
A B], ad0
AB=B, j∈ N,B∈ g. (11)
Alsoofinterest,istheexponentialofthisad Aoperator,
AdA=exp(adA), (12)
whoseactionon gisgivenby
AdA(B)=exp(A)Bexp(−A)=
∞∑
k=0
1
k!
adk
AB, B∈ g. (13)
The type of matrices we will handle more frequently are orthogonal, unitary and symplectic. Here are their
characterizationandthenotationweshallusefortheirgroupandalgebra.
Thespecialorthogonalgroup,SO (n),isthesetofall n×nrealmatriceswithunitdeterminantsatisfying ATA=AAT=I,
whereATisthetransposeof AandIdenotestheidentitymatrix.Thecorrespondingalgebra so(n)consistsoftheskew-
symmetricmatrices.
An×ncomplexmatrix Aiscalledunitaryif AĎA=AAĎ=I,where AĎistheconjugatetransposeorHermitianadjoint
ofA.Thespecialunitarygroup,SU (n),isthesetofall n×nunitarymatriceswithunitdeterminant.Thecorresponding
algebra su(n)consistsoftheskew-Hermitiantracelessmatrices.Specialrelevanceinsomequantummechanicalproblems
wediscusswillhavethecase n=2.Inthiscaseaconvenientbasisfor su(2)ismadeupbythePaulimatrices
σ1=
(
0 1
1 0
)
, σ 2=
(
0 −i
i 0
)
, σ 3=
(
1 0
0 −1
)
. (14)
Theysatisfytheidentity
σjσk=δjk+iϵjklσl, (15)
andcorrespondingly
[σj,σk]= 2iϵjklσl, (16)
whichdirectlygivethestructureconstantsforSU (2).Thefollowingidentitieswillproveusefulfor aandbin R3:
(a·σ)(b·σ)=a·bI+i(a×b)·σ, [a·σ,b·σ]= 2i(a×b)·σ, (17)
wherewehavedenoted σ=(σ1,σ2,σ3).AnyU∈SU(2)canbewrittenas
U=exp(ia·σ)=cos(a)I+i
sin(a)
a
a·σ, (18)
wherea=‖a‖=
√
a2
1+a2
2+a2
3.Amoreelaborateexpressionwhichweshallmakeuseof,inlatersections,is(with a=1)
exp(ia·σt)(b·σ)exp(−ia·σt)=b·σ+sin2t(b×a)·σ+sin2t(a×(b×a))·σ. (19)
InHamiltonianproblems,thesymplecticgroupSp (n)playsafundamentalrole.Itisthegroupof2 n×2nrealmatrices
satisfying
ATJA=J, withJ=
(
On In
−In On
)
(20)
andIndenotesthen-dimensionalidentitymatrix.ItscorrespondingLiealgebra sp(n)consistsofmatricesverifying BTJ+JB=
O2n.Infact,thesecanbeconsideredparticularinstancesoftheso-called J-orthogonalgroup,definedas[ 41]
OJ(n)={A∈GL(n):ATJA=J}, (21)
158 S.Blanesetal./PhysicsReports470(2009)151–238
whereGL(n)isthegroupofall n×nnonsingularrealmatricesand JissomeconstantmatrixinGL (n).Thus,onerecovers
theorthogonalgroupwhen J=I,thesymplecticgroupSp (n)whenJisthebasicsymplecticmatrixgivenin (20),andthe
LorentzgroupSO (3,1)whenJ=diag(1,−1,−1,−1).ThecorrespondingLiealgebraistheset
oJ(n)={B∈ gln(R):BTJ+JB=O}, (22)
where gln(R)istheLiealgebraofall n×nrealmatrices.If B∈oJ(n),thenitsCayleytransform
A=(I−αB)−1(I+αB) (23)
isJ-orthogonal.
AnotherimportantmatrixLiegroupnotincludedinthepreviouscharacterization,isthespeciallineargroupSL (n),
formedbyall n×nrealmatriceswithunitdeterminant.ThecorrespondingLiealgebra sl(n)comprisesalltracelessmatrices.
Forreal2 ×2matricesin sl(2)onehas
exp
(
a b
c −a
)
=


cosh(η)+
a
η
sinh(η)
b
η
sinh(η)
c
η
sinh(η) cosh(η)−
a
η
sinh(η)

 (24)
withη=
√
a2+bc.
Whendealingwithconvergenceproblemsitisnecessarytousesometypeofnormforamatrix.Bysuchwemeana
non-negativerealnumber ‖A‖associatedwitheachmatrix A∈ Cn×nandsatisfying
(a)‖A‖≥ 0forall Aand‖A‖= 0iff A=On.
(b)‖αA‖=| α|‖A‖,forallscalars α.
(c)‖A+B‖≤‖ A‖+‖ B‖.
Quiteoften,oneaddsthesub-multiplicativeproperty
‖AB‖≤‖ A‖‖B‖, (25)
butnotallmatrixnormssatisfythiscondition[ 42].
Thereexistdifferentfamiliesofmatrixnorms.Amongthemorepopularones,wehavethe p-norm‖A‖pandtheFrobenius
norm‖A‖F.Foramatrix Awithelements aij,i,j=1... n,theyaredefinedas
‖A‖p= max
‖x‖p=1
‖Ax‖p (26)
‖A‖F=
vuu√
n∑
i=1
n∑
j=1
|aij|2=
√
tr(AĎA), (27)
respectively,where‖x‖p=(∑n
j=1|xj|p)
1
pandtr(A)isthetraceofthematrix A.Althoughbothverify (25),thep-normshave
theimportantpropertythatforeverymatrix Aandx∈ Rnonehas‖Ax‖p≤‖A‖p‖x‖p.Themostused p-normscorrespond
top=1,p=2andp=∞.
Ofparamountimportanceinnumericallinearalgebraisthecase p=2.Theresulting2-normofavectorisnothingbut
theEuclideannorm,whereasinthematrixcaseitisalsocalledthespectralnormof Aandcanbecharacterizedasthesquare
rootofthelargesteigenvalueof AĎA.AfrequentlyusedinequalityrelatingtoFrobeniusandspectralnormsisthefollowing:
‖A‖2≤‖A‖F≤√
n‖A‖2. (28)
Infact,thislastinequalitycanbemademorestringent[ 43]:
‖A‖F≤
√
rank(A)‖A‖2. (29)
ConsideringinamatrixLiealgebra ganormsatisfyingproperty (25),itisclearthat ‖[A,B]‖≤ 2‖A‖‖B‖,andthead
operatordefinedby (11)isbounded,since
‖adA‖≤ 2‖A‖
foranymatrix A.
Amatrixnormissaidtobeunitarilyinvariantif ‖UAV‖=‖ A‖wheneverU,Vareunitarymatrices.Frobeniusand
p-normsarebothunitarilyinvariant[ 44].
InsomeofthemostbasicformulasfortheMagnusexpansion,therewillappeartheso-calledBernoullinumbers Bn,
whicharedefinedthroughthegeneratingfunction[ 45]
tezt
et−1
=
∞∑
n=0
Bn(z)
tn
n!, |t|<2π
S.Blanesetal./PhysicsReports470(2009)151–238 159
asBn=Bn(0).Equivalently,
x
ex−1
=
∞∑
n=0
Bn
n!
xn,
whereastheformula
ex−1
x
=
∞∑
n=0
1
(n+1)!
xn
willbealsousefulinthesequel.ThefirstfewnonzeroBernoullinumbersare B0=1,B1=− 1
2,B2= 1
6,B4=− 1
30.Ingeneral
onehas B2m+1=0form≥1.
2. TheMagnusexpansion(ME)
Magnus’proposalwithrespecttothelinearevolutionequation
Y′(t)=A(t)Y(t) (30)
withinitialcondition Y(0)=I,wastoexpressthesolutionastheexponentialofacertainfunction,
Y(t)=expΩ(t). (31)
Thisisincontrasttotherepresentation
Y(t)= T
(
exp
∫ t
0
A(s)ds
)
intermsofthe time-orderingoperator T introducedbyDyson[ 13].
Itturnsoutthat Ω(t)in(31)canbeobtainedexplicitlyinanumberofways.Thecrucialpointistoderiveadifferential
equationfortheoperator Ωthatreplaces (30).HerewereproducetheresultfirstestablishedbyMagnusasTheoremIII
in[4]:
Theorem1 (Magnus1954).LetA(t)beaknownfunctionof t(ingeneral,inanassociativering),andletY (t)beanunknown
functionsatisfying (30)withY(0)=I.Then,ifcertainunspecifiedconditionsofconvergencearesatisfied,Y (t)canbewrittenin
theform
Y(t)=expΩ(t),
where
dΩ
dt
=
∞∑
n=0
Bn
n!
adn
ΩA, (32)
andBnaretheBernoullinumbers.Integrationof (32),byiteration,leadstoaninfiniteseriesfor Ω,thefirsttermsofwhichare
Ω(t)=
∫ t
0
A(t1)dt1−
1
2
∫ t
0
[∫ t1
0
A(t2)dt2,A(t1)
]
dt1+··· .
2.1. AproofofMagnus’Theorem
Theproofofthistheoremislargelybasedonthederivativeofthematrixexponentialmap,whichwediscussnext.Given
ascalarfunction ω(t)∈ R,thederivativeoftheexponentialisgivenbydexp (ω(t))/dt=ω′(t)exp(ω(t)).Onecouldthink
ofasimilarformulaforamatrix Ω(t).However,thisisnotthecase,sinceingeneral [Ω,Ω′]⁄= 0.Instead,onehasthe
followingresult.
Lemma2. Thederivativeofamatrixexponentialcanbewrittenalternativelyas
(a)
d
dt
exp(Ω(t))=dexpΩ(t)(Ω′(t))exp(Ω(t)), (33)
(b)
d
dt
exp(Ω(t))=exp(Ω(t))dexp−Ω(t)(Ω′(t)), (34)
(c)
d
dt
exp(Ω(t))=
∫ 1
0
exΩ(t)Ω′(t)e(1−x)Ω(t)dx, (35)
160 S.Blanesetal./PhysicsReports470(2009)151–238
wheredexpΩ(C)isdefinedbyits(everywhereconvergent)powerseries
dexpΩ(C)=
∞∑
k=0
1
(k+1)!
adk
Ω(C)≡
exp(adΩ)−I
adΩ
(C). (36)
Proof.LetΩ(t)beamatrix-valueddifferentiablefunctionandset
Y(σ,t)≡ ∂
∂t
(exp(σΩ(t)))exp(−σΩ(t))
forσ,t∈ R.Differentiatingwithrespectto σ,
∂Y
∂σ = ∂
∂t
(exp(σΩ)Ω)exp(−σΩ)+ ∂
∂t
(exp(σΩ))(−Ω)exp(−σΩ)
=
(
exp(σΩ)Ω′+ ∂
∂t
(exp(σΩ))Ω
)
exp(−σΩ)− ∂
∂t
(exp(σΩ))Ωexp(−σΩ)=exp(σΩ)Ω′exp(−σΩ)
=exp(adσΩ)(Ω′)=
∞∑
k=0
σk
k!
adk
Ω(Ω′),
wherethefirstequalityinthelastlinefollowsreadilyfrom (12)and(13).Ontheotherhand
d
dt
(expΩ)exp(−Ω)=Y(1,t)=
∫ 1
0
∂
∂σ
Y(σ,t)dσ (37)
sinceY(0,t)=0,and
∫ 1
0
∂
∂σ
Y(σ,t)dσ=
∫ 1
0
∞∑
k=0
σk
k!
adk
Ω(Ω′)dσ=
∞∑
k=0
1
(k+1)!
adk
Ω(Ω′),
fromwhichformula (33)follows.Theconvergenceofthepowerseries (36)isaconsequenceoftheboundednessofthead
operator:‖adΩ‖≤ 2‖Ω‖.
Multiplyingbothsidesof (33)byexp(−Ω),wehave
e−ΩdeΩ
dt
=e−ΩdexpΩ(Ω′)eΩ=ead−ΩdexpΩ(Ω′)=
ead−Ω−I
ad−Ω
Ω′=dexp−Ω(Ω′)
fromwhich(34)followsreadily.Finally,Eq. (35)isobtainedbytaking
∫ 1
0
∂
∂σ
Y(σ,t)dσ=
∫ 1
0
exp(σΩ)Ω′exp(−σΩ)dσ
in(37). ■
AccordingtoRossmann[ 46]andSternberg[ 47],formula(33)wasfirstprovedbyF.Schurin1890[ 48]andwastakenup
laterfromadifferentpointofviewbyPoincaré(1899),whereastheintegralformulation (35)hasbeenderivedanumberof
timesinthephysicsliterature[ 19].
AsaconsequenceoftheInverseFunctionTheorem,theexponentialmaphasalocalinverseinthevicinityofapoint Ω
atwhichdexp Ω=(exp(adΩ)−I)/adΩisinvertible.Thefollowinglemmaestablisheswhenthistakesplace.
Lemma3 (Baker1905).Iftheeigenvaluesofthelinearoperator adΩaredifferentfrom 2mπiwithm ∈{± 1,±2,...},then
dexpΩisinvertible.Furthermore,
dexp−1
Ω (C)=
adΩ
eadΩ−I
C=
∞∑
k=0
Bk
k!
adk
Ω(C) (38)
andtheconvergenceofthe dexp−1
Ω expansioniscertainlyassuredif ‖Ω‖<π.
Proof.Theeigenvaluesofdexp Ωareoftheform
µ=
∑
k≥0
νk
(k+1)!=
eν−1
ν ,
whereνisaneigenvalueofad Ω.Byassumption,thevaluesof µarenon-zero,sothatdexp Ωisinvertible.Bydefinition
oftheBernoullinumbers,thecompositionof (38)with(36)givestheidentity.Convergencefor ‖Ω‖ < πfollowsfrom
‖adΩ‖≤ 2‖Ω‖andfromthefactthattheradiusofconvergenceoftheseriesexpansionfor x/(ex−1)is2π. ■
S.Blanesetal./PhysicsReports470(2009)151–238 161
Itremainstodeterminetheeigenvaluesoftheoperatorad Ω.Infact,itisnotdifficulttoshowthatif Ωhasneigenvalues
{λj, j=1,2,..., n},thenad Ωhasn2eigenvalues{λj−λk, j,k=1,2,..., n}.
Asaconsequenceofthepreviousdiscussion, Theorem1canberephrasedmorepreciselyinthefollowingterms.
Theorem4. ThesolutionofthedifferentialequationY ′=A(t)YwithinitialconditionY (0)=Y0canbewrittenasY (t)=
exp(Ω(t))Y0withΩ(t)definedby
Ω′=dexp−1
Ω (A(t)), Ω(0)=O, (39)
where
dexp−1
Ω (A)=
∞∑
k=0
Bk
k!
adk
Ω(A).
Proof.Comparingthederivativeof Y(t)=exp(Ω(t))Y0,
dY
dt
=
d
dt
(exp(Ω(t)))Y0=dexpΩ(Ω′)exp(Ω(t))Y0
withY′=A(t)Y,weobtain A(t)=dexpΩ(Ω′).Applyingtheinverseoperatordexp −1
Ω tothisrelationyieldsthedifferential
equation(39)forΩ(t). ■
TakingintoaccountthenumericalvaluesofthefirstfewBernoullinumbers,thedifferentialequation (39)therefore
becomes
Ω′=A(t)−
1
2
[Ω,A(t)]+
1
12
[Ω,[Ω,A(t)]]+··· ,
whichisnonlinearin Ω.Bydefining
Ω[0]=O, Ω[1]=
∫ t
0
A(t1)dt1,
andapplyingPicardfixedpointiteration,onegets
Ω[n]=
∫ t
0
(
A−
1
2
[Ω[n−1],A]+
1
12
[Ω[n−1],[Ω[n−1],A]]+···
)
dt1
andlimn→∞Ω[n](t)=Ω(t)inasuitablysmallneighborhoodoftheorigin.
2.2. FormulaeforthefirsttermsinMagnusexpansion
Supposenowthat Aisoffirstorderinsomeparameter εandtryasolutionintheformofaseries
Ω(t)=
∞∑
n=1
Ωn(t), (40)
whereΩnissupposedtobeoforder εn.Equivalently,wereplace AbyεAin(30)anddeterminethesuccessivetermsof
Ω(t)=
∞∑
n=1
εnΩn(t). (41)
Thiscanbedoneexplicitly,atleastforthefirstterms,bysubstitutingtheseries (41)in(39)andequatingpowersof ε.
Obviously,theMagnusseries (40)isrecoveredbytaking ε=1.Thus,usingthenotation A(ti)≡Ai,thefirstfourorders
read
(1) Ω′
1=A,sothat
Ω1(t)=
∫ t
0
dt1A1. (42)
(2) Ω′
2=− 1
2[Ω1,A].Thus
Ω2(t)=
1
2
∫ t
0
dt1
∫ t1
0
dt2[A1,A2]. (43)
(3) Ω′
3=− 1
2[Ω2,A]+ 1
12[Ω1,[Ω1,A]].Aftersomework,andusingtheformula
∫ α
0
dx
∫ x
0
f(x,y)dy=
∫ α
0
dy
∫ α
y
f(x,y)dx (44)
162 S.Blanesetal./PhysicsReports470(2009)151–238
weobtain
Ω3(t)=
1
6
∫ t
0
dt1
∫ t1
0
dt2
∫ t2
0
dt3{[A1,[A2,A3]]+[[ A1,A2],A3]}. (45)
(4) Ω′
4=− 1
2[Ω3,A]+ 1
12[Ω2,[Ω1,A]]+ 1
12[Ω1,[Ω2,A]],whichyields
Ω4(t)=
1
12
∫ t
0
dt1
∫ t1
0
dt2
∫ t2
0
dt3
∫ t3
0
dt4{[[[A1,A2],A3]A4]
+[A1,[[A2,A3],A4]]+[ A1,[A2,[A3,A4]]]+[ A2,[A3,[A4,A1]]]}. (46)
Theapparentsymmetryintheformulaeaboveisdeceptive.Highordersrequirerepeateduseof (44)andbecomeunwieldy.
PratoandLamberti[ 49]giveexplicitlythefifthorderusinganalgorithmicpointofview.Onecanalsofindintheliterature,
quiteinvolvedexplicitexpressionsforanarbitraryorder[ 50–54].Inthenextsubsectionwedescribearecursiveprocedure
togeneratethetermsintheexpansion.
2.3. Magnusexpansiongenerator
Theaboveprocedurecan,indeed,providearecursiveproceduretogenerateallthetermsintheMagnusseries (40).Thus,
bysubstituting Ω(t)=∑∞
n=1ΩnintoEq.(39)andequatingtermsofthesameorder,onegetsingeneral
Ω′
1=A
Ω′
n=
n−1∑
j=1
Bj
j!
S(j)
n , n≥2, (47)
where
S(k)
n =
∑
[Ωi1,[...[Ωik,A]...]] (i1+···+ ik=n−1). (48)
Noticethat,inthelastequation,theorderin Ahasbeenexplicitlyreckoned,whereas krepresentsthenumberof Ω’s.The
newlydefinedoperators S(k)
n canagainbecalculatedrecursively.Therecurrencerelationsarenowgivenby
S(j)
n =
n−j∑
m=1
[
Ωm,S(j−1)
n−m
]
, 2≤j≤n−1 (49)
S(1)
n =[Ωn−1,A], S(n−1)
n =adn−1
Ω1 (A).
Afterintegrationwereachthefinalresultintheform
Ω1=
∫ t
0
A(τ)dτ
Ωn=
n−1∑
j=1
Bj
j!
∫ t
0
S(j)
n (τ)dτ, n≥2. (50)
Alternatively,theexpressionof S(k)
n givenby (48)canbeinsertedinto (50),thusarrivingat
Ωn(t)=
n−1∑
j=1
Bj
j!
∑
k1+···+kj=n−1
k1≥1,...,kj≥1
∫ t
0
adΩk1(s)adΩk2(s)··· adΩkj(s)A(s)ds n≥2. (51)
Noticethateachterm Ωn(t)intheMagnusseriesisamultipleintegralofcombinationsof n−1nestedcommutators
containingnoperatorsA(t).If,inparticular, A(t)belongstosomeLiealgebra g,thenitisclearthat Ω(t)(andinfact
anytruncationoftheMagnusseries)alsostaysin gandthereforeexp (Ω)∈ G,where GdenotestheLiegroupwhose
correspondingLiealgebra(thetangentspaceattheidentityof G)is g.
2.4. Magnusexpansionandtime-dependentperturbationtheory
ItisnotdifficulttoestablishaconnectionbetweenMagnusseriesandDysonperturbativeseries[ 13].Thelattergivesthe
solutionof(30)as
Y(t)=I+
∞∑
n=1
Pn(t), (52)
S.Blanesetal./PhysicsReports470(2009)151–238 163
wherePnaretime-orderedproducts
Pn(t)=
∫ t
0
dt1...
∫ tn−1
0
dtnA1A2... An,
whereAi≡A(ti).Then
∞∑
j=1
Ωj(t)=log
(
I+
∞∑
j=1
Pj(t)
)
.
AsstatedbySalzman[ 55],
Ωn=Pn−
n∑
j=2
(−1)n
j
R(j)
n , n≥2, (53)
where
R(k)
n =
∑
Pi1Pi2... Pik (i1+···+ ik=n)
obeysthequadraticrecursionformula
R(j)
n =
n−j+1∑
m=1
R(1)
mR(j−1)
n−m, (54)
R(1)
n =Pn, R(n)
n =Pn
1.
Eq.(54)representstheMagnusexpansiongeneratorinSalzman’sapproach.Itmaybeusefultowritedownthefirstfew
equationsprovidedbythisformalism:
Ω1=P1
Ω2=P2−
1
2
P2
1 (55)
Ω3=P3−
1
2
(P1P2+P2P1)+
1
3
P3
1.
AsimilarsetofequationswasdevelopedbyBurum[ 56],thusproviding
P1=Ω1,
P2=Ω2+
1
2!Ω2
1, (56)
P3=Ω3+
1
2!(Ω1Ω2+Ω2Ω1)+
1
3!Ω3
1
andsoon.Thegeneraltermreads
Ωn=Pn−
n∑
j=2
1
j
Q(j)
n , n≥2, (57)
where
Q(k)
n =
∑
Ωi1... Ωik, (i1+···+ ik=n). (58)
Asbefore,subscriptsindicatetheorderwithrespecttotheparameter ε,whilesuperscriptsrepresentthenumberoffactors
ineachproduct.Thus,thesummationin (58)extendsoverallpossibleproductsof k(ingeneralnon-commuting)operators
Ωisuchthattheoverallorderofeachtermisequalto n.Byregroupingterms,onehas
Q(k)
n = Ω1
∑
i2+···+ik=n−1
Ωi2··· Ωik+Ω2
∑
i2+···+ik=n−2
Ωi2··· Ωik+···+ Ωn−k+1
∑
i2+···+ik=k−1
Ωi2··· Ωik, (59)
whereQ(j)
n mayalsobeobtainedrecursivelyfrom
Q(j)
n =
n−j+1∑
m=1
Q(1)
m Q(j−1)
n−m , (60)
Q(1)
n =Ωn, Q(n)
n =Ωn
1.
Byworkingoutthisrecurrence,onegetsthesameexpressionsas (54)forthefirstterms.Furtheraspectsoftherelationship
betweenMagnus,Dysonseriesandtime-orderedproductscanbefoundin[ 57,58].
164 S.Blanesetal./PhysicsReports470(2009)151–238
2.5. GraphtheoreticalanalysisofMagnusexpansion
Thepreviousrecursionsallowus,inprinciple,toexpressany ΩkintheMagnusseriesintermsof Ω1,..., Ωk−1.Infact,
thisprocedurehassomeadvantagesfromacomputationalpointofview.Ontheotherhand,aswehavementionedbefore,
whentherecursionsaresolvedexplicitly, Ωkcanbeexpandedasalinearcombinationoftermsthatarecomposedfrom
integralsandcommutatorsactingiterativelyon A.Theactualexpression,however,becomesincreasinglycomplexwith k,as
itshouldbeevidentfromthefirstterms (42)–(46).AnalternativeformoftheMagnusexpansion,amenablealsoforrecursive
derivationbyusinggraphicaltools,canbeobtainedbyassociatingeachtermintheexpansionwitha binaryrootedtree ,an
approachworkedoutbyIserlesandNørsett[ 37].Forcompleteness,inthesequel,weshowtheequivalenceoftherecurrence
(49)–(50)withthisgraphtheoreticalapproach.
Inessence,theideaofIserlesandNørsettistoassociateeachtermin Ωkwitharootedtree,accordingtothefollowing
prescription.
Let T0bethesetconsistingofthesinglerootedtreewithonevertex,then T0={ s},establishtherelationshipbetween
thistreeand Athroughthemap
s↝A(t)
anddefinerecursively
Tm=
{
@ 
τ1
τ2 :τ1∈ Tk1, τ2∈ Tk2,k1+k2=m−1
}
.
Next,giventwoexpansionterms Hτ1andHτ2,whichhavebeenassociatedpreviouslywith τ1∈ Tk1andτ2∈ Tk2,respectively
(k1+k2=m−1),weassociate
Hτ(t)=
[∫ t
0
Hτ1(ξ)dξ,Hτ2(t)
]
withτ=@ 
τ1
τ2
.
Thus,eachHτforτ∈ Tminvolvesexactlymintegralsandmcommutators.
Thesecompositionrulesestablishaone-to-onerelationshipbetweenarootedtree τ ∈ T ≡∪ m≥0 Tm,andamatrix
functionHτ(t)involvingA,multivariateintegralsandcommutators.
Fromhereitiseasytodeducethatevery τ∈ Tm,m≥1,canbewritteninauniquewayas
τ=@ 
τ1
@ 
τ2
@
τ3
@ 
s
τs
....
orτ≡a(τ1,τ2,...,τ s).ThentheMagnusexpansioncanbeexpressedintheform[ 37,59]
Ω(t)=
∞∑
m=0
∑
τ∈Tm
α(τ)
∫ t
0
Hτ(ξ)dξ, (61)
withthescalar α( s)=1 and,ingeneral,
α(τ)=
Bs
s!
s∏
l=1
α(τl).
Letusillustratethisprocedurebywritingdown,explicitly,thefirsttermsintheexpansioninatreeformalism.In T1we
onlyhavek1=k2=0,sothatasingletreeispossible,
τ1= s, τ 2= s, ⇒ τ=@ 
s
s
,
withα(τ)=−1/2.In T2therearetwopossibilities,namely k1=0,k2=1and k1=1,k2=0,andthusonegets
τ1= s, τ 2=@ 
s
s
⇒ τ=@ 
@ 
s
s
s
, α(τ) = 1
12
τ1=@ 
s
s
, τ 2= s ⇒ τ= @ 
@ 
s
s
s
α(τ)= 1
4
S.Blanesetal./PhysicsReports470(2009)151–238 165
andtheprocesscanberepeatedforany Tm.Thecorrespondencebetweentreesandexpansiontermsshouldbeclearfrom
thepreviousgraphs.Forinstance,thelasttreeisnothingbuttheintegralof A,commutedwith A,integratedandcommuted
withA.Inthatway,bytruncatingtheexpansion (61)atm=2wehave
Ω(t)=
s
−
1
2
@ 
s
s
+
1
4
@ 
@ 
s
s
s
+
1
12
@ 
@ 
s
s
s
+··· , (62)
i.e.,theexplicitexpressionscollectedinSection 2.2.
Finally,therelationshipbetweenthetreeformalismandtherecurrence (49)–(50)canbeestablishedasfollows.From
(61)wecanwrite
∞∑
m=1
∑
τ∈Tm
α(τ)Hτ(t)=
m∑
s=1
Bs
s!
∑
k1,...,ks
k1+···+ks=m−s
∑
τi∈Tki
α(τ1)··· α(τs)Ha(τ1,...,τs).
Thus,bycomparing (50)and(61)wehave
Ωm(t)=
∑
τ∈Tm−1
α(τ)
∫ t
0
Hτ(ξ)dξ=
m−1∑
j=1
Bj
j!
∫ t
0
S(j)
m(ξ)dξ
sothat
S(j)
m =
∑
k1,...,kj
k1+···+kj=m−1−j
∑
τi∈Tki
α(τ1)··· α(τj)Ha(τ1,...,τj).
Inotherwords,eachterm S(j)
n intherecurrence (49)carriesonacompletesetofbinarytrees.Althoughbothproceduresare
equivalent,theuseof (49)and(50)canbeparticularlywellsuitedwhenhighordersoftheexpansionareconsidered,for
tworeasons:(i)theenormousnumberoftreesinvolvedforlargevaluesof mand(ii)in (61)manytermsareredundant,and
acarefulgraphtheoreticalanalysisisneededtodeducewhichtermshavetobediscarded[ 37].
Recently,anME-typeformalismhasbeendevelopedinthemoreabstractsettingofdendriformalgebras.Thisgeneralized
expansionincorporatestheusualoneasalimit,butisformulatedmoreinlinewith(non-commutative)Butcherseries.In
thiscontext,theuseofplanarrootedtreestorepresenttheexpansionandtheso-calledpre-Lieproduct,allowsonetoreduce
thenumberoftermsateachorderincomparisonwithexpression (61)[60].
2.6. Time-symmetryoftheexpansion
Themap ϕt:Y(t0)−→Y(t)correspondingtothelineardifferentialequation (30)withY(t0)=Y0istimesymmetric,
ϕ−t◦ϕt=Id,sinceintegrating (30)fromt=t0tot=tfforeverytf≥t0andbackto t0leadsustotheoriginalinitialvalue
Y(t0)=Y0.Observethat,accordingto (3),themap ϕtcanbeexpressedintermsofthefundamentalmatrix(orevolution
operator)U(t,t0)asϕtf(Y0)=U(tf,t0)Y0.Thentime-symmetryestablishesthat
U(t0,tf)=U−1(tf,t0)
or,intermsoftheMagnusexpansion,
Ω(tf,t0)=−Ω(t0,tf).
Totakeadvantageofthisfeature,letuswritethesolutionof (30)atthefinaltime tf=t0+sas
Y
(
t1/2+
s
2
)
=exp
(
Ω
(
t1/2+
s
2
,t1/2−
s
2
))
Y
(
t1/2−
s
2
)
, (63)
wheret1/2=(t0+tf)/2.Then
Y
(
t1/2−
s
2
)
=exp
(
−Ω
(
t1/2+
s
2
,t1/2−
s
2
))
Y
(
t1/2+
s
2
)
. (64)
Ontheotherhand,thesolutionat t0canbewrittenas
Y
(
t1/2−
s
2
)
=exp
(
Ω
(
t1/2−
s
2
,t1/2+
s
2
))
Y
(
t1/2+
s
2
)
, (65)
166 S.Blanesetal./PhysicsReports470(2009)151–238
sothat,bycomparing (64)and(65),
Ω
(
t1/2−
s
2
,t1/2+
s
2
)
=−Ω
(
t1/2+
s
2
,t1/2−
s
2
)
(66)
andthus Ωdoesnotcontainevenpowersof s.If A(t)isananalyticfunctionandaTaylorseriescenteredaround t1/2is
considered,theneachtermin Ωkisanoddfunctionof sand,inparticular, Ω2i+1(s)= O(s2i+3).Thisfacthasbeennoticedin
[61,62]andwillbefullyexploitedinSection 5.4whenanalyzingtheMagnusexpansionasanumericaldeviceforintegrating
differentialequations.
2.7. ConvergenceoftheMagnusexpansion
Aswepointedoutintheintroduction,fromamathematicalpointofview,thereareatleasttwodifferentissuesof
paramountimportanceattheverybasisoftheMagnusexpansion:
(1)(Existence).Forwhatvaluesof tandforwhatoperators AdoesEq. (30)admitanexponentialsolutionintheform
Y(t)=exp(Ω(t))foracertain Ω(t)?
(2)(Convergence).Givenacertainoperator A(t),forwhatvaluesof tdoestheMagnusseries (40)converge?
Ofcourse,giventherelevanceoftheexpansion,bothproblemshavebeenextensivelytreatedintheliteraturesince
Magnusproposedthisformalismin1954.Wenextreviewsomeofthemostrelevantcontributionsavailableregardingboth
aspects,withspecialemphasisontheconvergenceoftheMagnusseries.
2.7.1. Ontheexistenceof Ω(t)
Inmostcases,oneisinterestedinthecasewhere AbelongstoaLiealgebra gunderthecommutatorproduct.Inthis
generalsetting,theMagnustheoremcanbeformulatedasfourstatementsconcerningthesolutionof Y′=A(t)Y,eachone
morestringentthanthepreceding[ 16].Specifically,
(A)Thedifferentialequation Y′=A(t)Yhasasolutionoftheform Y(t)=expΩ(t).
(B)Theexponent Ω(t)liesintheLiealgebra g.
(C)Theexponent Ω(t)isacontinuousdifferentiablefunctionof A(t)andt,satisfyingthenonlineardifferentialequation
Ω′=dexp−1
Ω (A(t)).
(D)Theoperator Ω(t)canbecomputedbytheMagnusseries (40).
Letusnowanalyzeindetailtheconditionsunderwhichstatements(A)–(D)hold.
(A)IfA(t)andY(t)aren×nmatrices,fromwell-knowngeneraltheoremsondifferentialequationsitisclearthattheinitial
valueproblemdefinedby (30)andY(0)=Ialwayshasauniquelydeterminedsolution Y(t)whichiscontinuousandhas
acontinuousfirstderivativeinanyintervalinwhich A(t)iscontinuous[ 63].Furthermore,thedeterminantof Yisalways
differentfromzero,since
detY(t)=exp
(∫ t
0
trA(s)ds
)
.
Ontheotherhand,itiswellknownthatanymatrix Ycanbewrittenintheformexp Ωifandonlyifdet Y⁄=0[64,p.239],
sothatitisalwayspossibletowrite Y(t)=expΩ(t).
InthegeneralcontextofLiegroupsandLiealgebras,itisindeedtheregularityoftheexponentialmapfromtheLiealgebra
gtotheLiegroup Gthatdeterminestheglobalexistenceofan Ω(t)∈ g[65,66]:theexponentialmapofacomplexLiealgebra
isgloballyone-to-oneifandonlyifthealgebraisnilpotent,i.e.thereexistsafinite nsuchthatad x1adx2··· adxn−1xn=0,
wherexjarearbitraryelementsfromtheLiealgebra.Ingeneral,however,theinjectivityoftheexponentialmapisonly
assuredfor ξ∈ gsuchthat‖ξ‖<ρ Gforarealnumber ρG>0andsomenormin g[32,67].
(B)Althoughinprinciple ρGconstitutesasharpupperboundforthemereexistenceoftheoperator Ω∈ g,itspractical
valueinthecaseofdifferentialequationsislessclear.Aswehavenoticed,anynonsingularmatrixhasalogarithm,butthis
logarithmmightbein gl(n, C)evenwhenthematrixisreal.Thelogarithmof Y(t)maybecomplexevenforreal A(t)[16].
Insuchasituation,thesolutionof (30)cannotbewrittenastheexponentialofamatrixbelongingtotheLiealgebraoverthe
fieldofrealnumbers.Onemightarguethatthisisindeedpossibleoverthefieldofcomplexnumbers,but(i)theelement
ΩcannotbecomputedbytheMagnusseries (40),sinceitcontainsonlyrealrationalcoefficients,and(ii)examplesexist
wherethelogarithmofacomplexmatrixdoesnotlieinthecorrespondingLiesubalgebra[ 16].
Itisthereforeinterestingtodetermineforwhichrangeof tareal A(t)in(30)leadstoareallogarithm.Thisissuehas
beentackledbyMoanin[ 67]inthecontextofacompletenormed(Banach)algebra,provingthatif
∫ t
0
‖A(s)‖2ds<π (67)
thenthesolutionof (30)canindeedbewrittenas Y(t)=expΩ(t),where Ω(t)isintheBanachalgebra.
S.Blanesetal./PhysicsReports470(2009)151–238 167
(C)Inhisoriginalpaper[ 4],Magnuswaswellawarethatifthefunction Ω(t)isassumedtobedifferentiable,itmaynotexist
everywhere.Infact,herelatedthedifferentiabilityissuetotheproblemofsolvingdexp Ω(Ω′)=A(t)withrespectto Ω′
andprovidedanimplicitconditionforanarbitrary A.Morespecifically,heprovedthefollowingresultforthecaseof n×n
matrices(TheoremVin[ 4]).
Theorem5. TheequationA (t)=dexpΩ(Ω′)canbesolvedby Ω′=dexp−1
Ω A(t)foranarbitraryn ×nmatrixAifandonlyif
noneofthedifferencesbetweenanytwooftheeigenvaluesof Ωequals2πim,wherem =±1,±2,...,( m⁄=0).
Thisresultcanbeconsidered,infact,asareformulationof Lemma3,but,unfortunately,doesnothaveverymuchpractical
applicationunlesstheeigenvaluesof Ω caneasilybedeterminedfromthoseof A(t).Onewouldinsteadliketohave
conditionsbaseddirectlyon A.
2.7.2. ConvergenceoftheMagnusseries
Fordealingwiththevalidityofstatement(D)onehastoanalyzetheconvergenceoftheseries
∑∞
k=1Ωk.Magnusalso
consideredthequestionofwhentheseriesterminatesatsomefiniteindex m,thusgivingagloballyvalid Ω=Ω1+···+ Ωm.
Thiswillhappen,forinstance,if
[
A(t),
∫ t
0
A(s)ds
]
=0
identicallyforallvaluesof t,sincethen Ωk=0for k>1.Asufficient(butnotnecessary)conditionforthevanishingofall
termsΩkwithk>nisthat
[A(s1),[A(s2),[A(s3),..., [A(sn),A(sn+1)]...]]]= 0
foranychoiceof s1,..., sn+1.Infact,theterminationoftheseriescannotbeestablishedsolelybyconsiderationofthe
commutativityofA(t)withitself,andMagnusconsideredanexampleillustratingthispoint.
Ingeneral,however,theMagnusseriesdoesnotconvergeunless Aissmallinasuitablesense.Severalboundstothe
actualradiusofconvergenceintermsof Ahavebeenobtainedintheliterature.Mostoftheseresultscanbestatedas
follows.If Ωm(t)denotesthehomogeneouselementwith m−1commutatorsintheMagnusseries,asgivenby (51),then
Ω(t)=∑∞
m=1Ωm(t)isabsolutelyconvergentfor0 ≤t<T,with
T=max
{
t≥0:
∫ t
0
‖A(s)‖2ds<rc
}
. (68)
Thus,bothPechukasandLight[ 15]andKarasevandMosolova[ 68]obtained rc=log2=0.693147..., whereasChacon
andFomenko[ 69]got rc=0.57745....In1998,Blanesetal.[ 30]andMoan[ 70]obtainedindependentlytheimproved
bound
rc=
1
2
∫ 2π
0
1
2+ x
2(1−cot x
2)
dx≡ξ=1.08686870... (69)
byanalyzingtherecurrence (49)–(50)and(51),respectively.Furthermore,Moanalsoobtainedaboundontheindividual
terms ΩmoftheMagnusseries[ 67]whichisuseful,inparticular,forestimatingerrorswhentheseriesistruncated.
Specifically,heshowedthat
‖Ωm(t)‖≤
fm
2
(
2
∫ t
0
‖A(s)‖2ds
)m
≤π
(
1
ξ
∫ t
0
‖A(s)‖2ds
)m
,
wherefmarethecoefficientsof
G−1(x)=
∑
m≥1
fmxm=x+
1
4
x2+
5
72
x3+
11
576
x4+
479
86400
x5+··· ,
theinversefunctionof
G(s)=
∫ s
0
1
2+ x
2(1−cot x
2)
dx.
Ontheotherhand,byanalyzingsomeselectedexamples,Moan[ 67]concludedthat,inordertogetconvergence forall
realmatricesA (t),itisnecessarythat rc≤πin(68),andmorerecentlyMoanandNiesen[ 71]havebeenabletoprovethat,
indeed,rc=πprovidedonlyrealmatricesareinvolved.
Inanycase,itisimportanttoremarkthatstatement(D)islocallyvalid,butcannotbeusedtocompute Ωinthelarge.
However,aswehaveseen,theotherstatementsneednotdependonthevalidityof(D).Inparticular,if(B)and(C)are
globallyvalid,onecanstillinvestigatemanyofthepropertiesof Ω,eventhoughonecannotcomputeitwiththeaidof(D).
168 S.Blanesetal./PhysicsReports470(2009)151–238
2.7.3. Animprovedradiusofconvergence
ThepreviousresultsontheconvergenceoftheMagnusserieshavebeenestablishedfor n×nrealmatrices:if A(t)isa
realn×nmatrix,then(67)givesaconditionfor Y(t)tohaveareallogarithm.Infact,underthesamecondition,theMagnus
series(40)convergespreciselytothislogarithm,i.e.,itssum Ω(t)satisfiesexp(Ω(t))=Y(t)[71].
Oneshouldhaveinmind,however,thattheoriginalexpansionwasconceivedbyrequiringonlythat A(t)bealinear
operatordependingonarealvariable tinanassociativering( Theorem1).Theideawastodefine,intermsof A,anoperator
Ω(t)suchthatthesolutionoftheinitialvalueproblem Y′=A(t)Y,Y(0)=I,forasecondoperator Yisgivenas Y=expΩ.
Theproposedexpressionfor Ωisaninfiniteseries,satisfyingtheconditionthat‘‘itspartialsumsbecomeHermitianafter
multiplicationbyiifiAisaHermitianoperator’’[ 4].Asthisquotationillustrates,Magnusexpansionwasfirstderivedinthe
contextofquantummechanics,andsoonetypicallyassumesthatitisalsovalidwhen A(t)isalinearoperatorinaHilbert
space.Therefore,itmightbedesirabletohaveconditionsfortheconvergenceoftheMagnusseriesinthismoregeneral
setting.In[ 31],byapplyingstandardtechniquesofcomplexanalysisandsomeelementarypropertiesoftheunitsphere,
thebound rc= πhasbeenshowntobealsovalidfor anyboundednormaloperator A(t)inaHilbertspaceofarbitrary
dimension.Nextwereviewthemainissuesinvolvedandreferthereaderto[ 31]foramoredetailedtreatment.
Letusassumethat A(t)isaboundedoperatorinaHilbertspace H,with2 ≤dim H≤∞.Thenweintroduceanew
parameterε∈ Canddenoteby Y(t;ε)thesolutionoftheinitialvalueproblem
dY
dt
=εA(t)Y, Y(0)=I, (70)
whereInowdenotestheidentityoperatorin H.Itisknownthat Y(t;ε)isananalyticfunctionof εforafixedvalueof t.Let
usintroducetheset Bγ⊂ Ccharacterizedbytherealparameter γ,
Bγ=
{
ε∈ C:|ε|
∫ t
0
‖A(s)‖ds<γ
}
.
Here‖.‖standsforthenormdefinedbytheinnerproducton H,i.e.,the2-normintroducedinSection 1.2.
Iftisfixed,theoperatorfunction ϕ(ε) = logY(t;ε)iswelldefinedin Bγ whenγ issmallenough,say γ < log2,
asananalyticfunctionof ε.Asamatteroffact,thisisadirectconsequenceoftheresultscollectedinSection 2.7.2:if,
inparticular, |ε|
∫t
0‖A(s)‖ds < log2,theMagnusseriescorrespondingto (70)convergesanditssum Ω(t;ε)satisfies
exp(Ω(t;ε))=Y(t;ε).Inotherwords,thepowerseries Ω(t;ε)coincideswith ϕ(ε)when|ε|
∫t
0‖A(s)‖ds<log2,andso
theMagnusseriesisthepowerseriesexpansionof ϕ(ε)aroundε=0.
Theorem6. Thefunction ϕ(ε)=logY(t;ε)isananalyticfunctionof εinthesetB π,with
Bπ=
{
ε∈ C:|ε|
∫ t
0
‖A(s)‖ds<π
}
.
If Hisinfinitedimensional,thestatementholdstrueifYisanormaloperator.
Inotherwords, γ=π.Theproofofthistheoremisbasedonsomeelementarypropertiesoftheunitsphere S1inaHilbert
space.Letusdefinetheanglebetweenanytwovectors x⁄=0,y⁄=0in H,Ang{x,y}= α,0≤α≤π,from
cosα=
Re⟨x,y⟩
‖x‖‖y‖,
where⟨·,·⟩istheinnerproducton H.Thisangleisametricin S1,i.e.,thetriangleinequalityholdsin S1.
Thefirstpropertyweneedisgivenbythenextlemma[ 67].
Lemma7. Foranyx ∈ H,x⁄=0,Ang{Y(t;ε)x,x}≤| ε|
∫t
0‖A(s)‖ds.
Observethatif Yisanormaloperatorin H,i.e., YY Ď=Y ĎY(inparticular,if Yisunitary),then ‖Y Ďx‖=‖ Yx‖forall x∈ H
andthereforeAng{Y Ďx,x}= Ang{Yx,x}.
Thesecondrequiredpropertyprovidesusefulinformationonthelocationoftheeigenvaluesofagivenboundedoperator
in H[72].
Lemma8. LetTbea(bounded)operatoron H.If Ang{Tx,x}≤ γ andAng{T Ďx,x}≤ γ foranyx ⁄= 0,x ∈ H,whereT Ď
denotestheadjointoperatorofT,thenthespectrumofT, σ(T),iscontainedintheset
∆γ={z=|z|eiω∈ C:|ω|≤ γ}.
Proof(ofTheorem6).Letusintroducetheoperator T≡Y(t;ϵ),with ε∈Bγ,γ <π.Thenby Lemma7,Ang{Tx,x}≤ γfor
allx⁄=0,andthus,by Lemma8,
σ(T)⊂∆γ. (71)
Ifdim H=∞ andweassumethat Y(t;ϵ)isanormaloperator,then (71)alsoholds.
S.Blanesetal./PhysicsReports470(2009)151–238 169
FromEq.(70)inintegralform,
Y(t;ε)=I+ε
∫ t
0
A(s)Yds,
onegets‖Y‖≤ 1+|ε|
∫t
0‖A(s)‖‖Y‖ds,andapplicationofGronwall’slemma[ 73]leadsto
‖Y(t;ε)‖≤ exp
(
|ε|
∫ t
0
‖A(s)‖ds
)
.
Ananalogousreasoningfortheinverseoperatoralsoprovesthat
‖Y−1(t;ε)‖≤ exp
(
|ε|
∫ t
0
‖A(s)‖ds
)
.
Inconsequence,
‖T‖≤ eγ and ‖T−1‖≤ eγ.
Ifλ⁄=0∈σ(T),then|λ|≤‖ T‖[74]andtherefore |λ|≤ eγ.Inaddition, 1
λ∈σ(T−1),sothat |λ|≥ e−γ.Equivalently,
σ(T)⊂{z∈ C:e−γ≤|z|≤ eγ}≡ Gγ. (72)
Puttingtogether(71)and(72),onehas
σ(T)⊂Gγ∩∆γ≡Λγ.
Nowchooseanyvalue γ′suchthat γ <γ′<π (e.g.,γ′=(γ+π)/2)andconsidertheclosedcurve Γ=∂Λγ′.Noticethat
thecurve Γenclosesσ(T)initsinterior,sothatitispossibletodefine[ 75]thefunction ϕ(ε)=logY(t;ε)bytheequation
ϕ(ϵ)=
1
2πi
∫
Γ
logz(zI−Y(t;ϵ))−1dz, (73)
wheretheintegrationalong Γ isperformedinthecounterclockwisedirection.Asiswellknown, (73)definesananalytic
functionof εinBγ′[75]andtheresultofthetheoremfollows. ■
Theorem9. LetusconsiderthedifferentialequationY ′=A(t)YdefinedinaHilbertspace HwithY (0)=I,andletA (t)bea
boundedoperatorin H.Then,theMagnusseries Ω(t)=∑∞
k=1Ωk(t),with Ωkgivenby(51)convergesintheintervalt ∈[0,T)
suchthat
∫ T
0
‖A(s)‖ds<π
andthesum Ω(t)satisfiesexpΩ(t)=Y(t).Thestatementalsoholdswhen Hisinfinite-dimensionalifYisanormaloperator
(inparticular,ifYisunitary).
Proof.Theorem6 showsthatlog Y(t;ε)≡ϕ(ε)isawelldefinedandanalyticfunctionof εfor
|ε|
∫ t
0
‖A(s)‖ds<π.
IthasalsobeenshownthattheMagnusseries Ω(t;ε)= ∑∞
k=1εkΩk(t),with Ωkgivenby (51),isabsolutelyconvergent
when|ε|
∫t
0‖A(s)‖ds<ξ =1.0868... anditssumsatisfiesexp Ω(t;ε)=Y(t;ε).Hence,theMagnusseriesisthepower
seriesoftheanalyticfunction ϕ(ε)inthedisk |ε| < ξ/
∫t
0‖A(s)‖ds.But ϕ(ε)isanalyticin Bπ⊃Bξandthepowerseries
hastobeunique.Inconsequence,thepowerseriesof ϕ(ε)inBπhastobethesameasthepowerseriesof ϕ(ε)inBξ,which
ispreciselytheMagnusseries.Finally,bytaking ε=1wegetthedesiredresult. ■
2.7.4. Furtherdiscussion
Theorem9 providessufficientconditionsfortheconvergenceoftheMagnusseriesbasedonanestimatebythenorm
oftheoperator A.Inparticular,itguaranteesthattheoperator Ω(t)inY(t)=expΩ(t)cansafelybeobtainedwiththe
convergentseries
∑
k≥1Ωk(t)for0≤t<Twhentheterms Ωk(t)arecomputedwith (51).Anaturalquestionatthisstage
is—whatistheoptimalconvergencedomain?Inotherwords,istheboundestimate rc=πgivenby Theorem9 sharpor
istherestillroomforimprovement?Inordertoclarifythisissue,wenextanalyzetwosimpleexamplesinvolving2 ×2
matrices.
Example1. MoanandNiesen[ 71]considerthecoefficientmatrix
A(t)=
(
2 t
0 −1
)
. (74)
170 S.Blanesetal./PhysicsReports470(2009)151–238
Ifweintroduce,asbefore,thecomplexparameter εintheproblem,thecorrespondingexactsolution Y(t;ε)of(70)isgiven
by
Y(t;ε)=

e2εt 1
9ε
e2εt−
(
1
9ε+
1
3
t
)
e−εt
0 e −εt

 (75)
andtherefore
logY(t;ε)=
(
2t g(t;ε)
0 −t
)
, withg(t;ε)=
t(1−e3εt+3εt)
3(1−e3εt) .
TheMagnusseriescanbeobtainedbycomputingtheTaylorexpansionoflog Y(t;ε)aroundε=0.Noticethatthefunction
ghasasingularitywhen εt= 2π
3i,andthus,bytaking ε= 1,theMagnusseriesonlyconvergesupto t= 2
3π.Onthe
otherhand,condition
∫T
0‖A(s)‖ds<π leadstoT≈1.43205< 2
3π.Inconsequence,theactualconvergencedomainofthe
Magnusseriesislargerthantheestimateprovidedby Theorem9. □
Example2. Letusintroducethematrices
X1=
(
1 0
0 −1
)
=σ3, X2=
(
0 1
0 0
)
(76)
anddefine
A(t)=
{
βX2 0≤t≤1
αX1 t>1
withα,β complexconstants.Then,thesolutionofEq. (30)att=2is
Y(2)=eαX1eβX2=
(
eα βeα
0 e −α
)
,
sothat
logY(2)=log(eαX1eβX2)=αX1+
2αβ
1−e−2αX2, (77)
ananalyticfunctionif |α|<π withfirstsingularitiesat α=±iπ.Therefore,theMagnusseriescannotconvergeat t=2if
|α|≥ π,independentlyof β⁄=0,evenwhenitispossibleinthiscasetogetaclosed-formexpressionforthegeneralterm.
Specifically,astraightforwardcomputationwiththerecurrence (49)–(50)showsthat
∞∑
n=1
Ωn(2)=αX1+βX2+
∞∑
n=2
(−1)n−12n−1Bn−1
(n−1)! αn−1βX2. (78)
Ifwetakethespectralnorm,then ‖X1‖=‖ X2‖= 1and
∫ t=2
0
‖A(s)‖ds=|α|+| β|,
sothattheconvergencedomainprovidedby Theorem9 is|α|+| β|<π forthisexample.Noticethatinthelimit |β|→ 0
thisdomainisoptimal. □
Fromtheanalysisof Examples1and2wecanconcludethefollowing.First,theconvergencedomainoftheMagnusseries
providedbyTheorem9isthebestresultonecangetforagenericboundedoperator A(t)inaHilbertspace,inthesensethat
onemayconsiderspecificmatrices A(t),asin Example2,wheretheseriesdivergesforanytime tsuchthat
∫t
0‖A(s)‖ds>π.
Second,therearealsosituations(asin Example1)wheretheboundestimate r=πisstillratherconservative: indeed,the
Magnusseriesconvergesforalargertimeintervalthanthatgivenby Theorem9.Thisisparticularlyevidentifonetakes A(t)
asadiagonalmatrix:then,theexactsolution Y(t;ε)of(70)isadiagonalmatrixwhoseelementsarenon-vanishingentire
functionsof ε,andobviouslylog Y(t;ε)isalsoanentirefunctionof ε.Insuchcircumstances,theconvergencedomain
|ε|
∫t
0‖A(s)‖ds < πfortheMagnusseriesdoesnotmakemuchsense.Thus,anaturalquestionarises:isitpossibleto
obtainamoreprecisecriterionofconvergence?Intryingtoanswerthisquestion,in[ 31]analternativecharacterization
oftheconvergencehasbeendevelopedwhichisvalidfor n×ncomplexmatrices.Moreprecisely,aconnectionhasbeen
establishedbetweentheconvergenceoftheMagnusseriesandtheexistenceofmultipleeigenvaluesofthefundamental
matrixY(t;ε)forafixed t,whichwedenoteby Yt(ε).Byusingthetheoryofanalyticmatrixfunctions,andinparticular,of
thelogarithmofananalyticmatrixfunction(suchasisdone,e.g.in[ 76]),thefollowingresulthasbeenprovedin[ 31]:ifthe
analyticmatrixfunction Yt(ε)hasaneigenvalue ρ0(ε0)ofmultiplicityl>1foracertain ε0suchthat:(a)thereisacurvein
S.Blanesetal./PhysicsReports470(2009)151–238 171
theε-planejoining ε=0with ε=ε0,and(b)thenumberofequaltermsinlog ρ1(ε0),log ρ2(ε0),..., logρl(ε0)suchthat
ρk(ε0)= ρ0,k=1,..., lislessthanthemaximumdimensionoftheelementaryJordanblockcorrespondingto ρ0,then
theradiusofconvergenceoftheseries Ωt(ε)=∑
k≥1εkΩt,kverifyingexp Ωt(ε)=Yt(ε)isprecisely r=|ε0|.Ananalysis
alongthesamelinehasbeencarriedoutin[ 77].
Whenthiscriterionisappliedto Example1,itgives,astheradiusofconvergenceoftheMagnusseriescorrespondingto
Eq.(70)forafixed t,
Ωt(ε)=
∞∑
k=1
εkΩt,k, (79)
thevalue
r=|ε|=
2π
3t
. (80)
TogettheactualconvergencedomainoftheusualMagnusexpansionwehavetotake ε= 1,andso,from (80),weget
2π/(3t)=1,orequivalently t=2π/3,i.e.,theresultachievedfromtheanalysisoftheexactsolution.
Withrespectto Example2,onegets[ 31]
|ε|= π
|α|(t−1).
Ifwenowfix ε=1,theactual t-domainofconvergenceoftheMagnusseriesis
t=1+ π
|α|.
Observethat,when t=2,weget |α|= πandthusthepreviousresultisrecovered:theMagnusseriesconvergesonlyfor
|α|<π.
It should also be mentioned that the case of a diagonal matrixA(t) is compatible with this alternative
characterization[31].
2.8. MagnusexpansionandtheBCHformula
TheMagnusexpansioncanalsobeusedtoexplicitlyobtainthetermsoftheseries Zin
Z=log(eX1eX2),
X1andX2beingtwononcommutingindeterminatevariables.Asitiswellknown[ 41],
Z=X1+X2+
∞∑
n=2
Gn(X1,X2), (81)
whereGn(X1,X2)isahomogeneousLiepolynomialin X1andX2ofgrade n;inotherwords, Gncanbeexpressedinterms
ofX1andX2byaddition,multiplicationbyrationalnumbersandnestedcommutators.Thisresultisoftenknownasthe
Baker–Campbell–Hausdorff(BCH)theoremandprovestobeveryusefulinvariousfieldsofmathematics(theoryoflinear
differentialequations[ 4],Liegrouptheory[ 78],numericalanalysis[ 79])andtheoreticalphysics(perturbationtheory,
transformationtheory,QuantumMechanicsandStatisticalMechanics[ 19,80,81]).Inparticular,inthetheoryofLiegroups,
withthistheoremonecanexplicitlywritetheoperationofmultiplicationinaLiegroupincanonicalcoordinatesinterms
oftheLiebracketoperationinitsalgebraandalsoprovetheexistenceofalocalLiegroupwithagivenLiealgebra[ 78].
IfX1andX2arematricesandoneconsidersthepiecewiseconstantmatrix-valuedfunction
A(t)=
{
X2 0≤t≤1
X1 1<t≤2 (82)
thentheexactsolutionof (30)att=2is Y(2)=eX1eX2.Bycomputing Y(2)=eΩ(2)withrecursion (51)onegetsforthe
firstterms
Ω1(2)=X1+X2
Ω2(2)=
1
2
[X1,X2] (83)
Ω3(2)=
1
12
[X1,[X1,X2]]−
1
12
[X2,[X1,X2]]
Ω4(2)=
1
24
[X1,[X2,[X2,X1]]].
Ingeneral,each Gn(X1,X2)isalinearcombinationofthecommutatorsoftheform [V1,[V2,..., [Vn−1,Vn]...]]with
Vi∈{ X1,X2}for1 ≤ i≤ n,thecoefficientsbeinguniversalrationalconstants.Thisisperhapsoneofthereasonswhy
theMagnusexpansionisoftenreferredtointheliteratureasthecontinuousanalogueoftheBCHformula.Asamatterof
fact,Magnusproposedadifferentmethodforobtainingthefirsttermsintheseries (40)basedon (81)[4].
172 S.Blanesetal./PhysicsReports470(2009)151–238
Nowwecanapply Theorem9 andobtainthefollowingsharpbound.
Theorem10. TheBaker–Campbell–Hausdorffseriesintheform (81)convergesabsolutelywhen ‖X1‖+‖ X2‖<π.
Thisresultcanbegeneralized,ofcourse,toanynumberofnoncommutingoperators X1,X2,..., Xq.Specifically,theseries
Z=log(eX1eX2··· eXq),
convergesabsolutelyif ‖X1‖+‖ X2‖+···+‖ Xq‖<π.
2.9. Preliminarylineartransformations
ToimprovetheaccuracyandtheboundsontheconvergencedomainoftheMagnusseriesforagivenproblem,itisquite
commontofirstconsideralineartransformationonthesysteminsuchawaythattheresultingdifferentialequationcanbe
moreeasilyhandledinacertainsense,tobespecifiedforeachproblem.Toillustratetheprocedure,letusconsiderasimple
example.
Example.Supposewehavethe2 ×2matrix
A(t)=α(t)X1+β(t)X2, (84)
whereX1andX2aregivenby (76)andαandβarecomplexfunctionsoftime, α,β : R−→ C.Thentheexactsolutionof
Y′=A(t)Y,Y(0)=Iis
Y(t)=

e
∫t
0α(s)ds
∫ t
0
ds1e
∫t
s1
α(s2)ds2β(s1)e−
∫s1
0 α(s2)ds2
0 e −
∫t
0α(s)ds

. (85)
Letusfactorizethesolutionas Y(t)=˜Y0(t)˜Y1(t),with ˜Y0(t)thesolutionoftheinitialvalueproblemdefinedby
˜Y′
0=A0(t)˜Y0 A0(t)=α(t)X1=
(
α(t) 0
0 −α(t)
)
(86)
and˜Y0(0)=I.Then,theequationsatisfiedby ˜Y1is
˜Y′
1=A1(t)˜Y1, withA1=˜Y−1
0 A˜Y0−A0=
(
0 β(t)e2
∫t
0α(s)ds
0 0
)
, (87)
sothatthefirsttermoftheMagnusexpansionappliedto (87)alreadyprovidestheexactsolution (85). □
This,ofcourse,isnotthetypicalbehavior,butinanycase,ifthetransformation ˜Y0inthefactorization Y(t)=˜Y0(t)˜Y1(t)
ischosenappropriately,thefirstfewtermsintheMagnusseriesappliedtotheequationsatisfiedby ˜Y1usuallygivevery
accurateapproximations.
SincethiskindofpreliminarytransformationisfrequentlyusedinQuantumMechanics,wespecializethetreatmentto
thisparticularsettinghere,andconsiderEq. (4)instead.Inotherwords,wewrite (30)inthemoreconventionalformofthe
timedependentSchödingerequation
dU(t)
dt
=˜H(t)U(t), (88)
where˜H≡H/(i¯h),¯histhereducedPlanckconstant, HistheHamiltonianand Ucorrespondstotheevolutionoperator.
Asintheexample,supposethat ˜Hcanbesplitintotwopieces, ˜H = ˜H0+ε˜H1,with ˜H0asolvableHamiltonianand
ε≪ 1asmallperturbationparameter.Insuchasituation,onetriestointegrateoutthe ˜H0piecesoastocircumscribe
theapproximationtothe ˜H1 piece.InthecaseofEq. (88),thisiscarriedoutbymeansofalineartime-dependent
transformation.InQuantumMechanics,thispreliminarylineartransformationcorrespondstoanewevolutionpicture,such
astheinteractionortheadiabaticpicture.
Amongotherpossibilities,wemayfactorizethetime-evolutionoperatoras
U(t)=G(t)UG(t)GĎ(0), (89)
whereG(t)isalineartransformationwhosepurposeisyettobedefined.Inthenew G-Picture,thecorrespondingtime-
evolutionoperatorUGobeystheequation
U′
G(t)=˜HG(t)UG(t), ˜HG(t)=GĎ(t)˜H(t)G(t)−GĎ(t)G′(t). (90)
The choice ofG depends on the nature of the problem at hand. There is no generic formal recipe to find out the
mostappropriate G.InthespiritofcanonicaltransformationsofClassicalMechanics,oneshouldbuildupthevery UG
S.Blanesetal./PhysicsReports470(2009)151–238 173
perturbatively.However,theaimhereisdifferentbecause Gisdefinedfromthebeginning.Tworathercommonchoices
are:
•Interactionpicture.Itiswellsuitedwhen ˜H0(t)isdiagonalinsomebasis,orelse,itisconstant.Inthatcase
G(t)=exp
(∫ t
0
˜H0(τ)dτ
)
(91)
sothat
˜HG(t)=εexp
(
−
∫ t
0
˜H0(τ)dτ
)
˜H1(t)exp
(∫ t
0
˜H0(τ)dτ
)
. (92)
•Adiabaticpicture.Atimescaleofthesystem,muchsmallerthanthatoftheinteraction,definesanadiabaticregime.
Forinstance,supposethattheHamiltonianoperator H(t)dependssmoothlyontimethroughthevariable τ = t/T,
whereTdeterminesthetimescaleand T→∞.Thenthequantummechanicalevolutionofthesystemisdescribedby
dU/dt=˜H(εt)U,with ε≡1/T≪1,orequivalently
dU(τ)
dτ =
1
ε
˜H(τ)U(τ), (93)
withτ≡εt.Inthiscasetheappropriatetransformationisa Gthatrenders ˜H(t)instantaneouslydiagonal,i.e.,
GĎ(t)˜H(t)G(t)=E(t)=diag[E1(t),E2(t),...]. (94)
Theterm GĎG′ofthenewHamiltonianin (90)is,underadiabaticconditions,verysmall.Itsmaindiagonalgeneratesthe
so-calledBerry,orgeometric,phase[ 82].
Bothtypesof Gdonotexcludemutually,buttheymaybeusedinsuccession.Asamatteroffact,correctionstothe
adiabaticapproximationmustbefollowedbytheformerone.Inturn,anadiabatictransformationmaybeiterated,as
proposedbyGarrido[ 83]andBerry[ 84].
InSection4weshallextensivelyusethesepreliminarylineartransformationsonseveralstandardproblemsofQuantum
MechanicstoillustratethepracticalfeaturesoftheMagnusexpansion.
2.10. Exponentialproductrepresentations
IncontrasttoMagnusexpansion,muchlessattentionhasbeenpaidtosolutionsof (30)intheformofaproductof
exponentialoperators.Bothapproachesarebynomeansequivalent,since,ingeneral,theoperators Ωndonotcommute
witheachother.Forinstance,foraquantumsystemasinEq. (88),theansatz U=∏
exp(Φn)(whereΦnareskew-Hermitian
operatorstobedetermined)isanalternativetotheMagnusexpansion,alsopreservingtheunitarityofthetime-evolution
operator.OnesuchprocedurewasdevisedbyFerin1958inapaperdevotedtothestudyofsystemsoflineardifferential
equations[20].AlthoughtheoriginalresultobtainedbyFerwascitedandexplicitlystatedbyBellman[ 85,p.204],sometimes
ithasbeenmisquotedasareferencefortheMagnusexpansion[ 22].Ontheotherhand,WilcoxassociatedFer’snamewith
aninterestingalternativeinfiniteproductexpansionwhichisindeedacontinuousanalogueoftheZassenhausformula[ 19]
(somethingalsoattributedtotheFerfactorization[ 2,p.372]).This,however,alsoledtosomeconfusion,sincehisapproach
isinthespiritofperturbationtheory,whereasFer’soriginalonewasessentiallynonperturbative.Thesituationwasclarified
in[86],wherealsosomeapplicationstoQuantumMechanicswerecarriedoutforthefirsttime.
InthissectionwebrieflydiscussthemainfeaturesoftheFerandWilcoxexpansions,andhowthelattercanbederived
fromthesuccessivetermsoftheMagnusseries.Thiswillclarifythedifferentcharacterofthetwoexpansions.Wealso
includesomedetailsonthefactorizationofthesolutionproposedbyWeiandNorman[ 17,87].Finallyweprovideanother
interpretationoftheMagnusexpansionasthecontinuousanalogueoftheBCHformulainlinearcontroltheory.
2.10.1. Fermethod
AnintuitivewaytointroduceFerformalismisthefollowing[ 59].Giventhematrixlinearsystem Y′=A(t)Y,Y(0)=I,
weknowthat
Y(t)=exp(F1(t)) (95)
istheexactsolutionif Acommuteswithitstimeintegral F1(t)=
∫t
0A(s)ds,and Y(t)evolvesintheLiegroup GifAliesin
itscorrespondingLiealgebra g.IfthegoalistorespecttheLie-groupstructureinthegeneralcase,weneedto‘correct’ (95)
withoutlosingthisimportantfeature.
Twopossibleremediesariseinaquitenaturalway.Thefirstisjusttoseekacorrection ∆(t)evolvingintheLiealgebra
gsothat
Y(t)=exp(F1(t)+∆(t)).
174 S.Blanesetal./PhysicsReports470(2009)151–238
ThisisnothingbuttheMagnusexpansion.Alternatively,onemaycorrectwith Y1(t)intheLiegroup G,
Y(t)=exp(F1(t))Y1(t). (96)
ThisispreciselytheapproachpursuedbyFer,i.e.representingthesolutionof (30)inthefactorizedform (96),where
(hopefully)Y1willbeclosertotheidentitymatrixthan Y,atleastforsmall t.
Thequestionnowistofindthedifferentialequationsatisfiedby Y1.Substituting (96)intoEq. (30)wehave
d
dt
Y=
(
d
dt
eF1
)
Y1+eF1
d
dt
Y1=AeF1Y1, (97)
sothat,takingintoaccounttheexpressionforthederivativeoftheexponentialmap( Lemma2),onearriveseasilyat
Y′
1=A1(t)Y1 Y1(0)=I, (98)
where
A1(t)=e−F1AeF1−
∫ 1
0
dxe−xF1AexF1. (99)
Theaboveprocedurecanberepeatedtoyieldasequenceofiteratedmatrices Ak.Afternstepswehavethefollowingrecursive
scheme,knownastheFerexpansion:
Y=eF1eF2··· eFnYn (100)
Y′
n=An(t)Yn Yn(0)=I, n=1,2,...
withFn(t)andAn(t)givenby
Fn+1(t)=
∫ t
0
An(s)ds A 0(t)=A(t), n=0,1,2,...
An+1 = e−Fn+1AneFn+1−
∫ 1
0
dxe−xFn+1AnexFn+1
=
∫ 1
0
dx
∫ x
0
due−(1−u)Fn+1[An,Fn+1]e(1−u)Fn+1
=
∞∑
j=1
(−)jj
(j+1)!
ad
j
Fn+1
(An), n=0,1,2....
(101)
When,afternstepsweimpose Yn=I,weareleftwithanapproximationtotheexactsolution Y(t).
Inspectionoftheexpressionof An+1in(101)revealsaninterestingfeatureoftheFerexpansion.Ifweassumethata
perturbationparameter εisintroducedin A(i.e.ifwesubstitute AbyεAintheformalism),since Fn+1isofthesameorderin
εasAnthenanelementaryrecursionshowsthatthematrix Anstartswithatermoforder ε2n
(correspondinglytheoperator
Fncontainstermsoforder ε2n−1
andhigher).ThisshouldgreatlyenhancetherateofconvergenceoftheproductinEq. (100)
totheexactsolution.
Itispossibletoderiveaboundontheconvergencedomainintimeoftheexpansion[ 30].Theideaisjusttolookfor
conditionson A(t) whichensure Fn → 0as n→∞ .AsinthecaseoftheMagnusexpansion,wetake A(t)tobea
boundedmatrixwith ‖A(t)‖≤ k(t)≡k0(t).Fer’salgorithm,Eqs. (100)and(101),thenprovidesarecursiverelationamong
correspondingbounds kn(t) for‖An(t)‖.Ifwedenote Kn(t)≡
∫t
0kn(s)ds,wecanwritethisrelationinthegenericform
kn+1=f(kn,Kn),which,afterintegration,gives
Kn+1=M(Kn). (102)
Thequestionnowis:whenis Kn →0as n→∞?Thisiscertainlysoif0isastablefixedpointfortheiterationofthe
mappingM andK0 iswithinitsbasinofattraction.Toseewhenthisisthecase,wehavetosolvetheequation ξ=M(ξ)
tofindwherethenextfixedpointlies.Letusdoitexplicitly.Bytakingnormsintherecursivescheme (101)wehave
‖An+1‖≤
∫ 1
0
dx
∫ x
0
due2(1−u)Kn‖[An,Fn+1]‖,
whichcanbewrittenas ‖An+1‖≤ kn+1,with
kn+1=
1−e2Kn(1−2Kn)
2Kn
dKn
dt
S.Blanesetal./PhysicsReports470(2009)151–238 175
andconsequentlyKn+1isgivenbyEq. (102)with
M(Kn)=
∫ Kn
0
1−e2x(1−2x)
2x
dx. (103)
Thatisthemappingwehavetoiterate.Itisclearthat ξ=0 isastablefixedpointof M.Thenext,unstable,fixedpointis
ξ=0.8604065.SowecanconcludethatwehaveaconvergentFerexpansion,atleastforvaluesoftime t,suchthat
∫ t
0
‖A(s)‖ds≤K0(t)< 0.8604065. (104)
NoticethattheboundfortheconvergencedomainprovidedbythisresultissmallerthanthatcorrespondingtotheMagnus
expansion(Theorem9).
2.10.2. Wilcoxmethod
AmoretractableformofinfiniteproductexpansionhasbeendevisedbyWilcox[ 19]inanalogywiththeMagnus
approach.Theidea,asusual,istotreat εin
Y′=εA(t)Y, Y(0)=I (105)
asanexpansionparameterandtodeterminethesuccessivefactorsintheproduct
Y(t)=eW1eW2eW3··· (106)
byassumingthat Wnisexactlyoforder εn.Hence,itisclearfromtheverybeginningthatthemethodsofFerandWilcox
giveriseindeedtocompletelydifferentinfiniteproductrepresentationsofthesolution Y(t).
Theexplicitexpressionsof W1,W2andW3aregivenin[ 19].Itisnoteworthythattheoperators Wncanbeexpressedin
termsofMagnusoperators Ωk,forwhichcompactformulaeandrecursiveproceduresareavailable.Tothisend,wesimply
usetheBaker–Campbell–Hausdorffformulatoextractformallyfromtheidentity
eW1eW2eW3···= eΩ1+Ω2+Ω3+···, (107)
termsofthesameorderin ε.Afterastraightforwardcalculationonefindsforthefirstterms
W1=Ω1, W2=Ω2, W3=Ω3−
1
2
[Ω1,Ω2], (108)
W4=Ω4−
1
2
[Ω1,Ω3]+
1
6
[Ω1,[Ω1,Ω2]], etc. (109)
ThemaininterestoftheWilcoxformalismstemsfromthefactthatitprovidesexplicitexpressionsforthesuccessive
approximationstoasolutionrepresentedasaninfiniteproductofexponentialoperators.Thisoffersausefulalternativeto
theFerexpansionwheneverthecomputationof FnfromEq.(101)istoocumbersome.Wenote,inpassing,thattofirstorder
thethreeexpansionsyieldthesameresult: F1=W1=Ω1.
2.10.3. Wei–Normanfactorization
Nowsupposethat AandYinEq.(30)arelinearoperatorsandthat A(t)canbeexpressedintheform
A(t)=
m∑
i=1
ui(t)Xi, mfinite, (110)
wheretheui(t)arescalarfunctionsoftime,and X1,X2,..., Xmaretime-independentoperators.Furthermore,supposethat
theLiealgebra ggeneratedbythe Xiisoffinitedimension l(thisisobviouslytrueif AandYarefinitedimensionalmatrix
operators).Undertheseconditions,if X1,X2,..., Xlisabasisfor g,theMagnusexpansionallowsustoexpressthesolution
locallyintheform Y(t)=exp(∑l
i=1fi(t)Xi).WeiandNorman,ontheotherhand,showthatthereexistsaneighborhoodof
t=0inwhichthesolutioncanbewrittenasaproduct[ 17,87]
Y(t)=exp(g1(t)X1)exp(g2(t)X2)··· exp(gl(t)Xl), (111)
wherethegi(t)arescalarfunctionsoftime.Moreover,the gi(t)satisfyasetofnonlineardifferentialequationswhichdepend
onlyontheLiealgebra gandtheui(t)’s.Theseauthorsalsostudytheconditionsunderwhichthesolutionconvergesglobally,
thatis,forall t.Inparticular,thishappensforallsolvableLiealgebrasinasuitablebasis,andforanyreal2 ×2systemof
equations[87].
IntheterminologyofLiealgebrasandLiegroups,therepresentation Y(t) = exp(∑l
i=1fi(t)Xi)correspondstothe
canonicalcoordinatesofthefirstkind ,whereasEq. (111)definesasystemof canonicalcoordinatesofthesecondkind [41,
78,88].
176 S.Blanesetal./PhysicsReports470(2009)151–238
ThisclassoffactorizationhasbeenusedincombinationwiththeFerexpansiontoobtainclosed-formsolutionsofthe
Cauchyproblemdefinedbycertainclassesofparaboliclinearpartialdifferentialequations[ 89].Whenthealgorithmis
applied,thesolutioniswrittenasafiniteproductofexponentials,dependingoncertainorderingfunctionsforwhich
convergentapproximationsareconstructedinexplicitform.
Noticethattherepresentation (111)isclearlyusefulwhenthespectralpropertiesoftheindividualoperators Xiare
readilyavailable.Sincethe Xiareconstantandoftenhavesimplephysicalinterpretation,theevaluationoftheeigenvalues
andeigenvectorscanbedoneonceforalltimes,andthismayfacilitatethecomputationoftheexponentials.Thissituation
arises,inparticular,incontroltheory[ 88].Thefunctions ui(t)areknownasthecontrols,andtheoperator Y(t)actsonthe
statesofthesystem,describinghowthestatesaretransformedalongtime.
2.11. ThecontinuousBCHformula
Whenappliedtotheequation Y′=A(t)Ywiththematrix A(t)givenby(110),theMagnusexpansionadoptsaparticularly
simpleform.Furthermore,bymakinguseofthestructureconstantsoftheLiealgebra,itisrelativelyeasytogetexplicit
expressionsforthecanonicalcoordinatesofthefirstkind fi(t).Letusillustratetheprocedurebyconsideringtheparticular
case
A(t)=u1(t)X1+u2(t)X2.
Denotingby αi(t)=
∫t
0ui(s)ds,and,foragivenfunction µ,
(∫
i
µ
)
(t)≡
∫ t
0
ui(s)µ(s)ds,
astraightforwardcalculationshowsthatthefirsttermsof ΩintheMagnusexpansioncanbewrittenas
Ω(t)= β1(t)X1+β2(t)X2+β12(t)[X1,X2]+ β112(t)[X1,[X1,X2]]+ β212(t)[X2,[X1,X2]]+··· (112)
where
βi=αi, i=1,2,
β12=
1
2
(∫
1
α2−
∫
2
α1
)
, (113)
β112=
1
12
(∫
2
α2
1−
∫
1
α1α2
)
−
1
4
(∫
1
∫
2
α1−
∫
1
∫
1
α2
)
,
β212=
1
12
(∫
2
α1α2−
∫
1
α2
2
)
+
1
4
(∫
2
∫
1
α2−
∫
2
∫
2
α1
)
.
TakingintoaccountthestructureconstantsoftheparticularfinitedimensionalLiealgebraunderconsideration,from (112)
oneeasilygetsthefunctions fi(t).Inthegeneralcase, (112)allowsustoexpress Ωasalinearcombinationofelementsof
abasisofthefreeLiealgebrageneratedby X1andX2.Inthiscase,therecurrence (49)–(50)definingtheMagnusexpansion
canbecarriedoutonlywiththenestedintegrals
αi1···is(t)≡
(∫
is
···
∫
i1
1
)
(t)=
∫ t
0
∫ ts
0
···
∫ t3
0
∫ t2
0
uis(ts)··· ui1(t1)dt1··· dts (114)
involvingthefunctions u1(t)andu2(t).Thus,forinstance,thecoefficientsin (113)canbewritten(aftersuccessive
integrationbyparts)as
βi=αi, i=1,2,
β12=
1
2
(∫
1
α2−
∫
2
α1
)
=
1
2
(α21−α12),
β112=
1
6
(∫
2
∫
1
α1+
∫
1
∫
1
α2−2
∫
1
∫
2
α1
)
=
1
6
(α112+α211−2α121),
β212=
1
6
(
2
∫
2
∫
1
α2−
∫
2
∫
2
α1−
∫
1
∫
2
α2
)
=
1
6
(2α212−α122−α221).
Theseries(112)expressedintermsoftheintegrals (114)isusuallyreferredtoasthecontinuousBaker–Campbell–Hausdorff
formula[90,91]forthelinearcase.Wewillgeneralizethisformalismtothenonlinearcaseinthenextsection.
3. GeneralizationsoftheMagnusexpansion
InviewoftheattractivepropertiesoftheMagnusexpansionasatooltoconstructapproximatesolutionsofnon-
autonomoussystemsoflinearordinarydifferentialequations,itishardlysurprisingthatseveralattemptshavebeenmade
S.Blanesetal./PhysicsReports470(2009)151–238 177
alongtheyears,eithertoextendtheproceduretoamoregeneralsettingortomanipulatetheseriestoachievefurther
improvements.Inthissection,wereviewsomeofthesegeneralizations,withspecialemphasisonthetreatmentofnonlinear
differentialequations.
FirstwereconsideraniterativemethodoriginallydevisedbyVoslamber[ 92]forcomputingapproximations Ω(n)(t)
inY(t) = exp(Ω(t))forthelinearequation Y′ = A(t)Y.Theresultingapproximationmaybeinterpretedasare-
summationoftermsintheMagnusseriesandpossessesinterestingfeaturesnotsharedbythecorrespondingtruncation
oftheconventionalMagnusexpansion.ThenweadapttheMagnusexpansiontothephysicallyrelevantcaseofaperiodic
matrixA(t)withperiodTwhichincorporates,inanaturalway,thestructureofthesolutionensuredbytheFloquettheorem.
NextwegoonestepfurtherandgeneralizetheMagnusexpansiontotheso-callednonlinearLieequation Y′=A(t,Y)Y.
Finally,weshowhowtheprocedurecanbeappliedto anynonlinearexplicitlytime-dependentdifferentialequation.
Althoughthetreatmentislargelyformal,inSection 5wewillseethatitisofparamountimportancefordesigningnew
andhighlyefficientnumericalintegrationschemesforthisclassofdifferentialequations.Weparticularizethetreatment
totheimportantcaseofHamiltoniansystems,andalsoestablishaninterestingconnectionwiththeChen–Fliessseriesfor
nonlineardifferentialequations.
3.1. Voslamberiterativemethod
LetusconsiderEq. (30)whenthereisaperturbationparameter εinthe(ingeneral,complex)matrix A,i.e.,Eq. (105).
Theorem9 guaranteesthat,forsufficientlysmallvaluesof t,Y(t;ε)=expΩ(t;ε),where
Ω(t;ε)=
∞∑
n=1
εnΩn(t). (115)
Theadvantagesofthisrepresentationandtheapproximationsobtainedwhentheseriesistruncatedhavebeensufficiently
recognizedinthetreatmentdoneinprevioussections.Thereis,however,apropertyoftheexactsolutionnotsharedbyany
truncationoftheseries (115)whichcouldberelevantincertainphysicalapplications: (1/ε)∑m
n=1εnΩn(t)withm>1is
unboundedfor ε→∞ evenwhen Ω(t,ε)/ε isboundeduniformlywithrespectto εunderrathergeneralassumptionson
thematrix A(t)[92].Noticethatthisisthecase,inparticular,fortheadiabaticproblem (93).
WhenSchur’sunitarytriangularizationtheorem[ 44]isappliedtotheexactsolution Y(t;ε)onehas
Tε=U ĎYU , (116)
whereTεisanuppertriangularmatrixand Uisunitary.Inotherwords, Yisunitarilyequivalenttoanuppertriangular
matrixTε.Differentiating(116)andusing (105),onearrivesat
T′
ε=εU ĎAUTε+
[
Tε,U ĎU′]
.
Sincethesecondtermontherighthandsideisnotuppertriangular,itfollowsatoncethat
Tε(t)=exp
(
ε
∫ t
0
(U ĎAU)∆ds
)
,
wherethesubscript ∆denotestheuppertriangularpart(includingtermsonthemaindiagonal)ofthecorrespondingmatrix.
Takingintoaccount (116)onegets
Ω(t,ε)=εU
(∫ t
0
(U ĎAU)∆ds
)
U Ď. (117)
ConsideringnowtheFrobeniusnorm(whichisunitarilyinvariant,Section 1.2)ofbothsidesofthisequation,onehas
‖Ω‖F=| ε|
‖‖‖‖
∫ t
0
(U ĎAU)∆ds
‖‖‖‖
F
≤|ε|
∫ t
0
‖(U ĎAU)∆‖Fds
≤| ε|
∫ t
0
‖U ĎAU‖Fds=|ε|
∫ t
0
‖A‖Fds. (118)
Ifthespectralnormisconsideredinstead,frominequalities (28),(29)and(118),oneconcludesthat
‖Ω‖2≤
√
rank(A)|ε|
∫ t
0
‖A‖2ds.
Inanycase,whatisimportanttostresshereisthatfortheexactsolution Ω(t;ε)/εisboundeduniformlywithrespect
tothe εparameter.Voslamberproceedsbyderivinganalgorithmforgeneratingsuccessiveapproximationsof Y(t;ε)=
exp(Ω(t;ε))which,contrarilytothedirectseriesexpansion (115),preservethisproperty.Hispointofdepartureistogeta
seriesexpansionfortheso-called dressedderivativeof Ω[93]
Γ≡eΩ/2Ω′e−Ω/2. (119)
178 S.Blanesetal./PhysicsReports470(2009)151–238
Thisisaccomplishedbyinserting (39)in(119).Specifically,onehas
Γ =eadΩ/2Ω′=eadΩ/2dexp−1
Ω (εA)=eadΩ/2
adΩ
eadΩ−1
(εA)
=
adΩ/2
sinhΩ/2
(εA)=
∞∑
n=0
Bn(1/2)
n!
adn
Ω(εA)
andfinally[92,93]
Γ=
∞∑
n=0
21−n−1
n!
Bnadn
Ω(εA), (120)
where,asusual, BndenoteBernoullinumbers.Inordertoexpress Γ asapowerseriesof εonehastoinserttheMagnus
series(115)intoEq.(120).Thenweget
Γ(t;ε)=
∞∑
n=1
εnΓn(t), (121)
wheretheterms Γncanbeexpressedasafunctionof Ωkwithk≤n−2throughtherecursiveprocedure[ 93]
Γ1=A, Γ2=0, (122)
Γn=
n−1∑
j=2
cj
∑
k1+···+kj=n−1
k1≥1,...,kj≥1
adΩk1
adΩk2
··· adΩkj
A, n≥3.
Here
cj≡
21−j−1
j!
Bj,
withc2j+1=0,c2=−1/24,c4=7/5760,etc.Inparticular,
Γ3=−
1
24
[Ω1,[Ω1,A]]
Γ4=−
1
24
([Ω1,[Ω2,A]]+[ Ω2,[Ω1,A]]).
Now,fromthedefinitionof Γ,Eq.(119),wewrite
Ω′=e−Ω/2ΓeΩ/2,
which,afterintegrationover t,canbeusedforconstructingsuccessiveapproximationsto Ωoncetheterms Γnareknown
intermsof Ωk,k≤n−2.Thus,the nthapproximant Ω(n)isdefinedby
Ω(n)(t)=
∫ t
0
e−1
2Ω(n−1)(s)Γ(n)(s)e
1
2Ω(n−1)(s)ds, n=1,2,... (123)
wherethe εdependencehasbeenomittedbysimplicityand Γ(n)= ∑n
k=1εkΓk,Ω(0)= O.Thefirsttwoapproximants
explicitlyread
Ω(1)(t,ε)=εΩ1(t)=ε
∫ t
0
A(s)ds
Ω(2)(t,ε)=ε
∫ t
0
e−1
2Ω(1)(s,ε)A(s)e
1
2Ω(1)(s,ε)ds. (124)
Inthisapproach,thesolutionisapproximatedby Y(t)≃ exp(Ω(n)).Observethat Ω(n)containscontributionsfroman
infinityofordersin ε,whereasthe nthtermintheMagnusseries (115)isproportionalto εn.Furthermore, Ω(n)contains∑n
k=1εkΩkandalsohigherpowers εm(m>n).Inparticular,oneeasilygets
Ω(2)(t;ε)=εΩ1(t)+ε2Ω2(t)+
∞∑
k=3
(−1)k−1
2k−1(k−1)!εk
∫ t
0
adk−1
Ω1(s)A(s)ds.
Fromthestructureoftheexpression (123)itisalsopossibletofindtheasymptoticbehaviorof Ω(n)/ε(n≥3)for ε→∞
andprovethatitremainsbounded[ 92],justastheexactsolutiondoes.ThispropertyoftheVoslamberiterativealgorithm
mayleadtobetterapproximationsof Y(t)whentheparameter εisnotverysmall,sinceinthatcase Ω(n)/εisexpectedto
remaincloseto Ω/ε,asshownin[ 93].
S.Blanesetal./PhysicsReports470(2009)151–238 179
3.2. Floquet–Magnusexpansion
WenowturnourattentiontoaspecificcaseofEq. (30)withimportantphysicalandmathematicalapplications,namely
whenthe(complex) n×nmatrix-valuedfunction A(t)isperiodicwithperiod T.Thenfurtherinformationisavailableon
thestructureoftheexactsolution,asisgivenbythecelebratedFloquettheorem,whichensuresthefactorizationofthe
solutioninaperiodicpartandapurelyexponentialfactor.Morespecifically,
Y(t)=P(t)exp(tF), (125)
whereFandParen×nmatrices,P(t)=P(t+T)foralltandFisconstant.Thus,albeitasolutionof (30)isnot,ingeneral,
periodic,thedeparturefromperiodicityisdeterminedby (125).Thisresult,whenappliedinquantummechanics,isreferred
toasBlochwavetheory[ 94,95].Itiswidelyusedinproblemsofsolidstatephysicswherespace-periodicpotentialsarequite
common.InNuclearMagneticResonance,thisstructureisexploitedasfaraseithertime-dependentperiodicmagneticfields
orsamplespinningareinvolved[ 24].Asymptoticstabilityofthesolution Y(t)isdictatedbythenatureoftheeigenvalues
ofF,theso-calledcharacteristicexponentsoftheoriginalperiodicsystem[ 96].
AnalternativemannerofinterpretingEq. (125)istoconsiderthepiece P(t),provideditisinvertible,toperforma
transformationofthesolutioninsuchawaythatthecoefficientmatrixcorrespondingtothenewrepresentationhasall
itsmatrixentriesgivenbyconstants.Thusthepieceexp (tF)in(125)maybeconsideredasanexactsolutionofthesystem
(30)previouslymovedtoarepresentationwherethecoefficientmatrixistheconstantmatrix F[76].The t-dependent
changeofrepresentationiscarriedoutby P(t).ConnectingwithSection 2.9,P(t)istheappropriatepreliminarylinear
transformationforperiodicsystems.Ofcourse,Floquettheorembyitselfgivesnopracticalinformationaboutthisprocedure.
Itjuststatesthatsucharepresentationdoesexist.Infact,aseriousdifficultyinthestudyofdifferentialequationswith
periodiccoefficientsisthatnogeneralmethodtocomputeeitherthematrix P(t)ortheeigenvaluesof Fisknown.
Mainly,twowaysofexploitingtheabovestructureof Y(t)arefoundintheliterature[ 97].Thefirstoneconsistsin
performingaFourierexpansionoftheformalsolution,leadingtoaninfinitesystemoflineardifferentialequationswith
constantcoefficients.Thus,the t-dependentfinitesystemisreplacedwithaconstantoneatthepriceofhandlinginfinite
dimension.Resolutionofthetruncatedsystemfurnishesanapproximatesolution.Thesecondapproachisofperturbative
nature.Itdealsdirectlywiththeform (125)byexpanding
P(t)=
∞∑
n=1
Pn(t), F=
∞∑
n=1
Fn. (126)
EverytermFnin(126)isfixedsoastoensure Pn(t)=Pn(t+T),whichinturnguaranteestheFloquetstructure (125)atany
orderofapproximation.
AlthoughtheMagnusexpansion,suchasithasbeenformulatedinthiswork,doesnotexplicitlyprovidethestructureof
thesolutionensuredbyFloquettheorem,itcanbeadapted,withoutspecialdifficulty,toalsocopewiththissituation.The
startingpointistointroducetheFloquetform (125)intothedifferentialequation Y′=A(t)Y.Inthatway,theevolution
equationforPisobtained:
P′(t)=A(t)P(t)−P(t)F, P(0)=I. (127)
Theconstantmatrix Fisalsounknownandwewilldetermineitsoastoensure P(t+T)=P(t).Nowwereplacetheusual
perturbativeschemeinEq. (126)withtheexponentialansatz
P(t)=exp(Λ(t)), Λ(0)=O. (128)
Obviously,Λ(t+T)=Λ(t)soastopreserveperiodicity.NowEq. (127)conveys
d
dt
exp(Λ)=Aexp(Λ)−exp(Λ)F, (129)
fromwhich,aswiththeconventionalMagnusexpansion,itfollowsreadilythat
Λ′=
∞∑
k=0
Bk
k!
adk
Λ(A+(−1)k+1F). (130)
Thisequationisnow,intheFloquetcontext,theanalogueofMagnusequation (39).Noticethatifweput F=Othen(39)is
recovered.Thenextmoveistoconsidertheseriesexpansionsfor ΛandF
Λ(t)=
∞∑
k=1
Λk(t), F=
∞∑
k=1
Fk, (131)
withΛk(0)=O,forall k.Equatingtermsofthesameorderin (130)onegetsthesuccessivecontributionstotheseries (131).
Therefore,theexplicitansatzwearepropoundingreads
Y(t)=exp
(∞∑
k=1
Λk(t)
)
exp
(
t
∞∑
k=1
Fk
)
. (132)
Thiscanbeproperlyreferredasthe Floquet–Magnusexpansion.
180 S.Blanesetal./PhysicsReports470(2009)151–238
SubstitutingtheexpansionsofEq. (131)into(130)andequatingtermsofthesameorder,onecanwrite
Λ′
n=
n−1∑
j=0
Bj
j!
(
W(j)
n (t)+(−1)j+1T(j)
n (t)
)
(n≥1). (133)
ThetermsW(j)
n (t)maybeobtainedbyasimilarrecurrencetothatgiveninEq. (49)
W(j)
n =
n−j∑
m=1
[
Λm,W(j−1)
n−m
]
(1≤j≤n−1),
W(0)
1 =A, W(0)
n =O (n>1),
(134)
whereastheterms T(j)
n (t)obeytherecurrencerelation
T(j)
n =
n−j∑
m=1
[
Λm,T(j−1)
n−m
]
(1≤j≤n−1),
T(0)
n =Fn (n>0).
(135)
EveryFnisfixedbythecondition Λn(t+T)= Λn(t).Anoutstandingfeatureisthat Fncanbedeterminedindependently
ofΛn(t)asthesolution Y(t)=P(t)exp(tF)shrinkstoY(T)=exp(TF).Consequently,theconventionalMagnusexpansion
Y(t)=exp(Ω(t))computedat t=Tmustfurnish
Fn= Ωn(T)
T
, forall n. (136)
ThefirstcontributionstotheFloquet–Magnusexpansionread,explicitly,
Λ1(t)=
∫ t
0
A(x)dx−tF1,
F1=
1
T
∫ T
0
A(x)dx,
Λ2(t)=
1
2
∫ t
0
[A(x)+F1,Λ1(x)]dx−tF2, (137)
F2=
1
2T
∫ T
0
[A(x)+F1,Λ1(x)]dx.
Moreover,fromtherecurrencerelations (134)and(135)itispossibletoobtainasufficientconditionsuchthatconvergence
oftheseries
∑Λnisguaranteedinthewholeinterval t∈[0,T][34].Infact,onecanshowthatabsoluteconvergenceof
theFloquet–Magnusseriesisensuredatleastif
∫ T
0
‖A(t)‖dt<ξF≡0.20925. (138)
Noticethatconvergenceoftheseries
∑
Fnisalreadyguaranteedby (136)andthediscussionconcerningtheconventional
MagnusexpansioninSections 2.7.2and2.7.3.Thebound ξF intheperiodicFloquetcaseturnsouttobesmallerthan
thecorrespondingbound rc = πintheconventionalMagnusexpansion.Atfirstsightthiscouldbeunderstoodasan
impoverishmentoftheresult.However,ithastoberecalledthat,duepreciselytoFloquettheorem,oncethecondition
isfulfilledinoneperiod,convergenceisassuredforanyvalueoftime.Onthecontrary,inthegeneralMagnuscase,the
boundalwaysgivesarunningcondition.
3.3. Magnusexpansionsfornonlinearmatrixequations
It is possible to extend the procedure leading to the Magnus expansion for the linear equation(30), and obtain
approximatesolutionsforthenonlinearmatrixequation
Y′=A(t,Y)Y, Y(0)=Y0∈ G, (139)
where GisamatrixLiegroup, A : R+× G −→ gand gdenotesthecorrespondingLiealgebra.Eq. (139)appearsin
relevantphysicalfieldssuchasrigidbodymechanics,inthecalculationofLyapunovexponents( G≡ SO(n))andother
problemsarisinginHamiltoniandynamics( G≡Sp(n)).Infact,itcanbeshownthateverydifferentialequationevolvingon
amatrixLiegroup Gcanbewrittenintheform (139)[59].Moreover,theanalysisofgenericdifferentialequationsdefined
inhomogeneousspacescanbereducedtotheLie-groupEq. (139)[98].
S.Blanesetal./PhysicsReports470(2009)151–238 181
In[99]ageneralprocedurefordevisingMagnusexpansionsforthenonlinearequation (139)isintroduced.Itisbasedon
applyingPicard’siterationontheassociateddifferentialequationintheLiealgebraandretainingineachiterationtheterms
necessarytoincreasetheorder,whilemaintainingtheexplicitcharacteroftheexpansion.Theresultingmethodsarethus
explicitbydesignandareexpressedintermsofintegrals.
Asusual,thestartingpointintheformalismistorepresentthesolutionof (139)intheform
Y(t)=exp(Ω(t,Y0))Y0. (140)
Thenoneobtainsthedifferentialequationsatisfiedby Ω:
Ω′=dexp−1
Ω
(
A(t,eΩY0)
)
, Ω(0)=O, (141)
wheredexp−1
Ω isgivenby (38).Now,asinthelinearcase,onecanapplyPicard’siterationtoEq. (141),givinginstead
Ω[m+1](t)=
∫ t
0
dexp−1
Ω[m](s)A(s,eΩ[m](s)Y0)ds
=
∫ t
0
∞∑
k=0
Bk
k!
adk
Ω[m](s)A(s,eΩ[m](s)Y0)ds, m≥0.
Thenextstepingettingexplicitapproximationsistotruncateappropriatelythedexp −1operatorintheaboveexpansion.
Roughlyspeaking,whenthewholeseriesfordexp −1isconsidered,thepowerseriesexpansionoftheiteratefunction
Ω[k](t),k ≥ 1,onlyreproducestheexpansionofthesolution Ω(t)uptoacertainorder,say m.Inconsequence,the
(infinite)powerseriesof Ω[k](t)andΩ[k+1](t)differinterms O(tm+1).Theideaisthentodiscardin Ω[k](t)alltermsof
ordergreaterthan m.Thisofcourserequirescarefulanalysisofeachtermintheexpansion.Forinstance, Ω[0]=Oimplies
that(Ω[1])′=A(t,Y0)andtherefore
Ω[1](t)=
∫ t
0
A(s,Y0)ds=Ω(t,Y0)+ O(t2).
Since
A(s,eΩ[1](s)Y0)=A(0,Y0)+ O(s)
itfollowsatoncethat
−
1
2
∫ t
0
[Ω[1](s),A(s,eΩ[1](s)Y0)]ds= O(t3).
Whenthissecondtermin Ω[2](t)isincludedand Ω[3]iscomputed,itturnsoutthat Ω[3]reproducescorrectlytheexpression
ofΩ[2]upto O(t2).Thereforewetruncatedexp −1atthek=0termandtake
Ω[2](t)=
∫ t
0
A(s,eΩ[1](s)Y0)ds.
Withgreatergenerality,welet
Ω[1](t)=
∫ t
0
A(s,Y0)ds (142)
Ω[m](t)=
m−2∑
k=0
Bk
k!
∫ t
0
adk
Ω[m−1](s)A(s,eΩ[m−1](s)Y0)ds, m≥2
andtaketheapproximation Ω(t) ≈ Ω[m](t).Thisresultsinanexplicitapproximatesolutionthatinvolvesalinear
combinationofmultipleintegralsofnestedcommutators,sothat Ω[m](t)∈ gforall m≥ 1.Itcanalsobeprovedthat
Ω[m](t),onceinsertedin (140),providesanexplicitapproximation Y[m](t)forthesolutionof (139)thatiscorrectupto
terms O(tm+1)[99].Inaddition, Ω[m](t)reproducesexactlythesumofthefirst mtermsinthe ΩseriesoftheusualMagnus
expansionforthelinearequation Y′ = A(t)Y.Itmakessense,then,toregardthescheme (142)asanexplicitMagnus
expansionforthenonlinearequation (139).
Thisprocedurecanbeeasilyadaptedtoconstructanexponentialrepresentationofthesolutionforthedifferentialsystem
Y′=[A(t,Y),Y], Y(0)=Y0∈Sym(n). (143)
HereSym(n)standsforthesetof n×nsymmetricrealmatricesandthe(sufficientlysmooth)function Amaps R+×Sym(n)
into so(n),theLiealgebraof n×nrealskew-symmetricmatrices.ItiswellknownthatthesolutionitselfremainsinSym (n)
forall t ≥ 0.Furthermore,theeigenvaluesof Y(t)areindependentoftime,i.e., Y(t)hasthesameeigenvaluesas Y0.
Thisremarkablequalitativefeatureofthesystem (143)isthereasonwhyitiscalledan isospectralflow.Suchflowshave
182 S.Blanesetal./PhysicsReports470(2009)151–238
severalinterestingapplicationsinphysicsandappliedmathematics,frommoleculardynamicstomicromagneticstolinear
algebra[100].
SinceY(t)andY(0)sharethesamespectrum,thereexistsamatrixfunction Q(t)∈SO(n)suchthatY(t)Q(t)=Q(t)Y(0)
or,equivalently,
Y(t)=Q(t)Y0QT(t). (144)
Then,byinserting (144)into(143),itisclearthatthetimeevolutionof Q(t)isdescribedby
Q′=A(t,QY0QT)Q, Q(0)=I, (145)
i.e.,anequationoftype (139).Yetthereisanotherpossibility:ifweseektheorthogonalmatrixsolutionof (145)as
Q(t)=exp(Ω(t))withΩskew-symmetric,
Y(t)=eΩ(t)Y0e−Ω(t), t≥0,Ω(t)∈ so(n), (146)
thenthecorrespondingequationfor Ωreads
Ω′=dexp−1
Ω
(
A(t,eΩY0e−Ω)
)
, Ω(0)=O. (147)
InasimilarwayasforEq. (141),weapplyPicard’siterationto (147)andtruncatethedexp −1seriesat k=m−2.Nowwe
canalsoconsistentlytruncatetheoperator
AdΩY0≡eΩY0e−Ω=eadΩY0
and the outcome still lies inso(n). By doing so, we replace the computation of one matrix exponential by several
commutators.
Intheend,theschemereads
Ω[1](t)=
∫ t
0
A(s,Y0)ds
Θm−1(t)=
m−1∑
l=0
1
l!
adl
Ω[m−1](t)Y0 (148)
Ω[m](t)=
m−2∑
k=0
Bk
k!
∫ t
0
adk
Ω[m−1](s)A(s,Θm−1(s))ds, m≥2
and,asbefore,onehas Ω(t)=Ω[m](t)+ O(tm+1).Thus
Θ1(t)=Y0+[Ω[1](t),Y0]
Ω[2](t)=
∫ t
0
A(s,Θ1(s))ds
Θ2(t)=Y0+[Ω[2](t),Y0]+
1
2
[Ω[2](t),[Ω[2](t),Y0]]
Ω[3](t)=
∫ t
0
A(s,Θ2(s))ds−
1
2
∫ t
0
[Ω[2](s),A(s,Θ2(s))]ds
andsoon.Observethatthisprocedurepreservestheisospectralityoftheflow,sincetheapproximation Ω[m](t)liesin so(n)
forallm≥1andt≥0.Itisalsoequallypossibletodevelopaformalismbasedonrootedtreesinthiscase,inasimilarway
asforthestandardMagnusexpansion.
Example.Thedoublebracketequation
Y′=[[Y,N],Y], Y(0)=Y0∈Sym(n) (149)
wasintroducedbyBrockett[ 101]andChu&Driessel[ 102]tosolvecertainstandardproblemsinappliedmathematics,
althoughsimilarequationsalsoappearintheformulationofphysicaltheoriessuchasmicromagnetics[ 103].Here Nisa
constantn×nsymmetricmatrix.Itclearlyconstitutesanexampleofanisospectralflowwith A(t,Y)≡[Y,N].Whenthe
procedure(148)isappliedto (149),onereproducesexactlytheexpansionobtainedin[ 104]withtheconvergencedomain
establishedin[105]. □
3.4. Treatmentofgeneralnonlinearequations
Asamatteroffact,theMagnusexpansioncanbeformallygeneralizedtoanynonlinearexplicitlytime-dependent
differentialequation.Giventheimportanceoftheexpansion,ithas,indeed,been(re)derivedanumberoftimesalong
theyearsindifferentsettings.Wehavetomention,inthisrespect,theworkofAgrachevandGamkrelidze[ 106–108],and
S.Blanesetal./PhysicsReports470(2009)151–238 183
Strichartz[53].InthecontextofHamiltoniandynamicalsystems,theexpansionwasfirstproposedin[ 109]andsubsequently
appliedinamoregeneralcontextin[ 110]withtheaimofdesigningnewnumericalintegrationalgorithms.
Byintroducingnonstationaryvectorfieldsandflows,itturnsoutthatonegetsalineardifferentialequationintermsof
operatorswhichcanbeanalyzedinexactlythesamewayasinSection 2.Thusitisinprinciplepossibletobuildapproximate
solutionsofthedifferentialequationwhichpreservesomegeometricpropertiesoftheexactsolution.Thecorresponding
Magnusseriesexpansionallowsustowritetheformalsolution,andthendifferentapproximationscanbeobtainedby
truncatingtheseries.Obviously,thisformalexpansionpresentstwodifficultiesinordertorenderausefulalgorithmin
practice:(i)itisnotevidentwhatthedomainofconvergenceis,and(ii)somedevicehastobedesignedtocomputethe
exponentialmaponcetheseriesistruncated.
Nextwebrieflysummarizethemainideasinvolvedintheprocedure.Tobeginwith,letusconsidertheautonomous
equation
x′=f(x), x(0)=x0∈ Rn. (150)
Ifϕtdenotestheexactflowof (150),i.e. x(t)=ϕt(x0),thenforeachinfinitelydifferentiablemap g: Rn−→ R,g(ϕt(y))
admitstherepresentation
g(ϕt(y))=Φt[g](y) (151)
wheretheoperator Φtactsondifferentiablefunctions[ 111].Tobemorespecific,letusintroducetheLiederivative(orLie
operator)associatedwith f,
Lf=
n∑
i=1
fi
∂
∂xi
. (152)
Itactsondifferentiablefunctions F: Rn−→ Rm(see[112,Chap.8]formoredetails)as
LfF(y)=F′(y)f(y),
whereF′(y)denotestheJacobianmatrixof F.Itfollowsfromthechainrulethat,forthesolution ϕt(x0)of(150),
d
dt
F(ϕt(x0))=(LfF)(ϕt(x0)), (153)
andapplyingtheoperatoriterativelyonegets
dk
dtkF(ϕt(x0))=(Lk
fF)(ϕt(x0)), k≥1.
Therefore,theTaylorseriesof F(ϕt(x0))att=0isgivenby
F(ϕt(x0))=
∑
k≥0
tk
k!(Lk
fF)(x0)=exp(tLf)[F](x0). (154)
Now,puttingF(y)=Id(y)=y,theidentitymap,thisisjusttheTaylorseriesofthesolutionitself
ϕt(x0)=
∑
k≥0
tk
k!(Lk
fId)(x0)=exp(tLf)[Id](x0).
Ifwesubstitute Fbygin(154)andcomparewith (151),thenitisclearthat Φt[g](y)=exp(tLf)[g](y).Theobjectexp (tLf)
iscalledtheLietransformassociatedwith f.
Atthispoint,letussupposethat f(x)canbesplitas f(x)=f1(x)+f2(x),insuchawaythatthesystems
x′=f1(x), x′=f2(x)
haveflows ϕt
1andϕt
2,respectively,sothat
g(ϕt
i(y))=exp(tLfi)[g](y) i=1,2.
Then,fortheircompositiononehas
g(ϕt
2◦ϕs
1(y))=exp(sLf1)exp(tLf2)[g](y). (155)
Thisispreciselyformula (154)withf=f1,treplacedwith sandwith F(y)=exp(tLf2)[g](y).Noticethattheindices1and
2,aswellas sandttotheleftandrightofEq. (155),arepermuted.Inotherwords, theLietransformsappearinthereverse
ordertotheircorrespondingmaps [79].
TheLiederivative Lfsatisfiessomeremarkableproperties.Giventwofunctions ψ1, ψ2,itcanbeeasilyverifiedthat
Lf(α1ψ1+α2ψ2)=α1Lfψ1+α2Lfψ2, α 1,α2∈ R
Lf(ψ1ψ2)=(Lfψ1)ψ2+ψ1Lfψ2
184 S.Blanesetal./PhysicsReports470(2009)151–238
andbyinductionwecanprovetheLeibnizrule
Lk
f(ψ1ψ2)=
k∑
i=0
(
k
i
)(
Li
fψ1
)(
Lk−i
f ψ2
)
,
withLi
fψ=Lf
(
Li−1
f ψ
)
andL0
fψ=ψ,justifyingthenameofLiederivative.Inaddition,giventwovectorfields fandg,then
α1Lf+α2Lg=Lα1f+α2g,
[Lf,Lg]= LfLg−LgLf=Lh,
wherehisanothervectorfieldcorrespondingtotheLiebracketofthevectorfields fandg,denotedby h=(f,g),whose
componentsare
hi=(f,g)i=Lfgi−Lgfi=
n∑
j=1
(
fj
∂gi
∂xj
−gj
∂fi
∂xj
)
. (156)
Moreover,from(151)and(153)(replacingFwithg)wecanwrite
d
dt
Φt[g](x0)=
d
dt
g(ϕt(x0))=(Lfg)(ϕt(x0))=ΦtLf[g](x0).
Particularizingtothefunction g(x)=Idj(x)=xj,weget
d
dt
Φt[Idj](y)=ΦtLf(y)[Idj](y), j=1,..., n,y=x0
or,inshort,
d
dt
Φt=ΦtLf(y), y=x0, (157)
i.e.,alineardifferentialequationfortheoperator Φt.Noticethat,asexpected,Eq. (157)admitsasformalsolution
Φt=exp(tLf(y)), y=x0. (158)
Wecanfollowthesamestepsforthenon-autonomousequation
x′=f(t,x), (159)
where,now,theoperationalequationtobesolvedis
d
dt
Φt=ΦtLf(t,y), y=x0. (160)
Tosimplifynotation,fromnowonweconsider x0asasetofcoordinatessuchthat f(t,x0)isadifferentiablefunctionof x0.
SinceLfisalinearoperator,wecanthendirectlyusetheMagnusseriesexpansiontoobtaintheformalsolutionof (160)as
Φt=exp(Lw(t,x0)),withw=∑
iwi.Thefirsttwotermsarenow
w1(t,x0)=
∫ t
0
f(s,x0)ds
w2(t,x0)=−
1
2
∫ t
0
ds1
∫ s1
0
ds2(f(s1,x0),f(s2,x0)). (161)
Observethatthesignof w2ischangedwhencomparedwith Ω2in(43),andtheintegralsonlyaffecttheexplicittime-
dependentpartofthevectorfield.Ingeneral,duetothestructureofEqs. (30)and(160),theexpressionfor wn(t,x0)canbe
obtainedfromthecorresponding Ωn(t)inthelinearcasebyapplyingthefollowingrules:
(1)replaceA(ti)byf(ti,x0);
(2)replacethecommutator [·,·]bytheLiebracket (156);
(3)changethesignin wn(t,x0)foreven n.
Oncew[n]=∑n
i=1wi(t,x0)iscomputed,itstillremainstoevaluatetheactionoftheLietransformexp (Lw(t,x0))onthe
initialconditionsx0.Attime t=T,thiscanbeseenasthe1-flowsolutionoftheautonomousdifferentialequation
S.Blanesetal./PhysicsReports470(2009)151–238 185
y′=w[n](T,y), y(0)=x0, (162)
sincey(1)=exp(Lw(T,x0))x0=x(T).
AlthoughthisisarguablythemostdirectwaytoconstructaMagnusexpansionfor arbitrarytimedependentnonlinear
differentialequations,itisbynomeanstheonlyone.Inparticular,AgrachevandGamkrelidze[ 107,108]obtainasimilar
expansionbytransforming (160)intotheintegralequation
Φt=Id+
∫ t
0
Φs⃗Xsds (163)
whichissubsequentlysolvedbysuccessiveapproximations.Here,forclarity,wehavedenoted ⃗Xs≡Lf(s,x0).Thenonegets
theformalseries
Φt=Id+
∫ t
0
dt1⃗Xt1+
∫ t
0
dt1
∫ t1
0
dt2⃗Xt2
⃗Xt1+···
=Id+
∞∑
m=1
∫ t
0
dt1
∫ t1
0
dt2···
∫ tm−1
0
dtm⃗Xtm··· ⃗Xt1. (164)
Anobjectwiththisshapeiscalleda formalchronologicalseries [107],andthesetofallformalchronologicalseriescanbe
endowedwitharealassociativealgebrastructure.Itisthenpossibletoshowthatthereexistsanabsolutelycontinuous
formalchronologicalseries
Vt(⃗Xt)=
∞∑
m=1
∫ t
0
dt1
∫ t1
0
dt2···
∫ tm−1
0
dtmGm(⃗Xt1,..., ⃗Xtm) (165)
suchthat
Φt=exp(Vt(⃗Xt)).
HereGm(⃗Xt1,..., ⃗Xtm)areLiepolynomials,homogeneousofthefirstgradeineachvariable,whichcanbealgorithmically
constructed.Inparticular,
G1(⃗Xt1)=⃗Xt1
G2(⃗Xt1,⃗Xt2)=
1
2
[⃗Xt2,⃗Xt1]
G3(⃗Xt1,⃗Xt2,⃗Xt3)=
1
6
([⃗Xt3,[⃗Xt2,⃗Xt1]]+[[⃗Xt3,⃗Xt2],⃗Xt1]).
Theseries (165)ingeneraldiverges,eveniftheLieoperator ⃗Xtisanalytic[ 106].Nevertheless,incertaincasesconvergence
holds.Forinstance,if ⃗XtbelongstoaBanachLiealgebra Bforallt∈ R,whereonehasanormsatisfying ‖[X,Y]‖≤‖ X‖‖Y‖
forallX,Y∈ Band
∫t
0‖⃗Xs‖ds≡
∫t
0‖Lf(s,x0)‖ds≤0.44,thenVt(⃗Xt)convergesabsolutelyin B[107].Asamatteroffact,an
argumentanalogoustothatusedin[ 30,70]mayallowustoimprovethisboundandgetconvergencefor
∫ t
0
‖⃗Xs‖ds≤
1
2
∫ 2π
0
1
2+ x
2(1−cot x
2)
dx=1.08686870....
3.4.1. TreatmentofHamiltoniansystems
Wehaveseenhowthealgebraicsettingwehavedevelopedforlinearsystemsofdifferentialequationsmaybeextended
formallytononlinearsystems.WewillnextreviewhowitcanbeadaptedtotheimportantclassofHamiltoniansystems.In
thiscontext,theroleofaLiebracketofvectorfields (156)isplayedbytheclassicalPoissonbracket[ 113].
TheLiealgebraicpresentationofHamiltoniansystemsinClassicalMechanicshasbeenapproachedindifferentways,and
theMagnusexpansioninvokedinthiscontextbydiverseauthors[ 114–116].MoreexplicituseoftheMagnusexpansionis
donein[109]wheretheevolutionoperatorforaclassicalsystemisconstructedanditsdifferentialequationanalyzed.
Toparticularizetothissituationtheprecedinggeneraltreatment,letusconsiderasystemwith ldegreesoffreedom
andphasespacevariables x =(q,p)=(q1,..., ql,p1,..., pl),where (qi,pi),i=1,..., laretheusualpairsofcanonical
conjugatecoordinateandmomentum,respectively.BydefiningthePoissonbracketoftwoscalarfunctions F(q,p)and
G(q,p)ofphasespacevariablesintheconventionalway[ 113]
{F,G}≡
l∑
i=1
(∂F
∂qi
∂G
∂pi
− ∂F
∂pi
∂G
∂qi
)
,
186 S.Blanesetal./PhysicsReports470(2009)151–238
wehave
{F,G}=
2l∑
i,j=1
∂F
∂xi
Jij
∂G
∂xj
,
andinparticular
{xi,xj}= Jij.
HereJisthebasicsymplecticmatrixappearinginEq. (20)(withn= l).Withthesedefinitions,thesetof(sufficiently
smooth)functionsonphasespaceacquiresthestructureofaLiealgebraandwecanassociatewithanysuchfunction F(x)
aLieoperator
LF=
2l∑
i,j=1
∂F
∂xi
Jij
∂
∂xj
(166)
whichactsonthesamesetoffunctionsas LFG={F,G}.ItisthenasimpleexercisetoshowthatthesetofallLieoperators
isalsoaLiealgebraundertheusualcommutator [LF,LG]=LFLG−LGLFandfurthermore
[LF,LG]=L{F,G}.
GiventheHamiltonianfunction H(q,p,t): R2l× R→ R,where q, p∈ Rl,theequationsofmotionare
q′= ∇pH, p′=− ∇qH, (167)
or,equivalently,intermsof x,
x′=J ∇xH.
ItisthenelementarytoshowthattheLieoperator L−HisnothingbuttheLiederivative Lf(152)associatedwiththefunction
f=J ∇xH.
Therefore,theoperationalequation (160)becomes
d
dt
Φt
H=Φt
HL−H(y,t), y=x0 (168)
andtheprevioustreatmentalsoholdsinthissetting.Asaresult,theMagnusexpansionreads
Φt
H=exp(LW), (169)
whereW=∑∞
i=1Wiandthefirsttwotermsare
W1(x0)=−
∫ t
0
H(x0,s)ds (170)
W2(x0)=−
1
2
∫ t
0
ds1
∫ s1
0
ds2{H(x0,s1),H(x0,s2)}.
3.5. MagnusexpansionandtheChen–Fliessseries
Supposethat finEq. (159)hastheform f(t,x)= ∑m
i=1ui(t)fi(x),i.e.,wearedealingwiththenonlineardifferential
equation
x′(t)=
m∑
i=1
ui(t)fi(x(t)), x(0)=p, (171)
whereui(t)areintegrablefunctionsoftime.Systemsoftheform (171)appear,forinstance,innonlinearcontroltheory.In
thatcontext,thefunctions uiarethecontrolsand fiarerelatedtothenon-varyinggeometryofthesystem.Observethatthis
problemconstitutesthenatural(nonlinear)generalizationofthecasestudiedinSection 2.11.
Oneofthemostbasicproceduresforobtaining x(T)foragiven TisbyapplyingsimplePicarditeration.Forananalytic
outputfunctiong : Rn−→ R,from (153)itisclearthat
d
dt
g(x(t))=(L(∑
uifi)g)(x(t))=
m∑
i=1
ui(t)(Eig)(x(t)), g(x(0))=g(p), (172)
S.Blanesetal./PhysicsReports470(2009)151–238 187
where,forsimplicity,wehavedenotedby EitheLiederivative Lfi.Thiscanbeparticularizedtothecase g = xi,the ith
componentfunction.
Byrewriting(172)asanequivalentintegralequationanditeratingweget
g(x(t))=g(p)+
∫ t
0
m∑
i1=1
ui1(t1)(Ei1g)(x(t1))dt1
=g(p)+
∫ t
0
m∑
i1=1
ui1(t1)
(
(Ei1g)(p)+
∫ t1
0
m∑
i2=1
ui2(t2)(Ei2Ei1g)(x(t2))dt2
)
dt1
=g(p)+
∫ t
0
m∑
i1=1
ui1(t1)
(
(Ei1g)(p)+
∫ t1
0
m∑
i2=1
ui2(t2)
(
(Ei2Ei1g)(p)
+
∫ t2
0
m∑
i3=1
ui3(t3)(Ei3Ei2Ei1g)(x(t3))dt3
)
dt2
)
dt1 (173)
andsoon.Noticethat,inthisexpression,thetimedependenceofthesolutionisseparatedfromthenon-varyinggeometryof
thesystem,whichiscontainedinthevectorfields Eiandneedtobecomputedonlyonce,atthebeginningofthecalculation.
Next,wereversethenamesoftheintegrationvariablesandindicesused(e.g.,rename i1tobecome i3andviceversa),so
that
g(x(t))=g(p)+
m∑
i1=1
(∫ t
0
ui1(t1)dt1
)
(Ei1g)(p)+
m∑
i2=1
m∑
i1=1
(∫ t
0
∫ t2
0
ui2(t2)ui1(t1)dt1dt2
)
(Ei1Ei2g)(p)
+
m∑
i3=1
m∑
i2=1
m∑
i1=1
(∫ t
0
∫ t3
0
∫ t2
0
ui3(t3)ui2(t2)ui1(t1)dt1dt2dt3
)
(Ei1Ei2Ei3g)(p)+··· . (174)
ObservethattheindicesintheLiederivativesandintheintegralsareintheoppositeorder.Thisprocedurecanbefurther
iterated,thusyieldingtheformalinfiniteseries
g(x(t))=g(x(0))+
∑
s≥1
∑
i1···is
∫ t
0
∫ ts
0
···
∫ t3
0
∫ t2
0
uis(ts)··· ui1(t1)dt1··· dtsEi1··· Eisg(x(0)), (175)
whereeachij∈L={1,..., m}.Anexpressionoftheform (175)isreferredtoastheChen–Fliessseries,anditcanbeproved
that,undercertaincircumstances,itactuallyconvergesuniformlytothesolutionof (172)[90].ThisseriesoriginatesinK.T.
Chen’swork[117]ongeometricinvariantsanditeratedintegralsofpathsin Rn.Later,Fliess[ 118]appliedthetheorytothe
analysisofcontrolsystems.
OneofthegreatadvantagesoftheChen–Fliessseriesisthatitcanbemanipulatedwithpurelyalgebraicandcombinatorial
tools,insteadofworkingdirectlywithnestedintegrals.Toemphasizethisaspect,observethateachtermintheseriescan
beidentifiedbyasequenceofindicesor wordw=i1i2··· isinthe alphabetL throughthefollowingtwomaps:
M1:w=i1i2··· is↦−→
(
g↦→(Ewg)(p)=(Ei1Ei2··· Eisg)(p)
)
,
M2:w=i1i2··· is↦−→
(
u↦→
∫ t
0
uis(ts)
∫ ts
0
···
∫ t2
0
ui1(t1)dt1··· dts−1dts
)
.
Infact,thenestedintegralappearinginthemap M2canbeexpressedinasimpleway,aswedidforthelinearcasein (114)
αi1···is=
∫ t
0
uis(ts)
∫ ts
0
···
∫ t2
0
ui1(t1)dt1··· dts−1dts. (176)
Withthisnotation,theseriesoflineardifferentialoperatorsappearingattheright-handsideof (175)canbewritteninthe
compactform[91]
∑
w∈L∗
αwEw, (177)
whereL∗denotesthesetofwordsonthealphabet L={1,2,..., m},thefunction αwisgivenby (176)foreachword w∈L∗
and
Ew=Ei1··· Eis, ifw=i1··· is∈L∗.
ItwasprovedbyChenthattheseries (177)isanexponentialLieseries[ 117],i.e.,itcanberewrittenastheexponentialofa
seriesofvectorfieldsobtainedasnestedcommutatorsof E1,..., Em.Suchanexpressionisreferredtoinnonlinearcontrol
188 S.Blanesetal./PhysicsReports470(2009)151–238
astheformalanalogueofacontinuousBaker–Campbell–HausdorffformulaandalsoasthelogarithmoftheChen–Fliess
series[119].
NoticethesimilaritiesofthisprocedurewiththemoregeneraltreatmentcarriedoutinSection 3.4forthenonlinear
differentialequation(150).Thus,expression (164)constitutesthegeneralizationof (175)toanarbitraryfunction fin(150).
Conversely,thelogarithmoftheChen–FliessseriescanbeviewedasthecorrespondingnonlinearMagnusseriesforthe
particularnonlinearsystem (171).
Fromtheseconsiderations,itisclearthat,inprinciple,onecanobtainanexplicitformulaforthetermsofthelogarithm
oftheChen–FliessseriesinabasisoftheLiealgebrageneratedby E1,..., Em,butthisproblemhasbeenonlyrecentlysolved
foranynumberofoperators mandarbitraryorder,usinglabeledrootedtrees[ 91].Thus,forinstance,when m=2,itholds
that
∑
w∈L∗
αwEw=exp(β1E1+β2E2+β12[E1,E2]+ β112[E1,[E1,E2]]+ β212[E2,[E1,E2]]+··· ), (178)
where,notsurprisingly,theexpressionsofthe βcoefficientsaregivenby (113)withthecorrespondingchangeofsignin
β12duetothenonlinearcharacterofEq. (171).
AnotherrelevantconsequenceoftheconnectionbetweenMagnusseriesandtheChen–Fliessseriesisthefollowing:the
LieseriesdefiningthelogarithmoftheChen–Fliessseriescanbeobtainedexplicitlyfromtherecurrence (49)–(50),validin
principleforthelinearcase.Ofcourse,thesuccessivetermsoftheChen–Fliessseriesitselfcanbegeneratedbyexpanding
theexponential.
4. Illustrativeexamples
Afterhavingreviewed,intheprecedingtwosections,themaintheoreticalaspectsoftheMagnusexpansionandother
exponentialmethods,inthissectionwegathersomeexamplesoftheirapplication.Allofthemarestandardproblems
ofQuantumMechanicswheretheexactsolutionfortheevolutionoperator U(t)iswellknown.Duetotheirsimplicity,
higherordercomputationsarepossiblewithareasonableamountofeffort.Thecomparisonbetweenapproximateand
exactanalyticresultsmayhelpthereadertograsptheadvantagesaswellasthetechnicaldifficultiesofthemethodswe
haveanalyzed.
Theexamplesconsideredherearetreatedin[ 15,34,86,93],althoughsomeresultsareunpublishedmaterial,inparticular
thoseinvolvinghighestordercomputations.InSection 4.1wepresentresultsconcerningthemoststraightforwardwayof
dealingwithME,namelycomputationsintheInteractionPicture.InSection 4.2anapplicationofMEintheadiabaticbasisis
developed.Section4.3isdevotedtoillustratingtheexponentialinfinite-productexpansionsofFerandWilcox.Anexample
ontheapplicationoftheiterativeversionofMEbyVoslamberisgiveninSection 4.4.Eventually,Section 4.5containsan
applicationoftheFloquet–Magnusformalism.
4.1. MEintheInteractionPicture
WeillustratetheapplicationofMEintheInteractionPicture(seeSection 2.9)bymeansoftwosimpletime-dependent
physicalsystemsfrequentlyencounteredintheliterature,forwhichexactsolutionsareavailable:thetime-dependentforced
harmonicoscillator,andaparticleofspin 1
2inaconstantmagneticfield.Inthefirstcasewefix ¯h=1forconvenience.
Aswewillsee,MEintheInteractionPictureisappropriatewheneverthecharacteristictimescaleoftheperturbationis
shorterthanthepropertimescaleofthesystem.
Toillustrateandevaluatethequalityofthevariousapproximationsforthetime-evolutionoperator,wecomputethe
transitionprobabilitiesamongnon-perturbedeigenstates,inducedbythesmallperturbation.
4.1.1. Linearlyforcedharmonicoscillator
TheHamiltonianfunctiondescribingalinearlydrivenharmonicoscillatorreads( ¯h=1)
H=H0+V(t), withH0=
1
2
ω0(p2+q2),V(t)=
√
2f(t)q (179)
andf(t)isreal.Here qandpstandforthepositionandmomentumoperatorssatisfying [q,p]= iandω0givestheenergy
levelspacinginabsenceoftheperturbation V(t).Weintroducetheusualoperators a±≡ 1√
2(q∓ip),sothat [a−,a+]= 1.
Withthisnotationwehave
H0=ω0
(
a+a−+
1
2
)
, V=f(t)(a++a−). (180)
Theeigenstatesof H0aredenotedby |n⟩,sothat H0|n⟩= ω0(n+ 1
2)|n⟩,wherenstandsforthequantumnumber.Withthis
notationn=0correspondstothegroundstate.
S.Blanesetal./PhysicsReports470(2009)151–238 189
Forsimplicityinthecomputationswechoose ω0=1.InaccordancewiththeprescriptionsinSection 2.9,theHamiltonian
intheInteractionPictureisgivenby (92)andreads
HI(t)=eiH0tV(t)e−iH0t=f(t)(eita++e−ita−). (181)
Accordingly,theevolutionoperatorisfactorizedas
U(t,0)=exp(−iH0t)UI(t,0), (182)
wherethenewevolutionoperator UIisobtainedfrom U′
I=˜HI(t)UI≡−iHI(t)UI.
TheinfiniteMagnusseriesterminatesinthepresentexample.IthappensbecausethesecondorderMagnusapproximant,
whichinvolvesthecomputationof
[˜HI(t1),˜HI(t2)]= f(t1)f(t2)
(
ei(t1−t2)[a+,a−]+ e−i(t1−t2)[a−,a+]
)
=2if(t1)f(t2)sin(t2−t1) (183)
reducestoascalarfunction.ThustheMagnusseriesintheInteractionPicturefurnishestheexactevolutionoperator
irrespectiveoff(t):
UI(t,0)=exp
(∫ t
0
dt1˜HI(t1)−
1
2
∫ t
0
dt1
∫ t1
0
dt2[˜HI(t1),˜HI(t2)]
)
=exp
(
−i(αa++α∗a−)−iβ
)
=exp(−iαa+)exp(−iα∗a−)exp(−iβ−|α|2/2), (184)
wherewehavedefined
α≡
∫ t
0
dt1f(t1)eit1, (185)
β≡
∫ t
0
dt1
∫ t1
0
dt2f(t1)f(t2)sin(t2−t1). (186)
Eqs.(184)and(182)yieldtheexacttime-evolutionoperatorforthelinearlyforcedharmonicoscillatorHamiltonian
(179)[120].
Tocomputetransitionprobabilitiesbetweenfreeharmonicoscillatorstatesofquantumnumbers nandm,
Pn→m=|⟨m|UI|n⟩|2, (187)
thelastformin (184)ismostconvenient.Specifically,assumingthattheoscillatorwasinitiallyinitsgroundstate |0⟩,we
getinparticularthefamiliarPoissondistributionforthetransitionprobabilities
P0→n=
1
n!|α|2nexp(−|α|2). (188)
4.1.2. Two-levelquantumsystems
ThegenericHamiltonianforatwo-levelquantumsystemcanbewrittendownintheform
H(t)=
(
E1(t) C(t)
C∗(t) E2(t)
)
(189)
whereE1(t),E2(t)arerealfunctionsand C(t)is,ingeneral,acomplexfunctionof t.Wedefinethesolvablepieceofthe
Hamiltonianasthediagonalmatrix
H0(t)=
(
E1(t) 0
0 E2(t)
)
(190)
andallthetime-dependentinteractiondescribedbythefunction C(t)isconsideredasaperturbation.IntheInteraction
Picture,thenewHamiltonianreads(see (92))
HI(t)=


0 C(t)exp
(
i
∫ t
0
dt′ω(t′)
)
C∗(t)exp
(
−i
∫ t
0
dt′ω(t′)
)
0

 (191)
withω=(E1−E2)/¯h.Supposenowthat H0istime-independent.Then U(t)=exp(˜H0t)UI(t).Withoutlossofgenerality,
theH0mayberenderedtraceless,sothat E1=−E2≡E.Thus±Edenotetheeigenenergiesassociatedtotheeigenvectors
190 S.Blanesetal./PhysicsReports470(2009)151–238
|+⟩≡ (1,0)T,|−⟩≡ (0,1)TofH0,theunperturbedsystem.IntermsofPaulimatricestheHamiltonianinthiscasemaybe
expressedas
H(t)=
1
2¯hωσ3+f(t)σ1+g(t)σ2, (192)
wheref=Re(C)andg=−Im(C).
SinceH0isdiagonal,thetransitionprobabilitybetweeneigenstates |+⟩,|−⟩ofH0issimply
P(t)=|⟨+|UI(t)|−⟩|2. (193)
Astheevaluationof (193)requiresthecomputationandmanipulationofexponentialmatricesinvolvingPaulimatrices,
formulas(18)and(19)inSection 1.2comeinhandyhere.
Next,westudytwoparticularcasesofinteractionforwhichtheexactsolutionofthetimeevolutionoperatoradmitsan
analyticexpression.
1-Rectangularstep.Supposethatin (192)g=0,namely,
H(t)=
1
2¯hωσ3+f(t)σ1 (194)
withf =0for t <0and f =V0fort≥0.Alternatively,ifwerestrictourselvestocomputeanobservablesuchasthe
transitionprobability,thisexampleisequivalenttoarectangularmound(orrectangularbarrier)ofwidth T=tabove.The
exactsolutionforthisproblemreads
U(t,0)=exp
(
−i
(ω
2
σ3+
V0
¯h
σ1
)
t
)
, (195)
whichyieldstheexacttransitionprobability
Pex=
4γ2
4γ2+ξ2sin2
√
γ2+ξ2/4 (196)
betweeneigenstates|+⟩,|−⟩ofH0.Herewehavedenoted γ≡V0t/¯handξ≡ωt.
TheInteractionPictureisdefinedherebytheexplicitintegrationofthediagonalpieceintheHamiltonian,sothat
U=exp(−iξσ3/2)UI,where UIstandsforthetimeevolutionoperatorintheInteractionPictureandobeys
U′
I=˜HI(t)UI, UI(0)=I (197)
with
HI(t)=f(t)(σ1cosξ−σ2sinξ). (198)
Acomputationwiththeusualtime-dependentperturbationtheorygivesforthefirstorders(formula (52))
P(1)
pt =P(2)
pt =
4γ2
ξ2 sin2(ξ/2) (199)
P(3)
pt =P(4)
pt = γ2
ξ2
[
2sin
ξ
2
− γ2
3ξ2
(
9sin
ξ
2
+sin
3ξ
2
−6ξcos
ξ
2
+4sin3ξ
2
)]2
.
NoticethatP(i)
pt >1mayhappenintheequationsabovebecausetheunitarycharacteroftheoperator U(t)isnotpreserved
bytheusualtime-dependentperturbationformalism.
InthisexampleitisnotdifficulttocomputethefirstfourtermsintheMagnusseriescorrespondingto UI(t)=expΩ(t)
in(197).Tofacilitatethenotation,wedefine s=sinξandc=cosξ.TheMagnusapproximantsintheInteractionPicture
maybewrittendownintermsofPaulimatricesandreadexplicitly
Ω1=−i
γ
ξ[σ1s+σ2(1−c)]
Ω2=−i
(γ
ξ
)2
σ3(s−ξ)
Ω3=−i
(γ
ξ
)31
3
{σ1[3ξ(1+c)−(5+c)s]+ σ2[(3ξ−s)s−4(1−c)]}
Ω4=−i
(γ
ξ
)41
3
σ3[(4c+5)ξ−(c+8)s]. (200)
S.Blanesetal./PhysicsReports470(2009)151–238 191
Fig.3. Rectangularstep:Transitionprobabilitiesasafunctionof ξ,with γ=1.5.Thesolidlinecorrespondstotheexactresult (196).Brokenlinesstand
forapproximationsobtainedviaME,andlineswithsymbolscorrespondtoperturbationtheory,accordingtothelegend.Computationsuptofourthorder,
intheInteractionPicture.
Fig.4. Rectangularstep:Transitionprobabilitiesasafunctionof ξ,with γ = 2.Linesarecodedasin Fig.3.Computationsuptofourthorder,inthe
InteractionPicture.
Thefirsttwoformulaefortheapproximatetransitionprobabilitiesare,respectively
P(1)
M =sin2
(
2γ
ξ
sin(ξ/2)
)
P(2)
M =
4γ2
ξ2
sin2λ
λ2 sin2(ξ/2), λ =[4sin2(ξ/2)+γ2
ξ2(sinξ−ξ)2]1/2. (201)
Weomitexplicitexpressionsfor P(3)
M andP(4)
M sincetheyarequiteinvolved.However,weincludetheiroutputsin Figs.3–5,
whereweplotthefirsttofourthorderapproximatetransitionprobabilitieswithMEintheInteractionPictureandcompare
themtotheexactcase,andalsowithperturbationtheoryoutputs.In Figs.3 and4weset γ=1.5and γ=2respectively,
whereasinFig.5 wefix ξ=1.
WeobservethatfortheMagnusexpansionintheInteractionPicture,thesmallerthevalueoftheparameter ξ,thebetter
theapproximatesolutionworks.Asamatteroffact,inthesuddenlimit, ξ ≪ 1,MEfurnishestheexactresult;unlike
perturbationtheory.Asfarastheintensityoftheperturbation γincreases,thequalityoftheapproximationsspoils.This
effectismuchmoredramaticforthestandardperturbationtheory.
192 S.Blanesetal./PhysicsReports470(2009)151–238
Fig.5. Rectangularstep:Transitionprobabilitiesasafunctionof γ,with ξ = 1.Linesarecodedasin Fig.3.Computationsuptofourthorder,inthe
InteractionPicture.
Ontheotherhand,itisclearfrom (198)that
∫ t
−∞
‖HI(t1)‖2dt1=
∫ t
0
|f(t1)|dt1=V0t,
whence
∫t
−∞‖˜HI(t1)‖2dt1= γ,andthus Theorem9 guaranteesthattheMagnusexpansionintheInteractionPictureis
convergentif γ < π.Noticethatthisisalwaysthecasefortheparametersconsideredin Figs.3–5.Theestimate γ < π
fortheconvergencedomainintheInteractionPictureshouldbecomparedwiththecorrespondingoneintheSchrödinger
picture:
∫ t
−∞
‖˜H(t1)‖2dt1=
√
γ2+ξ2
4
<π.
Noticethenthat,aspointedoutinSection 2.9,achangeofpictureallowsustoimprovetheconvergenceoftheMagnus
expansion.
2-Hyperbolicsecantstep:Rosen–Zenermodel .IntheRosen–ZenerHamiltonian[ 121]theinteraction C(t)in(189)isgiven
bytherealfunction V(t)=V0sech(t/T),where Tdeterminesthetime-scale.Wewillusethenotation γ= πV0T/¯hand
ξ=ωT=2ET/¯h.
ThecorrespondingHamiltonianintermsofPaulimatricesis
H(t)=Eσ3+V(t)σ1≡a(t)·σ, V(t)=V0/cosh(t/T), (202)
witha≡(V(t),0,E).IntheInteractionPictureonehas
HI(s)=V(s)(σ1cos(ξs)−σ2sin(ξs)) (203)
intermsofthedimensionlesstime-variable s=t/T.Noticethat ξmeasurestheratiobetweenthe interactiontimeTand
theinternaltimeofthesystem ¯h/2E.From (203),andafterstraightforwardcalculation,thefirstandsecondMEoperators
arereadilyobtained.
Theexactresultforthetransitionprobability(providedthetimeintervalextendsfrom −∞to+∞),aswellas
perturbationtheoryandMagnusexpansionuptosecondorderread[ 15]
Pex=
sin2γ
cosh2(πξ/2)
P(1)
pt =P(2)
pt = γ2
cosh2(πξ/2)
P(1)
M =sin2[γ/cosh(πξ/2)]
P(2)
M =
sin2λ
λ2
γ2
cosh2(πξ/2)
(204)
λ=γ
[
1
cosh2(πξ/2)+γ2g2(ξ)
π4
]1/2
, g(ξ)=8ξ
∞∑
k=0
2k+1
[(2k+1)2+ξ2]2.
S.Blanesetal./PhysicsReports470(2009)151–238 193
Fig.6. Rosen–Zenermodel:Transitionprobabilities (204)asafunctionof ξ,with γ=1.5.Thesolidlinestandsfortheexactresult.Brokenlinesstand
forapproximationsobtainedviaME,andtrianglescorrespondtoperturbationtheory,accordingtothelegend.Computationsuptosecondorder,inthe
InteractionPicture.
Fig.7. Rosen–Zenermodel:Transitionprobabilitiesasafunctionof γ,with ξ=0.3.Linesarecodedasin Fig.6.Computationsuptosecondorder,inthe
InteractionPicture.
InFigs.6and7weplotsomeresultsfromtheformulaein (204).In Fig.6 wetake γ=1.5andin Fig.7 weset ξ=0.3.
Similarlytothecaseoftherectangularstep,weobservein Fig.6 thattheMagnusexpansionworksbetterinthesudden
regimedefinedby ξ≪1,namely,whentheinternaltimeofthesystem ¯h/2Eismuchlargerthanthetimescale Tofthe
perturbation.Also,Fig.7illustrateshowtheapproximationsspoilasfarastheintensity γincreases.Notice,inbothfigures,
theunitarityviolationoftheapproximationbuiltwiththeusualperturbationtheory.
Inthiscase,asimplecalculationshowsthat
∫ ∞
−∞
‖˜HI(t)‖2dt=(1/¯h)
∫ ∞
−∞
|V(t)|dt=V0πT/¯h=γ,
andthustheMagnusseriesconvergesatleastfor γ <π.
4.2. MEintheAdiabaticPicture
HerewewillillustratetheeffectofusingtheAdiabaticPictureintroducedinSection 2.9.Theuseofthistypeof
preliminarytransformationisconvenientwheneverthetimescaleoftheinteractionismuchlargerthanthepropertimeof
theunperturbedsystem.
194 S.Blanesetal./PhysicsReports470(2009)151–238
Sinceanadiabaticregimeconveysasmoothprofilefortheperturbation,namely,existenceofderivatives,thecaseofthe
rectangularstepcannotbeproperlyusedforthesakeofillustration.
4.2.1. Linearlyforcedharmonicoscillator
Forthelinearlydrivenharmonicoscillator,theprocedureyieldstheexactsolution,asintheprecedingSection 4.1.2,
albeitthemethodisabitmoretechnicallyinvolved[ 120].
4.2.2. Rosen–Zenermodel
Following[122]wewilldealwiththeRosen–Zenermodel(seeSection 4.1.2and[15])sinceitallowsaclearillustration
oftheadiabaticregime.
Thepreliminarylineartransformation G(s)definedin(94)fortheHamiltonian (202)isgivenby G(s)=ˆb·σ,wherethe
unitvectorˆbpointsinthedirection b=ˆa+ˆk(ˆk=unitvectoralongthe z-axis).Rememberthat s=t/Tisthedimensionless
time-variable.Theevolutionoperatorthengetsfactorizedas
UG(s)=GĎ(s)U(s)G(s0), (205)
which,accordingto (90),satisfiestheequation
dUG
ds
=˜HG(s)UG. (206)
Here˜HG≡−iHG/¯hisgivenby
˜HG(s)=
T
i¯h
aσ3−i
θ′
2
σ2, (207)
witha2=E2
0+V2
0/cosh2sandcot θ=(E0/V0)coshs.
Next,inanalogyto (203),weintroducetheAdiabaticInteractionPicturewhichallowsustointegratethediagonalpiece
of˜HG(s).Thetime-evolutionoperatorgetseventuallyfactorizedas
UG(s)=exp
(
(−iT/¯h)
∫ ∞
0
ds′a(s′)σ3
)
U(I)
G (s)exp
(
(−iT/¯h)
∫ 0
−∞
ds′a(s′)σ3
)
, (208)
whereU(I)
G (s)obeystheequation
dU(I)
G
ds
=˜H(I)
G (s)U(I)
G , (209)
with
˜H(I)
G (s)=−i(θ′/2)[σ1sinA(s)+σ2cosA(s)], (210)
and
A(s)=
2T
¯h
∫ s
0
ds′a(s′)= ξ
2
ln
1+ρ
1−ρ+
2γ
π
arctan
2γ
πξρ. (211)
Wehaveintroducedthedefinition
ρ={1−[1+(πξ/2γ)]sin2θ}1/2, (212)
intermsofthedimensionlessstrengthparameter γ = πV0T/¯handθ.UsingtheMEtofirstorderintheadiabaticbasis
(whichcoincideswiththefixedoneat s=±∞),onefindsthespin-flipapproximate(firstorder)transitionprobability
adP(1)
M =sin2
[∫ θ0
0
dθsinA(s(θ))
]
. (213)
InFig.8 wecomparethenumericalresultsgivenbythenewapproximation (213)withtheexactformula Pexin(204).For
thesakeofillustration,wealsoplottheresultsintheusualInteractionPicturetofirstorderinME(see P(1)
M in(204)).The
gainachievedwhenusingtheadiabaticMEintheintermediateregime(i.e.,moderatevaluesof ξ)isofnote,althoughonly
thefirstorderisconsidered.Here,theadiabaticregimecorrespondstolargevaluesof ξ=2ET/¯h(ε=1/T≪1).
Itshouldalsobenotedthat,fortheHamiltonian (210)onehas
∫ s
s0
‖˜H(I)
G (s1)‖2ds1=
1
2
|θ(s)−θ(s0)|<
1
2
2π=π
andthustheconvergenceconditiongivenby Theorem9 isalwayssatisfied.Inotherwords,forthisexample theMagnus
expansionisalwaysconvergentintheAdiabaticInteractionPicture .
MoreinvolvedillustrativeexamplesofMEintheAdiabaticPicturemaybefoundin[ 120,123].
S.Blanesetal./PhysicsReports470(2009)151–238 195
Fig.8. Rosen–Zenermodel:Transitionprobabilityasafunctionof ξ,with γ=1.Thesolidlinestandsfortheexactresultin (204).Theremaininglines
standforfirstordercomputationswithME(circles)andperturbationtheory(triangles).OpensymbolsarefortheAdiabaticPictureandsolidsymbolsfor
theInteractionPicture.
4.3. FerandWilcoxinfinite-productexpansions
NextweillustratetheuseofFerandWilcoxinfinite-productexpansionsbyusingthesametime-dependentsystemsas
before.
4.3.1. Linearlyforcedharmonicoscillator
Sincethecommutator[a−,a+]isac-number,FeriteratedHamiltonians H(n)withn>1eventuallyvanishsothat Fn=0
forn >2.TheWilcoxoperators Wnwithn >2ineq. (106)vanishforthesamereason.Thus,inthisparticularcase,the
second-orderapproximationineithermethodleadstotheexactsolutionoftheSchrödingerequation,justasMEdid.To
sumup,thefinalresultreads
UI=eΩ1+Ω2=eW1eW2=eF1eF2=e−iβe−i(αa++α∗a−), (214)
whereα(t)andβ(t)aregivenin (185)and(186),respectively.
4.3.2. Two-levelquantumsystem:Rectangularstep
FortheHamiltonian (194),thefirst-orderFerandWilcoxoperatorsintheInteractionPictureverify
F1=W1=Ω1=
∫ t
0
dt1˜HI(t1), (215)
where˜HI(t)isgivenby (198).Theexplicitexpressioniscollectedin (200)(firstequation).Analogously,thesecondequation
therealsocorrespondstothesecond-orderWilcoxoperator W2=Ω2.
ToproceedfurtherwithFer’smethod,wemustcalculatethemodifiedHamiltonian ˜H(1)in(96).Afterstraightforward
algebra,oneeventuallyobtains
˜H(1)=
1
2θ
(
sin2θ
θ −sin2θ+
1
θ
(
sin2θ
2θ −cos2θ
)
F1
)
[F1,˜HI], (216)
whereθ=(2γ/ξ) sin(ξ/2)(noticethat ˜H(1)andtherefore F2dependon σ1andσ2,while W2isproportionalto σ3).Since
itdoesnotseempossibletoderiveananalyticalexpressionfor F2,thecorrespondingmatrixelementshavebeencomputed
byreplacingtheintegralbyaconvenientlychosenquadrature.
Thetransitionprobability P(t)fromaninitialstatewithspinuptoastatewithspindown(orviceversa)isgivenby
(193).Thisexpressionhasbeencomputedassuming UI ≃ eF1 = eW1,UI ≃ eF1eF2,UI ≃ eW1eW2,UI ≃ eF1eF2eF3and
UI≃eW1eW2eW3,andtheresultshavebeencomparedwiththeexactanalyticalsolution (196).
InFigs.9and10weshowthetransitionprobability Pasafunctionof ξfortwodifferentvaluesof γ(γ=1.5and γ=2,
respectively),whilein Fig.11 wehaveplotted Pversusγforξfixed.NoticethatthesecondorderintheWilcoxexpansion
doesnotcontributetothetransitionprobability(thisissimilartowhathappensinperturbationtheory).Ontheotherhand,
Fer’ssecond-orderapproximationisalreadyinremarkableagreementwiththeexactresult,whereasthethirdordercannot
evenbedistinguishedfromtheexactresultin Fig.10atthecostofamuchlargercomputationaleffort.Wilcoxapproximants
preserveunitaritybutdonotgiveacceptableapproximations.
196 S.Blanesetal./PhysicsReports470(2009)151–238
Fig.9. Rectangularstep:Transitionprobabilityasafunctionof ξ,with γ=1.5.Thesolidlinecorrespondstotheexactresult (196).Brokenlinesstandfor
FerandWilcoxapproximationsuptothirdorder.Computationsuptothirdorder,intheInteractionPicture.
Fig.10. Rectangularstep:Transitionprobabilityasafunctionof ξ,withγ=2.Linesarecodedasin Fig.9.Computationsuptothirdorder,intheInteraction
Picture.
4.4. Voslamberiterativemethod
Justtokeepthesamestructureasinprecedingsubsections,wementionthattheVoslamberiterativemethodof
Section3.1alsoyieldstheexactsolutionforthelinearlydrivenharmonicoscillatoraftercomputingtheseconditeration.
Next,forthetwo-levelsystemwitharectangularstep,describedbytheHamiltonian (194),wecomputetheseconditerate
Ω(2)andcomparewithsecondorderMEapproximationfor UI.Asatest,weshallagainobtainthetransitionprobability P(t)
givenby (196).Theexpression (193)willbecalculatedhere,assuming: UI≃expΩ(1)=expΩ1,UI≃exp(Ω1+Ω2)and
UI≃expΩ(2).
ThesecondorderMagnusapproximationtothetransitionprobabilityisgivenby (201),whereastheseconditerateis
obtainedfrom(124),
Ω(2)(t)=−i
γ
ω
∫ ωt
0
{[sin2(∆)+cos2(∆)cosξ]σ1+cos2(∆)sinξσ2−sin(2∆)sin(ξ/2)σ3}dξ, (217)
where∆≡ γ
ω|sin(ξ/2)|,γ=V0t/¯h,ξ= ωt.Sinceitdoesnotseempossibletoderiveananalyticalexpressionfor Ω(2),
thecorrespondingmatrixelementshavebeencomputedbyapproximatingtheintegralin (217)withasufficientlyaccurate
quadrature.
S.Blanesetal./PhysicsReports470(2009)151–238 197
Fig.11. Rectangularstep:Transitionprobabilityasafunctionof γ,withξ=1.Linesarecodedasin Fig.9.Computationsuptothirdorder,intheInteraction
Picture.
Fig.12. Rectangularstep:Transitionprobabilityinthetwolevelsystemasafunctionof ξ,for γ=1.3:Exactresult (204)(solidline),seconditerateof
Voslambermethod(dashedline),secondorderME(dottedline)andfirstVoslamberiterate(ororderinME)(dash-dottedline).Computationsaredonein
theInteractionPicture.
InFig.12,thevariousapproximatedtransitionprobabilities,aswellastheexactresult (196),havebeenplottedasa
functionof ξforafixedvalue γ=1.5.Weobservethattheapproximationfromtheseconditeratekeepsthetrendofthe
exactsolutioninabetterwaythanthesecondorderMagnusapproximationdoes.
InFig.13wehaveplottedthecorrespondingtransitionprobabilitiesversus γforfixedvalue ξ=1.Althoughlocally,the
secondorderMagnusapproximationmaybemoreaccurate,itseemsthatthetrendoftheexactsolutionismimickedfora
longerintervalof γ.
Asithasalreadybeenpointedoutabove,theMagnusexpansionworksbetterthemoresuddentheperturbation.Thus,
there-summationinvolvedintheiterativemethodslightlyimprovesthatissue.Furtherresultsonthepresentexamplemay
befoundin[ 93].
4.5. Linearperiodicsystems:Floquet–Magnusformalism
Next we deal with a periodically driven harmonic oscillator, where the infinite expansions obtained from
Floquet–Magnusrecurrences(seeSection 3.2),areutterlysummed.Comparisonwiththeexactsolutionillustratesthe
feasibilityofthemethod.
TheparticularsystemweconsiderisdescribedbytheHamiltonian (179)withf(t)= β√
2cosωtandω0 < ω.Oncethe
recurrencesoftheFloquet–Magnusexpansion(seeSection 3.2)areexplicitlycomputedforseveralorders,theirgeneralterm
198 S.Blanesetal./PhysicsReports470(2009)151–238
Fig.13. Rectangularstep:Transitionprobabilityinthetwolevelsystemasafunctionof γ,for ξ=1.Linesarecodedasin Fig.12.Computationsaredone
intheInteractionPicture.
maybeguessedbyinspection.FortheFloquetoperatorweget
F=−i
[
ω0
2
(
p2+q2)
−βω0
ω
∞∑
k=0
(ω0
ω
)k
q+β2 ω0
4ω2
∞∑
k=0
(2k+1)
(ω0
ω
)k
]
, (218)
andtheassociatedtransformationresultsfrom
Λ(t)=iβ2ω0
ω3
[
sin(ωt)
∞∑
k=0
(k+1)
(ω0
ω
)k
−ωt
2
∞∑
k=0
(ω0
ω
)k
]
−i[sin(ωt)q+ω0(cos(ωt)−1)p]β
ω
∞∑
k=0
(ω0
ω
)k
. (219)
Theresultingseriesmaybesummedinclosedform,thusyieldingtheFloquetoperator
F=−i
ω0
2
[(
q− β
ω0(ρ2−1)
)2
+p2
]
−i
β2
4ω0
(
ρ2−1
), (220)
withρ≡ω/ω0.Itseigenvaluesaretheso-called Floqueteigenenergies[124]
En=ω0
(
n+
1
2
)
+ β2
4ω0
(
ρ2−1
). (221)
Thecorresponding Λtransformationaftersummationoftheseriesin (219)is
Λ(t)=i
β/ω0
1−ρ2
[
(ρsinωt)q+(cosωt−1)p+
(
2ρ2
1−ρ2+cosωt
)βsinωt
4ω
]
. (222)
Noticethat,astheyshould,bothoperatorsareskew-Hermitianandreproducetheexactsolutionoftheproblem.
5. NumericalintegrationmethodsbasedontheMagnusexpansion
