---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-015-29-free-cumulants-of-the-transition-measure
section_title: "Free cumulants of the transition measure"
section_number: 2.9
pages: 9-10
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.961
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
Cauchy transform of a compactly supported probability measure is given at the neighborhood of infinity by a power series $$G_{\mu}(z)=\frac{1}{z}+\sum_{n\geq 2} M_n z^{-n-1},$$ where $M_n=\int_R x^n d\mu$ are the moments of the measure $\mu$. It follows that on some neighborhood of infinity $G_{\mu}$ has a right inverse $K_{\mu}$ with respect to the composition of power series given by $$K_{\mu}(z)=\frac{1}{z}+\sum_{n\geq 1} R_n z^{n-1}$$ convergent on some neighborhood of $0$. The coefficients $R_i=R_i(\mu)$ are called free cumulants of measure $\mu$. Free cumulants appeared implicitly in Voiculescu's $R$--transform [@VoiculescuAddition] and their combinatorial meaning was given by Speicher [@Speicher1997].

Free cumulants are homogenous in the sense that if $X$ is a random variable and $c$ is some number then $$R_i(cX)=c^i R_i(X)$$ and for this reason they are very useful in the study of asymptotic questions.

Each free cumulant $R_n$ is a polynomial in the moments $M_1,M_2,\dots,M_n$ of the measure and each moment $M_n$ can be expressed as a polynomial in the free cumulants $R_1,\dots,R_n$; in other words the sequence of moments $M_1,M_2,\dots$ and the sequence of free cumulants $R_1,R_2,\dots$ contain the same information about the probability measure. The functionals of Young diagrams considered in [\[eq:p-tylda\]](#eq:p-tylda){reference-type="eqref" reference="eq:p-tylda"} have a nice geometric interpretation but they are not very convenient in actual calculations. For this reason we will prefer to describe the shape of a Young diagram by considering a family of functionals $$\label{eq:wolnekumulanty} \lambda\mapsto R_n(\mu^{\lambda})$$ given by the free cumulants of the transition measure. Equation [\[eq:definicja3\]](#eq:definicja3){reference-type="eqref" reference="eq:definicja3"} shows that functionals $\tilde{p}_k$ from the family [\[eq:p-tylda\]](#eq:p-tylda){reference-type="eqref" reference="eq:p-tylda"} can be expressed as polynomials in the functionals from the family [\[eq:wolnekumulanty\]](#eq:wolnekumulanty){reference-type="eqref" reference="eq:wolnekumulanty"} and vice versa.

Please note that the first two cumulants of a transition measure do not carry any interesting information since $$R_1(\mu^{\lambda})=M_1(\mu^{\lambda})=0,$$ $$R_2(\mu^{\lambda})=M_2(\mu^{\lambda})=q,$$ where $q$ denotes the number of the boxes of the Young diagram $\lambda$.

Above we treated the free cumulant $R_i$ as a function on Young diagrams, but it also can be viewed (via Fourier transform) as a central element in ${\mathbb{C}}(S_q)$.
