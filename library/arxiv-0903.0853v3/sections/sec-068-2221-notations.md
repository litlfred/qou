---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-068-2221-notations
section_title: "Notations"
section_number: 22.2.1
pages: 118-118
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.839
latex_coverage_ratio: 1.0
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
We use some notations from $q$-calculus for this chapter only. Let $p \in {\mathbf C}$ be such that $0 < \left |p \right |< 1$, *e.g.* $p := q^{-1}$. Let $a,a_{1},\ldots,a_{k} \in {\mathbf C}$ and $n \in {\mathbf N}$. The *$q$-Pochhammer symbols* are: []{#not98 label="not98"} $$\begin{aligned}
\index{$q$-Pochhammer symbol}
(a;p)_{n} & := \prod_{0 \leq i < n} (1 - a p^{i}), \\
(a;p)_{\infty} & := \prod_{i = 0}^{\infty} (1 - a p^{i}), \\
(a_{1},\ldots,a_{k};p)_{n} & := \prod_{j=1}^{k} (a_{j};p)_{n}, \\
(a_{1},\ldots,a_{k};p)_{\infty} & := \prod_{j=1}^{k} (a_{j};p)_{\infty}.
\end{aligned}$$ Note that, for all $n \in {\mathbf N}$, we have: $$(a;p)_{n} = \dfrac{(a;p)_{\infty}}{(a;p^{n})_{\infty}},$$ but, since the right hand side is well defined for all $n \in {\mathbf Z}$, this allows us to extend the definition of $q$-Pochhammer symbols; and similarly for $(a_{1},\ldots,a_{k};p)_{n}$.\
[]{#not99 label="not99"} With these notations, Jacobi's theta functions $\theta(z;q)$ and ${\theta_{q}}$ respectively defined in equations [\[eqn:tripleproduit\]](#eqn:tripleproduit){reference-type="eqref" reference="eqn:tripleproduit"} and [\[eqn:thq\]](#eqn:thq){reference-type="eqref" reference="eqn:thq"} page admit the factorisations: $$\begin{aligned}
\label{eqn:deuxtriplesproduits}
\theta(z;q) & = (q^{-1},- z,- q^{-1} z^{-1};q^{-1})_{\infty}, \\
{\theta_{q}}(z) & = (q^{-1},-q^{-1} z,-z^{-1};q^{-1})_{\infty}.
\end{aligned}$$ (This is again Jacobi's triple product formula.) In section [\[section:qEuler\]](#section:qEuler){reference-type="ref" reference="section:qEuler"}, we use functions derived from $\theta(z;q)$, as in chapter [\[chapter:asymptotictheory\]](#chapter:asymptotictheory){reference-type="ref" reference="chapter:asymptotictheory"}. In section [\[section:qEulersquare\]](#section:qEulersquare){reference-type="ref" reference="section:qEulersquare"}, we use functions derived from ${\theta_{q}}$, as in chapter [\[chapter:geometryofF(M)\]](#chapter:geometryofF(M)){reference-type="ref" reference="chapter:geometryofF(M)"}. In section [\[section:MockTheta\]](#section:MockTheta){reference-type="ref" reference="section:MockTheta"}, we use both kinds in alternance. Last, note that, along with these two forms, we shall also use in section [\[section:QuadForms\]](#section:QuadForms){reference-type="ref" reference="section:QuadForms"} the "classical" forms $\theta_{i,j}$, $i,j \in \{0,1\}$.
