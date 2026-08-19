---
doc_id: phys-rep09
doc_title: "PhysicsReports470(2009)151–238 Contents lists available at ScienceDirect PhysicsReports journal homepage: www.elsevier.com/locate/physrep TheMagnusexpansionandsomeofitsapplications"
section_id: sec-003-electromagnetism
section_title: "Electromagnetism"
section_number: null
pages: 82-82
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
doc_brief: "PhysicsReports470(2009)151–238 PhysicsReports TheMagnusexpansionandsomeofitsapplications S.Blanes a,F.Casas b,J.A.Oteo c,J.Ros c,d,∗ aInstitutodeMatemáticaMultidisciplinar,UniversidadPolitécnicadeVale"
---
TheMaxwellequationsgoverntheevolutionofelectromagneticwaves.Theequationsarelinearintheusualformand,
althoughtheyhavebeenextensivelystudied,thecomplexityofobtainingapproximatesolutionsisrathersignificant.When
reformulatingtheequationsforagivenproblem,wherethegeometry,theboundaryconditionsetc,areconsidered,and
appropriatediscretizationsaretakenintoaccount,itiscommontoendwithlinearnon-autonomousequations,sothe
Magnusexpansioncanbeofinteresthere.
Toillustratesomepossibleapplications,letusconsidertheMaxwellequations



∂H
∂t
=−
1
µ∇× E
∂E
∂t
=
1
ε∇× H−
1
ε
J(t)
(355)
whereH,E,Jarethemagneticandelectricfieldintensities,andthecurrentdensity,respectively, µisthepermeability
andεisthepermittivity.Afterspacediscretization,theseequationsturnintoalargelinearsystemofnon-homogeneous
equationsandMagnusintegratorscan,inprinciple,beapplied.Timedependentcontributionscanalsoappearfromboundary
conditionsorexternalinteractions.Insomecases J=σE[225,226],sothat,iftheconductivity σisnotconstant,Magnus
integratorscanbeuseful.
LetusnowconsiderthefrequencydomainMaxwellequations(with J=0)
{
∇× E=iwµH
∇× H=−iwεE (356)
wherewistheangularfrequency.Theseequationsareofinterestfortime-harmoniclightwaves,propagatinginawave-
guidingstructurecomposedoflinearisotropicmaterials.Ifoneisinterestedinthe xandycomponentsofHandE,andhow
theypropagateinthe zdirection,theequationstosolve,afterappropriatediscretization,taketheform[ 227]
−iwε
du
dz
=A(z)v, −iwµ
dv
dz
=B(z)u. (357)
Hereu,varevectorsand A,Bmatricesdependingon z,which,inthiscase,playtheroleofevolutionparameter.Afourth-
orderMagnusintegratorhasbeenusedin[ 227].FromSection 5weobservethathigherorderMagnusintegrators,combined
withsplittingmethods,couldalsoleadtoefficientalgorithmstoobtainaccuratenumericalresultswithpreservedqualitative
propertiesoftheexactsolution.
