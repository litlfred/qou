The [acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ admits
horizons wherever $|v| = c_s$.

**Acoustic metric.**
Perturbations $\delta\psi$ of the brane fluid propagate on the
acoustic geometry

$$
  g_{\mathrm{ac}}
  = 
  \frac{\rho}{c_s}
  \begin{pmatrix}
    -(c_s^2 - |v|^2) & -v^T \\
    -v & \mathbf{1}_{3}
  \end{pmatrix},
$$

where $c_s^2 = \partial p / \partial\rho\big|_{Q_q}$ is the local
sound speed incorporating quantum pressure effects.

**Sound speed in the brane fluid.**
From the equation of state $p = p(\rho, q)$ determined by the
[q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction),
the sound speed is

$$
  c_s^2
  = 
  c_q^2\Bigl(1 - \frac{\hbar_q^2}{4\rho}
  \Delta_q\!\left(\frac{1}{\sqrt{\rho}}\right)
  \cdot \sqrt{\rho}\Bigr),
$$

where $c_q = 1/(q-1)$ is the
[speed of light](#def:substrate-parameter).  The second term is the
quantum correction: at low density ($\rho \to 0$), the quantum
pressure diverges and $c_s \to \infty$; at high density, the
quantum correction is negligible and $c_s \to c_q$.

**Horizon formation conditions.**
An acoustic horizon forms at a surface $\Sigma$ where
$|v| = c_s$.  Three conditions must hold simultaneously:

1. **Transonic flow.**  The Mach number
   $\mathcal{M} = |v|/c_s$ crosses unity on $\Sigma$:
   $\mathcal{M}|_\Sigma = 1$, with $\mathcal{M} < 1$ on one
   side (subsonic) and $\mathcal{M} > 1$ on the other
   (supersonic).

2. **Non-degeneracy.**  The gradient of the Mach number is
   non-vanishing on $\Sigma$:
   $\nabla(\mathcal{M}^2)|_\Sigma \neq 0$.  This ensures the
   horizon is a smooth hypersurface, not a degenerate critical
   point.

3. **Energy condition.**  The effective energy density
   $T_{00} = \frac{1}{2}\rho(|v|^2 + c_s^2) + Q_q\rho$
   satisfies the null energy condition
   $T_{\mu\nu}k^\mu k^\nu \geq 0$ for all null vectors $k^\mu$
   of $g_{\mathrm{ac}}$.  This is automatically satisfied when
   $\rho > 0$ and $Q_q \geq 0$.

**Surface gravity and Hawking temperature.**

At an acoustic horizon, the surface gravity is

$$
  \kappa_H
  = 
  \frac{1}{2}\frac{\partial(c_s^2 - |v|^2)}{\partial n}
  \bigg|_\Sigma,
$$

where $n$ is the outward normal to $\Sigma$.  By analogy with
Unruh's result for acoustic black holes, the horizon radiates at
the Hawking temperature

$$
  T_H
  = 
  \frac{\hbar_q\kappa_H}{2\pic_s}.
$$

In the brane fluid, $\hbar_q = (q-1)/q$, so:

$$
  T_H
  = 
  \frac{(q-1)}{2\pi q}
  \frac{\kappa_H}{c_s}.
$$

As $q \to 1$, $T_H \to 0$: the classical limit has no Hawking
radiation, consistent with the vanishing of $\hbar_q$.  At the
physical value $q \approx 1.110$, $T_H$ is suppressed by a factor
$(q-1)/q \approx 0.099$ relative to the naive estimate
$\kappa_H / (2\pi c_s)$.

**Types of acoustic horizon in the brane fluid.**

| Configuration | Flow structure | Physical analogue |
|---|---|---|
| **Spherical inflow** | Radial $v = -v_r(r)\hat{r}$ with $v_r(r_H) = c_s$ | Schwarzschild black hole |
| **Vortex drain** | Circular $v = v_\varTheta(r)\hat\varTheta + v_r(r)\hat{r}$ | Kerr (rotating) black hole |
| **Expanding shell** | Outward $v = v_r(r)\hat{r}$ with $v_r(r_C) = c_s$ | Cosmological horizon (de Sitter) |
| **Vortex core** | Concentrated circulation $\lvert v\rvert \to \infty$ at $r \to 0$ | Naked singularity (if $\lvert v\rvert > c_s$ for all $r < r_0$) |

**$q$-dependent horizon radius.**
For a spherically symmetric inflow with velocity
$v_r = -\Gamma_q / (4\pi r^2)$, the horizon forms at

$$
  r_H
  = 
  \left(\frac{\Gamma_q}{4\pic_s}\right)^{1/2}
  = 
  \left(\frac{[j]_q[j+1]_q}{4\pic_q}\right)^{1/2}
  \cdot (1 + O(\hbar_q)).
$$

At the fundamental level $j = 1/2$:
$[1/2]_q[3/2]_q = (q^2 + q^{-2} - q - q^{-1})/(q - q^{-1})^2
\approx 0.75$ at $q \approx 1.110$.  The horizon radius $r_H$
is of order $\ell_q = (q-1)/q$.

**Connection to gravitational emergence.**
The [GR substrate geometry](#rem:gr-substrate-geometry) identifies
the acoustic metric with the physical spacetime metric in the
archimedean realisation.  Acoustic horizons are therefore
**gravitational horizons**: black holes are regions where the
brane fluid flows supersonically.  The Einstein field equations
emerge as the long-wavelength limit of the
[q-Navier--Stokes equation](#def:q-navier-stokes), with the
stress-energy tensor $T_{\mu\nu}$ encoding the fluid momentum
flux.  Singularity theorems (Penrose--Hawking) translate into
statements about the breakdown of smooth transonic flow — the
classical singularity is the $q \to 1$ limit of a smooth
$q$-deformed vortex core.
