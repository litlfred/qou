We define acoustic horizons where the fluid velocity matches the local sound speed, $|v| = c_s$.

**Acoustic metric.**
Perturbations $\delta\psi$ of the brane fluid propagate on the [acoustic metric](#rem:madelung-fluid)

$$
  g_{\mathrm{ac}}
  = 
  \frac{\rho}{c_s}
  \begin{pmatrix}
    -(c_s^2 - |v|^2) & -v^T \\
    -v & \mathbf{1}_{3}
  \end{pmatrix}.
$$

The term $c_s^2 = \partial p / \partial\rho\big|_{Q_q}$ is the local sound speed incorporating quantum pressure effects.

**Sound speed in the brane fluid.**
The equation of state $p = p(\rho, q)$ from the [q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) determines the sound speed:

$$
  c_s^2
  = 
  c_q^2\Bigl(1 - \frac{\hbar_q^2}{4\rho}
  \Delta_q\!\left(\frac{1}{\sqrt{\rho}}\right)
  \cdot \sqrt{\rho}\Bigr).
$$

Here, $c_q = 1/(q-1)$ is the [speed of light](#def:substrate-parameter). The second term represents the quantum correction. At low density ($\rho \to 0$), quantum pressure diverges and $c_s \to \infty$. At high density, the quantum correction becomes negligible and $c_s \to c_q$.

**Horizon formation conditions.**
An acoustic horizon forms at a surface $\Sigma$ where $|v| = c_s$. Three conditions must hold simultaneously:

1. **Transonic flow.** The Mach number $\mathcal{M} = |v|/c_s$ crosses unity on $\Sigma$: $\mathcal{M}|_\Sigma = 1$. The flow is subsonic ($\mathcal{M} < 1$) on one side and supersonic ($\mathcal{M} > 1$) on the other.

2. **Non-degeneracy.** The gradient of the Mach number does not vanish on $\Sigma$: $\nabla(\mathcal{M}^2)|_\Sigma \neq 0$. This ensures the horizon is a smooth hypersurface rather than a degenerate critical point.

3. **Energy condition.** The effective energy density $T_{00} = \frac{1}{2}\rho(|v|^2 + c_s^2) + Q_q\rho$ satisfies the null energy condition $T_{\mu\nu}k^\mu k^\nu \geq 0$ for all null vectors $k^\mu$ of $g_{\mathrm{ac}}$. This holds automatically when $\rho > 0$ and $Q_q \geq 0$.

**Surface gravity and Hawking temperature.**

At an acoustic horizon, the surface gravity is

$$
  \kappa_H
  = 
  \frac{1}{2}\frac{\partial(c_s^2 - |v|^2)}{\partial n}
  \bigg|_\Sigma.
$$

The vector $n$ is the outward normal to $\Sigma$. By Unruh's acoustic analogy, the horizon radiates at the Hawking temperature

$$
  T_H
  = 
  \frac{\hbar_q\kappa_H}{2\pi c_s}.
$$

In the brane fluid, $\hbar_q = (q-1)/q$. We obtain

$$
  T_H
  = 
  \frac{(q-1)}{2\pi q}
  \frac{\kappa_H}{c_s}.
$$

As $q \to 1$, $T_H \to 0$. The classical limit admits no Hawking radiation, tracking the vanishing of $\hbar_q$. At the physical value $q \approx 1.110$, the factor $(q-1)/q \approx 0.099$ suppresses $T_H$ relative to the baseline estimate $\kappa_H / (2\pi c_s)$.

**Types of acoustic horizon in the brane fluid.**

| Configuration | Flow structure | Physical analogue |
|---|---|---|
| **Spherical inflow** | Radial $v = -v_r(r)\hat{r}$ with $v_r(r_H) = c_s$ | Schwarzschild black hole |
| **Vortex drain** | Circular $v = v_\varTheta(r)\hat\varTheta + v_r(r)\hat{r}$ | Kerr (rotating) black hole |
| **Expanding shell** | Outward $v = v_r(r)\hat{r}$ with $v_r(r_C) = c_s$ | Cosmological horizon (de Sitter) |
| **Vortex core** | Concentrated circulation $\lvert v\rvert \to \infty$ at $r \to 0$ | Naked singularity (if $\lvert v\rvert > c_s$ for all $r < r_0$) |

**$q$-dependent horizon radius.**
For a spherically symmetric inflow with velocity $v_r = -\Gamma_q / (4\pi r^2)$, the horizon forms at

$$
  r_H
  = 
  \left(\frac{\Gamma_q}{4\pi c_s}\right)^{1/2}
  = 
  \left(\frac{[j]_q[j+1]_q}{4\pi c_q}\right)^{1/2}
  \cdot (1 + O(\hbar_q)).
$$

At the fundamental level $j = 1/2$, we compute $[1/2]_q[3/2]_q = (q^2 + q^{-2} - q - q^{-1})/(q - q^{-1})^2 \approx 0.75$ at $q \approx 1.110$. The horizon radius $r_H$ is of order $\ell_q = (q-1)/q$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. We invoke real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. We evaluate generic categorical or $q$-deformation identities over an abstract coefficient ring; we specialise their archimedean realisation here.
