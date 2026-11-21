## Relation to the Fermi constant

Standard Fermi theory sets the decay rate as $\Gamma = G_F^2m_e^5/(2\pi^3) \cdot |M|^2 \cdot f(Z, Q)$. This effective theory formula packages two distinct mass scales. The crossing energy is $\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$. The weak scale is $v \approx 246$ GeV, entering via $G_F = 1/(\sqrt{2}v^2)$.

In the backup model $m_e$ was read off the $3$ crossings of the trefoil and $v$ off the electroweak topology. In the corpus $m_e$ is the CAL-1 leptonic mass-scale input, not derived from a knot ([electron](#def:electron-knot)), so the ratio $v / m_e \approx 4.8 \times 10^5$ is not derived here.

The half-life depends on the combination

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

with effective weak-scale crossing count $N_v = v / (\mathfrak{E}_{\times}\mu_0)$. This reduces to a pure function of $q$ times $\mu_0$: the Fermi constant is not an independent parameter.

## $q$-dependence of the decay rate

The decay rate depends on $q$ through four channels:

- $|\mathcal{W}(q)|^2$: The $T_{3,5}$ weak vertex form factor.
- $[2]_q = q + q^{-1}$: The weak-vertex dimension.
- $|\mathcal{M}_q|^2$: The Markov trace ratio. This reflects the crossing structure of the nuclear braid at $q$.
- $Q^5$: The categorical action difference ([transition energy](#def:Q-value-transition)). This depends on the pair Skein weights $\mathcal{S}_{ab}(q)$, which depend on $q$ through the dressed quark masses $\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$. For $q \neq 1$, the $q$-anomaly $\delta_q$ is nonzero and $Q \neq T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}$.

In the classical limit $q = 1$, $s = 0$ and $[2]_1 = 2$; crossing asymmetry vanishes, isobars become degenerate ($Q = 0$) and beta decay ceases. For $q > 1$, crossing asymmetry splits the isobars, yielding finite $Q$ and finite half-lives.

## Parameter count

The half-life formula depends on $q$ (the substrate parameter, fixed by the muon-electron mass ratio), $\mu_0$ (a unit choice), and the nuclear quantum numbers $(p, n)$. Every standard-physics constant decomposes into $q$-dependent factors times $\mu_0$: the electron mass is $m_e = 3\mathfrak{E}_{\times}\mu_0$, the weak scale is $v = N_v\mathfrak{E}_{\times}\mu_0$, and the fine structure constant is $\alpha = q^{-1}/([9]_q \cdot [10]_q)$ ([EM coupling projection](#prop:em-coupling-projection)), which is the **bare** form and sits $-0.155\%$ from CODATA. The Chern-Simons correction is a separate and conjectural addition, stated in [the Chern-Simons block](#rem:em-coupling-chern-simons) rather than in the projection proposition, and its Gram constant $\kappa$ is unproved; with the derived $\kappa$ at the proton pin it leaves $-468\;\mathrm{ppb}$.

## Open computations

1. **Weak scale crossing count** $N_v$. This must be derived (equivalently, $v$) from the Skein algebra. The $T_{3,5}$ knot mediates the weak interaction, with the mass scale $v$ emerging from the $10$-crossing structure of the $T_{3,5}$ braid: the vertex form factor $\mathcal{W}(q)$ supplies the coupling and $v$ provides the range.
2. **Weak vertex form factor** $\mathcal{W}(q)$, the Markov trace of $(\sigma_1\sigma_2)^5$ in $H_3(q)$. What remains open is its use: the half-life tables still carry the single-crossing approximation $s^2$, and whether replacing $s^2$ by $|\mathcal{W}(q)|^2$ resolves the systematic $10$–$17\%$ overshoot in heavy-nucleus half-life predictions has not been computed.
