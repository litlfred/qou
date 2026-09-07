---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-5
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
In many problems in mathematical optimization, symmetries arise naturally. For
the representative MIPLIB 2017 collection [1], at least 47% of the instances in the
collection contains some permutation or reflection symmetry [2]. Symmetry can pose
a serious challenge for (spatial) branch-and-cut algorithms in mixed-integer linear
programming (MILP) and mixed-integer nonlinear programming (MINLP). If sym-
metries are not handled adequately, they may cause a branch-and-cut algorithm to
repeatedly explore symmetric parts of the search space [3]. In the worst case, all sym-
metric solutions to a problem are enumerated, which can cause a major performance
degradation in the branch-and-cut algorithm, and make it difficult to solve the given
optimization problem efficiently.
Previous works that develop symmetry handling methods for mathematical opti-
mization can loosely be categorized into two categories. The first category consists of
symmetry handling methods that remove symmetries from the problem formulation
byprojection, which remove symmetric parts of the feasible region by projecting onto
the fixed space of the symmetry group. By doing so, one obtains a symmetry-free
formulation with fewer variables and constraints, which is attractive from a compu-
tational perspective. This method is used primarily for convex optimization problems
such as linear programming [4] and semidefinite programs [5].
In contrast to the symmetry handling methods for convex optimization problems,
mixed-integer linear programming solvers typically handle symmetry bybreakingit,
either through specialized branching rules [6] or by adding valid inequalities [7]. Due
to the non-convexity of the integrality constraints, the projection-based methods used
for convex optimization problems no longer apply as they do not necessarily preserve
integrality. Although breaking symmetries is still very popular for mixed-integer lin-
ear programming, a few recent works, such as the work on Orbital Shrinking [8–10],
challenge the idea that symmetry handling methods for mixed-integer linear pro-
gramming must necessarily break symmetry. This work falls into the same category
and formulates symmetry-handling methods that bridge the gap between the strong
symmetry handling methods for linear programs to the more challenging setting of
mixed-integer linear programs. As our main result, we show that the strong dimension
reduction method for linear programs from [11] can be extended to mixed-integer
linear programs. Secondly, we show that the dimension reduction method from [11]
can be extended to include the class of reflection symmetries, which generalizes the
permutation symmetries that are handled by their dimension reduction method.
Next, we consider some of the relevant previous works in further detail.
Symmetry handling for linear programs
For linear programs, Bödi, Herr and Joswig [4] show that one can exploit the con-
vexity of the linear program by projecting the linear program onto the fixed space of
its symmetry group. This method is computationally attractive, as it both removes
the symmetries from the linear program and reduces its dimension. Furthermore,
Bödi, Herr and Joswig present an algorithm that exploits the projection onto the
2
fixed space to solve highly symmetric integer programs whose symmetry group is
(almost) transitive. Their work was inspired by the symmetry handling for Semidef-
inite Programs [5, 12, 13], where symmetries of Semidefinite Programs are exploited
by applying results from invariant theory and representation theory to reduce the
dimensions of the Semidefinite Programs.
One downside of projecting onto the fixed space of the symmetry group is that
the computation of the symmetry group of the Linear Program may be too expensive
compared to simply solving the symmetric original program. Typically, the symmetry
group is computed by detecting automorphisms of an auxilliary graph representing
the (Mixed-Integer) Linear Program [3]. The exact complexity of the graph auto-
morphism problem is unknown, and no polynomial time algorithms are known [14].
However, there are several software packages such asbliss[15],nauty[16] and
saucy[17] that can handle large graphs in practice.
Grohe, Kersting, Mladenov and Selman [11] observed that instead of computing
the symmetry group via graph automorphism on an auxilliary graph, it is sufficient to
run a color refinement method to reduce the dimension of the underlying LP, which
they callDimension Reduction via Color Refinement(DRCR). Some sources also
refer to their technique asLP foldingorweak symmetry. Their approach has two key
advantages compared to the projection onto the fixed space of the symmetry group.
First of all, it generalizes the handling of permutation symmetries and may provide
additional reductions. Secondly, the color refinement approach is fast in theory and
fast in practice since it runs in linearithmic time. One downside of DRCR is that the
color refinement algorithm presented in [11] only detects permutation symmetries,
whereas Bödi, Herr and Joswig [4] show that projecting to the fixed space of the
symmetry group works for the more general linear symmetry group. However, this is
not a major limitation in practice, as the majority of symmetries in (Mixed-Integer)
Linear Programs are permutation symmetries [2]. The developers of the FICO Xpress
solver report that after implementing DRCR that they ‘observed improvements of
an average of up to 30% on standard LP benchmark sets’ [18]. In this case, the
average is a somewhat skewed measure; for the affected linear programming models
that can be reformulated, applying DRCR even leads to solving times that are ‘often
more than 5 times as fast on average’. However, the technique is only applicable to
a limited set of models, which make up roughly 10% of their test set. Similar results
are reported by Gurobi [19]. To the best of our knowledge, DRCR has currently not
yet been implemented in any open source solver. This is somewhat surprising, as a
speedup of up to 30% for linear programming solvers from a single technique is very
rare. DRCR can be considered one of the most important algorithmic advances for
linear programming software in the last 15 years.
Symmetry handling for mixed-integer linear programming
Although the symmetry handling methods for Linear Programming are very powerful,
they are unfortunately not directly applicable to Mixed-Integer Linear Programming,
as the dimension reduction by projecting to the fixed space relies on the convex-
ity of the problem. For Mixed-Integer Linear Programs, the non-convex integrality
3
constraints invalidate the use of the reduction. Instead, there is a vast collection of
symmetry handling methods, where most methods handle symmetry by breaking it
in a static or dynamic fashion. Some methods attempt to eliminate the symmetry
by adding symmetry-breaking constraints [7, 20]. Other methods, such as Isomor-
phism Pruning [21, 22] or Orbital Branching [6, 23] handle symmetry dynamically by
pruning symmetric branches from the branch-and-bound tree. For a more complete
overview, we refer the reader to the surveys by Margot [3] and Pfetsch and Rehn [24].
One symmetry handling method that does not break symmetry is discussed by
Pfetsch and Rehn. They consider the fixing of continuous variables to the fixed space
of the symmetry group whose automorphisms only permute the continuous variables.
From their experiments, they conclude that “fixing the continuous variables slightly
speeds up LP-solving, but does not result in a significant overall speed-up” compared
to other symmetry handling methods.
One method for symmetry handling for MILP which is relevant to the current work
isOrbital Shrinking, which was introduced by Fischetti and Liberti [8], and whose
theory was later solidified in [10]. The key idea of Orbital Shrinking is to aggregate
variables in each orbit of the symmetry group to a single variable per orbit to obtain
a smaller mixed-integer program. This is similar to the projection to the fixed space
of the symmetry group for linear programs, which also aggregates variables in each
orbit. However, due to the non-convexity of the integrality constraints, the reduced
mixed-integer problem defines a relaxation of the original problem. Thus, solutions
to the relaxed problem are checked by solving a subproblem to check feasibility in
the original model. Frequently, this feasibility problem is solved using Constraint
Programming techniques [9, 25]. Because orbital shrinking defines a relaxation, any
dual bound generated for the relaxed model is also valid for the original model. Due
to the smaller size of the relaxed model and the fact that the reduced model contains
fewer/no symmetries, the computed dual bounds from the reduced model are typically
quite strong for highly symmetric instances [9, 25].
Another innovative method for MILP that preserves symmetry is the core point
method [26], which extend the more theoretical work by Bödi, Herr and Joswig [4].
Although they do show that their algorithm is effective for integer programs with
(nearly) transitive symmetry groups, their algorithm does not perform as well as
orbital branching on arbitrary MILP instances. For a careful comparison between
Orbital Shrinking and the core point method, we recommend [10, section 3].
Finally, most modern MIP solvers have fast presolving procedures for detecting
simple symmetries arising from parallel columns and parallel rows [27], which are
typically implemented using 2-level hashing schemes [27, 28]. This can also be con-
sidered a form of variable aggregation to remove symmetries, although the treated
symmetries are very simple. In [27, Section 7.1] a special structure is presented where
non-overlapping symmetries can be aggregated. In particular, if there is an automor-
phism of the ILP such that variables contained in the same orbit appear in disjoint
constraints, then one can aggregate all the variables in the orbit into one variable
without breaking linear and integer feasibility.
4
