---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-026-10-a-decomposition-conjecture
section_title: "A decomposition conjecture"
section_number: 10
pages: 37-44
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
A decomposition conjecture
Let W ⊆Rn be a linear space. As the analogue of maximal augmentations, we say that a
conformal circuit decomposition of z ∈W is maximal, if it can be obtained as follows. If z ∈W
is an elementary vector, return the decomposition containing the single vector z. Otherwise,
select an arbitrary g ∈F(W) that is conformal with z (in particular, supp(g) ⊊supp(z)), and
set g1 = αg for the largest value α > 0 such that z −g1 is conformal with z. Then, recursively
apply this procedure to z −g1 to obtain the other elementary vectors g2, . . . , gh. We have h ≤n,
since the support decreases by at least one due to the maximal choice of α. If κW = ˙κW = 1,
then it is easy to verify the following.
Proposition 10.1. Let W ⊆Rn be a linear space with κW = 1, and let z ∈W ∩Zn. Then, for
every maximal conformal circuit decomposition z = Ph
k=1 gk, we have gk ∈F(W) ∩Zn.
We formulate a conjecture asserting that this property generalizes for arbitrary ˙κW values.
Note that in the conjecture, we only require the existence of some (not necessarily maximal)
conformal circuit decomposition.
Conjecture 10.1.1. Let W ⊆Rn be a rational linear subspace. Then, for every z ∈W ∩Zn,
there exists a conformal circuit decomposition z = Ph
k=1 gk, h ≤n such that each gk is a
1/˙κW -integral vector in F(W).
Note that it is equivalent to require the same property for elements of the Graver basis z ∈
G(A). Hence, the conjecture asserts that every vector in the Graver basis is a ‘nice’ combination
of elementary vectors.
We present some preliminary evidence towards this conjecture:
Proposition 10.2. Let W ⊆Rn be a rational linear subspace with κ∗
W = 1. Then, for every
z ∈W ∩Zn, and every maximal conformal circuit decomposition z = Ph
k=1 gk, we have that gk
is a 1/˙κ-integral vector in F(W).
Proof. Assume κDW = 1 for some D ∈Dn. By Theorem 5.3, we can select D such that all
diagonal entries di = Dii ∈Z and di| ˙κW. Let z = Ph
k=1 gk be any maximal conformal circuit
decomposition of z ∈W ∩Zn. Clearly, Dz = Ph
k=1 Dgk is also a maximal conformal circuit
decomposition of Dz ∈DW ∩Zn. By Proposition 10.1, Dgk ∈F(DW) ∩Zn. Since di | ˙κW ,
this implies that gk is 1/˙κW-integral.
By Theorem 5.5, this implies the conjecture whenever ˙κW = pα for p ∈P, p > 2, α ∈N.
Let us now consider the case when ˙κW is a power of 2. We verify the conjecture when the
decomposition contains at most three terms.
Proposition 10.3. Let W ⊆Rn be a rational linear subspace with κW = 2α for α ∈Zn. If
z ∈W ∩Zn has a maximal conformal circuit decomposition z = Ph
k=1 gk with h ≤3, then each
gk is a 1/˙κ-integral vector in F(W).
Proof. Let us write the maximal conformal circuit decomposition in the form z = Ph
k=1 λkgk
such that lcm(gk) = 1, and all entries gk
i ∈{±1, ±2, ±4, . . . , ±2α} for k ∈[h], i ∈[n]. There
is nothing to prove for h = 1. If h = 2, then by the maximality of the decomposition, λ1 =
minj{zj/g1
j }. Hence, λ1 is 1/2α-integral. Consequently, both λ1g1 and λ2g2 = z −λ1g1 are
1/2α-integral.
If h = 3, then λ1g1 is 1/2α-integral as above. It also follows that λ2g2 and λ3g3 are 1/2β-
integral for some β ≥α. Let us choose the smallest such β; we are done if β = α.
Assume for a contradiction β > α. Let µk = 2βλk for k = 1, 2, 3. Thus, µk ∈Z, µ1 is even,
and at least one of µ2 and µ3 is odd. We show that both µ2 and µ3 must be odd. Let us ﬁrst
assume that µ3 is odd. There exists an i ∈[n] such that |g3
i | = 1. Then, 2βzi = µ1g1
i +µ2g2
i +µ3g3
i
implies that µ2 must also be odd. Similarly, if µ2 is odd then µ3 must also be odd.
Let us take any j ∈[n] such that g1
j = 0. Then, 2βzi = µ2g2
j + µ3g3
j . Noting that |g2
j | and
|g3
j | are powers of 2, both at most 2α, it follows that |g2
j | = |g3
j |; by conformity, we have g2
j = g3
j .
Consequently, supp(g2 −g3) ⊆supp(g1). Clearly, g2 −g3 ∈W \ {0}, and the containment
is strict by the maximality of the decomposition: there exists an index i ∈supp(z) such that
zj = λ1g1
j . This contradicts the fact that g1 ∈F(W).
Acknowledgements
The authors are grateful to Daniel Dadush for numerous inspiring discussions and joint work
on circuit imbalances and linear programming, and to Luze Xu for pointing them to Jon Lee’s
papers [Lee89,Lee90]. The authors would also like to thank Jes´us De Loera, Martin Kouteck´y,
and the anonymous reviewers for their helpful comments and suggestions.
References
[AK04]
G. Appa and B. Kotnyek.
Rational and integral k-regular matrices.
Discrete
Mathematics, 275(1-3):1–15, 2004.
[AMO93]
R. K. Ahuja, T. L. Magnanti, and J. B. Orlin. Network Flows: Theory, Algorithms,
and Applications. Prentice-Hall, Inc., 1993.
[BDSE+14]
N. Bonifas, M. Di Summa, F. Eisenbrand, N. H¨ahnle, and M. Niemeier. On sub-
determinants and the diameter of polyhedra. Discrete & Computational Geometry,
52(1):102–115, 2014.
[BFH15]
S. Borgwardt, E. Finhold, and R. Hemmecke.
On the circuit diameter of dual
transportation polyhedra. SIAM Journal on Discrete Mathematics, 29(1):113–121,
2015.
[Bla76]
R. G. Bland.
On the generality of network ﬂow theory.
Presented at the
ORSA/TIMS Joint National Meeting, Miami, FL, 1976.
[BR13]
T. Brunsch and H. R¨oglin. Finding short paths on polytopes by the shadow ver-
tex algorithm. In Proceedings of the 40th International Colloquium on Automata,
Languages, and Programming (ICALP), pages 279–290. Springer, 2013.
[BSY18]
S. Borgwardt, T. Stephen, and T. Yusun.
On the circuit diameter conjecture.
Discrete & Computational Geometry, 60(3):558–587, 2018.
[BT89]
F. Barahona and ´E. Tardos. Note on Weintraub’s minimum-cost circulation algo-
rithm. SIAM Journal on Computing, 18(3):579–583, 1989.
[BV20]
S. Borgwardt and C. Viss. An implementation of steepest-descent augmentation
for linear programs. Operations Research Letters, 48(3):323–328, 2020.
[Cam64]
P. Camion. Matrices Totalement Unimodulaires et Problemes Combinatoires. PhD
thesis, Communaut´e europ´enne de l’´energie atomique (EURATOM), 1964. EUR
1632.1.
[Cam65]
P. Camion. Characterization of totally unimodular matrices. Proceedings of the
American Mathematical Society, 16(5):1068–1068, May 1965.
[Ced57]
I. Cederbaum. Matrices all of whose elements and subdeterminants are 1, −1, or
0. Journal of Mathematics and Physics, 36(1-4):351–361, 1957.
[CLS19]
M. B. Cohen, Y. T. Lee, and Z. Song. Solving linear programs in the current
matrix multiplication time. In Proceedings of the 51st Annual ACM Symposium
on Theory of Computing (STOC), pages 938–942, 2019.
[DF94]
M. Dyer and A. Frieze. Random walks, totally unimodular matrices, and a ran-
domised dual simplex algorithm. Mathematical Programming, 64(1):1–16, 1994.
[DH16]
D. Dadush and N. H¨ahnle. On the shadow simplex method for curved polyhedra.
Discrete & Computational Geometry, 56(4):882–909, 2016.
[DHNV20]
D. Dadush, S. Huiberts, B. Natura, and L. A. V´egh. A scaling-invariant algorithm
for linear programming whose running time depends only on the constraint matrix.
In Proceedings of the 52nd Annual ACM Symposium on Theory of Computing
(STOC), pages 761–774, 2020.
[Dik67]
I. Dikin.
Iterative solution of problems of linear and quadratic programming.
Doklady Akademii Nauk, 174(4):747–748, 1967.
[Din70]
E. A. Dinic. Algorithm for solution of a problem of maximum ﬂow in networks
with power estimation.
In Soviet Math. Doklady, volume 11, pages 1277–1280,
1970.
[DKNV21]
D. Dadush, Z. K. Koh, B. Natura, and L. A. V´egh. On circuit diameter bounds
via circuit imbalances. arXiv preprint arXiv:2111.07913, 2021.
[DLHL15]
J. A. De Loera, R. Hemmecke, and J. Lee. On augmentation algorithms for lin-
ear and integer-linear programming: From Edmonds–Karp to Bland and beyond.
SIAM Journal on Optimization, 25(4):2494–2511, 2015.
[DLKS19]
J. A. De Loera, S. Kafer, and L. Sanit`a.
Pivot rules for circuit-augmentation
algorithms in linear optimization. arXiv preprint arXiv:1909.12863, 2019.
[DLSV12]
J. A. De Loera, B. Sturmfels, and C. Vinzant. The central curve in linear pro-
gramming. Foundations of Computational Mathematics, 12(4):509–540, 2012.
[DNV20]
D. Dadush, B. Natura, and L. A. V´egh. Revisiting Tardos’s framework for linear
programming: Faster exact solutions using approximate solvers. In Proceedings of
the 61st Annual IEEE Symposium on Foundations of Computer Science (FOCS),
pages 931–942, 2020.
[DSEFM14] M. Di Summa, F. Eisenbrand, Y. Faenza, and C. Moldenhauer. On largest volume
simplices and sub-determinants. In Proceedings of the 26th annual ACM-SIAM
Symposium on Discrete Algorithms (SODA), pages 315–323, 2014.
[DVZar]
D. Dadush, L. A. V´egh, and G. Zambelli. On ﬁnding exact solutions to linear
programs in the oracle model. In Proceedings of the 2022 ACM-SIAM Symposium
on Discrete Algorithms (SODA), 2022 (to appear).
[EHK18]
F. Eisenbrand, C. Hunkenschr¨oder, and K.-M. Klein. Faster Algorithms for Integer
Programs with Block Structure. In Proceedings of the 45th International Collo-
quium on Automata, Languages, and Programming (ICALP 2018), pages 49:1–13,
2018.
[EHK+19]
F. Eisenbrand, C. Hunkenschr¨oder, K.-M. Klein, M. Kouteck´y, A. Levin, and
S. Onn.
An algorithmic theory of integer programming.
arXiv preprint
arXiv:1904.01361, 2019.
[EJ70]
J. Edmonds and E. L. Johnson. Matching: A well-solved class of integer linear pro-
grams. In Combinatorial Structures and Their Applications, pages 89–92. Gordon
and Breach, 1970.
[EK72]
J. Edmonds and R. M. Karp. Theoretical improvements in algorithmic eﬃciency
for network ﬂow problems. Journal of the ACM (JACM), 19(2):248–264, 1972.
[EV17]
F. Eisenbrand and S. Vempala. Geometric random edge. Mathematical Program-
ming, 164(1-2):325–339, 2017.
[Fra11]
A. Frank.
Connections in Combinatorial Optimization.
Number 38 in Oxford
Lecture Series in Mathematics and its Applications. Oxford University Press, 2011.
[Ful68]
D. Fulkerson. Networks, frames, blocking systems. Mathematics of the Decision
Sciences, Part I, Lectures in Applied Mathematics, 2:303–334, 1968.
[GD21]
J. B. Gauthier and J. Desrosiers. The minimum mean cycle-canceling algorithm
for linear programs. European Journal of Operational Research, 2021. (in press).
[GHR95]
O. G¨uler, A. J. Hoﬀman, and U. G. Rothblum. Approximations to solutions to
systems of linear inequalities. SIAM Journal on Matrix Analysis and Applications,
16(2):688–696, 1995.
[GKS95]
J. W. Grossman, D. M. Kulkarni, and I. E. Schochetman. On the minors of an
incidence matrix and its Smith normal form. Linear Algebra and its Applications,
218:213–224, March 1995.
[GS86]
A. M. Gerards and A. Schrijver. Matrices with the Edmonds–Johnson property.
Combinatorica, 6(4):365–379, 1986.
[GT89]
A. V. Goldberg and R. E. Tarjan. Finding minimum-cost circulations by canceling
negative cycles. Journal of the ACM (JACM), 36(4):873–886, 1989.
[Hel57]
I. Heller.
On linear systems with integral valued solutions.
Paciﬁc Journal of
Mathematics, 7(3):1351–1364, 1957.
[HK56]
A. Hoﬀman and J. Kruskal. Integral boundary points of convex polyhedra. In Lin-
ear Inequalities and Related Systems, pages 223–246. Princeton University Press,
1956.
[HMNT93]
D. S. Hochbaum, N. Megiddo, J. S. Naor, and A. Tamir. Tight bounds and 2-
approximation algorithms for integer programs with two variables per inequality.
Mathematical Programming, 62(1):69–83, 1993.
[Hof52]
A. J. Hoﬀman. On approximate solutions of systems of linear inequalities. Journal
of Research of the National Bureau of Standards, 49(4):263––265, 1952.
[HT56]
I. Heller and C. Tompkins. An extension of a theorem of Dantzig’s. Linear in-
equalities and related systems, 38:247–254, 1956.
[HT02]
J. C. Ho and L. Tun¸cel. Reconciliation of various complexity and condition mea-
sures for linear programming problems and a generalization of Tardos’ theorem. In
Foundations of Computational Mathematics, pages 93–147. World Scientiﬁc, 2002.
[Kha95]
L. Khachiyan.
On the complexity of approximating extremal determinants in
matrices. Journal of Complexity, 11(1):138–153, 1995.
[KM97]
A. V. Karzanov and S. T. McCormick. Polynomial methods for separable convex
optimization in unimodular linear spaces with applications.
SIAM Journal on
Computing, 26(4):1245–1275, 1997.
[Knu85]
D. E. Knuth. Semi-optimal bases for linear dependencies. Linear and Multilinear
Algebra, 17(1):1–4, 1985.
[KT95]
D. Klatte and G. Thiere. Error bounds for solutions of linear equations and in-
equalities. Zeitschrift f¨ur Operations Research, 41(2):191–214, 1995.
[Lee89]
J. Lee. Subspaces with well-scaled frames. Linear Algebra and its Applications,
114:21–56, 1989.
[Lee90]
J. Lee. The incidence structure of subspaces with well-scaled frames. Journal of
Combinatorial Theory, Series B, 50(2):265–287, 1990.
[LHK12]
J. D. Loera, R. Hemmecke, and M. K¨oppe. Algebraic and Geometric Ideas in the
Theory of Discrete Optimization. Society for Industrial and Applied Mathematics,
USA, 2012.
[LS19]
Y. T. Lee and A. Sidford. Solving linear programs with ˜O(
√
rank) linear system
solves. arXiv preprint 1910.08033, 2019.
[MS00]
S. T. McCormick and A. Shioura. Minimum ratio canceling is oracle polynomial for
linear programming, but not strongly polynomial, even for networks. Operations
Research Letters, 27(5):199–207, 2000.
[MT03]
R. D. C. Monteiro and T. Tsuchiya.
A variant of the Vavasis-Ye layered-step
interior-point algorithm for linear programming. SIAM Journal on Optimization,
13(4):1054–1079, 2003.
[MT05]
R. D. C. Monteiro and T. Tsuchiya. A new iteration-complexity bound for the
MTY predictor-corrector algorithm. SIAM Journal on Optimization, 15(2):319–
347, 2005.
[MT08]
R. D. Monteiro and T. Tsuchiya. A strong bound on the integral of the central
path curvature and its relationship with the iteration-complexity of primal-dual
path-following LP algorithms. Mathematical Programming, 115(1):105–149, 2008.
[MTY93]
S. Mizuno, M. Todd, and Y. Ye.
On adaptive-step primal-dual interior-point
algorithms for linear programming. Mathematics of Operations Research - MOR,
18:964–981, 11 1993.
[O’L90]
D. P. O’Leary. On bounds for scaled projections and pseudoinverses. Linear Algebra
and its Applications, 132:115–117, April 1990.
[PVZ20]
J. Pena, J. C. Vera, and L. F. Zuluaga. New characterizations of Hoﬀman constants
for systems of linear constraints. Mathematical Programming, 187:1–31, 2020.
[RG94]
T. Radzik and A. V. Goldberg. Tight bounds on the number of minimum-mean
cycle cancellations and related results. Algorithmica, 11(3):226–242, 1994.
[Roc69]
R. T. Rockafellar. The elementary vectors of a subspace of RN. In Combinatorial
Mathematics and Its Applications: Proceedings North Carolina Conference, Chapel
Hill, 1967, pages 104–127. The University of North Carolina Press, 1969.
[San12]
F. Santos. A counterexample to the Hirsch conjecture. Annals of Mathematics,
pages 383–412, 2012.
[Sch98]
A. Schrijver. Theory of linear and integer programming. John Wiley & Sons, 1998.
[Sch03]
A. Schrijver. Combinatorial Optimization – Polyhedra and Eﬃciency. Springer,
2003.
[Sey80]
P. Seymour. Decomposition of regular matroids. Journal of Combinatorial Theory,
Series B, 28(3):305–359, 1980.
[Sey93]
M. Seysen.
Simultaneous reduction of a lattice basis and its reciprocal basis.
Combinatorica, 13(3):363–376, 1993.
[SIM00]
M. Shigeno, S. Iwata, and S. T. McCormick. Relaxed most negative cycle and
most positive cut canceling algorithms for minimum cost ﬂow. Mathematics of
Operations Research, 25(1):76–104, 2000.
[Sma98]
S. Smale. Mathematical problems for the next century. The Mathematical Intelli-
gencer, 20:7–15, 1998.
[SSZ91]
G. Sonnevend, J. Stoer, and G. Zhao. On the complexity of following the central
path of linear programs by linear extrapolation II. Mathematical Programming,
52(1-3):527–553, 1991.
[Ste89]
G. Stewart.
On scaled projections and pseudoinverses.
Linear Algebra and its
Applications, 112:189–193, 1989.
[SW99]
A. S. Schulz and R. Weismantel. An oracle-polynomial time augmentation algo-
rithm for integer programming. In Proceedings of the 10th ACM-SIAM Symposium
on Discrete Algorithms (SODA), pages 967–968, 1999.
[Tar86]
´E. Tardos. A strongly polynomial algorithm to solve combinatorial linear programs.
Operations Research, pages 250–256, 1986.
[Tod90]
M. J. Todd.
A Dantzig–Wolfe-like variant of Karmarkar’s interior-point linear
programming algorithm. Operations Research, 38(6):1006–1018, 1990.
[TTY01]
M. J. Todd, L. Tun¸cel, and Y. Ye. Characterizations, bounds, and probabilistic
analysis of two complexity measures for linear programming problems. Mathemat-
ical Programming, 90(1):59–69, Mar 2001.
[Tun99]
L. Tun¸cel. Approximating the complexity measure of Vavasis-Ye algorithm is NP-
hard. Mathematical Programming, 86(1):219–223, Sep 1999.
[Tut65]
W. T. Tutte. Lectures on matroids. J. Research of the National Bureau of Stan-
dards (B), 69:1–47, 1965.
[vdBLL+21] J. van den Brand, Y. P. Liu, Y.-T. Lee, T. Saranurak, A. Sidford, Z. Song, and
D. Wang. Minimum cost ﬂows, MDPs, and L1-regression in nearly linear time for
dense instances. In Proceedings of the 53rd Annual ACM SIGACT Symposium on
Theory of Computing (STOC), pages 859–869, 2021.
[vdBLN+20] J. van den Brand, Y.-T. Lee, D. Nanongkai, R. Peng, T. Saranurak, A. Sidford,
Z. Song, and D. Wang. Bipartite matching in nearly-linear time on moderately
dense graphs.
In IEEE 61st Annual Symposium on Foundations of Computer
Science (FOCS), pages 919–930, 2020.
[VY96]
S. A. Vavasis and Y. Ye. A primal-dual interior point method whose running time
depends only on the constraint matrix. Mathematical Programming, 74(1):79–120,
1996.
[Wal89]
C. Wallacher. A generalization of the minimum-mean cycle selection rule in cycle
canceling algorithms. unpublished manuscript, Institute f¨ur Angewandte Mathe-
matik, Technische Universit¨at Braunschweig, 1989.
[Way02]
K. D. Wayne. A polynomial combinatorial algorithm for generalized minimum cost
ﬂow. Mathematics of Operations Research, pages 445–459, 2002.
[Wei74]
A. Weintraub. A primal algorithm to solve network ﬂow problems with convex
costs. Management Science, 21(1):87–97, 1974.
[WZ99]
C. Wallacher and U. T. Zimmermann. A polynomial cycle canceling algorithm for
submodular ﬂows. Mathematical programming, 86(1):1–15, 1999.
