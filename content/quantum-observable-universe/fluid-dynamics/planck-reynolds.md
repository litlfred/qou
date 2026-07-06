In the brane fluid, the [substrate parameter](#def:substrate-parameter) $q$ sets all three Reynolds-number ingredients: velocity $c_q = 1/(q-1)$, length $\ell_q = (q-1)/q$, and viscosity $\nu_q = \hbar_q/2 = (q-1)/(2q)$. The **Planck--Reynolds number** is

$$
  \mathrm{Re}_q
  = \frac{c_q \cdot \ell_q}{\nu_q}
  = \frac{2}{q-1}.
$$

| Regime | $q$ | $\mathrm{Re}_q$ | Character |
|---|---|---|---|
| Classical | $\to 1^+$ | $\to \infty$ | Fully turbulent |
| Physical | $\approx 1.110$ | $\approx 18.2$ | Transitional |
| Deep quantum | $\gg 1$ | $\to 0$ | Laminar |

The substrate parameter acts as an inverse turbulence dial. At $q = 1$, the Reynolds number diverges and the full Kolmogorov cascade operates, but the contact structure degenerates and no particles exist. At $q \approx 1.110$, the fluid is transitional. It has enough turbulence for a rich [discrete vortex spectrum](#prop:discrete-vortex-spectrum), but not enough to make the spectrum continuous.

The laminar--turbulent transition occurs at $\mathrm{Re}_q \sim 1$, giving $q \sim 3$. Active Kelvin modes satisfy $[k]_q \leq \mathrm{Re}_q^{1/2}$. At $q \approx 1.110$, this bound gives $k_{\max} \approx 4$. This is consistent with four [intensity levels](#rem:vortex-intensity-modes) ($j = \frac{1}{2}, 1, \frac{3}{2}, 2$).
