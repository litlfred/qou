---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-010-5-proof-of-theorem-5
section_title: "Proof of Theorem 5"
section_number: 5
pages: 15-17
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
---
Fix a measure ν on Cn and consider the process νt constructed in Section 2.2. An application of
[7, Lemma 6] gives
H(ν) = 1
2E
[ ∫ ∞
0
Tr (Cov(νt)) dt
]
. (30)
Deﬁne h : Cn → R by
h(x) = −
∑
i∈[n]
1 + xi
2 log 1 + xi
2 + 1 − xi
2 log 1 − xi
2 .
It is easily veriﬁed that
˜H(ν) = h
( ∫
xdν(x)
)
= h (a0) . (31)
Recall (equation (11)) that
dat = Cov(νt)dBt.
Thus, by Itˆ o’s formula,
dh(at) = ⟨∇h(at), da t⟩ + 1
2 Tr
(
Cov(νt)∇2h(at)Cov(νt)
)
dt.
A calculation gives
∇2h(x) = −diag
( 1
1 − x2
1
, . . . , 1
1 − x2
n
)
.
Observe also that since ν is supported on Cn,
diag (Cov(νt)) = In − diag(at)2.
Combining the last displays gives
dh(at) = 1
2Tr
(
Cov(νt) (diag (Cov(νt)))−1 Cov(νt)
)
dt + martingale. (32)
Using (8), the condition (5) implies that, almost surely for all t, Cov(νt) ≼ β diag (Cov(νt))
which yields
Tr
(
Cov(νt) (diag (Cov(νt)))−1 Cov(νt)
)
≤ β Tr(Cov(νt)). (33)
15
Combining the above ﬁnally gives
˜H(ν)
(31)
= h(a0)
= h(a0) − E
[
lim
t→∞
h(a∞)
]
(32)
= 1
2 E
[ ∫ ∞
0
Tr
(
Cov(νt) (diag (Cov(νt)))−1 Cov(νt)
)
dt
]
(33)
≤ 1
2 β E
[ ∫ ∞
0
Tr
(
Cov(νt)
)
dt
]
(30)
= β H(ν).
References
[1] Nima Anari, Kuikui Liu, and Shayan Oveis Gharan. Spectra l independence in
high-dimensional expanders and applications to the hardco re model. arXiv preprint
arXiv:2001.00303, 2020.
[2] Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant. Log-concave poly-
nomials II: High-dimensional walks and an FPRAS for countin g bases of a matroid. In
STOC’19—Proceedings of the 51st Annual ACM SIGACT Symposiu m on Theory of Com-
puting, pages 1–12. ACM, New Y ork, 2019.
[3] Nima Anari, Shayan Oveis Gharan, and Cynthia Vinzant. Lo g-concave polynomials, en-
tropy, and a deterministic approximation algorithm for cou nting bases of matroids. In
59th Annual IEEE Symposium on F oundations of Computer Scien ce—FOCS 2018 , pages
35–46. IEEE Computer Soc., Los Alamitos, CA, 2018.
[4] Henry W. Block, Thomas H. Savits, and Moshe Shaked. Some c oncepts of negative de-
pendence. Ann. Probab., 10(3):765–772, 1982.
[5] Devdatt Dubhashi and Desh Ranjan. Balls and bins: a study in negative dependence.
Random Structures Algorithms, 13(2):99–124, 1998.
[6] Ronen Eldan. Thin shell implies spectral gap up to polylo g via a stochastic localization
scheme. Geom. Funct. Anal. , 23(2):532–569, 2013.
[7] Ronen Eldan. Taming correlations through entropy-efﬁc ient measure decompositions with
applications to mean-ﬁeld approximation. Probab. Theory Related Fields, 176(3-4):737–
755, 2020.
[8] Ronen Eldan, Frederic Koehler, and Ofer Zeitouni. A spec tral condition for spectral gap:
Fast mixing in high-temperature ising models. arXiv preprint arXiv:2007.08200, 2020.
[9] Kevin Garbe and Jan V ondrak. Concentration of lipschitz functions of negatively depen-
dent variables. arXiv preprint arXiv:1804.10084, 2018.
[10] Bo’az Klartag. Concentration of measures supported on the cube. Israel J. Math. ,
203(1):59–80, 2014.
16
[11] Peter M¨ orters and Y uval Peres. Brownian motion , volume 30 of Cambridge Series in
Statistical and Probabilistic Mathematics. Cambridge University Press, Cambridge, 2010.
With an appendix by Oded Schramm and Wendelin Werner.
[12] Robin Pemantle. Towards a theory of negative dependenc e. volume 41, pages 1371–1390.
2000. Probabilistic techniques in equilibrium and nonequi librium statistical physics.
[13] Robin Pemantle and Y uval Peres. Concentration of Lipsc hitz functionals of determinantal
and other strong Rayleigh measures. Combin. Probab. Comput., 23(1):140–160, 2014.
[14] Adrien Saumard and Jon A. Wellner. Log-concavity and st rong log-concavity: a review.
Stat. Surv., 8:45–114, 2014.
[15] J. van den Berg and U. Fiebig. On a combinatorial conject ure concerning disjoint occur-
rences of events. Ann. Probab., 15(1):354–374, 1987.
[16] J. van den Berg and H. Kesten. Inequalities with applica tions to percolation and reliability.
J. Appl. Probab., 22(3):556–569, 1985.
[17] David G. Wagner. Negatively correlated random variabl es and Mason’s conjecture for
independent sets in matroids. Ann. Comb., 12(2):211–239, 2008.
17
