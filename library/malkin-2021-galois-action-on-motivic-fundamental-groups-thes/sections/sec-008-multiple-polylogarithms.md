---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-008-multiple-polylogarithms
section_title: "Multiple polylogarithms"
section_number: null
pages: 29-34
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
We review the properties of multiple polylogarithms ([G3]).
It is well known that these functions obey a family ofdouble shuﬄe relations, similar to our relations
for the Hodge correlators that we will show in Chapter 2. However, they do not enjoy some of their other
properties. They are multi-valued and do not satisfy dihedral symmetry relations. The shuﬄe relations
between multiple polylogarithms involve products, while for Hodge correlators they are linear.
Deﬁnition and properties
The multiple polylogarithms are deﬁned by
Li=1,...,=A(I1,...,I A)=
Õ
0<:1<···<:A
I:1
1 ...I :A
A
:=1
1 ...: =A
A
, = 1,...,= A > 0. (1.15)
(The depth of this formal expression isA and theweight is F := =1+···+ =A.) These series converge for
|I8| < 1 and have analytic continuations to multivalued functions with singularities onCA. The multivalued
structure is encoded by a smooth variation of mixed Hodge-Tate structures of weightF over a dense open
subset ofCA.
WhenA = 1, the multiple polylogarithms are the classical polylogarithms Li=(I). Their monodromy and
associated mixed Hodge-Tate structures are well understood ([H]).
We can form an algebra! generated overQ by the multiple polylogarithms, ﬁltered by the weight and
the depth. The expression (1.15) yields expansions for products of polylogarithms, which shows that! has a
well-deﬁned multiplication. For example,
Li=1(I1)Li=2(I2)=
(Õ
0<:1
I:1
1
:=1
1
) (Õ
0<:2
I:2
2
:=2
2
)
=
[ Õ
0<:1<:2
+
Õ
0<:2<:1
+
Õ
0<:1=:2
]
I:1
1 I:2
1
:=1
1 :=2
2
= Li=1,=2(I1,I 2)+ Li=2,=1(I2,I 1)+ Li=1+=2(I1I2).
21
Notice that the left side and all terms on the right side have weight=1+=2; however, the left side and the ﬁrst
two terms on the right side have depth 2, while Li=1+=2(I1I2) has depth 1.
The general relation is:
Li=1,...,=A(I1,...,I A)Li=A+1,...,=A+B(IA+1,...,I A+B)
=
Õ
f∈ΣA,B
Li=f−1(1),...,=f−1(A+B)(If−1(1),...,I f−1(A+B))+ lower-depth terms, (1.16)
whereΣA,B ⊂(A+B is the set of(A,B)-shuﬄes.
Expressions(1.16)arecalled ﬁrstshuﬄerelationsformultiplepolylogarithms. Itisconvenienttoexpress
them with generating functions. Let
!(I1,...,I A|C1 :··· :CA
) Õ
=8>0
Li=1,...,=A(I1,...,I A)
AÖ
C=1
C=8−1
8 ;
then
!(I1,...,I A|C1 :··· :CA
)!(IA+1,...,I A+B|CA+1,...,C A+B
) =
=
Õ
f∈ΣA,B
!(If−1(1),...,I f−1(A+B)|Cf−1(1) :··· :Cf−1(A+B)
)+lower-depth terms. (1.17)
To describe the lower-depth terms in the right side of (1.16), we need the notion ofquasishuﬄe. Let
={01 <··· <0 A} and={11 <··· < 1B} be two ordered sets. A quasishuﬄe of and is a sequence
of slots{1,...," } and a placement of each element of∪ in a slot, such that each slot is ﬁlled with one
of: (1) some08∈ , (2) some19∈ , or (3) a pair
{
08,1 9
}
, and such that the sequence of slots containing
the01,...,0 A and the sequence of slots containing the11,...,1 B are ordered left to right. If08 and19 share
a slot, they are said tocollide. If no elements collide, the quasishuﬄe is said to be a shuﬄe.
Let={1,...,A }and={A+ 1,...,A +B}withthenaturalorders. Then,equivalently,thequasishuﬄes
arethesurjectivemaps {1,...,A +B}
f
−→{1,...," f}thatarestrictlyincreasingon 1,...,A andA+1,...,A +B.
An index8∈{1,...,A } collides with an index9∈{A+ 1,...,A +B} wheneverf(8)=f(9). LetΣA,B be the
set of quasishuﬄes.
A quasishuﬄef is a shuﬄe if"f =A+B. We naturally identifyΣA,B with the the subset of shuﬄes in
ΣA,B.
22
We then have:
Li=1,...,=A(I1,...,I A)Li=A+1,...,=A+B(IA+1,...,I A+B)=
=
Õ
f∈~ΣA,B
Li ˜=f−1(1),..., ˜=f−1("f)( ˜If−1(1),..., ˜If−1("f)), (1.18)
where
˜=f−1(8) =
Õ
f(9)=8
=9, ˜If−1(8) =
Ö
f(9)=8
I9.
Such relations are easily proved by interpreting the terms as cells of the simplicial decomposition of the
product of anA-simplex and anB-simplex.
Iterated integrals
The analytic continuation of the multiple polylogarithms has a presentation in terms of iterated integrals. Let

=1,...,=A(I1 :I2 :··· :IA+1)=
„
W
3C
I1−C◦ 3C
C ◦···◦ 3C
C|                      {z                      }
=1
◦···◦ 3C
IA−C◦ 3C
C ◦···◦ 3C
C|                      {z                      }
=A
,
whereW :[0, 1]→ C is a path from 0 toIA+1. Here, for 1-formsl1,...,l A,
„
W
l1◦···◦ lA :=
„
0≤C1≤···≤ CA≤1
<Û
8=1
W∗l8(C8)
is Chen’s iterated path integral ([C]). Then ([G3], Theorem 2.1)
Li=1,...,=A(I1,...,I A)=
=1,...,=A(1 : I1 :I1I2 :··· :I1...I A). (1.19)
Iterated path integrals also satisfy a shuﬄe product formula, whose terms correspond to the top-dimensional
cells of a decomposition of the product of two simplices:
„
W
l1◦···◦ lA
„
W
l<+1◦···◦ l<+==
Õ
f∈Σ<,=
lf−1(1)◦···◦ lf−1(<+=).
23
This gives a diﬀerent kind of shuﬄe relations (second shuﬄe relations) on the iterated integrals
=1,...,=A,
which can also be expressed in terms of generating functions. Let
!′(I1 :··· :IA+1|C1,...,C A
) =
=
Õ
=8>0

=1,...,=A(I1 :··· :IA+1)C=1−1
1 (C1+C2)=2−1... (C1+···+ CA)=A−1, (1.20)
so
!(I1,...,I A|C1 :··· :CA
) =!′(1 : I1 :··· :I1...I A|C1,C 2−C1,...,C A−CA−1
). (1.21)
Then
!′(I1 :··· :IA : 1|C1,...,C A
)!′(IA+1 :··· :IA+B : 1|CA+1,...,C A+B
) =
=
Õ
f∈ΣA,B
!′(If−1(1) :··· :If−1(A+B) : 1|Cf−1(1),...,C f−1(A+B)
). (1.22)
Double shuﬄe relations
Notethesimilaritybetween(1.17)and(1.22). Thereisadualitybetweentherelationswithhomogeneousand
inhomogeneous argumentsI8 andC8. Together, they form systems ofdouble shuﬄe relations.
The combinatorics of such relations are studied by [G3, G5], allowing them to describe a connection
betweenanalgebraofvaluesofthemultiplepolylogarithmsatrootsofunityandthegeometryofsomelocally
symmetric spaces forGL=(Z) (== 2, 3; and recently for== 4 in [G10]).
Relation to Hodge correlators
In depth 1, the Hodge correlators are related to the multiple polylogarithms. We have seen this in weights 1
and 2. In higher weight, deﬁne a single-valued version of the polylogarithm by
L=(I)=
 

Re = odd
Im = even
(=−1Õ
:=0
V: log:|I|·Li=−:(I)
)
(=≥ 2),
whereV:,closerelativesoftheBernoullinumbers,arethecoeﬃcientsoftheTaylorexpansion 2G
42G−1 = ˝V:G:.
Then
CorH(1, 0,..., 0|   {z   }
=−1
,I)=−(2c8)−=
(2=− 2
=− 1
)−1 Õ
0≤:≤=−2
: even
(2=−:− 3
=− 1
) 2:+1
(:+ 1)!L=−:(I) log:|I|. (1.23)
24
ThepreciserelationshipbetweenthemultiplepolylogarithmsandHodgecorrelatorsindepth > 1isunknown.
Remark
A formula relating iterated integrals and Hodge correlators, and a diﬀerent interpretation of the quasishuﬄe
relations (Chapter 2), was very recently found by Rudenko ([R2], §4).
25
Chapter 2
Shuﬄe relations for Hodge and motivic
correlators onP1
The results of this chapter have appeared in [M2].
