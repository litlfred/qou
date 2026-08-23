---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-020-relations-for-correlators
section_title: "Relations for correlators"
section_number: null
pages: 87-89
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
Recall from §1.1.1 that the Hodge correlators satisfy a ﬁrst shuﬄe relation, and that in Chapter 2 we describe
a family ofsecond shuﬄe relationsfor correlators on P1, the terms of which were formed by permuting
quotients of successive arguments. One of the main results of this chapter is that the Hodge correlators on an
elliptic curve satisfy second shuﬄe relations in depth 2.
79
0
/u1D44E /u1D44E + /u1D44F
/u1D446/u1D45B1,/u1D45B′
1
/u1D446/u1D45B2,/u1D45B′
2
/u1D446/u1D45B0,/u1D45B′
0
+
0
/u1D44F /u1D44E + /u1D44F
/u1D446/u1D45B2,/u1D45B′
2
/u1D446/u1D45B1,/u1D45B′
1
/u1D446/u1D45B0,/u1D45B′
0
Figure 3.2. The highest-depth terms of the second shuﬄe relation on an elliptic curve.
For Hodge correlators of depth 2 on an elliptic curve with arbitrary base point, this new relation has the
form:
CorH((=0,=′
0, 0,(=1,=′
1,0,( =2,=′
2,0+1)+CorH((=0,=′
0, 0,(=2,=′
2,1,( =1,=′
1,0+1)+lower-depth terms= 0, (3.5)
where an argument(=,=′ indicates that we sum over all possible ways to insert in some order the arguments
l,...,l|    {z    }
=
,l,..., l|    {z    }
=′
.
Thehighest-depthtermsintheserelationsarisefromshuﬄesofthe diﬀerencesbetweensuccessivearguments,
G8−G8−1, together with the 1-forms between those arguments. For example, in (3.5) we have shuﬄed0 (with
=1 copies ofl and=′
1 ofl) with1 (with=2l’s and=′
2l’s). See Figure 3.2) for an illustration.
We describe the lower-depth correction terms in §3.2.2. In the simplest case – weight 4 – the full relation
is:
CorH(0,0,0 +1)+ CorH(0,1,0 +1)−( CorH(0,l, l,0+1)+ CorH(0,l,l,0 +1))
− 1
2
(
CorH(0,0,l, l)− CorH(0,0, l,l)
+CorH(0,1,l, l)− CorH(0,1, l,l)
+CorH(l,l,0,0 +1)− CorH(l,l,0,0 +1)
+CorH(l,l,1,0 +1)− CorH(l,l,1,0 +1)
)
= 0.
Therelation(3.5)canbeformulatedsimplyasafunctionalequationonbiperiodicfunctionsofthreecomplex
variables. It states that a sum of several integrals over an elliptic curve is equal to 0, modulo correlators of
depth 1 (which are expressed by Kronecker-Eisenstein series). However, this functional equation is diﬃcult
to prove. To understand it, we will need to upgrade it to the Hodge-theoretic or motivic setting.
The second shuﬄe relations have a prehistory. The ﬁrst objects known to satisfy a system of ﬁrst and
80
second shuﬄe relations of this form were the multiple polylogarithms (see §1.2.3 and [G3]): these relations
followfromtwoalternativeexpressionsformultiplepolylogarithms: aspowerseriesandasiteratedintegrals.
In Chapter 2, for- = P1, we found second shuﬄe relations for Hodge correlators, in every depth, and
described the lower-depth terms. In depth 2, these relations depend on integers=0,= 1,= 2≥ 0 and points
0,1 ∈ G<\{1}. They state:
CorH(0,..., 0|   {z   }
=0
, 1, 0,..., 0|   {z   }
=1
,0, 0,..., 0|   {z   }
=2
,01)+ CorH(0,..., 0|   {z   }
=0
, 1, 0,..., 0|   {z   }
=2
,1, 0,..., 0|   {z   }
=1
,01)
+lower-depth terms= 0. (3.6)
The highest-depth terms in these relations arise from shuﬄes of the quotients between successive arguments,
G8
G8−1
,togetherwiththe0sbetweenthosearguments. Forexample,in(3.6)wehaveshuﬄed 0 (with=1 0s)with
1 (with=2 0s).
Conjecturally,theﬁrstandsecondshuﬄerelationsgivealllinearrelationsamongtheHodgecorrelatorson
P1. While the ﬁrst shuﬄe relations emerge from the trivalent tree construction – they hold on the level of the
integrandsin(1.4)–theproofofthesecondshuﬄerelationsisdiﬃcult,requiringmotivicorHodge-theoretic
arguments even in depth 2.
Note the similarity between (3.6) and (3.5). In fact, as an elliptic curve degenerates to a nodal projective
line, a variant of the second shuﬄe relation (3.5) specializes to (3.6).
In §3.2.3 (Theorem 3.8) we will prove these relations, as well as their upgrades to the Hodge correlator
coalgebra. Assumingthemotivicformalism,allresultsofthischaptershouldholdinthe ℓ-adicrealizationas
well.
