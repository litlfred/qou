### Proof

The identity composes two named identities:

1. [Electromagnetic coupling from the antisymmetric braiding and force-carrier crossings](#prop:em-coupling-projection) establishes the bare combinatorial form:

   $$
     \alpha_{EM}^{-1} \;=\; q \cdot [9]_q \cdot [10]_q.
   $$

   We derive this from the antisymmetric eigenvalue $-q^{-1}$ of the $R$-matrix and the $q$-deformed crossing numbers of the force-carrier generators $T_{2,9}$ and $T_{3,5}$. By [$(T_{2,9}, T_{3,5})$ is the unique pair of genus-$4$ torus knots](#prop:force-carrier-bring-uniqueness), this basis consists exactly of the genus-$4$ saturating torus-knot set on $\Sigma_4$.

2. [Pole order at $q=0$ of the torus-knot character](#prop:alpha-shift-torus-knot) establishes the closed-form identity:

   $$
     \alpha_{\mathrm{shift}}(T_{p,k}) \;=\; k(p-1)
     \qquad (\gcd(p, k) = 1)
   $$

   on the all-anti-symmetric channel $V_{(1^p)}$. We specialise at $(p, k) \in \{(2, 9), (3, 5)\}$:

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

The composition holds exactly at the symbolic level. Numerical re-evaluation at $q_0$ (50-digit arithmetic) takes the upstream values $\alpha_{\mathrm{shift}}(T_{2,9})$ and $\alpha_{\mathrm{shift}}(T_{3,5})$. It compares the chain expression to the bare expression:

$$
  |\,\text{chain} - \text{bare}\,| \;=\; 0
$$

identically to mpmath precision, with both equalling $\alpha_{EM}^{-1}(q_0) \approx 136.823$. The gap $|\,\text{chain} - \text{CODATA}\,| \approx 0.213$ is the $\mathcal{O}(10^{-3})$ precision gap inherited from [Electromagnetic coupling from the antisymmetric braiding and force-carrier crossings](#prop:em-coupling-projection). This refactoring leaves it unchanged. Closing this gap requires [Conjectured categorical derivation of $E_h = m_e c_q^2 \alpha_{EM}^2$ via $J^1$-vanishing in the molecular LP dual](#conj:e-hartree-categorical-derivation) and higher-order $C_5$-invariant corrections.

All $3$ assertions in the witness pass.
