---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2)"
section_id: sec-005-6-multiplicities-and-lattice-paths
section_title: "Multiplicities and lattice paths"
section_number: 6
pages: 14-18
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.944
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of unity into direct sums"
---
[]{#rec-mult label="rec-mult"} Here we reformulate the problem of tensor power decomposition over $U_q(\mathfrak{sl}_2)$ and $u_q(\mathfrak{sl}_2)$ resolved in the previous section in terms of counting lattice paths on the set of dominant weights for the corresponding quantum groups and will give a combinatorial derivation of multiplicity formulae for $T(1)^{\otimes N}$ derived before.

## Lattice path model for tensor power decomposition of $U_q(\mathfrak{sl}_2)$-modules {#lpm}

### Elementary steps and lattice paths.

Tensor product decomposition ([\[A\]](#A){reference-type="ref" reference="A"}) can be regarded as the description of a lattice walk on the set of integral dominant weights which is for $U_q(\mathfrak{sl}_2)$ is $\mathbb{Z}_{\geq 0}=\{0,1,2,\dots\}$.

Let us describe elementary steps of such a walk. We will refer to points of the weight space $\mathbb{Z}_{\geq 0}$ also as nodes (of our lattice walk). We will say a step has multiplicity $2$ if it is counted twice (see below). If the multiplicity of a step is not specified, we assume it has multiplicity one.

1.  From the node $k$, when $k\neq ml-2, ml-1, ml$ there are two possible steps, one to $k+1$ and one to $k-1$.

2.  From the node $ml-2$ ($m\geq 3$) only steps to $ml-1, ml-3, (m-2)l-1$ are possible. From $2l-2$ there are only steps to $2l-1$ and $2l-3$.

3.  From the node $ml-1$ there is one step leading to the node $ml$.

4.  From the node $ml$ there is a multiplicity $2$ step to the node $ml-1$ and simple (multiplicity one) step to $ml+1$.

Denote the set of these elementary steps $S_U$. They can be described by a diagram on Figure [1](#elem-steps){reference-type="ref" reference="elem-steps"}.

![The set of elementary steps $\mathbb{S}_U$, where red arrows denote steps of multiplicity 2.](A-steps.pdf){#elem-steps width="350pt"}

A graph of such lattice walk is a lattice path in $\mathcal{L}_U=\mathbb{Z}_{\geq 0}\times \mathbb{Z}_{\geq 0}$ with points $(x,y)$ where $x\in \mathbb{Z}_{\geq 0}$ is a dominant weight and $y$ is the degree $N$ is the tensor power $T(1)^{\otimes N}$. The set of elementary steps $\mathbb{S}_U$ for such lattice paths is $$\mathbb{S}_U=\{((x,y), (x',y+1))\,|\, (x,x')\in S_U\}$$ Note that multiplicities of elementary steps define weights on $\mathbb{S}_U$. For large $k=lk_1+k_0$ the graph of elementary steps is $2l$-periodic.

Examples of such lattice paths are given on Figure [2](#two-paths){reference-type="ref" reference="two-paths"}.

![Two paths with elementary steps from $\mathbb{S}_U$. Red lines indicate elementary steps with multiplicity 2. A vertex with coordinate $(k,N)$ represents the highest weight $k$ of the tilting module $T(k)\subset T(1)^{\otimes N}$. The number of lattice paths from the origin to $(k,N)$ is the multiplicity $M_k^{(l)}(N)$. Elementary steps $\mathbb{S}_U$ from a vertex on this lattice are represented by possible lines down the lattice. Similarly, the number of paths starting at $(n,0)$ and descending to $(k,N)$ is the multiplicity of the tilting module $T(k)\subset T(n)\otimes T(1)^{\otimes N}$.](Untitled1.pdf){#two-paths width="250pt"}

Using recursive formulae ([\[A\]](#A){reference-type="ref" reference="A"}) for the decomposition of tensor products and the corresponding lattice path model, these multiplicities can be described as follows:

::: theorem
[]{#U-model label="U-model"} The multiplicity of the tilting $U_q(\mathfrak{sl}_2)$-module $T(k)$ in the decomposition of $T(1)^{\otimes N}$ is equal to the weighted number of lattice paths on $\mathcal{L}_U$ connecting $(0,0)$ and $(k,N)$ with weights given by multiplicities of elementary steps $\mathbb{S}_U$.
:::

Path counting formula for this lattice path model was derived in [@Sol] where the number of paths was computed explicitly in terms $F_k^{(N)}$ using combinatorial methods such as reflection principle. This formula coincides with expressions ([\[p-numbers\]](#p-numbers){reference-type="ref" reference="p-numbers"}).

## Lattice path model for decomposition of tensor powers of $u_q(\mathfrak{sl}_2)$-modules {#small_lpm}

### Elementary steps and lattice paths

In this case the lattice is $\mathcal{L}_u=\{0,1,\dots, 3l-2\}\times \mathbb{Z}_{\geq 0}$. The following set of elementary steps is determined by the decomposition rules ([\[B\]](#B){reference-type="ref" reference="B"}).

1.  From the node $0$ there is only one step to $1$.

2.  From the node $k$, when $k\neq ml-2,ml-1,ml$ there are two possible steps, one to $k+1$ and one to $k-1$.

3.  From the node $2l-2$ there is a step to $2l-1$ with multiplicity $2$ and a step to $2l-3$.

4.  From the node $3l-2$ there is a step to $l-1$ with multiplicity $2$ and a step to $3l-3$.

5.  From the node $ml-1$ there is only step to $ml$.

6.  From the node $ml$ there is a step to $ml-1$ with multiplicity $2$ and a step to $ml+1$.

The set $S_u$ can be characterized by the diagram on Figure [3](#A-u-steps){reference-type="ref" reference="A-u-steps"}.

![The set of elementary steps $\mathbb{S}_u$, where red arrows denote steps of multiplicity 2.](A-u-steps.pdf){#A-u-steps width="250pt"}

A graph of such lattice walk is a lattice path in $\mathcal{L}_u$ with points $(x,y)$ where $x\in \mathbb{Z}_{\geq 0}$ is a dominant weight and $y$ is the degree $N$ is the tensor power $T(1)^{\otimes N}$. Nodes of this graph are identified with tilting modules as follows:

-   To each node $0\leq m \leq l-2$ we assign module $T(m)$, where $T(0)=\mathbb{C}$;

-   To each node $l-1\leq m \leq 2l-2$ we assign module $T_+(m)$;

-   To each node $2l-1\leq m \leq 3l-2$ we assign module $T_-(m-l)$.

The set of elementary steps $\mathbb{S}_u$ is given by $$\mathbb{S}_u=\{((x,y), (x',y+1))\,|\, (x,x')\in S_u\}$$ Multiplicities of elementary step define weights on $\mathbb{S}_u$.

Examples of such lattice paths are given on Figure [4](#two-paths-u){reference-type="ref" reference="two-paths-u"}.

![Two paths with elementary steps from $\mathbb{S}_u$. Red arrows indicate elementary steps with multiplicity 2. A vertex with coordinate $(k,N)$ represents the highest weight $k$ of the tilting module $T(k)\subset T(1)^{\otimes N}$. The number of lattice paths from the origin to $(k,N)$ is the multiplicity $m_k^{(l)}(N)$. Elementary steps $\mathbb{S}_u$ from a vertex on this lattice are represented by possible lines down the lattice. Similarly, the number of paths starting at $(n,0)$ and descending to $(k,N)$ is the multiplicity of the tilting module $T(k)\subset T(n)\otimes T(1)^{\otimes N}$.](Untitled2.pdf){#two-paths-u width="250pt"}

Using recursive formulae ([\[B\]](#B){reference-type="ref" reference="B"}) we arrive to the following theorem describing multiplicities in terms of lattice paths:

::: theorem
[]{#u-model label="u-model"} The multiplicity of the tilting $u_q(\mathfrak{sl}_2)$-module $T(k)$ in the decomposition of $T(1)^{\otimes N}$ is equal to the weighted number of lattice paths in $\mathcal{L}_u$ connecting $(0,0)$ and $(k,N)$ with weights given by multiplicities of elementary steps $\mathbb{S}_u$.
:::

Now we can compute multiplicities using the lattice path model and compare the formulae with the ones that we already derived in Theorem [\[small_mult\]](#small_mult){reference-type="ref" reference="small_mult"}

::: theorem
[]{#th_u label="th_u"}

1.  The number of lattice paths is given by the following formulae. For $k_0\neq l-1$ we have $$\label{ind1}
            m^{(l)}_{l+k_0,+}(N)=\sum_{k=1}^{\lfloor\frac{N}{2l}\rfloor}k^2F^{(N)}_{k_0-l-2kl}+\sum_{k=0}^{\lfloor\frac{N-l}{2l}\rfloor}(k+1)^2 F^{(N)}_{k_0+l+2kl}$$ $$\label{ind3}
            m^{(l)}_{l+k_0,-}(N)=\sum_{k=1}^{\lfloor\frac{N-l}{2l}\rfloor}(k^2+k)F^{(N)}_{k_0-2l-2kl}+\sum_{k=0}^{\lfloor\frac{N-2l}{2l}\rfloor}((k+1)^2+(k+1)) F^{(N)}_{k_0+2l+2kl}$$ For $T_{+}(l-1)$, $T_{-}(l-1)$ the multiplicities are: $$m^{(l)}_{l-1,+}(N)=\sum_{k=0}^{\lfloor\frac{N}{2l}+\frac{1}{2}\rfloor}(2k+1)F^{(N)}_{l-1+2kl},$$ $$m^{(l)}_{l-1,-}(N)=\sum_{k=0}^{\lfloor\frac{N}{2l}+1\rfloor}(2k+2)F^{(N)}_{2l-1+2kl},$$ Note that in these formulae some $F^{(N)}_m$ can be negative.

2.  These numbers are exactly the same as in Theorem [\[small_mult\]](#small_mult){reference-type="ref" reference="small_mult"}.
:::

The proof of this theorem is given in Appendix [\[prthu\]](#prthu){reference-type="ref" reference="prthu"}.
