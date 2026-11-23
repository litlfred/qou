The [color superconductivity conjecture](#conj:color-superconductivity-borromean) makes three quantitative predictions testable with astrophysical data.

**1. Equation of state: stiffening at the CFL transition.**
In the Borromean phase, the baryon mass is dominated by the hyperbolic volume $V_B = 7.32772$:

$$
  P_B(\rho)
   \sim 
  \rho^{5/3} \cdot \frac{\hbar_q^2}{V_B / \hbar_q^2}
   \propto 
  \rho^{5/3} \cdot \frac{(q-1)^4}{q^4 \cdot V_B}.
$$

In the CFL phase, $\mathrm{Vol}(\mathcal{L}_H) = 0$ and the mass arises from crossing energy alone. The equation of state becomes:

$$
  P_D(\rho)
   \sim 
  \rho^{5/3} \cdot \frac{\hbar_q^2}{(q + q^{-1})}
   \propto 
  \rho^{5/3} \cdot \frac{(q-1)^2}{q^2 \cdot (q + q^{-1})}.
$$

The ratio $P_D / P_B \sim V_B / [\hbar_q^2 \cdot (q + q^{-1})] \gg 1$. The CFL phase has a much stiffer equation of state. This produces a kink in the mass-radius relation $M(R)$ at the critical central density $\rho_c$.

**Prediction**: Neutron stars with $M \gtrsim 2M_\odot$ (those with CFL cores) possess systematically larger radii at a given mass than predicted by purely hadronic equations of state. The NICER X-ray timing mission measures $R \approx 12\text{--}13$ km for $\sim 2M_\odot$ pulsars. This is consistent with stiffening but does not discriminate the mechanism.

**2. Cooling anomaly: CFL gap suppresses neutrino emission.**
The CFL gap $\Delta_{\mathrm{CFL}} \approx 2.5$ MeV ([energy crossover](#prop:borromean-hopf-energy-crossover)) suppresses the modified Urca neutrino emission process below:

$$
  T_{\mathrm{gap}}
  = 
  \frac{\Delta_{\mathrm{CFL}}}{k_B}
   \approx 
  \frac{2.5  \mathrm{MeV}}{8.617 \times 10^{-5}  \mathrm{eV/K}}
   \approx 
  2.9 \times 10^{10}  \mathrm{K}.
$$

**Prediction**: Neutron stars with CFL cores show a cooling plateau at ages $10^2\text{--}10^4$ years. The surface temperature $T_s$ remains higher than predicted by standard cooling models. The Cassiopeia A neutron star ($\sim 330$ years old, $T_s \approx 2 \times 10^6$ K) shows rapid cooling. This constrains but does not rule out a CFL core.

**3. Gravitational wave $f$-mode splitting.**
The first-order phase transition at $\rho_c$ produces a density discontinuity at the Borromean–CFL interface. This discontinuity modifies the principal ($f$) mode oscillation frequency of the neutron star:

$$
  \delta f
   \sim 
  f_0 \cdot \frac{\Delta\rho}{\bar{\rho}}
   \sim 
  f_0 \cdot \frac{V_B / \hbar_q^2}{V_B / \hbar_q^2 + (q + q^{-1})}
   \approx 
  0.996 f_0.
$$

The density jump is nearly total (the Borromean contribution $V_B / \hbar_q^2 \approx 749$ dominates). The $f$-mode shows a split peak or broadening. This is detectable by third-generation gravitational wave observatories (Einstein Telescope, Cosmic Explorer) during neutron star mergers.

**Summary of predictions.**
| Observable | Borromean-only | With CFL core | Instrument |
|-----------|---------------|---------------|------------|
| $R$ at $2M_\odot$ | $\sim 11$ km | $\sim 13$ km | NICER |
| Cooling at $10^3$ yr | $T_s \sim 10^5$ K | $T_s \sim 10^6$ K (plateau) | Chandra |
| $f$-mode peak | Single | Split / broadened | ET / CE |
| Tidal deformability $\Lambda$ | Lower | Higher (stiffer) | LIGO O5 |
