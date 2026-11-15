---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-007-centering-the-linear-program
section_title: "Centering the linear program"
section_number: null
pages: 13-14
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 1.0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Initially, we consider the linear program $F(A,b,\ell,u,c)$. In order to detect reflection symmetries, we would like to center each variable at the center of its domain. This can be achieved using an affine transformation that offsets the variables.

::: proposition
[]{#thm_affine_equivalent label="thm_affine_equivalent"} For any scalar $\delta \in \R$, $x \in P(A,b,\ell,u)$ holds if and only if $x'\coloneqq x - \delta \in P(A,b- A \delta,\ell - \delta,u- \delta)$ holds. Moreover, $\transpose{c} x' = \transpose{c} x - \transpose{c} \delta$ holds.
:::

::: proof
*Proof.* It is sufficient to observe that $A x = b \iff A x - A \delta = b - A\delta \iff Ax' = b - A \delta$ and that $\ell \leq x \leq u \iff \ell - \delta \leq x - \delta \leq u -\delta \iff \ell - \delta \leq x' \leq u -\delta$. Moreover, $\transpose{c} x' = \transpose{c} x - \transpose{c} \delta$ follows by definition of $x'$. ◻
:::

The main idea that we use [\[thm_affine_equivalent\]](#thm_affine_equivalent){reference-type="ref" reference="thm_affine_equivalent"} for in the context of equitable partitions is that that $F(A,b-A \delta, \ell-\delta,u-\delta,c)$ may admit a coarser equitable partition than $F(A,b,\ell,u,c)$. We note that there are infinitely many choices for $\delta$ to do so, so it is not clear how $\delta$ may be chosen. Frequently, we use [\[thm_affine_equivalent\]](#thm_affine_equivalent){reference-type="ref" reference="thm_affine_equivalent"} to center the variables at their domains by using $\delta_w \coloneqq \frac{u_w + \ell_w}{2}$. For variables with infinite lower or upper bounds, such a centered $\delta_w$ value is not well-defined. Later on, we will clarify how one should choose $\delta_w$ in such cases. For now, we analyze the equitable partitions of $F(A,b-A \delta, \ell-\delta,u-\delta,c)$ for any finite $\delta \in \R$.\
Furthermore, we note that $\delta$ corresponds to an offset of the primal variables. It is also possible to expand the results in this work by using an offset for the dual variables, which corresponds to adding weighted multiples of the rows to the objective. One could hope that doing so may help to construct additional variables that have identical objective value, which would lead to potentially coarser equitable partitions. In order to simplify the presentation, we do not consider this extension here.
