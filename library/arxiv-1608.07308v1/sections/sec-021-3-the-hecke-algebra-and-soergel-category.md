---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-021-3-the-hecke-algebra-and-soergel-category
section_title: "The Hecke algebra and Soergel category"
section_number: 3
pages: 19-20
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.941
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sec:Sbim label="sec:Sbim"}

## The Hecke algebra

Recall that the Hecke algebra of type $A_n$ has $n-1$ generators: $$H_n = \mathbb{C}(q) \langle \sigma_1,...,\sigma_{n-1} \rangle$$ modulo relations: $$\label{eqn:hecke1}
\left(\sigma_i-q^{\frac 12} \right)\left(\sigma_i+q^{-\frac 12} \right) = 0 \ \qquad \ \forall \ i\in \{1,\ldots,n-1\}$$ $$\label{eqn:hecke2}
\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1} \qquad \forall \ i\in \{1,\ldots,n-2\}$$ $$\label{eqn:hecke3}
\sigma_i\sigma_j = \sigma_j\sigma_i \qquad \quad \ \ \forall \ |i-j|>1.$$ The algebra $H_n$ is a $q$-deformation of the group algebra of the symmetric group $\mathbb{C}[S_n]$. The irreducible representations $V_{\lambda}$ of $H_n$ at generic parameter $q$ are labeled by partitions of $n$, or, equivalently, by Young diagrams of size $n$. The multiplicity of $V_{\lambda}$ in the regular representation is equal to its dimension, which is itself equal to the number of standard Young tableaux (henceforth abbreviated SYT) of shape $\lambda$. Therefore, the regular representation of $H_n$ splits into a direct sum of irreducible representations labeled by standard tableaux. For each such tableau $T$, let $P_T$ denote the projector onto the irreducible summand in $H_n$ labeled by $T$. By construction, these projectors have the following properties: $$\label{proj}
P_T P_{T'} = \delta_{T'}^T P_T, \qquad \sum_{T}P_{T}=1.$$ The projectors $P_T$ can be written very explicitly in terms of the generators $\sigma_i$, see [@AiMor; @gyoja] for details. They satisfy the following **branching rule**: $$\label{branching}
i(P_T)=\sum_{\square}P_{T+\square},$$ where $i:H_n\to H_{n+1}$ is the natural inclusion and the summation in the right hand side is over all possible SYT obtained from $T$ by adding a single box labeled by $n+1$.

The renormalized **Markov trace** $\chi: H_n \to \mathbb{C}(a,q)$ satisfies the relations: $$\chi(\sigma \sigma ') = \chi(\sigma'  \sigma), \qquad
\chi(i(\sigma)) = \chi(\sigma) \cdot \frac{1-a}{q^{\frac 12}-q^{-\frac 12}}, \qquad
\chi(i(\sigma) \sigma_n) = \chi(\sigma).$$ There is a natural pairing $\langle  \cdot, \cdot \rangle:  H_n \times H_n \to \mathbb{C}(a,q)$ given by $\langle \sigma, \tau \rangle = \chi(\sigma \tau ^\dagger)$, where $\sigma^\dagger$ is the "Hermitian conjugate" of $\sigma$ (this is the $\mathbb{C}$-antilinear map determined by the relations $q^\dagger = q^{-1}$, $\sigma_i^\dagger = \sigma _i^{-1}$, and $(\sigma \tau )^\dagger = \tau^\dagger \sigma ^\dagger$). With respect to this pairing, the adjoint of the inclusion $i: H_n \to H_{n+1}$ is the **partial Markov trace**: $$\mathop{\mathrm{Tr}}: H_{n+1} \to H_n \otimes \mathbb{C}[a].$$ It follows easily from the definitions that for all $\sigma \in H_n$, we have $\chi(\sigma) = \mathop{\mathrm{Tr}}^n(\sigma).$

The Markov trace of a projector $P_T$ only depends on the underlying Young diagram $\lambda$ of the SYT $T$, and is equal to the $\lambda$-colored HOMFLY-PT polynomial of the unknot. Specifically, we have the following result:

::: proposition
(e.g. [@Ai]) The Markov trace of $P_T$ equals: $$\mathop{\mathrm{Tr}}^n(P_T)=\prod_{\square\in \lambda}\frac{1-aq^{c(\square)}}{1-q^{h(\square)}},$$ where $c(\square)$ and $h(\square)$ respectively denote the content and the hook length of a square $\square$ in $\lambda$.
:::
