---
doc_id: 9-81
doc_title: "Singular Euclidean Structures on a Simplicial Complex with Weighted Edges KAMEISatoshi"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 9_81.pdf
source_sha256: 12a83d647032306e
doc_brief: "Kamei, Singular Euclidean structures on a simplicial complex with weighted edges (2003) — extends Rivin's geometric structures on a 2-simplicial complex to weighted-edge assignments."
---
In [3] and [5], Rivin considered geometric structures on a 2-simplicial complex which is homeomorphic to an
orientablesurfacewhensomevaluesareassignedtotheedgesofthesimplicialcomplexandtheassignedvaluesare
distributedtotheverticesofthe2-facesastheirangles.Ifthereisadistributionsuchthatthesumoftheanglesofeach
2-face is equal to/C25, then each 2-face can be realized as a Euclidean triangle. The realization is called alocally
Euclidean structure on the simplicial complex. Furthermore if any adjacent facets are glued isometrically at
correspondingedges,therealizationiscalleda singular Euclidean structureonthesimplicialcomplex.In[5],Rivin
present a necessary and suﬃcient condition of the assignments in order for a 2-simplicial complex which is
homeomorphictoanorientablesurfacetoadmitlocallyEuclideanstructures.Furthermorein[3],heprovedthatthere
existsauniquesingularEuclideanstructureinthelocallyEuclideanstructuresonthesimplicialcomplexcomingfrom
someassignment.Inthispaper,wewillextendhisresults. Firstwepreparesomeelementarynotations.
Asimplicialcomplex C isaﬁnitesetofsimplicesinsomeEuclideanspacesuchthat(1)if /C272 C,allthefacesof /C27
(including the empty set) are contained inC, and (2) if/C27; /C27
0 2 C, then/C27\ /C270 is a face of both/C27and /C270.T h e0 -
dimensionalsimplicesin C arethe vertices,the 1-dimensionalsimplicesarethe edgesof C.Theinclusion-maximum
facesarethe facetsof C.Wedenotethesetofalledgesof C byEðC Þandthesetofall2-facesof C byFðC Þ.The
dimensionof C isthelargestdimensionofafacet.Ifallfacetsof C havethesamedimension,then C iscalled pure.In
particular,thesimplicialcomplexwhichhasonlytheemptysetasafaceisapuresimplicialcomplexofdimension /C01,
withasinglefacet.Theunion jC jofthesimplicesof C iscalledthe underlying spaceof C.If jC jishomeomorphicto
a manifoldM, thenC is atriangulation of M. In this paper, we also say thatC is homeomorphic toM if C is a
triangulationof M.A k-skeletonofasimplicialcomplexisasubcomplexmadeofallfacesofthesimplicialcomplex
whosedimensionsareatmost k.
Deﬁnition. LetSbeacompactconnectedpure2-simplicialcomplex.Foranyfacet FofS,if F \fS nFgisapure1-
simplicialcomplex,then Siscalleda branched surface.
We consider a functionw :EðC Þ!ð 0;/C25Þand call it aweightof the edges ofC, or simply a weight ofC. Now
assume that some weight w of C is given. Let e be an edge of C. Let A;B be the vertices of e and
ABC1;ABC2; ... ;ABCn bethe2-facesof C whichcontain e.Considerthedistributionof wðeÞtoC1;C2; /C1/C1/C1Cn suchthat
eachdistributedvalueispositive.Weregardeachdistributedvalueastheangleateachvertex.SeeFig. 1.
Deﬁnition. Let C beabranchedsurfaceoracompactconnectedpure3-simplicialcomplexwhichishomeomorphic
toa3-manifold,and nbethedimensionof C.Ifeachfacetof C canberealizedasaEuclideantriangleoraEuclidean
tetrahedron respectively and any adjacent facets are glued isometrically at correspondingðn /C01Þ-faces, then the
realizationiscalleda singular Euclidean structureon C.
Forabranchedsurface,wewillprovethefollowingtheorem.
Theorem 4.1. LetS be a branched surface andw be a weight ofS.L e tF0 be a subset ofFðSÞ, and letE0 be the set of
all edges contained in an element ofF0. Suppose that eachF0 satisﬁes
Interdisciplinary Information Sciences,Vol.9,No.1,pp.81–87(2003)
X
e2E0
wðeÞ/C21/C25jF0j
with equality if and only ifF0 ¼FðSÞ orF0 ¼ /C30. ThenS admits a unique singular Euclidean structure coming fromw.
Furthermorewewillprovethefollowingtheorem.
Theorem 4.2. Let C be a compact connected pure 3-simplicial complex which is homeomorphic to a 3-manifold and
wbeaweight of C.Let Sbethe2-skeleton of C.Let F0 beasubsetof FðSÞandE0 betheset ofall edgescontainedin an
element ofF0. Suppose that eachF0 satisﬁes
X
e2E0
wðeÞ/C21/C25jF0j
with equality if and only ifF0 ¼FðSÞ orF0 ¼ /C30. Then C admits a singular Euclidean structure coming fromw.
InSect.2,wewillconsideranecessaryandsuﬃcientconditionofaweightofabranchedsurfaceinorderforeach2-
face of the branched surface to be realized as a Euclidean triangle. We will regard the set of the realizations as the
feasible regionofalinearprogramandusesomewell-knownresults oflinearprogramming.
InSect.3,wewillconsiderthegluingsoftheadjacent2-facesofabranchedsurface.Forthepurpose,wewilluse
someresults ofhyperbolicgeometry.
Remark. (1) The proof of Theorem 4.1 can be proceeded almost parallel to [3] and [5]. But we will give precise
proofsbecausethedeﬁnitionofaweightisdiﬀerentfromthe‘‘dihedralangle’’statedin[3]and[5].(2)In[3]and[5],
Rivinconsideredonlythecasewhereasurfaceisorientable.Buttheorientabilityisnotanessentialrestriction.Infact,
wecanprovethesamestatementsinthenonorientablecases(CompareDeﬁnition3.5andDeﬁnition6.4in[3]).Inthis
paper,wewillconsiderbothcasesimplicitly.
