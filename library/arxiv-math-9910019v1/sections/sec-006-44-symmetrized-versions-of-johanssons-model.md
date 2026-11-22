---
doc_id: arxiv-math-9910019v1
doc_title: "Symmetrized random permutations"
section_id: sec-006-44-symmetrized-versions-of-johanssons-model
section_title: "Symmetrized versions of Johansson's model"
section_number: 4.4
pages: 12-17
source_pdf: 9910019v1.pdf
source_sha256: 07dd7ab7068b1482
toc_source: inferred
doc_brief: "Symmetrized random permutations — 8 sections: Front matter; Introduction; Tracy-Widom distribution functions"
---
In [22], Johansson introduced a certain model which has several probabilistic interpretations, as a randomly
growing Young diagram, a totally asymmetric one dimensional exclusion process, a certain zero-temperature
directed polymer in a random environment or as a kind of ﬁrst-passage site percolation model. Here we consider
the symmetrized versions. The limiting distributions are parallel to the results of Section 3 depending on the
symmetry type.
Each model is deﬁned on M, a subset of Z2, and at each site (i, j) ∈M, we deﬁne a random variable w(i, j)
of geometric distribution. We are interested in “the length of the longest up/right path”. Let g(q) denote the
geometric distribution with parameter q. Let 0 < q < 1, and let α, β ≥0 such that α√q, β√q < 1. Otherwise
stated, the random variables w(i, j) are independent each other.
We denote by (j, k) ր (j′, k′) the set of
up/right paths π from (j, k) to (j′, k′).
(i). Let M = Z2
+. Let
w(i, j) ∼g(q).
(4.8)
Deﬁne
G (N) = max{
X
(i,j)∈π
w(i, j) : π ∈(1, 1) ր (N, N)}.
(4.9)
12
(ii). Let M = Z2. Let w(i, j) = 0 if i = 0 or j = 0, and for i, j̸ = 0, let
w(i, j) = w(−i, −j) ∼g(q).
(4.10)
Deﬁne
G · (N) = max{
X
(i,j)∈π
w(i, j) : π ∈(−N, −N) ր (N, N)}.
(4.11)
(iii). Let M = Z2
+. Let
w(i, j) = w(j, i)
∼
g(q),
i̸ = j,
(4.12)
w(i, i)
∼
g(α√q).
(4.13)
Deﬁne
G (N) = max{
X
(i,j)∈π
w(i, j) : π ∈(1, 1) ր (N, N)}.
(4.14)
(iv). Let M = Z+ × Z−. Let
w(i, −j) = w(j, −i)
∼
g(q),
i̸ = −j,
(4.15)
w(i, −i)
∼
g(β√q).
(4.16)
Deﬁne
G (N) = max{
X
(i,j)∈π
w(i, j) : π ∈(1, −N) ր (N, −1)}.
(4.17)
(v). Let M = Z2. Let w(i, j) = 0 if i = 0 or j = 0. Otherwise
w(i, j) = w(−i, −j)
∼
g(q),
|i|̸ = |j|,
(4.18)
w(i, i) = w(−i, −i)
∼
g(α√q),
(4.19)
w(i, −i) = w(−i, i)
∼
g(β√q).
(4.20)
Deﬁne
G (N) = max{
X
(i,j)∈π
w(i, j) : π ∈(−N, −N) ր (N, N)}.
(4.21)
We are interested in the limiting distributions of G⊛(N).
Theorem 4.2. Set
η(q) =
2√q
1 −√q ,
ρ(q) = q1/6(1 + √q)1/3
1 −√q
.
(4.22)
We have
13
(i).
lim
N→∞Pr
G (N; q) −η(q)N
ρ(q)N 1/3
≤x

= F2(x).
(4.23)
(ii).
lim
N→∞Pr
G · (N; q) −η(q)(2N)
22/3ρ(q)(2N)1/3
≤x

= F2(x)2.
(4.24)
(iii).
lim
N→∞Pr
G (N; q, α) −η(q)N
ρ(q)N 1/3
≤x

=
F4(x),
0 ≤α < 1,
(4.25)
lim
N→∞Pr
G (N; q, α) −η(q)N
ρ(q)N 1/3
≤x

=
F (x; w),
α = 1 −
2w
ρ(q)N 1/3 ,
(4.26)
lim
N→∞Pr
G (N; q, α) −η(q)N
ρ(q)N 1/3
≤x

=
0,
α > 1.
(4.27)
(iv).
lim
N→∞Pr
G (N; q, β) −η(q)N
ρ(q)N 1/3
≤x

= F1(x),
0 ≤β.
(4.28)
(v).
lim
N→∞Pr
G (N; q, α, β) −η(q)(2N)
22/3ρ(q)(2N)1/3
≤x

=
F2(x),
0 ≤α < 1, β ≥0,
(4.29)
lim
N→∞Pr
G (N; q, α, β) −η(q)(2N)
22/3ρ(q)(2N)1/3
≤x

=
F (x; w),
α = 1 −
2w
ρ(q)(2N)1/3 , β ≥0
(4.30)
lim
N→∞Pr
G (N; q, α, β) −η(q)(2N)
22/3ρ(q)(2N)1/3
≤x

=
0,
α > 1, β ≥0.
(4.31)
Remark. The results (4.23) and (4.26) with w = 0 are obtained in [21]. For
, the longest up/right path in
(1, 1) ր (M, N), M̸ = N, is also considered.
The proof of the above theorem is analogous to that of the result in Section 3. There again is a Toeplitz/Hankel
determinantal formula for each case. In fact, the only change with the symmetrized permutation case is that
we have (1 + q + 2√q cos θ)Ndθ/(2π) instead of e2t cos θdθ/(2π) for the weight. In analyzing the asymptotics of
orthogonal polynomials, we need diﬀerent scaling, but once we scale, the analysis is parallel. One important
common property of the above two weights is that both of the supports of their equilibrium measures change
from the full circle to a part of the circle with one gap depending on 2t/k < 1 and 2t/k > 1, and N/k < η(q)−1
and N/k > η(q)−1. And also in the one gap case, the equilibrium measures decay like a square root at the ends
of the supports.
14
References
[1] D. Aldous and P. Diaconis. Longest increasing subsequences: from patience sorting to the Baik-Deift-
Johansson theorem. preprint.
[2] D. Aldous and P. Diaconis. Hammersley’s interacting particle process and longest increasing subsequences.
Prob. Th. and Rel. Fields, 103:199–213, 1995.
[3] J. Baik, P. Deift, and K. Johansson. On the distribution of the length of the second row of a Young disgram
under Plancherel measure. e-print math.CO/9901118.
[4] J. Baik, P. Deift, and K. Johansson. On the distribution of the length of the longest increasing subsequence
of random permutations. J. Amer. Math. Soc., 12:1119–1178, 1999.
[5] J. Baik and E. M. Rains. Algebraic aspects of increasing subsequences. e-print math.CO/9905083.
[6] J. Baik and E. M. Rains.
The asymptotics of monotone subsequences of involutions.
e-print
math.CO/9905084.
[7] A. Borodin.
Longest increasing subsequences of random colored permutations.
Electron. J. Combin.,
6(1):R13, 1999.
[8] A. Borodin, A. Okounkov, and G. Olshanski. On asymptotics of Plancherel measures for symmetric groups.
in prepartion.
[9] P. Deift, T. Kriecherbauer, K. McLaughlin, S. Venakides, and X. Zhou. Strong asymptotics of orthogonal
polynomials with respect to exponential weights. to appear in Comm. Pure Appl. Math.
[10] P. Deift, T. Kriecherbauer, K. McLaughlin, S. Venakides, and X. Zhou. Uniform asymptotics for polyno-
mials orthogonal with respect to varying exponential weights and applications to universality questions in
random matrix theory. to appear in Comm. Pure Appl. Math.
[11] P. Deift, T. Kriecherbauer, K. McLaughlin, S. Venakides, and X. Zhou.
Asymptotics for polynomials
orthogonal with respect to varying exponential weights. Internat. Math. Res. Notices, 16:759–782, 1997.
[12] P. Deift and X. Zhou. A steepest descent method for oscillatory Riemman-Hilbert problems; asymptotics
for the MKdV equation. Ann. of Math., 137:295–368, 1993.
[13] P. Deift and X. Zhou. Asymptotics for the Painlev´e II equation. Comm. Pure Appl. Math., 48:277–337,
1995.
[14] H. Flaschka and A. Newell. Monodromy and spectrum preserving deformations, I. Comm. Math. Phys.,
76(1):67–116, 1980.
[15] A. Fokas, A. Its, and V. Kitaev. Discrete Painlev´e equations and their appearance in quantum gravity.
Comm. Math. Phys., 142:313–344, 1991.
15
[16] A. Fokas and X. Zhou. On the solvability of Painlev´e II and IV. Comm. Math. Phys., 144:601–622, 1992.
[17] P. Forrester. Random walks and random permutations. e-print math.CO/9907037.
[18] I. Gessel. Symmetric functions and P-recursiveness. J. Combin. Theory Ser. A, 53:257–285, 1990.
[19] S. Hastings and J. McLeod. A boundary value problem associated with the second Painlev´e transcendent
and the Korteweg de Vries equation. Arch. Rational Mech. Anal., 73:31–51, 1980.
[20] M. Jimbo, T. Miwa, and K. Ueno. Monodromy preserving deformations of linear ordinary diﬀerential
equations with rational coeﬃcients, I. General theory and τ-function. Phys. D, 2(2):306–352, 1981.
[21] K. Johansson. Discrete orthogonal polynomial ensembles and the Plancherel measure. in preparation.
[22] K. Johansson. Shape ﬂuctuations and random matrices. e-print math.CO/9903134.
[23] K. Johansson. Transversal ﬂuctuations for increasing subsequences on the plane. preprint, 1999.
[24] K. Johansson. The longest increasing subsequence in a random permutation and a unitary random matrix
model. Math. Res. Lett., 5(1-2):63–82, 1998.
[25] S. Kerov. Transition probabilities of continual Young diagrams and the Markov moment problem. Funct.
Anal. Appl, 27:104–117, 1993.
[26] D. E. Knuth. Sorting and Searching, volume 3 of The Art of Computer Programming. Addison Wesley,
Reading, Mass., second edition, 1973.
[27] B. Logan and L. Shepp. A variational problem for random Young tableaux. Adv. in Math., 26:206–222,
1977.
[28] M. Mehta. Random matrices. Academic press, San Diago, second edition, 1991.
[29] A. Odlyzko and E. Rains. On longest increasing subsequences in random permutations. Technical report,
AT&T Labs, 1998.
[30] A. Okounkov. Random matrices and random permutations. e-print math.CO/9903176.
[31] E. M. Rains. Increasing subsequences and the classical groups. Electron. J. Combin., 5(1):R12, 1998.
[32] A. Regev. Asymptotic values for degrees associated with strips of Young diagrams. Adv. in Math., 41:115–
136, 1981.
[33] C. Schensted. Longest increasing and decreasing subsequences. Canad. J. Math., 13:179–191, 1961.
[34] T. Sepp¨al¨ainen. A microscopic model for the burgers equation and longest increasing subsequences. Elec-
tron. J. Prob., 1(5), 1995.
[35] C. Tracy and H. Widom. On the distribution of the lengths of the longest monotone subsequences in
random words. e-print math.CO/9904042.
16
[36] C. Tracy and H. Widom. Random unitary matrices, permutations and Painlev´e. e-print math.CO/9811154.
[37] C. Tracy and H. Widom. Level-spacing distributions and the Airy kernel. Comm. Math. Phys., 159:151–174,
1994.
[38] C. Tracy and H. Widom. On orthogonal and symplectic matrix ensembles. Comm. Math. Phys., 177:727–
754, 1996.
[39] A. Vershik and S. Kerov. Asymptotics of the Plancherel measure of the symmetric group and the limiting
form of Young tables. Soviet Math. Dokl., 18:527–531, 1977.
[40] A. Vershik and S. Kerov. Asymptotic behavior of the maximum and generic dimensions of irreducible
representations of the symmetric group. Funct. Anal. Appl, 19:21–31, 1985.
17
