---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-020-freefem-code-for-genus-2
section_title: "FreeFEM++ Code for Genus 2"
section_number: null
pages: 118-130
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
The following box contains the FreeFEM-++ code for the{Balza surface. It contains basic
comments, but for more information about the various solvers and finite element spaces
available in the software, please consult the manual [32].

int n = 30; //number of modes

int nev=100; //number of eigenvalues to be calculated
string fnm = "bolza_surface_30n_100nev.txt"; //file name for saving

real r = 0.4550898605622276; //radius of circle
real c = 1.09868411346781; //centre of circle on x-axis

border Gl (t—5*pi/4,3*pi/4) { x<ctr*cos(t); y=r«esin(t);};

border G2 (t=5«pi/4,3*pi/4) { x=cos(pi/4)*(ct+r*cos(t))—sin(pi/4)*r«sin(t);
y=sin(pi/4)*(c+r*cos(t))+cos(pi/4)*r*sin(t);};

border G3 (t=5«pi/4,3*pi/4) { x=cos(pi/2)*(c+r*cos(t))—sin(pi/2)*r«sin(t);
y=sin(pi/2)*(c+r*cos(t))+cos(pi/2)*r*sin(t);};

border G4 (t=5*pi/4,3*pi/4) { x=cos(3*pi/4)*(ctr*cos(t))—sin(3*pi/4)*r*sin(t);
y=sin (3* pi/4)*(ct+r*cos(t))+cos(3*pi/4)*r*sin(t);};

border G5 (t=5*pi/4,3*pi/4) { x=cos(pi)*(ctr*cos(t))—sin(pi)*r*sin(t);
y=sin (pi)*(ctr*cos(t))+cos(pi)*r*sin(t);}3

border G6 (t=5*pi/4,3*pi/4) { x=cos(5*pi/4)*(ctr*cos(t))—sin(5*pi/4)*r*sin(t);
y=sin (5* pi/4)*(ct+r*cos(t))+cos(5*pi/4)*r*sin(t);};

border G7 (t=5*pi/4,3*pi/4) { x=cos(6*pi/4)*(ctr*cos(t))—sin(6*pi/4)*r*sin(t);
y=sin (6* pi /4)*(ct+r*cos(t))+cos(6*pi/4)*r*sin(t);};

border G8 (t=5*pi/4,3*pi/4) { x=cos(7*pi/4)*(ctr*cos(t))—sin(7*pi/4)*r*sin(t);
y=sin (7* pi /4)*(ct+r*cos(t))+cos(7*pi/4)*r*sin(t);};

plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n));

mesh Th=buildmesh (G1(n)-+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n) , fixeborder=true );
plot (Th, wait=true, fill=true);

fespace Vh(Th,P2, periodic =[[1,y] ,[5,y],[3,x],[7,x],[2,y—x] ,[6,y-x] ,[4.,.y+x] ,[8,y+x]]);

//glues opposite sides such that orientation is preserved
Vh ul, u2;

real sigma = 0.00001; //value of the shift
varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma*(4*ul¥u2)/(1—x°2-y~>2)*2);

108
varf b({ul] ,[u2]) = int2d (Th) ((4*ul*u2)/(1—x*2-y*2)*2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);
matrix B=b(Vh,Vh, solver=CG, eps=le —20);

real[int] ev(nev);
Vh[int] eV(nev);

int k-EigenValue(OP,B,sym-true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int i=0;i<k;i++) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm int2d(Th)(ulxul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

[/ cout <K<M——Nc< ccceufif<<"erra="

//<<de (ul )* dx (ul) + dy(ul)*dy(ul) — (ev[i])*uleul << "—— "<<endl; plot(eV/i],
cmm="Eigen_ Vector "+i+" valeur=" + ev[i] ,wait=1,value=1);

(/uapconamer tHe above two lines to display level sets for each eigenfunction
}

Table C.1 shows the positive eigenvalues of the veclel wae up to approximately

y eigenvalues calculated by.

—

//wiw1.maths.leeds.ac.uk/~pmtast/publications/eigdata/datafile.html. Here

100. They can be compared with the much higher accu:

trohmaier and Uski using the algorithm described in _ The data files associated wit

can be found the first 1000 eigenvalues of the Bolza surface, and other genus 2 surfaces,
including the other two in this appendix.

Related to the Bolza surface is the (2, 3, 8) triangle that tessellates it. We have
produced a program to calculate that eigenvalues of this - please see the Bolza surface
code for comments. The one comment included in this code relates to boundary conditions
- it is straightforward to change between Dirichlet and Neumann boundary conditions.
int n = 50;
int nev = 100;

string fmm = "238tri_50n_100nev_nnn. txt";

border Gl (t=0,0.4056163087774724) { x=t; y=0;};

border G2 (t=0.33681578765748216,0) { x=t; y=t*tan(pi/8);};

border G3 (t=0.4056163087774724 ,0.33681578765748216) { x=t;
y=0.5946036542842016— sqrt ((1.189207445439991~2) —(t —1.435500206409523) ~2);};

plot (G1(n)+G2(n)+G3(n));
mesh Th=buildmesh (G1(n)+G2(n)+G3(n));
plot (Th);

fespace Vh(Th,P2);

109
Vh ul, u2;
real sigma = 0.001;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma+(4*ul*u2) /(1—x*2—-y*2)*2);
//naturally, this gives Neumann boundary conditions on all three sides.
//To change one or more sides to a Dirichlet condition, add the phrase
//‘+on(G1,ul=0)’ after the closed parenthesis.
//This will give a Dirichlet condition on G1.

varf b([ul] ,[u2]) = int2d (Th) ((4*ul*u2)/(1—x*2-y~2)*2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);
matrix B=b(Vh,Vh, solver=CG, eps=le —20);

real[int] ev(nev);
Vh[int] eV(nev);

int k-EigenValue(OP,B,sym-true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int i=0;i<k;i++) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm int2d(Th)(ulxul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

Also of interest is the spectrunk-of-the-sigdlt angled pentagon of area 5 with mixed
boundary conditions, studied in Section 3.4. All of the multiplicity 4 eigenvalues of B ap-
pear in this spectrum with simple multiplicity. Recall the discussion about isospectrality
in the introduction to this work - one can see for oneself that swapping the Dirichlet and
Neumann conditions in the code below (sde_the coments in the code for the (2, 3, 8)
triangle) produces the same spectrum! |Table C.2| shows the eigenvalues of this problem __|
up to 200; one can compare this to Table C.1, where all of the eigenvalues in Table C.2
appear with multiplicity 4.
int n=30;
int nev=100;
real r=0.643594;

string fmm = "pentagon _30n_100nev.txt"; //file name for saving

border Gl (t=0.5,1) { x=r«2*cos(pi/8)+r*cos((9—2*t)*pi/8); y=r*sin((9—2*t)*pi/8);};
border G2 (t=-1,0) { x=cos(pi/4)*r#2*cos(pi/8)+r*cos((9—2*t)*pi/8);

y=sin (pi/4)*r*2«cos(pi/8)+r*sin ((9—2«t)*pi/8);}5
border G3 (t=1,0.5) { x=rxsin((9—2*t)*pi/8); y=rx2*cos(pi/8)+r*cos((9—2*t)* pi /8);};
border G4 (t=0.545613,0) { x=0; y=t;};
border G5 (t=0,0.545613) { x=t; y=0;};
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n));

mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n));

110
plot (Th);
fespace Vh(Th,P2);

Vh ul, u2;

real sigma — 0.00001;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigmax ul*u2)
+on (G2, ul=0)+on (G4, ul =0);

varf b({ul] ,[u2]) = int2d (Th) ((4*ul*u2)/(1—x*2-y~>2)*2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);
matrix B=b(Vh,Vh, solver=CG, eps=le —20);

real[int] ev(nev);
Vh[int] eV(nev);

int k-EigenValue(OP,B,sym-true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int i=0;i<k;i++) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm int2d(Th)(ulxul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

We have produced FreeFEM++ codes for other genus 2 surfaces during this project,
and would like to include them in this appendix. First, we give the code that computes
the spectrum of the surface with automorphism group Zio:
int n = 50;
int nev = 50;

string fnm="Z10—Eigenvalues—n50—nev50.txt"; //file name for saving

real r = 0.4133042381223985;
-082044543098821;
real s = 0.6687403049764225;

a

real c =

real x01 = s;
real y0l = 0;
real x04 = s*cos(3*pi/5);
real y04 = s*sin(3*pi/5);

real x03 = s*cos(2«pi/5);
real y03 = s*sin(2«pi/5);
real x06 = s*cos(pi);

real y06 = s*sin(pi);

real x05 = s*cos(4*pi/5);
real y05 = s*sin(4*pi/5);
real x08 = s*cos(7*pi/5);
real y08 = s*sin(7*pi/5);

real x07 = s*cos(6*pi/5);
real y07 = s*sin(6*pi/5);

111
real x10 = s*cos(9*pi/5);
real y10 = s*sin(9*pi/5);

real x09 = s*cos(8*pi/5);

real y09 = s*sin(8*pi/5);

real x02 = s*cos(pi/5);

real y02 = s*sin(pi/5);

border Gl (t=6*pi/5,4*pi/5) { x=ctr*cos(t); y=resin(t);};

border G2 (t=6*pi/5,4*pi/5) { x=cos(pi/5)*(ctr*cos(t))—sin(pi/5)*r*sin(t);
y=sin(pi/5)*(c+r*cos(t))+cos(pi/5)*r*sin(t);};

border G3 (t—6*pi/5,4*pi/5) { x=cos(2*pi/5)*(ct+r*cos(t))—sin (2«pi/5)*r«sin(t);
y=sin (2« pi /5)*(ctr*cos(t))+cos(2*pi/5)*r*sin(t);};

border G4 (t—6*pi/5,4*pi/5) { x=cos(3*pi/5)*(ct+r*cos(t))—sin(3*pi/5)*r«sin(t);
y=sin (3* pi /5)*(ctr*cos(t))+cos(3*pi/5)*resin(t);};

border G5 (t—6*pi/5,4*pi/5) { x=cos(4*pi/5)*(ct+r*cos(t))—sin (4«pi/5)*r«sin(t);
y=sin (4* pi /5)*(ctr*cos(t))+cos(4*pi/5)*r*sin(t);};

border G6 (t=6«pi/5,4*pi/5) { x=cos(pi)*(ctr*cos(t))—sin(pi)*r*sin(t);
y=sin (pi)*(ct+r*cos(t))+cos(pi)*r*sin(t);};

border G7 (t—6*pi/5,4*pi/5) { x=cos(6*pi/5)*(ct+r*cos(t))—sin (6*pi/5)*r«sin(t);
y=sin (6* pi /5)*(ctr*cos(t))+cos(6*pi/5)*r*sin(t);};

border G8 (t—6*pi/5,4*pi/5) { x=cos(7*pi/5)*(ct+r*cos(t))—sin(7*pi/5)*r«sin(t);
y=sin (7* pi /5)*(ctr*cos(t))+cos(7*pi/5)*r*sin(t);};

border G9 (t—6*pi/5,4*pi/5) { x=cos(8*pi/5)*(ct+r*cos(t))—sin (8*pi/5)*r«sin(t);
y=sin (8* pi /5)*(ctr*cos(t))+cos(8*pi/5)*r*sin(t);};

border G10 (t=6*pi/5,4*pi/5) { x=cos(9«pi/5)*(ctr*cos(t))—sin(9* pi/5)*resin(t);
y=sin (9* pi /5)*(ctr*cos(t))+cos(9*pi/5)*r*sin(t);};

plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n) );

mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n) ,
fixeborder=true );

plot (Th, wait=true, fill=true);

fespace Vh(Th,P2, periodic =[[1,y] ,[4, cos (2* pi/5)*(y—y04)—sin(—2*pi/5)*(x-x04)],

2x pi/5)*(y—y03)—sin (2* pi/5)*(x-x03)],[6,y],

2% pi /5)*(y—y05)—sin(—2«pi /5)*(x-x05)],

2x pi/5)*(y—-y08)—sin(—2« pi /5)*(x—x08)],

[7 , cos (2* pi /5)*(y—y07)—sin (2* pi /5)*(x-x07)],

[10 , cos (2« pi /5)*(y—y10)—sin(—2«pi/5)*(x—x10)],

[9 , cos (2* pi/5)*(y—y09)—sin (2 pi /5)*(x—x09)],

[2 , cos (2 pi /5)*(y—y02)—sin (2* pi /5)*(x-x02)]]);

[3, cos

[5, cos

[8 , cos

Vh ul, u2;
real sigma — 0.00001;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma*(4*ul¥u2)/(1—x°2-y~>2)*2);
varf b({ul] ,[u2]) = int2d (Th) ((4*ul*u2)/(1—x°2-y~>2)*2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);

matrix B=b(Vh,Vh, solver=CG, eps=le —20);

real[int] ev(nev);
Vh[int] eV(nev);

int k-EigenValue(OP,B,sym-true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int i=0;i<k;i++) {

112
ul=eV[i];
real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm= int2d(Th)(ul*ul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

Side associations:
1—4,3-—6,5-—8,7-10,9-2

Figure C.1: Fundamental polygon for the surface with automorphism group Zj9

Next, we have the surface that has a semi-regular 12-gon aslita fundamental domain,

and has automorphism group (4, 6| 2, 2) of order 24 (see [20] for a classification of this

group):
int n = 50;
int nev = 50;

string fnm="12gon—Higenvalues—n50—nev50.txt"; //file name for saving

real cx = 1.0206207261596574;
real cy = 0.3535533905932733;
real r = 0.4082482904638626;

real s=0.6835992463050957;
real theta —0.22037122071230927;
real x01=s*cos(theta);
theta);
pi/3—theta);
pi/3—theta);
pi/3+theta);
pi/3+theta);
2 pi/3—theta);
2 pi/3—theta);
2x pi/3+theta);
2x pi/3+theta);
3% pi/3—theta);

real yOl=s*sin
real x02=s*cos
real y02=s*sin
real x03=s*cos

real y03=s*sin

real x04=s*cos

real y04=s*sin

real x05=s*cos
real y05=s*sin

real x06=s*cos

113
real y06=s*sin (3% pi/3—theta );

real x07=s*cos(3*pi/3+theta);

real y07=s*sin(3*pi/3+theta);

real x08=s*cos (4 pi/3—theta );

real y08=s*sin (4% pi/3—theta );

real x09=s*cos(4* pi/3+theta );

real y09=s*sin (4* pi/3+theta);

real x10=s*cos(5* pi/3—theta);

real yl0=s*sin(5* pi/3—theta);

real xll=s*cos(5*pi/3+theta);

real yll=s*sin(5*pi/3+theta);

real x12=s*cos(—theta);

real yl2=s*sin(—theta);

border Gl (t=4*pi/3,pi) { x=cx+r*cos(t); y=cy+r*sin(t);};

border G2 (t=pi,2*pi/3) { x=cos(pi/3)*(cx+r*cos(t))—sin(pi/3)*(—cy+r*sin(t));
y=sin (pi/3)*(cx+r*cos(t))+cos(pi/3)*(—cy+tr*sin(t));};

border G3 (t=4*pi/3,pi) { x=cos(pi/3)*(cxtr*cos(t))—sin(pi/3)*(cy+r*sin(t));
y=sin (pi/3)*(cx+r*cos(t))+cos(pi/3)*(cy+r*sin(t));}3

border G4 (t=pi,2*pi/3) { x=cos(2*pi/3)*(cx+r*cos(t))—sin(2* pi/3)*(—cy+r«sin(t));
y=sin (2* pi /3)*(cx+r*cos(t))+cos(2* pi/3)*(—cyt+r*sin(t));};

border G5 (t=4*pi/3,pi) { x=cos(2*pi/3)*(cx+r*cos(t))—sin(2« pi/3)*(cy+r*sin(t));
y=sin (2* pi/3)*(cx+r*cos(t))+cos(2* pi/3)*(cyt+r*sin(t));};

border G6 (t=pi,2*pi/3) { x=cos(3*pi/3)*(cx+r«*cos(t))—sin(3*pi/3)*(—cy+r*sin(t));
y=sin (3* pi/3)*(cx+r*cos(t))+cos(3* pi/3)*(—cyt+r*sin(t));};

border G7 (t=4*pi/3,pi) { x=cos(3*pi/3)*(cx+r*cos(t))—sin(3«pi/3)*(cy+r*sin(t));
y=sin (3* pi/3)*(cx+r*cos(t))+cos(3* pi/3)*(cyt+r*sin(t));};

border G8 (t=pi,2*pi/3) { x=cos(4*pi/3)*(cx+r*cos(t))—sin (4% pi/3)*(—cy+r«sin(t));
y=sin (4* pi/3)*(cx+r*cos(t))+cos(4* pi/3)*(—cy+r*sin(t));};

border G9 (t=4*pi/3,pi) { x=cos(4*pi/3)*(cx+r*cos(t))—sin(4* pi/3)*(cy+r*sin(t));
y=sin (4* pi/3)*(cxt+r*cos(t))+cos(4* pi/3)*(cyt+r*sin(t));};

border G10 (t=pi,2*pi/3) { x=cos(5*pi/3)*(cx+r*cos(t))—sin(5* pi/3)*(—cy+r*sin(t));
y=sin (5* pi/3)*(cx+r*cos(t))+cos(5* pi/3)*(—cyt+r*sin(t));};

border Gll (t=4*pi/3,pi) { x=cos(5*pi/3)*(cx+r*cos(t))—sin(5*pi/3)*(cy+r*sin(t));
y=sin (5* pi/3)*(cxt+r*cos(t))+cos(5* pi/3)*(cyt+r*sin(t));};

border G12 (t=pi,2*pi/3) { x=cx+r*cos(t); y=-cy+tr*sin(t);};

plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n));

mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n) , fixeborder=true );

plot (Th, wait=true, fill=true);

fespace Vh(Th,P2, periodic =[[2,(cos(pi/6))*(y—y02)—(sin (pi /6))*(x-x02)],
[5 ,(cos(—pi/6))*(y—y05)—(sin(—pi/6))*(x-x05)],
[4,(cos(pi/2))*(y-y04)—(sin (pi /2))*(x-x04)] ,

[7 ,(cos (pi /6))*(y-y07)—(sin (pi /6))*(x-x07)] ,

[6 ,(cos(—7*pi /6))*(y—y06)—(sin(—7*pi/6))*(x—x06)] ,
[9 ,(cos(pi/2))*(y-y09)—(sin (pi /2))*(x-x09)] ,

[8 ,(cos (pi /6))*(y-y08)—(sin (pi /6))*(x-x08)] ,

[11 ,(cos (pi /6))*(y-yl1)—(sin(—pi/6))*(x-x11)],

[10 ,( cos (pi/2))*(y-yl0)—(sin (pi /2))*(x-x10)],

[1 (cos (pi/6))*(y-y01)—(sin (pi /6))*(x-x01)] ,

[12 ,(cos(pi/6))*(y-yl2)—(sin(—pi/6))*(x-x12)],

[3 ,(cos(—pi/2))*(y-y03)—(sin(—pi /2))*(x—x03 )]]);

114
Vh ul, u2;

real sigma — 0.00001;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma+(4*ul*u2) /(1—x*2—-y*2)*2);
varf b({ul] ,[u2]) = int2d (Th) ((4*ul*u2)/(1—x*2-y*2)*2);

matrix OP= op(Vh,Vh, solver—Crout , factorize=1);
matrix B=b(Vh,Vh, solver—CG, eps=le—20);

real[int] ev(nev);
Vh[int] eV(nev);

int k-EigenValue(OP,B,sym-true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int i=0;i<k;i++) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm int2d(Th)(ulxul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

9 10

Side associations:
2-5,4-7,6-9,8-11,10-1,12-3

Figure C.2: Fundamental domain for the surface with order 24 automorphism group
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
