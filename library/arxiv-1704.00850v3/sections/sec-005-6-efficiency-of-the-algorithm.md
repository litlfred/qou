---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-005-6-efficiency-of-the-algorithm
section_title: "Efficiency of the algorithm"
section_number: 6
pages: 15-17
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 1.0
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
[]{#efficiency label="efficiency"}

To obtain an interval estimate of $\lambda_1$ based on [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"} or [\[estimator2\]](#estimator2){reference-type="eqref" reference="estimator2"}, one needs to run $N$ iterations of Algorithm 1 or 2. If the time needed to simulate one step of the DA chain is $\tau$, then the time needed to run $N$ iterations of Algorithm 1 or 2 is approximately $kN\tau$. Note that significant speedup can be achieved through parallel computing, since the $N$ iterations are carried out independently. Given $k$ and $N$, the accuracy of the estimate depends on two factors: 1. The distance between $l_k$ and $u_k$, and 2. The errors in the estimates, $l^*_k$ and $u^*_k$. We now briefly analyze these two factors, and give some additional guidelines regarding the choice of $\omega(\cdot)$ and $\psi(\cdot)$.

As before, suppose that $$1 = \lambda_0 > \lambda_1 = \lambda_2 = \cdots = \lambda_m > \lambda_{m+1} \geq \cdots \geq \lambda_{\kappa} > 0$$ for some $m < \infty$. Clearly, as $k \to \infty$, $$s_k - 1 = \lambda_1^k \left( m + O \left( \lambda_{m+1}^k/\lambda_1^k \right) \right).$$ Hence, as $k \to \infty$, $$l_k := \frac{s_k-1}{s_{k-1}-1} = \lambda_1 \left( 1 + O \left( \lambda_{m+1}^{k-1}/\lambda_1^{k-1} \right) \right),$$ and $$\begin{aligned}
    u_k &:= (s_k-1)^{1/k}\\
    &= \lambda_1 m^{1/k} \left(1 + O\left( k^{-1} \lambda_{m+1}^k/\lambda_1^k \right) \right) \\
    &= \lambda_1 \left( 1 + (\log m) O\left(k^{-1}\right) \right) \left(1 + O\left( k^{-1} \lambda_{m+1}^k/\lambda_1^k \right) \right).\\
    &= \left\{
    \begin{array}{@{}ll@{}}
    \lambda_1 \left(1 + O\left( k^{-1} \lambda_2^k/\lambda_1^k \right) \right)  & m=1 \\
    \lambda_1 \left( 1 + O\left(k^{-1}\right) \right) & m > 1. \,
    \end{array} \right. 
    \end{aligned}$$ Depending on whether $m=1$ or not, $u_k-l_k$ decreases at either a geometric or polynomial rate as $k$ grows.

The errors of $l^*_k$ and $u^*_k$ arise from those of $s^*_k$ and $s^*_{k-1}$. We now consider the estimator [\[estimator2\]](#estimator2){reference-type="eqref" reference="estimator2"} for estimating $s_k$. Its variance is given by $$\begin{aligned}
    \frac{D'^2}{N} &= \frac{1}{N} \left\{ \int_{S_U}\int_{S_V}\int_{S_V} \bigg(\frac{\pi_{U|V}(u|v)}{\psi(u)}\bigg)^2
    r(v',dv) \pi_{V|U}(v'|u) \psi(u) \,\nu(dv') \, \mu(du) - s_k^2 \right\}\\
    &= \frac{1}{N} \left\{ \int_{S_U}\int_{S_V} \int_{S_U} \frac{\pi_{U|V}^2(u|v)}{\psi(u)} \pi_{V|U}(v|u') p^{(k)}(u,u') \, \mu(du') \, \nu(dv) \, \mu(du) - s_k^2 \right\}.
    \end{aligned}$$ Note that $$p_k\left( (u,v), (u',v') \right) := \pi_{V|U}(v'|u') p^{(k)}(u,u')$$ gives the $k$-step Mtd of a Gibbs chain whose stationary pdf is $\pi_{U,V}(\cdot,\cdot)$. Thus, under suitable conditions, for almost any $u \in S_U$, $$\begin{aligned}
    \lim\limits_{k \to \infty} s_k(u) &:= \lim\limits_{k \to \infty} \int_{S_V} \int_{S_U} \frac{\pi_{U|V}^2(u|v)}{\psi(u)} \pi_{V|U}(v|u') p^{(k)}(u,u') \, \mu(du') \, \nu(dv) \\
    &= \int_{S_V} \int_{S_U} \frac{\pi_{U|V}^2(u|v)}{\psi(u)} \pi_{U,V}(u',v) \, \mu(du') \, \nu(dv) \\
    &= \frac{p(u,u) \pi_U(u)}{\psi(u)}.
    \end{aligned}$$ As $k \to \infty$, we expect $$D'^2 = \int_{S_U} s_k(u) \, \mu(du) - s_k^2 \to \int_{S_U} \frac{p(u,u) \pi_U(u)}{\psi(u)} \, \mu(du) - 1.$$ Suppose that $\psi(u) \approx \pi_U(u)$, then heuristically, $$\int_{S_U} \frac{p(u,u) \pi_U(u)}{\psi(u)} \, \mu(du) - 1 \approx \int_{S_U} p(u,u) \mu(du) - 1 = s_1 - 1.$$ Thus, if the sum of $P$'s eigenvalues, $s_1$, is relatively small, we recommend picking $\psi(\cdot)$s that resemble $\pi_U(\cdot)$, with possibly heavier tails (to ensure that the moment condition [\[momentconddual\]](#momentconddual){reference-type="eqref" reference="momentconddual"} holds). By a similar argument, when using the estimator [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"}, picking $\omega(\cdot)$s that resemble $\pi_V(\cdot)$ is likely to control $D^2$ around $s_1 - 1$ for large $k$s.

While (under suitable conditions) the variance of $s_k^*$ converges to a constant as $k \rightarrow \infty$, this is not the case for $u^*_k$ and $l^*_k$ (because $u_k$ and $l_k$ are non-linear in $s_k$ and $s_{k-1}$). In fact, using the delta method, one can show that these variances are unbounded. Thus, there's a trade-off between decreasing $u_k - l_k$ (by increasing $k$) and controlling the errors of $u^*_k$ and $l^*_k$. We do not recommend increasing $k$ indefinitely. As long as $k$ is large enough so that $s_k - 1$ is significantly smaller than $1$, $u_k$ serves as a non-trivial (and often decent) upper bound for $\lambda_1$.
