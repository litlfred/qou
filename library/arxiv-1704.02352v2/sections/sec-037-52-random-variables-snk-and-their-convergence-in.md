---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-037-52-random-variables-snk-and-their-convergence-in
section_title: "Random variables S[n]k and their convergence in probability."
section_number: 5.2
pages: 36-37
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.829
latex_coverage_ratio: 0.8
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
We start the proof of [\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"}. For $k\geq 2$ consider the random variable $$S_k^{[n]}:=\frac{1}{n^{\frac{k}{2}}} \mathcal{S}_k(\lambda_n).$$ By aproximate factorization property, the condition [\[item:AFP-A\]](#item:AFP-A){reference-type="ref" reference="item:AFP-A"} from [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"} is fulfilled; it follows that the condition [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"} is fulfilled as well. In the special case $\ell=1$ and $x_1=\mathcal{S}_k$ it follows that the limit $$\label{eq:limit-in-LLN}
s_k:=\lim_{n\to\infty} \mathbb{E}_{\chi_n} S^{[n]}_k  = 
\lim_{n\to\infty} \frac{1}{n^{\frac{k}{2}}} \mathbb{E}_{\chi_n}  \mathcal{S}_k$$ exists; in the special case $\ell=2$ and $x_1=x_2=\mathcal{S}_k$ it follows that the variance $$\operatorname{Var} S^{[n]}_k = 
\kappa_2^{\chi_n}\left( \frac{1}{n^{\frac{k}{2}}} \mathcal{S}_k,\frac{1}{n^{\frac{k}{2}}} \mathcal{S}_k  \right)=
O\left( \frac{1}{n} \right)$$ converges to zero. Chebyshev's inequality implies that for each $k\geq 2$ the sequence of random variables $(S_k^{[n]})_n$ converges (as $n\to\infty$) to $s_k$ in probability.
