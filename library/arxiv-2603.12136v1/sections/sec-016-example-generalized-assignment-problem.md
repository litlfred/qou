---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-016-example-generalized-assignment-problem
section_title: "Example: Generalized Assignment problem"
section_number: null
pages: 45-48
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Consider the generalized assignment problem, where one computes an assignment of
Jitems with sizesa j, j∈JtoIknapsacks with capacityC i such that we maxi-
mize the sum of profitsP
j∈Jcj such that the capacities on the knapsacks are not
exceeded. This can be modeled as an integer program using the binary variables
xij =
(
1ifjis packed into knapsacki
0otherwise for alli∈I,j∈J.
max
X
i∈I
X
j∈J
cjxij (14a)
s.t.
X
j∈J
ajxij≤C i ∀i∈I(14b)
45
X
i∈I
xij≤1∀j∈J(14c)
xij∈{0,1} ∀i∈I,∀j∈J(14d)
Now, suppose that there exist identical itemsj∈Jthat have the same weight and
cost. LetK={K 1,...,K n}be a partition ofJintonitem sets that have identical
cost and weight. Clearly,n≤|J|must hold, and by definition we have thataK =a j
andc K =c j for anyj∈K, for anyK∈K. Let the variable partitionQbe given by
the partsQiK ={x ij|∀j∈K}fori∈I,K∈K, where identical items are placed
into the same part. LetPbe a constraint partition where all constraints (14c) and
(14d) belonging to identical items are placed into the same partitionP∈Pand all
other constraints are given their own partition. Then, it can be verified that(P,Q)
is an equitable partition of the generalized assignment problem in (14). Applying the
reformulation suggested by the equitable partition we obtain a smaller formulation:
max
X
i∈I
X
K∈K
cKyiK (15a)
s.t.
X
K∈K
aKyiK≤C i ∀i∈I(15b)
X
i∈I
yiK≤|K| ∀K∈K(15c)
yik∈{0,1,···,|K|} ∀i∈I,∀K∈K(15d)
Now, suppose that we are given any integral solutiony⋆ to the reduced problem.
For these values, we wish to recover a solution in thex-space. Then, we can add the
constraints (16d), that link thexvariables toy⋆, and hope to recover a solution forx.
max
X
i∈I
X
j∈J
cjxij (16a)
s.t.
X
j∈J
ajxij≤C i ∀i∈I(16b)
X
i∈I
xij≤1∀j∈J(16c)
X
j∈K
xij =y ⋆
iK ∀i∈I,∀K∈K(16d)
xij∈{0,1} ∀i∈I,∀j∈J(16e)
We can substitute the equations (16d) into the constraints (16b) and the objective
(16a).
46
max
X
i∈I
X
K∈K
cKy⋆
iK (17a)
s.t.
X
K∈K
aKy⋆
iK≤C i ∀i∈I(17b)
X
i∈I
xij≤1∀j∈J(17c)
X
j∈K
xij =y ⋆
iK ∀i∈I,∀K∈K(17d)
xij∈{0,1} ∀i∈I,∀j∈J(17e)
Note that in (17), both the objective and the knapsack constraints are not dependent
onxanymore. In fact, by feasibility ofy ⋆, all constraints in (17b) are feasible by
feasibility of (15b). Then, we observe that the remaining problem is given by an
assignment problem on thexvariables. Since the constraints (17c), (17d) form a
totally unimodular matrix and the right-hand side given by1andy⋆ is integral, the
LP relaxation of (17) is integral. Moreover, the solution¯xij = y⋆
iK
|K| for alli∈I,K∈K
such thatj∈Kis feasible for the LP relaxation of (17) by Proposition 3. Thus, an
integral solutionxcan be obtained by finding a vertex solution of the LP relaxation
of (17).
The reformulation of (16) into (17) can be seen as exhibiting an affine TU
decomposition. The rows of the constraints (17d) correspond to theT-matrix, and
their substitution in (17b) corresponds to theU-matrix. The rows of (17c) form the
nonzeros of theS-matrix. Additionally, note that the usage of the equations to cancel
the nonzeros in the objective is possible due to the fact that the objective vector is
equitably partitioned byQ.
There are a few interesting observations that can be made about the generalized
assignment problem. First of all, as also implied by Salvagnin [9], the used equitable
partition is not necessarily the coarsest equitable partition. Suppose for example, that
for all knapsacksi∈Ithe capacityC i is equal to some constantC. Then, the knapsack
constraints (14c) have additional permutation symmetries which permute the items
between the bins. These symmetries are also captured by the coarsest equitable parti-
tion since equitable partitions generalize permutation symmetries. Consequently, for
the coarsest equitable partition(P,Q),Qcontains variablesx ij belonging to multiple
bins inI. In the case where one would reformulate (14) using orbital shrinking, the
orbital shrinking subproblem would then become theNP-hard binpacking problem, in
contrast to the polynomial-time solvable assignment problem that we derive here. Sal-
vagnin shows in [9] that for the generalized assignment model, employing a constraint
programming solver to solve the binpacking subproblem and additionally reformulat-
ing the symmetric knapsacks yields better performance than the reformulation with
the assignment problem that we derive here.
47
Secondly, we note that there is a minor way to improve the postsolve subproblem
in (17). LetK 1 :={K∈ K |a K = 1}andJ 1 :={j∈J|a j = 1}denote the
set of items with weight1. For these items, it is not necessary to fix them to their
correspondingy ⋆
iK value in (17). In particular, if we change the equalities in (17d) to
only be added for allK\K 1, and substitute only all items with non-unit weight in
(17b), we obtain the following reformulation.
max
X
i∈I
X
J∈J 1
cjxij +
X
i∈I
X
K∈K\K 1
cKy⋆
iK (18a)
s.t.
X
j∈J 1
xij≤C i−
X
K∈K\K 1
aKy⋆
iK ∀i∈I(18b)
X
i∈I
xij≤1∀j∈J(18c)
X
j∈K
xij =y ⋆
iK ∀i∈I,∀K∈K\K 1 (18d)
xij∈{0,1} ∀i∈I,∀j∈J(18e)
It is not difficult to see that (18) is still a perfect formulation. The constraint
matrix defined by (18b)–(18d) is totally unimodular as it is the node-edge incidence
matrix of a bipartite graph and the right-hand sides are integral. The two parts of
the bipartition are given by constraints (18c) and ((18b) plus (18d)), respectively.
The fixings forK1 can be left out due to the fact that the variables inJ1 are implied
integer. LetPbe the linear relaxation of (14). Then total unimodularity of (18) shows
by affine TU decomposition thatconv(P∩Z n) = conv({x∈P| P
j∈Kxij∈Z,∀i∈
I,∀K∈K\K 1})holds. From this equality it also follows thatyiK is implied integer
for alli∈Iand allK∈K 1 by the other variables in (15). One way in which this
additional power from implied integrality manifests is that in contrast to (17), solving
(18) may give a stronger solution than the providedy⋆ solution, ify ⋆ is suboptimal
and one of the itemsj∈J 1 can still be assigned to some knapsack. This correspond
to having the proper subsetQ′⊂Q I in the statement of Theorem 32.
