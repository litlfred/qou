---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-005-24-the-associative-multiplication-algebras-of-o
section_title: "The Associative Multiplication Algebras of O"
section_number: 2.4
pages: 7-8
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.784
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
The non-associativity of $\mathbb{O}$ means that the algebra is not representable as a matrix algebra (with the standard matrix product). The algebra generated from the composition of left (and/or right) actions of $\mathbb{O}$ on itself, however, is associative, since each such left (right) action corresponds to a linear operator (endomorphism). Suppose that $a,x$ are elements of some algebra $\mathbb{A}$, and define: $$L_a[x]:=ax,\quad R_a[x]:=xa,\quad \forall a,x\in  \mathbb{A} \:.$$ It is clear that $L_a$ and $R_a$ denote linear operator corresponding to left and right multiplication of $x\in \mathbb{A}$ by $a\in \mathbb{A}$, respectively. These maps send the element $x\in\mathbb{A}$ to some other element $y\in\mathbb{A}$, and thus $L_a$ and $R_a\in \text{End}(\mathbb{A)}$. The mappings $a\mapsto L_a$ and $a\mapsto R_a$ do not correspond to algebra homomorphisms. Instead, via composition each generates an associative algebra referred to as the *associative multiplication algebra*.

Note in particular, that for a non-associative algebras such as $\mathbb{O}$, $$\begin{aligned}
    L_aL_b[x] &=a(bx) \quad \neq \quad L_{ab}[x]=(ab)x,\\
    R_aR_b[x] &=(xb)a \quad \neq \quad R_{ab}[x]=x(ab),\quad\forall a,b,x\in\mathbb{O}.
\end{aligned}$$ We denoted by $\mathbb{O}_L$ and $\mathbb{O}_R$, the left and right associative multiplication algebras of octonions respectively, which we will henceforth refer to simply as the *left (right) multiplication algebra*[^1] These linear maps preserve the quadratic relations $\langle x,y\rangle=\frac{1}{2}(x\overline{y}+y\overline{x})$, where $x,y\in \mathbb{O}$ $$L_xL_{\overline{y}}1+L_yL_{\overline{x}}1=2\langle x,y \rangle 1=R_xR_{\overline{y}}1+R_yR_{\overline{x}}1 \:.$$

Since $L_a$ ($R_a$) correspond to linear operators, they can be represented as $8\times 8$ real matrices acting on the vector space $\mathbb{O}$ written as a column vector.

Within $\mathbb{O}_L$, one finds the following identities [@dixon2013division; @furey2016standard]: $$\begin{aligned}
    L_{e_1}L_{e_2}L_{e_3}L_{e_4}L_{e_5}L_{e_6}x &= L_{e_7}x,\\
    ...L_{e_b}L_{e_a}L_{e_a}L_{e_c}....x &= -...L_{e_b}L_{e_c}....x,\\
    ...L_{e_a}L_{e_b}...x &= -...L_{e_b}L_{e_a}...,
\end{aligned}$$ where $a,b,c=1,...,7$.

The non-associativity of $\mathbb{O}$ means that $\mathbb{O}_L$ ($\mathbb{O}_R$) contains genuinely new maps which are not captured by $\mathbb{O}$ itself. For example, $e_3(e_4(e_6+e_2))\neq y(e_6+e_2)$ for any $y\in\mathbb{O}$. There are a total of 64 distinct left-acting real linear maps from $\mathbb{O}$ to itself, and these (due to the given identities above) provide a faithful representation of the real Clifford algebra $C\ell(0,6)$. Furthermore, any left (right) adjoint action can always be rewritten as a right (left) adjoint action, so that $\mathbb{O}_L=\mathbb{O}_R$ [@dixon2013division].

For the complex octonions, $\mathbb{C}\otimes\mathbb{O}$, the left (right) multiplication algebra is likewise complexified and becomes the complex Clifford algebra $\mathbb{C}\ell(6)$, having complex dimension $64$.

[^1]: We remark that the left multiplication algebra is also referred to as the *octonionic chain algebra* $\mathbb{C}\otimes \overleftarrow{\mathbb{O}}$; see for example [@furey2016standard].
