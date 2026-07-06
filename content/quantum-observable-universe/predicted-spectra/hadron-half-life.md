A nucleus displaced from the valley of stability ([integer stability](#prop:integer-stability)) beta decays toward stability. The half-life — the time for half a population to decay — is governed by the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) via the $q$-deformed transition amplitude.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with substrate parameter $q$. A nucleus $\mathcal{N}(Z, N)$ ([stable nucleus](#def:stable-nucleus)) with proton displacement $\delta p = p - p_{\mathrm{stab}}(A)$ from the valley of stability has beta-decay half-life:

$$
  t_{1/2}(p, A)
  = 
  \frac{\ln 2}{\Gamma_\beta(p, A)}.
$$

The decay rate $\Gamma_\beta$ depends only on $q$ and a single dimensional scale $\mu_0$ ([building blocks](#rem:building-block-knots)).

## Decay rate from $q$ and $\mu_0$

Beta decay is mediated by the torus knot $T_{3,5}$, which has $10$ crossings ([beta decay as crossing change](#def:beta-decay-skein), [force identification](#rem:force-knot-identification)). The $T_{3,5}$ braid $(\sigma_1\sigma_2)^5$ is inserted at the converting quark. Its $10$ crossings partition into the electron trefoil ($3$), the neutrino unknot ($0$), and the nuclear re-reduction residue ($7$). The fundamental weak coupling is the weak vertex form factor $\mathcal{W}(q)$, defined as the Markov trace of the $T_{3,5}$ braid word in $H_3(q)$.

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

Every factor here is fixed by $q$:

1. **Weak vertex form factor** $|\mathcal{W}(q)|^2 = |\mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)|^2$: This is the full $10$-crossing weak vertex coupling, replacing the single-crossing approximation $s^2 = (q^{1/2} - q^{-1/2})^2$. In the classical limit $q \to 1$, $\mathcal{W}(1) = 0$ and beta decay vanishes.
2. **$q$-integer modulation** $[2]_q = q + q^{-1}$: The categorical dimension of the $\mathrm{SU}_q(2)$ fundamental representation. It replaces the classical weak-interaction factor of $2$.
3. **$q$-deformed matrix element:** The squared matrix element is the Markov trace ratio between parent and daughter Gröbner--Shirshov normal forms ([trace ratio observable](#prop:trace-ratio-observable)):

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

   where $\hat{V}_i = z \cdot a_i + b_i$ is the Markov-traced generator volume ([factorization theorem](#thm:markov-trace-factorization)).
4. **Phase-space integral:** The $Q$-value ([transition energy](#def:Q-value-transition)) is the categorical action difference $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$. This replaces classical energy conservation ($M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e$), which assumes $d_q^2 = 0$ and fails for $q \neq 1$. Each nucleus's action evaluates at $q$ via the terminal resolution of its composite link ([terminal resolution](#prop:terminal-resolution)), using the pair Skein mass formula $\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$. The fifth-power Sargent rule sets $f(Q) \propto Q^5$ for allowed transitions.
5. **Dimensional scale** $\mu_0$: The single free parameter converting Skein units to physical units (MeV, seconds). It represents a choice of units, not a physical parameter.

## Relation to the Fermi constant

Standard Fermi theory sets the decay rate as $\Gamma = G_F^2m_e^5/(2\pi^3) \cdot |M|^2 \cdot f(Z, Q)$. This effective theory formula packages two distinct mass scales:

- The electron mass $m_e = 3\mathfrak{E}_{\times}(q) \cdot \mu_0$ ([building blocks](#rem:building-block-knots)), where $\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$ is the crossing energy.
- The weak scale $v \approx 246$ GeV, via $G_F = 1/(\sqrt{2}v^2)$.

Both scales are fixed by $q$ and $\mu_0$, yet originate from distinct knot structures: $m_e$ from the trefoil's 3 crossings, and $v$ from the electroweak topology. The pure number ratio $v / m_e \approx 4.8 \times 10^5$ is determined strictly by topology.

The combination entering the half-life is:

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

where $N_v = v / (\mathfrak{E}_{\times}\mu_0)$ is the effective crossing count of the weak scale. This reduces to a pure function of $q$ times $\mu_0$. The Fermi constant is not an independent parameter.

**Open computations:**

1. **$N_v$ (weak scale crossing count):** We must derive $N_v$ (equivalently, $v$) from the Skein algebra. Since $T_{3,5}$ mediates the weak interaction, $v$ emerges from the $10$-crossing structure of the $T_{3,5}$ braid. The vertex form factor $\mathcal{W}(q)$ supplies the coupling; the mass scale $v$ provides the range.
2. **$\mathcal{W}(q)$ (weak vertex form factor):** This is the Markov trace of $(\sigma_1\sigma_2)^5$ in $H_3(q)$ evaluated at $q$. It replaces the single-crossing approximation $s^2$ and is expected to resolve the systematic $10$–$17\%$ overshoot in heavy-nucleus half-life predictions.

## $q$-dependence of the decay rate

The decay rate depends on $q$ through four channels:

- $|\mathcal{W}(q)|^2$: The $T_{3,5}$ weak vertex form factor.
- $[2]_q = q + q^{-1}$: The weak-vertex dimension.
- $|\mathcal{M}_q|^2$: The Markov trace ratio, reflecting the nuclear braid's crossing structure at $q$.
- $Q^5$: The categorical action difference ([transition energy](#def:Q-value-transition)). This depends on the pair Skein weights $\mathcal{S}_{ab}(q)$, which in turn depend on $q$ through the dressed quark masses $\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$. Note that $Q \neq T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}$ for $q \neq 1$ (the $q$-anomaly $\delta_q \neq 0$).

In the classical limit $q = 1$, we have $s = 0$ and $[2]_1 = 2$. Crossing asymmetry vanishes, isobars become degenerate ($Q = 0$), and beta decay ceases. For $q > 1$, crossing asymmetry splits the isobars, yielding finite $Q$ and half-lives.

The decay rate's sensitivity to $q$ is:

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  = 
  \frac{q^2 - 1}{q^2 + 1}
  + 
  5\frac{q^2 + 1}{q^2 - 1}
   \approx  48
  \quad\text{at } q = q_0.
$$

A $1\%$ shift in $q$ changes decay rates by $\sim 50\%$.

The half-life is not a free observable. It derives from the categorical action $\mathfrak{S}_q$ on the nuclear link using the identical parameter $q$ that dictates the valley of stability. The parameter $q$ determines both which nuclei are stable and how fast unstable nuclei decay.

## Parameter count

The half-life formula depends on:
- $q$: The substrate parameter (fixed by the muon-electron mass ratio).
- $\mu_0$: The dimensional scale (unit choice).
- $(p, n)$: The nuclear quantum numbers.

Every standard-physics constant decomposes into $q$-dependent factors times $\mu_0$: the electron mass $m_e = 3\mathfrak{E}_{\times}\mu_0$, the weak scale $v = N_v\mathfrak{E}_{\times}\mu_0$, and the fine structure constant $\alpha = q^{-1}/([9]_q \cdot [10]_q)$ via the Chern-Simons correction ([EM coupling projection](#prop:em-coupling-projection)). The fine structure constant strictly derives from $q$ ($2.1\;\mathrm{ppm}$ deviation from CODATA). The weak scale crossing count $N_v$ remains open (see [verification](#ex:hadron-half-life-verification)).
