---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-008-73-bayesian-linear-regression-model-with-non-gau
section_title: "Bayesian linear regression model with non-Gaussian errors"
section_number: 7.3
pages: 23-26
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
LetY1,Y 2,...,Y n be independentd-dimensional random vectors from the linear regression model
Yi =βTxi + Σ1/2εi,
wherexi∈ Rp is known, whileβ∈ Rp×d and thed×d positive deﬁnite matrix Σ are to be estimated. The
iid errors,ε1,ε 2,...,ε n, are assumed to have a pdf that is a scale mixture of Gaussian densities:
fh(ε) =
∫
R+
ud/2
(2π)d/2 exp
(
− u
2εTε
)
h(u)du,
whereh(·) is a pdf with positive support, andR+ := (0,∞). For instance, ifd = 1 andh(u)∝u−2e−1/(8u),
thenε1 has pdf proportional toe−|ε|/2.
To perform a Bayesian analysis, we require a prior on the unknown parameter, (β, Σ). We adopt the
(improper) Jeffreys prior, given by 1/|Σ|(d+1)/2. Let y represent the n×d matrix whose ith row is the
observed value of Yi. The following four conditions, which are sufﬁcient for the resulting posterior to be
proper (Qin and Hobert, 2018; Fernandez and Steel, 1999), will be assumed to hold:
1. n≥p +d,
2. (X :y) is full rank, whereX is then×p matrix whoseith row isxT
i ,
3.
∫
R+
ud/2h(u)du< ∞, and
4.
∫
R+
u−(n−p−d)/2h(u)du< ∞.
The posterior density is highly intractable, but there is a well-known DA algorithm to sample from it (Liu,
1996). Under our framework, the DA chain Φ is characterized by the Mtd
p
(
(β, Σ), (·,·)
)
=
∫
Rn
+
πU|V (·,·|z)πV|U(z|β, Σ)dz,
23
wherez = (z1,z 2,...,z n)T ,
πU|V (β, Σ|z)∝| Σ|−(n+d+1)/2
n∏
i=1
exp
{
− zi
2
(
yi−βTxi
)T Σ−1(
yi−βTxi
)}
, and
πV|U(z|β, Σ)∝
n∏
i=1
zd/2
i exp
{
− zi
2
(
yi−βTxi
)T Σ−1(
yi−βTxi
)}
h(zi).
The ﬁrst conditional density,πU|V (·,·|z), characterizes a multivariate normal distribution on top of an inverse
Wishart distribution, i.e. β|Σ,z is multivariate normal, and Σ|z is inverse Wishart. The second conditional
density,πV|U(·|β, Σ), is a product of n univariate densities. Moreover, when h(·) is a standard pdf on R+,
these univariate densities are often members of a standard parametric family. The following proposition
about the resulting DA operator is proved in Qin and Hobert (2018).
Proposition 8. Supposeh(·) is strictly positive in a neighborhood of the origin. If there exists ξ∈ (1, 2)
andδ >0 such that ∫ δ
0
ud/2h(u)∫ξu
0 vd/2h(v)dv
du< ∞,
thenP is trace-class.
When P is trace-class, we can pick an ω(·) and try to make use of (13). A sufﬁcient condition for
the estimator’s variance,D2, to be ﬁnite is stated in the following proposition, whose proof is given in the
appendix.
Proposition 9. Suppose thath(·) is strictly positive in a neighborhood of the origin. If ω(z) can be written
as∏n
i=1ωi(zi), and there existsξ∈ (1, 4/3) such that for alli∈{ 1, 2,...,n },
∫
R+
u3d/2h3(u)
(
∫ξu
0 vd/2h(v)dv)3ω2
i (u)
du< ∞, (21)
then (15) holds, and thus by Theorem 4, the estimator (13) has ﬁnite variance.
For illustration, taked = 1 andh(u)∝u−2e−1/(8u). Thenε1 follows a scaled Laplace distribution, and
the model can be viewed as a median regression model with varianceΣ unknown. It’s easy to show thath(·)
satisﬁes the assumptions in Proposition 8, so the resultant DA operator is trace-class. Now let
ω(z) =
n∏
i=1
ωi(zi)∝
n∏
i=1
z−3/2
i e−1/(32zi).
The following result shows that this will lead to an estimator with ﬁnite variance.
Corollary 10. Supposed = 1,h(u)∝u−2e−1/(8u), and
ω(z) =
n∏
i=1
ωi(zi)∝
n∏
i=1
z−α−1
i e−γ/zi,
where 0<α< 3/4 and 0<γ < 3/64. Then the variance,D2, is ﬁnite.
24
●
● ●
●
●
●
● ●
●
●
0.4
0.6
0.8
4 8 12 16 20
n
Interval estimates of λ1
●●
●●
Est. lk 
Est. uk
(a) Interval estimates forλ1 for differentns.
●
●
● ●
●
●
●
●
●
●
0.2
0.3
0.4
0.5
0.6
0.7
2 4 6 8
p
Interval estimates of λ1
●●
●●
Est. lk 
Est. uk (b) Interval estimates forλ1 for differentps.
Figure 3: Spectral gap estimation for the DA chain for Bayesian linear model
Proof. In light of Proposition 9, we only need to show that (21) holds for someξ∈ (1, 4/3). For anyξ >0,
making use of the fact that (by monotone convergence theorem)
lim
u→∞
∫ ξu
0
v1/2h(v)dv =
∫
R+
u1/2h(u)du> 0,
one can easily show for anyδ >0,
∫ ∞
δ
u3/2h3(u)
(
∫ξu
0 v1/2h(v)dv)3ω2
i (u)
du =
∫ ∞
δ
u2α−5/2 exp{2γ/u− 3/(8u)}
(
∫ξu
0 v1/2h(v)dv)3
du< ∞. (22)
On the other hand, using L’Hˆopital’s rule, we can see for(1− 16γ/3)−1<ξ < 4/3,
lim
u→0
(
u3/2h3(u)
(
∫ξu
0 v1/2h(v)dv)3ω2
i (u)
)1/3
= lim
u→0
u2α/3−5/6 exp{2γ/(3u)− 1/(8u)}∫ξu
0 v−3/2e−1/(8v)dv
= lim
u→0
R(u) exp
{
−
(
− 2γ
3 − 1
8ξ + 1
8
) 1
u
}
= 0,
where R(u) is a function that is either bounded near the origin or goes to ∞ at the rate of some power
function asu→ 0. It follows that forξ∈ ((1− 16γ/3)−1, 4/3) and small enoughδ,
∫ δ
0
u3/2h3(u)
(
∫ξu
0 v1/2h(v)dv)3ω2
i (u)
du< ∞. (23)
Combining (22) and (23) yields (21). The result then follows.
We now test the effectiveness of the Monte Carlo estimator (13) on a sequence of growing datasets
with d = 1 . Let p = 3 , and let X be an n×p design matrix with 3 distinct rows, (1, 0, 0)T , (0, 1, 0)T ,
and (0, 0, 1)T , each replicated r times, so that n = 3r. The responses, Y1,Y 2,··· ,Yn, are then generated
25
according to the previously deﬁned linear regression model with the true value of β being (−3, 0, 3)T , and
the true value of Σ being 1. In other words, Yi−xT
i (−3, 0, 3)T ∼ fh(·) independently for each i, where
fh(u)∝ e−|u|/2. The resultant DA chain Φ lives in SU = R3× R+, and SV = Rn = R3r. Let r grow
from 2 to 6. We use a Monte Carlo sample size ofN = 2× 106 to form interval estimates ofλ1 for different
values of r. For simplicity, we ﬁx k to be 4. The results are given in Figure 3a. As n grows, the length
of the interval estimate increases quite rapidly. This is understandable, since our method is essentially an
importance sampling technique, which does not work well in high dimensional settings unless tuned with
great care. In the previous subsection where we study Bayesian probit regression, we are able to easily deal
with a dataset withn> 800. Part of the reason is that, in that case, Algorithm 2 is used, and sinceSU is low
dimensional, it’s easy to chooseψ(·) that resemblesπU(·).
Consider another sequence of datasets where d = 1,n = 10, and p is increased from 1 to 8. The ijth
element of the design matrixX is set to bepj(i), where{pj(·)}p
j=1 are orthogonal polynomials generated in
R. The responses are generated according to the aforementioned linear regression model with the true value
ofβ being (−p,p + 2p/(1−p),−p + 4p/(1−p),...,p )T , and the true value of Σ being 1. In this case,
SU = Rp× R+, andSV = R10. Using a Monte Carlo sample size of N = 2× 106 and settingk = 4, we
obtain interval estimates ofλ1 for differentps. The results are given in Figure 3b. Compare this to the case
wherep is ﬁxed ann grows. We see that the effectiveness of Algorithm 1, characterized by the length of the
interval estimate it produces, is much less susceptible to the growing dimension ofSU than to that ofSV .
Acknowledgment. The second and third authors were supported by NSF Grant DMS-15-11945.
Appendix
