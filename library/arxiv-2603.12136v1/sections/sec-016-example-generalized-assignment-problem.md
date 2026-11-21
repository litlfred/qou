---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-016-example-generalized-assignment-problem
section_title: "Example: Generalized Assignment problem"
section_number: null
pages: 45-48
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.974
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
[]{#sec_example label="sec_example"} Consider the generalized assignment problem, where one computes an assignment of $J$ items with sizes $a_j, ~j\in J$ to $I$ knapsacks with capacity $C_i$ such that we maximize the sum of profits $\sum_{j\in J} c_j$ such that the capacities on the knapsacks are not exceeded. This can be modeled as an integer program using the binary variables $x_{ij} = \begin{cases}
    1 &\text{ if $j$ is packed into knapsack $i$}\\
    0 &\text{ otherwise}
\end{cases}$ for all $i\in I, j\in J$.

$$\label{eq_mk_orig}
\begin{align}
\max\quad & \sum_{i\in I}\sum_{j\in J} c_j x_{ij} \\
\text{s.t.}\quad 
& \sum_{j\in J} a_j x_{ij} \leq C_i 
&& \forall i\in I \\
& \sum_{i\in I} x_{ij} \leq 1 
&& \forall j\in J \label{eq_mk_orig_item_packing}\\
& x_{ij} \in \{0,1\} 
&& \forall i\in I,\ \forall j\in J \label{eq_mk_orig_bounds}
\end{align}$$

Now, suppose that there exist identical items $j\in J$ that have the same weight and cost. Let $\mathcal{K} = \{K_1,\dotsc, K_n\}$ be a partition of $J$ into $n$ item sets that have identical cost and weight. Clearly, $n \leq |J|$ must hold, and by definition we have that $a_K = a_j$ and $c_K = c_j$ for any $j\in K$, for any $K\in \mathcal{K}$. Let the variable partition $\MQ$ be given by the parts $Q_{iK} = \{x_{ij} \mid \forall j\in K\}$ for $i\in I$, $K\in \mathcal{K}$, where identical items are placed into the same part. Let $\MP$ be a constraint partition where all constraints [\[eq_mk_orig_item_packing\]](#eq_mk_orig_item_packing){reference-type="eqref" reference="eq_mk_orig_item_packing"} and [\[eq_mk_orig_bounds\]](#eq_mk_orig_bounds){reference-type="eqref" reference="eq_mk_orig_bounds"} belonging to identical items are placed into the same partition $P\in \MP$ and all other constraints are given their own partition. Then, it can be verified that $(\MP,\MQ)$ is an equitable partition of the generalized assignment problem in [\[eq_mk_orig\]](#eq_mk_orig){reference-type="eqref" reference="eq_mk_orig"}. Applying the reformulation suggested by the equitable partition we obtain a smaller formulation: $$\label{eq_mk_reduced}
\begin{align}
\max\quad & \sum_{i\in I}\sum_{K\in \mathcal{K}} c_K y_{iK} \\
\text{s.t.}\quad 
& \sum_{K\in \mathcal{K}} a_K y_{iK} \leq C_i 
&& \forall i\in I \label{eq_mk_reduced_knapsack}\\
& \sum_{i\in I} y_{iK} \leq |K| 
&& \forall K\in \mathcal{K} \\
& y_{ik} \in \{0,1,\cdots,|K|\} 
&& \forall i\in I,\ \forall K\in \mathcal{K}
\end{align}$$

Now, suppose that we are given any integral solution $y^\star$ to the reduced problem. For these values, we wish to recover a solution in the $x$-space. Then, we can add the constraints [\[eq_mk_affine_fixing\]](#eq_mk_affine_fixing){reference-type="eqref" reference="eq_mk_affine_fixing"}, that link the $x$ variables to $y^\star$, and hope to recover a solution for $x$.

$$\label{eq_mk_affine}
\begin{align}
\max\quad & \sum_{i\in I}\sum_{j\in J} c_j x_{ij} \label{eq_mk_affine_fixing_obj}\\
\text{s.t.}\quad 
& \sum_{j\in J} a_j x_{ij} \leq C_i 
&& \forall i\in I \label{eq_mk_affine_fixing_knapsack}\\
& \sum_{i\in I} x_{ij} \leq 1 
&& \forall j\in J \\
& \sum_{j\in K} x_{ij} = y^{\star}_{iK} &&\forall i \in I, \forall K \in \mathcal{K} \label{eq_mk_affine_fixing}\\
& x_{ij} \in \{0,1\} 
&& \forall i\in I,\ \forall j\in J
\end{align}$$

We can substitute the equations [\[eq_mk_affine_fixing\]](#eq_mk_affine_fixing){reference-type="eqref" reference="eq_mk_affine_fixing"} into the constraints [\[eq_mk_affine_fixing_knapsack\]](#eq_mk_affine_fixing_knapsack){reference-type="eqref" reference="eq_mk_affine_fixing_knapsack"} and the objective [\[eq_mk_affine_fixing_obj\]](#eq_mk_affine_fixing_obj){reference-type="eqref" reference="eq_mk_affine_fixing_obj"}.

$$\label{eq_mk_postsolve_fixed}
\begin{align}
\max\quad & \sum_{i\in I}\sum_{K\in K} c_K y^\star_{iK} \\
\text{s.t.}\quad 
& \sum_{K\in \mathcal{K}} a_K y^\star_{iK} \leq C_i 
&& \forall i\in I \label{eq_mk_postsolve_knapsack}\\
& \sum_{i\in I} x_{ij} \leq 1 
&& \forall j\in J \label{eq_mk_postsolve_usedonce}\\
& \sum_{j\in K} x_{ij} = y^{\star}_{iK} &&\forall i \in I, \forall K\in \mathcal{K} \label{eq_mk_postsolve_linking}\\
& x_{ij} \in \{0,1\} 
&& \forall i\in I,\ \forall j\in J
\end{align}$$ Note that in [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"}, both the objective and the knapsack constraints are not dependent on $x$ anymore. In fact, by feasibility of $y^\star$, all constraints in [\[eq_mk_postsolve_knapsack\]](#eq_mk_postsolve_knapsack){reference-type="eqref" reference="eq_mk_postsolve_knapsack"} are feasible by feasibility of [\[eq_mk_reduced_knapsack\]](#eq_mk_reduced_knapsack){reference-type="eqref" reference="eq_mk_reduced_knapsack"}. Then, we observe that the remaining problem is given by an assignment problem on the $x$ variables. Since the constraints [\[eq_mk_postsolve_usedonce\]](#eq_mk_postsolve_usedonce){reference-type="eqref" reference="eq_mk_postsolve_usedonce"}, [\[eq_mk_postsolve_linking\]](#eq_mk_postsolve_linking){reference-type="eqref" reference="eq_mk_postsolve_linking"} form a totally unimodular matrix and the right-hand side given by $1$ and $y^\star$ is integral, the LP relaxation of [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"} is integral. Moreover, the solution $\bar{x}_{ij} = \frac{y^\star_{iK}}{|K|}$ for all $i\in I, K\in\mathcal{K}$ such that $j\in K$ is feasible for the LP relaxation of [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"} by [\[thm_lp_folding\]](#thm_lp_folding){reference-type="ref" reference="thm_lp_folding"}. Thus, an integral solution $x$ can be obtained by finding a vertex solution of the LP relaxation of [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"}.

The reformulation of [\[eq_mk_affine\]](#eq_mk_affine){reference-type="eqref" reference="eq_mk_affine"} into [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"} can be seen as exhibiting an affine TU decomposition. The rows of the constraints [\[eq_mk_postsolve_linking\]](#eq_mk_postsolve_linking){reference-type="eqref" reference="eq_mk_postsolve_linking"} correspond to the $T$-matrix, and their substitution in [\[eq_mk_postsolve_knapsack\]](#eq_mk_postsolve_knapsack){reference-type="eqref" reference="eq_mk_postsolve_knapsack"} corresponds to the $U$-matrix. The rows of [\[eq_mk_postsolve_usedonce\]](#eq_mk_postsolve_usedonce){reference-type="eqref" reference="eq_mk_postsolve_usedonce"} form the nonzeros of the $S$-matrix. Additionally, note that the usage of the equations to cancel the nonzeros in the objective is possible due to the fact that the objective vector is equitably partitioned by $\MQ$.\
There are a few interesting observations that can be made about the generalized assignment problem. First of all, as also implied by Salvagnin [@Salvagnin2013], the used equitable partition is not necessarily the coarsest equitable partition. Suppose for example, that for all knapsacks $i\in I$ the capacity $C_i$ is equal to some constant $C$. Then, the knapsack constraints [\[eq_mk_orig_item_packing\]](#eq_mk_orig_item_packing){reference-type="eqref" reference="eq_mk_orig_item_packing"} have additional permutation symmetries which permute the items between the bins. These symmetries are also captured by the coarsest equitable partition since equitable partitions generalize permutation symmetries. Consequently, for the coarsest equitable partition $(\MP,\MQ)$, $\MQ$ contains variables $x_{ij}$ belonging to multiple bins in $I$. In the case where one would reformulate [\[eq_mk_orig\]](#eq_mk_orig){reference-type="eqref" reference="eq_mk_orig"} using orbital shrinking, the orbital shrinking subproblem would then become the $\cplxNP$-hard binpacking problem, in contrast to the polynomial-time solvable assignment problem that we derive here. Salvagnin shows in [@Salvagnin2013] that for the generalized assignment model, employing a constraint programming solver to solve the binpacking subproblem and additionally reformulating the symmetric knapsacks yields better performance than the reformulation with the assignment problem that we derive here.

Secondly, we note that there is a minor way to improve the postsolve subproblem in [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"}. Let $\mathcal{K}^1 \coloneqq \{K\in \mathcal{K} \mid a_{K} = 1\}$ and $J^1 \coloneqq \{ j\in J \mid a_j = 1\}$ denote the set of items with weight $1$. For these items, it is not necessary to fix them to their corresponding $y^\star_{iK}$ value in [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"}. In particular, if we change the equalities in [\[eq_mk_postsolve_linking\]](#eq_mk_postsolve_linking){reference-type="eqref" reference="eq_mk_postsolve_linking"} to only be added for all $\mathcal{K}\setminus \mathcal{K}^1$, and substitute only all items with non-unit weight in [\[eq_mk_postsolve_knapsack\]](#eq_mk_postsolve_knapsack){reference-type="eqref" reference="eq_mk_postsolve_knapsack"}, we obtain the following reformulation.

$$\label{eq_mk_unit}
\begin{align}
\max\quad & \sum_{i\in I}\sum_{J\in \mathcal{J}^1} c_j x_{ij} + \sum_{i\in I}\sum_{K\in \mathcal{K}\setminus \mathcal{K}^1} c_K y^\star_{iK}  \\
\text{s.t.}\quad 
& \sum_{j\in \mathcal{J}^1} x_{ij} \leq C_i - \sum_{K\in \mathcal{K}\setminus \mathcal{K}^1} a_K y^\star_{iK}
&& \forall i\in I \label{eq_mk_unit_knapsack}\\
& \sum_{i\in I} x_{ij} \leq 1 
&& \forall j\in J \label{eq_mk_unit_usedonce}\\
& \sum_{j\in K} x_{ij} = y^{\star}_{iK} &&\forall i \in I, \forall K\in \mathcal{K}\setminus \mathcal{K}^1 \label{eq_mk_unit_linking}\\
& x_{ij} \in \{0,1\} 
&& \forall i\in I,\ \forall j\in J
\end{align}$$

It is not difficult to see that [\[eq_mk_unit\]](#eq_mk_unit){reference-type="eqref" reference="eq_mk_unit"} is still a perfect formulation. The constraint matrix defined by [\[eq_mk_unit_knapsack\]](#eq_mk_unit_knapsack){reference-type="eqref" reference="eq_mk_unit_knapsack"}--[\[eq_mk_unit_linking\]](#eq_mk_unit_linking){reference-type="eqref" reference="eq_mk_unit_linking"} is totally unimodular as it is the node-edge incidence matrix of a bipartite graph and the right-hand sides are integral. The two parts of the bipartition are given by constraints [\[eq_mk_unit_usedonce\]](#eq_mk_unit_usedonce){reference-type="eqref" reference="eq_mk_unit_usedonce"} and ([\[eq_mk_unit_knapsack\]](#eq_mk_unit_knapsack){reference-type="eqref" reference="eq_mk_unit_knapsack"} plus [\[eq_mk_unit_linking\]](#eq_mk_unit_linking){reference-type="eqref" reference="eq_mk_unit_linking"}), respectively. The fixings for $\mathcal{K}^1$ can be left out due to the fact that the variables in $J^1$ are implied integer. Let $P$ be the linear relaxation of [\[eq_mk_orig\]](#eq_mk_orig){reference-type="eqref" reference="eq_mk_orig"}. Then total unimodularity of [\[eq_mk_unit\]](#eq_mk_unit){reference-type="eqref" reference="eq_mk_unit"} shows by affine TU decomposition that $\mathrm{conv}(P\cap \Z^n) = \mathrm{conv}(\{x\in P \mid \sum_{j\in K} x_{ij} \in \Z, ~ \forall i\in I, ~\forall K \in \mathcal{K}\setminus \mathcal{K}^1\})$ holds. From this equality it also follows that $y_{iK}$ is implied integer for all $i\in I$ and all $K\in \mathcal{K}^1$ by the other variables in [\[eq_mk_reduced\]](#eq_mk_reduced){reference-type="eqref" reference="eq_mk_reduced"}. One way in which this additional power from implied integrality manifests is that in contrast to [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"}, solving [\[eq_mk_unit\]](#eq_mk_unit){reference-type="eqref" reference="eq_mk_unit"} may give a stronger solution than the provided $y^\star$ solution, if $y^\star$ is suboptimal and one of the items $j\in J^1$ can still be assigned to some knapsack. This correspond to having the proper subset $\MQ' \subset \MQ_I$ in the statement of [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref" reference="thm_fibers_symmetry_integral"}.
