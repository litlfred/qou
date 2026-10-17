---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-020-freefem-code-for-genus-3
section_title: "FreeFEM++ Code for Genus 3"
section_number: null
pages: 130-144
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 24 sections: Front matter; Introduction; Background"
---
Similarly to Appendix C, here we give the FreeFEM++ codes for particular surfaces of
genus 3. We start with the Klein quartic:
int
n=30;
int
nev =100;
s t r i n g
fnm=" klein_quartic −Eigenvalues−n30−nev100 . txt " ;
// f i l e
name
for
saving
r e a l
cx = 1.031969722;
r e a l
r = 0.254875473;
r e a l
s =0.7770942488589633;
r e a l
x06=s ∗cos (5∗pi / 7 ) ;
r e a l
y06=s ∗s i n (5∗pi / 7 ) ;
r e a l
x03=s ∗cos (2∗pi / 7 ) ;
r e a l
y03=s ∗s i n (2∗pi / 7 ) ;
r e a l
x05=s ∗cos (4∗pi / 7 ) ;
r e a l
y05=s ∗s i n (4∗pi / 7 ) ;
r e a l
x10=s ∗cos (9∗pi / 7 ) ;
r e a l
y10=s ∗s i n (9∗pi / 7 ) ;
r e a l
x07=s ∗cos (6∗pi / 7 ) ;
r e a l
y07=s ∗s i n (6∗pi / 7 ) ;
r e a l
x12=s ∗cos (11∗pi / 7 ) ;
r e a l
y12=s ∗s i n (11∗pi / 7 ) ;
r e a l
x09=s ∗cos (8∗pi / 7 ) ;
r e a l
y09=s ∗s i n (8∗pi / 7 ) ;
r e a l
x14=s ∗cos (13∗pi / 7 ) ;
r e a l
y14=s ∗s i n (13∗pi / 7 ) ;
r e a l
x11=s ∗cos (10∗pi / 7 ) ;
r e a l
y11=s ∗s i n (10∗pi / 7 ) ;
r e a l
x02=s ∗cos ( pi / 7 ) ;
r e a l
y02=s ∗s i n ( pi / 7 ) ;
r e a l
x13=s ∗cos (12∗pi / 7 ) ;
r e a l
y13=s ∗s i n (12∗pi / 7 ) ;
r e a l
x04=s ∗cos (3∗pi / 7 ) ;
r e a l
y04=s ∗s i n (3∗pi / 7 ) ;
border G1 ( t=9∗pi /7 ,5∗pi /7)
{ x=cx+r ∗cos ( t ) ;
y=r ∗s i n ( t ) ; l a b e l =1;};
border G2 ( t=9∗pi /7 ,5∗pi /7)
{ x=cos ( pi /7)∗( cx+r ∗cos ( t ))−s i n ( pi /7)∗( r ∗s i n ( t ) ) ;
y=s i n ( pi /7)∗( cx+r ∗cos ( t ))+ cos ( pi /7)∗( r ∗s i n ( t ) ) ; } l a b e l =2;;
border G3 ( t=9∗pi /7 ,5∗pi /7)
{ x=cos (2∗pi /7)∗( cx+r ∗cos ( t ))−s i n (2∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (2∗pi /7)∗( cx+r ∗cos ( t ))+ cos (2∗pi /7)∗r ∗s i n ( t ) ; } l a b e l =3;;
border G4 ( t=9∗pi /7 ,5∗pi /7)
{ x=cos (3∗pi /7)∗( cx+r ∗cos ( t ))−s i n (3∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (3∗pi /7)∗( cx+r ∗cos ( t ))+ cos (3∗pi /7)∗r ∗s i n ( t ) ; l a b e l =4;};
border G5 ( t=9∗pi /7 ,5∗pi /7)
{ x=cos (4∗pi /7)∗( cx+r ∗cos ( t ))−s i n (4∗pi /7)∗r ∗s i n ( t ) ;
120
y=s i n (4∗pi /7)∗( cx+r ∗cos ( t ))+ cos (4∗pi /7)∗r ∗s i n ( t ) ; l a b e l =5;};
border G6 ( t=9∗pi /7 ,5∗pi /7)
{ x=cos (5∗pi /7)∗( cx+r ∗cos ( t ))−s i n (5∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (5∗pi /7)∗( cx+r ∗cos ( t ))+ cos (5∗pi /7)∗r ∗s i n ( t ) ; l a b e l =6;};
border G7 ( t=9∗pi /7 ,5∗pi /7)
{ x=cos (6∗pi /7)∗( cx+r ∗cos ( t ))−s i n (6∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (6∗pi /7)∗( cx+r ∗cos ( t ))+ cos (6∗pi /7)∗r ∗s i n ( t ) ; l a b e l =7;};
border G8 ( t=9∗pi /7 ,5∗pi /7)
{ x=cos (7∗pi /7)∗( cx+r ∗cos ( t ))−s i n (7∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (7∗pi /7)∗( cx+r ∗cos ( t ))+ cos (7∗pi /7)∗r ∗s i n ( t ) ; l a b e l =8;};
border G9 ( t=9∗pi /7 ,5∗pi /7)
{ x=cos (8∗pi /7)∗( cx+r ∗cos ( t ))−s i n (8∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (8∗pi /7)∗( cx+r ∗cos ( t ))+ cos (8∗pi /7)∗r ∗s i n ( t ) ; l a b e l =9;};
border
G10
( t=9∗pi /7 ,5∗pi /7)
{ x=cos (9∗pi /7)∗( cx+r ∗cos ( t ))−s i n (9∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (9∗pi /7)∗( cx+r ∗cos ( t ))+ cos (9∗pi /7)∗r ∗s i n ( t ) ; l a b e l =10;};
border
G11
( t=9∗pi /7 ,5∗pi /7)
{ x=cos (10∗pi /7)∗( cx+r ∗cos ( t ))−s i n (10∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (10∗pi /7)∗( cx+r ∗cos ( t ))+ cos (10∗pi /7)∗r ∗s i n ( t ) ; l a b e l =11;};
border
G12
( t=9∗pi /7 ,5∗pi /7)
{ x=cos (11∗pi /7)∗( cx+r ∗cos ( t ))−s i n (11∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (11∗pi /7)∗( cx+r ∗cos ( t ))+ cos (11∗pi /7)∗r ∗s i n ( t ) ; l a b e l =12;};
border
G13
( t=9∗pi /7 ,5∗pi /7)
{ x=cos (12∗pi /7)∗( cx+r ∗cos ( t ))−s i n (12∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (12∗pi /7)∗( cx+r ∗cos ( t ))+ cos (12∗pi /7)∗r ∗s i n ( t ) ; l a b e l =13;};
border
G14
( t=9∗pi /7 ,5∗pi /7)
{ x=cos (13∗pi /7)∗( cx+r ∗cos ( t ))−s i n (13∗pi /7)∗r ∗s i n ( t ) ;
y=s i n (13∗pi /7)∗( cx+r ∗cos ( t ))+ cos (13∗pi /7)∗r ∗s i n ( t ) ; l a b e l =14;};
p l o t (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n)+G13(n)
+G14(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n)+G13(n)+G14(n ) , f i x e b o r d e r=true ) ;
p l o t (Th, wait=true , f i l l =true ) ;
f e s p a c e
Vh(Th, P2 , p e r i o d i c =[[1 , y ] , [ 6 , ( cos (2∗pi /7))∗( y−y06)−( s i n (−2∗pi /7))∗( x−x06 ) ] ,
[ 3 , ( cos (2∗pi /7))∗( y−y03)−( s i n (2∗pi /7))∗( x−x03 ) ] , [ 8 , y ] ,
[ 5 , ( cos (4∗pi /7))∗( y−y05)−( s i n (4∗pi /7))∗( x−x05 ) ] ,
[ 1 0 , ( cos (2∗pi /7))∗( y−y10)−( s i n (2∗pi /7))∗( x−x10 ) ] ,
[ 7 , ( cos (6∗pi /7))∗( y−y07)−( s i n (6∗pi /7))∗( x−x07 ) ] ,
[ 1 2 , ( cos (4∗pi /7))∗( y−y12)−( s i n (4∗pi /7))∗( x−x12 ) ] ,
[ 9 , ( cos (6∗pi /7))∗( y−y09)−( s i n (−6∗pi /7))∗( x−x09 ) ] ,
[ 1 4 , ( cos (6∗pi /7))∗( y−y14)−( s i n (6∗pi /7))∗( x−x14 ) ] ,
[ 1 1 , ( cos (4∗pi /7))∗( y−y11)−( s i n (−4∗pi /7))∗( x−x11 ) ] ,
[ 2 , ( cos (6∗pi /7))∗( y−y02)−( s i n (−6∗pi /7))∗( x−x02 ) ] ,
[ 1 3 , ( cos (2∗pi /7))∗( y−y13)−( s i n (−2∗pi /7))∗( x−x13 ) ] ,
[ 4 , ( cos (4∗pi /7))∗( y−y04)−( s i n (−4∗pi /7))∗( x−x04 ) ] ] ) ;
Vh u1 ,
u2 ;
r e a l
sigma = 0 . 0 0 0 0 1 ;
v a r f
op ( u1 , u2)=
int2d (Th) ( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma ∗(4∗u1∗u2)/(1−x^2−y ^2)^2);
v a r f
b ( [ u1 ] , [ u2 ] ) = int2d (Th) ( ( 4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh, Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh, Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
Vh[ int ]
eV( nev ) ;
int
k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l =1e −10, maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
u1=eV [ i ] ;
r e a l
gg = int2d (Th) ( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream
Eva(fnm ,
append ) ;
Eva <<
ev [ i ] << "\n" ;
}
Of relevance to the Klein quartic (and indeed to Hurwitz surfaces in other genera) is
the (2, 3, 7) triangle. We include the code for its spectrum; as with the (2, 3, 8) triangle
121
and the pentagon in Appendix C, it is possible to add a Dirichlet condition to one or
more of its sides.
int
n = 30;
int
nev =100;
s t r i n g
fnm="237−Eigenvalues−n30−nev100 . txt " ;
// f i l e
name
for
saving
r e a l
c = 2.012192172612278;
r e a l
r = 1.74611492735219;
border G1 ( t =0 ,0.2660772452600879)
{ x=t ;
y =0;};
border G2 ( t =0.3007426187463789 ,0)
{ x=cos ( pi /7)∗t ;
y=t ∗s i n ( pi / 7 ) ; } ;
border G3 ( t=pi ,3.066792828504322)
{ x=c+r ∗cos ( t ) ;
y=r ∗s i n ( t ) ; } ;
p l o t (G1(n)+G2(n)+G3(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n ) ) ;
p l o t (Th ) ;
f e s p a c e
Vh(Th, P2 ) ;
Vh u1 ,
u2 ;
r e a l
sigma = 0 . 0 0 0 5 ;
v a r f
op ( u1 , u2)=
int2d (Th) ( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma ∗(4∗u1∗u2)/(1−x^2−y ^2)^2);
v a r f
b ( [ u1 ] , [ u2 ] ) = int2d (Th) ( ( 4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh, Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh, Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
Vh[ int ]
eV( nev ) ;
int
k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l =1e −10, maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
u1=eV [ i ] ;
r e a l
gg = int2d (Th) ( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream
Eva(fnm ,
append ) ;
Eva <<
ev [ i ] << "\n" ;
}
Next, we include the code for the surface M3 in [72]:
int
n = 30;
int
nev = 100;
s t r i n g
fnm="m3−Eigenvalues−n30−nev100 . txt " ;
// f i l e
name
for
saving
r e a l
cx = 1 . 0 1 2 2 ;
r e a l
cy = 0 . 1 5 6 6 ;
r e a l
r = 0 . 2 2 1 4 ;
r e a l
s = 0 . 8 0 4 5 ;
r e a l
theta = 0 . 1 2 3 8 ;
r e a l
x01 = s ∗cos ( theta ) ;
r e a l
y01 = s ∗s i n ( theta ) ;
r e a l
x02 = s ∗cos ( pi/6−theta ) ;
r e a l
y02 = s ∗s i n ( pi/6−theta ) ;
r e a l
x03 = s ∗cos ( pi/6+theta ) ;
r e a l
y03 = s ∗s i n ( pi/6+theta ) ;
r e a l
x04 = s ∗cos (2∗pi/6−theta ) ;
r e a l
y04 = s ∗s i n (2∗pi/6−theta ) ;
r e a l
x05 = s ∗cos (2∗pi/6+theta ) ;
122
r e a l
y05 = s ∗s i n (2∗pi/6+theta ) ;
r e a l
x06 = s ∗cos (3∗pi/6−theta ) ;
r e a l
y06 = s ∗s i n (3∗pi/6−theta ) ;
r e a l
x07 = s ∗cos (3∗pi/6+theta ) ;
r e a l
y07 = s ∗s i n (3∗pi/6+theta ) ;
r e a l
x08 = s ∗cos (4∗pi/6−theta ) ;
r e a l
y08 = s ∗s i n (4∗pi/6−theta ) ;
r e a l
x09 = s ∗cos (4∗pi/6+theta ) ;
r e a l
y09 = s ∗s i n (4∗pi/6+theta ) ;
r e a l
x10 = s ∗cos (5∗pi/6−theta ) ;
r e a l
y10 = s ∗s i n (5∗pi/6−theta ) ;
r e a l
x11 = s ∗cos (5∗pi/6+theta ) ;
r e a l
y11 = s ∗s i n (5∗pi/6+theta ) ;
r e a l
x12 = s ∗cos (6∗pi/6−theta ) ;
r e a l
y12 = s ∗s i n (6∗pi/6−theta ) ;
r e a l
x13 = s ∗cos (6∗pi/6+theta ) ;
r e a l
y13 = s ∗s i n (6∗pi/6+theta ) ;
r e a l
x14 = s ∗cos (7∗pi/6−theta ) ;
r e a l
y14 = s ∗s i n (7∗pi/6−theta ) ;
r e a l
x15 = s ∗cos (7∗pi/6+theta ) ;
r e a l
y15 = s ∗s i n (7∗pi/6+theta ) ;
r e a l
x16 = s ∗cos (8∗pi/6−theta ) ;
r e a l
y16 = s ∗s i n (8∗pi/6−theta ) ;
r e a l
x17 = s ∗cos (8∗pi/6+theta ) ;
r e a l
y17 = s ∗s i n (8∗pi/6+theta ) ;
r e a l
x18 = s ∗cos (9∗pi/6−theta ) ;
r e a l
y18 = s ∗s i n (9∗pi/6−theta ) ;
r e a l
x19 = s ∗cos (9∗pi/6+theta ) ;
r e a l
y19 = s ∗s i n (9∗pi/6+theta ) ;
r e a l
x20 = s ∗cos (10∗pi/6−theta ) ;
r e a l
y20 = s ∗s i n (10∗pi/6−theta ) ;
r e a l
x21 = s ∗cos (10∗pi/6+theta ) ;
r e a l
y21 = s ∗s i n (10∗pi/6+theta ) ;
r e a l
x22 = s ∗cos (11∗pi/6−theta ) ;
r e a l
y22 = s ∗s i n (11∗pi/6−theta ) ;
r e a l
x23 = s ∗cos (11∗pi/6+theta ) ;
r e a l
y23 = s ∗s i n (11∗pi/6+theta ) ;
r e a l
x24 = s ∗cos ( theta ) ;
r e a l
y24 = s ∗s i n (−theta ) ;
border G1 ( t=15∗pi /12 ,11∗pi /12)
{ x=cx+r ∗cos ( t ) ;
y=cy+r ∗s i n ( t ) ; } ;
border G2 ( t=11∗pi /12 ,15∗pi /12)
{ x=cos ( pi /6)∗( cx+r ∗cos ( t ))−s i n ( pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n ( pi /6)∗( cx+r ∗cos ( t ))+ cos ( pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G3 ( t=15∗pi /12 ,11∗pi /12)
{ x=cos ( pi /6)∗( cx+r ∗cos ( t ))−s i n ( pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n ( pi /6)∗( cx+r ∗cos ( t ))+ cos ( pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border G4 ( t=11∗pi /12 ,15∗pi /12)
{ x=cos (2∗pi /6)∗( cx+r ∗cos ( t ))−s i n (2∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (2∗pi /6)∗( cx+r ∗cos ( t ))+ cos (2∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G5 ( t=15∗pi /12 ,11∗pi /12)
{ x=cos (2∗pi /6)∗( cx+r ∗cos ( t ))−s i n (2∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (2∗pi /6)∗( cx+r ∗cos ( t ))+ cos (2∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border G6 ( t=11∗pi /12 ,15∗pi /12)
{ x=cos (3∗pi /6)∗( cx+r ∗cos ( t ))−s i n (3∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (3∗pi /6)∗( cx+r ∗cos ( t ))+ cos (3∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G7 ( t=15∗pi /12 ,11∗pi /12)
{ x=cos (3∗pi /6)∗( cx+r ∗cos ( t ))−s i n (3∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (3∗pi /6)∗( cx+r ∗cos ( t ))+ cos (3∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border G8 ( t=11∗pi /12 ,15∗pi /12)
{ x=cos (4∗pi /6)∗( cx+r ∗cos ( t ))−s i n (4∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (4∗pi /6)∗( cx+r ∗cos ( t ))+ cos (4∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G9 ( t=15∗pi /12 ,11∗pi /12)
{ x=cos (4∗pi /6)∗( cx+r ∗cos ( t ))−s i n (4∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (4∗pi /6)∗( cx+r ∗cos ( t ))+ cos (4∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G10
( t=11∗pi /12 ,15∗pi /12)
{ x=cos (5∗pi /6)∗( cx+r ∗cos ( t ))−s i n (5∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (5∗pi /6)∗( cx+r ∗cos ( t ))+ cos (5∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G11
( t=15∗pi /12 ,11∗pi /12)
{ x=cos (5∗pi /6)∗( cx+r ∗cos ( t ))−s i n (5∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (5∗pi /6)∗( cx+r ∗cos ( t ))+ cos (5∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G12
( t=11∗pi /12 ,15∗pi /12)
{ x=cos (6∗pi /6)∗( cx+r ∗cos ( t ))−s i n (6∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (6∗pi /6)∗( cx+r ∗cos ( t ))+ cos (6∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G13
( t=15∗pi /12 ,11∗pi /12)
{ x=cos (6∗pi /6)∗( cx+r ∗cos ( t ))−s i n (6∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
123
y=s i n (6∗pi /6)∗( cx+r ∗cos ( t ))+ cos (6∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G14
( t=11∗pi /12 ,15∗pi /12)
{ x=cos (7∗pi /6)∗( cx+r ∗cos ( t ))−s i n (7∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (7∗pi /6)∗( cx+r ∗cos ( t ))+ cos (7∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G15
( t=15∗pi /12 ,11∗pi /12)
{ x=cos (7∗pi /6)∗( cx+r ∗cos ( t ))−s i n (7∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (7∗pi /6)∗( cx+r ∗cos ( t ))+ cos (7∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G16
( t=11∗pi /12 ,15∗pi /12)
{ x=cos (8∗pi /6)∗( cx+r ∗cos ( t ))−s i n (8∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (8∗pi /6)∗( cx+r ∗cos ( t ))+ cos (8∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G17
( t=15∗pi /12 ,11∗pi /12)
{ x=cos (8∗pi /6)∗( cx+r ∗cos ( t ))−s i n (8∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (8∗pi /6)∗( cx+r ∗cos ( t ))+ cos (8∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G18
( t=11∗pi /12 ,15∗pi /12)
{ x=cos (9∗pi /6)∗( cx+r ∗cos ( t ))−s i n (9∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (9∗pi /6)∗( cx+r ∗cos ( t ))+ cos (9∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G19
( t=15∗pi /12 ,11∗pi /12)
{ x=cos (9∗pi /6)∗( cx+r ∗cos ( t ))−s i n (9∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (9∗pi /6)∗( cx+r ∗cos ( t ))+ cos (9∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G20
( t=11∗pi /12 ,15∗pi /12)
{ x=cos (10∗pi /6)∗( cx+r ∗cos ( t ))−s i n (10∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (10∗pi /6)∗( cx+r ∗cos ( t ))+ cos (10∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G21
( t=15∗pi /12 ,11∗pi /12)
{ x=cos (10∗pi /6)∗( cx+r ∗cos ( t ))−s i n (10∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (10∗pi /6)∗( cx+r ∗cos ( t ))+ cos (10∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G22
( t=11∗pi /12 ,15∗pi /12)
{ x=cos (11∗pi /6)∗( cx+r ∗cos ( t ))−s i n (11∗pi /6)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (11∗pi /6)∗( cx+r ∗cos ( t ))+ cos (11∗pi /6)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G23
( t=15∗pi /12 ,11∗pi /12)
{ x=cos (11∗pi /6)∗( cx+r ∗cos ( t ))−s i n (11∗pi /6)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (11∗pi /6)∗( cx+r ∗cos ( t ))+ cos (11∗pi /6)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G24
( t=11∗pi /12 ,15∗pi /12)
{ x=cx+r ∗cos ( t ) ;
y=−cy−r ∗s i n ( t ) ; } ;
p l o t (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n)+G13(n)
+G14(n)+G15(n)+G16(n)+G17(n)+G18(n)+G19(n)+G20(n)+G21(n)+G22(n)+G23(n)+G24(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n)+G13(n)+G14(n)+G15(n)+G16(n)+G17(n)+G18(n)+G19(n)+G20(n)+G21(n)+G22(n)+G23(n)
+G24(n ) , f i x e b o r d e r=true ) ;
p l o t (Th, wait=true , f i l l =true ) ;
f e s p a c e
Vh(Th, P2 , p e r i o d i c = [ [ 2 , ( cos ( pi /12))∗( y−y02)−( s i n ( pi /12))∗( x−x02 ) ] ,
[ 9 , ( cos (3∗pi /12))∗( y−y09)−( s i n (−3∗pi /12))∗( x−x09 ) ] ,
[ 4 , ( cos (3∗pi /12))∗( y−y04)−( s i n (3∗pi /12))∗( x−x04 ) ] ,
[ 1 1 , ( cos ( pi /12))∗( y−y11)−( s i n (−pi /12))∗( x−x11 ) ] ,
[ 6 , ( cos (5∗pi /12))∗( y−y06)−( s i n (5∗pi /12))∗( x−x06 ) ] ,
[ 1 3 , ( cos ( pi /12))∗( y−y13)−( s i n ( pi /12))∗( x−x13 ) ] ,
[ 8 , ( cos (7∗pi /12))∗( y−y08)−( s i n (7∗pi /12))∗( x−x08 ) ] ,
[ 1 5 , ( cos (3∗pi /12))∗( y−y15)−( s i n (3∗pi /12))∗( x−x15 ) ] ,
[ 1 0 , ( cos (9∗pi /12))∗( y−y10)−( s i n (9∗pi /12))∗( x−x10 ) ] ,
[ 1 7 , ( cos (5∗pi /12))∗( y−y17)−( s i n (5∗pi /12))∗( x−x17 ) ] ,
[ 1 2 , ( cos (11∗pi /12))∗( y−y12)−( s i n (11∗pi /12))∗( x−x12 ) ] ,
[ 1 9 , ( cos (7∗pi /12))∗( y−y19)−( s i n (7∗pi /12))∗( x−x19 ) ] ,
[ 1 4 , ( cos (13∗pi /12))∗( y−y14)−( s i n (13∗pi /12))∗( x−x14 ) ] ,
[ 2 1 , ( cos (9∗pi /12))∗( y−y21)−( s i n (9∗pi /12))∗( x−x21 ) ] ,
[ 1 6 , ( cos (15∗pi /12))∗( y−y16)−( s i n (15∗pi /12))∗( x−x16 ) ] ,
[ 2 3 , ( cos (11∗pi /12))∗( y−y23)−( s i n (11∗pi /12))∗( x−x23 ) ] ,
[ 1 8 , ( cos (17∗pi /12))∗( y−y18)−( s i n (17∗pi /12))∗( x−x18 ) ] ,
[ 1 , ( cos (13∗pi /12))∗( y−y01)−( s i n (13∗pi /12))∗( x−x01 ) ] ,
[ 2 0 , ( cos (19∗pi /12))∗( y−y20)−( s i n (19∗pi /12))∗( x−x20 ) ] ,
[ 3 , ( cos (15∗pi /12))∗( y−y03)−( s i n (15∗pi /12))∗( x−x03 ) ] ,
[ 2 2 , ( cos (21∗pi /12))∗( y−y22)−( s i n (21∗pi /12))∗( x−x22 ) ] ,
[ 5 , ( cos (17∗pi /12))∗( y−y05)−( s i n (17∗pi /12))∗( x−x05 ) ] ,
[ 2 4 , ( cos (23∗pi /12))∗( y−y24)−( s i n (23∗pi /12))∗( x−x24 ) ] ,
[ 7 , ( cos (19∗pi /12))∗( y−y07)−( s i n (19∗pi /12))∗( x−x07 ) ] ] ) ;
Vh u1 ,
u2 ;
r e a l
sigma = 0 . 0 0 0 0 1 ;
v a r f
op ( u1 , u2)=
int2d (Th) ( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma ∗(4∗u1∗u2)/(1−x^2−y ^2)^2);
v a r f
b ( [ u1 ] , [ u2 ] ) = int2d (Th) ( ( 4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh, Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh, Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
124
Vh[ int ]
eV( nev ) ;
int
k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l =1e −10, maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
u1=eV [ i ] ;
r e a l
gg = int2d (Th) ( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream
Eva(fnm ,
append ) ;
Eva <<
ev [ i ] << "\n" ;
}
1
3
5
7
9
11
13
15
17
19
21
23
24
2
4
6
8
10
12
14
16
18
20
22
Side associations:
2 – 9, 4 – 11, 6 – 13, 8 – 15, 10 – 17, 12 – 19,
14 – 21, 16 – 23, 18 – 1, 20 – 3, 22 – 5, 24 – 7
Figure D.1: Fundamental polygon for the surface M3
We also include the code for the Fermat quartic:
int
n=30;
int
nev =100;
s t r i n g
fnm=" fermat_quartic−Eigenvalues−n30−nev100 . txt " ;
// f i l e
name
for
saving
r e a l
cx = 1 . 0 0 4 4 ;
r e a l
cy = 0 . 2 2 7 5 ;
r e a l
r = 0 . 2 4 6 3 ;
r e a l
s =0.7881;
r e a l
theta =0.1698;
r e a l
x01=s ∗cos ( theta ) ;
r e a l
y01=s ∗s i n ( theta ) ;
r e a l
x06=s ∗cos (3∗pi/4−theta ) ;
r e a l
y06=s ∗s i n (3∗pi/4−theta ) ;
125
r e a l
x03=s ∗cos ( pi/4+theta ) ;
r e a l
y03=s ∗s i n ( pi/4+theta ) ;
r e a l
x08=s ∗cos ( pi−theta ) ;
r e a l
y08=s ∗s i n ( pi−theta ) ;
r e a l
x05=s ∗cos ( pi/2+theta ) ;
r e a l
y05=s ∗s i n ( pi/2+theta ) ;
r e a l
x10=s ∗cos (5∗pi/4−theta ) ;
r e a l
y10=s ∗s i n (5∗pi/4−theta ) ;
r e a l
x07=s ∗cos (3∗pi/4+theta ) ;
r e a l
y07=s ∗s i n (3∗pi/4+theta ) ;
r e a l
x12=s ∗cos (6∗pi/4−theta ) ;
r e a l
y12=s ∗s i n (6∗pi/4−theta ) ;
r e a l
x09=s ∗cos ( pi+theta ) ;
r e a l
y09=s ∗s i n ( pi+theta ) ;
r e a l
x14=s ∗cos (7∗pi/4−theta ) ;
r e a l
y14=s ∗s i n (7∗pi/4−theta ) ;
r e a l
x11=s ∗cos (5∗pi/4+theta ) ;
r e a l
y11=s ∗s i n (5∗pi/4+theta ) ;
r e a l
x16=s ∗cos ( theta ) ;
r e a l
y16=s ∗s i n (−theta ) ;
r e a l
x13=s ∗cos (6∗pi/4+theta ) ;
r e a l
y13=s ∗s i n (6∗pi/4+theta ) ;
r e a l
x02=s ∗cos ( pi/4−theta ) ;
r e a l
y02=s ∗s i n ( pi/4−theta ) ;
r e a l
x15=s ∗cos (7∗pi/4+theta ) ;
r e a l
y15=s ∗s i n (7∗pi/4+theta ) ;
r e a l
x04=s ∗cos ( pi/2−theta ) ;
r e a l
y04=s ∗s i n ( pi/2−theta ) ;
border G1 ( t=11∗pi /8 ,7∗pi /8)
{ x=cx+r ∗cos ( t ) ;
y=cy+r ∗s i n ( t ) ; } ;
border G2 ( t=7∗pi /8 ,11∗pi /8)
{ x=cos ( pi /4)∗( cx+r ∗cos ( t ))−s i n ( pi /4)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n ( pi /4)∗( cx+r ∗cos ( t ))+ cos ( pi /4)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G3 ( t=11∗pi /8 ,7∗pi /8)
{ x=cos ( pi /4)∗( cx+r ∗cos ( t ))−s i n ( pi /4)∗( cy+r ∗s i n ( t ) ) ;
y=s i n ( pi /4)∗( cx+r ∗cos ( t ))+ cos ( pi /4)∗( cy+r ∗s i n ( t ) ) ; } ;
border G4 ( t=7∗pi /8 ,11∗pi /8)
{ x=cos ( pi /2)∗( cx+r ∗cos ( t ))−s i n ( pi /2)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n ( pi /2)∗( cx+r ∗cos ( t ))+ cos ( pi /2)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G5 ( t=11∗pi /8 ,7∗pi /8)
{ x=cos ( pi /2)∗( cx+r ∗cos ( t ))−s i n ( pi /2)∗( cy+r ∗s i n ( t ) ) ;
y=s i n ( pi /2)∗( cx+r ∗cos ( t ))+ cos ( pi /2)∗( cy+r ∗s i n ( t ) ) ; } ;
border G6 ( t=7∗pi /8 ,11∗pi /8)
{ x=cos (3∗pi /4)∗( cx+r ∗cos ( t ))−s i n (3∗pi /4)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (3∗pi /4)∗( cx+r ∗cos ( t ))+ cos (3∗pi /4)∗(−cy−r ∗s i n ( t ) ) ; } ;
border G7 ( t=11∗pi /8 ,7∗pi /8)
{ x=cos (3∗pi /4)∗( cx+r ∗cos ( t ))−s i n (3∗pi /4)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (3∗pi /4)∗( cx+r ∗cos ( t ))+ cos (3∗pi /4)∗( cy+r ∗s i n ( t ) ) ; } ;
border G8 ( t=7∗pi /8 ,11∗pi /8)
{ x=cos ( pi )∗( cx+r ∗cos ( t ))−s i n ( pi )∗(−cy−r ∗s i n ( t ) ) ;
y=s i n ( pi )∗( cx+r ∗cos ( t ))+ cos ( pi )∗(−cy−r ∗s i n ( t ) ) ; } ;
border G9 ( t=11∗pi /8 ,7∗pi /8)
{ x=cos ( pi )∗( cx+r ∗cos ( t ))−s i n ( pi )∗( cy+r ∗s i n ( t ) ) ;
y=s i n ( pi )∗( cx+r ∗cos ( t ))+ cos ( pi )∗( cy+r ∗s i n ( t ) ) ; } ;
border
G10
( t=7∗pi /8 ,11∗pi /8)
{ x=cos (5∗pi /4)∗( cx+r ∗cos ( t ))−s i n (5∗pi /4)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (5∗pi /4)∗( cx+r ∗cos ( t ))+ cos (5∗pi /4)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G11
( t=11∗pi /8 ,7∗pi /8)
{ x=cos (5∗pi /4)∗( cx+r ∗cos ( t ))−s i n (5∗pi /4)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (5∗pi /4)∗( cx+r ∗cos ( t ))+ cos (5∗pi /4)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G12
( t=7∗pi /8 ,11∗pi /8)
{ x=cos (6∗pi /4)∗( cx+r ∗cos ( t ))−s i n (6∗pi /4)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (6∗pi /4)∗( cx+r ∗cos ( t ))+ cos (6∗pi /4)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G13
( t=11∗pi /8 ,7∗pi /8)
{ x=cos (6∗pi /4)∗( cx+r ∗cos ( t ))−s i n (6∗pi /4)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (6∗pi /4)∗( cx+r ∗cos ( t ))+ cos (6∗pi /4)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G14
( t=7∗pi /8 ,11∗pi /8)
{ x=cos (7∗pi /4)∗( cx+r ∗cos ( t ))−s i n (7∗pi /4)∗(−cy−r ∗s i n ( t ) ) ;
y=s i n (7∗pi /4)∗( cx+r ∗cos ( t ))+ cos (7∗pi /4)∗(−cy−r ∗s i n ( t ) ) ; } ;
border
G15
( t=11∗pi /8 ,7∗pi /8)
{ x=cos (7∗pi /4)∗( cx+r ∗cos ( t ))−s i n (7∗pi /4)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (7∗pi /4)∗( cx+r ∗cos ( t ))+ cos (7∗pi /4)∗( cy+r ∗s i n ( t ) ) ; } ;
border
G16
( t=7∗pi /8 ,11∗pi /8)
{ x=cx+r ∗cos ( t ) ;
y=−cy−r ∗s i n ( t ) ; } ;
p l o t (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n)+G13(n)
+G14(n)+G15(n)+G16(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n)+G13(n)+G14(n)+G15(n)+G16(n ) , f i x e b o r d e r=true ) ;
126
p l o t (Th, wait=true , f i l l =true ) ;
f e s p a c e
Vh(Th, P2 , p e r i o d i c =[[1 , cos ( pi /8)∗( y−y01)−s i n ( pi /8)∗( x−x01 ) ] ,
[ 6 , cos (3∗pi /8)∗( y−y06)−s i n (−3∗pi /8)∗( x−x06 ) ] ,
[ 3 , cos (3∗pi /8)∗( y−y03)−s i n (3∗pi /8)∗( x−x03 ) ] ,
[ 8 , cos ( pi /8)∗( y−y08)−s i n (−pi /8)∗( x−x08 ) ] ,
[ 5 , cos (5∗pi /8)∗( y−y05)−s i n (5∗pi /8)∗( x−x05 ) ] ,
[ 1 0 , cos ( pi /8)∗( y−y10)−s i n ( pi /8)∗( x−x10 ) ] ,
[ 7 , cos (7∗pi /8)∗( y−y07)−s i n (7∗pi /8)∗( x−x07 ) ] ,
[ 1 2 , cos (3∗pi /8)∗( y−y12)−s i n (3∗pi /8)∗( x−x12 ) ] ,
[ 9 , cos (9∗pi /8)∗( y−y09)−s i n (9∗pi /8)∗( x−x09 ) ] ,
[ 1 4 , cos (5∗pi /8)∗( y−y14)−s i n (5∗pi /8)∗( x−x14 ) ] ,
[ 1 1 , cos (11∗pi /8)∗( y−y11)−s i n (11∗pi /8)∗( x−x11 ) ] ,
[ 1 6 , cos (7∗pi /8)∗( y−y16)−s i n (7∗pi /8)∗( x−x16 ) ] ,
[ 1 3 , cos (13∗pi /8)∗( y−y13)−s i n (13∗pi /8)∗( x−x13 ) ] ,
[ 2 , cos (9∗pi /8)∗( y−y02)−s i n (9∗pi /8)∗( x−x02 ) ] ,
[ 1 5 , cos (15∗pi /8)∗( y−y15)−s i n (15∗pi /8)∗( x−x15 ) ] ,
[ 4 , cos (11∗pi /8)∗( y−y04)−s i n (11∗pi /8)∗( x−x04 ) ] ] ) ;
Vh u1 ,
u2 ;
r e a l
sigma = 0 . 0 0 0 0 1 ;
v a r f
op ( u1 , u2)=
int2d (Th) ( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma ∗(4∗u1∗u2)/(1−x^2−y ^2)^2);
v a r f
b ( [ u1 ] , [ u2 ] ) = int2d (Th) ( ( 4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh, Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh, Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
Vh[ int ]
eV( nev ) ;
int
k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l =1e −10, maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
u1=eV [ i ] ;
r e a l
gg = int2d (Th) ( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream
Eva(fnm ,
append ) ;
Eva <<
ev [ i ] << "\n" ;
}
Remark D.1 The observant reader will recognize λ2 in Table D.3 - it is roughly equal to
the ﬁrst positive eigenvalue of the Bolza surface! Moreover, it appears to have the same
multiplicity. In fact, if one takes the subset of eigenvalues in Table D.3 with multiplicity
1, 2 or 3, one ﬁnds that they match the subset of eigenvalues of Table C.1, and that
the multiplicities are the same. This is no coincidence. Recall the presentation of the
automorphism group given in Chapter 1:

a, b, c | a8 = b3 = c2 = (ab)2 = (a2b2)3 = (a4b2)3 = acac = bcbc = e

,
where a is a rotation of order 8 around the centre of the fundamental 16-gon, b is a
rotation of order 3 around one of the 32 (4, 4, 4) triangles that can be used to tessellate
the surface (note this is twice as many as in the case of the Bolza surface), and c is a
reﬂection in the real line. As we have done with the Bolza surface and Klein quartic, we
can input this presentation into GAP to get information about the structure of the group
127
1
3
5
7
9
11
13
15
16
2
4
6
8
10
12
14
Side associations:
1 – 6, 3 – 8, 5 – 10, 7 – 12,
9 – 14, 11 – 16, 13 – 2, 15 – 4
Figure D.2: Fundamental polygon for the Fermat quartic
and information about its representation theory. The code below indicates that the full
automorphism group is isomorphic to (((Z4 × Z4) ⋊Z3) ⋊Z2) ⋊Z2.
gap> g:=FreeGroup ( 3 ) ;
<f r e e
group on the
generators
[
f1 ,
f2 ,
f3
]>
gap> f :=g / [ g .1^8 , g .2^3 , g .3^2 ,( g .1∗g .2)^2 ,( g .1^2∗g .2^2)^3 ,( g .1^4∗g .2^2)^3 ,
g .1∗g .3∗g .1∗g . 3 , g .2∗g .3∗g .2∗g . 3 ] ;
<fp
group on the
generators
[
f1 ,
f2 ,
f3
]>
gap> Order ( f ) ;
192
gap> StructureDescription ( f ) ;
" ( ( ( C4xC4 ) : C3 ) : C2 ) : C2"
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
gap> Display ( CharacterTable ( f ) ) ;
CT1
2
6
4
4
1
5
6
4
3
4
3
4
5
1
4
3
1
.
.
1
.
.
1
.
.
.
.
.
1
.
1a 2a 2b 3a 4a 2c 2d 8a 4b 8b 4c 4d 6a 2e
2P 1a 1a 1a 3a 2c 1a 1a 4d 2c 4a 2c 2c 3a 1a
3P 1a 2a 2b 1a 4a 2c 2d 8a 4b 8b 4c 4d 2d 2e
5P 1a 2a 2b 3a 4a 2c 2d 8a 4b 8b 4c 4d 6a 2e
128
7P 1a 2a 2b 3a 4a 2c 2d 8a 4b 8b 4c 4d 6a 2e
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
1 −1 −1 −1 −1
1
1
1
X. 3
1 −1
1
1
1
1 −1 −1 −1
1
1
1 −1 −1
X. 4
1
1 −1
1
1
1 −1
1
1 −1 −1
1 −1 −1
X. 5
2
.
. −1
2
2 −2
.
.
.
.
2
1 −2
X. 6
2
.
. −1
2
2
2
.
.
.
.
2 −1
2
X. 7
3 −1 −1
. −1
3
3
1 −1
1 −1 −1
. −1
X. 8
3 −1
1
. −1
3 −3
1 −1 −1
1 −1
.
1
X. 9
3
1 −1
. −1
3 −3 −1
1
1 −1 −1
.
1
X.10
3
1
1
. −1
3
3 −1
1 −1
1 −1
. −1
X.11
6 −2
.
.
2 −2
.
.
2
.
. −2
.
.
X.12
6
. −2
. −2 −2
.
.
.
.
2
2
.
.
X.13
6
.
2
. −2 −2
.
.
.
. −2
2
.
.
X.14
6
2
.
.
2 −2
.
. −2
.
. −2
.
.
gap> chi := I r r ( f ) ; ;
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 1 ] ) ;
[
f1 ,
f2 ,
f3
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
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 2 ] ) ;
[
f1 ,
f2 ,
f3
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
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 3 ] ) ;
[
f1 ,
f2 ,
f3
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
[
1
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 4 ] ) ;
[
f1 ,
f2 ,
f3
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
[ −1 ]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 5 ] ) ;
[
f1 ,
f2 ,
f3
] −> [
[
[
0 , −1 ] ,
[
−1, 0
]
] ,
[
[ E(3)^2 ,
0
] ,
[
0 , E(3)
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
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 6 ] ) ;
[
f1 ,
f2 ,
f3
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
[ E(3)^2 ,
0
] ,
[
0 , E(3)
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
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 7 ] ) ;
[
f1 ,
f2 ,
f3
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
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0
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
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 8 ] ) ;
[
f1 ,
f2 ,
f3
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
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0
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
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 9 ] ) ;
[
f1 ,
f2 ,
f3
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
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0
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
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 1 0 ] ) ;
[
f1 ,
f2 ,
f3
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
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0
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
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 1 1 ] ) ;
[
f1 ,
f2 ,
f3
] −>
[
[
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[ E(4) ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 , E(4 ) ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 , −E(4) ,
0
] ,
[
0 ,
0 ,
0 ,
1 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 , −E(4)
]
] ,
[
[
0 ,
0 ,
1 ,
0 ,
0 ,
0
] ,
[
−1, 0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
−1, 0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
−1, 0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 , −1 ] ,
[
0 ,
0 ,
0 ,
1 ,
0 ,
0
]
] ,
129
[
[
0 ,
0 ,
0 ,
1 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
1 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
1 ,
0 ,
0 ,
0
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 1 2 ] ) ;
[
f1 ,
f2 ,
f3
] −>
[
[
[
0 ,
0 ,
0 ,
1 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
1 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 ,
1
] ,
[ −E(4) ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 , E(4) ,
0 ,
0 ,
0
]
] ,
[
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
1 ,
0 ,
0 ,
0
] ,
[
1 ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 , −E(4)
] ,
[
0 ,
0 ,
0 , E( 4) ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
1 ,
0
]
] ,
[
[
0 ,
0 ,
−1, 0 ,
0 ,
0
] ,
[
0 ,
−1, 0 ,
0 ,
0 ,
0
] ,
[
−1, 0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 , E(4)
] ,
[
0 ,
0 ,
0 ,
0 ,
−1, 0
] ,
[
0 ,
0 ,
0 , −E(4) ,
0 ,
0
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 1 3 ] ) ;
[
f1 ,
f2 ,
f3
] −>
[
[
[
0 ,
0 ,
0 ,
1 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
1 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 ,
1
] ,
[ −E(4) ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 , E(4) ,
0 ,
0 ,
0
]
] ,
[
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
1 ,
0 ,
0 ,
0
] ,
[
1 ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 , −E(4)
] ,
[
0 ,
0 ,
0 , E( 4) ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
1 ,
0
]
] ,
[
[
0 ,
0 ,
1 ,
0 ,
0 ,
0
] ,
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[
1 ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 , −E(4)
] ,
[
0 ,
0 ,
0 ,
0 ,
1 ,
0
] ,
[
0 ,
0 ,
0 , E( 4) ,
0 ,
0
]
]
]
gap> I r r e d u c i b l e A f f o r d i n g R e p r e s e n t a t i o n ( chi [ 1 4 ] ) ;
[
f1 ,
f2 ,
f3
] −>
[
[
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[ E(4) ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 , −E(4) ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 , −E(4) ,
0
] ,
[
0 ,
0 ,
0 ,
1 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 , E(4)
]
] ,
[
[
0 ,
0 ,
1 ,
0 ,
0 ,
0
] ,
[
1 ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
1 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 ,
1
] ,
[
0 ,
0 ,
0 ,
1 ,
0 ,
0
]
] ,
[
[
0 ,
0 ,
0 ,
1 ,
0 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
1 ,
0
] ,
[
0 ,
0 ,
0 ,
0 ,
0 ,
1
] ,
[
1 ,
0 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
1 ,
0 ,
0 ,
0 ,
0
] ,
[
0 ,
0 ,
1 ,
0 ,
0 ,
0
]
]
]
130
Eigenvalue
Numerical multiplicity
2.6767
8
6.61848
7
10.8637
6
12.1775
8
17.2397
7
21.9563
7
24.0649
8
25.9085
6
30.7817
6
36.4369
8
37.4073
8
41.4847
6
44.8658
8
49.0165
6
50.6025
6
57.7794
8
57.8082
7
61.9464
7
67.7629
8
69.9676
6
71.0138
8
75.6357
6
81.8839
6
82.6094
7
89.4299
7
90.5087
8
92.7509
8
96.8869
6
Table D.1: First positive eigenvalues of the Klein Quartic
131
Eigenvalue
Numerical multiplicity
2.45206
4
2.8381
3
4.35754
3
7.61965
4
8.45728
1
10.126
4
10.1635
3
11.76
3
14.1724
4
14.2628
2
17.6818
2
18.812
1
19.2547
3
21.2083
4
22.827
4
24.166
3
24.1744
4
26.9546
3
28.0159
1
28.3388
3
30.7729
4
35.8649
3
37.1106
3
37.3413
4
37.976
4
38.6914
3
38.9579
2
42.7433
3
44.0167
4
44.6724
4
46.6306
2
49.448
4
Table D.2: First positive eigenvalues of the surface M3
132
Eigenvalue
Numerical multiplicity
2.4877
6
3.83889
3
7.16032
6
8.24958
2
11.4272
6
13.3096
6
15.049
3
18.6587
3
19.3559
6
23.0736
1
24.7216
6
27.0788
6
27.5915
6
28.0796
3
32.6738
1
36.1647
6
36.2386
2
38.8039
6
40.1168
3
44.0176
3
44.412
6
45.5628
6
Table D.3: First positive eigenvalues of the Fermat quartic
133
Appendix E
