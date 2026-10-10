---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-014-dimension-reduction-for-mixed-integer-linear-pro
section_title: "Dimension Reduction for Mixed-Integer Linear Programs"
section_number: null
pages: 37-44
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
text_source: latex
latex_prose_ratio: 0.753
latex_coverage_ratio: 0.779
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
[]{#sec_dimred_milp label="sec_dimred_milp"}

Throughout this section we consider a mixed-integer linear program given by a linear program $F(A,b,\ell,u,c)$ with $A\in\R^{V\times W}$, $b\in \R^V$, $\ell, u, c \in \R^W$ and integer variables $W_I \subseteq W$. For any partition $\MQ$ of $W$ that is compatible with $W_I$, we use $\MQ_I \coloneqq \{Q \in \MQ \mid Q \subseteq W_I\}$ to denote the corresponding partition over the integer variables.\
Let us consider the effect of DRCR in context of mixed-integer linear programs. For the mixed-integer linear program given by $F(A,b,\ell,u,c)$ and integrality constraints $x \in \M^{W_I}$, we consider the *reduced problem* $R^{\MP,\MQ}(F(A,b,\ell,u,c))$ with integrality constraints $y\in \M^{\MQ_I}$ for $y\in R^{\MP,\MQ}(F(A,b,\ell,u,c))$. For the linear programming relaxations, [\[thm_lp_folding\]](#thm_lp_folding){reference-type="ref+label" reference="thm_lp_folding"} establishes a correspondence between the original and the reduced problem. Let us consider how these mappings interact with integrality. For a solution $x\in F(A,b,\ell,u,c)\cap \M^{W_I}$, we can observe that $y \coloneqq \transpose{\Pi_{\MQ}} x$ satisfies the integrality constraints for the reduced problem, since then $y_Q \coloneqq \sum_{w\in Q} x_w$ is integral for any $Q\in \MQ_I$ as it is the sum of integral values. Linear feasibility and optimality are guaranteed already by [\[thm_lp_folding\]](#thm_lp_folding){reference-type="ref+label" reference="thm_lp_folding"}. Thus, every mixed-integer solution for the original problem maps to a mixed-integer solution of the reduced problem. However, for the other direction integrality is not preserved, since for $y\in R^{\MP,\MQ}(F(A,b,\ell,u,c))\cap \M^{\MQ_I}$ the original solution is given for $w\in W$ with $w\in Q$ by $x_w \coloneqq \frac{1}{|Q|} y_Q$, which is not necessarily integral. In particular, this is an issue if the reduced problem contains integer solutions $y\in R^{\MP,\MQ}(F(A,b,\ell,u,c)) \cap \M^{Q_I}$ that do not map to integer solutions of the original problem. Previous works on Orbital Shrinking [@Fischetti2012; @Fischetti2017; @Salvagnin2013] deal with this limitation by solving a feasibility subproblem, which checks if the provided mixed-integer solution for the reduced problem can be mapped to a mixed-integer solution of the original problem. For any fixed mixed-integer $y$-solution, these subproblems can be formulated by adding the constraints $\transpose{\Pi_\MQ} x = y$ to the original MILP. This subproblem is a mixed-integer linear program of reduced size with no objective, and the DRCR procedures defines a point that is feasible for its LP relaxation. Frequently, this subproblem is solved using techniques such as constraint programming that exploit the specific structure of the subproblem [@Salvagnin2012; @Salvagnin2013].\
In this work, we take a different approach compared to previous works on Orbital Shrinking by characterizing when each solution of the reduced problem corresponds to a solution of the original model. In terms of orbital shrinking, one can think of our approach as *Exact Orbital Shrinking*, where the orbital shrinking subproblem is given by a perfect formulation of a mixed-integer linear program. In this case, the orbital shrinking subproblem can be solved via linear programming. One of the main advantages of our approach is that it guarantees a tight correspondence between the mixed-integer solutions of the original and the reduced problem, and that the subproblems can be solved easily via linear programming. This correspondence comes at a cost: the main downside of our approach is that it cannot handle all symmetries. Due to the requirement that the subproblem is a perfect formulation, our approach cannot in general handle the complete symmetry group of the MILP, and instead only handles a subgroup of the symmetry group that generates subproblems that are perfect formulations.\
In [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"}, we characterize when reflection reductions, which generalize the DRCR procedure, can be used to reduce the dimension of a mixed-integer linear program.

::: theorem
[]{#thm_milp_folding label="thm_milp_folding"} Let $(\MP,\MQ,\gamma,\lambda,\delta,V_U,W_U)$ be a reflection reduction of $F(A,b,\ell,u,c)$ such that $\delta\in \M^{W_I\cap W_U}$ holds and $W_I \cap W_U$ is compatible with $\MQ$. We formulate the reduced mixed integer program using $A'\coloneqq \transpose{\Pi_{\MP}}\Gamma A_{V_U,W_U}\Lambda \widetilde{\Pi_{\MQ}}$, $b'\coloneqq \transpose{\Pi_{\MP}}\Gamma(b_{V_U} - A_{V_U,W_U} \delta_{W_U})$, $\ell' \coloneqq \transpose{\Pi_{\MQ}} \ell^{\lambda,\delta}_{W_U}$, $u'\coloneqq  \transpose{\Pi_{\MQ}} u^{\lambda,\delta}_{W_U}$ and $c'\coloneqq \transpose{\widetilde{\Pi_\MQ}} \Lambda c_{W_U}$. If the following equation holds $$\begin{equation}
        \label{thm_milp_folding_condition}
        \mathrm{conv}(\{x\in P(A,b,\ell,u) \mid (\transpose{\Pi_{\MQ}} \Lambda x)_{\MQ_I} \in \Z^{\MQ_I}\}) = \mathrm{conv}(P(A,b,\ell,u)\cap \M^{W_I})
\end{equation}$$ then the following hold:

1.  []{#thm_milp_folding_to_red label="thm_milp_folding_to_red"} For any $x\in P(A,b,\ell,u)\cap \M^{W_I}$, then $y\coloneqq \transpose{\Pi_{\MQ}} \Lambda (x_{W_U}-\delta_{W_U}) \in P(A',b',\ell',u')\cap \M^{\MQ_{I}}$ and $\transpose{c} x = \transpose{c'} y + \transpose{c} \delta$ hold.

2.  []{#thm_milp_folding_from_red label="thm_milp_folding_from_red"} For any $y\in P(A',b',\ell',u') \cap \M^{\MQ_{I}}$ there exists a solution $x\in P(A,b,\ell,u) \cap \M^{W_I}$ such that $\transpose{c} x \leq \transpose{c'} y + \transpose{c} \delta$ hold.
:::

::: proof
*Proof.* First, consider the proof of the first point. By [\[def_refeqpart\]](#def_refeqpart){reference-type="ref+label" reference="def_refeqpart"}[\[def_refeqpart_to_red\]](#def_refeqpart_to_red){reference-type="ref" reference="def_refeqpart_to_red"}, it follows that $y\in P(A',b',\ell',u')$ and $\transpose{c} x = \transpose{c'} y + \transpose{c} \delta$ hold. Thus, it is sufficient to show that $y\in \M^{\MQ_I}$ holds. First, since $x\in \M^{W_I}$ and $\delta\in \M^{W_I\cap W_U}$ hold we have that $x_{W_U} - \delta_{W_U} \in \M^{W_I\cap W_U}$. Then, for any $Q\in \MQ_I$, we have that $y_Q = (\transpose{\Pi_{\MQ}} \Lambda (x_{W_U} - \delta_{W_U}))_Q = \sum_{w\in Q} \lambda_w (x_w - \delta_w)$. Since $Q\in \MQ_I$ holds, it follows that all $w\in Q$ satisfy $w\in W_I$. Thus, this implies that $x_w$ and $\delta_w$ must be integral by the given conditions. Then, since $\lambda_w$ is also integral, it follows that $y_Q$ is integral. Since this holds for any $Q\in \MQ_I$, we have $y\in \M^{\MQ_I}$.

We proceed with the proof of the second point. Let $y\in P(A',b',\ell',u')\cap \M^{\MQ_I}$ be given. Then, by [\[def_refeqpart\]](#def_refeqpart){reference-type="ref+label" reference="def_refeqpart"}[\[def_refeqpart_from_red\]](#def_refeqpart_from_red){reference-type="ref" reference="def_refeqpart_from_red"} we have for $x' \coloneqq (\Lambda \widetilde{\Pi_\MQ} y, \zerovec) + \delta$ that $x'\in P(A,b,\ell,u)$ and $\transpose{c'} y +\transpose{c} \delta = \transpose{c} x'$ hold. Then, we observe that for each $Q\in \MQ$, we have the following for $\transpose{\Pi_{\MQ}} \Lambda x'$: $$\begin{align*}
        (\transpose{\Pi_{\MQ}} \Lambda x')_Q = \sum_{w\in Q} \lambda_w x'_w &= \sum_{w\in Q} \lambda_w (\frac{\lambda_w y_Q}{|Q|} + \delta_w) = \sum_{w\in Q} \frac{y_Q}{|Q|} + \lambda_w \delta_w = y_Q + \sum_{w\in Q} \lambda_w \delta_w.
\end{align*}$$ Then, for $Q\in \MQ_I$, $y_Q$ is integral by assumption, and all $w\in Q$ lie in $W_I$ by definition, which shows that $\sum_{w\in Q} \lambda_w \delta_w$ is integral since $\delta\in \M^{W_I\cap W_U}$ holds. Thus, we have that $x'\in \mathrm{conv}(\{x\in P(A,b,\ell,u) \mid (\transpose{\Pi_{\MQ}} \Lambda x)_{\MQ_I} \in \Z^{\MQ_I}\})$ holds. By the equality in [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} we have that $x'\in \mathrm{conv}(P(A,b,\ell,u)\cap \M^{W_I})$ holds. Since $\mathrm{conv}(P(A,b,\ell,u)\cap \M^{W_I})$ is a convex polyhedron, there exists some $x\in P(A,b,\ell,u)\cap \M^{W_I}$ such that $\transpose{c} x \leq \transpose{c} x'$ holds. Then $\transpose{c} x \leq \transpose{c'} y +\transpose{c} \delta$ follows, which completes the proof. ◻
:::

[\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+Label" reference="thm_milp_folding"} differs from reflection reductions in a few subtle but important ways. First of all, the new and crucial condition [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} in [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} states for each part $Q\in \MQ_I$ that the integrality of all variables in $Q$ must be implied by the integrality of the sum $\sum_{w\in Q} \lambda_w x_w \in \Z$. We will later elaborate on a few different methods to detect this fact. Additionally, note that the partition $\MQ$ may not have parts that contain both integer and continuous variables and that $\delta_{W_I\cap W_U}$ must be integral.

In the second point of [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} we only show existence of a better solution in the original problem, rather than proving that a direct mapping exists, as was done in [\[thm_lp_folding\]](#thm_lp_folding){reference-type="ref+label" reference="thm_lp_folding"}. This is due to the fact that the mapped solution, $x'$ in the proof, does not necessarily satisfy all the integrality constraints for $W_I$, even though it is feasible for the linear relaxation. This raises an important issue; it is not yet clear how, given arbitrary $x'\in P(A',b',\ell',u')$, if one can obtain in polynomial time a solution solution $x$ to the original problem that also satisfies the integrality constraints. Intuitively, one may suspect that it is sufficient to consider the affine subspace generated by $x = \transpose{\Pi_{\MQ}} \Lambda (x_{W_U} - \delta_{W_U})$ in the original problem and recover an original solution. This approach is also taken in Orbital Shrinking [@Fischetti2017]. However, we show in [\[example_fiber_nonintegral\]](#example_fiber_nonintegral){reference-type="ref+label" reference="example_fiber_nonintegral"} that it may be the case that there exists no solution $x\in P(A,b,\ell,u) \cap \M^{W_I}$ such that $x' = \transpose{\Pi_{\MQ}} \Lambda (x_{W_U} - \delta_{W_U})$ holds, even though the conditions of [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} and $x'\in \M^{\MQ_I}$ hold. This fact is an important limitation for Orbital Shrinking [@Fischetti2017] as it may be difficult to recover integral solutions for the original integer program.

::: example
[]{#example_fiber_nonintegral label="example_fiber_nonintegral"} Consider the integer program given by polyhedron $P = \{(x,y)\in \R^2 \mid -x + 2 y \leq 2, ~ 2x - y \leq 2, x \geq 0, y \geq 0 \}$ and $x\in \Z, y\in \Z$ and note that $P = \mathrm{conv}(P\cap \Z^2) = \mathrm{conv}(\{(x,y) \in P \mid x+y\in \Z\})$ holds and that [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} is applicable to the standard representation of the integer program, where $\lambda= \gamma = \onevec$, $V_U = V$ and $W_U = W$ hold. See [\[fig_fiber_nonintegral_example\]](#fig_fiber_nonintegral_example){reference-type="ref+Label" reference="fig_fiber_nonintegral_example"} for the geometric representation of $P$. For the reduced integer program $P' = \{z\in \R \mid z\leq 4, z\geq 0\}\cap \Z$, $z=3$ is a feasible integer solution. However, there exists no solution $(x,y)\in P$ such that $x+y=3$, $x\in \Z$ and $y\in \Z$ hold.
:::

<figure data-latex-placement="h">
<figure>

</figure>
<figure>

</figure>
<figcaption>Examples of symmetric integral polyhedra with non-integral affine fibers</figcaption>
</figure>

Finally, [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} clarifies the need to prove the variant of [\[thm_lp_folding\]](#thm_lp_folding){reference-type="ref+label" reference="thm_lp_folding"} compared to that in [@Grohe2014]. In [@Grohe2014], the mapping from the original to the reduced problem is scaled, which makes it so that integrality of the original solution does not imply integrality of the mapped solution in the reduced problem. Instead, we require the scaling as in [\[thm_lp_folding\]](#thm_lp_folding){reference-type="ref+label" reference="thm_lp_folding"} in [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} to ensure that we can map integral solutions between the original and the reduced problem. A similar scaling is also used in Orbital Shrinking [@Fischetti2017].\
Next, we will consider several methods to detect that [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} is satisfied. For each method, we additionally show that a solution to the original problem can be recovered in polynomial time from a solution to the reduced problem.

First, we show in [\[thm_integer_unit_partition\]](#thm_integer_unit_partition){reference-type="ref+label" reference="thm_integer_unit_partition"} that an equitable partition where each integer variable is contained in its own part of size $1$ satisfies [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"}. This result seems to already be known as a folklore result within the integer programming solver community[^1], but to the best of our knowledge it was never documented in public. This idea also extends naturally to reflection reductions.

::: lemma
[]{#thm_integer_unit_partition label="thm_integer_unit_partition"} If $\delta\in \M^{W_I}$ and if for each $w\in W_I$, $\{w\}\in \MQ$ holds, then [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} is satisfied. Additionally, for every $y\in P(A',b',\ell',u')\cap \M^{\MQ_I}$, $x' \coloneqq (\Lambda \widetilde{\Pi_\MQ} y, \zerovec)  + \delta$ lies in $P(A,b,\ell, u)\cap \M^{W_I}$.
:::

::: proof
*Proof.* For the first point, note that $(\transpose{\Pi_{\MQ}} \Lambda x)_{\MQ_I} \in \Z^{\MQ_I} \iff (\Lambda x)_{W_I} \in \Z^{W_I} \iff x_{W_I} \in \Z^{W_I}$ holds, where the first equivalence follows since every $w\in W_I$ is a part of size one. The second equivalence holds since $\Lambda$ is a unimodular matrix. Thus, this directly establishes that [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} holds.

For the second point, note that for all $\{w\} = Q\in \MQ_{I}$, $x_w=((\Lambda \widetilde{\Pi_\MQ} y, \zerovec)  + \delta)_w = \lambda_w y_Q + \delta_w$ holds since $|Q|=1$ holds. The latter expression is integral since $y_Q$, $\delta_w$ and $\lambda_w$ are all integral, which shows that $x\in \M^{W_I}$. By [\[def_refeqpart\]](#def_refeqpart){reference-type="ref+label" reference="def_refeqpart"}[\[def_refeqpart_from_red\]](#def_refeqpart_from_red){reference-type="ref" reference="def_refeqpart_from_red"}, $x\in P(A,b,\ell,u)$ holds, which completes the proof. ◻
:::

It is implicit in [\[thm_integer_unit_partition\]](#thm_integer_unit_partition){reference-type="ref+label" reference="thm_integer_unit_partition"} that all bipolar parts must consist of continuous variables only by the condition that each $w\in W_I$ has $\{w\}\in \MQ$. This condition is not required in [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"}.

The condition in [\[thm_integer_unit_partition\]](#thm_integer_unit_partition){reference-type="ref+label" reference="thm_integer_unit_partition"} that each integer variable is in its own partition class can be easily enforced during detection by modifying the initial partition $\MQ_0$ of the refinement algorithm. The condition also implies a strong condition on the rows by the requirement that the partition is equitable for the constraint matrix. In particular, this implies that for any $P\in \MP$ that $A_{v_1,w} = A_{v_2,w}$ holds for any $v_1,v_2\in P$ and $w\in W_I$. In other words, for any two rows $v_1,v_2$ that are in the same row partition, the rows must be identical in the column submatrix $A_{\star, W_I}$. Another perspective is that we are considering DRCR for a parametric set of LPs, whose right-hand sides depend on the fixed integer values for the $x_{W_I}$ variables. Since the right-hand sides for two rows in the same row-block need to be identical under all fixed integer values of $x_{W_I}$, their rows in $A_{\star,W_I}$ must be identical.\
Although [\[thm_integer_unit_partition\]](#thm_integer_unit_partition){reference-type="ref+label" reference="thm_integer_unit_partition"} is very useful, the detection of [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} is mostly seen as an afterthought and is done by making the partition much finer. Thus, we investigate more sophisticated methods to detect [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} which do not require every integer variable to be in its own part, so that we may also aggregate integer variables. In the context of detecting equivalent mixed-integer formulations as we have in [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"}, there are two works that are relevant to the current work. Recall that a matrix $A$ is said to be *totally unimodular* if $\det(A')= \pm 1$ holds for every nonsingular square submatrix $A'$ of $A$. A famous result by Hoffman and Kruskal [@HoffmanK56] shows that $\{x \in \R^n \mid A x \leq b, x\geq 0\}$ defines an integral polyhedron for all $b\in \Z^m$ if and only if $A$ is totally unimodular. First of all, the author has previously investigated the phenomenon of *implied integrality* [@VanDerHulst2025], which is said to occur when $\mathrm{conv}(P\cap \M^W) = \mathrm{conv}(P\cap \M^{W'})$ holds for some $W'\subseteq W$. There, implied integrality is detected by detecting totally unimodular submatrices within the constraint matrix.\
In their work, Bader, Hildebrand, Weismantel and Zenklusen [@BaderHWZ18] investigate methods to detect matrices $T\in \Z^{k\times n}$ where $k < n$ such that $\mathrm{conv}(\{x \in P \mid T x \in \Z^k\}) = \mathrm{conv}(P\cap \Z^n)$ holds. They investigate the case where $T$ is totally unimodular and formulate the notion of an *affine totally unimodular decomposition* (affine TU decomposition) to detect such cases.

::: definition
A matrix $A\in \Z^{m\times n}$ admits a *$k$-row affine totally unimodular decomposition* if there exist matrices $S \in \Z^{m\times n}$, $U\in \Z^{m\times k}$ and $T\in \Z^{k\times n}$ such that $\begin{bmatrix}
    S\\
    T
\end{bmatrix}$ is totally unimodular and $A = S + U T$ holds.
:::

In particular, they show that affine TU decompositions can be used to remove and reformulate integrality constraints.

::: proposition
[]{#thm_atu_ilp_integral label="thm_atu_ilp_integral"} Let $A = S + UT \in \Z^{m\times n}$ with $T\in \{-1,0,1\}^{k\times n}$ be a $k$-row affine TU decomposition and $b\in \Z^m$ and $\ell\in (\Z\cup \{-\infty\})$, $u\in(\Z\cup \{\infty\}$ with $\ell \leq u$. Then for $P = \{x\in \R^n \mid~\ell \leq x \leq u, Ax \leq b\}$ it holds that $\mathrm{conv}(\{x\in P \mid Tx \in \Z^k\}) = \mathrm{conv}(P\cap \Z^n)$.
:::

Note that the matrix $\transpose{\Pi_{\MQ}} \Lambda$ in [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} is totally unimodular as it contains at most one $\pm 1$ entry in every column. Thus, the notion of an affine TU decomposition is very suitable for our setting.

One idea which is central to the proof of [\[thm_atu_ilp_integral\]](#thm_atu_ilp_integral){reference-type="ref+Label" reference="thm_atu_ilp_integral"} and the detection of implied integrality, is to show that every *fiber* defined by a linear subspace of $P$ given by $T x = d$ for some $d\in \Z^Q$ is (mixed)-integral. Although this is not a necessary condition for the possibility of a mixed-integer formulation (see [\[fig_fiber_nonintegral_example\]](#fig_fiber_nonintegral_example){reference-type="ref+label" reference="fig_fiber_nonintegral_example"}), it is practical to detect and exploit this condition. In our setting, imposing the requirement that the fibers have to be integral has the additional benefit that an integral solution to the original problem may be recovered in polynomial time, avoiding the issue in [\[fig_fiber_nonintegral_example\]](#fig_fiber_nonintegral_example){reference-type="ref+Label" reference="fig_fiber_nonintegral_example"}. We adapt [\[thm_affine_fiber_integral\]](#thm_affine_fiber_integral){reference-type="ref+label" reference="thm_affine_fiber_integral"} from the proof of [\[thm_atu_ilp_integral\]](#thm_atu_ilp_integral){reference-type="ref+label" reference="thm_atu_ilp_integral"} in [@BaderHWZ18] to work in a slightly more general mixed-integer setting.

::: lemma
[]{#thm_affine_fiber_integral label="thm_affine_fiber_integral"} Let $P \subseteq \R^W$ be a rational polyhedron, let $W_I\subseteq W$ denote the integer variables. Let $T\in \Z^{k\times W_I}$ be any integral matrix and consider the affine fiber $H_d \coloneqq \{x \in P \mid T x_{W_I} = d\}$ for any fixed $d\in \Z^k$. If $H_d$ is $W_I$-integral for every $d\in \Z^k$, then $\mathrm{conv}(\{x \in P \mid T x_{W_I} \in \Z^k\}) = \mathrm{conv}(P \cap \M^{W_I})$ holds.
:::

::: proof
*Proof.* Let $G \coloneqq \mathrm{conv}(\{ x\in P \mid Tx_{W_I} \in \Z^{k}\})$. First, we show that $G$ is a rational polyhedron. This is relatively easy to see, since it is the projection of the rational mixed integer program given by $G'\coloneqq \mathrm{conv}(\{(x,d) \in \M^{W_I} \times \Z^k \mid x \in P,~ Tx_{W_I} = d\})$. By Meyer's theorem [@Meyer74], $G'$ is a rational polyhedron. Then, since the projection of a rational polyhedron is again a polyhedron and $G = \mathrm{proj}_{x}(G')$, $G$ is also a rational polyhedron.

Then the following holds: $$\begin{align*}
        G &=\mathrm{conv}(\{ x\in P \mid Tx_{W_I} \in \Z^k\})= \mathrm{conv}(\bigcup_{d\in \Z^k} H_d) \stackrel{\textup{(a)}} =  \mathrm{conv}(\bigcup_{d\in \Z^k} \mathrm{conv}(H_d\cap \M^{W_I}))\\
        &= \mathrm{conv}(\bigcup_{d\in \Z^k} H_d \cap \M^{W_I})
        \stackrel{\textup{(b)}}= \mathrm{conv}( P \cap \M^{W_I}).
\end{align*}$$ The equality in [(a)]{.upright} follows from the fact that $H_d$ is $W_I$-integral. For [(b)]{.upright} note that $T$ is an integral matrix, which implies for all $x\in \M^{W_I}$ that $T x_{W_I} = d$ holds for some $d\in \Z^k$. Then, the equality $\bigcup_{d\in \Z^k}H_d \cap \M^{W_I} = P \cap \M^{W_I}$ holds since any $x\in P\cap \M^{W_I}$ must be contained in $H_d\cap \M^{W_I}$ for some $d\in \Z^k$, which implies that $P\cap \M^{W_I} \subseteq \bigcup_{d \in \Z^k} H_d\cap \M^{W_I}$ holds. The reverse inclusion follows easily since $H_d \subseteq P$ holds. ◻
:::

Then, using [\[thm_affine_fiber_integral\]](#thm_affine_fiber_integral){reference-type="ref+label" reference="thm_affine_fiber_integral"}, we show that one can recover solutions to the original problem from solutions to the reduced problem in polynomial time.

::: theorem
[]{#thm_fibers_symmetry_integral label="thm_fibers_symmetry_integral"} Consider the setting of [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} and let $\MQ'\subseteq \MQ_I$. If for each $d \in \Z^{\MQ'}$, $H_d \coloneqq \{x\in P(A,b,\ell,u) \mid 
    (\transpose{\Pi_\MQ} \Lambda x)_{\MQ'} = d\}$ is an $\M^{W_I}$-integral polyhedron then [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} holds and $H'_{d'} \coloneqq \{y\in P(A',b',\ell',u') \mid y_{\MQ'} = d'\}$ is a $\MQ_I$-integral polyhedron for each $d'\in Z^{\MQ'}$. Moreover, for every $y\in P(A',b',\ell',u')\cap \M^{Q'}$ there exists a feasible solution $x \in H_{d^y}\cap \M^{W_I}$ with $d^y \coloneqq (y + \transpose{\Pi_\MQ} \Lambda \delta_{W_U})_{\MQ'}$ that can be found in polynomial time, where $\transpose{c} x \leq \transpose{c'} y + \transpose{c} \delta$ holds.
:::

::: proof
*Proof.* For $G=P(A,b,\ell,u)$, we have that $$\begin{equation*}
        \{x\in G \mid (\transpose{\Pi_\MQ} \Lambda x)_{\MQ'} \in \Z^{\MQ'}\} \subseteq \{x\in G \mid (\transpose{\Pi_\MQ} \Lambda x)_{\MQ_I} \in \Z^{\MQ_I}\} \subseteq G \cap \M^{W_I},
\end{equation*}$$ where the first inclusion follows since $\MQ'\subseteq \MQ_I$ holds and the latter inclusion since $(\transpose{\Pi_\MQ} \Lambda x)_{\MQ_I} \in \Z^{\MQ_I}$ holds for all $x\in \M^{W_I}$. Then, by monotonicity of the convex hull we have: $$\begin{equation*}
        \mathrm{conv}(\{x\in G \mid (\transpose{\Pi_\MQ} \Lambda x)_{\MQ'} \in \Z^{\MQ'}\}) \subseteq \mathrm{conv}(\{x\in G \mid (\transpose{\Pi_\MQ} \Lambda x)_{\MQ_I} \in \Z^{\MQ_I}\}) \subseteq \mathrm{conv}(G\cap \M^{W_I}).
\end{equation*}$$

Since the conditions of [\[thm_affine_fiber_integral\]](#thm_affine_fiber_integral){reference-type="ref+label" reference="thm_affine_fiber_integral"} are satisfied for $\MQ'$, we have equality throughout, which shows that [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} holds.

Secondly, let $y\in P(A',b',\ell',u')\cap \M^{\MQ'}$ be a feasible solution to the reduced problem. By [\[def_refeqpart\]](#def_refeqpart){reference-type="ref+label" reference="def_refeqpart"}[\[def_refeqpart_from_red\]](#def_refeqpart_from_red){reference-type="ref" reference="def_refeqpart_from_red"} it holds for $x' \coloneqq (\Lambda \widetilde{\Pi_\MQ} y,\zerovec_{W_B}) + \delta$ that $x'\in P(A,b,\ell, u)$ and $\transpose{c} x' = \transpose{c'} y + \transpose{c} \delta$. Then, we have for $Q\in \MQ'$ that: $$\begin{equation*}
        (\transpose{\Pi_\MQ} \Lambda x')_Q = \sum_{w\in Q} \lambda_w x'_w = \sum_{w\in Q} \lambda_w (\lambda_w \frac{y_Q}{|Q|} + \delta_w) = y_Q + \sum_{w\in Q} \lambda_w \delta_w = (y + \transpose{\Pi_\MQ} \Lambda \delta_{W_U})_{Q} = d^y_{Q},
\end{equation*}$$ where $d^y_Q$ is integral by integrality of $y_Q$, $\Lambda$ and $\delta_{W_I\cap W_U}$. Note that we implicitly use that $Q\subseteq W_U$ holds, which is implied by $Q\in \MQ'$. Since this holds for any $Q\in \MQ'$, it follows that $x'\in H_{d^y}$ holds. Since $H_{d^y}$ is $W_I$-integral and nonempty since $x'\in H_{d^y}$ holds, the linear program $\min\{\transpose{c} x \mid x \in H_{d^y}\}$ contains a solution $x\in H_{d^y}\cap \M^{W_I}$ in its minimal face such that $\transpose{c} x \leq \transpose{c} x'$. Such a solution can be found in polynomial time using the ellipsoid method [@Khachiyan1980], see [@Grotschel1981] and [@Bland1981] for an explanation on how the optimal minimal face can be identified. Proposition 6.1 in [@VanDerHulst2025] provides a proof of how $x$ can be determined from the minimal face in polynomial time. Furthermore, note that $\transpose{c} x \leq \transpose{c} x' = \transpose{c'} y + \transpose{c} \delta$ holds.

Finally, let us show that $H'_{d'}$ is an $\MQ_I$-integral polyhedron for any $d'\in \Z^{\MQ'}$. First, note that we obtained $P(A',b',\ell',u')$ through the affine map $\kappa : \R^{W_U} \to \R^{\MQ}$ defined as $\kappa(x_{W_U}) \coloneqq 
    \transpose{\Pi_\MQ} \Lambda (x_{W_U} - \delta{W_U})$ that was applied to $P(A,b,\ell,u)$. Thus, the preimage of $H'_{d'}$ in $P(A,b,\ell,u)$ consists of those $x\in P(A,b,\ell,u)$ such that $(\transpose{\Pi_\MQ} \Lambda (x_{W_U} - \delta_{W_U}))_{\MQ'} = d'$. Then, for $d \coloneqq d' + (\transpose{\Pi_\MQ} \Lambda \delta_{W_U})_\MQ'$ the preimage of $H'_{d'}$ is exactly $H_d$. As we have $|\MQ| \leq |W_U|$, $\kappa$ is a surjective affine transformation and standard theory shows that the preimage of any face $F'$ of $H'_{d'}$ contains some minimal face $F$ of $H_d$ (see e.g. [@Ziegler01 Lemma 7.10]). Since $H_d$ is $\M^{W_I}$-integral, there exists some $x\in F\cap \M^{W_I}$. Then, note that $y \coloneqq \transpose{\Pi_\MQ} \Lambda (x_{W_U} - \delta_{W_U}) \in \M^{\MQ_I}$ holds, which we show in the proof of [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"}[\[thm_milp_folding_to_red\]](#thm_milp_folding_to_red){reference-type="ref" reference="thm_milp_folding_to_red"}. Then, since $y\in F'$ holds, it follows that any minimal face $F'$ of $H'_{d'}$ contains a $\MQ_I$-integral point, which shows that $H'_{d'}$ is $\MQ_I$-integral. ◻
:::

In [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref+label" reference="thm_fibers_symmetry_integral"}, we also show that $H'_{d}$ is integral. By [\[thm_affine_fiber_integral\]](#thm_affine_fiber_integral){reference-type="ref+label" reference="thm_affine_fiber_integral"}, this directly implies that $\mathrm{conv}(P(A',b',\ell',u') \cap \M^{\MQ'}) = \mathrm{conv}(P(A',b',\ell',u') \cap \M^{\MQ_I})$ holds for the reduced problem. Thus, any variables $Q\in \MQ_I \setminus \MQ'$ are implied integer in the reduced problem. One may hypothesize that the condition $\MQ'\subseteq \MQ_I$ is unnecessary and that the integrality of the fibers for $\MQ'$ implies the integrality for the fibers of $\MQ_I$. The example in [\[fig_nonintegral_affine_fiber_integral_fibers\]](#fig_nonintegral_affine_fiber_integral_fibers){reference-type="ref+Label" reference="fig_nonintegral_affine_fiber_integral_fibers"} shows that this is not the case, and that the condition $\MQ'\subseteq \MQ_I$ can indeed be helpful when the the fibers obtained by fixing the matrix with respect to $\MQ_I$ are not integral.\
Given [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref+label" reference="thm_fibers_symmetry_integral"}, we are motivated to investigate methods to determine when the affine fibers $H_d$ are integral. Although [\[thm_atu_ilp_integral\]](#thm_atu_ilp_integral){reference-type="ref+label" reference="thm_atu_ilp_integral"} is useful for integer programs, we cannot apply it directly to mixed-integer programs, as they do not satisfy its conditions. Thus, we generalize affine TU decompositions to mixed-integer linear programs to deal with this limitation.

## Affine TU decompositions for mixed-integer linear programs

We consider a mixed-integer linear program with variables $(x,y,z,\omega) \in \Z^{W^1} \times \Z^{W^2} \times \R^{W^3} \times \M^{W^4_I}$, where $W^4_I\subseteq W^4$ are the integer variables in $W^4$. We use $W_I = W^1 \cup W^2 \cup W^4_I$ to denote the integer variables and $W = W^1\cup W^2 \cup W^3 \cup W^4$ to denote all variables. The linear relaxation of the integer program is of the form: $$\begin{align*}
    P \coloneqq \{A x + B y + C z = b,~ D x + E y + F \omega = g,~ \ell \leq \transpose{\begin{bmatrix}
        x &
        y &
        z &
        \omega
    \end{bmatrix}} \leq u \},
\end{align*}$$ where $A \in \Z^{m_1\times W^1}$, $B\in \Z^{m_1\times W^2}$, $C\in \Z^{m_1\times W^3}$, $b\in \Z^{m_1}$, $D\in \Q^{m_2\times W^1}$, $E\in \Q^{m_2\times W^2}$, $F\in \Q^{m_2\times W^4}$ and $\ell \leq u$ hold, where $\ell$ and $u$ are rational vectors where we consider infinite entries to be integral. Any MILP can be brought into this form if we allow $m_1=0$ and $m_2=0$ to hold.

::: theorem
[]{#thm_atu_milp_integral label="thm_atu_milp_integral"} Suppose that for $k \leq |W^2|$, there exist matrices $S \in \Z^{m_1\times W^2}$, $U\in \Z^{m_1 \times k}$, $T\in \Z^{k \times W^2}$ and $R\in \Q^{m_2\times k}$ such that $B= S + U T$, $E=RT$ and $\begin{bmatrix}
    S & C\\
    T & \zerovec
\end{bmatrix}$ is totally unimodular and that $\ell,u \in \M^{W_I \cup W^3}$ holds. Then, for any $d = (d_{W^1}, d_T, d_{W^4_I}) \in \Z^{W^1} \times \Z^{k} \times \Z^{W^4_I}$, the affine fiber $H_d \coloneqq \{(x,y,z,\omega) \in P \mid x = d_{W^1},~ T y = d_T, ~\omega_{W^4_I} = d_{W^4_I} \}$ satisfies $$\begin{equation*}
        H_d = \mathrm{conv}(H_d \cap \M^{W_I}) = \mathrm{conv}(H_d \cap \M^{W_I \cup W^3}) \text{ and }
\end{equation*}$$ $$\begin{equation*}
        \mathrm{conv}(P\cap \M^{W_I}) = \mathrm{conv}(P\cap\M^{W_I\cup W^3})  = \mathrm{conv}(\{(x,y,z,\omega)\in P \mid x\in \Z^{W^1},~T y \in \Z^k,~ \omega \in \M^{W^4_I} \})
\end{equation*}$$ holds.
:::

::: proof
*Proof.* We consider the affine fiber $H_d$ for any fixed $d\in \Z^{W^1} \times \Z^{k} \times \Z^{W^4_I}$ and rewrite it by substituting $B = S + U T$ and $D = R T$.

$$\begin{align*}
      H_d \coloneqq& 
      \begin{aligned}[t]
          \{(x,y,z,\omega) \in \R^W \mid&~ A x + B y + C z = b,~ D x + E y + F \omega = g,~  x = d_{W^1},~ T y = d_T, \\&
       ~\omega_{W^4_I} = d_{W^4_I},~ \ell \leq \transpose{\begin{bmatrix}
        x &
        y &
        z &
        \omega
    \end{bmatrix}} \leq u \}
      \end{aligned}\\
      =& 
      \begin{aligned}[t]
          \{(x,y,z,\omega) \in \R^W \mid~&  x = d_{W^1},~ Sy + C z = b - A d_{W^1} - U d_{T},~ T y = d_T, \\
      &F \omega = g - D d_{W^1} - R d_T,~\omega_{W^4_I} = d_{W^4_I},~ \ell \leq \transpose{\begin{bmatrix}
        x &
        y &
        z &
        \omega
    \end{bmatrix}} \leq u \} 
      \end{aligned}\\
      = & \begin{aligned}[t]
      & \{x \in \R^{W^1} \mid x = d_{W^1}, ~\ell_{W^1} \leq x \leq u_{W^1} \} \times \\
      & \{\omega \in \R^{W^4} \mid F \omega = g - D d_{W^1} - R d_T, ~\omega_{W^4_I} = d_{W^4_I},~\ell_{W^4} \leq~ \omega \leq u_{W^4}\} \times \\
      &\{(y,z) \in \R^{W^2 \cup W^3} \mid Sy + C z = b - A d_{W^1} - U d_{T},~ T y = d_T, \ell_{W^2\cup W^3} \leq \transpose{\begin{bmatrix}
        y &
        z 
    \end{bmatrix}} \leq u_{W^2\cup W^3}\}
      \end{aligned}\\
    \coloneqq& H^{x}_d \times H^{\omega}_d \times H^{y,z}_d
\end{align*}$$

In the third step, we use that $H_d$ can be rewritten as the Cartesian product of the three polyhedra $H^x_d \subseteq \R^{W^1}$, $H^{y,z}_d \subseteq \R^{W^2\cup W^3}$ and $H^\omega_d \subseteq \R^{W^4}$. Then since $\begin{bmatrix}
        S & C \\
        T & \zerovec
    \end{bmatrix}$ is totally unimodular and $\begin{bmatrix}
        b - A d_{W^1} - U d_{T} \\
        d_T
    \end{bmatrix}$ is integral by integrality of $b$, $U$, $A$ and $d$, and $\ell_{W^2\cup W^3}$ and $u_{W^2\cup W^3}$ are integral, $H^{y,z}_d$ is an integral polyhedron by Hoffman and Kruskal's theorem [@HoffmanK56]. Thus, we have $H^{y,z}_d = \mathrm{conv}(H^{y,z}_d \cap \Z^{W^2 \cup W^3}) = \mathrm{conv}(H^{y,z}_d \cap (\Z^{W^2} \times \R^{W^3}))$, where the last equality follows since $H^{y,z}_d \cap \Z^{W^2 \cup W^3} \subseteq H^{y,z}_d \cap (\Z^{W^2} \times \R^{W^3}) \subseteq H^{y,z}_d$ holds. This implies that $H_d = \mathrm{conv}(H_d \cap \M^{W_I}) = \mathrm{conv}(H_d \cap \M^{W_I \cup W^3})$ holds.

Then, note that $C$ is totally unimodular since it is a submatrix of $\begin{bmatrix}
        S & C \\
        T & \zerovec
    \end{bmatrix}$. Since $A$, $B$ and $b$ are integral and the variable bounds $\ell_{W^3}$ and $u_{W^3}$ of $z$ are integral we have by that the equation $\mathrm{conv}(P\cap \M^{W_I}) = \mathrm{conv}(P \cap \M^{W_I \cup W^3})$ holds by [@VanDerHulst2025 Theorem 3]. Finally, using $\widehat{T} = \begin{bmatrix}
        I_{W^1} & \zerovec & \zerovec\\
        \zerovec & T & \zerovec \\
        \zerovec & \zerovec & I_{W^3_I}
    \end{bmatrix}$ as the matrix in [\[thm_affine_fiber_integral\]](#thm_affine_fiber_integral){reference-type="ref+label" reference="thm_affine_fiber_integral"} and the fact that $H_d = \mathrm{conv}(H_d \cap \M^{W_I})$ holds, we derive that $\mathrm{conv}(P \cap \M^{W_I})) = \mathrm{conv}(\{(x,y,z,\omega)\in P \mid x\in \Z^{W^1},~T y \in \Z^k,~ \omega \in \M^{W^4_I} \})$ holds. ◻
:::

There are a few key differences between [\[thm_atu_ilp_integral\]](#thm_atu_ilp_integral){reference-type="ref+label" reference="thm_atu_ilp_integral"} and [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref+label" reference="thm_atu_milp_integral"} that make the latter more convenient to use. First of all, we do not require integrality of all of the right-hand sides, and we only need to construct an affine TU decomposition of a block in the constraint matrix rather than the complete matrix. Additionally, the $E=RT$ condition in [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref+label" reference="thm_atu_milp_integral"} is new. This condition broadens the scope of the theorem, as otherwise, $D=\zerovec$ would have to hold to guarantee implied integrality in the affine fiber $H_d$ in the proof. Furthermore, during the detection we infer implied integrality for the continuous variables and have $\mathrm{conv}(P\cap \M^{W_I}) = \mathrm{conv}(P\cap \M^{W_I\cup W^3})$.\
[\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref+Label" reference="thm_atu_milp_integral"} can be used directly to show that the condition [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} in [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} holds. For integer variables $W_I\subseteq W$ and an equitable partition $(\MP,\MQ)$ such that either $Q\cap W_I = \emptyset$ or $Q\subseteq W_I$ holds, let $\MQ^2 = \{Q \in \MQ_I \mid |Q| > 1\}$ and let $W^2 = W_B \cup \bigcup_{Q\in \MQ^2} Q$. Then, if the conditions of [\[thm_atu_milp_integral\]](#thm_atu_milp_integral){reference-type="ref+label" reference="thm_atu_milp_integral"} hold for $T=(\transpose{\Pi_\MQ} \Lambda)_{\MQ',\star}$ for some subset $\MQ'\subseteq \MQ^2$, this directly shows condition [\[thm_milp_folding_condition\]](#thm_milp_folding_condition){reference-type="eqref" reference="thm_milp_folding_condition"} in [\[thm_milp_folding\]](#thm_milp_folding){reference-type="ref+label" reference="thm_milp_folding"} by using [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref+label" reference="thm_fibers_symmetry_integral"}, and [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref+label" reference="thm_fibers_symmetry_integral"} shows that we can recover integral solutions for the original model.

## Example: Generalized Assignment problem {#sec_example}

Consider the generalized assignment problem, where one computes an assignment of $J$ items with sizes $a_j, ~j\in J$ to $I$ knapsacks with capacity $C_i$ such that we maximize the sum of profits $\sum_{j\in J} c_j$ such that the capacities on the knapsacks are not exceeded. This can be modeled as an integer program using the binary variables $x_{ij} = \begin{cases}
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
\end{align}$$ Note that in [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"}, both the objective and the knapsack constraints are not dependent on $x$ anymore. In fact, by feasibility of $y^\star$, all constraints in [\[eq_mk_postsolve_knapsack\]](#eq_mk_postsolve_knapsack){reference-type="eqref" reference="eq_mk_postsolve_knapsack"} are feasible by feasibility of [\[eq_mk_reduced_knapsack\]](#eq_mk_reduced_knapsack){reference-type="eqref" reference="eq_mk_reduced_knapsack"}. Then, we observe that the remaining problem is given by an assignment problem on the $x$ variables. Since the constraints [\[eq_mk_postsolve_usedonce\]](#eq_mk_postsolve_usedonce){reference-type="eqref" reference="eq_mk_postsolve_usedonce"}, [\[eq_mk_postsolve_linking\]](#eq_mk_postsolve_linking){reference-type="eqref" reference="eq_mk_postsolve_linking"} form a totally unimodular matrix and the right-hand side given by $1$ and $y^\star$ is integral, the LP relaxation of [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"} is integral. Moreover, the solution $\bar{x}_{ij} = \frac{y^\star_{iK}}{|K|}$ for all $i\in I, K\in\mathcal{K}$ such that $j\in K$ is feasible for the LP relaxation of [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"} by [\[thm_lp_folding\]](#thm_lp_folding){reference-type="ref+label" reference="thm_lp_folding"}. Thus, an integral solution $x$ can be obtained by finding a vertex solution of the LP relaxation of [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"}.

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

It is not difficult to see that [\[eq_mk_unit\]](#eq_mk_unit){reference-type="eqref" reference="eq_mk_unit"} is still a perfect formulation. The constraint matrix defined by [\[eq_mk_unit_knapsack\]](#eq_mk_unit_knapsack){reference-type="eqref" reference="eq_mk_unit_knapsack"}--[\[eq_mk_unit_linking\]](#eq_mk_unit_linking){reference-type="eqref" reference="eq_mk_unit_linking"} is totally unimodular as it is the node-edge incidence matrix of a bipartite graph and the right-hand sides are integral. The two parts of the bipartition are given by constraints [\[eq_mk_unit_usedonce\]](#eq_mk_unit_usedonce){reference-type="eqref" reference="eq_mk_unit_usedonce"} and ([\[eq_mk_unit_knapsack\]](#eq_mk_unit_knapsack){reference-type="eqref" reference="eq_mk_unit_knapsack"} plus [\[eq_mk_unit_linking\]](#eq_mk_unit_linking){reference-type="eqref" reference="eq_mk_unit_linking"}), respectively. The fixings for $\mathcal{K}^1$ can be left out due to the fact that the variables in $J^1$ are implied integer. Let $P$ be the linear relaxation of [\[eq_mk_orig\]](#eq_mk_orig){reference-type="eqref" reference="eq_mk_orig"}. Then total unimodularity of [\[eq_mk_unit\]](#eq_mk_unit){reference-type="eqref" reference="eq_mk_unit"} shows by affine TU decomposition that $\mathrm{conv}(P\cap \Z^n) = \mathrm{conv}(\{x\in P \mid \sum_{j\in K} x_{ij} \in \Z, ~ \forall i\in I, ~\forall K \in \mathcal{K}\setminus \mathcal{K}^1\})$ holds. From this equality it also follows that $y_{iK}$ is implied integer for all $i\in I$ and all $K\in \mathcal{K}^1$ by the other variables in [\[eq_mk_reduced\]](#eq_mk_reduced){reference-type="eqref" reference="eq_mk_reduced"}. One way in which this additional power from implied integrality manifests is that in contrast to [\[eq_mk_postsolve_fixed\]](#eq_mk_postsolve_fixed){reference-type="eqref" reference="eq_mk_postsolve_fixed"}, solving [\[eq_mk_unit\]](#eq_mk_unit){reference-type="eqref" reference="eq_mk_unit"} may give a stronger solution than the provided $y^\star$ solution, if $y^\star$ is suboptimal and one of the items $j\in J^1$ can still be assigned to some knapsack. This correspond to having the proper subset $\MQ' \subset \MQ_I$ in the statement of [\[thm_fibers_symmetry_integral\]](#thm_fibers_symmetry_integral){reference-type="ref+label" reference="thm_fibers_symmetry_integral"}.

[^1]: Developers of both Gurobi and FICO Xpress mentioned this idea in personal communication.
