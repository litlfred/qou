---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-014-8-numerical-experiments
section_title: "Numerical experiments"
section_number: 8
pages: 23-26
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.937
---
[]{#sec:num label="sec:num"}

We will test our algorithm for steepest descent on the flag manifold numerically. As we explained in Section [\[sec:cg\]](#sec:cg){reference-type="ref" reference="sec:cg"}, the experiments for conjugate gradient algorithm is more involved and is deferred to [@next]. We run our numerical experiments on two problems: (i) the principal flag problem in Section [0.1](#sec:dis){reference-type="ref" reference="sec:dis"} is one for which the solution may be determined in closed-form analytically, and thus it serves to demonstrate the correctness of our algorithm, i.e., converges to the true solution; (ii) a variation of the previous problem with a more complicated objective function to show that the convergence behavior remains unchanged. In addition, neither problem can be solved by simply treating them as nonlinear optimization problems with equality constraints and applying standard nonlinear optimization algorithms.

In the following we will assume the identification in [\[eq:identify\]](#eq:identify){reference-type="eqref" reference="eq:identify"} and use Stiefel coordinates throughout.

## Principal flags {#sec:dis}

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

## Nonlinear eigenflags {#sec:disv}

This is a variation of the principal flag problem [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"}: $$\label{eq:eig}
\begin{tabular}{rl}
maximize & $\sum_{i=1}^{d}\mathop{\mathrm{tr}}(Y_i^{\scriptscriptstyle\mathsf{T}}MY_i)^2$\\[1ex]
subject to & $\llbracket Y_1,\dots,Y_d \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d; n)$.
\end{tabular}$$ Again $M \in \mathbb{R}^{n \times n}$ is a symmetric matrix and the flag is given in Stiefel coordinates $Y = [Y_1,\dots,Y_d] \in \mathbb{R}^{n \times n_d}$, $Y^{\scriptscriptstyle\mathsf{T}}Y = I$, but partitioned into submatrices $Y_i \in \mathbb{R}^{n \times (n_i - n_{i-1})}$, $Y_i^{\scriptscriptstyle\mathsf{T}}Y_i = I$, $i =1,\dots,d$. More generally, the objective function in [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} may be replaced by $\sum_{i=1}^{d}f_i\bigl(\mathop{\mathrm{tr}}(Y_i^{\scriptscriptstyle\mathsf{T}}M Y_i)\bigr)$ with $f_1,\dots,f_d \in C^2(\mathbb{R})$. Choosing $f_1(x) = \dots = f_d(x) = x$ gives us [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} and choosing $f_1(x) = \dots = f_d(x) = x^2$ gives us [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"}. Note that it will take considerable effort to formulate a problem like [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} as a constrained optimization problem in Euclidean space.

![Convergence trajectories for [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} on $\mathop{\mathrm{Flag}}(3,7,12; 60)$.](flag2log.pdf){#fig:convergence2}

The convergence trajectories for Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} applied to [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} are shown in Figure [2](#fig:convergence2){reference-type="ref" reference="fig:convergence2"}. The nonlinearity imposes a cost --- it takes around $390$ iterations to satisfy one of the our stopping criteria, although the function values stabilize after around $60$ iterations. The jagged spikes seen in Figure [2](#fig:convergence2){reference-type="ref" reference="fig:convergence2"} are a result of iterates moving along a geodesic and then jumping to another geodesic. So this is indicative of steepest descent following a path that comprises multiple geodesics. A caveat is that unlike the principal flag problem [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"}, we do not have a closed-form solution for [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} and thus we may only guarantee convergence to a local minimizer, which is reflected in Figure [2](#fig:convergence2){reference-type="ref" reference="fig:convergence2"}.
