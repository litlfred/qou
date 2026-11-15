---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-008-72-bayesian-probit-regression
section_title: "Bayesian probit regression"
section_number: 7.2
pages: 19-23
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.986
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
Let $Y_1,Y_2,\dots, Y_n$ be independent Bernoulli random variables with $\mathbb{P}(Y_1=1|\beta) = \Phi(x_i^T\beta),$ where $x_i,\beta
        \in \mathbb{R}^p$, and $\Phi(\cdot)$ is the cumulative distribution function of the standard normal distribution. Take the prior on $\beta$ to be $\mbox{N}_p(Q^{-1}w, Q^{-1}),$ where $w \in \mathbb{R}^p$ and $Q$ is positive definite. The resulting posterior distribution is intractable, but [@albert1993bayesian] devised a DA algorithm to sample from it. Let $z=(z_1,z_2,\dots,z_n)^T$ be a vector of latent variables, and let $X$ be the design matrix whose $i$th row is $x_i^T.$ The Mtd of the Albert and Chib (AC) chain, $p(\beta,\cdot), \beta \in \mathbb{R}^p,$ is characterized by $$\pi_{U|V} (\beta|z) \propto \exp \bigg[ -\frac{1}{2} \big\{
        \beta - \big( X^TX+Q \big)^{-1} \big( w+X^Tz \big) \big\}^T
        \big( X^TX + Q \big) \big\{ \beta - \big( X^TX+Q \big)^{-1}
        \big( w+X^Tz \big) \big\} \bigg] \,,$$ and $$\pi_{V|U}(z|\beta) \propto \prod_{i=1}^{n}\exp \bigg\{
        -\frac{1}{2}\big(z_i-x_i^T\beta\big)^2 \bigg\}
        I_{\mathbb{R}_+}\big((y_i-0.5)z_i \big) \,.$$ The first conditional density, $\pi_{U|V}(\cdot|z)$, is a multivariate normal density, and the second conditional density, $\pi_{V|U}(\cdot|\beta)$, is a product of univariate truncated normal pdfs.

A sandwich step can be added to facilitate the convergence of the AC chain. [@chakraborty2016convergence] constructed a Haar PX-DA variant of the chain, which is a sandwich chain with transition density of the form [\[sandwich\]](#sandwich){reference-type="eqref" reference="sandwich"} (see also [@roy2007convergence]). The sandwich step $s(z, dz')$ is equivalent to the following update: $z \mapsto z' = gz$, where the scalar $g$ is drawn from the following density: $$\pi_G(g|z) \propto g^{n-1} \exp \bigg[ -\frac{1}{2} z^T\big\{ I_n - X(X^TX+Q)^{-1}X^T \big\} z g^2 + z^TX(X^TX + Q)^{-1}w g   \bigg].$$ Note that this pdf is particularly easy to sample from when $w = 0$.

@chakraborty2016convergence showed that, for the AC chain, $P$ is trace-class when one uses a concentrated prior (corresponding to $Q$ having large eigenvalues). In fact, the following is shown to hold in their proof.

::: proposition
[]{#probittrace label="probittrace"} Suppose that $X$ is full rank. If all the eigenvalues of $Q^{-1/2}X^TXQ^{-1/2}$ are less than $7/2,$ then for any polynomial function $t:
          \mathbb{R}^p \to \mathbb{R}$, $$\int_{\mathbb{R}^p} |t(\beta)| p(\beta,\beta) \,
                d\beta < \infty \,.$$
:::

We will use the estimator [\[estimator2\]](#estimator2){reference-type="eqref" reference="estimator2"}. The following proposition provides a class of $\psi(\cdot)$s that lead to estimators with finite variance.

::: proposition
[]{#probitpsi label="probitpsi"} Suppose the hypothesis in Proposition [\[probittrace\]](#probittrace){reference-type="ref" reference="probittrace"} holds. If $\psi(\cdot)$ is the pdf of a $p$-variate $t$-distribution, i.e. $$\psi(\beta) \propto \bigg\{ 1 + \frac{1}{a}(\beta - b)^T \Sigma^{-1}  (\beta - b) \bigg\}^{-(a+p)/2}$$ for some $b \in \mathbb{R}^p,$ positive definite matrix $\Sigma \in \mathbb{R}^{p \times p},$ and positive integer $a,$ then the estimator [\[estimator2\]](#estimator2){reference-type="eqref" reference="estimator2"} has finite variance.
:::

::: proof
*Proof.* Note that for every $\beta$ and $z$ $$\pi^3_{U|V} (\beta|z) \leq C \pi_{U|V} (\beta|z) \,,$$ where $C$ is a constant. Hence, by Proposition [\[probittrace\]](#probittrace){reference-type="ref" reference="probittrace"}, for any polynomial function $t: \mathbb{R}^p \to \mathbb{R},$ $$\int_{\mathbb{R}^p} \int_{\mathbb{R}^n} |t(\beta)|
                \pi^3_{U|V} (\beta|z) \pi_{V|U} (z|\beta) \,
                dz\,d\beta \leq C\int_{\mathbb{R}^p} |t(\beta)|
                p(\beta,\beta) \, d\beta < \infty.$$ Since $\psi^{-2}(\cdot)$ is a polynomial function on $\mathbb{R}^p$, the moment condition [\[momentconddual\]](#momentconddual){reference-type="eqref" reference="momentconddual"} holds. The result follows from Corollary [\[secondmomentdual\]](#secondmomentdual){reference-type="ref" reference="secondmomentdual"}. ◻
:::

As a numerical illustration, we apply our method to the Markov operator associated with the AC chain corresponding to the famous "lupus data" of [@van2001art]. In this dataset, $n=55$ and $p=3$. We will construct an asymptotically valid 95% CI for the second largest eigenvalue, and this appears to be the most rigorous and detailed analysis to date of the spectrum of a practically relevant MCMC algorithm on an uncountable state space. As in [@chakraborty2016convergence], we will let $w=0$ and $Q=X^TX/c$, where $c=3.499999$. It can be easily shown that the assumptions in Proposition [\[probittrace\]](#probittrace){reference-type="ref" reference="probittrace"} are met. [@chakraborty2016convergence] compared the AC chain, $\Phi$, and its Haar PX-DA variant, $\tilde{\Phi}$, defined a few paragraphs ago. This comparison was done using estimated autocorrelations. Their results suggest that $\tilde{\Phi}$ outperforms $\Phi$ when estimating a certain test function. We go further and estimate the second largest eigenvalue of each operator.

It can be shown that the posterior pdf, $\pi_{U}(\cdot)$, is log-concave, and thus possess a unique mode. Let $\hat{\beta}$ be the posterior mode, and $\hat{\Sigma}$ the estimated variance of the MLE. We pick $\psi(\cdot)$ to be the pdf of $t_{30}(\hat{\beta},(\hat{\Sigma}^{-1}+Q)^{-1}).$ This is to say, for any $\beta \in \mathbb{R}^p,$ $$\psi(\beta) \propto \Big\{ 1 + \frac{1}{30} (\beta-\hat{\beta})^T (\hat{\Sigma}^{-1}+Q) (\beta-\hat{\beta}) \Big\}^{-(p+30)/2}.$$ By Proposition [\[probitpsi\]](#probitpsi){reference-type="ref" reference="probitpsi"}, this choice of $\psi(\cdot)$ guarantees finite variance. When $n$ is large, $\psi(\cdot)$ is expected to resemble $\pi_U(\cdot)$. The performance of our method seems insensitive to the degrees of freedom of the $t$-distribution (which is set at 30 for illustration).

We use a Monte Carlo sample size of $N = 4\times 10^5$ to form our estimates for the DA operator, and the results are shown in Table [1](#probit){reference-type="ref" reference="probit"}. Asymptotic $95\%$ CIs for $l_5$ and $u_5$ are $(0.397,0.545)$ and $(0.573,0.595)$, respectively. Using a Bonferroni argument, we can state that asymptotically, with at least $95\%$ confidence, $\lambda_1
        \in (0.397, 0.595)$.

::: center
::: {#probit}
   $k$   Est. $s_k$   Est. $D'/\sqrt{N}$   Est. $l_k$   Est. $u_k$
  ----- ------------ -------------------- ------------ ------------
   $1$    $6.744$          $0.072$          $0.000$      $5.744$
   $2$    $2.041$          $0.007$          $0.181$      $1.020$
   $3$    $1.363$          $0.004$          $0.349$      $0.713$
   $4$    $1.156$          $0.004$          $0.430$      $0.628$
   $5$    $1.068$          $0.003$          $0.436$      $0.584$

  : Estimated power sums of eigenvalues for the AC chain
:::
:::

::: center
::: {#probit2}
   $k$   Est. $\tilde{s}_k$   Est. $D'/\sqrt{N}$   Est. $\tilde{l}_k$   Est. $\tilde{u}_k$
  ----- -------------------- -------------------- -------------------- --------------------
   $1$        $3.796$              $0.012$              $0.000$              $1.796$
   $2$        $1.538$              $0.004$              $0.193$              $0.734$
   $3$        $1.172$              $0.004$              $0.319$              $0.556$
   $4$        $1.060$              $0.003$              $0.352$              $0.496$
   $5$        $1.025$              $0.003$              $0.419$              $0.479$

  : Estimated power sums of eigenvalues for the Haar PX-DA version of the AC chain
:::
:::

We now consider the sandwich chain, $\tilde{\Phi}$. It is known that the Mtd of any Haar PX-DA chain is representable [@hobert2008theoretical]. Hence, $\tilde{P}$ is indeed a DA operator. Recall that $\{\tilde{\lambda}_i\}_{i=0}^{\tilde{\kappa}}, \, 0 \leq
        \tilde{\kappa} \leq \infty$, denote the decreasingly ordered positive eigenvalues of $\tilde{P}$. It was shown in [@khare2011spectral] that $\tilde{\lambda}_i \leq
        \lambda_i$ for $i \in \mathbb{N}$ with at least one strict inequality. For a positive integer $k,$ $\sum_{i=0}^{\tilde{\kappa}}
        \tilde{\lambda}_i^k$ is denoted by $\tilde{s}_k$. Let $\tilde{u}_k$ and $\tilde{l}_k,$ be the respective counterparts of $u_k$ and $l_k$. Estimates of $\tilde{s}_k,\,k=1,2,\cdots,5$ using $4\times 10^5$ Monte Carlo samples are given in Table [2](#probit2){reference-type="ref" reference="probit2"}. Our estimate of $\tilde{s}_1-1$ is less than half of $s_1-1$, implying that, in an average sense, the sandwich version of the AC chain reduces the nontrivial eigenvalues of $P$ by more than half. Asymptotic $95\%$ CIs for $\tilde{l}_5$ and $\tilde{u}_5$ are $(0.321, 0.518)$ and $(0.456,0.503)$. Thus, asymptotically, with at least $95\%$ confidence, $\tilde{\lambda}_1 \in (0.321,0.503)$. The method does not detect a significant difference between $\lambda_1$ and $\tilde{\lambda}_1$.

<figure id="fig:ProbitGrowingP">
<figure id="fig:ProbitGrowingN">
<img src="ProbitGrowingN" />
<figcaption>Interval estimates for <span class="math inline"><em>λ</em><sub>1</sub></span> for different <span class="math inline"><em>n</em></span>s.</figcaption>
</figure>
<figure id="fig:ProbitGrowingP">
<img src="ProbitGrowingP" />
<figcaption>Interval estimates for <span class="math inline"><em>λ</em><sub>1</sub></span> for different <span class="math inline"><em>p</em></span>s.</figcaption>
</figure>
<figcaption>Spectral gap estimation for the AC chain</figcaption>
</figure>

We now study the performance of our method when $n$ or $p$ increases for the original AC chain. First, consider a sequence of datasets where $n$ grows. Let $X_{\scriptsize\mbox{lupus}} \in \mathbb{R}^{55 \times 3}$ be the design matrix for the lupus data, and let $r$ be a positive integer. Set $X \in \mathbb{R}^{n \times 3}$ to be $r$ copies of $X_{\scriptsize\mbox{lupus}}$ stacked on top of each other, so that $n=55r$. The response vector $(Y_1,Y_2,\dots,Y_n)^T$ is randomly generated in accordance with the probit regression model with the true value of $\beta$ being $(-3,0,3)^T$. Let $r$ range from $1$ to $15$. This gives rise to a sequence of datasets with $n$ growing from $55$ to $825$. An interval estimate for $\lambda_1$ is then constructed for each of these datasets. Throughout the simulation, $k$ is fixed at $5$, and $N$ is fixed at $4 \times 10^5$. The result is given in Figure [1](#fig:ProbitGrowingN){reference-type="ref" reference="fig:ProbitGrowingN"}. Increasing $n$, which is the dimension of $S_V$, apparently does not undermine the method.

Now we consider a sequence of datasets where $n$ is fixed and $p$ grows. Let $n=200$, and let $X$ be a $200 \times p$ matrix whose $ij$th element is $p_j(i)$, with $\{p_j(\cdot)\}_{j=1}^p$ being a set of orthogonal polynomials generated using the `R` function `poly()`. The response vector is randomly generated according to the probit model with the true value of $\beta$ being $(-p, -p+2p/(1-p), -p + 4p/(1-p), \cdots, p)^T$. We apply our method to such a dataset when $p$ is increased from $3$ to $15$. $N$ is set to be $4\times 10^5$, and $k$ is either $4$ or $5$, whichever yields a better estimate. The interval estimates for $\lambda_1$ are given in Figure [3](#fig:ProbitGrowingP){reference-type="ref" reference="fig:ProbitGrowingP"}. As $p$ increases, the length of the interval estimate grows quite rapidly, indicating that the method does not scale well with $p$, that is, the dimension of $S_U$. This is consistent with the analysis near the end of Section [\[MC\]](#MC){reference-type="ref" reference="MC"}, which suggests that Algorithm 2 works well when $n$ is large and $p$ is small, but not the other way around.
