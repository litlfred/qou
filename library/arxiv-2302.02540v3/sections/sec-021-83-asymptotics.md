---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-021-83-asymptotics
section_title: "Asymptotics"
section_number: 8.3
pages: 28-32
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
(8.1)λ 1(M)≤λ 0(Ddiam(M)/2)
for any closed hyperbolic surfaceM, whereD R is a hyperbolic disk of radiusR,λ 0(Ω)
is the smallest Dirichlet eigenvalue of Ω, and diam(M) is the diameter ofM. From this,
Cheng deduces [Che75, Corollary 2.3] the more explicit bound
λ1(M)≤ 1
4 +
 4π
diam(M)
2
.
However, this can be improved using an inequality of Gage [Gag80, Theorem 5.2(a)] on
the smallest eigenvalue of hyperbolic disks, which states that
(8.2)λ 0(DR)≤ 1
4 + π2
R2− 1
4 sinh2(R).
If we ignore the last term (of smaller order), we obtain the improved inequality
λ1(M)≤ 1
4 +
 2π
diam(M)
2
.
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 29
In turn, the best known lower bound on the diameter is Bavard’s bound
diam(M)≥arccosh
 1√
3 tan(π/(12g−6))

wheregis the genus ofM[Bav96]. Since the tan(x)∼xasx→0 and arccosh(x) is
asymptotic to log(x) asx→∞, Bavard’s inequality has the same asymptotic behaviour
as the more elementary inequalities
diam(M)≥2 arcsinh(
p
g−1)≥log(g−1)
coming from area considerations, which result in
λ1(M)≤ 1
4 +
 2π
log(g−1)
2
.
We will improve upon this by another factor of 4.
Theorem 8.3.There exists someg 0≥2such that every closed hyperbolic surfaceMof
genusg≥g 0 satisfies
λ1(M)< 1
4 +
 π
log(g) + 0.7436
2
.
Remark8.4.An inequality of Savo [Sav09, Theorem 5.6] states that
(8.3)λ 0(DR)≥ 1
4 + π2
R2− 4π2
R3
for everyR >0. It follows that the leading terms in Gage’s upper bound (8.2) cannot
be improved. Moreover, there exist sequences of hyperbolic surfacesM g of genusgwhose
diameter is asymptotic to log(g) [BCP21]. It follows that no multiplicative improvement
as in Theorem 8.3 could be obtained from Cheng’s inequality (8.1).
Remark8.5.As stated in the introduction, it is still unknown if there exist surfaces with
λ1(M)≥1/4 in every genus. However, it was proved recently that for anyε>0, there exist
surfaces withλ 1(M)>1/4−εin large enough genus [HM23] (see also [AM25, HMT25,
MPvH25]).
The proof of Theorem 8.3 will require the following limit calculation.
Lemma 8.6.We have
lim
R→∞
R4
Z ∞
0
sin2(πRx)
1−(Rx) 2
xtanh(πx)
(Rx)2 dx= π2
2
Z ∞
0
sinh(x)
xcosh 3(x)dx>4.20718.
Proof.The following proof is due to an anonymous referee. Our goal is to simplify
I(R) :=R 4
Z ∞
0
sin2(πRx)
1−(Rx) 2
xtanh(πx)
(Rx)2 dx
=R 2
Z ∞
0
sin2(πy)
1−y 2
tanh(πy/R)
y dy
= R2
4
Z ∞
−∞
sin2(πy) tanh(πy/R)
2
y− 1
y+ 1 − 1
y−1

dy
30 MAXIME FORTIER BOURQUE AND BRAM PETRI
where we sety=Rxand used the fact that the integrand is even. After splitting the
integral as a sum of three integrals and making the changes of variableu=y±1 in two of
them, we obtain
I(R) = R2
4
Z ∞
−∞
sin2(πy)
y

2 tanh(πy/R)−tanh(π(y−1)/R)−tanh(π(y+ 1)/R)

dy
since sin2(π(y±1)) = sin 2(πy) for ally∈R. The addition formulas for sinh and cosh yield
2 tanh(a) + tanh(a−b) + tanh(a+b) = 2 tanh(a) sinh2(b)
cosh(a−b) cosh(a+b)
for anya,b∈R, so that
I(R) = R2 sinh2(π/R)
2
Z ∞
−∞
sin2(πy)
y
tanh(πy/R)
cosh(π(y−1)/R) cosh(π(y+ 1)/R) dy
= (Rsinh(π/R)) 2
2
Z ∞
−∞
sin2(Rx) tanh(x)
xcosh(x−π/R) cosh(x+π/R) dx
= (Rsinh(π/R)) 2
4
Z ∞
−∞
(1−cos(2Rx))ϕ R(x)dx,
where we setx=πy/Randϕ R(x) := tanh(x)/(xcosh(x−π/R) cosh(x+π/R)). Integration
by parts and the triangle inequality shows that

Z ∞
−∞
cos(2Rx)ϕR(x)dx

 =

1
2R
Z ∞
−∞
sin(2Rx)ϕ′
R(x)dx

≤∥ϕ′
R(x)∥1
2R
and this tends to zero asR→∞. Indeed, it is not difficult to bound|ϕ ′
R|by an integrable
function that does not depend onR.
We conclude that
lim
R→∞
I(R) = lim
R→∞
(Rsinh(π/R)) 2
4 lim
R→∞
Z ∞
−∞
ϕR(x)dx
= π2
4
Z ∞
−∞
tanh(x)
xcosh 2(x)dx= π2
2
Z ∞
0
sinh(x)
xcosh 3(x)dx,
where we used the dominated convergence theorem (ϕ R is dominated by tanhx
xcoshx ) and the
parity of the integrand.
To get a rigorous lower bound this last integral, we observe that the integrand is positive
so that
π2
2
Z ∞
0
sinh(x)
xcosh 3(x)dx≥ π2
2
Z B
A
sinh(x)
xcosh 3(x)dx
for any 0<A<B. ForA= 1/10 6 andB= 500, interval arithmetic inSageMathcertifies
that the right-hand side is at least 4.20718596495552>4.20718.□
We can now prove the theorem.
Proof of Theorem 8.3.The idea of the proof is to apply Theorem 8.1 with functions of the
formf R(x) =f(x/R)/Rfor some fixed non-negative admissible functionfsuch that bfis
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 31
non-positive on [1,∞), so that cfR(x) = bf(Rx) is non-positive on [1/R,∞). ThenR=R(g)
must be chosen as large as possible such that the inequality
(8.4) bf(Ri/2)≤2(g−1)
Z ∞
0
bf(Rx)xtanh(πx)dx
remains valid.
We choose
f(x) =
rπ
8 (2π−|x|+ sin|x|)χ [−2π,2π](x)
whose Fourier transform is equal to
bf(x) = sin2(πx)
x2(1−x 2).
Note thatfis non-negative onRand bfis non-positive on [1,∞), as required. We also
have thatfis admissible since bfis entire and isO(|x| −4) on any horizontal strip of finite
height.
For a given genusg≥2, we want to find anR=R(g)>0 such that inequality (8.4)
holds. We first compute
bf(Ri/2) = 4 sinh2(πR/2)
R2(1 +R 2/4) < 4eπR
R4 .
For the integral term, we have
lim
R→∞
R4
Z ∞
0
bf(Rx)xtanh(πx)dx= π2
2
Z ∞
0
sinh(x) cosh(x)−x
x3 cosh2(x) dx
by Lemma 8.6. Ifcis any positive number strictly smaller than the right-hand side (such
as 4.2071), then we have
(8.5)
bf(Ri/2)R∞
0
bf(Rx)xtanh(πx)dx
< 4
ceπR
provided thatRis large enough. Ifgis sufficiently large, then we can takeR= log(g−1)+log(c/2)
π
so that the right-hand side of (8.5) becomes equal to 2(g−1). Thenf R satisfies the hy-
potheses of Theorem 8.1, which proves the upper boundλ 1(M)≤Lfor every closed
hyperbolic surfaceMof large enough genusg, whereLis such that
p
L−1/4 = 1/R,
the point after which cfR stays non-positive. This gives
L= 1
4 + 1
R2 = 1
4 + π2
(log(g−1) + log(c/2)) 2.
Since log(4.20718/2)>0.7436 and log(g)−log(g−1) tends to zero asg→∞, the inequality
λ1(M)< 1
4 + π2
(log(g) + 0.7436)2
holds for all closed hyperbolic surfaces of sufficiently large genus.□
32 MAXIME FORTIER BOURQUE AND BRAM PETRI
Remark8.7.The choice offin the above proof is not at all random. It is proportional to
the functionψ 1/2(j1/2x) from Section 5. It can be shown that this function is optimal for
the strategy we use. Indeed, the problem amounts to minimizing the growth of bf(Ri/2)
among functions such that
R∞
0
bf(Rx)xtanh(πx)dxis eventually positive (so that equation
(8.4) has any chance of being satisfied). By a change of variable and an application of the
dominated convergence theorem (see the proof of Proposition 9.3 below), we get that a
necessary condition for this eventual positivity is that the second moment
R∞
0
bf(x)x 2dxis
non-negative. Moreover, by the Paley–Wiener theorem, the growth ofbf(Ri/2) is controlled
by the support off. The question thus boils down to minimizing the support offamong
non-negative even functions whose Fourier transform is non-positive outside [−1,1] and
has a non-negative second moment. According to [GIT20, Remark 1.2] (withd=s= 1,
m= 0, andfand bfinterchanged), the optimal function for this problem is the one we
used.
