---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming:"
section_id: sec-001-11-our-contributions
section_title: "Our Contributions"
section_number: 1.1
pages: 4-8
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: — 4 sections: Introduction.; Our Contributions; Proofs"
---
theorem beyond LP to ILP. Our main results and proofs extend w hat Bland did for circuits to
Graver bases. We look at several augmentation rules. Althou gh they are very similar, our results
here are naturally divided into the LP and ILP cases, with sma ll but important technical changes.
Also, depending on whether variables are restricted to be in tegers or not, we rely on diﬀerent sets as
the set of allowable augmentation directions, which we deno te by T (A). The set T (A) will change
depending on the case.
In what follows, we will employ T (A) in augmentation algorithms that iteratively replace a
feasible (either continuous or integer) solution xk to Ax = b, 0 ≤ x ≤ u, by a better feasible solution
xk+1 := xk + αz, where c⊺z < 0 and α > 0. We consider three speciﬁc augmentation rules.
Definition 1 (Discrete Deepest Descent). With respect to a feasible solution xk, we
choose z such that −αc⊺z is maximized among all z ∈ T (A) and α > 0 such that xk+1 := xk + αz
is feasible (note that for ILP this means that α ∈ Z).
Definition 2 (Discrete Dantzig Descent). With respect to a feasible solution xk, we
choose z such that −c⊺z is maximized among all z ∈ T (A) such that xk + ǫz is feasible for some
ǫ > 0 (note that for LP this means for all suﬃciently small ǫ > 0, and for ILP this means for ǫ = 1).
Then we take a maximum augmentation in such a direction. That is, we let xk+1 := xk + αz, where
α is the largest value for which xk + αz is feasible (note that for ILP this means that α ∈ Z).
Definition 3 (Discrete Steepest Descent). With respect to a feasible solution xk, we
choose z such that −c⊺z/‖z‖1 is maximized among all z ∈ T (A) such that xk + ǫz is feasible for
some ǫ > 0 (note that for LP this means for all suﬃciently small ǫ > 0, and for ILP this means for
ǫ = 1). Then we take a maximum augmentation in such a direction. That is, we let xk+1 := xk + αz,
where α is the largest value for which xk + αz is feasible (note that for ILP this means that α ∈ Z).
Note that all three augmentation rules produce maximal augm entations. Practically speaking,
there are more situations in which discrete steepest descen t and discrete Dantzig descent can be
practically implemented, as compared to discrete deepest d escent. Still, it is interesting to analyze
and contrast these augmentation rules. We derive the follow ing main results concerning these
augmentation rules for the ILP and the LP cases. In some struc tured situations, these bounds will
provide very good guarantees of performance. Our ILP theore m is new, while our LP results extend
what Bland started early on, and greatly extends the applica bility of the bounds of Kitahara and
Mizuno.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
5
Next we state the results. Note that in what follows the base o f all logarithms is two.
For the discrete deepest-descent rule, in the ILP case a poly nomial time bound was ﬁrst proved,
but not explicitly stated as a proposition, in [ 21] and in [ 27] (see top of page 47 (end of proof of
Lemma 3.10)). Here we make it very explicit:
Lemma 1 ((see also [ 21])). The number of discrete deepest-descent augmentations need ed to
reach an optimal solution from x0 is bounded by (4n − 4) log(c⊺(x0 − xmin)).
In addition, for the other two augmentation rules we prove:
Theorem 1 (ILP case) . Let A ∈ Zd×n, b ∈ Zd and c ∈ Zn deﬁne the ILP
min { c⊺x : Ax = b, 0 ≤ x ≤ u, x ∈ Zn } .
Let x0 be an initial feasible solution, let xmin be an optimal solution, and let γ be the maximum
non-zero entry (in absolute value) in any feasible solution . Then we have the following bounds on
the number of augmentations to reach an optimal solution fro m x0.
(a) The number of discrete Dantzig-descent augmentations n eeded to reach an optimal solution of
the ILP is bounded by (4n − 4)γ log(c⊺(x0 − xmin)).
(b) Any discrete steepest-descent direction (which by deﬁn ition belongs to G(A)) is an overall
steepest-descent direction (which could be any applicable direction from Zn). Moreover, the num-
ber of discrete steepest-descent augmentations to reach an optimal solution of the given ILP is
bounded by |G(A)|.
Next we present our results for augmentation algorithms in l inear programming. The results for
integer augmentations arguments in [ 21] and in [ 27] (see top of page 47 (end of proof of Lemma
3.10)) could be adapted to obtain an LP bound too, but the boun d one obtains from [ 21] leads
directly to an extra factor of n in the number of augmentations due to the strategy presented there
to ensure termination. Our contribution is that we manage to get rid of this factor of n:
Lemma 2. The number of discrete deepest-descent augmentations need ed to reach an optimal
solution from x0 is bounded by 2n log(δ c⊺(x0 − xmin)).
Moreover we prove the following extensions to the other augm entation rules for LPs:
Theorem 2 (LP case) . Let A ∈ Zd×n, b ∈ Zd and c ∈ Zn deﬁne the LP
min { c⊺x : Ax = b, 0 ≤ x ≤ u, x ∈ Rn } .
Let x0 be an initial feasible solution, let xmin be an optimal solution, let γ be the maximum non-zero
entry (in absolute value) in any feasible solution, and let δ denote the least common multiple of
all subdeterminants of A. Then we have the following bounds on the number of augmentat ions to
reach an optimal solution from x0.
(a) The number of discrete Dantzig-descent augmentations n eeded to reach an optimal solution from
x0 is no more than 2n2δγ log(δ c⊺(x0 − xmin)).
(b) Any discrete steepest-descent direction (which by deﬁn ition belongs to C(A)) is an overall
steepest-descent direction (which could be any applicable direction from Rn). Moreover, the num-
ber of discrete steepest-descent augmentations to reach an optimal solution of the given LP is
bounded by |C(A)|.
While by nature LP augmentation algorithms cannot have cycl ing, as can happen for the sim-
plex method, it should be noted that the LP case of the discret e deepest-descent and the discrete
Dantzig-descent augmentation algorithms only guarantee t hat we reach a feasible solution xk with
objective value “close enough” to the optimal value. Whethe r any given feasible solution is “close
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
6
enough” can be checked by generating a vertex of the feasible region with objective value that is
at least as good as c⊺xk. Finding such a vertex can be done by augmenting xk only along such
(discrete deepest-/Dantzig-descent) circuit directions that lead to a better feasible solution with an
additional component reaching its lower or upper bound. Geo metrically, this corresponds to (iter-
ative) augmentation within the smallest face of the polyhed ron { x : Ax = b, 0 ≤ x ≤ u, x ∈ Rn }
that contains xk. (The circuits of the problem matrix A provide such a restricted optimality certiﬁ-
cate). We recommend the example in [ 19]. Finally, again using the circuits of A, it can be checked
whether the vertex found is optimal. The overall closeness- test requires at most n augmentations.
Finally we present the interesting consequences of the main theorems. Note that the bounds in
part (c) of Theorems 1 and 2 only depend on A, but not on b, c, and the particular initial feasible
solution x0 chosen. As a direct consequence of Part (b) of Theorem 1, we obtain the following
corollaries.
Corollary 1. For the pure 0/1 ILP min { c⊺x : Ax = b, 0 ≤ x ≤ 1, x ∈ Zn } the number of
discrete deepest-/Dantzig-/steepest-descent augmentations is bounded by O(n log(‖c‖1)).
We note that in the LP case, the proof of Theorem 2, part (c), immediately gives Bland’s
fundamental result:
Corollary 2 (Bland’s Theorem). The number of discrete steepest-descent augmentations
needed to solve min { c⊺x : Ax = b, 0 ≤ x ≤ u, x ∈ Rn } is bounded by the number of (diﬀerent) posi-
tive values of −c⊺z/‖z‖1 over all (elementary vectors) z ∈ C(A) times the number n of variables.
As for totally-unimodular matrices A, C(A) = G(A), i.e., they coincide for the LP and ILP cases,
the proof of Theorem 2, part (c), also implies:
Corollary 3. For totally-unimodular matrix A, the number of discrete steepest-descent aug-
mentations needed to solve min { c⊺x : Ax = b, 0 ≤ x ≤ u, x ∈ Zn } is bounded by the number of (dif-
ferent) positive values of −c⊺z/‖z‖1 over all (elementary vectors) z ∈ C(A) times the number n of
variables.
For a totally-unimodular matrix A, C(A) consists only of vectors with (at most d + 1) entries
in { −1, 0, 1 } Thus, for z ∈ C(A) we have | − c⊺z| ≤ ‖c‖1 and ‖z‖1 takes on at most d + 1 diﬀerent
values. Plugging this into Corollary 3 we get the following.
Corollary 4. For totally-unimodular matrix A, the number of discrete steepest-descent aug-
mentations needed to solve min { c⊺x : Ax = b, 0 ≤ x ≤ u, x ∈ Zn } is bounded by n(d + 1)‖c‖1.
From this we immediately recover the complexity bound for th e algorithm of Edmonds and Karp
to ﬁnd maximum ﬂows in a network: let A be the node/arc-incidence matrix of a connected directed
graph. Note that one row of A is linearly dependent on the other rows and thus can be remove d
from A. Then n = |E| and d = |V | − 1. As we maximize the ﬂow on a speciﬁc (auxiliary) arc (from
sink to source), we have ‖c‖1 = 1. Thus, n(d + 1)‖c‖1 = |E| · |V | bounds the number of discrete
steepest-descent augmentations to solve the max-ﬂow probl em. This observation is not surprising,
as the augmentation approach using Graver bases specialize s to the algorithm by Edmonds and
Karp in the setting of maximum ﬂows.
It is worth recalling that although the complexity statemen ts in Corollary 1 and Corollary 4
depend on the unary size of c, these two results actually can be improved based on the resu lts
of Frank and Tardos [ 16]. Frank and Tardos used Diophantine approximation to repla ce c with a
new objective function c′ where the integer numbers occurring in the entries are small but deﬁne
an equivalent problem with the same optima. Furthermore, th e new weight function c′ can be
found in strongly polynomial-time. In conclusion, if we are able to generate in polynomial time the
corresponding augmentation elements of the Graver basis ac cording to one of the three rules, we
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
7
obtain strongly polynomial-time algorithms. Of course, th is is in general hard to do other than by
computing the entire Graver basis, but for special matrices A, one can do much better.
Our results on augmentations for totally-unimodular matri ces provide another interesting geo-
metric result. For years, researchers have been looking at t he diameter of the graph of polyhedra
(i.e., the graph whose nodes are the vertices of the convex po lyhedron P = {x : Ax = b, 0 ≤ x ≤ u}).
It has been shown in [ 9] that the diameter of the graph of totally-unimodular d-dimensional poly-
topes (i.e., the length of the longest shortest path between a pair of nodes) is bounded above by
d3. 5 log(d). We wish to stress that in our circuit augmentations, we do n ot always follow edges of
the polyhedron P . Rather, we may cut through the interior of P or the interior of some faces. This
suggests the notion of circuit diameter . The circuit distance from v1 to v2 is the smallest number
of circuit augmentations needed to go from v1 to v2. We can then deﬁne the circuit diameter as
the maximum number of steps along circuit basis directions t hat are needed to go from any vertex
of the polyhedron to any other vertex of the polyhedron. This notion was ﬁrst introduced and
investigated in the article [ 10]. More recently other generalizations of the notion of diam eter using
circuits were introduced in [ 11]. One can show that the circuit diameter of a polyhedron is bo unded
from above by the usual combinatorial diameter of polyhedra (this is because arcs are themselves
some of the possible augmentation directions, a subset of th e circuits). In this context, our results
show that one can bound the circuit diameter for totally-unimodular polytopes in standard form
as follows
Corollary 5. For a d × n totally-unimodular matrix A, the circuit diameter of the polyhedron
P := { x : Ax = b, 0 ≤ x ≤ u} is bounded above by 2(n(d + 1)(n − d)).
This corollary is a good general bound for totally-unimodul ar matrices, but we suspect it can be
further improved, as we already know that for network-ﬂow po lytopes a better bound is possible.
Indeed, Orlin [ 28] designed a polynomial-time primal network-simplex algor ithm for the minimum-
cost ﬂow problem which gives a graph-diameter bound of O(|E||V | log(|V |)), with E, V equal to
the sets of of arcs and nodes in the network.
Proof: To see this, take any vertex v of P . Choose a cost vector speciﬁc to v: namely, let ci = 1
if vi = 0 and ci = −1 if vi = ui. Otherwise, put ci = 0. Thus, this new objective function c has n − d
= n − rank(A) many nonzero entries. Thus, by Corollary 4, with the steepest-descent rule, any
other vertex is connected to v with no more than n(d + 1)(n − d) many augmentations. Hence, the
path between any pair of vertices of P is bounded by 2 n(d + 1)(n − d). □
Finally, let us consider optimization problems for which th e constraint matrix is structured.
Recall that an N -fold matrix is a matrix of the form
[A, B](N ) :=


B B · · · B
A O O
O A O
. . .
O O A


.
For ﬁxed matrices A and B, the size of the Graver basis of [ A, B](N ) (and its binary encoding
length) increases only polynomially with N . Combining this with Theorems 1 and 2, parts (c), we
obtain the following result.
Theorem 3. For ﬁxed matrices A and B, the associated families of N -fold LPs and ILPs can
be solved in strongly polynomial time.
This generalizes the results from [ 20, 21], which showed that for ﬁxed matrices A and B, the
corresponding N -fold ILPs could be solved in time polynomial in N , in fact in O(N 3) steps.
Theorem 3 strengthens this to strong polynomiality. As a direct conse quence we obtain the following
results:
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
8
Corollary 6. The following special cases of N -fold matrices can be solved in strongly poly-
nomial time in the linear and integer case:
• All 2-way transportation problems with a ﬁxed number of rows or co lumns.
• All 3-way transportation problems with two of the three dimensio ns ﬁxed.
• All d-way transportation problems with d − 1 dimensions of ﬁxed constant value.
