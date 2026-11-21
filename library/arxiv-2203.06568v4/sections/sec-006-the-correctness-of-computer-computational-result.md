---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-006-the-correctness-of-computer-computational-result
section_title: "The correctness of computer computational results"
section_number: null
pages: 10-11
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.958
doc_brief: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
[]{#subsec:err label="subsec:err"} Since numerical methods will be used to approximate the optimal solution to an SDP, when we have a large number of variables, the accuracy of computer simulations may not be sufficient. In [@Gij05], Gijswijt used the weak duality of the optimization program to verify the SDP bounds. We describe his method here.

Consider an SDP of the following form: $$\begin{aligned}
    &\text{maximize} \quad \sum_{i=1}^{m}x_{i}c_{i}\\
    &\text{subject to} \quad \sum_{i=1}^{m}x_{i}F_{i} + F_{0}  \text{ is positive semidefinite}
\end{aligned}$$ with variables $x_{1}, \dots, x_{m}\in\mathbb{R}$, constants $c_{1}, \dots, c_{m}\in\mathbb{R}$ and symmetric matrices $F_{0}, \dots, F_{m}\in\mathbb{R}^{n\times n}$. Its dual problem is as follows:

$$\begin{aligned}
    \text{minimize} \quad & \text{tr}{F_{0} Y} \\
    \text{subject to} \quad &\text{tr}{F_{i}Y} + c_{i}=0  \text{ for } i=1,\dots, m\\
    & Y \text{ is positive semidefinite.}
\end{aligned}$$ Every feasible $Y$ in the dual problem gives an upper bound of the primal problem.

In a numerical computation, a dual solution $Y$ may not exactly satisfy the constraints, but $$\text{tr} F_{i} Y + c_{i} = \epsilon_{i}$$ for some small numbers $\epsilon_{1}, \dots, \epsilon_{m}$ due to the computer accuracy. Similarly, a primal solution may not be reliable. However, we can estimate the computation error as follows. Let $x_{1}^\star, \dots, x_{m}^\star$ be an optimal solution for the primal problem with objective value $P = \sum_{i = 1}^{m}x_{i}^\star c_{i}$. Let $X=\sum_{i=1}^{m}x_{i}^\star F_{i} + F_{0}$, which is positive semidefinite since $x_i^\star$ are feasible. Then $$\begin{aligned}
    \text{tr} F_{0} Y  &= \text{tr}  \left\{\left(-\sum_{i = 1}^{m} x_{i}^\star F_{i} +X\right) Y \right\}\\
    & \geq \text{tr}  \left\{-\sum_{i = 1}^{m} x_{i}^\star F_{i} Y \right\}\\
    &= -\sum_{i=1}^{m} x_{i}^\star \text{tr}  F_{i} Y  \\
    &= -\sum_{i = 1}^{m} x_{i}^\star(-c_{i}+ \epsilon_{i})\\
    &= P - \sum_{i = 1}^{m} x_{i}^\star\epsilon_{i}.
\end{aligned}$$

In our SDP ([\[eq:main_SDP\]](#eq:main_SDP){reference-type="ref" reference="eq:main_SDP"}), the variables $x_{i,j,i',j'}^{t,t'}$ are negative and no larger than one by ([\[eq:split_cons\]](#eq:split_cons){reference-type="ref" reference="eq:split_cons"}). For our purpose, we can have an upper bound on the optimal value $P$ that $$P \leq  \text{tr} F_{0} Y + \sum_{i = 1}^{m}x_{i}^{*}\epsilon_{i} \leq  \text{tr} F_{0} Y + \sum_{i=1}^{m}{\rm max}\{0,\epsilon_{i}\}.$$ Therefore, we may use the dual optimal value and error terms to estimate an upper bound in our computational results.
