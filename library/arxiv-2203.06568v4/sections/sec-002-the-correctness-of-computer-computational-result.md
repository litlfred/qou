---
doc_id: arxiv-2203.06568v4
doc_title: "Semidefinite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-002-the-correctness-of-computer-computational-result
section_title: "The correctness of computer computational results"
section_number: null
pages: 10-14
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
doc_brief: "Semidefinite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.98
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

## computational results

We use the CVX toolbox [@GB14], [@GB08] in MATLAB with the MOSEK solver to run our SDP. Our main results are as follows. In our SDP, we have tested all possible values of splits $n_{1}$ and $n_{2}$. The computational results give us two improvements $A(18,4) \leq 6551$ and $A(19,4) \leq 13087$. However, using Gijswijt's method in the previous subsection, we are only able to ensure one of them is improved.

::: theorem
$A(18,4) \leq 6551$.
:::

::: proof
*Proof.* Using $n_{1} = 2$, we obtain $A(18,4)\leq 6551.93$ with an error term less than $10^{-16}$. Thus $A(18,4)\leq 6551$. ◻
:::

::: remark
$A(18,4) \leq 6551$ can be obtained by the split SDP with $n_{1} = 2$ and only the constraints ([\[sem1\]](#sem1){reference-type="ref" reference="sem1"}), ([\[sem2\]](#sem2){reference-type="ref" reference="sem2"}), ([\[le3\]](#le3){reference-type="ref" reference="le3"}) and ([\[le5\]](#le5){reference-type="ref" reference="le5"}). Then, we have $A(18,4) \leq 6551.98$ with an error term less than $10^{-16}$. All the above mentioned constraints are necessary in this case.
:::

# Generalization {#sec:gener}

In this section, we consider an $m$-split distance distribution defined on a partition of $\{1, \dots, n\}$ with arbitrary $m$ subsets, say $T_{1}, \dots, T_{m}$, each of size $\lvert T_{p}\rvert = n_{p}$ for $p \in \{1, \dots, m\}$. Our method can be generalized in this case to introduce more semidefinite constraints. Proofs to these generalizations are similar to the $2$-split case and will be omitted. Finally, we discuss the underlying association scheme structure.\

## Semidefinite constraints from $m$-split Terwilliger algebras

Consider a group $G = \prod_{p = 1}^{m}G_{p}$, where $G_{p}$ is the isometry group on the power set of $T_{p}$. Let $\sigma_{1}, \dots, \sigma_{q}$ be the orbits of $G$ acting on ${\cal P}$ for some $q$. Then we define $\lvert {\cal P}\rvert \times \lvert {\cal P}\rvert$ matrices, indexed by ${\cal P}$, $$(M_{\sigma_{k}})_{X, Y} = \left\{
    \begin{aligned}
        &1, \text{ if } X, Y \in \sigma_{k},\\
        &0, \text{ otherwise}
    \end{aligned}\right.$$ for all $k$. Observe that $(X, Y)$ and $(U, V)$ belong to the same orbit if and only if $\lvert X \cap T_{k}\rvert = \lvert U \cap T_{k}\rvert$, $\lvert Y \cap T_{k}\rvert = \lvert V \cap T_{k}\rvert$ and $\lvert X \Delta Y \cap T_{k}\rvert = \lvert U \Delta V \cap T_{k}\rvert$ for each $k$. Let ${\bm i}= (i_{1}, \dots, i_{m})$, ${\bm j}= (j_{1}, \dots, j_{m})$, and ${\bm t}= (t_{1}, \dots, t_{m})$ for $i_{k}, j_{k}, t_{k} \in \{0, \dots, n_{k}\}$ with $i_{k} + j_{k} - 2t_{k} \in \{0, \dots, n_{k}\}$, for all $k \in \{1, \dots, m\}$. Then the orbits of $G$ can be indexed by $({\bm i}, {\bm j}, {\bm t})$ and we may rewrite $M_{\sigma_{k}}$ as $$(M_{{\bm i}, {\bm j}}^{{\bm t}})_{X, Y} = \left\{
    \begin{aligned}
        &1, \text{ if } \lvert X \cap T_{k}\rvert = i_{k}, \lvert Y \cap T_{k}\rvert = j_{k}, \lvert X \cap Y \cap T_{k}\rvert = t_{k} \text{ for all } k;\\
        &0, \text{ otherwise.}
    \end{aligned}\right.$$ For ${\bm n}= (n_{1}, \dots, n_{m})$, we denote the algebra generated by $\{M_{{\bm i}, {\bm j}}^{{\bm t}}\}$ over $\mathbb{C}$, defined as above, by ${\cal A}_{{\bm n}}$, which is called an $m$-split Terwilliger algebra of the Hamming scheme.

::: lemma
${\cal A}_{{\bm n}}$ is isomorphic to $\bigotimes_{i = 1}^{m} {\cal A}_{n_{i}}$.
:::

::: corollary
[]{#cor:blo_g label="cor:blo_g"} There is an isomorphism from ${\cal A}_{{\bm n}}$ to $$\bigoplus_{k_{1} = 0}^{\left\lfloor \frac{n_{1}}{2} \right\rfloor} \cdots \bigoplus_{k_{m} = 0}^{\left\lfloor \frac{n_{m}}{2} \right\rfloor} \mathbb{C}^{N_{{\bm k}} \times N_{{\bm k}}},$$ with $N_{{\bm k}} = \prod_{a = 1}^{m} (n_{a}-2k_{a}+1)$, that maps $A = \sum_{{\bm i}, {\bm j}, {\bm t}}x_{{\bm i}, {\bm j}}^{{\bm t}} M_{{\bm i}, {\bm j}}^{{\bm t}}$ to $$\bigoplus_{k_{1} = 0}^{\left\lfloor \frac{n_{1}}{2} \right\rfloor} \cdots \bigoplus_{k_{m} = 0}^{\left\lfloor \frac{n_{m}}{2} \right\rfloor} {\cal B}_{{\bm k}},$$ where $$\begin{aligned}
            {\cal B}_{{\bm k}} = \left( \sum_{{\bm t}} \prod_{a = 1}^{m} \binom{n_{a}-2k_{a}}{i_{a}-k_{a}}^{-\frac{1}{2}} \binom{n_{a}-2k_{a}}{j_{a}-k_{a}}^{-\frac{1}{2}}  \beta_{i_{a}, j_{a}, k_{a}}^{n_{a}, t_{a}} x_{{\bm i}, {\bm j}}^{{\bm t}} \right)_{({\bm i}, {\bm j}) = ({\bm k}, {\bm k})}^{({\bm n}-{\bm k}, {\bm n}-{\bm k})}
        \end{aligned}$$
:::

Next we derive additional semidefinite constraints for an $(n,d)$ code $C$ from the $m$-split Terwilliger algebra. Define $$x_{{\bm i}, {\bm j}}^{{\bm t}} = \frac{1}{\lvert C\rvert \prod_{k = 1}^{m}\binom{n_{k}}{i_{k}-t_{k}, j_{k}-t_{k}, t_{k}}} \lambda^{{\bm t}}_{{\bm i}, {\bm j}},$$ where $$\begin{aligned}
        \lambda^{{\bm t}}_{{\bm i}, {\bm j}} =  \lvert \{&(X, Y, Z) \in C^{3} : \lvert (X \Delta Y)\cap T_{k}\rvert = i_{k}, \lvert(X \Delta Z)\cap T_{k}\rvert = j_{k},  \\
        &\lvert((X \Delta Y)\cap (X \Delta Z))\cap T_{k}\rvert = t_{k}, \text{ for } k=1,\dots, m \} \rvert.
    \end{aligned}$$ Now, the size of the code $C$ is $$\lvert C\rvert=\sum_{a = 0}^{n} \sum_{{\bm i}\cdot {\bm 1}= a} \prod_{k = 1}^{m} \binom{n_{k}}{i_{k}} x_{{\bm i}, {\bm 0}}^{{\bm 0}},$$ where ${\bm 1}$ denotes the all-one vector and ${\bm 0}$ denotes the zero vector. Then the group $G$ acts on $C$ as follows: $$(g_{1}, \dots, g_{m}) \cdot (c) = \bigcup_{k=1}^{m} g_{k}(c \cap T_{k}),$$ for $g_{i} \in G_{i}$, $i = 1, \dots, m$ and $c \in C$. We define the sets $$\begin{aligned}
    & \Pi_{\rm {\bm s}} = \{g \in G \mid \emptyset \in g(C)\},\\
    & \Pi_{\rm {\bm s}}' = \{g \in G \mid \emptyset \notin g(C)\},
\end{aligned}$$ and consider the semidefinite matrices $$\begin{aligned}
    & R_{\rm {\bm s}} = \frac{1}{\lvert \Pi_{\rm {\bm s}}\rvert} \sum_{g \in \Pi_{\rm {\bm s}}} \chi^{g(C)} (\chi^{g(C)})^{T}, \\
    & R_{\rm {\bm s}}' = \frac{1}{\lvert \Pi_{\rm {\bm s}}'\rvert}\sum_{g \in \Pi_{\rm {\bm s}}'} \chi^{g(C)} (\chi^{g(C)})^{T},
\end{aligned}$$ which are elements of ${\cal A}_{{\bm n}}$. In fact, we have the following proposition.

::: proposition
[]{#pro:R_g label="pro:R_g"} $$\begin{aligned}
            &R_{\rm {\bm s}} = \sum_{{\bm i}, {\bm j}, {\bm t}} x_{{\bm i}, {\bm j}}^{{\bm t}}M_{{\bm i}, {\bm j}}^{{\bm t}},\\
            & 
            \begin{aligned}
                R_{\rm {\bm s}}' =& \frac{\lvert C\rvert}{2^{n}-\lvert C\rvert}\sum_{{\bm i}, {\bm j}, {\bm t}} \left( x_{{\bm i}+{\bm j}-2{\bm t}, {\bm 0}}^{{\bm 0}}-x_{{\bm i}, {\bm j}}^{{\bm t}}\right)M_{{\bm i}, {\bm j}}^{{\bm t}}.
            \end{aligned}
        \end{aligned}$$
:::

From Proposition [\[pro:R_g\]](#pro:R_g){reference-type="ref" reference="pro:R_g"}, we can also obtain the $m$-split generalized Delsarte's inequalities [@Sim95]. Consider the generalized distance distribution $\{A_{{\bm i}}\}$ of $C$, where $$A_{{\bm i}} = \frac{1}{\lvert C\rvert}\lvert\{(a, b) \in C \times C \mid \lvert a \Delta b \cap T_{k}\rvert = i_{k} \text{ for } k=1,\dots,m\}\rvert.$$

::: corollary
If $R_{\rm {\bm s}}$ and $R_{\rm {\bm s}}'$ are positive semidefinite, then []{#coro:m_gen_del label="coro:m_gen_del"} $$\sum_{{\bm i}} A_{{\bm i}} \prod_{k = 1}^{m}K_{p_{k}}^{n_{k}}(i_{k}) \geq 0,$$ for ${\bm p}= (p_{1}, \dots, p_{m})$ with $0 \leq p_{k} \leq n_{k}$ for all $k$.
:::

It can be showed that the generalized Schrijver's SDP constraints with $k = m+2$ induces our positive semidefinite constraint on $R_{s}$.

::: proposition
The positive semidefinite constraints in the generalized Schrijver's SDP with $k = m+2$ implies the positive semidefiniteness of $R_{s}$ .
:::

By the block diagonal form for ${\cal A}_{{\bm n}}$, we have additional semidefinite constraints. For ${\bm k}= (k_{1}, \dots, k_{m})$ with $k_{a} \in \{0, \dots, \lfloor \frac{n_{a}}{2} \rfloor \}$ and $a \in\{1, \dots, m\}$, the matrices $$\label{eq:gen_sdp_1}
    \begin{aligned}
        \left( \sum_{{\bm t}} \prod_{a = 1}^{m} \binom{n_{a}-2k_{a}}{i_{a}-k_{a}}^{-\frac{1}{2}} \binom{n_{a}-2k_{a}}{j_{a}-k_{a}}^{-\frac{1}{2}}  \beta_{i_{a}, j_{a}, k_{a}}^{n_{a}, t_{a}} x_{{\bm i}, {\bm j}}^{{\bm t}} \right)_{({\bm i}, {\bm j}) = ({\bm k}, {\bm k})}^{({\bm n}-{\bm k}, {\bm n}-{\bm k})},
    \end{aligned}$$ $$\label{eq:gen_sdp_2}
    \begin{aligned}
        \left( \sum_{{\bm t}} \prod_{a = 1}^{m} \binom{n_{a}-2k_{a}}{i_{a}-k_{a}}^{-\frac{1}{2}} \binom{n_{a}-2k_{a}}{j_{a}-k_{a}}^{-\frac{1}{2}}  \beta_{i_{a}, j_{a}, k_{a}}^{n_{a}, t_{a}} (x_{{\bm i}+{\bm k}-2{\bm t}, {\bm 0}}^{{\bm 0}}-x_{{\bm i}, {\bm j}}^{{\bm t}}) \right)_{({\bm i}, {\bm j}) = ({\bm k}, {\bm k})}^{({\bm n}-{\bm k}, {\bm n}-{\bm k})}
    \end{aligned}$$ are semidefinite.

::: proposition
Let $C$ be a code with length $n$ and minimum distance at least $d$. Then we have the following linear constraints on $x_{{\bm i}, {\bm j}}^{{\bm t}}$ corresponding to $C$: for proper ${\bm i}, {\bm j}, {\bm t}$, $$\begin{aligned}
        \label{eq:gen_lin}
        \begin{array}{cl}
            \mbox{(i) }& x_{{\bm 0}, {\bm 0}}^{{\bm 0}} = 1 \\
            \mbox{(ii) }& 0 \leq x_{{\bm i}, {\bm j}}^{{\bm t}} \leq x_{{\bm i}, {\bm 0}}^{{\bm 0}} \\
            \mbox{(iii) }& x_{{\bm i}, {\bm 0}}^{{\bm 0}} + x_{{\bm 0}, {\bm j}}^{{\bm 0}} \leq 1 + x_{{\bm i}, {\bm j}}^{{\bm t}} \\
            \mbox{(iv) }& x_{{\bm i}, {\bm j}}^{{\bm t}} = x_{{\bm a}, {\bm b}}^{{\bm c}} \mbox{ if } ({\bm i}, {\bm j}, {\bm i}+{\bm j}-2{\bm t})  \\
            &\mbox{ is a permutation of } ({\bm a}, {\bm b}, {\bm a}+{\bm b}-2{\bm c}),  \\
            \mbox{(v) }&  x_{{\bm i}, {\bm j}}^{{\bm t}} = 0 \mbox{ if } \{{\bm i}, {\bm j}, {\bm i}+{\bm j}-2{\bm t}\} \cap \{1, \dots, d-1\} \neq \emptyset. 
        \end{array}
    
\end{aligned}$$
:::

To sum up, we have an SDP for $A(n, d)$ with variables $x_{{\bm i}, {\bm j}}^{{\bm t}} \in \mathbb{C}$: $$\begin{aligned}
    {\rm maximize } &\sum_{a = 0}^{n} \sum_{{\bm i}\cdot {\bm 1}= a} \prod_{k = 1}^{m} \binom{n_{k}}{i_{k}} x_{{\bm i}, {\bm 0}}^{{\bm 0}}.  \notag\\
    {\rm subject\ to\ }       &  \mbox{ positive semidefiniteness of }(\ref{eq:gen_sdp_1}) \text{ and } (\ref{eq:gen_sdp_2}) \notag
    \\ & (\ref{eq:gen_lin})   \notag
\end{aligned}$$ This SDP is called an $m$-split SDP, which corresponds to an $m$-split Terwilliger algebra ${\cal A}_{{\bm n}}$.
