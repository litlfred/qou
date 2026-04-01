The stable neutron number $n^*(p)$ for each element is determined
by extremizing the Skein binding Lagrangian
([Skein binding Lagrangian](#def:skein-binding-lagrangian)) over $n$
at fixed $p$.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$.  For a multi-nucleon Hopf link
$L = Z\,\mathfrak{p} \bowtie N\,\mathfrak{n}$ with $A = Z + N$,
the beta-stable configuration satisfies
$\partial \mathcal{L}_{\mathrm{bind}} / \partial n = 0$, which
gives the beta-stability line

$$
  p^*(A)
  \;=\;
  \frac{A}{2 + a_C \, A^{2/3} / (2\,a_A)}
$$

where $a_C = (q - q^{-1}) \cdot \lambda_C$ is the Coulomb
coefficient from the crossing asymmetry and $a_A$ is the Pauli
asymmetry coefficient.

Equivalently, for given $p$, the stable mass number is the
fixed point of

$$
  A^*(p) = p \left(2 + \frac{a_C}{2\,a_A}\, {A^*}^{2/3}\right)
$$

and $n^*(p) = A^*(p) - p$.

**Derivation.**
At fixed $A$, beta decay converts
$\mathfrak{n} \to \mathfrak{p}$ (or vice versa) while preserving
$A$.  The mass $M(p, A) = p \cdot m_{\mathfrak{p}} + (A-p) \cdot
m_{\mathfrak{n}} - \mathcal{L}_{\mathrm{bind}}(p, A-p)$ is minimized
when $\partial M / \partial p \big|_A = 0$:

$$
  (m_{\mathfrak{p}} - m_{\mathfrak{n}})
  + \frac{a_C \, (2p - 1)}{A^{1/3}}
  - \frac{a_A \, (A - 2p)}{A}
  = 0.
$$

Solving for $p$ (dropping the $-1$ and mass-difference correction,
which are small):

$$
  a_A \, \frac{A - 2p}{A}
  = a_C \, \frac{2p}{A^{1/3}},
  \qquad
  p = \frac{A}{2 + a_C \, A^{2/3} / (2\,a_A)}.
$$

**Verification.**
At $q = q_0$ with $a_C = (q - q^{-1}) \times 3.334 \approx
0.697$ MeV and $a_A \approx 23.29$ MeV, the formula reproduces
observed stable neutron numbers across the periodic table with
mean error $|\Delta n| \approx 1.4$ neutrons (see
[knot-periodic table](#app:knot-periodic-table)).

**Limiting behaviour.**

| Regime | $q$ | $a_C$ | $n^*/p$ | Physics |
|--------|-----|-------|---------|---------|
| Classical | $q \to 1$ | $0$ | $1.00$ | No Coulomb; all nuclei symmetric |
| Our universe | $q = q_0$ | $0.70$ | $1.0$--$1.6$ | Valley of stability |
| Deep quantum | $q \to \infty$ | $\to \infty$ | $\to \infty$ | Coulomb overwhelms; no heavy nuclei |

The entire nuclear chart — which isotope is stable for each
element — is a consequence of the single parameter $q$.
