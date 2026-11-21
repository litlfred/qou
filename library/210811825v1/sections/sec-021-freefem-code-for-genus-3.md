---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-021-freefem-code-for-genus-3
section_title: "FreeFEM++ Code for Genus 3"
section_number: null
pages: 130-144
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
LT

Similarly to Appendix C, here we give the FreeFEM++ codes for particular surfaces of
genus 3. We start with the Klein quartic:

int n=30;
int nev=100;

string fnm="klein_quartic—Eigenvalues—n30—nev100.txt"; //file name for saving

real cx = 1.031969722;
real r = 0.254875473;

real s=0.7770942488589633;
real x06=s*cos(5*pi/7);
real y06=s*sin(5*pi/7);

real x03=s*cos(2*pi/7);
real y03=s*sin(2*pi/7);
real x05=s*cos(4*pi/7);

real y05=s*sin(4*pi/7);

real s*cos(9*pi/7);
real s*sin(9*pi/7);
real x07=s*cos(6*pi/7);
real x12=s*cos(11l*pi/7);
11*pi/7);
8*pi/7);
8*pi/7);

real
real

real

real xl4=s*cos(13*pi/7);

)
13*pi/7);

)

)

real yl4=s«sin

real xll=s*cos(10*pi/7);

(
(
(
(
(
(
(
(
real y07=s*sin(6*pi/7);
(
(
(
(
(
(
(
(

real yll=s*sin(10*pi/7);
real x02=s*cos(pi/7);

real y02=s*sin(pi/7);

real x13=s*cos(12*pi/7);
(12* pi/7);
real x04=s*cos(3*pi/7);
(

real yl3=sx*sin

real y04=s*sin(3*pi/7);

border Gl (t=9*pi/7,5*pi/7) { x=cx+rxcos(t); y=re*sin(t);label=1;};

border G2 (t=9«pi/7,5*pi/7) { x=cos(pi/7)*(cx+r*cos(t))—sin(pi/7)*(r*sin(t));
y=sin (pi/7)*(cx+r*cos(t))+cos(pi/7)*(r*sin(t));} label =2;;

border G3 (t=9«pi/7,5*pi/7) { x=cos(2* pi/7)*(cx+r*cos(t))—sin(2*pi/7)*r*sin(t);

2% pi/7)*r*sin(t);}label=3;;

3% pi /7)*(cx+rxcos(t))—sin(3*pi/7)*r*sin(t);

3*pi/7)*r*sin(t);label=4;};

4x pi /7)*(cx+r*cos(t))—sin(4*pi/7)*r*sin(t);

y=sin (2* pi /7)*(cx+r*cos(t))+cos
border G4 (t=9«pi/7,5*pi/7) { x=cos
y=sin (3% pi /7)*(cx+r*cos(t))+cos
border G5 (t=9«pi/7,5*pi/7) { x=cos

120
y=sin (4* pi/7)*(cx+r*cos(t))+cos(4* pi/7)*r*sin(t); label =5;};

border G6 (t=9«pi/7,5*pi/7) { x=cos(5* pi/7)*(cxt+r*cos(t))—sin(5*pi/7)*r*sin(t);
y=sin (5 pi/7)*(cx+r*cos(t))+cos(5* pi/7)*r*sin(t); label =6;};

border G7 (t=9«*pi/7,5*pi/7) { x=cos(6* pi/7)*(cx+r*cos(t))—sin(6*pi/7)*r*sin(t);
y=sin (6* pi /7)*(cx+r*cos(t))+cos(6*pi/7)*r*sin(t);label ahs

border G8 (t=9«*pi/7,5*pi/7) { x=cos(7*pi/7)*(cx+r*cos(t))—sin(7*pi/7)*r*sin(t);
y=sin(7* pi/7)*(cxt+r*cos(t))+cos(7* pi/7)*r*sin(t); label =8;};

border G9 (t=9«*pi/7,5*pi/7) { x=cos(8*pi/7)*(cxt+r*cos(t))—sin(8*pi/7)*r*sin(t);
y=sin (8*pi/7)*(cx+r*cos(t))+cos(8*pi/7)*r*sin(t); label =9;};

border G10 (
y=sin (9 pi/7)*(cx+r*cos(t))+cos(9* pi/7)*r*sin(t); label =10;};

border Gll (t=9«xpi/7,5*pi/7) { x=cos(10*pi/7)*(cx+r*cos(t))—sin(10* pi/7)*r*sin(t);
y=sin (10 pi/7)*(cx+r*cos(t))+cos(10* pi/7)*r*sin(t);label=11;};

border G12 (t=9«xpi/7,5*pi/7) { x=cos(11*pi/7)*(cx+r*cos(t))—sin(11*pi/7)*r*sin(t);
y=sin (11 pi/7)*(cx+r*cos(t))+cos(11* pi/7)*r*sin(t); label =12;};

border G13 (t=9«xpi/7,5*pi/7) { x=cos(12*pi/7)*(cx+r*cos(t))—sin(12* pi/7)*r*sin(t);
y=sin (12 pi/7)*(cx+r*cos(t))+cos(12* pi/7)*r*sin(t); label =13;};

border G14 (t=9«xpi/7,5*pi/7) { x=cos(13*pi/7)*(cx+r*cos(t))—sin(13*pi/7)*r*sin(t);
y=sin (13* pi/7)*(cx+r*cos(t))+cos(13* pi/7)*r*sin(t); label =14;};

Qxpi/7,5*pi/7) { x=cos(9*pi/7)*(cx+r*cos(t))—sin(9*pi/7)*r*sin(t);

plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n)+G13(n)
+G14(n));

mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n)+G13(n)+G14(n) , fixeborder=true);

plot (Th, wait=true , fill=true);

fespace Vh(Th,P2, periodic=[[1,y] ,[6 ,(cos(2* pi/7))*(y—y06)—(sin(—2*pi/7))*(x—x06)],
[3 ,(cos(2* pi/7))*(y-y03)—(sin (2% pi/7))*(x—x03)],[8.y],
[5 ,(cos(4* pi/7))*(y-y05)—(sin (4% pi/7)) *(x—x05 )],
[10 , (cos (2* pi/7))*(y—y10)—(sin (2*pi/7))*(x-x10)],
[7 , (cos (6* pi/7))*(y—y07)—(sin (6% pi/7)) *(x—x07)],
[12 ,(cos (4* pi/7))*(y—y12)—(sin (4* pi/7))*(x-x12)]
[9 , (cos (6% pi/7)) *(y-y09)—(sin (—6*pi /7))*(x—x09 )]
[14 , (cos (6* pi/7))*(y—y14)—(sin (6* pi/7))*(x-x14)],
[11 , (cos (4* pi/7))*(y—y11)—(sin(—4*pi/7))*(x-x11)],
]
)
]

[2 , (cos (6% pi/7))*(y—y02)—(sin(—G6*pi/7))*(x—x02)],
[13 , (cos (2* pi/7))*(y—y13)—(sin(—2*pi /7))*(x—x13)],
[4 , (cos (4% pi/7)) *(y-y04) —(sin (—4* pi /7))*(x—x04 )]]);
Vh ul, u2;

real sigma = 0.00001;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma*(4*ul*u2)/(1—x*2—y~2)~2);
varf b([ul] ,[u2]) = int2d(Th)((4*ul*u2)/(1—x*2-y~2)>2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);
matrix B=b(Vh, Vh, solver=CG, eps=le —20);

real[int] ev(nev);

Vh[int] eV(nev);

int k=EigenValue (OP,B,sym=true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int i=0;i<k;i++) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm= int2d(Th)(ul*ul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

Of relevance to the Klein quartic (and indeed to Hurwitz surfaces in other genera) is
the (2, 3, 7) triangle. We include the code for its spectrum; as with the (2, 3, 8) triangle

121
CL)

and the pentagon in Appendix C, it is possible to add a Dirichlet condition to one or
more of its sides.

int n = 30;

int nev=100;

string fnm="237—Eigenvalues—n30—nev100.txt"; //file name for saving

real c = 2.012192172612278;

real r 1.74611492735219;

border Gl (t=0,0.2660772452600879) { x=t; y=0;};
border G2 (t=0.3007426187463789,0) { x=cos(pi/7)*t; y=t*sin(pi/7);};
border G3 (t=pi,3.066792828504322) { x=ctr*cos(t); y=rxsin(t);};

plot (G1(n)+G2(n)+G3(n));
mesh Th=buildmesh (G1(n)+G2(n)+G3(n));
plot (Th);

fespace Vh(Th,P2);

Vh ul, u2;
real sigma = 0.0005;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma*(4*ul*u2)/(1—x*2—y~2)~2);
varf b([ul] ,[u2]) = int2d(Th)((4*ul*u2)/(1—x*2-y~2)>2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);
matrix B=b(Vh, Vh, solver=CG, eps=le —20);

real[int] ev(nev);

Vh[int] eV(nev);

int k=EigenValue (OP,B,sym=true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int ji<k;it+) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm= int2d(Th)(ul*ul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

’ LJ
Next, we include the code for the surface M3 in [72]:

int n = 30;

int nev = 100;

string fnm="m3-Eigenvalues—n30—nev100.txt"; //file name for saving

real cx = 1.0122;
real cy = 0.1566;
real r = 0.2214;

real s = 0.8045;
real theta = 0.1238;

real x01 = sxcos(theta);

real y0Ol = sxsin(theta);

real x02 = sxcos(pi/6—theta);
real y02 = s*sin(pi/6—theta);
real x03 = sxcos(pi/6+theta);
real y03 = sxsin(pi/6+theta);
real x04 = s*cos(2*pi/6—theta);
real y04 = s*sin(2*pi/6—theta);
real x05 = sxcos(2*pi/6+theta);

122
real y05 = s*sin(2*pi/6+theta);

real x06 = s*cos(3*pi/6—theta

real y06 = s*sin(3*pi/6—theta);
real x07 = s*cos(3*pi/6+theta);
real y07 = s*sin(3*pi/6+theta);

real x08 = s*cos(4*pi/6—theta

real y08 = s*sin(4*pi/6—theta
real x09 = s*cos(4*pi/6+theta

real y09 = s*sin(4*pi/6+theta);
real x10 = s*cos(5*pi/6—theta);
real yl0 = s*sin(5*pi/6—theta);
real xll = s*cos(5*pi/6+theta);

real yll = s*sin(5*pi/6+theta

real yl2 = s*sin(6*pi/6—theta

real x13 = s*cos(6*pi/6+theta

real y13 = s*sin(6*pi/6+theta

real x14 = s*cos(7*pi/6—theta

real yl4 = s*sin(7*pi/6—theta

real yl5 = s*sin(7*pi/6+theta);

real x16 = s*cos(8*pi/6—theta);

real yl6 = s*sin(8*pi/6—theta);

real x17 = s*cos(8*pi/6+theta

real yl7 = s*sin(8*pi/6+theta);

real x18 = s*cos(9*pi/6—theta);

real y18 = s*sin(9*pi/6—theta);

)
)
)
)
)
)
)
)
)
)
)
)
)
real x12 = s*cos(6*pi/6—theta);
)
)
)
)
)
)
)
)
)
)
)
)
)
)

real x19 = s*cos(9*pi/6+theta);
real yl9 = s*sin(9*pi/6+theta);
real x20 = s*cos(10*pi/6—theta);
real y20 = s*sin(10*pi/6—theta);
real x21 = sxcos(10*pi/6+theta );
real y21 = s*sin(10*pi/6+theta);
real x22 = s*cos(11*pi/6—theta);
real y22 = s*sin(11*pi/6—theta);
real x23 = sxcos(1l*pi/6+theta);
real y23 = s*sin(11*pi/6+theta);
real x24 = sxcos(theta);

(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
real x15 = s*cos(7*pi/6+theta
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(

real y24 = sxsin(—theta);

border Gl (t=

border G2 (t=1l*xpi/12,15*pi/12) { x=cos(pi/6)*(cx+r*cos(t))—sin(pi/6)*(—cy—r«sin(t));
y=sin (pi/6)*(cx+r*cos(t))+cos(pi/6)*(—cy—r«*sin(t));};

border G3 (t=15*pi/12,11*pi/12) { x=cos(pi/6)*(cx+r*cos(t))—sin(pi/6)*(cy+r*sin(t));
y=sin(pi/6)*(cx+r*cos(t))+cos(pi/6)*(cy+r*sin(t));};

border G4 (t=1l*pi/12,15*pi/12) { x=cos(2*pi/6)*(cx+r*cos(t))—sin(2* pi/6)*(—cy—r*sin(t));
y=sin (2* pi /6)*(cx+r*cos(t))+cos(2* pi/6)*(—cy—r*sin(t));};

border G5 (t=15«pi/12,11*pi/12) { x=cos(2*pi/6)*(cxt+r*xcos(t))—sin(2* pi/6)*(cy+r*sin(t));
y=sin (2* pi /6)*(cx+r*cos(t))+cos(2* pi/6)*(cy+r*sin(t));};

border G6 (t=1l*xpi/12,15*pi/12) { x=cos(3*pi/6)*(cx+r*cos(t))—sin (3 pi/6)*(—cy—r*sin(t));
y=sin (3* pi /6)*(cx+r*cos(t))+cos(3* pi/6)*(—cy—r«*sin(t));};

border G7 (t=15*pi/12,11*pi/12) { x=cos(3*pi/6)*(cxt+r*cos(t))—sin(3*pi/6)*(cy+r*sin(t));
y=sin (3* pi /6)*(cx+r*cos(t))+cos(3* pi/6)*(cy+r*sin(t));}3

border G8 (t=1l*pi/12,15*pi/12) { x=cos(4*pi/6)*(cx+r*xcos(t))—sin(4* pi/6)*(—cy—r*sin(t));
y=sin (4* pi /6)*(cx+r*cos(t))+cos(4* pi/6)*(—cy—r*sin(t));};

border G9 (t=15*pi/12,11*pi/12) { x=cos(4*pi/6)*(cx+r*xcos(t))—sin(4* pi/6)*(cy+r*sin(t));
y=sin (4 pi /6)*(cx+r*cos(t))+cos(4* pi/6)*(cy+r*sin(t));};

border G10 (t=1l*pi/12,15*pi/12) { x=cos(5* pi/6)*(cx+r*cos(t))—sin (5 pi/6)*(—cy—r*sin(t));
y=sin (5* pi /6)*(cx+r*cos(t))+cos(5* pi/6)*(—cy—r*sin(t));};

border G11 (t=15*pi/12,11*pi/12) { x=cos(5*pi/6)*(cx+r*cos(t))—sin(5* pi/6)*(cy+r*sin(t));
y=sin (5* pi /6)*(cx+r*cos(t))+cos(5* pi/6)*(cy+r*sin(t));}3

border G12 (t=1l*pi/12,15*pi/12) { x=cos(6* pi/6)*(cx+r*cos(t))—sin (6 pi/6)*(—cy—r*sin(t));
y=sin (6* pi /6)*(cx+r*cos(t))+cos(6* pi/6)*(—cy—r*sin(t));};

border G13 (t=15*pi/12,11*pi/12) { x=cos(6*pi/6)*(cx+r*cos(t))—sin (6* pi/6)*(cy}+r*sin(t));

5xpi/12,11*pi/12) { x=cxtr*cos(t); y=cy+r*sin(t);

123
y=sin (6* pi /6)*(cx+r*cos(t))+cos(6* pi/6)*(cy+r*sin(t));};

border G14 (t=1l*pi/12,15*pi/12) { x=cos(7*pi/6)*(cx+r*cos(t))—sin(7* pi/6)*(—cy—r*sin(t));
y=sin (7* pi /6)*(cx+r*cos(t))+cos(7* pi/6)*(—cy—r*sin(t));};

border G15 (t=15*pi/12,11*pi/12) { x=cos(7*pi/6)*(cx+r*cos(t))—sin(7* pi/6)*(cy}+r*sin(t));
y=sin (7* pi /6)*(cx+r*cos(t))+cos(7* pi/6)*(cy+r*sin(t));}3

border G16 (t=1l*pi/12,15*pi/12) { x=cos(8*pi/6)*(cx+r*cos(t))—sin (8 pi/6)*(—cy—r*sin(t));

6)*(cx+rxcos(t))+cos(8* pi/6)*(—cy—r*sin(t));};

5xpi/12,11*pi/12) { x=cos(8*pi/6)*(cx+r*cos(t))—sin(8* pi/6)*(cy+r*sin(t));
y=sin (8* pi /6)*(cx+r*cos(t))+cos(8*pi/6)*(cy+r*sin(t));};

border G18 (t=1l*pi/12,15*pi/12) { x=cos(9*pi/6)*(cx+r*cos(t))—sin (9* pi/6)*(—cy—r*sin(t));
y=sin (9* pi /6)*(cx+r*cos(t))+cos(9* pi/6)*(—cy—r*sin(t));};

border G19 (t=15*pi/12,11*pi/12) { x=cos(9*pi/6)*(cx+r*cos(t))—sin(9* pi/6)*(cy+r*sin(t));
y=sin (9* pi /6)*(cx+r*cos(t))+cos(9* pi/6)*(cy+r*sin(t));};

border G20 (t=11l*pi/12,15*pi/12) { x=cos(10* pi/6)*(cx+r*cos(t))—sin(10* pi/6)*(—cy—r*sin(t));
y=sin (10« pi /6)*(cx+r«cos(t))+cos (10% pi/6)*(—cy—r«sin(t));};

border G21 (t=15*pi/12,11*pi/12) { x=cos(10* pi/6)*(cx+r*cos(t))—sin(10*pi/6)*(cy+r*sin(t));
y=sin (10« pi /6)*(cx+r*cos(t))+cos(10* pi/6)*(cy+r*sin(t));};

border G22 (t=1l*pi/12,15*pi/12) { x=cos(11*pi/6)*(cx+r*cos(t))—sin(11*pi/6)*(—cy—r*sin(t));
y=sin (11* pi /6)*(cx+r«*cos(t))+cos(11* pi/6)*(—cy—rx«sin(t));};

border G23 (t=15*pi/12,11*pi/12) { x=cos(11*pi/6)*(cx+r*cos(t))—sin(11*pi/6)*(cy+r*sin(t));
y=sin (11* pi/6)*(cx+r«*cos(t))+cos(11* pi/6)*(cy+r*sin(t));};

border G24 (t=11l*pi/12,15*pi/12) { x=cx+rxcos(t); y=-cy—r*sin(t);};

y=sin (8 pi/
border G17 (t

plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n)+G13(n)
+G14(n)+G15(n)+G16 (n)+G17(n)+G18(n)+G19(n)-+G20(n)+G21 (n)+G22(n)+G23(n)+G24(n));

mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n)+G13(n)+G14(n)+G15(n)+G16(n)+G17(n)+G18 (n)+G19(n)+G20(n)+G21 (n)+G22(n)+G23(n)
+G24(n) , fixeborder=true);

plot (Th, wait=true, fill—true);

fespace Vh(Th,P2, periodic =[[2,(cos(pi/12))*(y—y02)—(sin (pi/12))*(x—x02)],
[9 (cos (3% pi/12))*(y—y09)—(sin(—3*pi /12))*(x—x09)],
[4 (cos (3* pi /12))*(y—y04)—(sin (3* pi /12))*(x—-x04)],
[11 (cos (pi/12))*(y-y11)—(sin(—pi/12))*(x-x11)],
[6 ,(cos(5* pi /12))*(y—y06)—(sin (5* pi /12))*(x—x06)],
[13 ,(cos(pi/12))*(y—-y13)—(sin (pi/12))*(x-x13)],
[8 ,(cos(7* pi /12))*(y—y08)—(sin (7* pi /12))*(x—x08)],
[15 , (cos (3* pi /12))*(y—y15)—(sin (3* pi /12))*(x—x15)],
[10 , (cos (9* pi /12))*(y—y10)—(sin (9* pi /12))*(x—x10)],
[17 , (cos (5* pi /12))*(y—y17)—(sin (5* pi /12))*(x—x17)],
[12 ,(cos(11* pi /12))*(y-y12)—(sin (11* pi/12))*(x-x12)],
[19 , (cos (7* pi /12)) *(y—y19)—(sin (7* pi /12))*(x—x19)],
[14 ,(cos (13% pi /12))*(y-y14) —(sin (13% pi /12))*(x-x14)],
[21 , (cos (9* pi /12)) *(y—y21)—(sin (9* pi /12))*(x—x21)],
[16 ,(cos(15* pi /12))*(y—y16)—(sin (15* pi/12))*(x-x16)],
[23 ,(cos(11* pi /12))*(y—y23) —(sin (11* pi /12))*(x-x23)],
[18 ,(cos(17* pi /12))*(y—y18) —(sin (17* pi /12))*(x-x18)] ,
[1 , (cos (13* pi /12)) *(y—y01)—(sin (13% pi/12))*(x-x01)],
[20 ,(cos(19* pi /12))*(y—y20) —(sin (19% pi /12))*(x—x20)] ,
[3 , (cos (15* pi/12)) *(y—y03)—(sin (15% pi/12))*(x-x03)],
[22 ,(cos(21* pi /12))*(y—y22)—(sin (21* pi /12))*(x—x22)],
[5 ,(cos(17* pi /12)) *(y—y05)—(sin (17* pi/12))*(x-x05)],
[24 ,(cos (23% pi /12))*(y—y24) —(sin (23 pi /12))*(x-x24)],
[7 , (cos (19* pi /12)) *(y—y07)—(sin (19* pi /12))*(x-x07 )]]);

Vh ul, u2;

real sigma = 0.00001;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma*(4*ul*u2)/(1—x*2—y~2)~2);
varf b([ul] ,[u2]) = int2d(Th)((4*ul*u2)/(1—x*2-y~2)>2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);
matrix B=b(Vh, Vh, solver=CG, eps=le —20);

real[int] ev(nev);

124
Vh[int] eV(nev);

int k=EigenValue (OP,B,sym=true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int i=0;i<k;i++) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm= int2d(Th)(ul*ul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

}
12
13
18 19
Side associations:
2-9,4-11, 6 — 13, 8— 15, 10-17, 12-19,
14 — 21, 16 — 23, 18 — 1, 20 — 3, 22-5, 24-7
Figure D.1: Fundamental polygon for the surface M3
We also include the code for the Fermat quartic:
int n=30;

int nev=100;
string fnm="fermat_quartic—Eigenvalues—n30—nev100.txt"; //file name for saving
real cx = 1.0044;

real cy = 0.2275;
real r = 0.2463;

real s=0.7881;
real theta=0.1698;
real x01=s*cos (theta);

real y0l=s*sin(theta);

real x06=s*cos(3*pi/4—theta);

real y06=s*sin(3*pi/4—theta);
real x03=s*cos(pi/4+theta);
real y03=s*sin(pi/4+theta );
real x08=s*cos(pi—theta);

real y08=s*sin(pi—theta);

real x05=s*cos(pi/2+theta);
real y05=s*sin(pi/2+theta);
real xl0=s*cos(5*pi/4—theta

real yl0=s*sin(5*pi/4—theta);
real x07=sxcos(3*pi/4+theta);

i/4—theta
real yl2=s*sin(6*pi/4—theta

real x12=s*cos(6*p

)
( )
( )
real y07=s*sin(3*pi/4+theta )
( )
( )

real x09=s*cos(pi+theta);
real y09=s*sin(pi+theta);
real xl4=s*cos(7*pi/4—theta);
real yl4=s*sin(7*pi/4—theta);
)
)

(

real xll=s*cos(5«pi/4+theta
real yll=s*sin(5*pi/4+theta);
real xl6=s*cos(theta);

real yl6=s*sin(—theta);

real x13=s*cos(6*pi/4+theta);
real yl3=s*sin(6«pi/4}theta);
real x02=s*cos(pi/4—theta);
real y02=s*sin(pi/4—theta);
real x15=s*cos(7*pi/4+theta);
real yl5=s*sin(7*pi/4+theta);
real x04=s*cos(pi/2—theta);
real y04=s*sin(pi/2—theta);

border Gl (t=1l«xpi/8,7*pi/8) { x=cxtr*cos(t); y=cyt+r*sin(t);};

border G2 (t=7*pi/8,ll*pi/8) { x=cos(pi/4)*(cx+r*cos(t))—sin(pi/4)*(—cy—r*sin(t));
y=sin(pi/4)*(cx+r*cos(t))+cos(pi/4)*(—cy—r«*sin(t));};

border G3 (t=1ll*pi/8,7*pi/8) { x=cos(pi/4)*(cx+r*cos(t))—sin(pi/4)*(cy+r*sin(t));
y=sin(pi/4)*(cx+r*cos(t))+cos(pi/4)*(cy+r*sin(t));};

border G4 (t=7*pi/8,ll*pi/8) { x=cos(pi/2)*(cx+r*cos(t))—sin(pi/2)*(—cy—r*sin(t));
y=sin (pi/2)*(cx+r*cos(t))+cos(pi/2)*(—cy—r«*sin(t));};

border G5 (t=11l*pi/8,7*pi/8) { x=cos(pi/2)*(cx+r*cos(t))—sin(pi/2)*(cy+r*sin(t));
y=sin(pi/2)*(cx+r*cos(t))+cos(pi/2)*(cy+r*sin(t));};

border G6 (t=7*pi/8,l1l*pi/8) { x=cos(3* pi/4)*(cx}r*cos(t))—sin(3*pi/4)*(—cy—r«*sin(t));
y=sin (3% pi /4)*(cx+r*cos(t))+cos(3* pi/4)*(—cy—r«*sin(t));};

border G7 (t=ll*pi/8,7*pi/8) { x=cos(3*pi/4)*(cx+r*cos(t))—sin(3*pi/4)*(cyt+r*sin(t));
y=sin (3* pi /4)*(cx+r*cos(t))+cos(3* pi/4)*(cy+r*sin(t));};

border G8 (t=7*pi/8,ll*pi/8) { x=cos(pi)*(cx}+r*cos(t))—sin(pi)*(—cy—r*sin(t));
y=sin (pi) *(cx+r*cos(t))+cos(pi)*(—cy—r«*sin(t));};

border G9 (t=1l*xpi/8,7*pi/8) { x=cos(pi)*(cx}+r*cos(t))—sin(pi)*(cy+r*sin(t));
y=sin (pi) *(cx+r*cos(t))+cos(pi)*(cy+resin(t));};

border G10 (t=7*pi/8,11*pi/8) { x=cos(5*pi/4)*(cx+r*cos(t))—sin(5* pi/4)*(—cy—re*sin(t));
y=sin (5% pi /4)*(cx+r*cos(t))+cos(5* pi/4)*(—cy—r*sin(t));};

border G11 (t=1l*pi/8,7*pi/8) { x=cos(5*pi/4)*(cx+r*cos(t))—sin(5*pi/4)*(cyt+r*sin(t));
y=sin (5* pi /4)*(cx+r*cos(t))+cos(5* pi/4)*(cy+r*sin(t));};

border G12 (t=7*«pi/8,11*pi/8) { x=cos(6*pi/4)*(cx}r*cos(t))—sin (6* pi/4)*(—cy—re*sin(t));
y=sin (6* pi /4)*(cx+r*cos(t))+cos(6* pi/4)*(—cy—r«*sin(t));};

border G13 (t=1l*pi/8,7*pi/8) { x=cos(6*pi/4)*(cx+r*cos(t))—sin(6*pi/4)*(cy+r*sin(t));
y=sin (6 pi /4)*(cx+r*cos(t))+cos(6* pi /4)*(cy+r*sin(t));}3

border G14 (t=7«pi/8,11*pi/8) { x=cos(7*pi/4)*(cx}r*cos(t))—sin(7* pi/4)*(—cy—re*sin(t));
y=sin (7* pi /4)*(cx+r*cos(t))+cos(7* pi/4)*(—cy—r*sin(t));};

border G15 (t=1l*pi/8,7*pi/8) { x=cos(7*pi/4)*(cx+r*cos(t))—sin(7*pi/4)*(cyt+r*sin(t));
y=sin (7* pi /4)*(cx+r*cos(t))+cos(7*pi/4)*(cy+r*sin(t));};

border G16 (t=7*pi/8,11*pi/8) { x=cxjr*cos(t); y=-cy—r*sin(t);};

plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n)+G13(n)
+G14(n)+G15(n)+G16(n));

mesh Th=buildmesh (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n)+G13(n)+G14(n)+G15(n)+G16(n) , fixeborder=true );

126
plot (Th, wait=true , fill=true);

fespace Vh(Th,P2, periodic =[[1,cos(pi/8)*(y—y01)—sin(pi/8)*(x—x01)],
[6 , cos (3* pi/8)*(y—y06)—sin(—3* pi/8)*(x—x06)],
[3 , cos (3* pi /8) *(y—y03)—sin (3% pi/8)*(x—x03)],
[8 , cos (pi/8) *(y—y08)—sin(—pi/8) *(x-x08)],
[5 , cos (5* pi/8)*(y—y05)—sin (5* pi/8)*(x—x05)],
[10 ,cos(pi/8)*(y—y10)—sin (pi/8)*(x-x10)],
[7 , cos (7* pi/8) *(y—y07)—sin (7* pi/8)*(x—x07)],
[12 , cos (3* pi /8)*(y—y12)—sin (3 pi/8)*(x—x12)],
[9 , cos (9* pi /8) *(y—y09)—sin (9% pi/8)*(x—x09)],
[14 cos (5% pi/8)*(y—y14)—sin (5* pi/8)*(x—x14)],
[11 ,cos(11* pi/8)*(y—y11)—sin (11* pi/8)*(x-x11)],
[16 ,cos(7* pi /8)*(y—y16)—sin(7* pi/8)*(x—x16)],
[13 , cos(13* pi/8)*(y—y13)—sin (13% pi/8)*(x-x13)],
[2 , cos (9* pi /8) *(y—y02)—sin (9% pi/8)*(x—x02)],
[15 ,cos(15* pi/8)*(y—y15)—sin (15% pi/8)*(x—-x15)],
[4 cos (11* pi /8)*(y—y04)—sin (11* pi /8) *(x—x04 )]]);

Vh ul, u2;

real sigma = 0.00001;

varf op(ul,u2)= int2d(Th)(dx(ul)*dx(u2)+ dy(ul)*dy(u2)— sigma*(4*ul*u2)/(1—x*2—y~2)~2);
varf b([ul] ,[u2]) = int2d(Th)((4*ul*u2)/(1—x*2-y~2)>2);

matrix OP= op(Vh,Vh, solver=Crout , factorize=1);
matrix B=b(Vh, Vh, solver=CG, eps=le —20);

real[int] ev(nev);
Vh[int] eV(nev);

int k=EigenValue (OP,B,sym=true , sigma=sigma , value=ev , vector=eV, tol=le—10,maxit=0,ncv=0);
for (int i=0;i<k;i++) {

ul=eV [i];

real gg = int2d(Th)(dx(ul)*dx(ul) + dy(ul)*dy(ul)); real mm= int2d(Th)(ul*ul) ;

ofstream Eva(fnm, append);

Eva << ev[i] << "\n";

}

Remark D.1 The observant reader will recognize 2 in Table D.3 - it is roughly equal to
the first positive eigenvalue of the Bolza surface! Moreover, it appears to habe the same

multiplicity. In fact, if one takes the subset of eigenvalues in Table D.3 With multiplicity
1, 2 or 8, one finds that they match the subset of eigenvalues of Table C.1, and that

the multiplicities are the same. coincidence. Recall the presentation of the

automorphism group given in Chapter 1:

(a, b,c

a’ = b8 = c? = (ab)? = (ab)? = (a*b’)? = acac = bebe = e) ,

where a is a rotation of order 8 around the centre of the fundamental 16-gon, b is a
rotation of order 3 arownd one of the 32 (4,4,4) triangles that can be used to tessellate
the surface (note this is twice as many as in the case of the Bolza surface), and c is a
reflection in the real line. As we have done with the Bolza surface and Klein quartic, we

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
7P la 2a 2b 3a 4a 2c 2d 8a 4b 8b 4c 4d 6a 2e

X.1 1121212212222 21223232232 «*212
X.2 1-1-1 1 212 2 2-1-1-1-1 21212
X.3 1-1 1 21 21 2-1-1 -1 1 1 #1 -1-1
X.4 1 1-1 1 1 2-1 2 «2-1-1 «1-1-1
X.5 2 -1 22-2... =. 2 1-2
X.6 2 »--1 22 2 . . . . 2-1 2
X.7 3-1 -1 -1 3 i =i i =i =i =
X.8 3-1 1 -1 3-3 1-1-1 1-1. 1
X.9 3 1-1 -1 3-3-1 1 1-1-1. 1
X.10 3 11 -1 3 3-1 1-1 1-1 .-1
X.11 6 —2 2-2 2 —2

XK.12 6 —2 —2 -2 2

X.13 6 . 2 .-2-2 . . . . -2

X.14 6 2. . 2-2 . .-2 . . -2

gap> chi:=Irr(f);;

gap> IrreducibleA ffordingRepresentation (chi [1]);

[ fl, #2, 8 J] >{f[ [ft] 1,011], T0111)

gap> IrreducibleA ffordingRepresentation (chi [2]);

[ fl, 2, f8 JST a}],0l1)),¢la11)

gap> IrreducibleA ffordingRepresentation (chi [3]);

[ f1, #2, 8 J] >f[f-1]], 111, 2) 11

gap> IrreducibleA ffordingRepresentation (chi [4]);

[ fl, #2, 8 J] >f [ft] 1,011], 6-2) 11

gap> IrreducibleA ffordingRepresentation (chi [5]);

[ fl, #2, £8 ] > [ [ [ 0, -1], [ -1,0] ], [ [ B(3)°2, 0], [ 0, E(3) J J,
[10,1], [1,0] ]]

gap> IrreducibleA ffordingRepresentation (chi [6]);

[ fl, 2, 8 |S [ [10,1], 11,0] |, [| [ £(3)72, 0], | 0, B(3) | J,
[10,1], [1,0] ]]

gap> IrreducibleA ffordingRepresentation (chi [7]);

[ fl, £2, £8 ] > [[[0, 1,0], [| -1,0,0], [0,0,1] ],
{[0,1,0], [ 0, 0,1], [ 1, 0,0] ],

[ [ 0, -1,0], [ -1, 0,0], [ 0, 0, -1] ] ]
gap> IrreducibleA ffordingRepresentation (chi [8]);

[ fl, £2, £8 ] > [[[ 0, 1,0], [| -1,0,0], [0,0,1] ],
{[0,1,0], [ 0, 0,1], [ 1, 0,0] ],
{10,1,0], [ 1, 0,0], [0,0,1]]]

gap> IrreducibleA ffordingRepresentation (chi [9]);

[ fl, f2, £8 |] ~ [ [ [ 0, -1, 0], [ 1, 0, 0 ], [ 0, 0, -1 ] J,
{[0,1,0], [ 0, 0,1], [ 1, 0,0] ],

{ [ 0, -1,0], [ -1, 0,0], [ 0,0,-1]] ]
gap> IrreducibleA ffordingRepresentation (chi[10]);
[ fl, f2, £8 |] ~ [ [ [ 0, -1, 0], [ 1, 0, 0 ], [ 0, 0, -1 ] J,

{[0,1,0], [ 0, 0,1], [ 1, 0,0] ],

{10,1,0], [ 1, 0,0], [0,0,1]]]
gap> IrreducibleA ffordingRepresentation(chi[11]);

[ fl, £2, £8 ] >

[tl

, 1, 0, 0, 0, 0 ], [ E(4)

, 0, 0,0], [ 0, 0, E(4), 0, 0, 0 ],

[ [ 0, 0, 0, 1, 0, 0], [ 0, 0, 0, 0, 1, 0], [ 0, 0, 0, 0, 0,1],

[ 1, 0, 0, 0, 0, 0], [ O, 1, 0, 0, 0, oO], [ 0, O,
gap> IrreducibleAffordingRepresentation (chi[12]);
[ fl, £2, £3 | >

[ | [ 0, 0, 0, 1, 0, 0], [ 0, 0, 0, 0, 1, 0 J], [ 0, 0, 0,
[ -E(4), 0, 0, 0, 0, 0], [ 0, 1, 0, 0, 0, 0 J, [ 0,

], [ | 0, 1, 0, 0, 0, 0], [ 0, 0, 1, 0, 0, 0}, [ 1,

[ 0, 0, 0, 0, 0, -E(4) J], [ 0, 0, 0, E(4), 0, 0 J, [

I;
{ [ 0, 0, -1, 0, 0, 0], [ 0, -1, 0, 0, 0, 0 J, [ -1, 0,
[ 0, 0, 0, 0, 0, E(4) J], [ 0, 0, 0, 0, -1, 0],
[ 0, 0, 0, -B(4), 0,0] ] ]
gap> IrreducibleAffordingRepresentation(chi[13]);
[ f1, £2, £8 ] >

[ | [ 0, 0, 0, 1, 0, 0], [ 0, 0, 0, 0, 1, 0 J], [ 0, 0, 0,
[ -E(4), 0, 0, 0, 0, 0], [ 0, 1, 0, 0, 0, 0 J, [ 0,
], [ | 0, 1, 0, 0, 0, 0], [ 0, 0, 1, 0, 0, 0}, [ 1,
[ 0, 0, 0, 0, 0, -E(4) J], [ 0, 0, 0, E(4), 0, 0 J, [
], [ | 0, 0, 1, 0, 0, 0], [ 0, 1, 0, 0, oj, [ 1,
[ 0, 0, 0, 0, 0, -E(4) J], [ 0, 0, 0, 0, 1, 0], [ 0,
1]
gap> IrreducibleAffordingRepresentation(chi[14]);
[ fl, £2, £3 ]
[ [ [ 0, 1, 0, 0, 0, 0 J, [ B(4), 0, 0 , 0,0], [ 0, 0,
[ 0, 0, 0, 0, -E(4), 0], [ 0, 0 , 1, 0,0], [ 0,
], [ [ 0, 0, 1, 0, 0, 0], [ 1, 0, 0, 0, 0, 0}, [ 0,
{[ 0, 0, 0, 0, 1, 0], [ 0, 0, 0, 0, 0, 1 J, 0, 0

if
[ [ 0, 0, 0, 1, 0, 0], [ 0, 0, 0, 0, 1, 0 J], [ 0, 0, 0,
[ 1, 0, 0, 0, 0, 0], [ 0, 1, 0, 0, 0, 0], [

130

0, 0,1
0, E(4),
0, 0, 0,
0, 0, 0,
0, 0, 0,
0, 0, B(4
-E(4), 0,
0, 0, 0, 0
1, 0, 0, 0
0, 1, 0, 0
0, 0,14,
1, 0, 0, 0

ooroo
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
