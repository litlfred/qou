*Let $\mathcal{N}(Z, N)$ be the Gröbner-Shirshov-reduced nuclear braid word in $H_A(q)$. At each generator $\sigma_i$, let $(a_i, b_i)$ be the transfer-matrix-reduced chain coefficients. Let $z = q^{3}/(q^{2}+1)$ (**convention D**) be the Markov trace parameter. The Markov trace factors exactly:*

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

The product of $k_i$ transfer matrices at generator $\sigma_i$ yields $M_i \in \mathrm{GL}_2(\mathbb{Q}(q))$, whose entries are polynomials of degree bounded by $2k_i$. Then $\hat{V}_i(q) = z \cdot (M_i)_{21} + (M_i)_{22}$ evaluates the Skein polynomial $P_{\mathcal{N}}(q) = \prod_{i=0}^{A-2} \hat{V}_i(q)$ in factored form.

> **⚠ Readout corrected 2026-09-05.** This line published $z \cdot (M_i)_{11} + (M_i)_{21}$, which is the readout of the **deprecated** `fsh-guts/deprecated/computations/transfer_matrix_symbolic.py` (`V_hat_i = z * M_i[0,0] + M_i[1,0]`), not the live one. Measured against the Lean-proved single-crossing factor [$\mathrm{tr}_2(\sigma + d) = z + d$](#rem:canonical-trace-factorises-over-chain) on a one-crossing matrix, all three bonds:
>
> | bond | $z + d$ | published $z(M)_{11} + (M)_{21}$ | corrected $z(M)_{21} + (M)_{22}$ |
> |---|---:|---:|---:|
> | $pp$ | $0.612688037146$ | $1.128088744114$ | $0.612688037146$ |
> | $nn$ | $0.403627738351$ | $1.000000000000$ | $0.403627738351$ |
> | $pn$ | $0.508229789377$ | $1.064088425325$ | $0.508229789377$ |
>
> The corrected readout reproduces $z + d$ exactly; the published one misses every bond and is not even monotone in $d$. The factorisation statement itself is unaffected — what was wrong was the recipe for reading $(a_i, b_i)$ off $M_i$, i.e. $a_i = (M_i)_{21}$ and $b_i = (M_i)_{22}$. The same wrong readout is recorded as a trap in `no_within_generator_noncommutativity_probe.py`, whose docstring reports the identical $1.128089$ at $q_0$ from an earlier encounter with it.

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
