---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-022-freefem-code-for-genus-4
section_title: "FreeFEM++ Code for Genus 4"
section_number: null
pages: 144-150
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
Figure E.1: Fundamental polygon for Bring’s surface
The most symmetric surface of genus 4 is Bring’s surface (also referred to as Bring’s
curve) [71].
It can be obtained by associating the sides of a hyperbolic icosagon of
area 12π, as shown in Figure E.1. Similarly to the Bolza surface and Klein quartic, we
conjecture that because it has maximal symmetry among hyperbolic surfaces of genus 4,
it also maximizes the ﬁrst positive eigenvalue of the Laplace-Beltrami operator among
surfaces of this class. In this appendix, we provide a ﬁnite element code for computing the
ﬁrst 100 eigenvalues of Bring’s surface, along with the output, shown in Table E.1, which
134
list-the-vigenvalues and their predicted multiplicities based on the numerical results.
The FreeFEM-++ code follows the same style as that in earlier appendices; please refer
to Appendix C for comments on how to interpret it.

The fundamental polygon for Bring’s surface can be tessellated by 240 (2, 4, 5) tri-
angles. The group action naps between the triangles in this tessellation
give the 240 symmetries of Bring’s surface. Note that this means Bring’s surface is not a
Hurwitz surface (recall Theorem 1.30), and that there does not exist a Hurwitz surface

of genus 4. The generators of the group satisfy the following relations
(r, 8, t|r? = 8° =? =rtrt = stst = (rs) = (sr’sr*)? =e),

where r is rotation of order 5 about the center o the fundamental icosagon, s is rotation
of order 2 about a vertex where 4 triangles meet in the tessellation by (2, 4, 5) triangles,
and ¢ is a reflection in the real line (see [71] for more details on this group). The final
piece of code in this appendix shows analysis of this finitely presented group in GAP. In

particular, we see that it is isomorphic to S; x Ze, and show its character table.

int n = 30;

int nev = 100;

string fm="brings—surface—Higenvalues—n30—nev100.txt"; //file name for saving
real cx = 1.00156;

real cy = 0.17178;

real r = 0.180621;

real s = 0.837843;

real = 0.138855;
real = sxcos(theta);
real y sxsin(theta);
real sxcos(pi/5—theta);
real y sxsin(p );
real sxcos(p );
real y sxsin ( ;
real s*cos ( );
real y sxsin ( );
real sxcos(2*pi/5+theta);
real y sxsin (2*pi/5+theta);
real sxcos (‘ );
real y sxsin(; );
real excou(S+pi/st thats);
real y sxsin (3 pi/5 );
real sxcos(4* pi );
real y sxsin (4% pi );
real sxcos(4*pi/5+theta);
real y sxsin (4% pi );
real sxcos(5*pi );
real y sxsin(5*pi );
real sxcos(5*pi/5+theta);
real y sxsin(5*pi );
real = sxcos(6*pi );
real y sxsin(6*pi/5—theta);
real sxcos(6*pi/5+theta);
real y sxsin (6% pi/ );
real sxcos(7*pi );
( )

real 3 s*sin(7*pi/5
r e a l
x15 = s ∗cos (7∗pi/5+theta ) ;
r e a l
y15 = s ∗s i n (7∗pi/5+theta ) ;
r e a l
x16 = s ∗cos (8∗pi/5−theta ) ;
r e a l
y16 = s ∗s i n (8∗pi/5−theta ) ;
r e a l
x17 = s ∗cos (8∗pi/5+theta ) ;
r e a l
y17 = s ∗s i n (8∗pi/5+theta ) ;
r e a l
x18 = s ∗cos (9∗pi/5−theta ) ;
r e a l
y18 = s ∗s i n (9∗pi/5−theta ) ;
r e a l
x19 = s ∗cos (9∗pi/5+theta ) ;
r e a l
y19 = s ∗s i n (9∗pi/5+theta ) ;
r e a l
x20 = s ∗cos ( theta ) ;
r e a l
y20 = s ∗s i n (−theta ) ;
border G1 ( t=7∗pi /5 ,4∗pi /5)
{ x=cx+r ∗cos ( t ) ;
y=cy+r ∗s i n ( t ) ; } ;
border G2 ( t=4∗pi /5 ,7∗pi /5)
{ x=cos ( pi /5)∗( cx+r ∗cos ( t ))−s i n ( pi /5)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n ( pi /5)∗( cx+r ∗cos ( t ))+ cos ( pi /5)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G3 ( t=7∗pi /5 ,4∗pi /5)
{ x=cos ( pi /5)∗( cx+r ∗cos ( t ))−s i n ( pi /5)∗( cy+r ∗s i n ( t ) ) ;
y=s i n ( pi /5)∗( cx+r ∗cos ( t ))+ cos ( pi /5)∗( cy+r ∗s i n ( t ) ) ; } ;
border G4 ( t=4∗pi /5 ,7∗pi /5)
{ x=cos (2∗pi /5)∗( cx+r ∗cos ( t ))−s i n (2∗pi /5)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (2∗pi /5)∗( cx+r ∗cos ( t ))+ cos (2∗pi /5)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G5 ( t=7∗pi /5 ,4∗pi /5)
{ x=cos (2∗pi /5)∗( cx+r ∗cos ( t ))−s i n (2∗pi /5)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (2∗pi /5)∗( cx+r ∗cos ( t ))+ cos (2∗pi /5)∗( cy+r ∗s i n ( t ) ) ; } ;
border G6 ( t=4∗pi /5 ,7∗pi /5)
{ x=cos (3∗pi /5)∗( cx+r ∗cos ( t ))−s i n (3∗pi /5)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (3∗pi /5)∗( cx+r ∗cos ( t ))+ cos (3∗pi /5)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G7 ( t=7∗pi /5 ,4∗pi /5)
{ x=cos (3∗pi /5)∗( cx+r ∗cos ( t ))−s i n (3∗pi /5)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (3∗pi /5)∗( cx+r ∗cos ( t ))+ cos (3∗pi /5)∗( cy+r ∗s i n ( t ) ) ; } ;
border G8 ( t=4∗pi /5 ,7∗pi /5)
{ x=cos (4∗pi /5)∗( cx+r ∗cos ( t ))−s i n (4∗pi /5)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (4∗pi /5)∗( cx+r ∗cos ( t ))+ cos (4∗pi /5)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G9 ( t=7∗pi /5 ,4∗pi /5)
{ x=cos (4∗pi /5)∗( cx+r ∗cos ( t ))−s i n (4∗pi /5)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (4∗pi /5)∗( cx+r ∗cos ( t ))+ cos (4∗pi /5)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G10
( t=4∗pi /5 ,7∗pi /5)
{ x=cos ( pi )∗( cx+r ∗cos ( t ))−s i n ( pi )∗(−cy−r ∗s i n ( t ) ) ;
y=s i n ( pi )∗( cx+r ∗cos ( t ))+ cos ( pi )∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G11
( t=7∗pi /5 ,4∗pi /5)
{ x=cos ( pi )∗( cx+r ∗cos ( t ))−s i n ( pi )∗( cy+r ∗s i n ( t ) ) ;
y=s i n ( pi )∗( cx+r ∗cos ( t ))+ cos ( pi )∗( cy+r ∗s i n ( t ) ) ; } ;
border
G12
( t=4∗pi /5 ,7∗pi /5)
{ x=cos (6∗pi /5)∗( cx+r ∗cos ( t ))−s i n (6∗pi /5)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (6∗pi /5)∗( cx+r ∗cos ( t ))+ cos (6∗pi /5)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G13
( t=7∗pi /5 ,4∗pi /5)
{ x=cos (6∗pi /5)∗( cx+r ∗cos ( t ))−s i n (6∗pi /5)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (6∗pi /5)∗( cx+r ∗cos ( t ))+ cos (6∗pi /5)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G14
( t=4∗pi /5 ,7∗pi /5)
{ x=cos (7∗pi /5)∗( cx+r ∗cos ( t ))−s i n (7∗pi /5)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (7∗pi /5)∗( cx+r ∗cos ( t ))+ cos (7∗pi /5)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G15
( t=7∗pi /5 ,4∗pi /5)
{ x=cos (7∗pi /5)∗( cx+r ∗cos ( t ))−s i n (7∗pi /5)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (7∗pi /5)∗( cx+r ∗cos ( t ))+ cos (7∗pi /5)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G16
( t=4∗pi /5 ,7∗pi /5)
{ x=cos (8∗pi /5)∗( cx+r ∗cos ( t ))−s i n (8∗pi /5)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (8∗pi /5)∗( cx+r ∗cos ( t ))+ cos (8∗pi /5)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G17
( t=7∗pi /5 ,4∗pi /5)
{ x=cos (8∗pi /5)∗( cx+r ∗cos ( t ))−s i n (8∗pi /5)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (8∗pi /5)∗( cx+r ∗cos ( t ))+ cos (8∗pi /5)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G18
( t=4∗pi /5 ,7∗pi /5)
{ x=cos (9∗pi /5)∗( cx+r ∗cos ( t ))−s i n (9∗pi /5)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (9∗pi /5)∗( cx+r ∗cos ( t ))+ cos (9∗pi /5)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G19
( t=7∗pi /5 ,4∗pi /5)
{ x=cos (9∗pi /5)∗( cx+r ∗cos ( t ))−s i n (9∗pi /5)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (9∗pi /5)∗( cx+r ∗cos ( t ))+ cos (9∗pi /5)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G20
( t=4∗pi /5 ,7∗pi /5)
{ x=cx+r ∗cos ( t ) ;
y=−cy−r ∗s i n ( t ) ; } ;
p l o t (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n)+G13(n)
+G14(n)+G15(n)+G16(n)+G17(n)+G18(n)+G19(n)+G20(n ) ) ; mesh
Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n)
+G13(n)+G14(n)+G15(n)+G16(n)+G17(n)+G18(n)+G19(n)+G20(n ) , f i x e b o r d e r=true ) ;
p l o t (Th, wait=true , f i l l =true ) ;
f e s p a c e
Vh(Th, P2 , p e r i o d i c = [ [ 1 , ( cos ( pi /10))∗( y−y01)−( s i n ( pi /10))∗( x−x01 ) ] ,
[ 1 4 , ( cos (3∗pi /10))∗( y−y14)−( s i n (3∗pi /10))∗( x−x14 ) ] ,
[ 3 , ( cos (3∗pi /10))∗( y−y03)−( s i n (3∗pi /10))∗( x−x03 ) ] ,
[ 1 2 , ( cos ( pi /10))∗( y−y12)−( s i n ( pi /10))∗( x−x12 ) ] ,
[ 5 , ( cos (5∗pi /10))∗( y−y05)−( s i n (5∗pi /10))∗( x−x05 ) ] ,
[ 1 8 , ( cos (7∗pi /10))∗( y−y18)−( s i n (7∗pi /10))∗( x−x18 ) ] ,
136
[7 ,(cos(7* pi/10))*(y—y07)—(sin (7* pi /10))*(x—x07)],
[16 , (cos (5* pi/10)) *(y—y16)—(sin (5* pi /10))*(x—x16)],
[9 ,(cos(9* pi /10))*(y—y09)—(sin (9% pi/10))*(x—-x09)],

[2 ,(cos(11* pi /10)) *(y—y02)—(sin (11* pi/10))*(x-x02)],
[11 (cos (11* pi /10))*(y-y11)—(sin (11* pi/10))*(x-x11)],
[20 , (cos (9* pi /10))*(y—y20)—(sin (9* pi /10))*(x—x20)],
[13 ,(cos (13% pi /10))*(y—y13) —(sin (13 pi /10))*(x—-x13)],
[6 , (cos (15* pi/10)) *(y—y06)—(sin (15% pi/10))*(x-x06)],
[15 ,(cos (15% pi /10))*(y—y15)—(sin (15* pi/10))*(x—-x15)],
[4 (cos (13* pi/10)) *(y—y04)—(sin (13% pi/10))*(x-x04)],
[17 (cos (17* pi /10))*(y-y17) —(sin (17* pi /10))*(x-x17)],
[10 ,(cos(19* pi /10))*(y—y10) —(sin (19* pi /10))*(x-x10)] ,
[19 ,(cos(19* pi /10))*(y—y19) —(sin (19% pi /10))*(x-x19)] ,
[8 , (cos (17* pi /10)) *(y—y08)—(sin (17* pi/10)) *(x-x08 )]]);

Vh ul, u2;
real sigma = 0.00001;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma* ulxu2);
varf b([ul] ,[u2]) = int2d(Th)((4*ul*u2) /(1—x*2-y~2)>2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);
matrix B=b(Vh, Vh, solver=CG, eps=le —20);

real[int] ev(nev);
Vh[int] eV(nev);

int k=EigenValue (OP,B,sym=true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int ji<k;it+) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm= int2d(Th)(ul*ul) ;

//cout<<"——— "<< icc <<ev[if<<"err="
//<<int2d (Th)(4/(1—272-y*2)72) << "—— "<<endl; plot(eV[i],cmm="Eigen Vector "ti+" valeur ="
+ ev[i] ,wait=1,value=1);

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

The following_shows the GAP analysis of the symmetry group of Bring’s surface.

Please refer to Appendix A for details on how to interpret this code.

gap> f:=FreeGroup (3);

<free group on the generators [ fl, f2, £3 |>

gap> g:=f/[f.175,f.272,f.3°2,f.1*f.34f.1*f.3,f.2*f.3%f.2*f.3,
(f.1*£.2)°4,(£.2*£.173«f.2«f.172)>2];

<fp group on the generators [| fl, f2, £3 ]>

gap> Order(g);

240
gap> StructureDescription(g);
"C2_x 85"

gap> RequirePackage("repsn");;
gap> Display (CharacterTable(g));
cT1

137
1a 2a 2b 6a 2c 3a 5a 4a 6b 4b 6c 10a 2d 2e
2P 1a 1a 1a 3a 1a 3a 5a 2d 3a 2d 3a
5a 1a 1a
3P 1a 2a 2b 2c 2c 1a 5a 4a 2a 4b 2e 10a 2d 2e
5P 1a 2a 2b 6a 2c 3a 1a 4a 6b 4b 6c
2e 2d 2e
7P 1a 2a 2b 6a 2c 3a 5a 4a 6b 4b 6c 10a 2d 2e
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
1
X. 2
1 −1 −1
1
1
1
1 −1 −1
1 −1
−1
1 −1
X. 3
1 −1
1 −1 −1
1
1 −1 −1 −1
1
1
1
1
X. 4
1
1 −1 −1 −1
1
1
1
1 −1 −1
−1
1 −1
X. 5
4 −2
.
1 −2
1 −1
.
1
.
1
−1
.
4
X. 6
4
2
. −1
2
1 −1
. −1
.
1
−1
.
4
X. 7
4
2
.
1 −2
1 −1
. −1
. −1
1
. −4
X. 8
4 −2
. −1
2
1 −1
.
1
. −1
1
. −4
X. 9
5
1
1
1
1 −1
. −1
1 −1 −1
.
1
5
X.10
5 −1
1 −1 −1 −1
.
1 −1
1 −1
.
1
5
X.11
5 −1 −1
1
1 −1
.
1 −1 −1
1
.
1 −5
X.12
5
1 −1 −1 −1 −1
. −1
1
1
1
.
1 −5
X.13
6
. −2
.
.
.
1
.
.
.
.
1 −2
6
X.14
6
.
2
.
.
.
1
.
.
.
.
−1 −2 −6
gap> ConjugacyClasses ( g ) ;
[ <i d e n t i t y
... >^G,
f1 ^2∗( f1 ^2∗f2 )^2∗f1 ∗f2 ∗f1 ∗f3^G,
f3^G,
f1 ^2∗( f1 ^2∗f2 )^2∗f1 ∗f2 ∗f1^G,
f2^G,
f1 ^3∗( f1 ∗f2 )^2∗f1 ^4^G,
f1^G,
f1 ^2∗( f1 ^2∗f2 )^2∗f1 ∗f2 ∗f3^G,
f2 ∗f1 ^4∗f3^G,
f2 ∗f1^G,
f1 ^3∗( f1 ∗f2 )^2∗f1 ^3∗f3^G,
f1 ^3∗( f1 ∗f2 )^2∗f1 ^2∗f3^G,
f1 ∗( f1 ∗f2 )^2∗f1 ^4^G,
( f1 ∗f2 ∗f1 )^3∗f2 ∗f3^G ]
138
Eigenvalue
Numerical multiplicity
1.91556
6
2.78954
5
5.89883
5
7.3379
5
8.26099
4
8.55338
6
13.2289
6
13.5082
4
15.1462
4
17.0459
6
17.7721
5
19.0882
6
22.5953
4
24.3521
5
24.6075
4
28.0573
6
28.5767
6
29.6861
4
31.4013
5
Table E.1: First positive eigenvalues of Bring’s surface
139
Appendix F
