---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-008-split-reformulations-of-linear-programs
section_title: "Split reformulations of linear programs"
section_number: null
pages: 14-16
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 1.0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
In both papers [@Hojny2025-si] and [@Christophel2014], the authors reduce the problem of finding reflection symmetries to finding permutation symmetries by adding both the original and the complemented variables to the auxiliary graph used for symmetry detection. For linear programs, a similar effect can be achieved by splitting each variable $x$ as $x=x^+ - x^-$, where $x^+$ represents the positive domain of $x$ and $x^-$ corresponds to the negative domain of $x$. We introduce the notion of a *split reformulation* to achieve such a reformulation.

::: definition
[]{#def_split_reform label="def_split_reform"} Let $F(A,b,\ell,u,c)$ be any linear program with $A\in \R^{V\times W}$, $b\in \R^V$, $c\in \R^W$ and vectors $\ell,u$ with $\ell_w\in \R\cup \{-\infty\}$ and $u \in \R\cup \{\infty\}$ for all $w\in W$. If $\ell \leq 0$ and $u \geq 0$ hold, we define the *split reformulation* of $F(A,b,\ell,u,c)$ to be the following linear program with variables $x^+\in \R^W$ and $x^-\in \R^W$: $$\begin{split}
            \min\,  \transpose{c} x^+ - \transpose{c} x^-\\
            A x^+ - A x^- &= b\\
            -A x^+ + A x^- &= -b\\
            0\leq x^+ &\leq u \\
            0 \leq x^- &\leq -\ell
        \end{split}
        \tag{$F_S(A,b,\ell,u,c))$}$$ We use $F_S(A,b,\ell,u,c)$ to denote the linear program that is the split reformulation of $F(A,b,\ell,u,c)$, and we use $P_S(A,b,\ell,u)$ to denote its feasible region. Furthermore, we use $\widehat{M} = \begin{bmatrix}
        A & -A\\
        -A & A
    \end{bmatrix}\in \R^{(\widehat{V}^+ \cup \widehat{V}^-) \times (\widehat{W}^+ \cup \widehat{W}^-)}$, to denote the constraint matrix and $\widehat{V} \coloneqq \widehat{V}^+ \cup \widehat{V}^-$ and $\widehat{W} \coloneqq \widehat{W}^+ \cup \widehat{W}^-$ to denote the row and column index sets.
:::

Note that the split reformulation $F_S(A,b,\ell,u)$ includes the constraints $-Ax^+ + A x^- = -b$, indexed by $\widehat{V}_2$, which are redundant as they are directly implied by negating $Ax^+ - Ax^- = b$. Thus, they may be left out without changing the feasible region. Previous works do not consider the duplication of constraints. However, we will see that these redundant equations may be useful for the derivation of coarse equitable partitions. In particular, they may help to establish equitable partitions that arise if a subset of the rows are multiplied by $-1$.\
In [\[thm_splitting_equivalent\]](#thm_splitting_equivalent){reference-type="ref" reference="thm_splitting_equivalent"}, we show that the split reformulation of any linear program is equivalent to its original linear program.

::: lemma
[]{#thm_splitting_equivalent label="thm_splitting_equivalent"} Let $A\in \R^{V\times W}$, $b\in \R^V$, $c\in \R^W$ and vectors $\ell,u,$ with $l_w \in \R_{\leq0} \cup \{-\infty\}$ and $u_w\in \R_{\geq 0} \cup \{\infty\}$ for all $w\in W$. Then, the following hold:

1.  []{#thm_splitting_equivalent_to_red label="thm_splitting_equivalent_to_red"} If $x\in P(A,b,\ell,u)$, then for $x^+\coloneqq \max(x,\zerovec)$ and $x^-\coloneqq \max(-x,\zerovec)$ it holds that $(x^+,x^-) \in P_S(A,b,\ell,u)$ and $\transpose{c} x = \transpose{c}x^+ - \transpose{c} x^-$.

2.  []{#thm_splitting_equivalent_from_red label="thm_splitting_equivalent_from_red"} If $(x^+,x^-)\in P_S(A,b,\ell,u)$ then for $x\coloneqq x^+ - x^-$ it holds that $x\in P(A,b,\ell,u)$ and $\transpose{c} x = \transpose{c}x^+ - \transpose{c} x^-$.
:::

::: proof
*Proof.* To prove [\[thm_splitting_equivalent_to_red\]](#thm_splitting_equivalent_to_red){reference-type="ref" reference="thm_splitting_equivalent_to_red"}, let $x\in P(A,b,\ell,u)$ be given and consider $x^+=\max(x,\zerovec)$ and $x^-=\max(-x,\zerovec)$. Then, we have: $$Ax^+ - Ax^- = A(x^+-x^-) = A(\max(x,\zerovec)- \max(-x,\zerovec)) = A x \stackrel{\textup{(a)}}{=} b,$$ where [(a)]{.upright} follows since $x\in P(A,b,\ell,u)$ holds. It follows directly that also $-Ax^+ + Ax^- = -(Ax^+ - Ax^-) = -b$ holds. Furthermore, note that $x^+ \geq 0$ and $x^-\geq 0$ hold by definition of the $\max$ operator. The upper bounds $x^+\leq u$ and $x^- \leq -\ell$ follow from $x\leq u$ and $-x \leq - \ell$ which are satisfied since $x\in P(A,b,\ell,u)$ holds. Then, since $\ell \leq 0$ and $u\geq 0$, it follows that $(x^+,x^-)$ is feasible for $P_S(A,b,\ell,u)$. Finally, note that $\transpose{c} x = \transpose{c} (\max(x,\zerovec)- \max(-x,\zerovec)) = \transpose{c} x^+ - \transpose{c} x^-$ shows that the objectives are equal.

To prove [\[thm_splitting_equivalent_from_red\]](#thm_splitting_equivalent_from_red){reference-type="ref" reference="thm_splitting_equivalent_from_red"}, let $(x^+,x^-)\in P_S(A,b,\ell,u)$ be given and consider $x\coloneqq x^+-x^-$. Then, $Ax = A x^+ - Ax^- = b$ holds since $(x^+,x^-) \in P_S(A,b,\ell,u)$. Since $x^+\geq 0$ and $x^-\geq 0$ hold in $P_S(A,b,\ell,u)$, we also have that $x = x^+ - x^- \leq u + \zerovec = u$ and $x = x^+ - x^- \geq \zerovec - -\ell = \ell$, which shows that $\ell \leq x \leq u$ holds, and thus it follows that $x\in P(A,b,\ell,u)$. Finally, we have by definition of $x$ that $\transpose{c} x = \transpose{c} (x^+ - x^-) = \transpose{c} x^+ - \transpose{c} x^-$. ◻
:::

First of all, we note that $\ell \leq 0$ and $u \geq 0$ are necessary conditions to guarantee that the split reformulation exists in the proof of [\[thm_splitting_equivalent\]](#thm_splitting_equivalent){reference-type="ref" reference="thm_splitting_equivalent"}. For any linear programs with $\ell_w \leq u_w$ for variable $x_w$, one can achieve this by transforming $x_w$ into $x'_w$ using $x_w' = x_w + \delta_w$ for any $\delta_w$ that satisfies $\ell_w \leq \delta_w \leq u_w$. If $\ell_w \leq u_w$ does not hold, then the linear program is clearly infeasible.\
For the detection of reflection symmetries, previous approaches detect reflection symmetries by detecting permutation symmetries on a mixed-integer linear program obtained from a split reformulation. Thus, a logical next step is to consider the application of DRCR to a split reformulation $F_S(A,b,\ell,u,c)$ for any linear program $F(A,b,\ell,u,c)$ with $\ell \leq \zerovec$ and $u\geq \zerovec$. To do so, we first need to understand some of the special properties of equitable partitions of split reformulations.
