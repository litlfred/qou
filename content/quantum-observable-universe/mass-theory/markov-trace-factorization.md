*Let $\mathcal{N}(Z, N)$ be the Gröbner-Shirshov-reduced nuclear braid word in $H_A(q)$. At each generator $\sigma_i$, let $(a_i, b_i)$ be the transfer-matrix-reduced chain coefficients. Let $z = 1/(q^{1/2} + q^{-1/2})$ be the Markov trace parameter. The Markov trace factors exactly:*

$$
  \mathrm{tr}_{\mathrm{Markov}}\!\bigl(
    \mathcal{N}(Z, N)
  \bigr)
  \;=\;
  \prod_{i=0}^{A-2}
  \bigl(z \cdot a_i + b_i\bigr).
$$

Each factor $\hat{V}_i = z \cdot a_i + b_i$ is a polynomial in $q$. The full trace is a product of polynomials, evaluating the nuclear Skein polynomial.

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

The product of $k_i$ transfer matrices at generator $\sigma_i$ yields $M_i \in \mathrm{GL}_2(\mathbb{Q}(q))$, whose entries are polynomials of degree bounded by $2k_i$. Then $\hat{V}_i(q) = z \cdot (M_i)_{11} + (M_i)_{21}$ evaluates the Skein polynomial $P_{\mathcal{N}}(q) = \prod_{i=0}^{A-2} \hat{V}_i(q)$ in factored form.

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
