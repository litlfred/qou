---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-008-8-computational-results
section_title: "Computational Results"
section_number: 8
pages: 18-18
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 1.0
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linear and integer programming problems."
---
[]{#sec:experiments label="sec:experiments"} The following experiments were carried out on an Intel(R) Core(TM) i7 920 2.67GHz machine, with 12GB of main memory, running Ubuntu 10.04 (Lucid Lynx). The performance of each core is estimated at 5346.16 bogomips each. All our tests were run single-threaded.

The goal of the experiments is to compare the performances of a conventional branch-and-cut approach (with automated symmetry detection) and the Core-Point-Algorithm [\[algo:core_point\]](#algo:core_point){reference-type="ref" reference="algo:core_point"} on highly symmetric integer linear programs. For the test of the conventional branch-and-cut method we used `CPLEX`, Version 12.1.0, while the Core-Point-Algorithm was implemented and tested in `polymake`, Version 2.9.9 [@polymake]. As a major difference `polymake` employs exact rational arithmetic (via `GMP`), while `CPLEX` uses floating-point arithmetic. It should be stressed that `CPLEX` can detect if the symmetry group of an integer linear program contains the full symmetric group acting on the standard basis of ${\mathbb{R}}^n$, and this is exploited in its algorithms. For input in this category (which includes all our examples below), it is thus quite a challenge to beat `CPLEX`.

## Hypertruncated Cubes

We tested our algorithms on the $(\lfloor n/e\rfloor,n;1/2)$-hypertruncated cubes; see Remark [\[rem:hypertruncated:parameters\]](#rem:hypertruncated:parameters){reference-type="ref" reference="rem:hypertruncated:parameters"}. In this case we have only $4n$ linear inequalities from Proposition [\[prop:hypertruncated_facets\]](#prop:hypertruncated_facets){reference-type="ref" reference="prop:hypertruncated_facets"} as input. Each coefficient is small, and computationally accuracy (for floating-point computations) or coefficient growth (for exact arithmetic) is not an issue here. This benign input can be dealt with easily up to high dimensions. Table [\[tab:HypertruncatedCube\]](#tab:HypertruncatedCube){reference-type="ref" reference="tab:HypertruncatedCube"} lists the timings for `CPLEX`' Branch-and-Cut and `polymake`'s Core Point Algorithm. The timings required to obtain the solution of the linear relaxation are given separately for both systems.

The fact that `polymake` takes more time is due to the overhead induced by the `GMP` exact rational arithmetic. Since coefficient growth does not occur the overhead versus floating-point arithmetic can be estimated to be constant. Hence the roughly quadratic overhead (in dependence of $n$) versus the `CPLEX` result is a consequence of the total algorithmic complexity of $O(mn^2)$ from Corollary [\[cor:core_point\]](#cor:core_point){reference-type="ref" reference="cor:core_point"}. Altogether both solvers behave pretty well for these kinds of examples.

::: tabular*
\@rrrrr@ & &\
& & & &\
& 0.00 & 0.07 & 0.01 & 0.08\
200 & 0.07 & 0.29 & 0.02 & 0.57\
300 & 0.19 & 0.73 & 0.03 & 1.88\
400 & 0.41 & 1.58 & 0.06 & 4.26\
500 & 0.90 & 2.99 & 0.10 & 8.39\
600 & 1.52 & 4.80 & 0.14 & 14.30\
700 & 2.21 & 7.01 & 0.18 & 22.29\
800 & 3.44 & 11.59 & 0.24 & 32.96\
900 & 5.17 & 16.37 & 0.31 & 47.11\
1000 & 6.77 & 21.66 & 0.38 & 65.11\
1100 & 8.25 & 26.55 & 0.47 & 85.52\
1200 & 11.75 & 35.47 & 0.55 & 111.59\
1300 & 14.05 & 45.63 & 0.65 & 142.76\
1400 & 18.96 & 57.23 & 0.74 & 175.23\
1500 & 23.42 & 73.50 & 0.85 & 217.19\
1600 & 28.11 & 78.13 & 0.98 & 263.21\
1700 & 32.07 & 97.23 & 1.11 & 315.38\
1800 & 41.82 & 128.88 & 1.25 & 374.63\
1900 & 44.68 & 137.22 & 1.40 & 444.48\
2000 & 50.39 & 154.35 & 1.54 & 511.59\
:::

An industry strength solver as `CPLEX` comes with a number of bolts and whistles which allow to tune its behavior in many ways. For the hypertruncated cubes this does not play any role. Since no parallel implementation of the Core Point Algorithm is available (yet) we set the number of `CPLEX`' parallel threads to one.
