---
doc_id: 9-81
doc_title: "Singular Euclidean Structures on a Simplicial Complex with Weighted Edges KAMEISatoshi"
section_id: sec-002-3-singular-euclidean-structures
section_title: "Singular Euclidean Structures"
section_number: 3
pages: 5-6
source_pdf: 9_81.pdf
source_sha256: 12a83d647032306e
doc_brief: "Kamei, Singular Euclidean structures on a simplicial complex with weighted edges (2003) — extends Rivin's geometric structures on a 2-simplicial complex to weighted-edge assignments."
---
Inthissection,weconsiderwhen SadmitsasingularEuclideanstructure.Todiscussthat,wewillusesomeresultsof
hyperbolicgeometry.Atﬁrst,wepreparesomeelementarynotations.
Considertheupperhalf-space modelof H3 andanidealsimplexinit.Let A,B,C, 1betheverticesoftheideal
simplex,and /C11, /C12, /C13bethedihedralanglesattheedges 1A, 1B, 1Crespectively.Noticethat /C11, /C12, /C13areequaltothe
anglesofthetriangle ABConxy-planewhichisseenasaEuclideantriangle.AccordingtotheMilnor’sformula(see[2]
or[6]),thevolumeoftheidealsimplexisexpressedasthefollowing:
V ¼Vð/C11; /C12; /C13Þ¼ Lð/C11Þþ Lð/C12Þþ Lð/C13Þð 2Þ
whereLðxÞisthe Lobachevsky function
LðxÞ¼/C0
Zx
0
logð2 sin /C18Þd/C18: ð3Þ
Remark. Usuallytheintegrandof( 3)isdenotedby log j2 sin /C18j.Butwewillonlyconsiderthecasewhereeachangle
islessthan /C25.Thenweadoptthedeﬁnitionabove.
Lemma 3.1 ([3, Theorem 2.1]).V is convex onfð/C11; /C12; /C13Þ2 R3j/C11>0;/C12 >0;/C13 >0;/C11þ /C12þ /C13¼ /C25g.
Deﬁnition. A volume V ðA Þ of a locally Euclidean structureA 2 AðS;wÞ is the sum of the volumes of the ideal
simplicesofwhich dihedral angles areequaltotheanglesofthe2-faceswhich areassignedfrom A.
Lemma 3.2. V is convex onAðS;wÞ.
Proof. FromLemma3.1, V isconvexon fð/C111;/C121;/C131; ... ;/C11l;/C12l;/C13lÞ2 R3lj/C11i > 0;/C12i > 0;/C13i > 0;/C11i þ /C12i þ /C13i ¼ /C25for
1 /C20i /C20lg.Theconstraints fromaweightdeterminesanaﬃne subspace, then V isconvexon AðS;wÞ. /C3
Lemma 3.3. If AðS;wÞ is not empty, thenV has only one critical point onAðS;wÞ which gives the maximum value.
Proof. Let AðS;wÞbetheclosureof AðS;wÞ.Theclosure AðS;wÞiscompactand V iscontinuousonit.Thentoprove
theassertion, itissuﬃcienttoshowthatthecriticalpointisnoton @AðS;wÞ.
Let p 2 @AðS;wÞand q 2 int AðS;wÞ.Let pi andqi bethe i-thcoordinatesof pand qrespectively.Wemayassume
that qissuﬃcientlycloseto psothat max1/C20i/C20n jqi /C0pij < 1.Let v ¼ q /C0pand rðtÞ¼ p þtv.Wewillshowthatthe
inequality V ðp þtvÞ > V ðpÞholdsforasuﬃcientlysmallvalue t.Reorderthecoordinatesof pasp1 ¼ /C1/C1/C1 ¼pi0 ¼ 0
and 0 <pi0 þ1; ... ;pn </C25.Let f ðtÞ¼ V ðrðtÞÞ.When t > 0,itisseen that
f 0ðtÞ¼
Xn
i¼1
@V
@ri
/C12/C12/C12
rðtÞ
ðqi /C0piÞ:
LetMðpÞ¼ mini0 /C20i/C20nðminðpi;/C25/C0piÞÞ,andassumethat t <t0 ¼MðpÞ=ð2kvkÞ,then
f 0ðtÞ >
Xi0
i¼1
@V
@ri
/C12/C12/C12/C12/C12
rðtÞ
ðqi /C0piÞ/C0ðn /C0i0Þ log 2 sin MðpÞ
2
/C18/C19/C12/C12/C12/C12
/C12/C12/C12/C12: ð4Þ
Sincethefunction logð2 sinxÞiscontinuouson ð0;/C25Þandgoesto /C01atboth0and /C25,wecantakesuﬃcientlysmall
valueti foreach 1 <i <i0 sothattheinequality
@V
@ri
/C12/C12/C12/C12/C12
rðtÞ
ðqi /C0piÞ > ðn /C0i0Þ log 2 sin MðpÞ
2
/C18/C19/C12/C12/C12/C12
/C12/C12/C12/C12 ð5Þ
holdsfor 0 <t <ti.Let tmin ¼ minðt1; ... ;ti0 Þ.Thentheinequality f 0ðtÞ > 0holdsfor 0 <t <tmin from( 4)and( 5).By
the mean value theorem, there exists some value/C16for 0 </C16<tmin such that V ðrðtminÞÞ /C0V ðpÞ¼ f ðtminÞ/C0
f ð0Þ¼ f 0ð/C16Þ.Thus V ðrðtminÞÞ ¼f ðtminÞ >f ð0Þ¼ V ðpÞ. /C3
Nowweconsiderthegluingsoftheadjacent2-facesof SwhichadmitsthelocallyEuclideanstructurescomingfrom
w. Letc/C3¼ft1;t2; ... ;tk ¼t1g be an ordered collection of the 2-faces ofS such thatti and tj share an edge if
ji /C0jj¼ 1.Thecollection c/C3iscalleda dual cycleofS.
Deﬁnition. Let ti be a Euclidean triangle and assignti ¼ABC satisfying AB ¼ti/C01 \ti and AC ¼ti \tiþ1. The
dilatationofti withrespecttothevertex Aisthequantity Dðti;AÞ¼ log jACj/C0log jABj.
SingularEuclideanStructuresonaSimplicialComplex 85
Thenextlemmafollowsimmediately.
Lemma 3.4. Let /C11, /C12, /C13be the angles of a trianglet ¼ABC respectively. ThenDðt;AÞ¼ log sin /C12/C0log sin /C13.
Deﬁnition. Letvi ¼ti/C01 \ti \tiþ1.Thevalue Hðc/C3; A Þ¼ Pk/C01
i¼1 Dðti;viÞiscalledthe holonomyofc/C3.
Lemma 3.5. There exists a singular Euclidean structure onS if and only if the holonomies of all dual cycles ofS are
equal to 0.
Proof. Firstweassumethattheholonomiesofalldualcyclesof Sareequalto0.Takesomebase2-face t1.Forany
other2-face t,takeachainof2-faces a/C3¼ft1; ... ;tk ¼tgsuchthat ti andtiþ1 sharetheedge ei.Thisﬁxesthesizeof t,
andthevanishingsoftheholonomiesassurethatthissizeisindependentofthechoiceofthechain a/C3.Conversely,if
thereisasingularEuclideanstructureof S,theratiosofthelengthsofedgesareindependentofthechainconnecting
them,andhencetheholonomiesofalldualcycles of Sareequalto0. /C3
Lemma 3.6. The holonomies of all dual cycles ofS are equal to0 at the critical point ofV.
Proof. We consider the volumeV as a function ofR3jFðSÞj of which coordinates are the angles of the 2-faces ofS.
There are the constraints which are the equations/C11t þ /C12t þ /C13t ¼ /C25at eacht 2FðSÞ and PvalðeÞ
i¼1 /C11i ¼wðeÞ at each
e 2EðSÞ.
FromLemma3.3,thevolume V hasonecriticalpoint(andalsoitgivesthemaximumvalue).Let Mbethecritical
point.Take F as
F ¼ V ðA Þ/C0
X
t2FðSÞ
C1ðtÞð/C11t þ /C12t þ /C13t /C0/C25Þ/C0
X
e2EðSÞ
C2ðeÞ
XvalðeÞ
i¼1
/C11i /C0wðeÞ
 !
sothat
@F
@/C11j
/C12/C12/C12/C12/C12
M
¼ 0
fromtheLagrange’smethodofindeterminatecoeﬃcients.Let mj bethe j-thcoordinateof M.Let tj bethe2-faceof S
whichcontains /C11j,and ej betheedge of tj whichisoppositeto /C11j.Then
@F
@/C11j
/C12/C12/C12/C12/C12
M
¼/C0logð2 sinmjÞ/C0C1ðtjÞ/C0C2ðejÞ¼ 0: ð6Þ
Nowlet c/C3¼ft1;t2; ... ;th ¼t1gandvi ¼ti/C01 \ti \tiþ1.Let ei ¼ti/C01 \ti andeiþ1 ¼ti \tiþ1.From( 6)andLemma
3.4,Dðti;viÞ¼ C2ðeiþ1Þ/C0C2ðeiÞatM.Thustheholonomies ofalldualcyclesareequalto0. /C3
TheremainderofthissectionisdevotedtoprovethatthesingularEuclideanstructurein AðS;wÞisunique.Inorder
to see the uniqueness, it is suﬃcient to showthat any singular Euclidean structure is realized as a critical point of
V ðA Þ.
Lemma 3.7. There exists at most one singular Euclidean structure in all locally Euclidean structures onS coming
fromw.
Proof. We assume that the holonomies of all dual cycles are equal to 0, and construct ‘‘Lagrange multipliers’’
C
1 :FðSÞ! RandC2 :EðSÞ! R.Since C1 doesnotcontributetotheholonomy,itissuﬃcienttoconstruct C2.Let
ABCbesome2-faceof Sand /C11, /C12, /C13betheanglesofthe2-facecorrespondingtothevertices A;B;C.Itisclearthatwe
canconstruct C2 satisfyingC2ðABÞ/C0C2ðACÞ¼ logð2 sin /C12Þ/C0logð2 sin /C13Þ.
IfthereisasingularEuclideanstructureon Scomingfrom w,wetakemultipliersthesameasabove.Soitisacritical
pointof V.Ontheotherhand,thereisonlyonecriticalpointfromLemma3.3.ThenthesingularEuclideanstructurein
AðS;wÞisuniqueifitexists. /C3
Theorem 3.8. If AðS;wÞ is not empty, then there is a unique singular Euclidean structure.
Proof. Theassertionfollows fromLemma3.5andLemma 3.7. /C3
