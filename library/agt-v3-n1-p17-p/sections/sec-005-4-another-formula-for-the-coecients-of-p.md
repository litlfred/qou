---
doc_id: agt-v3-n1-p17-p
doc_title: "Published: 16 June 2003 Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum"
section_id: sec-005-4-another-formula-for-the-coecients-of-p
section_title: "Another formula for the coecients of !p"
section_number: 4
pages: 12-17
source_pdf: agt-v3-n1-p17-p.pdf
source_sha256: df196f0a732ad6b9
doc_brief: "Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum — We use skein theory to compute the coecients of certain power series considered by Habiro in his theory ofsl2 invariants of"
---
Following Habiro, we introduce the polynomials R0
n =(fng!)−1Rn and write
!p =
1X
n=0
c0
n;pR0
n ; (34)
where
c0
n;p =fng!cn;p :
The aim of this section is to show that c0
n;p is a Laurent polynomial, i.e. that
c0
n;p 2Z[A]. This fact was shown by Habiro [H3] using the quantum group
Uqsl2 . Observe that by (9) and (7), we already know this fact for p =1:
c0
n;1 =(−1)nan(n+3)=2 ;c 0
n;−1 =a−n(n+3)=2 :
(But Formula (33) tells us only that
c0
n;p = 1
(a−a−1)n
nX
k=0
(−1)kp
2k[2k +1 ] [n]!
[n +k +1 ] ![n−k]! ; (35)
from which it is not clear that c0
n;p2Z[A].)
To do so, we will replace Formula (32) in the previous section by Formula (42)
below. For this, we need the following two Lemmas.
Algebraic &GeometricTopology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 549
Lemma 4.1 We have
n
n =
nX
k=0
Cn;k kk
n−k
n−k
;
where
Cn;k =an(n−k)
n
k
 nY
j=n−k+1
(1−a−2j) : (36)
Here, as usual, n
k

= [n][n−1] [n−k +1 ]
[k]! :
Proof For 0pn, let us write, more generally,
n
p =
nX
k=0
Cn;p;k kk
n−k
p−k
:
First, we consider the case p = 1. By induction on n, it is easy to prove that
n
= an
n
+an−1(1−a−2n)
n−1
(recall a =A2 ). Using this, we now 
x n and do induction on p to obtain the
recursion formula
Cn;p+1;k =an−2kCn;p;k +an−2k+1(1−a−2(n−k+1))Cn;p;k−1 : (37)
Here we have used the following two facts which follow from the de
ning prop-
erties of the Jones-Wenzl idempotents.2
p +q p
q = p +q p
q (38)
p +q p
q = A−pq p +q p
q (39)
2Equation (39) is a special case of the half-twist coecient.
Algebraic &GeometricTopology, Volume 3 (2003)
550 Gregor Masbaum
Note that the coecientsCn;p;k behave like the binomial coecients
(p
k

in that
Cn;0;0 =1 ,a n d Cn;p;k =0f o r k< 0o r k>p . It follows that the recursion
formula (37) determines the Cn;p;k uniquely. One 
nds
Cn;p;k =ap(n−k)
p
k
 nY
j=n−k+1
(1−a−2j) :
Specializing to the case p =n, this proves the Lemma.
Remark 4.2 The coecient Cn;n was computed by a di
erent method in
[A, Prop. 4.4]. Knowing this coecient would be enough to obtain Habiro’s
formula (7) for ! (see Remark 4.4 below). Unfortunately, the method of [A]
does not give the coecients C
n;k for k6= n, which we will need to obtain a
formula for !p .
Lemma 4.3 We have
n
n kk
n−k
n−k
= 2
n−k
2n
kk
n−k
n−k
(40)
Proof The left hand side of (40) is equal to
kk
n−k
n−k
By an isotopy, this becomes
−2
k kk
n−k
n−k
Applying the coecients (n;n−k;k )−2 and (n;k;n−k)−2 , which are both
equal to kn−k−1
n (see also (39)), we see that this is equal to the right hand
side of (40).
Algebraic &GeometricTopology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 551
Let C(p)
n;k be the coecient de
ned by the expansion
n
n  =
nX
k=0
C(p)
n;k kk
n−k
n−k
; (41)
(where the diagram on the left hand side of (41) has 2p crossings). Putting the
two preceding Lemmas together, we may obtain a formula for this coecient.
In particular, it follows by induction on p that C(p)
n;k is a Laurent polynomial
divisible by Qn
j=n−k+1(1−a2j).
We are interested in the coecient C(p)
n;n ,s i n c ew eh a v e
2n
2n
n
n
 = C(p)
n;n
2n
2n
nn
= C(p)
n;n
2n
(42)
(where there are 2p crossings in the diagram on the left). Using (30) and (31)
from Section 3, it follows that
−2p
n cn;p(−1)n(fng!)2 =C(p)
n;n
and therefore
c0
n;p =fng!cn;p =(−1)n2p
n (fng!)−1C(p)
n;n : (43)
As already observed, C(p)
n;n is divisible by
nY
j=1
(1−a2j)= a−n(n+1)=2fng!
and hence c0
n;p is indeed a Laurent polynomial.
Remark 4.4 In the case p =1 ,w eh a v e
C(1)
n;n =Cn;n =a−n(n+1)=2fng! : (44)
Plugging this into (43), we get
c0
n;1 =(−1)nan2+2na−n(n+1)=2 =(−1)nan(n+3)=2 ;
giving another proof of Habiro’s formula (7) for cn;1 .
Algebraic &GeometricTopology, Volume 3 (2003)
552 Gregor Masbaum
Here is an explicit formula forC(p)
n;n which follows from (36) and (40). The sum is
over all multi-indices k =(k1;:::;k p) such that ki 0 for all i,a n dPki =n.
For convenience, put si =k1 +::: +ki and ri =n−si =ki+1 +::: +kp ,a n d
de
ne
’(k)=
p−1X
i=1
ri(ri−1 +ri +2 ): (45)
C(p)
n;n =
X
k
Cn;k1
2
n−k1
2n
Cn−k1;k2
2
n−k1−k2
2n
 Cn−sp−2;kp−1
2
n−sp−1
2n
Cn−sp−1;kp
=2−2p
n
X
k
 p−1Y
i=1
2
ri
! pY
i=1
Cri−1;ki
=2−2p
n
0
@
nY
j=1
(1−a−2j)
1
AX
k
 p−1Y
i=1
ari2+2ri
!p−1Y
i=1

ari−1ri
ri−1
ki

=2−2p
n a−n(n+1)=2fng!
X
k
a’(k)
n
k

w h e r ew eh a v ep u t ,a su s u a l ,
n
k

= [n]!
[k1]! [kp]! :
In view of (43), and using 2
n =an2+2n , we obtain the following 
nal result:
Theorem 4.5 (Habiro [H3]) Forp 1, the coecients c0
n;p of !p in (34) are
given by
c0
n;p =(−1)nan(n+3)=2 X
k=(k1;:::;kp)
ki0; Pki=n
a’(k)
n
k

: (46)
where ’(k) is de
ned in (45).
Remark 4.6 Since c0
n;−p =(−1)nc0n;p , this also determines the coecients of
negative powers of !.
Remark 4.7 In [H3], Habiro has obtained a similar formula using the quantum
group Uqsl2 .
Algebraic &GeometricTopology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 553
Example: Assume p = 2. We may write k =(k;n−k). Then
c0
n;2 =(−1)nan(n+3)=2
nX
k=0
a(n−k)(n+n−k+2)
n
k

=(−1)na(5n2+7n)=2
nX
k=0
ak2−2k−3nk
n
k

