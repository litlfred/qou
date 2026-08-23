---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-014-proof-of-theorem-25
section_title: "Proof of Theorem 2.5"
section_number: null
pages: 52-71
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
Summary of the proof
The proof of the Theorem 2.5 will be by induction on the depth of the second shuﬄes.
Deﬁne
QShA,B(F1|(1,...,F =|(=,F 0|(0)=
=
Õ
f∈ΣA,B
(−1)A+B−"f ∗(Ff−1(1),...,F f−1("f),F 0| (f−1(1),...,( f−1("f),( 0
),
whereF8∈
 with ˛
8F8 = 1, and
QSh
A,B
(F1|(1,...,F =|(=,F 0|(0)= QShA,B(F1|(1,...,F =|(=,F 0|(0) (2.28)
− ∗(F1,...,F A,F{A+1,...,A+B,0}| (1,...,( A,({A+1,...,A+B,0}
) (2.29)
− ∗(FA+1,...,F A+B,F{1,...,A, 0}| (A+1,...,( A+B,({1,...,A, 0}
). (2.30)
We must show that the elementsQSh form a coideal, i.e., their coproducts vanish modulo other elements of
this form.
44
To make the notation more transparent, whenA andB are ﬁxed, we will relabel
)1,...,) A =(1,...,( A,
*1,...,* B =(A+1,...,( A+B,
+ =(0,
01,...,0 A =F1,...,F A
11,...,1 B =F1,...,F A+B,
2=F0,
so that we consider elements
QSh
A,B
(01|)1,...,0 A|)A,1 1|*1,...,1 B|*B,2|+).
The main steps will be the following:
Step 0.Fixthe 08 and19. Showthatitsuﬃcestoassume |)8|=|*8|=|+|= 1. Denotethethreeterms(2.28),
(2.29), (2.30) by&,’, and’, respectively.
Step 1.Show thatX(&−’−’) is zero modulo shuﬄe relations of lower depth and elements of the form
(0,G) (Lemma 2.14).
(a) Group the terms ofX& according to a combinatorial classiﬁcation and reduce them using shuﬄe
relations of lower depth (Lemma 2.16).
(b) Groupthetermsof X(’) andX(’) inthesamewayandshowthattheycoincidewiththeterms
found in (a) (Lemma 2.22).
Step 2.Show that the (weight 1)∧(weight≥ 1) component ofX(&−’−’) is 0, modulo shuﬄe relations
of lower depth (Lemma 2.15).
Throughout the proof, in a term∗(F1,...,F :,F 0| B1,...,B :,B 0
) appearing in the deﬁnition ofQSh,
call the segment(F0| B0
) the distinguished segment(i.e., (2| E) in (2.28) and the collapsed segments in
(2.29) and (2.30)). In the following lemmas, we will always use the following classiﬁcation of terms of the
coproduct of a generating function (see Figure 2.6).
(1) Terms6∧ℎ where one of the parts6 or ℎ contains the distinguished segment (i.e., the distinguished
segment is not cut). In this case, we always write the term in the form±6∧ℎ, where6 contains the
distinguished segment.
45
/u1D4650 /u1D465/u1D458
/u1D465/u1D456
/u1D465/u1D457−1
/u1D465/u1D457
/u1D454
Ă
−/u1D454 ∧ Ă
/u1D4650 /u1D465/u1D458
/u1D465/u1D456
/u1D465/u1D456+1
/u1D465/u1D457
/u1D454
Ă
/u1D454 ∧ Ă
/u1D4650 /u1D465/u1D458
/u1D465/u1D456
/u1D465/u1D456+1 /u1D465/u1D457−1
/u1D465/u1D457
/u1D454
Ă
−/u1D454 ∧ Ă
/u1D4650 /u1D465/u1D458
/u1D465/u1D456
/u1D465/u1D456+1 /u1D465/u1D457−1
/u1D465/u1D457
/u1D454
Ă
/u1D454 ∧ Ă
(1a) (1b) (1c) (1d)
/u1D4650 /u1D465/u1D458
/u1D465/u1D456
/u1D454 Ă
−/u1D454 ∧ Ă
/u1D4650 /u1D465/u1D458
/u1D465/u1D456/u1D465/u1D456−1
/u1D454 Ă
−/u1D454 ∧ Ă
/u1D4650 /u1D465/u1D458
/u1D465/u1D456/u1D465/u1D456−1
/u1D454 Ă
/u1D454 ∧ Ă
(2a) (2b) (2c)
Figure 2.6. Classiﬁcation of terms in the coproduct used in the proof of Theorem 2.5.
(a) Cut from a pointG8 to the segment(F9| B9
) (0≤8 < 9≤ :).
(b) Cut from a pointG9 to the segment(F8+1| B8+1
) (0≤8 < 9≤ :).
(c) Cut from a 0 on the segment(G8+1|CB+1
) to the segment(F9|C9
) (0≤8 < 9≤ :).
(d) Cut from a 0 on the segment(G9| B9
) to the segment(F8+1|C8+1
) (0≤8 < 9≤ :).
(2) Terms6∧ℎwherethedistinguishedsegmentiscut. Inthiscase,wealwayswrite ±6∧ℎ,where 6contains
the pointG0 andℎ the pointG:.
(a) Cut from a pointG8 to the distinguished segment.
(b) Cut from a 0 on the segment(F8| B8
) to the distinguished segment (0<8 < :).
(c) Cut from a 0 on the distinguished segment to the segment(B8|C8
) (0<8 < :).
Step 0
As stated in Step 0 above, we ﬁx< >0 and= >0, the08,19,2, and the)8,*9,+, and let&,’,’ be the
three terms of the expression deﬁningQSh: (2.28), (2.29), and (2.30), respectively.
We may assume)8 ={C8},*9 =
{
D9
}
, and+ ={E}, by the following:
Lemma 2.13(Step 0). The shuﬄe relations for|)8| =

*9

=|+| = 1 imply the shuﬄe relations for general
index sets.
Proof. Obvious by induction using (2.13). □
46
Lemma 2.14(Step 1). Modulo shuﬄe relations of lower depth and elements(0,G),X(&−’−’)= 0.
Lemma 2.15(Step 2). Modulo lower-depth shuﬄe relations and terms(0,G)∧ (0,H),
X(&−’−’)=

<Õ
8=1
(0,08)(C8−E)+
=Õ
9=1
(0,1 9)(D9−E)

∧(&−’−’). (2.31)
Proof of Step 1
Lemma-Computation2.16 (Step1(a)). Moduloshuﬄerelationsoflowerdepthandelements (0,G),X& is
given by the sum of expressions (2.74)-(2.78) below.
Group all terms ofX& by the type of cut as deﬁned in the outline above. Some computational lemmas
will simplify the contributions toX& coming from the cuts of each type. The contribution of cuts (1a/b/c/d)
is computed in Lemma 2.17, and cuts (2a/b/c) are dealt with in Lemma 2.21.
Lemma-Computation 2.17. The contribution of cuts of type (1a/b/c/d) toX&, modulo shuﬄe relations of
lower depth and elements(0,G), is given by (2.57) below.
The cuts of types (1a) and (1b) contribute terms of the form (2.19), while cuts of types (1c) and (1d)
contribute terms of the form (2.20) below.
Consider the upper parts6 of terms±6∧ℎ as shown in Figure 2.6; by cyclic invariance modulo(0,G)
we may write
6= ∗(F1,...,F ;,2 | (1,...,( ;,+ ).
Let (F?| (?
) be the new segment arising from the cut (that is, the bracketed segment in (2.19) or (2.20)).
We say that08 appears in6 if either the segment(08|C8
) or some(0819|
{
C8,D 9
} ) is present in6 as one
of the(F;| (;
) (;≠8), and similarly for19. Then the set of segments thatdo notappear in6 (“appear below
g”) is determined by theF1,..., ˆF?,...,F ; and consists of consecutively indexed elements08 and19, i.e.,
080,...,0 81 and190,...,1 91, where by convention80=81+ 1 if no08 appear, and likewise for90,9 1.
Group the terms6∧ℎ by the sequence of segmentsF1,..., ˆF?,...,F ;. To shorten notation, write
~6(()= ∗(F1,...,F ?,...,F ;,2 | (1,...,( ? =(,...,( ;,+ ).
There are three cases:
(1) 81−80 > 0 and 91− 90 > 0: at least two08 and two19 appear below6 (Lemma-Computation 2.18).
47
(2) 81−80=−1 or 91− 90=−1: only08’s or only19’s appear below6 (Lemma-Computation 2.19).
(3) 81−80= 0 or 91− 90= 0: only one08 or only one19 appear below6 (Lemma-Computation 2.20).
We compute the contribution of each case in the next three lemmas.
Lemma-Computation 2.18.Case 1 (81−80 > 0 and 91− 90 > 0) contributes 0 toX&.
Proof. Consideraterm 6∧ℎ comingfromacutinCase1. Let 8′
0≥80 beminimalsuchthat 08′
0 appearsin ℎ,
and8′
1≤81 be maximal such that08′
1 appears inℎ. Deﬁne9′
0,9 ′
1 in the analogous way. For example, for cuts
of type (1a),8′
0=80; for cuts of type (1c),
8′
0=
 

80 if (F| () is (180|D80
)
80+ 1 if (F| () is (080|C80
) or (080180|
{
C80,D 90
} ) ,
where (F| () is the segment that contains the vertex of the cut. Notice that8′
0−80≤ 1 and 90− 9′
0≤ 1, and
81−80 > 0 implies8′
1−8′
0≥− 1.
Group all terms ofX& coming from Case 1 by the type of cut and by8′
0,9 ′
0,8′
1,9 ′
1. These groups can be
expressed in terms of
~6((1)∧ QSh(08′
0,...,0 8′
1,1 9′
0,...,1 9′
1,
(
08′
0...0 8′
1·19′
0...1 9′
1
)−1
|
C8′
0,...,C 8′
1,D 9′
0,...,D 9′
1,( 2
)
for some(1,( 2. Indeed, the arrangements of segments that may occur in the lower part of the cut, given
80,9 0 and8′
1,9 ′
1, are precisely the quasishuﬄes. Applying the lower-weight shuﬄe relations, this expression
becomes
~6((1)∧
(
∗(08′
0,...,0 8′
1,
(
08′
0...0 8′
1
)−1
|C8′
0,...,C 8′
1,
{
D9′
0,...,D 9′
1
}
⊔(2
))
+~6((1)∧
(
∗(19′
0,...,1 9′
1,
(
19′
0...1 9′
1
)−1
|D9′
0,...,D 9′
1,
{
C8′
0,...,C 8′
1
}
⊔(2
))
. (2.32)
Fix8′
0,8′
1,9 ′
0,9 ′
1, and introduce the notation
~5(8′
0,8′
1,()= ∗(08′
0,...,0 8′
1,
(
08′
0...0 8′
1
)−1
|C8′
0,...,C 8′
1,
{
D90+1,...,D 91−1
}
⊔(),
~5(9′
0,9 ′
1,()= ∗(19′
0,...,1 9′
1,
(
19′
0...1 9′
1
)−1
|D9′
0,...,D 9′
1,
{
C80+1,...,C 81−1
}
⊔().
The expressions in (2.32) can be rewritten with~5 and ~5.
48
Now let us collect these terms coming from diﬀerent cuts and show that they yield 0. By symmetry, it
suﬃces to show this for three kinds of terms~5(8′
0,8′
1,9 ′
0,9 ′
1,( 2): where8′
0=80 and8′
1=81; where8′
0=80 and
8′
1=81− 1; and where8′
0=80+ 1 and8′
1=81− 1.
Look at the terms with8′
0 =80 and8′
1 =81 (all08 that are not in6 are in5). They arise from cuts (1a)
and (1b) where the cut segment is180+1 or181−1 and from cuts (1c) and (1d) where the cut segment and the
segment containing the vertex are180+1 and181−1, or vice versa. These cases give:
−~6 (D91
)∧ ~5(80,8 1,
{
D90
}
⊔
{
D91
}
),
~6 (D90
)∧ ~5(80,8 1,
{
D91
}
⊔
{
D90
}
),
(D91−D90)~6 ({
D90,D 91
})∧ ~5(80,8 1,
{
D90,D 91
}
),
the sum of which is 0 by (2.13).
The terms with8′
0=80 and8′
1=81− 1 (all08 that are not in6, except the last, are in5) come from three
sources:
– cuts of type (1a) where the cut segmentG2 is either081 or081191;
– cutsoftype(1c)and(1d)wherethesegment G1 containingthevertexandthesegment G2 thatiscutare 190
and081, or vice versa;
– cutsoftype(1c)and(1d)wherethesegment G1 containingthevertexandthesegment G2 thatiscutare 190
and081191, or vice versa.
A similar computation shows their total contribution is 0.
Finally, consider terms with8′
0 =80+ 1 and8′
1 =81− 1 (all08 not in6 except the ﬁrst and last are in5).
They arise from cuts of type (1c) and (1d), where the segmentG1 is either080 or080190 and the segmentG2 is
either081 or081191, yielding four cases:
(G1,G 2)=(080,0 91),(080190,0 91),(080,0 91191),(080190,081191).
The sum of their contributions is also 0. □
Lemma-Computation2.19. ThecontributionofCase2( 81−80=−1)to X& isgivenbythesumofexpressions
(2.33)-(2.36) below.
49
Proof. Suppose that81−80=−1. The cuts of types (1a), (1b), (1c), and (1d) contribute
−~6 (D91
)∧ ~5(90,9 1− 1,D 91), (2.33)
~6 (D90
)∧ ~5(90+ 1,9 1,D 90), (2.34)
−D90~6 ({
D90,D 91
})∧ ~5(90+ 1,9 1− 1,
{
D90,D 91
}
), (2.35)
D91~6 ({
D90,D 91
})∧ ~5(90+ 1,9 1− 1,
{
D90,D 91
}
), (2.36)
respectively. □
By symmetry, analogous expressions will result if91− 90=−1.
Lemma-Computation 2.20. The contribution of Case 3 (81−80 = 0) to theX& is given by the sum of
expressions (2.45) and (2.46) below.
Proof. Suppose81−80= 0, so only one segment08 occurs below6.
If 91− 90= 0, then it is easy to see that only cuts of type (1a) and (1b) contribute nonzero terms, and that
the (1a) terms cancel with the (1b) terms. So assume91− 90 > 0.
The cuts of type (1a) fall into three classes depending on which segment is cut: (i)080, (ii)191, or (iii)
080191. The ﬁrst two contribute
−~6 (C80
)∧ ~5(90,9 1,C80), (2.37)
−~6 (D91
)∧ QSh1,9 1−90
(080,1 90,...,1 91−1, (080190...1 91−1
)−1|
C80,D 90,...,D 91−1,D 91
)
≡− ~6 (D91
)∧
(
~5(90,9 1− 1,
{
C80,D 91
}
)
+ ∗(080,0−1
80 |C80,
{
D90,...,D 91
} ))
, (2.38)
respectively, where we have used that the sequences that may occur in the lower part of the cut are precisely
the shuﬄes of08 and19 appearing below6, except the cut segment191. Finally, the third class gives
1
C80−D91
(
~6 (C80
)∧ ~5(90,9 1− 1,C80)
−~6 (D91
)∧ ~5(90,9 1− 1,D 91)
)
, (2.39)
where we have applied (2.13) to break the generating functions with
{
C80,D 91
}
into ones with onlyC80 orD91.
The cuts of type (1c) fall into ﬁve classes, depending on the segment where the vertex of the cut lies and
50
the segment that is cut: (i) vertex on080 and191 is cut, (ii) vertex on190 and191 is cut, (iii) vertex on190 and
080 iscut,(iv)vertexon 190 and080191 iscut,(v)vertexon 080190 and191 iscut. Theycontributethefollowing
terms:
−C80~6 ({
C80,D 91
})∧ ~5(90,9 1− 1,
{
C80,D 91
}
), (2.40)
−D90~6 ({
D90,D 91
})∧ QSh1,9 1−90−1(080,1 90+1,...,1 91−1, (080190+1...1 91−1
)−1|
C80,D 90+1,...,D 91−1,
{
D90,D 91
} )
≡−D90~6 ({
D90,D 91
})∧
(
~5(90+ 1,9 1− 1,
{
C80,D 90,D 91
}
)
+ ∗(080,0−1
80 |C80,
{
D90,...,D 91
} ))
, (2.41)
−D90~6 ({
D90,C80
})∧ ~5(90+ 1,9 1,
{
D90,C 90
}
), (2.42)
1
C80−D91
(
D90~6 ({
D90,C80
})∧ ~5(90+ 1,9 1− 1,
{
D90,C80
}
)
−D90~6 ({
D90,D 91
})∧ ~5(90+ 1,9 1− 1,
{
D90;D91
}
)
)
, (2.43)
1
C80−D90
(
C80~6 ({
C80,D 91
})∧ ~5(90+ 1,9 1− 1,
{
C80,D 91
}
)
−D90~6 ({
D90,D 91
})∧ ~5(90+ 1,9 1− 1,
{
D90,D 91
}
)
)
. (2.44)
Thecuts(1b)and(1d)contributeantisymmetricterms,i.e., D90 andD91 areexchangedand ~5(90+30,9 1−
31,() becomes−~5(90+31,9 1−30,().The entire contribution of case 3 is then the symmetrization of the
sum of expressions (2.37)-(2.44).
The expression (2.37) with its symmetrization cancels to 0.
The remaining terms form the contribution of Case 3, and are simpliﬁed to
~6 ({
C80,D 91
})∧ ~5(90,9 1− 1,D 91)− ~6 ({
C80,D 90
}) ∧~5(90+ 1,9 1,D 90) (2.45)
−(D91−D90)~6 ({
C,D 90,D 91
})∧ ~5(90+ 1,9 1− 1,
{
D90,D 91
}
). (2.46)
Analogous expressions result if91− 90= 0. □
Proof of Lemma 2.17.Letuscollectthetermsobtainedfromcases2and3: (2.33)-(2.36),(2.45),and(2.46).
Considerﬁrsttheexpressionsoftheform ~5(90,9 1− 1,D 91),arisingfrom(2.33)and(2.45). (Thenotation
~5(), which by deﬁnition depends on80 and81, is unambiguous here since no08 appear in the expression for
51
~5() when81−80≤ 0.) We claim that for ﬁxed90 and 91, the sum of these terms over all6 is precisely
−QSh<,=−(91−90)(01,...,0 A,1 1,...,1 90...1 91,...,1 B,2 |
C1,...,C A,D 1,...,D 91,...,D B,E ) ∧ ~5(90,9 1− 1,D 91). (2.47)
Indeed, the term that appears on the left side for a ﬁxed6 is−~6 (D91
) if81−80 =−1 and ~6 ({
C80,D 91
}) if
81−80 = 0 . The quasishuﬄes for which the underlined segment collides with no08 provides the terms with
81−80=−1,whilethequasishuﬄesforwhichtheunderlinedsegmentcollideswithsome 08 providetheterms
with80=81=8.
In a similar way, the expressions withD90
~5(90+ 1,9 1− 1,
{
D90,D 91
}
), coming from (2.46) and (2.35),
yield
−D0QSh<,=−(91−90)(01,...,0 A,1 1,...,1 90...1 91,...,1 B,2 |
C1,...,C A,D 1,...,
{
D90,D 91
}
,...,D B,E ) ∧ ~5(90+ 1,9 1− 1,
{
D90,D 91
}
). (2.48)
The expressions with~5(90+ 1,9 1,D 91) andD91
~5(90+ 1,9 1− 1,
{
D90,D 91
}
) give the antisymmetric terms.
Applying the shuﬄe relations of lower depth to (2.47) and (2.48), we get the total contribution of cases 2
and 3 for ﬁxed90 and 91:
−
(
∗(01,...,0 A,1 1...1 B·2|C1,...,C A,
{
D1,...,D 90−1,D 91,D 91+1,...,D B,E
} )
+ ∗(11,...,1 90...1 91,...,1 B,0 1...0 A·2|D1,...,D 91,...,D B,{C1,...,C A,E} ))
∧ ∗(190,1 90+1,...,1 91−1, (190...1 91−1
)−1|D90,D 90+1,...,D 91−1,D 91
) (2.49)
+
(
∗(01,...,0 A,1 1...1 B·2|C1,...,C A,
{
D1,...,D 90−1,D 90,D 91+1,...,D B,E
} )
+ ∗(11,...,1 90...1 91,...,1 B,0 1...0 A·2|D1,...,D 91,...,D B,{C1,...,C A,E} ))
∧ ∗(190+1,...,1 91−1,1 91, (190+1...1 91
)−1|D90+1,...,D 91−1,D 91,D 90
) (2.50)
+(D91−D90)
(
∗(01,...,0 A,1 1...1 B·2|C1,...,C A,
{
D1,...,D 90−1,D 90,D 91,D 91+1,...,D B,E
} )
+ ∗(11,...,1 90...1 91,...,1 B,0 1...0 A·2|D1,...,
{
D90,D 91
}
,...,D B,{C1,...,C A,E} ))
∧ ∗(190+1,...,1 91−1, (191...1 91−1
)−1|D90+1,...,D 91−1,
{
D90,D 91
} ). (2.51)
Notice that this expression does not depend on80,8 1, and all but one of the segments in each generating
52
function 5 depends only on the08 or only on the19.
Reindexingleadstocancelationofallterms 5(01,...,0 A,... ) exceptthetermin(2.49)where 90= 1and
the term in (2.50) where91==. That is, if90≠ 1 and 91≠=, then this expression becomes
(90,9 1) :=−
(
∗(11,...,1 90...1 91,...,1 B,0 1...0 A·2|D1,...,D 91,...,D B,{C1,...,C A,E} )
∧ ∗(190,1 90+1,...,1 91−1, (190...1 91−1
)−1|D90,D 90+1,...,D 91−1,D 91
))
(2.52)
+
(
∗(11,...,1 90...1 91,...,1 B,0 1...0 A·2|D1,...,D 90,...,D B,{C1,...,C A,E} )
∧ ∗(190+1,...,1 91−1,1 91, (190+1...1 91
)−1|D90+1,...,D 91−1,D 91,D 90
))
(2.53)
+
(
∗(11,...,1 90...1 91,...,1 B,0 1...0 A·2|D1,...,
{
D90,D 91
}
,...,D B,{C1,...,C A,E} )
∧ ∗(190+1,...,1 91−1, (191...1 91−1
)−1|D90+1,...,D 91−1,
{
D90,D 91
} ))
(D91−D90). (2.54)
If 90= 1 or 91=B, the following terms remain, respectively:
!(91) :=− ∗(01,...,0 A,1 1...1 B·2|C1,...,C A,
{
D91,D 91+1,...,D B,E
} )
∧ ∗(11,...,1 91−1, (11...1 91−1
)−1|D1,...,D 91−1,D 91
), (2.55)
’(90) := ∗(01,...,0 A,1 1...1 B·2|C1,...,C A,
{
D1,...,D 90,E
} )
∧ ∗(190+1,...,1 B, (190+1...1 B
)−1|D90+1,...,D B,D 90
). (2.56)
Identical terms
(80,8 1),
!(81),
’(80) with the(08| C8
) and (19| D9
) exchanged appear in the cases
91− 90= 0 or−1.
So the total contribution of cuts of type 1 is
Õ
1≤90,9 1≤B
91−90≥−1
(90,9 1)+
Õ
1≤80,81≤A
81−80≥−1

(80,8 1)
+
Õ
1≤91≤B
!(91)+
Õ
1≤90≤B
’(90)+
Õ
1≤81≤A

!(81)+
Õ
1≤80≤A

’(80) (2.57)
ﬁnishing the computation. □
Lemma-Computation 2.21. The contribution of cuts of type (2) toX& is given by the sum of expressions
(2.73)-(2.77) below, plus symmetrical terms.
Proof. A cut of type (2a/b/c) divides the circle into a left part6 and a right partℎ (see Figure 2.6). Let80 be
53
maximalsuchthat 080 appearsin 6 and81 minimalsuchthat 081 appearsin ℎ, with80=−1or81=<+ 1ifthe
corresponding segments do not appear. Deﬁne90,9 1 in the same manner, for the19.
Let
5!(80,9 0,()= ∗(01,...,0 80, (01...0 80
)−1|C1,...,C 80,
{
D1,...,D 90
}
⊔(),
5’(81,9 1,()= ∗(081,...,0 A, (081...0 A
)−1|C81,...,C A,
{
D91,...,D <
}
⊔(),
and deﬁne6!(80,9 0,() and6’(81,9 1,() in a similar way for the(19| D9
). (As usual, one interprets these
expressions as 0 if the index set is empty.) Also let
@!(80,9 0,()= QSh80,9 0
(01,...,0 80,1 1,...,1 90, (01...0 80·11...1 90
)−1|C1,...,C 80,D 1,...,D 90,( ),
= 5!(80,9 0,()+ 6!(80,9 0,()
@’(81,9 1,()= QShA−81+1,B−91+1(081,...,0 A,1 91,...,1 B, (081...0 A·191...1 B
)−1|C81,...,C A,D 91,...,D B,( )
= 5’(81,9 1,()+ 6’(81,9 1,().
Consider cuts (2a) for ﬁxed80,8 1,9 0,9 1. For such cuts,
81−80= 91− 90= 1, −1≤80≤A, −1≤ 90≤ B.
The6 that occur in the resulting terms are exactly the quasishuﬄes of{08 :8≤80} and
{
19 : 9≤ 90
}
. The
analogous statement holds forℎ. The contribution of cuts (2a) is
−@!(80,9 0,E)∧ @’(80+ 1,9 0+ 1,E). (2.58)
Now look at cuts (2b) and (2c). The non-distinguished segment containing the vertex or the cut is either
080+1 (80 <A ),190+1 (90 < B), or080+1190+1 (80 <A,9 0 < B). The terms coming from the sum of (2b) and (2c)
are, for these three cases respectively,
(E−C80+1)@!(80,9 0,
{
C80+1,E
}
)∧ @’(80+ 2,9 0+ 1,
{
C80+1,E
}
), (2.59)
(E−D90+1)@!(80,9 0,
{
D90+1,E
}
)∧ @’(80+ 1,9 0+ 2,
{
D90+1,E
}
), (2.60)
−1
C80+1−D90+1
(
(E−C80+1)@!(80,9 0,
{
C80+1,E
}
)∧ @’(80+ 2,9 0+ 2,
{
C80+1,E
}
)
−(E−D80+1)@!(80,9 0,
{
D90+1,E
}
)∧ @’(80+ 2,9 0+ 2,
{
D90+1,E
}
)
)
. (2.61)
54
Letusassemblethetermsoftheform 5!∧6’and6!∧6’comingfromapplicationoftheshuﬄerelations
to the@! and@’. (The terms6!∧ 5’and 5!∧ 5’are symmetrical.)
The terms5!∧6’, for−1≤80 <A and−1≤ 90 < B, are:
−5!(80,9 0,E)∧ 6’(80+ 1,9 0+ 1,E)
+(E−C80+1)5!(80,9 0,
{
C80+1,E
}
)∧ 6’(80+ 2,9 0+ 1,
{
C80+1,E
}
),
+(E−D90+1)5!(80,9 0,
{
D90+1,E
}
)∧ 6’(80+ 1,9 0+ 2,
{
D90+1,E
}
),
− 1
C80+1−D90+1
(
(E−C80+1)5!(80,9 0,
{
C80+1,E
}
)∧ 6’(80+ 2,9 0+ 2,
{
C80+1,E
}
)
−(E−D80+1)5!(80,9 0,
{
D90+1,E
}
)∧ 6’(80+ 2,9 0+ 2,
{
D90+1,E
}
)
)
= 5!(80,9 0,C80+1)∧ 6’(80+ 1,9 0+ 1,E)
−5!(80,9 0+ 1,C80+1)∧ 6’(80+ 1,9 0+ 2,E).
Summing this over90 leaves
5!(80, 0,C80+1)∧ 6’(80+ 1, 1,E)− 5!(80,B,{DB,E})∧ 6’(80+ 1,B+ 1,E) (2.62)
= 5!(80, 0,C80+1)∧ 6’(80+ 1, 1,E) =−
!(80+ 1). (2.63)
If80=A,9 0 < B, then from (2.58) and (2.60) we also have the terms
−5!(A,9 0,E)∧ 6’(A+ 1,9 0+ 1,E), (2.64)
(E−D90+1)5!(A,9 0,
{
D90+1,E
}
)∧ 6’(A+ 1,9 0+ 2,
{
D90+1,E
}
)
= 5!(A,9 0+ 1,E)∧ (6’(A+ 1,9 0+ 2,E)− 6’(A+ 1,9 0+ 2,D 90+1)). (2.65)
The last term5!(A,9 0+ 1,E)∧ 6’(A+ 1,9 0+ 2,D 90+1) is’(90+ 1). The remaining term and (2.64) mostly
cancel when summed over90, leaving only
/ :=−5!(A, 0,E)∧ 6’(A+ 1, 1,E)+ 5!(A,B,E )∧ 6’(A+ 1,B+ 1,E)
=−∗(01,...,0 A,
Ö
9
19·2|C1,...,C A,E )∧ ∗(11,...,1 B,
Ö
8
08·2|D1,...,D B,E ). (2.66)
55
If 90=B,8 0 <A , there are terms
−5!(80,B,E)∧ 6’(80+ 1,B+ 1,E) = 0,
(E−C80+1)5!(80,B,
{
C80+1,E
}
)∧ 6’(80+ 2,B+ 1,
{
C80+1,E
}
) = 0. (2.67)
Finally,80=A,9 0=B also produces 0.
Thus the sum of terms5!∧6’is
/−
A−1Õ
80=0

!(80+ 1)−
B−1Õ
90=0
’(90+ 1). (2.68)
Similarly, terms of the form6!∧ 5’give
−/−
B−1Õ
90=0
!(90+ 1)−
A−1Õ
80=0

’(80+ 1). (2.69)
The terms6!∧6’where80 <A , 90 < Bare, similarly:
−6!(80,9 0,C80+1)∧ 6’(80+ 2,9 0+ 1,
{
C80+1,E
}
)
+6!(80,9 0,
{
C80+1,D 90+1
}
)∧ 6’(80+ 2,9 0+ 2,
{
C80+1,E
}
). (2.70)
If80=A,9 0 < B, we get the terms
−6!(A,9 0,E)∧ 6’(A+ 1,9 0+ 1,E),
(E−D90+1)6!(A,9 0,
{
D90+1,E
}
)∧ 6’(A+ 1,9 0+ 2,
{
D90+1,E
}
). (2.71)
If 90=B,8 0 <A , there are terms
−6!(80,B,E)∧ 6’(80+ 1,B+ 1,E) = 0,
(E−C80+1)6!(80,B,
{
C80+1,E
}
)∧ 6’(80+ 2,B+ 1,
{
C80+1,E
}
) = 0. (2.72)
The case80=A, 90=B again contributes 0.
The terms5!∧ 5’are symmetrical.
56
Assembling (2.69)-(2.71), the total contribution of cuts (2a/b/c) is
−
AÕ
8=1

!(8)−
BÕ
9=1
’(9) (2.73)
+
A−1Õ
80=0
B−1Õ
90=0
(
−6!(80,9 0,C80+1)∧ 6’(80+ 2,9 0+ 1,
{
C80+1,E
}
) (2.74)
+6!(80,9 0,
{
C80+1,D 90+1
}
)∧ 6’(80+ 2,9 0+ 2,
{
C80+1,E
}
)
)
(2.75)
+
B−1Õ
90=0
(
−6!(A,9 0,E)∧ 6’(A+ 1,9 0+ 1,E) (2.76)
+(E−D90+1)6!(A,9 0,
{
D90+1,E
}
)∧ 6’(A+ 1,9 0+ 2,
{
D90+1,E
}
)
)
, (2.77)
plus symmetrical terms. □
Proof of Lemma 2.16.Cancellation of (2.57) with (2.73) leaves
Õ
1≤90,9 1≤B
91−90≥−1
(90,9 1) (2.78)
plus the symmetrical term.
ThusX& is the symmetrized sum of expressions (2.74)-(2.78). □
Lemma-Computation 2.22(Step 1(b)). Modulo elements(0,G), X’ and X’ are given by expression
(2.91) below and its symmetric expression, respectively.
Proof of Lemma 2.22.We computeX’.
Recall that the distinguished segment of’ is ˛
908·2. We use the above classiﬁcation of cuts of type
(1a/b/c/d) and (2a/b/c).
Consider ﬁrst the terms5∧6 coming from cuts of type (1). For each such term, let90,9 1 be the minimal
and maximal indices of19 that do not appear in6. For ﬁxed90,9 1, the cuts of type (1a), (1b), and (1c/d)
produce precisely the expressions (2.52), (2.53), and (2.54) above. Thus the contribution of cuts of type (1)
is(90,9 1), and the total contribution is
Õ
0≤90,9 1≤B
91−90≥−1
(90,9 1). (2.79)
Next, we look at cuts of type (2). We will need a simpliﬁed formula for terms where either the vertex or
the cut are on a segment indexed with(={B1,...,B :}. If: = 1 and the vertex is at a nonzero point, we get
57
terms of the form
∗(···| ...,B 1
)∧ ∗(···| B1,... ).
Applying (2.13), it is easy to show by induction that, for general:, the resulting terms are
:Õ
8=1
∗(···| ..., {B1,...,B 8} )∧ ∗(···| {B8,...,B :},... ). (2.80)
For example, if: = 2, this becomes
∗(···| ...,B 1
)∧ ∗(···| {B1,B 2},... )+ ∗(···| ..., {B1,B 2} )∧ ∗(···| B2,... )
= 1
B1−B2
(
∗(···| ...,B 1
)∧ ∗(···| B1,... )+ ∗(···| ...,B 2
)∧ ∗(···| B2,... ))
,
agreeing with the formula following directly from (2.13) that has been used in the previous computations.
Similarly, if the vertex is on some segmentB′, the term for: = 1,
B′∗(···| ..., {B1,B′} )∧ ∗(···| {B1,B′},... ),
expands into
B′
:Õ
8=1
∗(···| ..., {B1,...,B 8,B′} )∧ ∗(···| {B8,...,B :,B′},... ). (2.81)
Finally, if the vertex is at a 0 on the segmentB8 and the cut is on the segmentB′, we get terms
:Õ
8=1
B8∗(···| ..., {B1,...,B 8,B′} )∧ ∗(···| {B8,...,B :,B′},... )
+
:−1Õ
8=1
∗(···| ..., {B1,...,B 8,B′} )∧ ∗(···| {B8+1,...,B :,B′},... ). (2.82)
Theseidentitiescanalsobeshowncombinatorially,byinterpretingthedeﬁnitionofthemultiplegenerating
functions in terms of collapsing segments.
For a term5∧6 coming from a cut of type (2), let90 be the maximal index of19 appearing in5 and 91
the minimal index in6, so91− 90= 1for cuts (2a) and91− 90= 2for cuts (2b/c). By (2.80), for ﬁxed90, the
cuts of type (2a) contribute
−
<Õ
8=1
6!(8,9 0,∅)∧ 6’(8,9 0+ 1,E) (2.83)
+6!(A,9 0,E)∧ 6’(A+ 1,9 0+ 1,E). (2.84)
58
By (2.81), the cuts of type (2b) contribute
−
<Õ
8=1
D90+16!(8,9 0,D 90+1)∧ 6’(8,9 0+ 2,
{
D90+1,E
}
) (2.85)
−D90+16!(A,9 0,
{
D90+1,E
}
)∧ 6’(A+ 1,9 0+ 2,
{
D90+1,E
}
). (2.86)
By (2.82), the cuts of type (2c) contribute
<Õ
8=1
C86!(8,9 0,D 90+1)∧ 6’(8,9 0+ 2,
{
D90+1,E
}
) (2.87)
+E6!(A,9 0,
{
D90+1,E
}
)∧ 6’(A+ 1,9 0+ 2,
{
D90+1,E
}
) (2.88)
+
<Õ
8=1
6!(8,9 0,D 90+1)∧ 6’(8+ 1,9 0+ 2,
{
D90+1,E
}
). (2.89)
The sum of expressions (2.85), (2.87), and (2.89) simpliﬁes to
6!(8,9 0,D 90+1)∧ 6’(8,9 0+ 2,E). (2.90)
Then, letting
(90) be the sum of expressions (2.83), (2.84), (2.86), (2.88), and (2.90), the coproduct of’
is
Õ
0≤90,9 1≤B
91−90≥−1
(90,9 1)+
B−1Õ
9=0

(9). (2.91)
The coproduct of’ is the symmetric expression. □
Proof of Lemma 2.14.We now compare the results of the computations in Lemmas 2.16 and 2.22.
We have computed thatX& is the symmetrization of
(2.74)+( 2.75)+( 2.76)+( 2.77)+( 2.78)
andX’+X’ is the symmetrization of
(2.79)+
=−1Õ
9=0
[
(2.83)+( 2.84)+( 2.86)+( 2.88)+( 2.90)
]
.
Obviously(2.79)=(2.78). Now
(2.74)=
Õ
(2.83), (2.75)=
Õ
(2.90), (2.76)=
Õ
(2.84), (2.77)=
Õ
[(2.86)+( 2.88)],
59
which ﬁnishes the proof. □
Proof of Step 2
Here we show the terms of weight(1)∧( F− 1) coming fromX&−X’−X’ are 0.
Proof of Lemma 2.15.Weﬁrstexaminetherelevanttermsof X&. Letuscomputethecoeﬃcient !
8 occurring
with(0,08). These come from shuﬄes containing segment(08| C8
), a segment(0819|
{
C8,D 9
} ), and the
segment (2|E) (where we write2= ˛
80−1
8
˛
91−1
9 ).
Inspectthegeneratingfunctionsofdepth1 ∗(F,F−1| B1,B 2
) thatappearedintheproofofLemma2.14.
All generating functions in the lower half of cuts (1a/b/c/d) were written in a form where(F| B1
) is the ﬁrst
segment counterclockwise of the distinguished segment, rather than with the segment counterclockwise of
the vertex of the cut as in (2.19)).
So, by the remark following Lemma 2.10, the terms (2.24) vanish in the coproduct, so the terms arising
from these cuts are canceled by the lower-depth shuﬄe relations in Lemma 2.14. Similarly, for cuts of type
(2), we only have terms (2.22) contributing the coeﬃcient of(0,0−1
8 ).
Forquasishuﬄesinwhich (08|C8
)appears,theterms(2.23)wheresome 19 appearsimmediatelyclockwise
of08 gives terms
QShA,B
(89)
(01,...,0 8,...,0 A,1 1,...,1 9,2 |C1,..., ∅,...,C A,D 1,...,D 9,...,D B,E ), (2.92)
where QShA,B
(89) denotes the sum over only those quasishuﬄes where08 collapses with19.
The terms (2.23) where either08−1 or some08−119 appears immediately clockwise of08 sum to
QShA−1,B (01,...,0 8−108,08+1,...,0 A,1 1,...,1 B,2 |C1,...,C 8−1,C8+1,...,C A,D 1,...,D B,E ). (2.93)
Finally, the terms (2.22) contribute to!
8 the terms
C8QShA,B
(8)
(01,...,0 A,1 1,...,1 B,2 |C1,...,C A,D 1,...,D B,E ) (2.94)
where QSh(8) denotes the the quasishuﬄes in which08 does not collapse with any19.
For quasishuﬄes in which some(0819|
{
C8,D 9
} ) appears, the terms (2.23) contribute 0, since they arise
60
from cuts of segments containing no 0s.The terms (2.22) give
−1
C8−D9
(
C8QShA,B
(89)
(01,...,0 8,...,0 A,1 1,...,1 9,...,1 B,2 |C1,...,C 8,...,C A,D 1,..., ∅,...,D B,E )
−D9 QShA,B
(89)
(01,...,0 8,...,0 A,D 1,...,D 9,...,D B,E |C1,..., ∅,...,C A,D 1,...,D 9,...,D B,E ))
=−C8QShA,B
(89)
(01,...,0 8,...,0 A,1 1,...,1 B,2 |C1,...,C 8,...,C A,D 1,...,D 9,...,D B,E ) (2.95)
−QShA,B
(89)
(01,...,0 8,...,0 A,1 1,...,1 B,2 |C1,..., ∅,...,C A,D 1,...,D 9,...,D B,E ). (2.96)
For the segment(2|E), which includes a factor of0−1
8 , we get a contribution of
−EQShA,B (01,...,0 A,1 1,...,1 B,2 |C1,...,C A,D 1,...,D B,E ) =−E&. (2.97)
from (2.22) and
−QShA−1,B (01,...,0 <−1,1 1,...,1 B,0A2|C1,...,C A−1,D 1,...,D B,CA
)
−QShA,B−1(01,...,0 A,1 1,...,1 =−1,1B2|C1,...,C A,D 1,...,D B−1,DB
)
+QShA−1,B−1(01,...,0 <−1,1 1,...,1 =−1,0A1B2|C1,...,C A−1,D 1,...,D B−1,{CA,DB} ),
from (2.23), with three terms, depending on which segment (0A,1B, or0A1B) appears clockwise of2. By the
lower-depth shuﬄe relations, this simpliﬁes to
−∗(01,...,0 A,
Ö
9
19·2|C1,...,C A,{D1,...,D B} ) (2.98)
−∗(11,...,1 B,
Ö
8
08·2|D1,...,D B,{C1,...,C A} ). (2.99)
The terms (2.92) cancel with (2.96). Summing (2.95) over9 and adding to (2.94) results in
C8QShA,B (01,...,0 A,1 1,...,1 B,2 |C1,...,C A,D 1,...,D B,E ) =C8&. (2.100)
Thus!
8 is the sum of (2.93), (2.97), (2.98), (2.99) and (2.100). Applying lower-depth shuﬄe relations and
61
(2.13), this sum simpliﬁes to
!
8 = ∗(01,...,0 8−108,08+1,...,0 A,
Ö
9
19·2|C1,...,C 8−1,C8+1,...,C A,{D1,...,D B}⊔{E} ) (2.101)
−∗(01,...,0 A,
Ö
9
19·2|C1,...,C A,{D1,...,D B} ) (2.102)
+(C8−E)(&−’). (2.103)
Nowletuscomputethecoeﬃcient "
8 occurringwith (0,08) inX(’). Forthesegment (08|C8
) in’,
(2.22) and (2.23) contribute the terms
C8∗(01,...,0 8,...,0 A,
Ö
9
19·2|C1,...,C 8,...,C A,{D1,...,D B}⊔{E} ) =C8’, (2.104)
∗(01,...,0 8−108,08+1,...,0 A,
Ö
9
19·2|C1,...,C 8−1,C8+1,...,C A,{D1,...,D B}⊔{E} ), (2.105)
where the second term appears only if8 >1.
Thedistinguishedsegment (˛
80−1
8 |
{
D9
}
⊔{E} ) contributesonlyaterm(2.22). Byanargumentsimilar
to that in Lemma 2.22, this term can be written
−E’− ∗(01,...,0 A,
Ö
9
19·2|C1,...,C A,{D1,...,D B} ). (2.106)
Combining (2.101)-(2.106), we ﬁnd that
(!
8 −"
8)=(C8−E)(&−’−’).
Therefore, adding the symmetric terms for the(0,1 9),
X(&−’−’)=

AÕ
8=1
(0,08)(C8−E)+
BÕ
9=1
(0,1 9)(D9−E)

∧(&−’−’)
modulo lower-depth shuﬄe relations and elements(weight 1)∧( weight 1). □
Conclusion
Wearereadytousethecoproductwehavecomputedtoreducetheproofoftherelationstoasimplebasecase.
Proof of Theorem 2.5(a).We induct on the depthA+B. WhenA = 0 orB= 0, QSh
A,B
is identically 0.
62
IfA,B > 0,takingcoproductonbothsidesof(2.31)andusingthat X2= 0,onededucesthat X(&−’−’)=
0 modulo shuﬄe relations of depth<A +B and terms (weight 1)∧(weight 1).
When no terms(0,G)∧ (0,H) are present in the coproduct, Lemma 2.13 and Lemma 2.15 imply that
X(&−’−’) lies in the ideal generated by lower-depth relations.
These terms appear only in a base case: the constant term of the shuﬄe relation forA = B= 1. Showing
the coproduct of this term is 0 amounts to proving the identity
X([∗(0|0,1|0,2|0)+ ∗(1|0,0|0,2|0)− ∗(01|1,2|0)]−∗(0|0,12|1)− ∗(1|0,02|1))= 0. (2.107)
We compute directly that the left side of (2.107) is
(1,0)∧ (1,01)+ (1,01)∧( (1,1)+ (0,0))+( (1,1)+ (0,0))∧ (1,0)
+(1,1)∧ (1,01)+ (1,01)∧( (1,0)+ (0,1))+( (1,0)+ (0,1))∧ (1,1)
−(1,01)∧ (0,01)+ (1,0)∧ (0,0)+ (1,1)∧ (0,1)
= (1,01)∧ (0,0)+ (0,0)∧ (1,0)
+(1,01)∧ (0,1)+ (0,1)∧ (1,1)
−(1,01)∧ (0,01)+ (1,0)∧ (0,0)+ (1,1)∧ (0,1) = 0.
The theorem is proved. □
