---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-053-242-analytic-aspects
section_title: "Analytic aspects"
section_number: 24.2
pages: 127-128
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.904
---
[]{#section:qEulersquareanalytic label="section:qEulersquareanalytic"}

### The square of the Tshakaloff series is not summable with one level

Consider the square $\hat Y := \text{\tencyr\cyracc Ch}^{2}$ of the Tshakaloff series: $$\hat Y(z) = \left(\sum_{n\ge 0}q^{n(n-1)/2} z^n\right)^2.$$ Its $q$-Borel transform ${\mathcal{B}_{q,1}}\hat Y$ (at level $1$) can be computed from the following simple remark: $$\hat f(z) = \sum_{n\ge 0} a_n z^n \text{~and~} \hat g \in{{\mathbf C}[[z]]}
\Longleftrightarrow
{\mathcal{B}_{q,1}}(\hat f \hat g) =
\sum_{n \ge 0} a_n q^{-n(n-1)/2} \xi^n {\mathcal{B}_{q,1}}\hat g(q^{-n} \xi).$$ It follows that, if $P(\xi) = {\mathcal{B}_{q,1}}\hat Y(\xi){\prod_{n\ge 0}(1-q^{-n}\xi)}$, then $P$ is an entire function such that: $$\label{equation:BorelCarre}
P(q^m) = (-1)^mq^{m(3m+1)/2}(q^{-1};q^{-1})_m(q^{-1};q^{-1})_\infty.$$ From this, we see that $P$ has at infinity $q$-exponential growth of order $\geq 3$.\
The $q$-Borel transform of $\hat Y$ represents a meromorphic function in ${\mathbf C}$ with (simple) poles on $q^{\mathbf N}$ and having at infinity in ${\mathbf C}\setminus q^{\mathbf N}$ $q$-exponential growth of order exactly $2$.\
Thus, $\hat Y = \text{\tencyr\cyracc Ch}^{2}$ is not $q$-Borel-Laplace summable as $\text{\tencyr\cyracc Ch}$ itself is. This comes from the fact that the Newton polygon of the former (resp. of the latter) has three (resp. two) slopes as we have seen. Moreover, the problem is cousin to a nonlinear problem.
