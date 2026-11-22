---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-023-mathematica-code-for-bolza-surface
section_title: "Mathematica Code for Bolza Surface"
section_number: null
pages: 150-153
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
The following block of code helps us to choose the optimal value of L to deﬁne the
spectral function h(t) in Section 3.4.
We ﬁrst deﬁne “lemult” as the ordered list of
lengths of geodesics in the length spectrum, using the formula in Section 3.2, along with
their multiplicities. Note that only the multiplicity of the ﬁrst length in the spectrum is
precise; all others have been calculated numerically. Also note that whilst the multiplicity
of the systole of the Bolza surface is 12, here we are concerned about moving along the
geodesic in both a positive and negative direction, so we double the multiplicity to take
this into account. We then use “les” to ﬂatten this into one list, rather than a list of pairs,
where each length appears multiple times.
We deﬁne the spectral function
h(x, L) =
sin Lx
Lx
4
,
along with its Fourier transform g(ξ, L), and the derivative of the Fourier transform,
gd(x, L). Note that all of these are functions of L as well as the usual variable.
For a given value of L, the function “multbound” calculates the bound on the mul-
tiplicity of the ﬁrst eigenvalue, using the method described in Section 3.4. Finally, we
can use Mathematica’s “DiscretePlot” function to plot the bounds on m given by “mult-
bound(L)” for values of L between 0.4 and 1, with a step size of 0.01. The output is
shown in Figure F.1, where we see that L =
93
100 gives the lowest bound.
lemult = {{2 ArcCosh [ 1 + Sqrt [ 2 ] ] ,
24} ,
{2 ArcCosh [3 + 2
Sqrt [ 2 ] ] ,
24} ,
{2 ArcCosh [5 + 3
Sqrt [ 2 ] ] ,
48} ,
{2 ArcCosh [7 + 5
Sqrt [ 2 ] ] ,
96} ,
{2 ArcCosh [9 + 6
Sqrt [ 2 ] ] ,
48} ,
{2 ArcCosh [9 + 7
Sqrt [ 2 ] ] ,
48} ,
{2 ArcCosh [11 + 8
Sqrt [ 2 ] ] ,
8} ,
{2 ArcCosh [13 + 9
Sqrt [ 2 ] ] ,
96}};
l e s = Flatten [
Table [ Table [ lemult [ [ i ] ] [ [ 1 ] ] ,
{k ,
1 ,
lemult [ [ i ] ] [ [ 2 ] ] } ] ,
{ i ,
1 ,
8 } ] ] ;
140
h [x_, L_] = ( Sin [ L x ] / ( L x))^4
g [ \ [ Xi ]_, L_] = FourierTransform [ h [ t , L ] ,
t ,
\[ Xi ] ] / Sqrt [2
Pi ]
Zer [x_] = 0;
gd [x_, L_] = D[ g [ x , L ] ,
x ]
/.
{ Sign ’−>Zer}
multbound [L_]:=( h [x_]=h [ x , L ] ;
␣␣␣␣g [ \ [ Xi ]_]=g [ \ [ Xi ] , L ] ;
␣␣␣␣gd [x_]=gd [ x , L ] ;
␣␣␣␣RightSide=−2NIntegrate [ gd [ x ]/ Sinh [ x /2] ,{ x ,0 ,4L}]+
␣␣␣␣Sum[Sum[ l e s [ [ i ] ] g [ k∗l e s [ [ i ] ] ] / ( 2 Sinh [ k∗l e s [ [ i ] ] / 2 ] ) , { i , 1 , Length [ l e s ] } ] , { k , 1 , 1 0 } ] ;
␣␣␣␣( RightSide−h [ I /2])/ h [ Sqrt [116469/28089 −1/4]])
DiscretePlot [ multbound [ L] , {L , 0 . 4 , 1 . 0 , 0 . 0 1 } ]
0.5
0.6
0.7
0.8
0.9
1.0
6
7
8
9
10
11
Figure F.1: Output of the function “multbound” for diﬀerent values of L
We also include the code used to produce Figure 3.19.
Here we construct a test
function to satisfy the hypothesis of Corollary 3.17, and plot its nodal line as a function
of t. We superimpose this plot of the nodal line against a plot of the boundary of the
annulus considered in Section 3.4.1 to show that the test function is positive inside the
desired region.
(∗
Eigenvalue
∗)
\[ Lambda ] = 5 . ;
(∗
Length
of
core
geodesic
∗)
e l l = 2.
ArcCosh [1/2
Csc [ \ [ Pi ] / 8 ] ] ;
(∗
Hypergeometric
f u n c t i o n s
with
eigenvalue
\ [ Lambda ] .
For
efunc1 ,
\
141
the m variable gives the restriction of the eigenfunction to the mth \
Fourier node *)
efunc0 [\[Rho]_] =
Re[ Evaluate [
Sinh [\[Rho]] Hypergeometric2F1[(3/2 + I Sart[\[Lambda] — 1/4])/
2, (2 — (1/2 + I Sart [\[Lambda] — 1/4]))/2,
3/2, —Sinh[\[Rho]]~2] ]];
efuncl [\[Rho]_, m_] =
Re[ Evaluate [
Sinh [\[Rho]] Cosh[\[Rho]]*(2 Pi I m/
ell) Hypergeometric2F1[(3/2 + I Sart [\[Lambda] — 1/4])/2 +
Im Pifell, (2 — (1/2 + I Saqrt[\[Lambda] — 1/4]))/2 +
Pi Im /ell, 3/2, —Sinh[\[Rho]]*2] ]];

(« Nodal Line as a function of t. *)
\ [Rho] zero [
t_] := (\[Rho] /.
FindRoot [
efunc0[\[Rho]] — (0.038 Sin[2 Pi (t)/ell — Pi/2]) efuncl[\[Rho],
1] — (0.0002 Cos[2 2 Pi (t)/ell]) efuncl[\[Rho], 2], {\[Rho],
0.5, 1.9}]);
nodal = Plot[{\[Rho] zero[t]}, {t, 0, ell }];

(* Parametric plot of boundary of annulus «)
xl = Cos[2 Pi t/ell];
yl = Sin[2 Pi t/ell];
x2 = 4.61158 Cos[2 Pi t/ell];
61158 Sin[2 Pi t/ell];
.0986840182524393 + 0.4550896306919397 Cos[2 Pi t/ell];
.4550896306919397 Sin[2 Pi t/ell];
.0986840182524393 + 0.4550896306919397 Cos[2 Pi t/ell];
.4550896306919397 Sin[2 Pi t/ell];
.5537741953480246 + 1.3820929243421862 Cos[2 Pi t/ell];
-3820929243421862 Sin[2 Pi t/ell];
.066671210777469 + 2.0986830534021754 Cos[2 Pi t/ell];
y5 = 2.0986830534021754 Sin[2 Pi t/ell];
boundary =
ParametricPlot [{{Log[Sqrt[y172 + x1>2]],
ArcSinh[xl/yl]}, {Log[Sqrt[y272 + x2>2]],
ArcSinh[x2/y2]}, {Log[Sqrt[y3*2 + x3>2]],
ArcSinh [x3/y3]}, {Log[Sart[y4*2 + x4~2]],
ArcSinh [x4/y4]}, {Log[Saqrt[y5*2 + x5~2]], ArcSinh[x5/y5]}}, {t,
0.0001, ell}, AspectRatio > Automatic, PlotRange —> All];

y4 =

wo
|
arnNnorFrorRA

x5 =

(* Superimpose nodal line plot onto boundary of annulus *)

\
Show[nodal, boundary, PlotRange —> {{0, 1.6}, {1, 2.3}}]

142
Appendix G
