---
doc_id: arxiv-math-0608414v1
doc_title: "Exponential asymptotics, trans-series and generalized Borel summation for analytic nonlinear rank one systems of ODE’s Ovidiu Costin ∗"
section_id: sec-004-analytic-structure-and-averaging
section_title: "Analytic structure and averaging"
section_number: null
pages: 38-44
source_pdf: 0608414v1.pdf
source_sha256: bd9a8d48a6d66945
doc_brief: "Exponential asymptotics, trans-series and generalized Borel summation for analytic nonlinear rank one systems of ODE’s Ovidiu Costin ∗ — For analytic nonlinear systems of ordinary diﬀerential equa"
---
Having the general structure of the solutions of (1.25) given in Pro position
3 and in Lemma 36 we can obtain various analytic identities. The functio n
Y±
0 := Y± has been deﬁned in the previous section.
38
Proposition 37 For m≥ 0,
Y−
m = Y+
m +
∞∑
k=1
( m + k
m
)
Sk
β(Y+
m+k·H )◦ τk (2.86)
Proof.
Y−
0 (p) is a particular solution of (1.25). It follows from Lemma 36 that
the following identity holds on R+:
Y−
0 = Y+
0 +
∞∑
k=1
Sk
β(Y+
k·H )◦ τk (2.87)
since, by (1.29) and (1.12), (2.87) holds for p∈ (0, 2).
By Lemma 36 for any C+ there is a C− such that
Y+
0 +
∞∑
k=1
C k
+(Y+
k·H )◦ τk = Y−
0 +
∞∑
k=1
C k
−(Y−
k·H )◦ τk (2.88)
To ﬁnd the relation C+ and C− we take p∈ (1, 2); we get, comparing with
(2.87):
Y+
0 (p) + C+Y1(p− 1) = Y−
0 (p) + C−Y1(p− 1)⇒ C+ = C− + Sβ (2.89)
whence, for any C∈ C,
Y+
0 +
∞∑
k=1
(C + Sβ)k(Y+
k·H )◦ τk = Y−
0 +
∞∑
k=1
C k(Y−
k·H )◦ τk (2.90)
Diﬀerentiating m times w.r. to C and taking C = 0 we get
∞∑
k=m
k!
(k− m)! Sk−m
β (Y+
k·H )◦ τk = m!(Y−
m·H )◦ τm
from which we obtain (2.86) by rearranging the terms and applying τ−m.
Proposition 38 The functions Yk, k≥ 0, are analytic in R1.
39
Proof.
Starting with (2.87), if we take p∈ (1, 2) and obtain:
Y−
0 (p) = Y+
0 (p) + SβY1(p− 1) (2.91)
By Proposition 26 and Lemma 36 the l.h.s of (2.91) is analytic in a lower
half plane neighborhood of ( ε, 1− ε), (∀ε∈ (0, 1)) and continuous in the
closure of such a neighborhood. The r.h.s. is analytic in an upper half p lane
neighborhood of ( ε, 1− ε), (∀ε∈ (0, 1)) and continuous in the closure of such
a neighborhood. Thus, Y−
0 (p) can be analytically continued along a path
crossing the interval (1 , 2) from below, i.e., Y−+
0 exists and is analytic.
Now, in (2.87), let p∈ (2, 3):
S2
βY2(p− 2) = Y0(p)−− Y(p)+− SβY1(p− 1)+ =
Y0(p)−− Y0(p)+− Y0(p)−+ + Y0(p)+ = Y0(p)−− Y0(p)−+(2.92)
and, in general, taking p∈ (k, k + 1) we get
Sk
βYk(p− k) = Y0(p)−− Y0(p)−k−1+ (2.93)
Using (2.93) inductively, the same arguments that we used for p∈ (0, 1) show
that Y−k
0 (p) can be continued analytically in the upper half plane. Thus, we
have
Remark 39 The function Y0 is analytic in R1. In fact, for p∈ (j, j + 1),
k∈ N,
Y−j+
0 (p) = Y+
0 (p) +
j∑
k=1
Sk
βY+
k (p− k)H(p− k) (2.94)
The relation (2.94) follows from (2.93) and (2.87).
R39
Note: Unlike (2.87), in (2.94) the sum contains a ﬁnite number of term s.
For instance we have:
Y−+
0 (p) = Y+
0 (p) +H(p− 1)Y+
1 (p− 1). (∀p∈ R+) (2.95)
The analyticity of Ym, m≥ 1 is shown inductively on m, using (2.86)
and following exactly the same course of proof as for k = 0.
40
Remark 40 If Sβ = 0 then Yk are analytic in W1∪ N.
Indeed, this follows from (2.87) (2.86) and Lemma 36, i)
On the other hand, if Sβ⁄= 0, then all Yk are analytic continuations of
the Borel transform of y0 (cf. (2.92)). This is an instance of the so-called
resurgence.
Moreover, we can now calculate Yba
0 . By deﬁnition, (see the discussion before
Remark 23) on the interval (0 , 2),
Yba
0 = 1
2 (Y+
0 + Y−
0 ) = Y+
0 + 1
2 Sβ(Y1H)◦ τ1 (2.96)
Now we are looking for a solution of (1.25) which satisﬁes the condition
(2.96). By comparing with Lemma 36, which gives the general form of the
solutions of (1.25), we get, now on the whole positive axis,
Yba
0 = Y+
0 +
∞∑
k=1
1
2k Sk
β(Y+
kH)◦ τk (on R+) (2.97)
which we can rewrite using (2.93):
Yba
0 = Y+
0 +
∞∑
k=1
1
2k
(
Y−k
0 − Y−k−1,+
0
)
(H◦ τk) (2.98)
Proposition 41 Let y1(p), y2(p) be analytic in R1, and such that for any
path γ = t↦→t exp(iφ(t)) inR1,
|y1,2(γ(t))| < f γ(t)∈ L1
loc(R+) (2.99)
Assume further that for some large enough b, M and any path γ inR1:
∫
γ
|y1,2|(s)e−b|s||ds| < M (2.100)
Then the analytic continuation ACγ(y1∗ y2) along a path γ inR1, of their
convolution product y1∗ y2 (deﬁned for small p by (1.20)) exists, is locally
integrable and satisﬁes (2.99) and, for the same b and some γ-independent
M ′ > 0,
∫
γ
|y1∗ y2|(s)e−b|s||ds| < M ′ (2.101)
41
Proof.
Since
2y1∗ y2 = (y1 + y2)∗ (y1 + y2)− y1∗ y1− y2∗ y2 (2.102)
it is enough to take y1 = y2 = y. For p∈ R+\N we write:
y− = y+ +
∞∑
k=1
(H· y+
k )◦ τk (2.103)
The functions yk are deﬁned inductively (the superscripts “+,(-)” mean, as
before, the analytic continuations in R1 going below(above) the real axis).
In the same way (2.93) was obtained we get by induction:
yk = (y−− y−k−1+)◦ τ−k (2.104)
where the equality holds on R+\N and + ,− mean the upper and lower con-
tinuations. For any p only ﬁnitely many terms in the sum in (2.103) are
nonzero. The sum is also convergent in ‖‖b (by dominated convergence; note
that, by assumption, the functions y−−..−± belong to the same L1
b).
If t↦→γ(t) inR1, is a straight line, other than R+, then:
ACγ((y∗ y)) = ACγ(y)∗γ ACγ(y) if arg( γ(t))=const⁄= 0 (2.105)
(Since y is analytic along such a line). The notation ∗γ means (1.20) with
p = γ(t).
Note though that, suggestive as it might be, (2.105) is incorrect if the
condition stated there is not satisﬁed and γ is a path that crosses the real
line (see the Appendix, Section A.2)!
We get from (2.105), (2.103) (see also (A.9), in the Appendix):
(y∗ y)− = y−∗ y− = y+∗ y+ +
∞∑
k=1
(
H
k∑
m=0
y+
m∗ y+
k−m
)
◦ τk =
(y∗ y)+ +
∞∑
k=1
(
H
k∑
m=0
(ym∗ yk−m)+
)
◦ τk (2.106)
and now the analyticity of y∗ y inR1 follows: on the interval p∈ (m, m + 1)
we have from (2.104)
42
(y∗ y)−j
(p) = ( y∗ y)−(p) = ( y∗2)+(p) +
j∑
k=1
k∑
m=0
(ym∗ yk−m)+(p− k) (2.107)
Again, formula (2.107) is useful for analytically continuing ( y∗ y)−j
along
a path as the one depicted in Fig.1. By dominated convergence, ( y∗ y)±∈
T ±
(0,∞), (2.60). By (2.104), ym are analytic in R+
1 :=R1∩{ p :ℑ(p) > 0} and
thus by (2.105) the r.h.s. of (2.107) can be continued analytically in R+
1 .
The same is then true for ( y∗ y)−. The function ( y∗ y) can be extended
analytically along paths that cross the real line from below. Likewise, (y∗y)+
can be continued analytically in the lower half plane so that ( y∗ y) is analytic
inR1.
Combining (2.107), (2.105) and (2.102) we get a similar formula for the
analytic continuation of the convolution product of two functions, f, g satis-
fying the assumptions of Proposition 41
(f∗ g)−j+ = f +∗ g+ +
j∑
k=1
(
H
k∑
m=0
f +
m∗ g+
k−m
)
◦ τk (2.108)
Note that (2.108) corresponds to (2.103) and in those notations w e have:
(f∗ g)k =
k∑
m=0
fm∗ gk−m (2.109)
Integrability as well as (2.101) follow from (2.104), (2.107) and Rema rk 9.
P 41
By (1.16) and (2.104),
yba = y+ +
∞∑
k=1
1
2k (y+
kH)◦ τk
so that (see (A.9))
yba∗ yba =
(
y+ +
∞∑
k=1
1
2k (H◦ τk)(y+
k◦ τk)
) ∗2
=
43
y+∗ y+ +
∞∑
k=1
1
2kH◦ τk
k∑
m=0
(y+
m◦ τm)∗ (y+
k−m◦ τk−m)◦ τk =
y+∗ y+ +
∞∑
k=1
1
2kH◦ τk
k∑
m=0
(ym∗ yk−m)+◦ τk = (y∗2)ba (2.110)
To ﬁnish the proof of Theorem 2 note that on any ﬁnite interval the sum
in (1.16) has only a ﬁnite number of terms and by (2.110) balanced ave raging
commutes with any ﬁnite sum of the type
∑
k1,..,kn
ck1..knfk1∗ ..∗ fkn (2.111)
and then, by continuity, with any sum of the form (2.111), with a ﬁnit e or
inﬁnite number of terms, provided it converges in L1
loc. Averaging thus com-
mutes with all the operations involved in the equations (2.73). By uniq ueness
therefore, if Y0 = Yba then Yk = Yba
k for all k. Preservation of reality is im-
mediate since (1.25), (1.27) are real if (1.1) is real, therefore Yba
0 is real-valued
on R+\N (since it is real-valued on [0 , 1)∪ (1, 2)) and so are, inductively, all
Yk.
