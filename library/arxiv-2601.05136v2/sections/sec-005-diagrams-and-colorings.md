---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL₂(ℂ) Chern–Simons invariant"
section_id: sec-005-diagrams-and-colorings
section_title: "Diagrams and colorings"
section_number: null
pages: 5-6
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
doc_brief: "State integrals for the quantized SL₂(ℂ) Chern–Simons invariant — Previous work of the author and N."
---
Deﬁnition2.1.Adecoratedrepresentation ofaknot Kisarepresentation ρ: π1(S3\K)→ SL2(C)
andachoiceofeigenspacefortheimageofeachperipheralsubgroupof K underρ.
More formally, given a choice of peripheral subgroupΠ⊂ π1(S3\K) a decoration is an
eigenspaceL⊂ C2 ofρ(Π), which we take to be a right eigenspace. This does not depend on
thechoiceofperipheralsubgroup: anyotherchoiceisaconjugate y−1Πy andthecorresponding
eigenspace isLρ(y). An orientation ofK determines a meridianm∈ Πand the decorationL
determinesaneigenvalue m∈ C× by
vρ(m) =m−1v
wherevisanynonzeroelementof L. Theinverseisunfortunatebutcorrectandischosentomatch
theconventionsof[MR25;McP25a]. Clearly mdoesnotdependonthechoiceof Π.
Deﬁnition2.2.LetK beanoriented,framedknotin S3. Anopen diagramofK isanoriented,
blackboard-framedtanglediagram D withoneincomingandoneoutgoingboundarycomponent
whoseclosureisadiagramof K. ThesegmentsofD aretheedgesofitsunderlyinggraph. Wecall
thetwosegmentsincidenttotheboundaryofthetanglethe boundary segments,calltheremainder
the internal segments, and writeE for the set of internal segments ofD. Writingcr(D) for the
crossingnumberofthediagramwehave 2 cr(D) =|E| + 1.
Deﬁnition2.3.Adecorated matrixis a pair(g, [v])∈ SL2(C)× CP1 of a matrixg and a right
eigenspace [v]forg. Thedistinguished eigenvalueof (g, [v])isthe m∈ C× satisfying
vg =m−1v.
Wedeﬁneabinaryoperationondecoratedmatricesby
(2.1) (g, [v])◁ (h, [w]) := (h−1gh, [vh])
Adecorated SL2(C)-coloringofatanglediagram D assignsdecoratedmatricestoeveryarcof D
subjecttothecrossingrelations
(2.2)
g2
g2◁g 1g1
g1
g1
g1◁g 2g2
g2
where◁istheinverseof ◁deﬁnedby (g, [v])◁ (h, [w]) := (hgh−1, [vh−1]).Wealwaysrequire
thata SL2(C)-coloringofanopendiagramassignsthesamedecoratedmatrixtobothboundary
segments,orequivalentlythatitgivesawell-deﬁnedcoloringoftheclosure.
2. Preliminaries 5
[KKY18]H.Kim,S.Kim,andS.Yoon,“Octahe-
draldevelopingofknotcomplementI:Pseudo-
hyperbolicstructure”. arXiv doi
TheWirtingerpresentationof π1(S3\K)makesitclearthatdecoratedrepresentationsof
K areinbijectionwithdecorated SL2(C)-coloringsof D sowedenotebothby ρ. Todeﬁneour
invariantweneedtomakeanadditionalchoiceofdiagram-dependentgaugedata. 4 Thevalueof
Zψ
N isindependentofthischoice.
Deﬁnition2.4.Ashadow coloring(ρ,u )ofadiagram D isadecorated SL2(C)-coloringρofD
alongwithanassignment u: j7→uj ofcolumnvectors uj∈ C2 totheregions j ofD,subjectto
therule
(2.3) (g, [v])
u
gu
Inthediagramabovewesaytheregionlabeledby uisabovethesegment.
It is not hard to see that a shadow coloring is determined uniquely by the vectoru0∈ C2
assignedtothetopmostregionof D (ortoanyotherregion).
Deﬁnition2.5.Ashadowcoloringofadiagram D deﬁnesregion parameters
(2.4) aj := e1uj foreachregion j
andsegment parameters
(2.5) bi :=−vie2
viui↑
foreachsegment i
wherei↑ istheregionabovesegment i:
(gi, [vi])
ui↑
Ifnoneoftheregionorsegmentparametersare 0or∞wesaytheshadowcoloringis admissible.
Deﬁnition2.6.Ashadowcoloring (ρ,u )ofanopendiagram D isnormalizedifitisadmissible
andthesegmentparameterassignedtotheopensegmentsis 1.
Clearly one can always choose a normalized coloring by rescaling the vectorsui. This is a
specialcaseofthetype(B)gaugetransformationdeﬁnedbelow.
