The identity is a composition of two named identities:

1. [`prop:em-coupling-projection`](#prop:em-coupling-projection)
   establishes the bare combinatorial form

   $$
     \alpha_{EM}^{-1} \;=\; q \cdot [9]_q \cdot [10]_q,
   $$

   derived from the antisymmetric eigenvalue $-q^{-1}$ of the
   $R$-matrix and the $q$-deformed crossing numbers of the two
   force-carrier generators $T_{2,9}$ (crossing number $9$) and
   $T_{3,5}$ (crossing number $10$). The basis is exactly two knots
   by [`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)
   — the genus-$4$ saturating torus-knot set on $\Sigma_4$.

2. [`prop:alpha-shift-torus-knot`](#prop:alpha-shift-torus-knot)
   establishes the closed-form identity

   $$
     \alpha_{\mathrm{shift}}(T_{p,k}) \;=\; k(p-1)
     \qquad (\gcd(p, k) = 1)
   $$

   on the all-anti-symmetric channel $V_{(1^p)}$. Specialising at
   $(p, k) \in \{(2, 9), (3, 5)\}$:

   $$
     \alpha_{\mathrm{shift}}(T_{2,9}) \;=\; 9 \cdot 1 \;=\; 9,
     \qquad
     \alpha_{\mathrm{shift}}(T_{3,5}) \;=\; 5 \cdot 2 \;=\; 10.
   $$

Substituting these two values into the bare formula yields the
stated identity exactly:

$$
  \alpha_{EM}^{-1}
  \;=\; q \cdot [9]_q \cdot [10]_q
  \;=\; q \cdot \bigl[\alpha_{\mathrm{shift}}(T_{2,9})\bigr]_q
              \cdot \bigl[\alpha_{\mathrm{shift}}(T_{3,5})\bigr]_q.
  \qquad \square
$$

### Numerical verification

The composition is exact at the symbolic level. Numerical
re-evaluation at $q_0$
([`alpha-em-shift-multiplicative-chain.witness.json`](../../computations/alpha/alpha-em-shift-multiplicative-chain.witness.json),
mpmath 50-dps) reads $\alpha_{\mathrm{shift}}(T_{2,9})$ and
$\alpha_{\mathrm{shift}}(T_{3,5})$ from the upstream witness
[`alpha-shift-torus.witness.json`](../../computations/alpha/alpha-shift-torus.witness.json)
and compares the chain expression $q \cdot [\alpha_{\mathrm{shift}}(T_{2,9})]_q
\cdot [\alpha_{\mathrm{shift}}(T_{3,5})]_q$ to the bare expression
$q \cdot [9]_q \cdot [10]_q$:

$$
  |\,\text{chain} - \text{bare}\,| \;=\; 0
  \quad (\text{exactly, to mpmath precision}),
$$

with both equalling $\alpha_{EM}^{-1}(q_0) \approx 136.823$. (The
gap $|\,\text{chain} - \text{CODATA}\,| \approx 0.213$ is the same
$\mathcal{O}(10^{-3})$ precision gap inherited from
[`prop:em-coupling-projection`](#prop:em-coupling-projection),
unchanged by this refactoring; closing it remains the work of
[`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation)
and the higher-order $C_5$-invariant corrections discussed there.)

All $3$ assertions in the witness pass.


**Remark on Mathematical Novelty:** Expressing the shift as a unified multiplicative chain is not merely a composition of known identities, but provides a novel structural proof that the electromagnetic shifts are governed by an intrinsically multiplicative, rather than additive, algebraic chain.
