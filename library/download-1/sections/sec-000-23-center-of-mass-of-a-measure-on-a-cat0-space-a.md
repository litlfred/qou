---
doc_id: download-1
doc_title: "Central and Lp-concentration of 1-Lipschitz maps into R-trees"
section_id: sec-000-23-center-of-mass-of-a-measure-on-a-cat0-space-a
section_title: "Center of mass of a measure on a CAT(0)-space and observ-"
section_number: 2.3
pages: 7-23
source_pdf: Download (1).pdf
source_sha256: bbb001c909958e8a
doc_brief: "Central and Lp-concentration of 1-Lipschitz maps into R-trees — In this paper, we study the Le ´vy-Milman concentration phenomenon of 1-Lipschitz maps from mm-spaces to R-trees."
---
able central radius.
2.3.1 Basics of the center of mass of a measure on a CAT(0)-space.
In this subsection, we review Sturm ’s works about measures on a CAT(0)-
space. We refer to [ 8]a n d[ 15] for details. A geodesic metric space X is called a
CAT(0)-space if we have
dX ðx; /C13ð1=2ÞÞ2 /C20 1
2 dX ðx; yÞ2 þ 1
2 dXðx; zÞ2 /C0 1
4 dXðy; zÞ2
for any x; y; z 2 X and any minimizing geodesic /C13 : ½0; 1/C138!X from y to z.F o r
example, Hadamard manifolds, Hilbert spaces, and R-trees are all CAT(0)-
spaces.
Let ðX; dX Þ b eam e t r i cs p a c e .W ed e n o t eb yBðXÞ the set of all ﬁnite Borel
measures /C23 on X with separable supports. We indicate by B1ðXÞ the set of all
Borel measures /C23 2 BðXÞ such that
R
X dX ðx; yÞd/C23ðyÞ < þ1 for some (hence all)
x 2 X.W ea l s oi n d i c a t eb yP1ðXÞ the set of all probability measures in B1ðXÞ.
For any /C23 2 B1ðXÞ and z 2 X, we consider the function hz;/C23 : X ! R deﬁned by
hz;/C23ðxÞ :¼
Z
X
fdX ðx; yÞ2 /C0 dX ðz; yÞ2gd/C23ðyÞ:
Note that
Z
X
j dX ðx; yÞ2 /C0 dX ðz; yÞ2jd/C23ðyÞ/C20 dXðx; zÞ
Z
X
fdX ðx; yÞþ dX ðz; yÞgd/C23ðyÞ < þ1:
Ap o i n tz0 2 X is called the center of mass of the measure /C23 2 B1ðXÞ if for any
z 2 X, z0 is a unique minimizing point of the function hz;/C23.W ed e n o t et h ep o i n tz0
by cð/C23Þ. A metric space X is said to be centric if every /C23 2 B1ðXÞ h a st h ec e n t e ro f
mass.
PROPOSITION 2.10 (cf. [ 15, Proposition 4.3]). Any complete CAT(0)-space
Central and Lp-concentration of 1-Lipschitz maps into R-trees 489
is centric.
A simple variational argument yields the following lemma.
LEMMA 2.11 (cf. [ 15, Proposition 5.4]). Let H be a Hilbert space. Then for
each /C23 2 B1ðHÞ with m ¼ /C23ðXÞ,w eh a v e
cð/C23Þ¼ 1
m
Z
H
yd/C23ðyÞ:
Let ðT; dT Þ be an R-tree and /C23 2 B1ðT Þ.F o r z 2 T and T 0 2 C 0
T ðzÞ, we put
cz;T 0 ð/C23Þ :¼
Z
T 0
dT ðz; wÞd/C23ðwÞ/C0
Z
T nT 0
dT ðz; wÞd/C23ðwÞ:
Let us consider a (possibly inﬁnite) simplicial tree Ts. Here, the length of each
edge of Ts is not necessarily equal to 1. We assume that every vertex of Ts is an
isolated point in the vertex set of Ts.
PROPOSITION 2.12 (cf. [ 15, Proposition 5.9]). Let /C23 2 B1ðTsÞ and z 2 Ts.
Then, z ¼ cð/C23Þ if and only if cz;T 0 ð/C23Þ/C20 0 for any T 0 2 C 0
Ts ðzÞ.
PROPOSITION 2.13 (cf. [ 15, Proposition 6.1]). Let X be a complete
CAT(0)-space and /C23 2 B1ðXÞ. Assume that the support of /C23 is contained in a
closed convex subset K of X. Then, we have cð/C23Þ2 K.
Let X be a metric space. For /C22; /C232 P1ðXÞ, we deﬁne the L1-Wasserstein
distance dW
1 ð/C22; /C23Þ between /C22 and /C23 as the inﬁmum of
R
X/C2 X dX ðx; yÞd/C25ðx; yÞ,w h e r e
/C25 2 P1ðX /C2 XÞ runs over all couplings of /C22 and /C23, that is, measures /C25 with the
property that /C25ðA /C2 XÞ¼ /C22ðAÞ and /C25ðX /C2 AÞ¼ /C23ðAÞ for any Borel subset A /C18X.
LEMMA 2.14 (cf. [ 18, Theorem 7.12]). As e q u e n c ef/C22ng1
n¼1 /C18P1ðXÞ con-
verges to /C22 2 P1ðXÞ with respect to the distance function dW
1 if and only if the
sequence f/C22ng1
n¼1 converges weakly to the measure /C22 and
lim
n!1
Z
X
dX ðx; yÞd/C22nðyÞ¼
Z
X
dXðx; yÞd/C22ðyÞ
for some (and then any) x 2 X.
THEOREM 2.15 (cf. [ 15, Theorem 6.3]). Let X be a CAT(0)-space. Given
490 K. F UNANO
/C22; /C232 P1ðXÞ,w eh a v e dX ðcð/C22Þ;c ð/C23ÞÞ /C20 dW
1 ð/C22; /C23Þ.
2.3.2 Observable central radius.
Let Y be a metric space and assume that /C23 2 B1ðY Þ has the center of mass.
We denote by BY ðy; rÞ the closed ball in Y centered at y 2 Y and with radius
r> 0. For any /C20> 0, putting m :¼ /C23ðY Þ, we deﬁne the central radius
CRadð/C23; m/C0 /C20Þ of /C23 as the inﬁmum of /C26> 0 such that /C23ðBY ðcð/C23Þ;/C26ÞÞ /C21m /C0 /C20.
Let ðX; dX ;/C22X Þ be an mm-space with /C22X 2 B1ðXÞ and Y a centric metric
space. For any /C20> 0, we deﬁne
ObsCRadY ðX; /C0 /C20Þ :¼ supfCRadðf/C3 ð/C22X Þ;m /C0 /C20Þj f : X ! Y is a 1-Lipschitz mapg;
and call it the observable central radius of X.
LEMMA 2.16 (cf. [ 7, Section 3(1/2).31]). For any /C20> 0,w eh a v e
diamð/C23; m/C0 /C20Þ/C20 2C R a dð/C23; m/C0 /C20Þ:
In particular, we get
ObsDiamY ðX; /C0 /C20Þ/C20 2O b s C R a dY ðX; /C0 /C20Þ:
REMARK 2 . 1 7 . F r o mt h ea b o v el e m m a ,w es e et h a tt h ec e n t r a lc o n c e n -
tration implies the concentration. T he converse is not true in general. For
example, let us consider the mm-spaces Xn :¼f xn;y ng with the distance function
dXn given by dXn ðxn;y nÞ :¼ n and with the Borel probability measure /C22Xn given by
/C22Xn ðfxngÞ :¼ 1 /C0 1=n and /C22Xn ðfyngÞ :¼ 1=n. Then, 1-Lipschitz maps fn : Xn ! R
deﬁned by fnðxÞ :¼ dXn ðx; xnÞ satisfy that cððfnÞ/C3 ð/C22Xn ÞÞ ¼ 1 for all n 2 N ,w h e r e a s
the maps fn concentrate to 0 and ObsDiamRðXn; /C0 /C20Þ! 0 as n !1 for any
/C20> 0.
LEMMA 2.18. Let /C23 2 B1ðRnÞ with m :¼ /C23ðRnÞ. Then, for any p /C211 and
/C20> 0,w eh a v e
CRadð/C23; m/C0 /C20Þ/C20 Vpð/C23Þ
ðm/C20Þ1=p : ð2:1Þ
I nt h ec a s eo fp ¼ 2, we also have the better estimate
CRadð/C23; m/C0 /C20Þ/C20 V2ð/C23Þﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
2m/C20
p : ð2:2Þ
Central and Lp-concentration of 1-Lipschitz maps into R-trees 491
PROOF. We shall prove that /C23ðRn n BRn ðcð/C23Þ;/C260ÞÞ /C20 /C20 for /C260 :¼ Vpð/C23Þ=
ðm/C20Þ1=p. Suppose that /C23ðRn n BRn ðcð/C23Þ;/C260ÞÞ >/C20 . From Lemma 2.11, we get
Z
Rn
jcð/C23Þ/C0 xjpd/C23ðxÞ/C20 Vpð/C23Þp
m :
Hence, by Chebyshev’s inequality, we see that
Vpð/C23Þp
m ¼ /C26p
0/C20<
Z
Rn
jcð/C23Þ/C0 xjpd/C23ðxÞ/C20 Vpð/C23Þp
m ;
which is a contradiction. Therefore, we obtain /C23ðBRn ðcð/C23Þ;/C260ÞÞ /C21m /C0 /C20 and so
(2.1).
Since
Z
Rn
jcð/C23Þ/C0 xj2d/C23ðxÞ¼ V2ð/C23Þ2
2m ;
the same argument yields (2.2). This completes the proof. /C3
COROLLARY 2.19. Let X be an mm-space with /C22X 2 B1ðXÞ. Then, for any
p /C211,w eh a v e
ObsCRadRn ðX; /C0 /C20Þ/C20 1
ðm/C20Þ1=p Obs Lp-VarRn ðXÞ: ð2:3Þ
I nt h ec a s eo fp ¼ 2, we also have the better estimate
ObsCRadRn ðX; /C0 /C20Þ/C20 1ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
2m/C20
p Obs L2-VarRn ðXÞ: ð2:4Þ
COROLLARY 2.20. Let X be an mm-space. Then, for any p /C211 and /C20> 0,
we have
SepðX; /C20; /C20Þ/C20 2
ðm/C20Þ1=p Obs Lp-VarRðXÞ: ð2:5Þ
I nt h ec a s eo fp ¼ 2,w ea l s oh a v e
SepðX; /C20; /C20Þ/C20
ﬃﬃﬃﬃﬃﬃﬃﬃ
2
m/C20
r
Obs L2-VarRðXÞ: ð2:6Þ
492 K. F UNANO
PROOF. Assume ﬁrst that there is a 1-Lipschitz function f : X ! R such
that f/C3 ð/C22XÞ =2 B1ðRÞ.F r o mH o¨lder’s inequality, we have
R
R jx /C0 yjpdf/C3 ð/C22X ÞðyÞ¼
þ1 for any x 2 X. This implies VpðfÞ¼þ 1 and so Obs Lp-VarRðXÞ¼þ 1 .
We consider the other case that f/C3 ð/C22XÞ2 B1ðRÞ for any 1-Lipschitz function
f : X ! R. Combining Proposition 2.4 with Lemma 2.16 and (2.3), we have
SepðX; /C20; /C20Þ/C20 2
ðm/C200Þ1=p Obs Lp-VarRðXÞ
for any /C20>/C20 0 > 0. Letting /C200 ! /C20, we have (2.5). Replacing (2.3) with (2.4) in the
above argument, we also obtain (2.6). /C3
3. Existence of a median in an R-tree.
Let T be an R-tree and /C23 a ﬁnite Borel measure on T with m :¼ /C23ðT Þ < þ1.
Am e d i a no f/C23 is a point z 2 T such that there exist two subtrees T 0, T 00 /C18T such
that T ¼ T 0 [ T 00, T 0 \ T 00 ¼f zg, /C23ðT 0Þ/C21m=3,a n d /C23ðT 00Þ/C21m=3.
EXAMPLE 3.1. For i ¼ 1; 2; 3,l e t Ti :¼f ði; rÞj r 2½ 0; þ1Þg be three copies
of ½0; þ1Þ equipped with the usual Eucli dean distance function. The tripod T is
the metric space obtained by gluing together all these spaces Ti, i ¼ 1; 2; 3,a tt h e i r
origins with the intrinsic distance function. We consider the Borel probability
measure /C23 deﬁned by /C23ðfði; 1ÞgÞ :¼ 1=3 for all i ¼ 1; 2; 3. We easily see that the
origin of T is a median of the measure /C23. We note that there is no point in T
separating T into two subtrees with measures greater than 1/3.
The existence of a median of a ﬁnite Borel measure on a simplicial tree is
proved in [ 3, Proposition 5.2]. The purpose of this section is to prove the existence
of a median of a ﬁnite Borel measure on an R-tree, which is needed for the proofs
of our main theorems. Although the proof of the existence is similar to the proof
for the case of a simplicial tree, we give it for completeness:
PROPOSITION 3.2. Every ﬁnite Borel measure on an R-tree has a median.
PROOF.L e t /C23 be a ﬁnite Borel measure on an R-tree with m :¼ /C23ðT Þ.
Assume that a point z 2 T satisﬁes that /C23ðT 0Þ <m =3 for any T 0 2 C0
T ðzÞ,t h e ni ti s
easy to check that z is a median of /C23. So, we assume that for any z 2 T there exists
T ðzÞ2 C 0
T ðzÞ such that /C23ðT ðzÞÞ /C21m=3.I ff o rs o m e z 2 T ,t h e r ee x i s t s
T 0 2 C 0
T ðzÞnf T ðzÞg such that /C23ðT 0Þ/C21m=3, then this z is a median of /C23. Thereby,
we also assume that /C23ðT 0Þ <m =3 for any z 2 T and T 0 2 C 0
T ðzÞnf T ðzÞg.
Fixing a point z0 2 T , we assume that there exists z 2 T ðz0Þnf z0g such that
Central and Lp-concentration of 1-Lipschitz maps into R-trees 493
z0 2 T ðzÞ.P u t
t0 :¼ infft 2ð 0; dT ðz0;z Þ/C138 jz0 2 T ð/C30z0 ;zðtÞÞg:
CLAIM 3.3. /C30z0 ;zðt0Þ is a median of /C23.
PROOF. Assume ﬁrst that t0 ¼ 0. Then, taking a monotone decreasing
sequence ftng1
n¼1 /C18ð0; dT ðz0;z Þ/C138such that tn ! 0 as n !1 and z0 2 T ð/C30z0 ;zðtnÞÞ
for any n 2 N ,w es h a l ls h o wt h a tT1
n¼1 T ð/C30z0 ;zðtnÞÞ /C18 ðT n T ðz0ÞÞ [ fz0g.I fi ti s ,
we conclude that the point z0 ¼ /C30z0 ;zð0Þ is a median of /C23 a sf o l l o w s :F r o mt h e
uniqueness of T ð/C30z0;zðtnÞÞ,w eh a v e T ð/C30z0;zðtnþ1ÞÞ /C18 T ð/C30z0 ;zðtnÞÞ for each n 2 N .
Thus, we get /C23ðT1
n¼1 T ð/C30z0 ;zðtnÞÞÞ ¼ limn!1 /C23ðT ð/C30z0 ;zðtnÞÞÞ /C21m=3.
Suppose that there exists w 2ð T ðz0Þnf z0gÞ \T1
n¼1 T ð/C30z0 ;zðtnÞÞ.N o t et h a t
ðz0;z /C138T \ð z0;w /C138T 6¼; . Actually, if ðz0;z /C138T \ð z0;w /C138T ¼; , then it follows from the
property (2) of R-trees that ½z; w/C138T ¼½ z0;z /C138T [½ z0;w /C138T . Especially, we have
z0 2½ z; w/C138T .S i n c eT ðz0Þnf z0g is convex by virtue of Lemma 2.8, ½z; w/C138T does not
contain the point z0. This is a contradiction. Thus, there exists t 2ð 0; dT ðz0;z Þ/C138
such that /C30z0 ;zðtÞ2ð z0;z /C138T \ð z0;w /C138T .W ep i c k n0 2 N with tn0 <t .S i n c e
w 2ð T ðz0Þnf z0gÞ \T1
n¼1 T ð/C30z0 ;zðtnÞÞ /C18 T ð/C30z0 ;zðtn0 ÞÞ n fz0g,w eg e t /C30z0 ;zðtÞ2ð z0;
w/C138T /C18T ð/C30z0 ;zðtn0 ÞÞ n fz0g. Thereby, we get /C30z0;zðtÞ2 T ð/C30z0;zðtn0 ÞÞ n f/C30z0 ;zðtn0 Þg.
Therefore, since z0 2 T ð/C30z0 ;zðtn0 ÞÞ n f/C30z0 ;zðtn0 Þg and T ð/C30z0;zðtn0 ÞÞ n f/C30z0 ;zðtn0 Þg is
convex, we obtain
/C30z0 ;zðtn0 Þ2½ z0;/C30z0 ;zðtÞ/C138T /C18T ð/C30z0 ;zðtn0 ÞÞ n f/C30z0;zðtn0 Þg:
This is a contradiction. Therefore, we have T1
n¼1 T ð/C30z0 ;zðtnÞÞ /C18 ðT n T ðz0ÞÞ [ fz0g.
We consider the other case that t0 > 0. Take a monotone increasing sequence
ftng1
n¼1 /C18ð0; þ1Þ such that tn ! t0 as n !1 and z0 =2 T ð/C30z0 ;zðtnÞÞ for each
n 2 N .T h e n ,t h es a m ep r o o fi nt h ec a s eo f t0 ¼ 0 implies that
/C23ðT1
n¼1 T ð/C30z0 ;zðtnÞÞÞ /C21m=3 and T1
n¼1 T ð/C30z0;zðtnÞÞ /C18 ðT n T ð/C30z0 ;zðt0ÞÞÞ [ f/C30z0 ;zðt0Þg.
Therefore, /C30z0;zðt0Þ is a median of /C23. This completes the proof of the claim. /C3
We next assume that z0 =2 T ðzÞ for any z 2 T ðz0Þ.W ed e n o t eb y/C0the set of
all unit speed geodesics /C13 : ½0;L ð/C13Þ/C138 !T ðz0Þ such that /C13ð0Þ¼ z0 and /C13ð½t; Lð/C13Þ/C138Þ /C18
T ð/C13ðtÞÞ for any t 2½ 0;L ð/C13Þ/C138. Because of the assumption, we easily see
CLAIM 3.4. For any z 2 T ðz0Þ,w eh a v e /C30z0 ;z 2 /C0.
CLAIM 3.5. For any /C13; /C130 2 /C0with Lð/C13Þ/C20 Lð/C130Þ,w eh a v e
½/C13ð0Þ;/C13ðLð/C13ÞÞ/C138T /C18½/C130ð0Þ;/C130ðLð/C130ÞÞ/C138T :
494 K. F UNANO
PROOF. Suppose that
t0 :¼ supft 2½ 0;L ð/C13Þ/C138 j ½/C13ð0Þ;/C13ðtÞ/C138T /C18½/C130ð0Þ;/C130ðLð/C130ÞÞ/C138T g <L ð/C13Þ:
Then, we have /C13ðtÞ =2½ /C130ð0Þ;/C130ðLð/C130ÞÞ/C138T for any t>t 0.A c t u a l l y ,i f /C13ðtÞ2
½/C130ð0Þ;/C130ðLð/C130ÞÞ/C138T ,t h e nw eh a v e /C13ðtÞ¼ /C130ðtÞ.T h u s , ½/C13ðt0Þ;/C13ðtÞ/C138T ¼½ /C130ðt0Þ;/C130ðtÞ/C138T
by the property ð2Þ of R-trees. Thereby, we get ½/C13ð0Þ;/C13ðtÞ/C138T /C18½/C130ð0Þ;/C130ðLð/C130ÞÞ/C138T .
Since t>t 0, this contradicts the deﬁnition of t0. Therefore, from the property (2)
of R-trees, we have
½/C13ðLð/C13ÞÞ;/C130ðLð/C130ÞÞ/C138T ¼½ /C13ðt0Þ;/C13ðLð/C13ÞÞ/C138T [½ /C130ðt0Þ;/C130ðLð/C130ÞÞ/C138T : ð3:1Þ
Since /C13; /C130 2 /C0,w eh a v e /C13ðLð/C13ÞÞ;/C130ðLð/C130ÞÞ 2 T ð/C13ðt0ÞÞ n f/C13ðt0Þg. So, from the
convexity of T ð/C13ðt0ÞÞ n f/C13ðt0Þg,w eg e t ½/C13ðLð/C13ÞÞ;/C130ðLð/C130ÞÞ/C138T /C18T ð/C13ðt0ÞÞ n f/C13ðt0Þg.
This is a contradiction, because /C13ðt0Þ2½ /C13ðLð/C13ÞÞ;/C130ðLð/C130ÞÞ/C138T by (3.1). This
completes the proof of the claim. /C3
Putting /C11 :¼ supfLð/C13Þj /C13 2 /C0g, we shall show that /C11< þ1.I f /C11< þ1,w e
ﬁnish the proof of the proposition as follows: By the completeness of R-trees and
Claim 3.5, there exists unique /C13 2 /C0with Lð/C13Þ¼ /C11.W ea l s on o t et h a t/C11> 0 by
Claim 3.4. Thus, there exists a monotone increasing sequence ftng1
n¼1 of positive
numbers such that tn ! /C11 as n !1 . We easily see that T ð/C13ðtnþ1ÞÞ /C18 T ð/C13ðtnÞÞ for
any n 2 N and T1
n¼1 T ð/C13ðtnÞÞ ¼ f /C13ðLð/C13ÞÞg.S i n c e /C23ðT ð/C13ðtnÞÞÞ /C21m=3, the point
/C13ðLð/C13ÞÞ is a median of /C23.
Suppose that /C11 ¼þ 1. Then, taking a sequence f/C13ng1
n¼1 /C18/C0such that
Lð/C13nÞ <L ð/C13nþ1Þ for any n 2 N and Lð/C13nÞ!þ 1 as n !1 ,w eo b t a i nT1
n¼1 T ð/C13nðLð/C13nÞÞÞ ¼ ; .S i n c e T ð/C13nþ1ðLð/C13nþ1ÞÞÞ /C18 T ð/C13nðLð/C13nÞÞÞ for any n 2 N ,
we have
0 ¼ /C23
\1
n¼1
T ð/C13nðLð/C13nÞÞÞ
 !
¼ lim
n!1
/C23ðT ð/C13nðLð/C13nÞÞÞÞ /C21m
3 ;
which is a contradiction. This completes the proof of the proposition. /C3
4. The necessity in Proposition 2.12 for R-trees.
In order to prove the main theorems, we extend the necessity in Proposition
2.12 to R-trees:
PROPOSITION 4.1. Let T be an R-tree and /C23 2 B1ðT Þ. Then, we have
Central and Lp-concentration of 1-Lipschitz maps into R-trees 495
ccð/C23Þ;T 0 ð/C23Þ/C20 0 for any T 0 2 C 0
T ðcð/C23ÞÞ.
PROOF. For simplicity, we assume that /C23ðT Þ¼ 1. We shall approximate
the measure /C23 by a measure whose support lies on a simplicial tree in T .G i v e n
n 2 N , there exists a compact subset Kn /C18T such that /C23ðT n KnÞ < 1=n andR
T nKn
dT ðcð/C23Þ;w Þd/C23ðwÞ < 1=n.T a k ea ð1=nÞ-net fzn
i gln
i¼1 of Kn with mutually
diﬀerent elements such that dT ðcð/C23Þ;z n
1 Þ < 1=n.W et h e nt a k eas e q u e n c efAn
i gln
i¼1
of mutually disjoint Borel subset of Kn such that zn
i 2 An
i , An
i /C18BT ðzn
i ; 1=nÞ,a n d
Kn ¼Sln
i¼1 An
i . Deﬁne the Borel probability measure /C23n on fzn
i gln
i¼1 by
/C23nðfzn
1 gÞ :¼ /C23ðAn
1 Þþ /C23ðT n KnÞ and /C23nðfzn
i gÞ :¼ /C23ðAn
i Þ for i /C212.
CLAIM 4.2. dW
1 ð/C23n;/C23Þ! 0 as n !1 .
PROOF.W e s h a l l s h o w t h a t
lim
n!1
Z
T
dT ðcð/C23Þ;w Þd/C23nðwÞ¼
Z
T
dT ðcð/C23Þ;w Þd/C23ðwÞ: ð4:1Þ
Since
Z
T
dT ðcð/C23Þ;w Þd/C23nðwÞ¼
Xln
i¼1
dT ðcð/C23Þ;z n
i Þ/C23ðAn
i Þþ dT ðcð/C23Þ;z n
1 Þ/C23ðT n KnÞ;
we have
Z
T
dT ðcð/C23Þ;w Þd/C23nðwÞ/C0
Xln
i¼1
dT ðcð/C23Þ;z n
i Þ/C23ðAn
i Þ
/C12/C12/C12/C12/C12
/C12/C12/C12/C12/C12< 1
n2 : ð4:2Þ
By An
i /C18BT ðzn
i ; 1=nÞ,w eg e t
Xln
i¼1
dT ðcð/C23Þ;z n
i Þ/C23ðAn
i Þ/C0
Z
Kn
dT ðcð/C23Þ;w Þd/C23ðwÞ
/C12/C12/C12/C12/C12
/C12/C12/C12/C12/C12 ð4:3Þ
¼
Xln
i¼1
Z
An
i
fdT ðcð/C23Þ;w Þ/C0 dT ðcð/C23Þ;z n
i Þgd/C23ðwÞ
/C12/C12/C12/C12/C12
/C12/C12/C12/C12/C12/C20
Xln
i¼1
Z
An
i
dT ðw; zn
i Þd/C23ðwÞ/C20 1
n :
Hence, combining (4.2) with (4.3) and
Z
Kn
dT ðcð/C23Þ;w Þd/C23ðwÞ/C0
Z
T
dT ðcð/C23Þ;w Þd/C23ðwÞ
/C12/C12/C12/C12
/C12/C12/C12/C12/C20
Z
T nKn
dT ðcð/C23Þ;w Þd/C23ðwÞ < 1
n ;
496 K. F UNANO
we obtain (4.1). The same way as the above proof shows that the sequence f/C23ng1
n¼1
converges weakl y to the measure /C23. Therefore, by using Lemma 2.14, this
completes the proof of the claim. /C3
Applying Claim 4.2 to Theorem 2.15, we get cð/C23nÞ! cð/C23Þ as n !1 .S i n c e
the convex hull in T of the set fzn
i gln
i¼1 is a simplicial tree with ﬁnite vertex set and
cð/C23nÞ is contained in the convex hull by Proposition 2.13, it follows from
Proposition 2.12 that ceT; cð/C23n Þð/C23nÞ/C20 0 for any eT 2 C 0
T ðcð/C23nÞÞ.L e t T 0 2 C 0
T ðcð/C23ÞÞ.
Assume ﬁrst that cð/C23nÞ2 T n T 0 for inﬁnitely many n 2 N . Then, taking Tn 2
C 0
T ðcð/C23nÞÞ with T 0 /C18Tn,w eh a v e
cT 0 ;cð/C23Þð/C23nÞ/C20 cTn ;cð/C23n Þð/C23nÞþ dT ðcð/C23nÞ;c ð/C23ÞÞ /C20 dT ðcð/C23nÞ;c ð/C23ÞÞ:
Therefore, we obtain cT 0 ;cð/C23Þð/C23Þ¼ limn!1 cT 0 ;cð/C23Þð/C23nÞ/C20 0.
We consider the other case that cð/C23nÞ2 T 0 for any n 2 N .L e t
zn 2½ cð/C23Þ;c ð/C231Þ/C138T be the unique point such that
dT ðzn;c ð/C23nÞÞ ¼ inffdT ðz; cð/C23nÞÞ j z 2½ cð/C23Þ;c ð/C231Þ/C138T g:
Since cð/C23nÞ2 T 0 for all n 2 N and cð/C23nÞ! cð/C23Þ as n !1 ,b yt a k i n gas u b s e -
quence, we may assume that dT ðcð/C23Þ;z nþ1Þ/C20 dT ðcð/C23Þ;z nÞ for any n 2 N .F o re a c h
n /C212,w et a k e Tn 2 C 0
T ðznÞ and eTn 2 C 0
T ðcð/C23nÞÞ such that cð/C231Þ2 Tn and cð/C231Þ2
eTn.O b s e r v et h a tTn /C18Tnþ1.S i n c eTn /C18eTn,w eh a v e
cTn ;zn ð/C23nÞ/C20 ceT; cð/C23n Þð/C23nÞþ dT ðcð/C23nÞ;z nÞ/C20 dT ðcð/C23nÞ;z nÞ: ð4:4Þ
We also easily see
CLAIM 4.3. T 0 nf cð/C23Þg ¼S1
n¼2 Tn.
The same proof as Claim 4.2 implies that
sup
Z
A
dT ðzn;w Þd/C23nðwÞ/C0
Z
A
dT ðzn;w Þd/C23ðwÞ
/C12/C12/C12/C12
/C12/C12/C12/C12jA /C18T is a Borel subset
/C26/C27
! 0a s n !1 :
Combining this with (4.4) and Claim 4.3, we obtain
cT 0 ;cð/C23Þð/C23Þ¼ lim
n!1
cTn ;zn ð/C23Þ¼ lim
n!1
cTn ;zn ð/C23nÞ/C20 lim
n!1
dT ðcð/C23nÞ;z nÞ¼ 0:
This completes the proof of the proposition. /C3
Central and Lp-concentration of 1-Lipschitz maps into R-trees 497
The author does not know whether the co nverse of Proposition 4.1 holds or
not.
5. Proof of the main theorems.
Combining Proposition 3.2 with the same proof as [ 3, Lemma 5.3] implies the
following proposition:
PROPOSITION 5.1. Let T be an R-tree and /C23 a ﬁnite Borel measure. Then,
for any /C20> 0,w eh a v e
/C23B T m/C23; Sep /C23; m
3 ; /C20
2
/C18/C19/C18/C19/C18/C19
/C21m /C0 /C20; ð5:1Þ
where m/C23 is a median of the measure /C23.I np a r t i c u l a r ,l e t t i n gX be an mm-space,
we have
ObsDiamT ðX; /C0 /C20Þ/C20 2S e p X; m
3 ; /C20
2
/C18/C19
: ð5:2Þ
Proposition 5.1 together with Corollary 2.6 yields Theorem 1.1. The
following way to prove Theorem 1.1 is much easier and more straightforward
than the above way, that is, to prove the existence of a median of a measure on an
R-tree.
PROOF OF THEOREM 1.1. Our goal is to prove the following inequality:
ObsDiamT ðX; /C0 /C20Þ/C20 3S e p X; /C20
3 ; /C20
3
/C18/C19
þ 4O b s D i a mRðX; /C0 /C20Þð 5:3Þ
for any /C20> 0 with /C20 /C20 m=2.L e t f : X ! T be an arbitrary 1-Lipschitz map. Fixing
ap o i n t z0 2 T ,w es h a l lc o n s i d e rt h ef u n c t i o n g : T ! R deﬁned by
gðzÞ :¼ dT ðz; z0Þ.S i n c eg /C14f : X ! R is a 1-Lipschitz function, by the deﬁnition
of the observable diameter, there is an interval A ¼½ s; t/C138/C18½0; þ1Þ such that
diam A /C20 ObsDiamRðX; /C0 /C20Þ and ðg /C14fÞ/C3 ð/C22X ÞðAÞ/C21m /C0 /C20. Observe that the set
g/C0 1ðAÞ is the annulus fz 2 T j s /C20 dT ðz; z0Þ/C20 tg.W ed e n o t eb y C the set of all
connected components of the set g/C0 1ðAÞnf z0g.
CLAIM 5.2. For any T 0 2 C , we have diam T 0 /C20 2d i a mA.
PROOF.G i v e n a n y z1;z 2 2 T 0, we shall show that /C30z0;z1 ðsÞ¼ /C30z0;z2 ðsÞ.
498 K. F UNANO
Suppose that /C30z0;z1 ðsÞ 6¼ /C30z0;z2 ðsÞ. Then, putting s0 :¼ supft 2½ 0; þ1Þ j /C30z0 ;z1 ðtÞ¼
/C30z0 ;z2 ðtÞg,w eh a v e 0 <s 0 <s . By the deﬁnition of s0 and the property (2) of
R-trees, we have ð/C30z0 ;z1 ðs0Þ;z 1/C138T \ð /C30z0 ;z2 ðs0Þ;z 2/C138T ¼; . Therefore, by the property
(2) of R-trees, we get
½z1;z 2/C138T ¼½ /C30z0 ;z1 ðs0Þ;z 1/C138T [½ /C30z0 ;z2 ðs0Þ;z 2/C138T :
Hence, since T 0 is convex by virtue of Proposition 2.9, the points z1 and z2 must be
included in diﬀerent components in C T ð/C30z0 ;z1 ðs0ÞÞ. This is a contradiction, since
T 0 ¼SfC \ T 0 j C 2 C T ð/C30z0 ;z1 ðs0ÞÞg and T 0 is connected. Thus, we have
/C30z0 ;z1 ðsÞ¼ /C30z0 ;z2 ðsÞ. Consequently, we obtain
dT ðz1;z 2Þ/C20 dT ðz1;/C30z0;z1 ðsÞÞ þ dT ð/C30z0;z2 ðsÞ;z 2Þ/C20 2ðt /C0 sÞ/C20 2O b s D i a mRðX; /C0 /C20Þ:
This completes the proof of the claim. /C3
We shall consider the relation /C24 on C deﬁned by T 0 /C24 T 00 if and only if
dT ðT 0;T 00Þ/C20 SepðX; /C20=3;/C20 =3Þ.
CLAIM 5.3. The relation /C24 is an equivalence relation on C .
PROOF.W e o n l y p r o v e ‘ ‘T1 /C24 T2, T2 /C24 T3 ) T1 /C24 T3’ ’ for diﬀerent Ti 2 C ,
i ¼ 1; 2; 3. Taking points zi 2 Ti for i ¼ 1; 2; 3, we put s12 :¼ maxft 2½ 0; þ1Þ j
/C30z0 ;z1 ðtÞ¼ /C30z0 ;z2 ðtÞg and s23 :¼ maxft 2½ 0; þ1Þ j /C30z0 ;z2 ðtÞ¼ /C30z0 ;z3 ðtÞg.S i n c eTi are
diﬀerent to each other, we easily see that s12 /C20 s, s23 /C20 s,
dT ðT1;T 2Þ¼ dT ð/C30z0 ;z1 ðsÞ;/C30z0;z1 ðs12ÞÞ þ dT ð/C30z0 ;z1 ðs12Þ;/C30z0 ;z2 ðsÞÞ
¼ 2ðs /C0 s12Þ
/C20 SepðX; /C20=3;/C20 =3Þ;
and similarly dT ðT2;T 3Þ¼ 2ðs /C0 s23Þ/C20 SepðX; /C20=3;/C20 =3Þ.I f s12 /C20 s23,w et h e n
obtain
dT ðT1;T 3Þ/C20 dT ð/C30z0 ;z1 ðsÞ;/C30z0 ;z3 ðsÞÞ
/C20 dT ð/C30z0 ;z1 ðsÞ;/C30z0 ;z1 ðs12ÞÞ þ dT ð/C30z0;z2 ðs12Þ;/C30z0 ;z2 ðs23ÞÞ
þ dT ð/C30z0 ;z3 ðs23Þ;/C30z0 ;z3 ðsÞÞ
¼ð s /C0 s12Þþð s23 /C0 s12Þþð s /C0 s23Þ
¼ 2ðs /C0 s12Þ
/C20 SepðX; /C20=3;/C20 =3Þ:
Central and Lp-concentration of 1-Lipschitz maps into R-trees 499
I nt h ec a s eo fs23 /C20 s12, the same conclusion also follows from the same argument
as the above. This completes the proof of the claim. /C3
Let C 0 denote the set of equi valence classes of C = /C24 . Suppose that
f/C3 ð/C22X ÞðS
T 02S T 0Þ </C20 =3 for any S 2 C 0.S i n c e f/C3 ð/C22XÞðg/C0 1ðAÞÞ /C21m /C0 /C20 /C21/C20,w e
have C 0 /C18C 0 such that
/C20
3 /C20 f/C3 ð/C22X Þ
[
S0 2C 0
[
T 0 2S0
T 0
 !
< 2/C20
3 :
Hence, by putting C 00 :¼ C 0 n C 0,w eg e t
Sep X; /C20
3 ; /C20
3
/C18/C19
< dT
[
S0 2C 0
[
T 0 2S0
T 0;
[
S002C 00
[
T 00 2S00
T 00
 !
/C20 Sep f/C3 ð/C22X Þ; /C20
3 ; /C20
3
/C18/C19
/C20 Sep X; /C20
3 ; /C20
3
/C18/C19
;
which is a contradiction. Thereby, there exists S 2 C 0 such that f/C3 ð/C22X ÞðS
T 02S
T 0Þ/C21/C20=3. For a subset A /C18T and r> 0, we put Ar :¼f z 2 T j dT ðz; AÞ/C20 rg.
CLAIM 5.4. f/C3 ð/C22X ÞððS
T 0 2S T 0ÞSepðX;/C20=3;/C20=3ÞÞ/C21m /C0 2/C20=3.
PROOF. Suppose that f/C3 ð/C22X ÞððS
T 0 2S T 0ÞSepðX;/C20=3;/C20=3ÞÞ <m /C0 2/C20=3. Then, we
have a contradiction since
Sep X; /C20
3 ; /C20
3
/C18/C19
< dT
[
T 0 2S
T 0;T n
[
T 0 2S
T 0
 !
SepðX;/C20=3;/C20=3Þþ"
0
@
1
A
/C20 Sep f/C3 ð/C22X Þ; /C20
3 ; /C20
3
/C18/C19
/C20 Sep X; /C20
3 ; /C20
3
/C18/C19
for any suﬃciently small "> 0. /C3
Combining Claims 5.2 and 5.4, we obtain
500 K. F UNANO
diamðf/C3 ð/C22X Þ;m /C0 /C20Þ/C20 diam
[
T 02S
T 0
 !
SepðX;/C20=3;/C20=3Þ
0
@
1
A
/C20 3S e p X; /C20
3 ; /C20
3
/C18/C19
þ 4O b s D i a mRðX; /C0 /C20Þ
and so (5.3). This completes the proof of the theorem. /C3
Note that the inequality (5.3) yields a slightly worse estimate for the
observable diameter ObsDiamT ðX; /C0 /C20Þ than (5.2).
Let T be an R-tree and /C23 2 B1ðT Þ with m :¼ /C23ðXÞ.T a k i n gam e d i a nm/C23 2 T
of the measure /C23,w el e t T/C23 an element in C 0
T ðcð/C23ÞÞ with m/C23 2 T/C23. We then deﬁne
the function ’/C23 : T ! R by ’/C23ðwÞ :¼ dT ðcð/C23Þ;w Þ if w 2 T/C23 and ’/C23ðwÞ :¼/C0 dT ðcð/C23Þ;
wÞ otherwise. The function ’/C23 is clearly the 1-Lipschitz function.
LEMMA 5.5. Let T be an R-tree and /C23 2 B1ðT Þ.T h e n ,t h ef u n c t i o n’/C23 :
T ! R satisﬁes that cðð’/C23Þ/C3 ð/C23ÞÞ /C20 0,
jcðð’/C23Þ/C3 ð/C23ÞÞj /C20 CRadðð’/C23Þ/C3 ð/C23Þ;m /C0 /C20Þþ Sep ð’/C23Þ/C3 ð/C23Þ; m
3 ; /C20
2
/C18/C19
ð5:4Þ
þ Sepðð’/C23Þ/C3 ð/C23Þ; m /C0 /C20; m/C0 /C20Þ;
and
CRadð/C23; m/C0 /C20Þ/C20 CRadðð’/C23Þ/C3 ð/C23Þ;m /C0 /C20Þþ Sep /C23; m
3 ; /C20
2
/C18/C19
ð5:5Þ
þ Sep ð’/C23Þ/C3 ð/C23Þ; m
3 ; /C20
2
/C18/C19
þ Sepðð’/C23Þ/C3 ð/C23Þ; m /C0 /C20; m/C0 /C20Þ
for any /C20> 0.
PROOF. Combining Lemma 2.11 with Proposition 4.1, we have
/C23ðT Þcðð’/C23Þ/C3 ð/C23ÞÞ ¼
Z
T
’/C23ðzÞ d/C23ðzÞ¼
Z
T/C23
dT ðcð/C23Þ;z Þd/C23ðzÞ/C0
Z
T nT/C23
dT ðcð/C23Þ;z Þd/C23ðzÞ
¼ cT/C23;cð/C23Þð/C23Þ/C20 0:
Put r1 :¼ CRadðð’/C23Þ/C3 ð/C23Þ;m /C0 /C20Þ and r2 :¼ Sepðð’/C23Þ/C3 ð/C23Þ; m=3;/C20 =2Þ.F r o m( 5 . 1 ) ,
we observe that ð’/C23Þ/C3 ð/C23ÞðBRð’/C23ðm/C23Þ;r 2ÞÞ /C21/C23ðBT ðm/C23;r 2ÞÞ /C21m /C0 /C20.T h u s ,w eg e t
dRðBRðcðð’/C23Þ/C3 ð/C23ÞÞ;r 1Þ;B Rð’/C23ðm/C23Þ;r 2ÞÞ /C20 Sepðð’/C23Þ/C3 ð/C23Þ; m /C0 /C20; m/C0 /C20Þð 5:6Þ
Central and Lp-concentration of 1-Lipschitz maps into R-trees 501
and so (5.4). The above inequality (5.6) together with cðð’/C23Þ/C3 ð/C23ÞÞ /C20 0 yields that
dT ðcð/C23Þ;m /C23Þ¼ ’/C23ðm/C23Þ/C20j cðð’/C23Þ/C3 ð/C23ÞÞ /C0 ’/C23ðm/C23Þj
/C20 r1 þ r2 þ Sepðð’/C23Þ/C3 ð/C23Þ; m /C0 /C20; m/C0 /C20Þ¼ : r3:
Therefore, putting r4 :¼ Sepð/C23; m=3;/C20 =2Þ,w eo b t a i n
/C23ðBT ðcð/C23Þ;r 3 þ r4ÞÞ /C21/C23ðBT ðm/C23;r 4ÞÞ /C21m /C0 /C20
and so (5.5). This completes the proof. /C3
PROPOSITION 5.6. Let T be an R-tree and X an mm-space with /C22X 2
B1ðXÞ. Then, for any /C20> 0 we have
ObsCRadT ðX; /C0 /C20Þ/C20 ObsCRadRðX; /C0 /C20Þþ 2S e p X; m
3 ; /C20
2
/C18/C19
þ SepðX; m /C0 /C20; m/C0 /C20Þ:
PROOF. This follows from Lemmas 2.2 and 5.5. /C3
PROOF OF THEOREM 1.2. Proposition 5.6 together with Corollary 2.6 and
Lemma 2.16 directly implies the theorem. /C3
LEMMA 5.7. Let T be an R-tree and /C23 2 B1ðT Þ.T h e n ,f o ra n y p /C211 and
/C20> 0,w eh a v e
Vpð/C23Þ/C20 2m2=p
/C26
CRadðð’/C23Þ/C3 ð/C23Þ;m /C0 /C20Þþ Sep ð’/C23Þ/C3 ð/C23Þ; m
3 ; /C20
2
/C18/C19
ð5:7Þ
þ Sepðð’/C23Þ/C3 ð/C23Þ; m /C0 /C20; m/C0 /C20Þ
/C27
þ 2Vpð’/C23Þ:
I nt h ec a s eo fp ¼ 2, we also have the better estimate
V2ð/C23Þ2 /C20 4m2
/C26
CRadðð’/C23Þ/C3 ð/C23Þ;m /C0 /C20Þþ Sep ð’/C23Þ/C3 ð/C23Þ; m
3 ; /C20
2
/C18/C19
ð5:8Þ
þ Sepðð’/C23Þ/C3 ð/C23Þ; m /C0 /C20; m/C0 /C20Þ
/C27 2
þ 2V2ð’/C23Þ2:
PROOF. From the triangle inequality, we have
Vpð/C23Þ/C20 2
ZZ
T /C2 T
dT ðcð/C23Þ;z Þpd/C23ðzÞd/C23ðwÞ
/C18/C19 1=p
¼ 2 m
Z
T
dT ðcð/C23Þ;z Þpd/C23ðzÞ
/C18/C19 1=p
:ð5:9Þ
502 K. F UNANO
Putting c/C23 :¼ cðð’/C23Þ/C3 ð/C23ÞÞ,w ea l s og e t
Z
T
dT ðcð/C23Þ;z Þpd/C23ðzÞ
/C18/C19 1=p
¼
Z
T
j’/C23ðzÞjpd/C23ðzÞ
/C18/C19 1=p
ð5:10Þ
/C20 m1=pjc/C23jþ
Z
R
jc/C23 /C0 rjpdð’/C23Þ/C3 ð/C23ÞðrÞ
/C18/C19 1=p
/C20 m1=pjc/C23jþ Vpð’/C23Þ
m1=p ;
where in the last inequality we used Lemma 2.11. Combining (5.9) with (5.10), we
obtain (5.7).
I nt h ec a s eo fp ¼ 2,w eh a v e
Z
T
dT ðcð/C23Þ;z Þ2d/C23ðzÞ¼
Z
R
jrj2dð’/C23Þ/C3 ð/C23ÞðrÞð 5:11Þ
¼ mjc/C23j2 þ
Z
R
jr /C0 c/C23j2dð’/C23Þ/C3 ð/C23ÞðrÞ
¼ mjc/C23j2 þ V2ð’/C23Þ2
2m ;
where in the second and the last equalities we used Lemma 2.11. Substituting
(5.11) to (5.9), we obtain (5.8). This completes the proof. /C3
PROPOSITION 5.8. Let T be an R-tree and X an mm-space. Then, for any
p /C211,w eh a v e
Obs Lp-VarT ðXÞ/C20 2f21=pð1 þ 2 /C121=pÞþ 1gObs Lp-VarRðXÞ: ð5:12Þ
I nt h ec a s eo fp ¼ 2, we also have the better estimate
Obs L2-VarT ðXÞ2 /C20ð 38 þ 16
ﬃﬃﬃ
2
p
ÞObs L2-VarRðXÞ2: ð5:13Þ
PROOF. Assume ﬁrst that f/C3 ð/C22XÞ2 B1ðT Þ for any 1-Lipschitz map
f : X ! T . Then, Lemma 2.2 together with Lemma 2.3 and (5.7) implies that
Central and Lp-concentration of 1-Lipschitz maps into R-trees 503
Obs Lp-VarT ðXÞ/C20 2m2=p ObsCRadRðX; /C0 /C20Þþ Sep X; m
3 ; /C20
2
/C18/C19/C26/C27
þ 2Obs Lp-VarRðXÞ
/C20 2m2=p ObsCRadRðX; /C0 /C20Þþ Sep X; /C20
2 ; /C20
2
/C18/C19/C26/C27
þ 2Obs Lp-VarRðXÞ
for any 0 </C20<m = 2. Hence, applying the inequalities (2.3) and (2.5) to this
inequality, we get
Obs Lp-VarT ðXÞ/C20 2fm1=p/C20/C0 1=pð1 þ 2 /C121=pÞþ 1gObs Lp-VarRðXÞ
for any 0 </C20<m = 2.L e t t i n g/C20 ! m=2,w eg e t( 5 . 1 2 ) .I nt h ec a s eo fp ¼ 2,f r o m
(5.8), we have
Obs L2-VarT ðXÞ2 /C20 4m2 ObsCRadRðX; /C0 /C20Þþ Sep X; /C20
2 ; /C20
2
/C18/C19/C26/C27 2
þ 2Obs L2-VarRðXÞ2
for any 0 </C20<m = 2. Therefore, substituting the i nequalities (2.4) and (2.6) to
this inequality, we get
Obs L2-VarT ðXÞ2 /C20 2fm/C20/C0 1ð2
ﬃﬃﬃ
2
p
þ 1Þ2 þ 1gObs L2-VarRðXÞ2
for any 0 </C20<m = 2. Letting /C20 ! m=2, we obtain (5.13).
We consider the other case that there exists a 1-Lipschitz map f : X ! T
with f/C3 ð/C22X Þ =2 B1ðT Þ.B yu s i n gH o¨lder’s inequality and Fubini’s theorem, we have
VpðfÞ¼þ 1 .T a k i n gx0 2 X, we put fn :¼ fjBX ðx0;nÞ for each n 2 N .F r o mL e m m a
2.7 and the above proof, we have
VpðfnÞ/C20 Obs Lp-VarT ðBX ðx0;n ÞÞ /C20 2f21=pð1 þ 2 /C121=pÞþ 1gObs Lp-VarRðBXðx0;n ÞÞ
/C202f21=pð1 þ 2 /C121=pÞþ 1gObs Lp-VarRðXÞ:
Since V2ðfnÞ! V2ðfÞ¼þ 1 as n !1 , this implies Obs Lp-VarRðXÞ¼þ 1 .T h i s
completes the proof. /C3
PROOF OF THEOREM 1.3. Proposition 5.8 directly implies the theorem. /C3
504 K. F UNANO
ACKNOWLEDGEMENTS . The author would like to express his thanks to
Professor Takashi Shioya for his valuable suggestions and assistances during the
preparation of this paper. He thanks Pro fessor Vitali Milman and Professor Shin-
ichi Ohta for useful comments. He also thanks the referee for carefully reading the
manuscript and fruitful suggestions. Wi thout them, this work would have never
been completed.
