---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-018-computational-results
section_title: "Computational Results"
section_number: null
pages: 55-56
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 1.0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
[]{#sec_results label="sec_results"}

In order to validate the developed algorithms, we perform experiments on linear programming and mixed-integer linear programming problems.

and the reflection reduction detection algorithm are implemented in C++ and are publicly available [@VanDerHulstFolding]. The implementation of  uses the network matrix augmentation algorithms described in [@RowNetworkMatrixPaper] and [@BixbyWagner1988] to recognize totally unimodular matrices, which are also publicly available [@VanDerHulstMatrec]. All experiments are run on a AMD Ryzen 2600 CPU with 16GB of memory. Prior to their solution, the linear programming and mixed-integer linear programming instances are presolved using PaPILO 3.0.0 [@GGHpapilo]. In the context of our study, presolving the instances with PaPILO has two benefits. First of all, well-known presolving reductions such as those described in [@AchterbergBGRW20] may provide additional opportunities for the DRCR algorithm, and provide a realistic setting for the application of DRCR. Secondly, PaPILO removes parallel rows and columns from the problem, which would also be detected by DRCR. This way, we can be sure that the reductions detected by R-DRCR and DRCR are not detected easily by other presolving techniques.

For our experiments on mixed-integer linear programs we use the SCIP 10 solver [@hojny2025scipoptimizationsuite100]. We note that currently parallel column reductions are not available in SCIP 10 due to technical limitations of its API. Thus, presolving once with PaPILO before handing the problem to SCIP is necessary to provide a fair comparison of DRCR for MILP with state-of-the-art presolving techniques.
