---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-020-42-potential-and-main-category-of-matrix-factori
section_title: "Potential and main category of matrix factorizations"
section_number: 4.2
pages: 21-22
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.926
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In this section we introduce an associative convolution operation in the category of matrix factorizations on the space $\calX_2$. In subsequent sections we construct a homomorphism from the braid group into this convolution algebra. This allows us to associate a particular matrix factorization to a braid and in the section [\[sec: link inv 2\]](#sec: link inv 2){reference-type="ref" reference="sec: link inv 2"} we explain how one can extract knot homology out of this matrix factorization.

We choose coordinates on $\calX_2=\frg\times (G\times \frb)^2$ as $(X,g_1,Y_1,g_2,Y_2)$ and consider a $G\times B^2$-invariant potential on $\calX_2$: $$\label{eq: potential}
 \SymbolPrint{W}(X,g_1,Y_1,g_2,Y_2)=\Tr(X(\Ad_{g_1}(Y_1)-\Ad_{g_2}(Y_2))).$$

The torus $T_{sc}$ acts on $\calX_2$ and $\deg_{\Tsc}W = t^2$.

Consider the category of

$\SymbolPrint{\MF_{B^2}(\calX_2,W)}$ of $\Tsc$-graded $B^2$-equivariant matrix factorizations whose differentials have degree $\deg_{\Tsc}D = t$.

The morphisms and homotopies in the category are assumed to be $T_{sc}$-invariant.

Our main category is the subcategory $\MF_{ B^2}(\calX_2,W)^G$ of $\MF_{B^2}(\calX_2,W)$ that consists of the complexes that are $G$-equivariant in the strong sense. The $G$-action on $\calX_2$ is free and as we show in subsection [\[ssec: Gslice\]](#ssec: Gslice){reference-type="ref" reference="ssec: Gslice"} the category $\MF_{ B^2}(\calX_2,W)^G$ is equivalent to the category of $B^2$-equivariant matrix factorizations on $\calX_2/G$. To simplify notations, from now on we use notation $\MF_{B^2}(\calX_2,W)$ for $\MF_{B^2}(\calX_2,W)^G$.

We also use notation $\SymbolPrint{\mathbf{q}^k\mathbf{t}^m}$ for shift functor for the weights of the action of $T_{sc}$: if $V$ is a vector space with $\CC^*_t\times\CC^*_q$ action then $\mathbf{q}^k\mathbf{t}^m\cdot V$ is the same vector space with $q$- and $t$-degrees shifted by $k$ and $m$: for $v\in V$ and $(\lambda,\mu)\in\CC^*_t\times\CC^*_q$ we define $(\lambda,\mu)\cdot(\mathbf{q}^k\mathbf{t}^m v) = \lambda^k\mu^m \mathbf{q}^k\mathbf{t}^m((\lambda,\mu)\cdot v)$. Respectively we use notation $\mathbf{q}^k\mathbf{t}^m\cdot \calF\in \MF_{B^2}(\calX_2,W)$ for the matrix factorization with the same differentials as $\calF\in \MF_{B^2}(\calX_2,W)$ but the the twisted $T_{sc}$-equivariant structure of the underlying module.

Let us make a small clarification about the $t$-grading in our categories. Let $F$ be a potential on the space $\calZ$ and $\calZ$ has $T_{sc}=\CC^*_t\times \CC^*_q$ action such that $F$ has the weight $t^2$. Then we define $\MF(\calZ,F)$ to the homotopic category whose objects are $2$-quasi-periodic complexes: $$\dots \xrightarrow{D_{-1}}M_{0}\xrightarrow{D_0}M_1\xrightarrow{D_1}M_2\xrightarrow{D_2}\dots,$$ such that $D_{i+2}=D_i$ and $M_{i+2}=\mathbf{t}^2 \cdot M_i$ and $D_i$ are of degree $t$. In particular, if $F=0$ then for $\calF=(M_\bullet,D_\bullet)\in \MF(\calZ,F)$ we have well defined $T_{sc}$-equivariant modules: $$\SymbolPrint{\textup{H}^{even}}(\calF):=\textup{H}^0(M_\bullet,D_\bullet),\quad 
\SymbolPrint{\textup{H}^{odd}}(\calF):=\textup{H}^1(M_\bullet,D_\bullet).$$
