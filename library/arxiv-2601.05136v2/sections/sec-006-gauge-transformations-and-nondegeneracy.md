---
doc_id: arxiv-2601.05136v2
doc_title: "N(K,ρ,µ ) of a knotK, a representationρ: π1(S3\K)→ SL2(C), andalogarithm µofameridianeigenvalueof ρ. Itcanbeinterpretedasa geometrictwistoftheKashaevinvariantorasaquantizationofthe"
section_id: sec-006-gauge-transformations-and-nondegeneracy
section_title: "Gauge transformations and nondegeneracy"
section_number: null
pages: 6-8
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
doc_brief: "Stateintegralsforthequantized SL2(C)Chern-Simonsinvariant CalvinMcPhail-Snyder DepartmentofMathematics,DukeUniversity calvin@sl2.site — Previous work of the author and N."
---
Thediagram D determinesasemi-idealtriangulation TD ofS3\K (withtwonon-idealpoints)
called theoctahedral decomposition; we refer to [KKY18] for a detailed discussion and [McP22;
McP25b]fortherelationshiptoourparameters. TD assignseachcrossingof D fourtetrahedra,
withoneineachcornerofthecrossing. Thesegmentparametersnaturallyparametrizehyperbolic
structuresonthesetetrahedraintermsof shape parameterszk. Labelingthesegmentsandcorners
ofacrossingas
(2.6)
2
2′1
1′
N
W
S
E
2. Preliminaries 6
5 Strictly speaking a shape parameterz =
z0 corresponds to a pair of edges of a vertex-
orderedtetrahedron,withtheotheredgepairs
assignedz1 = 1/(1−z0)andz2 = 1−1/z0.
Admissibilitymeansthataparticularpreferred
edgepairisnot 0or∞.
[KC26]S.KimandP.Choi, Diagram.site: Bound-
ary parabolic representations for knots
6 Moreformallytheassociatedoctahedralde-
compositionisessential.
theshapeparametersofthetetrahedraaregivenby
(2.7)
zN =
b2′
b1
ϵ
zS =
b2
b1′
ϵ
zW =
 b2
mb1
ϵ
zE =
mb2′
b1′
ϵ
whereϵisthesignofthecrossing. Theshapeparametersariseascrossratiosofthepositionsofthe
verticesin CP1. Inparticularatetrahedronisgeometricallydegeneratewhenitsshapeparameter
liesin{0, 1,∞}.
Ifashadowcoloringisadmissibleasdeﬁnedabovethennoneoftheshapeparametersof TD are
0or∞.5 Thisisanecessaryconditiontodeﬁne Zψ
N,andeveryrepresentation ρisgauge-equivalent
toanadmissibleone. Since Zψ
N isgauge-invariantthisallowsustodeﬁneitforany ρ.
Deﬁnition2.7([McP25b,Section4]) .Let (ρ,u )beashadowcoloringof D withsegmentcolors
i7→ (gi, [vi])andregioncolors j7→uj. Agauge transformationofitisacoloringoftheform
(A) i7→ (h−1gih,Lih)andj7→h−1uj
(B) i7→ (gi,Li)andj7→h−1uj
for someh∈ SL2(C). We say the new colorings are the images oftype (A)and type (B)gauge
transformationsbyh.
Lemma2.8([McP25b,Theorem2]) .Letρbeadecoratedrepresentationand D anopendiagram
ofK. Any shadow coloring(ρ,u ) ofD is gauge-equivalent to one with an admissible shadow
coloring. ⌟
Whilewecanensuretheshapeparametersliein C\{0}wecannotnecessarilyensuretheyavoid
1. Havingshapeparameter 1isindependentofthechoiceofshadowcoloringandisequivalenttoa
naturalconditiononthedecoratedrepresentation:
Deﬁnition2.9.Acrossingwithadecorated SL2(C)-coloring
(g2, [v2])
(g2′, [v2′])(g1, [v1])
(g1′, [v1′])
ispinchedif [v1] = [v2],equivalently [vi] = [vj]foranypair (i,j )ofadjacentsegments. (Notethat
thisconditiondoesnotdependonachoiceofshadowcoloring.) Acoloringofadiagramispinched
ifanyofitscrossingsare. If ρisadecoratedrepresentationof K andD anopendiagramof K we
sayD isρ-pinchedifthecoloringinducedby ρispinched(andconverselythat ρisD-pinched). If
nocrossingispinchedwesay (D,ρ )issmooth.
Anugatorycrossingisalwayspinched. If D isacrossing-minimaldiagramithasnonugatory
crossingsandinthiscasemost(butnotall)nontrivialrepresentations ρareD-smooth. Forexample,
uptogaugetransformationthe 85 knothas 11boundary-parabolicrepresentations[KKY18]. In
the standard diagramD [KKY18, Figure 28] of this knot10 are smooth and1 is pinched.85 is
hyperbolic and its discrete faithful representation isD-smooth. According to the database of
boundary-parabolic representations computed by Kim and Choi [KC26] this pattern holds in
general: forcrossing-minimalDmostbutnotallrepresentationsare D-smooth,butthehyperbolic
holonomyrepresentationisalwayssmooth.
Inthestandardterminologyanot ρhyp-pincheddiagramissaidtobe essential.6 By[McP25b,
2. Preliminaries 7
7 We denote these byai because they corre-
spondtoratiosoftheregionparameters aj.
Theorem3]beingessentialisequivalenttoapurelygroup-theoreticconditioncalled arc-faithfulness.
Itisnothardtoseethatif Disnotarc-faithfulthenitispinchedforeverydecoratedrepresentation
ρ. Itisnaturaltoconjecture(see[McP25b,Section5])thatanyhyperbolicknothasanarc-faithful
diagram. Itisknownthatanyreducedalternatingdiagramofahyperbolicknotisarc-faithful.
At any pinched crossing the shape parameters are1 so theR-matrix elements deﬁningZψ
N
encounterthepolesandzerosofthequantumdilogarithm. Onecanshowthatthesecancel,butin
adelicatewaythatpreventsourstateintegralsfrombeingwell-deﬁned. Moregenerallytoavoid
thesingularitiesweneedtoensurethatnoshapeparameterhasnorm 1,andifnocrossingsare
pinchedthenwecanachievethisviaagaugetransformation.
Lemma 2.10 ([McP25b, Corollary 5.3]).Letρ be a decorated representation of a knotK andD
be an open diagram ofK. Suppose thatD is notρ-pinched. Then there is a representationρ′
gauge-equivalentto ρandashadowcoloring (ρ′,u )ofD inwhichnoshapeparameterhasnorm
1. Inthiscasewesay (ρ′,u )avoids the unit circle. ⌟
