---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-010-23-generalization-to-young-diagrams-on-r2
section_title: "Generalization to Young diagrams on R+2"
section_number: 2.3
pages: 8-8
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 1.0
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
We may identify a Young diagram with a subset of $\mathbb{R}^2$ given by a graphical representation of $\lambda$ (according to the French notation). For example, for a partition $\lambda=(\lambda_1,\dots,\lambda_k)$ it is the set $$\label{eq:identify}
\bigcup_{1\leq i\leq k}   [0,\lambda_i] \times  [i-1,i] .$$ In this way we may consider colorings $h$ of the cycles of permutations $\sigma_1$ and $\sigma_2$ which take real values instead of natural numbers. If we fix some numbering of the cycles in $C=C(\sigma_1)\sqcup C(\sigma_2)$ then any such coloring $h\colon C\rightarrow\mathbb{R}_+$ can be identified with an element of $\mathbb{R}_+^{|C|}$.

We define $$\label{eq:generalized}
N^{\lambda}(\sigma_1,\sigma_2)= \mathop{\mathrm{vol}}\{h\in \mathbb{R}_+^{|C|}:h \text{ compatible with } \lambda \}.$$ Notice that in the case when $\lambda\subset\mathbb{R}^2$ is as prescribed by [\[eq:identify\]](#eq:identify){reference-type="eqref" reference="eq:identify"}, the set of functions $h\in \mathbb{R}_+^{|C|}$ compatible with $\lambda$ is a polyhedron hence there is no difficulty in defining its volume; furthermore definitions [\[eq:usual\]](#eq:usual){reference-type="eqref" reference="eq:usual"} and [\[eq:generalized\]](#eq:generalized){reference-type="eqref" reference="eq:generalized"} give the same value.

The advantage of the definition [\[eq:generalized\]](#eq:generalized){reference-type="eqref" reference="eq:generalized"} is that it allows to define characters for any bounded set $\lambda\in\mathbb{R}_+^2$, in particular for *generalized Young diagrams* (see [@Kerov1993]).

It is very natural therefore to ask if Theorem [\[theo:character-sniady\]](#theo:character-sniady){reference-type="ref" reference="theo:character-sniady"} holds true also for skew Young diagrams. Unfortunately, this is not the case as it can be seen for the skew Young diagram $\lambda=(3,2) \setminus (1)$.
