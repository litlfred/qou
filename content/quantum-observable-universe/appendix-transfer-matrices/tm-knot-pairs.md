A transfer matrix records how a single crossing between two knotted strands acts on the Hecke chain. Each knot pair contributes a $2 \times 2$ block determined by its crossing coefficients $c$ and $d$. Every nuclear and electromagnetic crossing reduces to one of just three classes (Section 5). This section lists every transfer matrix for each knot pair over $\mathbb{Z}[q^{± 1/2}]$.

## 1. Trivial transfer matrices

**1a. Unknot--unknot (vacuum--vacuum)**
Knots: $K_1 = T_{1,0}$, $K_2 = T_{1,0}$.
Jones polynomials: $J_{T_{1,0}}(q) = 1$, $J_{T_{1,0} \# T_{1,0}}(q) = 1$.
Crossing coefficients: $c = 1$, $d = 0$.

$$
  T_{\nu\nu}(q) = \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}
$$

This is the simplest non-identity transfer matrix.

**1b. Identity (no crossing)**
When two strands do not cross at generator $\sigma_i$, the transfer matrix is the identity:

$$
  T_{\varnothing}(q) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \mathbb{I}
$$

This is the $c = 0, d = 1$ case.

## 2. Nuclear transfer matrices (proton--neutron pairs)

These three matrices govern all nuclear interactions.

**2a. Proton--proton ($\mathfrak{p}$-$\mathfrak{p}$)**
Knots: $K_1 = T_{2,3}$ (up quark), $K_2 = T_{2,3}$ (up quark).
Crossing coefficients: $c = 1$, $d = 0$.

$$
  T_{pp}(q) = \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}
$$

Explicit entries are in [Table 1](#tbl:tm-knot-pairs-table1-data). Eigenvalues are $\lambda_{±} = \frac{1}{2}\left((q - q^{-1}) ± \sqrt{(q-q^{-1})^2 + 4}\right)$.

**2b. Neutron--neutron ($\mathfrak{n}$-$\mathfrak{n}$)**
Knots: $K_1 = T_{2,3}^{\sigma}$ (down quark), $K_2 = T_{2,3}^{\sigma}$ (down quark).
Crossing coefficients: $c = 1$, $d = -(q - q^{-1})$.

$$
  T_{nn}(q) = \begin{pmatrix} 0 & 1 \\ 1 & -(q - q^{-1}) \end{pmatrix}
$$

Explicit entries are in [Table 2](#tbl:tm-knot-pairs-table2-data). Relation to $T_{pp}$: $T_{nn}(q) = T_{pp}(q) - (q - q^{-1}) \mathbb{I}$.

**2c. Mixed ($\mathfrak{p}$-$\mathfrak{n}$)**
Knots: $K_1 = T_{2,3}$ (up), $K_2 = T_{2,3}^{\sigma}$ (down).
Crossing coefficients: $c = 1$, $d = -\frac{1}{2}(q - q^{-1})$.

$$
  T_{\mathrm{mix}}(q) = \begin{pmatrix} \frac{q - q^{-1}}{2} & 1 \\ 1 & -\frac{q - q^{-1}}{2} \end{pmatrix}
$$

Explicit entries are in [Table 3](#tbl:tm-knot-pairs-table3-data). Midpoint property: $T_{\mathrm{mix}}(q) = \frac{1}{2}(T_{pp}(q) + T_{nn}(q))$. This gives beta decay a universal matrix.

