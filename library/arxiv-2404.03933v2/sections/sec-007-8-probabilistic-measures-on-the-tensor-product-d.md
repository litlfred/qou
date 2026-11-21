---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2)"
section_id: sec-007-8-probabilistic-measures-on-the-tensor-product-d
section_title: "Probabilistic measures on the tensor product decomposition"
section_number: 8
pages: 21-23
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.902
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of unity into direct sums"
---
[]{#probmeas label="probmeas"} Here we introduce some natural probabilistic measures on indecomposable components of $T(1)^{\otimes N}$ for big and small quantum $\mathfrak{sl}_2$ and we show that they are all induced by Markov processes.

## The character and the Plancherel measures for $U_q(\mathfrak{sl}_2)$ 

Let $X^{(l)}_N$ be the set of tilting modules of $U_q(\mathfrak{sl}_2)$ that occur in the decomposition of $T(1)^{\otimes N}$. It can be naturally identified with the subset of dominant integral weights of $\mathfrak{sl}_2$, i.e. with $k\in \mathbb{Z}_{\geq 0}$ such that $k\leq N$, $k\equiv N\,{\rm mod}\,2$. Define the multiplicity function on $\mathbb{Z}_{\geq 0}$ as the multiplicity of $T(k)\subset T(1)^{\otimes N}$ when $k\in X^{(l)}_N$ and zero otherwise.

::: definition
The character measure on $\mathbb{Z}_{\geq 0}$ is given by $$p^{(l)}_N(k;t)=\frac{M^{(l)}_{k}(N)\mathrm{ch}_{T(k)}(e^t)}{(\mathrm{ch}_{T(1)}(e^t))^N}.$$ Here $M^{(l)}_{k}(N)$ is the multiplicity function, $t$ is a real parameter and $\mathrm{ch}_{T(k)}(e^t)$ is the formal character from Lemma [\[fchar\]](#fchar){reference-type="ref" reference="fchar"} evaluated on $e^t$.
:::

Multiplicativity and additivity of characters imply that the character measure a probability measure, i.e. $\sum\limits_{k\in X^{(l)}_N} p^{(l)}_N(k;t)=1$. Recall that the multiplicity function is computed explicitly.

::: definition
[]{#planchdef label="planchdef"} When $t=0$ the character measure becomes the Plancherel measure $$p^{(l)}_N(k)=\frac{M^{(l)}_{k}(N)\dim T(k)}{(\dim  T(1))^N}.$$
:::

Dimensions of tilting modules can be easily derived from their formal characters: $$\dim T(k_0+lk_1)=
\begin{cases}
k_0+1,&\text{if $0\leq k_0\leq l-2$ and $k_1=0$,}\\
l(k_1+1), & \text{if $k_0=l-1$ and $k_1\in\mathbb{Z}_{>0}$,}\\
2k_1l,&\text{if $0\leq k_0\leq l-2$ and $k_1\in\mathbb{Z}_{>0}$.}
\end{cases}$$ It is clear that the Plancherel measure for $U_q(\mathfrak{sl}_2)$ is the specialization of the character measure at $t=0$. We distinguish it because as we will see that limit $N\to \infty$ is not interchangable with the limit $t\to 0$.

## The Plancherel measure for $u_q(\mathfrak{sl}_2)$ {#secplanch}

Now let us define the Plancherel measure on indecomposable components of $T(1)^{\otimes N}$ for $u_q(\mathfrak{sl}_2)$. Recall that in Section [\[small_lpm\]](#small_lpm){reference-type="ref" reference="small_lpm"} to each node of a graph in Figure [\[A-u-steps\]](#A-u-steps){reference-type="ref" reference="A-u-steps"} we assigned a tilting module. From now on we will use notation corresponding to this assignment:

-   $T(k)=T_+(k)$ when $l-1 \leq k\leq 2l-2$ and $m^{(l)}_{k}(N)=m^{(l)}_{k, +}(N)$,

-   $T(k)=T_-(k-l)$ when $2l-1 \leq k\leq 3l-2$ and $m^{(l)}_{k}(N)=m^{(l)}_{k-l, -}(N)$.

In this case, dimensions of indecomposable representations that occur in the decomposition of the tensor product $T(1)^{\otimes N}$ are written as follows $$\dim T(k)=
\begin{cases}
k+1,&\text{if $0 \leq k\leq l-2$,}\\
l, & \text{if $k=l-1,2l-1$,}\\
2l,& \text{otherwise.}
\end{cases}$$

::: definition
The Plancherel measure on indecomposable components of $u_q$-module $T(1)^{\otimes N}$ is $$p^{(l)}_N(k)=\frac{m^{(l)}_{k}(N)\dim T(k)}{(\dim  T(1))^N},\quad 0\leq k\leq 3l-2$$ and is zero for $k>3l-2$.
:::

## The quantum Plancherel measure for $u_q(\mathfrak{sl}_2)$. {#qdims}

Quantum dimension [@KR] of the irreducible $U_v(\mathfrak{sl}_2)$-module $V(k)$ is $$\dim_v(V(k))=\frac{v^{k+1}-v^{-k-1}}{v-v^{-1}}.$$ For quantum dimensions of modules that $T(k)$ which occur in the decomposition of $T(1)^{\otimes N}$ we have $$\dim_q(T(k))=\frac{q^{k+1}-q^{-k-1}}{q-q^{-1}}$$ for $0\leq k\leq l-2$. For other modules $T(k)$ quantum dimensions are zero.

Note that when $q=e^{\frac{i\pi}{l}}$ we have $\dim_q(T(k))\in\mathbb{R}_{\geq 0}$ for arbitrary values of $k$ and $\dim_q(T(k))\in\mathbb{R}_{> 0}$ for $0\leq k\leq l-2$.[^1]. It is not difficult to show that this is the only root of degree $l$ from $-1$ with such property.

::: definition
Quantum Plancherel measure is defined as $$p^{(l)}_N(k)=\frac{m^{(l)}_{T(k)}(N)\mathrm{dim}_qT(k)}{(\mathrm{dim}_q T(1))^N},\quad 0\leq k\leq l-2$$ and is zero for $k>l-2$.
:::

[^1]: This positivity is closely related to the unitarity of Wess-Zumino-Witten conformal field theory and of quantum Chern-Simons topological quantum field theory.
