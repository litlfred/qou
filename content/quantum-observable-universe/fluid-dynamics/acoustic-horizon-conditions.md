The [acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ manifests horizons wherever the flow speed matches the local sound speed: $|v| = c_s$.

**Acoustic metric.**
Perturbations $\delta\psi$ in the brane fluid propagate along the acoustic geometry

$$
  g_{\mathrm{ac}}
  = 
  \frac{\rho}{c_s}
  \begin{pmatrix}
    -(c_s^2 - |v|^2) & -v^T \\
    -v & \mathbf{1}_{3}
  \end{pmatrix},
$$

where $c_s^2 = \partial p / \partial\rho\big|_{Q_q}$ sets the local sound speed, natively tracking the quantum pressure.

**Sound speed in the brane fluid.**
Extracting the equation of state $p = p(\rho, q)$ from the [q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) dictates the sound speed:

$$
  c_s^2
  = 
  c_q^2\Bigl(1 - \frac{\hbar_q^2}{4\rho}
  \Delta_q\!\left(\frac{1}{\sqrt{\rho}}\right)
  \cdot \sqrt{\rho}\Bigr).
$$

Here $c_q = 1/(q-1)$ identifies the substrate [speed of light](#def:substrate-parameter). The trailing term supplies the quantum correction. At low density ($\rho \to 0$), the quantum pressure diverges, sending $c_s \to \infty$. At high density, the quantum correction collapses, leaving $c_s \to c_q$.

**Horizon formation conditions.**
An acoustic horizon forms exactly on a surface $\Sigma$ satisfying $|v| = c_s$. Three structural conditions must hold simultaneously:

1. **Transonic flow.** The Mach number $\mathcal{M} = |v|/c_s$ must traverse unity exactly on $\Sigma$: $\mathcal{M}|_\Sigma = 1$, transitioning from $\mathcal{M} < 1$ (subsonic) on one side to $\mathcal{M} > 1$ (supersonic) on the other.
2. **Non-degeneracy.** The gradient of the Mach number must remain non-zero across $\Sigma$: $\nabla(\mathcal{M}^2)|_\Sigma \neq 0$. This ensures the horizon forms a smooth hypersurface rather than collapsing into a degenerate critical point.
3. **Energy condition.** The effective energy density $T_{00} = \frac{1}{2}\rho(|v|^2 + c_s^2) + Q_q\rho$ must obey the null energy condition $T_{\mu\nu}k^\mu k^\nu \geq 0$ evaluated over all null vectors $k^\mu$ mapped by $g_{\mathrm{ac}}$. The inequalities $\rho > 0$ and $Q_q \geq 0$ automatically guarantee this.

**Surface gravity and Hawking temperature.**
Evaluating the surface gravity at an acoustic horizon gives

$$
  \kappa_H
  = 
  \frac{1}{2}\frac{\partial(c_s^2 - |v|^2)}{\partial n}
  \bigg|_\Sigma,
$$

where $n$ points strictly outward from $\Sigma$. Tracking Unruh's acoustic black hole mapping, the horizon radiates at the Hawking temperature

$$
  T_H
  = 
  \frac{\hbar_q\kappa_H}{2\pic_s}.
$$

Applying the brane fluid identity $\hbar_q = (q-1)/q$ produces:

$$
  T_H
  = 
  \frac{(q-1)}{2\pi q}
  \frac{\kappa_H}{c_s}.
$$

As $q \to 1$, $T_H \to 0$: the classical limit eliminates Hawking radiation entirely, matching the collapse of $\hbar_q$. At the physical value $q \approx 1.110$, the geometric factor $(q-1)/q \approx 0.099$ heavily suppresses $T_H$ compared to the generic estimate $\kappa_H / (2\pi c_s)$.

**Types of acoustic horizon in the brane fluid.**

| Configuration | Flow structure | Physical analogue |
|---|---|---|
| **Spherical inflow** | Radial $v = -v_r(r)\hat{r}$ where $v_r(r_H) = c_s$ | Schwarzschild black hole |
| **Vortex drain** | Circular $v = v_\varTheta(r)\hat\varTheta + v_r(r)\hat{r}$ | Kerr (rotating) black hole |
| **Expanding shell** | Outward $v = v_r(r)\hat{r}$ where $v_r(r_C) = c_s$ | Cosmological horizon (de Sitter) |
| **Vortex core** | Concentrated circulation $\lvert v\rvert \to \infty$ as $r \to 0$ | Naked singularity (requires $\lvert v\rvert > c_s$ exclusively for $r < r_0$) |

**$q$-dependent horizon radius.**
Evaluated for spherically symmetric inflow operating at velocity $v_r = -\Gamma_q / (4\pi r^2)$, the horizon nucleates at

$$
  r_H
  = 
  \left(\frac{\Gamma_q}{4\pic_s}\right)^{1/2}
  = 
  \left(\frac{[j]_q[j+1]_q}{4\pic_q}\right)^{1/2}
  \cdot (1 + O(\hbar_q)).
$$

At the fundamental level $j = 1/2$, the circulation evaluates to $[1/2]_q[3/2]_q = (q^2 + q^{-2} - q - q^{-1})/(q - q^{-1})^2 \approx 0.75$ using the physical anchor $q \approx 1.110$. The resulting horizon radius $r_H$ matches the scale of $\ell_q = (q-1)/q$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
