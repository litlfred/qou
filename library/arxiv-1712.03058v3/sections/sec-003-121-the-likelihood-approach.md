---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-003-121-the-likelihood-approach
section_title: "The likelihood approach"
section_number: 1.2.1
pages: 3-4
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.941
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
The idea behind likelihood-based inference is the following. Suppose we have data in the form of a sequence of $N$ observations $\bm{y}^*_{1:N}$ at times $t_1,\dots ,t_N$ and a model for the data $f(\bm{y}_{1:N};\bm{\theta})$ where $f$ is typically a probability mass or density function parametrized by a vector of parameters denoted by $\bm{\theta}$. In our context $\bm{y}^*_{1:N}$ might, for example, represent the weekly number of newly reported cases over a certain period of time and $\bm{\theta}$ might contain the parameters of a suitable Markovian epidemic transmission model. In order to calibrate the model to our observations we would like to find the elements of the parameter vector $\bm{\theta}$ for which our observations are most likely under the chosen probability model. In other words, we would like to maximize this function $f$ with respect to $\bm{\theta}$ evaluated at the data $\bm{y}^*_{1:N}$. This translates to optimizing the function $$\begin{aligned}
\mathcal{L}(\bm{\theta};\bm{y}^*_{1:N})&=f(\bm{y}^*_{1:N};\bm{\theta}).
\end{aligned}$$ The function $\mathcal{L}$ is called the *likelihood function* and in the following we will suppress its dependence on the data and simply write $\mathcal{L}(\bm{\theta})$ for convenience. The parameter vector which maximizes this function is called the *maximum likelihood estimate* (MLE) and is given as $$\begin{aligned}
\hat{\bm{\theta}} =\underset{\bm{\theta}\in \bm{\Theta}}{\arg\max} \mathcal{L}(\bm{\theta}),
\label{mle}
\end{aligned}$$ where $\bm{\Theta}$ is the parameter space containing all possible sets of parameters.\
For many applications it is often more convenient to work with the *log-likelihood function* $$\begin{aligned}
l(\bm{\theta})=\log \mathcal{L}(\bm{\theta}).
\end{aligned}$$ This transformation often simplifies optimization, but does not change the location of the MLE since the natural logarithm is a monotonically increasing function.
