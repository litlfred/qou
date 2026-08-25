---
doc_id: 104171-qt-83
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot"
section_id: sec-001-calculation-by-the-saddle-point-method
section_title: "Calculation by the saddle point method"
section_number: null
pages: 14-25
source_pdf: 10.4171-qt-83.pdf
source_sha256: d95b9363de2766d2
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
---
In this section, we calculate Gaussian integrals by the sadd le point method.
We calculate a Gaussian integral in Proposition /three.prop./one.prop, a Gaussian integral with per-
turbative terms in Proposition /three.prop./two.prop, and multi-variable cases in Propositions /three.prop./four.prop
and /three.prop./five.prop. We use Proposition /three.prop./five.propin the proof of Theorem /one.prop./one.propin Section /five.prop. For the
saddle point method, see e.g. [ /three.prop/nine.prop].
Proposition /three.prop./one.prop.For a non-zeroa 2 C, the domain ¹z 2 C j Reaz2<0 º has two
connected components. We choose z0;z1 from the two components respectively.
LetC be a path from z0 toz1 in C..See Figure /two.prop./ Then, there exists ">0 such
that
Z
C
eN az2
dz D
p
p/NULa 
p
N
CO.e /NUL "N/;
where we choose the sign of p/NULa such that Rez1
p/NULa>0 .
We note that" depends onz0,z1 anda.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 683
z0
z1/NUL 1p
/NUL a
1p
/NUL a
C
Figure /two.prop. The domain¹z 2 C j Reaz 2<0 º is shaded.
Proof. By replacing z withz=p/NULa, we can reduce the proof to the case where
a D /NUL1. Putting a D /NUL1, we show that
Z z1
z0
e/NUL Nz 2
dz D
pp
N
CO.e /NUL "N/:
Since
R 1
/NUL1 e/NUL Nz 2
dz D p=
p
N , it is suﬃcient to show that
Z z0
/NUL1
e/NUL Nz 2
dz DO.e /NUL "N/;
Z 1
z1
e/NUL Nz 2
dz DO.e /NUL "N/:
We show the latter formula. (The former formula can be shown s imilarly.) The
latter formula is calculated
Z 1
z1
e/NUL Nz 2
dz D
Z Rez1
z1
e/NUL Nz 2
dz C
Z 1
Rez1
e/NUL Nz 2
dz;
and the two terms of the right-hand side are estimated
ˇ
ˇ
ˇ
ˇ
Z Rez1
z1
e/NUL Nz 2
dz
ˇ
ˇ
ˇ
ˇ 
Z Rez1
z1
je/NUL Nz 2
j  jdzj

Z Rez1
z1
e/NUL N Rez2
jdzj

Z Rez1
z1
e/NUL N Rez2
1 jdzj
D j Imz1j e/NUL N Rez2
1
DO.e /NUL "N/;
684 T. Ohtsuki
and
0 
Z 1
Rez1
e/NUL Nz 2
dz 
Z 1
Rez1
e/NUL N.Rez1/zdz D e/NUL N.Rez1/2
N  Rez1
DO.e /NUL "N/
for some">0 . Hence, we obtain the required formula. 
We generalize Proposition /three.prop./one.propto the case where there are perturbative terms in
the exponential of the integrand.
Proposition /three.prop./two.prop.Leta be a non-zero complex number, and let  .z/ andr.z/ be
holomorphic functions of the form
 .z/ Daz2 Cr.z/; r.z/ Db3z3 Cb4z4 C   ;
de/f_ined in a neighborhood of 0. The domain
¹z 2 C j Re .z/<0 º (15)
has two connected components in a neighborhood of 0. We choose z0;z1
from these two components respectively. Let C be a path from z0 to z1 in C.
.See Figure
/three.prop./ Then,
Z
C
eN .z/dz D
p
p/NULa 
p
N

1 C
dX
kD1
k
Nk CO
 1
Nd C1

;
for any d , where we choose the sign of p/NULa similarly as in Proposition /three.prop./one.prop,
andk’s are constants given by using coeﬃcients of the expansion o f .z/ /semicolon.alt such
presentations are obtained by formally expanding the formu la
1 C
1X
kD1
k
Nk D exp

Nr
 @
@u

exp

/NUL u2
4Na
ˇ
ˇ
ˇ
uD0
: (16)
In particular,1 is given by
1 D /NUL15b2
3
16a3 C 3b4
4a2:
On the asymptotic expansion of the Kashaev invariant of the 52 knot 685
z0
z1
C
Figure /three.prop. The domain¹z 2 C j Re .z/<0 º is shaded.
Proof. We show the proposition modifying a proof of the saddle point method
written in [ /three.prop/nine.prop].5 We show the proposition, for simplicity, putting a D /NUL1 as in
the proof of Proposition /three.prop./one.prop. We put Or.z/ D r.z/=z2. Since Or.z/ is analytic in a
neighborhood of0, there exists a suﬃciently small ı1>0 such that
Or.z/ D
1X
i D1
bkC2zk
for jzj< ı1. Let w be a non-negative real parameter. For each /f_ixed w, we have
that
ew Or.z/ D
1X
kD0
Pk.w/zk
for jzj < ı1, where Pk.w/ is a polynomial in w of degree  k. Since Or.0/ D 0,
there exist small ı2 > 0and"1 > 0such that j Or.x/ j  "1 for /NULı2 x ı2; we
can further assume that "1<1 andı2 ı1. For each /f_ixed integerm>0 , we can
put
ew Or.x/ D
mX
kD0
Pk.w/xk CRmxmC1 (17)
for /NULı2  x  ı2 and any w  0, where RmxmC1 is the error term, which is
estimated by
j ReRmj  max
jxjı2
ˇ
ˇ
ˇ
ˇ Re dmC1
dxmC1ew Or.x/
ˇ
ˇ
ˇ
ˇ; j ImRmj  max
jxjı2
ˇ
ˇ
ˇ
ˇ Im dmC1
dxmC1ew Or.x/
ˇ
ˇ
ˇ
ˇ:
5 As for the1-variable case, a proof of a more general statement of the sad dle point method
is written in [ /three.prop/nine.prop], though the multi-variable case is not written in [ /three.prop/nine.prop]. We review (a simpler
modi/f_ication of) the proof of [ /three.prop/nine.prop], in order to generalize it to the multi-variable case later
(Proposition /three.prop./five.prop).
686 T. Ohtsuki
Further, since
dmC1
dxmC1ew Or.x/ Dew Or.x/ 
 polynomial inw and diﬀerentials of Or.x/
of degree mC1

;
we have that
jRmj e"1wK1.wmC1 C1/ K2e"2w (18)
for someK1;K2>0 and"2 <1 , which are independent of x andw (noting that
m is bounded by using d later). Further, we replace the path C with the union of
a pathC1 fromz0 to /NULı, a pathC2 from /NULı toı along the real axis, and a path C3
fromı toz1. We can assume that there exist suﬃciently small ı;"3>0 such that
ı ı2 andC1 andC3 are in the domain
¹z 2 C j Re .z/  /NUL"3º: (19)
Then, the integral of the proposition is given by
Z
C
eN .z/dz D
Z
C1
eN .z/dz C
Z
C2
eN .z/dz C
Z
C3
eN .z/dz: (20)
SinceC1 andC3 are in the domain ( /one.prop/nine.prop), we have that
Z
C1
eN .z/dz DO.e /NUL N" 3/ (21a)
and
Z
C3
eN .z/dz DO.e /NUL N" 3/: (21b)
Hence, it is suﬃcient to show that the integral along C2 gives the required formula.
The integral along C2 is calculated as
Z
C2
eN .z/dz D
Z ı
/NUL ı
eN .x/dx
D
Z ı
/NUL ı
e/NUL Nx 2
eNx 2 Or.x/dx
D
2d C1X
kD0
Z ı
/NUL ı
Pk.Nx2/xke/NUL Nx 2
dx C
Z ı
/NUL ı
R2d C1x2d C2e/NUL Nx 2
dx;
(22)
by (/one.prop/seven.prop), puttingw DNx2 andm D2d C1. When k is odd, the summand of the
/f_irst term of (/two.prop/two.prop) is equal to 0, since the integrand is an odd function. When k is
On the asymptotic expansion of the Kashaev invariant of the 52 knot 687
even, the summand of the /f_irst term of ( /two.prop/two.prop) is given by a sum of integrals of the
form
Z ı
/NUL ı
.Nx2/lxke/NUL Nx 2
dx D
Z 1
/NUL1
Nlx2lCke/NUL Nx 2
dx CO.e /NUL N" 4/
D 1
Nk=2 p
N
Z 1
/NUL1
y2lCke/NUL y2
dx CO.e /NUL N" 4/
D .2l Ck /NUL1/ŠŠp
2lCk=2Nk=2 p
N
CO.e /NUL N" 4/;
for some"4>0 , where we obtain the /f_irst equality in a similar way as in the proof
of Proposition /three.prop./one.prop, and obtain the second equality putting y D
p
Nx . Hence, the
/f_irst term of (/two.prop/two.prop) is given by the form
pp
N

1 C
dX
kD1
k
Nk

CO.e /NUL N" 4/:
Further, by (/one.prop/eight.prop) puttingw DNx2, the second term of ( /two.prop/two.prop) is estimated by
ˇ
ˇ
ˇ
Z ı
/NUL ı
R2d C1x2d C2e/NUL Nx 2
dx
ˇ
ˇ
ˇ 
Z ı
/NUL ı
jR2d C1jx2d C2e/NUL Nx 2
dx
K2
Z ı
/NUL ı
x2d C2e/NUL .1/NUL "2/Nx 2
dx
DO
 1
Nd C 3
2

;
where we obtain the last equality in a similar way as the above calculation. Hence,
by (/two.prop/two.prop),
Z
C2
eN .z/dz D
pp
N

1 C
dX
kD1
k
Nk CO
 1
Nd C1

:
Therefore, by (/two.prop/zero.prop) and ( /two.prop/one.prop), the integral of the proposition is given by the form
Z
C
eN .z/dz D
pp
N

1 C
dX
kD1
k
Nk CO
 1
Nd C1

:
688 T. Ohtsuki
In particular,1 is concretely calculated by re/f_ining the above calculation, as
follows. Since
Or.z/ Db3z Cb4z2 C   ;
we have that
ew Or.z/ D1 Cw Or.z/ C1
2w2 Or.z/2 C    D1 Cb3wz C
b3
2w2 Cb4w

z2 C   :
Hence,Z
C
eN .z/dz
D
Z 1
/NUL1
e/NUL Nx 2

1 Cb3Nx2 x C
b2
3
2 .Nx2/2 Cb4Nx2

x2 C   

dx
D
pp
N

1 C
15
16b2
3 C3
4b4
1
N CO
 1
N2

:
This is the required formula for d D1 whena D /NUL1.
We obtain a concrete presentation of any k by the following formal calcula-
tion. Noting that
zm D
 @
@u
m
euz
ˇ
ˇ
ˇ
uD0
;
we have thatZ
eNaz 2
zmdz D
Z  @
@u
m
eNaz 2Cuz
ˇ
ˇ
ˇ
uD0
dz
D
Z  @
@u
m
exp

Naw2 /NUL u2
4Na
ˇ
ˇ
ˇ
uD0
dw
D
p

p/NULa 
p
N

 @
@u
m
exp

/NUL u2
4Na
ˇ
ˇ
ˇ
uD0
;
which can be justi/f_ied by a similar calculation as above, to be precise.Hence,
putting exp.Nr.z// DP
m Qbmzm,
Z
eN .z/dz D
Z
eNaz 2
exp.Nr.z//dz
D
Z
eNaz 2
X
m
Qbmzm

dz
D
p

p/NULa 
p
N

X
m
Qbm
 @
@u
m
exp

/NUL u2
4Na
ˇ
ˇ
ˇ
uD0
D
p

p/NULa 
p
N
 exp

Nr
 @
@u

exp

/NUL u2
4Na
ˇ
ˇ
ˇ
uD0
;
and this gives (
/one.prop/six.prop). By expanding this formula formally, we obtain concrete
presentations ofk’s in terms of coeﬃcients of the expansion of  .z/ . 
On the asymptotic expansion of the Kashaev invariant of the 52 knot 689
Remark /three.prop./three.prop.We can extend Proposition /three.prop./two.propto the case where  .z/ depends on
N in such a way that  .z/ is of the form
 .z/ D 0.z/ C 1.z/ 1
N C 2.z/ 1
N2 C    C m.z/ 1
Nm Crm.z/ 1
NmC1; (23)
where i.z/’s are holomorphic functions independent of N , and we assume that
 0.z/ satis/f_ies the assumption of the proposition and jrm.z/j is bounded by a
constant which is independent of N . Then, eN .z/ D 
.z/eN 0.z/, where we
put

.z/ D exp

 1.z/ C 2.z/ 1
N C    C m.z/ 1
Nm/NUL 1 Crm.z/ 1
Nm

D
0.z/ C
1.z/ 1
N C
2.z/ 1
N2 C    C
m/NUL 1.z/ 1
Nm/NUL 1 C Qrm.z/ 1
Nm:
Here, Qrm.z/ is the error term such that j Qrm.z/j is bounded by a constant which
is independent of N . As written in [ /three.prop/nine.prop], in the same way as in the proof of
Proposition /three.prop./two.prop, we can show the asymptotic expansion of R 
i.z/eN 0.z/dz by
expanding
i.z/ atz D 0. Further, we can estimate R Qrm.z/eN 0.z/dz similarly
as in the proof of Proposition /three.prop./two.prop, noting that only values of Qrm.z/ in a suﬃciently
small neighborhood of0 contribute to the resulting expansion. In this way, we can
justify the statement of Proposition /three.prop./two.propin the case where  .z/ depends on N as
in the form ( /two.prop/three.prop).
We generalize Proposition/three.prop./one.propto the case ofn variables. LetA be a non-singular
symmetric complexnn matrix, and let z be a column vector.z1;:::;z n/T 2 Cn.
The domain
¹z 2 Cn j Re zTAz<0 º (24)
is homotopy equivalent toSn/NUL 1. LetD be an orientedn-ball embedded in Cn such
that@D is included in the domain ( /two.prop/four.prop), whose inclusion is homotopy equivalent.
There exists a matrixP such that /NULA DPTP ; we note that detP D ˙
p
det./NULA/.
We choose ann-ball as a neighborhood of the origin in Rn  Cn. The matrixP /NUL 1
takes thisn-ball to an n-ball satisfying the above assumption ofD. We choose the
sign of
p
det./NULA/ by setting it to be det P ifP takes the orientation of D to the
standard orientation of Rn, and /NULdetP otherwise.
Proposition /three.prop./four.prop.LetA;D be as above. Then, there exists ">0 such that
Z
D
eN zTAzd z D n=2
Nn=2
p
det./NULA/
CO.e /NUL "N/;
where we putd z Ddz1   dzn, and we choose the sign of
p
det./NULA/ as above.
690 T. Ohtsuki
Proof. By changing the coordinate of z linearly, we can reduce the proof to the
case whereA is a diagonal matrix. Further, sinced.eN zTAzd z/ D0, we can move
the domainD in Cn by Stokes’ theorem; we can also move@D in the domain (/two.prop/four.prop)
ignoring error terms of ordere/NUL N" for some">0 as in the proof of Proposition/three.prop./one.prop.
In this way, we can move D into Rn  Cn, which means that we can reduce the
proof to the product of copies of the formula of Proposition /three.prop./one.prop. 
We generalize Proposition /three.prop./four.propto the case where there are perturbative terms
in the exponential of the integrand.
Proposition /three.prop./five.prop.LetA be a non-singular symmetric complex nn matrix, and
let .z/ andr.z/ be holomorphic functions of the form
 .z/ D zTAz Cr.z/; (25a)
r.z/ Dr.z1;   ;zn/ D
X
i;j;k
bijkzizjzk C
X
i;j;k;l
cijklzizjzkzl C   ; (25b)
de/f_ined in a neighborhood of 0 2 Cn. The restriction of the domain
¹z 2 Cn j Re .z/<0 º (26)
to a neighborhood of 0 2 Cn is homotopy equivalent to Sn/NUL 1. Let D be an
oriented n-ball embedded in Cn such that @D is included in the domain /parenleft.alt
/two.prop/six.prop/parenright.alt
whose inclusion is homotopic to a homotopy equivalence to th e above Sn/NUL 1 in
the domain /parenleft.alt/two.prop/six.prop/parenright.alt. Then,
Z
D
eN . z/d z D n=2
Nn=2
p
det./NULA/

1 C
dX
i D1
i
Ni CO
 1
Nd C1

;
for any d , where we choose the sign of
p
det./NULA/ as in Proposition /three.prop./four.prop, and
i ’s are constants given by using coeﬃcients of the expansion o f  .z//semicolon.alt such
presentations are obtained by formally expanding the formu la
1 C
1X
i D1
i
Ni D exp

Nr
 @
@u1
;:::; @
@un

exp

/NUL 1
4N uTA/NUL 1u
ˇ
ˇ
ˇ
uD0
: (27)
In particular,1 is given by
1 D /NUL1
28 3
X
i1;i2;;i6
2S6
bi1i2i3bi4i5i6 Nai .1/i .2/ Nai .3/i .4/ Nai .5/i .6/
C 1
32
X
i1;i2;i3;i4

2S4
ci1i2i3i4 Nai
 .1/i
 .2/ Nai
 .3/i
 .4/;
where Sn is thenth symmetric group, and we put . Naij/i;j DA/NUL 1.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 691
Proof. Similarly as in the proof of Proposition /three.prop./four.prop, we can reduce the proof to the
case where A D /NULE, where E denotes the identity matrix of size n. Then, the
integral of the problem is rewritten
Z
D
eN zT z exp.Nr. z//d z; (28)
where we can letD be a suﬃciently small neighborhood of 0 in Rn as in the proof
of Proposition /three.prop./four.prop. The second exponential in the integrand of (/two.prop/eight.prop) is calculated as
exp
/NUL
Nr. z/

D1 CNr. z/ C1
2N2r.z/2 C   
D1 CN
X
i;j;k
bijkzizjzk CN
X
i;j;k;l
cijklzizjzkzl
C1
2N2 X
i1;i2;;i6
bi1i2i3bi4i5i6zi1zi2zi3zi4zi5zi6 C   :
Hence, we can calculate the asymptotic expansion of the inte gral ( /two.prop/eight.prop) similarly
as the calculation of 1 in the proof of Proposition /three.prop./two.prop, and we can show that the
asymptotic expansion of ( /two.prop/eight.prop) is given by
Z
D
eN . z/d z D n=2
Nn=2

1 C1
N C 2
N2 C   

:
We estimate the remaining part “   ” of the above formula as in the proof of
Proposition /three.prop./two.prop, as follows. We can put
r.z/ D
X
i;j
zizj Orij.z/
for some Orij.z/ which satis/f_ies that Orij.z/ D Orji.z/. Let wij be non-negative real
parameters, and put w D.wij/. For each /f_ixedw, we have
exp
X
i;j
wij Orij.z/

D
1X
kD0
X
i1;:::;ik
Pi1ik.w/zi1   zik
for suﬃciently small z, where Pi1ik.w/ is a polynomial in wij’s of degree k.
Further, for each /f_ixed integerm>0 , we can put
exp
X
i;j
wij Orij.x/

D
mX
kD0
X
i1;:::;ik
Pi1ik.x/xi1   xik C
X
j1;:::;jmC1
Rj1jmC1xj1   xjmC1
692 T. Ohtsuki
whereRj1jmC1xj1   xjmC1 is the error term. Similarly as in the proof of Propo-
sition /three.prop./two.prop, we can estimate it by
jRj1jmC1j  K exp
X
i;j
"ijwij

for someK >0 and"ij >0 which satis/f_ies that"ij D"ji andE/NUL."ij/ is positive
de/f_inite. Further, similarly as in the proof of Proposition/three.prop./two.prop, puttingm D2d C1,
we can show that the error term is of order O.1=Nn=2Cd C1/. Hence, we can
show that the integral of the problem has the asymptotic expansion of the required
formula.
We obtain concrete presentations of k’s by the following formal calculation.
Noting that
zi1   zim D @
@ui1
   @
@uim
euT zˇ
ˇ
uD0
we have that
Z
eN zTAzzi1   zimd z
D
Z @
@ui1
   @
@uim
eN zTAzCuT zˇ
ˇ
uD0d z
D
Z @
@ui1
   @
@uim
exp

N  wTAw /NUL 1
4N uTA/NUL 1u
ˇ
ˇ
ˇ
uD0
d w
D n=2
Nn=2
p
det./NULA/
 @
@ui1
   @
@uim
exp

/NUL 1
4N uTA/NUL 1u
ˇ
ˇ
ˇ
uD0
:
Hence, we obtain (
/two.prop/seven.prop) from this formula similarly as in the proof of Proposi-
tion /three.prop./two.prop.
The above expansion is concretely calculated as
@
@ui1
   @
@ui2k
exp

/NUL 1
4N uTA/NUL 1u
ˇ
ˇ
ˇ
uD0
D @
@ui1
   @
@ui2k
1
kŠ

/NUL 1
4N uTA/NUL 1u
k
D ./NUL1/k
kŠ4kNk
X
2S2k
Nai .1/i .2/    Nai .2k/NUL 1/i .2k/:
In particular, we obtain the presentation of 1 from such calculation. 
On the asymptotic expansion of the Kashaev invariant of the 52 knot 693
Remark /three.prop./six.prop.Similarly as Remark /three.prop./three.prop, we can extend Proposition /three.prop./five.propto the case
where .z/ depends onN in such a way that  .z/ is of the form
 .z/ D 0.z/ C 1.z/1
N C 2.z/ 1
N2 C    C m.z/ 1
Nm Crm.z/ 1
NmC1; (29)
where i.z/’s are holomorphic functions independent of N , and we assume that
 0.z/ satis/f_ies the assumption of the proposition and jrm.z/j is bounded by a
constant which is independent of N .
