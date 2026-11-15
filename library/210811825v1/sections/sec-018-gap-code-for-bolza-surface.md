---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-018-gap-code-for-bolza-surface
section_title: "GAP Code for Bolza Surface"
section_number: null
pages: 111-115
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
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

gap> ConjugacyClasses(g);

[ <identity ...>°G, r 72 t “G, s *G, uG, r “3% s * t “G, r 7~4°G,
r*2e s * + “G, r72* t au°G, rs °G, r*5e t “G, r*s * t «u°G,
r73°G, or 77* t *ux r 7G J

gap> RequirePackage("repsn");

Repsn for Constructing Representations of Finite Groups
Version 3.0.2

Written by
Vahid Dabbaghian

true

gap> StructureDescription(g);
"GL(2,3):C2"

gap> Display (CharacterTable(g));
CT1

la 4a 2a 3a 4b 2b 2c 12a 2d 8a 6a 8b 12b
2P la 2b la 3a 2b la la 6a la 4b 3a 4b 6a
3P la 4a 2a la 4b 2b 2c 4a 2d 8a 2b 8b 4a
5P la 4a 2a 3a 4b 2b 2c 12b 2d 8a 6a 8b 12a
7P la 4a 2a 3a 4b 2b 2c 12b 2d 8a 6a 8b 12a
11P la 4a 2a 3a 4b 2b 2c 12a 2d 8a 6a 8b 12b

X.1 ldiii2i1i21i21 222212 «21

X.2 1-1-1 1 1 2 21 -1-1-1 1 1 «=-1

X.3 2-1 1 2 1 2-1 -1-1 1 1-1 -1

X.4 11-1 21 1 2-1 #2 1-1 1-1 «#21

X.5 2-2 -1 2 2 1-2 -1 1

X.6 22 .-1 2 2 -1 2 .-1 -1

X.7 3-3 -1 -1 3 1.21 .-1

X.8 3-3 1 .-1 3-1 . 1-1. 1

X.9 393-1 .-1 3-1 .-1 1. 1

X.10 3°93 1 .-1 3 1 -1-1 -1

X.11 4 2 —4 . 2

X.12 4 1 .-4 . A. . Al —A

X.13 4 1 .-4 . -A . .-1 . A

A = -E(12)*7+E(12)*11
= Sqrt(3) = r3

gap> IrreducibleRepresentations(g);

Ll teu} >fEttill, fF 1), brid, t bid dd,
if >ftttild, fb -1)), £711, bt) 1d,
if >ftftaAll,tttld. (£4711, ttt),
if >All tfald,tbttldi. (bili),
if >to], 1,0} ], . £0 -1], .-1 0] J,

[0,-1] ], [£0 -1], [1,-1] J 1,
if >fft,0], f-h 1) 1), €'1,0), | -1,-4] 4,
0,1) ), Ef -1,-1], 1,0] 1 1,

[ r,s, t, u] — [[[-1, 0, -1], [1, 0,0], [1, 1, 0] ],
[ [ -1, 0, -1], [ 0, -1,1 ], [ 0, 0, 1] ]
{ [ 0, 1, -1], [ 1, 0, 1], [ 0, 0, 1] ]
[f 4, 1,0], [0 -1,1], [0 -1,0] ] ],
[z,s, t, u] > [[[1, 1, 1 ], [ -1, 0, -1 ], [ -1, -1, 0] ],
[ [ 1, 0, 0 J], [ -1, 0, -1], [ -1, -1, 0 ] J
{ [ 1, 0, 0], [ 0, 0,1], [ 0, 1, 0] J,
[f 4, 1,0], [ -1, -1,-1], [ -1, 0,0] ] J,
[r, s, t, u] — [[[ 0, -1,1 ], [ 1, 1,0], [ 0, 1,0] ]
[ [ -1, 0, 0], [ 0, 0, -1], [ 0, -1, 0 ] J,
{ [ -1, 0, 0], [ 1, 0, 1], [ 1, 1, 0] J,
[f 1, 0,1], [ 0,6, -1], [ 0,1, -1] ] J,
[3r, s, uj] —>t{[[][ 0, -1,0], [ 0, 0, -1], [ -1, 1, -1] ],
[ [ 1, -1,1 ], [ 0, 0, 1], [ 0, 1, 0] ],
{ [ 0, 0, 1], [ 1, -1,1 ], [ 1, 0, 0] ],
[ fa, -1,1], [ 0, -1,1], [ 0, -1,0] J],
[r,s, t, u] >[[ [ 0, 0, -B(12)*7, 0], [ 0, 0, 0, -E(3) |
{ -F(12)*7, E(4), 0, 0], [ -1, -E(3), 0, 0] J,
[ [ 0, 0, 0, -E(12)*7 ], [ 0, 0, -B(3), 0 J,
[ 0, -B(3)*2, 0, 0 ], [ B(12)*11, 0, 0, 0 ] J,
[ | -B(Q2)711, B(12)*7, 0, 0 |, [ B(42)*7, B(12)*11, 0, 0 J,
[ 0, 0, E(12)711, -B(3) |, [ 0, 0, B(3), -E(12)711 ] J,
{ [ E(3), 0, 0, 0], [ -1, E(3)-2, 0, 0], [ 0, 0, B(3), EB(4) J,
[ 0, 0, 0, B(3)*2 ] J J,
[3r, s, t, u ] — [ [ [ 0, -E(3)72, 0, 0 J], [ 1, 0, -B(3)72, 0 ],
[ 0, -1, 0, -E(12)°7 ], [ -E(12)*7, 0, 0, 0 ] J,
[ [ 0, -B(4), 0, E(3) ], [ 0, 0, -H(12)77, 0 ], [ 0, E(12)711, 0, 0 ],
[ E(3)°2, 0, 1, 0] J,
{ [| E(12)711, 0, -E(12)-7, 0 ], [ 0, 0, 0, -1 J,
[ -E(12)°*7, 0, -E(12)711, 0 J], [ 0, -1, 0, 0] ],
{ [ 0, 0, E(3)72, 0 J, [ 0, -B(3)72, 0, -B(4) J,
[ -1, 0, -E(3), 0 ], [ 0, -E(12)-7, 0, 0] J] J,
[3r, s, t, u ] — [ [ [ 0, -E(12)-7, 0, B(3)-2 |, [ 0, 0, E(4), 0 J,
[ 0, 0, 0, 1 ], [ -E(3)*2, 0, E(3), 0 ] J,
{ [ 0, 1, 0, 0], [ 1, 0, 0, 0 ], [ 0, -B(3)-2, 0, B(12)°7 J,
[ -E(12)*7, 0, -H(12)711, 0 J] J,
{[ [ -E(Q42)°7, 0, -B(12)711, 0 ], [ 0, 0, 0, 1 ],
[ -E(12)*11, 0, E(12)°7, 0 ], [ 0, 1, 0, 0] J,
{ [ 1, 0, E(3), 0 ], [ 0, -E(3)-2, 0, -E(4) ], [ 0, 0, E(3)72, 0 J,
[ 0, -B(12)-7, 0, 0] ] J] J
gap> chis:=Irr(g);;
gap> IrreducibleAffordingRepresentation(chis [1]);
ff, 2, 8, MM) ft)i,tf1))1,0l11), 00111)
gap> IrreducibleA ffordingRepresentation (chis [2]);
ff, 2,8, M@1oflr)1¢f411,fla1httt1d)
gap> IrreducibleA ffordingRepresentation (chis [3]);
ff, 2, 8, M@1oflali,¢fili,flalhtttid)
gap> IrreducibleA ffordingRepresentation (chis [4]);
Pf, 2, 8, M@]oflali,tfol),¢f1)ittt1d)
gap> IrreducibleA ffordingRepresentation (chis [5]);
[ fl, f2, £8, f4]—>[[[0,-1], [-1,0]], [[0,1], [1,0] ],
{ [ -1,0], [ 0, -1] J], [ [ B(3)*2, 0], [ 6, B(3) J] J J
gap> IrreducibleA ffordingRepresentation (chis [6]);
[ fl, f, 8, f4]—>[[[0,1], [1,0] ], [101], [1,0] ],

103
{f1,0], [0,1] ], [ [ B(3)°2, 0], [ 0, B(3) 1] 1]
gap> IrreducibleAffordingRepresentation (chis[7]);
[ fl, £2, #3, f4 ] > [ [ [ 0, -1,0], [ 1, 0,0], [ 0, 0, -1] ],
[ [ 0, -1,0], [ -1, 0,0], [ 0, 0, -1] ],
{[ 1, 0,0], [ 0, 1,0], [ 0, 0, -1] ],
[[ 0, 1,0], | 0, 0,1], [ 1, 0,0] ] ]
gap> IrreducibleAffordingRepresentation (chis [8]);
[ fl, £2, #3, f4 ] > [ [ [ 0, 1,0], [ -1, 0,0], [ 0, 0,1] ],

[[ 0, 1,0], [ 1, 0,0], [ 0, 0,1] ],
[[ 1, 0, 0], [ 0, 1, 0], [ 0, 0, -1] ],
[[ 0, 1,0], [ 0, 0,1], [ 1, 0,0] ] ]

gap> IrreducibleAffordingRepresentation (chis [9]);

[ fl, f2, £8, f4 ] > [[[ 0, 1, 0], [ -1, 0, 0], [ 0, 0, 1] ],
[ [ 0, -1,0 ], [ -1, 0, 0 ], [ 0, 0, -1] ],
[ [ -1, 0, 0], [ 0, -1, 0], [ 0, 0,1] ],
[[ 0, 1,0], [ 0, 0,1], [ 1, 0,0] ] ]

gap> IrreducibleAffordingRepresentation(chis [10]);

[ fl, f2, £3, f4 ] > [ [ [ 0, -1, 0], [ 1, 0, 0], [ 0, 0, -1] ],
[[ 0, 1,0], [ 1, 0,0], [ 0, 0,1] ],
[ [ -1, 0, 0], [ 0, -1, 0], [ 0, 0,1] ],
[[ 0, 1,0], [ 0, 0,1], [ 1, 0,0] ] ]

104
Appendix B
