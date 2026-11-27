---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-025-93-asymptotics
section_title: "Asymptotics"
section_number: 9.3
pages: 36-39
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
start by proving a sublinear bound onm 1 under the assumption thatλ 1 is fairly large. In
the statement below,j α stands for the first positive zero of the Bessel functionJ α. The
k-th positive zero is denotedj α,k.
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 37
Proposition 9.3.For everyp 1,p 2∈(j 0,π], there exists a constantCand someg 0≥2
such that ifg≥g 0 andMis a closed hyperbolic surface of genusgwith
λ1(M)∈
"
1
4 +
 p1
log(g)
2
, 1
4 +
 p2
log(g)
2#
,
thenm 1(M)≤Cg/log(g) 3.
Proof.We start by picking two constantsαandcthat only depend onp 1 andp 2 (and not
ong).
For everyk∈N, thek-th zeroj α,k ofJ α is increasing as a function ofαprovided that
α≥0 [Wat95, p.507]. Together with the interlacing property of the Bessel zeros [Wat95,
p.479], this implies that
j0,2 >j 1,1 >j 1/2,1 =π >j 0,1 =j 0.
In fact, much better numerics are known, namely,j 0≈2.4048 andj 0,2≈5.5201 [DK27].
In particular, we have
p1
p2
> j0
π > j0
j0,2
.
Sincej α,k depends continuously onαfor everyk[Wat95, p.507], there exists someαin
(0,1/2) such that
p1 >j α and p1
p2
> jα
jα,2
.
We then take anyc∈(j α/p1,min{jα,2/p2,1}). This interval is not empty sincej α/p1 <1
andj α/p1 <j α,2/p2.
We setR=clog(g) and apply Theorem 9.1 with the functionfsuch that
bf(x) =ψ α(Rx) = Jα(Rx)2
(Rx)2α(1−R 2x2/j2
α).
The function bfis positive-definite by [GIT20, Remark 1.1] and
µ:= min

−bf(x) :x∈
 p1
log(g), p2
log(g)

= min{−ψ α(y) :y∈[cp 1,cp 2]}
is a positive constant that only depends on our choice of parameters, but not on the genus.
Indeed,ψ α is continuous and strictly negative on (j α,jα,2)⊃[cp 1,cp 2].
By the asymptotic behaviour of Bessel functions along the imaginary axis (5.1), we have
bf(i/2)∼ 1
π
eR
R2α+1(1 +R 2/(4j2
α)) =o
 g
log(g)3

asg→∞.
38 MAXIME FORTIER BOURQUE AND BRAM PETRI
For the integral term, we make a change of variable to find that

Z ∞
0
bf(x)xtanh(πx)dx

 =

Z ∞
0
ψα(Rx)xtanh(πx)dx

=

π
R3
Z ∞
0
ψα(y)y2 tanh(πy/R)
πy/R dy

≤ π
R3
Z ∞
0
|ψα(y)|y2dy
=O
 1
log(g)3

.
Indeed,|ψ α(y)|y2 is integrable by the asymptotic estimate (5.2) sinceα>0.
By Theorem 9.1 applied with the functionf, we obtain
m1(M)≤ 1
µ

bf(i/2)−2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx

=O
 g
log(g)3

if
p
λ1(M)−1/4∈
h
p1
log(g), p2
log(g)
i
and ifgis sufficiently large.□
Remark9.4.It is easy to modify the proof of Theorem 9.1 to bound the total number of
eigenvalues in an interval [a,b] assuming thatλ 1(M)∈[a,b] (see [FBP24, Lemma 3.2]).
This more general version of the criterion implies that under the same hypotheses as above,
the total number of eigenvalues contained in the given interval is bounded by the same
quantityCg/log(g) 3.
See [GLMST21, Corollary 1.7] for a similar result showing that for any compact interval
Icontained in [0,1/4)∪(1/4,∞), the multiplicity of any eigenvalue inIgrows at most
sublinearly with the genusgwith probability tending to 1 asg→∞with respect to the
Weil–Petersson measure. See also [Mon22, Corollary 6]. An upper bound onm 1 of the
formO(g/logg) was recently proved in [LM24] for negatively pinched surfaces with systole
bounded away from zero.
We then combine the sublinear upper bound from Proposition 9.3 with a previous (linear)
upper bound from [FBP24] for slightly smallerλ 1 to obtain a global upper bound onm 1
in large genus.
Theorem 9.5.There exists someg 0≥2such that every closed hyperbolic surfaceMof
genusg≥g 0 satisfies
m1(M)≤2g−1.
Proof.By Theorem 8.3, we can assume that
λ1(M)≤ 1
4 +
 π
log(g) + 0.7436
2
≤ 1
4 +
 π
log(g)
2
.
Now pick anyp∈(j 0,π). Proposition 9.3 implies (a stronger version of) the result if
λ1(M)≥ 1
4 +
 p
log(g)
2
.
It remains to consider the case whereλ 1(M) is smaller than this bound. This case was
already handled in [FBP24, Theorem 1.1], which states thatm 1(M)≤2g−1 whenever
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 39
λ1(M)≤a g, wherea g is the smallest Dirichlet eigenvalue on a hyperbolic disk of area
4π(g−1) and hence of radius 2 arcsinh( √g−1). From Savo’s inequality (8.3), we have
ag− 1
4≥ π2
4 arcsinh(√g−1) 2− π2
2 arcsinh(√g−1) 3∼ π2
log(g)2 asg→∞.
In particular, whengis large enough we have
ag > 1
4 +
 p
log(g)
2
.
As such, all possibilities forλ 1(M) are covered and the inequality is proved.□
Note that the proof relied partly on [FBP24, Theorem 1.1] whose proof is based on the
results of S´ evennec [S´ ev02]. Different methods would be required to prove sublinear upper
bounds.
