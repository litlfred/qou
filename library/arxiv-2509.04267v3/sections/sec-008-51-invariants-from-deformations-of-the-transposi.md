---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-008-51-invariants-from-deformations-of-the-transposi
section_title: "Invariants from deformations of the transposition"
section_number: 5.1
pages: 12-15
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.92
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
Let us consider a finite dimensional vector space $V$ along with the transposition map $R=\tau : V\otimes V \rightarrow V\otimes V$, which is a YBO on $V$.

::: lemma
For $R=\tau$, we have $H^2_{\rm YB}(V, V) = C^2_{\rm YB}(V, V) = {\rm Hom} (V^{\otimes 2}, V^{\otimes 2})$.
:::

::: proof
*Proof.* For a $2$-cochain $\phi$, we use the structure constants $\phi(e_i\otimes e_j) = \phi_{ij}^{k\ell}e_k\otimes e_\ell$, where we employ the usual Einstein notation for the sums of repeated indices, and we have denoted by $e_1, \ldots, e_n$ a basis for $V$. The first term in the 2-cocycle condition is $$\begin{aligned}
                (R \otimes \mathbb 1) (\mathbb 1 \otimes R)(\phi \otimes \mathbb 1)(e_i \otimes e_j \otimes e_k)
                = (\tau  \otimes \mathbb 1) (\mathbb 1 \otimes \tau) ( \phi_{ij}^{tr} e_t \otimes e_r \otimes e_k) ) = 
                \phi_{ij}^{tr}  e_k \otimes e_t \otimes e_r.
            
\end{aligned}$$ Similarly the 2-cocycle condition is computed as $$\begin{aligned}
        \lefteqn{   \delta^2_{\rm YB}(\phi)(e_i \otimes e_j \otimes e_k ) }\\
        &=&             \phi_{ij}^{tr} e_k\otimes e_t\otimes e_r + \phi_{ik}^{tr} e_t\otimes e_j\otimes e_r 
                    + \phi_{jk}^{tr} e_t\otimes e_r\otimes e_i \\ 
                    & & - \phi_{jk}^{tr} e_t\otimes e_r\otimes e_i -  \phi_{ik}^{tr} e_t\otimes e_j\otimes e_r  - \phi_{ij}^{tr} e_k\otimes e_t\otimes e_r =0 , 
            
\end{aligned}$$ which is satisfied. It follows that any $2$-cochain is a $2$-cocycle. Similarly, using the notation $f(e_i) = f_i^je_j$ for a $1$-cochain $f:V\rightarrow V$, we find directly that $\delta^1_{\rm YB}(f) = 0$. Hence we have $H^2_{\rm YB}(V, V) = C^2_{\rm YB}(V, V)$. ◻
:::

For the transposition $\tau$, Equations [\[eqn:mu_comm\]](#eqn:mu_comm){reference-type="eqref" reference="eqn:mu_comm"} and [\[eqn:partial_tr\]](#eqn:partial_tr){reference-type="eqref" reference="eqn:partial_tr"} can be checked to see that $S=(R,\alpha, \beta, \mu_0)= (\tau, 1, 1, \mathbb 1)$ is an EYBO. We consider the problem of finding enhanced $2$-cocycles of $\tau$.

::: lemma
[]{#lem:cocy_tau label="lem:cocy_tau"} Let $V = \mathbb R\langle e_0,e_1\rangle$ be a 2-dimensional real vector space on basis $e_0, e_1$. Let $S=(\tau, 1, 1, \mathbb 1)$ be an EYBO as above. Let $\tilde S=(\tilde R, 1, 1, \tilde \mu)$ where $\tilde R = \tau +    \hbar \phi$ and $\tilde \mu= \mathbb 1 + \hbar \mu_1$. Consider the following choices for $\phi$ and $\mu_1$: $$\begin{aligned}
 \quad
\phi_{i0}^{k0} = - \phi_{0i}^{0k}, \ 
\phi_{i1}^{k1} = - \phi_{1i}^{1k}, \
\phi_{01}^{10} \ {\rm and} \  \phi_{10}^{01} \ {\rm arbitrary,\  with} \ 
 \mu_1 \ {\rm defined \ by}\  \mu_i^k = -\phi_{i0}^{k0} - \phi_{i1}^{k1}.
\label{eq:phi}
\end{aligned}$$

Then we have that $\tilde S =(\tau + \hbar \phi, 1, 1, \mathbb 1 + \hbar \mu_1)$ is an EYBO.
:::

::: proof
*Proof.* Let $\tilde \mu = \mu_0 + \hbar \mu_1$ be a deformation of $\mu_0$, where $\mu_0=\mathbb 1$, and write $\mu_1(e_i) = \mu_i^je_j$. We need to obtain the constraints on $\phi$ and $\mu_1$ in order to have Equation [\[eqn:inf_mu_comm\]](#eqn:inf_mu_comm){reference-type="eqref" reference="eqn:inf_mu_comm"} to hold. The first term in the left-hand side of Equation [\[eqn:inf_mu_comm\]](#eqn:inf_mu_comm){reference-type="eqref" reference="eqn:inf_mu_comm"} for $(0,0,1) \in \Gamma_2$ is $\phi_0( \mu_0 \otimes \mu_1)(e_i \otimes e_j )$, and substituting $\phi_0=\tau$, $\mu_0=\mathbb 1$ and $\mu_1 (e_j ) = \mu_j^k e_k$, we obtain $\mu_j^k e_k\otimes e_i$ as the first term. Similar computations for Equation [\[eqn:inf_mu_comm\]](#eqn:inf_mu_comm){reference-type="eqref" reference="eqn:inf_mu_comm"} give $$\begin{aligned}
                    \mu_j^k e_k\otimes e_i + \mu_i^k e_j\otimes e_k + \phi_{ij}^{k\ell}e_k\otimes e_{\ell} = \phi_{ij}^{k\ell}e_k\otimes e_{\ell} + \mu_i^ke_j\otimes e_k + \mu_j^ke_k\otimes e_i,
            
\end{aligned}$$ which once again holds identically.

For the deformation $\tilde S=(\tilde R, \alpha, \beta, \phi)=(\tau+\hbar \phi, \mathbb 1, \mathbb 1, \mu_1)$ to give an EYBE, it is sufficient to verify Equations [\[eqn:inf_partial_tr+\]](#eqn:inf_partial_tr+){reference-type="eqref" reference="eqn:inf_partial_tr+"} and [\[eqn:inf_partial_tr-\]](#eqn:inf_partial_tr-){reference-type="eqref" reference="eqn:inf_partial_tr-"}. To evaluate $\mathop{\mathrm{Tr}}_2$, we calculate as follows. With basis $\{ e_i \}$, let an operator $A$ defined via the tensor notation $A(e_i\otimes e_j) = \sum_{kl} a_{ij}^{kl}e_k\otimes e_l$, and let $e_j^*$ be dual basis vectors. Then the computation for $\mathop{\mathrm{Tr}}_2(A)$ is performed as $$e_i \mapsto \sum_j e_i\otimes e_j\otimes e_j^* 
            \mapsto \sum_j A(e_i\otimes e_j)\otimes e_j^* 
            \mapsto \sum_j a_{ij}^{kl} e_k\otimes e_l \otimes e^*_j 
            \mapsto \sum_j a_{ij}^{kl}\delta_{jl} e_k 
            =  \sum_j a_{ij}^{kj} e_k.$$ Hence the entry $ik$ of the matrix for $\mathop{\mathrm{Tr}}_2(A)$ is $\sum_j a_{ij}^{kj}$, or simply $a_{ij}^{kj}$ in Einstein convention.

We compute $\mathop{\mathrm{Tr}}_2 \tau(\mu_0\otimes \mu_1)(e_i) =  \mu_i^ke_k = \mu_1(e_i)$, $\mathop{\mathrm{Tr}}_2 \tau(\mu_1\otimes \mu_0)(e_i) =   \mu_i^je_j = \mu_1(e_i)$, and $\hat \phi_1 = -\phi_0^{-1}\phi_1\phi_0^{-1}$ as in Theorem [\[thm:inf_YB_inv\]](#thm:inf_YB_inv){reference-type="ref" reference="thm:inf_YB_inv"}. For Equations [\[eqn:inf_partial_tr+\]](#eqn:inf_partial_tr+){reference-type="eqref" reference="eqn:inf_partial_tr+"} we compute $$\mathop{\mathrm{Tr}}_2 \tau(\mu_0\otimes \mu_1)(e_i) + \mathop{\mathrm{Tr}}_2 \tau(\mu_1\otimes \mu_0)(e_i) + \mathop{\mathrm{Tr}}_2 \phi(\mu_0\otimes \mu_0)(e_i) =\mu_1 (e_i),$$ hence we obtain $\phi_{ij}^{kj} = - \mu_i^k$. Similarly for Equations [\[eqn:inf_partial_tr-\]](#eqn:inf_partial_tr-){reference-type="eqref" reference="eqn:inf_partial_tr-"} we obtain $\phi_{ji}^{jk} = \mu_i^k$. Then it is checked that the stated Solution [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} indeed satisfies these equations, due to the symmetry $\phi_{ik}^{i\ell} = - \phi_{ki}^{\ell i}$, which uniquely fixes $\mu_1$, and the fact that $\phi_{01}^{10}$ and $\phi_{10}^{01}$ do not appear in the equations for the partial trace. ◻
:::

Let $\sigma_1$ denote the standard generator of the 2-strand braid group ${\mathbb B}_2$, and let $T_n$ be the closure of $\sigma_1^n$ for s positive integer $n$. For $n=2,3$, $T_n$ is a Hopf link and trefoil knot, respectively.

::: proposition
[]{#prop:Tn label="prop:Tn"} Consider the special case of Solution [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} in Lemma [\[lem:cocy_tau\]](#lem:cocy_tau){reference-type="ref" reference="lem:cocy_tau"}: $$\phi_{01}^{01} = -\phi_{10}^{10} = \phi_{01}^{11} = - \phi_{10}^{11} = 1, \
 \phi_{01}^{10} = \phi_{10}^{01} = q,$$ and $\phi_{ij}^{k\ell} = 0$ otherwise, where $q$ is an arbitrary real number, along with $\mu_0^0 = \mu_0^1 = -\mu_1^1 = 1$, $\mu_1^0 = 0$.

For the knots and links $T_n$ and the YB 2-cocycle $\phi$ in this solution, we have the following values. $$\begin{aligned}
                \Phi_{\phi} (T_n) =\begin{cases}
                    4+2nq\hbar \ \ n = 2k  \\
                    2  \ \ n = 2k+1
                \end{cases}
\end{aligned}$$
:::

::: proof
*Proof.* We consider $\Phi_\phi^i(T_n)$ for $i=0,1$ separately. For $i=0$, $\Phi_\phi^i(T_n)$ is the trace of $\tau^n$, which takes values $4$ or $2$ depending on the parity of $n$. For the degree $i=1$ we first compute the traces $$\mathop{\mathrm{Tr}}(\phi) = \mathop{\mathrm{Tr}}(\tau\phi\tau) =0, \quad {\rm and} \quad \mathop{\mathrm{Tr}}(\phi\tau) = \mathop{\mathrm{Tr}}(\tau\phi) = 2q,$$ which are obtained by direct inspection of the action of the operators on the four basis vectors $e_i\otimes e_j$. Moreover, a direct computation shows that $$\mathop{\mathrm{Tr}}(\tau[\mu_1\otimes \mathbb 1 + \mathbb 1\otimes \mu_1]) = \mathop{\mathrm{Tr}}(\mu_1\otimes \mathbb 1 + \mathbb 1\otimes \mu_1) = 0,$$ which in turn implies that $\mathop{\mathrm{Tr}}(\tau^n[\mu_1\otimes \mathbb 1 + \mathbb 1\otimes \mu_1])=0$ for all $n$. Therefore we do not include $\mu_1$ terms in the computations below.

We now proceed by induction. We need to compute $$\begin{aligned}
                \Phi^1_\phi(T_n) &=& \sum_{i=0}^{n-1} \mathop{\mathrm{Tr}}(\tau^{n-i-1}\phi\tau^i), 
        
\end{aligned}$$ and proceed by induction on $k$, where we distinguish the two cases $n=2k$ and $n=2k+1$, with $k\geq 0$. The base case $k=0$ of $n=2k+1$ is clearly satisfied, since $\Phi^1_\phi(T_n) = \mathop{\mathrm{Tr}}(\phi) = 0$. Suppose that $\Phi^1_\phi(T_n) = 0$ for $n = 2k-1$. We compute $$\begin{aligned}
                    \Phi^1_\phi(T_{2k+1}) 
                    &=&  \sum_{i=0}^{2k} \mathop{\mathrm{Tr}}(\tau^{2k-i}\phi\tau^i)\\
                    &=& \sum_{i=0}^{2k-2} \mathop{\mathrm{Tr}}(\tau^2\tau^{2k-i}\phi\tau^i) + \mathop{\mathrm{Tr}}(\tau \phi \tau^{2k-1}) + \mathop{\mathrm{Tr}}(\tau^2 \phi \tau^{2k})\\
                    &=& \sum_{i=0}^{2k-2} \mathop{\mathrm{Tr}}(\tau^{2k-i}\phi\tau^i) + \mathop{\mathrm{Tr}}(\tau \phi \tau) + \mathop{\mathrm{Tr}}(\phi)\\
                    &=& 0. 
        
\end{aligned}$$ For the even case, $n = 2k$, we have the base case $\Phi^1_\phi(T_2) =   \mathop{\mathrm{Tr}}(\phi\tau) +  \mathop{\mathrm{Tr}}(\tau\phi) = 4q$. Suppose now the result holds for $n=2k$. We show it for $n=2k+2$. As in the previous case we have $$\begin{aligned}
            \Phi^1_\phi(T_{2k+2}) 
            &=&  \sum_{i=0}^{2k+1} \mathop{\mathrm{Tr}}(\tau^{2k-i+1}\phi\tau^i)\\
            &=& \sum_{i=0}^{2k} \mathop{\mathrm{Tr}}(\tau^2\tau^{2k-i+1}\phi\tau^i) + \mathop{\mathrm{Tr}}(\tau \phi \tau^{2k}) + \mathop{\mathrm{Tr}}(\tau^2 \phi \tau^{2k+1})\\
            &=& \sum_{i=0}^{2k} \mathop{\mathrm{Tr}}(\tau^{2k-i+1}\phi\tau^i) + \mathop{\mathrm{Tr}}(\tau \phi) + \mathop{\mathrm{Tr}}(\phi\tau)\\
            &=& 4kq+4q.  
        
\end{aligned}$$ This completes the proof. ◻
:::

Since the invariant of the unknot and unlink are $d$ and $d^2$ where $d$ is the dimension of $V$, we find that the quantum cocycle invariant is nontrivial for this choice of enhanced $2$-cocycle.
