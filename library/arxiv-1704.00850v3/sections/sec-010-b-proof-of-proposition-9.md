---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-010-b-proof-of-proposition-9
section_title: "B Proof of Proposition 9"
section_number: null
pages: 30-34
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
Proposition 9. Suppose thath(·) is strictly positive in a neighborhood of the origin. Ifω(z) can be written
as∏n
i=1ωi(zi), and there existsξ∈ (1, 4/3) such that for alli∈{ 1, 2,...,n },
∫
R+
u3d/2h3(u)
(
∫ξu
0 vd/2h(v)dv)3ω2
i (u)
du< ∞,
then (15) holds, and thus by Theorem 4, second moment exists for the estimator (13).
30
Proof. Let Sd be the set of d×d positive deﬁnite matrices. For any β ∈ Rp, Σ ∈ Sd, z∈ Rn, and
ξ∈ (1, 4/3),
πU|V (β, Σ|z)π3
V|U(z|β, Σ)
= |Σ|−(n+d+1)/2∏n
i=1 exp{−zi(yi−βTxi)T Σ−1(yi−βTxi)/2}∫
Rp
∫
Sd
|˜Σ|−(n+d+1)/2∏n
i=1 exp{−zi(yi− ˜βTxi)T ˜Σ−1(yi− ˜βTxi)/2}d˜Σd ˜β
×
n∏
i=1
z3d/2
i exp{−3zi(yi−βTxi)T Σ−1(yi−βTxi)/2}h3(zi)
{
∫∞
0 vd/2 exp[−v(yi−βTxi)T Σ−1(yi−βTxi)/2]h(v)dv}3
≤ |Σ|−(n+d+1)/2∏n
i=1 exp{−zi(yi−βTxi)T [Σ/(4− 3ξ)]−1(yi−βTxi)/2}∫
Rp
∫
Sd
|˜Σ|−(n+d+1)/2∏n
i=1 exp{−zi(yi− ˜βTxi)T ˜Σ−1(yi− ˜βTxi)/2}d˜Σd ˜β
×
n∏
i=1
z3d/2
i h3(zi)
(
∫ξzi
0 vd/2h(v)dv)3
.
Note that
∫
Sd
|Σ|−(n+d+1)/2
n∏
i=1
exp
{
− zi
2
(
yi−βTxi
)T
( Σ
4− 3ξ
)−1(
yi−βTxi
)}
dΣ
= (4− 3ξ)−nd/2
∫
Sd
|Σ|−(n+d+1)/2
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
dΣ.
Thus, ∫
Rp
∫
Sd
πU|V (β, Σ|z)π3
V|U(z|β, Σ)dΣdβ≤ (4− 3ξ)−nd/2
n∏
i=1
z3d/2
i h3(zi)
(
∫ξzi
0 vd/2h(v)dv)3
.
The result follows immediately.
References
AHUES , M., L ARGILLIER , A. and L IMAYE , B. (2001). Spectral Computations for Bounded Operators .
CRC Press.
ALBERT , J. H. and C HIB , S. (1993). Bayesian analysis of binary and polychotomous response data.Journal
of the American statistical Association 88 669–679.
BILLINGSLEY , P. (1995). Probability and Measure. 3rd ed. John Wiley & Sons.
BRISLAWN , C. (1988). Kernels of trace class operators. Proceedings of the American Mathematical Society
104 1181–1190.
CHAKRABORTY , S. and K HARE , K. (2017). Convergence properties of Gibbs samplers for Bayesian probit
regression with proper priors. Electronic Journal of Statistics 11 177–210.
31
CHAKRABORTY , S. and K HARE , K. (2019+). Consistent estimation of the spectrum of trace class data
augmentation algorithms. Bernoulli, to appear .
CHAN , K. S. and G EYER , C. J. (1994). Discussion: Markov chains for exploring posterior distributions.
Annals of Statistics 22 1747–1758.
CHOI , H. M. and R OM ´AN, J. C. (2017). Analysis of Polya-Gamma Gibbs sampler for Bayesian logistic
analysis of variance. Electronic Journal of Statistics 11 326–337.
CONWAY, J. B. (1990). A Course in Functional Analysis. 2nd ed. Springer-Verlag.
CONWAY, J. B. (2000). A Course in Operator Theory. American Mathematical Soc.
DIACONIS , P., K HARE , K. and S ALOFF -COSTE , L. (2008). Gibbs sampling, exponential families and
orthogonal polynomials (with discussion). Statistical Science 23 151–200.
DIACONIS , P. and S TROOCK , D. (1991). Geometric bounds for eigenvalues of Markov chains. Annals of
Applied Probability 1 36–61.
ERD ¨OS, J. (1974). On the trace of a trace class operator. Bulletin of the London Mathematical Society 6
47–50.
FERNANDEZ , C. and S TEEL , M. F. (1999). Multivariate student-t regression models: Pitfalls and inference.
Biometrika 86 153–167.
GARREN , S. T. and S MITH , R. L. (2000). Estimating the second largest eigenvalue of a Markov transition
matrix. Bernoulli 6 215–242.
GOHBERG , I., G OLDBERG , S. and K RUPNIK , N. (2012). Traces and Determinants of Linear Operators ,
vol. 116. Birkh ¨auser.
HELMBERG , G. (2014). Introduction to Spectral Theory in Hilbert Space. Elsevier.
HOBERT , J. P. (2011). The data augmentation algorithm: Theory and methodology. In Handbook of Markov
Chain Monte Carlo (S. Brooks, A. Gelman, G. Jones and X.-L. Meng, eds.). Chapman & Hall/CRC Press.
HOBERT , J. P. and M ARCHEV , D. (2008). A theoretical comparison of the data augmentation, marginal
augmentation and PX-DA algorithms. Annals of Statistics 36 532–554.
KHARE , K. and H OBERT , J. P. (2011). A spectral analytic comparison of trace-class data augmentation
algorithms and their sandwich variants. Annals of Statistics 39 2585–2606.
32
KOLTCHINSKII , V. and G IN ´E, E. (2000). Random matrix approximation of spectra of integral operators.
Bernoulli 6 113–167.
KONTOYIANNIS , I. and M EYN , S. P. (2012). Geometric ergodicity and the spectral gap of non-reversible
Markov chains. Probability Theory and Related Fields 154 327–339.
LAWLER , G. F. and S OKAL , A. D. (1988). Bounds on the l2 spectrum for Markov chains and Markov
processes: A generalization of Cheegers inequality. Transactions of the American Mathematical Society
309 557–580.
LIU, C. (1996). Bayesian robust multivariate linear regression with incomplete data.Journal of the American
Statistical Association 91 1219–1227.
LIU, J. S., W ONG , W. H. and K ONG , A. (1994). Covariance structure of the Gibbs sampler with applica-
tions to the comparisons of estimators and augmentation schemes. Biometrika 81 27–40.
LIU, J. S. and W U, Y. N. (1999). Parameter expansion for data augmentation. Journal of the American
Statistical Association 94 1264–1274.
MIRA , A. and G EYER , C. J. (1999). Ordering Monte Carlo Markov chains. Technical Report 632, School
of Statistics, University of Minnesota. .
PAL, S., K HARE , K. and H OBERT , J. P. (2017). Trace class Markov chains for Bayesian inference with
generalized double Pareto shrinkage priors. Scandinavian Journal of Statistics 44 307–323.
QIN, Q. and H OBERT , J. P. (2018). Trace-class Monte Carlo Markov chains for Bayesian multivariate linear
regression with non-Gaussian errors. Journal of Multivariate Analysis 166 335 – 345.
ROBERTS , G. O. and R OSENTHAL , J. S. (1997). Geometric ergodicity and hybrid Markov chains. Elec-
tronic Communications in Probability 2 13–25.
ROY, V. and H OBERT , J. P. (2007). Convergence rates and asymptotic standard errors for Markov chain
Monte Carlo algorithms for Bayesian probit regression. Journal of the Royal Statistical Society: Series B
(Statistical Methodology) 69 607–623.
SINCLAIR , A. and J ERRUM , M. (1989). Approximate counting, uniform generation and rapidly mixing
Markov chains. Information and Computation 82 93–133.
TANNER , M. A. and W ONG , W. H. (1987). The calculation of posterior distributions by data augmentation
(with discussion). Journal of the American statistical Association 82 528–540.
33
VAN DYK, D. A. and M ENG , X.-L. (2001). The art of data augmentation (with discussion). Journal of
Computational and Graphical Statistics 10 1–50.
ZHANG , L., K HARE , K. and X ING , Z. (2019). Trace class Markov chains for the Normal-Gamma Bayesian
shrinkage model. Electronic Journal of Statistics 13 166–207.
34
