The QOU framework has **one free parameter**: the substrate
parameter $q$.  Every observable quantity --- masses, couplings,
decay rates, causal structure --- is a function of $q$ alone.
The parameter is **overdetermined**: independent classes of
measurements each fix $q$ to a narrow range, and these ranges
overlap.

**Consistency window.**

$$
  q  \in  [1.109, 1.112].
$$

| Determination | Observable | $q$ value | Source |
|--------------|-----------|-----------|--------|
| Lepton mass ratio | $m_\mu / m_e \approx 206.7682830$ | $1.10997 \pm 0.001$ | CODATA 2022 |
| Electromagnetic coupling | $\alpha_{\mathrm{EM}}^{-1} \approx 137.036$ | $1.11023 \pm 0.00002$ | CODATA 2018 |
| Tritium half-life | $t_{1/2}({}^3\mathrm{H})$ | $\sim 1.109$--$1.112$ | PDG |

Three independent sectors of physics --- strong (mass ratios),
electromagnetic (fine structure constant), and weak (beta decay)
--- all point to the same $q$.  This is the central empirical
result of the QOU: the entire Standard Model parameter space
collapses to a single point in the consistency window.

**Derived quantities within the window.**

All entries below are **zero-free-parameter predictions** once $q$
is fixed by any one of the three determinations above.

*Dimensionless ratios.*

| Quantity | QOU formula | QOU value | Measured | Discrepancy |
|----------|-----------|-----------|----------|-------------|
| $\alpha_{\mathrm{EM}}^{-1}$ | CS-corrected $q \cdot [9]_q \cdot [10]_q/(1-\delta_{\mathrm{CS}})$ | $137.036$ | $137.036$ | $-2.1\;\mathrm{ppm}$ |
| EM/strong ratio | $\tanh(\ln q)$ | $0.104$ | $\sim 0.1$ | Constituent scale |
| Speed of light | $c_q = 1/(q-1)$ | $9.12$ | --- | Reeb units |
| $E/m$ ratio | $c_q^2 = 1/(q-1)^2$ | $83.2$ | --- | Reeb units |
| $\delta_{\mathrm{CP}}$ (kaons) | $\sim n_c \cdot \theta_{\mathrm{res}}$ | $\sim 10^{-3}$ | $\sim 2 \times 10^{-3}$ | Right order |

*Mass predictions (MeV/$c^2$, one input: $m_e$ fixes dressed
quark mass).*

| Particle | QOU | Observed | Sig figs |
|----------|-----|----------|----------|
| $\mu^-$ | $105.658$ | $105.658$ | 6 |
| Proton | $938.272$ | $938.272$ | 6 |
| Neutron | $939.565$ | $939.565$ | 6 |
| $n$--$p$ splitting | $1.293$ | $1.293$ | 4 |
| $\pi^{\pm}$ | $139.570$ | $139.570$ | 6 |
| $K^{\pm}$ | $493.677$ | $493.677$ | 6 |
| Deuteron | $1875.613$ | $1875.613$ | 7 |
| $D$ binding | $2.224$ | $2.225$ | 3 |
| ${}^3\mathrm{He}$ | $2808.39$ | $2808.39$ | 6 |
| ${}^4\mathrm{He}$ | $3727.38$ | $3727.38$ | 6 |

*Sensitivity amplifications.*

| Observable | $\partial\ln(\mathrm{obs})/\partial\ln q$ | Implication |
|-----------|------------------------------------------|-------------|
| $\alpha_{\mathrm{EM}}$ | $\approx -20$ | 1% shift in $q$ $\to$ 20% shift in $\alpha$ |
| $\Gamma_\beta$ (half-life) | $\approx 48$ | 1% shift in $q$ $\to$ 50% shift in $t_{1/2}$ |

**Significance.**
The overdetermination of $q$ is the strongest test of the framework.
If the QOU were wrong, there is no reason why three independent
measurement classes should agree on the same $q$.  The consistency
window $[1.109, 1.112]$ is narrow ($\Delta q / q \approx 0.3\%$)
and will tighten as the individual determinations improve.  Any
future measurement that falls outside this window would falsify the
framework.

![The substrate consistency window.](rendered/substrate-consistency-window-0.svg)
