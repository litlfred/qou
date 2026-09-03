---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-007-5-tail-bounds
section_title: "Tail bounds"
section_number: 5
pages: 28-34
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
doc_brief: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one — We investigate links between the so-called Stein’s density approach indimension"
---
In the following theorem, we establish lower tail bounds whe n the Stein kernel is uniformly bounded
away from zero. In particular, the support of the measure is R in this case, as can be seen from the
explicit formula (6).
Theorem 20 Take a real random variable X of distribution ν with density p with respect to the
Lebesgue measure on R. Assume that E [X] = 0, p has a connected support and denote τν the Stein
kernel of ν. If τν ≥ σ 2
min > 0 ν-almost surely, then the density p of ν is positive on R and the
function
R (x) =ex2/ 2σ 2
min
∫ +∞
x
yp (y)dy
is nondecreasing on R+. In particular, for any x ≥ 0,
∫ +∞
x
yp (y)dy ≥ E [(X)+]e−x2/ 2σ 2
min . (65)
By symmetry, for any x ≤ 0,
−
∫ x
−∞
yp (y)dy ≥ E [(X)−]e−x2/ 2σ 2
min . (66)
Assume in addition that the function L (x) = x1+βp (x) is nonincreasing on [s, +∞), s >0. Then
for all x ≥s, it holds
P (X ≥x) ≥
(
1 − 1
β
) E
[
(X)+
]
x exp
(
− x2
2σ 2
min
)
. (67)
Alternatively, assume that there exists α ∈ (0, 2) such that lim supx→+∞x−α logτν (x)< +∞. Then
for any δ ∈ (0, 2), there exist L,x 0 > 0 such that, for all x>x 0,
P (X ≥x) ≥ L
x exp
(
− x2
(2 −δ)σ 2
min
)
. (68)
The results presented in Theorem 20 can be found in [NV09] und er the additional assumption,
related to the use of Malliavin calculus, that the random var iable X ∈ D1, 2.
Proof. For any smooth function ϕ nondecreasing,
E [Xϕ (X)] = E
[
τν (X)ϕ ′ (X)
]
≥σ 2
minE
[
ϕ ′ (X)
]
.
28
Takeϕ (x) = min
{
(x −c)+,ε
}
, for some c ∈ R and ε> 0. Then
E [Xϕ (X)] =
∫ c+ε
c
x (x −c)p (x)dx +ε
∫ +∞
c+ε
xp (x)dx
and E [ϕ ′ (X)] = P (X ∈ (c,c +ε]). Dividing the latter two terms by ε and letting ε tend to zero
gives, ∫ +∞
c
xp (x)dx ≥σ 2
minp (c) . (69)
Now set V (c) =
∫ +∞
c xp (x)dx. Inequality (69) writes, for any c ≥ 0,
c
σ 2
min
V (c) ≥ −V ′ (c) .
Then deﬁne, for any c ≥ 0,
R (c) =V (c) exp
( c2
2σ 2
min
)
.
We can diﬀerentiate R and we have
R′ (c) =
(
V ′ (c) + c
σ 2
min
V (c)
)
exp
( c2
2σ 2
min
)
≥ 0 .
In particular R (c) ≥R (0), which gives (65). As τ−X (x) = τX (−x), we deduce by symmetry that
(66) also holds. The proof of inequalities (67) and (68) foll ows from the same arguments as in the
proof of points (ii) and (ii)’, Theorem 4.3, [NV09]. We give t hem, with slight modiﬁcations, for the
sake of completeness. By integration by parts, we have
V (c) =cP (X ≥c) +
∫ +∞
c
P (X ≥x)dx .
We also have, for x> 0,
P (X ≥x) =
∫ +∞
x
y1+βp (y)
y1+β dy ≤x1+βp (x)
∫ +∞
x
dy
y1+β = xp (x)
β .
Hence,
V (c) ≤cP (X ≥c) +β −1
∫ +∞
c
xp (x)dx =cP (X ≥c) +V (c)
β
or equivalently,
P (X ≥c) ≥
(
1 − 1
β
) V (c)
c .
The conclusion follows by combining the latter inequality w ith inequality (65). It remains to prove
(68). By formula (20) applied with h (y) ≡y - note that this is possible since by assumption τν > 0
on R -, it holds
p (x) = E [|X|]
2τν (x) exp
(
−
∫ x
0
y
τν (y)dy
)
≥ E [|X|]
2τν (x) exp
(
− x2
2σ 2
min
)
.
29
Let us ﬁx ε> 0. By assumption on τν, we get that there exists a positive constant C such that, for
x large enough,
p (x) ≥C exp
(
− x2
2σ 2
min
−xα
)
≥C exp
(
− x2
(2 −ε)σ 2
min
)
.
Hence, for x large enough,
P (X ≥x) ≥C
∫ +∞
x
exp
(
− y2
(2 −ε)σ 2
min
)
dy .
The conclusion now easily follows from the following classi cal inequality:
∫ +∞
x e−y2/ 2dy ≥ (x/ (1 +
x2)) exp
(
−x2/ 2
)
.
In the following proposition, we give some further tail boun ds under a variety of assumptions on
the Stein kernel. We omit the proof as it follows directly fro m the same arguments as in the proof
of Corollary 4.5 in [Vie09], where they are derived under the assumption that X ∈ D1, 2.
Proposition 21 Take a real random variable X of distribution ν with density p with respect to the
Lebesgue measure on R. Assume that E [|X|] < +∞, p has a connected support and denote τν the
Stein kernel of ν. If there exist c ∈ (0, 1) and x0 > 1 such that for all x > x0, τν (x) ≤ cx2, then
there exists a positive constant L such that, for all x>x 0
P (X ≥x) ≥L
exp
(
−
∫ x
0
y
τ ν (y)dy
)
x .
If in addition τν ≥σ 2
min> 0 ν-almost surely, then
P (X ≥x) ≥ L
x exp
(
− x2
2σ 2
min
)
.
If there exists rather a positive constant c− ∈ (0,c ] such that τν (x) ≥c−x2 for all x>x 0, then there
exists a positive constant K such that for all x>x 0,
P (X ≥x) ≥ K
x1+1/c −
.
If there exist instead p ∈ (0, 2) and cp > 0 such that, for all x>x 0, τν (x) ≥cpxp, then there exists
a positive constant H such that, for all x>x 0,
P (X ≥x) ≥ L
x exp
(
− x2−p
(2 −p)cp
)
.
In the last two points, if the inequalities on τν in the hypotheses are reversed, then the conclusions
are also reversed, without changing any of the constants.
Acknowledgments
I owe thanks to Guillaume Poly for an instructive discussion about Stein’s method, to Yvik Swan for
a number of pointers to the literature and to Jon Wellner as we ll as Max Fathi for useful comments.
I also warmly thank Michel Bonnefont and Ald´ eric Joulin fornice discussions and valuable comments
related to some (weighted) functional inequalities. Final ly, I express my gratitude to two anonymous
referees for several insightful comments and suggestions t hat helped to complete the study and
improve the quality of the paper.
30
References
[ABC+00] C. An ´e, S. Blach `ere, D. Chafa ¨ı, P. Foug `eres, I. Gentil, F. Malrieu,
C. Roberto, and G. Scheffer . “Sur les in´ egalit´ es de Sobolev logarithmiques”, vol-
ume 10 of “Panoramas et Synth` eses [Panoramas and Syntheses]”. Soci´ et´ e Math´ ematique
de France, Paris (2000). With a preface by Dominique Bakry an d Michel Ledoux.
[ABJ16] M. Arnaudon, M. Bonnefont, and A. Joulin . Intertwinings and generalized
Brascamp-Lieb inequalities. arXiv preprint arXiv:1602.03836 (2016).
[BCG08] D. Bakry, P. Cattiaux, and A. Guillin. Rate of convergence for ergodic continuous
Markov processes: Lyapunov versus Poincar´ e.J. Funct. Anal. 254(3), 727–759 (2008).
[BG99] S. G. Bobkov and F. G¨otze. Exponential integrability and transportation cost related
to logarithmic Sobolev inequalities. J. Funct. Anal. 163(1), 1–28 (1999).
[BGH01] S. G. Bobkov, F. G ¨otze, and C. Houdr ´e. On Gaussian and Bernoulli covariance
representations. Bernoulli 7(3), 439–451 (2001).
[BGL14] D. Bakry, I. Gentil, and M. Ledoux . “Analysis and geometry of Markov diﬀusion
operators”, volume 348 of “Grundlehren der Mathematischen Wissenschaften [Funda-
mental Principles of Mathematical Sciences]”. Springer, B erlin (2014).
[BH97] S. G. Bobkov and C. Houdr ´e. Isoperimetric constants for product probability mea-
sures. Ann. Probab. 25(1), 184–205 (1997).
[BJ14] M. Bonnefont and A. Joulin . Intertwining relations for one-dimensional diﬀusions
and application to functional inequalities. Potential Anal. 41(4), 1005–1031 (2014).
[BJM16a] Michel Bonnefont, Ald´eric Joulin, and Yutao Ma . A note on spectral gap and
weighted Poincar´ e inequalities for some one-dimensionaldiﬀusions. ESAIM Probab. Stat.
20, 18–29 (2016).
[BJM16b] Michel Bonnefont, Ald´eric Joulin, and Yutao Ma. Spectral gap for spherically
symmetric log-concave probability measures, and beyond. J. Funct. Anal. 270(7), 2456–
2482 (2016).
[BL76] H. J. Brascamp and E. H. Lieb. On extensions of the Brunn-Minkowski and Pr´ ekopa-
Leindler theorems, including inequalities for log concave functions, and with an applica-
tion to the diﬀusion equation. J. Functional Analysis 22(4), 366–389 (1976).
[BL97] S. Bobkov and M. Ledoux . Poincar´ e’s inequalities and Talagrand’s concentration
phenomenon for the exponential distribution. Probab. Theory Related Fields 107(3),
383–400 (1997).
[BL09a] S. G. Bobkov and M. Ledoux. On weighted isoperimetric and Poincar´ e-type inequal-
ities. In “High dimensional probability V: the Luminy volume”, volume 5 of “Inst. Math.
Stat. (IMS) Collect.”, pages 1–29. Inst. Math. Statist., Be achwood, OH (2009).
[BL09b] S. G. Bobkov and M. Ledoux . Weighted Poincar´ e-type inequalities for Cauchy and
other convex measures. Ann. Probab. 37(2), 403–427 (2009).
31
[BL14] S. Bobkov and M. Ledoux. One-dimensional empirical measures, order statistics, a nd
Kantorovich transport distances (2014). To appear in the Me moirs of the Amer. Math.
Soc.
[BLM13] S. Boucheron, G. Lugosi, and P. Massart . “Concentration inequalities”. Ox-
ford University Press, Oxford (2013). A nonasymptotic theo ry of independence, With a
foreword by Michel Ledoux.
[BR03] F. Barthe and C. Roberto. Sobolev inequalities for probability measures on the real
line. Studia Math. 159(3), 481–497 (2003). Dedicated to Professor Aleksander Pe/suppresslczy´ nski
on the occasion of his 70th birthday (Polish).
[BRW18] A.D. Barbour, N. Ross, and Y. Wen . Central moment inequalities using Stein’s
method. arXiv preprint arXiv:1802.10225 (2018).
[CCEL13] E. A. Carlen, D. Cordero-Erausquin, and E. H. Lieb . Asymmetric covariance
estimates of Brascamp-Lieb type and related inequalities f or log-concave measures. Ann.
Inst. Henri Poincar´ e Probab. Stat. 49(1), 1–12 (2013).
[CD10] S. Chatterjee and P. S. Dey . Applications of Stein’s method for concentration
inequalities. Ann. Probab. 38(6), 2443–2485 (2010).
[CEG17] D. Cordero-Erausquin and N. Gozlan . Transport proofs of weighted Poincar´ e
inequalities for log-concave distributions. Bernoulli 23(1), 134–158 (2017).
[CFP17] T. A. Courtade, M. Fathi, and A. Pananjady. Existence of Stein Kernels under a
Spectral Gap, and Discrepancy Bound. arXiv preprint arXiv:1703.07707 (2017).
[CGGR10] P. Cattiaux, N. Gozlan, A. Guillin, and C. Roberto . Functional inequalities for
heavy tailed distributions and application to isoperimetr y. Electron. J. Probab. 15, no.
13, 346–385 (2010).
[CGJ18] N. Cook, L. Goldstein, and T. Johnson. Size biased couplings and the spectral gap
for random regular graphs. Ann. Probab. 46(1), 72–125 (2018).
[CGS11] L. H. Y. Chen, L. Goldstein, and Q.-M. Shao . “Normal approximation by Stein’s
method”. Probability and its Applications (New York). Spri nger, Heidelberg (2011).
[CGW11] P. Cattiaux, A. Guillin, and L.-M. Wu . Some remarks on weighted logarithmic
Sobolev inequality. Indiana Univ. Math. J. 60(6), 1885–1904 (2011).
[Cha07] S. Chatterjee. Stein’s method for concentration inequalities. Probab. Theory Related
Fields 138(1-2), 305–321 (2007).
[Cha12] S. Chatterjee. A new approach to strong embeddings. Probab. Theory Related Fields
152(1-2), 231–264 (2012).
[Cha14] S. Chatterjee. A short survey of Stein’s method. In “Proceedings of the Int ernational
Congress of Mathematicians—Seoul 2014. Vol. IV”, pages 1–2 4. Kyung Moon Sa, Seoul
(2014).
[D¨ ob15] C. D¨obler. Stein’s method of exchangeable pairs for the beta distribu tion and general-
izations. Electron. J. Probab. 20, no. 109, 34 (2015).
32
[D¨ um10] Lutz D ¨umbgen. Bounding Standard Gaussian Tail Probabilities. Technica l Report,
(2010).
[EV13] R. Eden and F. Viens. General upper and lower tail estimates using Malliavin calculus
and Stein’s equations. In “Seminar on Stochastic Analysis, Random Fields and Appli-
cations VII”, volume 67 of “Progr. Probab.”, pages 55–84. Bi rkh¨ auser/Springer, Basel
(2013).
[Fat18] Max Fathi. Stein kernels and moment maps. arXiv preprint arXiv:1804.04699 (2018).
to appear in Annals of probability.
[FN17] M. Fathi and B. Nelson. Free Stein kernels and an improvement of the free logarithmic
Sobolev inequality. Adv. Math. 317, 193–223 (2017).
[GG11a] S. Ghosh and L. Goldstein . Applications of size biased couplings for concentration
of measures. Electron. Commun. Probab. 16, 70–83 (2011).
[GG11b] S. Ghosh and L. Goldstein . Concentration of measures via size-biased couplings.
Probab. Theory Related Fields 149(1-2), 271–278 (2011).
[GGR11] S. Ghosh, L. Goldstein, and M. Rai ˇc. Concentration of measure for the number of
isolated vertices in the Erd¨ os–R´ enyi random graph by sizebias couplings. Statist. Probab.
Lett. 81(11), 1565–1570 (2011).
[GIs14] L. Goldstein and ¨U. I¸slak. Concentration inequalities via zero bias couplings.Statist.
Probab. Lett. 86, 17–23 (2014).
[Goz10] N. Gozlan. Poincar´ e inequalities and dimension free concentration of measure. Ann.
Inst. Henri Poincar´ e Probab. Stat. 46(3), 708–739 (2010).
[LaO00] R. Lata/suppress l a and K. Oleszkiewicz. Between Sobolev and Poincar´ e. In “Geometric
aspects of functional analysis”, volume 1745 of “Lecture Notes in Math.”, pages 147–168.
Springer, Berlin (2000).
[LL01] E. H. Lieb and M. Loss. “Analysis”, volume 14 of “Graduate Studies in Mathematics”.
American Mathematical Society, Providence, RI, second edi tion (2001).
[LLJ16] Q. Liu, J. Lee, and M. Jordan . A kernelized Stein discrepancy for goodness-of-ﬁt
tests. In “International Conference on Machine Learning”, pages 276–284 (2016).
[LNP15] Michel Ledoux, Ivan Nourdin, and Giovanni Peccati . Stein’s method, logarith-
mic Sobolev and transport inequalities. Geom. Funct. Anal. 25(1), 256–306 (2015).
[LNP17] M. Ledoux, I. Nourdin, and G. Peccati. A Stein deﬁcit for the logarithmic Sobolev
inequality. Sci. China Math. 60(7), 1163–1180 (2017).
[LRS17] Christophe Ley, Gesine Reinert, and Yvik Swan . Stein’s method for comparison
of univariate distributions. Probab. Surv. 14, 1–52 (2017).
[MG16] L. Mackey and J. Gorham . Multivariate Stein factors for a class of strongly log-
concave distributions. Electron. Commun. Probab. 21, Paper No. 56, 14 (2016).
33
[Mic08] L. Miclo. Quand est-ce que des bornes de Hardy permettent de calculer une constante
de Poincar´ e exacte sur la droite? Ann. Fac. Sci. Toulouse Math. (6) 17(1), 121–192
(2008).
[MJC+14] L. Mackey, M. I. Jordan, R. Y. Chen, B. Farrell, and J. A. Tropp . Matrix
concentration inequalities via the method of exchangeable pairs. Ann. Probab. 42(3),
906–945 (2014).
[MO13] G. Menz and F. Otto . Uniform logarithmic sobolev inequalities for conservati ve spin
systems with super-quadratic single-site potential. Annals of Probability 41, 2182–2224
(2013).
[Muc72] B. Muckenhoupt . Hardy’s inequality with weights. Studia Math. 44, 31–38 (1972).
Collection of articles honoring the completion by Antoni Zygmund of 50 years of scientiﬁc
activity, I.
[NV09] I. Nourdin and F. G. Viens . Density formula and concentration inequalities with
Malliavin calculus. Electron. J. Probab. 14, no. 78, 2287–2309 (2009).
[PMT16] D. Paulin, L. Mackey, and J. A. Tropp. Efron-Stein inequalities for random matri-
ces. Ann. Probab. 44(5), 3431–3473 (2016).
[Ste72] C. Stein . A bound for the error in the normal approximation to the dist ribution of
a sum of dependent random variables. In “Proceedings of the S ixth Berkeley Sym-
posium on Mathematical Statistics and Probability (Univ. C alifornia, Berkeley, Calif.,
1970/1971), Vol. II: Probability theory”, pages 583–602. U niv. California Press, Berke-
ley, Calif. (1972).
[Ste86] C. Stein. “Approximate computation of expectations”, volume 7 of “I nstitute of Math-
ematical Statistics Lecture Notes—Monograph Series”. Ins titute of Mathematical Statis-
tics, Hayward, CA (1986).
[SW18a] A. Saumard and J. A. Wellner . Efron’s monotonicity property for measures on R2.
J. Multivariate Anal. 166C, 212–224 (2018).
[SW18b] A. Saumard and J. A. Wellner . On the isoperimetric constant, covariance in-
equalities and Lp-poincar´ e inequalities in dimension one. Bernoulli (2018). to appear,
arXiv:1711.00668.
[TM15] J. Treilhard and A.-R. Mansouri. Concentration inequalities via Malliavin calculus
with applications. Electron. Commun. Probab. 20, no. 36, 14 (2015).
[Vie09] F. G. Viens . Stein’s lemma, Malliavin calculus, and tail bounds, with a pplication to
polymer ﬂuctuation exponent. Stochastic Process. Appl. 119(10), 3671–3698 (2009).
34
