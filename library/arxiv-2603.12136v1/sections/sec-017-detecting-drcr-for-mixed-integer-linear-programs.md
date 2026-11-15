---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-017-detecting-drcr-for-mixed-integer-linear-programs
section_title: "Detecting DRCR for mixed-integer linear programs"
section_number: null
pages: 48-55
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.986
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
[]{#sec_algorithm label="sec_algorithm"} Next, let us formulate an algorithm to detect the reductions described in [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref" reference="thm_milp_folding"}. To achieve such a reduction, we need to balance two conditions: we would like the partition $\MQ$ to be as coarse as possible, but [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} must also hold. These two objectives naturally conflict with each other, as a coarse partition of the integer variables requires us to find an affine TU decomposition with fewer integrality constraints. Although one could consider the coarsest possible partition and simply try to detect an affine TU decomposition and apply [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} and [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref" reference="thm_fibers_symmetry_integral"}, it is unlikely that [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} holds, either by the structure of the problem or by additional symmetries. For the example of the generalized assignment problem in [\[sec_example\]](#sec_example){reference-type="ref" reference="sec_example"}, if two bins have identical capacities then the symmetries that permute the two bins imply that [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} is not satisfied for the coarsest equitable partition.\
In order to detect an affine TU decomposition that we can use, we attempt to detect the structure of [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} where $T$ is given by $(\transpose{\Pi_\MQ} \Lambda x_{W_U})_{\MQ',\star}$, where $\MQ' \subseteq  \{ Q\in \MQ_I \mid |Q| > 1\}$. Note that the columns of $T$ consist of unit vectors, which may have been negated. For $w\in W^2$ we have for its column in $T$ that $T_{\star,w} = \lambda_w \mathbbm{e}_{Q}$ holds for $Q\in \MQ'$ such that $w\in Q$, where $\mathbbm{e}_{Q}$ is a unit vector. Then it follows that $B_{\star,w} = (S + U T)_{\star,w} = S_{\star,w} + U T_{\star,w} = S_{\star,w} + \lambda_w U_{\star,Q}$ holds. Since we want $S$ to be part of the totally unimodular matrix, its entries are $\pm 1$ values. Thus, if a column $B_{\star,w}$ contains large entries these must come from the $U_{\star,Q}$ vector. Furthermore, note that for all columns in the block $Q$, its entries must differ by at most $1$ from $\lambda_w U_{\star,Q}$. Thus, columns in $B_{\star,Q}$ must differ by at most $1$ up to $\pm 1$ scaling. For example, if $Q$ contains some block $(P,Q)\in \MP \times \MQ$ such that $B_{P,Q} = \begin{bmatrix}
    3 & 0 \\
    0 & 3
\end{bmatrix}$, then it is impossible to construct $U$ and $S$ such that we can get $B = S + U T$, since $B_{P,w_1} - B_{P,w_2} \notin \{-1,0,1\}^P$ implies that there exists no choice of $U_{\star,Q}$ such that we can construct a totally unimodular matrix $S$.\
For a matrix $A \in \R^{V\times W}$, we define the *nonternary mask* $\mathrm{ntmask}(A) \in \R^{V\times W}$ such that $\mathrm{ntmask}(A)_{v,w} \coloneqq \begin{cases}
    0 &\text{ if $|A_{v,w}| = 1$}\\
    A_{v,w} &\text{ otherwise }
\end{cases}$ holds for all $v\in V$ and $w\in W$. Then, if two columns of $B$ have the same nonternary mask up to $\pm 1$ scaling, they are candidates to belong to the same part $Q\in \MQ$. In order to generate equitable partitions which satisfy this condition, we change the initial partition that we pass to the color refinement algorithm to only place two integer columns $w_1$ and $w_2$ in the same initial part $Q\in \MQ_0$ if $\mathrm{ntmask}(A_{\star,w_1}) = \pm \mathrm{ntmask}(A_{\star,w_2})$ holds. Using standard hashing techniques, this can be done in linear time, see [@Gemander2020] for further details. The condition that the nonternary masks are equivalent requirement is a sufficient condition to ensure that $S$ is a ternary matrix, but not a necessary one. For example, we have $\begin{bmatrix}
    3 & 2\\
    2 & 3 
\end{bmatrix} = \begin{bmatrix}
    1 & 0 \\
    0 & 1 
\end{bmatrix} + \transpose{\begin{bmatrix}
    2 & 2
\end{bmatrix}} \begin{bmatrix}
    1 & 1 
\end{bmatrix}$ where the $\transpose{\begin{bmatrix}
    S & T
\end{bmatrix}}$ matrix is given by the totally unimodular matrix $\transpose{\begin{bmatrix}
    1 & 0 & 1 \\
    0 & 1 & 1 
\end{bmatrix}}$ but the two nonternary masks of the original columns differ.\
Then, consider the second condition that $E=R T$ holds. For $v\in V$ and $w\in W$ we have $E_{v,w} = (R \transpose{\Pi_\MQ} \lambda)_{v,w} = R_{v,Q} \lambda_w$ for $Q$ such that $w\in Q$, which only holds if the columns in $E_{\star,Q}$ are identical up to $\pm 1$ scaling. Thus, we require that $E_{\star,w} = \pm E_{\star,w'}$ holds for all $w,w'\in Q$.\
Although totally unimodular matrices can be detected in polynomial time [@Truemper1990], current implementations still have quintic time complexity [@Walter2013], which is too slow for practical purposes. Instead, we focus on *network matrices* and their transposes, which form large subclasses of totally unimodular matrices [@Schrijver86]. We use the fast column augmentation algorithms by Bixby and Wagner for network matrices [@BixbyWagner1988] and the algorithm by van der Hulst and Walter for transposed network matrices [@RowNetworkMatrixPaper]. For a (transposed) network matrix $M \in \R^{V\times W}$ and a column $u\in \R^V$, both algorithms are given by a procedure $\mathrm{AugmentNetwork}(M,u)$ that returns whether the augmented matrix $\begin{bmatrix}
    M & u
\end{bmatrix}$ is a (transposed) network matrix, growing the (transposed) network matrix by one column. The operation of *augmenting* a column to a matrix $M$ turns $M$ into $\begin{bmatrix}
    M & u
\end{bmatrix}$.\
Then, we are ready to describe an algorithm that detects the conditions of [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref" reference="thm_milp_folding"} by simultaneously computing a reflection reduction and an affine TU decomposition of the MILP. The algorithm is described in [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"} and consists of roughly five steps.\
In the first step, we determine the row partition that is used for [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"}, by partitioning the rows according to whether they contain non-integral entries or right-hand side. Then, we determine for each of the the connected components of the submatrix formed by the continuous columns that is in the integral part whether it is (transposed) network. These components form the $C$-matrix in [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"}. This step is identical to part of the algorithm described in [@VanDerHulst2025] to detect implied integrality using totally unimodular submatrices.\
In the second step, we use the computed row partition for [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} to compute an initial partition that we pass to the color refinement algorithm. As discussed above, we put two columns in the same partition only if they are (up to $\pm 1$ scaling) identical in the non-integral rows and if their nonternary masks are identical (up to $\pm 1$ scaling) in the integral rows. In the third step, we compute a reflection reduction given this initial partition.\
For the fourth step, we consider the computed reflection reduction and attempt to construct a matching affine TU decomposition using [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} that extends the computed reduction to integer variables. For every $Q \in \MQ'$, where $\MQ' \coloneq \{ Q \in \MQ_I \mid |Q| > 1 \}$, we consider adding a column $u$ to the $U$ matrix of the affine TU decomposition. For our approach in [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"}, we simply check if $A_{v,Q} =  \alpha \lambda_{Q}$ holds for some $\alpha \in \R\setminus \{0\}$. If so, then we set $u_v = \alpha_v$. Then, we use $S_{\star,Q} = A_{\star,Q} - u (\transpose{\Pi_\MQ} \Lambda)_{\star,Q}$ This effectively cancels the $v$'th row of $A_{\star,w}$ by using $u$. If $u = \zerovec$, then we do not need the additional row of $\Pi_\MQ \Lambda$ to cancel any rows, and the additional row in the $T$ part of the affine TU decomposition can only harm detection of total unimodularity, as any submatrix of a TU matrix is TU. In this case, we consider the partition of the subset $\MQ' \setminus \{Q\}$ rather than $\MQ'$, which is sufficient by [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref" reference="thm_fibers_symmetry_integral"}, and we do not add the corresponding row to the $T$ matrix. Finally, we ensure that for the affine TU decomposition $E=R T$ holds by checking if $S_{V_R,Q} = \zerovec$ holds, i.e. that all rows in $V_R$ are properly canceled.\

::: algorithm
$V_R\gets \{v\in V | \, b_v \notin \mathbb{Z}$ or $a_{v,w}\notin\mathbb{Z}$ for some $w\in W\}$[]{#algo_eos_start label="algo_eos_start"} Let $\mathcal{K}$ be the set of connected components of $A_{V, W \setminus W_I}$ Let $M$ denote the (transposed) network matrix that is constructed []{#algo_eos_point1 label="algo_eos_point1"} Let $\MQ_0$ be a partition of $W$ such that $Q\cap W_I = \emptyset$ or $Q\subseteq W_I$ holds for all $Q\in \MQ_0$. Additionally, we impose the condition that for all $Q\subseteq W_I$, $w,w'\in Q$ holds if and only if $A_{V_R,w} = \pm A_{V_R,w'}$ and $\mathrm{ntmask}(A_{V\setminus V_R,w}) = \pm \mathrm{ntmask}(A_{V\setminus V_R,w'})$ hold[]{#algo_eos_point2 label="algo_eos_point2"} Let $\MP_0 \gets \{V\}$ $(\MP^1,\MQ^1, \lambda, \gamma, \delta, V^1_O, W^1_O) \gets \textsc{ReflectionRefinement}(\MP_0, \MQ_0, A, b, \ell, u)$[]{#algo_eos_first_refine label="algo_eos_first_refine"}

Sort $\MQ^1$ by descending size $|Q|$ of its parts $Q \in \MQ^1$[]{#algo_eos_start_ATU label="algo_eos_start_ATU"} []{#algo_eos_end_ATU label="algo_eos_end_ATU"} $(\MP^2,\MQ^2, \lambda, \gamma, \delta, V^2_O, W^2_O) \gets \textsc{ReflectionRefinement}(\MP^1, \MQ^1, A, b, \ell, u)$[]{#algo_eos_additional_refinements label="algo_eos_additional_refinements"} $(\MP^2,\MQ^2, \lambda, \gamma, \delta, V^2_O, W^2_O)$
:::

In the fifth and final step, we consider all $Q\in \MQ$ that could not be added to the affine TU decomposition. For each such a part $Q$, we *individualize* it by splitting $Q$ into $|Q|$ parts where each element is in its own part of size $1$, and run the refinement algorithm again. Note that this final refinement may refine 'good' parts that we computed the affine TU decomposition for previously into several parts. This is unfortunate, as it may adjust the requirements for the $T$ matrix, and break the affine TU decomposition. An example of this phenomenon is shown in [\[example_refinement_problematic\]](#example_refinement_problematic){reference-type="ref" reference="example_refinement_problematic"}. However, we show in [\[thm_refinement_integrality_okay\]](#thm_refinement_integrality_okay){reference-type="ref" reference="thm_refinement_integrality_okay"} that, because the new partition $\MQ$ is a refinement of the previous partition, [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} is still satisfied and we can still recover solutions in polynomial time.

::: example
[]{#example_refinement_problematic label="example_refinement_problematic"} We consider a run of [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"} on the mixed-integer linear program $\mathrm{conv}(\{x \in \R^6 \mid A x = b, x\geq 0 \}\cap \Z^6)$ where $$A = \begin{bmatrix}
    2 & 2 & 2 & 2 & 3 & 3 \\
    1 & 0 & 1 & 0 & 1 & 0 \\
    0 & 1 & 0 & 1 & 1 & 0 \\
    0 & 1 & 1 & 0 & 0 & 1 \\
    1 & 0 & 0 & 1 & 0 & 1 \\
    1 & 0 & 0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 & 1 & 0 \\
    0 & 0 & 1 & 0 & 0 & 1 \\
    0 & 0 & 0 & 1 & 0 & 1 
    \end{bmatrix} \in \Z^{9\times 6}\text{ and } b= \begin{bmatrix}
        8\\
        2\\
        2\\
        2\\
        2\\
        1\\
        1\\
        1\\
        1
    \end{bmatrix} \in \Z^9.$$ We use $v_i$ to indicate the $i$'th row index and $w_j$ to indicate the $j$'th column index. The partition returned by [ReflectionReduction]{.smallcaps} is given by $\MP_1 = \{\{v_1\}, \{v_2,v_3,v_4,v_5\}, \{v_6,v_7,v_8,v_9\}\}$ and $\MQ_1 = \{\{w_1,w_2,w_3,w_4\}, \{w_5,w_6\}\}$. Consider $Q\coloneqq \{w_1,w_2,w_3,w_4\}$, and note that $A_{\star,Q}$ admits an affine TU decomposition using $A_{\star,Q} = \begin{bmatrix}
        \zerovec_{1\times4}\\
        A_{V\setminus \{v_1\},Q}
    \end{bmatrix} + \begin{bmatrix}
        2 \\
        \zerovec_{8\times 1}
    \end{bmatrix} \begin{bmatrix}
        1 & 1 & 1 & 1
    \end{bmatrix}$, where it can be verified that the matrix $\begin{bmatrix}
        \zerovec_{1\times4}\\
        A_{V\setminus \{v_1\},Q}\\
        \onevec_{1\times,4}
    \end{bmatrix}$ is totally unimodular. Thus, initially, [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"} will reformulate the integrality constraints on $Q$. Then, [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"} attempts to reformulate the integrality constraints for $\{w_5,w_6\}$ and fails to do so. Thus, we refine $\{w_5,w_6\}$ into $\{w_5\},\{w_6\}$, and run [ReflectionReduction]{.smallcaps} again, which results in the partition given by $\MP_2 =\{\{v_1\}, \{v_2,v_3\},\{v_4,v_5\}, \{v_6,v_7\},\{v_8,v_9\}\}$ and $\MQ_2 = \{\{w_1,w_2\},\{w_3,w_4\},\{w_5\},\{w_6\}\}$. Note for $\MQ_2$ that $Q$ is now split up into the two parts $\{w_1,w_2\}$ and $\{w_3,w_4\}$. However, this also affects the affine TU decomposition that we previously computed, as the matrix $\transpose{\Pi_\MQ}$ that represents the $T$ matrix in the affine TU decomposition is refined from $\transpose{\Pi_{\MQ_1}}$ to $\transpose{\Pi_{\MQ_2}}$, where the nonzero submatrix on $Q$ changes from $\onevec_{1\times 4}$ to $\begin{bmatrix}
        1 & 1 & 0 & 0\\
        0 & 0 & 1 & 1
    \end{bmatrix}$. Unfortunately, the matrix $\begin{bmatrix}
        0 & 0 & 0 & 0 \\
        \multicolumn{4}{c}{A_{V\setminus \{v_1\},Q}}\\
        1 & 1 & 0 & 0 \\
        0 & 0 & 1 & 1 
    \end{bmatrix}$ is not totally unimodular, which invalidates the previously computed affine TU decomposition. Thus, it may be the case that after a run of [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"} that the affine TU decomposition that is computed no longer matches the equitable partition, due to the additional refinements that are computed in line [\[algo_eos_additional_refinements\]](#algo_eos_additional_refinements){reference-type="ref" reference="algo_eos_additional_refinements"} of [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"}.
:::

::: lemma
[]{#thm_refinement_integrality_okay label="thm_refinement_integrality_okay"} Let $(\MP^1,\MQ^1,\gamma^1,\lambda^1,\delta,V^1_O,W^1_O)$ be a reflection reduction of $G\coloneqq P(A,b,\ell,u)$ and let it be given that for some $\widehat{\MQ^1} \subseteq \MQ^1_I$ that $H_d \coloneqq \{ x \in G \mid (\transpose{\Pi_{\MQ^1}} \Lambda^1 x_{W^1_O})_{\widehat{\MQ^1}} = d \}$ is a ${W_I}$-integral polyhedron for all $d\in \Z^{\widehat{\MQ^1}}$. Consider any refinement $(\MP^2,\MQ^2, \lambda^2, \gamma^2,\delta,V^2_O,W^2_O)$ of the given reflection reduction where $\widehat{\MQ}^2 \subseteq \MQ^2$ corresponds to the parts that were refined from $\widehat{\MQ}^1$ such that $\bigcup_{Q\in \widehat{\MQ}^2} Q = \bigcup_{Q\in \widehat{\MQ}^1} Q$ holds. Then, [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} holds for the refined reduction, i.e. we have: $$\mathrm{conv}(G\cap \M^{W_I}) = \mathrm{conv}(\{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{{\MQ^2_I}} \in \Z^{{\MQ^2_I}}\}) = \mathrm{conv}(\{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{\widehat{\MQ^2}} \in \Z^{\widehat{\MQ^2}}\}),$$
:::

::: proof
*Proof.* First, let us show a few facts about the refined reduction $(\MP^2,\MQ^2, \lambda, \gamma,\delta,V^2_O,W^2_O)$. First of all, note that $\MP^2$ and $\MQ^2$ must refine $\MP^1$ and $\MQ^1$ respectively, and we must have $W^1_O\subseteq W^2_O$ since additional refinements can only turn bipolar variables into unipolar variables, but not the other way around. Furthermore, note that additional refinements cannot change the value of $\lambda^1_w$ for $w\in W^1_O$, since the relative signs of unipolar parts are fixed. Thus, $\lambda^{1} = \lambda^{2}_{W^1_O}$ holds. By design of our algorithm, $\delta$ is constant in both reductions. Then, we claim that the following holds: $$G\cap \M^{W_I}
        \subseteq \{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{\widehat{\MQ^2}} \in \Z^{\widehat{\MQ^2}}\} \subseteq \{x \in G \mid (\transpose{\Pi_{\MQ^1}} \Lambda^1 x_{W^1_O})_{\widehat{\MQ^1}} \in \Z^{\widehat{\MQ^1}}\}.$$ Here, the first inclusion follows since $\transpose{\Pi_\MQ} \Lambda^2$ is an integral matrix. For the second inclusion, consider any $x \in \{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{\widehat{\MQ^2}} \in \Z^{\widehat{\MQ^2}}\}$. Then, consider any $Q \in \widehat{\MQ^1}$. Since $\MQ^2$ refines $\MQ^1$, there exist parts $Q'_i \in \widehat{\MQ^2}$ for $i=1,\cdots,k$ such that $\bigcup_{i=1}^k Q'_i = Q$ holds. Then, we can derive that:

$$(\transpose{\Pi_{\MQ^1}} \Lambda^1 x_{W^1_O})_{Q} = \sum_{w\in Q} \lambda^1_w x_w = \sum_{i=1}^k \sum_{w\in Q'_i} \lambda^1_w x_w \stackrel{\textup{(a)}}{=} \sum_{i=1}^k \sum_{w\in Q'_i} \lambda^2_w x_w = \sum_{i=1}^k (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{Q'_i},$$ where [(a)]{.upright} holds since $\lambda^1 = \lambda^2_{W^1_O}$ holds, and the final expression is integral by integrality of $(\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{Q'_i}$, using that $Q'_i \in \widehat{Q^2}$.

Taking convex hulls, we note that by applying [\[thm_affine_fiber_integral\]](#thm_affine_fiber_integral){reference-type="ref" reference="thm_affine_fiber_integral"}, using ${W_I}$-integrality of $H_d$, we have equality throughout: $$\mathrm{conv}(G\cap \M^{W_I}) = \mathrm{conv}(\{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{\widehat{\MQ^2}} \in \Z^{\widehat{\MQ^2}}\}) = \mathrm{conv}(\{x \in G \mid (\transpose{\Pi_{\MQ^1}} \Lambda^1 x_{W^1_O})_{\widehat{\MQ^1}} \in \Z^{\widehat{\MQ^1}}\}).$$ Finally, we have the following inclusions: $$G\cap \M^{W_I}
         \subseteq \{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^1_O})_{\MQ^2_I} \in \Z^{\MQ^2_I}\} \subseteq \{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{\widehat{\MQ^2}} \in \Z^{\widehat{\MQ^2}}\},$$ taking convex hulls and noting that the first and last sets are equal, we again have equality throughout, which concludes the proof $$\mathrm{conv}(G\cap \M^{W_I})
         = \mathrm{conv}(\{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^1_O})_{\MQ^2_I} \in \Z^{\MQ^2_I}\}) = \mathrm{conv}(\{x \in G \mid (\transpose{\Pi_{\MQ^2}} \Lambda^2 x_{W^2_O})_{\widehat{\MQ^2}} \in \Z^{\widehat{\MQ^2}}\}),$$ ◻
:::

It is not too difficult to see that finding a solution to the original problem can also still be done in polynomial time by simply considering the fiber $H_d$ defined where the affine subspaces are defined by $\Pi_\MQ^1 \Lambda^1 x_{W^1_O} = d$. In [\[example_refinement_problematic\]](#example_refinement_problematic){reference-type="ref" reference="example_refinement_problematic"}, this corresponds to adding the equality $x_1 + x_2 + x_3 + x_4 = y_{1,2} + y_{3,4}$ in the postsolve procedure rather than the two equalities $x_1 + x_2 = y_{1,2}$ and $x_3 + x_4 = y_{3,4}$ which are shown to be problematic in [\[example_refinement_problematic\]](#example_refinement_problematic){reference-type="ref" reference="example_refinement_problematic"}. Although the latter two equalities clearly imply the former equality, adding them to the linear program breaks the integrality guarantee.

Next, let us consider the total runtime. As for linear programs, we assume that the reflection reduction uses a $\delta$-vector whose bitlength is of the same order in the worst-case, which is reasonable as the choice for $\delta$ that is described in [\[thm_delta_equivalent_complemented\]](#thm_delta_equivalent_complemented){reference-type="ref" reference="thm_delta_equivalent_complemented"} satisfies this assumption.

::: theorem
For a mixed-integer linear program $F(A,b,\ell,u,c)$ with $A\in \R^{V\times W}$ and integer variables $W_I\subseteq W$, let $m$ be the total bitlength of the entries of $\begin{bmatrix}
    \ell & 0 \\
    u & 0 \\
    c & 0\\
    A & b
\end{bmatrix}$ and let $n = |V| + |W|$. Assuming that [ReflectionRefinement]{.smallcaps} computes a $\delta$ with total bitlength $\orderO(m)$, [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"} computes a reflection reduction $(\MP,\MQ,\gamma,\lambda,\delta,V_U,W_U)$ of $F(A,b,\ell,u,c)$ such that [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} holds, i.e.: $$\mathrm{conv}(\{x\in P(A,b,\ell,u) \mid (\transpose{\Pi_{\MQ}} \Lambda x)_{\MQ_I} \in \Z^{\MQ_I}\}) = \mathrm{conv}(P(A,b,\ell,u)\cap \M^{W_I})$$ in $\orderO(n+m)$ space and $\orderO((n+m)\log n)$ time using network matrices or $\orderO(n^2\alpha(n,n) + m \log(n))$ time using transposed network matrices.
:::

::: proof
*Proof.* We do not provide a complete proof of every step here, but instead emphasize the most relevant parts of the correctness proof and the running time. First let us prove correctness. In lines [\[algo_eos_start\]](#algo_eos_start){reference-type="ref" reference="algo_eos_start"}-[\[algo_eos_point1\]](#algo_eos_point1){reference-type="ref" reference="algo_eos_point1"}, we compute the connected components of the continuous variables that are (transposed) network, which is necessary to compute our affine TU decomposition. Then, we compute an initial reflection reduction in lines [\[algo_eos_point2\]](#algo_eos_point2){reference-type="ref" reference="algo_eos_point2"}-[\[algo_eos_first_refine\]](#algo_eos_first_refine){reference-type="ref" reference="algo_eos_first_refine"}, where $\MQ_1$ satisfies the following for all $Q\in \MQ_1$:

1.  Either $Q\cap W_I$ or $Q\subseteq W_I$ holds.

2.  If $Q\subseteq W_I$, then $A_{V_R,w} = \pm A_{V_R,w'}$ and $\mathrm{ntmask}(A_{V\setminus V_R,w}) = \pm \mathrm{ntmask}(A_{V\setminus V_R,w'})$ hold for all $w,w'\in Q$.

In lines [\[algo_eos_start_ATU\]](#algo_eos_start_ATU){reference-type="ref" reference="algo_eos_start_ATU"}-[\[algo_eos_end_ATU\]](#algo_eos_end_ATU){reference-type="ref" reference="algo_eos_end_ATU"}, we greedily construct an affine TU decomposition that satisfies the conditions of [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} where we keep the invariant that $T$ is equal to $(\transpose{\Pi_{\MQ^1}} \Lambda)_Q$ for some $\MQ'\subseteq \MQ^1$. The construction uses condition 2. by testing if the vector $\begin{bmatrix}
        A_{V_R,w} \\
        \mathrm{ntmask}(A_{V\setminus V_R,w})
    \end{bmatrix}$, which is identical up to $\pm 1$ scale for all $w\in Q$ by construction, can be used to augment the (transposed) network matrix in the affine TU decomposition. Our construction does not always add such a column to $u$: we determine dynamically if this is necessary by checking if $V_{\mathrm{cancel}} \neq \emptyset$ holds. If an additional column in the $U$-matrix is needed, we add $Q$ to $\MQ'$ and add the row $(\transpose{\Pi_{\MQ^1}} \Lambda)_Q$ to $T$. Otherwise, we leave $\MQ'$ and $T$ unchanged. By doing so for all columns, we ensure that $T = \transpose{\Pi_{\MQ'}} \Lambda$ holds. For any $Q\in \MQ^1$ that can not added to the affine TU decomposition, we simply split it into single-variable parts in $\MQ^1$ to satisfy the conditions of the affine TU decomposition. Then, it follows from [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref" reference="thm_atu_milp_integral"} and [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref" reference="thm_fibers_symmetry_integral"} that for $\MQ^1_I = \{Q \in \MQ^1 \mid Q\subseteq W_I \}$ we have: $$\label{eq_before_refinement_condition}
    \mathrm{conv}(\{x\in P(A,b,\ell,u) \mid (\transpose{\Pi_{\MQ^1}} \Lambda x)_{\MQ^1_I} \in \Z^{\MQ^1_I}\}) = \mathrm{conv}(P(A,b,\ell,u)\cap \M^{W_I}).$$ Finally, we refine $\MQ^1$ to $\MQ^2$ in [\[algo_eos_additional_refinements\]](#algo_eos_additional_refinements){reference-type="ref" reference="algo_eos_additional_refinements"} to ensure that $\MQ^2$ corresponds to a reflection reduction. By [\[eq_before_refinement_condition\]](#eq_before_refinement_condition){reference-type="eqref" reference="eq_before_refinement_condition"} and the fact that $\MQ^2$ refines $\MQ^1$, [\[thm_refinement_integrality_okay\]](#thm_refinement_integrality_okay){reference-type="ref" reference="thm_refinement_integrality_okay"} shows for $\MQ^2_I \coloneqq \{Q \in \MQ^2 \mid Q\subseteq W_I \}$ that $$\mathrm{conv}(\{x\in P(A,b,\ell,u) \mid (\transpose{\Pi_{\MQ^2}} \Lambda x)_{\MQ^1_I} \in \Z^{\MQ^2_I}\}) = \mathrm{conv}(P(A,b,\ell,u)\cap \M^{W_I}).$$ Then, since $(\MP^2,\MQ^2, \lambda, \gamma, \delta, V^2_O, W^2_O)$ is a reflection reduction of $F(A,b,\ell,u,c)$, it follows that the conditions of [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref" reference="thm_milp_folding"} hold. Thus, we have shown correctness of [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"}.\
Next, let us consider the running time and space-complexity of [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"}. First of all, $\textsc{ReflectionRefinement}$ runs in $\orderO((n+m) \log(n))$ and $\orderO(n+m)$ space by [\[thm_running_time_extended\]](#thm_running_time_extended){reference-type="ref" reference="thm_running_time_extended"} and is called twice. Note that we use the fact that $\delta$ has bitlength at most $\orderO(m)$.

At the start of the [\[algo_eos\]](#algo_eos){reference-type="ref" reference="algo_eos"}, we compute the connected components of the submatrix formed by the continuous columns. This can be done in $\orderO(n)$ time and space by using a depth-first search.

Computing the initial partition $\MQ_0$ can be done in $\orderO(n+m)$ time and space by using standard hashing techniques. Sorting $\MQ^1$ can be done in $\orderO(n \log(n))$ time.

Finally, we note that $\mathrm{AugmentNetwork}$ is called at most once for every column. The matrix $M$ has size $(|V| + |\MQ|)  \times |W|$, which is of the order $\orderO(n) \times \orderO(n)$. Moreover, $M$ has $\orderO(m)$ nonzeros as it has fewer nonzeros than $A$, since we only add the additional row of $(\transpose{\Pi_\MQ} \Lambda)_Q$ for all $Q \in \MQ$ if it can be used to cancel one or more rows from $A_{\star,Q}$. We note that regardless of the size of the nonzero entries, one can check in constant time if a nonzero has value $\pm 1$. For network matrices the column augmentation algorithm by Bixby and Wagner then runs in $\orderO(m \alpha(m,n))$ time, where $\alpha$ is the inverse Ackermann function, which grows extremely slowly and is dominated by the order $\orderO((n+m) \log(n))$ running time for the reflection reduction. The transposed network algorithm by van der Hulst and Walter runs in $\orderO(n^2 \alpha(n,n))$ time, and dominates the total runtime in case it is used. Taking the bitlength $m$ into account, we can simplify to $\orderO(n^2 \alpha(n,n) + m\log(n))$ in this case. ◻
:::
