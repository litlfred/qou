---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-002-12-the-rogers-and-the-cyclic-dilogarithms
section_title: "The Rogers and the cyclic dilogarithms"
section_number: 1.2
pages: 3-4
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.829
latex_coverage_ratio: 0.903
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
[]{#sub.dilog label="sub.dilog"}

Recall the *Rogers dilogarithm* [@Neumann:CCS; @Goette] $$\label{eq.rogers}
\operatorname{R}(z)=
\operatorname{Li_2}(z)+\frac12 \log(z)\log(1-z)-\frac{\pi^2}{6}$$ and its extension as a multivalued function on the universal abelian cover of $\mathbbm C\setminus\{0,1\}$.

The *cyclic (quantum) dilogarithm* $\operatorname{D}_N(x;q)$ is the $N$-th root of a polynomial in $x$ with constant term $1$ defined by $$\label{eq.DN}
\operatorname{D}_N(x;q)=\prod_{k=1}^{N-1} (1-q^k x)^{k/N} \,.$$ It appeared in [@Kashaev:star Eqn.C.3] and [@Kashaev:quantum.hyper Eqn.2.30], and its $N$-th power is characterized among polynomials by the functional equation $$\frac{\operatorname{D}_N(\zeta_N x;\zeta_N)^N}{\operatorname{D}_N(x;\zeta_N)^N}
= \frac{(1-x)^N}{1-x^N}, \qquad \operatorname{D}_N(0)^N=1.$$ It will be useful to introduce the following variant $\slashed{\operatorname{D}}_N$ defined by $$\slashed{\operatorname{D}}_N(x;q)
=\prod_{k=1}^{N}(1-xq^k)^{k/N}=(1-xq^N)\operatorname{D}_N(x;q) \,.$$
