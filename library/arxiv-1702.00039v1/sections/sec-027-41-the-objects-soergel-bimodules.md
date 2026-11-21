---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-027-41-the-objects-soergel-bimodules
section_title: "The objects: Soergel bimodules"
section_number: 4.1
pages: 20-22
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.985
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
In this section we will introduce Soergel bimodules in the baby example A, i.e. the symmetric group $S_3.$ This case is hard enough to start with and most of the features of general Soergel bimodules are already visible in this example.

Consider the polynomial ring $R=\mathbb{R}[x,y,z]$ (we could replace $\mathbb R$ by any field of characteristic different from $2$ in this section and the results would stay true). We have a natural action of $S_3$ on $R$. The simple reflection $s$ interchanges $x$ and $y$. In formulas $$s\cdot f(x,y,z)=f(y,x,z).$$ The simple reflection $r$ interchanges $y$ and $z$. So $R^s$ (the subset of $R$ fixed by the action of $s$) is the polynomial ring $\mathbb{R}[x+y, xy, z]$ and $R^r=\mathbb{R}[x, y+z,yz].$ The subring fixed by both simple reflections $s$ and $r$ (or, what is the same, by the whole group $S_3$) is $$R^{s,r}=\mathbb{R}[x+y+z,xy+xz+yz,xyz].$$

If we want to enter into Soergel-bimoduland (this is an invented word) we have to take the grading into account. For technical reasons we need $R$ to have the usual $\mathbb{Z}$-grading multiplied by two. So $x,y$ and $z$ will be in degree $2$ (there are no elements of odd degree). The polynomials $x^2$ and $xz$ have degree $4$, the polynomial $3xy^2z^7$ has degree $20.$ And we define the ring $R$ shifted "down" by one $R(1)$ by declaring that $x$ is in degree $1$, $x^2$ in degree $3$ and $3xy^2z^7$ in degree $19.$ Formally, if $B=\oplus_{i\in \mathbb{Z}}B_i$ is a graded object, we declare that the shifted object $B(m)$ in degree $i$ is $B(m)_i:=B_{m+i}.$

The $\mathbb{Z}$-graded $R-$bimodule $R$ is the easiest example of a Soergel bimodule. The second example of a Soergel bimodule is the $\mathbb{Z}$-graded $R-$bimodules $B_s:=R\otimes_{R^s}R(1)$, for $s\in S$. Just for pedagogical reasons we insist that in $B_s$ the elements $x\otimes y$ and $z^2\otimes1 +1\otimes xz$ have degree $3$ and $x^3\otimes zx$ has degree $9.$

Another example is the product $B_s\otimes_R B_r$, that we will call (for reasons that will be clear later) $B_{sr}.$ Another example of a Soergel bimodule for $S_3$ is the $\mathbb{Z}$-graded $R-$bimodule $B_{srs}:=R\otimes_{R^{s,r}}R(3)$.

We will use the convention that if $M$ and $N$ are two $R-$bimodules then their "product" is defined by $$MN:=M\otimes_R N.$$

We can now introduce the category of Soergel bimodules $\mathcal{B}(S_3)$ in our baby example $S_3$. They are $\mathbb{Z}$-graded $R-$bimodules that are isomorphic to direct sums and grading shifts of the following set of $\mathbb{Z}$-graded $R-$bimodules $$\mathbb I=\{R, B_s, B_r, B_{sr}, B_{rs}, B_{srs}\}.$$

**Philosphy:** *One should think of $B_s$, $B_sB_r$ and $B_{srs}$ as analogous objects to the elements $b_s$, $b_{sr}$ and $b_{srs}$ respectively in the Hecke algebra. One should also think of the product (resp. direct sum) between Soergel bimodules as an analogue of product (resp. sum) in the Hecke algebra. Shifting the degree of a Soergel bimodule by one should be seen as multiplying the corresponding element in the Hecke algebra by $v$. We will make this statement precise at some point.*

This philosophy will gently emerge in the following pages. Recall that the Hecke algebra $\mathcal H(S_3)$ is free over $\mathbb Z[v,v^{-1}]$ with basis $$\{1, b_s, b_r,b_{sr}, b_{rs},b_{srs}\}.$$
