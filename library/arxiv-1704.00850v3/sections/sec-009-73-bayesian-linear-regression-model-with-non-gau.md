---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-009-73-bayesian-linear-regression-model-with-non-gau
section_title: "Bayesian linear regression model with non-Gaussian errors"
section_number: 7.3
pages: 23-26
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.984
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
Let $Y_1,Y_2,\dots,Y_n$ be independent $d$-dimensional random vectors from the linear regression model $$Y_i = \beta^T x_i + \Sigma^{1/2}\varepsilon_i \,,$$ where $x_i \in \mathbb{R}^{p}$ is known, while $\beta \in
    \mathbb{R}^{p \times d}$ and the $d\times d$ positive definite matrix $\Sigma$ are to be estimated. The iid errors, $\varepsilon_1,\varepsilon_2,\dots,\varepsilon_n$, are assumed to have a pdf that is a scale mixture of Gaussian densities: $$f_h(\varepsilon) = \int_{\mathbb{R}_+} \frac{u^{d/2}}{(2\pi)^{d/2}} \exp \Big( -\frac{u}{2} \varepsilon^T\varepsilon \Big) h(u) \, du,$$ where $h(\cdot)$ is a pdf with positive support, and $\mathbb{R}_+ := (0,\infty).$ For instance, if $d=1$ and $h(u)
    \propto u^{-2}e^{-1/(8u)},$ then $\varepsilon_1$ has pdf proportional to $e^{-|\varepsilon|/2}.$

To perform a Bayesian analysis, we require a prior on the unknown parameter, $(\beta,\Sigma)$. We adopt the (improper) Jeffreys prior, given by $1/|\Sigma|^{(d+1)/2}$. Let $y$ represent the $n \times d$ matrix whose $i$th row is the observed value of $Y_i$. The following four conditions, which are sufficient for the resulting posterior to be proper [@qin2018trace; @fernandez1999multivariate], will be assumed to hold:

1.  $n \geq p + d$,

2.  $(X:y)$ is full rank, where $X$ is the $n\times
            p$ matrix whose $i$th row is $x_i^T$,

3.  $\int_{\mathbb{R}_+} u^{d/2} h(u) \, du < \infty$, and

4.  $\int_{\mathbb{R}_+} u^{-(n-p-d)/2} h(u) \, du < \infty$.

The posterior density is highly intractable, but there is a well-known DA algorithm to sample from it [@liu1996bayesian]. Under our framework, the DA chain $\Phi$ is characterized by the Mtd $$p\big((\beta,\Sigma),(\cdot,\cdot) \big) = \int_{\mathbb{R}_+^n} \pi_{U|V}(\cdot,\cdot| z) \pi_{V|U}(z|\beta,\Sigma) \, dz,$$ where $z=(z_1,z_2,\dots,z_n)^T$, $$\begin{aligned}
    \pi_{U|V}(\beta,\Sigma|z) & \propto |\Sigma|^{-(n+d+1)/2} \prod_{i=1}^{n}\exp \Big\{ -\frac{z_i}{2} \big(y_i-\beta^Tx_i \big)^T \Sigma^{-1} \big(y_i-\beta^Tx_i \big) \Big\}, \, \mbox{and} \\
    \pi_{V|U}(z|\beta,\Sigma) & \propto \prod_{i=1}^{n}
    z_i^{d/2} \exp \Big\{ -\frac{z_i}{2} \big(y_i-\beta^Tx_i
    \big)^T \Sigma^{-1} \big(y_i-\beta^Tx_i \big) \Big\} h(z_i)
    \,.
    \end{aligned}$$ The first conditional density, $\pi_{U|V}(\cdot,\cdot|z)$, characterizes a multivariate normal distribution on top of an inverse Wishart distribution, i.e. $\beta|\Sigma,z$ is multivariate normal, and $\Sigma|z$ is inverse Wishart. The second conditional density, $\pi_{V|U}(\cdot|\beta,\Sigma)$, is a product of $n$ univariate densities. Moreover, when $h(\cdot)$ is a standard pdf on $\mathbb{R}_+$, these univariate densities are often members of a standard parametric family. The following proposition about the resulting DA operator is proved in [@qin2018trace].

::: proposition
[]{#nongaussian label="nongaussian"} Suppose $h(\cdot)$ is strictly positive in a neighborhood of the origin. If there exists $\xi \in (1,2)$ and $\delta>0$ such that $$\int_{0}^{\delta} \frac{u^{d/2}h(u)}{\int_{0}^{\xi u} v^{d/2} h(v) \, dv} \, du < \infty,$$ then $P$ is trace-class.
:::

When $P$ is trace-class, we can pick an $\omega(\cdot)$ and try to make use of [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"}. A sufficient condition for the estimator's variance, $D^2$, to be finite is stated in the following proposition, whose proof is given in the appendix.

::: proposition
[]{#nongaussianmoment label="nongaussianmoment"} Suppose that $h(\cdot)$ is strictly positive in a neighborhood of the origin. If $\omega(z)$ can be written as $\prod_{i=1}^{n}
        \omega_i(z_i),$ and there exists $\xi \in (1,4/3)$ such that for all $i \in \{1,2,\dots,n\},$ $$\label{nongaussianomega}
        \int_{\mathbb{R}_+} \frac{u^{3d/2}h^3(u)} {(\int_{0}^{\xi u} v^{d/2}h(v) \, dv)^3 \omega_i^2(u) } \, du < \infty,$$ then [\[momentcond\]](#momentcond){reference-type="eqref" reference="momentcond"} holds, and thus by Theorem [\[secondmoment\]](#secondmoment){reference-type="ref" reference="secondmoment"}, the estimator [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"} has finite variance.
:::

For illustration, take $d=1$ and $h(u) \propto
    u^{-2}e^{-1/(8u)}$. Then $\varepsilon_1$ follows a scaled Laplace distribution, and the model can be viewed as a median regression model with variance $\Sigma$ unknown. It's easy to show that $h(\cdot)$ satisfies the assumptions in Proposition [\[nongaussian\]](#nongaussian){reference-type="ref" reference="nongaussian"}, so the resultant DA operator is trace-class. Now let $$\omega(z) = \prod_{i=1}^{n} \omega_i(z_i) \propto
    \prod_{i=1}^{n} z_i^{-3/2} e^{-1/(32z_i)} \,.$$ The following result shows that this will lead to an estimator with finite variance.

::: corollary
Suppose $d=1$, $h(u) \propto u^{-2}e^{-1/(8u)}$, and $$\omega(z) = \prod_{i=1}^{n} \omega_i(z_i) \propto
        \prod_{i=1}^{n} z_i^{-\alpha-1} e^{-\gamma/z_i} \,,$$ where $0 < \alpha < 3/4$ and $0 < \gamma < 3/64$. Then the variance, $D^2$, is finite.
:::

::: proof
*Proof.* In light of Proposition [\[nongaussianmoment\]](#nongaussianmoment){reference-type="ref" reference="nongaussianmoment"}, we only need to show that [\[nongaussianomega\]](#nongaussianomega){reference-type="eqref" reference="nongaussianomega"} holds for some $\xi \in (1,4/3).$ For any $\xi > 0,$ making use of the fact that (by monotone convergence theorem) $$\lim\limits_{u \to \infty} \int_{0}^{\xi u}
        v^{1/2}h(v) \, dv = \int_{\mathbb{R}_+} u^{1/2} h(u)
        \, du > 0 \,,$$ one can easily show for any $\delta > 0$, $$\label{inftyend}
        \int_{\delta}^{\infty} \frac{u^{3/2}h^3(u)} {(\int_{0}^{\xi u} v^{1/2}h(v) \, dv)^3 \omega_i^2(u) } \, du = \int_{\delta}^{\infty} \frac{u^{2\alpha-5/2}\exp\{ 2\gamma/u-3/(8u) \} } {(\int_{0}^{\xi u} v^{1/2}h(v) \, dv)^3} \, du < \infty.$$ On the other hand, using L'Hôpital's rule, we can see for $(1-16\gamma/3)^{-1} < \xi < 4/3,$ $$\begin{aligned}
        \lim\limits_{u \to 0} \Bigg( \frac{u^{3/2}h^3(u)} {(\int_{0}^{\xi u} v^{1/2}h(v) \, dv)^3 \omega_i^2(u) } \Bigg)^{1/3} &= \lim\limits_{u \to 0} \frac{u^{2\alpha/3-5/6} \exp\{ 2\gamma/(3u)-1/(8u) \}}{ \int_{0}^{\xi u} v^{-3/2}e^{-1/(8v)}\, dv } \\
        &= \lim\limits_{u \to 0} R(u) \exp \Big\{ -\Big(-\frac{2\gamma}{3} - \frac{1}{8\xi} + \frac{1}{8} \Big)\frac{1}{u} \Big\} \\
        & = 0,
        \end{aligned}$$ where $R(u)$ is a function that is either bounded near the origin or goes to $\infty$ at the rate of some power function as $u \to 0.$ It follows that for $\xi \in ((1-16\gamma/3)^{-1}, 4/3)$ and small enough $\delta,$ $$\label{origend}
        \int_{0}^{\delta} \frac{u^{3/2}h^3(u)} {(\int_{0}^{\xi u} v^{1/2}h(v) \, dv)^3 \omega_i^2(u) } \, du < \infty.$$ Combining [\[inftyend\]](#inftyend){reference-type="eqref" reference="inftyend"} and [\[origend\]](#origend){reference-type="eqref" reference="origend"} yields [\[nongaussianomega\]](#nongaussianomega){reference-type="eqref" reference="nongaussianomega"}. The result then follows. ◻
:::

<figure id="fig:GrowingP">
<figure id="fig:GrowingN">
<img src="GrowingN" />
<figcaption>Interval estimates for <span class="math inline"><em>λ</em><sub>1</sub></span> for different <span class="math inline"><em>n</em></span>s.</figcaption>
</figure>
<figure id="fig:GrowingP">
<img src="GrowingP" />
<figcaption>Interval estimates for <span class="math inline"><em>λ</em><sub>1</sub></span> for different <span class="math inline"><em>p</em></span>s.</figcaption>
</figure>
<figcaption>Spectral gap estimation for the DA chain for Bayesian linear model</figcaption>
</figure>

We now test the effectiveness of the Monte Carlo estimator [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"} on a sequence of growing datasets with $d=1$. Let $p=3$, and let $X$ be an $n \times p$ design matrix with 3 distinct rows, $(1,0,0)^T$, $(0,1,0)^T$, and $(0,0,1)^T$, each replicated $r$ times, so that $n = 3r$. The responses, $Y_1,Y_2,\cdots,Y_n$, are then generated according to the previously defined linear regression model with the true value of $\beta$ being $(-3,0,3)^T$, and the true value of $\Sigma$ being $1$. In other words, $Y_i - x_i^T (-3,0,3)^T \sim f_h(\cdot)$ independently for each $i$, where $f_h(u) \propto e^{-|u|/2}$. The resultant DA chain $\Phi$ lives in $S_U = \mathbb{R}^3 \times \mathbb{R}_+$, and $S_V = \mathbb{R}^n = \mathbb{R}^{3r}$. Let $r$ grow from $2$ to $6$. We use a Monte Carlo sample size of $N = 2 \times 10^6$ to form interval estimates of $\lambda_1$ for different values of $r$. For simplicity, we fix $k$ to be $4$. The results are given in Figure [1](#fig:GrowingN){reference-type="ref" reference="fig:GrowingN"}. As $n$ grows, the length of the interval estimate increases quite rapidly. This is understandable, since our method is essentially an importance sampling technique, which does not work well in high dimensional settings unless tuned with great care. In the previous subsection where we study Bayesian probit regression, we are able to easily deal with a dataset with $n>800$. Part of the reason is that, in that case, Algorithm 2 is used, and since $S_U$ is low dimensional, it's easy to choose $\psi(\cdot)$ that resembles $\pi_U(\cdot)$.

Consider another sequence of datasets where $d=1$, $n=10$, and $p$ is increased from $1$ to $8$. The $ij$th element of the design matrix $X$ is set to be $p_j(i)$, where $\{p_j(\cdot)\}_{j=1}^p$ are orthogonal polynomials generated in `R`. The responses are generated according to the aforementioned linear regression model with the true value of $\beta$ being $(-p, p+2p/(1-p), -p + 4p/(1-p), \dots, p)^T$, and the true value of $\Sigma$ being $1$. In this case, $S_U = \mathbb{R}^p \times \mathbb{R}_+$, and $S_V = \mathbb{R}^{10}$. Using a Monte Carlo sample size of $N=2 \times 10^6$ and setting $k=4$, we obtain interval estimates of $\lambda_1$ for different $p$s. The results are given in Figure [3](#fig:GrowingP){reference-type="ref" reference="fig:GrowingP"}. Compare this to the case where $p$ is fixed an $n$ grows. We see that the effectiveness of Algorithm 1, characterized by the length of the interval estimate it produces, is much less susceptible to the growing dimension of $S_U$ than to that of $S_V$.

. The second and third authors were supported by NSF Grant DMS-15-11945.
