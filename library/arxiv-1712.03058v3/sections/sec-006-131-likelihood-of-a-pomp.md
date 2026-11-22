---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-006-131-likelihood-of-a-pomp
section_title: "Likelihood of a POMP"
section_number: 1.3.1
pages: 5-7
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.867
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
A POMP consists of two model components, (i) an unobserved Markov process $\{\bm{X}(t;\bm{\theta}): t \geq 0 \}$, which can be discrete or continuous in time, and (ii) an observation model which describes how the data collected at discrete points in time $t_1,\dots ,t_N$, is connected to the transmission model. For notational convenience, we write $\bm{X}_n=\bm{X}(t_n;\bm{\theta})$ and $\bm{X}_{0:N}=(\bm{X}_0,\dots,\bm{X}_N)$. In our application, the process $\bm{X}_{0:N}$ describes the dynamics of the disease spread, e.g. in the case of the simple Markovian SIR model $\bm{X}_n= (S(t_n),I(t_n), R(t_n))'$ counts the number of susceptible, infectious and removed individuals at time $t_n$. Let $\bm{Y}_n$ denote the random variable counting the observations at time $t_n$ which depend on the state of the transmission process $\bm{X}_n$ at that time, cf. Figure [\[pomp\]](#pomp){reference-type="ref" reference="pomp"}. Our data, $\bm{y}^*_{1:N} = (\bm{y}^*_{1} , \dots,\bm{y}^*_{N})$, are then modeled as a realization of this observation process. Depending on how many aspects of the disease dynamics we observe, $\bm{y}^*_{1:N}$ can be either a univariate or multivariate time series. Assuming that the observable random variable $\bm{Y}_n$ is independent of all other variables given the state of the transmission process $\bm{X}_{n}$, the joint density of the states and the observations is defined as the product of the one-step transmission density, $f_{\bm{X}_n|\bm{X}_{n-1}}(\bm{x}_n|\bm{x}_{n-1};\bm{\theta})$, the observation density, $f_{\bm{Y}_n|\bm{X}_{n}}(\bm{y}_n|\bm{x}_{n};\bm{\theta})$, and the initial density $f_{\bm {X}_0}(\bm{x}_0;\bm{\theta})$ as $$\begin{aligned}
f_{\bm{X}_{0:N},\bm{Y}_{1:N}}(\bm{x}_{0:N},\bm{y}_{1:N};\bm{\theta})=&f_{\bm{X}_0}(\bm{x}_0;\bm{\theta})\\
&\times \prod_{n=1}^{N}f_{\bm{X}_n|\bm{X}_{n-1}}(\bm{x}_n|\bm{x}_{n-1};\bm{\theta})f_{\bm{Y}_n|\bm{X}_{n}}(\bm{y}_n|\bm{x}_{n};\bm{\theta}).
\end{aligned}$$ Hence, the likelihood of the parameter vector can be written as the marginal density for a sequence of observations $\bm{Y}_{1:N}$ evaluated at the data $\bm{y}^*_{1:N}$ as

$$\begin{aligned}
\mathcal{L}(\bm{\theta})&=f_{\bm{Y}_{1:N}}(\bm{y}^*_{1:N};\bm{\theta})=\int f_{\bm{X}_{0:N},\bm{Y}_{1:N}}(\bm{x}_{0:N},\bm{y}^*_{1:N};\bm{\theta})d\bm{x}_{0:N}.
\label{lik}
\end{aligned}$$ The dimension of the integral in ([\[lik\]](#lik){reference-type="ref" reference="lik"}) depends on the number of compartments of the Markov process and the number of observations, so this integral is usually high-dimensional and, except for the simplest situations, cannot be solved analytically. The method we will present in the following sections uses the property that it is fairly easy to draw samples from the density $f_{\bm{X}_n|\bm{X}_{n-1}}$ rather than evaluating the function. Because the distribution $f_{\bm{X}_0}$ of the initial state of the Markov process is usually not known, one practical way to deal with this is to fix the initial values of the system at some reasonable values or, treat them as parameters we would like to estimate, see Section [\[complications\]](#complications){reference-type="ref" reference="complications"} for further discussion.
