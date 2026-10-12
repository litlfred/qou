---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-047-2221-notations
section_title: "Notations"
section_number: 22.2.1
pages: 118-119
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 1.0
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
\end{aligned}$$ (This is again Jacobi's triple product formula.) In section [1](#section:qEuler){reference-type="ref" reference="section:qEuler"}, we use functions derived from $\theta(z;q)$, as in chapter [\[chapter:asymptotictheory\]](#chapter:asymptotictheory){reference-type="ref" reference="chapter:asymptotictheory"}. In section [\[section:qEulersquare\]](#section:qEulersquare){reference-type="ref" reference="section:qEulersquare"}, we use functions derived from ${\theta_{q}}$, as in chapter [\[chapter:geometryofF(M)\]](#chapter:geometryofF(M)){reference-type="ref" reference="chapter:geometryofF(M)"}. In section [\[section:MockTheta\]](#section:MockTheta){reference-type="ref" reference="section:MockTheta"}, we use both kinds in alternance. Last, note that, along with these two forms, we shall also use in section [\[section:QuadForms\]](#section:QuadForms){reference-type="ref" reference="section:QuadForms"} the "classical" forms $\theta_{i,j}$, $i,j \in \{0,1\}$.

# The $q$-Euler equation and confluent basic hypergeometric series {#section:qEuler}

Consider a $q$-difference system of rank $2$ and level $1$ (that is, its slopes are $\mu,\mu+1$ for some $\mu \in {\mathbf Z}$). Through some analytic gauge transformation, its matrix can be put in the form $b z^{\mu} ~ \begin{pmatrix} 1 & u \\ 0 & a z \end{pmatrix}$, where $a,b \in {\mathbf C}^{*}$, $\mu \in {\mathbf Z}$ and $u \in {{\mathbf C}(\{z\})}$. The $b z^{\mu}$ factor corresponds to a tensor product by a rank one object $L$, which does not affect the Stokes phenomenon, nor the isoformal classification, *i.e.* the map $M \leadsto L \otimes M$ induces an isomorphism: $${\mathcal{F}}(P_{1},\ldots,P_{k}) \rightarrow {\mathcal{F}}(L \otimes P_{1},\ldots,L \otimes P_{k}).$$ We therefore assume that $b = 1, \mu = 0$. The associated inhomogeneous equation is the following *$q$-Euler equation*: $$\label{eqn:qEuler}
\begin{pmatrix} 1 & f \\ 0 & 1 \end{pmatrix}:
\begin{pmatrix} 1 & 0 \\ 0 & a z \end{pmatrix} \simeq
\begin{pmatrix} 1 & u \\ 0 & a z \end{pmatrix}
\Longleftrightarrow
a z \sigma_qf - f = u.$$

## A digest on the $q$-Euler equation {#subsection:qEuler}
