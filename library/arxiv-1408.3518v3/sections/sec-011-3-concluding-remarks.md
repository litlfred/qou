---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond"
section_id: sec-011-3-concluding-remarks
section_title: "Concluding remarks"
section_number: 3
pages: 13-15
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
toc_source: outline
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond — 13 sections: Front matter; Introduction.; Our Contributions"
---
Through the notion of Graver basis, we have obtained extensions of
classical results of Bland, Edmonds, and Karp. Our new version applies now to the case of integer-
linear programs. As a consequence we have also derived the ﬁrst-ever strongly polynomial-time
algorithm for N-fold integer-linear optimization. Our new results also show that Kitahara-Mizuno-
style bounds [24] hold in larger generality to include augmentations that go through the interior
of the polytope and are not restricted to edges. Theorem 1 is in fact an ILP extension of those
bounds too.
There are at least three interesting directions for improvement and further research. First, we
remark the numbers n and 2n−2 from Carath´eodory’s and Seb¨o’s theorems we used in many of the
arguments can be further improved to be n−rank(A) and 2(n−rank(A))−2 respectively because
the arguments can be modiﬁed to use the dimension of the kernel of A. Such small improvement
slightly strengthens several of the results of the paper, but we leave the details to the reader.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
14
Second, as was demonstrated in [10, 11] the estimation of number of augmentations contribute
to the estimation of the diameters of polytopes. Third, it would be interesting to improve our
strongly polynomial algorithm for N-fold matrices. Currently, the number of augmentations does
not depend on b and u, but is a polynomial of degree O(g(A,B)) with g(A,B) the Graver complexity
(see [22, 30, 3]) Thus the degree depends on the ﬁxed matrices A and B. It would be desirable to
arrive to a lower exponent algorithm, like the one of [20] which is not strongly polynomial yet, the
number of augmentations is linear in the binary encoding of b and u, and it is only cubic in N,
O(N 3).
Acknowledgments
We are grateful for the comments from Shmuel Onn. The ﬁrst and the
third author are grateful for the hospitality received by the Isaac Newton Institute for Mathematical
Sciences at the University of Cambridge, UK during the program “Polynomial Optimization”.
The ﬁrst author is thankful to the Technical University of Munich for the support and hospitality
received during his visit in Spring 2013 as a John von Neumann professor and to the NSF for
the support received through grant DMS-0914107. J. Lee was partially supported by NSF grant
CMMI–1160915 and ONR grant N00014-14-1-0315.
References
[1] Ahuja, R.K., T.L. Magnanti, J.B. Orlin. 1993. Network ﬂows. Prentice Hall Inc., Englewood Cliﬀs, NJ.
Theory, algorithms, and applications.
[2] B´ar´asz, M., S. Vempala. 2010.
A new approach to strongly polynomial linear programming.
http://www.cc.gatech.edu/∼vempala/papers/aﬃne.pdf.
[3] Berstein, Y., S. Onn. 2009. The Graver complexity of integer programming. Annals of Combinatorics
13 289–296.
[4] Bixby, R. E., O. M.-C. Marcotte, L. E. Trotter, Jr. 1987. Packing and covering with integral feasible
ﬂows in integral supply-demand networks. Math. Programming 39(3) 231–239.
[5] Bland, R. G. 1974. Complementary orthogonal subspaces of n-dimensional Euclidean space and ori-
entability of matroids. Thesis (Ph.D.)–Cornell University.
[6] Bland, R. G. 1976. On the generality of network ﬂow theory. Presented at the ORSA/TIMS Joint
National Meeting, Miami, Florida, Fall 1976.
[7] Bland, R. G., D. L. Jensen. 1992. On the computational behavior of a polynomial-time network ﬂow
algorithm. Math. Programming 54(1, Ser. A) 1–39.
[8] Bland, R.G., J. Edmonds. 1982. Fast primal algorithms for totally unimodular linear programming.
Presented at XIth International Symposium on Mathematical Programming, Bonn, West Germany
(August 1982).
[9] Bonifas, N., M. Di Summa, F. Eisenbrand, N. H¨ahnle, M. Niemeier. 2014. On sub-determinants and
the diameter of polyhedra. Discrete and Computational Geometry 52(1) 102–115.
[10] Borgwardt, S., E. Finhold, R. Hemmecke. 2014. On the circuit diameter of dual transportation polyhe-
dra. To appear in SIAM Discrete Math. Available as Arxiv:1405.3184.
[11] Borgwardt, S., De Loera J.A., E. Finhold. 2014. Edges vs circuits: a hierarchy of diameters in polyhedra.
Available as ArXiv:1409.7638.
[12] Cardoso, D., J. Cl´ımaco. 1992.
The generalized simplex method.
Operations Research Letters. 12
337–348.
[13] De Loera, J. A., R. Hemmecke, M. K¨oppe. 2013. Algebraic and geometric ideas in the theory of dis-
crete optimization, MOS-SIAM Series on Optimization, vol. 14. Society for Industrial and Applied
Mathematics (SIAM), Philadelphia, PA.
[14] De Loera, J. A., R. Hemmecke, S. Onn, R. Weismantel. 2008. N-fold integer programming. Discrete
Optimization 5(2) 231–241. In Memory of George B. Dantzig.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
15
[15] Edmonds, J., R. M. Karp. 1972. Theoretical improvements in algorithmic eﬃciency for network ﬂow
problems. J. ACM 19(2) 248–264.
[16] Frank, A., E Tardos. 1987. An application of simultaneous diophantine approximation in combinatorial
optimization. Combinatorica 7(1) 49–65.
[17] Fulkerson, D. R. 1968. Networks, frames, blocking systems. Mathematics of the Decision Sciences, Part
1 (Seminar, Stanford, Calif., 1967). Amer. Math. Soc., Providence, R.I., 303–334.
[18] Graver, J. E. 1975. On the foundation of linear and integer programming I. Mathematical Programming
9 207–226.
[19] Hemmecke, R. 2003. On the positive sum property and the computation of Graver test sets. Math.
Programming, Series B 96 247–269.
[20] Hemmecke, R., S. Onn, L. Romanchuk. 2013. N-fold integer programming in cubic time. Mathematical
Programming 137 325–341.
[21] Hemmecke, R., S. Onn, R. Weismantel. 2011. A polynomial oracle-time algorithm for convex integer
minimization. Mathematical Programming 126 97–117.
[22] Ho¸sten, S., S. Sullivant. 2007. A ﬁniteness theorem for Markov bases of hierarchical models. J. Combin.
Theory Ser. A 114(2) 311–321.
[23] Kern, W., U. Faigle, B. Peis. 2012. Unpublished manuscript.
[24] Kitahara, T., S. Mizuno. 2013. A bound for the number of diﬀerent basic solutions generated by the
simplex method. Math. Program. 137(1-2, Ser. A) 579–586.
[25] Lee, J. 1986. Subspaces with well-scaled frames. Ph.D. thesis, Cornell University.
[26] Lee, J. 1989. Subspaces with well-scaled frames. Linear Algebra and its Applications 114-115 21–56.
Special Issue Dedicated to Alan J. Hoﬀman.
[27] Onn, S. 2010. Non-Linear Discrete Optimization. Zurich Lectures in Advanced Mathematics, European
Mathematical Society.
[28] Orlin, J.B. 1997. A polynomial time primal network simplex algorithm for minimum cost ﬂows. Math.
Programming 78(2, Ser. B) 109–129. Network optimization: algorithms and applications (San Miniato,
1993).
[29] Rockafellar, R. T. 1969. The elementary vectors of a subspace of RN. Combinatorial Mathematics and
its Applications (Proc. Conf., Univ. North Carolina, Chapel Hill, N.C., 1967). Univ. North Carolina
Press, Chapel Hill, N.C., 104–127.
[30] Santos, F., B. Sturmfels. 2003. Higher Lawrence conﬁgurations. J. Comb. Theory Ser. A 10 151–164.
[31] Scarf, H. E. 1997. Test sets for integer programs. Mathematical Programming, Series A 79 355–368.
[32] Schulz, A.S, R. Weismantel. 1999.
An oracle–polynomial time augmentation algorithm for integer
programming. Proceedings of the 10th Annual ACM–SIAM Symposium on Discrete Algorithms. 967–
968.
[33] Schulz, A.S, R. Weismantel. 2002. The complexity of generic primal algorithms for solving general
integer program. Mathematics of Operations Research 27 681 – 692.
[34] Seb¨o, A. 1990. Hilbert bases, Caratheodory’s theorem and combinatorial optimization. Ravi Kannan,
William R. Pulleyblank, eds., IPCO. University of Waterloo Press, 431–455.
[35] Seymour, P. D. 1980. Decomposition of regular matroids. J. Combin. Theory Ser. B 28(3) 305–359.
[36] Tardos, ´E. 1986. A strongly polynomial algorithm to solve combinatorial linear programs. Operations
Research 34(2) pp. 250–256.
[37] Ye, Y. 2011. The simplex and policy-iteration methods are strongly polynomial for the markov decision
problem with a ﬁxed discount rate. Math. Oper. Res. 36(4) 593–603.
