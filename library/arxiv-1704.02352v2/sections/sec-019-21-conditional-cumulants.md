---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-019-21-conditional-cumulants
section_title: "Conditional cumulants"
section_number: 2.1
pages: 14-15
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.703
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
[]{#sec:conditional-cumulants label="sec:conditional-cumulants"}

Let $\mathcal{A}$ and $\mathcal{B}$ be commutative unital algebras and let $\mathbb{E}\colon\mathcal{A}\to\mathcal{B}$ be a unital linear map. We will say that $\mathbb{E}$ is a *conditional expectation value*; in the literature one usually imposes some additional constraints on the structure of $\mathcal{A}$, $\mathcal{B}$ and $\mathbb{E}$, but for the purposes of the current paper such additional assumptions will not be necessary.

For any tuple $x_1,\dots,x_\ell \in\mathcal{A}$ we define their *conditional cumulant* as $$\begin{gathered}
 \kappa_{\mathcal{A}}^{\mathcal{B}}(x_1,\dots,x_\ell) =  
[t_1 \cdots t_\ell] \log \mathbb{E}e^{t_1 x_1+\dots+t_\ell x_\ell} = \\
\left. \frac{\partial^\ell}{\partial t_1 \cdots \partial t_\ell}
\log \mathbb{E}e^{t_1 x_1+\dots+t_\ell x_\ell} \right|_{t_1=\cdots=t_\ell=0}
\in \mathcal{B},
\end{gathered}$$ where the operations on the right-hand side should be understood in the sense of formal power series in variables $t_1,\dots,t_\ell$.

Note that the cumulants for partitions which we introduced in [\[sec:concatenation\]](#sec:concatenation){reference-type="ref" reference="sec:concatenation"} fit into this general framework: for $\mathcal{A}:=\mathbb{R}[\mathcal{P}]$ one should take the semigroup algebra of partitions, for $\mathcal{B}:=\mathbb{R}$ the real numbers and for $\mathbb{E}:=\chi\colon\mathbb{R}[\mathcal{P}]\to\mathbb{R}$ the character.
