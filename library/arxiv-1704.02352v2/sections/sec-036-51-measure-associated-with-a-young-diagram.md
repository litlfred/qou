---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-036-51-measure-associated-with-a-young-diagram
section_title: "Measure associated with a Young diagram"
section_number: 5.1
pages: 36-36
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
[]{#subsec:MeasureAssociatedWithYoung label="subsec:MeasureAssociatedWithYoung"}

Suppose an anisotropic Young diagram $\Lambda\subseteq \mathbb{R}\times \mathbb{R}$ (viewed in the French coordinate system) is given. We will assume that the area of $\Lambda$ is equal to $1$. Let $(x,y)\in\Lambda$ be a random point in $\Lambda$, sampled with the uniform probability. We denote by $P_{\Lambda}$ the probability distribution of its Russian coordinate $$u = x-y.$$ It is a probability measure on $\mathbb{R}$ with the probability density $$\label{eq:density}
f_{\Lambda}(u)=\frac{\omega_\Lambda(u)-|u|}{2}.$$ This density is a Lipschitz function with the Lipschitz constant equal to $1$. Such probability measures $P_{\Lambda}$ will be our main tool for investigation of asymptotics of Young diagrams $\Lambda$. The Reader should be advised that this is *not* Kerov's transition measure which is also a probability measure on the real line associated with a Young diagram [@Kerov1993transition] for similar purposes.

Any anisotropic Young diagram $\Lambda$ with unit area which contains some point $(x_0,y_0)$, contains also the whole rectangle $\{ (x,y) : 0\leq x \leq x_0, 0\leq y\leq y_0 \}$; by comparison of the areas it follows that $x_0 y_0\leq 1$. The latter inequality written in the Russian coordinate system gives the following restriction on the possible values of the corresponding profile $\omega$: $$|u| \leq \omega(u) \leq \sqrt{u^2+4}$$ and for the corresponding density $$\label{eq:bounds-on-density}
0\leq f_\Lambda(u) \leq \frac{\sqrt{u^2+4}-|u|}{2} = \frac{2}{\sqrt{u^2+4}+|u|}.$$

A simple change of variables in the integrals shows that for a Young diagram $\lambda_n$ with $n$ boxes and the corresponding anisotropic Young diagram $\Lambda_n$ given by [\[eq:Lambda\]](#eq:Lambda){reference-type="eqref" reference="eq:Lambda"} the moments of the measure $P_{\Lambda_n}$ are given by $$\int u^{k} \dif P_{\Lambda_n}(u) = \frac{1}{k+1} \frac{1}{n^{\frac{k+2}{2}}}   \mathcal{S}_{k+2}(\lambda_n)
\qquad \text{for $k\geq 0$.}$$
