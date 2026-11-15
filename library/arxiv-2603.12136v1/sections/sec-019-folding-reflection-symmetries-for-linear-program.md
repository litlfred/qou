---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-019-folding-reflection-symmetries-for-linear-program
section_title: "Folding reflection symmetries for Linear Programs"
section_number: null
pages: 56-57
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.994
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
[]{#sec_lp_folding_results label="sec_lp_folding_results"} As a baseline, we compare our dimension reduction algorithm against DRCR as described in [@Grohe2014]. The improved DRCR algorithm as presented [\[sec_reflection_symmetry\]](#sec_reflection_symmetry){reference-type="ref" reference="sec_reflection_symmetry"} is denoted by R-DRCR.

We use the linear programming relaxations of problems in the MIPLIB 2017 collection dataset [@Gleixner2021], which contains 1065 instances. We exclude the 10 largest instances due to memory requirements, and any instances with the (nonlinear) indicator constraints. Furthermore, we exclude instances where DRCR and R-DRCR produce an identical reduced instance. This yields a subset of 83 instances that we use for the computational experiments. The resulting linear programs are solved using SoPlex 8.0.0 [@hojny2025scipoptimizationsuite100] with a time limit of 1 hour. An overview of the results can be found in [1](#tab:drcr_lp_summary){reference-type="ref" reference="tab:drcr_lp_summary"}. The complete results can be found in Appendix [\[appendix_drcr_lp\]](#appendix_drcr_lp){reference-type="ref" reference="appendix_drcr_lp"}.

::: {#tab:drcr_lp_summary}
                               DRCR                   R-DRCR                       
  ------------ ----------- -------- ------------ -- -------- ------------ -------- --------
    3-4 subset   instances     time   iterations        time   iterations   faster   slower
           all          83     1.27       1866.0        0.93        962.0       40       43
         \<0.1          34     0.02        142.9        0.02         60.4       13       21
                        20     0.35       2907.9        0.33       2441.6        9       11
                         9     3.26      11942.0        3.00       7783.7        5        4
          \>10          20   174.02      37205.0       58.50      13094.6       13        7

  : Performance comparison between DRCR and R-DRCR on the 83 linear programming relaxations of instances in the MIPLIB2017 collection set where R-DRCR finds additional reductions compared to DRCR. The subsets contain the instances whose solution time for the DRCR method (in seconds) lies in the indicated bracket. The times reported are shifted geometric means in seconds, with a shift of 1 second. The iterations column indicates the number of simplex iterations, and is reported as a shifted geometric mean with a shift of 10 iterations. The faster and slower columns indicate the number of instances where R-DRCR is faster/slower than DRCR.
:::

The R-DRCR algorithm was also tested on the well-known Netlib linear programming dataset. However, for all of the instances in this dataset, DRCR and R-DRCR produced identical reduced instances. Thus, we omit the results on Netlib in this report.

From the results in [1](#tab:drcr_lp_summary){reference-type="ref" reference="tab:drcr_lp_summary"}, it is clear that R-DRCR is more effective than DRCR on the tested subset. In all categories, the running time is smaller and the number of required simplex iterations is also reduced. The running time improvement is particularly impressive for some of the more difficult linear programs that take longer than 10 seconds to solve, with the shifted geometric mean of the running times dropping from 174.0 to 58.5 seconds. Furthermore, we observe that on many of the easier instances there is a moderate reduction in running time and a clear reduction in the number of simplex iterations.

Let us highlight a few instances where reflection refinement is particularly effective. For the combinatorial instances `pythago7824` and `pythago7825`, the linear program is even reduced to a linear program with a single variable and row. Interestingly, these instances do not contain any (reflection) symmetries. Another impressive result is on the large instance `neos-3402454-bohle` where the solution time is reduced from 1353 to 6 seconds, where in the latter case, the majority of the running time is spent computing the reduced problem. The original problem has over 2.8 million rows, whereas the reduced problem has roughly 80 thousand rows.
