---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-062-82-affine-charts-for-flag-hilbert-schemes
section_title: "Affine charts for flag Hilbert schemes"
section_number: 8.2
pages: 59-59
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.953
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:affinecharts2 label="sub:affinecharts2"}

The situation is somewhat better in the case of flag Hilbert schemes $\mathrm{FHilb}_n(*)$ for any $* \in \{\mathbb{C}^2, \mathbb{C}, \mathrm{point}\}$, where one has affine coverings: $$\label{eqn:chart}
\mathrm{FHilb}_n(*) = \bigcup_{T \vdash n} \mathring{\mathrm{FHilb}}_T(*)$$ indexed by standard Young tableaux $T$ of size $n$. Recall that a standard Young tableau is a numbering of the boxes of a Young diagram of size $n$ with the numbers $1,...,n$ such that the numbers increase as we go up and right in the diagram. A covering [\[eqn:chart\]](#eqn:chart){reference-type="eqref" reference="eqn:chart"} is called **good** if all the charts are $\mathbb{C}^{*} \times \mathbb{C}^*$ equivariant and it respects passage from $n+1$ to $n$: $$\includegraphics{before_8_4.png}$$ where the chart corresponding to any $T'$ maps to the chart corresponding to $T = T' \backslash \square_{n+1}$. Here, $\square_{n+1}$ denotes the box labeled $n+1$ in $T$, which must necessarily be an outer corner of $T$ and an inner corner of $T'$. Restricting the sheaf of dg algebras $\mathrm{FHilb}_n^\text{dg}(*)$ to the affine charts [\[eqn:chart\]](#eqn:chart){reference-type="eqref" reference="eqn:chart"} gives rise to dg algebras: $$\label{eqn:coordinaterings}
\mathring{\mathcal{A}}^\text{dg}_T(*) = \mathbb{C}\left[\mathring{\mathrm{FHilb}}^\text{dg}_T(*)\right]$$

::: conjecture
[]{#conj:charts label="conj:charts"}

There exists a good covering whose coordinate rings [\[eqn:coordinaterings\]](#eqn:coordinaterings){reference-type="eqref" reference="eqn:coordinaterings"} satisfy: $$\label{eqn:genrel}
\mathring{\mathcal{A}}_{T \cup \square}(*) = \frac {\mathring{\mathcal{A}}_{T}(*)[*, f_{\square_1},f_{\square_2},...]}{(r_{\blacksquare_1},r_{\blacksquare_2},...)}$$ where $\square_1,\square_2,...$ denote the inner corners of $T$ different from $\square$, and $\blacksquare_1,\blacksquare_2,...$ denote the outer corners of $T$ (except for the outer corner labeled $n$ in the case $* = \mathrm{point}$). The generators denoted by $*$ stand for the affine coordinates $\{x_{n+1},y_{n+1}\}$, $\{x_{n+1}\}$, $\emptyset$ when $* = \mathbb{C}^2, \mathbb{C}, \mathrm{point}$.
:::

We do not know how to define the generators $f_k$ and the relations $r_k$, but we know how to predict their characters with respect to the $\mathbb{C}^{*} \times \mathbb{C}^*$ action. Specifically, for a box $\square = (a,b)$ in a Young diagram, we define its weight as: $$\label{eqn:weight}
z_\square = q^a t^b$$ When $\blacksquare$ is the box labeled by $i$ in a Young tableau $T$, we will write $z_\blacksquare= z_i$ for brevity. Then we expect that the generators and relations of [\[eqn:genrel\]](#eqn:genrel){reference-type="eqref" reference="eqn:genrel"} have equivariant weights $$\label{eqn:expectation}
\text{weight }f_{\blacksquare} = \frac {z_{\blacksquare}}{z_{\square}}, \qquad \text{weight }r_{\blacksquare} = \frac {z_{\blacksquare}}{z_{\square}}$$ where $\square$ is the corner that is being added in [\[eqn:genrel\]](#eqn:genrel){reference-type="eqref" reference="eqn:genrel"}. In the remainder of this Section, we will establish a weaker version of Conjecture [\[conj:charts\]](#conj:charts){reference-type="ref" reference="conj:charts"}, by constructing affine $\mathbb{C}^{*} \times \mathbb{C}^*$ invariant open sets that contain the fixed points of $\mathrm{FHilb}_n(*)$, but are not required to cover it.
