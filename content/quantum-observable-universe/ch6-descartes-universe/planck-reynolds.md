The Reynolds number $\mathrm{Re} = UL/\nu$ governs the transition
from laminar to turbulent flow in classical hydrodynamics.  In the
brane fluid, all three ingredients — velocity scale $U$, length
scale $L$, and kinematic viscosity $\nu$ — are determined by the
[substrate parameter](#def:substrate-parameter) $q$.

**Brane-fluid velocity and length scales.**
The characteristic velocity is the [speed of light](#def:speed-of-light)
$c_q = 1/(q-1)$, which diverges as $q \to 1$ (classical limit) and
decreases as the brane thickens.  The characteristic length is the
[Planck length](#def:planck-length) $\ell_q = (q-1)/q$, which
vanishes classically and grows with $q$.  The kinematic viscosity
arises from the quantum pressure: dimensional analysis of the
[quantum Euler equation](#rem:madelung-fluid) gives

$$
  \nu_q \;=\; \frac{\hbar_q}{2}
  \;=\; \frac{q-1}{2q},
$$

where $\hbar_q = (q-1)/q$ is the
[$q$-deformed Planck constant](#def:quantum-planck-constant).
The factor $\frac{1}{2}$ reflects the quantum pressure's role as
a diffusive term for $\sqrt{\rho}$ rather than for $v$ itself.

**The Planck--Reynolds number.**
Combining these scales defines the **Planck--Reynolds number** of
the brane fluid:

$$
  \mathrm{Re}_q
  \;\equiv\;
  \frac{c_q \cdot \ell_q}{\nu_q}
  \;=\;
  \frac{\dfrac{1}{q-1} \cdot \dfrac{q-1}{q}}{\dfrac{q-1}{2q}}
  \;=\;
  \frac{2}{q-1}.
$$

This is a monotonically decreasing function of $q$:

| Regime | $q$ range | $\mathrm{Re}_q$ | Flow character |
|---|---|---|---|
| Classical limit | $q \to 1^+$ | $\to \infty$ | Fully turbulent (Kolmogorov cascade) |
| Physical substrate | $q \approx 1.110$ | $\approx 18.2$ | Transitional (discrete vortex modes) |
| Deep quantum | $q \gg 1$ | $\to 0$ | Laminar (single-mode, no cascade) |

**Interpretation.**
The substrate parameter $q$ is the **inverse turbulence dial** of
the brane fluid.  At $q = 1$, the infinite Reynolds number permits
the full Kolmogorov cascade of eddies at all scales — but this is
also the degenerate limit where the contact structure collapses and
no particles exist.  As $q$ increases past $1$, the Reynolds number
drops and the fluid admits only finitely many active vortex modes.
At the physical value $q \approx 1.110$, the Planck--Reynolds number
$\mathrm{Re}_q \approx 18.2$ sits in the **transitional regime**:
enough turbulence to support a rich spectrum of
[discrete vortex modes](#prop:discrete-vortex-spectrum), but not so
much that the spectrum becomes continuous.

**Critical separation.**
The laminar--turbulent transition occurs at $\mathrm{Re}_q \sim 1$,
i.e. $q \sim 3$.  For $q > 3$, the brane fluid is laminar and
supports at most a single vortex mode — too few degrees of freedom
for particle physics.  The physical constraint $q \approx 1.110$
places the universe deep in the transitional regime, consistent with
the observed richness of the particle spectrum.

**Connection to the discrete spectrum.**
The number of active Kelvin modes on a vortex filament of length
$L$ is bounded above by $\mathrm{Re}_q$: modes with $q$-integer
index $[k]_q > \mathrm{Re}_q^{1/2}$ are viscously damped by the
quantum pressure.  At $q \approx 1.110$, this gives approximately
$k_{\max} \approx 4$ active modes, consistent with the four
generations of the [vortex intensity
levels](#rem:vortex-intensity-modes) ($j = \frac{1}{2}, 1,
\frac{3}{2}, 2$) before damping suppresses higher states.
