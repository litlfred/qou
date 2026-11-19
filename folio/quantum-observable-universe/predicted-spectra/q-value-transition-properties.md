The $Q$-value of a nuclear transition exhibits distinct precision behaviour, a crossing-level decomposition, a $q$-anomaly, and non-conservation of $q$-momentum; in particular, the $q$-anomaly breaks classical energy conservation.

This definition is consistent with mass accuracy. If $|\Delta M/M| \approx 0.002\%$, then $Q$-values for transitions with $Q \gg \Delta M$ inherit the same precision. For transitions with small $Q$ (e.g. ${}^3\mathrm{H} \to {}^3\mathrm{He}$, $Q = 18.6$ keV), catastrophic cancellation amplifies the mass error: $\delta Q/Q \approx (M/Q) \times (\delta M/M)$.

At $k = 11$: $Q(n \to {}^1\mathrm{H}) = 0.782$ MeV ($0.00\%$), $Q({}^3\mathrm{H} \to {}^3\mathrm{He}) = 0.01823$ MeV ($-2.1\%$).

## Crossing-level decomposition

The parent normal form $\mathcal{N}(p,n)$ and daughter normal form $\mathcal{N}(p+1, n-1)$ differ at exactly $|\delta p|$ crossings. These are the quarks of the converting nucleon. At each changed crossing:

$$
  \Delta \mathfrak{E}_\times
  = 
  \mathfrak{E}_\times^{(\epsilon_{\mathrm{par}})}(q)
  - \mathfrak{E}_\times^{(\epsilon_{\mathrm{dau}})}(q).
$$

For a $\mathfrak{d} \to \mathfrak{u}$ change ($\sigma_k^{-1} \to \sigma_k$), the crossing-energy increment is $\Delta \mathfrak{E}_\times = q - q^{-1}$. The $Q$-value is:

$$
  Q
  = 
  \sum_{\text{changed crossings}} \Delta \mathfrak{E}_\times
  -  \mathfrak{S}_q(e).
$$

Because the unknot has trivial action, $\mathfrak{S}_q(\nu^{\sigma}) = 0$ drops out.

## Classical limit and the $q$-anomaly

**Warning.** Classical energy conservation is not assumed.

In classical physics, conservation of energy defines the $Q$-value:

$$
  Q_{\mathrm{classical}}
  = 
  T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}
  \stackrel{?}{=}
  M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e.
$$

This equality uses $E_{\mathrm{before}} = E_{\mathrm{after}}$. In the $q$-deformed framework, this conservation law fails because the $q$-differential does not satisfy $d_q^2 = 0$:

$$
  d_q f(x) =  \frac{f(qx) - f(x)}{(q-1)x}.
$$

$$
  d_q(f \cdot g) =  (d_q f) \cdot g +  f(qx) \cdot (d_q g).
$$

The $q$-Leibniz rule has a shift $f(qx)$ rather than $f(x)$. The $q$-differential of a product is not the sum of differentials. Squaring gives:

$$
  d_q^2  \neq  0 \quad \text{for } q \neq 1.
$$

**Corollary:** The total $q$-energy of the products need not equal the total $q$-energy of the parent. The discrepancy defines the $q$-anomaly:

$$
  \delta_q
   := 
  Q
  - 
  (T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}).
$$

This anomaly is a genuine physical effect of the $q$-deformation. It does not vanish in general.

## Structure of the $q$-anomaly

The $q$-anomaly arises from the non-commutativity of the Iwahori--Hecke algebra. The Skein crossing change converts one quark. The re-reduction to Gröbner--Shirshov normal form introduces R2 moves $T^2 = (q - q^{-1})T + 1$. Each R2 move shifts the local $q$-environment:

$$
  q_{\mathrm{eff}} \mapsto q_{\mathrm{eff}} + \Delta q,
$$

where $\Delta q \propto \hbar_q^2 = (1 - q^{-1})^2$.

The self-deformation produces a net shift:

$$
  \Delta q_{\mathrm{eff}}
  = 
  \frac{A - 1}{A^2} \cdot \hbar_q^2.
$$

This shift modifies $Q$ at second order:

$$
  Q
  = 
  \underbrace{\Delta \mathfrak{S}_q - \mathfrak{S}_q(e)}_{\text{leading (crossing change)}}
  + 
  \underbrace{\frac{\partial \mathfrak{S}_q}{\partial q} \cdot \Delta q_{\mathrm{eff}}}_{\delta_q \text{ (q-anomaly)}}.
$$

**At $q = 1$:** $\delta_q = 0$ and $Q \to Q_{\mathrm{classical}}$. Classical conservation is restored.

**At the aether parameter $q$:** $\delta_q \neq 0$. For tritium ($A = 3$), $\Delta q_{\mathrm{eff}} = 2/9 \cdot \hbar_q^2 \approx 0.0022$. This gives a correction $\delta_q / Q \sim 5\%$. This correction brings the tritium half-life prediction from 13 yr to 12.4 yr (observed 12.32 yr).

## $Q$ is not conserved

The $q$-anomaly $\delta_q$ implies that $Q$ is not the sum of kinetic energies. The $q$-deformation of the vacuum absorbs the missing energy. The effective aether parameter shifts from $q$ to $q + \Delta q_{\mathrm{eff}}$.

This is the $q$-deformed quantum anomaly. The full categorical action $\mathfrak{S}_q$ of the entire system is the conserved quantity:

$$
  \mathfrak{S}_q(\mathrm{par})
  = 
  \mathfrak{S}_{q + \Delta q}(\mathrm{dau})
  + 
  \mathfrak{S}_q(e)
  + 
  \mathfrak{S}_q(\nu^{\sigma})
  + 
  \text{kinetic terms}.
$$

Evaluating the daughter at the shifted parameter $q + \Delta q$ gives the $q$-analogue of energy conservation.

## Limits

| $q$ | Regime | $Q$ | $\delta_q$ |
|-----|--------|:---:|:---:|
| $q = 1$ | Classical | $0$ | $0$ |
| the aether $q$ | Descartes universe | $\mathcal{Q}_{\exp} + \delta_q$ | $\neq 0$ |
| $q \to \infty$ | Deep-quantum | $\to \infty$ | $\to \infty$ |

## $q$-Momentum

The $q$-momentum satisfies a similar non-conservation. Classically:

$$
  \vec{p}_{\mathrm{par}} = \vec{p}_{\mathrm{dau}} + \vec{p}_e + \vec{p}_{\nu^{\sigma}}.
$$

In the $q$-deformed case, the Iwahori--Hecke algebra non-commutativity implies:

$$
  p_q(\mathrm{par})
  = 
  p_q(\mathrm{dau}) + p_q(e) + p_q(\nu^{\sigma})
  + 
  \delta p_q,
$$

where $\delta p_q \propto \hbar_q$ is a $q$-anomaly in momentum. This is the braid-group analogue of the quantum anomaly in gauge theories.
