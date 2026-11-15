---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-023-81-principal-flags
section_title: "Principal flags"
section_number: 8.1
pages: 23-25
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.978
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:dis label="sec:dis"}

Let $M \in \mathbb{R}^{n \times n}$ be symmetric. We seek the solution to $$\label{eq:dis}
\begin{tabular}{rl}
maximize & $ \mathop{\mathrm{tr}}(Y^{\scriptscriptstyle\mathsf{T}}MY)$ \\[1ex]
subject to & $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d; n)$.
\end{tabular}$$ Here $Y \in \mathbb{R}^{n \times n_d}$, $Y^{\scriptscriptstyle\mathsf{T}}Y = 1$, and the objective function is well-defined as a function on the flag manifold: If we have $Y$ and $Y'$ with $\llbracket Y \rrbracket= \llbracket Y'\rrbracket$, then they must be related as in [\[eq:rep\]](#eq:rep){reference-type="eqref" reference="eq:rep"} and thus $\mathop{\mathrm{tr}}(Y^{\scriptscriptstyle\mathsf{T}}MY) =  \mathop{\mathrm{tr}}(Y^{\prime{\scriptscriptstyle\mathsf{T}}} MY')$.

As we saw in Example [\[eg:pca\]](#eg:pca){reference-type="ref" reference="eg:pca"}, when $M$ is a sample covariance matrix, the solution to [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} is equivalent to PCA when we seek a complete flag, i.e., $d=n-1$ and $n_i =i$, $i =1,\dots,n-1$. An advantage proffered by this approach is that if we do not know the intrinsic dimension of the data set a priori, then finding the flag as opposed to any particular subspace gives us the entire profile, showing how increasing dimension accounts for an increasingly amount of variance. The problem in [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} is thus a generalization of PCA, allowing us to seek any flag, not necessarily a complete one. It may also be interpreted as finding subspaces of dimensions $n_1,n_2-n_1,\dots,n_d-n_{d-1}$ that are independent and explain different levels of variance in the data set.

Figure [1](#fig:convergence){reference-type="ref" reference="fig:convergence"} shows the convergence trajectories of steepest descent, i.e., Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"}, on the flag manifold $\mathop{\mathrm{Flag}}(3,7,12; 60)$, a $623$-dimensional manifold. The symmetric matrix $M \in \mathbb{R}^{60 \times 60}$ is generated randomly with standard normal entries. Since the true solution of [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} may be determined in closed form --- it is the sum of the $k$ largest eigenvalues of $M$ --- we may therefore conclude that Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} converges to the true solution in around $80$ iterations. Indeed the function values stabilize after as few as $10$ iterations. At least for this problem, we see that the vanishing of the Riemannian gradient serves as a viable stopping condition. In our implementation, our stopping conditions are determined by (i) Frobenius norm of Riemannian gradient, (ii) distance between successive iterates, and (iii) number of iterations.

![Convergence trajectories for [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} on $\mathop{\mathrm{Flag}}(3,7,12; 60)$.](flag1log.pdf){#fig:convergence}

We perform extensive experiments beyond that in Figure [1](#fig:convergence){reference-type="ref" reference="fig:convergence"} by taking average of $100$ instances of the problem [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} for various values of $n_1,\dots,n_d$. We tabulate our results showing accuracy and speed in Tables [1](#table:distdis1){reference-type="ref" reference="table:distdis1"}--[4](#table:timedis2){reference-type="ref" reference="table:timedis2"}. Tables [1](#table:distdis1){reference-type="ref" reference="table:distdis1"} and [3](#table:distdis2){reference-type="ref" reference="table:distdis2"} show that Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} is robust across all dimensions of flags and ambient spaces that we tested. Tables [2](#table:timedis1){reference-type="ref" reference="table:timedis1"} and [4](#table:timedis2){reference-type="ref" reference="table:timedis2"} show that elapsed time taken for Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} increases roughly linearly with the dimension of the flag manifold.

::: {#table:distdis1}
                            $k$    30    40     50     60    70     80     90    100    
  ----------------------------- ----- ----- ------ ------ ----- ------ ------ ------ -- --
    Accuracy ($\times 10^{-4}$)   $2$   $8$   $64$   $32$   $4$   $87$   $20$   $15$    

  : Distance to true solution for [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} on $\mathop{\mathrm{Flag}}(3,9,21;k)$.
:::

::: {#table:timedis1}
             $k$       30       40       50       60       70       80       90      100    
  -------------- -------- -------- -------- -------- -------- -------- -------- -------- -- --
    Elapsed Time   $0.38$   $0.40$   $0.67$   $0.93$   $1.71$   $2.27$   $3.08$   $4.07$    

  : Elapsed time for [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} on $\mathop{\mathrm{Flag}}(3,9,21;k)$.
:::

::: {#table:distdis2}
                            $k$       1       2       3       4       5      6      7       8       9     10    
  ----------------------------- ------- ------- ------- ------- ------- ------ ------ ------- ------- ------ -- --
    Accuracy ($\times 10^{-4}$)   $1.4$   $3.4$   $3.4$   $8.6$   $2.8$   $18$   $19$   $5.1$   $9.3$   $11$    

  : Distance to true solution for [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} on $\mathop{\mathrm{Flag}}(2,\dots,2k;60)$.
:::

::: {#table:timedis2}
             $k$        1        2        3        4        5        6        7        8        9       10    
  -------------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -- --
    Elapsed Time   $0.54$   $0.81$   $0.79$   $0.96$   $1.05$   $0.91$   $1.20$   $1.06$   $1.18$   $1.12$    

  : Elapsed time for [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} on $\mathop{\mathrm{Flag}}(2,\dots,2k;60)$.
:::

::: {#table:distdis3}
                            $k$       1       2       3       4       5      6      7       8       9     10    
  ----------------------------- ------- ------- ------- ------- ------- ------ ------ ------- ------- ------ -- --
    Accuracy ($\times 10^{-4}$)   $1.4$   $3.4$   $3.4$   $8.6$   $2.8$   $18$   $19$   $5.1$   $9.3$   $11$    

  : Distance to true solution for [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} on $\mathop{\mathrm{Flag}}(2,\dots,2k;60)$.
:::
