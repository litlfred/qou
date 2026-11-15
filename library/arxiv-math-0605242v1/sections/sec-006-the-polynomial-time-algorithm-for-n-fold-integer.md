---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming"
section_id: sec-006-the-polynomial-time-algorithm-for-n-fold-integer
section_title: "The polynomial time algorithm for n-fold integer programming"
section_number: null
pages: 13-16
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
toc_source: outline
doc_brief: "N-Fold Integer Programming — In this article we study a broad class of integer programming problems in variable dimension."
---
The polynomial time algorithm for n-fold integer programming
We now provide the polynomial time algorithm for the generalized n-fold integer programming problem
min{cx : [A, B](n)x = b, x ∈Nnq}
.
(2)
First, combining the results of the previous two sections, we get a polynomial time procedure for
converting any feasible solution to an optimal one. We record this result in the following lemma.
Lemma 5.1 Fix any pair of integer matrices A ∈Zr×q and B ∈Zs×q. Then there is a polynomial time
algorithm that, given n, objective vector c ∈Nnq, and nonnegative integer vector x ∈Nnq, solves the
generalized n-fold integer programming problem in which x is feasible, i.e. the one with b := [A, B](n)x.
Proof. First, apply the polynomial time algorithm underlying Theorem 4.2 on input n and compute
the Graver basis G([A, B](n)) of the n-fold matrix [A, B](n). Then apply the polynomial time algorithm
underlying Theorem 3.3 on input [A, B](n), G([A, B](n)), c and x, solving the integer program (2). □
We now show that, moreover, given any b, we can eﬃciently ﬁnd an initial feasible solution to (2).
Lemma 5.2 Fix any pair of integer matrices A ∈Zr×q and B ∈Zs×q. Then there is a polynomial
time algorithm that, given n and demand vector b ∈Ns+nr, either ﬁnds a feasible solution x ∈Nnq to
the generalized n-fold integer programming problem (2), or asserts that no feasible solution exists.
Proof. Introduce 2n(r + s) auxiliary variables to the given generalized n-fold integer program, and
denote by z the resulting vector of n(2(r + s) + q) variables. Consider the auxiliary integer program
of ﬁnding a nonnegative integer vector z that minimizes the sum of the auxiliary variables subject to
13
the following system of equations, with Ir and Is the r × r and s × s identity matrices:









B
Is
−Is
0
0
B
Is
−Is
0
0
B
· · ·
B
Is
−Is
0
0
A
0
0
Ir
−Ir
0
0
0
0
0
0
· · ·
0
0
0
0
0
0
0
0
0
0
A
0
0
Ir
−Ir
0
· · ·
0
0
0
0
0
...
0
0
0
0
0
0
0
0
0
0
0
· · ·
A
0
0
Ir
−Ir









· z = b
.
This auxiliary program is in fact again a generalized n-fold integer program, with matrices ¯A =
(A, 0, 0, Ir, −Ir) and ¯B = (B, Is, −Is, 0, 0). Since A and B are ﬁxed, so are ¯A and ¯B. Due to the special
structure of the auxiliary program, a feasible solution of this program can be written down easily in
terms of b. Consequently, the auxiliary program can be solved by the algorithm underlying Lemma 5.1,
in time polynomial in n and the bit size of b. Since the auxiliary objective is bounded below by zero,
the algorithm will output an optimal solution z. If the optimal objective value is (strictly) positive,
then the original n-fold program (2) has no feasible solution, whereas if the optimal value is zero, then
the restriction of z to the original variables is a feasible solution x of the original program (2).
□
Combining the results of Lemmas 5.1 and 5.2, we obtain the main result of this article.
Theorem 1.2 Fix any pair of integer matrices A, B of compatible sizes. Then there is a polynomial
time algorithm that solves the generalized n-fold integer programming problem on any input n, b, c.
Clearly, Theorem 1.1 is deduced from Theorem 1.2 in the special case B = Iq. We emphasize again
that, by solving the generalized n-fold integer programming problem, we mean in the complete sense
that the algorithm concludes with precisely one of the following: it either asserts that there is no
feasible solution, or asserts that the objective function is unbounded, or returns an optimal solution.
References
[1] Aoki, S., Takemura, A.: Minimal basis for connected Markov chain over 3 × 3 × K contingency
tables with ﬁxed two-dimensional marginals. Austr. New Zeal. J. Stat. 45 (2003) 229–249
[2] Balinski, M.L., Rispoli, F.J.: Signature classes of transportation polytopes. Math. Prog. Ser. A 60
(1993) 127–144
[3] Cox L.H.: Bounds on entries in 3-dimensional contingency tables. Inference Control in Statistical
Databases - From Theory to Practice. Lec. Not. Comp. Sci., Springer, New York, 2316 (2002) 21–33
[4] Cox L.H.: On properties of multi-dimensional statistical tables. J. Stat. Plan. Infer. 117 (2003)
251–273
14
[5] De Loera, J., Onn, S.: The complexity of three-way statistical tables. SIAM J. Comp. 33 (2004)
819–836
[6] De Loera, J., Onn, S.: All rational polytopes are transportation polytopes and all polytopal integer
sets are contingency tables. Proc. 10th Ann. Math. Prog. Soc. Symp. Integ. Prog. Combin. Optim.,
(Columbia University, New York), Lec. Not. Comp. Sci., Springer, New York, 3064 (2004) 338–351
[7] De Loera, J., Onn, S.: Markov bases of three-way tables are arbitrarily complicated. J. Symb.
Comp., to appear
[8] Duncan, G.T, Fienberg, S.E., Krishnan, R., Padman, R., Roehrig, S.F.: Disclosure limitation meth-
ods and information loss for tabular data. In: Doyle, P., Land, J.I., Theeuwes, J.M., Zayatz, L.V.
(Eds.), Conﬁdentiality, Disclosure and Data Access: Theory and Practical Applications for Statis-
tical Agencies, North-Holland (2001)
[9] Graver, J.E.: On the foundation of linear and integer programming I. Math. Prog. 9 (1975) 207–226
[10] Hemmecke, R.: On the positive sum property and the computation of Graver test sets. Math.
Prog. 96 (2003) 247–269
[11] Hemmecke,
R.:
Exploiting
symmetries
in
the
computation
of
Graver
bases.
e-print:
arXiv:math.CO/0410334 (2004)
[12] Hemmecke, R., Malkin, P.: 4ti2 Version 1.2–Computation of Hilbert bases, Graver bases, toric
Gr¨obner bases, and more. Available at http://www.4ti2.de/, July 2005
[13] Ho¸sten, S., Sullivant, S.: Finiteness theorems for Markov bases of hierarchical models. e-print:
arXiv:math.CO/0401379, (2004)
[14] Irving, R., Jerrum, M.R.: Three-dimensional statistical data security problems. SIAM J. Comput.
23 (1994) 170–184
[15] Klee, V., Witzgall, C.: Facets and vertices of transportation polytopes. In: Mathematics of the
Decision Sciences, Part I (Stanford, CA, 1967), AMS, Providence, RI, (1968) 257–282
[16] Lenstra Jr., H.W.: Integer programming with a ﬁxed number of variables. Math. Oper. Res. 8
(1983) 538–548
[17] Onn, S., Rothblum, U.G.: Convex combinatorial optimization. Disc. Comp. Geom. 32 (2004)
549–566
[18] Queyranne, M., Spieksma, F.C.R.: Approximation algorithms for multi-index transportation
problems with decomposable costs. Disc. App. Math. 76 (1997) 239–253
15
[19] Santos, F., Sturmfels, B.: Higher Lawrence conﬁgurations. J. Combin. Theory Ser. A 103 (2003)
151–164
[20] Schrijver, A.: Theory of Linear and Integer Programming. Wiley, New York (1986)
[21] Schulz, A., Weismantel, R.: The complexity of generic primal algorithms for solving general inte-
gral programs. Math. Oper. Res. 27 (2002) 681–692
[22] Vlach, M.: Conditions for the existence of solutions of the three-dimensional planar transportation
problem. Disc. App. Math. 13 (1986) 61–78
[23] Yemelichev, V.A., Kovalev, M.M., Kravtsov, M.K.: Polytopes, Graphs and Optimisation. Cam-
bridge University Press, Cambridge (1984)
Jesus De Loera
University of California at Davis, Davis, CA 95616, USA
email: deloera@math.ucdavis.edu,
http://www.math.ucdavis.edu/∼deloera
Raymond Hemmecke
Otto-von-Guericke Universit¨at Magdeburg, D-39106 Magdeburg, Germany
email: hemmecke@imo.math.uni-magdeburg.de,
http://www.math.uni-magdeburg.de/∼hemmecke
Shmuel Onn
Technion - Israel Institute of Technology, 32000 Haifa, Israel
email: onn@ie.technion.ac.il,
http://ie.technion.ac.il/∼onn
Robert Weismantel
Otto-von-Guericke Universit¨at Magdeburg, D-39106 Magdeburg, Germany
email: weismantel@imo.math.uni-magdeburg.de,
http://www.math.uni-magdeburg.de/∼weismant
16
