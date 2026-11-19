## Decay rate from $q$ and $\mu_0$

The torus knot $T_{3,5}$ mediates beta decay ([beta decay as crossing change](#def:beta-decay-skein), [force identification](#rem:force-knot-identification)). The $T_{3,5}$ braid $(\sigma_1\sigma_2)^5$ inserts at the converting quark. Its $10$ crossings partition into the electron trefoil ($3$), the neutrino unknot ($0$), and the nuclear re-reduction residue ($7$). The fundamental weak coupling is the weak vertex form factor $\mathcal{W}(q)$, the Markov trace of the $T_{3,5}$ braid word in $H_3(q)$.

The decay rate is

$$
  \Gamma_\beta(p, A)
  = 
  \frac{|\mathcal{W}(q)|^2 \cdot \mu_0}{2\pi^3}
   \cdot 
  [2]_q
   \cdot 
  |\mathcal{M}_q|^2
   \cdot 
  f(Q).
$$

The parameter $q$ fixes every factor:

1. **Weak vertex form factor** $|\mathcal{W}(q)|^2 = |\mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)|^2$. This full $10$-crossing coupling replaces the single-crossing approximation $s^2 = (q^{1/2} - q^{-1/2})^2$. Under the canonical Markov trace it has the closed form $\mathcal{W}(q) = q^2(q^{12} + q^8 - 1)/(q^2+1)^2$, with $\mathcal{W}(1) = 1/4$; the vanishing of the rate in the classical limit $q \to 1$ is carried by the $q$-prefactor of the rate, which is zero at $q = 1$, and not by the vertex factor.
2. **$q$-integer modulation** $[2]_q = q + q^{-1}$. This is the categorical dimension of the $\mathrm{SU}_q(2)$ fundamental representation. It replaces the classical weak-interaction factor of $2$.
3. **$q$-deformed matrix element** $|\mathcal{M}_q|^2$. This is the Markov trace ratio between parent and daughter Gröbner--Shirshov normal forms ([trace ratio observable](#prop:trace-ratio-observable)):

   $$
     |\mathcal{M}_q|^2
     = 
     s^2
      \cdot 
     \prod_{i=0}^{p}
     \left|
       \frac{\hat{V}_i^{\mathrm{par}}}{\hat{V}_i^{\mathrm{dau}}}
     \right|^2
   $$

   The Markov-traced generator volume is $\hat{V}_i = z \cdot a_i + b_i$ ([factorization theorem](#thm:markov-trace-factorization)).
4. **Phase-space integral** $f(Q)$. The $Q$-value ([transition energy](#def:Q-value-transition)) is the categorical action difference $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$. This replaces classical energy conservation ($M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e$). The classical formula assumes $d_q^2 = 0$ and fails for $q \neq 1$. The action of each nucleus at $q$ is evaluated via the terminal resolution of its composite link ([terminal resolution](#prop:terminal-resolution)), using the pair Skein mass formula $\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$. The fifth-power Sargent rule sets $f(Q) \propto Q^5$ for allowed transitions.
5. **Dimensional scale** $\mu_0$. This single free parameter converts Skein units to physical units (MeV, seconds). It represents a choice of units rather than a physical parameter.

The sensitivity of the decay rate to $q$ is

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  = 
  \frac{q^2 - 1}{q^2 + 1} +
  5\frac{q^2 + 1}{q^2 - 1}
   \approx  48
  \quad\text{at } q = q_0,
$$

so a $1\%$ shift in $q$ changes the decay rate by approximately $50\%$. The half-life is derived from the categorical action $\mathfrak{S}_q$ on the nuclear link, using the identical parameter $q$ that dictates the valley of stability.
