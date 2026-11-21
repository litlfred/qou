---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-001-contribution
section_title: "Contribution"
section_number: null
pages: 5-6
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
We extend the DRCR procedure from [11] in several directions. First of all, we show
that DRCR for Linear Programs can be extended to reflection symmetries, which
arise from the action of signed permutation matrices on linear programs. Our main
idea for realizing this uses two transformations. First, we reformulate the original
LP by centering the origin at the center of the variable domains using an affine
transformation. Then, we split each variable into two variables, where one variable
corresponds to the positive domain and one variable corresponds to the negative
domain. We show that by applying DRCR to this reformulated linear program, one
can recover the variable complementation and row scaling that achieves the best
possible reduction among all linear programs obtained by complementing variables
and negating rows. The procedure can be implemented efficiently with only minor
modifications to the original DRCR procedure.
For our second contribution, we aim to close the gap between the strong sym-
metry handling methods for linear programs and the symmetry handling methods
for mixed-integer linear programs by specializing DRCR to mixed-integer linear
programs. In particular, we show the ‘folklore’ result that DRCR can also be applied
to the continuous columns of mixed-integer linear programs. Additionally, we further
investigate the application of DRCR in MILP to also aggregate integer variables.
We use implied integrality [29] and affine TU decompositions [30] to infer redundant
integrality constraints on a subset of variables. Then, the implied convexity of these
variables is exploited by applying DRCR to aggregate these variables. Our approach
can also be thought of as Exact Orbital Shrinking, where one shows that the orbital
shrinking relaxation has the same strength as the original problem, and the feasi-
bility subproblem is an integer program that is given by a perfect formulation and
can be solved using linear programming. We formulate an algorithm that specializes
DRCR for mixed-integer linear programs. One of its crucial components are fast
detection algorithms for network matrices [31, 32], which are a subclass of totally
unimodular matrices [33]. The developed algorithm does not handle the complete
permutation symmetry group, but only aggregates variables that appear in auto-
morphisms where all the permuted variables have no integrality constraints or have
integrality constraints that can be reformulated using affine TU decompositions or
implied integrality.
We conduct experiments on the MIPLIB 2017 collection set [1]. For the linear pro-
grams, we consider the linear relaxations, and show that taking reflection symmetries
into account in DRCR can lead to additional reductions and a reduced model size
and soution time. For the DRCR algorithm for MILP, we show that it has two favor-
able characteristics. First, the aggregation of variables to remove symmetries from the
model is effective in reducing the running time of affected mixed-integer linear pro-
grams. In a computational comparison using SCIP 10 [34], the affected mixed-integer
linear programming instances in MIPLIB 2017 that can be solved by SCIP or our
method are solved, on average, more than twice as fast compared to the default con-
figuration of SCIP 10. Second, we observe that our detection algorithm for DRCR in
5
MILP is fast and scales well to large problems, much like in the linear programming
case.
