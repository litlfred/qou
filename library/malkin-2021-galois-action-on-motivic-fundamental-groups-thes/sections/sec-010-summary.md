---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-010-summary
section_title: "Summary"
section_number: null
pages: 34-41
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
TheHodgecorrelatorsCor H(I0,I 1,...,I =) arefunctionsofseveralcomplexvariables,deﬁnedbyanexplicit
integralformulain[G9]. Theysatisfysomelinearrelations: thedihedralsymmetryrelations,thedistribution
relations, and the shuﬄe relations.
We found new relations, calledsecond shuﬄe relations. When I8∈{0}∪‘#, where‘# are the#-th
roots of unity, they should give almost all relations: the results of [G10] suggest that the other relations are
sporadic, i.e., cannot be described by universal formulae.
When theI8 run through a ﬁnite subset( of C, the Hodge correlators are the canonical real periods of
the mixed Hodge-Tate structures on the pronilpotent completion of the fundamental groupcnil
1 (CP1\( (∪
{∞}),E∞), withthetangential basepointat ∞. Thelatteris aLiealgebrain thecategoryofmixed Q-Hodge-
Tate structures. The Hodge correlators describe theR-mixed Hodge structure on this Lie algebra tensored
over Q by R.
Thecategoryofmixed Q-Hodge-Tatestructuresiscanonicallyequivalenttothecategoryofrepresentations
ofagradedLiealgebraover Q. Letustakeitsimageintherepresentationdeﬁning cnil
1 (CP1\((∪{∞}),E∞),
andconsiderthegradeddualLiecoalgebraLie ∨
HT((). TheHodgecorrelatorswereliftedin[G9]tocanonical
26
elements
CorHod(I0,...,I =)∈ Lie∨
HT((). (2.1)
TherealnumbersCor H arethecanonicalrealperiodsoftheseelements. Weprovethatournewrelationscan
be lifted to relations on the elements (2.1).
Let ( ⊂ Q⊂ C. The Lie algebra cnil
1 (CP1\( (∪{∞}),E∞) is the Betti realization of the motivic
fundamentalgroup cMot
1 (P1\((∪{∞}),E∞). ThelatterisaLiealgebrainthecategoryofmixedTatemotives
over Q,deﬁnedin[DG]. ThiscategoryisidentiﬁedwiththecategoryofrepresentationsofthemotivicGalois
Liealgebra. JustlikeintheHodgecase,wetaketheimageofthisLiealgebraintherepresentationprovidedby
the motivic fundamental group, and consider the graded dual Lie coalgebra Lie∨
MT((). In [G9], the elements
(2.1) were lifted to elements
CorMot(I0,...,I =)∈ Lie∨
MT((). (2.2)
We prove that our relations can be upgraded to linear relations on these elements.
The universal enveloping algebra for the Lie coalgebra Lie∨
MT(() was described in [G5] via motivic
multiple polylogarithms. The motivic double shuﬄe relations for them were proved in [G6]. The explicit
relation between motivic correlators and multiple polylogarithms is an interesting open problem.
The multiple polylogarithms obey a similar system of double shuﬄe relations, but the dihedral symmetry
relationholdsonlyatrootsofunity. Thecombinatoricsofthoserelations, originallydescribedby[G3]-[G5],
were studied further by [R1].
Themotiviccorrelatordescriptionof cMot
1 (P1\((∪{∞}),E∞) hasseveraladvantages. Mostimportantly,
motivic correlators are deﬁned for any algebraic curve, not onlyA1\(, and the double shuﬄe relations
admit a generalization to elliptic curves, at least in the depth 2 (see Chapter 3). The motivic correlators
obey double shuﬄe and cyclic symmetry relations at all points. Motivic correlators describe elements of the
Lie coalgebra rather than its universal enveloping algebra. Finally, they give the best way to describe the
mysterious connection between the Lie coalgebra Lie∨
MT({0}∪‘#) and modular manifolds ([G10]).
Structure
In the remainder of the introduction, we will state the main results: Theorems 2.1, 2.6, and 2.7. Their proof
has three parts.
The ﬁrst and longest part (§2.2) is a combinatorial calculation, the construction of the quasidihedral
coalgebra.
The second part (§2.3) is a specialization theorem that allows us to make continuity arguments about the
27
Hodge correlators.
The third part (§2.4) is a series of formal arguments to deduce the three realizations of the main result.
2.1.2 Hodge correlator integrals and shuﬄe relations
The main result of this chapter is a set of functional equations on the Hodge correlator integrals and the
Hodge-theoreticandmotivicupgradesoftheserelations. LetusﬁrststatetheresultsfortheHodgecorrelator
integrals.
Second shuﬄe relation
Recall the ﬁrst shuﬄe relation for the Hodge correlator integrals (1.5):
Õ
f∈Σ8,9
CorH(G0,Gf−1(1),Gf−1(2),...,G f−1(8+9))= 0.
The shuﬄe relations may be considered “easy” because they hold on the level of the sum over trees of the
integrandsin (1.3).
We found another relation on the Hodge correlators. Together, the two relations form thedouble shuﬄe
relations. To state the new relations, we must introduce some notation.
Becauseofthemultiplicativeinvariance(inweight > 1)ofHodgecorrelators,itispossibleandconvenient
to introduce an inhomogeneous notation for them, where the arguments are represented by the quotients
betweensuccessivenonzerovaluesandthenumberof0sbetweenthem. Thatis,given F0,...,F :∈ C∗ such
thatF0F1...F : = 1, deﬁne
Cor∗
H(F0|=0,F 1|=1,...,F :|=:) :=
= CorH(0,..., 0|   {z   }
=0
, 1, 0,..., 0|   {z   }
=1
,F 1, 0,..., 0|   {z   }
=2
,F 1F2,..., 0,..., 0|   {z   }
=:
,F 1...F :). (2.3)
This deﬁnition is illustrated in Figure 2.1.
ThedepthofanexpressionCor H(I0,...,I =)isonelessthanthenumberofargumentsinthemultiplicative
notation, that is,: in the formula above.
Our new shuﬄe relation states:
Õ
f∈ΣA,B
Cor∗
H(Ff−1(1)|=f−1(1),...,F f−1(A+B)|=f−1(A+B),F 0|=0)+ lower-depth terms= 0. (2.4)
28
/u1D4670
/u1D4671 /u1D4672
0
00
0
00
/u1D45B0/u1D45B1
/u1D45B2
· · · /braˆ~[t]pupl~ft/bracehext/bracehext/bracehext/braˆ~[t]pd}w{r]~[t/braˆ~[t]pd}w{l~ft
/bracehext/bracehext/bracehext/braˆ~[t]pupr]~[t· · ·
/braˆ~[t]pupl~ft/bracehext/bracehext/bracehext/braˆ~[t]pd}w{r]~[t/braˆ~[t]pd}w{l~ft
/bracehext/bracehext/bracehext/braˆ~[t]pupr]~[t
· · ·
/braˆ~[t]pupl~ft/bracehext/bracehext/bracehext/braˆ~[t]pd}w{r]~[t/braˆ~[t]pd}w{l~ft/bracehext/bracehext/bracehext/braˆ~[t]pupr]~[t
/u1D45B1
/u1D45B2
/u1D45B0/u1D4641
/u1D4642
/u1D4640
F8 = I8
I8−1
Figure 2.1. Deﬁnition of Cor∗
H: CorH(I0, 0,..., 0|   {z   }
=1
,I 1, 0,..., 0|   {z   }
=2
,I 2, 0,..., 0|   {z   }
=0
)≡ Cor∗
H(F1|=1,F 2|=2,F 0|=0).
That is, we shuﬄe two ordered sets of expressions(F8| =8), while leaving the segment(F0| =0) ﬁxed. For
example the(1, 1)-shuﬄe relation begins:
/u1D45B1
/u1D45B2
/u1D45B0/u1D4641
/u1D4642
/u1D4640
/u1D45B2
/u1D45B1
/u1D45B0/u1D4642
/u1D4641
/u1D4640
Cor∗
H(F1|=1,F 2|=2,F 0|=0) + Cor∗
H(F2|=2,F 1|=1,F 0|=0)
We explicitly describe the lower-depth terms in (2.4). They come in two kinds:
(1) Terms coming from the(A,B)-quasishuﬄes that are not proper shuﬄes (see §1.2.3). Whenever the
segments(F8|=9) and(F9|=9) collide, we get a new segment(F8F9|=8+=9+ 1) in their place – a 0
is inserted – and the term picks up a negative sign.
For the(1, 1)-shuﬄe relation, there is only one quasishuﬄe that is not a shuﬄe. In this quasishuﬄe, the
two segments(F1|=1) and(F2|=2) collide:
/u1D45B1 + /u1D45B2 + 1
/u1D45B0
/u1D4641/u1D4642
/u1D4640
−Cor∗
H(F1F2|=1+=2+ 1,F 0|=0)
29
(2) Two additional terms: one where the segmentsF1,...,F A appear in order and the remaining seg-
ments FA+1,...,F A+B,F 0 collapse; another where the segmentsFA+1,...,F A+B appear in order and
F1,...,F A,F 0 collapse. These terms come with a negative sign.
For the(1, 1)-shuﬄe relation:
/u1D45B2 + /u1D45B0 + 1
/u1D45B1
/u1D4642/u1D4640
/u1D4641
/u1D45B1 + /u1D45B0 + 1
/u1D45B2
/u1D4641/u1D4640
/u1D4642
−Cor∗
H(F1|=1,F 2F0|=2+=0+ 1) − Cor∗
H(F2|=2,F 1F0|=1+=0+ 1)
In summary, the(1, 1)-shuﬄe relation states, forF0,F 1,F 2∈ C∗ andF0F1F2= 1,
Cor∗
H(F1|=1,F 2|=2,F 0|=0)+ Cor∗
H(F2|=2,F 1|=1,F 0|=0)
−Cor∗
H(F1F2|=1+=2+ 1,F 0|=0)
−Cor∗
H(F1|=1,F 2F0|=2+=0+ 1)
−Cor∗
H(F2|=2,F 1F0|=1+=0+ 1) = 0.
Itisalreadyanontrivialrelationwhichisnoteasytoprovefromthedeﬁnition(1.3)evenfor =0==1==2= 0.
By formula (1.10), Hodge correlators in weight 2 are expressed in a simple way in terms of the Bloch-
Wigner functionL2. The (1, 1)-shuﬄe relation with=0 = =1 = =2 = 0 is equivalent to the ﬁve-term
relation,
L2
( 1−F1
1−F1F2
)
+L 2
( 1−F2
1−F1F2
)
+L 2(1−F1F2)+L 2(F1)+L 2(F2)= 0.
Accordingto[B5],thisisessentiallytheonlyfunctionalequationfor L2. Itfollowsthatthedihedralsymmetry
and shuﬄe relations are theonlyrelations between the Hodge correlators in weight 2.
For further illustration, let us write out the(2, 1)-shuﬄe relation for the Hodge correlator
Cor∗
H(F1|0,F 2|1|F3|1,F 4|0),
whereF1 andF2 will be shuﬄed withF3:
(0) There are three terms from the shuﬄes:
30
F1F2F3 F1F3F2 F3F1F2
1
/u1D4641
0 /u1D4641/u1D4642
0
/u1D4641/u1D4642/u1D4643
1
/u1D4641
0 /u1D4641/u1D4643
0
/u1D4641/u1D4642/u1D4643
1
0
/u1D4643 /u1D4641/u1D4643
0
/u1D4641/u1D4642/u1D4643
(1) There are two terms from the quasishuﬄes that are not shuﬄes:

F1
F3

F2 F1

F2
F3

1
0
0 /u1D4641/u1D4643
0
/u1D4641/u1D4642/u1D4643
1
/u1D4641
0 0
0
/u1D4641/u1D4642/u1D4643
(2) There are two additional terms:
1
/u1D4641
0 /u1D4641/u1D4642
0
0
1
0
/u1D4643 0
0
0
The full relation is then
Cor∗
H(F1|0,F 2|1,F 3|1,F 4|0)+ Cor∗
H(F1|0,F 3|1,F 2|1,F 4|0)+ Cor∗
H(F3|1,F 1|0,F 2|1,F 4|0)
−Cor∗
H(F1F3|2,F 2|1,F 4|0)− Cor∗
H(F1|0,F 2F3|3,F 4|0)
−Cor∗
H(F1|0,F 2|1,(F1F2)−1|2)− Cor∗
H(F3|1,F−1
3 |3) = 0,
where the3+ 2+ 2 terms in the three rows match the3+ 2+ 2 pictures above.
We now write out the general relation:
Theorem 2.1.(a) Supposethat A,B > 1andthatnotall =8 = 0ornotall F8 = 1. ThentheHodgecorrelators
satisfy the relation:
Õ
f∈ΣA,B
(−1)A+B−"fCor∗
H(Ff−1(1)|=f−1(1),...,F f−1("f)|=f−1("f),F 0|=0)
−Cor∗
H(F1|=1,...,F A|=A,F{A+1,...,A+B,0}|={A+1,...,A+B,0})
−Cor∗
H(FA+1|=A+1,...,F A+B|=A+B,F{1,...,A, 0}|={1,...,A, 0}) = 0,
31
where
=
 =
Õ
8∈

(=8+ 1)− 1, F 
 =
Ö
8∈

F8.
(b) The Hodge correlators satisfy all specializations of this relation as any subset of theF8(1≤ 8≤ =)
approaches 0.
Applications
Theorem 2.1 gives simple proofs of certain results of [GR].
Corollary2.2 ([GR],Proposition2.8) . For=> 2,everyHodgecorrelatorofweight =isalinearcombination
of Hodge correlators of weight= and depth at most=− 2. Explicitly, forI1,...,I =∈ C∗, we have
CorH(I1,...,I =, 0)=
=Õ
8=1
CorH
(
I1,...,I 8−1,I8,I8
I1
I=
,...,I =−1
I1
I=
,I=
I1
I=
)
−
=Õ
8=2
CorH
(
I1,...,I 8−1, 0,I8
I1
I=
,...,I =−1
I1
I=
,I=
I1
I=
)
−CorH
(
I1,I 1
I1
I=
, 0,..., 0
)
. (2.5)
In weight 3, we deduce the Hodge correlator version of relations (27) and (29) from [GR].
Corollary 2.3.The Hodge correlators in weight 3 satisfy the relations:
CorH(1, 0, 0,G)+ CorH(1, 0, 0, 1−G)+ CorH(1, 0, 0, 1−G−1)= CorH(1, 0, 0, 1), (2.6)
CorH(0,G, 1,H)=−CorH(1, 0, 0, 1−G−1)− CorH(1, 0, 0, 1−H−1)− CorH
(
1, 0, 0, H
G
)
−CorH
(
1, 0, 0, 1−H
1−G
)
+CorH
(
1, 0, 0, 1−H−1
1−G−1
)
+CorH(1, 0, 0, 1). (2.7)
We have noted that the double shuﬄe and dihedral symmetry relations give all relations between Hodge
correlators in weight 2. In weight 3, the Hodge correlators of depth 1 are expressed in terms of the single-
valued trilogarithmL3 (see the end of §1.2.3). By the results of [GR], the relations (2.7) imply the general
functional equation forL3 ([G1]). We conclude that the double shuﬄe relations for Hodge correlators imply
all functional equations forL2 andL3.
32
/u1D4650/u1D4651
/u1D465/u1D45B
/u1D465/u1D456/u1D465/u1D456+1
/u1D6FF
/uni21A6.endl→
/u1D4650
/u1D465/u1D45B
/u1D465/u1D456+1
∧
/u1D4650/u1D4651
/u1D465/u1D456
Figure 2.2. The typical term of the coproduct in the cyclic Lie coalgebra.
