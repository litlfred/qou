---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-044-runge--kutta-methods
section_title: "Runge--Kutta methods"
section_number: null
pages: 50-52
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The Runge-Kutta (RK) class of methods are possibly the most frequently used algorithms for numerically solving ODEs.
Among them, perhaps the most successful during more than half a century has been the 4th-order method, which, applied
to Eq. (224), provides the following numerical approximation for the integration step t, > thy: = th +h:

Y; =Xn

h
Y2 = Xn + hltn, Ys)
h h
Ys = 1+ 58( t+ 5.¥ (227)
h
Yq = Xp, + hf | t+ 7%3

h h h
Knut = Xa te (f1.¥) + 2t(t + A) + 2t(t + a) + (ty + nv.) .

Notice that the function f can always be computed explicitly because each Y; depends only on the Yj, j < i, previously
evaluated. To measure the computational cost of the method, it is usual to consider that the evaluation of the function f(t, x)
is the most consuming part. In this sense, scheme (227) requires four evaluations, which is precisely the number of stages
(or inner steps) in the algorithm.

The general class of s-stage Runge-Kutta methods are characterized by the real numbers aj, bj (i,j = 1,...,5) and

§
Ci = Dijan aij, aS

s
Yi=X th) ayfltr +GhY), i=1....s
j=l
s
Xnu1 = Xn tM) bi fla + cit, Yi), (228)
i=1
where Y;,i = 1,..., s are the intermediate stages. For simplicity, the associated coefficients are usually displayed with the

so-called Butcher tableau [125,126] as follows:

(229)

If aj = 0,j = i, then the intermediate stages Y; can be evaluated recursively and the method is explicit. In that case, the
zero aj coefficients (in the upper triangular part of the tableau) are omitted for clarity. With this notation, ‘the’ 4th-order
Runge-Kutta method (227) can be expressed as

(230)

BNIB NIE O
oONe

1
6

IN| One

1

1 2

6 6
Otherwise, the scheme is implicit and requires one to numerically solve a system of sd nonlinear equations of the form

y=X, +hG(h,y), (231)

wherey = (Y;,..., Ys)", Xn = (Xn, .--,Xn)" € R™, and Gis a function which depends on the method. A standard procedure
to get Xn+1 from (231) is applying simple iteration:

yl =x,+hn6(h,y"), j=1,2,.... (232)

When h is sufficiently small, the iteration starts with y'°! = X, and stops once ||y! — y¥-"|| is smaller than a prefixed
tolerance. Of course, more sophisticated techniques can be used [126].

After these general considerations, let us now turn our attention to the linear equation (223). When dealing with
numerical methods applied to this equation, it is important to keep in mind that the relevant small parameter here is no
longer the norm of the matrix A(t) as in the analytical treatment, but the time step h. For this reason, the concept of order of
S. Blanes et al. / Physics Reports 470 (2009) 151-238 201

accuracy of a method is different in this context. Now f(t, x) = A(t)x and the general class of s-stage Runge-Kutta methods
adopt the more compact form

5
YHx tn aA, i=1,...,5
j=l

s
Xn = Xn + BAY, (233)

i=1

with A; = A(t, + cjh). In terms of matrices, this is equivalent to

Y Xn 7 Y; 7 QA, +++ Q4sAs
Dps=y ig thAy se, withA= : :
Y; Xn Y; Gs;A, ++: dssAg
Yi
Xng1=Xath(biAr ++» bAs)} 2 fp, (234)
Ys

so that the application of the method for the integration step t, > th41 = tn + h can also be written as
~ 1
Xn41 = (1 +h(biA, +++ BsAs) (Isa — hA) Isdxa) Xn, (235)

where I¢xa = (la, Id, ..-, 1g)" and Iy is the d x d identity matrix. For instance, taking s = 2 and using Matlab this can be
easily implemented as follows

A= [a11*A1 al12%*A2; a21%*A1 a22 x A2];
X= (Id+hx[b1*A1 b2* A2] x ((I2d —h x A) \ [Id Id]')) * x;

where b1, b2,a11,...,a22 are the coefficients of the method, Al, A2 correspond to A;, Az and Id, [2d are the identity
matrices of dimension d and 2d, respectively.

There is extensive literature regarding RK methods built for many different purposes [125,126]. It is therefore reasonable
to look for the most appropriate scheme to be used for each problem. In practice, explicit RK methods are preferred, because
its implementation is usually simpler. They typically require more stages than implicit methods and, in general, a higher
number of evaluations of the matrix A(t), although this is not always the case. For instance, the 4-stage fourth order method
(227) only requires two new evaluations of A(t) per step (A(t, + h/2) and A(t, + h)), which is precisely the minimum
number of evaluations needed by any fourth order method. In our numerical examples, we will also use the 7-stage sixth
order method with coefficients [125, p. 203-205]

0
5-v5 5-V/5
10 10
5t+v5 -v5 5425
10 10 10
5s-V5 | =1547V5  -14- V5 15-7.V5
10 20 4 10
54/5 5—J/5 0 1 1547/5 (236)
10 60 6 60
5-5 54+V5 0 9-55 1 =543V5
10 60 12 6 10
1 i 0 =55:425V5 =25-105 5-2/5 StS
1 5 5 1
= 0 0 0 a a D2

Observe that this method only requires three new evaluations of the matrix A(t) per step. This is, in fact, the minimum
number for a sixth-order method. Other implicit RK schemes widely used in the literature involving the minimum number
of stages at each order are based on Gauss-Legendre collocation points [126]. For instance, the corresponding methods of
order four and six (with two and three stages, respectively) have the following coefficients:

5-V15 — 2_ V5 5 _ V15
3/3 1 3-2/3 10 36 9 i 36 30
6 4 12 1 54 VB 2 54 V5
34v3 | 34+2V3 1 2 36 ' 24 9 36 24 (237)
6 12 4 s+V15 | 5 4 V5 24 v5 5
1 1 10 36 ET 9 T 36
2 2 S 4 5

18 9 18
202 S. Blanes et al. / Physics Reports 470 (2009) 151-238
