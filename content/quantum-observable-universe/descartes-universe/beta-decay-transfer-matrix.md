Beta decay is mediated by the $T_{3,5}$ torus knot with $10$
crossings ([beta decay](#def:beta-decay-skein)).  The $T_{3,5}$
insertion at the converting quark produces a **universal** 2×2
matrix-valued polynomial $\Delta_\beta(q)$ that governs every
beta transition in every nucleus.  The transfer matrix captures
the effect of the $10$-crossing weak vertex on each nucleon pair.

## The three crossing transfer matrices

Each nucleon pair $(i, j)$ contributes a transfer matrix
$T(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1/2}])$:

$$
  T(c, d) \;=\;
  \begin{pmatrix}
    c(q - q^{-1}) + d & c \\
    c & d
  \end{pmatrix}
$$

with crossing coefficients $(c, d)$ depending on the pair type:

$$
  T_{pp}(q) \;=\;
  \begin{pmatrix}
    q - q^{-1} & 1 \\
    1 & 0
  \end{pmatrix},
  \quad
  T_{nn}(q) \;=\;
  \begin{pmatrix}
    q^2(q - q^{-1}) - qs & q^2 \\
    q^2 & -qs
  \end{pmatrix}
$$

$$
  T_{\mathrm{mix}}(q) \;=\;
  \begin{pmatrix}
    \frac{1+q^2}{2}(q - q^{-1}) - \frac{q s}{2}
      & \frac{1+q^2}{2} \\[4pt]
    \frac{1+q^2}{2} & -\frac{q s}{2}
  \end{pmatrix}
$$

where $s = q^{1/2} - q^{-1/2}$ is the Skein amplitude.

## The universal beta decay matrix

**Proposition.**
*The two elementary decay matrices $\Delta_\beta^{nn \to \mathrm{mix}}$
and $\Delta_\beta^{\mathrm{mix} \to pp}$ are identical:*

$$
  \Delta_\beta^{nn \to \mathrm{mix}}(q)
  \;=\; T_{\mathrm{mix}}(q) - T_{nn}(q)
  \;=\; T_{pp}(q) - T_{\mathrm{mix}}(q)
  \;=\; \Delta_\beta^{\mathrm{mix} \to pp}(q)
$$

*There is a single universal beta decay matrix:*

$$
  \boxed{
    \Delta_\beta(q)
    \;=\;
    \tfrac{1}{2}(1 - q^2) \, T_{pp}(q)
    \;+\;
    \tfrac{1}{2}\, q \, s \;\mathbb{I}
  }
$$

*where $\mathbb{I}$ is the $2 \times 2$ identity.*

*Proof.*
The off-diagonal entries of both differences are
$\frac{1+q^2}{2} - q^2 = \frac{1-q^2}{2}$ and
$1 - \frac{1+q^2}{2} = \frac{1-q^2}{2}$.

The $(2,2)$ entry of both is
$-\frac{qs}{2} - (-qs) = \frac{qs}{2}$ and
$0 - (-\frac{qs}{2}) = \frac{qs}{2}$.

The $(1,1)$ entry of both is
$\frac{1-q^2}{2}(q - q^{-1}) + \frac{qs}{2}$.

These are identical for both $T_{\mathrm{mix}} - T_{nn}$ and
$T_{pp} - T_{\mathrm{mix}}$, hence the two elementary decay
matrices coincide.

Writing in terms of $T_{pp}$ and $\mathbb{I}$:
the off-diagonal entries $\frac{1-q^2}{2}$ match
$\frac{1-q^2}{2} \cdot 1$ (the off-diagonal of
$\frac{1-q^2}{2} T_{pp}$).  The $(2,2)$ entry
$\frac{qs}{2}$ is $\frac{1-q^2}{2} \cdot 0 + \frac{qs}{2} \cdot 1$.  The $(1,1)$ entry is $\frac{1-q^2}{2}(q - q^{-1}) + \frac{qs}{2} \cdot 1$.  $\square$

**Explicit entries at the substrate parameter $q$:**

$$
  \Delta_\beta(q_0) \;=\;
  \begin{pmatrix}
    +0.0337 & -0.1161 \\
    -0.1161 & +0.0579
  \end{pmatrix}
$$

## The decay formula

At generator $\sigma_i$ (affected by the converting nucleon
at position $p$), the transfer matrix product factors as:

$$
  M_i^{\mathrm{par}}(q) = L_i(q) \cdot T_{\mathrm{par}}(q) \cdot R_i(q)
$$

where $L_i$ is the product of matrices to the left of the
converting crossing (unchanged) and $R_i$ to the right
(unchanged).  The daughter matrix product is:

$$
  M_i^{\mathrm{dau}}(q) = L_i(q) \cdot (T_{\mathrm{par}}(q) + \Delta_\beta(q)) \cdot R_i(q)
$$

The change in the transfer matrix product:

$$
  \Delta M_i(q) = L_i(q) \cdot \Delta_\beta(q) \cdot R_i(q)
$$

The change in the Markov-traced volume:

$$
  \Delta \hat{V}_i(q)
  \;=\;
  z \cdot (\Delta M_i)_{11} + (\Delta M_i)_{21}
$$

The $\mathcal{Q}_q$-value
([transition energy](#def:q-value-transition)) in log form:

$$
  \ln \frac{P_{\mathrm{dau}}(q)}{P_{\mathrm{par}}(q)}
  \;=\;
  \sum_{i=0}^{p} \ln \frac{\hat{V}_i^{\mathrm{dau}}(q)}{\hat{V}_i^{\mathrm{par}}(q)}
$$

where the sum runs only over generators affected by the
converting nucleon.  Generators $\sigma_i$ with $i > p$ cancel
exactly (unaffected by the conversion).
