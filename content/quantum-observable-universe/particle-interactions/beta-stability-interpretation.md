**Derivation.**
At fixed $A$, beta decay converts $\mathfrak{n} \to \mathfrak{p}$ (or vice versa) while preserving $A$. We minimize the mass $M(p, A) = p \cdot m_{\mathfrak{p}} + (A-p) \cdot m_{\mathfrak{n}} - \mathcal{L}_{\mathrm{bind}}(p, A-p)$ by setting $\partial M / \partial p \big|_A = 0$:

$$
  (m_{\mathfrak{p}} - m_{\mathfrak{n}})
  + \frac{a_C  (2p - 1)}{A^{1/3}}
  - \frac{a_A  (A - 2p)}{A}
  = 0.
$$

Solving for $p$ (dropping the $-1$ and the small mass-difference correction):

$$
  a_A  \frac{A - 2p}{A}
  = a_C  \frac{2p}{A^{1/3}},
  \qquad
  p = \frac{A}{2 + a_C  A^{2/3} / (2a_A)}.
$$

**Verification.**
At $q = q_0$, with $a_C = (q - q^{-1}) \times 3.334 \approx 0.697$ MeV and $a_A \approx 23.29$ MeV, the formula reproduces the observed stable neutron numbers across the periodic table. The mean error is $|\Delta n| \approx 1.4$ neutrons (see [knot-periodic table](#prose:knot-periodic-table)).

**Limiting behaviour.**

| Regime | $q$ | $a_C$ | $n^*/p$ | Physics |
|--------|-----|-------|---------|---------|
| Classical | $q \to 1$ | $0$ | $1.00$ | No Coulomb; all nuclei symmetric |
| Our universe | $q = q_0$ | $0.70$ | $1.0$--$1.6$ | Valley of stability |
| Deep quantum | $q \to \infty$ | $\to \infty$ | $\to \infty$ | Coulomb overwhelms; no heavy nuclei |

The entire nuclear chart --- dictating which isotope is stable for each element --- follows from the single parameter $q$.
