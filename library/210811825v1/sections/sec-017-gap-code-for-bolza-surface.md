---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-017-gap-code-for-bolza-surface
section_title: "GAP Code for Bolza Surface"
section_number: null
pages: 111-115
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 24 sections: Front matter; Introduction; Background"
---
The following output gives details of the isometry group of the Bolza surface, computed
by the computer algebra package GAP [26]. We ﬁrst deﬁne the group as a free group on
the 4 generators introduced in Section 3.1 with the relevant relations. We conﬁrm that
the order of this group is 96, and the “StructureDescription” command tells us that it is
isomorphic to GL2(Z3) ⋊Z2.
Representatives of each conjugacy class of Isom(B) are given by the command “Con-
jugacyClasses”. Each row of the character table tell us the value of one of the characters
on each of the 13 conjugacy classes of the group, where the conjugacy classes are in the
same order as the output of “ConjugacyClasses”. The data at the top of the character
table concerns the various “power maps” of the character table, and is irrelevant to this
work. The interested reader can learn how to interpret this data by consulting the GAP
manual. To interpret the character values on the diﬀerent conjugacy classes, one must
also be aware of the following notation used by GAP:
E(x) := e
2πi
x .
The “IrreducibleAﬀordingRepresentation”s below the ﬁrst set of irreducible represen-
tations give a simpler set of representation matrices that are easier to work with, but
correspond to the same character table. One may see more easily which of these corre-
spond to rotations, and so on. Unfortunately it was not possible to calculate these for
the four dimensional representations, but we make use of them for our analysis of the 2
and 3 dimensional representations in Section 3.4.
gap> f :=FreeGroup ( " r " , " s " , " t " , "u" ) ;
<f r e e
group on the
generators
[
r ,
s ,
t ,
u ]>
gap> g:= f / [ f .1^8 , f .2^2 , f .3^2 , f .4^3 , f .1∗f .2∗f .1∗f . 2 , f .2∗f .3∗f .2∗f . 3 , f .1∗f .3∗f .1^3∗f . 3 ,
f .1^7∗f .4^2∗f .1^7∗f .4^2 , f .4^2∗f .1∗f .4^2∗f .3∗f . 2 , f .4∗f .2∗f .4∗f . 2 ,
f .4∗f .3∗f .4^2∗f .2∗f . 1 ^ 7 ] ;
<fp
group on the
generators
[
r ,
s ,
t ,
u ]>
gap> Order ( g ) ;
101
96
gap> ConjugacyClasses ( g ) ;
[ <i d e n t i t y
... >^G,
r ^2∗t ^G,
s ^G,
u^G,
r ^3∗s ∗
t ^G,
r ^4^G,
r ^2∗s ∗
t ^G,
r ^2∗t
∗u^G,
r
∗s ^G,
r ^5∗t ^G,
r
∗s ∗
t
∗u^G,
r ^3^G,
r ^7∗t
∗u∗
r ^G ]
gap> RequirePackage ( " repsn " ) ;
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Repsn for
Constructing
Representations
of
F i n i t e
Groups
Version
3 . 0 . 2
Written by
Vahid Dabbaghian
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
true
gap> StructureDescription ( g ) ;
"GL( 2 , 3 ) : C2"
gap> Display ( CharacterTable ( g ) ) ;
CT1
2
5
4
3
2
4
5
3
2
4
3
2
3
2
3
1
1
.
1
.
1
.
1
.
.
1
.
1
1a 4a 2a 3a 4b 2b 2c 12a 2d 8a 6a 8b 12b
2P 1a 2b 1a 3a 2b 1a 1a
6a 1a 4b 3a 4b
6a
3P 1a 4a 2a 1a 4b 2b 2c
4a 2d 8a 2b 8b
4a
5P 1a 4a 2a 3a 4b 2b 2c 12b 2d 8a 6a 8b 12a
7P 1a 4a 2a 3a 4b 2b 2c 12b 2d 8a 6a 8b 12a
11P 1a 4a 2a 3a 4b 2b 2c 12a 2d 8a 6a 8b 12b
X. 1
1
1
1
1
1
1
1
1
1
1
1
1
1
X. 2
1 −1 −1
1
1
1
1
−1 −1 −1
1
1
−1
X. 3
1 −1
1
1
1
1 −1
−1 −1
1
1 −1
−1
X. 4
1
1 −1
1
1
1 −1
1
1 −1
1 −1
1
X. 5
2 −2
. −1
2
2
.
1 −2
. −1
.
1
X. 6
2
2
. −1
2
2
.
−1
2
. −1
.
−1
X. 7
3 −3 −1
. −1
3
1
.
1
1
. −1
.
X. 8
3 −3
1
. −1
3 −1
.
1 −1
.
1
.
X. 9
3
3 −1
. −1
3 −1
. −1
1
.
1
.
X.10
3
3
1
. −1
3
1
. −1 −1
. −1
.
X.11
4
.
. −2
. −4
.
.
.
.
2
.
.
X.12
4
.
.
1
. −4
.
A
.
. −1
.
−A
X.13
4
.
.
1
. −4
.
−A
.
. −1
.
A
A = −E(12)^7+E(12)^11
= Sqrt (3) = r3
gap> I r r e d u c i b l e R e p r e s e n t a t i o n s ( g ) ;
[
[
r ,
s ,
t ,
u
] −> [
[
[
1
]
] ,
[
[
1
]
] ,
[
[
1
]
] ,
[
[
1
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
1
]
] ,
[
[ −1 ]
] ,
[
[ −1 ]
] ,
[
[
1
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[ −1 ]
] ,
[
[
1
]
] ,
[
[ −1 ]
] ,
[
[
1
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[ −1 ]
] ,
[
[ −1 ]
] ,
[
[
1
]
] ,
[
[
1
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
0 ,
1
] ,
[
1 ,
0
]
] ,
[
[
0 , −1 ] ,
[
−1, 0
]
] ,
[
[
−1, 0
] ,
[
0 , −1 ]
] ,
[
[
0 , −1 ] ,
[
1 , −1 ]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
1 ,
0
] ,
[
−1, −1 ]
] ,
[
[
1 ,
0
] ,
[
−1, −1 ]
] ,
[
[
1 ,
0
] ,
[
0 ,
1
]
] ,
[
[
−1, −1 ] ,
[
1 ,
0
]
]
] ,
102
[
r ,
s ,
t ,
u
] −> [
[
[
−1, 0 , −1 ] ,
[
1 ,
0 ,
0
] ,
[
1 ,
1 ,
0
]
] ,
[
[
−1, 0 , −1 ] ,
[
0 ,
−1, 1
] ,
[
0 ,
0 ,
1
]
] ,
[
[
0 ,
1 , −1 ] ,
[
1 ,
0 ,
1
] ,
[
0 ,
0 ,
1
]
] ,
[
[
1 ,
1 ,
0
] ,
[
0 ,
−1, 1
] ,
[
0 ,
−1, 0
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
1 ,
1 ,
1
] ,
[
−1, 0 , −1 ] ,
[
−1, −1, 0
]
] ,
[
[
1 ,
0 ,
0
] ,
[
−1, 0 , −1 ] ,
[
−1, −1, 0
]
] ,
[
[
1 ,
0 ,
0
] ,
[
0 ,
0 ,
1
] ,
[
0 ,
1 ,
0
]
] ,
[
[
1 ,
1 ,
0
] ,
[
−1, −1, −1 ] ,
[
−1, 0 ,
0
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
0 ,
−1, 1
] ,
[
1 ,
1 ,
0
] ,
[
0 ,
1 ,
0
]
] ,
[
[
−1, 0 ,
0
] ,
[
0 ,
0 , −1 ] ,
[
0 ,
−1, 0
]
] ,
[
[
−1, 0 ,
0
] ,
[
1 ,
0 ,
1
] ,
[
1 ,
1 ,
0
]
] ,
[
[
1 ,
0 ,
1
] ,
[
0 ,
0 , −1 ] ,
[
0 ,
1 , −1 ]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
0 ,
−1, 0
] ,
[
0 ,
0 , −1 ] ,
[
−1, 1 , −1 ]
] ,
[
[
1 ,
−1, 1
] ,
[
0 ,
0 ,
1
] ,
[
0 ,
1 ,
0
]
] ,
[
[
0 ,
0 ,
1
] ,
[
1 ,
−1, 1
] ,
[
1 ,
0 ,
0
]
] ,
[
[
1 ,
−1, 1
] ,
[
0 ,
−1, 1
] ,
[
0 ,
−1, 0
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
0 ,
0 , −E(12)^7 ,
0
] ,
[
0 ,
0 ,
0 , −E(3)
] ,
[ −E(12)^7 , E(4) ,
0 ,
0
] ,
[
−1, −E(3) ,
0 ,
0
]
] ,
[
[
0 ,
0 ,
0 , −E(12)^7
] ,
[
0 ,
0 , −E(3 ) ,
0
] ,
[
0 , −E(3)^2 ,
0 ,
0
] ,
[ E(12)^11 ,
0 ,
0 ,
0
]
] ,
[
[ −E(12)^11 , E(12)^7 ,
0 ,
0
] ,
[ E(12)^7 , E(12)^11 ,
0 ,
0
] ,
[
0 ,
0 , E(12)^11 , −E(3)
] ,
[
0 ,
0 , E( 3) , −E(12)^11
]
] ,
[
[ E(3) ,
0 ,
0 ,
0
] ,
[
−1, E(3)^2 ,
0 ,
0
] ,
[
0 ,
0 , E(3) , E(4)
] ,
[
0 ,
0 ,
0 , E(3)^2
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
0 , −E(3)^2 ,
0 ,
0
] ,
[
1 ,
0 , −E(3)^2 ,
0
] ,
[
0 ,
−1, 0 , −E(12)^7
] ,
[ −E(12)^7 ,
0 ,
0 ,
0
]
] ,
[
[
0 , −E(4) ,
0 , E(3)
] ,
[
0 ,
0 , −E(12)^7 ,
0
] ,
[
0 , E(12)^11 ,
0 ,
0
] ,
[ E(3)^2 ,
0 ,
1 ,
0
]
] ,
[
[ E(12)^11 ,
0 , −E(12)^7 ,
0
] ,
[
0 ,
0 ,
0 , −1 ] ,
[ −E(12)^7 ,
0 , −E(12)^11 ,
0
] ,
[
0 ,
−1, 0 ,
0
]
] ,
[
[
0 ,
0 , E(3)^2 ,
0
] ,
[
0 , −E(3)^2 ,
0 , −E(4)
] ,
[
−1, 0 , −E(3) ,
0
] ,
[
0 , −E(12)^7 ,
0 ,
0
]
]
] ,
[
r ,
s ,
t ,
u
] −> [
[
[
0 , −E(12)^7 ,
0 , E(3)^2
] ,
[
0 ,
0 , E(4 ) ,
0
] ,
[
0 ,
0 ,
0 ,
1
] ,
[ −E(3)^2 ,
0 , E(3) ,
0
]
] ,
[
[
0 ,
1 ,
0 ,
0
] ,
[
1 ,
0 ,
0 ,
0
] ,
[
0 , −E(3)^2 ,
0 , E(12)^7
] ,
[ −E(12)^7 ,
0 , −E(12)^11 ,
0
]
] ,
[
[ −E(12)^7 ,
0 , −E(12)^11 ,
0
] ,
[
0 ,
0 ,
0 ,
1
] ,
[ −E(12)^11 ,
0 , E(12)^7 ,
0
] ,
[
0 ,
1 ,
0 ,
0
]
] ,
[
[
1 ,
0 , E(3) ,
0
] ,
[
0 , −E(3)^2 ,
0 , −E(4)
] ,
[
0 ,
0 , E(3)^2 ,
0
] ,
[
0 , −E(12)^7 ,
0 ,
0
]
]
]
]
gap> c h i s := I r r ( g ) ; ;
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 1 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[
1
]
] ,
[
[
1
]
] ,
[
[
1
]
] ,
[
[
1
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 2 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[
1
]
] ,
[
[ −1 ]
] ,
[
[ −1 ]
] ,
[
[
1
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 3 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[ −1 ]
] ,
[
[
1
]
] ,
[
[ −1 ]
] ,
[
[
1
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 4 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[ −1 ]
] ,
[
[ −1 ]
] ,
[
[
1
]
] ,
[
[
1
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 5 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[
0 , −1 ] ,
[
−1, 0
]
] ,
[
[
0 ,
1
] ,
[
1 ,
0
]
] ,
[
[
−1, 0
] ,
[
0 , −1 ]
] ,
[
[ E(3)^2 ,
0
] ,
[
0 , E(3)
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 6 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[
0 ,
1
] ,
[
1 ,
0
]
] ,
[
[
0 ,
1
] ,
[
1 ,
0
]
] ,
103
[
[
1 ,
0
] ,
[
0 ,
1
]
] ,
[
[ E(3)^2 ,
0
] ,
[
0 , E(3)
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 7 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[
0 ,
−1, 0
] ,
[
1 ,
0 ,
0
] ,
[
0 ,
0 , −1 ]
] ,
[
[
0 ,
−1, 0
] ,
[
−1, 0 ,
0
] ,
[
0 ,
0 , −1 ]
] ,
[
[
1 ,
0 ,
0
] ,
[
0 ,
1 ,
0
] ,
[
0 ,
0 , −1 ]
] ,
[
[
0 ,
1 ,
0
] ,
[
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 8 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[
0 ,
1 ,
0
] ,
[
−1, 0 ,
0
] ,
[
0 ,
0 ,
1
]
] ,
[
[
0 ,
1 ,
0
] ,
[
1 ,
0 ,
0
] ,
[
0 ,
0 ,
1
]
] ,
[
[
1 ,
0 ,
0
] ,
[
0 ,
1 ,
0
] ,
[
0 ,
0 , −1 ]
] ,
[
[
0 ,
1 ,
0
] ,
[
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 9 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[
0 ,
1 ,
0
] ,
[
−1, 0 ,
0
] ,
[
0 ,
0 ,
1
]
] ,
[
[
0 ,
−1, 0
] ,
[
−1, 0 ,
0
] ,
[
0 ,
0 , −1 ]
] ,
[
[
−1, 0 ,
0
] ,
[
0 ,
−1, 0
] ,
[
0 ,
0 ,
1
]
] ,
[
[
0 ,
1 ,
0
] ,
[
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( c h i s [ 1 0 ] ) ;
[
f1 ,
f2 ,
f3 ,
f4
] −> [
[
[
0 ,
−1, 0
] ,
[
1 ,
0 ,
0
] ,
[
0 ,
0 , −1 ]
] ,
[
[
0 ,
1 ,
0
] ,
[
1 ,
0 ,
0
] ,
[
0 ,
0 ,
1
]
] ,
[
[
−1, 0 ,
0
] ,
[
0 ,
−1, 0
] ,
[
0 ,
0 ,
1
]
] ,
[
[
0 ,
1 ,
0
] ,
[
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0
]
]
]
104
Appendix B
