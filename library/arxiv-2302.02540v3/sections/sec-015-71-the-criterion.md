---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-015-71-the-criterion
section_title: "The criterion"
section_number: 7.1
pages: 19-21
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
of oriented closed geodesics of minimal length. In the literature it is common to consider
the quantity 1
2 kiss(M), which counts the number of unoriented systoles inM. Our criterion
for bounding kissing numbers is the same as the one we used in [FBP22] for hyperbolic
manifolds in any dimension. We repeat the proof in the surface case for convenience.
Theorem 7.1.Lets>0and suppose thatfis an admissible function such that
• bf(ξ)≥0for everyξ∈R∪i

− 1
2, 1
2

;
•f(x)≤0wheneverx≥sandf(s)<0.
Then for every closed hyperbolic surfaceMof genusg≥2such thatsys(M) =swe have
kiss(M)≤4
√
2π(g−1) sinh(s/2)
s|f(s)|
Z ∞
0
bf(x)xtanh(πx)dx.
Proof.We have
0≤
∞X
j=0
bf
 r
λj(M)− 1
4
!
= 2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx+ 1√
2π
X
γ∈C(M)
Λ(γ)
2 sinh(ℓ(γ)/2)f(ℓ(γ))
≤2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx+ kiss(M)√
2π
sys(M)
2 sinh(sys(M)/2)f(sys(M))
since the contribution of geodesics longer than the systole is non-positive. Rearranging
gives the desired result.□
Remark7.2.We could take the value of bf(
p
−1/4) = bf(i/2) into account to get an a priori
better bound, but in practice we have found that the optimal functions seem to satisfy
bf(i/2) = 0. We therefore enforce this condition in our program to speed up convergence.
Definition 7.3.Fors>0, we defineK(s) as the infimum of
4
√
2π sinh(s/2)
s|f(s)|
Z ∞
0
bf(x)xtanh(πx)dx
over the functionsfthat satisfy the hypotheses of Theorem 7.1.
20 MAXIME FORTIER BOURQUE AND BRAM PETRI
Theorem 7.1 can then be restated as saying that
kiss(M)≤K(sys(M))(g−1).
The following monotonicity result will greatly simplify our task of finding a global bound
(independent of the systole) in each genus.
Lemma 7.4.The functionK(s)is non-decreasing fors∈[6,∞).
Proof.Letfbe a function that satisfies the hypotheses of Theorem 7.1 at somes 2 >6
and lets 1∈[6,s 2). We then consider the functionϕ(x) =f

s2
s1
x

withbϕ(x) = s1
s2
bf

s1
s2
x

.
By the hypotheses onfwe have thatϕ(x) =f

s2
s1
x

≤0 wheneverx≥s 1, because that
implies s2
s1
x≥s 2. Moreover, we haveϕ(s 1) =f(s 2)<0. Secondly, ifξ∈R∪i

− 1
2, 1
2

,
then s1
s2
ξ∈R∪i
h
− 1
2
s1
s2
, 1
2
s1
s2
i
⊂R∪i

− 1
2, 1
2

so that bϕ(ξ) = s1
s2
bf

s1
s2
ξ

≥0.
It remains to estimate the resulting bounds onK. We compute
sinh(s1/2)
s1
Z ∞
0
bϕ(x)xtanh(πx)dx= sinh(s1/2)
s1
s1
s2
Z ∞
0
bf
s1
s2
x

xtanh(πx)dx
= sinh(s1/2)s2
s2
1
Z ∞
0
bf(y)ytanh
s2
s1
πy

dy
≤ sinh(s1/2)s2
2
s3
1
Z ∞
0
bf(y)ytanh (πy)dy.
We then claim that
sinh(s1/2)s2
2
s3
1
≤ sinh(s2/2)
s2
.
Indeed, this is equivalent to saying that sinh(x/2)/x3 increases froms 1 tos 2 and elementary
computations show that the derivative of this function is non-negative provided thatxis
at least 6 tanh(x/2), which is certainly true ifx≥6.
We conclude that
sinh(s1/2)
s1|ϕ(s1)|
Z ∞
0
bϕ(x)xtanh(πx)dx≤ sinh(s2/2)
s2|f(s 2)|
Z ∞
0
bf(y)ytanh (πy)dy
and hence thatK(s 1)≤K(s 2) upon taking the infimum overf.□
When the systole is sufficiently small, any two shortest closed geodesics are disjoint,
which implies a bound on the kissing number for topological reasons. More precisely, by
the collar lemma [Bus10, Theorem 4.1.6], if sys(M)≤2 arcsinh(1), then kiss(M)≤6(g−1)
(and this is optimal).
In order to obtain a global upper bound on the kissing number in a given genusgfrom
Theorem 7.1, it remains to prove an upper bound forK(s) whens∈[2 arcsinh(1),6] and
ats= sys bound(g) where sys bound(g) is the bound on the systole in genusgcoming
from the previous section. This is if sys bound(g)>6, which happens as soon asg≥7.
In lower genus, we only have to boundK(s) forsin [2 arcsinh(1),sys bound(g)].
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 21
