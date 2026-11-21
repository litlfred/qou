## Decay rate from $q$ and $\mu_0$

The torus knot $T_{3,5}$ mediates beta decay ([beta decay as crossing change](#def:beta-decay-skein), [force identification](#rem:force-knot-identification)). The $T_{3,5}$ braid $(\sigma_1\sigma_2)^5$ inserts at the converting quark. Its $10$ crossings partition into the electron word $e^- = \sigma_0\sigma_1\sigma_0$ ($3$, a braid factor of the vertex, `QOU.BraidKnot.WeakVertexElectronFactor.weakVertex_eq_electron_mul`), the neutrino unknot ($0$), and the nuclear re-reduction residue ($7$). The fundamental weak coupling is the weak vertex form factor $\mathcal{W}_2(q)$, the two-term Lagrangian trace of the $T_{3,5}$ braid word on three strands.

The decay rate is

$$
  \Gamma_\beta(p, A)
  = 
  \frac{|\mathcal{W}_2(q)|^2 \cdot \mu_0}{2\pi^3}
   \cdot 
  [2]_q
   \cdot 
  |\mathcal{M}_q|^2
   \cdot 
  f(Q).
$$

The parameter $q$ fixes every factor:

1. **Weak vertex form factor** $\mathcal{W}_2(q) = t_1 + c_{\mathrm{em}}\,t_2$, the two-term Lagrangian trace of $X = (\sigma_1\sigma_2)^5$ on $V^{\otimes 3}$, $V = \mathrm{span}(u, d)$. With $W_m$ the weight spaces ($m = \#u - \#d$) and $\rho$ the Jimbo representation,

   $$
     t_1 = \frac{1}{[2]_q^3}\sum_m q^m\,\mathrm{Tr}_{W_m}\rho(X),
     \qquad
     t_2 = \frac{1}{[2]_q^3}\sum_m q^m\,\mathrm{Tr}_{W_m}\bigl(E(Q)^{\mathrm{conn}}\rho(X)\bigr).
   $$

   Here $Q = \sum_{i<j} Q_i Q_j$ is the all-pairs charge insertion, $E$ its expectation onto the commutant of $H_3(q)$ on $W_m$, and $E(Q)^{\mathrm{conn}}$ its part with the scalar $\mathrm{Tr}_{W_m}Q/\dim W_m$ removed.

   - **One-term part.** $t_1$ is the convention-D Markov trace, $t_1 = \mathcal{W}(q) = q^2(q^{12} + q^8 - 1)/(q^2+1)^2$, with $\mathcal{W}(1) = 1/4$. The vanishing of the rate in the classical limit $q \to 1$ is carried by the $q$-prefactor of the rate, which is zero at $q = 1$, and not by the vertex factor.
   - **Connected part.** $W_{\pm 3}$ are one-dimensional, so they contribute nothing to $t_2$. On $W_{\pm 1}$ the trivial isotypic idempotent is $P_{(3)} = v v^{\mathsf T}/(q^4+q^2+1)$ with $v = (1, q, q^2)$. For any diagonal insertion $Q$ the connected expectation is $\kappa\,(\tfrac32 P_{(3)} - \tfrac12)$, where $\kappa = \sum_b Q_b\,(d_b - \tfrac13)$ and $d = (1, q^2, q^4)/(q^4+q^2+1)$. Since $\mathrm{Tr}(P_{(3)}\rho(X)) = q^{10}$ and $\mathrm{Tr}_{W_{\pm 1}}\rho(X) = q^{10} - 1$,

     $$
       t_2 = \frac{(q\,\kappa_+ + q^{-1}\kappa_-)(2q^{10} + 1)}{2\,[2]_q^3}.
     $$

   - **When the correction vanishes.** If the three vertex strands carry one charge type, $Q$ is constant on each $W_m$, so $\kappa_\pm = 0$ and $\mathcal{W}_2 = \mathcal{W}$ for every $c_{\mathrm{em}}$. It also vanishes for every colouring under the colour-block projection, where only braids that keep quark strands with quark strands enter $E$.
   - **When it does not.** With mixed quark and lepton strands under the $H_3$ projection, $t_2 \neq 0$ and $t_2 \propto q^2 - 1$. It depends on which strand carries which charge. Write Q for a quark strand and L for a lepton strand. With quark charges $(u, d) = (\tfrac23, -\tfrac13)$ and lepton charges $(\nu, e^-) = (0, -1)$:

     | strands $(0, 1, 2)$ | $t_2$ | $2t_2/t_1$ at $q_0$ |
     |---|---|---|
     | $(\mathrm{Q}, \mathrm{Q}, \mathrm{Q})$ or $(\mathrm{L}, \mathrm{L}, \mathrm{L})$ | $0$ | $0$ |
     | $(\mathrm{L}, \mathrm{Q}, \mathrm{Q})$ | $-2q^2(q^2-1)(2q^{10}+1)/\bigl(9(q^2+1)^3\bigr)$ | $\approx -0.0643$ |
     | $(\mathrm{Q}, \mathrm{L}, \mathrm{L})$ | $+2q^2(q^2-1)(2q^{10}+1)/\bigl(9(q^2+1)^3\bigr)$ | $\approx +0.0643$ |
     | $(\mathrm{Q}, \mathrm{Q}, \mathrm{L})$ | $\dfrac{q^2(q^2-1)(2q^{10}+1)(q^4+4q^2+1)}{9(q^2+1)^3(q^4+q^2+1)}$ | $\approx +0.0638$ |
     | $(\mathrm{L}, \mathrm{L}, \mathrm{Q})$ | the negative of $(\mathrm{Q}, \mathrm{Q}, \mathrm{L})$ | $\approx -0.0638$ |
     | $(\mathrm{Q}, \mathrm{L}, \mathrm{Q})$ | $\dfrac{q^2(q^2-1)^3(2q^{10}+1)}{9(q^2+1)^3(q^4+q^2+1)}$ | $\approx +0.0005$ |
     | $(\mathrm{L}, \mathrm{Q}, \mathrm{L})$ | the negative of $(\mathrm{Q}, \mathrm{L}, \mathrm{Q})$ | $\approx -0.0005$ |

     The last column is $\partial \ln |\mathcal{W}_2|^2/\partial c_{\mathrm{em}}$ at $c_{\mathrm{em}} = 0$, the change in $\ln \Gamma_\beta$ per unit $c_{\mathrm{em}}$.

   The rate therefore depends on three inputs that are not derived here: the coefficient $c_{\mathrm{em}}$, the charges on the three vertex strands, and the projection that defines $E$ once lepton strands are present. No value of any of them is chosen. This full $10$-crossing coupling replaces the single-crossing approximation $s^2 = (q^{1/2} - q^{-1/2})^2$.
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
4. **Phase-space integral** $f(Q)$. The $Q$-value ([transition energy](#def:Q-value-transition)) is the categorical action difference $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$. This replaces classical energy conservation ($M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e$). The classical formula assumes $d_q^2 = 0$ and fails for $q \neq 1$. Evaluate the action of each nucleus at $q$ via the terminal resolution of its composite link ([terminal resolution](#prop:terminal-resolution)). This uses the pair Skein mass formula $\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$. The fifth-power Sargent rule sets $f(Q) \propto Q^5$ for allowed transitions.
5. **Dimensional scale** $\mu_0$. This single free parameter converts Skein units to physical units (MeV, seconds). It represents a choice of units, not a physical parameter.

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
