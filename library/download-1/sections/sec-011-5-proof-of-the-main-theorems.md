---
doc_id: download-1
doc_title: "Central and L p -concentration of 1-Lipschitz maps into R -trees"
section_id: sec-011-5-proof-of-the-main-theorems
section_title: "Proof of the main theorems."
section_number: 5
pages: 16-23
source_pdf: Download (1).pdf
source_sha256: bbb001c909958e8a
toc_source: inferred
doc_brief: "Central and L p -concentration of 1-Lipschitz maps into R -trees — In this paper, we study the Le´vy-Milman concentration phenomenon of 1-Lipschitz maps from mm-spaces to R-trees."
---
Proof of the main theorems.
Combining Proposition 3.2 with the same proof as [3, Lemma 5.3] implies the
following proposition:
PROPOSITION 5.1.
Let T be an R-tree and  a ﬁnite Borel measure. Then,
for any  > 0, we have
 BT
m; Sep ; m
3 ; 
2






 m  ;
ð5:1Þ
where m is a median of the measure . In particular, letting X be an mm-space,
we have
ObsDiamTðX; Þ  2 Sep X; m
3 ; 
2


:
ð5:2Þ
Proposition 5.1 together with Corollary 2.6 yields Theorem 1.1. The
following way to prove Theorem 1.1 is much easier and more straightforward
than the above way, that is, to prove the existence of a median of a measure on an
R-tree.
PROOF OF THEOREM 1.1.
Our goal is to prove the following inequality:
ObsDiamTðX; Þ  3 Sep X; 
3 ; 
3


þ 4 ObsDiamRðX; Þ
ð5:3Þ
for any  > 0 with   m=2. Let f : X ! T be an arbitrary 1-Lipschitz map. Fixing
a
point
z0 2 T,
we
shall
consider
the
function
g : T ! R
deﬁned
by
gðzÞ :¼ dTðz; z0Þ. Since g 	 f : X ! R is a 1-Lipschitz function, by the deﬁnition
of the observable diameter, there is an interval A ¼ ½s; t  ½0; þ1Þ such that
diam A  ObsDiamRðX; Þ and ðg 	 fÞðXÞðAÞ  m  . Observe that the set
g1ðAÞ is the annulus fz 2 T j s  dTðz; z0Þ  tg. We denote by C the set of all
connected components of the set g1ðAÞ n fz0g.
CLAIM 5.2.
For any T 0 2 C , we have diam T 0  2 diam A.
PROOF.
Given any z1; z2 2 T 0, we shall show that z0;z1ðsÞ ¼ z0;z2ðsÞ.
498
K. FUNANO
Suppose that z0;z1ðsÞ 6¼ z0;z2ðsÞ. Then, putting s0 :¼ supft 2 ½0; þ1Þ j z0;z1ðtÞ ¼
z0;z2ðtÞg, we have 0 < s0 < s. By the deﬁnition of s0 and the property (2) of
R-trees, we have ðz0;z1ðs0Þ; z1T \ ðz0;z2ðs0Þ; z2T ¼ ;. Therefore, by the property
(2) of R-trees, we get
½z1; z2T ¼ ½z0;z1ðs0Þ; z1T [ ½z0;z2ðs0Þ; z2T:
Hence, since T 0 is convex by virtue of Proposition 2.9, the points z1 and z2 must be
included in diﬀerent components in C Tðz0;z1ðs0ÞÞ. This is a contradiction, since
T 0 ¼ SfC \ T 0 j C 2 C Tðz0;z1ðs0ÞÞg
and
T 0
is
connected.
Thus,
we
have
z0;z1ðsÞ ¼ z0;z2ðsÞ. Consequently, we obtain
dTðz1; z2Þ  dTðz1; z0;z1ðsÞÞ þ dTðz0;z2ðsÞ; z2Þ  2ðt  sÞ  2 ObsDiamRðX; Þ:
This completes the proof of the claim.

We shall consider the relation 
 on C deﬁned by T 0 
 T 00 if and only if
dTðT 0; T 00Þ  SepðX; =3; =3Þ.
CLAIM 5.3.
The relation 
 is an equivalence relation on C .
PROOF.
We only prove ‘‘T1 
 T2, T2 
 T3 ) T1 
 T3’’ for diﬀerent Ti 2 C ,
i ¼ 1; 2; 3. Taking points zi 2 Ti for i ¼ 1; 2; 3, we put s12 :¼ maxft 2 ½0; þ1Þ j
z0;z1ðtÞ ¼ z0;z2ðtÞg and s23 :¼ maxft 2 ½0; þ1Þ j z0;z2ðtÞ ¼ z0;z3ðtÞg. Since Ti are
diﬀerent to each other, we easily see that s12  s, s23  s,
dTðT1; T2Þ ¼ dTðz0;z1ðsÞ; z0;z1ðs12ÞÞ þ dTðz0;z1ðs12Þ; z0;z2ðsÞÞ
¼ 2ðs  s12Þ
 SepðX; =3; =3Þ;
and similarly dTðT2; T3Þ ¼ 2ðs  s23Þ  SepðX; =3; =3Þ. If s12  s23, we then
obtain
dTðT1; T3Þ  dTðz0;z1ðsÞ; z0;z3ðsÞÞ
 dTðz0;z1ðsÞ; z0;z1ðs12ÞÞ þ dTðz0;z2ðs12Þ; z0;z2ðs23ÞÞ
þ dTðz0;z3ðs23Þ; z0;z3ðsÞÞ
¼ ðs  s12Þ þ ðs23  s12Þ þ ðs  s23Þ
¼ 2ðs  s12Þ
 SepðX; =3; =3Þ:
Central and Lp-concentration of 1-Lipschitz maps into R-trees
499
In the case of s23  s12, the same conclusion also follows from the same argument
as the above. This completes the proof of the claim.

Let C 0 denote the set of equivalence classes of C = 
. Suppose that
fðXÞðS
T 02S T 0Þ < =3 for any S 2 C 0. Since fðXÞðg1ðAÞÞ  m    , we
have C 0  C 0 such that

3  fðXÞ
[
S02C 0
[
T 02S0
T 0
 
!
< 2
3 :
Hence, by putting C 00 :¼ C 0 n C 0, we get
Sep X; 
3 ; 
3


< dT
[
S02C 0
[
T 02S0
T 0;
[
S002C 00
[
T 002S00
T 00
 
!
 Sep fðXÞ; 
3 ; 
3


 Sep X; 
3 ; 
3


;
which is a contradiction. Thereby, there exists S 2 C 0 such that fðXÞðS
T 02S
T 0Þ  =3. For a subset A  T and r > 0, we put Ar :¼ fz 2 T j dTðz; AÞ  rg.
CLAIM 5.4.
fðXÞððS
T 02S T 0ÞSepðX;=3;=3ÞÞ  m  2=3.
PROOF.
Suppose that fðXÞððS
T 02S T 0ÞSepðX;=3;=3ÞÞ < m  2=3. Then, we
have a contradiction since
Sep X; 
3 ; 
3


< dT
[
T 02S
T 0; T n
[
T 02S
T 0
 
!
SepðX;=3;=3Þþ"
0
@
1
A
 Sep fðXÞ; 
3 ; 
3


 Sep X; 
3 ; 
3


for any suﬃciently small " > 0.

Combining Claims 5.2 and 5.4, we obtain
500
K. FUNANO
diamðfðXÞ; m  Þ  diam
[
T 02S
T 0
 
!
SepðX;=3;=3Þ
0
@
1
A
 3 Sep X; 
3 ; 
3


þ 4 ObsDiamRðX; Þ
and so (5.3). This completes the proof of the theorem.

Note that the inequality (5.3) yields a slightly worse estimate for the
observable diameter ObsDiamTðX; Þ than (5.2).
Let T be an R-tree and  2 B1ðTÞ with m :¼ ðXÞ. Taking a median m 2 T
of the measure , we let T an element in C 0
TðcðÞÞ with m 2 T. We then deﬁne
the function ’ : T ! R by ’ðwÞ :¼ dTðcðÞ; wÞ if w 2 T and ’ðwÞ :¼  dTðcðÞ;
wÞ otherwise. The function ’ is clearly the 1-Lipschitz function.
LEMMA 5.5.
Let T be an R-tree and  2 B1ðTÞ. Then, the function ’ :
T ! R satisﬁes that cðð’ÞðÞÞ  0,
jcðð’ÞðÞÞj  CRadðð’ÞðÞ; m  Þ þ Sep ð’ÞðÞ; m
3 ; 
2


ð5:4Þ
þ Sepðð’ÞðÞ; m  ; m  Þ;
and
CRadð; m  Þ  CRadðð’ÞðÞ; m  Þ þ Sep ; m
3 ; 
2


ð5:5Þ
þ Sep ð’ÞðÞ; m
3 ; 
2


þ Sepðð’ÞðÞ; m  ; m  Þ
for any  > 0.
PROOF.
Combining Lemma 2.11 with Proposition 4.1, we have
ðTÞcðð’ÞðÞÞ ¼
Z
T
’ðzÞ dðzÞ ¼
Z
T
dTðcðÞ; zÞdðzÞ 
Z
TnT
dTðcðÞ; zÞdðzÞ
¼ cT;cðÞðÞ  0:
Put r1 :¼ CRadðð’ÞðÞ; m  Þ and r2 :¼ Sepðð’ÞðÞ; m=3; =2Þ. From (5.1),
we observe that ð’ÞðÞðBRð’ðmÞ; r2ÞÞ  ðBTðm; r2ÞÞ  m  . Thus, we get
dRðBRðcðð’ÞðÞÞ; r1Þ; BRð’ðmÞ; r2ÞÞ  Sepðð’ÞðÞ; m  ; m  Þ
ð5:6Þ
Central and Lp-concentration of 1-Lipschitz maps into R-trees
501
and so (5.4). The above inequality (5.6) together with cðð’ÞðÞÞ  0 yields that
dTðcðÞ; mÞ ¼ ’ðmÞ  jcðð’ÞðÞÞ  ’ðmÞj
 r1 þ r2 þ Sepðð’ÞðÞ; m  ; m  Þ ¼: r3:
Therefore, putting r4 :¼ Sepð; m=3; =2Þ, we obtain
ðBTðcðÞ; r3 þ r4ÞÞ  ðBTðm; r4ÞÞ  m  
and so (5.5). This completes the proof.

PROPOSITION 5.6.
Let T be an R-tree and X an mm-space with X 2
B1ðXÞ. Then, for any  > 0 we have
ObsCRadTðX; Þ  ObsCRadRðX; Þ þ 2 Sep X; m
3 ; 
2


þ SepðX; m  ; m  Þ:
PROOF.
This follows from Lemmas 2.2 and 5.5.

PROOF OF THEOREM 1.2.
Proposition 5.6 together with Corollary 2.6 and
Lemma 2.16 directly implies the theorem.

LEMMA 5.7.
Let T be an R-tree and  2 B1ðTÞ. Then, for any p  1 and
 > 0, we have
VpðÞ  2m2=p

CRadðð’ÞðÞ; m  Þ þ Sep ð’ÞðÞ; m
3 ; 
2


ð5:7Þ
þ Sepðð’ÞðÞ; m  ; m  Þ

þ 2Vpð’Þ:
In the case of p ¼ 2, we also have the better estimate
V2ðÞ2  4m2

CRadðð’ÞðÞ; m  Þ þ Sep ð’ÞðÞ; m
3 ; 
2


ð5:8Þ
þ Sepðð’ÞðÞ; m  ; m  Þ
2
þ 2V2ð’Þ2:
PROOF.
From the triangle inequality, we have
VpðÞ  2
Z Z
TT
dTðcðÞ; zÞpdðzÞdðwÞ

1=p
¼ 2 m
Z
T
dTðcðÞ; zÞpdðzÞ

1=p
:ð5:9Þ
502
K. FUNANO
Putting c :¼ cðð’ÞðÞÞ, we also get
Z
T
dTðcðÞ; zÞpdðzÞ

1=p
¼
Z
T
j’ðzÞjpdðzÞ

1=p
ð5:10Þ
 m1=pjcj þ
Z
R
jc  rjpdð’ÞðÞðrÞ

1=p
 m1=pjcj þ Vpð’Þ
m1=p ;
where in the last inequality we used Lemma 2.11. Combining (5.9) with (5.10), we
obtain (5.7).
In the case of p ¼ 2, we have
Z
T
dTðcðÞ; zÞ2dðzÞ ¼
Z
R
jrj2dð’ÞðÞðrÞ
ð5:11Þ
¼ mjcj2 þ
Z
R
jr  cj2dð’ÞðÞðrÞ
¼ mjcj2 þ V2ð’Þ2
2m
;
where in the second and the last equalities we used Lemma 2.11. Substituting
(5.11) to (5.9), we obtain (5.8). This completes the proof.

PROPOSITION 5.8.
Let T be an R-tree and X an mm-space. Then, for any
p  1, we have
Obs Lp-VarTðXÞ  2f21=pð1 þ 2 
 21=pÞ þ 1gObs Lp-VarRðXÞ:
ð5:12Þ
In the case of p ¼ 2, we also have the better estimate
Obs L2-VarTðXÞ2  ð38 þ 16
ﬃﬃ
2
p
ÞObs L2-VarRðXÞ2:
ð5:13Þ
PROOF.
Assume
ﬁrst
that
fðXÞ 2 B1ðTÞ for
any
1-Lipschitz
map
f : X ! T. Then, Lemma 2.2 together with Lemma 2.3 and (5.7) implies that
Central and Lp-concentration of 1-Lipschitz maps into R-trees
503
Obs Lp-VarTðXÞ  2m2=p
ObsCRadRðX; Þ þ Sep X; m
3 ; 
2




þ 2Obs Lp-VarRðXÞ
 2m2=p
ObsCRadRðX; Þ þ Sep X; 
2 ; 
2




þ 2Obs Lp-VarRðXÞ
for any 0 <  < m=2. Hence, applying the inequalities (2.3) and (2.5) to this
inequality, we get
Obs Lp-VarTðXÞ  2fm1=p1=pð1 þ 2 
 21=pÞ þ 1gObs Lp-VarRðXÞ
for any 0 <  < m=2. Letting  ! m=2, we get (5.12). In the case of p ¼ 2, from
(5.8), we have
Obs L2-VarTðXÞ2  4m2
ObsCRadRðX; Þ þ Sep X; 
2 ; 
2



2
þ 2Obs L2-VarRðXÞ2
for any 0 <  < m=2. Therefore, substituting the inequalities (2.4) and (2.6) to
this inequality, we get
Obs L2-VarTðXÞ2  2fm1ð2
ﬃﬃ
2
p
þ 1Þ2 þ 1gObs L2-VarRðXÞ2
for any 0 <  < m=2. Letting  ! m=2, we obtain (5.13).
We consider the other case that there exists a 1-Lipschitz map f : X ! T
with fðXÞ =2 B1ðTÞ. By using Ho¨lder’s inequality and Fubini’s theorem, we have
VpðfÞ ¼ þ1. Taking x0 2 X, we put fn :¼ fjBXðx0;nÞ for each n 2 N. From Lemma
2.7 and the above proof, we have
VpðfnÞ  Obs Lp-VarTðBXðx0; nÞÞ  2f21=pð1 þ 2 
 21=pÞ þ 1gObs Lp-VarRðBXðx0; nÞÞ
 2f21=pð1 þ 2 
 21=pÞ þ 1gObs Lp-VarRðXÞ:
Since V2ðfnÞ ! V2ðfÞ ¼ þ1 as n ! 1, this implies Obs Lp-VarRðXÞ ¼ þ1. This
completes the proof.

PROOF OF THEOREM 1.3.
Proposition 5.8 directly implies the theorem. 
504
K. FUNANO
ACKNOWLEDGEMENTS.
The author would like to express his thanks to
Professor Takashi Shioya for his valuable suggestions and assistances during the
preparation of this paper. He thanks Professor Vitali Milman and Professor Shin-
ichi Ohta for useful comments. He also thanks the referee for carefully reading the
manuscript and fruitful suggestions. Without them, this work would have never
been completed.
