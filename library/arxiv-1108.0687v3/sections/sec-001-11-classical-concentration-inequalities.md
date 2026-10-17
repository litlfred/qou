---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-001-11-classical-concentration-inequalities
section_title: "Classical concentration inequalities"
section_number: 1.1
pages: 2-3
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.959
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
Let $\{ X_n : n \geq 1 \}$ be independent Bernoulli random variables with respective means $\{ p_n \}$. Let $S_n := \sum_{k=1}^n X_k$ denote the partial sums, $\mu_n := {\mathbb E}S_n = \sum_{k=1}^n p_k$ denote the means and $V_n := \sum_{k=1}^n p_k (1-p_k)$ denote the variance of $S_n$. The simple and well known one-sided tail estimate for $S_n$ is the classical Gaussian bound $$\label{eq:chernoff}
{\mathbb P}(S_n - \mu_n \geq a) \leq
   \exp \left  (- \frac{2 a^2}{n} \right ) \, .$$ Replacing $X_n$ with $1-X_n$ gives the two-sided bound $$\label{eq:two-sided}
{\mathbb P}(|S_n - \mu_n| \geq a) \leq 2
   \exp \left  (- \frac{2 a^2}{n} \right ) \, .$$ The bound [\[eq:chernoff\]](#eq:chernoff){reference-type="eqref" reference="eq:chernoff"} may be found, among other places, in [@mcdiarmid89 Corollary 5.2]. The references given there include [@hoeffding (2.3)] as well as [@chernoff], which proves the result for identically distributed variables.

When $p_n$ and $1 - p_n$ are bounded away from zero, the variance of $S_n$ is of order $n$ and this kind of bound is the best one can expect. However, when $n \gg \mu_n$, one might hope for uniformity in $n$ via bounds in which the exponent depends on $\mu_n$ and not on $n$. For example, if $\max_{j \leq n} p_j$ is small then $S_n$ is well approximated by a Poisson variable with mean $\mu_n$. The upper tail of a Poisson is not as thin as a Gaussian, being $\exp [ - \Theta (a \log (a/\mu))]$ rather than $\exp [ - \Theta (a^2 / \mu)]$. The bound $$\label{eq:pois}
{\mathbb P}(S_n \geq a + \mu) \leq
   e^a \; \left ( \frac{\mu}{a + \mu} \right )^{a + \mu} \leq
   \exp \left [ - \frac{a^2}{2 (a + \mu)} \right ]$$ is proved in [@hoeffding Theorem 1]

and asymptotically matches the Poissonian upper tail.
