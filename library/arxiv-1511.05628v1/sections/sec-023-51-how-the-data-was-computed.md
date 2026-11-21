---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-023-51-how-the-data-was-computed
section_title: "How the data was computed"
section_number: 5.1
pages: 20-21
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.95
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.conv label="sub.conv"}

We use the Rolfsen notation for knots [@Rf]. `SnapPy` computes the Neumann-Zagier matrices of default ideal triangulations of the knots below, as well as their exact shapes and trace fields (computed for instance from the Ptolemy module of `SnapPy`) [@ptolemy; @snappy].

Given a Neumann-Zagier datum, the 2 and 3-loop invariants at level $k$ are algebraic numbers, elements of the field $F_{K,k}=F_K(\zeta_k)$, where $F_K$ is the trace field of $K$ and $\zeta_k=e^{\frac{2\pi i}{k}}$. However, these numbers are obtained by sums of algebraic numbers in a much larger number field. Moreover, the 1-loop invariant at level $k$ already contains a $k$-th root of elements of $F_{K,k}$. This makes exact computations impractical. To produce the interesting factorization of Equation [\[eq.phi0factor\]](#eq.phi0factor){reference-type="eqref" reference="eq.phi0factor"}, and keeping in mind the ambiguities of Section [\[sub.ambiguities\]](#sub.ambiguities){reference-type="ref" reference="sub.ambiguities"} we proceed as follows. We know that $x_{k,\ell}=\tau^k_k/(\tau^k_1 \zeta_{24k}^\ell) \in F_{K,k}$ for some natural number $\ell$. Given this, we compute the numerical value $x^{\mathrm{num}}_{k,\ell}$ of $x_{k,\ell}$ (for several values of $\ell$) and find a value of $\ell$ for which there is an element $x^{\mathrm{exact}}_{k,\ell}$ of $F_{K,k}$ which is reasonably close to our element. We accomplish this by the LLL algorithm [@LLL]. The Quantum Modularity Conjecture asserts that the exact element of $F_{K,k}$ should to have the form: $$\label{eq.xe}
x^{\mathrm{exact}}_{k,\ell} = \varepsilon_{K,k} \beta_{K,k}^k$$ for $\varepsilon_{K,k} \in \mathcal O_{F_K(\zeta_k)}^{\times}$ (an algebraic unit) and $\beta_{K,k} \in F_K(\zeta_k)^\times$. To find $\epsilon_{K,k}$ and $\beta_{K,k}$, factor the fractional ideal $$\label{eq.xpi}
x^{\mathrm{exact}}_{k,\ell} \mathcal O_{F_K(\zeta_k)} = 
\mathfrak{p}_1^{e_1} \dots \mathfrak{p}_r^{e_r}$$ into a product of prime ideals $\mathfrak{p}_i$, $i=1,\dots,r$. If all ramification exponents $e_i$ are divisible by $k$, and if the prime ideals are principal $\mathfrak{p}_i=(\wp_i)$ for $\wp_i \in
F_{K,k}^\times$ (the latter happens when the ideal class group of $F_{K,k}$ is trivial), then we define $$\beta_{K,k}=\prod_{i=1}^r \wp_i^{\frac{e_i}{k}} \in F_{K,k}^\times, \qquad
\varepsilon_{K,k}= x^{\mathrm{exact}}_{k,\ell}/\beta_{K,k}^k \,.$$ It follows that $\varepsilon_{K,k}$ is a unit, and that [\[eq.xe\]](#eq.xe){reference-type="eqref" reference="eq.xe"} holds. This gives us strong confidence that $x^{\mathrm{exact}}_{k,\ell}$ is the correct element, and that the computation is correct.

In practice, we have used a `Mathematica` program to compute $x^{\mathrm{num}}_{k,\ell}$ and $x^{\mathrm{exact}}_{k,\ell}$, and a `Sage` program (that uses internally `pari-gp`) to compute the ideal factorization [\[eq.xpi\]](#eq.xpi){reference-type="eqref" reference="eq.xpi"}.
