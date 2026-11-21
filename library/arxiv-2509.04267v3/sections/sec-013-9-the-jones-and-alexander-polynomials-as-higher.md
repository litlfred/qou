---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-013-9-the-jones-and-alexander-polynomials-as-higher
section_title: "The Jones and Alexander polynomials as higher order invariants"
section_number: 9
pages: 29-33
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.631
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
[]{#sec:Jones_Alex label="sec:Jones_Alex"}

In this section we discuss how to interpret the Jones and Alexander polynomials as quantum cocycle invariants. We need a slight generalization of the framework considered up to now, before proceeding with the main results of the section.

Note that YB cohomology used in this article does not depend on the invertibility of the YBO, as opposed to that used in [@Eis; @Eis1], for example. Therefore, it still makes sense to discuss YB cocycles of pre-YB operators, i.e. operators that satisty the YBE, but are not necessarily invertible. While we have assumed invertibility so far, in this section we will not make this assumption.

::: definition
[]{#def:Laurent label="def:Laurent"} Let $$\tilde R_{(n)}=\sum_{i=0}^n \hbar^i \phi_i  \in \tilde V_{(n)} = \mathbb k[[\hbar]]/(\hbar^{ n+1 } ) \otimes  V
\quad {\rm  and} \quad
\tilde R^{-1}_{(n)} = \sum_{i=0}^n \hat\hbar^i \hat \phi_i  \in \hat V_{(n)} = \mathbb k[[\hat \hbar]]/(\hat \hbar^{ n+1}  ) \otimes  V$$ be pre-YBOs for all $n=0, \ldots, N$. Regard $\tilde V_{(N)}$ and $\hat V_{(N)}$ as submodules of $$\mathcal V = \mathbb k [[\hbar, \hat \hbar ]]/ (\hbar \hat \hbar -1) .$$ If $\tilde R_{(N)}$ and $\tilde R^{-1}_{(N)}$ satisfy the YBE in $\mathcal V$, and are inverse to each other in $\mathcal V$, then we say that $(\tilde R_{(N)}, \tilde R^{-1}_{(N)})$ is a YBO obtained by *Laurent deformation* of pre-YBOs $(R, R^{-1})=(\phi_0, \hat \phi_0)$, of order $N$. We do not exclude the case where $N = \infty$, and $\tilde R_{(\infty)}=\sum_{i=0}^\infty \hbar \phi_i$, $\tilde R^{-1}_{(\infty)} = \sum_{i=0}^\infty \hat\hbar^i \hat \phi_i$.
:::

We further elucidate the situation in Definition [\[def:Laurent\]](#def:Laurent){reference-type="ref" reference="def:Laurent"}. For finite $N$, each $\tilde R_{(n)}$ is a pre-YBO modulo factors of degree $\hbar^{n+1}$, for $n=0, \ldots, N-1$. However, when considering $\tilde  R_{(N)}$, it is assumed in the definition that this operator satisfies the YBE exactly, in the sense that the YBE is satisfied even without quotienting modulo $\hbar^{N+1}$. A similar assumption is made for $R^{-1}_{(n)}$. Moreover, the operators $\tilde R_{(N)}$ and $\tilde  R^{-1}_{(N)}$ are inverse to each others when the condition $\hat \hbar = \hbar^{-1}$ is imposed. When $N=\infty$, we have that $\tilde  R_{(n)}$ and $\tilde  R^{-1}_{(n)}$ are pre-YBOs for each $n\in \mathbb N$, but the full power series satisfy the YBE exactly, and they are inverse to each other. When deformations are integrable, we can automatically find such $\tilde  R_{(\infty)}$ and $\tilde  R^{-1}_{(\infty)}$. We will provide two examples of finite order Laurent deformations that correspond to the Jones and Alexander polynomials below. They are both Laurent deformations of order $2$, and we will see that while the first order deformations are only pre-YBOs, hence they are invertible only modulo degrees of order $2$, the second order deformations satisfy the YBE exactly, and are invertible exactly.

::: lemma
Suppose that $\tilde R_{(n)}$ and $R^{-1}_{(n)}$ are pre-YBOs, and that $\phi_{n+1}$ and $\hat \phi_{n+1}$ satisfy Equation [\[eqn:higher_deform0\]](#eqn:higher_deform0){reference-type="ref" reference="eqn:higher_deform0"}: $$\delta^2_{\rm YB}\phi_{n+1} + \Theta_{n+1} = 0 \quad {\rm and } \quad \delta^2_{\rm YB}\hat \phi_{n+1} + \Theta_{n+1} = 0$$ respectively, for all $n=1, \ldots, n$, and that $\tilde R_{(n+1)}$ and $R^{-1}_{(n+1)}$ are inverses to each other in $\mathcal V$, then $( \tilde R_{(n+1)}, \tilde R^{-1}_{(n+1)}  )$ is a Laurent deformation of $(\phi_0, \hat \phi_0)$.
:::

::: proof
*Proof.* In the proof of the first statement of Theorem [\[thm:higher_YB_inv\]](#thm:higher_YB_inv){reference-type="ref" reference="thm:higher_YB_inv"}, it was not assumed that $\tilde R_{(n)}$ is invertible for any $n$, and that Equation [\[eqn:higher_deform0\]](#eqn:higher_deform0){reference-type="eqref" reference="eqn:higher_deform0"} is sufficient for $\tilde R_{(n)}$ to be a YBO. This also holds for $R^{-1}_{(n)}$ as well. ◻
:::

::: definition
[]{#def:ELaurent label="def:ELaurent"}

Let $(\tilde R_{(N)}, \tilde R^{-1}_{(N)})$ be a Laurent deformation of $(\phi_0, \hat \phi_0)$ as in Definition [\[def:Laurent\]](#def:Laurent){reference-type="ref" reference="def:Laurent"}. If $\tilde R_{(N)}$ and $\tilde R^{-1}_{(N)}$ are both enhanced YBO, then we call the pair $(\tilde R_{(N)}, {\tilde R_{(N)}}^{-1} )$ a *Laurent enhanced YBO (LEYBO)*.
:::

::: lemma
[]{#lem:LEYBOinv label="lem:LEYBOinv"} Let $(\tilde R_{(N)}, \tilde R^{-1}_{(N)})$ be a Laurent enhanced YBO. Let $b_m$ be an $m$-braid whose closure represents a knot $K$. (end replace, below $D$ is replaced by $b_m$) Let $\Psi_{(\tilde R_{(N)}, \tilde R^{-1}_{(N)}) } (b_m)$ be the braid representation defined from $(\tilde R_{(N)}, \tilde R^{-1}_{(N)})$. Let $$\begin{aligned}
                \Phi_{(\tilde R_{(N)}, \tilde R^{-1}_{(N)})}(b_m) =     \sum_{(i,j_1,\ldots,j_m)\in \Gamma^m_n}  \alpha^{-w(b_m)}\beta^{-m}\mathop{\mathrm{Tr}}(\Psi_{(\tilde R_{(N)}, \tilde R^{-1}_{(N)})  }(b_m)(\mu_{j_1}\otimes \cdots \otimes \mu_{j_m}))
        
\end{aligned}$$ be as in Theorem [\[thm:higher\]](#thm:higher){reference-type="ref" reference="thm:higher"}. Then $\Phi_{(\tilde R_{(N)}, \tilde R^{-1}_{(N)}) }(b_m)$ defines a knot invariant $\Phi_{(\tilde R_{(N)}, \tilde R^{-1}_{(N)}) }(K)$, called a *quantum cocycle invariant from LEYBO*.
:::

::: proof
*Proof.* The proof of Theorem [\[thm:higher\]](#thm:higher){reference-type="ref" reference="thm:higher"} applies without assumption of invertibility of $\tilde R_{(n)}$ and $\tilde R^{-1}_{(n)}$ for $n < N$, and only requires invertibility of $\tilde R_{(N)}$ and $\tilde R^{-1}_{(N)}$. ◻
:::

::: theorem
[]{#thm:Jones label="thm:Jones"} The Jones polynomial is a quantum cocycle invariant from LEYBO. Moreover, let $D$ be a closed braid diagram of the knot $K$ on $n$ strings, with $m^+$ positive and $m^-$ negative crossings. Then, we have $$\begin{aligned}
                    (\hbar+\hbar^{-1})J(K) = \hbar^{m^+-m^--n} 
                    \Phi_{(\tilde R_{(N)}, \tilde R^{-1}_{(N)}) }(K)
            
\end{aligned}$$ for some $\tilde R_{(N)}$ and $\tilde R^{-1}_{(N)}$.
:::

::: proof
*Proof.* We explicitly construct $\tilde R_{(N)}$ and $\tilde R^{-1}_{(N)}$.

Recall (e.g. [@Ohtsuki]) that the Jones polynomial (up to a factor of $t^{\frac{1}{2}}+t^{-\frac{1}{2}}$) can be obtained as a trace invariant of an appropriate EYBO $(J,\mu, 1, 1)$. We use this EYBO and rewrite it using the formalism developed in this article. By setting $t^{\frac{1}{2}} = \hbar$ we have $$\begin{aligned}
                J =  \begin{bmatrix}
                    t^{\frac{1}{2}} & 0 & 0 & 0\\
                    0 & 0 & t & 0\\
                    0 & t & t^{\frac{1}{2}}-t^{\frac{3}{2}} & 0\\
                    0 & 0 & 0 & t^{\frac{1}{2}}
                \end{bmatrix}
                = \hbar
                \begin{bmatrix}
                        1 & 0 & 0 & 0\\
                        0 & 0 & \hbar & 0\\
                        0 & \hbar & 1-\hbar^2 & 0\\
                        0 & 0 & 0 & 1
                \end{bmatrix}.
        
\end{aligned}$$ This form of $J$ can be rewritten as $$J=J_0 + \hbar J_1 + \hbar^2 J_2,$$ where $$\begin{aligned}
        J_0 = \begin{bmatrix}
        1 & 0 & 0 & 0\\
        0 & 0 & 0 & 0\\
        0 & 0 & 1 & 0\\
        0 & 0 & 0 & 1
        \end{bmatrix} ,
        \quad
        J_1= \begin{bmatrix}
        0 & 0 & 0 & 0\\
        0 & 0 & 1 & 0\\
        0 & 1 & 0 & 0\\
        0 & 0 & 0 & 0
        \end{bmatrix} ,
        \quad 
        J_2=        \begin{bmatrix}
    0 & 0 & 0 & 0\\
            0 & 0 & 0 & 0\\
            0 & 0 & -1 & 0\\
            0 & 0 & 0 & 0
        \end{bmatrix}.
    
\end{aligned}$$

By computer calculations, we find $J_0$ is a pre-YBO, i.e. it satisfies the YBE but it is not invertible, and $J_1$ is a YB $2$-cocycle. However, since the YBE for $J$ holds exactly, as opposed as being up to higher orders of $\hbar$ than $2$, it means that the deformation is integrable by adding zero maps of all orders.

To find an inverse, we proceed analogously by using the matrix $$\begin{aligned}
            J^{-1} = \begin{bmatrix}
                1 & 0 & 0 & 0\\
                0 & 1-\hbar^{-2} & \hbar^{-1} & 0\\
                0 & \hbar^{-1} & 0 & 0\\
                0 & 0 & 0 & 1
            \end{bmatrix},
    
\end{aligned}$$ and decompose this in terms of $\hbar^{-1}$, denoting the matrices by $\hat J_i$, $i=0,1,2$. The same discussion as for $J$ applies here too, mutatis mutandis.

Next, we have $$\begin{aligned}
            \mu = \begin{bmatrix}
                t^{-\frac{1}{2}} & 0\\
                0 & t^{\frac{1}{2}}
            \end{bmatrix}
                    = \hbar^{-1} \begin{bmatrix}
                        1 & 0\\
                        0 & \hbar^2
                    \end{bmatrix}.
    
\end{aligned}$$ It follows that $$\begin{aligned}
            \hbar \mu = \mu_0 + \mu_2 = 
            \begin{bmatrix}
            1 & 0\\
            0 & 0
            \end{bmatrix}
            + 
            \hbar^{-1} \begin{bmatrix}
            0 & 0\\
            0 & \hbar^2
            \end{bmatrix}.
    
\end{aligned}$$

To show that $$\begin{aligned}
        (\hbar+\hbar^{-1})J( K) = \hbar^{m^+-m^--n} \Phi_{(\tilde R_{(N)}, {\tilde R_{(N)}}^{-1} )}(  K),
    
\end{aligned}$$ we set $\phi = \sum_{i=0}^2 \hbar^i J_i$ and $\hat \phi = \sum_{i=0}^2 \hbar^i \hat J_i$. Then, $\Phi_{(\tilde R_{(N)}, \tilde R_{(N)}^{-1} ) } (  K)$ differs from the Jones polynomial $J(  K)$ by only a multiplying power of $\hbar$, which was initially factored out when constructing the matrices $J$ and $J^{-1}$. Since $J$ needs to be multiplied by $\hbar$ and $J^{-1}$ by $\hbar^{-1}$, it follows that $\hbar^{m^+-m^-}$ corrects this deficiency and gives $J( K)$ as needed. Lastly, each $\mu$ contributes with a factor $\hbar^{-1}$, and there are $n$ of them since $K$ is obtained as the closure of a braid on $n$ strings. ◻
:::

Although the trace is taken only in the factors $2, \ldots, m$ leaving the first factor in the following theorem, so that it is not fully LEYBO as defined, it provides a similar description for the Alexander polynomial, and we make the following statement.

::: theorem
[]{#thm:Alex label="thm:Alex"} The Alexander polynomial $\Delta( K)$ of a knot $K$ is a quantum cocycle invariant in the following sense. Let $K$ be represented by a closed braid form of an $m$-braid $b_m$. Assume that $b_m$ has $m^+$ positive and $m^-$ negative crossings. Then, we have $$\begin{aligned}
        \Delta (K) \cdot \mathbb 1 = \hbar^{-m^++m^-+m-1} \mathop{\mathrm{Tr}}_{2,\ldots, m}
        (\Psi_{(\tilde R_{(N)}, \tilde R^{-1} _{(N)} ) }(b_m) (\mathbb 1\otimes \mu^{\otimes (m-1)}) ) ,
    
\end{aligned}$$ for some $\phi$ and its inverse $\hat \phi$, where $\mathop{\mathrm{Tr}}_{2,\ldots, m}$ is the trace over the $2, 3, \ldots, m$ factors of ${\mathcal V}$.
:::

::: proof
*Proof.* The proof is analogous to the case of the Jones polynomial above. We have, from [@Ohtsuki], the equality $$\begin{aligned}
                    \Delta(K)\cdot \mathbb 1 = \mathop{\mathrm{Tr}}_{2,\ldots, m}(\psi_{\hat \Delta}(b_m) (\mathbb 1\otimes \mu^{\otimes (m-1)})), 
            
\end{aligned}$$ where $\psi_{\hat \Delta}(b_m)$ is the operator obtained from $b_m$ by replacing crossings with the matrix $$\begin{aligned}
                \hat \Delta = \begin{bmatrix}
                    t^{-\frac{1}{2}} & 0 & 0 & 0\\
                    0 & 0 & 1 & 0\\
                    0 & 1 & t^{-\frac{1}{2}}-t^{\frac{1}{2}} & 0\\
                    0 & 0 & 0 & -t^{\frac{1}{2}}
                \end{bmatrix}, 
            
\end{aligned}$$ and $$\begin{aligned}
                    \mu = \begin{bmatrix}
                        t^{\frac{1}{2}} & 0\\
                        0 & -t^{\frac{1}{2}}
                    \end{bmatrix}
                    =
                \hbar  \begin{bmatrix}
                        1 & 0\\
                        0 & -1
                    \end{bmatrix}.
            
\end{aligned}$$ We factor out a term of $\hbar^{-1} = t^{-\frac{1}{2}}$ from the matrix $\hat \Delta$ to obtain $$\begin{aligned}
                \Delta = \begin{bmatrix}
                    1 & 0 & 0 & 0\\
                    0 & 0 & \hbar & 0\\
                    0 & \hbar & 1-\hbar^2 & 0\\
                    0 & 0 & 0 & -\hbar^2
                \end{bmatrix}.
            
\end{aligned}$$ Its inverse is given by $$\begin{aligned}
                        \Delta^{-1} = \begin{bmatrix}
                            1 & 0 & 0 & 0\\
                            0 & 1-\hbar^{-2} & \hbar^{-1} & 0\\
                            0 & \hbar^{-1} & 0 & 0\\
                            0 & 0 & 0 & -\hbar^{-2}
                        \end{bmatrix}.
                    
\end{aligned}$$

In this case one needs to have $\Delta_i$ with $i=0,1,2$. As in the case of the Jones polynomial, computer calculations show that $\Delta_0$ is a pre-YBO and $\Delta_1$ is a YB 2-cocycle.

Since $\hbar^{-1}$ is factored out for $\Delta$, and $\hbar$ is factored out for $\Delta^{-1}$ (i.e., $\hbar \Delta^{-1}= \tilde{\Delta}^{-1}$), we find that the generalized quantum cocycle invariant needs to be multiplied by $\hbar^{-m^++m^-}$ to give the Alexander polynomial. The map $\mu$ introduces a factor of $\hbar^{m-1}$, one for each copy of $\mu$. The details are analogous to the case of the Jones polynomial in Theorem [\[thm:Jones\]](#thm:Jones){reference-type="ref" reference="thm:Jones"}, except the fact that the trace is a partial trace on the entries $2, \ldots, m$ of $V^{\otimes m}$. ◻
:::
