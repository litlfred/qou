---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-020-folding-symmetries-in-mixed-integer-linear-progr
section_title: "Folding symmetries in Mixed-Integer Linear Programming"
section_number: null
pages: 57-60
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.993
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
[]{#sec_milp_folding_results label="sec_milp_folding_results"} Next, we evaluate the impact of [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"} on the solution of mixed-integer linear programs. As before, we consider the MIPLIB 2017 collection dataset [@Gleixner2021]. We exclude the 10 largest instances and any instances with indicator constraints.

For our experiments, we consider two configurations of [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"}. We use R-DRCR-N to indicate the version that detects network matrices, and R-DRCR-T to indicate the version that detects transposed network matrices. For both configurations, we only test those instances where some reduction is found by the algorithms. R-DRCR-N find reductions on 207 of the 1065 MIPLIB 2017 collection instances, and R-DRCR-T finds reductions on 153 instances. In total, 208 of the instances admit a reduction by at least one of R-DRCR-N and R-DRCR-T.

The solving procedure is structured as follows. First, the problem is presolved using PaPILO. Then, we apply the DRCR algorithm to further reduce the presolved problem. Then, the presolved problem is solved using SCIP 10.0 [@hojny2025scipoptimizationsuite100] with a time limit of 1 hour. Finally, if SCIP finds a feasible integer solution to the reduced problem that is not integer when mapped to the original variables, we use SoPlex to postsolve the found integer solution to an integer solution. All running times reported include the runtime of the DRCR algorithm, SCIP's time to solve the problem, and time required to postsolve the final solution to obtain a feasible integral solution to the original problem. We compare the R-DRCR methods against the default SCIP 10 configuration, which is run on the presolved model that is output by PaPILO. In all cases, we use the default parameters and configuration of SCIP 10. One important detail is that, although the DRCR algorithm may also detect implied integrality in the reduced problem, we do not communicate this information to SCIP in order to measure the effect of the reduction detected by [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"} in isolation.

In [\[tab:drcr_n_mip_summary,tab:drcr_t_mip_summary\]](#tab:drcr_n_mip_summary,tab:drcr_t_mip_summary){reference-type="ref" reference="tab:drcr_n_mip_summary,tab:drcr_t_mip_summary"} we summarize the results of R-DRCR-N and R-DRCR-T compared to the SCIP 10 baseline on instances which were solved by at least one of the methods. In [3](#tab:PDItable){reference-type="ref" reference="tab:PDItable"} we compare the performance on the instances that were not solved within the time limit by any method. Here, we use the Primal-Dual Integral measure introduced by Berthold [@Berthold2013], which measures the average gap between the primal and dual solution during the solving process. This gives an indication for the quality of the obtained primal and dual bounds.

::: {#tab:drcr_n_mip_summary}
                             SCIP 10   R-DRCR-N                                   
  ------------ ----------- --------- ---------- ------- ------- -------- -------- --
    4-6 subset   instances    solved     solved  time     nodes   faster   slower 
           all         107       100        103  0.48      0.69       67       40 
          \<10          25        25         25  1.18      1.40       15       10 
                        24        24         23  0.86      0.98       12       12 
                        35        35         34  0.61      0.70       21       14 
        \>1000          23        16         21  0.075     0.25       19        4 

  : Performance comparison between SCIP 10 and R-DRCR-N on the solvable instances of the MIPLIB2017 collection set that are affected by R-DRCR-N. The subsets contain the instances whose solution time for SCIP 10 (in seconds) lies in the indicated bracket. The time and nodes column indicate the fraction of the shifted geometric mean of the R-DRCR method compared to the SCIP 10 baseline, where we use shifts of 1 second and 1 node respectively. The faster and slower columns indicate the number of instances where R-DRCR method is faster/slower than SCIP 10.
:::

::: {#tab:drcr_t_mip_summary}
                             SCIP 10   R-DRCR-T                                  
  ------------ ----------- --------- ---------- ------ ------- -------- -------- --
    4-6 subset   instances    solved     solved  time    nodes   faster   slower 
           all          77        75         76  0.75     0.86       47       30 
          \<10          19        19         19  1.08     0.95       12        7 
                        14        14         14  0.94     1.09        8        6 
                        30        30         30  0.80     0.92       17       13 
        \>1000          14        12         13  0.35     0.49       10        4 

  : Performance comparison between SCIP 10 and R-DRCR-T on the solvable instances of the MIPLIB2017 collection set that that are affected by R-DRCR-T.
:::

In [\[tab:drcr_n_mip_summary,tab:drcr_t_mip_summary\]](#tab:drcr_n_mip_summary,tab:drcr_t_mip_summary){reference-type="ref" reference="tab:drcr_n_mip_summary,tab:drcr_t_mip_summary"}, we observe that R-DRCR-N dominates R-DRCR-T in both the number of affected instances and the speedups on the affected instances. Of the 208 instances where some reduction was found by either of the two methods, R-DRCR-T found a smaller reduced problem on only 8 instances. One explanation for this observation is that assignment subproblems such as those in the generalized assignment problem discussed [\[sec_example\]](#sec_example){reference-type="ref" reference="sec_example"} consist of matrices that are in general network matrices but not transposed network matrices. Otherwise, both methods have similar characteristics. Although they do not seem to help with the solution of 'easy' problems that can be solved under 10 seconds, we observe large speedups for the more difficult problems.

For R-DRCR-N, seven new instances are newly solved, and four instances are no longer solved compared to SCIP 10's default. For the seven instances that are newly solved, the R-DRCR-N algorithm reduces the size of the original system significantly. For example, for the newly solved instance `neos-631710` the size of the constraint matrix is reduced from $169576\times167056$ to $9448\times7216$.

For the four instances that are no longer solved after applying R-DRCR-N, there are various potential explanations for the loss of performance. For the two instances `supportcase34` and `neos-5129192-manaia` a strong primal solution is no longer found early in the search after the reduction is applied to the problem. For `cvs08r139-94`, it seems that the default symmetry handling methods in SCIP are more effective than DRCR. One potential explanation for this is that the symmetries and the equitable partition in this instance are relatively simple: all the nontrivial variable parts consist of two binary variables that are aggregated into one integer variable.

::: {#tab:PDItable}
  Method       instances   nodes        SCIP 10 PDI         method PDI
  ---------- ----------- ------- ------------------ ------------------
  R-DRCR-N           100    1.19   $1.30\cdot 10^5$   $1.22\cdot 10^5$
  R-DRCR-T            76    1.25   $1.23\cdot 10^5$   $1.14\cdot 10^5$

  : Comparison of SCIP 10 and R-DRCR-N and R-DRCR-T on unsolved instances of MIPLIB 2017 collection set that are affected by the R-DRCR-N or R-DRCR-T. The two different rows of the table correspond to the two different instance sets for which R-DRCR-N and R-DRCR-T found one or more reductions. The 'nodes' column indicates the fractional of the shifted geometric mean of R-DRCR method compared to the SCIP 10 baseline. The SCIP 10 PDI and method PDI indicate the Primal-Dual Integral values of the SCIP 10 baseline and the R-DRCR method, respectively.
:::

In [3](#tab:PDItable){reference-type="ref" reference="tab:PDItable"} we evaluate the performance of DRCR on instances that were not solved within the time limit by any method. We observe that both DRCR methods help to reduce the Primal-Dual Integral, indicating that the DRCR helps to find strong primal and dual bounds more quickly than SCIP 10. Furthermore, we note that the DRCR-methods explore more branch-and-bound nodes within the time limit. This observation can be explained by the fact that the linear programming relaxations are easier to solve due to their reduced size.

::: {#tab:drcr_timings}
                 DRCR detection                             postsolve                        
  ------------ ---------------- ----------- ---------- -- ----------- ----------- ---------- ------
  2-4 Method              \<0.1   \[0.1,1\]   \[1,10\]          \<0.1   \[0.1,1\]   \[1,10\]   \>10
  R-DRCR-N                  146          46         15            134          37         28      8
  R-DRCR-T                  114          28         11            108          25         15      5

  : Distribution of the time taken (in seconds) to detect and postsolve for R-DRCR-N and R-DRCR-T for the affected instances. For each bracket, the number of instances that fall into it is indicated.
:::

[4](#tab:drcr_timings){reference-type="ref" reference="tab:drcr_timings"} provides an overview of the distribution of presolve and postsolve times. We note that for the vast majority of the instances, the presolve and postsolve procedures are cheap. For a small number of instances, the postsolve LP solution using SoPlex took longer than 10 seconds.

One effect that we observe in a few larger instances is that DRCR helps to reduce the running time of further symmetry detection methods. For example for the instance `neos-3322547-alsek`, symmetry detection for the original model with 1001000 columns takes 378.2 seconds. R-DRCR-N reduces the model to have only 82000 columns in 6.3 seconds. Symmetry detection on the reduced model completes in only 0.24 seconds.

To summarize our results, we observe that both R-DRCR methods are effective in reducing the solution time of general mixed-integer linear programs. The R-DRCR-N algorithm dominates the R-DRCR-T algorithm. Furthermore, R-DRCR-N solves three more instances, and both methods yield a smaller PDI on the set of instances that are not solved within the time limit.
