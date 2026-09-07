---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-017-822-convergence-bounds
section_title: "Convergence bounds"
section_number: 8.2.2
pages: 31-33
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
We now state the convergence bounds from [ DLHL15]. The original statement refers to subde-
terminant bounds; we paraphrase them in terms of ﬁnding appr oximately optimal solutions.
Theorem 8.2 (De Loera, Hemmecke, Lee [ DLHL15]). Consider a linear program in the form
LP(A,b,c,u ). Assume we are given an initial feasible solution x(0), and let OPT denote the
optimum value. By an ε- optimal solution we mean an iterate x(t) such that
⟨
c,x (t)⟩
≤ OPT +ε.
(a) For given ε > 0, one can ﬁnd an ε-optimal solution in 2n log2
(
⟨c,x(0)⟩−OPT
ε
)
deepest-
descent augmentations.
(b) For given ε >0, one can ﬁnd an ε-optimal solution in 2n2γ
ε log2
(
⟨c,x(0)⟩−OPT
ε
)
Dantzig-
descent augmentations, where γ is an upper bound on the maximum entry in any feasible
solution.
(c) One can ﬁnd an exact optimal solution in min{n|CA|,ℓA} steepest-descent augmentations,
whereℓA denotes the number of distinct values of ⟨c,g⟩/‖g‖1 over g∈F (A).
In general, circuit augmentation algorithms may not even ﬁn itely terminate; see [ MS00] for
an example on Wallacher’s rule for minimum cost ﬂows. In part s (a) and (b), assume that all
basic solutions are 1/k-integral for some k∈ Z and cost function is c∈ Zn. If x(t) is a ε-optimal
solution for ε< 1/k, then we can identify an optimal vertex of the face containin g x(t) using a
Carath´ eodory decomposition argument, this can be impleme nted by a sequence of ≤ n circuit
augmentations (see [ DLHL15, Lemma 5]).
According to part (c), steepest descent terminates with an optimal solution in a ﬁ nite number
of iterations; moreover, the bound only depends on the linea r space ker( A) and c, and not on
the parameters b and u. However, the bound can be exponentially large.
Bland’s original observation was that ℓA is strongly polynomially bounded for the maximum
ﬂow problem. Recall that all elementary vectors g correspond to cycles in the auxiliary graph.
31
Normalizing such that gi∈{ 0,±1},−⟨c,g⟩ = 1 for every augmenting cycle (as these must use
the (t,s ) arc), and ‖g‖1 is between 1 and |E|. In fact, the crucial argument by Edmonds and
Karp [ EK72] and Dinic [ Din70] is showing that the length of the shortest augmenting path i s
non-decreasing, and must strictly increase within |E| consecutive iterations.
For an integer cost function c∈ Zn, Lee [ Lee89, Proposition 3.2] gave the following upper
bound on ℓA:
Proposition 8.3. If‖c‖1≤ (n−m + 1)‖c‖∞, then
ℓA≤ 1
2‖c‖∞(n−m + 1)¯κA((n−m + 1)¯κA + 1).
In order to bound the circuit distance between vertices x and y let us use the following cost
function. For the basis B deﬁning y, let
ci =



0 if i∈B,
1 if i∈ [n]\B,yi = 0,
−1 if i∈ [n]\B,yi =ui.
(23)
With this cost function, Theorem 8.2(c) and Proposition 8.3 yield a bound O((n−m)2¯κ2
A) on
the circuit diameter using the steepest descent algorithm.
Extending the analysis of the Goldberg-Tarjan algorithm [ GT89], we present a new bound
that only depends on the fractional circuit imbalance κA, and is independent of c. The same
bound was independently obtained by Gauthier and Derosiers [GD21]. The proof is given in
Section 8.4.
Theorem 8.4. For the problem LP(A,b,c,u ) with constraint matrix A∈ Rm×n, the steepest-
descent algorithm terminates within O(n2mκA log(κA +n)) augmentations starting from any
feasible solution x(0).
This improves on the above bound O((n−m)2¯κ2
A) for most values of the parameters (recall
that κA≤ ¯κ2
A). Moreover, this bounds the running time for steepest desce nt for an arbitrary
cost function c, not necessarily of the form ( 23).
Both these bounds are independent of b, however, κA and ¯κA may be exponentially large
in the encoding length LA of the matrix A. In contrast, Theorem 8.2(a) yields a polynomial
bound O(nLA,b) on the number of deepest-descent iterations, where LA,b is the encoding length
of (A,b ). In what follows, we review a new circuit augmentation algo rithm from [ DKNV21] that
achieves a log κA dependence; the running time is bounded as O(n3LA), independently from b.
8.3 A circuit augmentation algorithm with log κA dependence
Recall that the diameter bound Theorem 8.1 is non-algorithmic in the sense that the augmen-
tation steps rely on knowing the optimal solution x∗. Dadush et al. [ DKNV21] complemented
this with an eﬃcient circuit augmentation algorithm, assum ing oracles are provided for certain
circuit directions.
Theorem 8.5 ([DKNV21]). Consider the primal of LP(A,b,c ). Given a feasible solution, there
exists a circuit augmentation algorithm that ﬁnds an optima l solution or concludes unbounded-
ness using O(n3 log(n +κA)) circuit augmentations.
The main circuit augmentation direction used in the paper fo r optimization is a step deﬁned
as Ratio-Circuit, a generalisation of the previously mentioned augmentatio n step by Wallacher
[Wal89] for minimum cost ﬂows. It ﬁnds a circuit that is a basic optim al solution to the following
linear system:
min⟨c,z⟩ s.t. Az = 0,
⟨
w,z −⟩
≤ 1. (24)
32
Equivalently, the goal is to minimize the cost to weight rati o of a circuit, where the unit weight
of increasing a variable xi is 0 and decreasing it is wi. This can be seen as an eﬃciently
implementable relaxation of the deepest-descent directio n: for suitable weights, it achieves a
geometric decrease in the objective value. For a vector x∈ Rn
+, we let 1/x∈ (R∪{∞} )n denote
the vector w with wi = 1/xi (in particular, wi =∞ if xi = 0).
Lemma 8.6 ([MS00]). Let OPT denote the optimum value of LP(A,b,c ). Given a feasible
solution x to LP(A,b,c ), let g be the elementary vector returned by Ratio-Circuit(A,c, 1/x),
and x′ the next iterate. Then,
⟨
c,x ′⟩
− OPT≤
(
1− 1
n
)
(⟨c,x⟩− OPT) .
Proof. Let x∗ be an optimal solution to LP(A,b,c ), and let z = (x∗−x)/n. Then, z is feasible
to ( 24) for w = 1/x. The claim easily follows by noting that ⟨c,g⟩≤⟨ c,z⟩ = (OPT−⟨c,x⟩)/n,
and noting that x +g is feasible since ⟨1/x,g −⟩≤ 1.
Repeated application of a Ratio-Circuit step thus provide an iterate whose optimality gap
decreases by a constant factor within O(n) iterations. However, as noted in [ MS00], using only
this rule does not even ﬁnitely terminate already for minimu m cost ﬂows.
Support Circuits For this reason, [DKNV21] occasionally uses a second circuit augmentation
step called Support-Circuit. Roughly speaking, when given a non-basic feasible point in the
system LP(A,b,c ), one can eﬃciently augment around a circuit g such that ⟨c,g⟩ ≤0 and
thereby reduce its support while maintaining the objective .
On a high level, the need for such an operation becomes clear w hen considering following
example. Assume c≡ 1 and further assume that we are given an iterate x with‖x‖≫ κA‖y‖
for some basic solution y. Then geometric progress in the objective ⟨c,x⟩ can be achieved by
just reducing the norm of x, but just geometric progress would not give the desired boun d in the
number of circuit augmentations. Note that the norm of all ba sic solutions lies within a factor of
poly(n)κA‖y‖ by Proposition 3.1. Therefore, it is helpful to reduce the support through at mo st
n Support-Circuit operations until a basic solution is reached instead of appl ying Ratio-
Circuit. Subsequent applications of Ratio-Circuit will now, again due to Proposition 3.1,
not be able to reduce the norm of x by more than a factor of poly( n)κA, a fact that will be
exploited in the proximity arguments.
The main progress in the algorithm in Theorem 8.5 is identifying a new index i such thatxi =
0 in the current solution and x∗
i = 0 in any optimal solution x∗. Such a conclusion derives using
a variant of the proximity theorem Theorem 6.5. To implement the main subroutine that ﬁxes a
variable to xi = 0, a careful combination of Ratio-Circuit and Support-Circuit iterations
is used. Interestingly, the Ratio-Circuit iterations do not use the original cost function c, but
a perturbed objective function c′. The main progress in the subroutine is identifying new ‘lar ge’
variables, similarly to the proof of Theorem 8.1. Perturbations are performed whenever a new
large variable xj is identiﬁed.
