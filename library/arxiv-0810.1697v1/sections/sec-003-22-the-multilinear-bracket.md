---
doc_id: arxiv-0810.1697v1
doc_title: "ON THE CABLE EXPANSION FORMULA"
section_id: sec-003-22-the-multilinear-bracket
section_title: "The multilinear bracket"
section_number: 2.2
pages: 3-5
source_pdf: 0810.1697v1.pdf
source_sha256: 1aef66179da3c154
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.971
doc_brief: "ON THE CABLE EXPANSION FORMULA — In this paper, a generalized version of Morton’s formula [8] is proved."
---
[]{#multilinear bracket label="multilinear bracket"} Given an framed link $L$ in $M$ with components $K_1,K_2,...K_m$, denote the framing of $K_j$ by $\sigma_j$. A multilinear bracket $\langle *,*,...,*\rangle_L$ in $S(M)$ can be constructed as following:

 

The framing $\sigma_j$ of $K_j$ determines a diffeomorphism $$\tau_j:D\times S^1 \to a\ tubular\ neighbourhood\ of\ K_j.$$ $\tau_j$ gives a map $D\times S^1 \to M$. It induces a homomorphism $$(\tau_j)_*:S(D\times S^1) \to S(M).$$ These $(\tau_j)_*$ combine together to give a multi-linear map $$\tau_*: S(D\times
S^1)\times S(D\times S^1)\times ...\times S(D\times S^1)\to S(M)$$ where the product contains $m$ factors.

Define $\langle
x_1,x_2,...,x_m\rangle_L$ to be $\tau_*(x_1,x_2,...,x_m)$.

 

Components of $L$ can be colored by integers. Assume $K_j$ is colored by $n_j$, then the colored framed link $L$ gives an element in $S(M)$, that is $\langle e_{n_1},e_{n_2},...,e_{n_m}\rangle_L$.

::: remark
Change the framing of certain components of $L$, while keeping the colors unchanged, for example $\sigma_1$ is changed to $\sigma_1+b$, where $b$ is an integer. Then $$\langle e_{n_1},e_{n_2},...,e_{n_m}\rangle_{L'}=(-1)^{bn_1}A^{b(n_1^2+2n_1)}\langle e_{n_1},e_{n_2},...,e_{n_m}\rangle_L$$ where $L'$ is the same link as $L$ with changed framings.
:::

### Examples

Let $K$ be a knot in $S^3$ with framing $\sigma$, the n-th colored Jones polynomial of K, $J_n^{\sigma}(A,K)$, is defined to be $\langle e_n
\rangle_K$,which is an element of $S(S^3)$. Since $S(S^3)$ is equal to $Z[A,A^{-1}]$, this element is a Laurent polynomial in A.

In particular, $$\langle e_n\rangle_U=(-1)^n[n+1]$$ where $U$ is the unknot with framing zero, and $[m]=\frac{A^{2m}-A^{-2m}}{A^2-A^{-2}}$.

Let L be the following link in $D\times S^1$: $$\scalebox{.25}{\psfig{file=link-L1.eps}}$$

Here both components have framing 0, --- consult the framing convention below. Then we have $$\langle e_m,e_n\rangle_L=(-1)^m \frac{[(m+1)(n+1)]}{[n+1]} e_n$$

If $K$ has framing 0, $J_n(A,K)$ is used for the colored Jones polynomial instead of $J_n^0(A,K)$.

### The framing convention

Since the linking number of two oriented knots in $S^3$ is defined, the framing of a knot in $S^3$ can be specified by an integer, the linking number.

For an arbitrary 3-manifold $M$, the framing of a knot $K$ in $M$ can't be specified by an integer. It is only possible under certain circumstances.

For example, $M$ is the solid torus $D\times S^1$ with a chosen curve $C_+$, $\{1\}\times S^1$, on its boundary. Embed $M$ into $S^3$. A framed knot $K$ in $M$ is then mapped to a framed knot in $S^3$. Its framing corresponds to an integer. In general the corresponding integer will change if the embedding is changed. If $D\times S^1$ is embedded into $S^3$ in such a way that $C_+$ has linking number zero with the core of the solid torus after the embedding, the corresponding integer will be the same for all such embeddings.

In the following, a knot $K$ in $D\times S^1$ is said to have framing n for some integer n in the sense that the knot is viewed as a knot in $S^3$ through such kind of embedding of $D\times S^1$ into $S^3$.
