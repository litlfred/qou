---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-008-8-computational-results
section_title: "Computational Results"
section_number: 8
pages: 18-18
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linea r and integer programming problems."
---
The following experiments were carried out on an Intel(R) Core(TM) i7 920 2.67GHz ma-
chine, with 12GB of main memory, running Ubuntu 10.04 (Lucid Lynx). The performance
of each core is estimated at 5346.16 bogomips each. All our tests we re run single-threaded.
The goal of the experiments is to compare the performances of a c onventional branch-
and-cut approach (with automated symmetry detection) and the Core-Point-Algorithm B on
highly symmetric integer linear programs. For the test of the conve ntional branch-and-cut
method we used CPLEX, Version 12.1.0, while the Core-Point-Algorithm was implemented
and tested in polymake, Version 2.9.9 [7]. As a major diﬀerence polymake employs exact
rational arithmetic (via GMP), while CPLEX uses ﬂoating-point arithmetic. It should be
stressed that CPLEX can detect if the symmetry group of an integer linear program cont ains
the full symmetric group acting on the standard basis of Rn, and this is exploited in its
algorithms. For input in this category (which includes all our examples below), it is thus
quite a challenge to beat CPLEX.
8.1. Hypertruncated Cubes. We tested our algorithms on the ( ⌊n/e⌋,n ; 1/2)-hyper-
truncated cubes; see Remark 44. In this case we have only 4 n linear inequalities from Propo-
sition 43 as input. Each coeﬃcient is small, and computationally accura cy (for ﬂoating-point
computations) or coeﬃcient growth (for exact arithmetic) is not a n issue here. This benign
input can be dealt with easily up to high dimensions. Table 1 lists the timing s for CPLEX’
Branch-and-Cut and polymake’s Core Point Algorithm. The timings required to obtain the
solution of the linear relaxation are given separately for both syste ms.
The fact that polymake takes more time is due to the overhead induced by the GMP exact
rational arithmetic. Since coeﬃcient growth does not occur the ov erhead versus ﬂoating-
point arithmetic can be estimated to be constant. Hence the rough ly quadratic overhead (in
dependence ofn) versus the CPLEX result is a consequence of the total algorithmic complexity
ofO(mn2) from Corollary 34. Altogether both solvers behave pretty well fo r these kinds of
examples.
An industry strength solver as CPLEX comes with a number of bolts and whistles which
allow to tune its behavior in many ways. For the hypertruncated cub es this does not play
any role. Since no parallel implementation of the Core Point Algorithm is available (yet)
we set the number of CPLEX’ parallel threads to one.
