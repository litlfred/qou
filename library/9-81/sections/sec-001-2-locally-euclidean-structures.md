---
doc_id: 9-81
doc_title: "Singular Euclidean Structures on a Simplicial Complex with Weighted Edges"
section_id: sec-001-2-locally-euclidean-structures
section_title: "Locally Euclidean Structures"
section_number: 2
pages: 2-5
source_pdf: 9_81.pdf
source_sha256: 12a83d647032306e
doc_brief: "Kamei, Singular Euclidean structures on a simplicial complex with weighted edges (2003) — extends Rivin's geometric structures on a 2-simplicial complex to weighted-edge assignments."
---
Inthissection,weconsideranecessaryandsuﬃcientconditionofaweightofabranchedsurfaceinorderforthe
branched surfacetoadmitlocallyEuclideanstructures,whichisstatedinthefollowingdeﬁnition.
Deﬁnition. Assumethatsomepositivevaluesareassignedtotheverticesofthe2-facesofabranchedsurfaceandthe
sumoftheassignedvaluesofeach2-faceisequalto /C25,theneach2-facecanberealizedasaEuclideantriangle.The
realizationiscalleda locally Euclidean structureonthebranched surface.
Firstweconsideranecessarycondition.Let Sbeabranchedsurfaceand wbeaweightof S.Thefollowingstatement
arisesnaturally.
Lemma2.1. LetF
0 /C18FðSÞ, and letE0 be the set of all edges contained inF0.I fSadmits a locallyEuclidean structure,
then
X
e2E0
wðeÞ/C21/C25jF0j ð1Þ
with equality if and only ifF0 ¼FðSÞ orF0 ¼ /C30.
Fig.1.
82 KAMEI
Proof. Theassertionfollows immediatelyfromthedeﬁnitionofaweight. /C3
Nextwewillseethatthenecessaryconditionaboveturnsouttobeasuﬃcientcondition,thatis,if wsatisﬁesthe
conditionofLemma2.1,then SalwaysadmitslocallyEuclideanstructures.Toseethat,weregardthesetofthelocally
Euclideanstructureson Scomingfrom wasthefeasibleregionofalinearprogram.Furthermoreweusethefollowing
theorem,whichisknownasDualityTheoremoflinearprogramming.See[1]fortheproofofDualityTheorem.Also
see[1]or[5]forbasic notations oflinearprogramming.
Theorem 2.2 (Duality Theorem). LetP be a linear program of the form:
minimize cx
T ; subject to the constraints AxT ¼ aT and x /C210:
Then the dual programP/C3is the following form:
maximize a/C21T ; subject to the constraints /C21A /C20cT :
The feasible region ofP is empty if and only if the objective function ofP/C3is not bounded. Conversely, the feasible
region ofP/C3is empty if and only if the objective function ofP is not bounded. If neither feasible region is empty, then
the values of the objective functions ofP andP/C3are equal.
NowwesetalinearprogramcorrespondingtothelocallyEuclideanstructureson Scomingfrom w.Let l ¼jFðSÞj
andm ¼jEðSÞj.Let valðeÞbethevalenceoftheedge eofS.Considerthefollowinglinearprogram.
Minimize ð0; ... ; 0Þ/C1ð/C111;/C121;/C131; ... ;/C11l;/C12l;/C13lÞT,subjectto
1. eachangleisstrictlypositive,
2. foreach2-face t,thesumofthreeangles /C11t þ /C12t þ /C13t isequalto /C25,
3. foreachedge e,wðeÞ¼ PvalðeÞ
i¼1 /C11i whereeach /C11i istheangleatthevertexwhich isoppositeto e.
Atﬁrst,weloosentheﬁrstconstraintaseachanglemaybe0,anddenotethelinearprogramby P.Wecanexpress P
usingamatrix asthefollowing.
Minimize ð0; ... ; 0Þ/C1ð/C111;/C121;/C131; ... ;/C11l;/C12l;/C13lÞT,subjectto
111000. . .000
000111. . .000
..
. ..
. ..
. ..
. ..
. ..
. . .
. ..
. ..
. ..
.
000000. . .111
010000. . .001
..
. ..
. ..
. ..
. ..
. ..
. . .
. ..
. ..
. ..
.
100010. . .100
0
BBBB
BBB
B
BBB
BB@
1
CCCC
CCC
C
CCC
CCA
/C11
1
/C121
/C131
...
/C11l
/C12l
/C13l
0
BBBB
BBB
BBB
BB@
1
CCCC
CCC
CCC
CCA
¼
/C25
/C25
..
.
/C25
wðe
1Þ
..
.
wðemÞ
0
BBBB
BBB
B
BBB
BB@
1
CCCC
CCC
C
CCC
CCA
and
/C11
1;/C121;/C131; ... ;/C11l;/C12l;/C13l
/C0/C1
/C210:
Thenthedualprogramof Pturnsouttobethefollowingform.
Maximize Fðu; vÞ¼ /C25P
t2FðSÞut þ P
e2EðSÞwðeÞve,subjectto
1. ut þve /C200whenevereisanedge of t.
Lemma 2.3. If the condition of Lemma 2.1 is satisﬁed, then the objective functionFðu; vÞ of the dual program ofP is
nonpositive, and it is equal to 0 if and only if there exists a valueu such thatut ¼/C0ve ¼u for allt 2FðSÞ and all
e 2EðSÞ.
Proof. Letu ¼ minðu1; ... ;ulÞ.Let uð1Þ
i ¼ui /C0uandvð1Þ
j ¼vj þu.Itisobviousthatthevector ðuð1Þ; vð1ÞÞsatisﬁesthe
constraintsofthedualprogram.Furthermore
Fðuð1Þ; vð1ÞÞ/C0Fðu; vÞ¼/C0ul /C25/C0
X
e2EðSÞ
wðeÞ
 !
¼ 0
from Lemma 2.1, so thatFðu; vÞ¼ Fðuð1Þ; vð1ÞÞ. Consider the case whereuð1Þ
i ¼ 0 for alli. Since allvð1Þ
j must be
nonpositiveandalloftheircoeﬃcientsarepositive,theobjectivefunction Fðu; vÞisnonpositiveandisequalto0only
if allvð1Þ
j are equal to 0. Then we assume thatuð1Þ
t > 0 for somet 2FðSÞ. LetFð1Þ be the subset ofFðSÞ such that
SingularEuclideanStructuresonaSimplicialComplex 83
uð1Þ
t > 0 for eacht 2Fð1Þ and uð1Þ ¼ mint2Fð1Þ ðuð1Þ
t Þ. Letlð1Þ ¼jFð1Þj. Letuð2Þ
t ¼uð1Þ
t ¼ 0 if t =2Fð1Þ and otherwise
uð2Þ
t ¼uð1Þ
t /C0uð1Þ.Alsolet vð2Þ
e ¼vð1Þ
e ifeisnotcontainedinsomeelementof Fð1Þ andotherwise vð2Þ
e ¼vð1Þ
e þuð1Þ.The
vector ðuð2Þ; vð2ÞÞstillsatisﬁes theconstraintsofthedualprogram.Furthermore
Fðuð2Þ; vð2ÞÞ/C0Fðuð1Þ; vð1ÞÞ¼/C0ul ð1Þ/C25/C0
X
e incident to Fð1Þ
wðeÞ
 !
> 0
fromLemma2.1,sothat Fðuð2Þ; vð2ÞÞ > Fðuð1Þ; vð1ÞÞ.Wetakethenewnonzeroset Fð2Þ asapropersubsetof Fð1Þ,andwe
repeatthisprocess.Attheend,wewillwindupwiththefeasiblepoint ðuðkÞ; vðkÞÞwithuðkÞ ¼ 0wherethevalueofthe
objectivefunctionisnonpositiveandstrictlygreaterthanthevalueoftheobjectivefunctionat ðu; vÞ.Thentheassertion
follows. /C3
Next we strengthen the ﬁrst constraint as each angle is strictly positive. To consider that, we put each angle/C11as
/C11¼ /C110 þ /C15and require that all /C110 are nonnegative. Set the newobjective function as ð0; ... ; 0; /C01Þ/C1ð/C1110;/C1210;
/C1310; ... ;/C11l0;/C12l0;/C13l0;/C15ÞT anddenotethislinearprogramby P0.Wecan express P0 usingamatrix asthefollowing.
Minimize ð0; ... ; 0; /C01Þ/C1ð/C1110;/C1210;/C1310; ... ;/C11l0;/C12l0;/C13l0;/C15ÞT subjectto
111000. . .000 3
000111. . .000 3
... .
.. .
.. .
.. .
.. .
.. . .. .
.. .
.. .
..
000000. . .111 3
010000. . .001v a l ðe
1Þ
... .
.. .
.. .
.. .
.. .
.. . .. .
.. .
.. .
..
100010. . .100v a l ðe
mÞ
0
BBB
BBB
B
BBB
BB@
1
CCC
CCC
C
CCC
CCA
/C11
1
0
/C121
0
/C131
0
...
/C11l
0
/C12l
0
/C13l
0
/C15
0
BBBB
BBB
B
BBB
BBB
@
1
CCCC
CCC
C
CCC
CCC
A
¼
/C25
/C25
..
.
/C25
wðe
1Þ
...
wðemÞ
0
BBBB
BBB
BBB
BBB
@
1
CCCC
CCC
CCC
CCC
A
and
/C11
1
0;/C121
0;/C131
0; ... ;/C11l
0;/C12l
0;/C13l
0;/C15
/C0/C1
/C210:
Thenthedualprogramof P0 turnsouttobethefollowing.
Maximize Fðu; vÞ¼ /C25P
t2FðSÞut þ P
e2EðSÞwðeÞve,subjectto
1. ut þve /C200whenevereisanedge of t,
2. 3 P
t2FðSÞut þ P
e2EðSÞ valðeÞve /C20/C01.
Lemma 2.4. The optimal value of the objective function of the dual program ofP0 is strictly negative.
Proof. Suppose the contrary. Then by Lemma 2.3,ut ¼/C0ve ¼ufor someu. In this case, the left hand side of the
secondconstraintis
3
X
t2FðSÞ
ut þ
X
e2EðSÞ
valðeÞve ¼u 3
X
t2FðSÞ
1 /C0
X
e2EðSÞ
valðeÞ
 !
:
Heretherighthandsideisequalto0thentheinequalityisnotsatisﬁed.Itcontradicts theﬁrstassumption. /C3
From Theorem 2.2 and Lemma 2.4, the objective function ofP0, that is ð0; ... ; 0; /C01Þ/C1ð/C1110;/C1210;/C1310; ... ;/C11l0;
/C12l0;/C13l0;/C15ÞT ¼/C0/C15, is strictly negative, so that there are the solutions that each angle is strictly positive. Thus the
condition ofLemma 2.1turnsouttobeasuﬃcientcondition.
Lemma 2.5. LetF0 /C18FðSÞ, and letE0 be the set of all edges contained inF0. Assume thatw satisﬁes the following
condition: X
e2E0
wðeÞ/C21/C25jF0j
with equality if and only ifF0 ¼FðSÞ orF0 ¼ /C30. ThenS admits locally Euclidean structures coming fromw.
We denote the set of all locally Euclidean structures onScoming fromwby AðS;wÞ. It is a subset ofR3l whose
coordinatesaretheanglesofthe2-facesof S.
84 KAMEI
