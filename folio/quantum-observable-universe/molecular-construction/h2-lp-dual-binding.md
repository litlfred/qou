**Proposition (conditional on [Seven-term atomic mass formula with $q$-integer coefficients](#conj:q-integer-mass-formula)).**
*The LP dual of the $H_2$ molecular braid selects the interleaved ordering $[\mathfrak{p}_1, e_2, \mathfrak{p}_2, e_1]$ as the ground state, with molecular volume:*

$$
  \Phi_1^{H_2} = \sum_{i=0}^{2} \ln\lvert \hat{V}_i^{H_2} \rvert
$$

*The **primal program** minimises the Markov trace of the molecular braid over all strand orderings and electron assignments:*

$$
  \min_{\pi \in S_4} \; \Phi_1\!\left(
    T_{\pi(0)\pi(1)} \cdot T_{\pi(1)\pi(2)} \cdot T_{\pi(2)\pi(3)}
  \right)
$$

*subject to:*
- *Each proton appears exactly once*
- *Each electron appears exactly once*
- *The shared electron is Hopf-linked to both protons (covalent constraint)*

*The **dual program** maximises the shadow price of the covalent constraint:*

$$
  \max_{y} \; y_{\mathrm{cov}}
  \quad\text{s.t.}\quad
  y_{\mathrm{cov}} \leq
  \Phi_1^{\mathrm{separated}} - \Phi_1^{H_2}(\pi)
  \;\;\forall\, \pi
$$

*where $\Phi_1^{\mathrm{separated}} = 2 \times \Phi_1^{H}$ is the $\Phi_1$ of two isolated hydrogen atoms.*

*Strong duality holds. The optimal $y_{\mathrm{cov}}^*$ equals the binding energy per shared electron. At $q_0$:*

### Numerical evaluation

*Two isolated H atoms (dressed):*

$$
  \Phi_1^{H} = \ln\lvert V^{H} \rvert
  = \ln\lvert q^5 \cdot (-(q-q^{-1})) + q^{-5} \cdot 1 \rvert
$$

*At $q_0 \approx 1.110$, $(q-q^{-1}) \approx 0.208$:*

- *$V^{H} = -q^5(q - q^{-1}) + q^{-5} \approx -1.680 \times 0.208 + 0.595 \approx 0.245$*
- *$\Phi_1^{H} = \ln(0.245) \approx -1.406$*
- *$\Phi_1^{\mathrm{sep}} = 2 \times (-1.406) = -2.812$*

*Molecular $H_2$ (interleaved ordering):*

*The three transfer matrices are $T_0 = T_{\mathfrak{p}_1 e_2}$, $T_1 = T_{e_2 \mathfrak{p}_2}^{\mathrm{dressed}}$, $T_2 = T_{\mathfrak{p}_2 e_1}$. The covalent crossings ($T_0$ and $T_2$) have eigenvalues $(q, -q^{-1})$. The dressed intra-atomic crossing ($T_1$) has eigenvalues $(q^5, -q^{-5})$.*

*The traced volumes at each generator:*

$$
  \hat{V}_0 = z \cdot a_0 + b_0, \quad
  \hat{V}_1 = z \cdot a_1 + b_1, \quad
  \hat{V}_2 = z \cdot a_2 + b_2
$$

*where $z = \mathrm{tr}_M(\mathcal{M}) / [3]_{q}!$ is the Markov-normalised trace variable.*

*The covalent channel ($\sigma_1$ mediating $e_2$--$\mathfrak{p}_2$) creates an additional attractive contribution that drives $\Phi_1^{H_2}$ below $\Phi_1^{\mathrm{sep}}$. The binding energy from the LP dual:*

$$
  y_{\mathrm{cov}}^* = \Phi_1^{\mathrm{sep}} - \Phi_1^{H_2}
  = 2\Phi_1^H - \Phi_1^{H_2} > 0
$$

*The molecule binds when the shared-electron $\Phi_1$ reduction exceeds the proton-proton repulsion penalty.*
