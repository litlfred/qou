---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-012-comparison-with-reflection-symmetries
section_title: "Comparison with reflection symmetries"
section_number: null
pages: 32-34
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.987
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Next, we will show that reflection reductions generalize reflection symmetries. First let us define reflection symmetries more formally. A *permutation matrix* $B$ is a square binary matrix with exactly one nonzero element with value $1$ in each row and column. It is well known that the inverse $B^{-1}$ is again a permutation matrix, which corresponds to the inverse permutation of the permutation given by $B$. A *signed permutation matrix* is a square $\{-1,0,1\}$-matrix with exactly one nonzero element in each row and column. Note that each signed permutation matrix $B$ can be decomposed as $\mathrm{diag}(s) C$ or $C \mathrm{diag}(s')$ where $C$ is the nonzero support of $B$, which is a permutation matrix, and $s$ and $s'$ are suitably chosen $\{-1,1\}$ vectors. In this section, we do not allow for arbitrary reordering of matrix columns and rows. In order to clarify the effect of the permutation symmetries, we denote each permutation explicitly using a permutation matrix.

::: definition
Consider a linear program $F(A,b,\ell,u,c)$, with $A\in \R^{V\times W}$. Let $\gamma \in \{-1,1\}^V$, $\lambda \in \{-1,1\}^W$ and define $\Gamma \coloneqq\mathrm{diag}(\gamma)$ and $\Lambda \coloneqq \mathrm{diag}(\lambda)$, and let $C\in \{0,1\}^{V\times V}$ and $D\in \{0,1\}^{W\times W}$ be permutation matrices. Then, $(\gamma,\lambda,C,D)$ is a *reflection symmetry of $F(A,b,\ell,u,c)$* if the following hold:

1.  $C\Gamma A \Lambda D = A$

2.  $C \Gamma b = b$

3.  $D^{-1} \lambda c = c$

4.  $-D^{-1}\mathrm{bs}(\ell,u,-\lambda)  = \ell$ and $D^{-1}\mathrm{bs}(u,\ell,\lambda)= u$

Furthermore, we say that $(C,D)$ is a *permutation symmetry* of $F(A,b,\ell,u,c)$ if $(\onevec,\onevec,C,D)$ is a reflection symmetry of $F(A,b,\ell,u,c)$.
:::

::: theorem
[]{#thm_reflection_symmetry_permutation_symmetry label="thm_reflection_symmetry_permutation_symmetry"} Every reflection symmetry of $F(A,b,\ell,u,c)$ induces a permutation symmetry of $F_S(A,b,\ell,u,c)$.
:::

::: proof
*Proof.* Let $(\gamma,\lambda,C,D)$ be a reflection symmetry of $F(A,b,\ell,u,c)$. Then, consider the split reformulation $F_S(A,b,\ell,u,c)$. We argued earlier that for the split permutation there exist permutation matrices $\widehat{C}_1$ and $\widehat{D}_1$ whose application to $F_S(A,b,\ell,u,c)$ yields the following linear program, see e.g. [\[lp_centered_extended_reordered\]](#lp_centered_extended_reordered){reference-type="eqref" reference="lp_centered_extended_reordered"}. Here, $\widehat{C}_1$ corresponds to the permutation that swaps $v^+$ and $v^-$ if $\gamma_v = -1$ holds, and $\widehat{D}_1$ corresponds to the permutation that swaps $w^+$ and $w^-$ if $\lambda_w = -1$ holds. $$\label{eq_reflection_symmetry_reordered}
    \begin{align}
        \min \transpose{(\Lambda c)} \widehat{x}^\lambda - \transpose{(\Lambda c)} \widehat{x}^{-\lambda}&\\
        \begin{bmatrix}
            \Gamma A \Lambda & - \Gamma A \Lambda\\
            -\Gamma A \Lambda & \Gamma A \Lambda
        \end{bmatrix} \begin{bmatrix}
            \widehat{x}^\lambda\\
            \widehat{x}^{-\lambda}
        \end{bmatrix} &= \begin{bmatrix}
            \Gamma b\\
            - \Gamma b
        \end{bmatrix}\\
        \zerovec \leq \begin{bmatrix}
            \widehat{x}^\lambda\\
            \widehat{x}^{-\lambda}
        \end{bmatrix} & \leq \begin{bmatrix}
            \mathrm{bs(\ell,u,\lambda)}\\
            \mathrm{bs(\ell,u,-\lambda)}
        \end{bmatrix} 
    \end{align}$$ Then, we define permutation matrices $\widehat{C}_2 \coloneqq \begin{bmatrix}
        C & \zerovec\\
        \zerovec & C
    \end{bmatrix}$ and $\widehat{D}_2 \coloneqq \begin{bmatrix}
        D & \zerovec\\
        \zerovec & D
    \end{bmatrix}$ and apply them to [\[eq_reflection_symmetry_reordered\]](#eq_reflection_symmetry_reordered){reference-type="eqref" reference="eq_reflection_symmetry_reordered"}. Doing so, we obtain the linear program: $$\label{eq_reflection_symmetry_permutation_symmetry}
    \begin{align}
        \min \transpose{(D^{-1} \Lambda c)} \widehat{x}^\lambda - \transpose{(D^{-1} \Lambda c)} \widehat{x}^{-\lambda}&\\
        \begin{bmatrix}
            C \Gamma A \Lambda D & - C\Gamma A \Lambda D\\
            -C\Gamma A \Lambda D & C\Gamma A \Lambda D
        \end{bmatrix} \begin{bmatrix}
            \widehat{x}^\lambda\\
            \widehat{x}^{-\lambda}
        \end{bmatrix} &= \begin{bmatrix}
            C\Gamma b\\
            - C\Gamma b
        \end{bmatrix}\\
        \zerovec \leq \begin{bmatrix}
            \widehat{x}^\lambda\\
            \widehat{x}^{-\lambda}
        \end{bmatrix} & \leq \begin{bmatrix}
            D^{-1} \mathrm{bs(\ell,u,\lambda)}\\
            D^{-1}\mathrm{bs(\ell,u,-\lambda)}
        \end{bmatrix} 
    \end{align}$$

Then, since $(\gamma,\lambda,C,D)$ is a reflection symmetry, it follows by substitution that $C \Gamma A \Lambda D = A$, $C \Gamma b = b$, $D^{-1} \mathrm{bs}(\ell,u,\lambda) = u$, $D^{-1} \mathrm{bs}(\ell,u,-\lambda) = - \ell$. Using these substitutions, [\[eq_reflection_symmetry_permutation_symmetry\]](#eq_reflection_symmetry_permutation_symmetry){reference-type="eqref" reference="eq_reflection_symmetry_permutation_symmetry"} is identical to $F_S(A,b,\ell,u,c,)$, without reordering the indices. Thus, the permutation matrices $\widehat{C} \coloneqq \widehat{C}_2 \widehat{C}_1$ and $\widehat{D} \coloneqq \widehat{D}_1 \widehat{D}_2$ form a permutation symmetry $(\widehat{C},\widehat{D})$ of $F_S(A,b,\ell,u,c)$. ◻
:::

By [\[thm_reflection_symmetry_permutation_symmetry\]](#thm_reflection_symmetry_permutation_symmetry){reference-type="ref" reference="thm_reflection_symmetry_permutation_symmetry"}, the reflection symmetries of a linear program are captured completely by the permutation symmetries of its split reformulation. In section 7.2 in [@Grohe2014], it is argued that for any linear program, performing the reduction from [\[thm_lp_folding\]](#thm_lp_folding){reference-type="ref" reference="thm_lp_folding"} using equitable partitions generalizes the projection to the fixed space of the symmetry group formed by the permutation symmetries. Although we do not show it formally, the permutation symmetries that we exhibit in the proof of [\[thm_reflection_symmetry_permutation_symmetry\]](#thm_reflection_symmetry_permutation_symmetry){reference-type="ref" reference="thm_reflection_symmetry_permutation_symmetry"} are bound-respecting, as they act similarly on the positive and negative variables of the split reformulation. As a consequence, the symmetry subgroup of the split reformulation corresponding to any permutation symmetries derived from reflection symmetries generates a bound-respecting equitable partition of the split reformulation. Thus, by computing bound-respecting equitable partitions of the split reformulation, our approach generalizes the projection to the fixed space of the symmetry group formed by reflections symmetries.\
As is also remarked in [@Grohe2014], equitable partitions may also occur even if there is no symmetry. Next, we show an example where this occurs for the split reformulation of a general class of matrices that does not necessarily contain symmetries.

::: example
Let $A\in \{0,1\}^{m\times n}$ be a matrix with two non-zero entries in each row. The matrix $A$ does not necessarily contain any symmetries, and we can consider the following linear program with no objective. $$\begin{aligned}
        A x &= \onevec\\
        \zerovec \leq x &\leq \onevec
    
\end{aligned}$$ Then, centering the linear program using $\delta_w \coloneqq \frac{1}{2}$ for all $w\in W$ yields the following linear program. $$\begin{aligned}
        A x &= \zerovec\\
        -\frac{1}{2} \leq x_w &\leq \frac{1}{2} & \forall w\in W
    
\end{aligned}$$ Its split reformulation is given by $$\begin{aligned}
        A x^+ - A x^- &= \zerovec\\
        -A x^+ + A x^- &= \zerovec\\
        0\leq x^+_w &\leq \frac{1}{2} & \forall w\in W\\
        0\leq x^-_w &\leq \frac{1}{2} & \forall w\in W
    
\end{aligned}$$ Then, since the objective and right-hand sides are all zero and the variable bounds are identical, the coarsest equitable partition of this linear program has a single bipolar variable part and a single bipolar row part, even though the original LP does not in general contain any symmetries.
:::
