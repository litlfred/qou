---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a ﬁnite set of points(: GalMot ⟳cMot 1 (-−(,E 0)"
section_id: sec-015-specialization-theorem-for-hodge-correlators
section_title: "Specialization theorem for Hodge correlators"
section_number: null
pages: 71-76
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a finite set of points(: GalMot ⟳cMot 1 (-−(,E 0). (1) — On the"
---
We now study how the Hodge correlators over a base behave when the sections collide. This will require
extending the theory of Hodge correlators to nodal curves.
The correlator Lie coalgebra for nodal curves
Recall the moduli spaceM′
0,= of = distinct points and a distinguished tangent vector onP1. Its Deligne-
Mumford compactiﬁcationM
′
0,= consists of the nodal curves of genus 0, i.e., those whose dual graph is a
tree and in which every component is a punctured projective line. with= marked points and a distinguished
tangent vectorE∞.
Let- = —
8-8 beagenus0nodalcurvewithasetofpunctures (. Let) bethedualtreeof -,withvertices
indexed by8 corresponding to-8, rooted at the component0with the base pointB0∈ -0, oriented away from
the root (write8→ 9 if(8,9) is an edge). Choose a coordinateI8 on each-8 such that the point joining the
63
component to its parent-9 is(I8 =∞,I 9 = E98), and the base point on-0 is atI0 =∞ with tangent vector
E∞. Let(8 be the set of punctures on-8. Let#8 =
{
E89 :8→ 9
}
.
We deﬁne the correlator Lie coalgebra for the nodal curve- by
CL∨
-,(,E∞ =
˚
8
CL∨
-8,(8∪#8,E8, (2.108)
whereE8 is the tangent vector−1
I2
8
m
mI8
atI8 =∞.
It coincides with the usual deﬁnition if- is smooth, justifying the notation. If- is not smooth, it is
diﬀerent from~CL
∨
-,(,B 0, the coalgebra naively deﬁned as the tensor algebra of( modulo cyclic symmetry
and shuﬄe relations with a
2(-) coeﬃcient. They are related in the following way. For each8, there is a
surjective coalgebra morphism to the component of the direct sum corresponding to-8:
~CL
∨
-,(,B 0
c8
−−→CL∨
-8,(8∪#8,E8.
To deﬁne it on a generator(G1⊗···⊗ G=)⊗[ -8], let? be the common parent of the components containing
theG9. If?≠8, the8-th component of the map is 0. Otherwise, set
c8(G)=
 

G, G ∈ -8
I8 =E89 ∈ #8, G ∈ -:, where∃ path8→ 9→···→ :
,
extended to preserve the tensor product. That is, points in-8 remain, while points in components below-8
collapsetothenearestnodeon -8. Evidentlythismappreservesthecoproductanddeﬁningrelations. Taking
the direct sum of the mapsc8, we have produced a coalgebra morphism:
c : ~CL
∨
-,(,E∞→CL ∨
-,(,E∞.
It preserves the decomposition of the domain by
2(-)= É
8
2(-8).
In particular, if(-,(,E 0) vary over a base→M ′
0,=, and the variation extends to→M
′
0,=, with
=\, then we have adegeneration map
c :CL∨
-/,(,E∞→ ~CL
∨
-/,(,E∞→CL ∨
-/,(,E∞, (2.109)
where the ﬁrst map simply applies the induced map on
2 and the second map is the quotient deﬁned above.
The composition forgets the way in which the sections in( collided at boundary of.
64
Specialization theorem
Recall that an element ofCL∨
-/,(,E∞
over a base→M ′
0,= determines, by the map CorHod, a variation of
Hodge structures over, and, by the period map?, a smooth function on. The maps CorHod and ? also
exist for- a nodal curve, extended by linearity from the deﬁnition (2.108).
Theorem2.23. Suppose→M′
0,= isafamilyofcurves (-,(,E ∞) extendingto →M
′
0,=,with =\
a normal crossings divisor, and supposeG∈CL ∨
-/,(,B 0
of weight=> 1.
(a) The Deligne’s canonical extension to of the variation of framed mixed Hodge structures determined
by CorHod(G) is independent of the normal vector to. Thus there is a specialized mapSpecCorHod :
(
CL-/,(,E∞→ Lie∨
HT/
)
F> 1
.
(b) This specialized map coincides with the Hodge correlator of the degeneration map:
(
CL∨
-/,(,E∞
)
F> 1
c //
CorHod

(
CL∨
-/,(,E∞
)
F> 1
CorHod

(Lie∨
HT/)
Spec //(Lie∨
HT/).
.
(c) LetC= 0 be a local equation for. Then
lim
C→0
?(CorHod(GC)) = ?(>AHod(GC=0)).
Proof. LetG∈CL ∨
-/,(,E∞
be a generator of weightF > 1. For anyE a normal vector to, we get the
specialized framed mixed Hodge-Tate structureSpecE
CorHod(G).
We must show that:
(1) The periods of CorHod(G) extend continuously to.
(2) The coproduct ofSpecE
CorHod(G) does not depend on the direction of specializationE at any smooth
point of.
(3) The periods of the specializations (i.e., the limits of the periods at) coincide with the periods of the
degeneration to.
We will prove (1)-(3) by induction on the weight. First, let us see how they imply the result.
Assuming (2), the coproduct ofSpecE
CorHod(G) is independent ofE. Because the coproduct commutes
with SpecE
, this element is independent ofE up toExt1(R(0), R(=)), which is 1-dimensional and controlled
65
by the period. By (1), the period is independent of the direction of specialization, which gives (a). By (3), it
coincides with the period of the degeneration, which gives (b). Then (c) follows by the deﬁnitions from (b).
To show (1), we let{Y8 = 0} be a set of smooth local equations for and prove that?(CorHod(G)) can
be represented locally as a polynomial in thelogY8 such that the terms withlogY8 appearing in positive
degree have coeﬃcients vanishing along{Y8 = 0} (tame logarithmic singularities). This will follow from the
diﬀerentialequationsontheperiods. Notethatinweight1,theperiodof (G,H) hasa(nottame)logarithmic
singularity alongG=H. In weight> 1, we proceed by induction.
Considerasimpleelement G=G0⊗···⊗ G=∈CL ∨
-/,(,E∞
(=> 1). Supposethatnotall G8 collideon ,
so we must only consider the summand of the nodalCL∨
-/,(,B 0
corresponding to the component containing
the base point. The terms ofX(G) can be grouped into those of two forms:
(i) G′∧G′′, where not all sections inG′ and inG′′ collide to the same section on;
(ii) G′∧(G′′
1−G′′
2), where not all sections inG′ collapse on, butG′′
1 andG′′
2 coincide on.
Bytheinductivehypothesis, thespecializationof X(G) doesnotdependonthedirectionofspecialization:
forterms(i), G′ andG′′ satisfy(2),whileinterms(ii)the G′′
1−G′′
2 vanishunderspecializationto . Thisgives
(2).
For (1), from the diﬀerential equations on the periods (1.14), we see that3?(CorHod(G)) is a sum of
termsthataresmoothover withlogarithmicsingularitiesalong  (fromtype(i))andtermsthatvanishalong
 by the inductive hypothesis (from type (ii)). We conclude that?E∞(G) has tame logarithmic singularities
along.
If allG8 collide on, we simply pass to their common parent component and apply the same argument.
We conclude with (3). We have shown that the specializations of CorE0
Hod and its coproduct to exist at
everypointandtheirperiodsareindependentof E, andthusthespecializedperiodmap ?◦CorHod isequalto
the period of the degeneration up to adding a constant for each smooth component of the smooth locus of.
We must show the constant 0.
Itisenoughtoshowthisfor  alowest-codimensionboundarystratumin M
′
6,=. Wearedonebythenext
lemma. □
Lemma 2.24. Let
 be a proper subset of{0, 1,...,= } (=> 1) andG0,...,G =∈ C∗ withG8 ≠G9 if8≠ 9 and
either8,9 ∈ 
 or8,9 ∉
. Let
G8(C)=
 

CG8 8∈ 
,
G8 8∉

.
66
Then
CorH(G0(C),G 1(C),...,G =(C))
is continuous atC= 0.
Proof. For== 2, this amounts to continuity ofL2 at 1.
In the proof of Theorem 2.23 it was established that
lim
C→0
CorH(G0(C),G 1(C),...,G =(C))− CorH(G0(0),G 1(0),...,G =(0))
is independent of theG8, for genericG8. Let us integrate this diﬀerence over(G0,...,G =)∈( (1)=+1, with
respect to the standard measures‘(G8) of volume 1 on(1={|I|= 1}⊂ C.
The limit is uniform in the directionsG8 (8∈ 
), and so
„
lim
C→0
CorH(G0(C),G 1(C),...,G =(C))
Ö
3‘(G8)= lim
C→0
„
CorH(G0(C),G 1(C),...,G =(C))
Ö
3‘(G8).
To conclude, it suﬃces to show that
„
CorH(G0(C),G 1(C),...,G =(C))
Ö
3‘(G8)= 0. (2.110)
for allC.
Foranytree ) enteringintotheFeynmanintegralexpressionfor(2.110),chooseapairofboundaryvertices
(without loss of generality, labeledG0 and G1) incident to a common internal vertexE with corresponding
variableGE, and letGF be variable corresponding to the third vertex incident toE. Then the integral over the
G8 contains the term
„
G0,G 1
(„
L2
(GF−G0(C)
GF−G1(C)
)
∧( terms independent ofG0(C),G 1(C))
)
3‘(G0)3‘(G1).
Exchanging the two integrals and noting thatL2(I−0
I−1) changes sign under the involution
07→0 I2
|I|2, 1 7→1 I2
|I|2,
we conclude that this expression is 0. □
The specialization theorem states that when the punctures labeling an element ofCL∨ collide, only the
component nearest to the base point of the resulting nodal curve determines the limit Hodge correlator. We
67
obtain as a corollary Theorem 1.6:
Theorem. The Hodge correlatorsCorH(I0,...,I =) are continuous onC=+1\{I0=··· =I=}.
For example,L2 is continuous with a tame logarithmic singularity at 1, butL2
(0−2
1−2
) has no limit as
0,1,2 → 0.
2.4 The second shuﬄe relations
