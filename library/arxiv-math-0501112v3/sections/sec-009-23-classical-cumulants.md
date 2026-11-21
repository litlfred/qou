---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-009-23-classical-cumulants
section_title: "Classical cumulants"
section_number: 2.3
pages: 6-6
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.862
latex_coverage_ratio: 0.98
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
[]{#subsec:cumulants label="subsec:cumulants"} The notion of cumulants (or semi-invariants) was introduced to describe the convolution of measures in the classical probability theory. For more details about cumulants in the classical and non-commutative probability theory we refer to overview articles [@Hald-EarlyHistoryCumulants; @MattnerWhat-are-cumulants; @Lehner2002cumulantsI].

If $X_1,\dots,X_n$ are random variables we define their (classical) cumulant to be an appropriate coefficient of the formal expansion of the logarithm of the multidimensional Fourier transform: $$k(X_1,\dots,X_n)= \frac{\partial^n}{\partial t_1 \cdots
\partial t_n}\bigg|_{t_1=\cdots=t_n=0} \log {\mathbb{E}}e^{t_1 X_1+\cdots+t_n
X_n}.$$ Cumulant is linear with respect to each of its arguments. If random variables $X_1,\dots,X_n$ can be split into two groups such that the random variables from the first class are independent with the random variables from the second class then their cumulant vanishes: $k(X_1,\dots,X_n)=0$.

The first two cumulants $$\begin{aligned}
 k(X)& ={\mathbb{E}}X, \\ k(X_1,X_2)&
={\mathbb{E}}(X_1 X_2)- {\mathbb{E}}(X_1) {\mathbb{E}}(X_2)= \mathop{\mathrm{Cov}}(X_1,X_2)
\end{aligned}$$ coincide with the mean value and the covariance.
