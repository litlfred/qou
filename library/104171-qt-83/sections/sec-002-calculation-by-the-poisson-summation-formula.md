---
doc_id: 104171-qt-83
doc_title: "DOI 10.4171/QT/83 Quantum Topology © European Mathematical Society On the asymptotic expansion of the Kashaev invariant of the 52 knot T omotada Ohtsuki1"
section_id: sec-002-calculation-by-the-poisson-summation-formula
section_title: "Calculation by the Poisson summation formula"
section_number: null
pages: 25-63
source_pdf: 10.4171-qt-83.pdf
source_sha256: d95b9363de2766d2
doc_brief: "DOI 10.4171/QT/83 Quantum Topology © European Mathematical Society On the asymptotic expansion of the Kashaev invariant of the 52 knot Tomotada Ohtsuki1 — We give a presentation of the asymptotic"
---
In this section, we calculate the sums corresponding to the i ntegrals of the propo-
sitions in the previous section by the Poisson summation for mula. Corresponding
to Propositions /three.prop./one.prop, /three.prop./two.prop, /three.prop./four.propand /three.prop./five.propin the previous section, we show Proposi-
tions /four.prop./one.prop, /four.prop./two.prop, /four.prop./five.prop, and /four.prop./six.propin this section. We use Proposition /four.prop./six.propin the proof of
Theorem /one.prop./one.propin Section /five.prop. We remark that the Poisson summation formula has also
been used in the study of large level asymptotics of quantum i nvariants of Seifert
/three.prop-manifolds [/one.prop/three.prop], [/one.prop/four.prop], [/three.prop/zero.prop], [/three.prop/one.prop], [/three.prop/two.prop].
Recall (see e.g. [ /three.prop/three.prop]) that the Poisson summation formula states that
X
m2Zn
f. m/ D
X
m2Zn
Of. m/ (30)
for a continuous integrable function f on Rn which satis/f_ies that
jf. z/j C.1 C jzj//NUL n/NUL ı; (31a)
and
j Of. z/j C.1 C jzj//NUL n/NUL ı (31b)
for someC;ı>0 , where Of is the Fourier transform of f de/f_ined by
Of. w/ D
Z
Rn
f. z/e/NUL 2
p
/NUL 1w T zd z:
694 T. Ohtsuki
Proposition /four.prop./one.prop.Leta;c be complex numbers satisfying that
Rea<0; j Imcj< /NUL
2 Re1
a:
We put
ƒ D
°k
N Cc 2 C
ˇ
ˇ
ˇk 2 Z; b0  k
N b1
±
and
C D ¹t Cc 2 C jt 2 R; b0 t b1º
for someb0;b1 2 R and"0>0 satisfying that Re.b0 Cc/<0< Re.b1 Cc/ and
Rea.bi Cc/2< /NUL"0.i D0;1/ /semicolon.alt see Figure/four.prop. Then, there exists ">0 such that
1
N
X
z2ƒ
eN az2
D
Z
C
eN az2
dz CO.e /NUL "N/:
We note that" depends ona,c and"0.
b0 Cc
b1 Cc
ƒ
Figure /four.prop. The domain¹z 2 C j Reaz 2<0 º is shaded.
Proof. By Proposition /three.prop./one.prop, the required formula is rewritten
X
k2Z
b0k=N b1
eN a.k=N Cc/2
D
p 
p
Np/NULa CO.e /NUL "N/:
On the asymptotic expansion of the Kashaev invariant of the 52 knot 695
Since
X
k2Z
k=N<b 0
eN a.k=N Cc/2
DO.e /NUL "N/;
and X
k2Z
b1<k=N
eN a.k=N Cc/2
DO.e /NUL "N/;
for some">0 , it is suﬃcient to show that
X
k2Z
eN a.k=N Cc/2
D
p 
p
Np/NULa CO.e /NUL "N/: (32)
In order to apply the Poisson summation formula ( /three.prop/zero.prop), we put
f.z/ DeN a.z=N Cc/2
:
Then, its Fourier transform is
Of./ D
Z 1
/NUL1
eN a.z=N Cc/2 /NUL 2
p
/NUL 1zdz
D
Z 1
/NUL1
e.a=N/.z CcN /NUL 
p
/NUL 1N=a/ 2
dz eN 2 2=aC2
p
/NUL 1cN
D
p 
p
Np/NULa eN 2 2=aC2
p
/NUL 1cN;
where we obtain the last equality by Proposition /three.prop./one.prop. These f.z/ and Of./ satisfy
the assumption ( /three.prop/one.prop) of the Poisson summation formula. Hence, by the Poisson
summation formula (/three.prop/zero.prop),
X
k2Z
eN a.k=N Cc/2
D
p 
p
Np/NULa
X
m2Z
eN 2m2=aC2
p
/NUL 1cNm:
The summand atm D0 gives the right-hand side of (/three.prop/two.prop). Whenm ¤0, the power
of the summand is
N m2

a C2
p
/NUL1c
m

;
and its real part is negative by the assumption of the proposi tion. Hence, the
summands atm ¤0 are of ordere/NUL "N for some">0 . Therefore, we obtain ( /three.prop/two.prop).

696 T. Ohtsuki
We generalize Proposition /four.prop./one.propto the case where there are perturbative terms in
the exponential of the summand.
Proposition /four.prop./two.prop.We put
ƒ D
°k
N Cc 2 C
ˇ
ˇ
ˇk 2 Z; b0  k
N b1
±
;
and
C D ¹t Cc 2 C jt 2 R; b0 t b1º
for some b0;b1 2 R andc 2 C. Let a be a complex number whose real part is
negative, letı0 be a real positive number, and let .z/ be a holomorphic function
of the form
 .z/ Daz2 Cb3z3 Cb4z4 C   ;
de/f_ined in a neighborhood of 0 including the ı0-neighborhood of C . The do-
main /parenleft.alt/one.prop/five.prop/parenright.alt has two connected components in a neighborhood of0. We assume that
b0Cc andb1Cc are in these two components respectively, andRe .bi Cc/< /NUL"0
.i D0;1/ for some"0>0 ..See Figure /five.prop./ Further, we assume that
b0 Cc andb1 Cc are in the same connected component of
¹w Cı
p
/NUL1 2 C jw 2C; ı2Œ0;ı0; Re. .w Cı
p
/NUL1/ /NUL2ı/<0 º;
(33)
and
they are in the same connected component of
¹w /NULı
p
/NUL1 2 C jw 2C; ı2Œ0;ı0; Re. .w /NULı
p
/NUL1/ /NUL2ı/<0 º:
(34)
Then,
1
N
X
z2ƒ
eN .z/ D
Z
C
eN .z/dz CO.e /NUL N"/
for some">0 .
We note that" depends on .z/ ,c,ı0 and"0; in particular, " directly depends on
"0
2 of (
/three.prop/nine.prop) in the proof of the proposition.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 697
b0 Cc
b1 Cc
ƒ
Figure /five.prop. The domain¹z 2 C j Re .z/<0 º is shaded.
Proof. The sum of the left-hand side of the required formula is rewri tten
X
k2Z
b0k=N b1
exp

N  
k
N Cc

: (35)
In order to apply the Poisson summation formula ( /three.prop/zero.prop), we put
f.z/ Dg
z
N Cc

exp

N  
z
N Cc

;
whereg is a diﬀerentiable function on R Cc satisfying that
g.w/ D
´
1 ifw 2C;
0 ifw …N.C/;
0 g.w/ 1 ifw 2N.C/ /NULC:
Here,N.C/ is a neighborhood ofC in R Cc such thatN.C/ /NULC is included in the
domain ¹z 2 C j Re .z/< /NUL"0=2º. Then, the Fourier transform of f is given by
Of./ D
Z
R
g
z
N Cc

exp

N  
z
N Cc

e/NUL 2
p
/NUL 1zdz
DN
Z
RCc
g.w/eN. .w/ /NUL 2
p
/NUL 1.w /NUL c//dw;
where we put
w Dz=N Cc:
698 T. Ohtsuki
Further,
2 Of./ D /NUL 1
42N
Z
RCc
g.w/eN .w/
 d
dw
2
e/NUL 2
p
/NUL 1N.w /NUL c/

dw
D /NUL 1
42N
Z
RCc
 d
dw
2
g.w/eN .w/

e/NUL 2
p
/NUL 1N.w /NUL c/dw
D /NUL 1
42N
Z
RCc
h.w/eN .w/e/NUL 2
p
/NUL 1N.w /NUL c/dw;
where we put
h.w/ Dg00.w/ C2g0.w/ 0.w/ Cg.w/. 00.w/ C 0.w/2/:
Since the above integral is bounded independently of , Of./ satis/f_ies the as-
sumption (/three.prop/one.prop) of the Poisson summation formula. Further, f.z/ also satis/f_ies (/three.prop/one.prop).
Therefore, by the Poisson summation formula ( /three.prop/zero.prop),
(/three.prop/five.prop) D
X
m2Z
Of.m/:
Whenm ¤0, we have that
Of.m/ D /NUL 1
42N  1
m2
Z
RCc
h.w/eN. .w/ /NUL 2
p
/NUL 1m.w/NUL c//dw
D /NUL 1
42N  1
m2
Z
C
. 00.w/ C 0.w/2/eN. .w/ /NUL 2
p
/NUL 1m.w/NUL c//dw (36)
/NUL 1
42N  1
m2
Z
N.C/ /NUL C
h.w/eN. .w/ /NUL 2
p
/NUL 1m.w/NUL c//dw; (37)
sinceh.w/ D 00.w/ C 0.w/2 forw 2C andh.w/ D0 forw 2.R Cc/ /NULN.C/ .
Further, since Re .w/< /NUL"0=2 forw 2N.C/ /NULC ,
X
m¤0
(/three.prop/seven.prop) DO.e /NUL N" 1/
for some"1>0 . Furthermore, whenm>0 , by pushing the contourC to a contour
C 0 in the domain of ( /three.prop/four.prop), we can show that
Z
C
. 00.w/ C 0.w/2/eN. .w/ /NUL 2
p
/NUL 1m.w/NUL c//dw
D
Z
C 0
. 00.w/ C 0.w/2/eN. .w/ /NUL 2
p
/NUL 1m.w/NUL c//dw
DO.e /NUL N" 2/
(38)
On the asymptotic expansion of the Kashaev invariant of the 52 knot 699
for some "2 > 0, which we can choose independently of m, since there exists
"0
2>0 such that
Re. .w/ /NUL2
p
/NUL1.w /NULc//< /NUL"0
2 (39)
for anyw 2C 0. Hence, X
m>0
(
/three.prop/six.prop) DO.e /NUL N" 2/:
When m < 0, by pushing the contour C into the domain of ( /three.prop/three.prop), we similarly
obtain X
m<0
(/three.prop/six.prop) DO.e /NUL N" 3/
for some"3>0 . Therefore,
X
m¤0
Of.m/ DO.e /NUL N" 4/
for some"4>0 . Hence,
(/three.prop/five.prop) D Of.0/ CO.e /NUL N" 4/ DN
Z
C
eN .w/dw CO.e /NUL N" 5/
for some"5>0 , and this implies the required formula. 
Remark /four.prop./three.prop.The assumptions ( /three.prop/three.prop) and ( /three.prop/four.prop) of Proposition /four.prop./two.propcan be replaced
with the condition that there exist positive integers m0;m1 and positive real
numbers ı0;ı1 such that for any integer m satisfying that /NULm0 < m < 0or
0<m<m 1, Z
C
eN. .w/ /NUL 2
p
/NUL 1m.w/NUL c//dw DO.e /NUL N"/
for some">0 , and
b0 Cc andb1 Cc are in the same connected component of
¹w Cı
p
/NUL1 2 C jw 2C; ı2Œ0;ı1; Re. .w Cı
p
/NUL1/ /NUL2ım1/<0 º;
and
they are in the same connected component of
¹w /NULı
p
/NUL1 2 C jw 2C; ı2Œ0;ı0; Re. .w /NULı
p
/NUL1/ /NUL2ım0/<0 º:
Proposition /four.prop./two.propfor this assumption can be proved by modifying the above proo f
of Proposition /four.prop./two.prop.
700 T. Ohtsuki
Remark /four.prop./four.prop.Proposition /four.prop./two.propcan naturally be extended to the case where the
holomorphic function  .z/ depends on N , if  .z/ uniformly converges
to 0.z/ asN ! 1 , and  0.z/ satis/f_ies the assumption of the proposition, and
j 00.z/ C 0.z/2j is bounded by a constant which is independent of N . In this
case, (/three.prop/nine.prop) holds for suﬃciently large N , and hence, ( /three.prop/eight.prop) holds. Therefore, Propo-
sition /four.prop./two.propalso holds in this case, where we note that we can choose" independently
ofN .
We generalize Proposition /four.prop./one.propto the case of n variables.
Proposition /four.prop./five.prop.For c 2 Cn and an orientedn-ballD0 in Rn, we put
ƒ D
°1
N k C c 2 Cn
ˇ
ˇ
ˇ k 2 Zn; 1
N k 2D0
±
;
and
D D ¹z C c 2 Cn j z 2D0  Rnº:
Let A be a non-singular symmetric complex n n matrix such that Re.A/NUL 1/ is
negative de/f_inite. We assume that@D is included in the domain /parenleft.alt/two.prop/four.prop/parenright.alt. Further, we
assume that
.Im c/T m< /NUL
2 mT  Re.A/NUL 1/  m
for any m 2 Zn /NUL¹ 0º. Then
1
Nn
X
z2ƒ
eN zTAz D
Z
D
eN zTAzd z CO.e /NUL N"/;
for some">0 .
Proof. By Proposition /three.prop./four.prop, the required formula is rewritte
X
z2ƒ
eN zTAz D n=2Nn=2
p
det./NULA/
CO.e /NUL "N/: (40)
Further, in a similar way as in the proof of Proposition /four.prop./one.prop, putting
f. z/ DeN .z=N Cc/TA.z=N Cc/;
we can show that
Of./ D n=2Nn=2
p
det./NULA/
eN 2 TA/NUL 1C2
p
/NUL 1N cT
On the asymptotic expansion of the Kashaev invariant of the 52 knot 701
by using Proposition /three.prop./four.prop. Hence, we obtain
X
k2Zn
eN .k=N Cc/TA.k=N Cc/ D n=2Nn=2
p
det./NULA/
X
m2Zn
eN 2mTA/NUL 1mC2
p
/NUL 1N cT m
by the Poisson summation formula ( /three.prop/zero.prop). By the assumption of the proposition,
the real part of
N2mTA/NUL 1m C2
p
/NUL1N cT m
is negative for any m 2 Zn/NUL¹0º. Therefore, only the summand at m D 0 survives,
and we obtain ( /four.prop/zero.prop) from it. 
We generalize Proposition /four.prop./five.propto the case where there are perturbative terms in
the exponential of the summand. Let e1; e2;:::; en be the standard basis vectors
of Cn,
e1 D.1;0;   ;0/T; e2 D.0;1;0;   ;0/T; :::; en D.0;   ;0;1/ T:
Proposition /four.prop./six.prop.For c 2 Cn and an orientedn-ballD0 in Rn, we put
ƒ D
°1
N k C c 2 Cn
ˇ
ˇ
ˇ k 2 Zn; 1
N k 2D0
±
;
and
D D ¹z C c 2 Cn j z 2D0  Rnº:
Let A be a non-singular symmetric complex n  n matrix, and let
 .z/ be a holomorphic function of the form /parenleft.alt/two.prop/five.prop/parenright.alt de/f_ined in a neighborhood
of 0 2 Cn including D. We assume that @D is included in the domain®
z 2 Cn j Re .z/ < /NUL"0
¯
for some "0 > 0. Further, we assume that there
existıi;ı 0
i >0.i D1;   ;n/ such that
@D is null-homotopic in
¹w Cı
p
/NUL1ei 2 Cn j w 2D; ı2Œ0;ıi; Re. .w Cı
p
/NUL1ei/ /NUL2ı/<0 º;
(41)
and
@D is null-homotopic in
¹w /NULı
p
/NUL1ei 2 Cn j w 2D; ı2Œ0;ı 0
i; Re. .w /NULı
p
/NUL1ei/ /NUL2ı/<0 º;
(42)
fori D1;   ;n , assuming that is holomorphic in these domains. Then
1
Nn
X
z2ƒ
eN . z/ D
Z
D
eN . z/d z CO.e /NUL N"/;
for some">0 .
702 T. Ohtsuki
We note that" depends on .z/, c,ıi ,ı0
i and"0.
Proof. The sum of the left-hand side of the required formula is rewri tten,
X
k2Zn
k=N 2D0
exp

N  
1
N k C c

: (43)
In order to apply the Poisson summation formula ( /three.prop/zero.prop), we put
f. z/ Dg
1
N z C c

exp

N  
1
N z C c

;
whereg is a diﬀerentiable function on RnC c satisfying that
g.w/ D
´
1 if w 2D;
0 if w …N.D/;
0 g.w/ 1 if w 2N.D/ /NULD:
Here,N.D/ is a neighborhood of D in Rn C c such that N.D/ /NULD is included
in the domain
®
z 2 Cn j Re .z/< /NUL"0=2
¯
. Then, the Fourier transform of f is
given by
Of./ D
Z
Rn
g
1
N z C c

exp

N  
1
N z C c

e/NUL 2
p
/NUL 1 T zd z
DNn
Z
RnCc
g.w/eN. . w//NUL 2
p
/NUL 1 T.w /NUL c//d w;
where we put w D z=N C c. Further, for an integer l >n=2,
jj2l Of./
D
 nX
i D1
2
i
l
Of./
DNn
 /NUL1
42N
lZ
RnCc
g.w/eN . w/
 nX
i D1
@2
@w2
i
l
e/NUL 2
p
/NUL 1N T.w /NUL c/

d w
DNn
 /NUL1
42N
lZ
RnCc
 nX
i D1
@2
@w2
i
l
g.w/eN . w/

e/NUL 2
p
/NUL 1N T.w /NUL c/d w
DNn
 /NUL1
42N
lZ
RnCc
h.w/eN . w/e/NUL 2
p
/NUL 1N T.w /NUL c/d w;
whereh.w/ is some polynomial in derivatives ofg.w/ and .w/. Since the above
integral is bounded independently of , Of./ satis/f_ies the assumption (/three.prop/one.prop) of the
On the asymptotic expansion of the Kashaev invariant of the 52 knot 703
Poisson summation formula. Further, f. z/ also satis/f_ies (/three.prop/one.prop). Therefore, by the
Poisson summation formula ( /three.prop/zero.prop),
(/four.prop/three.prop) D
X
m2Zn
Of. m/:
When m ¤ 0, we have
Of. m/ DNn
 /NUL1
42N
l
 1
jmj2l
Z
RnCc
h.w/eN. . w//NUL 2
p
/NUL 1mT.w /NUL c//d w
DNn
 /NUL1
42N
l
 1
jmj2l
Z
D
‰.w/eN. . w//NUL 2
p
/NUL 1mT.w /NUL c//d w (44)
CNn
 /NUL1
42N
l
 1
jmj2l
Z
N.D//NUL D
h.w/eN. . w//NUL 2
p
/NUL 1mT.w /NUL c//d w; (45)
where‰.w/ is some polynomial in (at most the2lth) derivatives of .w/. Further,
since Re .w/<0 for w 2N.D/ /NULD,
X
m¤0
(/four.prop/five.prop) DO.e /NUL N" 1/
for some "1 > 0. Furthermore, when m1 > 0, pushing the contour D into the
domain of (/four.prop/two.prop), we obtain
X
m2Zn
m1>0
(/four.prop/four.prop) DO.e /NUL N" 2/
for some"2>0 , similarly as in the proof of Proposition /four.prop./two.prop. Similarly we obtain
X
m2Zn
m1<0
(/four.prop/four.prop) DO.e /NUL N" 3/
for some"3>0 , from the assumption ( /four.prop/one.prop). Hence,
X
m¤0
(/four.prop/four.prop) D
X
m¤0
m1D0
(/four.prop/four.prop) CO.e /NUL N" 4/
for some"4>0 . By repeating this argument for m2;:::;m n, we obtain
X
m¤0
(/four.prop/four.prop) DO.e /NUL N" 5/
for some"5>0 . Therefore,
(/four.prop/three.prop) D Of. 0/ CO.e /NUL N" 6/ DNn
Z
D
eN . w/d w CO.e /NUL N" 6/
for some"6>0 , and this implies the required formula. 
704 T. Ohtsuki
Remark /four.prop./seven.prop.The assumptions ( /four.prop/one.prop) and ( /four.prop/two.prop) of Proposition /four.prop./six.propcan be modi/f_ied
similarly as in Remark /four.prop./three.prop.
Remark /four.prop./eight.prop.Similarly as in Remark /four.prop./four.prop, Proposition /four.prop./six.propcan naturally be ex-
tended to the case where the holomorphic function  .z/ depends on N , if  .z/
uniformly converges to 0.z/ asN ! 1 , and  0.z/ satis/f_ies the assumption of
the proposition, and j‰.z/j is bounded by a constant which is independent of N .
Similarly as in Remark /four.prop./four.prop, we can also choose" independently ofN in this case.
/five.prop. Proof of Theorem/one.prop./one.prop
In this section, we give a proof of Theorem /one.prop./one.prop. In Section /five.prop./one.prop, we give a proof of
the theorem by using lemmas proved in Sections /five.prop./two.prop, /five.prop./three.prop, and /five.prop./four.prop. In Section /five.prop./two.prop,
we show lemmas which calculate the asymptotic expansion. In Section /five.prop./three.prop,
we show a lemma which veri/f_ies the assumption of the saddle poi nt method.
In Section /five.prop./four.prop, we show a lemma which veri/f_ies the assumption of the Poisson
summation formula.
/five.prop./one.prop. Proof of Theorem
/one.prop./one.prop. In this section, we give a proof of Theorem/one.prop./one.prop, which
presents the asymptotic expansion of the Kashaev invariant h52iN of the52 knot.
To obtain the asymptotic expansion, as mentioned in Section /two.prop./two.prop, we rewrite
the sum ( /one.prop/four.prop) of h52iN by using an integral by the Poisson summation formula
(Proposition /four.prop./six.prop) and calculate the asymptotic expansion of the integral by t he
saddle point method (Proposition /three.prop./five.prop).
Proof of Theorem /one.prop./one.prop. We recall thath52iN is presented by the sum (/one.prop/four.prop). By Propo-
sition /four.prop./six.prop(Poisson summation formula) (see also Remark /four.prop./eight.propand Appendix B),
this sum is expressed by the integral
h52iN DeN&N5=2q
Z
0
exp.N V.t;s/ /NULN&/dtds CO.e /NUL N" 4/

(46)
for some "4 > 0, noting that we verify the assumptions of Proposition /four.prop./six.propin
Lemma /five.prop./eight.propbelow.
In order to apply the saddle point method (Proposition/three.prop./five.prop, see also Remark /three.prop./six.prop
and Appendix B) to ( /four.prop/six.prop), we consider a critical point of yV.t;s/ . From the
On the asymptotic expansion of the Kashaev invariant of the 52 knot 705
de/f_inition of yV.t;s/ , a critical point is a solution of the equations
@
@t
yV.t;s/ D /NUL log.1 /NULe/NUL 2
p
/NUL 1t/ /NUL2
p
/NUL1

t Cs /NUL 1
2

D0; (47a)
@
@s
yV.t;s/ D /NUL2 log.1 /NULe/NUL 2
p
/NUL 1s/ /NUL2
p
/NUL1.t C2s /NUL1/ D0: (47b)
Hence, puttingx De2
p
/NUL 1t andy De2
p
/NUL 1s,

1 /NUL 1
x

xy D /NUL1;

1 /NUL 1
y
2
xy2 D1:
Therefore,
x D1 /NUL 1
y; .y /NUL1/3 Dy:
Let .x0;y0/ be the solution of these equations mentioned in the introduc tion.
We consider the critical point .t0;s0/ such that
.Ret0; Res0/ 20 and .e2
p
/NUL 1t0;e2
p
/NUL 1s0/ D.x0;y0/:
It is numerically given by
t0 D0:22404487::: /NUL
p
/NUL1 0:04475430:::;
s0 D0:16393269::: C
p
/NUL1 0:06713145::::
Let .tc;sc/ be the critical point of V.t;s/ which goes to .t0;s0/ as N ! 1 .
We consider to apply Proposition/three.prop./five.proptoV.t /NULtc;s /NULsc/. We consider the expansion
V.t;s/ DV.tc;sc/C1
2Vtt .t /NULtc/2CVts .t /NULtc/.s/NULsc/C1
2Vss .s/NULsc/2 C   (48)
at the critical point, where we put
Vtt D @2V
@t2.tc;sc/; V ts D @2V
@t@s.tc;sc/; V ss D @2V
@s2.tc;sc/:
As we show in Section /five.prop./three.prop, we can make a concrete homotopy which moves0 to
a new domain containing the above critical point in such a way that it satis/f_ies
the assumption of the saddle point method. 6 Hence, we obtain the following
6 That is, the new domain is in the area Re yV.t;s/ &R /NUL " except for a neighborhood of the
above critical point. In order to obtain this new domain, it i s suﬃcient to push the shaded part in
Figure /one.propinto the imaginary direction by ./NUL
p
/NUL 1 0:04475430:::;
p
/NUL 1 0:06713145:::/ . For
details, see Section /five.prop./three.prop.
706 T. Ohtsuki
expansion by applying Proposition /three.prop./five.prop(see also Remark /three.prop./six.propand Appendix B)
to (/four.prop/six.prop):
h52iN DN5=2q exp

NV.t c;sc/

2
N .VttVss /NULV2
ts//NUL 1=2

1C
dX
i D1
i „i CO.„d C1/

;
(49)
wherei ’s are given in the proposition, noting that we verify the ass umptions of
Proposition /three.prop./five.propin Lemma /five.prop./seven.propbelow. Here, we also note that eN& O.e /NUL N" 4/
in (/four.prop/six.prop) is included in exp.NV.t c;sc// O.„d C1/ in (/four.prop/nine.prop); see Lemma /five.prop./two.propbelow
for the behavior of exp.NV.t c;sc//.
We calculate the concrete form of ( /four.prop/nine.prop), for simplicity, when d D 1.
By Lemmas /five.prop./two.prop, /five.prop./three.prop, and /five.prop./four.propbelow, (/four.prop/nine.prop) is rewritten
h52iN DN5=2q eN&e/NUL 
p
/NUL 1=4.1 /NULy0/1=2.1 C.C1 CC2/„ CO.„2//2
N
1
2
p
/NUL1
./NUL2y0 /NUL1//NUL 1=2.1 CC3„ CO.„2//.1 C.C4 CC5/„ CO.„2//
DeN&N3=2e
p
/NUL 1=4
2y0 C1
y0 /NUL1
/NUL 1=2
.1 C „.1 CC1 CC2 CC3 CC4 CC5/ CO.„2//;
where the constants C1;:::;C 5 are given in the lemmas. In particular, 1 of the
theorem is given by
1 D1 CC1 CC2 CC3 CC4 CC5
D 1
184./NUL16y2
0 C33y0 C9/ C 1
24.2y2
0 /NUL5y0/ C 1
46.8y2
0 /NUL17y0 C9/
C 1
92.2y2
0 C15y0/ /NUL 1
3174.197y2
0 C127y0 C227/ C1
D 1
12696.1650y2
0 /NUL3498y0 C2197/ C1:
Hence, we obtain the required formula for d D1.
For generald , eachi of the expansion (/four.prop/nine.prop) is given by a linear sum of higher
coeﬃcients of the expansion ( /four.prop/eight.prop) by Proposition /three.prop./five.prop(see also Remark /three.prop./six.propand
Appendix B). In the same way as the above case of d D1, such coeﬃcients are
given by some polynomials iny0 with rational coeﬃcients. Hence, each i of the
theorem can be given by some polynomial in y0 with rational coeﬃcients. 
On the asymptotic expansion of the Kashaev invariant of the 52 knot 707
/five.prop./two.prop. Calculation of the asymptotic expansion.In this section, we show some
lemmas used in the proof of Theorem /one.prop./one.prop.
Let.t0;s0/ and.tc;sc/ be the critical points of yV.t;s/ andV.t;s/ given in the
previous section. We put x0 D e2
p
/NUL 1t0,y0 De2
p
/NUL 1s0, and xc De2
p
/NUL 1tc ,
yc De2
p
/NUL 1sc . In order to show Lemma /five.prop./two.propbelow, we calculate.xc;yc/ in terms
of.x0;y0/, as follows. We show a proof of the following lemma in Appendi x C.
Lemma /five.prop./one.prop.We can put xc Dx0 Cx1„ CO.„2/ andyc Dy0 Cy1„ CO.„2/
for some x1;y1 2 C in a suﬃciently small neighborhood of .x0;y0/ .i.e., for
suﬃciently large N/ . Here,O.„2/ means that the absolute value of the error term
is bounded by C „2 with a constantC which is independent of N .
We calculate x1 andy1, as follows. We put x D e2
p
/NUL 1t andy D e2
p
/NUL 1s.
From the de/f_inition ofV.t;s/ and Proposition A./one.prop, we have
@
@tV.t;s/ D /NUL log

1 /NUL 1
x

/NUL2
p
/NUL1

t Cs /NUL 1
2 /NUL 1
2N

CO.„2/; (50a)
and
@
@sV.t;s/ D /NUL2 log

1 /NUL 1
y

/NUL2
p
/NUL1

t C2s /NUL1 /NUL 1
2N

CO.„2/: (50b)
Then, since.tc;sc/ is a critical point of V.t;s/ ,
8
ˆ
ˆ
<
ˆ
ˆ
:

1 /NUL 1
xc

./NULq/NUL 1=2xcyc/ D1 CO.„2/;

1 /NUL 1
yc
2
q/NUL 1=2xcy2
c D1 CO.„2/:
These are rewritten,
8
<
:
.1 /NULxc/yc Dq1=2 CO.„2/;
q1=2yc D.yc /NUL1/2.yc /NULq1=2/ CO.„2/:
Hence, puttingxc Dx0 Cx1„CO.„2/ andyc Dy0 Cy1„CO.„2/ by Lemma
/five.prop./one.prop,
we have
8
<
:
x0 D1 /NUL 1
y0
;
y0 D.y0 /NUL1/3;
8
ˆ
<
ˆ
:
/NUL x1
1 /NULx0
Cy1
y0
D 1
2;
y1 C1
2y0 D.y0 /NUL1/2

3y1 /NUL 1
2

:
Therefore, we obtain
y1 D y2
0
2.2y0 C1/; x 1 D /NUL y0 C1
2y0.2y0 C1/:
708 T. Ohtsuki
Further, in order to show Lemmas /five.prop./two.prop, /five.prop./three.propand /five.prop./four.propbelow, we calculate the
expansion (/four.prop/eight.prop) concretely, as follows. Putting Lt Dt /NULtc, we expand'.1 /NULt/=N
attc as follows:
'.1 /NULt/
N D '.1 /NULtc/
N /NUL '0.1 /NULtc/
N
Lt C1
2
'00.1 /NULtc/
N
Lt2
/NUL 1
6
'.3/.1 /NULtc/
N
Lt3 C 1
24
'.4/.1 /NULtc/
N
Lt4 C   ;
where we can calculate '.k/.1 /NUL tc/=N concretely by Proposition A./one.prop. Hence,
putting Lt Dt /NULtc and Ls Ds /NULsc, we can show by concrete calculation thatV.t;s/
is expanded at a critical point .tc;sc/ in the form
V.t;s/ DV.tc;sc/ C.degree /two.prop part/ C.degree /three.prop part/
C.degree /four.prop part/ C.degree 5 part/;
(51)
where
.degree /two.prop part/ D2
p
/NUL1
 Lt2
2
1
1 /NULxc
C Ls2
2
1 Cyc
1 /NULyc
/NUL .Lt C Ls/2
2

CO.„2/; (52)
.degree /three.prop part/ D.2
p
/NUL1/2.y0 /NUL1/
 Lt3
6 y0 C Ls3
6 2

CO.„/; (53)
.degree /four.prop part/ D.2
p
/NUL1/3
 Lt4
24.x2
0 Cx0/y3
0 /NUL Ls4
242.y0 C1/

CO.„/: (54)
Now, we show lemmas used in the proof of Theorem /one.prop./one.prop.
Lemma /five.prop./two.prop.Under the notation in the proof of Theorem /one.prop./one.prop,
exp.NV.t c;sc// DeN&e/NUL 
p
/NUL 1=4.1 /NULy0/1=2.1 C.C1 CC2/„ CO.„2//;
where we put
C1 D 1
184./NUL16y2
0 C33y0 C9/; C 2 D 1
24.2y2
0 /NUL5y0/:
Proof. We puttc D t0 Ct1=N C    andsc D s0 Cs1=N C    . Recalling that
xc De2
p
/NUL 1tc andyc De2
p
/NUL 1sc , we have
t1 D x1
x0
D /NUL y0 C1
2.y0 /NUL1/.2y0 C1/; s 1 D y1
y0
D y0
2.2y0 C1/:
On the asymptotic expansion of the Kashaev invariant of the 52 knot 709
Putting Lt D /NULt1=N and Ls D /NULs1=N in the degree /two.prop part (/five.prop/two.prop) of the expansion (/five.prop/one.prop),
we have
V.t0;s0/ DV.tc;sc/C2
p
/NUL1
 t2
1
2N2
1
1 /NULx0
C s2
1
2N2
1 Cy0
1 /NULy0
/NUL.t1 Cs1/2
2N2

CO.„3/:
Hence,
NV.t c;sc/ DNV.t 0;s0/ CC1„ CO.„2/;
where we put
C1 D /NUL1
2

t2
1
1
1 /NULx0
Cs2
1
1 Cy0
1 /NULy0
/NUL.t1 Cs1/2

D 1
184./NUL16y2
0 C33y0 C9/:
Hence,
exp.NV.t c;sc// D exp.NV.t 0;s0// .1 CC1„ CO.„2//: (55)
Further, we calculate V.t0;s0/, as follows. From the de/f_inition of V.t;s/ ,
we have
V.t0;s0/ D 1
N./NUL'.1 /NULt0/ /NUL2'.1 /NULs0// /NUL 1
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
t0 Cs0 /NUL 1
2N
2
C1
2s2
0 /NUL 1
2t0 /NULs0 C1
6

/NUL 3
p
/NUL1
4N C
p
/NUL1
4N2 :
Since this goes to yV.t0;s0/ asN ! 1, we have
yV.t0;s0/
D 1
2
p
/NUL1

/NUL Li2
/NUL 1
x0

/NUL2 Li2
/NUL 1
y0

/NUL 2
6

/NUL2
p
/NUL1
1
2.t0 Cs0/2 C1
2s2
0 /NUL 1
2t0 /NULs0 C1
6

D 1
2
p
/NUL1

Li2.x0y0/ C Li2
 1
x0y0

C Li2.y0/ /NUL Li2
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
D&:
710 T. Ohtsuki
Hence, by Proposition A./one.prop,
V.t0;s0/ D& C2
p
/NUL1t0 Cs0
2N /NUL 3
p
/NUL1
4N
C2
p
/NUL1
N2
 1
24.x0 /NUL1/ C 1
12.y0 /NUL1/

CO
 1
N3

:
Therefore,
exp.NV.t 0;s0// DeN&e/NUL 3
4
p
/NUL 1.x0y0/1=2.1 CC2„ CO.„2//
DeN&e/NUL 
p
/NUL 1=4.1 /NULy0/1=2.1 CC2„ CO.„2//;
where we put
C2 D 1
24.x0 /NUL1/ C 1
12.y0 /NUL1/ D 1
24.2y2
0 /NUL5y0/:
Hence, from the above formula and ( /five.prop/five.prop), we obtain the required formula. 
Lemma /five.prop./three.prop.Under the notation in the proof of Theorem /one.prop./one.prop,
VttVss /NULV2
ts D /NUL42./NUL2y0 /NUL1/.1 /NUL2C3„ CO.„2//;
.VttVss /NULV2
ts//NUL 1=2 D 1
2
p
/NUL1
./NUL2y0 /NUL1//NUL 1=2.1 CC3„ CO.„2//;
where we put
C3 D 1
46.8y2
0 /NUL17y0 C9/:
Proof. From the degree /two.prop part (/five.prop/two.prop) of the expansion ( /five.prop/one.prop), we have
Vtt D @2V
@t2.tc;sc/
D2
p
/NUL1
 1
1 /NULxc
/NUL1

CO.„2/
D2
p
/NUL1  xc
1 /NULxc
CO.„2/;
Vts D @2V
@t@s.tc;sc/ D /NUL2
p
/NUL1 CO.„2/;
Vss D @2V
@s2.tc;sc/
D2
p
/NUL1
1 Cyc
1 /NULyc
/NUL1

CO.„2/
D2
p
/NUL1  2yc
1 /NULyc
CO.„2/
On the asymptotic expansion of the Kashaev invariant of the 52 knot 711
Hence,
VttVss /NULV2
ts D /NUL42
 xc
1 /NULxc
 2yc
1 /NULyc
/NUL1

CO.„2/
D /NUL42
2q /NUL 1=2xcy2
c
1 /NULyc
/NUL1

CO.„2/
D /NUL42

/NUL2yc 1 /NULq/NUL 1=2yc
1 /NULyc
/NUL1

CO.„2/
D /NUL42

/NULyc
/NUL
2 C y0
1 /NULy0
„

/NUL1

CO.„2/
D /NUL42./NUL2y0 /NUL1/

1 /NUL y2
0.y0 C2/
.y0 /NUL1/.2y0 C1/2 „

CO.„2/
D /NUL42./NUL2y0 /NUL1/.1 /NUL2C3„/ CO.„2/;
where
C3 D y2
0.y0 C2/
2.y0 /NUL1/.2y0 C1/2 D 1
46.8y2
0 /NUL17y0 C9/:
Therefore, we obtain the required formulas. 
Lemma /five.prop./four.prop.Under the notation in the proof of Theorem /one.prop./one.prop,
1 DC4 CC5;
where we put
C4 D 1
92.2y2
0 C15y0/
and
C5 D /NUL 1
3174.197y2
0 C127y0 C227/:
Proof. We show the lemma by using Proposition/three.prop./five.prop. As shown in Proposition /three.prop./five.prop,
1 consists of two contributions from the degree /three.prop part and the degree /four.prop part of
the expansion (/five.prop/one.prop).
We calculate the contribution from the degree /four.prop part of the expansion (/five.prop/one.prop), as
follows. As in (/five.prop/four.prop), the degree /four.prop part of this expansion is given by
.2
p
/NUL1/3
 Lt4
24.x2
0 Cx0/y3
0 /NUL Ls4
242.y0 C1/

CO.„/: (56)
712 T. Ohtsuki
As explained in Proposition /three.prop./five.prop, the contribution from Lt4 is calculated as
N 
 @
@u1
4
exp

/NUL 1
4N
u1
u2
T
A/NUL 1
u1
u2
ˇ
ˇ
ˇ
ˇ
u1Du2D0
D 1
2N 
 @
@u1
4
/NUL 1
2N
u1
u2
TVtt Vts
Vts Vss
/NUL 1u1
u2
2
D 1
8N.VttVss /NULV2
ts/2
 @
@u1
4
.Vssu2
1 /NUL2Vtsu1u2 CVttu2
2/2
D 1
8N.VttVss /NULV2
ts/2 4Š V2
ss
D 4Š
8N.2
p
/NUL1/2.2y0 C1/2
 2y0
1 /NULy0
2
CO.„/;
by using Lemma /five.prop./three.propand formulas in the proof of Lemma /five.prop./three.prop. Similarly, the
contribution from Ls4 is calculated as
1
8N.VttVss /NULV2
ts/2
 @
@u2
4
.Vssu2
1 /NUL2Vtsu1u2 CVttu2
2/2
D 1
8N.VttVss /NULV2
ts/2 4Š V2
tt
D 4Š
8N.2
p
/NUL1/2.2y0 C1/2
 x0
1 /NULx0
2
CO.„/:
Hence, the contribution from ( /five.prop/six.prop) is equal to
2
p
/NUL1
8N.2y0 C1/2

.x2
0 Cx0/y3
0
 2y0
1 /NULy0
2
/NUL2.y0 C1/
 x0
1 /NULx0
2
DC4„;
where we put
C4 D 1
8.2y0 C1/2

.x2
0 Cx0/y3
0
 2y0
1 /NULy0
2
/NUL2.y0 C1/
 x0
1 /NULx0
2
D 1
92.2y2
0 C15y0/:
We calculate the contribution from the degree /three.prop part of the expansion (/five.prop/one.prop), as
follows. As in (/five.prop/three.prop), the degree /three.prop part of this expansion is given by
.2
p
/NUL1/2.y0 /NUL1/
 Lt3
6 y0 C Ls3
6 2

CO.„/;
On the asymptotic expansion of the Kashaev invariant of the 52 knot 713
and, hence, the corresponding degree /six.prop part is given by
1
2.2
p
/NUL1/4.y0 /NUL1/2
 Lt3
6 y0 C Ls3
6 2
2
CO.„/
D 1
2.2
p
/NUL1/4.y0 /NUL1/2
 Lt6
62 y2
0 C Ls6
62 4 C
Lt3 Ls3
62 4y0

CO.„/:
(57)
The contribution from Lt6 is calculated as
N2 
 @
@u1
6
exp

/NUL 1
4N
u1
u2
T
A/NUL 1
u1
u2
ˇ
ˇ
ˇ
ˇ
u1Du2D0
D 1
6N2 
 @
@u1
6
/NUL 1
2N
u1
u2
TVtt Vts
Vts Vss
/NUL 1u1
u2
3
D /NUL1
48N.VttVss /NULV2
ts/3
 @
@u1
6
.Vssu2
1 /NUL2Vtsu1u2 CVttu2
2/3
D /NUL1
48N.VttVss /NULV2
ts/3 6Š V3
ss
D 6Š
48N.2
p
/NUL1/3.2y0 C1/3
 2y0
1 /NULy0
3
CO.„/;
by using Lemma /five.prop./three.propand formulas in the proof of Lemma /five.prop./three.prop. Similarly, the
contribution from Ls6 is calculated as
/NUL1
48N.VttVss /NULV2
ts/3
 @
@u2
6
.Vssu2
1 /NUL2Vtsu1u2 CVttu2
2/3
D /NUL1
48N.VttVss /NULV2
ts/3 6Š V3
tt
D 6Š
48N.2
p
/NUL1/3.2y0 C1/3
 x0
1 /NULx0
3
CO.„/:
Similarly, the contribution from Lt3 Ls3 is calculated as
/NUL1
48N.VttVss /NULV2
ts/3
 @
@u1
3 @
@u2
3
.Vssu2
1 /NUL2Vtsu1u2 CVttu2
2/3
D /NUL1
48N.VttVss /NULV2
ts/3 6Š 
2
5./NULVts/3 C3
5VttVss./NULVts/

CO.„/
D 6Š
48N.2
p
/NUL1/3.2y0 C1/3
2
5 C3
5
x0
1 /NULx0
2y0
1 /NULy0

;
714 T. Ohtsuki
by using Lemma /five.prop./three.propand formulas in the proof of Lemma /five.prop./three.prop. Hence, the contri-
bution from (/five.prop/seven.prop) is equal to
5 2
p
/NUL1.y0 /NUL1/2
24N.2y0 C1/3

y2
0
 2y0
1/NULy0
3
C4
 x0
1/NULx0
3
C4y0
2
5 C3
5
x0
1/NULx0
2y0
1/NULy0

DC5„
where we put
C5 D 5.y0 /NUL1/2
24.2y0 C1/3

y2
0
 2y0
1 /NULy0
3
C4
 x0
1 /NULx0
3
C4y0
2
5 C3
5
x0
1 /NULx0
2y0
1 /NULy0

D /NUL 1
3174.197y2
0 C127y0 C227/:
Therefore, we obtain the required formula of the lemma. 
/five.prop./three.prop. Verifying the assumption of the saddle point method.In this section,
in Lemma /five.prop./seven.prop, we verify the assumption of the saddle point method (Propos i-
tion /three.prop./five.prop, see also Remark /three.prop./six.propand Appendix B) when we apply Proposition /three.prop./five.prop
and Remark /three.prop./six.propto (/four.prop/six.prop). The arguments of this section are due to Y okota [ /four.prop/four.prop].
Let V.t;s/ and yV.t;s/ be as in Section /two.prop./two.prop. As shown in Appendix B,
V.t;s/ uniformly converges to yV.t;s/ on 0 as N ! 1 . Hence, as men-
tioned in Remarks /three.prop./three.propand /three.prop./six.propand Appendix B, the saddle point method of the
problem can be reduced to the saddle point method of an integr al of the formR

.t;s/e N yV.t;s/dtds . Therefore, we verify the assumption of the saddle point
method for yV.t;s/ . We recall that the diﬀerentials of yV.t;s/ are given in ( /four.prop/seven.prop).
In order to show Lemma /five.prop./seven.propbelow, we calculate the behavior of the function
ft;s.ı1;ı2/ D Re yV.t Cı1
p
/NUL1;s Cı2
p
/NUL1/ /NUL&R:
The diﬀerentials of this function are given by
@
@ı1
ft;s.ı1;ı2/ D Re.
p
/NUL1@
@t
yV.t Cı1
p
/NUL1;s Cı2
p
/NUL1//
D /NUL Im

/NUL log

1 /NUL 1
x

/NUL2
p
/NUL1

t Cs /NUL 1
2

D Arg

1 /NUL 1
x

C2

t Cs /NUL 1
2

;
(58)
@
@ı2
ft;s.ı1;ı2/ D Re
p
/NUL1@
@s
yV.t Cı1
p
/NUL1;s Cı2
p
/NUL1/

D /NUL Im

/NUL2 log

1 /NUL 1
y

/NUL2
p
/NUL1.t C2s /NUL1/

D2

Arg

1 /NUL 1
y

C2
1
2t Cs /NUL 1
2

;
(59)
wherex De2
p
/NUL 1.tCı1
p
/NUL 1/ andy De2
p
/NUL 1.sCı2
p
/NUL 1/.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 715
Lemma /five.prop./five.prop(Y okota [/four.prop/four.prop]). Fixing.t;s/ 20 andı2 2 R, we regardft;s.X;ı2/
as a function of X 2 R.
(1) Ift Cs  1
2 , thenft;s.X;ı2/ is monotonically increasing forX 2 R.
(2) Ift Cs <1
2 , then ft;s.X;ı2/ has a unique minimal point at X D g1.t;s/ ,
where
g1.t;s/ D 1
2 log sin2.t Cs/
sin2s ;
i.e.,ft;s.X;ı2/ is monotonically decreasing for X < g1.t;s/ , and is mono-
tonically increasing forX >g1.t;s/ .
Proof. We put x D e2
p
/NUL 1.tCX
p
/NUL 1/. Then, 1=x D e2Xe/NUL 2
p
/NUL 1t . We put
 D Arg.1 /NUL 1
x/ in this proof. Since t <1
2 , is in the range
0< <2
1
2 /NULt

:
Whent Cs  1
2 , we show the lemma, as follows. By ( /five.prop/eight.prop),
@
@Xft;s.X;ı2/ D C2

t Cs /NUL 1
2

>0:
Therefore,ft;s.X;ı2/ is monotonically increasing, and (/one.prop) holds.
Whent Cs< 1
2 , we show the lemma, as follows. In this case, by ( /five.prop/eight.prop),
@
@Xft;s.X;ı2/
8
ˆ
ˆ
ˆ
ˆ
ˆ
ˆ
<
ˆ
ˆ
ˆ
ˆ
ˆ
ˆ
:
>0 if >2
1
2 /NULt /NULs

;
D0 if D2
1
2 /NULt /NULs

;
<0 if <2
1
2 /NULt /NULs

:
Further, andX are related as shown in the following picture.
10 1
2t 
e2X
1=x
716 T. Ohtsuki
Hence,X is monotonically increasing as a function of , and they satisfy
e2X
sin D 1
sin. /NUL2t /NUL/:
This is rewritten
X D 1
2 log sin
sin. /NUL2t /NUL/:
Therefore,
@
@Xft;s.X;ı2/
8
ˆ
ˆ
ˆ
<
ˆ
ˆ
ˆ
:
>0 ifX >g1.t;s/;
D0 ifX Dg1.t;s/;
<0 ifX <g1.t;s/;
where we put
g1.t;s/ D 1
2 log sin2.1
2 /NULt /NULs/
sin2s D 1
2 log sin2.t Cs/
sin2s :
Hence, (/two.prop) holds. 
Lemma /five.prop./six.prop(Y okota [/four.prop/four.prop]). Fixing.t;s/ 20 andı1 2 R, we regardft;s.ı1;Y/
as a function of Y 2 R.
(1) Ift C2s 1, thenft;s.ı1;Y/ is monotonically increasing forY 2 R.
(2) Ift C2s < 1, then ft;s.ı1;Y/ has a unique minimal point at Y D g2.t;s/ ,
where
g2.t;s/ D 1
2 log sin.t C2s/
sint ;
i.e.,ft;s.ı1;Y/ is monotonically decreasing for Y < g2.t;s/ , and is mono-
tonically increasing forY >g2.t;s/ .
Proof. We put y D e2
p
/NUL 1.sCY
p
/NUL 1/. Then, 1=y D e2Ye/NUL 2
p
/NUL 1s. We put
 D Arg
/NUL
1 /NUL 1
y

in this proof. Since s< 1
2 , is in the range
0< <2
1
2 /NULs

:
Whent C2s 1, we show the lemma, as follows. By ( /five.prop/nine.prop),
@
@Yft;s.ı1;Y/ D2. C.t C2s /NUL1//>0:
Hence,ft;s.ı1;Y/ is monotonically increasing, and (/one.prop) holds.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 717
Whent C2s<1 , we show the lemma, as follows. In this case, by ( /five.prop/nine.prop),
@
@Yft;s.ı1;Y/
8
ˆ
ˆ
ˆ
ˆ
ˆ
ˆ
<
ˆ
ˆ
ˆ
ˆ
ˆ
ˆ
:
>0 if >2
1
2 /NUL 1
2t /NULs

;
D0 if D2
1
2 /NUL 1
2t /NULs

;
<0 if <2
1
2 /NUL 1
2t /NULs

:
Further, similarly as in the proof of Lemma /five.prop./five.prop, andY are related by
Y D 1
2 log sin
sin. /NUL2s /NUL/:
SinceY is monotonically increasing as a function of ,
@
@Yft;s.ı1;Y/
8
ˆ
ˆ
ˆ
<
ˆ
ˆ
ˆ
:
>0 ifY >g2.t;s/;
D0 ifY Dg2.t;s/;
<0 ifY <g2.t;s/;
where we put
g2.t;s/ D 1
2 log
sin2
1
2 /NUL 1
2t /NULs

sin

 /NUL2s /NUL2
1
2 /NUL 1
2t /NULs
 D 1
2 log sin.t C2s/
sint :
Hence, we obtain the lemma. 
Lemma /five.prop./seven.prop(Y okota [/four.prop/four.prop]). When we apply Proposition /three.prop./five.prop.saddle point method/
to./four.prop/six.prop/, the assumption of Proposition /three.prop./five.propholds.
Proof. We show that there exists a homotopy 0
ı (0 ı 1) between0
0 D0
and0
1 such that
.tc;sc/ 20
1; (60)
0
1 /NUL ¹.tc;sc/º  ¹.t;s/ 2 C2 j Re yV.t;s/<& Rº; (61)
@0
ı  ¹.t;s/ 2 C2 j Re yV.t;s/<& Rº: (62)
718 T. Ohtsuki
For a suﬃciently large R>0 , we put
Og1.t;s/ D
8
<
:
max¹/NULR;g1.t;s/ º ift Cs< 1
2;
/NULR ift Cs  1
2;
Og2.t;s/ D
8
<
:
max¹/NULR;g2.t;s/ º ift C2s<1;
/NULR ift C2s 1:
We note that, since g1.t;s/ ! /NUL1 ast Cs ! 1
2 , Og1.t;s/ is continuous, and
similarly, sinceg2.t;s/ ! /NUL1 ast C2s !1, Og2.t;s/ is continuous. We put
0
ı D ¹.t Cı  Og1.t;s/
p
/NUL1;s Cı  Og2.t;s/
p
/NUL1/ 2 C2 j.t;s/ 20º:
We show (/six.prop/two.prop), as follows. From the de/f_inition of0,
@0  ¹.t;s/ 2 C2 j Re yV.t;s/<& Rº:
Further, by Lemmas /five.prop./five.propand /five.prop./six.prop,
Re yV.t Cı  Og1.t;s/
p
/NUL1;s Cı  Og2.t;s/
p
/NUL1/  yV.t;s/
for anyı 2Œ0;1 and any.t;s/ 20. Hence, ( /six.prop/two.prop) holds.
We show (/six.prop/zero.prop) and (/six.prop/one.prop), as follows. Consider the functions
F.t;s;X;Y/ D Re yV.t CX
p
/NUL1;s CY
p
/NUL1/;
h.t;s/ DF.t;s; Og1.t;s/; Og2.t;s//:
Whent C2s  1, /NULh.t;s/ is suﬃciently large (because we let R be suﬃciently
large), and (/six.prop/one.prop) holds in this case. Whent C2s<1 , it is shown from the de/f_initions
ofg1.t;s/ andg2.t;s/ that @F
@X D0 atX Dg1.t;s/ and @F
@Y D0 atY Dg2.t;s/ .
Hence, Im @ yV
@t D Im @ yV
@s D 0 at .t Cg1.t;s/
p
/NUL1;s Cg2.t;s/
p
/NUL1/. Further,
@h
@t D Re@ yV
@t and @h
@s D Re@ yV
@s at .t Cg1.t;s/
p
/NUL1;s Cg2.t;s/
p
/NUL1/. There-
fore, when .t;s/ is a critial point of h.t;s/ ,.t Cg1.t;s/
p
/NUL1;s Cg2.t;s/
p
/NUL1/
is a critical point of yV . It follows that h.t;s/ has a unique maximal point at
.t;s/ D.Retc; Resc/. Therefore, (/six.prop/zero.prop) and ( /six.prop/one.prop) hold. 
/five.prop./four.prop. Verifying the assumption of the Poisson summation formula. In this
section, in Lemma /five.prop./eight.prop, we verify the assumption of the Poisson summation
formula (Proposition /four.prop./six.prop, see also Remark /four.prop./eight.propand Appendix B) when we apply
Proposition /four.prop./six.propand Remark /four.prop./eight.propto (/one.prop/four.prop). As in the previous section, we consider
yV.t;s/ instead ofV.t;s/ in this section.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 719
We calculate a critical point .tr;sr/ 2 0 of Re yV.t;s/ , as follows. Putting
x De2
p
/NUL 1t andy De2
p
/NUL 1s, we have
@
@t Re yV.t;s/ D Re

/NUL log

1 /NUL 1
x

;
@
@s Re yV.t;s/ D Re

/NUL2 log

1 /NUL 1
y

;
sincet;s 2 R. Hence, putting xr De2
p
/NUL 1tr andyr De2
p
/NUL 1sr ,
jxr /NUL1j D jyr /NUL1j D1;
noting that jxr j D jyr j D1. Therefore,xr Dyr De2
p
/NUL 1=3, and ReV.t;s/ has a
unique maximal point /NUL 1
6; 1
6
 on0. Its maximal value is given by
Re yV
1
6;1
6

/NUL&R D Re 1
2
p
/NUL1
.Li2.e
p
/NUL 1=3/ /NUL2 Li2.e/NUL 
p
/NUL 1=3// /NUL&R
D0:03448931080::::
Hence,
Re yV.t;s/ /NUL&R 0:03448931080:::; (63)
for any.t;s/ 20.
Lemma /five.prop./eight.prop.When we apply Proposition /four.prop./six.propto./one.prop/four.prop/, the assumptions of Proposi-
tion /four.prop./six.prophold.
Proof. We verify the assumptions (/four.prop/one.prop) and (/four.prop/two.prop) fori D1 in Lemmas /five.prop./nine.propand /five.prop./one.prop/zero.prop
below, and verify the assumptions for i D2 in Lemmas /five.prop./one.prop/one.propand /five.prop./one.prop/two.propbelow. The
other assumptions of Proposition /four.prop./six.propcan be veri/f_ied easily. 
Lemma /five.prop./nine.prop.The assumption./four.prop/one.prop/ holds fori D1.
Proof. As for the assumption ( /four.prop/one.prop) fori D1, we show that @0 is null-homotopic
in
¹.t Cı
p
/NUL1;s/ 2 C2 j.t;s/ 20; ı0; ReV.t Cı
p
/NUL1;s/<& R C2ı º:
To show it, we show that the following disk bounds @0 in the above domain:
¹.t Cı0
p
/NUL1;s/ 2 C2 j.t;s/ 20º
[ ¹.t Cı
p
/NUL1;s/ 2 C2 j.t;s/ 2@0; ı2Œ0;ı0º:
720 T. Ohtsuki
We put
Ft;s.ı/ D ReV.t Cı
p
/NUL1;s/ /NUL&R /NUL2ı
in this proof. Then, it is suﬃcient to show that
Ft;s.ı0/<0 for any.t;s/ 20; (64)
and
Ft;s.ı/<0 for any.t;s/ 2@0 andı 2Œ0;ı0; (65)
for someı0>0 .
To show these, we estimate the diﬀerential of Ft;s.ı/, as follows. The diﬀer-
ential ofFt;s.ı/ is given by
d
dıFt;s.ı/ D Re
p
/NUL1@
@t
yV.t Cı
p
/NUL1;s/

/NUL2
D /NUL Im

/NUL log

1 /NUL 1
x

/NUL2
p
/NUL1

t Cs /NUL 1
2

/NUL2
D Arg

1 /NUL 1
x

C2

t Cs /NUL 3
2

;
where we put x D e2
p
/NUL 1.t Cı
p
/NUL 1/. Since 0:04  t  0:4, it is shown that
Arg.1 /NUL 1
x/ is in the range
0< Arg

1 /NUL 1
x

<:
Therefore, sincet Cs 0:6,
d
dıFt;s.ı/<2
1
2 C0:6 /NUL 3
2

D /NUL2 0:4:
We show (/six.prop/four.prop), as follows. We have
Ft;s.ı0/ DFt;s.0/ C
Z ı0
0
d
dıFt;s.ı/dı<F t;s.0/ /NUL2 0:4 ı0:
Further, by (/six.prop/three.prop),
Ft;s.0/ D Re yV.t;s/ /NUL&R 0:03448931080::::
Hence, (/six.prop/four.prop) is satis/f_ied for a suﬃciently large ı0.
We show (/six.prop/five.prop), as follows. From the de/f_inition of0, we have thatFt;s.0/<0
for any.t;s/ 2@0. Since d
dıFt;s.ı/<0 as shown above, it is shown similarly as
above thatFt;s.ı/<0 for anyı 0. Hence, ( /six.prop/five.prop) is satis/f_ied. 
On the asymptotic expansion of the Kashaev invariant of the 52 knot 721
Lemma /five.prop./one.prop/zero.prop.The assumption./four.prop/two.prop/ holds fori D1.
Proof. We put
Ft;s.ı/ D ReV.t /NULı
p
/NUL1;s/ /NUL&R /NUL2ı
in this proof. Similarly as the proof of Lemma /five.prop./nine.prop, it is suﬃcient to show that
there exists">0 such that
d
dıFt;s.ı/< /NUL"; (66)
for any.t;s/ 20.
We calculate this as
d
dıFt;s.ı/ D Re

/NUL
p
/NUL1@
@t
yV.t /NULı
p
/NUL1;s/

/NUL2
D Im

/NUL log

1 /NUL 1
x

/NUL2
p
/NUL1

t Cs /NUL 1
2

/NUL2
D /NUL Arg

1 /NUL 1
x

/NUL2

t Cs C1
2

;
where we put x D e2
p
/NUL 1.t /NUL ı
p
/NUL 1/. Since 0:04  t  0:4, it is shown that
Arg.1 /NUL 1
x/ is in the range
0< Arg

1 /NUL 1
x

<:
Therefore, sincet Cs 0:09,
d
dıFt;s.ı/< /NUL2

0:09 C1
2

D /NUL2 0:59;
and (/six.prop/six.prop) is satis/f_ied. 
Lemma /five.prop./one.prop/one.prop.The assumption./four.prop/one.prop/ holds fori D2.
Proof. We put
Ft;s.ı/ D ReV.t;s Cı
p
/NUL1/ /NUL&R /NUL2ı
in this proof. Similarly as the proof of Lemma /five.prop./nine.prop, it is suﬃcient to show that
there exists">0 such that
d
dıFt;s.ı/< /NUL"; (67)
for any.t;s/ 20.
722 T. Ohtsuki
To show these, we calculate the diﬀerential of Ft;s.ı/ as
d
dıFt;s.ı/ D Re
p
/NUL1@
@sV.t;s Cı
p
/NUL1/

/NUL2
D /NUL Im

/NUL2 log

1 /NUL 1
y

/NUL2
p
/NUL1.t C2s /NUL1/

/NUL2
D2 Arg

1 /NUL 1
y

C2.t C2s /NUL2/;
where we put y D e2
p
/NUL 1.sCı
p
/NUL 1/. Since 0:05  s  0:4, it is shown that
Arg
/NUL
1 /NUL 1
y

is in the range
0< Arg

1 /NUL 1
y

<2
1
2 /NULs

:
Therefore, sincet 0:4,
d
dıFt;s.ı/<2 2
1
2 /NULs

C2.t C2s /NUL2/ D2.t /NUL1/  /NUL2 0:6;
and (/six.prop/seven.prop) is satis/f_ied. 
Lemma /five.prop./one.prop/two.prop.The assumption /parenleft.alt/four.prop/two.prop/parenright.alt holds fori D2.
Proof. We put
Ft;s.ı/ D ReV.t;s /NULı
p
/NUL1/ /NUL&R /NUL2ı
in this proof. Similarly as the proof of Lemma /five.prop./nine.prop, it is suﬃcient to show that
there exists">0 such that
d
dıFt;s.ı/< /NUL"; (68)
for any.t;s/ 20.
We calculate this as
d
dıFt;s.ı/ D Re

/NUL
p
/NUL1@
@sV.t;s /NULı
p
/NUL1/

/NUL2
D Im

/NUL2 log

1 /NUL 1
y

/NUL2
p
/NUL1.t C2s /NUL1/

/NUL2
D /NUL2 Arg

1 /NUL 1
y

/NUL2.t C2s/;
where we put y D e2
p
/NUL 1.s/NUL ı
p
/NUL 1/. Since 0:05  s  0:4, it is shown that
Arg.1 /NUL 1
y/ is in the range
0< Arg

1 /NUL 1
y

<:
On the asymptotic expansion of the Kashaev invariant of the 52 knot 723
Therefore, sincet Cs 0:09 ands 0:05,
d
dıFt;s.ı/< /NUL2.0:09 C0:05/ D /NUL2 0:14;
and (/six.prop/eight.prop) is satis/f_ied. 
Appendixes
A. Properties of '.t/
In this appendix, we review some basic properties of '.t/ .
We put „ D 2
p
/NUL1=N , and put
ˆd.z/ D Li2.z/ C
X
1kd
„2kc2k 

z d
dz
2k/NUL 2 z
1 /NULz;
where we de/f_inec2k by
y=2
sinh.y=2/ D
X
k0
c2ky2k:
Proposition A./one.prop.We /f_ix any suﬃciently small ı > 0and any M > 0. Let d be
any non-negative integer. Then, in the domain
¹t 2 C jı  Ret 1 /NULı; j Imt j M º; (69)
'.t/ and'.k/.t/ are presented by
'.t/ D N
2
p
/NUL1
ˆd.e2
p
/NUL 1t/ CO
 1
N2d C1

; (70)
'.k/.t/ D N
2
p
/NUL1
d
dt
k
ˆd.e2
p
/NUL 1t/ CO
 1
N2d C1

; (71)
for eachk > 0, where O.1=N2d C1/ means the error term whose absolute value
is bounded byC=N2d C1 for someC >0, which is independent of t /parenleft.altbut possibly
dependent onı/parenright.alt.
In particular, 1
N'.t/ uniformly converges to 1
2
p
/NUL 1 Li2.e2
p
/NUL 1t/ in the do-
main ./six.prop/nine.prop/, and 1
N'0.t/ uniformly converges to /NUL log.1 /NUL e2
p
/NUL 1t/ in the do-
main./six.prop/nine.prop/.
724 T. Ohtsuki
Proof. We show (/seven.prop/zero.prop). We have
'.t/ D
Z 1
/NUL1
Ne.2t /NUL 1/x
4x2 sinhx  x=N
sinh.x=N/dx D
Z 1
/NUL1
Ne.2t /NUL 1/x
4x2 sinhx
X
k0
c2k
2x
N
2k
dx:
(72)
We put the “k D0” part of ( /seven.prop/two.prop) to be
f.t/ D
Z 1
/NUL1
Ne.2t /NUL 1/x
4x2 sinhxdx:
To calculatef.t/ , we consider the contour
h
/NUL

m C1
2

; /NUL1
i
[ ¹z 2 C j jzj D 1; Imz 0º
[
h
1;

m C1
2


i
[
°
z 2 C
ˇ
ˇ
ˇ jzj D m C1
2; Imz 0
±
:
Then, the integrand has poles at n
p
/NUL1 (n D1;2;:::;m ) in the region bounded
by the contour. Hence,
f.t/ D lim
m!1
mX
nD1
2
p
/NUL1 Res
xDn
p
/NUL 1
Ne.2t /NUL 1/x
4x2 sinhx
D2
p
/NUL1
1X
nD1
/NULN
42
.e2
p
/NUL 1t/n
n2
D N
2
p
/NUL1
Li2.e2
p
/NUL 1t/:
Further, for generalk>0 , the “k” part of ( /seven.prop/two.prop) is calculated as
c2k
N2kf.2k/.t/ D N
2
p
/NUL1
 c2k
N2k
d
dt
2k
Li2.e2
p
/NUL 1t/
D N
2
p
/NUL1
 „2kc2k

z d
dz
2k/NUL 2 z
1 /NULz:
Therefore, we can put
'.t/ D N
2
p
/NUL1
ˆd.e2
p
/NUL 1t/ CRd;
whereRd is the error term. We estimate it, as follows. Since j.y=2/= sinh.y=2/j
is bounded fory 2 R, there existsM0>0 such that
ˇ
ˇ
ˇ
ˇ
1
y2d C2
 y=2
sinhy=2 /NUL
dX
kD0
c2ky2k
ˇ
ˇ
ˇ
ˇ M0
On the asymptotic expansion of the Kashaev invariant of the 52 knot 725
for anyy 2 R. Hence, putting y D2x=N ,
jRd j D
ˇ
ˇ
ˇ
ˇ'.t/ /NUL N
2
p
/NUL1
ˆd.e2
p
/NUL 1t/
ˇ
ˇ
ˇ
ˇ
D
ˇ
ˇ
ˇ
ˇ
Z 1
/NUL1
Ne.2t /NUL 1/x
4x2 sinhx
 x=N
sinh.x=N/ /NUL
dX
kD0
c2k
2x
N
2k
dx
ˇ
ˇ
ˇ
ˇ

Z 1
/NUL1
ˇ
ˇ
ˇ
ˇ
Ne.2t /NUL 1/x
4x2 sinhx
ˇ
ˇ
ˇ
ˇ M0
ˇ
ˇ
ˇ
ˇ
2x
N
ˇ
ˇ
ˇ
ˇ
2d C2
dx
D 22dM0
N2d C1
 Z 1
1
e.2 Ret/NUL 1/x
j sinhxj x2ddx
C
Z /NUL 1
/NUL1
e.2 Ret/NUL 1/x
j sinhxj x2ddx
C
Z
jzjD1
Imz0
eRe..2t /NUL 1/z/
j sinhzj jdzj
!
:
(73)
Forx  1, the integrand of ( /seven.prop/three.prop) is bounded by M1e/NUL 2ıxx2d for some M1 > 0.
Forx  /NUL1, the integrand of ( /seven.prop/three.prop) is bounded by M2e2ıxx2d for some M2 > 0.
For jzj D 1, the integrand of ( /seven.prop/three.prop) is bounded by a constant. Hence, the values
of the integrals of ( /seven.prop/three.prop) is bounded by a constant. Therefore, jRd j is bounded by
C=N2d C1 for someC >0, which is independent of t . Hence, we obtain ( /seven.prop/zero.prop).
We obtain (/seven.prop/one.prop) by similar arguments for '.k/.t/ . 
Lemma A./two.prop.For anyt 2 C with0< Ret <1,
'.t/ C'.1 /NULt/ D2
p
/NUL1

/NUL N
2

t2 /NULt C1
6

C 1
24N

:
Proof. By de/f_inition,
'.t/ C'.1 /NULt/ D
Z

e.2t /NUL 1/x Ce.1/NUL 2t/x
4x sinhx sinh.x=N/dx:
Since this integrand is an odd function, if the contour was R, the integral would
vanish. In this case, since the contour 
 avoids the pole atx D0, the contribution
from the residue at this pole survives. By expanding the nume rator and the
denominator of the integrand as power series of x concretely, we can calculate
this residue, and obtain the required formula. 
726 T. Ohtsuki
Lemma A./three.prop(Kashaev). We have
'
 1
2N

D N
2
p
/NUL1
2
6 C1
2 logN C
p
/NUL1
4 /NUL 
p
/NUL1
12N
and
'

1 /NUL 1
2N

D N
2
p
/NUL1
2
6 /NUL 1
2 logN C
p
/NUL1
4 /NUL 
p
/NUL1
12N :
Proof. It is suﬃcient to show that
'
 1
2N

C'

1 /NUL 1
2N

D2
p
/NUL1

/NUL N
12 C1
4 /NUL 1
12N

; (74)
and
'
 1
2N

/NUL'

1 /NUL 1
2N

D logN: (75)
We obtain (/seven.prop/four.prop) from Lemma A./two.propby puttingt D1=2N .
We show (/seven.prop/five.prop), as follows. By ( /three.prop) and (/eight.prop),
exp

'
 1
2N

/NUL'

1 /NUL 1
2N

DN: (76)
Further, from the de/f_inition of'.t/ ,
'
 1
2N

/NUL'

1 /NUL 1
2N

D
Z

e.1/NUL 1=N/x /NULe.1=N /NUL 1/x
4x sinhx sinh.x=N/ dx:
By a similar argument as in the proof of Lemma A./two.prop, we can see that the residue
of this integrand at 0 vanishes. Hence, the value of this integral is real, and we
obtain (/seven.prop/five.prop) from (/seven.prop/six.prop). 
B. Convergence of V.t; s/ to yV .t; s/
When we apply the saddle point method and the Poisson summati on formula to
V.t;s/ , it is necessary to note how V.t;s/ converges to yV.t;s/ asN ! 1. In this
appendix, we verify that this convergence is suitable in tho se applications.
We recall that in Section /two.prop./two.propwe putV.t;s/ and yV.t;s/ by
V.t;s/ D 1
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
4N2
On the asymptotic expansion of the Kashaev invariant of the 52 knot 727
and
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
Lemma B./one.prop.Letm be any non-negative integer. Then, in the domain 00 of./one.prop/two.prop/,
V.t;s/ is presented by the form
V.t;s/ D yV.t;s/ CV1.t;s/ 1
N CV2.t;s/ 1
N2 C   CVm.t;s/ 1
Nm CRm.t;s/ 1
NmC1
whereVi.t;s/ ’s are holomorphic functions independent of N , and jRm.t;s/ j is
bounded by a constant which is independent of N .
In particular,V.t;s/ uniformly converges to yV.t;s/ in the domain00.
Proof. We obtain the required presentation by applying Proposition A./one.proptoV.t;s/ .
In particular, by Proposition A./one.prop, 1
N'.t/ uniformly converges to the value
1
2
p
/NUL 1 Li2.e2
p
/NUL 1t/ as N ! 1 in the domain 00. Hence, we obtain the
lemma. 
Lemma B./two.prop.Leti andj be any non-negative integers. Then, in the domain 00,ˇ
ˇ @i Cj
@it@ jsV.t;s/
ˇ
ˇ is bounded by a constant which is independent of N .
Proof. By Proposition
A./one.prop,
ˇ
ˇ @i Cj
@it@ jsV.t;s/
ˇ
ˇ uniformly converges to
ˇ
ˇ @i Cj
@it@ js
yV.t;s/
ˇ
ˇ
asN ! 1 in the domain00. Since00 is compact,
ˇ
ˇ @i Cj
@it@ js
yV.t;s/
ˇ
ˇ is bounded in
00. Hence, we obtain the lemma. 
When we apply the saddle point method, we need to show that V.t;s/ satis/f_ies
the condition of Remark
/three.prop./six.prop, noting that yV.t;s/ satis/f_ies the assumption of the
saddle point method as shown in Section /five.prop./three.prop. In fact, we can show the condition
of Remark /three.prop./six.propforV.t;s/ by Lemma B./one.prop.
When we apply the Poisson summation formula, we need to show t hatV.t;s/
satis/f_ies the condition of Remark /four.prop./eight.prop, noting that yV.t;s/ satis/f_ies the assumption
of the Poisson summation formula as shown in Section /five.prop./four.prop. In fact, we can show
the condition of Remark /four.prop./eight.propforV.t;s/ by Lemmas B./one.propand B./two.prop.
728 T. Ohtsuki
C. Critical points of V.t; s/ and yV .t; s/
In this appendix, we show a proof of Lemma /five.prop./one.prop.
We put „ D 2
p
/NUL1=N , and use the notation in Section /five.prop./two.prop. By Proposi-
tion A./one.prop, we can put
1
N'0.1 /NULt/ D /NUL log.1 /NULe/NUL 2
p
/NUL 1t/ Cr.t; „/„2
for some smooth function r.t; „/ oft and „. Then, from the de/f_inition of V.t;s/ ,
we have
@
@tV.t;s/ D /NUL log

1 /NUL 1
x

/NUL2
p
/NUL1

t Cs /NUL 1
2 /NUL 1
2N

Cr.t; „/„2;
@
@sV.t;s/ D /NUL2 log

1 /NUL 1
y

/NUL2
p
/NUL1

t C2s /NUL1 /NUL 1
2N

C2r.s; „/„2:
Hence, a critical point of V.t;s/ is a solution of
8
ˆ
ˆ
ˆ
<
ˆ
ˆ
ˆ
:

1 /NUL 1
x

./NULq/NUL 1=2xy/ Der.t; „/„2
;

1 /NUL 1
y
2
q/NUL 1=2xy2 De2r.s; „/„2
:
This is rewritten as 8
<
:
.1 /NULx/y Dq1=2er.t; „/„2
;
x.y /NUL1/2 Dq1=2e2r.s; „/„2
:
Further, by putting
F.t;s; „/ D.1 /NULx/y /NULq1=2er.t; „/„2
;
G.t;s; „/ Dx.y /NUL1/2 /NULq1=2e2r.s; „/„2
;
the above system of equations is rewritten as
´
F.t;s; „/ D0;
G.t;s; „/ D0:
(77)
We note that.t0;s0;0/ is a solution of (
/seven.prop/seven.prop).
On the asymptotic expansion of the Kashaev invariant of the 52 knot 729
Proof of Lemma /five.prop./one.prop. It is suﬃcient to show that there exists a smooth solution
.f. „/;g. „/; „/ of (/seven.prop/seven.prop) in a suﬃciently small neighborhood of .t0;s0;0/ . Hence,
by the implicit function theorem, it is suﬃcient to show
det
0
B
B
@
@
@tF.t0;s0;0/ @
@sF.t0;s0;0/
@
@tG.t0;s0;0/ @
@sG.t0;s0;0/
1
C
C
A ¤0: (78)
Sincex De2
p
/NUL 1t ,
d
dt D2
p
/NUL1x d
dx:
Similarly,
d
ds D2
p
/NUL1y d
dy:
Therefore, from the de/f_initions ofF.t;s; „/ andG.t;s; „/, we have
1
2
p
/NUL1
@
@tF.t0;s0;0/ Dx @
@x..1 /NULx/y/ j„D0 D /NULx0y0;
1
2
p
/NUL1
@
@sF.t0;s0;0/ Dy @
@y..1 /NULx/y/ j„D0 D.1 /NULx0/y0;
1
2
p
/NUL1
@
@tG.t0;s0;0/ Dx @
@x.x.y /NUL1/2/j„D0 Dx0.y0 /NUL1/2;
1
2
p
/NUL1
@
@sG.t0;s0;0/ Dy @
@y.x.y /NUL1/2/j„D0 D2x0y0.y0 /NUL1/:
Hence, the determinant of ( /seven.prop/eight.prop) is calculated as
/NUL42  det
 /NULx0y0 .1 /NULx0/y0
x0.y0 /NUL1/2 2x0y0.y0 /NUL1/

D42 x0y0.y0 /NUL1/.x0y0 Cx0 Cy0 /NUL1/
D42 .2y0 C1/.y0 /NUL1/3=y0 D42 .2y0 C1/
¤0;
sincex0 D1 /NUL1=y0 and.y0 /NUL1/3 Dy0. Therefore, we obtain ( /seven.prop/eight.prop), completing
the proof of the lemma. 
730 T. Ohtsuki
D. Proof of Lemma /two.prop./one.prop
In this appendix, we give a proof of Lemma /two.prop./one.prop.
Proof of Lemma /two.prop./one.prop. We put
ƒ.t/ D Re
 1
2
p
/NUL1
Li2.e2
p
/NUL 1t/

fort 2 R. We note that this function has period 1, andƒ./NULt/ D /NULƒ.t/. Since
ƒ0.t/ D /NUL log.2 sint/
for0<t <1 , the behavior of ƒ.t/ is as follows.
t 0   
1
6   
1
2   
5
6    1
ƒ.t/ 0 ! ƒ.1
6/ ! 0 ! /NULƒ.1
6/ ! 0
Here,ƒ.1
6/ D0:161533::: . See Figure /six.propfor the graph of ƒ.t/.
0.60.2 0.4 0.8
−
−
−
0.05
0.05
0.10
0.10
0.15
0.15
1.0
Figure /six.prop. The graph ofƒ.t/ for0 t 1.
We consider the domain
¹.t;s/ 2 R2 j Re yV.t;s/ &Rº: (79)
Fort;s 2 R,
Re yV.t;s/ D /NULƒ./NULt/ /NUL2ƒ./NULs/ Dƒ.t/ C2ƒ.s/:
Since2ƒ
/NUL 1
6

/NUL&R D /NUL0:127043::: < 0, the values of ƒ.t/ andƒ.s/ must be
positive when.t;s/ is in the domain ( /seven.prop/nine.prop). Hence, the domain ( /seven.prop/nine.prop) is included in
the area ®
.t;s/ 2 R2ˇ
ˇ0 t 0:5; 0 s 0:5
¯
:
We assume that0 t 0:5 and0 s 0:5 in the following of this proof.
On the asymptotic expansion of the Kashaev invariant of the 52 knot 731
We consider the minimal value tmin oft such that.t;s/ is in the domain ( /seven.prop/nine.prop).
It satis/f_ies thatƒ.tmin/ C2ƒ
/NUL 1
6

D&R. Since
ƒ.0:04/ C2ƒ
1
6

/NUL&R D /NUL0:031768:::<0;
we have that0:04<t min. Hence, the domain ( /one.prop/one.prop) is included in the area 0:04 t
for some suﬃciently small ">0 . Further, in similar ways, we can show that the
domain (/one.prop/one.prop) is included in the area
¹.t;s/ 2 R2 j0:04 t 0:4;0:05 s 0:4º
for some suﬃciently small ">0 . We assume that .t;s/ is in the above area in the
following of this proof.
By expandingƒ.t/ att D0:3, we can show that
ƒ.t/ ƒ.0:3/ Cƒ0.0:3/.t /NUL0:3/:
If.t;s/ is in the domain ( /seven.prop/nine.prop),
&R ƒ.t/ C2ƒ.s/
ƒ.0:3/ Cƒ0.0:3/.t /NUL0:3/ C2.ƒ.0:3/ Cƒ0.0:3/.s /NUL0:3//:
Hence,
t C2s 
&R /NUL3ƒ.0:3/
ƒ0.0:3/ C0:9:
Further, sincet 0:4,
t Cs  1
2
&R /NUL3ƒ.0:3/
ƒ0.0:3/ C1:3

D0:571668:::<0:6:
Therefore, the domain ( /one.prop/one.prop) is included in 0 for some suﬃciently small " > 0,
as required. 
