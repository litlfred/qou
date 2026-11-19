### Proof

The identity composes two named identities:

1. The [electromagnetic coupling projection](#prop:em-coupling-projection) establishes the bare combinatorial form:

   $$
     \alpha_{EM}^{-1} \;=\; q \cdot [9]_q \cdot [10]_q.
   $$

   This follows from the antisymmetric eigenvalue $-q^{-1}$ of the $R$-matrix and the $q$-deformed crossing numbers of the force-carrier generators $T_{2,9}$ and $T_{3,5}$. By [force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness), this basis consists exactly of the genus-$4$ saturating torus-knot set on $\Sigma_4$.

2. The [torus-knot shift formula](#prop:alpha-shift-torus-knot) establishes the closed-form identity:

   $$
     \alpha_{\mathrm{shift}}(T_{p,k}) \;=\; k(p-1)
     \qquad (\gcd(p, k) = 1)
   $$

   on the all-anti-symmetric channel $V_{(1^p)}$. Specialising at $(p, k) \in \{(2, 9), (3, 5)\}$ gives:

   $$
     \alpha_{\mathrm{shift}}(T_{2,9}) \;=\; 9 \cdot 1 \;=\; 9,
     \qquad
     \alpha_{\mathrm{shift}}(T_{3,5}) \;=\; 5 \cdot 2 \;=\; 10.
   $$

Substituting these values into the bare formula yields the stated identity exactly:

$$
  \alpha_{EM}^{-1}
  \;=\; q \cdot [9]_q \cdot [10]_q
  \;=\; q \cdot \bigl[\alpha_{\mathrm{shift}}(T_{2,9})\bigr]_q
              \cdot \bigl[\alpha_{\mathrm{shift}}(T_{3,5})\bigr]_q.
  \qquad \square
$$

### Numerical verification

The composition holds identically at the symbolic level. Numerical evaluation at $q_0$ to 50 decimal places compares the chain expression for $\alpha_{\mathrm{shift}}(T_{2,9})$ and $\alpha_{\mathrm{shift}}(T_{3,5})$ against the bare expression:

$$
  |\,\text{chain} - \text{bare}\,| \;=\; 0
$$

identically to arbitrary precision, with both equalling $\alpha_{EM}^{-1}(q_0) \approx 136.823$. The gap $|\,\text{chain} - \text{CODATA}\,| \approx 0.213$ is the $\mathcal{O}(10^{-3})$ tree-level offset of the [electromagnetic coupling projection](#prop:em-coupling-projection), which this algebraic refactoring leaves unchanged; closing it requires the [Bring-surface zero-mode shift](#prop:em-coupling-bring-zero-mode) and higher-loop corrections.
