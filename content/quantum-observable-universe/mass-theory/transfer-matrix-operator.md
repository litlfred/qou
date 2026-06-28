Every particle interaction in the Descartes universe is encoded by
a **transfer matrix** $T_{K_1, K_2}(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1/2}])$
determined by the knot types $K_1, K_2$ of the two interacting
strands.  The transfer matrix acts as an **operator** on the
Gröbner--Shirshov ideal of the Iwahori--Hecke algebra, and its entries are
polynomials in $q$.

## Definition

**Definition.**
Let $K_1, K_2$ be two building block knots
([building blocks](#rem:building-block-knots)) meeting at a
crossing in a braid word $\beta \in B_n$.  The **transfer
matrix** of the crossing is:

$$
  T_{K_1, K_2}(q)
  = 
  \begin{pmatrix}
    c(q - q^{-1}) + d & c \\
    c & d
  \end{pmatrix}
$$

where the **crossing coefficients** $(c, d) \in \mathbb{Z}[q^{\pm 1/2}]^2$
are determined by the knot types:

$$
  c_{K_1, K_2}
  = 
  \frac{J_{K_1}(q) \cdot J_{K_2}(q)}{J_{K_1 \# K_2}(q)},
  \qquad
  d_{K_1, K_2}
  = 
  -c \cdot \frac{q  s}{1 + J_{K_1}(q) \cdot J_{K_2}(q)}
$$

where $J_K(q)$ is the Jones polynomial of knot $K$ and
$s = q^{1/2} - q^{-1/2}$ is the Skein amplitude.

For the three nuclear crossing types (quarks as Borromean
unknot components), this specializes to:

| Crossing | $K_1$ | $K_2$ | $c$ | $d$ | Hecke element |
|----------|-------|-------|-----|-----|---------------|
| $\mathfrak{p}$-$\mathfrak{p}$ | $u$ | $u$ | $1$ | $0$ | $\sigma$ |
| $\mathfrak{n}$-$\mathfrak{n}$ | $d$ | $d$ | $1$ | $-(q - q^{-1})$ | $\sigma^{-1}$ |
| mixed | $u$ | $d$ | $1$ | $-\frac{1}{2}(q - q^{-1})$ | $\frac{1}{2}(\sigma + \sigma^{-1})$ |
