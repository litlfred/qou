---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-017-73-asymptotics
section_title: "Asymptotics"
section_number: 7.3
pages: 22-25
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
with a proposition that bounds this quantity in terms of the systole.
Proposition 7.5.There exist somes 0 >0such that
K(s)<18.355· 2 sinh(s/2)
s
for everys≥s 0. In particular, every closed hyperbolic surfaceMof genusg≥2and
systolesys(M)≥s 0 satisfies
kiss(M)<18.355· 2 sinh(sys(M)/2)
sys(M) (g−1).
Remark7.6.This improves upon [FBP22, Remark 4.4], where we obtained the same in-
equality but with the constant 63.71 instead of 18.355.
Proof.Recall that
K(s) = 2
√
2π 2 sinh(s/2)
s inf
f
 1
−f(s)
Z ∞
0
bf(x)xtanh(x)dx

where the infimum is over admissible functionsfsuch thatf(x)≤0 ifx≥s,f(s)<0,
and bf(ξ)≥0 ifξ∈R∪i[− 1
2, 1
2].
To prove the desired inequality, we use the same functions as for the asymptotic systole
bound but choose the parameters differently. That is, we takefsuch that
bf(x) = (c−1 +b 2x2)e−b2x2/2φα(Rx) = (c−1 +b 2x2)e−b2x2/2Jα(Rx/2)2
(Rx)2α
for some parametersα,b,candRbut now setc= 1 +b 2/4 so that bf(i/2) = 0.
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 23
Recall from Lemma 6.7 that for anyκ 0∈R, we have thatR 2α+1f(R+bκ 0) tends to
−L1 := b2α
πΓ(2α+ 1)
Z ∞
κ0
(x−κ 0)2α(c−x 2)e−x2/2dx,
asR→∞. We also saw in the proof of Theorem 6.4 that
L2 := lim
R→∞
R2α+1
Z ∞
0
bf(x)xtanh(πx)dx= 2
π
Z ∞
0
tanh(πx)
x2α (c−1 + (bx) 2)e−(bx)2/2dx
= 2b2
π
Z ∞
0
tanh(πx)
x2α (x2 + 1/4)e−b2x2/2dx.
Our goal is thus to minimize the ratioL 2/L1 over the parameters such that−L 1 <0
and such thatfis non-positive froms=R+bκ 0 onwards. Atα= 0.592,b= 0.981 and
κ0 = 0.061, we obtain 2
√
2πL2/L1 <18.355, which implies that
2
√
2π 1
−f(R+bκ 0)
Z ∞
0
bf(x)xtanh(x)dx<18.355
ifRis large enough. To prove that 2
√
2πL2/L1 <18.355, we observe that
Z ∞
0
tanh(πx)
x2α (x2 + 1/4)e−b2x2/2dx
is bounded above by
π

A2 + 1
4
 A2(1−α)
2(1−α) +
Z B
A
tanh(πx)
x2α (x2 + 1/4)e−b2x2/2dx+ 1
B2α
Z ∞
B
x3e−b2x2/2dx
whenever 0<A<2<Band estimate each term using interval arithmetic withA= 1/10 4
andB= 10 4, noting that the last term can be rewritten as
1
B2α
Z ∞
B
x3e−b2x2/2dx= 1
b4B2α
Z ∞
bB
y3e−y2/2dy= (b2B2 + 2)
b4B2α e−b2B2/2.
ForL 1, we need a lower bound. We have
Z ∞
0
1−cos(x)
x2α+1 dx≥
Z B
A
1−cos(x)
x2α+1 dx
since the integrand is non-negative. We then observe that
−
Z ∞
κ0
(x−κ 0)2α(c−x 2)e−x2/2dx≥−
Z B
κ0
(x−κ 0)2α(c−x 2)e−x2/2dx,
sinceB >√c. We split this last integral atκ 0 +Aand estimate
−
Z κ0+A
κ0
(x−κ 0)2α(c−x 2)e−x2/2dx≥−A 2α
Z κ0+A
κ0
(c−x 2)e−x2/2dx
Putting all the estimates together, we obtain the certified upper bound
2
√
2πL2
L1
≤18.3545723139258<18.355.
The last thing to check is that whenRis large enough, we havef(x)≤0 for every
x≥s=R+bκ 0. The proof of this fact is similar as for the systole bound, and is deferred
to the next lemma.
24 MAXIME FORTIER BOURQUE AND BRAM PETRI
The resulting upper bound on kiss(M) when sys(M)≥s 0 then follows from Theorem 7.1.
□
We now prove a small lemma which verifies that the functionfused above satisfies the
hypotheses of Theorem 7.1 fors=R+bκ 0 wheneverRis large enough. This is similar to
Lemma 6.9 and Corollary 6.10.
Lemma 7.7.Letfbe as in Proposition 7.5 withα= 0.592,b= 0.981,c= 1 +b 2/4, and
κ0 = 0.061. Then there exists someR 0 >0such thatf(x)≤0for everyx≥R+bκ 0 and
everyR≥R 0.
Proof.We begin by proving the pointwise result that for everyκ≥κ 0, we have that
f(R+bκ)≤0 ifRis sufficiently large. Sincefis the convolution of a non-negative
function supported in [−R,R] and a function which is non-positive outside [−b √c,b√c],
it is obviously non-positive at pointsxwith|x|≥R+b √c. In other words, the result is
obvious (and holds for everyR>0) ifκ≥ √c.
Forκ∈[κ 0,√c], we use the fact thatR 2α+1f(R+bκ) converges to a positive multiple of
I(κ) =
Z ∞
κ
(x−κ) 2α(c−x 2)e−x2/2dx
asR→∞, so it suffices to check thatI(κ)<0 for everyκ∈[κ 0,√c]. This is similar to
the statement of Lemma 6.9 but is easier to prove becauseI(κ 0) is not close to 0, so coarse
bounds suffice. We write
I(κ) =
Z √c
κ
(x−κ) 2α(c−x 2)e−x2/2dx+
Z ∞
√c
(x−κ) 2α(c−x 2)e−x2/2dx
≤
Z √c
κ0
(x−κ 0)2α(c−x 2)e−x2/2dx+
Z ∞
√c
(x−√c)2α(c−x 2)e−x2/2dx
then split the first integral atκ 0 + 1/100 and the second one at 100 to get that
I(κ)≤−0.276593809735452<0
for everyκ∈[κ 0,√c].
From this pointwise result and the same continuity and compactness argument as in
Corollary 6.10, we obtain that there exists someR 0 >0 such thatf(R+bκ)≤0 for every
κ≥κ 0 and everyR≥R 0. In other words, we have thatf(x)≤0 for everyx≥R+bκ
and everyR≥R 0.□
We then combine the previous proposition with our asymptotic bound for the systole to
obtain the following bound on kissing numbers that only depends on the genus.
Theorem 7.8.There exists someg 0≥2such that every closed hyperbolic surfaceMof
genusg≥g 0 satisfies
kiss(M)< 30.608·g 2
log(g) + 1.2045.
Remark7.9.For some towers of principal congruence covers of arithmetic surfaces, the
kissing number grows at least likeg 4/3−ε for anyε>0 [SS97]. This was recently generalized
to higher dimensional hyperbolic manifolds in [DFM24] withgreplaced by the volume and
an exponent that depends on the dimension.
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 25
Proof of Theorem 7.8.Recall that Theorem 6.4 states that
sys(M)≤2 log(g) + 2.409
ifgis large enough. Lets 0 be as in Proposition 7.5. Ifgis sufficiently large, then
2 log(g) + 2.409≥s 0 and we get
K(2 log(g) + 2.409)≤18.355 2 sinh((2 log(g) + 2.409)/2)
2 log(g) + 2.409
<9.1775 e1.2045g
log(g) + 1.2045
< 30.608·g
log(g) + 1.2045
where we used the fact that 2 sinh(x/2)<e x/2 for every real numberx.
By Theorem 7.1, we have
kiss(M)≤K(sys(M))(g−1).
Furthermore, Lemma 7.4 says thatKis non-decreasing on [6,∞). We thus get that
kiss(M)≤K(2 log(g) + 2.409)(g−1)< 30.608·g 2
log(g) + 1.2045.
provided sys(M)≥6 and 2 log(g) + 2.409≥max{6,s 0}, which holds whenevergis large
enough.
When the systole is at most 2 arcsinh(1), we noted previously that kiss(M)≤6(g−1)
by the collar lemma, and this quantity is smaller than the stated bound whengis large
enough (in fact, this is true for allg≥2).
The only interval left to cover is [2 arcsinh(1),6]. By the calculations used to produce
Table 2, the functionKis bounded on that interval. One can also prove this using a single
functionfdefined by
bf(x) = (x 2 + 1/4)e−x2/2φα(Rx)
withR= 2 arcsinh(1)−
p
5/4>0 and anyα∈(0,1), because it satisfies all the hypotheses
of Theorem 7.1 for everys≥2 arcsinh(1). The resulting linear upper bound on kiss(M)
when sys(M)∈[2 arcsinh(1),6] is eventually smaller than 30.608·g2
log(g)+1.2045 whengis large
enough. □
