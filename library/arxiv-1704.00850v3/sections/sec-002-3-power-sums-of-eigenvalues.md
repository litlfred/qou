---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-002-3-power-sums-of-eigenvalues
section_title: "Power sums of eigenvalues"
section_number: 3
pages: 5-7
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.992
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
[]{#powersum label="powersum"}

We now develop some results relating $\lambda_1$ to the power sum of $P$'s eigenvalues. We assume throughout this section that $P$ is non-negative and trace-class (compact with summable eigenvalues). For any positive integer $k$, let $$s_k = \sum_{i=0}^{\kappa} \lambda_i^k \,,$$ and define $s_0$ to be infinity. The first power sum, $s_1$, is the trace norm of $P$ [see e.g. @conway1990course; @conway2000course], while $\sqrt{s_2}$ is the Hilbert-Schmidt norm of $P.$ That $P$ is trace-class implies $s_1 < \infty,$ and it's clear that $s_k$ is decreasing in $k.$

The magnitude of $s_k$ is directly related to the convergence behavior of the chain. For instance, suppose that the chain starts at a point mass $\Phi_0 = u$, then the chi-square distance between the distribution of $\Phi_k$ and the stationary distribution is given by [see e.g. @diaconis2008gibbs] $$\chi_k^2(u) := \int_{S_U} \frac{\left(p^{(k)}(u,u') - \pi(u') \right)^2}{\pi(u')} \, \mu(du') =  \sum_{i=1}^{\kappa} \lambda_i^{2k} |f_i(u)|^2,$$ where $f_i: S_U \to \mathbb{C}$ is the normalized eigenfunction corresponding to $\lambda_i$. It follows that $$s_{2k} = \sum_{i=1}^{\kappa} \lambda_i^{2k} = \int_{S_U} \chi_k^2(u) \pi(u) \, \mu(du),$$ which is the average of $\chi_k^2(u)$ under $\pi.$ More importantly, one can use functions of $s_k$ to bound $\lambda_1,$ and thus the spectral gap.

Observe that, $$\lambda_1 \leq u_k := (s_k-1)^{1/k},\quad
          \forall \, k \in \mathbb{N} \,.$$ Moreover, if $\kappa \geq 1,$ then it's easy to show that $$\lambda_1 \geq l_k :=
          \frac{s_k-1}{s_{k-1}-1}, \quad \forall \, k \in \mathbb{N}
          \,.$$ We now show that, in fact, these bounds are monotone in $k$ and converge to $\lambda_1$.

::: proposition
[]{#eigenlim label="eigenlim"} As $k \to \infty$, $$\label{uklim}
        u_k \downarrow \lambda_1 \,,$$ and if furthermore $\kappa \geq 1,$ $$\label{lklim}
        l_k \uparrow \lambda_1 \,.$$
:::

::: proof
*Proof.* We begin with [\[uklim\]](#uklim){reference-type="eqref" reference="uklim"}. When $\kappa = 0,$ $s_k \equiv
          1$ and the conclusion follows. Suppose $\kappa \geq 1,$ and that the second largest eigenvalue is of multiplicity $m,$ i.e. $$1 = \lambda_0 > \lambda_1 = \lambda_2 = \dots =
                \lambda_m > \lambda_{m+1} \geq \dots \geq
                \lambda_{\kappa} > 0.$$ If $\kappa = m$, then $s_k - 1 = m\lambda_1^k$ for all $k\geq 1$ and the proof is trivial. Suppose for the rest of the proof that $\kappa \geq m+1.$ For positive integer $k,$ let $r_k = \sum_{i=m+1}^{\kappa}
                \lambda_i^k < \infty.$ Then $r_k > 0,$ and $$\frac{r_{k+1}}{r_k} \leq \lambda_{m+1} < \lambda_1 \,.$$ Hence, $$\lim\limits_{k \to \infty} \frac{r_k}{s_k-1-r_k} =
                \lim\limits_{k \to \infty} \frac{r_k}{m\lambda_1^k}
                \leq \lim\limits_{k \to \infty}
                \frac{r_1\lambda_{m+1}^{k-1}}{m\lambda_1^k} = 0 \,.$$ It follows that $$\log u_k = \log \lambda_1 + \frac{1}{k}\log m +
                \frac{1}{k} \log (1+o(1)) \to \log \lambda_1 \,.$$ Finally, $$u_{k+1} < \lambda_1^{1/(k+1)} \Big(
                \sum_{i=1}^{\kappa} \lambda_i^k \Big)^{1/(k+1)} \leq
                \Big( \sum_{i=1}^{\kappa} \lambda_i^k
                \Big)^{1/[k(k+1)]} \Big( \sum_{i=1}^{\kappa}
                \lambda_i^k \Big)^{1/(k+1)} = u_k \,,$$ and [\[uklim\]](#uklim){reference-type="eqref" reference="uklim"} follows.

Now onto [\[lklim\]](#lklim){reference-type="eqref" reference="lklim"}. We have already shown that $$s_k - 1 = m\lambda_1^k(1+o(1)) \,.$$ Thus, $$l_k =
                \frac{m\lambda_1^k(1+o(1))}{m\lambda_1^{k-1}(1+o(1))}
                \to \lambda_1 \,.$$ To show that $l_k$ is increasing in $k$, which would complete the proof, we only need note that $$\begin{aligned}
                  (s_{k+1}-1)(s_{k-1}-1) &= \sum_{i=1}^{\kappa} \lambda_i^{k+1} \sum_{j=1}^{\kappa} \lambda_j^{k-1} \\
                  &= \frac{1}{2}\sum_{i=1}^{\kappa} \sum_{j=1}^{\kappa} \lambda_i^{k-1}\lambda_j^{k-1} (\lambda_i^2 + \lambda_j^2) \\
                  & \geq \sum_{i=1}^{\kappa} \sum_{j=1}^{\kappa} \lambda_i^{k}\lambda_j^{k} \\
                  &= (s_k-1)^2 \,.
        \end{aligned}$$ ◻
:::

Suppose now that we are interested in the convergence behavior of a particular Markov operator that is known to be non-negative and trace-class. If it is possible to estimate $s_k$, then Proposition [\[eigenlim\]](#eigenlim){reference-type="ref" reference="eigenlim"} provides a method of getting approximate bounds on $\lambda_1$. When a DA Markov operator is trace-class, there is a nice integral representation of $s_k$ that leads to a simple, classical Monte Carlo estimator of $s_k$. In the following section, we describe some theory for DA Markov operators, and in Section [\[MC\]](#MC){reference-type="ref" reference="MC"}, we develop a classical Monte Carlo estimator of $s_k$.
