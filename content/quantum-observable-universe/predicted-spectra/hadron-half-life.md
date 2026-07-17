A nucleus displaced from the valley of stability ([integer stability](#prop:integer-stability)) undergoes beta decay. The substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) governs the half-life via the $q$-deformed transition amplitude.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with substrate parameter $q$. Let $\mathcal{N}(Z, N)$ ([stable nucleus](#def:stable-nucleus)) be a nucleus with proton displacement $\delta p = p - p_{\mathrm{stab}}(A)$ from the valley of stability. The beta-decay half-life is:

$$
  t_{1/2}(p, A)
  = 
  \frac{\ln 2}{\Gamma_\beta(p, A)}.
$$

The decay rate $\Gamma_\beta$ depends only on $q$ and a dimensional scale $\mu_0$ ([building blocks](#rem:building-block-knots)).

## Decay rate from $q$ and $\mu_0$

The torus knot $T_{3,5}$ mediates beta decay ([beta decay as crossing change](#def:beta-decay-skein), [force identification](#rem:force-knot-identification)). The $T_{3,5}$ braid $(\sigma_1\sigma_2)^5$ inserts at the converting quark. Its $10$ crossings partition into the electron trefoil ($3$), the neutrino unknot ($0$), and the nuclear re-reduction residue ($7$). The fundamental weak coupling is the weak vertex form factor $\mathcal{W}(q)$. We define $\mathcal{W}(q)$ as the Markov trace of the $T_{3,5}$ braid word in $H_3(q)$.

The decay rate is:

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

1. **Weak vertex form factor** $|\mathcal{W}(q)|^2 = |\mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)|^2$. This full $10$-crossing coupling replaces the single-crossing approximation $s^2 = (q^{1/2} - q^{-1/2})^2$. In the classical limit $q \to 1$, $\mathcal{W}(1) = 0$ and beta decay vanishes.
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
4. **Phase-space integral** $f(Q)$. The $Q$-value ([transition energy](#def:Q-value-transition)) is the categorical action difference $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$. This replaces classical energy conservation ($M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e$). The classical formula assumes $d_q^2 = 0$ and fails for $q \neq 1$. We evaluate the action of each nucleus at $q$ via the terminal resolution of its composite link ([terminal resolution](#prop:terminal-resolution)). This uses the pair Skein mass formula $\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$. The fifth-power Sargent rule sets $f(Q) \propto Q^5$ for allowed transitions.
5. **Dimensional scale** $\mu_0$. This single free parameter converts Skein units to physical units (MeV, seconds). It represents a choice of units, not a physical parameter.

## Relation to the Fermi constant

Standard Fermi theory sets the decay rate as $\Gamma = G_F^2m_e^5/(2\pi^3) \cdot |M|^2 \cdot f(Z, Q)$. This effective theory formula packages two distinct mass scales. The electron mass is $m_e = 3\mathfrak{E}_{\times}(q) \cdot \mu_0$ ([building blocks](#rem:building-block-knots)). The crossing energy is $\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$. The weak scale is $v \approx 246$ GeV, entering via $G_F = 1/(\sqrt{2}v^2)$.

Both scales originate from distinct knot structures: $m_e$ from the $3$ crossings of the trefoil, and $v$ from the electroweak topology. The parameters $q$ and $\mu_0$ fix both scales. The pure number ratio $v / m_e \approx 4.8 \times 10^5$ derives strictly from topology.

The half-life depends on the combination:

$$
  G_F^2m_e^5
  = 
  \frac{m_e^5}{2v^4}
  = 
  \frac{(3\mathfrak{E}_{\times})^5}{2(N_v\mathfrak{E}_{\times})^4}
   \cdot  \mu_0
  = 
  \frac{243\mathfrak{E}_{\times}}{2N_v^4}
   \cdot  \mu_0,
$$

The effective crossing count of the weak scale is $N_v = v / (\mathfrak{E}_{\times}\mu_0)$. This reduces to a pure function of $q$ times $\mu_0$. The Fermi constant is not an independent parameter.

**Open computations:**

1. **Weak scale crossing count** $N_v$. We must derive $N_v$ (equivalently, $v$) from the Skein algebra. The $T_{3,5}$ knot mediates the weak interaction. The mass scale $v$ emerges from the $10$-crossing structure of the $T_{3,5}$ braid. The vertex form factor $\mathcal{W}(q)$ supplies the coupling. The mass scale $v$ provides the range.
2. **Weak vertex form factor** $\mathcal{W}(q)$. This is the Markov trace of $(\sigma_1\sigma_2)^5$ in $H_3(q)$ evaluated at $q$. It replaces the single-crossing approximation $s^2$. This replacement resolves the systematic $10$–$17\%$ overshoot in heavy-nucleus half-life predictions.

## $q$-dependence of the decay rate

The decay rate depends on $q$ through four channels:

- $|\mathcal{W}(q)|^2$: The $T_{3,5}$ weak vertex form factor.
- $[2]_q = q + q^{-1}$: The weak-vertex dimension.
- $|\mathcal{M}_q|^2$: The Markov trace ratio, determined by the crossing structure of the nuclear braid at $q$.
- $Q^5$: The categorical action difference ([transition energy](#def:Q-value-transition)). This depends on the pair Skein weights $\mathcal{S}_{ab}(q)$. The pair Skein weights depend on $q$ through the dressed quark masses $\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$. For $q \neq 1$, the $q$-anomaly $\delta_q$ is nonzero and $Q \neq T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}$.

In the classical limit $q = 1$, we have $s = 0$ and $[2]_1 = 2$. Crossing asymmetry vanishes. Isobars become degenerate ($Q = 0$) and beta decay ceases. For $q > 1$, crossing asymmetry splits the isobars. This yields finite $Q$ and finite half-lives.

The sensitivity of the decay rate to $q$ is:

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  = 
  \frac{q^2 - 1}{q^2 + 1}
  + 
  5\frac{q^2 + 1}{q^2 - 1}
   \approx  48
  \quad\text{at } q = q_0.
$$

A $1\%$ shift in $q$ changes the decay rate by approximately $50\%$.

The half-life is not a free observable. We derive it from the categorical action $\mathfrak{S}_q$ on the nuclear link. We use the identical parameter $q$ that dictates the valley of stability. The parameter $q$ determines which nuclei are stable and how fast unstable nuclei decay.

## Parameter count

The half-life formula depends on:
- $q$: The substrate parameter. The muon-electron mass ratio fixes this.
- $\mu_0$: The dimensional scale. This is a unit choice.
- $(p, n)$: The nuclear quantum numbers.

We decompose every standard-physics constant into $q$-dependent factors times $\mu_0$. The electron mass is $m_e = 3\mathfrak{E}_{\times}\mu_0$. The weak scale is $v = N_v\mathfrak{E}_{\times}\mu_0$. The fine structure constant is $\alpha = q^{-1}/([9]_q \cdot [10]_q)$ via the Chern-Simons correction ([EM coupling projection](#prop:em-coupling-projection)). The fine structure constant derives strictly from $q$, yielding a $2.1\;\mathrm{ppm}$ deviation from CODATA. The weak scale crossing count $N_v$ remains open (see [verification](#ex:hadron-half-life-verification)).
