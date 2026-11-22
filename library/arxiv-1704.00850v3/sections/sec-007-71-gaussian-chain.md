---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-007-71-gaussian-chain
section_title: "Gaussian chain"
section_number: 7.1
pages: 17-19
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.994
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
We begin with a toy example. Let $S_U=S_V=\mathbb{R},$ $\pi_U(u) \propto \exp(-u^2),$ and $$\pi_{V|U}(v|u) \propto \exp \Big\{ -4\Big(v-\frac{u}{2}\Big)^2
        \Big\} \,.$$ Then $$\pi_{U|V} (u|v) \propto \exp \{ -2(u-v)^2 \} \,.$$ This leads to one of the simplest DA chains known. Indeed, the Mtd, $$p(u,\cdot) = \int_{\mathbb{R}} \pi_{U|V}(\cdot|v)
        \pi_{V|U}(v|u) \, dv \,, \; u \in S_U \,,$$ can be evaluated in closed form, and turns out to be a normal pdf. The spectrum of the corresponding Markov operator, $P$, has been studied thoroughly [see e.g. @diaconis2008gibbs]. It is easy to verify that [\[traceclass\]](#traceclass){reference-type="eqref" reference="traceclass"} holds, so $P$ is trace-class. In fact, $\kappa = \infty$, and for any non-negative integer $i,$ $\lambda_i = 1/2^i$. Thus, the second largest eigenvalue, $\lambda_1$, and the spectral gap, $\delta$, are both equal to $1/2$. Moreover, for any positive integer $k$, $$s_k = \sum_{i=0}^{\infty} \frac{1}{2^{ik}} =
        \frac{1}{1-2^{-k}} \,.$$

We now pretend to be unaware of this spectral information, and use [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"} to estimate $\{s_k,l_k,u_k\}_{k=1}^4$. Recall that $l_k$ and $u_k$ are lower and upper bounds for $\lambda_1$, respectively. Note that $$\int_{\mathbb{R}} \pi^3_{V|U}(v|u) \pi_{U|V} (u|v) \, du
        \propto \exp \Big( -\frac{6}{5}v^2 \Big) \,.$$ It follows that, if we take $\omega(v) \propto \exp(-v^2/2)$, then [\[momentcond\]](#momentcond){reference-type="eqref" reference="momentcond"} holds, and our estimator of $s_k$ has finite variance. We use a Monte Carlo sample size of $N = 1
        \times 10^5$ to form our estimates, and the results are shown in Table [1](#gaussian){reference-type="ref" reference="gaussian"}.

::: center
::: {#gaussian}
   $k$   Est. $s_k$   Est. $D/\sqrt{N}$   Est. $l_k$   Est. $u_k$
  ----- ------------ ------------------- ------------ ------------
   $1$    $1.996$          $0.004$         $0.000$      $0.996$
   $2$    $1.331$          $0.004$         $0.333$      $0.575$
   $3$    $1.142$          $0.004$         $0.429$      $0.522$
   $4$    $1.068$          $0.004$         $0.482$      $0.511$

  : Estimated power sums of eigenvalues for the Gaussian chain
:::
:::

Note that the estimates of the $s_k$s are quite good. We then construct $95\%$ confidence intervals (CIs) for $l_4$ and $u_4$ via the delta method, and the results are $(0.442,0.522)$ and $(0.498,0.524)$, respectively.

<figure id="fig:ClosingSpectralGap">
<figure id="fig:ClosingSpectralGap0">
<img src="ClosingSpectralGap0" />
<figcaption>The <span class="math inline"><em>k</em></span>s used for different values of <span class="math inline"><em>λ</em></span>. </figcaption>
</figure>
<figure id="fig:ClosingSpectralGap">
<img src="ClosingSpectralGap" />
<figcaption>Interval estimates for <span class="math inline"><em>λ</em><sub>1</sub></span>.</figcaption>
</figure>
<figcaption>Spectral gap estimation for the Gaussian chain for different <span class="math inline"><em>λ</em></span>s</figcaption>
</figure>

We now add an additional parameter to our toy example in order to study the effect of a closing spectral gap on our method. In particular, let $\pi_{V|U}(\cdot|u)$, $u \in \mathbb{R}$, be the pdf of $\mbox{N}(\lambda u, \lambda(1-\lambda)/2)$, where $\lambda \in (0,1)$. Note that our original example corresponds to $\lambda=1/2$. The eigenvalues of the resultant DA operator are $\{\lambda_i\}_{i=0}^{\infty} = \{\lambda^i\}_{i=0}^{\infty}$. We investigate the effectiveness of our method as $\lambda_1 = \lambda$ goes to $1$, that is, as the spectral gap $\delta = 1-\lambda$ closes. To this end, consider a sequence of Gaussian chains with $\lambda$ increasing from $0.5$ to $0.99$. In accordance with the discussion in Section [\[efficiency\]](#efficiency){reference-type="ref" reference="efficiency"}, for a given $\lambda$, we set $\omega$ to be the density function of a $t$-distribution with similar variance as $\pi_V(\cdot)$, which is the pdf of $\mbox{N}(0,\lambda/2)$. One can verify that [\[momentcond\]](#momentcond){reference-type="eqref" reference="momentcond"} holds for every $\lambda \in (0,1)$. Note that in order for $u_k = (s_k-1)^{1/k}$ to be a non-trivial upper bound on $\lambda_1$, we need $s_k < 2$. As $\lambda$ increases, so does $s_k$ for any given $k$, and thus one must increase $k$ in order to find a useful upper bound. Figure [1](#fig:ClosingSpectralGap0){reference-type="ref" reference="fig:ClosingSpectralGap0"} shows the $k$s used for different $\lambda$s. When $\lambda = 0.5$, we only need $k=4$ to get a decent result; but when $\lambda = 0.99$, $k \approx 70$ is needed. Recall that the time needed to run $N$ iterations of Algorithm 1 is approximately $kN\tau$, where $\tau$ is the time needed to simulate one step of the DA chain, which is roughly the same for any $\lambda \in (0,1)$. To compare the performance of our method for different $\lambda$s, we fix $kN = 1 \times 10^6$, and compare the length of the interval estimates of $\lambda_1$. The results are shown in Figure [3](#fig:ClosingSpectralGap){reference-type="ref" reference="fig:ClosingSpectralGap"}. As $\lambda$ grows, so does $k$, and we are forced to use a smaller sample size $N$. Thus, as $\lambda$ grows, it becomes more difficult to estimate the variances of $u_k^*$ and $l_k^*$ accurately. As a result, the length of the interval estimate of $\lambda_1$ becomes less stable when $\lambda$ is near $1$. This is reflected in Figure [3](#fig:ClosingSpectralGap){reference-type="ref" reference="fig:ClosingSpectralGap"} by an unusually wide interval estimate at $\lambda = 0.97$. On the other hand, most of the interval estimates at other values of $\lambda$ near $1$ are reasonably well-behaved.
