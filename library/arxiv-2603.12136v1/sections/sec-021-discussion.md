---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-021-discussion
section_title: "Discussion"
section_number: null
pages: 60-69
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
We will follow the structure of the paper, and first evaluate the extension to reflection
symmetries for linear programming and then the extension to mixed-integer linear
programs.
In Section 3, we extended DRCR to reflection symmetries of linear programs.
There are several ways in which the current work can still be extended. First of all,
we note that it is possible to extend the detection of reflection symmetries to not
just use a primal affine offsetδbut to also introduce adual offset. Such a dual offset
alters the objective by subtracting a weighted linear combination of the rows from
the objective. One hopes that doing so will lead to a coarser equitable partition by
having more similar entries in the objective. Similar to the choice ofδ, there are
infinitely many possibilities to do so. However, unlike the primal variables, the dual
variables of linear programming models are typically not explicitly bounded by the
user, so there is no ‘obvious choice’ at the center of the dual variable domains like for
the primal offset. Thus, one would need to come up with some method to choose a
sensible dual offset.
The choice ofδis somewhat justified by Corollary 21, which shows that it corre-
sponds to the complementation of the variables at their bounds. However, it is still
unclear whether other choices ofδmay lead to better results. This is true in particular
for free variables and variables with half-open domains, where any offset can be used
and may change the right-hand sides, and there is no obvious center of the variable
domain.
More generally, we believe it would be interesting to understand in further detail
how one should apply linear and affine transformations to linear programs in order
to detect arbitrary symmetries. One direction which naturally extends this research
60
would be to detect arbitrary row and column scalings that result in coarser equitable
partitions, compared to the±1scalings that we considered here.
In Section 6.1, we performed computational experiments on the linear program-
ming relaxations of MIPLIB 2017 instances. As expected, reflection symmetries are
somewhat uncommon as was also observed by Hojny [2], as for only 81 out of 1065
MIPLIB instances R-DRCR finds more reductions than DRCR. For these instances,
we observed on average a running-time reduction for R-DRCR of roughly 27% on the
affected models compared to DRCR, with most of the benefit coming from a few large
models. One limitation of the current study is that we did not include a crossover pro-
cedure to obtain a basic solution in our experiments, which is crucial in the context
of solving linear programming relaxations in MILP. However, we note that since we
compare R-DRCR against DRCR, a fair comparison with crossover would affect the
running time of both models, so the performance implications in this case are unclear.
As R-DRCR still clearly improves over DRCR without crossover it can be considered
a relevant improvement for the dimension reduction of linear programs. In particular,
reflection reductions can be computed in the same worst-case time complexity as
DRCR by Theorem 25. Also in practice, they can be computed with only minor com-
putational overhead using the implementation details that we describe in Section 3.7.
As the computational effort for crossover is the most important limitation for
applying DRCR to linear programs in practice, one direction for future research is to
investigate if it is possible to exploit symmetry to speed up the crossover procedure.
Since (R)-DRCR factors out symmetries, the crossover problem contains these sym-
metries. It is likely that these symmetries hinder the performance of the crossover
procedure. In an unpublished work, Deakins, Knueven and Ostrowski [56] formu-
late a method that takes advantage of equitable partitions using an iterative lifting
scheme and show that their method can reduce the time spent in crossover. It would
be promising to further develop symmetry-exploiting crossover methods and incor-
porate them with our approach. More generally, one could investigate if knowledge
of symmetries of a linear program can be used directly to improve the performance
of the simplex algorithm without modifying the analyzed (symmetric) polytope.
In Section 4, we extended DRCR to mixed-integer linear programs and high-
light that affine TU decompositions may be used to aggregate integer variables. In
Section 5, we formulate an algorithm that detects an equitable partition that satisfies
the necessary conditions for dimension reduction of mixed-integer linear programs.
The computational results in Section 6.2 indicate that the formulated algorithm is
effective in reducing the running time of an MILP solver: affected instances are solved
more than twice as quickly on average.
The algorithm we propose for MILPs may have several additional benefits. First
of all, if we are able to perform dimension reduction, we may also eliminate some
of the symmetries in the instance. Although we may only eliminate a subgroup of
the symmetries for MILP, this reduction may help to speed up the detection of the
61
remaining symmetries. Second, even if the dimension of the MILP is not reduced, our
algorithm still computes an affine TU decomposition and/or implied integrality that
can be used by the MIP solver. Thus, the computational effort to do so does not go
to waste, regardless of whether a nontrivial equitable partition is detected.
One downside of our algorithm is that it completely rejects any equitable integer
blockQ∈Q I that can not be taken into the reduced problem, by partitioning it into
its individual columns. Although this is a simple approach, it may also reject blocks
that have many columns that contain a network substructure and only a few that
break it. One may hope that instead of a rejecting the block completely, refining the
block to compute an equitable partition and then attempting to add certain subsets
of it might be more effective. However, this complicates the algorithm and requires a
way to decide how equitable parts must refined in case they can not be augmented
to the network matrix.
Our detection algorithm may benefit from detecting and exploiting additional
substructures. For example, if the equitable partitionQcontains someQ∈Qsuch
that the constraint P
w∈Qλwxw =bappears in the constraint matrix, then the
corresponding variable is fixed in the reduced problem and may be ignored for the
detection of the affine TU decomposition, as it is an integral constant in the reduced
problem. Additionally, it would be interesting to combine our reduction with the
aggregation of non-overlapping symmetric variables from Section 7.1 in [27]. Another
possibility that may enhance DRCR for mixed-integer programs is to take the view-
point that it corresponds to simultaneously performing DRCR on all affine fibersHd
that result from fixing integral expressions, where the vectord∈Z k indicates the
subspace. Our current analysis only performs reduces the dimension if DRCR can be
applied for alld∈Z k. It may be possible to use the structure of the polyhedron to
argue for some affine fibersHd that they are irrelevant for the MIP because they are
infeasible or suboptimal, and use this insight to derive a stronger size reduction that
exploits these properties.
For our computational experiments in Section 6.2, we remark that we did not
spend any time or effort for the postsolve procedure by solving it as a linear pro-
gram over the affine fibers, without utilizing the given non-basic LP-feasible point.
Although this is not a bottleneck of our approach, a crossover procedure that uses
the solution as an initial feasible point should be more efficient. If one uses affine
TU decompositions to aggregate symmetric integer variables, then a postsolve step
to recover integrality of the original solutions is necessary. We emphasize that in our
experiments in Section 6.2 we perform crossover only once for the best integer solu-
tion that is found. Most MILP solvers do not report just the optimal solution, but
also provide a solution pool that contains the best found primal solutions. For each
such a solution, one needs to call a crossover procedure. Thus, the computational
costs of the crossover step may become burdensome as it is repeated for every integer
solution that is reported to the user. Thus, this justifies research into fast crossover
procedures that can be used in conjunction with R-DRCR-N and R-DRCR-T.
62
Since we detect if the affine fibers are given by network matrices, the affine fibers
can be transformed into a network flow problem, see [57] for further information. In
crossover, one could also exploit this network structure by using crossover algorithms
that are specialized for network flow problems [58]. The authors of [58] show that
exploiting the network structure and using ideas from the network simplex algorithm
for crossover may help to reduce crossover time by a factor of 10 or more compared
to Gurobi’s default crossover procedure on large optimal transport instances. As the
crossover problem that we consider is also symmetric, the methods from [58] may be
further enhanced by formulating symmetry-aware crossover strategies.
Considering our results, we remark that R-DRCR-N was more effective on the
tested instances than R-DRCR-T. One explanation for this observation is that the
structure of the affine TU decomposition that we observe for the generalized assign-
ment problem corresponds to an assignment problem, which is given by a constraint
matrix that is a network matrix but not a transposed network matrix.
Our approach can also be interpreted asexact orbital shrinkingwhere the orbital
shrinking subproblem is a perfect formulation. Salvagnin [9] observed that orbital
shrinking may be significantly more powerful than exact orbital shrinking if one aggre-
gates a larger symmetry group, which leads to a more difficult subproblem that is
not necessarily a perfect formulation. Further research could investigate how one can
better navigate the trade-off between stronger bounds and the difficulty of the sub-
problem for orbital shrinking. A crucial component here is efficient solution strategies
for the orbital shrinking subproblem, which still contains the symmetries that are fac-
tored out of the original problem. As also remarked by Salvagnin [9], one could also
view orbital shrinking as a logic-based Benders’ decomposition and exploit infeasible
subproblems by providing cutting planes that cut off infeasible solutions.
Acknowledgements.I am grateful to Matthias Walter for his feedback that helped
improve the quality of this work, and I would like to thank Christopher Hojny for
recommending relevant literature.
The author acknowledges funding support from the Netherlands Organisation
for Scientific Research (NWO) on grant number OCENW.M20.151: “Making Mixed-
Integer Programming Solvers Smarter and Faster using Network Matrices".
References
[1] Gleixner, A., al.: Miplib 2017: data-driven compilation of the 6th mixed-integer
programming library. Mathematical Programming Computation13(3), 443–490
(2021) https://doi.org/10.1007/s12532-020-00194-3
[2] Hojny,C.:Detectingandhandlingreflectionsymmetriesinmixed-integer(nonlin-
ear) programming and beyond. Mathematical Programming Computation (2025)
https://doi.org/10.1007/s12532-025-00289-9
63
[3] Margot, F.: In: Jünger, M., Liebling, T.M., Naddef, D., Nemhauser, G.L., Pul-
leyblank, W.R., Reinelt, G., Rinaldi, G., Wolsey, L.A. (eds.) Symmetry in
Integer Linear Programming, pp. 647–686. Springer, Berlin, Heidelberg (2010).
https://doi.org/10.1007/978-3-540-68279-0_17 .https://doi.org/10.1007/978-3-
540-68279-0_17
[4] Bödi,R.,Herr,K.,Joswig,M.:Algorithmsforhighlysymmetriclinearandinteger
programs. Mathematical Programming137(1-2), 65–90 (2013) https://doi.org/
10.1007/s10107-011-0487-6 arXiv:1012.4941
[5] Gatermann, K., Parrilo, P.A.: Symmetry Groups, Semidefinite Programs, and
Sums of Squares vol. 192, pp. 95–128 (2004). https://doi.org/10.1016/j.jpaa.2003.
12.011
[6] Ostrowski, J., Linderoth, J., Rossi, F., Smriglio, S.: Orbital branching.
Mathematical Programming126(1), 147–178 (2011) https://doi.org/10.1007/
s10107-009-0273-x
[7] Liberti, L.: Reformulations in mathematical programming: automatic symme-
try detection and exploitation. Mathematical Programming131(1-2), 273–304
(2012) https://doi.org/10.1007/s10107-010-0351-0
[8] Fischetti, M., Liberti, L.: Orbital shrinking. In: Lecture Notes in Computer Sci-
ence (including Subseries Lecture Notes in Artificial Intelligence and Lecture
Notes in Bioinformatics) vol. 7422 LNCS, pp. 48–58. Springer, Berlin, Heidelberg
(2012). https://doi.org/10.1007/978-3-642-32147-4_6
[9] Salvagnin, D.: Orbital shrinking: A new tool for hybrid mip/cp methods. In: Lec-
ture Notes in Computer Science (including Subseries Lecture Notes in Artificial
Intelligence and Lecture Notes in Bioinformatics) vol. 7874 LNCS, pp. 204–215
(2013). https://doi.org/10.1007/978-3-642-38171-3_14
[10] Fischetti, M., Liberti, L., Salvagnin, D., Walsh, T.: Orbital shrinking: Theory
and applications. Discrete Applied Mathematics222, 109–123 (2017) https://
doi.org/10.1016/j.dam.2017.01.015
[11] Grohe, M., Kersting, K., Mladenov, M., Selman, E.: Dimension reduction via
colour refinement. Lecture Notes in Computer Science (including subseries
Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
8737 LNCS, 505–516 (2014) https://doi.org/10.1007/978-3-662-44777-2_42
arXiv:1307.5697
[12] Bachoc, C., Gijswijt, D.C., Schrijver, A., Vallentin, F.: Invariant semidefinite
programs. In: Handbook of Semidefinite, Conic and Polynomial Optimization
vol. 166, pp. 219–270. Springer, New York (2012). https://doi.org/10.1007/
978-1-4614-0769-0_9
64
[13] Permenter, F., Parrilo, P.A.: Dimension reduction for semidefinite programs via
jordan algebras. Mathematical Programming181(1), 51–84 (2020) https://doi.
org/10.1007/s10107-019-01372-5 arXiv:1608.02090
[14] Read, R.C., Corneil, D.G.: The graph isomorphism disease. Journal of Graph
Theory1(4), 339–363 (1977) https://doi.org/10.1002/jgt.3190010410
[15] Junttila, T., Kaski, P.: bliss: A Tool for Computing Automorphism Groups and
Canonical Labelings of Graphs. http://www.tcs.hut.fi/Software/bliss/ Accessed
6 November 2025
[16] McKay, B.D., Piperno, A.: Nauty User’s Guide (version 2.7) (2025). https://
users.cecs.anu.edu.au/$\sim$bdm/nauty/ Accessed 6 November 2025
[17] Darga, P.T., Katebi, H., Liffiton, M., Markov, I.L., Sakallah, K.: Saucy3: Fast
Symmetry Discovery in Graphs. http://vlsicad.eecs.umich.edu/BK/SAUCY/
Accessed 6 November 2025
[18] Berthold, T.: How to Fold a linear programming Problem (2018). https:
//community.fico.com/s/blog-post/a5Q80000000Drp2EAC/fico1299Accessed13
October 2025
[19] Optimization, G.: What’s new in the Gurobi Optimizer 9.1? (2020). https://
www.youtube.com/watch?v=EwuEPu-nBmg Accessed 2025-10-13
[20] Liberti, L., Ostrowski, J.: Stabilizer-based symmetry breaking constraints for
mathematical programs. Journal of Global Optimization60(2), 183–194 (2014)
https://doi.org/10.1007/s10898-013-0106-6
[21] Margot, F.: Pruning by isomorphism in branch-and-cut. Mathematical Program-
ming94(1), 71–90 (2002) https://doi.org/10.1007/s10107-002-0358-2
[22] Margot, F.: Exploiting orbits in symmetric ilp. Mathematical Programming98(1-
3), 3–21 (2003) https://doi.org/10.1007/s10107-003-0394-6
[23] Ostrowski, J., Linderoth, J., Rossi, F., Smriglio, S.: Constraint orbital branch-
ing. In: Integer Programming and Combinatorial Optimization vol. 5035 LNCS,
pp. 225–239. Springer, Berlin, Heidelberg (2008). https://doi.org/10.1007/
978-3-540-68891-4_16
[24] Pfetsch, M.E., Rehn, T.: A computational comparison of symmetry handling
methods for mixed integer programs. Mathematical Programming Computation
11(1), 37–93 (2019) https://doi.org/10.1007/s12532-018-0140-y
[25] Salvagnin, D., Walsh, T.: A hybrid mip/cp approach for multi-activity shift
scheduling. In: Lecture Notes in Computer Science (including Subseries Lecture
Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), vol. 7514
65
LNCS, pp. 633–646 (2012). https://doi.org/10.1007/978-3-642-33558-7_46
[26] Herr, K., Rehn, T., Schürmann, A.: Exploiting symmetry in integer convex opti-
mization using core points. Operations Research Letters41(3), 298–304 (2013)
https://doi.org/10.1016/j.orl.2013.02.007 arXiv:1202.0435
[27] Achterberg, T., Bixby, R.E., Gu, Z., Rothberg, E., Weninger, D.: Presolve reduc-
tions in mixed integer programming. Technical report, Zuse Institute Berlin,
Berlin (2016)
[28] Gemander, P., Chen, W.-K., Weninger, D., Gottwald, L., Gleixner, A., Martin,
A.: Two-row and two-column mixed-integer presolve using hashing-based pairing
methods. EURO Journal on Computational Optimization8(3-4), 205–240 (2020)
https://doi.org/10.1007/s13675-020-00129-6
[29] van der Hulst, R., Walter, M.: Implied integrality in mixed-integer optimiza-
tion. In: Integer Programming and Combinatorial Optimization, pp. 452–465.
Springer, Cham (2025). https://doi.org/10.1007/978-3-031-93112-3_33
[30] Bader, J., Hildebrand, R., Weismantel, R., Zenklusen, R.: Mixed integer
reformulations of integer programs and the affine tu-dimension of a matrix.
Mathematical Programming169(2), 565–584 (2018) https://doi.org/10.1007/
s10107-017-1147-2 1508.02940
[31] Bixby,R.E.,Wagner,D.K.:Analmostlinear-timealgorithmforgraphrealization.
Mathematics of Operations research13(1) (1988) https://doi.org/10.1287/moor.
13.1.99
[32] van der Hulst, R., Walter, M.: A row-wise algorithm for graph realization1, 1–44
(2025) arXiv:2408.12869
[33] Schrijver, A.: Theory of Linear and Integer Programming. John Wiley & Sons,
Inc., New York, NY, USA (1986)
[34] Hojny, C., Besançon, M., Bestuzheva, K., Borst, S., Dionísio, J., Ehls, J., Eifler,
L., Ghannam, M., Gleixner, A., Göß, A., Hoen, A., Holly-Ponientzietz, J., van
der Hulst, R., Kamp, D., Koch, T., Kofler, K., Lentz, J., Lübbecke, M., Maher,
S.J., Meinhold, P.M., Mexi, G., Mohr, T., Mühmer, E., Patel, K.K., Pfetsch,
M.E., Pokutta, S., Groba, C.R., Serrano, F., Shinano, Y., Turner, M., Vigerske,
S., Walter, M., Weninger, D., Xu, L.: The SCIP Optimization Suite 10.0 (2025).
https://arxiv.org/abs/2511.18580
[35] Paige, R., Tarjan, R.E.: Three partition refinement algorithms. SIAM Journal on
Computing16(6), 973–989 (1987) https://doi.org/10.1137/0216062
[36] Hopcroft, J.: An n log n algorithm for minimizing states in a finite automaton. In:
Theory of Machines and Computations vol. 7874 LNCS, pp. 189–196. Elsevier,
66
Haifa, Israel (1971). https://doi.org/10.1016/B978-0-12-417750-5.50022-1
[37] Geyer, A.J., Bulutoglu, D.A., Ryan, K.J.: Finding the symmetry group of an
lp with equality constraints and its application to classifying orthogonal arrays.
Discrete Optimization32, 93–119 (2019) https://doi.org/10.1016/j.disopt.2019.
01.001
[38] Gomory, R.E.: An algorithm for the mixed-integer problem. Technical Report
RM-2597, RAND Corporation (1960)
[39] Megiddo, N.: On finding primal- and dual-optimal bases. ORSA Journal on
Computing3(1), 63–65 (1991) https://doi.org/10.1287/ijoc.3.1.63
[40] Bolusani, S., Besançon, M., Bestuzheva, K., Chmiela, A., Dionísio, J.,
Donkiewicz, T., Doornmalen, J., Eifler, L., Ghannam, M., Gleixner, A., Graczyk,
C., Halbig, K., Hedtke, I., Hoen, A., Hojny, C., Hulst, R., Kamp, D., Koch, T.,
Kofler, K., Lentz, J., Manns, J., Mexi, G., Mühmer, E., Pfetsch, M.E., Schlösser,
F., Serrano, F., Shinano, Y., Turner, M., Vigerske, S., Weninger, D., Xu, L.: The
scip optimization suite 9.0 (05), 1–36 (2024) arXiv:2402.17702
[41] Christophel,P.M.,Güzelsoy,M.,Pólik,I.:Newsymmetriesinmixed-integerlinear
optimization: Symmetry heuristics and complement-based symmetries (2014)
[42] Berkholz, C., Bonsma, P., Grohe, M.: Tight lower and upper bounds for the
complexity of canonical colour refinement. Theory of Computing Systems60(4),
581–614 (2017) https://doi.org/10.1007/s00224-016-9686-0 arXiv:1509.08251
[43] Hoffman, A.J., Kruskal, J.B.: Integral boundary points of convex polyhedra.
In: Linear Inequalities and Related Systems vol. 38, pp. 223–246. Prince-
ton University Press, Princeton, New Jersey (1956). https://doi.org/10.1515/
9781400881987-014
[44] Meyer, R.R.: On the existence of optimal solutions to integer and mixed-integer
programming problems. Mathematical Programming7, 223–235 (1974) https:
//doi.org/10.1007/BF01585518
[45] Khachiyan, L.G.: Polynomial algorithms in linear programming. USSR Com-
putational Mathematics and Mathematical Physics20(1), 53–72 (1980) https:
//doi.org/10.1016/0041-5553(80)90061-0
[46] Grötschel, M., Lovász, L., Schrijver, A.: The ellipsoid method and its con-
sequences in combinatorial optimization. Combinatorica1(2), 169–197 (1981)
https://doi.org/10.1007/BF02579273
[47] Bland, R.G., Goldfarb, D., Todd, M.J.: The ellipsoid method: A survey. Opera-
tions Research29(6), 1039–1091 (1981) https://doi.org/10.1287/opre.29.6.1039
67
[48] Ziegler, G.M.: Lectures on Polytopes (Graduate Texts in Mathematics). Springer,
New York (2001)
[49] Truemper, K.: A decomposition theory for matroids. v. testing of matrix total
unimodularity. Journal of Combinatorial Theory, Series B49(2), 241–281 (1990)
https://doi.org/10.1016/0095-8956(90)90030-4
[50] Walter, M., Truemper, K.: Implementation of a unimodularity test. Mathe-
matical Programming Computation5(1), 57–73 (2013) https://doi.org/10.1007/
s12532-012-0048-x
[51] van der Hulst, R.: Folding Mixed-Integer Linear Programs and Reflection
Symmetries. GitHub (2026). https://github.com/rolfvdhulst/folding
[52] van der Hulst, R.: MATREC: Matrix recognition algorithms. GitHub (2024).
https://github.com/rolfvdhulst/matrec
[53] Gleixner, A., Gottwald, L., Hoen, A.: PaPILO: A parallel presolving library for
integer and linear programming with multiprecision support. INFORMS Journal
on Computing (2023) https://doi.org/10.1287/ijoc.2022.0171.cd
[54] Achterberg, T., Bixby, R.E., Gu, Z., Rothberg, E., Weninger, D.: Presolve reduc-
tions in mixed integer programming. INFORMS Journal on Computing32(2),
473–506 (2020) https://doi.org/10.1287/ijoc.2018.0857
[55] Berthold, T.: Measuring the impact of primal heuristics. Operations Research
Letters41(6), 611–614 (2013) https://doi.org/10.1016/j.orl.2013.08.007
[56] Deakins, E., Knueven, B., Ostrowski, J.: Orbital Crossover (2022). https://
optimization-online.org/2022/12/orbital-crossover/
[57] Bixby, R.E., Cunningham, W.H.: Converting linear programs to network prob-
lems. Mathematics of Operations Research5(3), 321–357 (1980) https://doi.org/
10.1287/moor.5.3.321
[58] Ge, D., Wang, C., Xiong, Z., Ye, Y.: From an interior point to a corner point:
Smart crossover. INFORMS Journal on Computing (December) (2025) https:
//doi.org/10.1287/ijoc.2022.0291 arXiv:2102.09420
68
