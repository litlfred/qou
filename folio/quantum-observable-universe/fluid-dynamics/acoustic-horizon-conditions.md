The Gordon [acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ of an irrotational brane flow exhibits a kinematic scalar trapping horizon wherever the fluid speed reaches the local sound speed: $|v| = c_s$.

*Acoustic metric.* Longitudinal phase and density perturbations $\delta\psi$ in the brane fluid satisfy the scalar wave equation governed by the effective acoustic line element

$$
  g_{\mathrm{ac}}
  \;=\;
  \frac{\rho}{c_s}
  \begin{pmatrix}
    -(c_s^2 - |v|^2) & -v^T \\
    -v & \mathbf{1}_{3}
  \end{pmatrix},
$$

where $c_s^2 = \partial p / \partial\rho\big|_{Q_q}$ sets the local sound speed incorporating quantum-pressure stiffness.

*Sound speed in the brane fluid.* Extracting the barotropic equation of state $p = p(\rho, q)$ from the [$q$-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) determines the local sound speed:

$$
  c_s^2
  \;=\;
  c_q^2\Bigl(1 - \frac{\hbar_q^2}{4\rho}
  \Delta_q\!\left(\frac{1}{\sqrt{\rho}}\right)
  \cdot \sqrt{\rho}\Bigr).
$$

Here $c_q = 1/(q - 1)$ denotes the aether velocity parameter ([aether parameter](#def:substrate-parameter)). At vanishing density ($\rho \to 0$), the quantum-pressure term dominates; at high density, the dispersive correction recedes so that $c_s \to c_q$.

*Kinematic scalar horizon conditions.* A scalar acoustic horizon forms on a spatial hypersurface $\Sigma$ satisfying $|v| = c_s$ whenever three conditions hold jointly:

1. **Transonic crossing.** The local Mach number $\mathcal{M} = |v|/c_s$ crosses unity transversely on $\Sigma$: $\mathcal{M}|_\Sigma = 1$, passing from subsonic ($\mathcal{M} < 1$) on the exterior side to supersonic ($\mathcal{M} > 1$) on the interior side.
2. **Non-degenerate surface gravity.** The normal gradient $\nabla(\mathcal{M}^2)|_\Sigma \neq 0$ is non-vanishing across $\Sigma$, ensuring a smooth trapping hypersurface with well-defined acoustic surface gravity $\kappa_{\mathrm{ac}} = \tfrac{1}{2}\bigl|\partial_n(c_s^2 - |v|^2)\bigr|_\Sigma$.
3. **Effective acoustic null-energy positivity.** The hydrodynamic energy density $T_{00} = \frac{1}{2}\rho(|v|^2 + c_s^2) + Q_q\rho$ satisfies $T_{\mu\nu}k^\mu k^\nu \geq 0$ along $g_{\mathrm{ac}}$-null vectors $k^\mu$ whenever $\rho > 0$ and $Q_q \geq 0$.

**Kinematic scalar-analogue scope.** Because an irrotational Madelung flow $(v = \nabla\theta, \rho)$ is parametrized by two real scalar fields on a fixed spatial foliation, $g_{\mathrm{ac}}$ defines a **kinematic scalar horizon analogue** governing longitudinal phonon modes rather than full Einsteinian gravity, which carries two transverse-traceless spin-2 polarizations and background-independent diffeomorphism covariance.
