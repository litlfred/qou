---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-022-a4-convergence-of-trace-class-operators
section_title: "Convergence of trace class operators"
section_number: A.4
pages: 40-43
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
be Hermitian nonnegative operators in L1(H). The following proposi-
tion is a special case of Theorem 2.20 in the book [31] (we are grateful
to P. Deift for this reference). For the reader’s convenience we give a
proof here.
Proposition A.9. The following conditions are equivalent:
(i) ∥Kn −K∥1 →0;
(ii) tr Kn →tr K and Kn →K in the weak operator topology.
First, prove a lemma:
Lemma A.10. Let X =

A
B
B∗
D

be a nonnegative operator 2 × 2
matrix. Then ∥B∥1 ≤
√
tr A · tr D.
Proof of Lemma. Without loss of generality one can assume that the
block B is a nonnegative diagonal matrix, B = diag(b1, b2, . . .). Write
the blocks A and D as matrices, too, and let ai and di be their diagonal
entries. Since X ≥0, we have b2
i ≤aidi and therefore
∥B∥1 =
X
bi ≤
X p
aidi ≤
qX
ai ·
X
di ≤
√
tr A · tr D.
Proof of Proposition A.9. Clearly, (i) implies (ii). To check the con-
verse claim, write K in the block form, K =

A
B
B∗
D

, where A is of
ﬁnite size and tr D is small. Write all the Kn’s in the block form with re-
spect to the same decomposition of the Hilbert space, Kn =

An
Bn
B∗
n
Dn

.
Since Kn →K weakly, we have convergence of ﬁnite blocks, An →A,
which implies tr An →tr A. Since tr Kn →tr K, we get tr Dn →tr D,
so that all the traces tr Dn are small together with tr D provided that
n is large enough.
Write K′ =

A
0
0
0

and similarly for Kn. Then
∥Kn −K∥1 ≤∥Kn −K′
n∥1 + ∥K′
n −K′∥1 + ∥K′ −K∥1.
In the right-hand side, the ﬁrst and the third summands are small
because of the lemma, while the second summand is small because it
is equal to ∥An −A∥1.
Proposition A.11. The map (A1, . . . , An) 7→det(I + λ1A1 + · · · +
λnAn) deﬁnes a continuous map from (L1(H))n to the algebra of entire
ASYMPTOTICS OF PLANCHEREL MEASURES
41
functions in n variables with the topology of uniform convergence on
compact sets.
Proof. The fact that det(I + λ1A1 + · · · + λnAn) is holomorphic in
{λi} for any trace class operators A1, . . . , An is proved in [30]. The
continuity of the map follows from the inequality
| det(I + B) −det(I + C)| ≤∥B −C∥1 exp(∥B∥1 + ∥C∥1 + 1)
which holds for any B, C ∈L1(H), see [27, 31].
References
[1] D. Aldous and P. Diaconis, Hammersley’s interacting particle process and
longest increasing subsequences, Prob. Theory and Rel. Fields, 103, 1995, 199–
213.
[2] J. Baik, P. Deift, K. Johansson, On the distribution of the length of the longest
increasing subsequence of random permutations, math.CO/9810105.
[3]
, On the distribution of the length of the second row of a Young diagram
under Plancherel measure, math.CO/9901118.
[4] P. Biane, Permutation model for semi-circular systems and quantum random
walks, Paciﬁc J. Math., 171, no. 2, 1995, 373–387.
[5]
, Representations of symmetric groups and free probability, preprint,
1998.
[6] A. Borodin and G. Olshanski, Distribution on partitions, point processes, and
the hypergeometric kernel, math.RT/9904010.
[7]
, paper in preparation.
[8]
, Z-measures on partitions, Robinson-Schensted-Knuth correspondence,
and β = 2 random matrix ensembles, math.CO/9905189.
[9] P. A. Clarkson and J. B. McLeod, A connection formula for the second Painlev´e
transcendent, Arch. Rat. Mech. Anal., 103, 1988, 97–138.
[10] D. J. Daley and D. Vere-Jones, An introduction to the theory of point processes,
Springer series in statistics, Springer Verlag, 1988.
[11] P. J. Forrester, The spectrum edge of random matrix ensembles, Nuclear
Phys. B, 402, 1993, no. 3, 709–728.
[12] Higher Transcendental functions, Bateman Manuscript Project, McGraw-Hill,
New York, 1953.
[13] P. Jacquet and W. Szpankowski, Analytical depoissonization and its applica-
tions, Theor. Computer Sc., 201, 1998, 1–62.
[14] K. Johansson, The longest increasing subsequence in a random permutation
and a unitary random matrix model, Math. Res. Letters, 5, 1998, 63–82.
[15]
,
Discrete
orthogonal
polynomials
and
the
Plancherel
measure,
math.CO/9906120.
[16] S. Kerov, Gaussian limit for the Plancherel measure of the symmetric group,
C. R. Acad. Sci. Paris, 316, S´erie I, 1993, 303–308.
[17]
, Transition probabilities of continual Young diagrams and the Markov
moment problem, Func. Anal. Appl., 27, 1993, 104–117.
[18]
, The asymptotics of interlacing roots of orthogonal polynomials, St. Pe-
tersburg Math. J., 5, 1994, 925–941.
42
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
[19]
, A diﬀerential model of growth of Young diagrams, Proceedings of the
St. Petersburg Math. Soc., 4, 1996, 167–194.
[20]
, Interlacing measures, Amer. Math. Soc. Transl., 181, Series 2, 1998,
35–83.
[21] B. F. Logan and L. A. Shepp, A variational problem for random Young
tableaux, Adv. Math., 26, 1977, 206–222.
[22] I. G. Macdonald, Symmetric functions and Hall polynomials, Oxford University
Press, 1995.
[23] A. Okounkov, Random matrices and random permutations, math.CO/9903176
[24]
, Inﬁnite wedge and measures on partitions, math.RT/9907127
[25] E. M. Rains, Increasing subsequences and the classical groups, Electr. J. of
Combinatorics, 5(1), 1998.
[26] A. Regev, Asymptotic values for degrees associated with strips of Young dia-
grams, Adv. Math., 41, 1981, 115-136.
[27] E. Seiler and B. Simon, On ﬁnite mass renormalization in the two-dimensional
Yukawa model, J. of Math. Phys., 16, 1975, 2289–2293.
[28] C. Schensted, Longest increasing and decreasing subsequences, Canad. J.
Math., 13, 1961, 179-191.
[29] T. Sepp¨al¨ainen, A microscopic model for Burgers equation and longest increas-
ing subsequences, Electron. J. Prob., 1, no. 5, 1996.
[30] B. Simon, Notes on Inﬁnite Determinants of Hilbert Space Operators, Adv.
Math., 24, 1977, 244–273.
[31]
, Trace ideals and their applications. London Math. Soc. Lecture Note
Ser., 35, Cambridge University Press, 1979, 134 pp.
[32] C. A. Tracy and H. Widom, Level-spacing distributions and the Airy kernel,
Commun. Math. Phys., 159, 1994, 151–174.
[33]
, Introduction to random matrices, Geometric and quantum aspects of
integrable systems, Lecture Notes in Phys., 424, 1993, Springer Verlag, pp.
103–130.
[34]
, On the distribution of the lengths of the longest monotone subsequences
in random words, math.CO/9904042.
[35] A. Vershik, Statistical mechanics of combinatorial partitions and their limit
conﬁgurations, Func. Anal. Appl., 30, no. 2, 1996, 90–105.
[36] A. Vershik and S. Kerov, Asymptotics of the Plancherel measure of the sym-
metric group and the limit form of Young tableaux, Soviet Math. Dokl., 18,
1977, 527–531.
[37]
, Asymptotic theory of the characters of a symmetric group Func. Anal.
Appl., 15, 1981, no. 4, 246-255.
[38]
, Asymptotics of the maximal and typical dimension of irreducible rep-
resentations of symmetric group, Func. Anal. Appl., 19, 1985, no.1.
[39] G. N. Watson, A treatise on the theory of Bessel functions, Cambridge Uni-
versity Press, 1944
[40] H. Widom, Random Hermitian matrices and (nonrandom) Toeplitz matrices,
Toeplitz Operators and Related Topics, the Harold Widom anniversary vol-
ume, edited by E. L. Basor and I. Gohberg, Operator Theory: Advances and
Application, Vol. 71, Birkh¨auser Verlag, 1994, pp. 9–15.
[41]
, The strong Szeg¨o limit theorem for circular arcs, Indiana U. Math. J.,
21, 1971, 271–283.
ASYMPTOTICS OF PLANCHEREL MEASURES
43
University of Pennsylvania, Department of Mathematics, Philadel-
phia PA 19104–6395
E-mail address: borodine@math.upenn.edu
University of Chicago, Department of Mathematics, 5734 Univer-
sity Ave., Chicago IL 60637
E-mail address: okounkov@math.berkeley.edu
Current address: Department of Mathematics, University of California at Berke-
ley, Evans Hall, Berkeley, CA 94720-3840
Dobrushin Mathematics Laboratory, Institute for Problems of In-
formation Transmission, Bolshoy Karetny 19, 101447, Moscow, Russia
E-mail address: olsh@glasnet.ru
