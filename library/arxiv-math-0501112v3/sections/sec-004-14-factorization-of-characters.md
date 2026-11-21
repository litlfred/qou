---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-004-14-factorization-of-characters
section_title: "Factorization of characters"
section_number: 1.4
pages: 3-4
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.984
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
Biane [@Biane2001approximate] proved (under some mild technical assumptions) that Young diagrams contributing to some finite-dimensional reducible representation of the symmetric group $S_q$ will concentrate around some limit shape if and only if the normalized character of the representation $$\chi(\pi):=\frac{\mathop{\mathrm{Tr}}\rho(\pi)}{\mathop{\mathrm{Tr}}\rho(e)}$$ approximately factorizes, i.e. informally speaking $$\label{eq:approximate} \chi( \sigma_1 \cdots \sigma_n) \approx
\chi(\sigma_1) \cdots \chi(\sigma_n)$$ for all permutations $\sigma_1,\dots,\sigma_n$ with disjoint supports (to be more precise: we consider a sequence of representations $(\rho_q)$ where $\rho_q$ is a representation of $S_q$ and the approximate equality [\[eq:approximate\]](#eq:approximate){reference-type="eqref" reference="eq:approximate"} should hold in the limit $q\to\infty$). The result of Biane can be viewed as an analogue of the law of large numbers while the results presented in this article are an analogue of the central limit theorem; one can ask therefore which condition should replace [\[eq:approximate\]](#eq:approximate){reference-type="eqref" reference="eq:approximate"} in order to prove such stronger results.

We will not be very far from the truth when we say that for the results of Biane [@Biane2001approximate] it is enough to assume some version of [\[eq:approximate\]](#eq:approximate){reference-type="eqref" reference="eq:approximate"} for $n=2$. If we treat permutations $\sigma_1,\sigma_2$ as random variables and the normalized character $\chi$ as an expectation ${\mathbb{E}}$ then this condition can be equivalently written as a condition for the covariance: $$\mathop{\mathrm{Cov}}(\sigma_1,\sigma_2)={\mathbb{E}}( \sigma_1
\sigma_2)-{\mathbb{E}}(\sigma_1) {\mathbb{E}}(\sigma_2) \approx 0.$$ Covariance is a special case of a more general probabilistic notion of a cumulant (we will recall the necessary definitions in Section [\[subsec:cumulants\]](#subsec:cumulants){reference-type="ref" reference="subsec:cumulants"}) therefore it is quite natural to expect that the correct condition for the factorization of characters should involve all cumulants and indeed in this article we prove that the following condition is sufficient for our purposes (Theorem and Definition [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"}): for any cycles $\sigma_1,\dots,\sigma_n$ with disjoint supports we assume that $$\label{eq:approximate2} k_n(\sigma_1,\dots,\sigma_n) = O\big(q^{-
\frac{|\sigma_1|+\cdots+|\sigma_n|+2(n-1)}{2} } \big),$$ where $|\pi|$ denotes the minimal number of factors needed to write the permutation $\pi$ as a product of transpositions.

It should be stressed that the decay of the cumulants in the condition [\[eq:approximate2\]](#eq:approximate2){reference-type="eqref" reference="eq:approximate2"} carries a strong resemblance to the decay of the cumulants of the entries of many interesting classes of random matrices [@Collins2002] and, as we mentioned in Section [\[subsec:higherorder\]](#subsec:higherorder){reference-type="ref" reference="subsec:higherorder"}, it is not an accident.
