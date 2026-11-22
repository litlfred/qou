---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-005-24-quantum-gv-invariant
section_title: "Quantum (g,V) invariant"
section_number: 2.4
pages: 8-10
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 0.932
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
One of the important ways to construct an enhanced Yang--Baxter operator is to use a quantum group, which is a deformation of a Lie algebra.

Let $\mathfrak{g}$ be a Lie algebra. Then one can define a quantum group $U_q(\mathfrak{g})$ as a deformation of $\mathfrak{g}$ with $q$ a complex parameter ([@Drinfeld:ICM86], [@Jimbo:LETMP1985]). Given a representation $\rho\colon\mathfrak{g}\to\mathfrak{gl}(V)$ of $\mathfrak{g}$ one can construct an enhanced Yang--Baxter operator. The corresponding invariant is called the quantum $(\mathfrak{g},V)$ invariant. For details see [@Turaev:INVEM88].

To define the colored Jones polynomial we need the Lie algebra $\mathfrak{sl}_2(\mathbb{C})$ and its $N$-dimensional irreducible representation $\rho_N\colon\mathfrak{sl}_2(\mathbb{C})\to\mathfrak{gl}(V_N)$. The quantum $(\mathfrak{sl}_2(\mathbb{C}),V_N)$ invariant is called the $N$-dimensional colored Jones polynomial $J_N(L;q)$.

A precise definition is as follows.

Put $V:=\mathbb{C}^N$ and define the $R$-matrix $R\colon V\otimes V\to V\otimes V$ by $$R(e_k\otimes e_l)
  :=
  \sum_{i,j=0}^{N-1}R_{kl}^{ij}e_{i}\otimes e_{j},$$ where $$\label{eq:R}
\begin{split}
  R^{ij}_{kl}
  :=&
  \sum_{m=0}^{\min(N-1-i,j)}
  \delta_{l,i+m}\delta_{k,j-m}
  \frac{\{l\}!\{N-1-k\}!}{\{i\}!\{m\}!\{N-1-j\}!}
  \\
  &
  \times q^{\bigl(i-(N-1)/2\bigr)\bigl(j-(N-1)/2\bigr)-m(i-j)/2-m(m+1)/4},
\end{split}$$ with $\{e_0,e_1,\dots,e_{N-1}\}$ is the standard basis of $V$, $\{m\}:=q^{m/2}-q^{-m/2}$ and $\{m\}!:=\{1\}\{2\}\cdots\{m\}$. Here $q$ is a complex parameter. A homomorphism $\mu\colon V\to V$ is given by $$\mu(e_j)
  :=
  \sum_{i=0}^{N-1}\mu^i_j e_i$$ with $$\mu^i_j
  :=
  \delta_{i,j}q^{(2i-N+1)/2}.$$

Then it can be shown that $(R,\mu,q^{(N^2-1)/4},1)$ gives an enhanced Yang--Baxter operator.

::: definition
For an integer $N\ge1$, put $V:=\mathbb{C}^N$ and define $R$ and $\mu$ as above. The $N$-dimensional colored Jones polynomial $J_N(L;q)$ for a link $L$ is defined as $$J_N(L;q):=T_{(R,\mu,q^{(N^2-1)/4},1)}(\beta)\times\frac{\{1\}}{\{N\}},$$ where $\beta$ is a braid presenting the link $L$.
:::

::: remark
Note that $J_N(\text{unknot};q)=1$ since $$\operatorname{Tr}_1(\mu)
  =
  \sum_{i=0}^{N-1}
  q^{(2i-N+1)/2}
  =
  \frac{\{N\}}{\{1\}}.$$
:::

The two-dimensional colored Jones polynomial $J_2(L;q)$ is (a version) the original Jones polynomial [@Jones:BULAM385] as shown below.

::: lemma
Let $L_+$, $L_-$, and $L_0$ be a skein triple, that is, they are the same links except for a small disk as shown in Figure $\ref{fig:skein_triple}$.

<figure id="fig:skein_triple">
<p><embed src="crossing_pos_small.eps" />, <embed src="crossing_neg_small.eps" />, <embed src="crossing_null_small.eps" /></p>
<figcaption>skein triple</figcaption>
</figure>

Then we have the following skein relation: $$q J_2(L_+;q)-q^{-1}J_2(L_-;q)=(q^{1/2}-q^{-1/2})J_2(L_0;q).$$
:::

::: proof
*Proof.* By the definition, the $R$-matrix is given by $$R
  =
  \begin{pmatrix}
    q^{1/4}&0               &0       &0 \\
    0      &q^{1/4}-q^{-3/4}&q^{-1/4}&0 \\
    0      &q^{-1/4}        &0       &0 \\
    0      &                &0       &q^{1/4}
  \end{pmatrix}$$ with respect to the basis $\{e_0\otimes e_0,e_0\otimes e_1,e_1\otimes e_0,e_1\otimes e_1\}$ of $V\otimes V$, and $\mu$ is given by $$\mu
  =
  \begin{pmatrix}
    q^{-1/2}&0 \\
    0       &q^{1/2}
  \end{pmatrix}$$ with respect to the basis $\{e_0,e_1\}$ of $V$.

Therefore we can easily see that $$\label{eq:skein_R}
  q^{1/4}R-q^{-1/4}R^{-1}
  =
  (q^{1/2}-q^{-1/2})\operatorname{Id}_V\otimes\operatorname{Id}_V.$$

Since $L_+$, $L_-$, and $L_0$ can be presented by $n$-braids $\beta\sigma_i\beta'$, $\beta\sigma_i^{-1}\beta'$, and $\beta\beta'$ respectively, we have $$\begin{split}
  &
  \left(
    qJ_2(L_+;q)
    -
    q^{-1}J_2(L_-;q)
  \right)
  \times\frac{\{2\}}{\{1\}}
  \\
  =&
  q\times
  q^{-3(w(\beta\beta')+1)/4}
  \operatorname{Tr}_1(\operatorname{Tr}_2(\cdots(\operatorname{Tr}_n(\Phi(\beta\sigma_i\beta')\mu^{\otimes n}))))
  \\
  &\quad
  -
  q^{-1}\times
  q^{-3(w(\beta\beta')-1)/4}
  \operatorname{Tr}_1(\operatorname{Tr}_2(\cdots(\operatorname{Tr}_n(\Phi(\beta\sigma_i^{-1}\beta')\mu^{\otimes n}))))
  \\
  =&
  q^{-3w(\beta\beta')/4}
  \\
  &\times
  \left(
    q^{1/4}
    \operatorname{Tr}_1(\operatorname{Tr}_2(\cdots(\operatorname{Tr}_n(\Phi(\beta\sigma_i\beta')\mu^{\otimes n}))))
    -
    q^{-1/4}
    \operatorname{Tr}_1(\operatorname{Tr}_2(\cdots(\operatorname{Tr}_n(\Phi(\beta\sigma_i^{-1}\beta')\mu^{\otimes n}))))
  \right)
  \\
  =&
  q^{-3w(\beta\beta')/4}
  \\
  &\times
  \left\{
    \operatorname{Tr}_1(\operatorname{Tr}_2(\cdots(\operatorname{Tr}_n(
    \Phi(\beta)
    (\operatorname{Id}_V^{\otimes(i-1)}\otimes q^{1/4}R\otimes\operatorname{Id}_V^{\otimes(n-i-1)})
    \Phi(\beta')
    \mu^{\otimes n}))))
  \right.
  \\
  &\left.
  \qquad
    -
    \operatorname{Tr}_1(\operatorname{Tr}_2(\cdots(\operatorname{Tr}_n(
    \Phi(\beta)
    (\operatorname{Id}_V^{\otimes(i-1)}\otimes q^{-1/4}R^{-1}\otimes\operatorname{Id}_V^{\otimes(n-i-1)})
    \Phi(\beta')\mu^{\otimes n}))))
  \right\}
  \\
  \intertext{(from \eqref{eq:skein_R})}
  =&
  q^{-3w(\beta\beta')/4}
  (q^{1/2}-q^{-1/2})
  \operatorname{Tr}_1(\operatorname{Tr}_2(\cdots(\operatorname{Tr}_n(\Phi(\beta\beta')\mu^{\otimes n}))))
  \\
  =&
  (q^{1/2}-q^{-1/2})J_2(L_0;q)\times\frac{\{2\}}{\{1\}},
\end{split}$$ completing the proof. ◻
:::

::: remark
The original Jones polynomial $V(L;q)$ satisfies $$q^{-1}V(L_+;q)-qV(L_-;q)
  =
  (q^{1/2}-q^{-1/2})V(L_0;q)$$ [@Jones:BULAM385 Theorem 12]. So we have $J_2(L;q)=(-1)^{\sharp(L)-1}V(L;q^{-1})$, where $\sharp(L)$ denotes the number of components of $L$.
:::
