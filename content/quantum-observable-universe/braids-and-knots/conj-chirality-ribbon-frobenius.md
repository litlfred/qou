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
    \sum_\lambda w_\lambda(q)\, q^{2 w(K) c(\lambda)}\, \chi_\lambda(T_w)
  }{
    \sum_\lambda w_\lambda(q)\, \chi_\lambda(T_w)
  },
$$

*where:*
- *$w_\lambda(q)$ are the Wenzl-bridge Markov weights
  ([prop:alpha-k-derivation-procedure](#prop:alpha-k-derivation-procedure)),*
- *$c(\lambda) = \sum_{x \in \lambda}(\mathrm{col}(x) - \mathrm{row}(x))$
  is the total content of the Young diagram $\lambda$,*
- *$\chi_\lambda(T_w)$ is the Hecke character of $T_w$ in the
  Wedderburn summand $\lambda$.*

*Furthermore, for all nucleon and nuclear knots appearing in the QOU
model, this exact form equals $1 + w(K) \cdot h$ to the precision
required by the $0.75\%$ accuracy of the mass formula.*

## Derivation sketch

**Step 1: Ribbon twist.**  In the Hecke algebra $H_n(q)$, the ribbon
element $\theta$ acts on each irreducible $V_\lambda$ as scalar
multiplication by $\theta_\lambda = q^{c(\lambda)}$, where
$c(\lambda) = \sum_{x \in \lambda}(j(x) - i(x))$ is the
Frobenius content of $\lambda$ ($i(x)$ = row, $j(x)$ = column of
cell $x$).

**Step 2: Framing change.**  Under a $+1$ framing change
($w(K) \mapsto w(K) + 1$), the Kauffman framing formula gives:

$$
  J_K(q)\big|_{w+1}
  \;=\;
  q^{c(\mu)} \cdot J_K(q)\big|_w,
$$

where $\mu$ is the dominant representation label for the standard
colored Jones polynomial.  The factor $q^{c(\mu)}$ is exactly
$\theta_\mu$, the ribbon twist eigenvalue.

**Step 3: Full writhe.**  After $w(K)$ framing changes, each
$V_\lambda$-component picks up $q^{w(K) \cdot 2c(\lambda)}$
(squared because the twist appears twice — once for each end of
the strand that closes the braid).  The Markov trace then gives the
ratio in the conjecture statement.

**Step 4: First-order expansion.**

$$
  q^{2 w(K) c(\lambda)}
  \;=\;
  e^{2 w(K) c(\lambda) \log q}
  \;=\;
  1 + 2 w(K) c(\lambda) \log q + O(h^2).
$$

Since $\log q = \tfrac{1}{2} h + O(h^3)$ (with $q = e^{h/2}$
in the standard normalization), the leading correction is
$w(K) c(\lambda) h$.  After Markov-averaging over $\lambda$ with
weights $w_\lambda \chi_\lambda(T_w)$, the numerator gives
$1 + w(K) h \langle c(\lambda) \rangle_\beta + O(h^2)$, where
$\langle c(\lambda) \rangle_\beta$ is the Plancherel-weighted mean
content.  The conjecture asserts $\langle c(\lambda) \rangle_\beta = 1$
for all confined knots — i.e. the mean content is exactly $1$.

## Proof obligations

1. **Ribbon-twist eigenvalue.**  Verify that
   $\theta_\lambda = q^{c(\lambda)}$ in the Hecke-algebra ribbon
   structure used in the QOU model (not the quantum-group normalization,
   which may differ by a global phase).

2. **Mean-content identity.**  Show
   $\langle c(\lambda) \rangle_\beta := \sum_\lambda w_\lambda \chi_\lambda(T_w) c(\lambda) / \sum_\lambda w_\lambda \chi_\lambda(T_w) = 1$
   for every nucleon/nuclear knot $T_w$.

3. **$O(h^2)$ bound.**  Estimate the second-order correction
   $O(h^2)$ at $q = q_0$ and show it is $< 0.75\%$ of the leading
   term (matching the overall mass-formula accuracy).

4. **Exact formula.**  For at least one chiral knot (trefoil $3_1$ as
   the proton model), evaluate the exact formula and compare with the
   first-order result.

## Relationship to GAP-A-2

This conjecture directly addresses GAP-A-2 of the
[derivation audit report](#prose:derivation-audit-report).

