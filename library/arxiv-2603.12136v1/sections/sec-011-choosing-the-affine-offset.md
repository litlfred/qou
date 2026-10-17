---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-011-choosing-the-affine-offset
section_title: "Choosing the affine offset"
section_number: null
pages: 28-32
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.996
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
[]{#sec_choosing_affine_offset label="sec_choosing_affine_offset"} In order to apply reflection reductions to arbitrary linear programs, we had to introduce the affine offset $\delta$ to ensure that the lower bounds were nonpositive and the upper bounds were nonnegative. Given $\delta$, the linear transformation that is represented by the $\pm1$ scaling vectors $\lambda$ and $\gamma$ follows automatically from the symmetric equitable partition of the split reformulation. In this section, we argue how to choose $\delta$. In previous work, Hojny [@Hojny2025-si] chooses $\delta$ to be the center of the variable domains such that $\delta_w \coloneqq \frac{\ell_w + u_w}{2}$. One issue is that such a center is not well-defined for variables with infinite lower or upper bounds. Similarly to Hojny, we use the offset $\delta^\mathcal{C}$ defined for all $w\in W$ as $$\delta^\mathcal{C}_w \coloneqq \begin{cases}
        \frac{\ell_w + u_w}2 &\text{if $\ell_w$ and $u_w$ are finite.}\\
        0 &\text{if $\ell_w = -\infty$ and $u_w = \infty$}\\
        \ell_w &\text{if $\ell_w$ is finite and $u_w = \infty$.}\\
        u_w &\text{if $\ell_w = -\infty$ and $u_w$ is finite.}
    \end{cases}$$

Next, let us argue why $\delta^\mathcal{C}$ is a good choice for the offset. First of all, we note that for the most common case of variables $w$ with $\ell_w$ and $u_w$ finite, they can only belong to bipolar parts if $-(\ell_w - \delta_w) = u_w - \delta_w$ holds, which holds exactly if $\delta_w = \frac{\ell_w + u_w}2$ holds. Thus, variables with finite bounds can only be detected as bipolar variables if $\delta_w = \delta^\mathcal{C}_w = \frac{\ell_w + u_w}2$ holds. Note that in the case exactly one of $\ell_w$ and $u_w$ is finite, we can never detect bipolarity. If $\ell_w = -\infty$ and $u_w = \infty$ hold, then the choice of $\delta_w$ does not affect the transformed variable bounds and bipolarity may be detected in any case.\
Second, recall that we assumed that the symmetric equitable partitions must be bound-respecting. For the linear program $F(A,b- A \delta,\ell- \delta,u- \delta,c)$, this condition can be stated as follows. The partition $(\widehat{\MP},\widehat{\MQ})$ of the split reformulation must satisfy for all $Q\in \widehat{\MQ}$ and any $w_1^s,w_2^s\in Q$ that $\ell_{w_1} - \delta_{w_1} = \ell_{w_2} - \delta_{w_2}$ and $u_{w_1} - \delta_{w_1} = u_{w_2}- \delta_{w_2}$ hold if $s_1 = s_2$ holds, and if $s_1 \neq s_2$ holds that $\ell_{w_1} - \delta_{w_1} = -u_{w_2} + \delta_{w_2}$ and $u_{w_1} - \delta_{w_1} = - \ell_{w_2} + \delta_{w_2}$ hold. Next, we show that for $\delta = \delta^\mathcal{C}$ only the *size* $u_w - \ell_w$ of the domain of $w$ matters. Assume for all $Q\in \MQ$ and any $w_1^s,w_2^s \in Q$ that $u_{w_1} - \ell_{w_1} = u_{w_2} - \ell_{w_2}$ holds. For the $s_1 = s_2$ case, we can use this assumption to show that: $$\ell_{w_1} - \delta^\mathcal{C}_{w_1} = \ell_{w_1} - \frac{\ell_{w_1} + u_{w_1}}{2} = 
    -\frac{u_{w_1} - \ell_{w_1}}{2} = \frac{u_{w_2} - \ell_{w_2}}{2} = \ell_{w_2} - \frac{\ell_{w_2} + u_{w_2}}{2} = \ell_{w_2} - \delta^\mathcal{C}_{w_2}$$ and similarly that $$u_{w_1} - \delta^\mathcal{C}_{w_1} = u_{w_1} - \frac{\ell_{w_1} + u_{w_1}}{2} = 
    \frac{u_{w_1} - \ell_{w_1}}{2} = \frac{u_{w_2} - \ell_{w_2}}{2} = u_{w_2} - \frac{\ell_{w_2} + u_{w_2}}{2} = u_{w_2} - \delta^\mathcal{C}_{w_2}.$$ Also for the $s_1 \neq s_2$ case, we can use the assumption to show: $$\ell_{w_1} - \delta^\mathcal{C}_{w_1} =
-\frac{u_{w_1} - \ell_{w_1}}{2} = -\frac{u_{w_2} - \ell_{w_2}}{2} = - u_{w_2} + \frac{u_{w_2} + \ell_{w_2}}2 = -u_{w_2} + \delta^\mathcal{C}_{w_2}$$ and similarly: $$u_{w_1} - \delta^\mathcal{C}_{w_1} =
\frac{u_{w_1} - \ell_{w_1}}{2} = \frac{u_{w_2} - \ell_{w_2}}{2} = - \ell_{w_2} + \frac{u_{w_2} + \ell_{w_2}}2 = -\ell_{w_2} + \delta^\mathcal{C}_{w_2}.$$ Thus, the simpler condition $u_{w_1} - \ell_{w_1} = u_{w_2} - \ell_{w_2}$ is sufficient in the case where $\delta = \delta^{\mathcal{C}}$ holds to show that a partition is bound-respecting for finite $u_{w_1}$ and $\ell_{w_1}$. For infinite values, the bound-respecting condition is still necessary. In particular, the above bound argumentation does not prevent that free variables may be aggregated with variables with one infinite bound, as in both cases the domain size is infinite. Thus, the domain-respecting assumption is still necessary for linear programs with infinite variable bounds.\
Although $\delta^{\mathcal{C}}$ is a natural choice, it does have a few problematic aspects. First of all, the product $A \delta^\mathcal{C}$ that appears in the right-hand side $b- A \delta^\mathcal{C}$ of the linear program after applying the transformation $x = x' + \delta$ can be problematic. If $A$ contains large nonzero-entries and/or $\delta^\mathcal{C}$ is large due to variables with large domains, then the product $A\delta^\mathcal{C}$ may result in large numerical values in the right-hand $b- A \delta^\mathcal{C}$ in the linear program obtained from the reflection reduction. This is undesirable, as it can lead to numerical problems that slow down the linear programming solver. Thus, we generally prefer offsets $\delta$ that are sparse and/or have small norms.\
A second issue appears when we apply reflection reductions in the context of mixed-integer linear programs: the offset $\delta^{\mathcal{C}}$ is not necessarily integer. As a result, an integrality constraint $x_w \in \Z$ may be transformed into the form $x'_{w} + \delta^\mathcal{C}_w \in \Z$, which cannot be handled directly by MILP solvers if $\delta^\mathcal{C}_w$ is not integer. Next, we formulate a result that helps to derive a family of reflection reductions for different $\delta$-values by detecting one for a single value of $\delta$. This result will be helpful to construct an offset $\delta$ that does not cause numerical issues and that also works well for mixed-integer linear programs.\

::: theorem
[]{#thm_delta_equivalent label="thm_delta_equivalent"} Let $(\widehat{\MP},\widehat{\MQ})$ be a symmetric equitable partition of $F_S(A,b - A \delta, \ell - \delta, u - \delta, c)$ and let $\gamma$, $\lambda$, $\MP_U$ and $\MQ_U$ be generated by $(\widehat{\MP},\widehat{\MQ})$. Let $\nu \in \R^{W_U}$ be a vector that is equitably partitioned by $\MQ_U$ and define $\delta' \coloneqq (\delta_{W_U} + \Lambda \nu,\delta_{W_B})$ such that $\ell \leq \delta' \leq u$. Then $(\widehat{\MP},\widehat{\MQ})$ is a symmetric equitable partition of $F_S(A,b- A \delta', \ell - \delta', u - \delta', c)$.
:::

::: proof
*Proof.* Clearly, $(\widehat{\MP},\widehat{\MQ})$ is also a symmetric partition of $F_S(A,b- A \delta', \ell - \delta', u - \delta', c)$. Since the objective and constraint matrix are unchanged compared to $F_S(A,b- A \delta, \ell - \delta, u - \delta, c)$ and remain so by the split reformulation, it is sufficient to show that $\widehat{\MP}$ is a symmetric equitable partition of the right-hand side and that $\widehat{\MQ}$ is an equitable partition of the variable upper bounds of $F_S(A,b- A \delta', \ell - \delta', u - \delta', c)$. Note that by definition of the split reformulation, all variables have lower bound zero, so we only consider the upper bounds.\
Let us state the reordered linear program of $F_S(A,b - A \delta', \ell-\delta',u-\delta',c)$, which is similar to the form [\[lp_centered_extended_reordered\]](#lp_centered_extended_reordered){reference-type="eqref" reference="lp_centered_extended_reordered"}.

$$\label{lp_centered_extended_reordered_delta}
\begin{align}
    \min\, \transpose{c_{W_U}} \Lambda \widehat{x}_{\widehat{W}^\lambda_U} - \transpose{c_{W_U}} \Lambda \widehat{x}_{\widehat{W}^{-\lambda}_U} & \\
\begin{bmatrix}
    \Gamma A_{V_U,W_U} \Lambda & -\Gamma A_{V_U,W_U} \Lambda & \widehat{M}^1
    \\
    -\Gamma A_{V_U,W_U} \Lambda & \Gamma A_{V_U,W_U} \Lambda & -\widehat{M}^1
    \\
    \widehat{M}^2 & -\widehat{M}^2 & \widehat{M}^3 \\
\end{bmatrix}
\begin{bmatrix}
    \widehat{x}_{\widehat{W}^\lambda_U}\\
    \widehat{x}_{\widehat{W}^{-\lambda}_U}\\
    \widehat{x}_{\widehat{W}_B}
\end{bmatrix} &= \begin{bmatrix}
    \Gamma (b - A \delta')_{V_U}\\
    -\Gamma (b- A \delta')_{V_U}\\
    \widehat{b}_{\widehat{V}_B}
\end{bmatrix}
\label{lp_centered_extended_reordered_delta_eqs}
\\
\zerovec \leq \widehat{x}_{\widehat{W}^\lambda_U} &\leq \mathrm{bs}(\ell-\delta',u-\delta',\lambda)_{W_U} \\
\zerovec \leq \widehat{x}_{\widehat{W}^{-\lambda}_U} &\leq \mathrm{bs}(\ell-\delta',u-\delta',-\lambda)_{W_U} \\
\zerovec \leq \widehat{x}_{\widehat{W}_B} &\leq \begin{bmatrix}
    -(\ell-\delta')_{W_B}\\
    (u-\delta')_{W_B}
\end{bmatrix} 
\end{align}$$ We use $\widehat{b}_{\widehat{V}_B} \coloneqq \begin{bmatrix}
    (b - A \delta')_{V_B}\\
    -(b - A \delta')_{V_B}\\
\end{bmatrix}$ to denote the variable bounds of the bipolar rows. For the variables $\widehat{W}^{\lambda}_U$, we can compute their upper bounds using: $$\begin{aligned}
        \mathrm{bs}(\ell-\delta',u-\delta',\lambda)_w &= \begin{cases}
            u_w - \delta'_w&\text{if }\lambda_w=1\\
            -\ell_w + \delta'_w&\text{if }\lambda_w=-1
        \end{cases} = \begin{cases}
            u_w - \delta_w - \lambda_w \nu_w &\text{if }\lambda_w=1\\
            -\ell_w + \delta_w + \lambda_w \nu_w &\text{if }\lambda_w=-1
        \end{cases}\\ &= - \nu_w + \begin{cases}
            u_w - \delta_w&\text{if }\lambda_w=1\\
            -\ell_w + \delta_w&\text{if }\lambda_w=-1
        \end{cases}= - \nu_w +  \mathrm{bs}(\ell-\delta,u-\delta,\lambda)_w.
    
\end{aligned}$$ Thus, we have that $\mathrm{bs}(\ell-\delta',u-\delta',\lambda) = -\nu + \mathrm{bs}(\ell-\delta,u-\delta,\lambda)$ holds. Then, since $\widehat{\MQ}^\lambda_U$ is exactly the partition given by $\MQ_U$ and $\nu$ is $\MQ_U$ equitable, it follows that it follows that $\widehat{\MQ}^\lambda_U$ is an equitable partition of $\mathrm{bs}(\ell-\delta',u-\delta',\lambda)$ since it is the sum of the equitably partitioned vectors $-\nu$ and $\mathrm{bs}(\ell-\delta,u-\delta,\lambda)$. For $\widehat{W}^{-\lambda}_U$ a similar argument shows that $\mathrm{bs}(\ell-\delta',u-\delta', -\lambda) = \nu + \mathrm{bs}(\ell-\delta,u-\delta,-\lambda)$ holds, which implies that the upper bounds $\mathrm{bs}(\ell-\delta',u-\delta', -\lambda)$ are equitably partitioned by $\widehat{\MQ}^\lambda_U$. For the bipolar variables $\delta'_{W_B} = \delta_{W_B}$ holds so the variable bounds are unchanged, which directly implies that $\widehat{\MQ}_B$ is an equitable partition of the variable bounds of $\widehat{W}_B$. Combining these statements, it follows that $\widehat{\MQ}$ is an equitable partition of the variable upper bounds of $F_S(A,b-A\delta',\ell-\delta',u-\delta',c)$.\
Next, let us show that the right-hand sides of [\[lp_centered_extended_reordered_delta_eqs\]](#lp_centered_extended_reordered_delta_eqs){reference-type="eqref" reference="lp_centered_extended_reordered_delta_eqs"} are equitably partitioned by $\widehat{\MP}$. Note that for any $v\in V$ that $$(b- A \delta')_v = b_v - (A (\delta + (\Lambda\nu,\zerovec_{W_B})))_v =(b- A\delta)_v - (A_{\star,W_U} \Lambda \nu)_v$$ holds. Thus, it follows that $$\Gamma(b- A \delta')_{V_U} = \Gamma(b- A \delta - A_{\star,W_U} \Lambda \nu )_{V_U} = \Gamma(b-A \delta)_{V_U} - \Gamma A_{V_U,W_U} \Lambda \nu.$$ The term $\Gamma(b-A \delta)_{V_U}$ is equitably partitioned by the subpartition $\widehat{\MP}^\gamma_U$ of $\widehat{\MP}$. Then, we claim that $\Gamma A_{V_U,W_U} \Lambda \nu$ is also a $\widehat{\MP}^\gamma_U$-equitable vector.

First, note that $(\widehat{\MP}^\gamma_U,\MQ_U)$ is an equitable partition of $\Gamma A_{V_U,W_U} \Lambda$, which follows from the fact that $(\widehat{\MP},\widehat{\MQ})$ is an equitable partition of $\widehat{M}$ in the linear program $F_S(A,b- A \delta, \ell- \delta, u - \delta,c)$, where $(\widehat{\MP}^\gamma_U,\widehat{\MQ}^\lambda_U) = (\widehat{\MP}^\gamma_U,\MQ_U)$ induces the subpartition.

Secondly, since $\nu$ is $\MQ_U$-equitable, we claim that multiplication of any $(\widehat{\MP}^\gamma_U,\MQ_U)$-matrix with a $\MQ_U$-equitable vector produces a $\widehat{\MP}^\gamma_U$-equitable vector. In particular note that for all $P\in \widehat{\MP}^\gamma_U$ and any $v\in P$, we have: $$\begin{aligned}
        (\Gamma A_{V_U,W_U} \Lambda \nu)_v &= \sum_{w\in W} (\Gamma A_{V_U,W_U} \Lambda)_{v,w} \nu_{w} = \sum_{Q\in \MQ_U} \sum_{w\in Q} (\Gamma A_{V_U,W_U} \Lambda)_{v,w} \nu_{w} \\ &\stackrel{\textup{(a)}}{=} \sum_{Q\in \MQ} \alpha_{Q} \sum_{w\in Q} (\Gamma A_{V_U,W_U} \Lambda)_{v,w} \stackrel{\textup{(b)}} = \sum_{Q\in \MQ} \alpha_{Q} \beta_{P,Q}.
    
\end{aligned}$$ Here, [(a)]{.upright} follows since $\MQ_U$ is an equitable partition of $\nu$, which implies that $\nu_w = \alpha_{Q}$ for $Q\in \MQ_U$ such that $w\in Q$. Then, [(b)]{.upright} follows since $(\widehat{\MP}^\gamma_U,\MQ_U)$ is an equitable partition of $\Gamma A \Lambda$, which implies that condition [\[eq_folding_row_sums\]](#eq_folding_row_sums){reference-type="eqref" reference="eq_folding_row_sums"} holds. Thus, the row sums of $\Gamma A \Lambda$ are identical for all $v\in P$, which we express using $\beta_{P,Q}$. Since the final expression is independent of $v$ for every part $P\in \widehat{\MP}^\gamma_U$, this shows that $\Gamma A \Lambda \nu$ is $\widehat{\MP}^\gamma_U$-equitable. Then, since the sum of two equitable vectors is equitable, it follows that $\widehat{\MP}^\gamma_U$ is an equitable partition of $\Gamma ( b- A \delta')_{V_U} = \Gamma(b- A \delta)_{V_U} - \Gamma A_{V_U,W_U} \Lambda \nu$. A very similar argument shows that $\widehat{\MP}^{-\gamma}_U$ is an equitable partition of $-\Gamma ( b- A \delta')_{V_U} = -\Gamma(b- A \delta)_{V_U} + \Gamma A_{V_U,W_U} \Lambda \nu$.

For the bipolar rows, we consider $(b-A \delta')_v$ for $v\in V_B$ such that $\{v^+,v^-\} \subseteq P$ for $P \in \widehat{\MP}_B$. Then, we have that: $$\begin{aligned}
        (b- A \delta')_{v} &= (b - A \delta)_v - (A_{\star,W_U} \Gamma \nu)_v \stackrel{\textup{(c)}}= - (A_{\star,W_U} \Gamma \nu)_v = - \sum_{w\in W_U} A_{v,w}\lambda_w \nu_w \\
        &\stackrel{\textup{(d)}}= - \sum_{Q\in \MQ_U} \alpha_Q \sum_{w\in Q} A_{v,w} \lambda_w \stackrel{\textup{(e)}}= - \sum_{Q\in \MQ_U} \alpha_Q \sum_{w^\lambda \in Q^\lambda} \widehat{M}_{v^+,w^\lambda} \stackrel{\textup{(f)}}= 0 
    
\end{aligned}$$ Here, [(c)]{.upright} follows since $(\widehat{\MP},\widehat{\MQ})$ being a symmetric equitable partition for $F_S(A,b- A \delta, \ell-\delta, u - \delta,c)$ implies that $(b-A \delta)_v = 0$ for all $v\in V_B$. The relation in [(d)]{.upright} follows since $\nu$ is an $\MQ_U$-equitable vector. In [(e)]{.upright}, we use that $(A \Lambda)_{v,Q} = \widehat{M}_{v^+,Q^\lambda}$ holds by construction of $\widehat{M}$. In [(f)]{.upright}, we use that $\sum_{w^\lambda \in Q^\lambda} \widehat{M}_{v^+,w^\lambda} = 0$ holds by [\[thm_bipolar_symmetric_equitable_sum\]](#thm_bipolar_symmetric_equitable_sum){reference-type="ref" reference="thm_bipolar_symmetric_equitable_sum"}, using that $v$ is bipolar and that the given partition is equitable. Then, it follows that $\widehat{b}_{\widehat{V}_B} \coloneqq \begin{bmatrix}
    (b - A \delta')_{V_B}\\
    -(b - A \delta')_{V_B}\\
\end{bmatrix} = \begin{bmatrix}
    \zerovec_{V_B}\\
    \zerovec_{V_B}
\end{bmatrix}$, which shows that $\widehat{\MP_B}$ is an equitable partition of $\widehat{b}$. Moreover, it implies that the rows $\widehat{V}_B$ remain bipolar, which implies that the symmetry of $(\widehat{\MP},\widehat{\MQ})$ is also preserved for $F_S(A,b- A \delta', \ell - \delta',u- \delta')$. Then, we have that $\widehat{\MP}$ is an equitable partition of the right-hand side of $F_S(A,b- A \delta', \ell- \delta',u-\delta',c)$. Using the earlier derived equitability for the variable bounds, we conclude that $(\widehat{\MP},\widehat{\MQ})$ is a symmetric equitable partition of $F_S(A,b- A \delta', \ell- \delta',u-\delta',c)$. ◻
:::

Usually, MIP solvers use *variable complementation*, which maps $x_w$ to $x_w - \ell_w$ or $u_w - x_w$, in the context of reflections. Since the bounds of an integer variable are integral, these transformations have the convenient property of preserving integrality. In [\[thm_delta_equivalent\]](#thm_delta_equivalent){reference-type="ref" reference="thm_delta_equivalent"}, we showed that by computing symmetric equitable partitions for one $\delta$ value, the obtained partition is valid for a larger set of $\delta$-values. Next, we use this result to show that computing the symmetric equitable partition for $\delta^\mathcal{C}$ can be used to derive variable complementations.

::: corollary
[]{#thm_delta_equivalent_complemented label="thm_delta_equivalent_complemented"} Let $(\widehat{\MP},\widehat{\MQ})$ be a symmetric, equitable and bound-respecting partition of $F_S(A,b - A \delta^\mathcal{C}, \ell - \delta^\mathcal{C}, u - \delta^\mathcal{C}, c)$ and let $\gamma$, $\lambda$, $\MP_U$ and $\MQ_U$ be generated by $(\widehat{\MP},\widehat{\MQ})$. Then, for $\delta^\mathcal{S}$ defined via $$\delta^\mathcal{S}_w \coloneqq \begin{cases}
        \ell_w &\text{if $\ell_w$ and $u_w$ are finite, $w\in W_U$ and $\lambda_w=1$.}\\
        u_w &\text{if $\ell_w$ and $u_w$ are finite, $w\in W_U$ and $\lambda_w=-1$.}\\
        \frac{\ell_w + u_w}2 &\text{if $\ell_w$ and $u_w$ are finite and $w\in W_B$.}\\
        0 &\text{if $\ell_w = -\infty$ and $u_w = \infty$.}\\
        \ell_w &\text{if $\ell_w$ is finite and $u_w = \infty$.}\\
        u_w &\text{if $\ell_w = -\infty$ and $u_w$ is finite.}
    \end{cases},$$ $(\widehat{\MP},\widehat{\MQ})$ is a symmetric equitable partition of $F_S(A,b - A \delta^\mathcal{S}, \ell - \delta^\mathcal{S}, u - \delta^\mathcal{S}, c)$.
:::

::: proof
*Proof.* Let $\nu \in \R^{W_U}$ be such that $\nu \coloneqq \begin{cases}
        -\frac{u_{w}- \ell_w}2 &\text{if $\ell_w$ and $u_w$ are finite and $w\in W_U$}\\
        0 &\text{otherwise.}
    \end{cases}$

Since the symmetric equitable partition is bound-respecting, the domain size $u_w - \ell_w$ is identical for all variables $w\in Q$ for some part $Q \in \MQ$ in the case where $u_w$ and $\ell_w$ are both finite. Thus, $\nu$ is a $\MQ_U$-equitable vector. Using $\frac{\ell_w + u_w}2 -\frac{u_{w}- \ell_w}2 = \ell_w$ and $\frac{\ell_w + u_w}2 + \frac{u_{w}- \ell_w}2 = u_w$ one can verify that $\delta^\mathcal{S} \coloneqq \delta^\mathcal{C} + (\Lambda \nu, \zerovec_{W_B})$ holds, and the result follows by [\[thm_delta_equivalent\]](#thm_delta_equivalent){reference-type="ref" reference="thm_delta_equivalent"}. ◻
:::

One important detail about [\[thm_delta_equivalent_complemented\]](#thm_delta_equivalent_complemented){reference-type="ref" reference="thm_delta_equivalent_complemented"} is that the variable bounds of bipolar variables are not adjusted and may still be fractional. Later on, we will see that this is not an issue in the context of Mixed-Integer Linear Programming as the bipolar variables are eliminated from the reduced model.
