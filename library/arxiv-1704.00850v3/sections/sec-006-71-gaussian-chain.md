---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-006-71-gaussian-chain
section_title: "Gaussian chain"
section_number: 7.1
pages: 17-19
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
We begin with a toy example. LetSU =SV = R,πU(u)∝ exp(−u2), and
πV|U(v|u)∝ exp
{
− 4
(
v− u
2
)2}
.
Then
πU|V (u|v)∝ exp{−2(u−v)2}.
This leads to one of the simplest DA chains known. Indeed, the Mtd,
p(u,·) =
∫
R
πU|V (·|v)πV|U(v|u)dv, u∈SU,
can be evaluated in closed form, and turns out to be a normal pdf. The spectrum of the corresponding Markov
operator,P , has been studied thoroughly (see e.g. Diaconis et al., 2008). It is easy to verify that (4) holds,
soP is trace-class. In fact, κ =∞, and for any non-negative integeri,λ i = 1/2i. Thus, the second largest
eigenvalue,λ1, and the spectral gap,δ, are both equal to 1/2. Moreover, for any positive integerk,
sk =
∞∑
i=0
1
2ik = 1
1− 2−k .
We now pretend to be unaware of this spectral information, and use (13) to estimate {sk,lk,uk}4
k=1.
Recall thatlk anduk are lower and upper bounds forλ1, respectively. Note that
∫
R
π3
V|U(v|u)πU|V (u|v)du∝ exp
(
− 6
5v2
)
.
17
● ●
●
●
●
●
●
●
20
40
60
0.5 0.6 0.7 0.8 0.9 1.0
λ
k
(a) Theks used for different values
ofλ.
●
●
●
●
●
●●●
0.6
0.8
1.0
0.5 0.6 0.7 0.8 0.9 1.0
λ
Interval estimates of λ1
● True value
(b) Interval estimates forλ1.
Figure 1: Spectral gap estimation for the Gaussian chain for differentλs
It follows that, if we take ω(v)∝ exp(−v2/2), then (15) holds, and our estimator of sk has ﬁnite variance.
We use a Monte Carlo sample size of N = 1× 105 to form our estimates, and the results are shown in
Table 1.
Table 1: Estimated power sums of eigenvalues for the Gaussian chain
k Est.sk Est.D/
√
N Est.lk Est.uk
1 1 .996 0 .004 0 .000 0 .996
2 1 .331 0 .004 0 .333 0 .575
3 1 .142 0 .004 0 .429 0 .522
4 1 .068 0 .004 0 .482 0 .511
Note that the estimates of the sks are quite good. We then construct 95% conﬁdence intervals (CIs) for
l4 andu4 via the delta method, and the results are (0.442, 0.522) and (0.498, 0.524), respectively.
We now add an additional parameter to our toy example in order to study the effect of a closing spectral
gap on our method. In particular, let πV|U(·|u),u∈ R, be the pdf of N(λu,λ (1−λ)/2), whereλ∈ (0, 1).
Note that our original example corresponds to λ = 1/2. The eigenvalues of the resultant DA operator are
{λi}∞
i=0 ={λi}∞
i=0. We investigate the effectiveness of our method as λ1 = λ goes to 1, that is, as the
spectral gapδ = 1−λ closes. To this end, consider a sequence of Gaussian chains with λ increasing from
0.5 to 0.99. In accordance with the discussion in Section 6, for a givenλ, we setω to be the density function
of a t-distribution with similar variance as πV (·), which is the pdf of N (0,λ/ 2). One can verify that (15)
18
holds for everyλ∈ (0, 1). Note that in order for uk = (sk− 1)1/k to be a non-trivial upper bound on λ1,
we need sk < 2. As λ increases, so does sk for any givenk, and thus one must increase k in order to ﬁnd
a useful upper bound. Figure 1a shows the ks used for differentλs. When λ = 0.5, we only need k = 4 to
get a decent result; but whenλ = 0.99,k≈ 70 is needed. Recall that the time needed to run N iterations of
Algorithm 1 is approximatelykNτ , whereτ is the time needed to simulate one step of the DA chain, which
is roughly the same for any λ∈ (0, 1). To compare the performance of our method for different λs, we ﬁx
kN = 1× 106, and compare the length of the interval estimates of λ1. The results are shown in Figure 1b.
Asλ grows, so doesk, and we are forced to use a smaller sample sizeN. Thus, asλ grows, it becomes more
difﬁcult to estimate the variances ofu∗
k andl∗
k accurately. As a result, the length of the interval estimate ofλ1
becomes less stable when λ is near 1. This is reﬂected in Figure 1b by an unusually wide interval estimate
atλ = 0.97. On the other hand, most of the interval estimates at other values of λ near 1 are reasonably
well-behaved.
