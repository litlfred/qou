*Let $\mathcal{N}(Z, N)$ be the nuclear braid word in $H_A(q)$, presented with its crossings grouped by generator in increasing order, $\mathcal{N} = X_0 X_1 \cdots X_{A-2}$ with each $X_i$ a product of factors $c\,\sigma_i + d$ at the single generator $\sigma_i$. At each generator, let $(a_i, b_i)$ be the transfer-matrix-reduced chain coefficients, so $X_i = a_i \sigma_i + b_i$. Let $z = q^{3}/(q^{2}+1)$ (**convention D**) be the Markov trace parameter. The Markov trace factors exactly:*

$$
  \mathrm{tr}_{\mathrm{Markov}}\!\bigl(
    \mathcal{N}(Z, N)
  \bigr)
  \;=\;
  \prod_{i=0}^{A-2}
  \bigl(z \cdot a_i + b_i\bigr).
$$

Each factor $\hat{V}_i = z \cdot a_i + b_i$ is a rational function of $q$ (since $z = q^3/(q^2+1)$), with coefficients in $\mathbb{Z}[\tfrac12]$. The full trace is their product.

The grouping hypothesis is essential. Letters at adjacent generators do not commute, so a word that interleaves them, such as $\sigma_1\sigma_2\sigma_1$ or the Borromean core $(\sigma_1\sigma_2^{-1})^3$, cannot be regrouped into this form, and its trace does not factor: $\mathrm{tr}_M(\sigma_1\sigma_2\sigma_1) = h z^2 + z \neq z^3$.

**The transfer matrix IS the polynomial.**
At each crossing between nucleons $i$ and $j$, the transfer matrix

$$
  T_j = 
  \begin{pmatrix}
    c_j(q - q^{-1}) + d_j & c_j \\
    c_j & d_j
  \end{pmatrix}
$$

carries polynomial entries. The crossing types determine the coefficients:

| Pair type | $c_j$ | $d_j$ | $\det(T_j)$ |
|---|---|---|:---:|
| $\mathfrak{p}$-$\mathfrak{p}$ | $1$ | $0$ | $-1$ |
| $\mathfrak{n}$-$\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ | $-1$ |
| mixed | $1$ | $-\frac{1}{2}(q - q^{-1})$ | $-1 - \frac{1}{4}(q - q^{-1})^2$ |

The product of $k_i$ transfer matrices at generator $\sigma_i$ yields $M_i \in \mathrm{GL}_2(\mathbb{Q}(q))$, whose entries are polynomials of degree bounded by $2k_i$. Then $\hat{V}_i(q) = z \cdot (M_i)_{21} + (M_i)_{22}$ evaluates the Skein polynomial $P_{\mathcal{N}}(q) = \prod_{i=0}^{A-2} \hat{V}_i(q)$ in factored form.

**Asymptotic behaviour.**
For heavy nuclei ($A \gg 1$), the ratio of $L_0^{-}$ and parent traces converges:

$$
  \frac{\mathrm{tr}(L_0^{-})}{\mathrm{tr}(\mathcal{N})}
   \;\longrightarrow\;
  \frac{1}{\hbar_q}
  \;=\;
  \frac{1}{1 - q^{-1}}
   \;\approx\;  10.09.
$$

The sub-leading $O(1/A)$ correction carries the nucleus-specific shell structure and pairing data.
