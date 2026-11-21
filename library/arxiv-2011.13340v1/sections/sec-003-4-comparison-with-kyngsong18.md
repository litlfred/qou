---
doc_id: arxiv-2011.13340v1
doc_title: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions *"
section_id: sec-003-4-comparison-with-kyngsong18
section_title: "Comparison with KyngSong18"
section_number: 4
pages: 15-15
source_pdf: 2011.13340v1.pdf
source_sha256: e73876ed2c923608
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.991
doc_brief: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions * — The Entropy method provides a powerful framework for proving scalar concentration in- equalities by establishing functional"
---
\label{sec:ks}
We first state the main result of \cite{KyngSong18} below.
\begin{theorem}\label{thm:kyngsong} Suppose $(x_1,\ldots,x_n)\in\{0,1\}^n$ is a random subset whose distribution is a $k$-homogenous strong Rayleigh distribution. Given a collection of PSD matrices $A_1,\ldots,A_n\in\mathbb{R}^{d\times d}$ s.t. for all $e \in [n]$ we have $\|A_e\|\leq 1$ and $\|\mathbb{E}[\sum_e x_e A_e]\|\leq\mu$. Then for any $\varepsilon > 0$,
  \begin{align*}
    \mathsf{Pr}[\|\sum_e x_e A_e - \mathbb{E}[\sum_e x_e A_e]\|\geq \varepsilon \mu]\leq de^{-\varepsilon^2\mu/(\log k + \varepsilon) \Theta(1)}
  \end{align*}
\end{theorem}
Compared to our Theorem \ref{thm:srBern}, immediate differences is that our theorem can handle any symmetric matrix valued Lipshitz function rather than just sums of random matrices associated to each element. Furthermore, \cite{KyngSong18} require their matrices to be PSD whereas we just require the matrices to be symmetric. Finally, in the special case of sums of PSD matrices. While Theorem \ref{thm:kyngsong} is concerned with multiplicative errors whereas we are concerned with additive errors, we can take $t=\varepsilon \mu$ and plugging this into Theorem \ref{thm:srBern}, noticing that sums of spectral norm 1 random matrices have $\Theta(1)$ Lipshitz constant and ignoring constants in both bounds we get that our bound is better when
\begin{align*}
  \frac{\varepsilon^2\mu}{\log(k)+\varepsilon}&\leq \frac{\varepsilon^2\mu^2}{k+\varepsilon\mu\sqrt{k}}\\
  k+\varepsilon\mu\sqrt{k}\leq \mu \log k+\varepsilon\mu
\end{align*}
Now assuming $\varepsilon \leq \frac{1}{\sqrt{k}}$, we get that the above equation is approximately
\begin{align*}
  \mu\geq k/(\log(k))
\end{align*}
Also notice that in this case, $\mu\leq k$ but it is conceivable that $\mu = \Theta(k)$ when there is no strong relation between the underlying strong Rayleigh measure and the matrices for each element. So our bound is better when such a condition is satisfied and we are looking for small error of the form $\varepsilon \leq 1/\sqrt{k}$. If one could establish a Matrix valued modified log-Sobolev and a Matrix Herbst argument, the $\sqrt{k}\varepsilon$ term in our bound will not appear which would allow us to get rid of the $\varepsilon \leq 1/\sqrt{k}$ condition and just require $\mu\geq k/\log(k)$. However, we are not aware of any strategy to get multiplicative bounds even in the scalar concentration settings using log-Sobolev or any other functional inequalities.
