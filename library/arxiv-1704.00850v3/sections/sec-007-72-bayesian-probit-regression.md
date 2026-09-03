---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-007-72-bayesian-probit-regression
section_title: "Bayesian probit regression"
section_number: 7.2
pages: 19-23
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
LetY1,Y 2,...,Y n be independent Bernoulli random variables with P(Y1 = 1|β) = Φ(xT
i β), wherexi,β ∈
Rp, and Φ(·) is the cumulative distribution function of the standard normal distribution. Take the prior on
β to be Np(Q−1w,Q−1), wherew∈ Rp andQ is positive deﬁnite. The resulting posterior distribution is
intractable, but Albert and Chib (1993) devised a DA algorithm to sample from it. Letz = (z1,z 2,...,z n)T
be a vector of latent variables, and let X be the design matrix whose ith row is xT
i . The Mtd of the Albert
and Chib (AC) chain,p(β,·),β∈ Rp, is characterized by
πU|V (β|z)∝ exp
[
− 1
2
{
β−
(
XTX +Q
)−1(
w+XTz
)}T(
XTX +Q
){
β−
(
XTX +Q
)−1(
w+XTz
)}]
,
and
πV|U(z|β)∝
n∏
i=1
exp
{
− 1
2
(
zi−xT
i β
)2
}
IR+
(
(yi− 0.5)zi
)
.
The ﬁrst conditional density,πU|V (·|z), is a multivariate normal density, and the second conditional density,
πV|U(·|β), is a product of univariate truncated normal pdfs.
A sandwich step can be added to facilitate the convergence of the AC chain. Chakraborty and Khare
(2017) constructed a Haar PX-DA variant of the chain, which is a sandwich chain with transition density of
the form (6) (see also Roy and Hobert (2007)). The sandwich step s(z,dz′) is equivalent to the following
update:z↦→z′ =gz, where the scalarg is drawn from the following density:
πG(g|z)∝gn−1 exp
[
− 1
2zT{
In−X(XTX +Q)−1XT}
zg 2 +zTX(XTX +Q)−1wg
]
.
19
Note that this pdf is particularly easy to sample from whenw = 0.
Chakraborty and Khare (2017) showed that, for the AC chain,P is trace-class when one uses a concen-
trated prior (corresponding to Q having large eigenvalues). In fact, the following is shown to hold in their
proof.
Proposition 6. Suppose that X is full rank. If all the eigenvalues of Q−1/2XTXQ−1/2 are less than 7/2,
then for any polynomial functiont : Rp→ R,
∫
Rp
|t(β)|p(β,β )dβ <∞.
We will use the estimator (18). The following proposition provides a class ofψ(·)s that lead to estimators
with ﬁnite variance.
Proposition 7. Suppose the hypothesis in Proposition 6 holds. Ifψ(·) is the pdf of ap-variatet-distribution,
i.e.
ψ(β)∝
{
1 + 1
a(β−b)T Σ−1(β−b)
}−(a+p)/2
for someb∈ Rp, positive deﬁnite matrix Σ∈ Rp×p, and positive integera, then the estimator (18) has ﬁnite
variance.
Proof. Note that for everyβ andz
π3
U|V (β|z)≤CπU|V (β|z),
whereC is a constant. Hence, by Proposition 6, for any polynomial functiont : Rp→ R,
∫
Rp
∫
Rn
|t(β)|π3
U|V (β|z)πV|U(z|β)dzdβ ≤C
∫
Rp
|t(β)|p(β,β )dβ <∞.
Since ψ−2(·) is a polynomial function on Rp, the moment condition (20) holds. The result follows from
Corollary 5.
As a numerical illustration, we apply our method to the Markov operator associated with the AC chain
corresponding to the famous “lupus data” of van Dyk and Meng (2001). In this dataset, n = 55 andp = 3.
We will construct an asymptotically valid 95% CI for the second largest eigenvalue, and this appears to be
the most rigorous and detailed analysis to date of the spectrum of a practically relevant MCMC algorithm
on an uncountable state space. As in Chakraborty and Khare (2017), we will let w = 0 andQ = XTX/c,
wherec = 3.499999. It can be easily shown that the assumptions in Proposition 6 are met. Chakraborty
and Khare (2017) compared the AC chain, Φ, and its Haar PX-DA variant, ˜Φ, deﬁned a few paragraphs ago.
This comparison was done using estimated autocorrelations. Their results suggest that ˜Φ outperforms Φ
20
when estimating a certain test function. We go further and estimate the second largest eigenvalue of each
operator.
It can be shown that the posterior pdf,πU(·), is log-concave, and thus possess a unique mode. Letˆβ be the
posterior mode, and ˆΣ the estimated variance of the MLE. We pickψ(·) to be the pdf oft30( ˆβ, (ˆΣ−1+Q)−1).
This is to say, for anyβ∈ Rp,
ψ(β)∝
{
1 + 1
30(β− ˆβ)T (ˆΣ−1 +Q)(β− ˆβ)
}−(p+30)/2
.
By Proposition 7, this choice ofψ(·) guarantees ﬁnite variance. Whenn is large,ψ(·) is expected to resemble
πU(·). The performance of our method seems insensitive to the degrees of freedom of the t-distribution
(which is set at 30 for illustration).
We use a Monte Carlo sample size of N = 4× 105 to form our estimates for the DA operator, and
the results are shown in Table 2. Asymptotic 95% CIs for l5 andu5 are (0.397, 0.545) and (0.573, 0.595),
respectively. Using a Bonferroni argument, we can state that asymptotically, with at least 95% conﬁdence,
λ1∈ (0.397, 0.595).
Table 2: Estimated power sums of eigenvalues for the AC chain
k Est.sk Est.D′/
√
N Est.lk Est.uk
1 6 .744 0 .072 0 .000 5 .744
2 2 .041 0 .007 0 .181 1 .020
3 1 .363 0 .004 0 .349 0 .713
4 1 .156 0 .004 0 .430 0 .628
5 1 .068 0 .003 0 .436 0 .584
We now consider the sandwich chain, ˜Φ. It is known that the Mtd of any Haar PX-DA chain is repre-
sentable (Hobert and Marchev, 2008). Hence, ˜P is indeed a DA operator. Recall that{˜λi}˜κ
i=0, 0≤ ˜κ≤∞ ,
denote the decreasingly ordered positive eigenvalues of ˜P . It was shown in Khare and Hobert (2011) that
˜λi≤λi fori∈ N with at least one strict inequality. For a positive integerk,∑˜κ
i=0 ˜λk
i is denoted by ˜sk. Let
˜uk and ˜lk, be the respective counterparts ofuk andlk. Estimates of ˜sk, k= 1, 2,··· , 5 using 4× 105 Monte
Carlo samples are given in Table 3. Our estimate of ˜s1− 1 is less than half of s1− 1, implying that, in an
average sense, the sandwich version of the AC chain reduces the nontrivial eigenvalues of P by more than
half. Asymptotic 95% CIs for ˜l5 and ˜u5 are (0.321, 0.518) and (0.456, 0.503). Thus, asymptotically, with at
least 95% conﬁdence, ˜λ1∈ (0.321, 0.503). The method does not detect a signiﬁcant difference between λ1
21
Table 3: Estimated power sums of eigenvalues for the Haar PX-DA version of the AC chain
k Est. ˜sk Est.D′/
√
N Est. ˜lk Est. ˜uk
1 3 .796 0 .012 0 .000 1 .796
2 1 .538 0 .004 0 .193 0 .734
3 1 .172 0 .004 0 .319 0 .556
4 1 .060 0 .003 0 .352 0 .496
5 1 .025 0 .003 0 .419 0 .479
●
● ●
●
● ●
●
●
● ●
●
●
0.40
0.45
0.50
0.55
0.60
0.65
0 250 500 750
n
Interval estimates of λ1
●●
●●
Est. lk 
Est. uk
(a) Interval estimates forλ1 for differentns.
●
●
●
●
●
●
●
● ●
●
0.2
0.4
0.6
0.8
4 8 12 16
p
Interval estimates of λ1
●●
●●
Est. lk 
Est. uk (b) Interval estimates forλ1 for differentps.
Figure 2: Spectral gap estimation for the AC chain
and ˜λ1.
We now study the performance of our method when n orp increases for the original AC chain. First,
consider a sequence of datasets wheren grows. LetXlupus∈ R55×3 be the design matrix for the lupus data,
and let r be a positive integer. Set X ∈ Rn×3 to be r copies of Xlupus stacked on top of each other, so
thatn = 55r. The response vector (Y1,Y 2,...,Y n)T is randomly generated in accordance with the probit
regression model with the true value of β being (−3, 0, 3)T . Let r range from 1 to 15. This gives rise to a
sequence of datasets withn growing from 55 to 825. An interval estimate forλ1 is then constructed for each
of these datasets. Throughout the simulation,k is ﬁxed at 5, andN is ﬁxed at 4× 105. The result is given in
Figure 2a. Increasingn, which is the dimension ofSV , apparently does not undermine the method.
Now we consider a sequence of datasets where n is ﬁxed and p grows. Let n = 200 , and let X be a
200×p matrix whoseijth element ispj(i), with{pj(·)}p
j=1 being a set of orthogonal polynomials generated
using the R function poly(). The response vector is randomly generated according to the probit model with
22
the true value ofβ being (−p,−p + 2p/(1−p),−p + 4p/(1−p),··· ,p )T . We apply our method to such
a dataset whenp is increased from 3 to 15. N is set to be 4× 105, andk is either 4 or 5, whichever yields a
better estimate. The interval estimates forλ1 are given in Figure 2b. Asp increases, the length of the interval
estimate grows quite rapidly, indicating that the method does not scale well with p, that is, the dimension
ofSU. This is consistent with the analysis near the end of Section 5, which suggests that Algorithm 2 works
well whenn is large andp is small, but not the other way around.
