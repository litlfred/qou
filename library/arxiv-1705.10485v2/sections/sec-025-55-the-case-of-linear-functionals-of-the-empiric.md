---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-025-55-the-case-of-linear-functionals-of-the-empiric
section_title: "The case of linear functionals of the empirical measure"
section_number: 5.5
pages: 49-53
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
As a particular case of Theorem 55, one recovers the central limit theorem for linear functionals of
empirical measures of Markov chains, that are random variables
Yn = Sn −E[Sn]
√n
=
1
√n
n
X
t=1
(f(Xt) −π(f))
with f : X →R ﬁxed function (independent of the time t). Thus, assuming for instance limn→∞Var(Yn) =
Σ2(f) > 0, we have
dKol
 
Sn −E[Sn]
p
Var(Sn)
, NR(0, 1)
!
≤77
 
∥f∥∞
√
M
Σ(f)
!3 1 + θP
1 −θP
2
1
√n
(13)
50
Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
for n large enough. We refer to [Cog72, KV86, Jon04, Häg05] and the references therein for the general
background of this Markovian CLT, and to [Bol80, Lez96, Man96] for estimates of the Kolmogorov
distance. It seems that we recover some results of [Man96] (see [SC97, §2.1.3]), but we were not able to
ﬁnd and read this paper. In this last paragraph, we discuss the problem of the variance Var(Yn), giving
suﬃcient conditions, which are simple to check on examples and ensure Σ2(f) > 0. We also remark that,
provided that Σ2(f) > 0, we can also prove complex mod-Gaussian convergence, which implies a zone of
normality result and moderate deviation estimates by [FMN16].
Denote g = f −π(f), which has expectation 0 under the stationary measure π. By eventually replacing
f with g, we can assume that f is centered. The variance of Yn tends to
Σ2(f) = E[(f(X0))2] + 2
∞
X
t=1
E[f(X0) f(Xt)] < +∞,
see [Cog72, Lemma 3.3]. If Σ2(f) > 0, then Var(Sn)
n2/3
= n1/3 Var(Yn) →+∞and Theorem 55 applies.
Unfortunately, one can easily construct non-trivial examples with Σ2(f) = 0. Thus, consider the Markov
chain with 3 states and transition matrix
P =


0
1
0
1/2 0 1/2
1
0
0

;
it admits for invariant measure π(1) = π(2) = 2
5 and π(3) = 1
5. Set f(1) = 1, f(2) = −1 and f(3) = 0;
one has π(f) = 0, and one computes
E[f(X0)f(Xk)] = 1
5

2 + i
(−1 −i)k +
2 −i
(−1 + i)k

.
It follows that Σ2(f) = 0, although f is non zero.
In the general case of an ergodic Markov chain, ﬁx an element a of the state space X, and denote
τa ≥1 the ﬁrst hitting time of a by the Markov chain, which is almost surely ﬁnite and with expectation
1/π(a) when starting from a. Then, the asymptotic variance Σ2(f) can be rewritten as
Σ2(f) = π(a) Ea


 τa
X
k=1
g(Xk)
!2
,
see [KS76, Chapter 4]. Therefore, a general condition in order to obtain the bound of Eq. (13) is:
Proposition 58. We have Σ2(f) > 0 if and only if there exists a cycle (x1, . . . , xn) in the graph of
transitions of the Markov chain such that the sum Pn
i=1 g(xi) of the values of g = f −π(f) along this
cycle is non-zero. In this case, the bound (13) holds.
The proposition explains readily why the irreducible aperiodic Markov chain
1
2
3
1
1/2
1/2
1
previously studied gives asymptotic variance 0 to the function f(1) = 1, f(2) = −1 and f(3) = 0: the
minimal cycles of the chains are (1, 2) and (1, 2, 3), and the sum of the values of f along these cycles is
always 0.
Mod-φ convergence, II: Estimates on the speed of convergence
51
Another simple criterion to apply Theorem 55 to linear functionals of the empirical measure is:
Proposition 59. Suppose that the ergodic Markov chain is reversible:
π(x) P(x, y) = π(y) P(y, x)
for any x, y. Then, if f is a non-constant function, Σ2(f) > 0 and the bound (13) holds.
Proof. To say that P is reversible is equivalent to the fact that P is a symmetric operator of the Hilbert
space L2( 1
π). In particular, P has only real eigenvalues. Besides, the restriction of the operator I +
2 P∞
k=1 P k to the space of functions f with π(f) = 0 is well deﬁned, and it is an auto-adjoint operator
on this space with eigenvalues
1 + λ2
1 −λ2
, . . . , 1 + λM
1 −λM
,
where λ2 ≥λ3 ≥· · · ≥λM are the real eigenvalues of P diﬀerent from 1. The quantities above are all
positive, and larger than 1−θP
1+θP (this value being obtained if λM = −θP ). Therefore,
Σ2(f) =
*
f

 
I + 2
∞
X
k=1
P k
!
f
+
L2(π)
≥1 −θP
1 + θP
π(f 2) > 0.
We then obtain
dKol
 
Sn −E[Sn]
p
Var(Sn)
, NR(0, 1)
!
≤77
 
∥g∥∞
√
M
p
π(g2)
!3 1 + θP
1 −θP
7
2
1
√n
for n large enough.
⊓⊔
Remark 60. In this remark, we discuss mod-Gaussian convergence for linear statistics of Markov chains.
We use the above notation and assume that Σ2(f) > 0. Consider the third cumulant of Sn. One can
easily prove that
ρ = 1
n lim
n→∞κ3(Sn) =
X
j,k∈Z
κ(f(X0, Xj, Xk)),
where (Xt)t∈Z is a bi-inﬁnite stationary Markov chain with transition matrix P. (The sum on the right-
hand side is ﬁnite, as consequence of Proposition 54). Let us call ρ this limit. We then consider the
rescaled random variables
Xn =
 Sn −E[Sn]
(Var(Sn))1/3

n∈N
.
As for the magnetization in the Ising model, from [FMN16, Section 5] (with αn = Var(Sn) and βn = 1),
we know that Xn converges in the mod-Gaussian sense with parameters tn = (Var(Sn))1/3 and limit
ψ(z) = exp( Lz3
6 ), with L =
ρ
Σ3(f). Again, this mod-Gaussian convergence takes place on the whole
complex plane and implies a normality zone for Sn/
p
Var(Sn) of size o(n1/6), see Proposition 4.4.1 in loc.
cit.; we also have moderate deviation estimates at the edge of this normality zone, see Proposition 5.2.1.
This mod-Gaussian convergence could also have been proved by using an argument of the perturbation
theory of linear operators, for which we refer to [Kat80]. Indeed, the Laplace transform of Xn writes
explicitly as
E[ezXn] = π (Pz,f)n 1,
where 1 is the column vector with all its entries equal to 1, π is the stationary measure of the process,
and Pz,f is the inﬁnitesimal modiﬁcation of the transition matrix deﬁned by
Pz,f(i, j) = P(i, j) e
z(f(j)−π(f))
(Var(Sn))1/3 .
For z in a zone of control of size O(n1/3), one can give a series expansion of the eigenvalues and eigenvectors
of Pz,f, which allows one to recover the mod-Gaussian convergence. The theory of cumulants and weighted
dependency graphs allows one to bypass these diﬃcult analytic arguments.
52
Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
References
[AHLV15] O. Arizmendi, T. Hasebe, F. Lehner, and C. Vargas. Relations between cumulants in noncommutative proba-
bility. Adv. Math., 282:56 – 92, 2015.
[AS08]
N. Alon and J. Spencer.
The probabilistic method.
Wiley-Interscience Series in Discrete Mathematics and
Optimization. Wiley, 2008. 3rd edn.
[Ber41]
A. C. Berry. The accuracy of the Gaussian approximation to the sum of independent variates. Trans. Amer.
Math. Soc., 49(1):122–136, 1941.
[BHNY08] P. Bourgade, C. Hughes, A. Nikeghbali, and M. Yor. The characteristic polynomial of a random unitary matrix:
a probabilistic approach. Duke Math. J., 145:45–69, 2008.
[Bil95]
P. Billingsley. Probability and Measure. Wiley Series in Probability and Mathematical Statistics. Wiley, 3rd
edition, 1995.
[BKN09]
A. D. Barbour, E. Kowalski, and A. Nikeghbali. Mod-discrete expansions. Probab. Th. Rel. Fields, 158(3):859–
893, 2009.
[BKR89]
A. D. Barbour, M. Karonśki, and A. Rucinśki. A central limit theorem for decomposable random variables with
applications to random graphs. J. Combin. Theory Ser. B, 47(2):125–145, 1989.
[Bol80]
E. Bolthausen. The Berry–Esseen theorem for functionals of discrete Markov chains. Z. Wahr. verw. Geb.,
54:59–73, 1980.
[Bón10]
M. Bóna. On three diﬀerent notions of monotone subsequences. In Permutation Patterns, volume 376 of London
Math. Soc. Lecture Note Series, pages 89–113. Cambridge University Press, 2010.
[BR89]
P. Baldi and Y. Rinott.
On normal approximations of distributions in terms of dependency graphs.
Ann.
Probab., 17(4):1646–1650, 1989.
[Bul96]
A. V. Bulinskii. Rate of convergence in the central limit theorem for ﬁelds of associated random variables. Th.
Prob. Appl., 40(1):136–144, 1996.
[CDMN15] R. Chhaibi, F. Delbaen, P.-L. Méliot, and A. Nikeghbali.
Mod-φ convergence: Approximation of discrete
measures and harmonic analysis on the torus. arXiv:1511.03922, 2015.
[Cog72]
R. Cogburn. The central limit theorem for Markov processes. In Proceedings of the Sixth Annual Berkeley
Symposium on Mathematical Statistics and Probability, volume 2, pages 485–512. University of California Press,
1972.
[DIS73]
M. Duneau, D. Iagolnitzer, and B. Souillard. Decrease properties of truncated correlation functions and analyt-
icity properties for classical lattices and continuous systems. Comm. Math. Phys., 31(3):191–208, 1973.
[DIS74]
M. Duneau, D. Iagolnitzer, and B. Souillard. Strong cluster properties for classical systems with ﬁnite range
interaction. Comm. Math. Phys., 35:307–320, 1974.
[DKN15]
F. Delbaen, E. Kowalski, and A. Nikeghbali. Mod-φ convergence. Intern. Math. Res. Not., 2015(11):3445–3485,
2015.
[DS91]
P. Diaconis and D. Stroock. Geometric bounds for eigenvalues of Markov chains. Ann. Appl. Probab., 1(1):36–61,
91.
[Ell85]
R. Ellis. Entropy, Large Deviations, and Statistical Mechanics. Springer, 1985.
[Fel71]
W. Feller. An Introduction to Probability Theory and Its Applications, Volume II. Wiley Series in Probability
and Mathematical Statistics. Wiley, 2nd edition, 1971.
[Fér16]
V. Féray. Weighted dependency graphs. arXiv preprint 1605.03836, 2016.
[Fil91]
J. A. Fill. Eigenvalue bounds on convergence to stationarity for nonreversible Markov chains, with an application
to the exclusion process. Ann. Appl. Probab., 1(1):62–87, 1991.
[FMN16]
V. Féray, P.-L. Méliot, and A. Nikeghbali. Mod-φ convergence: Normality zones and precise deviations. Springer-
Briefs in Probability and Mathematical Statistics. Springer, 2016.
[FV16]
S. Friedli and Y. Velenik.
Statistical Mechanics of Lattice Systems: a Concrete Mathematical Introduction.
Cambridge University press, 2016. In press.
[Gri92]
G. Grimmett. Weak convergence using higher-order cumulants. J. Theoretical Probability, 5(4):767–773, 1992.
[GW16]
L. Goldstein and N. Wiroonsri. Stein’s method for positively associated random variables with applications to
Ising, percolation and voter models. preprint arXiv:1603.05322, to appear in Ann. Inst. Henri Poincaré, 2016.
[Häg05]
O. Häggström. On the central limit theorem for geometrically ergodic Markov chains. Probab. Th. Rel. Fields,
132:74–82, 2005.
[Jan88]
S. Janson.
Normal convergence by higher semi-invariants with applications to sums of dependent random
variables and random graphs. Ann. Probab., 16:305–312, 1988.
[JKN11]
J. Jacod, E. Kowalski, and A. Nikeghbali. Mod-Gaussian convergence: new limit theorems in probability and
number theory. Forum Mathematicum, 23(4):835–873, 2011.
[Jon04]
G. L. Jones. On the Markov chain central limit theorem. Probability Surveys, 1:299–320, 2004.
[Kat80]
T. Kato. Perturbation Theory for Linear Operators. Classics in Mathematics. Springer-Verlag, 2nd edition,
1980.
[KN10]
E. Kowalski and A. Nikeghbali. Mod-Poisson convergence in probability and number theory. Internat. Math.
Res. Not., 18:3549–3587, 2010.
[KN12]
E. Kowalski and A. Nikeghbali. Mod-Gaussian distribution and the value distribution of ζ( 1
2 + it) and related
quantities. J. London Math. Soc., 86(2):291–319, 2012.
[KRT15]
K. Krokowski, A. Reichenbachs, and C. Thäle.
Discrete Malliavin–Stein method: Berry–Esseen bounds for
random graphs, point processes and percolation. arXiv:1503.01029v1 [math.PR], 2015.
Mod-φ convergence, II: Estimates on the speed of convergence
53
[KS76]
J. G. Kemeny and J. L. Snell. Finite Markov Chains. Undergraduate Texts in Mathematics. Springer-Verlag,
1976.
[KS00]
J. P. Keating and N. C. Snaith. Random matrix theory and ζ( 1
2 + it). Comm. Math. Phys., 214(1):57–89, 2000.
[KS10]
V. Y. Korolev and I. G. Shevtsova. On the upper bound for the absolute constant in the Berry–Esseen inequality.
Theory of Probability and its Applications, 54(4):638–658, 2010.
[KV86]
C. Kipnis and S. R. S. Varadhan. Central limit theorem for additive functionals of reversible Markov processes
and applications to simple exclusions. Communications in Mathematical Physics, 104:1–19, 1986.
[Lan93]
S. Lang. Real and Functional Analysis, volume 142 of Graduate Texts in Mathematics. Springer-Verlag, 3rd
edition, 1993.
[Lez96]
P. Lezaud. Chernoﬀ-type bound for ﬁnite Markov chains. PhD thesis, Université Paul Sabatier, Toulouse, 1996.
[LS59]
V. P. Leonov and A. N. Shiryaev. On a method of calculation of semi-invariants. Theory Prob. Appl., 4:319–329,
1959.
[Mal95]
P. Malliavin. Integration and Probability, volume 157 of Graduate Texts in Mathematics. Springer-Verlag, 1995.
[Man96]
B. Mann. Berry–Esseen central limit theorems for Markov chains. PhD thesis, Harvard University, 1996.
[MM91]
V. A. Malyshev and R. A. Minlos. Gibbs random ﬁelds. Springer, 1991.
[MN15]
P.-L. Méliot and A. Nikeghbali. Mod-Gaussian convergence and its applications for models of statistical me-
chanics.
In In Memoriam Marc Yor - Séminaire de Probabilités XLVII, volume 2137 of Lecture Notes in
Mathematics, pages 369–425. Springer-Verlag, 2015.
[New80]
C. M. Newman. Normal ﬂuctuations and the FKG inequalities. Comm. Math. Phys., 74(2):119–128, 1980.
[PY05]
M. Penrose and J. Yukich. Normal approximation in geometric probability. Stein’s Method and Applications,
Lecture Note Series, Institute for Mathematical Sciences, National University of Singapore, 5:37–58, 2005.
[Rin94]
Y. Rinott. On normal approximation rates for certain sums of dependent random variables. J. Comp. Appl.
Math., 55(2):135 – 143, 1994.
[Rud91]
W. Rudin. Functional Analysis. McGraw-Hill, 2nd edition, 1991.
[Sat99]
K.-I. Sato. Lévy processes and inﬁnitely divisible distributions, volume 68 of Cambridge Studies in Advanced
Mathematics. Cambridge University Press, 1999.
[SC97]
L. Saloﬀ-Coste. Lectures on ﬁnite Markov chains. In Lectures on probability theory and statistics (Saint-Flour,
1996), volume 1665 of Lecture Notes in Mathematics, pages 301–413. Springer-Verlag, 1997.
[Spi58]
F. Spitzer. Some theorems concerning 2-dimensional Brownian motion. Trans. Amer. Math. Soc., 87:187–197,
1958.
[SS91]
L. Saulis and V. A. Statulevičius.
Limit theorems for large deviations, volume 73 of Mathematics and its
Applications (Soviet Series). Kluwer Academic Publishers, 1991.
[Sta66]
V. A. Statulevičius. On large deviations. Prob. Th. Rel. Fields, 6(2):133–144, 1966.
[Str11]
D. W. Stroock. Probability Theory: An Analytic View. Cambridge University Press, 2nd edition, 2011.
[SY83]
K.-I. Sato and M. Yamazato. Stationary processes of ornstein-uhlenbeck type. In K. Itô and J. V. Prokhorov,
editors, Probability Theory and Mathematical Statistics, Fourth USSR-Japan Symp., volume 1021 of Lecture
Notes in Mathematics, pages 541–551. Springer-Verlag, 1983.
[Tao12]
T. Tao. Topics in Random Matrix Theory, volume 132 of Graduate Studies in Mathematics. American Mathe-
matical Society, 2012.
