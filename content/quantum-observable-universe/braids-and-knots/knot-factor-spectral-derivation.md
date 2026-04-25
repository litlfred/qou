**Setup.**
Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, let
$\beta \in B_n$ be the braid word of a nuclear configuration and
$\beta^* \in B_n$ its mirror.  In the Iwahori--Hecke algebra
$H_n(q)$, both decompose into central idempotents:

$$
  \beta \;=\; \sum_\lambda c_\lambda(\beta)\, p_\lambda,
  \qquad
  \beta^* \;=\; \sum_\lambda c_\lambda(\beta^*)\, p_\lambda,
$$

with $c_\lambda(\beta) = \chi_\lambda(\beta) \in R$.

**Proposition (knot factor as chirality Gram pairing).**
*The knot factor $a_K$ in the unified mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) is the
chirality Gram pairing
([Gram-spectral connection](#rem:gram-matrix-spectral-connection))*

$$
  a_K \;=\;
  \frac{G_{\beta, \beta^*}}{G_{\mathbf{1}, \mathbf{1}}}
  \;=\;
  \sum_{\lambda \,\vdash\, n}
    w_\lambda(q)\;
    \frac{c_\lambda(\beta)\, c_\lambda(\beta^*)}{c_\lambda(\mathbf{1})^2},
$$

*with Plancherel weights $w_\lambda(q) = \dim_q^2 V_\lambda /
[n]_q!$ summing to $1$.  The identity is exact in $R$.*

*Proof.* The Gram matrix is block-diagonal in the central-idempotent
basis with entries
$G_{\lambda \mu} = \delta_{\lambda \mu} \cdot \dim_q V_\lambda
\dim V_\lambda / [n]_q!$
([Gram-spectral connection](#rem:gram-matrix-spectral-connection)).
Substituting the central-idempotent expansions of $\beta$ and
$\beta^*$ and reducing produces the displayed Plancherel-weighted
sum.  $\square$
