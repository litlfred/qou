<!-- FILE_START: tm-general-form.md -->
A general form collapses every crossing type into a single two-parameter family. The three nuclear crossings and the connected-sum case become special points of one matrix. Every transfer matrix has the same $2 \times 2$ structure, parameterized by two crossing coefficients $(c, d)$:

$$
  T(c, d) = \begin{pmatrix} c(q - q^{-1}) + d & c \\ c & d \end{pmatrix}
$$

The coefficients $(c, d) \in \mathbb{Z}[q^{\pm 1/2}]$ depend on how the two knots interact. For knots meeting via connected sum, the Jones polynomial satisfies $J_{K_1 \# K_2} = J_{K_1} \cdot J_{K_2}$, giving $c = 1$ and $d = 0$. For knots meeting via the Hecke product (the physically relevant case for nucleon crossings), the coefficients are determined by the representation-theoretic structure of the crossing. They do not reduce to connected-sum formulas. The three nuclear crossing types have specific $(c, d)$ values listed in Section 3.2.

The transfer matrix acts on a Iwahori--Hecke algebra element $a\sigma_i + b$ by left multiplication and Hecke reduction ($T^2 = (q - q^{-1})T + 1$):

$$
  \begin{pmatrix} a' \\ b' \end{pmatrix} = T(c, d) \cdot \begin{pmatrix} a \\ b \end{pmatrix}
$$

Explicitly:

$$
  a' = ac(q - q^{-1}) + ad + bc, \qquad b' = ac + bd
$$

Three properties fix how the crossing acts: its determinant controls invertibility, its eigenvalues control spectral behavior under iteration, and its degenerate limits recover the connected-sum and scalar matrices.

**Determinant.** The determinant governs whether the crossing action is invertible:

$$
  \det T(c, d) = cd(q - q^{-1}) + d^2 - c^2
$$

**Eigenvalues** (when $c \neq 0$). The eigenvalues give the spectral behavior of the crossing under repeated application:

$$
  \lambda_{\pm} = \frac{1}{2}\Bigl[c(q - q^{-1}) + 2d \pm \sqrt{\bigl[c(q - q^{-1})\bigr]^2 + 4c^2}\Bigr]
$$

**Special cases.** The two degenerations of interest recover matrices met earlier: $c = 0$ collapses $T$ to the scalar matrix, while $c = 1, d = 0$ gives the connected-sum (fundamental) matrix.

- $c = 0$: $T(0, d) = d \cdot \mathbb{I}$ (scalar matrix)
- $d = 0$: $T(c, 0) = c \cdot \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}$
- $c = 1, d = 0$: The fundamental matrix $T_{pp}$
<!-- FILE_END: tm-general-form.md -->

