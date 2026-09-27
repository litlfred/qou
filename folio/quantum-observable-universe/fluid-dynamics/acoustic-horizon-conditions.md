The [acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ manifests horizons wherever the flow speed matches the local sound speed: $|v| = c_s$.

*Acoustic metric.* Perturbations $\delta\psi$ in the brane fluid propagate along the acoustic geometry

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

*Sound speed in the brane fluid.* Extracting the equation of state $p = p(\rho, q)$ from the [q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) dictates the sound speed:

$$
  c_s^2
  = 
  c_q^2\Bigl(1 - \frac{\hbar_q^2}{4\rho}
  \Delta_q\!\left(\frac{1}{\sqrt{\rho}}\right)
  \cdot \sqrt{\rho}\Bigr).
$$

Here $c_q = 1/(q-1)$ identifies the substrate [speed of light](#def:substrate-parameter). The trailing term supplies the quantum correction. At low density ($\rho \to 0$), the quantum pressure diverges, sending $c_s \to \infty$. At high density, the quantum correction collapses, leaving $c_s \to c_q$.

*Horizon formation conditions.* An acoustic horizon forms exactly on a surface $\Sigma$ satisfying $|v| = c_s$. Three structural conditions must hold simultaneously:

1. **Transonic flow.** The Mach number $\mathcal{M} = |v|/c_s$ must traverse unity exactly on $\Sigma$: $\mathcal{M}|_\Sigma = 1$, transitioning from $\mathcal{M} < 1$ (subsonic) on one side to $\mathcal{M} > 1$ (supersonic) on the other.
2. **Non-degeneracy.** The gradient of the Mach number must remain non-zero across $\Sigma$: $\nabla(\mathcal{M}^2)|_\Sigma \neq 0$. This ensures the horizon forms a smooth hypersurface rather than collapsing into a degenerate critical point.
3. **Energy condition.** The effective energy density $T_{00} = \frac{1}{2}\rho(|v|^2 + c_s^2) + Q_q\rho$ must obey the null energy condition $T_{\mu\nu}k^\mu k^\nu \geq 0$ evaluated over all null vectors $k^\mu$ mapped by $g_{\mathrm{ac}}$. The inequalities $\rho > 0$ and $Q_q \geq 0$ automatically guarantee this.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
