The chirality factor $a_K = 1 + w(K) \cdot h$, where $w(K)$ is the
writhe of the knot $K$ and $h = q - q^{-1}$, is derived to first
order in $h$ from the Kauffman framing formula applied to the ribbon
twist on $H_n(R, q)$
([prop:chirality-writhe-ribbon-derivation](#prop:chirality-writhe-ribbon-derivation)).
This conjecture states the exact (all-orders) form and asserts that
the first-order truncation is the correct chirality factor for all
confined knots in the model.

## Statement

**Conjecture.**
*Let $K$ be a confined knot with writhe $w(K)$ and canonical Hecke
braid element $T_w \in H_{n_0}(R, q)$.  The chirality factor of $K$
in the mass formula
([thm:knot-mass-formula-unified](#thm:knot-mass-formula-unified))
is the exact Wedderburn-weighted ribbon-twist ratio:*

$$
  a_K
  \;=\;
  \frac{
    \sum_\lambda w_\lambda\, q^{2 w(K) c(\lambda)}\, \chi_\lambda(T_w)
  }{
    \sum_\lambda w_\lambda\, \chi_\lambda(T_w)
  },
$$

*where $c(\lambda) = \sum_{x \in \lambda}(\mathrm{col}(x) - \mathrm{row}(x))$
is the total content of the Young diagram $\lambda$.*

*Furthermore, for all nucleon and nuclear knots appearing in the QOU
model, this exact form equals $1 + w(K) \cdot h$ to the precision
required by the $0.75\%$ accuracy of the mass formula.*

## Proof obligations

1. Verify that the ribbon twist $\varTheta_\lambda = q^{c(\lambda)} \mathrm{id}$
   on the irreducible $H_n(q)$-module $V_\lambda$ gives
   $a_K = \sum_\lambda w_\lambda q^{2w(K)c(\lambda)} \chi_\lambda(T_w) /
   \sum_\lambda w_\lambda \chi_\lambda(T_w)$ from the Kauffman framing formula.
2. Evaluate $\sum_\lambda w_\lambda q^{2w(K)c(\lambda)} \chi_\lambda(T_w)$
   symbolically for each particle knot.
3. Show the first-order expansion $a_K \approx 1 + w(K)h$ is exact
   (or estimate the $O(h^2)$ correction and show it is negligible
   within the $0.75\%$ mass accuracy).

## Relationship to GAP-A-2

This conjecture directly addresses GAP-A-2 of the
[derivation audit report](#prose:derivation-audit-report).
