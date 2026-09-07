---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel §"
section_id: sec-004-graver-bases-and-directed-augmentation
section_title: "Graver bases and directed augmentation"
section_number: null
pages: 8-11
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
doc_brief: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel § — In this article we study a broad class of integer programming problem s in variable dimension."
---
Consider the following family IP A of integer programs in standard form, with arbitrary demand vector
b ∈ Zm and arbitrary objective vector c ∈ Zn, sharing the same constraint matrix A ∈ Zm×n,
IPA(b, c ) : min {cx : Ax = b, x ∈ Nn}.
A universal test set for the family IP A is a ﬁnite subset G of the lattice L(A) := {x ∈ Zn : Ax = 0}
of dependencies on A such that whenever x is feasible but not optimal for IP A(b, c ) (where b := Ax),
there is an improving direction g ∈ G, namely such that x − g is feasible and better, that is, x − g ∈ Nn
and cg > 0. Thus, a universal test set enables the solution of the foll owing augmentation problem.
Augmentation problem. Given A ∈ Zm×n, x ∈ Nn and c ∈ Zn, either ﬁnd an improving direction
g ∈ Zn, namely one with x − g ∈ {y ∈ Nn : Ay = Ax} and cg > 0, or assert that no such g exists.
An augmentation oracle for a matrix A is one that solves the augmentation problem, that is, when
queried on x ∈ Nn and c ∈ Zn, it either returns an improving direction g or asserts that none exists.
Clearly, an explicit universal test set G for A enables the eﬃcient realization of an augmentation
oracle for A by simply searching for an improving direction g ∈ G. An oracle solving the augmentation
problem, and in particular, an explicit universal test set G, enable the following simple iterative
procedure that, for any program IP A(b, c ) in IP A with bounded objective function, converts any
feasible x to an optimal one: “while there exists an improving directio n g set x := x − g and repeat”.
In 1975, Graver [9] constructed, for every integer matrix A, a canonical universal test set. The
Graver basis G(A) of A can be deﬁned as follows. First, we need to extend the partial ordering ≤ from
Nn to Zn. For u, v ∈ Zn we say that u is conformal to v, denoted u ⊑ v, if |ui| ≤ | vi| and uivi ≥ 0 for
i = 1, . . . , n , that is, u and v lie in the same orthant of Rn and each component of u is bounded by the
corresponding component of v in absolute value. With this, G(A) consists precisely of all ⊑-minimal
vectors in L(A) \ {0}. For a more detailed introduction of Graver bases we refer to [10]. The currently
fastest algorithm to compute Graver bases, based on a comple tion procedure and a project-and-lift
approach, is described in [11] and implemented in the softwa re package 4ti2 [12].
The Graver basis, being a universal test set, provides an aug mentation oracle and hence enables
to convert any feasible solution to an optimal one for any IP A(b, c ) by the iterative augmentation
8
procedure above. But this in itself is not enough to guarante e an eﬃcient (polynomial time) solution:
a major remaining question is how many augmentation steps ar e needed to reach an optimal solution.
Recently, in [21], a directed version of the augmentation pr oblem was introduced; quite remarkably,
it was shown that the number of directed augmentation steps needed to reach optimality is polynomia l.
We discuss this next. First, we deﬁne the directed augmentat ion problem.
Directed augmentation problem. Given A ∈ Zm×n, x ∈ Nn and c′, c ′′ ∈ Zn, either ﬁnd g =
g+ − g− ∈ Zn satisfying x − g ∈ {y ∈ Nn : Ay = Ax} and c′g+ − c′′g− > 0, or assert that none exists.
Here and throughout, g+, g − ∈ Nn denote the positive and negative parts of g ∈ Zn, deﬁned by
g+
i := max {gi, 0} and g−
i := − min{gi, 0} for i = 1 , . . . , n . Thus, the directed augmentation problem
involves two objective function vectors: c′ controls the cost of the positive part of g and c′′ controls the
cost of the negative part of g. The usual augmentation problem occurs as the special case c′ = c′′ = c.
A directed augmentation oracle for A is one that solves the directed augmentation problem, i.e. w hen
queried on x ∈ Nn, c′, c ′′ ∈ Zn, it either returns an improving direction g or asserts that none exists.
In [21], it was assumed that the input includes an upper bound vector u ∈ Nn on the variables, so
that the actual feasible set is {y ∈ Nn : Ay = Ax, y ≤ u}. Under this assumption, the feasible region
is always bounded and there is always an optimal solution. Fu rther, the complexity estimates in [21]
depended on the bit size of u and b := Ax. However, this is not really needed. Consider the integer
program IP A(b, c ) : min {cy : Ay = b, y ∈ Nn} with b = Ax. Its objective function is bounded (and
hence there is an optimal solution) if and only if it is bounde d for the corresponding LP-relaxation
min{cy : Ay = b, y ∈ Rn
+}, which can be checked in polynomial time by linear programmi ng.
Furthermore, whenever IP A(b, c ) has an optimal solution, it has one of bit size polynomially bounded
in the size of A and b = Ax; this basically follows from Cramer’s rule, see e.g. [20, Se ction 17.1].
Therefore, it is possible to compute an upper bound u in terms of A and x only, and plug it into the
analysis of [21]; for instance, uk := m! n(n + 1)(max |xj|)(max |Ai,j|)m for k = 1, . . . , n will do.
With this, the results of [21] imply the following.
Proposition 3.1 There is a polynomial oracle time algorithm that, given A ∈ Zm×n, x ∈ Nn, c ∈ Zn,
solves the integer program IP A(b, c ) with b := Ax by querying a directed augmentation oracle for A.
Here, as usual, solving the (feasible) integer program means that the algorithm eit her returns an
optimal solution or asserts that the objective function is u nbounded; and polynomial oracle time
means that the number of arithmetic operations, the number o f calls to the oracle, and the size of the
numbers occurring throughout the algorithm are polynomial ly bounded in the size of the input A, x, c .
It is not hard to see that if the matrix A is totally unimodular, in particular the incidence matrix o f
9
a directed graph, then a directed augmentation oracle for A can be realized using linear programming.
However, in general it is not clear which matrices A admit eﬃcient directed augmentation.
As explained above, the Graver basis of a matrix A yields an augmentation oracle for A. We now
show that, moreover, it enables the realization of a directe d augmentation oracle for A as well.
Lemma 3.2 Let G(A) be the Graver basis of A ∈ Zm×n. For any x ∈ Nn and c′, c ′′ ∈ Zn, there is a
g ∈ Zn with x − g ∈ {y ∈ Nn : Ay = Ax} and c′g+ − c′′g− > 0 if and only if there is such g ∈ G (A).
Proof. Suppose g is an improving direction. Then g ∈ L (A) \ {0} and hence can be written as a
conformal sum of (not necessarily distinct) elements of the Graver basis o f A, that is, g = ∑ gi with
gi ⊑ g and gi ∈ G (A) for all i. To see this, recall that G(A) is the set of ⊑-minimal elements in
L(A) \ {0} and note that ⊑ is a well-ordering; if g ∈ G (A), we are done; otherwise there is an h ∈ G (A)
with h ⊏ g in which case, by induction on ⊑, there is a conformal sum g−h = ∑ gi giving g = h+∑ gi.
Now, gi ⊑ g is equivalent to ( gi)+ ≤ g+ and ( gi)− ≤ g−, so the conformal sum g = ∑ gi gives
corresponding sums of the positive and negative parts g+ = ∑ (gi)+ and g− = ∑ (gi)−. Consequently,
0 < c ′g+ − c′′g− = c′ ∑
(gi)+ − c′′ ∑
(gi)− =
∑
(c′(gi)+ − c′′(gi)−) ,
which implies that there is some gi in this sum with c′(gi)+ − c′′(gi)− > 0. Now, gi ∈ G (A) ⊂ L(A) so
Agi = 0 and hence A(x − gi) = Ax. Finally we show that x − gi ≥ 0: if gi
j ≤ 0 then xj − gi
j ≥ xj ≥ 0;
and if gi
j > 0 then gi ⊑ g implies gi
j ≤ gj and thus xj − gi
j ≥ xj − gj ≥ 0, the last inequality holding
because g is an improving direction. So gi ∈ G (A) is an improving direction in the Graver basis. □
As an immediate corollary of Proposition 3.1 and Lemma 3.2, w e get the following statement.
Theorem 3.3 There is a polynomial time algorithm that, given any matrix A ∈ Zm×n along with its
Graver basis G(A), and vectors x ∈ Nn and c ∈ Zn, solves the integer program IP A(b, c ) with b := Ax.
While Theorem 3.3 holds for any matrix, its complexity bound depends on the size of the Graver
basis which is part of the input. Typically, the Graver basis is very large and its cardinality may be
exponential in n. However, in the next section we show that for a broad and usef ul class of matrices,
we can tame the behavior of the Graver basis, leading to an eﬃc ient algorithm in terms of A, x, c only.
10
