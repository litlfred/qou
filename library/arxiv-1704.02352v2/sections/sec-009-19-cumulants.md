---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-009-19-cumulants
section_title: "Cumulants"
section_number: 1.9
pages: 5-5
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
[]{#sec:concatenation label="sec:concatenation"}

For partitions $\pi_1,\dots,\pi_k$ we define their *product* $\pi_1 \cdots \pi_k$ as their concatenation, for example $(4,3) \cdot (5,3,1)=(5,4,3,3,1)$. In this way the set of all partitions $\mathcal{P}=\bigsqcup_{n\geq 0} \mathcal{P}_{n}$ becomes a unital semigroup with the unit $1=\emptyset$ corresponding to the empty partition; we denote by $\mathbb{R}[\mathcal{P}]$ the corresponding semigroup algebra, the elements of which are formal linear combinations of partitions. Any character $\chi\colon\mathcal{P}\to\mathbb{R}$ with $\chi(\emptyset)=1$ can be canonically extended to a linear map $\chi\colon\mathbb{R}[\mathcal{P}]\to\mathbb{R}$ (such that $\chi(1)=\chi(\emptyset)=1$) which will be denoted by the same symbol.

For partitions $\pi_1,\dots,\pi_\ell$ we define their *cumulant* with respect to the character $\chi\colon \mathcal{P}\to\mathbb{R}$ as a coefficient in the expansion of the logarithm of an analogue of a multidimensional Laplace transform $$\label{eq:log-laplace}
k^{\chi}_\ell(\pi_1,\dots,\pi_\ell):= 
\left. \frac{\partial^\ell}{\partial t_1 \cdots \partial t_\ell}
\log \chi\left( e^{t_1 \pi_1+\cdots+t_\ell \pi_\ell} \right) 
\right|_{t_1=\cdots=t_\ell=0},$$ where the operations on the right-hand side should be understood in the sense of formal power series with coefficients either in $\mathbb{R}[\mathcal{P}]$ or in $\mathbb{R}$.

In the special case when each partition $\pi_i=(l_i)$ consist of just one part we will use a simplified notation and we will write $$k^{\chi}_\ell(l_1,\dots,l_\ell) = k^{\chi}_\ell\big( (l_1),\dots,(l_\ell) \big).$$ For example, $$\begin{aligned}
k^{\chi}_1(l_1) &= \chi(l_1), \\   
k^{\chi}_2(l_1,l_2) &= \chi(l_1,l_2)- \chi(l_1) \chi(l_2).
\end{aligned}$$
