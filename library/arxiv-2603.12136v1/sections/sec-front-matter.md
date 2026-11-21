---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Folding Mixed-Integer Linear Programs and
Reflection Symmetries
Rolf van der Hulst
University of Twente, Enschede, The Netherlands.
Abstract
For mixed-integer linear programming and linear programming it is well known
that symmetries can have a negative impact on the performance of branch-
and-bound and linear optimization algorithms. A common strategy to handle
symmetries in linear programs is to reduce the dimension of the linear program by
aggregating symmetric variables and solving a linear program of reduced dimen-
sion. In their work Dimension Reduction via Color Refinement (DRCR), Grohe,
Kersting, Mladenov and Selman show that it is sufficient to run a fast color
refinement algorithm to detect permutation symmetries and reduce the dimen-
sion of the linear program. We extend DRCR in two directions. First, we show
that DRCR can be extended to reflection symmetries, which generalize permuta-
tion symmetries. Second, we show the folklore result that DRCR can be applied
to the continuous columns of mixed-integer linear programs. In order to derive
additional reductions on the integer variables we use affine totally unimodular
decompositions to reformulate mixed-integer linear programs into mixed-integer
linear programs with fewer integer variables. Computational experiments on
MIPLIB 2017 collection set using SCIP 10 show that DRCR is an effective tool
for handling symmetries. For the linear programming relaxations, DRCR with
reflection symmetries yields a modest reduction in running time compared to the
original DRCR procedure. For mixed-integer linear programming models, DRCR
is very effective at reducing the solution time compared to the default configura-
tion of SCIP. Moreover, the developed DRCR detection algorithms are fast and
scale well to large problem instances.
Keywords: linear programming, reflection symmetry, mixed-integer linear
programming, symmetry, total unimodularity
1
arXiv:2603.12136v1  [math.OC]  12 Mar 2026
