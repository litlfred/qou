---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-012-8-higher-order-invariants
section_title: "Higher order invariants"
section_number: 8
pages: 26-29
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.969
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
[]{#sec:higher_def label="sec:higher_def"}

We consider now higher order deformations of YBOs, where the condition of being enhanced is preserved for the trace approach. It is known that YBOs can be nontrivially deformed to higher order, as seen explicitly in [@EZ_perturbative]. Our objective in this section is to characterize when higher order deformations define EYBOs, and how to use such deformed EYBOs to define higher order quantum cocycle invariants. Although a similar higher order deformations can be formulated, we focus on the trace approach in the remaining sections, as our purpose of defining this procedure is to give an interpretation of such deformations for the YBOs used for the Jones and Alexander polynomials.

We define the following in a manner similar to the infinitesimal deformation. Let $$\tilde R_{(n)} = \sum_{i=0}^n \hbar^i\phi_i \in \tilde V_{(n)} = \mathbb k [[\hbar]]/ (\hbar^{n+1} )  \otimes V$$ be an order $n$ deformation of the EYBO $\phi_0 := R$. Then, we say that $\phi_{n+1}$ is an enhanced order (or degree) $n+1$ deformation if $$\tilde R_{(n+1)} := \tilde R_{(n)}  + \hbar^{n+1}\phi_{n+1} =  \sum_{i=0}^{n+1} \hbar^i\phi_i 
\in 
\tilde V_{(n+1)} = \mathbb k [[\hbar]]/ (\hbar^{n+2} ) \otimes V$$ is an EYBO.

The following theorem provides conditions for $(\phi_{n+1}, \mu_{n+1})$ to extend deformation $\tilde R_{(n)}$ to $\tilde R_{(n+1)}$ as an EYBO.

We recall the following notation from Definition [\[def:gamma\]](#def:gamma){reference-type="ref" reference="def:gamma"}. $$\begin{aligned}
                    \hat  \Gamma_n^m = \{(j_1,\ldots,j_m )\ |\  j_1+\cdots +j_m= n, \  j_\ell \geq 0\ {\rm and}\  j_\ell \neq n,\ {\rm for\ all}\ \ell=1,\ldots,m \}.
\end{aligned}$$ Recall also, when $m$ is apparent, we use $\hat  \Gamma_n=\hat  \Gamma_n^m$.

We also define, following [@SZ-YBH], the quantity $$\begin{aligned}
        \Theta_{n+1} 
        &:=& \sum_{(i,j,k)\in \hat\Gamma_{n+1}} [(\phi_i\otimes \mathbb 1)(\mathbb 1\otimes \phi_j)(\phi_k\otimes \mathbb 1)- (\phi_k\otimes \mathbb 1)(\phi_i\otimes \mathbb 1)(\mathbb 1\otimes \phi_j)]
    
\end{aligned}$$

::: theorem
[]{#thm:higher_YB_inv label="thm:higher_YB_inv"} Let $R$ be a YBO, and let $\phi_1, \ldots, \phi_n$, $\mu_1, \ldots, \mu_n$, $\alpha, \beta$ be such that $S = (\tilde\phi, \alpha, \beta, \tilde \mu)$ is an EYBO, where $\tilde R_{(n)}= \sum_{i=0}^n \hbar^i\phi_i$ and $\tilde \mu_n = \sum_{i=0}^n \hbar^i\mu_i$. Then the obstruction for $(\phi_{n+1}, \mu_{n+1})$ to be an enhanced order $n+1$ deformation of $R$ is the following system of equations $$\begin{aligned}
\label{eqn:higher_deform0}
            \delta^2_{\rm YB} \phi_{n+1} + \Theta_{n+1} = 0 
            
\end{aligned}$$ and $$\begin{aligned}
\label{eqn:higher_deform}
                \begin{cases}
                                            \sum_{(i,j,k)\in \hat \Gamma_{n+1}} [(\mu_i\otimes \mu_j)\phi_k - \phi_i(\mu_j\otimes \mu_k)] = 0\\
                        \sum_{(i,j,k)\in \hat  \Gamma_{n+1}} \mathop{\mathrm{Tr}}(\phi_i(\mu_j\otimes \mu_k)) = \alpha\beta\mu_{n+1}\\
                        \sum_{(i,j,k)\in  \hat \Gamma_{n+1}} \mathop{\mathrm{Tr}}(\hat \phi_i(\mu_j\otimes \mu_k)) = \alpha\beta\mu_{n+1}
                \end{cases}
        
\end{aligned}$$ where $\hat \phi_i$ indicates the $i^{\rm th}$ component of the inverse of $\tilde R_{(n)} + \hbar^{n+1}\phi_{n+1}$ (modulo $\hbar^{n+2}$).
:::

::: proof
*Proof.* First we show that enhanced higher order deformations are equivalent to the system [\[eqn:higher_deform0\]](#eqn:higher_deform0){reference-type="eqref" reference="eqn:higher_deform0"} and [\[eqn:higher_deform\]](#eqn:higher_deform){reference-type="eqref" reference="eqn:higher_deform"}. It is a known result, see for instance [@SZ-YBH], that the obstruction for $\phi_{n+1}$ to be an order $n+1$ YB deformation of $\tilde \phi$ is $\delta^2_{\rm YB} \phi_{n+1} + \Theta_{n+1} = 0$, where the left-hand side lies in the third cohomology group of $R$. Hence $\phi_{n+1}$ extends $\tilde \phi$ to a YBO if and only if the first equality of [\[eqn:higher_deform0\]](#eqn:higher_deform0){reference-type="eqref" reference="eqn:higher_deform0"} holds.

Commutativity of $\tilde R_{(n+1)}= \tilde R_{(n)}+ \hbar^{n+1}\phi_{n+1}$ with the deformed $\tilde  \mu_{n+1} = \tilde \mu_{n} + \hbar^{n+1}\mu_{n+1}$ means that Equation [\[eqn:mu_comm\]](#eqn:mu_comm){reference-type="eqref" reference="eqn:mu_comm"} holds with $\tilde \mu_{(n+1)}$ and $\tilde R_{(n+1)}$. Taking terms of degree $n+1$ in $\hbar$ gives the first equation in [\[eqn:higher_deform\]](#eqn:higher_deform){reference-type="eqref" reference="eqn:higher_deform"}. Equation [\[eqn:partial_tr\]](#eqn:partial_tr){reference-type="eqref" reference="eqn:partial_tr"} with positive sign gives the second equation of [\[eqn:higher_deform\]](#eqn:higher_deform){reference-type="eqref" reference="eqn:higher_deform"} when considering terms of degree $n+1$ in $\hbar$. Similarly, we obtain the third equation of the system from Equation [\[eqn:partial_tr\]](#eqn:partial_tr){reference-type="eqref" reference="eqn:partial_tr"} with negative sign, where the existence of the inverse of $\tilde R_{(n+1)}$ has been shown in the first part of the proof. This completes the first statement of the theorem.

Next we show that $\tilde R_{(n)}  = \sum_{i=0}^n \hbar^i\phi_i$ is invertible modulo $\hbar^n$ for any $n$. Let us set $\tilde R^{-1}_{(n)}  = \sum_{i=0}^n \hbar^i  \hat \phi_i$. The fact that $\tilde R^{-1}_{(n)}$ is an inverse to $\tilde R_{(n)}$ is equivalent to the following two systems. $$\begin{aligned}
\label{eqn:system_inverse_right}
    \hat \phi_0 = \phi_0^{-1}, \ 
                    \ldots, \ 
                    \hat\phi_k = -\phi_0^{-1}\sum_{i=1}^k \phi_i\hat\phi_{k-i},
                    \  \ldots, \ 
                                        \hat\phi_n = -\phi_0^{-1}\sum_{i=1}^n \phi_i\hat\phi_{n-i}
\end{aligned}$$ and $$\begin{aligned}
\label{eqn:system_inverse_left}
\hat \phi_0 = \phi_0^{-1}, \ \ldots, \      \hat\phi_k = -\sum_{i=1}^k \phi_i\hat\phi_{k-i}\cdot \phi_0^{-1}, \ \ldots, \  
    \hat\phi_n = -\sum_{i=1}^n \phi_i\hat\phi_{n-i} \cdot \phi_0^{-1}
        
\end{aligned}$$ where [\[eqn:system_inverse_right\]](#eqn:system_inverse_right){reference-type="eqref" reference="eqn:system_inverse_right"} gives right-invertibility, and [\[eqn:system_inverse_left\]](#eqn:system_inverse_left){reference-type="eqref" reference="eqn:system_inverse_left"} corresponds to left invertiblity. Additionally, we need to verify that the solutions obtained by the two systems coincide. Let $\phi_{i_1}, \ldots, \phi_{i_k}$ be a list of elements appearing in $\tilde \phi$, not necessarily mutually distinct. We define the symmetrized expression $$\begin{aligned}
                (-1)^n\mathbb S(\phi_{i_1}|\ldots|\phi_{i_k}) = \sum_{\sigma\in \Sigma_k} \frac{1}{q_1!\cdots q_t!} \phi_0^{-1}\phi_{\sigma(i_1)}\phi_0^{-1} \cdots \phi_0^{-1} \phi_{\sigma(i_k)}\phi_0^{-1},
        
\end{aligned}$$ where $q_1, \ldots, q_t$ indicate the number of repeated indices among the $i_r$. Then, we have for example $$\mathbb S(\phi_1| \cdots | \phi_1) = - \phi_0^{-1}\phi_1\phi_0^{-1} \cdots \phi_0^{-1} \phi_1\phi_0^{-1}$$ when $\phi_1$ is repeated $2n+1$ times, $$\mathbb S(\phi_1| \cdots | \phi_1) = \phi_0^{-1}\phi_1\phi_0^{-1} \cdots \phi_0^{-1} \phi_1\phi_0^{-1}$$ when $\phi_1$ is repeated $2n$ times. Similarly, by a direct computation we have $$\mathbb S(\phi_1|\phi_1|\phi_2) = - \phi_0^{-1}\phi_1\phi_0^{-1}\phi_1\phi_0^{-1}\phi_2\phi_0^{-1} - \phi_0^{-1}\phi_1\phi_0^{-1}\phi_2\phi_0^{-1}\phi_1\phi_0^{-1} - \phi_0^{-1}\phi_2\phi_0^{-1}\phi_1\phi_0^{-1}\phi_1\phi_0^{-1}$$ and so forth. We now show that the inverse of $\tilde \phi$ is given by $$\begin{aligned}
\label{eqn:phin}
                \hat \phi_n = \sum \mathbb S(\phi_{i_1}| \cdots |\phi_{i_k}),
        
\end{aligned}$$ where the sum is taken over all the possible choices of indices $i_1, \ldots, i_k$ such that $i_1 \leq i_2 \leq \cdots \leq i_k$ and $\sum_{d=1}^k i_d = n$. We proceed by induction to show that $\hat \phi_n$ chosen as in Equation [\[eqn:phin\]](#eqn:phin){reference-type="eqref" reference="eqn:phin"} gives a solution of the system of equations [\[eqn:system_inverse_left\]](#eqn:system_inverse_left){reference-type="eqref" reference="eqn:system_inverse_left"}.

The case $n=0$ is trivial, since $\hat \phi_0 = \phi_0^{-1}$, and case $n=1$ was seen to produce $\hat \phi_1 = \phi_0^{-1}\phi_1\phi_0^{-1}$, which coincides with $\mathbb S(\phi_1)$, and therefore with Equation [\[eqn:phin\]](#eqn:phin){reference-type="eqref" reference="eqn:phin"} since there is no sum.

Suppose now that the inverse for $\tilde R_{(n)}$ has been determined when there are $n$ terms, with $n>1$. When we consider [\[eqn:system_inverse_left\]](#eqn:system_inverse_left){reference-type="eqref" reference="eqn:system_inverse_left"} for $\tilde R_{(n+1)}$. The first $n$ equations are identical to the case of length $n$. Therefore, they are given by Equation [\[eqn:phin\]](#eqn:phin){reference-type="eqref" reference="eqn:phin"} by the inductive assumption. The $(n+1)^{\rm th}$ equation is given by $$\hat \phi_{n+1} = - \phi_0^{-1} \sum_{i=1}^{n+1} \phi_i \hat \phi_{n+1-i} = - \phi_0^{-1} \sum_{i=1}^{n+1} \phi_i\sum \mathbb S(\phi_{i_1}|\cdots |\phi_{i_k}),$$ where the second sum is defined as in Equation [\[eqn:phin\]](#eqn:phin){reference-type="eqref" reference="eqn:phin"}. A direct inspection shows that the sum in $\hat \phi_{n+1}$ gives all the possible product of terms of type $\phi_0^{-1}\phi_{i_1} \phi_0^{-1} \cdots \phi_0^{-1}\phi_{i_r}\phi_0^{-1}$ where the indices $i_1, \ldots, i_r$ add up to $n+1$. This completes the inductive step. The case of [\[eqn:system_inverse_right\]](#eqn:system_inverse_right){reference-type="eqref" reference="eqn:system_inverse_right"} is analogous. This procedure also shows that both right and left inverses coincide, therefore implying that $\tilde \phi$ is invertible for any $n$. This implies that the system of equations [\[eqn:higher_deform\]](#eqn:higher_deform){reference-type="eqref" reference="eqn:higher_deform"} is well posed. ◻
:::

::: definition
We say that $\phi_1$ is an integrable enhanced deformation when the obstruction to deforming $\tilde R_{(n)} = R + \sum_{i=1}^n\hbar^i\phi_i$ to degree $n+1$, $\tilde R_{(n+1)} = R + \sum_{i=1}^{n+1}\hbar^i\phi_i$ vanishes for all $n$. In other words, if for all $n=1, 2, \ldots$ there exists $\phi_{n+1}$ such that $\tilde R_{(n)} = R + \sum_{i=1}^{n+1}\hbar^i\phi_i$ is an EYBO over $\tilde V_{(n)} = \mathbb k[[\hbar]]/(\hbar^{n+1})\otimes V$. In this case, we formally write $\tilde R = \sum_{i=0}^\infty \hbar^i\phi_i$, where we set $R = \phi_0$.
:::

::: theorem
[]{#thm:higher label="thm:higher"} Let a knot $K$ be given by a diagram that is in a closed braid form of an $m$-braid $b_m$. Suppose that $\tilde R_{(n)}$ is an EYBO with inverse $\tilde R^{-1}_{(n)}$ for all $n=1, \ldots, N$.

Let $\Psi_{ (\tilde R_{(N)}, \tilde R^{-1}_{(N)} ) } (b_m)$ be the operator defined from deformed YBOs $\tilde R^{\pm}_{(n)}$. Then we have that $$\begin{aligned}
                \Phi_{ (\tilde R_{(N)}, \tilde R^{-1}_{(N)} )  } (b_m) =    \sum_{(i,j_1,\ldots,j_m)\in \Gamma^m_n}  \alpha^{-w(b_m)}\beta^{-m}\mathop{\mathrm{Tr}}(\Psi_{ (\tilde R_{(N)}, \tilde R^{-1}_{(N)}) } (b_m)(\mu_{j_1}\otimes \cdots \otimes \mu_{j_m}))
        
\end{aligned}$$ is invariant under Markov moves, and therefore defines a knot invariant $\Phi_\phi (K)$.

Write $\Phi_{ (\tilde R_{(N)}, \tilde R^{-1}_{(N)} )  }  (K) =     \sum_{i=0}^n \hbar^i \Phi^i_{ (\tilde R_{(N)}, \tilde R^{-1}_{(N)} )  } (K)$, then we have $$\begin{aligned}
            \Phi^i_{ (\tilde R_{(N)}, \tilde R^{-1}_{(N)} )  } (K)= \sum_{(i,j_1,\ldots, j_m)\in \Gamma^{m+1}_k} \alpha^{-w(b_m)}\beta^{-m}\mathop{\mathrm{Tr}}(\Psi^i_{ (\tilde R_{(N)}, \tilde R^{-1}_{(N)} )  } (b_m)(\mu_{j_1}\otimes \cdots \otimes \mu_{j_m}))
        
\end{aligned}$$
:::

::: proof
*Proof.* We define the quantum invariant of Turaev [@Tur] associated to the EYBO $\tilde \phi$. Since $\tilde \phi$ is graded by the formal variable $\hbar$, it follows that each coefficient of the monomials in $\hbar$ in the quantum invariant is invariant under Markov moves. Considering the degree $n$ component in $\hbar$ we find the term $\sum_{(i,j_1,\ldots, j_m)\in \Gamma^{m+1}_k} \alpha^{-w(b_m)}\beta^{-m}\mathop{\mathrm{Tr}}(\Psi^i_\phi(b_m)(\mu_{j_1}\otimes \cdots \otimes \mu_{j_m}))$, which is therefore an invariant of the knot $K$. This completes the proof. ◻
:::

Although it is desirable to have cencrete examples of higher order invariants as defined above, it is out of the scope of this paper, and the purpose of this section is to generalize this further to Laurent polynomial deformation to give an interpretation of the Jones and Alexander polynomials as such quantum cocycle invariant in the next section.
