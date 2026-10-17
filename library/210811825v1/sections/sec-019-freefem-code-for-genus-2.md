---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-019-freefem-code-for-genus-2
section_title: "FreeFEM++ Code for Genus 2"
section_number: null
pages: 118-130
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
---
The following box contains the FreeFEM++ code for the Bolza surface. It contains basic
comments, but for more information about the various solvers and ﬁnite element spaces
available in the software, please consult the manual [32].
int n = 30;
//number
of
modes
int
nev =100; //number
of
eigenvalues
to
be
c a l c u l a t e d
s t r i n g
fnm = "bolza_surface_30n_100nev . txt " ;
// f i l e
name for
saving
r e a l
r = 0.4550898605622276;
// radius
of
c i r c l e
r e a l
c = 1.09868411346781;
// centre
of
c i r c l e
on x−axis
border G1 ( t=5∗pi /4 ,3∗pi /4)
{ x=c+r ∗cos ( t ) ;
y=r ∗s i n ( t ) ; } ;
border G2 ( t=5∗pi /4 ,3∗pi /4)
{ x=cos ( pi /4)∗( c+r ∗cos ( t ))−s i n ( pi /4)∗r ∗s i n ( t ) ;
y=s i n ( pi /4)∗( c+r ∗cos ( t ))+ cos ( pi /4)∗r ∗s i n ( t ) ; } ;
border G3 ( t=5∗pi /4 ,3∗pi /4)
{ x=cos ( pi /2)∗( c+r ∗cos ( t ))−s i n ( pi /2)∗r ∗s i n ( t ) ;
y=s i n ( pi /2)∗( c+r ∗cos ( t ))+ cos ( pi /2)∗r ∗s i n ( t ) ; } ;
border G4 ( t=5∗pi /4 ,3∗pi /4)
{ x=cos (3∗pi /4)∗( c+r ∗cos ( t ))−s i n (3∗pi /4)∗r ∗s i n ( t ) ;
y=s i n (3∗pi /4)∗( c+r ∗cos ( t ))+ cos (3∗pi /4)∗r ∗s i n ( t ) ; } ;
border G5 ( t=5∗pi /4 ,3∗pi /4)
{ x=cos ( pi )∗( c+r ∗cos ( t ))−s i n ( pi )∗r ∗s i n ( t ) ;
y=s i n ( pi )∗( c+r ∗cos ( t ))+ cos ( pi )∗r ∗s i n ( t ) ; } ;
border G6 ( t=5∗pi /4 ,3∗pi /4)
{ x=cos (5∗pi /4)∗( c+r ∗cos ( t ))−s i n (5∗pi /4)∗r ∗s i n ( t ) ;
y=s i n (5∗pi /4)∗( c+r ∗cos ( t ))+ cos (5∗pi /4)∗r ∗s i n ( t ) ; } ;
border G7 ( t=5∗pi /4 ,3∗pi /4)
{ x=cos (6∗pi /4)∗( c+r ∗cos ( t ))−s i n (6∗pi /4)∗r ∗s i n ( t ) ;
y=s i n (6∗pi /4)∗( c+r ∗cos ( t ))+ cos (6∗pi /4)∗r ∗s i n ( t ) ; } ;
border G8 ( t=5∗pi /4 ,3∗pi /4)
{ x=cos (7∗pi /4)∗( c+r ∗cos ( t ))−s i n (7∗pi /4)∗r ∗s i n ( t ) ;
y=s i n (7∗pi /4)∗( c+r ∗cos ( t ))+ cos (7∗pi /4)∗r ∗s i n ( t ) ; } ;
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n ) , f i x e b o r d e r=true ) ;
plot (Th, wait=true , f i l l =true ) ;
fespace Vh(Th, P2 , p e r i o d i c =[[1 , y ] , [ 5 , y ] , [ 3 , x ] , [ 7 , x ] , [ 2 , y−x ] , [ 6 , y−x ] , [ 4 , y+x ] , [ 8 , y+x ] ] ) ;
// g l u e s
opposite
s i d e s
such
that
o r i e n t a t i o n
i s
preserved
Vh u1 ,
u2 ;
r e a l
sigma = 0.00001;
// value
of
the
s h i f t
varf
op ( u1 , u2)= int2d (Th)( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma ∗(4∗u1∗u2)/(1−x^2−y ^2)^2);
108
varf
b ( [ u1 ] , [ u2 ] ) = int2d (Th)((4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh,Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh,Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
Vh[ int ]
eV( nev ) ;
int k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l=1e −10,maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
u1=eV [ i ] ;
r e a l
gg = int2d (Th)( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream Eva(fnm ,
append ) ;
Eva <<
ev [ i ] << "\n" ;
// cout<<"−−−−"<< i<<""<<ev [ i ]<<"err="
//<<dx (u1 )∗dx (u1) + dy (u1 )∗dy (u1) −( ev [ i ] ) ∗u1∗u1 << " −−−"<<endl ;
p l o t (eV[ i ] ,
cmm="Eigen␣Vector ␣"+i+"␣valeur ␣=" + ev [ i ]
, wait =1, value =1);
//un−comment the
above
two
l i n e s
to
d i s p l a y
l e v e l
s e t s
for
each
eigenfunction
}
Table C.1 shows the positive eigenvalues of the Bolza surface, up to approximately
100. They can be compared with the much higher accuracy eigenvalues calculated by
Strohmaier and Uski using the algorithm described in [77]. The data ﬁles associated with
the paper can be obtained from the personal website of Professor Strohmaier: http:
//www1.maths.leeds.ac.uk/~pmtast/publications/eigdata/datafile.html.
Here
can be found the ﬁrst 1000 eigenvalues of the Bolza surface, and other genus 2 surfaces,
including the other two in this appendix.
Related to the Bolza surface is the (2, 3, 8) triangle that tessellates it.
We have
produced a program to calculate that eigenvalues of this - please see the Bolza surface
code for comments. The one comment included in this code relates to boundary conditions
- it is straightforward to change between Dirichlet and Neumann boundary conditions.
int n = 50;
int
nev = 100;
s t r i n g
fnm = "238tri_50n_100nev_nnn . txt " ;
border G1 ( t =0 ,0.4056163087774724)
{ x=t ;
y =0;};
border G2 ( t =0.33681578765748216 ,0)
{ x=t ;
y=t ∗tan ( pi / 8 ) ; } ;
border G3 ( t =0.4056163087774724 ,0.33681578765748216)
{ x=t ;
y=0.5946036542842016 −sqrt ((1.189207445439991^2) −( t −1.435500206409523)^2);};
plot (G1(n)+G2(n)+G3(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n ) ) ;
plot (Th ) ;
fespace Vh(Th, P2 ) ;
109
Vh u1 ,
u2 ;
r e a l
sigma = 0 . 0 0 1 ;
varf
op ( u1 , u2)= int2d (Th)( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma ∗(4∗u1∗u2)/(1−x^2−y ^2)^2);
// naturally ,
t h i s
g i v e s Neumann boundary
conditions
on
a l l
three
s i d e s .
//To change one or more
s i d e s
to
a
D i r i c h l e t
condition ,
add
the
phrase
//‘+on(G1, u1=0)’
a f t e r
the
closed
parenthesis .
// This
w i l l
give
a
D i r i c h l e t
condition
on G1.
varf
b ( [ u1 ] , [ u2 ] ) = int2d (Th)((4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh,Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh,Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
Vh[ int ]
eV( nev ) ;
int k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l=1e −10,maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
u1=eV [ i ] ;
r e a l
gg = int2d (Th)( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream Eva(fnm ,
append ) ;
Eva <<
ev [ i ] << "\n" ;
}
Also of interest is the spectrum of the right angled pentagon of area π
2 with mixed
boundary conditions, studied in Section 3.4. All of the multiplicity 4 eigenvalues of B ap-
pear in this spectrum with simple multiplicity. Recall the discussion about isospectrality
in the introduction to this work - one can see for oneself that swapping the Dirichlet and
Neumann conditions in the code below (see the comments in the code for the (2, 3, 8)
triangle) produces the same spectrum! Table C.2 shows the eigenvalues of this problem
up to 200; one can compare this to Table C.1, where all of the eigenvalues in Table C.2
appear with multiplicity 4.
int n=30;
int
nev =100;
r e a l
r =0.643594;
s t r i n g
fnm = "pentagon_30n_100nev . txt " ;
// f i l e
name for
saving
border G1 ( t =0.5 ,1)
{ x=r ∗2∗cos ( pi /8)+ r ∗cos ((9−2∗t )∗pi / 8 ) ;
y=r ∗s i n ((9−2∗t )∗pi / 8 ) ; } ;
border G2 ( t =−1,0) { x=cos ( pi /4)∗r ∗2∗cos ( pi /8)+ r ∗cos ((9−2∗t )∗pi / 8 ) ;
y=s i n ( pi /4)∗r ∗2∗cos ( pi /8)+ r ∗s i n ((9−2∗t )∗pi / 8 ) ; } ;
border G3 ( t =1 ,0.5)
{ x=r ∗s i n ((9−2∗t )∗pi / 8 ) ;
y=r ∗2∗cos ( pi /8)+ r ∗cos ((9−2∗t )∗pi / 8 ) ; } ;
border G4 ( t =0.545613 ,0)
{ x=0; y=t ; } ;
border G5 ( t =0 ,0.545613)
{ x=t ;
y =0;};
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n ) ) ;
110
plot (Th ) ;
fespace Vh(Th, P2 ) ;
Vh u1 ,
u2 ;
r e a l
sigma = 0.00001;
varf
op ( u1 , u2)= int2d (Th)( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma∗u1∗u2 )
+on (G2, u1=0)+on (G4, u1=0);
varf
b ( [ u1 ] , [ u2 ] ) = int2d (Th)((4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh,Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh,Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
Vh[ int ]
eV( nev ) ;
int k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l=1e −10,maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
u1=eV [ i ] ;
r e a l
gg = int2d (Th)( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream Eva(fnm ,
append ) ;
Eva <<
ev [ i ] << "\n" ;
}
We have produced FreeFEM++ codes for other genus 2 surfaces during this project,
and would like to include them in this appendix. First, we give the code that computes
the spectrum of the surface with automorphism group Z10:
int n = 50;
int
nev = 50;
s t r i n g
fnm="Z10−Eigenvalues−n50−nev50 . txt " ;
// f i l e
name for
saving
r e a l
r = 0.4133042381223985;
r e a l
c = 1.082044543098821;
r e a l
s = 0.6687403049764225;
r e a l
x01 = s ;
r e a l
y01 = 0;
r e a l
x04 = s ∗cos (3∗pi / 5 ) ;
r e a l
y04 = s ∗s i n (3∗pi / 5 ) ;
r e a l
x03 = s ∗cos (2∗pi / 5 ) ;
r e a l
y03 = s ∗s i n (2∗pi / 5 ) ;
r e a l
x06 = s ∗cos ( pi ) ;
r e a l
y06 = s ∗s i n ( pi ) ;
r e a l
x05 = s ∗cos (4∗pi / 5 ) ;
r e a l
y05 = s ∗s i n (4∗pi / 5 ) ;
r e a l
x08 = s ∗cos (7∗pi / 5 ) ;
r e a l
y08 = s ∗s i n (7∗pi / 5 ) ;
r e a l
x07 = s ∗cos (6∗pi / 5 ) ;
r e a l
y07 = s ∗s i n (6∗pi / 5 ) ;
111
r e a l
x10 = s ∗cos (9∗pi / 5 ) ;
r e a l
y10 = s ∗s i n (9∗pi / 5 ) ;
r e a l
x09 = s ∗cos (8∗pi / 5 ) ;
r e a l
y09 = s ∗s i n (8∗pi / 5 ) ;
r e a l
x02 = s ∗cos ( pi / 5 ) ;
r e a l
y02 = s ∗s i n ( pi / 5 ) ;
border G1 ( t=6∗pi /5 ,4∗pi /5)
{ x=c+r ∗cos ( t ) ;
y=r ∗s i n ( t ) ; } ;
border G2 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos ( pi /5)∗( c+r ∗cos ( t ))−s i n ( pi /5)∗r ∗s i n ( t ) ;
y=s i n ( pi /5)∗( c+r ∗cos ( t ))+ cos ( pi /5)∗r ∗s i n ( t ) ; } ;
border G3 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos (2∗pi /5)∗( c+r ∗cos ( t ))−s i n (2∗pi /5)∗r ∗s i n ( t ) ;
y=s i n (2∗pi /5)∗( c+r ∗cos ( t ))+ cos (2∗pi /5)∗r ∗s i n ( t ) ; } ;
border G4 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos (3∗pi /5)∗( c+r ∗cos ( t ))−s i n (3∗pi /5)∗r ∗s i n ( t ) ;
y=s i n (3∗pi /5)∗( c+r ∗cos ( t ))+ cos (3∗pi /5)∗r ∗s i n ( t ) ; } ;
border G5 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos (4∗pi /5)∗( c+r ∗cos ( t ))−s i n (4∗pi /5)∗r ∗s i n ( t ) ;
y=s i n (4∗pi /5)∗( c+r ∗cos ( t ))+ cos (4∗pi /5)∗r ∗s i n ( t ) ; } ;
border G6 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos ( pi )∗( c+r ∗cos ( t ))−s i n ( pi )∗r ∗s i n ( t ) ;
y=s i n ( pi )∗( c+r ∗cos ( t ))+ cos ( pi )∗r ∗s i n ( t ) ; } ;
border G7 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos (6∗pi /5)∗( c+r ∗cos ( t ))−s i n (6∗pi /5)∗r ∗s i n ( t ) ;
y=s i n (6∗pi /5)∗( c+r ∗cos ( t ))+ cos (6∗pi /5)∗r ∗s i n ( t ) ; } ;
border G8 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos (7∗pi /5)∗( c+r ∗cos ( t ))−s i n (7∗pi /5)∗r ∗s i n ( t ) ;
y=s i n (7∗pi /5)∗( c+r ∗cos ( t ))+ cos (7∗pi /5)∗r ∗s i n ( t ) ; } ;
border G9 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos (8∗pi /5)∗( c+r ∗cos ( t ))−s i n (8∗pi /5)∗r ∗s i n ( t ) ;
y=s i n (8∗pi /5)∗( c+r ∗cos ( t ))+ cos (8∗pi /5)∗r ∗s i n ( t ) ; } ;
border G10 ( t=6∗pi /5 ,4∗pi /5)
{ x=cos (9∗pi /5)∗( c+r ∗cos ( t ))−s i n (9∗pi /5)∗r ∗s i n ( t ) ;
y=s i n (9∗pi /5)∗( c+r ∗cos ( t ))+ cos (9∗pi /5)∗r ∗s i n ( t ) ; } ;
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n ) ,
f i x e b o r d e r=true ) ;
plot (Th, wait=true , f i l l =true ) ;
fespace Vh(Th, P2 , p e r i o d i c =[[1 , y ] , [ 4 , cos (2∗pi /5)∗( y−y04)−s i n (−2∗pi /5)∗( x−x04 ) ] ,
[ 3 , cos (2∗pi /5)∗( y−y03)−s i n (2∗pi /5)∗( x−x03 ) ] , [ 6 , y ] ,
[ 5 , cos (2∗pi /5)∗( y−y05)−s i n (−2∗pi /5)∗( x−x05 ) ] ,
[ 8 , cos (2∗pi /5)∗( y−y08)−s i n (−2∗pi /5)∗( x−x08 ) ] ,
[ 7 , cos (2∗pi /5)∗( y−y07)−s i n (2∗pi /5)∗( x−x07 ) ] ,
[1 0 , cos (2∗pi /5)∗( y−y10)−s i n (−2∗pi /5)∗( x−x10 ) ] ,
[ 9 , cos (2∗pi /5)∗( y−y09)−s i n (2∗pi /5)∗( x−x09 ) ] ,
[ 2 , cos (2∗pi /5)∗( y−y02)−s i n (2∗pi /5)∗( x−x02 ) ] ] ) ;
Vh u1 ,
u2 ;
r e a l
sigma = 0.00001;
varf
op ( u1 , u2)= int2d (Th)( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma ∗(4∗u1∗u2)/(1−x^2−y ^2)^2);
varf
b ( [ u1 ] , [ u2 ] ) = int2d (Th)((4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh,Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh,Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
Vh[ int ]
eV( nev ) ;
int k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l=1e −10,maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
112
u1=eV [ i ] ;
r e a l
gg = int2d (Th)( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream Eva(fnm ,
append ) ;
Eva <<
ev [ i ] << "\n" ;
}
1
2
3
4
5
6
7
8
9
10
Side associations:
1 – 4, 3 – 6, 5 – 8, 7 – 10, 9 – 2
Figure C.1: Fundamental polygon for the surface with automorphism group Z10
Next, we have the surface that has a semi-regular 12-gon as its fundamental domain,
and has automorphism group (4, 6 | 2, 2) of order 24 (see [20] for a classiﬁcation of this
group):
int n = 50;
int
nev = 50;
s t r i n g
fnm="12gon−Eigenvalues−n50−nev50 . txt " ;
// f i l e
name for
saving
r e a l
cx = 1.0206207261596574;
r e a l
cy = 0.3535533905932733;
r e a l
r = 0.4082482904638626;
r e a l
s =0.6835992463050957;
r e a l
theta =0.22037122071230927;
r e a l
x01=s ∗cos ( theta ) ;
r e a l
y01=s ∗s i n ( theta ) ;
r e a l
x02=s ∗cos ( pi/3−theta ) ;
r e a l
y02=s ∗s i n ( pi/3−theta ) ;
r e a l
x03=s ∗cos ( pi/3+theta ) ;
r e a l
y03=s ∗s i n ( pi/3+theta ) ;
r e a l
x04=s ∗cos (2∗pi/3−theta ) ;
r e a l
y04=s ∗s i n (2∗pi/3−theta ) ;
r e a l
x05=s ∗cos (2∗pi/3+theta ) ;
r e a l
y05=s ∗s i n (2∗pi/3+theta ) ;
r e a l
x06=s ∗cos (3∗pi/3−theta ) ;
113
r e a l
y06=s ∗s i n (3∗pi/3−theta ) ;
r e a l
x07=s ∗cos (3∗pi/3+theta ) ;
r e a l
y07=s ∗s i n (3∗pi/3+theta ) ;
r e a l
x08=s ∗cos (4∗pi/3−theta ) ;
r e a l
y08=s ∗s i n (4∗pi/3−theta ) ;
r e a l
x09=s ∗cos (4∗pi/3+theta ) ;
r e a l
y09=s ∗s i n (4∗pi/3+theta ) ;
r e a l
x10=s ∗cos (5∗pi/3−theta ) ;
r e a l
y10=s ∗s i n (5∗pi/3−theta ) ;
r e a l
x11=s ∗cos (5∗pi/3+theta ) ;
r e a l
y11=s ∗s i n (5∗pi/3+theta ) ;
r e a l
x12=s ∗cos(−theta ) ;
r e a l
y12=s ∗s i n (−theta ) ;
border G1 ( t=4∗pi /3 , pi )
{ x=cx+r ∗cos ( t ) ;
y=cy+r ∗s i n ( t ) ; } ;
border G2 ( t=pi ,2∗pi /3)
{ x=cos ( pi /3)∗( cx+r ∗cos ( t ))−s i n ( pi /3)∗(−cy+r ∗s i n ( t ) ) ;
y=s i n ( pi /3)∗( cx+r ∗cos ( t ))+ cos ( pi /3)∗(−cy+r ∗s i n ( t ) ) ; } ;
border G3 ( t=4∗pi /3 , pi )
{ x=cos ( pi /3)∗( cx+r ∗cos ( t ))−s i n ( pi /3)∗( cy+r ∗s i n ( t ) ) ;
y=s i n ( pi /3)∗( cx+r ∗cos ( t ))+ cos ( pi /3)∗( cy+r ∗s i n ( t ) ) ; } ;
border G4 ( t=pi ,2∗pi /3)
{ x=cos (2∗pi /3)∗( cx+r ∗cos ( t ))−s i n (2∗pi /3)∗(−cy+r ∗s i n ( t ) ) ;
y=s i n (2∗pi /3)∗( cx+r ∗cos ( t ))+ cos (2∗pi /3)∗(−cy+r ∗s i n ( t ) ) ; } ;
border G5 ( t=4∗pi /3 , pi )
{ x=cos (2∗pi /3)∗( cx+r ∗cos ( t ))−s i n (2∗pi /3)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (2∗pi /3)∗( cx+r ∗cos ( t ))+ cos (2∗pi /3)∗( cy+r ∗s i n ( t ) ) ; } ;
border G6 ( t=pi ,2∗pi /3)
{ x=cos (3∗pi /3)∗( cx+r ∗cos ( t ))−s i n (3∗pi /3)∗(−cy+r ∗s i n ( t ) ) ;
y=s i n (3∗pi /3)∗( cx+r ∗cos ( t ))+ cos (3∗pi /3)∗(−cy+r ∗s i n ( t ) ) ; } ;
border G7 ( t=4∗pi /3 , pi )
{ x=cos (3∗pi /3)∗( cx+r ∗cos ( t ))−s i n (3∗pi /3)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (3∗pi /3)∗( cx+r ∗cos ( t ))+ cos (3∗pi /3)∗( cy+r ∗s i n ( t ) ) ; } ;
border G8 ( t=pi ,2∗pi /3)
{ x=cos (4∗pi /3)∗( cx+r ∗cos ( t ))−s i n (4∗pi /3)∗(−cy+r ∗s i n ( t ) ) ;
y=s i n (4∗pi /3)∗( cx+r ∗cos ( t ))+ cos (4∗pi /3)∗(−cy+r ∗s i n ( t ) ) ; } ;
border G9 ( t=4∗pi /3 , pi )
{ x=cos (4∗pi /3)∗( cx+r ∗cos ( t ))−s i n (4∗pi /3)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (4∗pi /3)∗( cx+r ∗cos ( t ))+ cos (4∗pi /3)∗( cy+r ∗s i n ( t ) ) ; } ;
border G10 ( t=pi ,2∗pi /3) { x=cos (5∗pi /3)∗( cx+r ∗cos ( t ))−s i n (5∗pi /3)∗(−cy+r ∗s i n ( t ) ) ;
y=s i n (5∗pi /3)∗( cx+r ∗cos ( t ))+ cos (5∗pi /3)∗(−cy+r ∗s i n ( t ) ) ; } ;
border G11 ( t=4∗pi /3 , pi )
{ x=cos (5∗pi /3)∗( cx+r ∗cos ( t ))−s i n (5∗pi /3)∗( cy+r ∗s i n ( t ) ) ;
y=s i n (5∗pi /3)∗( cx+r ∗cos ( t ))+ cos (5∗pi /3)∗( cy+r ∗s i n ( t ) ) ; } ;
border G12 ( t=pi ,2∗pi /3) { x=cx+r ∗cos ( t ) ;
y=−cy+r ∗s i n ( t ) ; } ;
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n ) ) ;
mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n ) , f i x e b o r d e r=true ) ;
plot (Th, wait=true , f i l l =true ) ;
fespace Vh(Th, P2 , p e r i o d i c =[[2 ,( cos ( pi /6))∗( y−y02)−( s i n ( pi /6))∗( x−x02 ) ] ,
[ 5 , ( cos(−pi /6))∗( y−y05)−( s i n (−pi /6))∗( x−x05 ) ] ,
[ 4 , ( cos ( pi /2))∗( y−y04)−( s i n ( pi /2))∗( x−x04 ) ] ,
[ 7 , ( cos ( pi /6))∗( y−y07)−( s i n ( pi /6))∗( x−x07 ) ] ,
[ 6 , ( cos (−7∗pi /6))∗( y−y06)−( s i n (−7∗pi /6))∗( x−x06 ) ] ,
[ 9 , ( cos ( pi /2))∗( y−y09)−( s i n ( pi /2))∗( x−x09 ) ] ,
[ 8 , ( cos ( pi /6))∗( y−y08)−( s i n ( pi /6))∗( x−x08 ) ] ,
[ 1 1 , ( cos ( pi /6))∗( y−y11)−( s i n (−pi /6))∗( x−x11 ) ] ,
[ 1 0 , ( cos ( pi /2))∗( y−y10)−( s i n ( pi /2))∗( x−x10 ) ] ,
[ 1 , ( cos ( pi /6))∗( y−y01)−( s i n ( pi /6))∗( x−x01 ) ] ,
[ 1 2 , ( cos ( pi /6))∗( y−y12)−( s i n (−pi /6))∗( x−x12 ) ] ,
[ 3 , ( cos(−pi /2))∗( y−y03)−( s i n (−pi /2))∗( x−x03 ) ] ] ) ;
114
Vh u1 ,
u2 ;
r e a l
sigma = 0.00001;
varf
op ( u1 , u2)= int2d (Th)( dx ( u1 )∗dx ( u2)+ dy ( u1 )∗dy ( u2)−sigma ∗(4∗u1∗u2)/(1−x^2−y ^2)^2);
varf
b ( [ u1 ] , [ u2 ] ) = int2d (Th)((4 ∗u1∗u2)/(1−x^2−y ^2)^2);
matrix OP= op (Vh,Vh, s o l v e r=Crout , f a c t o r i z e =1);
matrix B=b(Vh,Vh, s o l v e r=CG, eps=1e −20);
r e a l [ int ]
ev ( nev ) ;
Vh[ int ]
eV( nev ) ;
int k=EigenValue (OP,B, sym=true , sigma=sigma , value=ev , vector=eV ,
t o l=1e −10,maxit=0,ncv =0);
for
( int
i =0; i<k ; i++) {
u1=eV [ i ] ;
r e a l
gg = int2d (Th)( dx ( u1 )∗dx ( u1 ) + dy ( u1 )∗dy ( u1 ) ) ;
r e a l mm= int2d (Th) ( u1∗u1 )
;
ofstream Eva(fnm ,
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
12
2
4
6
8
10
Side associations:
2 – 5, 4 – 7, 6 – 9, 8 – 11, 10 – 1, 12 – 3
Figure C.2: Fundamental domain for the surface with order 24 automorphism group
115
Eigenvalue
Numerical multiplicity
3.83618
3
5.35083
4
8.24401
2
14.7149
4
15.0386
3
18.645
3
20.5069
4
23.0545
1
28.0591
3
30.8081
4
32.6493
1
36.2126
2
38.9353
4
40.0913
3
42.8344
4
43.9864
3
50.5199
3
57.4478
4
59.4306
4
60.988
2
62.595
3
67.5682
3
71.3853
4
73.6255
2
74.8779
1
75.5018
3
75.6305
4
86.1472
4
86.6702
3
91.4225
1
93.3361
4
97.8419
3
100.675
3
Table C.1: First positive eigenvalues of the Bolza surface
116
Eigenvalue
Numerical multiplicity
5.35323
1
14.7246
1
20.5174
1
30.8305
1
38.956
1
42.852
1
57.4803
1
59.4601
1
71.4156
1
75.6649
1
86.177
1
93.3682
1
105.547
1
110.988
1
111.675
1
127.163
1
133.738
1
144.59
1
151.081
1
154.5
1
166.766
1
170.721
1
182.089
1
193.034
1
200.792
1
Table C.2: First positive eigenvalues of the mixed boundary problem on a pentagon of area π
2
117
Eigenvalue
Numerical multiplicity
3.48586
2
4.56299
2
5.05739
2
8.6528
2
8.96267
2
12.1336
1
14.9476
2
16.2255
2
16.9401
2
19.9236
2
20.7194
2
22.1597
1
24.0114
2
24.0994
2
28.7943
2
32.0614
2
32.3071
2
34.5634
2
36.383
2
36.8106
2
40.0014
1
43.8803
2
44.0732
2
45.5809
2
46.316
2
48.2176
2
Table C.3: First positive eigenvalues of Z10 surface
118
Eigenvalue
Numerical multiplicity
3.10942
2
4.12201
2
6.96949
1
7.78
2
8.98983
4
11.1973
1
15.0295
1
16.7819
2
19.5961
2
20.6216
4
20.9365
1
24.5947
2
25.0792
2
26.7752
2
28.8984
2
34.0612
4
34.7219
1
36.2501
1
39.9781
2
40.008
3
46.176
2
46.2604
4
47.5021
1
Table C.4: First positive eigenvalues of the 12-gon with order 24 symmetry group
119
Appendix D
