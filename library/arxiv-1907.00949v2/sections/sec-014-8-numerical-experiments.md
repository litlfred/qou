---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-014-8-numerical-experiments
section_title: "Numerical experiments"
section_number: 8
pages: 23-26
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
We will test our algorithm for steepest descent on the ﬂag manifold numerically. As we explained
in Section 7.2, the experiments for conjugate gradient algorithm is more involved and is deferred
to [24]. We run our numerical experiments on two problems: (i) the principal ﬂag problem in
Section 8.1 is one for which the solution may be determined in closed-form analytically, and thus
it serves to demonstrate the correctness of our algorithm, i.e., converges to the true solution; (ii)
a variation of the previous problem with a more complicated objective function to show that the
convergence behavior remains unchanged. In addition, neither problem can be solved by simply
treating them as nonlinear optimization problems with equality constraints and applying standard
nonlinear optimization algorithms.
In the following we will assume the identiﬁcation in (45) and use Stiefel coordinates throughout.
8.1. Principal ﬂags. Let M∈ Rn×n be symmetric. We seek the solution to
maximize tr( Y TMY )
subject to JY K∈ Flag(n1,...,n d;n). (52)
Here Y ∈ Rn×nd, Y TY = 1, and the objective function is well-deﬁned as a function on the ﬂag
manifold: If we have Y and Y′ with JY K = JY′K, then they must be related as in (25) and thus
tr(Y TMY ) = tr(Y′TMY′).
As we saw in Example 1.5, when M is a sample covariance matrix, the solution to (52) is
equivalent to PCA when we seek a complete ﬂag, i.e., d =n− 1 and ni =i, i = 1,...,n − 1. An
advantage proﬀered by this approach is that if we do not know the intrinsic dimension of the data
set a priori, then ﬁnding the ﬂag as opposed to any particular subspace gives us the entire proﬁle,
showing how increasing dimension accounts for an increasingly amount of variance. The problem
in (52) is thus a generalization of PCA, allowing us to seek any ﬂag, not necessarily a complete
one. It may also be interpreted as ﬁnding subspaces of dimensions n1,n 2−n1,...,n d−nd−1 that
are independent and explain diﬀerent levels of variance in the data set.
Figure 1 shows the convergence trajectories of steepest descent, i.e., Algorithm 1, on the ﬂag
manifold Flag(3, 7, 12; 60), a 623-dimensional manifold. The symmetric matrix M∈ R60×60 is gen-
erated randomly with standard normal entries. Since the true solution of (52) may be determined
in closed form — it is the sum of the k largest eigenvalues of M — we may therefore conclude
that Algorithm 1 converges to the true solution in around 80 iterations. Indeed the function values
stabilize after as few as 10 iterations. At least for this problem, we see that the vanishing of the
Riemannian gradient serves as a viable stopping condition. In our implementation, our stopping
conditions are determined by (i) Frobenius norm of Riemannian gradient, (ii) distance between
successive iterates, and (iii) number of iterations.
We perform extensive experiments beyond that in Figure 1 by taking average of 100 instances
of the problem (52) for various values of n1,...,n d. We tabulate our results showing accuracy and
speed in Tables 1–4. Tables 1 and 3 show that Algorithm 1 is robust across all dimensions of ﬂags
24 K. YE, K. S.-W. WONG, AND L.-H. LIM
0 20 40 60 80 100
0
10
20
30
40
50
60
70
80
90
100function value
0 20 40 60 80 100
−12
−10
−8
−6
−4
−2
0
2
log(distance between iterates)
0 20 40 60 80 100
−10
−8
−6
−4
−2
0
2
log(distance to solution)
Iteration
0 20 40 60 80 100
−10
−8
−6
−4
−2
0
2
4
log(Riemannian gradient norm)
Iteration
Figure 1. Convergence trajectories for (52) on Flag(3, 7, 12; 60).
and ambient spaces that we tested. Tables 2 and 4 show that elapsed time taken for Algorithm 1
increases roughly linearly with the dimension of the ﬂag manifold.
k 30 40 50 60 70 80 90 100
Accuracy (×10−4) 2 8 64 32 4 87 20 15
Table 1. Distance to true solution for (52) on Flag(3 , 9, 21;k).
k 30 40 50 60 70 80 90 100
Elapsed Time 0.38 0 .40 0 .67 0 .93 1 .71 2 .27 3 .08 4 .07
Table 2. Elapsed time for (52) on Flag(3, 9, 21;k).
k 1 2 3 4 5 6 7 8 9 10
Accuracy (×10−4) 1.4 3 .4 3 .4 8 .6 2 .8 18 19 5 .1 9 .3 11
Table 3. Distance to true solution for (52) on Flag(2 ,..., 2k; 60).
OPTIMIZATION ON FLAG MANIFOLDS 25
k 1 2 3 4 5 6 7 8 9 10
Elapsed Time 0.54 0 .81 0 .79 0 .96 1 .05 0 .91 1 .20 1 .06 1 .18 1 .12
Table 4. Elapsed time for (52) on Flag(2,..., 2k; 60).
k 1 2 3 4 5 6 7 8 9 10
Accuracy (×10−4) 1.4 3 .4 3 .4 8 .6 2 .8 18 19 5 .1 9 .3 11
Table 5. Distance to true solution for (52) on Flag(2 ,..., 2k; 60).
8.2. Nonlinear eigenﬂags. This is a variation of the principal ﬂag problem (52):
maximize ∑d
i=1 tr(Y T
i MYi)2
subject to JY1,...,Y dK∈ Flag(n1,...,n d;n).
(53)
AgainM∈ Rn×n is a symmetric matrix and the ﬂag is given in Stiefel coordinatesY = [Y1,...,Y d]∈
Rn×nd,Y TY =I, but partitioned into submatrices Yi∈ Rn×(ni−ni−1),Y T
i Yi =I,i = 1,...,d . More
generally, the objective function in (53) may be replaced by ∑d
i=1fi
(
tr(Y T
i MYi)
)
withf1,...,f d∈
C2(R). Choosing f1(x) =··· =fd(x) =x gives us (52) and choosingf1(x) =··· =fd(x) =x2 gives
us (53). Note that it will take considerable eﬀort to formulate a problem like (53) as a constrained
optimization problem in Euclidean space.
0 50 100 150 200 250 300 350 400
0
1000
2000
3000
4000
5000function value
0 50 100 150 200 250 300 350 400
−4
−2
0
2
4
6
8
log(Riemannian gradient norm)
0 50 100 150 200 250 300 350 400
−12
−10
−8
−6
−4
−2
0
2
log(distance between iterates)
Iteration
Figure 2. Convergence trajectories for (53) on Flag(3, 7, 12; 60).
26 K. YE, K. S.-W. WONG, AND L.-H. LIM
The convergence trajectories for Algorithm 1 applied to (53) are shown in Figure 2. The nonlin-
earity imposes a cost — it takes around 390 iterations to satisfy one of the our stopping criteria,
although the function values stabilize after around 60 iterations. The jagged spikes seen in Figure 2
are a result of iterates moving along a geodesic and then jumping to another geodesic. So this is
indicative of steepest descent following a path that comprises multiple geodesics. A caveat is that
unlike the principal ﬂag problem (52), we do not have a closed-form solution for (53) and thus we
may only guarantee convergence to a local minimizer, which is reﬂected in Figure 2.
