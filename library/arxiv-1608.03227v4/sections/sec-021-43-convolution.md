---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-021-43-convolution
section_title: "Convolution"
section_number: 4.3
pages: 22-22
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.974
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
There are three natural projection maps $\SymbolPrint{\pi_{12},\pi_{23},\pi_{13}}:\calX_3\to\calX_2$ and $\pi_{12}^*(W)+\pi_{23}^*(W)=\pi_{13}^*(W)$. If we extend the action of $G\times B^2$ on $\calX_2$ to the action of $G\times B^3$ by natural projectors $\pi_{ij}:G\times B^3\to G\times B^2$ then the maps $\pi_{ij}$ become $G\times B^3$-equivariant and hence

for any $\calF,\calG\in \MF_{B^2}(\calX_2,W)$ we can define an object $$\pi_{12}^*(\calF)\otimes\pi_{23}^*(\calG)\in \MF_{B^3}(\calX_3,\pi_{13}^*(W)).$$

Naively we could define the convolution between $\calF$ and $\calG$ as a quotient of the tensor product by the action of the second copy $B^{(2)}$ of $B$ inside $G\times B^3$. We define a derived quotient with the help of the Chevalley-Eilenberg complex, we also explain how to define the convolution in a bigger category $\MF_{B^2}(\calZ,W)$.

Let $\calF,\calG\in \MF_{B^2}(\calX_2,W)$, $\calF=(M,D,\partial_l,\partial_r)$, $\calG=(\tilde{M},\tilde{D},\tilde{\partial}_l,\tilde{\partial}_r)$. The tensor product $M\otimes\tilde{M}$ is naturally a module over $B^3$ with the action $(b_1,b_2,b_3)(m\otimes\tilde{m})=(b_1,b_2)\cdot m\otimes (b_2,b_3)\cdot \tilde{m}$, hence we can define a tensor product of pull backs $\pi_{12}^*(\calF)$ and $\pi_{23}^*(\calG)$ as an object of $\MF_{B^3}(\calX_3,\pi_{13}^*(W))$: $$\pi_{12}^*(\calF)\otimes \pi_{23}^*(\calG)=(\pi_{12}^*(M)\otimes\pi_{23}^*(\tilde{M}),D+\tilde{D},\partial_l,\partial_r+\tilde{\partial}_l,\tilde{\partial}_r).$$

From here on we use notation $\SymbolPrint{\frn^{(1)},\frn^{(2)},\frn^{(3)}}$ for the first, second and third copy of $\frn$ on $\frn^3$; respectively for given $\frn^3$ module $M$ we denote by $d^{(i)}_{ce}$ the Chevalley-Eilenberg differential on $\CE_{\frn^3}\odel M$ corresponding $i$-th copy of $\frn$.

The complex $\CE_\frn$ is $T$-equivariant hence $T^{(2)}$-invariant part $\CE_{\frn^{(2)}}(\pi_{12}^*(\calF)\otimes\pi_{23}^*(\calG))^{T^{(2)}}$ is the matrix factorization from $\MF_{B^2}(\calX_3/B_{(2)},\pi_{13}^*(W))$. In more details: $\CE_{\frn^{(2)}}(\pi_{12}^*(\calF)\otimes_B\pi_{23}^*(\calG))^{T^{(2)}}$ is the matrix factorization with underlying module $$\CE_{\frn^{(2)}}(\pi_{12}^*(M)\otimes\pi_{23}^*(\tilde{M}))^{T^{(2)}}:=\Hom_{\frn^{(2)}}(\CE_{\frn^{(2)}},\CE_{\frn^{(2)}}\odel \left( \pi_{12}^*(M)\otimes\pi_{23}^*(\tilde{M}) \right))^{T^{(2)}},$$ the matrix factorization differential $D^{(2)}:=d^{(2)}_{ce}+\partial_r+\tilde{\partial}_l+D+\tilde{D}$ and $\frn^{(1)}\times\frn^{(2)}$ equivariant structure differentials are $\partial_l,\tilde{\partial}_r.$

In particular $(\CE_{\frn^{(2)}}(\pi_{12}^*(M)\otimes\pi_{23}^*(\tilde{M}))^{T^{(2)}}, D^{(2)})$ is a complex over the ring $\pi_{13}^*(\CC[\calX_2])\subset\CC[\calX_3]^{\frb_{(2)}}$ and as such it is an object of $\MF_{B^2}(\calX,W)$ which we denote $\pi_{13*}(\CE_{\frn_{(2)}}(\pi_{12}^*(\calF)\otimes\pi_{23}^*(\calG))^T_{(2)}$. The last complex provides us a bilinear operation on $\MF_{B^2}(\calX_2,W)$: $$\begin{gathered}
\label{eq: convolution}
\calF\SymbolPrint{\star}\calG:=\pi_{13*}(\CE_{\frn^{(2)}}(\pi_{12}^*(\calF)\otimes\pi_{23}^*(\calG))^{T^{(2)}})=\\(\CE_{\frn^{(2)}}(\pi_{12}^*(M)\otimes\pi_{23}^*(\tilde{M}))^{T^{(2)}},D^{(2)},\partial_l,\tilde{\partial}_r).
 
\end{gathered}$$ The proof of the following proposition is standard: it literally repeats the proof of the associativity of the convolution from the book [@CG]:

::: proposition
The binary operation $\star$ defines a strictures of associative algebra on $\MF_{B^2}(\calX_2,W)$.
:::
