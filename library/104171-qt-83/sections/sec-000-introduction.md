---
doc_id: 104171-qt-83
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-14
source_pdf: 10.4171-qt-83.pdf
source_sha256: d95b9363de2766d2
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
---
2 Calculation of the Kashaev invariant of the 52 knot . . . . . . . . . . . . 675
3 Calculation by the saddle point method . . . . . . . . . . . . . . . . . . 682
4 Calculation by the Poisson summation formula . . . . . . . . . . . . . . 693
5 Proof of Theorem /one.prop./one.prop. . . . . . . . . . . . . . . . . . . . . . . . . . . . 704
A Properties of'.t/ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 723
B Convergence ofV.t;s/ to yV.t;s/ . . . . . . . . . . . . . . . . . . . . . . 726
C Critical points of V.t;s/ and yV.t;s/ . . . . . . . . . . . . . . . . . . . . 728
D Proof of Lemma /two.prop./one.prop. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 730
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 731
1 This research was partially supported by JSPS KAKENHI Grant Number /two.prop/four.prop/three.prop/four.prop/zero.prop/zero.prop/one.prop/two.prop.
670 T. Ohtsuki
/one.prop. Introduction
In [/one.prop/six.prop] and [ /one.prop/seven.prop] Kashaev de/f_ined the Kashaev invariant hLiN 2 C of a link L for
N D 2;3;    by using the quantum dilogarithm. In [ /one.prop/eight.prop] he conjectured that, for
any hyperbolic linkL,
2  lim
N !1
loghLiN
N D vol.S3 /NULL/;
where “vol” denotes the hyperbolic volume, and gave evidenc e for the conjecture
for the /f_igure-eight knot, the52 knot and the 61 knot, by formal calculations. In
/one.prop/nine.prop/nine.prop/nine.prop, H. Murakami and J. Murakami [/two.prop/four.prop] proved that the Kashaev invariant hLiN
of any link L is equal to the N -colored Jones polynomial JN.LIe2
p
/NUL 1=N/ of
L evaluated at e2
p
/NUL 1=N , where JN.LIq/ denotes the invariant obtained as the
quantum invariant of links associated with the N -dimensional irreducible repre-
sentation of the quantum group Uq.sl2/. Further, as an extension of Kashaev’s
conjecture, they conjectured that, for any knot K,
2  lim
N !1
log jJN.KIe2
p
/NUL 1=N/j
N D vol.S3 /NULK/;
where “vol” in this formula denotes the simplicial volume (n ormalized by multi-
plying by the hyperbolic volume of the regular ideal tetrahe dron). This is called
the volume conjecture. As a complexi/f_ication of the volume conjecture, it is con-
jectured in [/two.prop/five.prop] that, for a hyperbolic link L,
2
p
/NUL1  lim
N !1
logJN.LIe2
p
/NUL 1=N/
N D cs.S3 /NULL/ C
p
/NUL1vol.S3 /NULL/ (1)
for an appropriate choice of a branch of the logarithm, where “cs” denotes the
Chern–Simons invariant. Furthermore, it is conjectured [ /one.prop/one.prop] (see also [ /three.prop], [ /one.prop/two.prop],
and [ /four.prop/six.prop]) from the viewpoint of the SL .2; C/ Chern–Simons theory that the
asymptotic expansion of JN.KIe2
p
/NUL 1=k/ of a hyperbolic knot K asN;k ! 1
/f_ixingu DN=k is given by the form
JN.KIe2
p
/NUL 1=k/ 
N;k!1
uDN=k W /f_ixed
eN&N3=2! 

1 C
1X
i D1
i 
2
p
/NUL1
N
i
(2)
for some scalars &;!; i depending on K andu, though they do not discuss the
Jones polynomial in the Chern–Simons theory in the case of va nishing quantum
dimension, which is discussed in [ /three.prop/eight.prop]. These conjectures look interesting in
the sense that they make a bridge between quantum topology an d hyperbolic
geometry, and it suggests the existence of a future theory be tween them.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 671
An approach toward a proof of the volume conjecture has been k nown, which
is due to Kashaev [ /one.prop/eight.prop], Thurston [ /three.prop/five.prop] and Y okota [ /four.prop/two.prop]. We brie/f_ly review this
approach, as follows. By de/f_inition, the Kashaev invarianthKiN (which we review
in Section /two.prop./one.prop) of a knotK is given by a sum of fractions whose denominators are
product of copies of .q/n, where
q D exp
2
p
/NUL1
N

and
.x/n D.1 /NULx/.1 /NULx2/   .1 /NULxn/I
for example, the Kashaev invariant h52iN of the52 knot is given by
h52iN D
X
0i;j
i Cj<N
N3q
.q/i Cj.q/N /NUL i /NUL j /NUL 1.q/j. Nq/j. Nq/i
;
as shown in ( /seven.prop). By the approximation
.q/n  exp
 N
2
p
/NUL1
.Li2.1/ /NUL Li2.e2n
p
/NUL 1=N//

;
we expect
h52iN 
‹
N3q
X
0i;j
i Cj<N
exp
 N
2
p
/NUL1
{V.e2
p
/NUL 1i=N;e2
p
/NUL 1j=N/

;
where we put
{V.x;y/ D Li2.xy/ C Li2
 1
xy

C Li2.y/ /NUL Li2
1
y

/NUL Li2
1
x

/NUL Li2.1/:
Further, by formally replacing the sum with an integral putt ing t D i=N and
s Dj=N , we expect that
h52iN 
‹‹
N5q
Z
0t;s
tCs1
exp
 N
2
p
/NUL1
{V.e2
p
/NUL 1t;e2
p
/NUL 1s/

dtds:
Furthermore, by applying the saddle point method, we expect that the asymptotic
behavior might be described by a critical value of {V . Y okota [/four.prop/two.prop] showed that a
critical value of such a function {V is given by the hyperbolic volume of the knot
complement. There are problems justifying this series of ar guments.
672 T. Ohtsuki
The volume conjecture has been rigorously proved for some pa rticular knots
and links such as torus knots [/one.prop/nine.prop] (see also [/five.prop]1), the /f_igure-eight knot (by Ekholm,
see also [/one.prop]2), Whitehead doubles of.2;p/ -torus knots [/four.prop/seven.prop], positive iterated torus
knots [ /three.prop/seven.prop], the 52 knot [ /two.prop/zero.prop], and some links [ /nine.prop], [ /one.prop/five.prop], [ /three.prop/six.prop], [ /three.prop/seven.prop], [ /four.prop/one.prop], [ /four.prop/seven.prop]; for
details see e.g. [ /two.prop/two.prop]. They (except for the 52 knot) have particular properties; for
example, the simplicial volumes of the complements of torus knots are 0, and
a critical point of {V for the /f_igure-eight knot is on the original contour of the
integral. The volume conjecture for them has been proved by using such particular
properties. In particular, the 52 knot is of a general case; the volume conjecture
for the 52 knot has been proved by Kashaev and Y okota [ /two.prop/zero.prop] by presenting the
above mentioned sum by the residue of a certain integral.
The aim of this paper is to give a presentation of the asymptot ic expansion of
the Kashaev invariant h52iN of the 52 knot rigorously (Theorem /one.prop./one.propbelow). Let
y0 be the unique solution with positive imaginary part of .y /NUL1/3 Dy,
y0 D0:3376410213::: C
p
/NUL1 0:5622795120::::
We put
x0 D1 /NUL 1
y0
;
& D 1
2
p
/NUL1

Li2.x0y0/ C Li2
 1
x0y0

C Li2.y0/
/NUL Li2
 1
y0

/NUL Li2
 1
x0

/NUL 2
6

D0:4501096100::: C
p
/NUL1 0:4813049796:::;
! De
p
/NUL 1=4
 y0 /NUL1
2y0 C1
1=2
D0:0901905774::: /NUL
p
/NUL1 0:6499757866::::
Then, we have
Theorem /one.prop./one.prop.The asymptotic expansion of the Kashaev invariant h52iN of the52
knot is given by the form
h52iN DeN&N3=2! 

1 C
dX
i D1
i 
2
p
/NUL1
N
i
CO
 1
Nd C1

;
1 A detailed asymptotic expansion of the colored Jones polyno mial for torus knots is given
in [/five.prop].
2 A detailed proof of the volume conjecture for the /f_igure-eight knot was given in [/one.prop] and the
termN 3=2 in (/two.prop) was also veri/f_ied there.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 673
for any d , where i is some constant given by a polynomial in y0 with rational
coeﬃcients/semicolon.alt in particular,1 is given by
1 D 1
.2y0 C1/3
37
4 y2
0 /NUL 31
6 y0 C35
8

C1
D 1
12696.1650y2
0 /NUL3498y0 C2197/ C1
D1:0537470859::: /NUL
p
/NUL1 0:1055728779::::
We can numerically observe that the limit ofq/NUL 1h52iNe/NUL N&N /NUL 3=2 tends to the
above mentioned value of!.
N q/NUL 1h52iNe/NUL N&N /NUL 3=2
200 0:0915851738::: /NUL
p
/NUL1 0:6519891312:::
500 0:0907489101::: /NUL
p
/NUL1 0:6507787459:::
1000 0:0904698237::: /NUL
p
/NUL1 0:6503768725:::
Further, we can numerically observe that the limit of
.h52iN.eN&N3=2!//NUL 1 /NUL1/N
2
p
/NUL1
tends to the above mentioned value of 1.
N .h52iN.eN&N3=2!//NUL 1 /NUL1/N=.2
p
/NUL1/
200 1:0567234007::: /NUL
p
/NUL1 0:0885918466:::
500 1:0549811019::: /NUL
p
/NUL1 0:0987904427:::
1000 1:0543713307::: /NUL
p
/NUL1 0:1021833710:::
As the conjecture ( /two.prop) suggests,! andi ’s of (/two.prop) are expected to be invariants
of K for any hyperbolic knot K. We have computed ! and 1 for the 52 knot
in this paper. It is conjectured that 2
p
/NUL1!2 of a hyperbolic knot is equal to the
twisted Reidemeister torsion associated with the action on sl2 of the holonomy
representation of the hyperbolic structure; see Remark/one.prop./four.propbelow. We discuss about
it for some knots in [ /two.prop/eight.prop].
We give a proof of the theorem in Section /five.propby justifying the above mentioned
approach. An outline of the proof is as follows. We rewrite th e sum ( /seven.prop) by an
integral by the Poisson summation formula. When we apply the Poisson summa-
tion formula, the right-hand side of the Poisson summation f ormula consists of
674 T. Ohtsuki
in/f_initely many summands, and we show that we can ignore them a ll except for
the one at0 in the sense that they are of suﬃciently small order at N ! 1 (Propo-
sition /four.prop./six.propand Lemma /five.prop./eight.prop). Further, by the saddle point method (Proposition /three.prop./five.prop),
we calculate the asymptotic expansion of the integral, and o btain the presentation
of the theorem.
By the method of this paper, the asymptotic behavior of the Ka shaev invariant
is discussed for the hyperbolic knots with up to 7 crossings in [ /two.prop/seven.prop] and [ /two.prop/six.prop] and
for some hyperbolic knots with 8 crossings in [/three.prop/four.prop].
Remark /one.prop./two.prop.The author has written the /f_irst version of this paper in Augus t
/two.prop/zero.prop/one.prop/one.prop. In February /two.prop/zero.prop/one.prop/two.prop, [/two.prop] was uploaded in the arXiv, in which Dimofte and
Garoufalidis de/f_ine a formal power series from an ideal tetrahedral decomposition
of a knot complement, which is expected to be equal to the asym ptotic expansion
of the Kashaev invariant of the knot.
Remark /one.prop./three.prop.The right-hand side of (
/one.prop) is equal to 2
p
/NUL1&, and it is called
the complex volume . It is known, see e.g. [ /four.prop/five.prop], that the complex volume can
be expressed by a critical value of the potential function. I t is also known, see
e.g. [/one.prop/zero.prop], that the complex volume can be regarded as the SL.2; C/ Chern–Simons
invariant.
Remark /one.prop./four.prop.The normalization of the above mentioned Reidemeister tors ion
is the cohomological Reidemeister torsion associated with the meridian used
in [
/two.prop/three.prop]. We note that the twisted Reidemeister torsion in [ /four.prop] is the twisted
Reidemeister torsion associated with the longitude, and it can be changed to the
twisted Reidemeister torsion associated with the meridian by [/two.prop/nine.prop, Théorème /four.prop./one.prop]
as mentioned in [ /two.prop/three.prop].
The paper is organized as follows. In Section /two.prop, we review de/f_initions and ba-
sic properties of the notation used in this paper. In Section /three.prop, we calculate the
asymptotic expansion of Gaussian integrals by the saddle point method, and show
Proposition /three.prop./five.prop. In Section /four.prop, we calculate the sum corresponding to the inte-
grals of Section /three.propby the Poisson summation formula, and show Proposition /four.prop./six.prop.
In Section /five.prop, we give a proof of Theorem /one.prop./one.propby using the Poisson summation
formula (Proposition /four.prop./six.prop) and the saddle point method (Proposition /three.prop./five.prop).
The author would like to thank Y oshiyuki Y okota for many helpful comments
on the volume conjecture and the calculation of the Kashaev invariant, and Takashi
Kumagai for many helpful comments on the calculation of the saddle point method
and the Poisson summation formula. The author would also lik e to thank T udor
On the asymptotic expansion of the Kashaev invariant of the 52 knot 675
Dimofte, Stavros Garoufalidis, Rinat Kashaev, Hitoshi Mur akami, Toshie Takata
and Dylan Thurston for many helpful comments. He would also l ike to thank the
referees for careful reading of the manuscript.
/two.prop. Calculation of the Kashaev invariant of the52 knot
In this section, we review the de/f_inition of the Kashaev invar iant and the cal-
culation of the Kashaev invariant h52iN of the 52 knot in Section /two.prop./one.prop. Further,
we continue to calculate the value of h52iN toward its asymptotic expansion in
Section /two.prop./two.prop.
/two.prop./one.prop. The Kashaev invariant of the52 knot. In this section, we review the
de/f_inition of the Kashaev invariant of oriented knots, and re view the calculation
of the Kashaev invariant h52iN of the 52 knot, which are due to Y okota [ /four.prop/three.prop].
The aim of this section is to show ( /seven.prop) which gives the value of h52iN .
LetN be an integer 2. We putq D exp.2
p
/NUL1=N/ , and put
.x/n D.1 /NULx/.1 /NULx2/   .1 /NULxn/
forn 0. It is known [ /two.prop/four.prop] that, for anyn;m withn m,
.q/n. Nq/N /NUL n/NUL 1 DN; (3)
X
nkm
1
.q/m/NUL k. Nq/k/NUL n
D1: (4)
Following Y okota [/four.prop/three.prop],3 we review the de/f_inition of the Kashaev invariant.
We put
N D ¹0;1;:::;N /NUL1º:
Fori;j;k;l 2 N, we put
Rij
kl D Nq /NUL 1
2 Ci /NUL kij
kl
.q/Œi /NUL j. Nq/Œj /NUL l.q/Œl/NUL k/NUL 1. Nq/Œk/NUL i
;
and
xRij
kl D Nq
1
2 Cj /NUL lij
kl
. Nq/Œi /NUL j.q/Œj /NUL l. Nq/Œl/NUL k/NUL 1.q/Œk/NUL i
;
3 We make a minor modi/f_ication of the de/f_inition of weights of cri tical points from the
de/f_inition in [/four.prop/three.prop], in order to make hKiN invariant under Reidemeister moves.
676 T. Ohtsuki
whereŒm 2 N denotes the residue of m moduloN , and we put
ij
kl D
8
<
:
1 ifŒi /NULj CŒj /NULl CŒl /NULk /NUL1 CŒk /NULi DN /NUL1;
0 otherwise.
LetK be an oriented knot. We consider a /one.prop-tangle whose closure is isotopic toK
such that its string is oriented downward at its end points. L etD be a diagram of
the /one.prop-tangle. We presentD by a union of elementary tangle diagrams shown in (
/five.prop).
We decompose the string of D into edges by cutting it at crossings and critical
points with respect to the height function of R2. A labeling is an assignment of an
element of N to each edge. Here, we assign 0 to the two edges adjacent to the end
points of D. For example, see ( /six.prop). We de/f_ine the weights of labeled elementary
tangle diagrams by
W
 i j
k l

DRij
kl; (5a)
W

i j
k l

D xRij
kl; (5b)
W

k l

Dq/NUL 1=2ık;l /NUL 1; (5c)
W

k l

Dık;l; (5d)
W
 i j 
Dq1=2ıi;j C1; (5e)
W
 i j 
Dıi;j: (5f)
Then, the Kashaev invariant hKiN ofK is de/f_ined by
hKiN D
X
labelings
Y
crossings
ofD
W. crossings/
Y
critical
pointsofD
W. critical points/ 2 C:
On the asymptotic expansion of the Kashaev invariant of the 52 knot 677
Following Y okota [/four.prop/three.prop],4 we review the calculation of the Kashaev invariant
h52iN of the52 knot, where the52 knot is the closure of the following /one.prop-tangle.
0
a k
j c
i
c C1
b i /NUL1 d
l e
e C10
(6)
We consider the above labeling. Then, it is shown by argument s in [ /four.prop/three.prop] that the
labelings of edges adjacent to the unbounded regions vanish , i.e.,
a Db Dc Dd De D0:
Hence, the Kashaev invariant of the 52 knot is given by
h52iN D
X
i;j;k;l
q1=2 xR00
0k xR0k
0j xRij
01 xR00
i /NUL 1l xR0l
01
D
X
i;j;k;l
q1=2  Nq
1
2 /NUL k
.q/Œ/NUL k. Nq/Œk/NUL 1
 Nq
1
2 Ck/NUL j
. Nq/Œ/NUL k.q/Œk/NUL j. Nq/Œj /NUL 1
 Nq /NUL 1
2 Cj
. Nq/Œi /NUL j.q/Œj /NUL 1.q/Œ/NUL i
 Nq
1
2 /NUL l
.q/Œ/NUL l. Nq/Œl/NUL i.q/Œi /NUL 1
 Nq /NUL 1
2 Cl
. Nq/Œ/NUL l.q/Œl/NUL 1
D
X
i;j;k;l
N3q
. Nq/Œ/NUL k.q/Œk/NUL j. Nq/Œj /NUL 1. Nq/Œi /NUL j.q/Œj /NUL 1.q/Œ/NUL i.q/Œ/NUL l. Nq/Œl/NUL i.q/Œi /NUL 1
;
4 Our resulting formula (/seven.prop) in this section isq times the corresponding formula in [/four.prop/three.prop]. This
diﬀerence is because of the diﬀerence of the de/f_initions of hKiN between ours and [ /four.prop/three.prop].
678 T. Ohtsuki
where we obtain the last equality from ( /three.prop). Further, by ( /four.prop), the above formula is
rewritten
h52iN D
X
1j i N
N3q
.q/i /NUL 1.q/N /NUL i.q/j /NUL 1. Nq/j /NUL 1. Nq/i /NUL j
D
X
0j i<N
N3q
.q/i.q/N /NUL i /NUL 1.q/j. Nq/j. Nq/i /NUL j
D
X
0i;j
i Cj<N
N3q
.q/i Cj.q/N /NUL i /NUL j /NUL 1.q/j. Nq/j. Nq/i
;
(7)
where we obtain the second equality by replacing i andj withi C1 andj C1,
and obtain the last equality by replacing i with i Cj . Hence, we obtain the
presentation (/seven.prop) of h52iN .
/two.prop./two.prop. Calculation ofh52iN toward its asymptotic expansion. In this section,
we continue to calculate the value of the Kashaev invariant h52iN of the 52 knot
toward its asymptotic expansion.
To calculate the asymptotic expansion of h52iN , we review an integral expres-
sion of.q/n. It is known [ /eight.prop], [/four.prop/zero.prop] that
.q/n D exp

'
 1
2N

/NUL'
2n C1
2N

;
. Nq/n D exp

'

1 /NUL 2n C1
2N

/NUL'

1 /NUL 1
2N

:
(8)
Here, following Faddeev [/six.prop], we de/f_ine a holomorphic function'.t/ on the domain
¹t 2 C j0< Ret <1º by
'.t/ D
Z 1
/NUL1
e.2t /NUL 1/xdx
4x sinhx sinh.x=N/;
noting that this integrand has poles at n
p
/NUL1 (n 2 Z), where, to avoid the pole
at0, we choose the contour of the integral

 D./NUL1; /NUL1 [ ¹z 2 C j jzj D 1; Imz 0º [Œ1; 1/:
We review some properties of '.t/ in Appendix A.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 679
By using'.t/ , we rewrite the presentation ( /seven.prop) of h52iN by (/eight.prop) as
h52iN DN3q
X
0i;j
i Cj<N
exp

N  zV
2i C1
2N ;2j C1
2N

;
where we put
zV.t;s/ D 1
N

'

t Cs /NUL 1
2N

C'

1 /NULt /NULs C 1
2N

C'.s/ /NUL'.1 /NULs/
/NUL'.1 /NULt/ /NUL3'
 1
2N

C2'

1 /NUL 1
2N

D 1
N

/NUL'.1 /NULt/ /NUL2'.1 /NULs/

/NUL 1
2
p
/NUL1
2
6
/NUL2
p
/NUL1
1
2

t Cs /NUL 1
2N
2
C1
2s2 /NUL 1
2t /NULs C1
6

/NUL 5
2N logN /NUL 3
p
/NUL1
4N C
p
/NUL1
4N2 :
Here, we obtain the second equality by Lemmas A./two.propand A./three.prop. Hence, by putting
V.t;s/ D zV.t;s/ C 5
2N logN
D 1
N./NUL'.1 /NULt/ /NUL2'.1 /NULs// /NUL 1
2
p
/NUL1
2
6
/NUL2
p
/NUL1
1
2

t Cs /NUL 1
2N
2
C1
2s2 /NUL 1
2t /NULs C1
6

/NUL 3
p
/NUL1
4N C
p
/NUL1
4N2 ;
the presentation of h52iN is rewritten
h52iN DN1=2q
X
0i;j
i Cj<N
exp

N V
2i C1
2N ;2j C1
2N

: (9)
The range of.i=N;j=N/ in this sum is given by the domain
 D ¹.t;s/ 2 R2 j0 t;0 s; tCs 1º:
Further, it follows from Proposition A./one.propthat V.t;s/ converges to the following
function asN ! 1:
yV.t;s/ D 1
2
p
/NUL1

/NUL Li2.e/NUL 2
p
/NUL 1t/ /NUL2 Li2.e/NUL 2
p
/NUL 1s/ /NUL 2
6

/NUL2
p
/NUL1
1
2t2 Cs2 Cts /NUL 1
2t /NULs C1
6

:
(10)
680 T. Ohtsuki
We will show that the asymptotic expansion of ( /nine.prop) is of order eN&R times
polynomial order in N , where &R is the real part of & which is given in the
introduction,
&R D Re& D0:4501096100::::
Hence, we can ignore summands of ( /nine.prop) in the domain where Re yV.t;s/ &R /NUL",
since they do not contribute to the resulting expansion. Fur ther, as we can see in
Figure /one.prop, Re yV.t;s/ /NUL&R is positive only for.t;s/ in a particular subdomain of .
In the following lemma, we consider to restrict  to a smaller domain 0 which
includes this subdomain; this restriction will be used to ve rify the assumptions of
the Poisson summation formula and the saddle point method la ter.
0.2 0.4 0.6 0.8 1.0
0.2
0.4
0.6
0.8
1.0

0
Figure /one.prop. The domain¹.t;s/ j Re yV.t;s/ &Rº.
Lemma /two.prop./one.prop.We put
0 D ¹.t;s/ 2 j0:04 t 0:4; 0:05s 0:4; tCs 0:6º:
Then, the following domain
¹.t;s/ 2 R2 j Re yV.t;s/ &R /NUL"º (11)
is included in 0 for some suﬃciently small ">0 .
We give a proof of the lemma in Appendix D. we can graphically observe the
inclusion of the lemma in Figure /one.prop.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 681
We put
00 D ¹.t;s/ 2 j0:04 t 0:9; 0:05s 0:9º: (12)
By Lemma B./one.prop,V.t;s/ uniformly converges to yV.t;s/ asN ! 1 in this domain.
By this uniform convergence, we can restrict00 to0 later. Before this restriction,
we consider to restrict  to00 in the following calculation of h52iN .
We consider the value of h52iN given in ( /seven.prop). The summand of the sum ( /seven.prop) is
estimated by
ˇ
ˇ
ˇ
ˇ
N3q
.q/i Cj.q/N /NUL i /NUL j /NUL 1.q/j. Nq/j. Nq/i
ˇ
ˇ
ˇ
ˇ D
ˇ
ˇ
ˇ
ˇ
N2
.q/i.q/2
j
ˇ
ˇ
ˇ
ˇ; (13)
where we obtain the equality by (
/three.prop). Since .q/n D .1 /NUL qn/.q/n/NUL 1 from the
de/f_inition of.q/n, the value of 1=j.q/nj is monotonically increasing with respect
ton for0  n  N
6 . Hence, for 0  i  0:04 N and0  j  0:05 N , the
value of (/one.prop/three.prop) is monotonically increasing with respect to i andj . Further, we can
similarly show that, for 0:9 N i < Nand0:9 N j < N, the value of ( /one.prop/three.prop)
is monotonically decreasing with respect to i andj . Furthermore, since V.t;s/
uniformly converges to yV.t;s/ asN ! 1 on00 by Lemma B./one.prop, ReV.t;s/ is
bounded by eN.&R/NUL "1/ for some "1 > 0 on @00 by Lemma /two.prop./one.prop. Hence, ( /one.prop/three.prop) is
bounded by the order eN.&R/NUL "2/ for some"2>0 . Therefore, by ( /seven.prop),
h52iN D
X
i;j 2Z
.i=N;j=N/ 200
N3q
.q/i Cj.q/N /NUL i /NUL j /NUL 1.q/j. Nq/j. Nq/i
CO.N2eN.&R/NUL "2//:
Hence, similarly as ( /nine.prop), we have that
h52iN DN1=2q
X
i;j 2Z
.i=N;j=N/ 200
exp

N V
2i C1
2N ;2j C1
2N

CO.N2eN.&R/NUL "2//
DeN&N1=2q
X
i;j 2Z
.i=N;j=N/ 200
exp

N V
2i C1
2N ;2j C1
2N

/NULN&

CO.N2eN.&R/NUL "2//:
682 T. Ohtsuki
By Lemma /two.prop./one.prop, we can restrict 00 to 0, where the error term of the sum is
estimated by the order N2e/NUL N" . Hence,
h52iN DeN&N1=2q
 X
i;j 2Z
.i=N;j=N/ 20
exp

N V
2i C1
2N ;2j C1
2N

/NULN&

CO.e /NUL N" 3/

;
(14)
for some"3>0 . Further, by the Poisson summation formula, we will see that the
above sum is expressed by the integral
h52iN DeN&N5=2q
Z
0
exp.N V.t;s/ /NULN&/dtds CO.e /NUL N" 4/

for some"4>0 .
We will analyse this integral in Section /five.propusing the saddle point method and
give the proof our main Theorem /one.prop./one.propthere. We will therefore devote the following
two sections to recalling the saddle point method and the Poi sson summation
formula.
