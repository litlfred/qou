Beta decay is a **universal** 2×2 matrix-valued polynomial in $q$.
The same matrix $\Delta_\beta(q)$ governs every beta transition in
every nucleus.

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
$\frac{qs}{2}$ is $\frac{1-q^2}{2} \cdot 0 + \frac{qs}{2}
\cdot 1$.  The $(1,1)$ entry is $\frac{1-q^2}{2}(q - q^{-1})
+ \frac{qs}{2} \cdot 1$.  $\square$

**Explicit entries at $q = 1.110$:**

$$
  \Delta_\beta(1.110) \;=\;
  \begin{pmatrix}
    +0.0337 & -0.1161 \\
    -0.1161 & +0.0579
  \end{pmatrix}
$$

## Universality

The universality $\Delta_\beta^{nn \to \mathrm{mix}} =
\Delta_\beta^{\mathrm{mix} \to pp}$ means that **the matrix
perturbation produced by converting one nucleon from
$\mathfrak{n}$ to $\mathfrak{p}$ is the same regardless of
whether the partner nucleon is a proton or a neutron.**

This is a consequence of the crossing coefficients being
**equally spaced**:

$$
  T_{\mathrm{mix}} = \tfrac{1}{2}(T_{pp} + T_{nn})
$$

The mixed matrix is exactly the midpoint.  Therefore the step
$T_{nn} \to T_{\mathrm{mix}}$ and $T_{\mathrm{mix}} \to T_{pp}$
are the same displacement $\Delta_\beta$.

**Physical interpretation**: beta decay shifts each crossing
at the converting nucleon by the **same universal amount**
$\Delta_\beta(q)$, independent of the partner.  The effect
on the Skein polynomial depends only on the **number** of
crossings affected and their positions in the transfer
matrix chain.

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

## Worked example: tritium

${}^3\mathrm{H}(p, n, n) \to {}^3\mathrm{He}(p, p, n)$.
Converting nucleon: position 1 (first neutron → proton).

**Generator $\sigma_0$** (2 crossings: with nucleons 1 and 2):

| Crossing | Parent | Daughter | Change |
|----------|--------|----------|--------|
| $(0, 1)$ | $\mathfrak{p}\mathfrak{n}$ = mixed | $\mathfrak{p}\mathfrak{p}$ = pp | $+\Delta_\beta$ |
| $(0, 2)$ | $\mathfrak{p}\mathfrak{n}$ = mixed | $\mathfrak{p}\mathfrak{n}$ = mixed | unchanged |

$$
  M_0^{\mathrm{par}} = T_{\mathrm{mix}} \cdot T_{\mathrm{mix}},
  \quad
  M_0^{\mathrm{dau}} = T_{pp} \cdot T_{\mathrm{mix}}
$$

$$
  \hat{V}_0^{\mathrm{par}} = 0.7684, \quad
  \hat{V}_0^{\mathrm{dau}} = 0.7510
$$

**Generator $\sigma_1$** (1 crossing: with nucleon 2):

| Crossing | Parent | Daughter | Change |
|----------|--------|----------|--------|
| $(1, 2)$ | $\mathfrak{n}\mathfrak{n}$ = nn | $\mathfrak{p}\mathfrak{n}$ = mixed | $+\Delta_\beta$ |

$$
  M_1^{\mathrm{par}} = T_{nn},
  \quad
  M_1^{\mathrm{dau}} = T_{\mathrm{mix}}
$$

$$
  \hat{V}_1^{\mathrm{par}} = 1.3029, \quad
  \hat{V}_1^{\mathrm{dau}} = 1.2036
$$

**Skein polynomial ratio:**

$$
  \frac{P_{{}^3\mathrm{He}}(q)}{P_{{}^3\mathrm{H}}(q)}
  \;=\;
  \frac{0.7510 \times 1.2036}{0.7684 \times 1.3029}
  \;=\;
  \frac{0.9039}{1.0011}
  \;=\; 0.9029
$$

$$
  \ln\!\left(\frac{P_{{}^3\mathrm{He}}}{P_{{}^3\mathrm{H}}}\right)
  \;=\; -0.1021
$$

Per-generator contribution:

| Generator | $\ln(\hat{V}^{\mathrm{dau}}/\hat{V}^{\mathrm{par}})$ | Fraction |
|:---------:|:---:|:---:|
| $\sigma_0$ | $-0.0229$ | $22\%$ |
| $\sigma_1$ | $-0.0792$ | $78\%$ |

Generator $\sigma_1$ (the converting nucleon's own generator)
contributes $78\%$ of the total — consistent with the generator
volume profile for heavier nuclei.

## Double beta decay

For $2\beta$ decay, two nucleons convert.  At each affected
generator, the transfer matrix perturbation is a **product** of
two $\Delta_\beta$ matrices (with intervening unchanged matrices):

$$
  \Delta M_i^{(2\beta)}
  \;=\;
  L_i \cdot \Delta_\beta \cdot C_i \cdot \Delta_\beta \cdot R_i
  \;+\;
  (\text{linear terms})
$$

where $C_i$ is the product of unchanged matrices between the
two converting positions.  The quadratic term
$\Delta_\beta \cdot C_i \cdot \Delta_\beta$ is the **2-jet
cross-term** — the nuclear matrix element of double beta decay
([jet expansion](#prop:generator-volume-decomposition)).

Since $\Delta_\beta$ is universal, the double beta matrix element
depends only on $C_i$ — the unchanged matrices between the two
converting nucleons.  This is computable from the nucleon types
in that region.
