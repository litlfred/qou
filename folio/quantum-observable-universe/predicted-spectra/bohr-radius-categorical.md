**Proposition.** The dressed atomic transfer matrix $T^{\mathrm{dressed}} \in H_n(q)$ with eigenvalues $(q^{2k+1}, -q^{-(2k+1)})$ at electronic shell $k$ admits a candidate categorical length scale

$$
  a_{0}^{\mathrm{cat}}
  \;=\;
  \frac{\hbar}{m_{e}\,c\,\alpha_{EM}}
$$

at which a postulated kinetic Markov-trace contribution $\Phi_{1}^{\mathrm{kin}}$ and a postulated EM-coupling Coulomb contribution $\Phi_{1}^{\mathrm{Coul}}$ are equal:

$$
  \Phi_{1}^{\mathrm{kin}}(a_{0}^{\mathrm{cat}})
  \;=\;
  \Phi_{1}^{\mathrm{Coul}}(a_{0}^{\mathrm{cat}}).
$$

Evaluating this candidate uses $\alpha_{EM} = 1/(q\,[9]_q\,[10]_q)$ as the operator-selection LP weight of the EM force-carrier ([prop:em-coupling-projection](#prop:em-coupling-projection)). The dressed transfer matrix eigenvalues derive from the $B_3$ dressing of the bare $pe$ crossing. Evaluating $a_{0}^{\mathrm{cat}}$ at $q_0 \approx 1.11$ yields $5.29 \times 10^{-11}$ m.

This formulation identifies the structural layer of Bohr-virial physics. It establishes the relationship between the dressed transfer matrix eigenvalue structure and the archimedean energy scale. The absence of a per-generator additive decomposition into kinetic and Coulomb components constitutes a Hecke-algebraic gap. This obstructs immediate categorical closure.

A full categorical derivation requires defining $\Phi_{1}^{\mathrm{kin}}$ and $\Phi_{1}^{\mathrm{Coul}}$ as Hecke-algebraic objects. Five algebraic strategies exist:

1. **Symbolic crossing-type tracking.** Compute $V_i$ symbolically in $q$. Track the contributions of intra-atomic dressed versus inter-atomic bare crossings as distinct monomials.
2. **Spectral-gap matching.** Define purely Hecke-algebraic spectral gaps $\Delta_{\mathrm{kin}}(k) := \log|q^{2k+1}/q^{-(2k+1)}| = (4k+2)\log q$ and $\Delta_{\mathrm{Coul}} := \log|q/q^{-1}| = 2\log q$.
3. **Length-grading of the Hecke algebra.** Introduce an axiomatic length grading on $H_n(q)$. Assign length $\ell_b$ to bare generators $\sigma_{i,\mathrm{bare}}$ and $\ell_d \cdot (2k+1)$ to dressed generators $\sigma_{i,\mathrm{dressed},k}$.
4. **Gröbner–Shirshov spectral sequence decomposition.** Decompose the molecular Markov trace via the spectral sequence ([prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse)) and curvature-rank stratification ([conj:curvature-rank-gb-stratification](#conj:curvature-rank-gb-stratification)). The kinetic contribution appears at curvature rank 0. The Coulomb contribution appears at rank 1+.
5. **Functorial uniqueness from $q \to 1$ smoothness.** Demand the archimedean realization functor commutes smoothly with the $q \to 1$ limit. This recovers the standard Hartree formula $E_h = m_e c^2 \alpha_{EM}^2$.

The Gröbner–Shirshov spectral sequence and symbolic crossing-type tracking are the primary paths to resolving the multiplicative mixing of the transfer-matrix update.
