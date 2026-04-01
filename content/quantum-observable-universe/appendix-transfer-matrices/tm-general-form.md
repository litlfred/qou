Every transfer matrix has the same $2 \times 2$ structure,
parameterized by two **crossing coefficients** $(c, d)$.

## General form

$$
  T(c, d)
  \;=\;
  \begin{pmatrix}
    c(q - q^{-1}) + d & c \\
    c & d
  \end{pmatrix}
$$

The coefficients $(c, d) \in \mathbb{Z}[q^{\pm 1/2}]$ are
determined by the Jones polynomials of the two knots at the
crossing:

$$
  c_{K_1, K_2}
  \;=\;
  \frac{J_{K_1}(q) \cdot J_{K_2}(q)}{J_{K_1 \# K_2}(q)},
  \qquad
  d_{K_1, K_2}
  \;=\;
  -\,c \cdot \frac{q \, s}{1 + J_{K_1}(q) \cdot J_{K_2}(q)}
$$

where $K_1 \# K_2$ is the connected sum of $K_1$ and $K_2$.

## Action on Hecke elements

The transfer matrix acts on a Hecke algebra element
$a\sigma_i + b$ by left multiplication and Hecke reduction
($T^2 = (q - q^{-1})T + 1$):

$$
  \begin{pmatrix} a' \\ b' \end{pmatrix}
  \;=\;
  T(c, d)
  \;\cdot\;
  \begin{pmatrix} a \\ b \end{pmatrix}
$$

Explicitly:

$$
  a' \;=\; ac(q - q^{-1}) + ad + bc,
  \qquad
  b' \;=\; ac + bd
$$

## Properties of $T(c, d)$

**Determinant:**

$$
  \det T(c, d) \;=\; d\bigl[c(q - q^{-1}) + d\bigr] - c^2
  \;=\; c^2(q - q^{-1})\!\cdot\!\frac{d}{c} + d^2 - c^2
$$

**Eigenvalues** (when $c \neq 0$):

$$
  \lambda_{\pm}
  \;=\;
  \frac{1}{2}\Bigl[
    c(q - q^{-1}) + 2d
    \;\pm\;
    \sqrt{\bigl[c(q - q^{-1})\bigr]^2 + 4c^2}
  \Bigr]
$$

**Special cases:**
- $c = 0$: $T(0, d) = d \cdot \mathbb{I}$ (scalar matrix)
- $d = 0$: $T(c, 0) = c \cdot \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}$
- $c = 1, d = 0$: The fundamental matrix $T_{pp}$ (see below)
